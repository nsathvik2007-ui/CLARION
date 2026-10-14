# CLARION offline investigator threat model (DESIGN, not audited software)

**Scope:** local Linux workstation, sensitive raw Bitcoin P2P metadata, user-supplied CSV/JSON/XML, optional external benchmark, local model weights, derived graph, analyst notes, PDF/CSV exports and a localhost dashboard. This document does not mean security tests have passed.

## 1. Protected assets and trust boundaries

| Trust boundary | Assets at risk | Threat | Planned controls | Verification |
|---|---|---|---|---|
| Imported file → parser | evidence bytes, operating system, output catalog | XXE, XML bomb, giant JSON arrays, malformed CSV, path traversal, data poisoning | allowlist formats, file/row/depth/array limits, DTD/external entities disabled, safe temp dir, no arbitrary shell execution | fuzz invalid inputs, decompression/size/time budgets |
| Source → immutable evidence | data integrity and chain of custody | fake/modified captures, clock spoof, mislabeled sources | source hash, capture ID, declared sensor time accuracy, append-only audit, raw read-only snapshots | source modifications detected; hashed rebuild |
| Wire → chain join | wallet/host association | forged TXID, repeated relays, stale clocks, NAT/hosted service | exact observed TXID, independent sensor count, confidence type and J0–J3 tiers, no owner edge | negative controls and no false Host→Address facts |
| Graph → learning | model and historical reconstruction | fabricated edges, future leakage, high-degree sampling bias | typed edge allowlist, cutoff enforcement, node/edge trust masks, fold-specific snapshots | graph temporal unit tests and leakage sweep |
| Dataset → model trainer | ML reliability | poisoned labels, generator shortcuts, class imbalance, unsafe serialized checkpoints | label provenance/eligibility, separate truth ledger, robust holdout, safe weights formats, strict model manifest | poison/label swap checks, artifact mismatch rejection |
| Frozen risk → propagation | legitimate actors | circular score boosting, sybil edges, 1→N amplification, exchange blanket contamination | immutable pass-1 seeds, separate value/context channels, normalized fan-out, ≤6 hops, absorbing service boundaries | property tests, neighbor FPR audit |
| API → browser | session and private evidence | unauthenticated LAN exposure, XSS, CSRF, data overfetch, directory escape | bind loopback by default, role-gated remote deployment, input escaping, CSP, query size/page/time limits | authorization, browser XSS and hostile URL tests |
| Browser → export | sensitive case content | leaked IPs, spreadsheet injection, injected PDF or unsanitized notes | redaction policy, Excel formula escaping, PDF sanitization, signed/hashed manifest, audit log | export opening/verification tests |
| Offline package → runtime | confidentiality and availability | external telemetry, hostile dependency, unsafe updater, malicious model pickle | pinned wheels and model hashes, supply-chain scan, no external runtime requests, refuse unsafe deserialization | network denied and SBOM/lockfile checks |

## 2. Sensitive information and retention

Raw sensor IP/port metadata may be personal data. Default access is local authorized analyst, with least-privilege file and database access. Separate raw evidence, masked analyst representations and public synthetic examples. Provide role-limited reveal/redaction of IPs and P2P captures. Do not log secrets, raw paths, entire network samples or annotations by default.

Propose a configurable retention schedule for raw, normalized, graph/cache and exported dossiers; every purge is audited, preserves legal holds if required, and does not falsely claim full erasure from external storage. Dataset licenses govern use of local GeoIP/ASN sources.

## 3. Model integrity, misuse and uncertainty

Do not let model score or GAT attention stand in for judicial evidence. Require provenance, calibration limits, benign alternatives, abstention and explicit "not verified ownership / not guilt" warnings in views and reports. Prevent remote model download or execution of arbitrary pickled checkpoint; use trusted weights with hashes and safe loaders.

**Adversarial analytics:** synthetic attacker patterns should test resistance to spurious relay correlations and capture bias, not promise identity tracing. An analyst cannot silently edit raw evidence or suppress uncertainty just by adding notes.

## 4. Offline-by-default product security profile

- Linux only release target for SIH; developer CI/network use does not change offline inference requirement.
- Dashboard serves on \`127.0.0.1\`; web assets bundled; no analytics, fonts, maps or third-party scripts.
- Local authorized operator account; before any LAN/team deployment, add authentication, roles, CSRF protections, TLS where needed, audit and reviewed network architecture.
- All wheels, models, static UI assets and legally distributable enrichment files are provisioned before network block. Dependency installation may be performed online in development but **offline release tests** run without network access.
- Feature flags cannot bypass critical ownership, clock, import and evidence-integrity checks.

## 5. Severity-ranked test scenarios

**Release-blocking:** XXE, path traversal, malicious joblib/pickle, unauthenticated case export, unauthorized IP leak, post-cutoff evidence exposure, forged Host→Address ownership edges, uncontrolled prop risk through exchange, external inference-time calls, truncated/modified dossier lacking warning.

**High priority:** excessively large graph query DoS, CSV formula injection, source hash mismatch, conflicting dedupe/sensor count, label poisoning without provenance, security log tampering.

**Medium priority:** optional ASN lookup missing, stale license manifest, slow deep graph visualization, dashboard inaccessible without network-installed font.

## 6. Security acceptance gate

[ ] documented asset owners; [ ] enforce read-only evidence and hash manifests; [ ] reject unsafe parsers and model serialization; [ ] no public network listener by default; [ ] logged authorized case export and redaction; [ ] offline egress test; [ ] risk graph invariant tests; [ ] confidentiality and synthetic-only sample policy; [ ] security scan artifacts linked to phase tracker.

**Source distinction:** the SIH statement requires a workable Linux offline system, while most specific controls above are proposed security design requirements, not confirmed functional behavior.
