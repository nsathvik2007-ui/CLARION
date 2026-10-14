# Investigative data privacy and access policy (proposed)

**Status: DESIGN, not a published legal policy or deployed feature.** CLARION may process IP addresses, port/timing, transaction and speculative entity groupings that can be sensitive. Legal basis, investigator jurisdiction and actual organizer data terms must be separately reviewed.

## 1. Separation of data classes

| Data | Classification | Default handling |
|---|---|---|
| Raw legal capture / source evidence with IPs | restricted | read-only encrypted/permissioned local storage, hash manifest, minimal copies |
| Transaction/UTXO chain graph | source-defined/public chain or restricted sample | source manifest, time window and no ownership conclusion |
| GeoIP/ASN | licensed or derived approximate context | local lookup only; license and refresh rules |
| Entity/cluster hypotheses | sensitive inferred analytical data | confidence and evidence trail; avoid definitive personal labels |
| Model labels and controlled synthetic truth | research restricted | separate feature access; no train/test leakage |
| Investigator review notes and case exports | privileged case work | role-limited access, redaction, audit and retention |
| Aggregated metrics for reports | shareable only if privacy-checked | prevent small-cell or direct IP disclosure |

## 2. Principle of purpose limitation

The app assists legitimate offline investigation of authorized datasets. It cannot claim real-world identities from network relays and should not be used as an automatic accusation engine. Investigators should be able to inspect uncertainty and non-illicit alternatives.

Never upload private evidence to remote LLMs, telemetry systems or convenience geolocation APIs. Default UI masks unneeded network identifiers and supports least-privilege reveal where lawful.

## 3. Retention and deletion

Configure distinct retention periods for raw evidence, normalized tables, intermediate graph/model caches, investigator dossiers and logs; actual periods require project owner/legal signoff. Track irreversible deletion limits, backed-up copies and legal holds. Raw evidence integrity/chain-of-custody rules supersede unreviewed auto-deletion.

## 4. Case export

Every export includes a case/run ID, evidence source IDs/hashes, analyst authorization, timestamp/cutoff, model versions, redaction policy version and generated file hash. CSV escapes leading formula characters and PDF output sanitizes text. No unsupported IP-to-entity ownership assertion.

## 5. Privacy tests and audit

- Role A (restricted) cannot access unredacted IPs or source paths in UI/API/PDF/CSV.
- Redacted graph and leads remain useful without revealing exact captured IP.
- Case views reflect the same temporal cutoff and evidence provenance.
- No private raw evidence in application logs/errors.
- Offline egress-denial audit covers exports, charts, ML and bundled assets.
- Manual annotations never overwrite raw capture evidence.

## 6. Open decisions

Determine investigator roles, legal basis, raw/derived retention, encryption/backups, lawful data sharing and GeoIP license restrictions from the actual operating environment. None is specified in the uploaded v4 architecture PDF; do not invent approval.
