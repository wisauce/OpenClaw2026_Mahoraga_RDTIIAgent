# Agenthon Profile Packaging Notes for RDTII Framework Agent

Use these notes when packaging or refreshing the RDTII Framework Hermes profile for RISTEK x Build Club OpenClaw Agenthon submissions.

## Durable workflow learned

When the user asks to make the RDTII Framework profile compliant with OpenClaw Agenthon requirements, treat the profile directory itself as the agent artifact, not merely documentation.

Recommended flow:

1. Load this `rdtii-policy-review` skill and, if the task involves Hermes Agent configuration/profile behavior, also load the `hermes-agent` skill.
2. Inspect the active profile folder, especially:
   - `SOUL.md` for persona and behavior;
   - `config.yaml` for local-only runtime settings;
   - `README.md` for judge-facing reproducibility;
   - `skills/RDTIIAnalyzer/rdtii-policy-review/SKILL.md` for the unique domain skill;
   - `examples/` and `references/` for demo prompts and compliance notes.
3. Make the profile demonstrate an autonomous AI agent, not a chatbot wrapper:
   - explicit RDTII domain identity;
   - decision-making and reviewer safeguards;
   - tool-backed evidence extraction/mapping/scoring workflow;
   - autonomous loop that produces a concrete artifact, e.g. `outputs/rdtii-review-report.md`;
   - separation of `ai_suggested_score`, `reviewer_score`, and `final_score`.
4. Keep the repository sanitized:
   - do not commit live `config.yaml`, `.env`, `auth.json`, `auth.lock`, `state.db*`, logs, sessions, caches, or credential/token/secret files;
   - generate or maintain a redacted `config.example.yaml` instead;
   - preserve `security.redact_secrets: true` in local profile config when present.
5. Add or refresh judge-facing artifacts:
   - profile `README.md` explaining RDTII Framework Agent as a domain-specific Hermes Agent for RDTII;
   - `references/agenthon-compliance-checklist.md` mapping Agenthon requirements to concrete behavior;
   - `references/openclaw-agenthon-technical-guidelines.md` or equivalent guideline summary;
   - `examples/rdtii-demo-prompt.md` showing an end-to-end RDTII workflow.
6. Validate before finalizing:
   - parse YAML/config where applicable;
   - check required files exist;
   - run a focused secret scan on staged/exported files;
   - verify ignored/absent status for sensitive paths after sync;
   - confirm local and remote Git HEADs after push if publishing.

## Preferred README positioning

The README should state clearly:

- RDTII Framework Agent is a domain-specific Hermes Agent for the Regional Digital Trade Integration Index (RDTII).
- The unique domain skill is under `skills/RDTIIAnalyzer/`.
- Other skills are bundled Hermes skills, not the submission's unique RDTII contribution.
- RDTII outputs are policy research assistance requiring expert review, not legal advice.
- The demo should show tool use and artifact generation, not only chat responses.

## Pitfalls

- Do not publish the live `config.yaml`; use `config.example.yaml`.
- Do not let Agenthon packaging obscure RDTII reviewer discipline: AI suggestions must stay distinct from human-confirmed scores.
- Do not present a profile export as complete unless the sensitive/runtime files are excluded and the repo has been verified after sync.
- Do not capture one-off commit hashes or token-handling details in the main skill body; keep this reference focused on reusable packaging procedure.
