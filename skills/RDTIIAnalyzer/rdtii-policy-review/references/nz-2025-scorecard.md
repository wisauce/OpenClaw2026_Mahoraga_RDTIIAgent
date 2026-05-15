# New Zealand 2025 — Full RDTII Scorecard (RDTII Agent Pipeline)

**Economy:** New Zealand
**Assessment year:** 2025
**Pipeline run:** Autonomous Hermes Agent (RDTII Agent, Team Mahoraga) — 4 parallel research subagents + live source verification
**Overall score:** **0.18** (provisional)
**Date:** 2026-05-15

---

## How this scorecard was produced

1. Economy + year identified: New Zealand, 2025
2. RDTII 2.1 scoring rubric loaded (12 pillars, known indicator weights)
3. Required databases attempted: WTO I-TIP ✅, Global Trade Alert ✅, WIPO Lex ✅, TAPED ❌ (Cloudflare)
4. Source access: legislation.govt.nz ✅ fully accessible — 5+ live laws verified via browser
5. Parallel research launched: 4 subagents covering all 12 pillars
6. Subagent findings verified against live primary sources
7. **Key correction applied:** Electronic Transactions Act 2002 is **Repealed** — replaced by Contract and Commercial Law Act 2017 Part 3 (ss 202-234). The P12 subagent cited the repealed Act; corrected after live verification.
8. Scores assigned per pillar, overall = simple average of 12 pillar scores

---

## Database Query Log

| Source | Status | Notes |
|--------|--------|-------|
| WTO I-TIP | ✅ Accessible | NZ in dropdown; trade defence data queryable |
| Global Trade Alert | ✅ Accessible | Via curl with browser UA |
| WIPO Lex | ✅ Accessible | NZ searchable; treaty membership verified |
| TAPED (UN ESCAP) | ❌ Blocked | Cloudflare challenge |
| legislation.govt.nz | ✅ Fully accessible | 5+ laws verified live in browser |
| Privacy Commissioner NZ | ✅ Accessible | Guidance documents available |

---

## Per-Pillar Scores

| Pillar | Score | Primary Evidence Source | Status |
|--------|-------|------------------------|--------|
| P1 — Tariffs & trade defence | **0.05** | WTO ITA/ITA-2 member; Customs and Excise Act 2018 | ✅ Verified |
| P2 — Public procurement | **0.05** | WTO GPA party (2014); Government Procurement Rules 2019 | ✅ Verified |
| P3 — Foreign direct investment | **0.15** | Overseas Investment Act 2005 (2021 amendments) | ✅ Verified |
| P4 — Intellectual property rights | **0.20** | Copyright Act 1994; Patents Act 2013; Trade Marks Act 2002 | ✅ Verified |
| P5 — Telecommunications | **0.15** | Telecommunications Act 2001; 2018 Amendment Act | ✅ Verified |
| P6 — Cross-border data | **0.35** | Privacy Act 2020 — IPP 12; Part 4 transfer rules | ✅ Verified |
| P7 — Data protection | **0.35** | Privacy Act 2020 — 13 IPPs; Part 6 breach notification | ✅ Verified |
| P8 — Intermediary liability | **0.30** | Copyright Act ss92A-92H; HDCA 2015; Films Act s124 | ✅ Verified |
| P9 — Content access | **0.30** | HDCA 2015; Films Act s124; Telecom Act TSO/UFB | ✅ Verified |
| P10 — Non-technical NTMs | **0.05** | No ICT quotas/LCRs/bans; full TFA implementation | ✅ Verified |
| P11 — Standards | **0.10** | Standards and Accreditation Act 2015; ISO/IEC adoption | ✅ Verified |
| P12 — Online sales | **0.15** | Contract and Commercial Law Act 2017 Part 3; FTA 1986; CGA 1993 | ✅ Verified (corrected: ETA → CCLA) |

**Overall score: 0.18** (simple average of 12 pillar scores)

---

## Key Findings Summary

- **Most restrictive pillars:** P6 (cross-border data — 0.35) and P7 (data protection — 0.35) due to IPP 12 transfer restrictions, no adequacy findings, modest enforcement
- **Least restrictive pillars:** P1 (tariffs — 0.05), P2 (procurement — 0.05), P10 (NTMs — 0.05) due to ITA membership, GPA adherence, open trade
- **Overall:** Very open digital trade environment (0.18), consistent with developed economy status and extensive FTA network
- **Key correction caught:** Subagent cited repealed ETA 2002 as in force; live verification on legislation.govt.nz showed the "Repealed" status banner — confirmed Pitfall #15

## Pitfall #15 Illustrated

| False claim (from subagent) | Reality (after live verification) |
|---|---|
| "Electronic Transactions Act 2002 — live primary legislation, verified" | **Repealed** since 1 Sep 2017. Banner at legislation.govt.nz page top clearly reads "Repealed". Replaced by Contract and Commercial Law Act 2017 Part 3. |

---

*Report generated 15 May 2026 by RDTII Agent (Hermes Agent for RDTII; Team Mahoraga). All scores provisional — require human reviewer confirmation.*
