# Japan 2025 RDTII Evidence Report — Session Artifact

This file documents the evidence gathered during the 2026-05-15 session for Japan (assessment year 2025). 

## What was attempted

- **12-pillar checklist created**: weights loaded from RDTII 2.1 skill
- **3 parallel subagents dispatched**: data/cross-border, telecom/platforms, trade/FDI/e-commerce
- **Primary source verified**: APPI (Act on Protection of Personal Information) Article 24 — cross-border data transfers — downloaded from official PPC PDF: https://www.ppc.go.jp/files/pdf/APPI_english.pdf
- **APPI Articles 23, 24 extracted** with exact legal text: consent required for third-party provision and cross-border transfers, with adequacy (EEA, UK) and equivalent-system (APEC CBPR) exceptions. No general data localization requirement.

## What was blocked

| Database | Issue |
|----------|-------|
| TAPED | Cloudflare block |
| Singapore SSO | CloudFront 403 |
| METI websites | Timeout |
| Global Trade Alert | Not attempted (subagent had no web tools) |
| V-Dem | Not attempted |
| WIPO Lex | Not attempted |

## Key legal findings (Japan)

### Pillar 6 — Cross-border data policies
- **APPI Article 24(1)**: Prior consent required for cross-border data provision to third parties in foreign countries
- **Exceptions**: Adequacy countries (EEA, UK) and equivalent systems (APEC CBPR, PPC Rules)
- **Article 24(2)**: Information obligation — must inform data subject about foreign protection system
- **Article 24(3)**: Ongoing compliance monitoring for equivalent-system transfers
- **No general data localization** in APPI (sector-specific only: Banking Act, Medical Care Act)
- **Suggested scores**: P6_I1 = 0.50, P6_I3 = 0.10 (provisional, needs reviewer confirmation)

### Pillar 7 — Domestic data protection
- APPI Chapters IV (Articles 15–35): comprehensive obligations including purpose specification, consent, security measures, third-party limits, data subject rights
- 2023 amendments effective April 2025: business suspension orders, mandatory breach notification, increased penalties

## Report output
Full report (`requires_human_review: true`): `/home/ubuntu/outputs/japan-rdtii-evidence-report.md`
Demo pipeline for P6: `/home/ubuntu/outputs/demo-singapore-rdtii-pipeline.md`
