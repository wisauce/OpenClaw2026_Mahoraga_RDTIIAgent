#!/usr/bin/env python3
"""SQLite-backed RDTII legal knowledge graph.

This is intentionally dependency-free and safe for demo/reviewer use:
- Uses local SQLite only; no network calls and no secrets.
- Creates parameterized tables for nodes, edges, source query logs, and evidence.
- Stores graph semantics as typed nodes/edges suitable for RDTII audit trails.

Example:
  python scripts/rdtii_kg.py --db outputs/rdtii_kg_demo.sqlite init
  python scripts/rdtii_kg.py --db outputs/rdtii_kg_demo.sqlite load-sample
  python scripts/rdtii_kg.py --db outputs/rdtii_kg_demo.sqlite context --indicator P6_I1
"""
from __future__ import annotations

import argparse
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

SCHEMA_VERSION = "1.0.0"

NODE_TYPES = {
    "economy",
    "document",
    "provision",
    "definition",
    "regulatory_measure",
    "rdtii_pillar",
    "rdtii_indicator",
    "evidence_record",
    "database_record",
    "reviewer_assessment",
}

EDGE_TYPES = {
    "contains",
    "defines",
    "references",
    "amends_or_repeals",
    "has_exception",
    "creates_obligation",
    "supports_measure",
    "maps_to_indicator",
    "supports_score",
    "database_supports_measure",
    "requires_human_review",
}

SCHEMA_SQL = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS graph_metadata (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS nodes (
  node_id TEXT PRIMARY KEY,
  node_type TEXT NOT NULL,
  label TEXT NOT NULL,
  economy TEXT,
  assessment_year INTEGER,
  source_type TEXT,
  citation TEXT,
  url TEXT,
  text TEXT,
  status TEXT,
  metadata_json TEXT NOT NULL DEFAULT '{}',
  created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS edges (
  edge_id TEXT PRIMARY KEY,
  source_node_id TEXT NOT NULL,
  target_node_id TEXT NOT NULL,
  edge_type TEXT NOT NULL,
  confidence TEXT NOT NULL DEFAULT 'medium',
  rationale TEXT,
  metadata_json TEXT NOT NULL DEFAULT '{}',
  created_at TEXT NOT NULL,
  FOREIGN KEY(source_node_id) REFERENCES nodes(node_id) ON DELETE CASCADE,
  FOREIGN KEY(target_node_id) REFERENCES nodes(node_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS source_queries (
  query_id TEXT PRIMARY KEY,
  economy TEXT NOT NULL,
  assessment_year INTEGER NOT NULL,
  source_name TEXT NOT NULL,
  query TEXT NOT NULL,
  url TEXT,
  attempted_at TEXT NOT NULL,
  status TEXT NOT NULL,
  result_summary TEXT,
  error_type TEXT,
  metadata_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS indicator_scores (
  score_id TEXT PRIMARY KEY,
  indicator_node_id TEXT NOT NULL,
  ai_suggested_score REAL,
  reviewer_score REAL,
  final_score REAL,
  score_status TEXT NOT NULL,
  rationale TEXT,
  uncertainty TEXT NOT NULL DEFAULT 'medium',
  created_at TEXT NOT NULL,
  FOREIGN KEY(indicator_node_id) REFERENCES nodes(node_id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_nodes_type ON nodes(node_type);
CREATE INDEX IF NOT EXISTS idx_nodes_economy_year ON nodes(economy, assessment_year);
CREATE INDEX IF NOT EXISTS idx_edges_source ON edges(source_node_id, edge_type);
CREATE INDEX IF NOT EXISTS idx_edges_target ON edges(target_node_id, edge_type);
CREATE INDEX IF NOT EXISTS idx_queries_economy_year ON source_queries(economy, assessment_year);
"""


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def connect(db_path: str) -> sqlite3.Connection:
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA_SQL)
    conn.execute(
        "INSERT OR REPLACE INTO graph_metadata(key, value) VALUES (?, ?)",
        ("schema_version", SCHEMA_VERSION),
    )
    conn.execute(
        "INSERT OR REPLACE INTO graph_metadata(key, value) VALUES (?, ?)",
        ("created_or_updated_at", now()),
    )
    conn.commit()


def json_dumps(value: dict[str, Any] | None) -> str:
    return json.dumps(value or {}, ensure_ascii=False, sort_keys=True)


def upsert_node(conn: sqlite3.Connection, node: dict[str, Any]) -> None:
    node_type = node["node_type"]
    if node_type not in NODE_TYPES:
        raise ValueError(f"Unsupported node_type: {node_type}")
    conn.execute(
        """
        INSERT INTO nodes(node_id, node_type, label, economy, assessment_year,
                          source_type, citation, url, text, status, metadata_json, created_at)
        VALUES(:node_id, :node_type, :label, :economy, :assessment_year,
               :source_type, :citation, :url, :text, :status, :metadata_json, :created_at)
        ON CONFLICT(node_id) DO UPDATE SET
          node_type=excluded.node_type,
          label=excluded.label,
          economy=excluded.economy,
          assessment_year=excluded.assessment_year,
          source_type=excluded.source_type,
          citation=excluded.citation,
          url=excluded.url,
          text=excluded.text,
          status=excluded.status,
          metadata_json=excluded.metadata_json
        """,
        {
            "node_id": node["node_id"],
            "node_type": node_type,
            "label": node["label"],
            "economy": node.get("economy"),
            "assessment_year": node.get("assessment_year"),
            "source_type": node.get("source_type"),
            "citation": node.get("citation"),
            "url": node.get("url"),
            "text": node.get("text"),
            "status": node.get("status"),
            "metadata_json": json_dumps(node.get("metadata")),
            "created_at": node.get("created_at", now()),
        },
    )


def upsert_edge(conn: sqlite3.Connection, edge: dict[str, Any]) -> None:
    edge_type = edge["edge_type"]
    if edge_type not in EDGE_TYPES:
        raise ValueError(f"Unsupported edge_type: {edge_type}")
    conn.execute(
        """
        INSERT INTO edges(edge_id, source_node_id, target_node_id, edge_type,
                          confidence, rationale, metadata_json, created_at)
        VALUES(:edge_id, :source_node_id, :target_node_id, :edge_type,
               :confidence, :rationale, :metadata_json, :created_at)
        ON CONFLICT(edge_id) DO UPDATE SET
          source_node_id=excluded.source_node_id,
          target_node_id=excluded.target_node_id,
          edge_type=excluded.edge_type,
          confidence=excluded.confidence,
          rationale=excluded.rationale,
          metadata_json=excluded.metadata_json
        """,
        {
            "edge_id": edge["edge_id"],
            "source_node_id": edge["source_node_id"],
            "target_node_id": edge["target_node_id"],
            "edge_type": edge_type,
            "confidence": edge.get("confidence", "medium"),
            "rationale": edge.get("rationale"),
            "metadata_json": json_dumps(edge.get("metadata")),
            "created_at": edge.get("created_at", now()),
        },
    )


def insert_source_query(conn: sqlite3.Connection, query: dict[str, Any]) -> None:
    conn.execute(
        """
        INSERT OR REPLACE INTO source_queries(query_id, economy, assessment_year, source_name,
          query, url, attempted_at, status, result_summary, error_type, metadata_json)
        VALUES(:query_id, :economy, :assessment_year, :source_name,
          :query, :url, :attempted_at, :status, :result_summary, :error_type, :metadata_json)
        """,
        {
            "query_id": query["query_id"],
            "economy": query["economy"],
            "assessment_year": query["assessment_year"],
            "source_name": query["source_name"],
            "query": query["query"],
            "url": query.get("url"),
            "attempted_at": query.get("attempted_at", now()),
            "status": query["status"],
            "result_summary": query.get("result_summary"),
            "error_type": query.get("error_type"),
            "metadata_json": json_dumps(query.get("metadata")),
        },
    )


def insert_indicator_score(conn: sqlite3.Connection, score: dict[str, Any]) -> None:
    conn.execute(
        """
        INSERT OR REPLACE INTO indicator_scores(score_id, indicator_node_id,
          ai_suggested_score, reviewer_score, final_score, score_status,
          rationale, uncertainty, created_at)
        VALUES(:score_id, :indicator_node_id, :ai_suggested_score,
          :reviewer_score, :final_score, :score_status, :rationale,
          :uncertainty, :created_at)
        """,
        {
            "score_id": score["score_id"],
            "indicator_node_id": score["indicator_node_id"],
            "ai_suggested_score": score.get("ai_suggested_score"),
            "reviewer_score": score.get("reviewer_score"),
            "final_score": score.get("final_score"),
            "score_status": score["score_status"],
            "rationale": score.get("rationale"),
            "uncertainty": score.get("uncertainty", "medium"),
            "created_at": score.get("created_at", now()),
        },
    )


def load_json(conn: sqlite3.Connection, payload: dict[str, Any]) -> None:
    init_db(conn)
    for node in payload.get("nodes", []):
        upsert_node(conn, node)
    for edge in payload.get("edges", []):
        upsert_edge(conn, edge)
    for query in payload.get("source_queries", []):
        insert_source_query(conn, query)
    for score in payload.get("indicator_scores", []):
        insert_indicator_score(conn, score)
    conn.commit()


def graph_context(conn: sqlite3.Connection, indicator_id: str) -> dict[str, Any]:
    indicator = conn.execute("SELECT * FROM nodes WHERE node_id = ?", (indicator_id,)).fetchone()
    if not indicator:
        raise SystemExit(f"Indicator node not found: {indicator_id}")
    inbound = conn.execute(
        """
        SELECT e.*, n.node_type, n.label, n.citation, n.url, n.text, n.status
        FROM edges e
        JOIN nodes n ON n.node_id = e.source_node_id
        WHERE e.target_node_id = ?
        ORDER BY e.edge_type, n.node_type, n.node_id
        """,
        (indicator_id,),
    ).fetchall()
    scores = conn.execute(
        "SELECT * FROM indicator_scores WHERE indicator_node_id = ? ORDER BY created_at DESC",
        (indicator_id,),
    ).fetchall()
    return {
        "indicator": dict(indicator),
        "supporting_nodes": [dict(row) for row in inbound],
        "scores": [dict(row) for row in scores],
    }


def export(conn: sqlite3.Connection) -> dict[str, Any]:
    tables = ["graph_metadata", "nodes", "edges", "source_queries", "indicator_scores"]
    return {table: [dict(r) for r in conn.execute(f"SELECT * FROM {table}")] for table in tables}


def sample_payload() -> dict[str, Any]:
    return {
        "nodes": [
            {"node_id": "NZL", "node_type": "economy", "label": "New Zealand", "economy": "NZL", "assessment_year": 2025, "status": "demo"},
            {"node_id": "P6", "node_type": "rdtii_pillar", "label": "P6 Cross-border data policies", "status": "framework"},
            {"node_id": "P6_I1", "node_type": "rdtii_indicator", "label": "P6.I1 Cross-border transfer conditions", "status": "framework", "metadata": {"pillar": "P6"}},
            {"node_id": "doc_nz_privacy_2020", "node_type": "document", "label": "Privacy Act 2020", "economy": "NZL", "assessment_year": 2025, "source_type": "primary", "url": "https://www.legislation.govt.nz/act/public/2020/0031/latest/LMS23223.html", "status": "in_force"},
            {"node_id": "prov_nz_privacy_ipp12", "node_type": "provision", "label": "Privacy Act 2020 — IPP 12", "economy": "NZL", "assessment_year": 2025, "source_type": "primary", "citation": "Privacy Act 2020, Information privacy principle 12", "url": "https://www.legislation.govt.nz/act/public/2020/0031/latest/LMS23342.html", "text": "IPP 12 sets conditions for disclosure of personal information to a foreign person or entity.", "status": "in_force"},
            {"node_id": "measure_nz_cross_border_transfer_conditions", "node_type": "regulatory_measure", "label": "Conditions on cross-border disclosure of personal information", "economy": "NZL", "assessment_year": 2025, "source_type": "primary", "citation": "Privacy Act 2020, IPP 12", "text": "Agency must meet statutory conditions before disclosing personal information to a foreign recipient.", "status": "verified"},
            {"node_id": "evidence_nz_p6_i1", "node_type": "evidence_record", "label": "Evidence for NZ P6.I1", "economy": "NZL", "assessment_year": 2025, "source_type": "primary", "citation": "Privacy Act 2020, IPP 12", "status": "verified"},
        ],
        "edges": [
            {"edge_id": "edge_p6_contains_p6i1", "source_node_id": "P6", "target_node_id": "P6_I1", "edge_type": "contains", "confidence": "high"},
            {"edge_id": "edge_doc_contains_ipp12", "source_node_id": "doc_nz_privacy_2020", "target_node_id": "prov_nz_privacy_ipp12", "edge_type": "contains", "confidence": "high"},
            {"edge_id": "edge_ipp12_creates_measure", "source_node_id": "prov_nz_privacy_ipp12", "target_node_id": "measure_nz_cross_border_transfer_conditions", "edge_type": "creates_obligation", "confidence": "high"},
            {"edge_id": "edge_measure_maps_p6i1", "source_node_id": "measure_nz_cross_border_transfer_conditions", "target_node_id": "P6_I1", "edge_type": "maps_to_indicator", "confidence": "high", "rationale": "The measure conditions disclosure of personal information to foreign recipients."},
            {"edge_id": "edge_evidence_supports_p6i1", "source_node_id": "evidence_nz_p6_i1", "target_node_id": "P6_I1", "edge_type": "supports_score", "confidence": "high"},
        ],
        "source_queries": [
            {"query_id": "query_nz_wipolex_privacy", "economy": "NZL", "assessment_year": 2025, "source_name": "WIPO Lex", "query": "New Zealand Privacy Act 2020", "url": "https://www.wipo.int/wipolex/", "status": "attempted", "result_summary": "Demo query log entry; reviewer should preserve live query details in production."},
            {"query_id": "query_nz_taped", "economy": "NZL", "assessment_year": 2025, "source_name": "UN ESCAP TAPED", "query": "New Zealand data transfer digital trade commitments", "url": "https://www.unescap.org/resources/taped", "status": "blocked_automated_access", "error_type": "Cloudflare", "result_summary": "Automated access blocked; pending manual verification."},
        ],
        "indicator_scores": [
            {"score_id": "score_nz_p6i1_demo", "indicator_node_id": "P6_I1", "ai_suggested_score": 0.35, "reviewer_score": None, "final_score": None, "score_status": "draft", "rationale": "Demonstrates AI-suggested scoring separated from reviewer confirmation.", "uncertainty": "medium"}
        ],
    }


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="SQLite RDTII legal knowledge graph")
    parser.add_argument("--db", default="outputs/rdtii_kg.sqlite", help="SQLite database path")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init")
    sub.add_parser("load-sample")
    p_import = sub.add_parser("import-json")
    p_import.add_argument("json_file")
    p_context = sub.add_parser("context")
    p_context.add_argument("--indicator", required=True)
    sub.add_parser("export-json")

    args = parser.parse_args(list(argv) if argv is not None else None)
    with connect(args.db) as conn:
        if args.command == "init":
            init_db(conn)
            print(f"Initialized {args.db}")
        elif args.command == "load-sample":
            load_json(conn, sample_payload())
            print(f"Loaded sample RDTII graph into {args.db}")
        elif args.command == "import-json":
            payload = json.loads(Path(args.json_file).read_text())
            load_json(conn, payload)
            print(f"Imported graph JSON into {args.db}")
        elif args.command == "context":
            print(json.dumps(graph_context(conn, args.indicator), ensure_ascii=False, indent=2))
        elif args.command == "export-json":
            print(json.dumps(export(conn), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
