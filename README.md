# OpenClaw-Agenthon_Mahoraga

**Mahoraga** is a domain-specific Hermes Agent for **RDTII** — the Regional Digital Trade Integration Index.

This repository is a sanitized Hermes profile export from `~/.hermes/profiles/lomba`, configured for RDTII-oriented law, policy, and compliance review workflows.

## Purpose

Mahoraga assists policy reviewers and builders working with RDTII systems by helping to:

- Map digital trade laws, regulations, policy measures, and evidence to RDTII pillars and indicators
- Support RDTII 2.1 scoring, reviewer assessment, and audit-trail workflows
- Design schemas, APIs, prompts, and datasets for RDTII review products
- Produce structured, evidence-oriented policy research outputs for human expert review

RDTII outputs should be treated as policy research assistance, not legal advice.

## OpenClaw Agenthon context

Mahoraga is packaged for **RISTEK x Build Club OpenClaw Agenthon 2026**. The profile understands the official technical guidelines from `http://ristek.link/Technical-Guidelines` and keeps them in mind for packaging, documentation, demo, and submission work.

Key guideline implications:

- This must be an AI Agent or Multi-Agent System, not a basic chatbot wrapper.
- The system should demonstrate reasoning, decision-making, tool usage, workflow execution, and an autonomous loop.
- At least one task should be completed end-to-end without manual human intervention.
- The README should stay reproducible for judges.
- The demo should clearly show product workflow and agent behavior within 2 minutes.
- The pitch deck should cover problem, solution, agent workflow/architecture, key features/tech stack, and future development/impact.

A concise guideline summary is stored in `references/openclaw-agenthon-technical-guidelines.md`.

## Skills

The skill unique to this agent lives under `skills/RDTIIAnalyzer/`, especially `skills/RDTIIAnalyzer/rdtii-policy-review/SKILL.md`.

All other skills in this repository are bundled Hermes skills included with the exported profile for general agent capability and should not be treated as Mahoraga-specific domain logic.

## Safety and secrets

Sensitive/runtime files are intentionally excluded. Use `config.example.yaml` as a redacted reference and create your local `config.yaml` / `.env` outside version control.

The `.gitignore` excludes profile secrets, credentials, local runtime state, databases, logs, sessions, caches, lock files, PID files, and live config.
