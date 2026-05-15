# RDTII Country Score Checks

Use this reference when a user asks for an RDTII score for a specific economy/country.

## Workflow

1. Treat the request as potentially asking for either:
   - an existing official/published RDTII score; or
   - a fresh calculation/estimate from indicator-level policy evidence.
2. Check whether the provided RDTII guide or local project documents include a completed scorecard/database for the economy. The RDTII guide may describe methodology without containing country scorecards.
3. If an official dataset cannot be verified, do **not** invent an overall score. State that the score is not verified from available sources and offer to compute it from indicator-level data or policy documents.
4. For a computation request, ask for or gather evidence by pillar/indicator and keep outputs in reviewer-assist mode: candidate pillar, indicator, score, evidence, rationale, confidence, and human-review status.
5. Preserve the distinction between methodology evidence and actual economy score evidence.

## Malaysia session note

In the session where the user asked to check Malaysia's RDTII score, the available RDTII 2.1 guide contained methodology and a few Malaysia examples, but not a complete Malaysia scorecard. The correct handling was to avoid fabricating a final Malaysia score and instead offer to start with a pillar or ingest Malaysia-specific policy documents / indicator datasets.

## Recommended response shape

```json
{
  "economy": "Malaysia",
  "score_status": "not_verified_from_available_sources",
  "available_evidence": "methodology guide only; no full scorecard located in provided material",
  "next_steps": [
    "provide completed indicator dataset",
    "provide Malaysia policy documents",
    "choose a pillar to score first"
  ],
  "human_review_required": true
}
```
