# RDTII Legal Knowledge Graph

RDTII Agent includes a small **real database implementation** for custom RDTII legal knowledge graphs using SQLite. It is designed for hackathon demos and reviewer-safe local execution: no server, no network calls, no secrets, and no external dependencies.

## What it stores

The graph persists RDTII review objects as typed nodes and typed edges.

Node types include:

- `economy`
- `document`
- `provision`
- `definition`
- `regulatory_measure`
- `rdtii_pillar`
- `rdtii_indicator`
- `evidence_record`
- `database_record`
- `reviewer_assessment`

Edge types include:

- `contains`
- `defines`
- `references`
- `amends_or_repeals`
- `has_exception`
- `creates_obligation`
- `supports_measure`
- `maps_to_indicator`
- `supports_score`
- `database_supports_measure`
- `requires_human_review`

The DB also stores:

- `source_queries` — required database/source attempts, including blocked sources.
- `indicator_scores` — separates `ai_suggested_score`, `reviewer_score`, and `final_score`.

## Quick demo

From the repository root:

```bash
python3 scripts/rdtii_kg.py --db outputs/rdtii_kg_demo.sqlite init
python3 scripts/rdtii_kg.py --db outputs/rdtii_kg_demo.sqlite load-sample
python3 scripts/rdtii_kg.py --db outputs/rdtii_kg_demo.sqlite context --indicator P6_I1
```

Import a JSON fixture:

```bash
python3 scripts/rdtii_kg.py --db outputs/rdtii_kg_fixture.sqlite init
python3 scripts/rdtii_kg.py --db outputs/rdtii_kg_fixture.sqlite import-json examples/rdtii_kg_fixture.json
python3 scripts/rdtii_kg.py --db outputs/rdtii_kg_fixture.sqlite context --indicator P12_I_ESIGNATURE
```

Export the graph:

```bash
python3 scripts/rdtii_kg.py --db outputs/rdtii_kg_demo.sqlite export-json
```

## Safety / review discipline

This database does **not** make final legal determinations. It supports policy research by preserving evidence relationships and uncertainty states.

Rules:

- Do not treat missing evidence as score `0`.
- Keep `ai_suggested_score`, `reviewer_score`, and `final_score` separate.
- Store blocked source attempts in `source_queries` rather than silently omitting them.
- Mark demo or unverified records as `needs_reviewer_confirmation` or `missing`.
- Use primary legal sources for final scoring where possible.

## Why SQLite

SQLite gives the Agenthon demo a real DB without operational risk:

- reproducible locally;
- no credentials;
- no exposed service port;
- easy to inspect with standard tools;
- can later migrate to Neo4j, PostgreSQL, or RDF if needed.

## Example claim for the pitch

> RDTII Agent creates a custom provision-level legal knowledge graph in SQLite: documents, provisions, measures, RDTII indicators, evidence records, source-query logs, and reviewer scores are persisted as typed nodes and edges, enabling auditable retrieval of scoring context while keeping final legal judgment with human reviewers.
