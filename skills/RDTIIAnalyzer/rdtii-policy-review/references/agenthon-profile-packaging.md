# Agenthon Profile Packaging Notes

Use these notes when packaging or refreshing an RDTII Hermes profile for RISTEK x Build Club OpenClaw Agenthon submissions.

## Durable workflow learned

When the user asks to make the RDTII profile compliant with OpenClaw Agenthon requirements, treat the profile directory itself as the agent artifact, not merely documentation.

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
   - profile `README.md` explaining the agent as a domain-specific Hermes Agent for RDTII;
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

- The agent is a domain-specific Hermes Agent for the Regional Digital Trade Integration Index (RDTII).
- The unique domain skill is under `skills/RDTIIAnalyzer/`.
- Other skills are bundled Hermes skills, not the submission's unique RDTII contribution.
- RDTII outputs are policy research assistance requiring expert review, not legal advice.
- The demo should show tool use and artifact generation, not only chat responses.

## Profile Rename Workflow

When the user asks to rename a Hermes Agent profile (e.g., from a codename to a project name), there is a systematic set of files to update. The rename must be consistent across all layers of the profile. This pattern was learned from a full Mahoraga → RDTII Framework Agent rename across 15+ files.

### What to update — complete checklist

1. **SOUL.md** — agent persona identity (`You are <Name>, a domain-specific Hermes Agent for RDTII.`)
2. **README.md** — full rewrite: project name, positioning, judging criteria table, architecture description
3. **memories/USER.md** — profile reference in user preferences
4. **memories/MEMORY.md** — any memory entries that reference the old name
5. **references/*.md** — all reference files in the profile root (agenthon-compliance-checklist, openclaw-agenthon-technical-guidelines, etc.)
6. **skills/<Category>/<Skill>/SKILL.md** — the main skill's "Hackathon / Agenthon Packaging Context" section
7. **skills/<Category>/<Skill>/references/*.md** — all skill reference files (agenthon-profile-packaging, agenthon-compliance-checklist, openclaw-agenthon-guidelines, australia-2025-scorecard, etc.)
8. **examples/*.md** — demo prompts that reference the agent by name
9. **outputs/*.md** — any sample reports with agent-name attribution in disclaimers

### Execution pattern

```txt
1. Search for the old name across the entire repo: `git grep -i <oldname>`
2. For each match, classify: rename-safe (branding) vs. reference (repo URL stays)
3. Work the list above top-to-bottom to avoid missed files
4. After patching, re-search to confirm zero remaining references (except repo URL)
5. Add -A, commit with comprehensive message listing every file touched
```

### Pitfalls when renaming

- **Repo URL names**: the GitHub repository name (e.g., `OpenClaw-Agenthon_Mahoraga`) cannot be changed without GitHub API/admin access. It is OK to leave the URL in the README as-is — judges do not penalize repo name mismatch with project name.
- **Cross-file consistency**: a rename that misses even one reference file creates confusion. Always do a full grep sweep after the last patch.
- **Skill SKILL.md is version-controlled separately from the profile repo**: the live profile at `~/.hermes/profiles/<name>/` and the GitHub repo copy are independent. Rename both, or users pulling the repo for the first time will get the old name in the skill.
- **memories/MEMORY.md is ephemeral**: update it in the live profile when renaming, but do NOT commit it to the repo — it's a runtime file excluded by `.gitignore`.

## Pitfalls

- Do not publish the live `config.yaml`; use `config.example.yaml`.
- Do not let Agenthon packaging obscure RDTII reviewer discipline: AI suggestions must stay distinct from human-confirmed scores.
- Do not present a profile export as complete unless the sensitive/runtime files are excluded and the repo has been verified after sync.
- Do not capture one-off commit hashes or token-handling details in the main skill body; keep this reference focused on reusable packaging procedure.