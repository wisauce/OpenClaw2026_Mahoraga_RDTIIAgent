# Mahoraga — RDTII Hermes Agent Profile

**Mahoraga** is a domain-specific Hermes Agent profile for **RDTII** — the Regional Digital Trade Integration Index — packaged for **RISTEK x Build Club OpenClaw Agenthon 2026**.

This profile is designed to show Hermes Agent as more than a chatbot: it uses Hermes profiles, persona files, skills, memory, tool calls, file operations, web extraction, code execution, and autonomous task loops to complete RDTII policy-review workflows end to end.

## What makes this an agent

Mahoraga is built on Hermes Agent, which provides:

- **Tool calls**: file read/write/search, terminal, Python/code execution, web extraction/search, browser automation, vision, messaging, todo tracking, and scheduled/background jobs.
- **Autonomous loop**: Hermes can continue reasoning, call tools, inspect outputs, revise actions, and verify results until a task is complete.
- **Skills**: reusable domain procedures. Mahoraga's unique skill is `skills/RDTIIAnalyzer/rdtii-policy-review/SKILL.md`.
- **Profile state**: persona (`SOUL.md`), config (`config.yaml`), memory, and skills are packaged as a reusable Hermes profile.
- **Multi-agent capability**: Hermes can delegate subtasks to isolated subagents for parallel research, review, or validation.

## Domain task Mahoraga completes

Given a policy document or URL, Mahoraga can autonomously:

1. Extract or fetch the policy text.
2. Identify discrete regulatory measures.
3. Map each measure to likely RDTII pillars and indicators.
4. Produce evidence-backed rationales with citations/quotes.
5. Suggest scores while keeping AI suggestions separate from human reviewer confirmation.
6. Generate a review-ready audit report and missing-evidence checklist.

This directly satisfies the Agenthon requirement for a system with reasoning, decision-making, tool usage, workflow execution, and at least one autonomous end-to-end task.

## OpenClaw Agenthon alignment

See `references/agenthon-compliance-checklist.md` for the competition-oriented checklist.

Key compliance points:

- Not a basic chatbot wrapper: the profile includes domain skill logic, structured workflow, evidence extraction, scoring rules, and tool-backed verification.
- Autonomous behavior: the agent is instructed to keep working through the workflow until it produces verified reviewer artifacts.
- Technical execution: the profile uses Hermes Agent's built-in tool system, skills, memory, profile configuration, and optional multi-agent delegation.
- Real-world deployability: outputs are designed for policy reviewers and include citations, confidence, uncertainty, and human-review gates.

## Unique vs bundled skills

- **Unique Mahoraga skill**: `skills/RDTIIAnalyzer/rdtii-policy-review/SKILL.md`
- **Bundled Hermes skills**: all other `skills/` directories are general Hermes skills included with the exported profile for broad agent capability.

## Reproducing locally

1. Install Hermes Agent: https://hermes-agent.nousresearch.com/docs
2. Import or place this profile under `~/.hermes/profiles/lomba`.
3. Add secrets/API keys to `.env` locally. Do **not** commit `.env`.
4. Start Hermes with the profile:

```bash
hermes --profile lomba
```

5. For an RDTII demo, ask:

```text
Use the RDTII policy review workflow on this policy text/URL. Extract measures, map them to RDTII pillars and indicators, suggest reviewer scores, and write an audit report.
```

## Safety

Mahoraga provides policy research assistance, not legal advice. Human reviewers should confirm mappings, citations, and final scores before publication or operational use.
