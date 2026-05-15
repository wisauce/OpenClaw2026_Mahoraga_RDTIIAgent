# Agenthon Pitch Deck Template — RDTII Agent / Team Mahoraga

Use this reference when generating 5-slide pitch deck contents for OpenClaw Agenthon 2026 submissions. Each slide must map to the judging criteria: Use Case Clarity (10%), Creativity (30%), Autonomy & Agent Behaviour (30%), Technical Execution (20%), Deployability (10%).

## Required slide structure

The Agenthon guidelines mandate this exact cover:

| Slide | Topic | Covers |
|-------|-------|--------|
| 1 | Problem Statement | Use case clarity, pain points, target users |
| 2 | Solution Overview | What it is, key capability, human-in-the-loop, evidence design |
| 3 | AI Agent Workflow & Architecture | Layers, subagents, reasoning/tool use, reviewer gate (Autonomy + Technical) |
| 4 | Key Features & Tech Stack | Unique RDTII features, frameworks, models, tools |
| 5 | Future Development & Impact | Roadmap, vision, real-world impact, Agenthon alignment checklist |

## Per-slide content shape

Each slide has four sections in the markdown source:

1. **Title** — a punchy claim, not a generic label (e.g. "Digital Trade Policy Review is Slow, Fragmented, and Error-Prone" not "Problem")
2. **Body** — 3–6 bullet points covering the key message. Keep scannable.
3. **Visual idea** — what the slide should look like as a suggestion to the designer (diagrams, grids, pipeline flows, heatmaps)
4. **Speaker notes** — 2–4 sentences for the presenter. Should explain the problem in concrete terms, the architecture in technical but accessible language, and the impact with a before/after comparison.

## Slide 1 — Problem Statement

**Title template:** `[Domain area] is [Slow / Fragmented / Error-Prone / Manual]`

Body should cover:
- The gap: what reviewers/users currently do manually
- The pain: specific breakdowns (citations lost, databases skipped, scoring inconsistent)
- The cost: timeline (weeks per economy), quality variance, audit gaps
- Who feels this: specific roles and organisations

**Visual ideas:** Grid of pillars with "missing evidence" badges. Messy dotted lines between documents and indicators. Timeline graphic showing weeks.

**Speaker notes pattern:** Name the specific framework (RDTII 2.1, 12 pillars, ~60 indicators). Give a concrete example (e.g. "our Japan research required 30+ primary sources with article-level citations"). Name the required databases that get skipped.

## Slide 2 — Solution Overview

**Title template:** `[Agent Name] — Domain-Specific AI Agent for [Framework/Index]`

Body should cover:
- What it is: framework + agent architecture (e.g. "Hermes Agent with embedded RDTII skill")
- Key capability: the autonomous pipeline (ingest → extract → map → score → report)
- Human-in-the-loop: AI suggests, reviewer confirms — legal finality stays with expert
- Evidence-first: article citations, source URLs, database query logs

**Visual ideas:** Pipeline flowing left-to-right: Document → Extract → Map to Pillars → Suggest Scores → Audit Report → "Reviewer Confirms" gate

**Speaker notes pattern:** Emphasise why this isn't a chatbot. Describe the reproducible, audit-ready workflow. Call out the separated-scoring design for legal compliance.

## Slide 3 — AI Agent Workflow & Architecture

**Title template:** `Autonomous Multi-Agent Pipeline with [Reviewer/Human] Gate`

Structure as layers (top to bottom):

**Layer 1 — Orchestrator Agent** (Hermes Agent)
- Loads domain skill, creates indicator checklist, dispatches parallel subagents

**Layer 2 — Multi-Agent Parallel Research** (N subagents)
- List subagent groups by thematic pillar clusters
- Each gets isolated tools (web, file, browser)

**Layer 3 — Central Scoring and Audit**
- Merge, verify against live sources, score with explicit status (verified/provisional/missing)
- Produces concrete artifact (`outputs/rdtii-review-report.md`)

**Layer 4 — Human Reviewer Hand-off**
- AI suggestion ≠ reviewer score ≠ final score
- Missing evidence, translation flags, blocked databases documented

**Visual ideas:** Stacked layer diagram. Top: user → agent. Middle: N parallel subagent boxes labelled by pillars. Bottom: merge → scoring → audit → reviewer gate.

**Speaker notes pattern:** Describe the subagent split rationale. Emphasise that the orchestrator verifies subagent findings against live sources (spot-checks official PDFs), not trusting self-reports. Call out the Agenthon alignment (multi-agent, tool use, autonomous end-to-end).

## Slide 4 — Key Features & Tech Stack

**Title template:** `Evidence-Grade [Domain] Engine Built on [Framework]`

Body should cover:

**Features** (table or checklist format):
- Structured framework data (pillars, indicators, weights, rule types)
- Provision dependency graph (cross-references, definitions, exceptions)
- Amendment-aware corpus processing
- Multilingual/script pipeline
- Required-database discipline
- Separated scoring (AI vs reviewer vs final)
- Audit-ready reports with evidence trails

**Tech Stack:**
- Agent framework: Hermes Agent (profiles, skills, memory, subagent delegation)
- LLM backend: compatible model name(s)
- Data models: modular JSON schemas
- Tool integrations: browser, web, curl, Python, OCR, file ops
- Deployment: local profile via config.yaml + skills/

**Visual ideas:** Left side: feature checkboxes with check marks. Right side: mini tech-stack logo row or column.

**Speaker notes pattern:** Pick 2–3 features to explain in more depth (e.g. dependency graph: "we don't score Article 12 without also understanding Article 3's definition and Article 18's exception"). Explain why this design is legally defensible for UN-grade reviews.

## Slide 5 — Future Development & Impact

**Title template:** `From Manual [X] to Scalable, Repeatable [Y]`

Body should cover:

**Near-term roadmap** (3 items):
- Reviewer UI or dashboard
- Automation / watchers / monitoring
- Comparative or cross-economy features

**Long-term vision** (2–3 items):
- Expand to other indices
- Advanced AI patterns (GraphRAG, holistic reasoning)
- Multi-language or multi-region support

**Real-world impact** (before/after table):
- Before: weeks, inconsistent evidence, missed databases
- After: days, auditable citations, verified primary sources

**Agenthon alignment checklist:**
- ✅ Autonomous end-to-end loop
- ✅ Multi-agent parallel research
- ✅ Tool-backed evidence verification
- ✅ Human-in-the-loop for legal finality
- ✅ Domain-specific skill

**Visual ideas:** Timeline "Weeks → Days" with downward trend. Map with heat-coded scores. Before/after comparison.

**Speaker notes pattern:** Call the reviewer UI "the final mile." Describe the watcher pattern (cron-based gazette monitoring auto-flags re-scoring). Explain the core insight that policy review is a structured information workflow, not creative writing, which is why AI agents excel at it. Close with the Agenthon criteria alignment.

## Naming convention

```
OpenClaw2026_NamaTim_NamaProject.pdf
```

Format the file header:
```markdown
# OpenClaw2026_NamaTim_NamaProject — Pitch Deck Contents

> Format: 5 slides, PDF
> Naming: `OpenClaw2026_NamaTim_NamaProject.pdf`
> Team: NamaTim
> Project: [Project Name]

---
```

## Speaker notes style

- Keep to 2–4 sentences per slide in the markdown source
- Start with the framework/domain context
- Include one concrete example or data point
- Describe the architecture in technical but accessible terms
- End with an impact statement or competition alignment

## Common pitfalls

- Slide 1 defines the problem too vaguely (generic "slow and manual" without specific costs or users)
- Slide 2 describes a chatbot instead of an agent (must show autonomous pipeline, not Q&A)
- Slide 3 has no layer separation or reviewer gate — architecture looks like a flat pipeline
- Slide 4 lists features without explaining why they matter or what makes them unique
- Slide 5 forgets the before/after impact comparison and Agenthon alignment checklist
- Speaker notes summarise the slide instead of adding depth for the presenter
- All 5 slides not included (guidelines mandate exactly 5 slides)
- Naming convention not followed for the PDF file
