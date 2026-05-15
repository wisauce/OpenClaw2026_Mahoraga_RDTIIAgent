# Agenthon 2026 Compliance Checklist — Mahoraga / RDTII

Reference checklist mapping OpenClaw Agenthon 2026 judging criteria to concrete Mahoraga behaviour.

## Judging Criterion 1: Use Case Clarity & Impact (10%)

- [ ] Problem statement clearly identifies the gap: legal/policy teams need structured RDTII evidence-mapping from raw laws/regulations.
- [ ] Solution positioned as an autonomous RDTII policy-review assistant, not a generic chatbot.
- [ ] Target users (policy reviewers, compliance analysts, trade researchers) named explicitly.
- [ ] Real-world impact articulated: faster indicator mapping, auditable evidence, reviewer-quality scoring.

## Judging Criterion 2: Creativity & Originality (30%)

- [ ] Domain-specific agent for RDTII 2.1 (not a generic chatbot wrapper).
- [ ] Unique RDTIIAnalyzer skill under skills/RDTIIAnalyzer/ with RDTII-specific data models, weights, indicators.
- [ ] Amendment-aware legal corpus processing (base-law vs amendment lifecycle).
- [ ] Provision dependency graph / GraphRAG design for holistic legal interpretation.
- [ ] Multilingual/non-Latin-script legal source pipeline (script-aware OCR, BCP-47 tags, translation review).
- [ ] Separate ai_suggested_score / reviewer_score / final_score to respect legal-review discipline.

## Judging Criterion 3: Autonomy & Agent Behaviour (30%)

- [ ] Autonomous loop: Hermes agent can ingest documents, extract measures, map to indicators, suggest scores, and produce an audit report without per-step human prompting.
- [ ] Tool use demonstrated: document reading, OCR, web search for official sources, structured JSON output, file creation.
- [ ] Decision-making: agent determines which pillar/indicator a measure maps to, suggests score, flags uncertainty.
- [ ] Workflow execution: follows the complete end-to-end pipeline (source discovery → fetch → extract → map → score → report).
- [ ] Human-in-the-loop: final score requires reviewer confirmation, but all upstream work is autonomous.
- [ ] Produces a concrete artifact (e.g. outputs/rdtii-review-report.md) autonomously.

## Judging Criterion 4: Technical Execution (20%)

- [ ] Configurable RDTII framework (12 pillars, indicators, weights in structured data).
- [ ] Reproducible evidence pipeline: source discovery log, fetch metadata, chunk preservation, citation tracking.
- [ ] JSON schemas for: measures, mappings, assessments, evidence, scorecards.
- [ ] Amendment workflow: base law, amendment, consolidation, repeal classification.
- [ ] Provision dependency graph with explicit edge types and confidence thresholds.
- [ ] Multilingual handling: BCP-47, original+translated text separation, translation method recording.
- [ ] Security: redact_secrets: true in local config, no live credentials in repo.

## Judging Criterion 5: Real-World Deployability (10%)

- [ ] Public GitHub repo with clear, reproducible README.
- [ ] config.example.yaml provided (redacted, no live credentials).
- [ ] Demo video (max 2 min, YouTube Unlisted) showing autonomous workflow.
- [ ] Pitch deck (max 5 slides, PDF) matching required cover.
- [ ] All links accessible without extra permission requests.
- [ ] Naming conventions followed: OpenClaw2026_NamaTim, repo, video, deck.
