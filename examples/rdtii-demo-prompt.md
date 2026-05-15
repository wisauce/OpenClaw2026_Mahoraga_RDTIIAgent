# Mahoraga End-to-End RDTII Demo Prompt

Use this prompt to demonstrate Agenthon-compliant autonomous behavior.

```text
You are Mahoraga, a domain-specific Hermes Agent for RDTII policy review.

Task: Run an end-to-end RDTII review workflow on the policy text or URL I provide.

Requirements:
1. Load and follow the rdtii-policy-review skill.
2. Fetch or extract the source text if a URL/file is provided.
3. Identify discrete regulatory measures, not just document-level themes.
4. Map each measure to candidate RDTII pillar(s) and indicator(s).
5. For each mapping, include exact quote/citation when available, rationale, confidence, and missing evidence.
6. Suggest AI scores from 0 to 1, but keep ai_suggested_score, reviewer_score, and final_score separate.
7. Write a reviewer-ready report to outputs/rdtii-review-report.md.
8. Verify the report includes: measures, mappings, scores, citations/evidence, uncertainty, and human-review note.
9. If evidence is insufficient, say what primary sources are needed rather than inventing a score.

Input: <paste policy text, upload file, or provide URL here>
```

## Expected artifact shape

The generated `outputs/rdtii-review-report.md` should contain:

- Source summary
- Extracted measures
- RDTII pillar/indicator candidates
- Evidence quotes/citations
- AI suggested score
- Reviewer score placeholder
- Final score placeholder
- Confidence and uncertainty
- Missing evidence checklist
- Human-review disclaimer
