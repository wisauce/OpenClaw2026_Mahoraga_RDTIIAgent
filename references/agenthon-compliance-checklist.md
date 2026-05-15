# Agenthon Compliance Checklist for RDTII Agent

This checklist translates the RISTEK x Build Club OpenClaw Agenthon 2026 technical guidelines into concrete profile requirements.

## Required agent behavior

- [x] **AI Agent / Multi-Agent System**: The agent is a Hermes Agent profile with domain persona, skills, memory, toolsets, and optional delegation.
- [x] **Reasoning**: RDTII mapping requires interpreting legal measures, policy area, indicator fit, confidence, missing evidence, and score implications.
- [x] **Decision-making**: The agent selects source-handling strategy, extracts measures, chooses candidate pillars/indicators, and identifies when evidence is insufficient.
- [x] **Tool usage**: The profile enables Hermes tools for web extraction/search, files, terminal/code execution, vision/OCR-adjacent analysis, todo tracking, memory, and skills.
- [x] **Workflow execution**: The RDTII skill defines a repeatable workflow from source ingestion to measure extraction, mapping, assessment, scorecard, and audit report.
- [x] **Autonomous loop**: Hermes should continue through tool calls and verification until it has produced the requested reviewer artifact or clearly reports blockers.
- [x] **End-to-end task**: A complete demo can start from a policy URL/text and end with a structured RDTII review report.

## Demo workflow recommended for judges

Use a short policy excerpt or public policy URL and ask the agent to:

1. Fetch/extract the document text.
2. Split the text into candidate legal/policy measures.
3. Map measures to RDTII pillars/indicators.
4. Suggest scores while preserving human-review gates.
5. Write `outputs/rdtii-review-report.md` with citations, confidence, and missing evidence.
6. Verify that the output contains the required fields.

## 2-minute demo video structure

- **0:00–0:15**: Problem — RDTII review is evidence-heavy and requires traceable policy mapping.
- **0:15–0:35**: Show the Hermes profile with unique `RDTIIAnalyzer` skill.
- **0:35–1:25**: Run the end-to-end workflow on a policy input; show tool calls and autonomous steps.
- **1:25–1:45**: Show generated audit report and human-review fields.
- **1:45–2:00**: Explain impact, deployability, and why it is an agent rather than a chatbot.

## 5-slide pitch deck outline

1. **Problem Statement** — policy reviewers need traceable, consistent RDTII mapping from legal text.
2. **Solution Overview** — a domain-specific Hermes Agent for RDTII review.
3. **AI Agent Workflow / Architecture** — Hermes loop + tools + RDTIIAnalyzer skill + reviewer outputs.
4. **Key Features & Tech Stack** — Hermes Agent, profile, skills, web/file/code tools, evidence schema, audit reports.
5. **Future Development / Impact** — reviewer UI, source ingestion pipeline, country scorecards, validation, deployment.

## Judging criteria mapping

- **Use Case Clarity & Impact (10%)**: RDTII policy review is a concrete law/compliance problem with real reviewer pain points.
- **Creativity & Originality (30%)**: Uses a domain-specific Hermes profile and skill system, not a generic chatbot.
- **Autonomy & Agent Behaviour (30%)**: Demonstrates tool use, autonomous loop, evidence extraction, mapping, and report generation.
- **Technical Execution (20%)**: Uses reproducible profile configuration, structured skill logic, safe secret handling, and clear outputs.
- **Real-World Deployability (10%)**: Preserves citations, uncertainty, human-review gates, and audit logs suitable for compliance workflows.

## Submission hygiene

- Public GitHub repository.
- Reproducible README.
- Clear AI tools/models used.
- No secrets, live config, logs, sessions, or runtime databases committed.
- Demo video must be Unlisted and accessible.
- Pitch deck must be PDF, max 5 slides.
