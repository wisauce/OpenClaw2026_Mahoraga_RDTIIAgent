# OpenClaw2026_Mahoraga_Mahoraga — Pitch Deck Contents

> **Format:** 5 slides, PDF
> **Naming:** `OpenClaw2026_Mahoraga_Mahoraga.pdf`
> **Team:** Mahoraga
> **Project:** Mahoraga — RDTII Domain-Specific Hermes Agent

---

## Slide 1 — Problem Statement

**Title:** Digital Trade Policy Review is Slow, Fragmented, and Error-Prone

**Body:**

- **The gap:** Policy reviewers hand-map hundreds of laws, regulations, and decrees to the UN Regional Digital Trade Integration Index (RDTII 2.1) — 12 pillars, ~60+ indicators, each needing primary-source legal evidence.
- **The pain:** Manual extraction is slow, citations get lost, databases are skipped, and scoring is inconsistent across economies.
- **The cost:** Takes weeks per economy. Audit trails are incomplete. Secondary sources replace primary law. Review quality varies by reviewer.
- **Who feels this:** Trade compliance analysts, policy researchers, international-trade law teams, UN ESCAP reviewers.

**Visual idea:** A grid of 12 pillar cards, many with "missing evidence" badges, connected by messy dotted lines to law documents. Arrows showing a "weeks per economy" timeline.

**Speaker notes:**
RDTII is the UN framework mapping 12 pillars of digital trade regulation from tariffs to data flows. Today, reviewers manually extract provisions from laws, map them to indicators, and score them — without structured tooling. Our research on Japan alone required 30+ primary sources, each with article-level citations. Most teams skip required databases like WTO I-TIP or TAPED because they're difficult to query systematically. This is the gap we solve.

---

## Slide 2 — Solution Overview

**Title:** Mahoraga — Domain-Specific AI Agent for RDTII Policy Review

**Body:**

- **What it is:** A domain-specific **Hermes Agent** with an embedded RDTII skill that autonomously ingests legal sources, extracts regulatory measures, maps them to RDTII indicators, suggests scores, and produces auditable review reports.
- **Key capability:** Completes the full review pipeline — source discovery → fetch → extract → map → score → report — without per-step human prompting.
- **Human in the loop:** AI suggests scores; reviewer confirms. Legal finality stays with the expert.
- **Evidence-first design:** Every score is backed by article-level citations, source URLs, primary/secondary distinctions, and a query log for every required database.

**Visual idea:** A pipeline diagram flowing left to right: Document → Extract Measures → Map to 12 Pillars → Suggest Scores → Audit Report. A "Reviewer Confirms" gate at the end.

**Speaker notes:**
Mahoraga isn't a chatbot that answers questions about trade policy. It's an autonomous AI agent that drives a reproducible, audit-ready review workflow. It separates AI suggestions from reviewer decisions — critical for legal compliance work. It queries required databases (WTO I-TIP, TAPED, Global Trade Alert, WIPO Lex, WITS) and documents access failures. Every output is structured for human expert finalisation.

---

## Slide 3 — AI Agent Workflow & Architecture

**Title:** Autonomous Multi-Agent Pipeline with Reviewer Gate

**Body:**

**Architecture (top to bottom):**

**Layer 1 — Orchestrator Agent (Hermes Agent)**
- Loads RDTII skill; creates indicator checklist; dispatches parallel research subagents.

**Layer 2 — Multi-Agent Parallel Research (4 subagents)**
- Data & Cross-border (P6, P7) | Telecom & Platforms (P5, P8, P9)
- Trade & Investment (P1, P2, P3, P10) | Digital Economy & IP (P4, P11, P12)
- Each subagent has isolated tool context (web search, file ops, browser).

**Layer 3 — Central Scoring and Audit**
- Orchestrator merges results, provisions, and database queries from all subagents.
- Verifies critical provisions against live official PDFs.
- Scores indicators with explicit `verification_status`: verified / provisional / missing.
- Produces `outputs/rdtii-review-report.md` with full evidence trail.

**Layer 4 — Human Reviewer Hand-off**
- AI suggestions labelled `ai_suggested_score`; reviewer sets `final_score`.
- Missing evidence, flagged translations, and blocked databases documented clearly.

**Visual idea:** A layered architecture diagram:
- Top: User prompt → Hermes Agent
- Middle: 4 parallel subagent boxes, each labelled with pillars
- Bottom: Central merge → Scoring engine → Audit report → Reviewer gate

**Speaker notes:**
The architecture uses Hermes Agent as the orchestrator. For a full economy review, it spawns 4 parallel subagents — each covering 2–4 related pillars — to research independently. Each subagent has web, terminal, and file tools. The orchestrator merges their findings, spot-checks critical provisions against live government PDFs, computes scores, and writes a structured audit report. Only at the final stage does a human reviewer confirm or adjust scores. This satisfies the Agenthon requirement for a multi-agent system with reasoning, tool use, and autonomous end-to-end execution.

---

## Slide 4 — Key Features & Tech Stack

**Title:** Evidence-Grade RDTII Engine Built on Hermes Agent

**Body:**

| Feature | What it does |
|---------|-------------|
| **Structured RDTII data** | 12 pillars, ~60 indicators, indicator weights, 6 scoring rule types (binary, ordinal, continuous, formula, external, membership) |
| **Provision dependency graph** | Tracks cross-references, definitions, exceptions, amendments per economy — avoids scoring provisions in isolation |
| **Amendment-aware corpus** | Classifies base law vs amendment vs consolidation vs repeal; rebuilds consolidated view for assessment year |
| **Multilingual legal pipeline** | Script-aware OCR (Latin, Arabic, Thai, Khmer, CJK); BCP-47 tagging; original + translation separation |
| **Database discipline** | Attempts WTO I-TIP, TAPED, Global Trade Alert, V-Dem, WIPO Lex, WITS; documents every block |
| **Separated scoring** | ai_suggested_score ≠ reviewer_score ≠ final_score — legal-review compliant |
| **Audit-ready reports** | Evidence tables, citation trails, source-query logs, uncertainty flags |

**Tech Stack:**

- **Agent framework:** Hermes Agent (tool-calling LLM orchestrator with profile, skills, memory, subagent delegation)
- **LLM backend:** Qwen 3.6+ / DeepSeek V4 (any Hermes-compatible model)
- **Data models:** Modular JSON schemas for measures, mappings, assessments, evidence, scorecards
- **Tool integrations:** Browser automation, web search, curl, Python/code exec, file ops, OCR pipeline
- **Deployment:** Local Hermes profile; configurable via config.yaml + skills/ directory

**Visual idea:** Left side: feature checkboxes with check marks. Right side: a mini tech-stack logo row (Hermes + LLM icons).

**Speaker notes:**
What makes Mahoraga unique is the RDTII-specific design built on top of Hermes Agent's general capabilities. The data model separates framework definition from source documents from extracted measures from reviewer assessments — this mirrors how real legal review works. The provision dependency graph means we don't score Article 12 without also understanding the definition in Article 3 and the exception in Article 18. The multilingual pipeline handles everything from Thai to Arabic to Chinese. And because we separately track AI suggestions and reviewer scores, the system is legally defensible for UN ESCAP-grade reviews.

---

## Slide 5 — Future Development & Impact

**Title:** From Manual Review to Scalable, Repeatable Digital Trade Intelligence

**Body:**

**Near-term roadmap:**
- **Interactive reviewer UI:** Dashboard for accept/reject mappings, adjust scores, view evidence side-by-side with source PDF
- **Automated amendment tracking:** Cron-based watchers for gazette updates per economy — auto-detect and flag provisions that need re-scoring
- **Comparative scoring:** Side-by-side pillar comparison across economies; heatmaps for regional digital trade integration

**Long-term vision:**
- Expand to other trade indices (OECD DSTRI, ADB ARIC) via reusable agent templates
- GraphRAG-based holistic legal reasoning across all 12 pillars for a single economy
- Multi-language reviewer interface for ASEAN+6 economies

**Real-world impact:**
- **Before Mahoraga:** Weeks per economy, inconsistent evidence, missed databases
- **With Mahoraga:** Days per economy, auditable citation trails, verified primary sources, reviewer-ready outputs

**Agenthon alignment:**
- ✅ Autonomous end-to-end loop
- ✅ Multi-agent parallel research
- ✅ Tool-backed evidence verification
- ✅ Human-in-the-loop for legal finality
- ✅ Domain-specific skill (RDTIIAnalyzer)

**Visual idea:** A timeline graphic: "Weeks per economy → Days per economy" with a graph trending down. Or a map of ASEAN+6 with heat-coded RDTII scores across countries.

**Speaker notes:**
The immediate next step is a reviewer dashboard — because while the agent produces excellent structured outputs, the final mile is human interaction. After that, we add automated amendment watchers so the system proactively tells reviewers "Japan's APPI was amended — these 4 indicators need re-scoring." Long-term, the same architecture applies to any structured trade index. The core insight is that policy review is a structured information workflow, not creative writing, and that's precisely what AI agents excel at — if you build the right domain layer. In OpenClaw terms, Mahoraga demonstrates agent autonomy, multi-agent parallelism, tool use, and an auditable output artifact — hitting all 5 judging criteria.
