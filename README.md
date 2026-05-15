# RDTII Framework Agent — Hermes Agent Profile for OpenClaw Agenthon 2026

**RDTII Framework Agent** is a domain-specific Hermes Agent for **RDTII** — the Regional Digital Trade Integration Index — packaged for **RISTEK x Build Club OpenClaw Agenthon Indonesia 2026**.

This agent is purpose-built for autonomous digital trade policy review. It uses Hermes Agent as its framework — with persona files, skills, memory, tool calls, web extraction, browser automation, code execution, and multi-agent task delegation — to complete end-to-end RDTII policy-review workflows without manual intervention.

## What makes this an agent

Built on Hermes Agent, this system demonstrates genuine agent behavior beyond chatbot interactions:

| Capability | How it works |
|---|---|
| **Autonomous loop** | Hermes reasons, calls tools, inspects outputs, revises actions, and verifies results until the task produces a concrete artifact (e.g., `outputs/rdtii-review-report.md`). |
| **Tool-backed execution** | File read/write, terminal, Python/code execution, web extraction/search, browser automation, vision, todo tracking, cron scheduling, and multi-agent delegation. |
| **Domain skill system** | The unique `skills/RDTIIAnalyzer/rdtii-policy-review/SKILL.md` encodes RDTII methodology, scoring rules, evidence extraction procedures, database fallback patterns, and reviewer safeguards. |
| **Multi-agent parallelism** | Can delegate pillar-specific research to isolated subagents running in parallel (e.g., Tariffs & Investment, Data & Privacy, Telecom & Platforms, Digital Economy & IP). |
| **Reviewer-safe scoring** | Separates `ai_suggested_score`, `reviewer_score`, and `final_score` — the agent never finalizes a score without human confirmation. |
| **Profile state** | Persona (`SOUL.md`), redacted config (`config.example.yaml`), memory, and skills are packaged as a reusable Hermes profile. |

## Domain task it completes

Given a policy document, URL, or country name, the agent autonomously:

1. Loads the `rdtii-policy-review` skill and follows its methodology.
2. Fetches or extracts the source text from primary legal/policy documents.
3. Identifies discrete regulatory measures (not just document-level themes).
4. Maps each measure to candidate RDTII pillar(s) and indicator(s) with exact quotes/citations.
5. Queries required secondary databases (WTO I-TIP, Global Trade Alert, TAPED, V-Dem, WIPO Lex, WITS) — documents failures if blocked.
6. Suggests AI scores while keeping them separate from human reviewer confirmation.
7. Writes a reviewer-ready audit report with evidence table, missing-evidence checklist, and source-query log.

## OpenClaw Agenthon alignment

See `references/agenthon-compliance-checklist.md` for the full competition checklist.

| Judging criterion | Weight | How we meet it |
|---|---|---|
| Use Case Clarity & Impact | 10% | RDTII is a real UN framework used by 30+ economies to benchmark digital trade regulation. |
| Creativity & Originality | 30% | Novel application of Hermes Agent to structured legal compliance workflow — not a chatbot. |
| Autonomy & Agent Behaviour | 30% | Autonomous end-to-end loop: load skill → fetch sources → extract measures → map to RDTII → produce report. |
| Technical Execution | 20% | Hermes Agent framework with tool-calling, skills, memory, delegation, browser, web, and code execution. |
| Real-World Deployability | 10% | Designed for actual UN ESCAP policy reviewers with audit trails, evidence logs, and human-in-the-loop gates. |

## Unique vs bundled skills

- **Unique skill**: `skills/RDTIIAnalyzer/rdtii-policy-review/SKILL.md` — the core domain expertise
- **Bundled Hermes skills**: all other `skills/` directories are standard Hermes skills included for agent capability (GitHub workflows, creative tools, etc.)

## Quickstart

### Prerequisites

- Python 3.11+
- Hermes Agent installed ([docs](https://hermes-agent.nousresearch.com/docs))

### Setup

```bash
# Clone or place this profile
git clone https://github.com/wisauce/OpenClaw-Agenthon_Mahoraga.git ~/.hermes/profiles/lomba
cd ~/.hermes/profiles/lomba

# Copy the redacted config and add your API keys
cp config.example.yaml config.yaml
# Edit config.yaml with your model provider and API key
# Or set up a .env file for secrets
```

### Run

```bash
hermes --profile lomba
```

### Demo an end-to-end RDTII review

Once Hermes is running, give the agent a task like:

```
Run an end-to-end RDTII review on Australia's digital trade policies. 
Load the rdtii-policy-review skill, fetch primary sources, extract 
regulatory measures, map to RDTII pillars, query required databases, 
suggest scores, and write the audit report to outputs/rdtii-review-report.md.
```

Or use the prepared demo prompt in `examples/rdtii-demo-prompt.md`.

## Project structure

```
.
├── README.md                              # This file
├── SOUL.md                                # Agent persona definition
├── config.example.yaml                    # Redacted config template
├── .gitignore                             # Sanitized repo rules
├── .no-bundled-skills                     # Prevents auto-skill-load duplication
├── bin/tirith                             # Security policy engine
├── memories/
│   └── USER.md                            # User profile for agent memory
├── skills/
│   ├── RDTIIAnalyzer/                     # ★ Unique domain skill
│   │   └── rdtii-policy-review/
│   │       ├── SKILL.md                   # Core RDTII methodology
│   │       └── references/                # Worked examples, checklists
│   └── ...                                # Bundled Hermes skills
├── references/
│   ├── agenthon-compliance-checklist.md   # Judging criterion mapping
│   └── openclaw-agenthon-guidelines.md    # Competition rules
├── examples/
│   └── rdtii-demo-prompt.md              # Ready-to-use demo prompt
└── bin/
    └── tirith                             # Safety policy enforcement
```

## Safety

RDTII Framework Agent provides **policy research assistance, not legal advice**. All outputs require human expert review before operational use. The agent:

- Cannot finalize RDTII scores without reviewer confirmation
- Documents uncertainty, blocked databases, and missing evidence explicitly
- Never replaces professional legal interpretation
- Separates AI suggestions from reviewer decisions in all output artifacts

## License

MIT — see the Hermes Agent license for the framework. The RDTII domain skill and this profile configuration are provided under MIT.
