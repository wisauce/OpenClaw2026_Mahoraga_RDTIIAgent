# OpenClaw Agenthon 2026 guidelines for RDTII Framework Agent packaging

Source used in session: `http://ristek.link/Technical-Guidelines` (Google Docs export for RISTEK x Build Club OpenClaw Agenthon 2026).

Use this reference when packaging, documenting, demoing, or submission-checking an RDTII Hermes Agent for the hackathon.

## Competition shape

- Online 12-hour build sprint focused on AI Agents and Multi-Agent Systems.
- Teams may be individuals or up to 4 people.
- One submission per participant/team.
- Any framework, model, API, programming language, or tools are allowed, including Hermes Agent, OpenClaw, Nano Claw, public/open-source templates, libraries, and third-party tools.

## Agent requirements to emphasize

The project should visibly demonstrate an AI Agent or Multi-Agent System with:

- reasoning;
- decision-making;
- tool calls / tool usage;
- workflow execution;
- an autonomous loop;
- at least one task completed end-to-end without manual human intervention.

Do not position the product as a plain chatbot wrapper or an empty UI. The judges care more about functioning agent logic and autonomy than pure visual polish.

## Submission requirements

Devpost: `https://openclawagenthon.devpost.com/`

Required materials:

1. Project description.
2. Public GitHub repository with a clear, reproducible README.
3. Demo video uploaded to YouTube as Unlisted.
4. Pitch deck PDF.
5. Live deployment link, if available.
6. List/explanation of AI tools and models used.

Naming conventions from the guidelines:

- Team: `OpenClaw2026_NamaTim`
- GitHub repo: `OpenClaw2026_NamaTim_NamaProject`
- Demo video: `OpenClaw2026_NamaTim_NamaProject`
- Pitch deck: `OpenClaw2026_NamaTim_NamaProject.pdf`

## Demo and deck constraints

Demo video:

- Maximum 2 minutes.
- Must clearly show product usage flow.
- Must show the AI Agent workflow clearly.
- Must be accessible without permission requests.

Pitch deck:

- PDF only.
- Maximum 5 slides.
- Cover: Problem Statement, Solution Overview, AI Agent Workflow / Architecture and Technical Explanation, Key Features & Tech Stack, Future Development / Impact.

## Judging weights

- Use Case Clarity & Impact: 10%
- Creativity & Originality: 30%
- Autonomy & Agent Behaviour: 30%
- Technical Execution: 20%
- Real-World Deployability: 10%

Optional track: Best Payment Use Case, only if the project integrates payments or financial transactions.

## RDTII Framework Agent positioning checklist

For an RDTII-focused Hermes profile, emphasize:

- End-to-end autonomous RDTII policy-review workflow.
- Tool calls for document ingestion, evidence extraction, indicator mapping, scoring, and report generation.
- Clear architecture: Hermes Agent + `RDTIIAnalyzer/rdtii-policy-review` skill + reviewer-facing outputs.
- Human reviewer confirmation for legal/policy scoring, while still showing agent autonomy in suggestion/extraction/report workflows.
- A README that states the unique skill is under `skills/RDTIIAnalyzer/`; other skills are bundled Hermes skills.
- A short demo that proves autonomous workflow execution, not just conversation.
