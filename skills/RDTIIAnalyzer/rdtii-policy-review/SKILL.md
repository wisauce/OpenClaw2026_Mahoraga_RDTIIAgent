---
name: rdtii-policy-review
description: Use when helping with RDTII 2.1 digital trade policy review systems, mapping legal/regulatory measures to RDTII pillars and indicators, scoring reviewer assessments, designing schemas, or auditing evidence for UN Regional Digital Trade Integration Index workflows.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [rdtii, digital-trade, compliance, policy-review, scoring, schema]
    related_skills: [ocr-and-documents, google-workspace]
---

# RDTII Policy Review

## Overview

Use this skill for tasks involving the **Regional Digital Trade Integration Index (RDTII) 2.1** and digital trade policy review workflows. The user's project helps law/compliance policy reviewers map digital trade laws, regulations, and official policy measures to RDTII pillars, indicators, and scores.

RDTII scores range from **0 to 1** and should be interpreted as indicators of regulatory characteristics and compliance-cost implications, **not** as a direct judgment of policy quality, effectiveness, or desirability. A score closer to `1` generally indicates a more extensive, restrictive, complex, or less interoperable regulatory environment for digital trade; a score closer to `0` generally indicates lower compliance cost or fewer captured restrictions.

## When to Use

Use this skill when the user asks to:

- Design or implement an RDTII scoring workflow or product.
- Map policy/legal text to RDTII pillars or indicators.
- Create a data model, database schema, JSON schema, or API for RDTII review.
- Build reviewer workflows for accepting/rejecting AI mappings and scores.
- Interpret RDTII scores, pillars, or methodology.
- Extract measures from laws, regulations, decrees, official guidelines, government reports, or secondary legal sources.
- Produce audit trails, evidence records, scorecards, or country/economy reports for RDTII.

Do **not** use this skill as a substitute for legal advice. Treat outputs as policy research assistance requiring human expert review.

## RDTII 2.1 Core Methodology

RDTII 2.1 evaluates the regulatory environment affecting digital trade businesses using **12 policy pillars**. Each pillar contains indicators that capture relevant measures in that policy area.

Calculation pattern:

1. Score each indicator from `0` to `1`.
2. Apply the indicator's weight within its pillar.
3. Compute each pillar score as a weighted average of its indicators.
4. Compute the overall RDTII score as a **simple average of the 12 pillar scores**.

Interpretation:

- `0`: low compliance cost / low captured restriction.
- `1`: high compliance cost / high captured restriction.
- Higher scores may result from administrative complexity, differential treatment, or lack of interoperability with recognized international norms.

Important caution:

- The score reflects the **presence and characteristics** of digital trade policy measures.
- It does **not** directly measure whether a regulation is good, bad, effective, or desirable.
- Policy implications must be evaluated case-by-case.

## The 12 Pillars

Use these pillar names as stable product reference data:

1. **Tariffs and trade defence** — tariffs and trade defence measures applied to ICT goods in regional trade.
2. **Public procurement** — participation rules for procurement of ICT goods and digital services.
3. **Foreign direct investment** — investment restrictions in sectors related to digital trade.
4. **Intellectual property rights** — IP frameworks, protection, innovation, copyright, patents, and trade secrets.
5. **Telecommunications regulations and competition** — telecom infrastructure, market access, competition, and regulator independence.
6. **Cross-border data policies** — data flows, data localization, local processing, privacy-related transfer conditions, and cross-border governance.
7. **Domestic data protection and privacy** — domestic privacy, data protection, retention, and cybersecurity measures.
8. **Internet intermediary liability** — safe harbour, liability frameworks, notice-and-takedown, and intermediary obligations.
9. **Content access** — blocking/filtering, shutdowns, licensing for digital content/providers, and illegal content measures.
10. **Non-technical NTMs** — non-technical non-tariff measures affecting ICT goods and digital services.
11. **Standards and procedures** — technical standards and conformity assessment procedures relevant to digital trade.
12. **Online sales and transactions** — e-commerce, electronic signatures, payments, delivery, consumer protection, and online transaction rules.

## Known Pillar Indicator Weights

When constructing seed data, use these weights where available from the RDTII 2.1 guide. Normalize and verify against the primary guide before production use.

```json
[
  {"pillar_id":"P1","name":"Tariffs and trade defence","known_weights":[0.40,0.32,0.08,0.20]},
  {"pillar_id":"P2","name":"Public procurement","known_weights":[0.40,0.32,0.20,0.08]},
  {"pillar_id":"P3","name":"Foreign direct investment","known_weights":[0.34,0.08,0.07,0.17,0.34]},
  {"pillar_id":"P4","name":"Intellectual property rights","known_weights":"verify indicator-level details from guide"},
  {"pillar_id":"P5","name":"Telecommunications regulations and competition","known_weights":[0.15,0.29,0.15,0.15,0.15,0.06,0.06]},
  {"pillar_id":"P6","name":"Cross-border data policies","known_weights":[0.38,0.12,0.31,0.12,0.08]},
  {"pillar_id":"P7","name":"Domestic data protection and privacy","known_weights":[0.31,0.31,0.16,0.06,0.16]},
  {"pillar_id":"P8","name":"Internet intermediary liability","known_weights":[0.25,0.25,0.25,0.25]},
  {"pillar_id":"P9","name":"Content access","known_weights":[0.33,0.33,0.13,0.21]},
  {"pillar_id":"P10","name":"Non-technical NTMs","known_weights":[0.42,0.21,0.21,0.17]},
  {"pillar_id":"P11","name":"Standards and procedures","known_weights":[0.20,0.20,0.30,0.30]},
  {"pillar_id":"P12","name":"Online sales and transactions","known_weights":[0.22,0.11,0.11,0.07,0.07,0.07,0.07,0.07,0.04,0.04,0.04,0.04,0.04]}
]
```

## Recommended Product Data Model

Separate five layers:

1. **RDTII framework definition** — framework, pillars, indicators, scoring rules.
2. **Source legal/policy documents** — uploaded primary and secondary sources.
3. **Extracted regulatory measures** — provisions or policy measures extracted from documents.
4. **Reviewer scoring decisions** — AI suggestions, human confirmation, rationale, evidence.
5. **Computed economy score** — indicator scores, pillar scores, overall score, coverage.

Core relationship:

```txt
RDTIIFramework
 └── Pillar
      └── Indicator
           └── ScoringRule

Economy
 └── PolicyDocument
      └── ExtractedMeasure
           └── IndicatorMapping
                └── ReviewerAssessment
                     └── Evidence
```

## Minimum Database Tables

For an MVP, use:

```txt
pillars
indicators
documents
measures
mappings
assessments
scorecards
```

For a fuller production system, use:

```txt
rdtii_frameworks
rdtii_pillars
rdtii_indicators
rdtii_scoring_rules

economies
policy_documents
document_chunks

regulatory_measures
measure_indicator_mappings
reviewer_assessments
assessment_evidence
assessment_notes

scorecards
pillar_scores
indicator_scores

users
review_assignments
audit_logs
```

## Source Document Rules

RDTII review should prioritize **primary sources**:

- official gazettes;
- statutes/laws;
- regulations;
- decrees;
- enforcement rules;
- official government guidelines;
- official government reports;
- treaty/agreement texts;
- regulator decisions or official notices.

Secondary sources such as legal reviews, news, databases, and publications should be used only to guide researchers toward primary sources unless the user explicitly says otherwise.

Model source type explicitly:

```json
"source_type": "primary | secondary | reviewer_note"
```

## Measure Extraction Rules

A regulatory measure should capture a specific legal or policy requirement, not just a whole document. Store exact quoted text and citation.

Recommended measure fields:

```json
{
  "measure_id": "measure_001",
  "document_id": "doc_001",
  "economy_id": "IDN",
  "title": "Requirement to process certain personal data domestically",
  "summary": "The law requires certain categories of personal data to be processed or stored within national territory.",
  "legal_text": "Exact quoted provision goes here.",
  "citation": {
    "article": "Article 20",
    "section": null,
    "paragraph": "2",
    "page": 14
  },
  "measure_type": "data_localization",
  "affected_policy_area": ["cross_border_data", "data_protection"],
  "affected_entities": ["foreign_service_providers", "domestic_service_providers", "data_controllers", "data_processors"],
  "affected_sectors": ["digital_services", "online_services", "cloud_services"],
  "territorial_scope": "national",
  "status": "in_force",
  "effective_date": "2022-10-17",
  "mappings": []
}
```

## Mapping Rules

A single measure can map to multiple indicators. Do not force one measure to only one indicator.

Example: a licensing law for digital platforms may map both to content/application provider licensing and to e-commerce licensing.

Mapping statuses:

```txt
suggested
accepted
rejected
needs_more_evidence
superseded
```

Recommended mapping fields:

```json
{
  "mapping_id": "mapping_001",
  "measure_id": "measure_001",
  "pillar_id": "P6",
  "indicator_id": "P6_I1",
  "indicator_code": "6.1",
  "mapping_confidence": 0.87,
  "mapping_status": "suggested",
  "mapped_by": "ai",
  "reviewed_by": null,
  "rationale": "The measure appears to restrict cross-border data processing by requiring domestic processing or storage.",
  "possible_alternative_indicators": [
    {
      "indicator_id": "P7_I1",
      "reason": "The same law may also relate to domestic data protection requirements."
    }
  ]
}
```

## Reviewer Assessment Rules

For legal/compliance use, AI should not silently finalize a score. Separate suggestion from human-confirmed result:

```json
{
  "ai_suggested_score": 0.75,
  "reviewer_score": 0.5,
  "final_score": 0.5,
  "finalized_by": "human_reviewer"
}
```

Assessment status values:

```txt
draft
reviewer_confirmed
finalized
```

Recommended fields:

```json
{
  "assessment_id": "assessment_001",
  "mapping_id": "mapping_001",
  "economy_id": "IDN",
  "framework_id": "rdtii_2_1",
  "indicator_id": "P6_I1",
  "ai_suggested_score": 0.75,
  "reviewer_score": 0.5,
  "final_score": 0.5,
  "score_status": "reviewer_confirmed",
  "confidence": "medium",
  "rationale": "The measure imposes conditions on cross-border transfer but does not appear to amount to a full ban.",
  "evidence": [
    {
      "evidence_id": "ev_001",
      "document_id": "doc_001",
      "measure_id": "measure_001",
      "citation": "Article 20(2)",
      "quoted_text": "Exact legal text...",
      "translation": "English translation if needed.",
      "source_type": "primary"
    }
  ]
}
```

## Scorecard Calculation

For an economy scorecard:

1. Compute each indicator score from the finalized assessment.
2. Multiply by `weight_within_pillar`.
3. Sum weighted indicators to get pillar score.
4. Average all 12 pillar scores to get the overall score.

Recommended scorecard fields:

```json
{
  "scorecard_id": "scorecard_IDN_2026_rdtii_2_1",
  "economy_id": "IDN",
  "framework_id": "rdtii_2_1",
  "assessment_year": 2026,
  "status": "draft",
  "pillar_scores": [
    {
      "pillar_id": "P6",
      "pillar_number": 6,
      "pillar_name": "Cross-border data policies",
      "pillar_score": 0.42,
      "calculation_method": "weighted_average_of_indicators",
      "indicator_scores": [
        {
          "indicator_id": "P6_I1",
          "indicator_code": "6.1",
          "indicator_score": 0.5,
          "indicator_weight": 0.38,
          "weighted_score": 0.19,
          "assessment_id": "assessment_001"
        }
      ]
    }
  ],
  "overall_score": 0.36,
  "overall_calculation_method": "simple_average_of_12_pillar_scores",
  "coverage": {
    "total_indicators": 0,
    "scored_indicators": 0,
    "missing_indicators": 0,
    "needs_review": 0
  }
}
```

## Reviewer Workflow

Recommended workflow:

```txt
Upload source document
   ↓
OCR / text extraction
   ↓
Chunk document by article/section
   ↓
AI suggests regulatory measures
   ↓
AI maps measures to pillar + indicator
   ↓
Reviewer accepts/rejects mapping
   ↓
AI suggests score + rationale
   ↓
Reviewer confirms final score
   ↓
System calculates pillar score
   ↓
System calculates country/economy RDTII score
   ↓
Export audit report
```

## Scoring Rule Types to Support

Design scoring infrastructure to support:

- `binary` — score is `0` or `1`.
- `ordinal` — score is selected from allowed values such as `0`, `0.25`, `0.5`, `0.75`, `1`.
- `continuous` — score can be any numeric value between `0` and `1`.
- `formula` — score is calculated from inputs, e.g. tariffs.
- `external_dataset` — score is imported or derived from a dataset.
- `membership_based` — score depends on treaty/agreement membership or adoption of model laws.

Example formula for tariffs:

```json
{
  "rule_type": "formula",
  "formula": "min(1, 0.1 * weighted_average_tariff_rate)",
  "input_fields": [
    {
      "field": "weighted_average_tariff_rate",
      "type": "number",
      "unit": "percent"
    }
  ],
  "notes": "If average tariff rate is above 10%, score is capped at 1."
}
```

## AI Output Rules

When assisting with RDTII mapping or scoring, always include:

- pillar and indicator candidate;
- exact source quote or citation if available;
- rationale;
- suggested score;
- uncertainty/confidence;
- missing evidence or follow-up needed;
- note that human reviewer confirmation is required.

Avoid unsupported legal conclusions. If primary legal text is unavailable, say so explicitly.

## Common Pitfalls

1. **Treating RDTII as a policy quality score.** It is a measure of regulatory characteristics and compliance-cost implications, not a direct good/bad score.

2. **Using secondary sources as final evidence.** Secondary sources should normally guide reviewers to primary sources.

3. **Forcing one measure to one indicator.** Cross-cutting measures may map to multiple indicators.

4. **Letting AI finalize scores.** Keep `ai_suggested_score`, `reviewer_score`, and `final_score` separate.

5. **Dropping citations.** Every final score should have traceable legal evidence.

6. **Ignoring de jure/de facto gaps.** Note when the law says one thing but implementation, discretion, or institutional opacity may affect interpretation.

7. **Failing to preserve null/unknown states.** Unknown evidence should not be silently treated as score `0`.

## Verification Checklist

Before finalizing an RDTII answer or design:

- [ ] Did I identify the relevant pillar(s)?
- [ ] Did I distinguish primary from secondary sources?
- [ ] Did I preserve exact citations and quotes where available?
- [ ] Did I allow one measure to map to multiple indicators?
- [ ] Did I separate AI suggestion from human reviewer confirmation?
- [ ] Did I avoid describing the score as policy quality/desirability?
- [ ] Did I explain uncertainty and missing evidence?
- [ ] Did I calculate composite scores as weighted indicators within pillars and simple average across 12 pillars?
