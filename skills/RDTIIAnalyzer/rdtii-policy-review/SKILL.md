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
"source_type": "primary | secondary | secondary_database | reviewer_note"
```

## Legal Document Scraping and Processing Workflow

When scraping or processing legal documents for RDTII evidence, use a reproducible evidence pipeline. Do not rely on ad-hoc page summaries.

### 1. Source discovery

For each indicator, discover candidate sources from:

- official government gazettes and legal databases;
- ministry/regulator websites;
- treaty/agreement repositories;
- required RDTII secondary databases such as WTO I-TIP, Global Trade Alert, WITS/WTO tariff data, V-Dem, TAPED, WIPO Lex, or other guide-named datasets;
- secondary legal reviews only as pointers to primary sources.

Keep a source discovery log with query, URL, access date, and reason for inclusion/exclusion.

### 2. Fetching and preservation

For every document or database result used:

- save the original file where permitted: PDF, HTML, DOCX, XLSX, CSV, JSON, or screenshot if needed;
- store canonical URL, retrieval timestamp, HTTP status, content type, checksum/hash, and file size;
- preserve the original filename and any official document ID, gazette number, act number, regulation number, or database record ID;
- avoid destructive cleaning that prevents later audit.

Recommended metadata:

```json
{
  "source_id": "src_001",
  "url": "https://...",
  "source_type": "primary",
  "issuing_authority": "...",
  "document_type": "law | regulation | guideline | database_record | treaty | circular",
  "retrieved_at": "YYYY-MM-DDTHH:MM:SSZ",
  "http_status": 200,
  "content_type": "application/pdf",
  "checksum_sha256": "...",
  "language": "en",
  "official_reference": "Act 854 / Gazette No. ...",
  "local_path": "..."
}
```

### 3. Text extraction

Use format-appropriate extraction:

- digital PDFs: extract embedded text first;
- scanned PDFs/images: OCR with page numbers preserved;
- HTML: extract main legal text while retaining headings, article numbers, tables, footnotes, and links;
- DOCX/XLSX/CSV: parse structured tables rather than flattening too early;
- database results: export/download raw records where possible.

Always preserve page number, section/article number, heading hierarchy, and table cell coordinates when relevant.

### 4. Normalization

Normalize into structured chunks suitable for legal citation:

```json
{
  "chunk_id": "doc_001_p014_art20_para2",
  "document_id": "doc_001",
  "page": 14,
  "part": "Part IV",
  "section": "20",
  "article": "Article 20",
  "paragraph": "2",
  "heading": "Cross-border transfer",
  "text": "...",
  "language": "en",
  "translation_of": null
}
```

Do not chunk purely by token count if it breaks articles, sections, tables, definitions, or exceptions. Legal meaning often depends on definitions and carve-outs.

### 5. De-duplication and version control

Legal sources often exist in amended, consolidated, unofficial, and historical versions. Record:

- whether text is official, unofficial, consolidated, amended, repealed, draft, or in force;
- effective date and commencement date;
- amendments and repeals;
- relationship between act/regulation/guideline/enforcement rule;
- hierarchy of law: statute → regulation/decree → rule/guideline → decision/notice.

Prefer the version in force for the assessment year. Keep older versions only for change tracking.

### 6. Translation and multilingual handling

Many economies publish binding legal sources only in local languages or non-Latin scripts. Treat multilingual handling as part of the evidence pipeline, not an afterthought.

If the official source is not in English:

- store original text and translated text separately;
- preserve the original script exactly, including diacritics, punctuation, article numbering, legal terms, and formatting;
- record language and script using BCP-47 language tags where possible, e.g. `ms-Latn`, `id-Latn`, `th-Thai`, `km-Khmr`, `lo-Laoo`, `my-Mymr`, `zh-Hans`, `zh-Hant`, `ja-Jpan`, `ko-Kore`, `ar-Arab`, `hi-Deva`, `bn-Beng`, `ru-Cyrl`;
- record translation method: official translation, machine translation, human translation, or reviewer translation;
- cite the original language text as authoritative unless an official English version exists;
- flag uncertain legal terms for reviewer confirmation;
- maintain a terminology glossary for recurring legal concepts such as controller/processor, data transfer, localization, public procurement, licensing, conformity assessment, intermediary, electronic signature, and critical infrastructure.

For non-Latin scripts and complex layouts:

- use OCR engines/models that support the target script; do not assume English OCR works;
- preserve Unicode normalization and avoid lossy transliteration;
- store both original-script text and optional romanization/transliteration only as auxiliary fields;
- handle right-to-left scripts such as Arabic carefully, preserving reading order and article numbering;
- check vertical or mixed writing modes where relevant;
- validate OCR output manually for critical provisions, names of authorities, thresholds, penalties, dates, and exceptions;
- preserve tables in structured form because translated table headers may shift meaning;
- keep screenshots or page images for provisions where OCR confidence is low.

Recommended multilingual chunk shape:

```json
{
  "chunk_id": "doc_001_sec129_para2",
  "document_id": "doc_001",
  "language": "ms",
  "script": "Latn",
  "bcp47": "ms-Latn",
  "original_text": "...",
  "official_translation_text": null,
  "machine_translation_text": "...",
  "translation_method": "machine_translation",
  "romanization": null,
  "ocr_confidence": 0.94,
  "needs_human_translation_review": true,
  "citation": {
    "page": 14,
    "section": "129",
    "paragraph": "2"
  }
}
```

Translation quality rules:

- Do not score from machine translation alone when wording materially affects the score, e.g. `must` vs `may`, `approval` vs `notification`, `prohibited` vs `restricted`, `local storage` vs `local processing`, `license` vs `registration`.
- If a score turns on a translated term, mark the indicator as `provisional` or `needs_reviewer_confirmation`.
- Prefer official bilingual versions when available, but still compare with the original-language legal text if the official translation is marked non-authoritative.
- For countries with multiple official languages, record which language version is authoritative or whether all versions are equally authoritative.

### 7. Measure extraction

Extract concrete regulatory measures, not just document-level themes. A measure should include:

- exact quoted text;
- citation;
- affected entities/sectors;
- obligation/prohibition/condition/exception;
- territorial scope;
- effective status;
- links to definitions and exceptions used to interpret it.

### 8. Quality checks

Before using a document as evidence:

- verify that the source is accessible and official where possible;
- verify the extracted text against the original page/image for critical provisions;
- confirm that citations point to exact article/section/page;
- check whether implementing regulations or guidelines alter the practical obligation;
- record missing pages, OCR confidence issues, blocked pages, or inaccessible attachments.

### 9. Robots, access, and ethics

Respect robots.txt, terms of use, rate limits, and site stability. Prefer official download/export endpoints over brittle scraping. If a site blocks automated access, record the failure and use manual download, public API, or alternative official mirror where lawful.

## Amendment-Aware Corpus Processing

For countries where legal obligations are spread across base laws, amendments, consolidations, regulations, and guidelines, process amendments before scoring. This improves performance because RDTII scoring depends on the law **in force for the assessment year**, not whichever PDF was found first.

Recommended amendment workflow:

1. **Classify each incoming document** as `base_law`, `amendment`, `consolidation`, `repeal`, `guideline`, `implementing_rule`, or `unknown`.
2. **Look up the canonical base law** in a law registry using title, act number, gazette number, issuing authority, and referenced law numbers.
3. If an amendment arrives before its base law, hold it in `pending_base_acquisition` and add the base law to a priority acquisition queue.
4. **Extract amendment scope**: provisions modified, inserted, deleted, repealed, effective date, commencement date, and transition rules.
5. **Merge at provision level**: supersede old provision versions, create new active versions, mark deleted provisions while retaining them for audit.
6. **Rebuild consolidated view** for scoring and flag impacted indicators for re-evaluation.
7. Trigger human review for missing base law, missing intermediate amendment, ambiguous amendment boundaries, repeal, or conflicting gazette/effective dates.

Recommended registry fields:

```json
{
  "law_registry_id": "...",
  "jurisdiction": "TH",
  "canonical_title": "Personal Data Protection Act",
  "official_identifier": "...",
  "source_language": "th",
  "status": "in_force | repealed | partially_repealed | draft | unknown",
  "base_law_source_id": "src_001",
  "current_consolidated_version_id": "ver_012",
  "amendment_chain": ["amd_001", "amd_002"],
  "effective_from": "YYYY-MM-DD"
}
```

## Provision Dependency Graph / Legal GraphRAG

For indicators requiring holistic reading of laws, especially RDTII Pillars 6 and 7, maintain a provision-level dependency graph. This improves retrieval quality because a provision cannot always be interpreted alone: definitions, exceptions, penalties, implementation rules, and cross-references may change its meaning.

Use one graph per jurisdiction/economy. Avoid cross-country dependency edges except for comparative examples; legal dependencies are jurisdiction-specific.

Node types:

- `provision` — article, section, paragraph, sub-clause, table row, schedule item, or definition.
- `document` — law/regulation/guideline/treaty/database record.
- `analyst_annotation` — human interpretive clarification; never treated as primary law.
- `database_record` — WTO I-TIP, Global Trade Alert, V-Dem, TAPED, WITS, etc. where relevant.

Useful edge types:

- `explicit_cross_reference` — textual citation from one provision to another.
- `definition_dependency` — provision uses a term defined elsewhere.
- `exception_condition` — one provision narrows, exempts, or conditions another.
- `penalty_enforcement` — one provision defines consequences or enforcement powers.
- `implementation_detail` — regulation/guideline operationalizes statute.
- `amends_or_repeals` — amendment relationship.
- `legal_clarification` — analyst annotation to provision.
- `database_supports_measure` — structured database record supports a finding.

Edge extraction should combine deterministic and LLM methods:

1. Regex/rule extraction for article references, law numbers, defined terms, dates, and amendment phrases.
2. LLM extraction for implicit exceptions, enforcement dependencies, and multilingual noisy text.
3. Semantic validation with multilingual embeddings against the article/provision index.
4. Add low-confidence edges to human review instead of silently using them.

Suggested semantic thresholds:

```txt
similarity > 0.92       confirmed edge
0.75–0.92               low_confidence edge; include only if needed and flag for review
similarity < 0.75       reject or hold as likely hallucinated reference
```

For amendments, use reverse graph traversal to find impacted provisions and indicators:

```txt
impact_set(changed_provision) = all provisions and scoring contexts with a dependency path to the changed provision
```

Flag the impact set for re-scoring.

## Retrieval and Scoring Context Assembly

For each indicator, retrieve evidence using two complementary signals:

1. **Tag-based retrieval**: query provisions tagged with RDTII topic tags, e.g. `data_localization`, `cross_border_transfer`, `DPO`, `breach_notification`, `cybersecurity`, `intermediary_liability`.
2. **Semantic retrieval**: embed the indicator definition/rubric and search provision embeddings within the jurisdiction.

Union and deduplicate the results, then expand through the dependency graph. Prioritize context by legal role:

1. definitions;
2. candidate scoring provisions;
3. exceptions/conditions;
4. implementing regulations/guidelines;
5. penalties/enforcement;
6. database records required by the guide;
7. analyst annotations last.

Use a bounded token budget and keep a scoring context log containing provision IDs, edge IDs, database record IDs, token count, score, rationale, ambiguity flags, and final reviewer status.

Prefer structured uncertainty over fake confidence numbers:

```json
{
  "ambiguity_flag": true,
  "alternative_interpretation": "...",
  "missing_context": ["implementing regulation for Article 12", "official commencement order"],
  "requires_human_review": true
}
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

## Country/Economy Score Lookup Workflow

When a user asks for an RDTII score for a country/economy, first distinguish two requests:

1. **Official score lookup** — find or verify an existing published RDTII score or scorecard.
2. **Score computation** — calculate/estimate from indicator-level policy evidence.

Do not invent an overall score if only the methodology guide is available. The guide may contain examples mentioning an economy without containing that economy's completed scorecard. If the official score cannot be verified, say so and offer to compute from indicator data, policy documents, or one pillar at a time.

For session-specific notes and a reusable response shape, see `references/country-score-checks.md`.

## Hackathon / Agenthon Packaging Context

When packaging an RDTII Hermes Agent such as Mahoraga for **RISTEK x Build Club OpenClaw Agenthon 2026**, apply the guideline summaries in `references/openclaw-agenthon-technical-guidelines.md` and `references/agenthon-compliance-checklist.md`.

Key implications:

- Position the project as an autonomous AI Agent or Multi-Agent System, not a basic chatbot wrapper.
- Demonstrate reasoning, decision-making, tool usage, workflow execution, and an autonomous loop completing at least one RDTII task end-to-end.
- Keep README instructions reproducible for judges.
- Make clear that the unique domain skill lives under `skills/RDTIIAnalyzer/`; other skills are bundled Hermes skills.
- For demos/decks, emphasize agent autonomy, RDTII evidence extraction/mapping/scoring workflow, and human-review safeguards.

## Reviewer Workflow

For any country/economy, do **not** produce a final RDTII score from high-level pillar impressions. The guideline-compliant workflow is indicator-level:

```txt
Identify economy + assessment year
   ↓
Load RDTII 2.1 guide / scoring rubric
   ↓
Create complete checklist of all pillars and indicators
   ↓
For each indicator, identify required source type/database
   ↓
Collect evidence from primary sources and required secondary databases
   ↓
Score each indicator according to its exact rule
   ↓
Apply indicator weights within each pillar
   ↓
Calculate each weighted pillar score
   ↓
Average the 12 pillar scores equally
   ↓
Label every result as verified / provisional / missing / needs reviewer confirmation
```

Important: A pillar-level estimate may be useful for scoping, but must be explicitly labeled as **rough provisional estimate** and not as a formal RDTII score.

## Required Source Discipline by Indicator Type

Use the RDTII guide to determine the source for each indicator. Typical source classes include:

- **Tariffs / ICT goods:** WTO tariff profile, WITS, UN Comtrade where needed, WTO ITA I/II membership, ITA III product list from the guide/ITIF, official customs tariff schedules.
- **Trade defence:** WTO I-TIP, WTO trade remedy databases, Global Trade Alert, and official national trade-remedy notices.
- **Public procurement:** WTO GPA party/observer status, official procurement laws, treasury circulars, e-procurement portals, FTA/CPTPP procurement schedules where applicable.
- **Foreign investment:** official investment laws, negative lists, sector regulators, licence conditions, FTA reservations, investment screening rules.
- **IP rights:** WIPO Lex, official IP office, treaty membership, copyright/patent/trademark statutes, enforcement rules.
- **Telecommunications:** telecom law, regulator licensing pages, access/interconnection rules, spectrum/licence conditions, competition authority materials.
- **Cross-border data:** data protection law, cross-border transfer rules/guidelines, data localization laws, sector-specific data rules, TAPED or official trade agreement text for data-flow commitments.
- **Domestic data/cyber/privacy:** data protection law, cybersecurity law, breach/DPO/processor/retention rules, regulator guidance.
- **Internet intermediary liability:** platform laws, safe-harbour provisions, notice-and-takedown rules, online safety laws, content regulator guidance.
- **Content access:** content-blocking/filtering rules, online safety law, platform licensing, V-Dem where the RDTII guide requires it, regulator orders/reports.
- **Non-technical NTMs:** WTO I-TIP, Global Trade Alert, UNCTAD TRAINS if relevant, official import/licensing restrictions, sector licensing rules.
- **Standards/procedures:** technical standards, conformity assessment, type approval, testing/labelling rules, regulator/certification body requirements, mutual-recognition agreements.
- **Online sales/transactions:** e-commerce law, e-signature/e-transaction law, consumer protection e-commerce rules, payment-services regulation, delivery/logistics requirements.

Secondary sources such as WTO I-TIP, Global Trade Alert, V-Dem, TAPED, legal reviews, or news are often required to locate measures or external scores, but final legal evidence should be traced back to primary sources whenever possible.

## Indicator Evidence Record

For each indicator, maintain this record shape:

```json
{
  "economy": "MYS",
  "assessment_year": 2026,
  "framework": "RDTII 2.1",
  "pillar_id": "P1",
  "indicator_code": "1.1",
  "indicator_name": "...",
  "required_sources": ["WITS", "WTO tariff profile", "official customs tariff schedule"],
  "source_queries_performed": [
    {
      "source": "WTO I-TIP",
      "query": "economy=Malaysia; product_scope=ICT goods; measure=trade defence",
      "date_accessed": "YYYY-MM-DD",
      "result_summary": "..."
    }
  ],
  "primary_evidence": [
    {
      "source_type": "primary",
      "title": "...",
      "url": "...",
      "citation": "article/section/page/table",
      "quoted_text": "..."
    }
  ],
  "secondary_evidence": [
    {
      "source_type": "secondary_database",
      "name": "Global Trade Alert",
      "url": "...",
      "record_id": "...",
      "finding": "..."
    }
  ],
  "score": null,
  "score_status": "missing | provisional | verified | reviewer_confirmed",
  "rationale": "...",
  "uncertainty": "low | medium | high",
  "missing_evidence": ["..."]
}
```

## Reviewer Workflow

Recommended product workflow:

```txt
Upload source document / choose economy
   ↓
OCR / text extraction
   ↓
Chunk document by article/section
   ↓
Generate complete RDTII indicator checklist
   ↓
For each indicator, fetch/query required primary and secondary sources
   ↓
AI suggests regulatory measures and indicator mappings
   ↓
Reviewer accepts/rejects mappings
   ↓
AI suggests indicator score + rationale + evidence status
   ↓
Reviewer confirms final indicator score
   ↓
System calculates weighted pillar scores
   ↓
System calculates country/economy RDTII score
   ↓
Export audit report with evidence table and source-query log
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

2. **Scoring a provision in isolation.** For legal indicators, especially data flow, privacy, cybersecurity, and intermediary liability, retrieve definitions, exceptions, implementing rules, penalties, and cross-references before scoring.

3. **Ignoring amendments and consolidated versions.** Always determine the law in force for the assessment year. A recent amendment may change an indicator even if the original provision text still appears in older PDFs.

4. **Trusting LLM-extracted graph edges without validation.** Validate cross-references against an article/provision index with deterministic parsing and multilingual semantic matching. Low-confidence edges should be reviewed.

5. **Using arbitrary token chunks that break legal meaning.** Chunk by legal hierarchy: part, chapter, article, paragraph, sub-clause, table row, schedule. Keep definitions and exceptions reachable.

2. **Producing a final score from pillar-level impressions.** Formal RDTII scoring must be indicator-level. If only pillar-level evidence was reviewed, label the result as a rough provisional estimate.

3. **Skipping required databases.** Some indicators require structured sources such as WTO I-TIP, Global Trade Alert, WITS, WTO tariff/trade remedy data, V-Dem, TAPED, or official agreement schedules. Do not replace these with generic web search when the guide names a specific source.

4. **Using secondary sources as final legal evidence.** Secondary sources should normally guide reviewers to primary sources, although database-derived indicators may legitimately cite the database output as part of the evidence record.

5. **Forcing one measure to one indicator.** Cross-cutting measures may map to multiple indicators.

6. **Letting AI finalize scores.** Keep `ai_suggested_score`, `reviewer_score`, and `final_score` separate.

7. **Dropping citations or source-query logs.** Every final score should have traceable legal evidence and a record of which required databases were queried.

8. **Ignoring de jure/de facto gaps.** Note when the law says one thing but implementation, discretion, or institutional opacity may affect interpretation.

9. **Failing to preserve null/unknown states.** Unknown evidence should not be silently treated as score `0`.

## Verification Checklist

Before finalizing an RDTII answer or design:

- [ ] Did I identify the relevant pillar(s)?
- [ ] Did I build or reference the complete indicator checklist, not just pillars?
- [ ] Did I identify the required source/database for each indicator?
- [ ] Did I query named sources where the guide requires them, such as WTO I-TIP, Global Trade Alert, WITS/WTO tariff data, V-Dem, TAPED, or official legal databases?
- [ ] Did I distinguish primary from secondary sources?
- [ ] Did I preserve original fetched documents or database exports where permitted?
- [ ] Did I store URL, retrieval timestamp, source type, issuing authority, document version/status, and checksum/file metadata?
- [ ] Did I preserve exact citations, page numbers, article/section hierarchy, tables, definitions, exceptions, and quotes where available?
- [ ] Did I verify extracted/OCR text against the original document for critical provisions?
- [ ] Did I log source queries and access dates for database-derived evidence?
- [ ] Did I handle multilingual/non-Latin-script sources with script-aware OCR/extraction, BCP-47 language tags, original-script preservation, and translation review where legal meaning affects scoring?
- [ ] Did I handle translations by storing original and translated text separately and flagging uncertain terms?
- [ ] Did I allow one measure to map to multiple indicators?
- [ ] Did I separate AI suggestion from human reviewer confirmation?
- [ ] Did I avoid describing the score as policy quality/desirability?
- [ ] Did I explain uncertainty and missing evidence?
- [ ] Did I identify amendments, consolidations, repeals, commencement dates, and the version in force for the assessment year?
- [ ] Did I retrieve definitions, exceptions, implementing rules, penalties, and cross-references before scoring legally dependent provisions?
- [ ] Did I validate LLM-extracted cross-reference/dependency edges against a provision index or multilingual embeddings before relying on them?
- [ ] Did I log the exact scoring context: provision IDs, dependency IDs, database records, token count, rationale, ambiguity fields, and final score source?
- [ ] Did I route genuine ambiguity to human review using `ambiguity_flag`, `alternative_interpretation`, and `missing_context` rather than inventing confidence numbers?
- [ ] Did I calculate composite scores as weighted indicators within pillars and simple average across 12 pillars?
- [ ] If the result is only pillar-level or missing required database checks, did I label it clearly as a rough provisional estimate rather than a formal score?
