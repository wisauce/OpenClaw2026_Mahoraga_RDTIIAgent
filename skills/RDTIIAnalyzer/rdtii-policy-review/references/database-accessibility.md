# RDTII Database and Source Accessibility Log

Last updated: 2026-05-15
Session: Australia 2025 full-scoring pipeline

## Accessible without residential proxies

| Source | URL | Method | Status | Notes |
|--------|-----|--------|--------|-------|
| WTO I-TIP (Trade Defence) | https://i-tip.wto.org/goods/Forms/GraphView.aspx?mode=tdb | Browser | Works | Complex multi-step form; starts with "ALL WTO MEMBER COUNTRIES" overview, use "TABLES by MEMBERS" or "DETAILED QUERY" link to narrow |
| Japan PPC — APPI English PDF | https://www.ppc.go.jp/files/pdf/APPI_english.pdf | curl + browser | Works | Two-column layout; use `pdftotext -layout` or extract via python3 + subprocess. 467KB, 49 pages. 2020 amendment version (not consolidated). Article 24 is the cross-border data transfer provision. |
| Australia legislation.gov.au | https://www.legislation.gov.au/ | Browser + curl | Works | Reliably accessible. No bot blocking. Acts available in HTML + PDF + Word. ID scheme: C2025C00378 for latest Privacy Act. |
| Australia OAIC — APPs full text | https://www.oaic.gov.au/privacy/australian-privacy-principles/read-the-australian-privacy-principles | Browser | Works | Full legal text of all 13 Australian Privacy Principles (Schedule 1, Privacy Act 1988). No bot blocking. Best single source for Australia's data protection framework. See also quick-reference at /privacy/australian-privacy-principles/australian-privacy-principles-quick-reference |
| Japan Law Translation | https://www.japaneselawtranslation.go.jp/ | Browser | Works, with 403 on specific paths | Landing page works; some individual law pages return 403. Try alternative paths. |
| WIPO Lex | https://wipolex.wipo.int/ | Browser | Works (previously) | Last verified earlier session; should work for IP law lookups. |

## Blocked (requires residential proxy)

| Source | URL | Error | Attempted method |
|--------|-----|-------|-----------------|
| UN ESCAP TAPED | https://www.unescap.org/analysis/taped | Cloudflare challenge | Browser — failed |
| TAPED alternative | https://taped.trade/ | Not attempted | — |
| Singapore SSO | https://sso.agc.gov.sg/Act/PDPA2012 | CloudFront 403 | Browser + curl — both blocked |
| SSO PDF endpoint | https://sso.agc.gov.sg/Act/PDPA2012?ViewType=Pdf | CloudFront 403 | curl — blocked |

## Timed out

| Source | URL | Method | Notes |
|--------|-----|--------|-------|
| METI (Japan FDI) | https://www.meti.go.jp/english/policy/external_economy/investment/index.html | Browser | Timed out (20s+). Try off-peak. |
| METI (Digital Platformer) | https://www.meti.go.jp/english/policy/mono_info_service/information_economy/digital_platformer/index.html | curl | Timed out (20s+). Try off-peak. |
| JETRO (Investment laws) | https://www.jetro.go.jp/en/invest/setting_up_laws/section3/page7.html | curl | Unknown — page may not exist at this URL |

## Alternative access methods to try

For blocked sources, try these before giving up:

1. **Wayback Machine**: `https://web.archive.org/web/*/https://blocked.url`
2. **Google cache**: `https://webcache.googleusercontent.com/search?q=cache:https://blocked.url`
3. **Alternative mirrors**: Some government databases have regional mirrors or FTP endpoints
4. **curl with specific User-Agent**: `curl -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"`
5. **curl with mobile UA**: `curl -A "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X)"`

## Preferred countries for primary-source English legal text

When demonstrating the pipeline or when a user wants an end-to-end example with accessible primary sources, prefer these countries (in order):

1. **Australia** — legislation.gov.au + OAIC website, no bot blocking, English, well-structured acts. Best overall choice for full pipeline demo.
2. **Japan** — PPC PDF available for APPI; other laws via Japanese Law Translation (sometimes blocked). Good for Pillar 6/7 demo.
3. **New Zealand** — legislation.govt.nz, no bot blocking (not verified in this session but historically accessible)
4. **United Kingdom** — legislation.gov.uk, no bot blocking (not verified in this session but historically accessible)
