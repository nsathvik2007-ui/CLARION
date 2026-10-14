# Definition of done — architecture, code and scientific acceptance gates

**Current state:** architecture review in progress; comment-only file stubs are not executable code. A documentation commit can verify internal links/traceability, but **cannot** establish that models train, a dashboard works, or the tool is production-ready.

## 1. Three distinct statuses

1. **DESIGNED:** diagram/source requirement, input/output contract, fallbacks, error path and tests specified.
2. **IMPLEMENTED:** real connected code and interface migrations exist; not necessarily correct.
3. **VERIFIED:** tests and experiment results actually executed with environment, logs, reproducible artifacts, measured limitations and review.

No document or PR may equate (1) with (2)/(3).

## 2. Design signoff gate

- [ ] Each PDF block 0–12 mapped to a real module, source-derived behavior and unresolved decisions.
- [ ] Source-provided vs engineering-added items clearly labeled.
- [ ] Canonical data schema and J0–J3 join tiers documented; no wallet ownership invention.
- [ ] Linux/offline architecture and model asset sourcing documented.
- [ ] MCU/MCER temporal clusters and false-merge safeguards; graph representation and motif contracts.
- [ ] Four-family stack, chronological OOF, Δ/Π eligibility, two-pass frozen-seed MLRP, propagation ≤25/100.
- [ ] Six node types; Country context only; five scored levels with different scales; financial vs observational channels.
- [ ] Investigator dashboard screens, API, pagination/security and evidence dossier contracts.
- [ ] Time-split and signed synthetic-truth protocol; per-tier false-positive/control requirements.
- [ ] Critical open decisions listed, classified as **unverified/blocked** rather than guessed.

Signoff may be **conditional** while actual SIH data is unavailable; the remaining requirements must then be implemented as honest gate/fallback behavior rather than assumed successful cross-layer inference.

## 3. Implementation/verification gate per phase

| Phase | Must demonstrate before merging implementation PR | Evidence |
|---|---|---|
| P1 | CSV/JSON/XML → strict canonical records → J0/J1 audit → typed graph → chain-only baseline | real command lines, parser tests, hashes, fixtures and Linux run |
| P2 | causal features/embeddings, stable temporal MCER, motif witness paths with benign controls | train/snapshot manifest, ARI/NMI/false-merge and motif test report |
| P3 | eligible supervised OOF meta-learner or honest unsupervised stack; Δ/Π abstention, pass-1 fusion | OOF leakage audit, holdout metrics, model card, abstentions |
| P4 | frozen-seed MLRP, cap/service tests, local API/dashboard and hash-bound PDF/CSV exports | running screenshots are supplementary, actual local E2E and network-denial logs mandatory |
| P5 | complete synthetic L0–L3 scenarios, held-out ablations, subgroup FPR, reproducibility and security | repeatable benchmark reports, CI, Linux offline test and final limitations |

**No fake pass counts:** always distinguish not-run, failed, skipped, and passed. CI on doc-only branches is not proof of a working system.

## 4. Scientific reporting

- Identify dataset, class definition, label provenance, subject granularity, sample N, time window, split, model and baseline.
- If valid negative labels are absent, don't provide precision/recall as though they were known.
- Show high-degree services, CoinJoin, VPN, custodial and privacy-user FP breakdown; report abstention rate for Δ/Π.
- Disclose synthetic-to-real performance gap and chain-only routing.
- Show propagation graph value conservation and prevent innocent 1-hop contamination.

## 5. Merge/production safety

- No confidential raw datasets, copyrighted licensed bulk data, private IP logs, secrets or oversized model binaries in Git.
- Every public interface/schema change has compatibility tests, documentation and an ADR.
- Model weights are safe, locally hashed and bundled; all UI static assets local.
- Repeated unknowns or blockers remain explicit in progress tracker and README until tested.

The detailed source-to-requirement audit is [REQUIREMENTS_AUDIT](../architecture/REQUIREMENTS_AUDIT.md).
