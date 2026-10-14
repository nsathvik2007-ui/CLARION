# CLARION v4 — Scientific experiment plan, gates and ablations

**Research protocol only; no results collected.** The uploaded §12 demands graded L0–L3 synthetic behavior, legitimate services, timed holdouts, per-tier and typology metrics, ARI/NMI, stack AUROC/AUPRC, Π abstention, and propagation contamination audit.

## 1. Questions and falsifiable hypotheses

- **RQ1 (utility):** does wire evidence improve held-out detection vs chain-only, beyond permuted pairs and sensor capture bias?
- **RQ2 (entity resolution):** do GraphSAGE/GAT features plus careful wire conflicts reduce pairwise false merges vs chain-only H1/H2?
- **RQ3 (stack):** do diverse base learners yield holdout PR-AUC/precision@K improvements over strongest single baseline without leakage?
- **RQ4 (Δ/Π):** do residual disagreement and economic-cost premiums capture *different* behavior in controlled synthetic groups? Does Δ decrease while Π rises across independently varied L0–L3 levels?
- **RQ5 (propagation):** can causal, value-conserving MLRP surface meaningful connected leads without contaminating innocents, exchanges, custodians and shared hosts?
- **RQ6 (human usefulness):** can an investigator reproduce the top-k lead from source evidence and identify uncertainty and benign explanations?

**Failure to support a hypothesis is an acceptable result.** A synthetic crossing pattern built in by the generator is not independent confirmation.

## 2. Dataset/evaluation axes

| Track | Source type | Primary valid targets | Prohibited claim |
|---|---|---|---|
| A1 | Elliptic++ transaction/actor graph benchmark | task-specific supervised graph detection, partial entity study | verified true IP/host associations |
| A2 | BitcoinHeist address feature benchmark | address anomaly and temporal behavior | definite clean negatives without audit |
| A3 | local Bitcoin Core on-chain samples | UTXO/fee/motif chain correctness | original P2P broadcaster IP |
| B | synthetic v4 chain/wire with sealed truth | exact joins, MCER truth, Δ/Π/MLRP end-to-end correctness | real-world illicit accuracy |
| C | actual SIH samples (if available) | format compliance, coverage and *eligible* detection | metrics for missing/unverified labels |

## 3. Frozen split design

- Dataset period sorted by a **declared meaningful event time**; define \`train\` oldest, \`valid/calibration\` later and \`test\` newest, not random shuffle. Do not assume header block times equal wire first seen.
- Expanding time folds: fit on past, predict next period. Keep fold-specific scaler, imputer, embedding encoder, MCER membership, graph snapshot, label eligibility, Δ/Π fit and anomaly base model; meta-training takes **only out-of-fold** base scores.
- Purge overlapping label windows and suspiciously shared scenario generator seeds; maintain grouped sensitivity experiments so cross-split graph relationships cannot leak future labels.
- Select threshold/hyperparameters on train/validation only; locked holdout evaluated once. Repetitions use multiple dataset/generator seeds and report distribution, not only best run.
- Refit final deployed models only after evaluation. Stamp manifest with time splits, feature versions, model dependencies and confidence limitations.
- MLRP validation must freeze pass-1 fold predictions before making fold-local propagation features for any learned pass-2 model.

## 4. Test matrices and primary metrics

| Subsystem | Primary metrics | Robustness checks |
|---|---|---|
| Import & joins | invalid-row %, exact join count/precision against synthetic truth, independent paired N, coverage | duplicates, sensor bias, clock drift, missing TXID |
| MCER | pair precision/recall, false-merge rate, ARI/NMI, abstain | custody, CoinJoin, shared host, version stability |
| Motifs | witnessed pattern precision/recall by type, paths | payroll/batching/consolidation and benign cycles |
| Classic & graph ML | PR-AUC (labeled), ROC-AUC, precision@K, recall, F1, Brier/ECE where valid | time shift, changing base rate, source changes |
| Δ | held-out residual vs shuffled null, component false positives, availability and abstain | independent sensors, high-degree relays, VPN/NAT |
| Π | accurate unit bills vs known synthetic objective, baseline sensitivity and abstain fraction | exchange batching signed premium, privacy negatives |
| Fusion | precision@analyst-budget, risk calibration if possible, subgroup false alerts, stability | Δ/Π missing, dependence of features, shift |
| MLRP | conservation, contamination vs hops, first-hop neighbor false alerts, path correctness | 1→200 split, temporal cycles, service absorption |
| UI/dossier | exact source trace, export hash, time cutoff, usability | private IP redaction, XSS, offline and large graph |
| Operational | throughput, RSS/VRAM, model size, latency, artifact rebuild | CPU-only, network blocked, invalid model weights |

**Never** collapse per-model, per-tier, per-typology and per-service failures into one top-level accuracy figure.

## 5. Ablation grid (required)

A0: chain rule-only. A1: causal chain features + tabular ML. A2: + chain graph embeddings. A3: + MCER/motif (no wire). A4: + observed wire features when validated. A5: + Δ residual. A6: + itemized eligible Π. A7: + meta-model stack. A8: + frozen-seed MLRP. Additional leave-one-family-out and chain-only counterfactual ablations.

**Scientific comparability:** each paired ablation shares the same cohort, cutoff, label definitions, feature availability, training resources where possible, hyperparameter-selection budget and held-out test. If a signal is unavailable, report **not comparable / abstained**, not an artificially favorable zero.

## 6. Synthetic L0–L3 and hard negatives

Generate multiple degrees of transaction splitting, address reuse, fee/time/infrastructure cost and wire detectability with **independent factors**, not a deterministic L0→L3 label code. Keep ledger control and ground truth separate from observed features. Introduce exchange batching, payment processors, custodians, CoinJoin, shared relay nodes, sensor loss, clock skew, VPN/mobile routes and fee regime changes.

Run **cross-generator / parameter shift**: train on one generator configuration and evaluate on another, to surface reliance on synthetic shortcuts. Document how "criminal" label is defined—never imply a specific mathematical motif proves motive.

## 7. Error analysis and uncertainty

Report 95% confidence intervals via subject-/time-grouped bootstrap where support allows (not a blanket formula), false discovery burden among P1 leads, subgroup sample counts, and calibration drift. Explicitly publish when positive samples are too few to estimate a metric. Document manual analyst review cases and corrections separately from original labeled truth.

**Risk audit:** test that an innocent 1-hop neighbor of a frozen seed does not automatically become P1, that 1→200 fan-out remains diluted, and that host/ASN/Country cannot contaminate unrelated customers.

## 8. Exit criteria

[ ] time split frozen; [ ] every feature has available_at; [ ] OOF stack proven; [ ] test cohort separation; [ ] legitimate controls; [ ] Δ/Π abstention analysis; [ ] MCER false-merge audit; [ ] propagation mass/boundary tests; [ ] dashboard evidence reproduction; [ ] local air-gap test; [ ] accurate provenance and source hashes; [ ] results distinguish synthetic, benchmark and operational data.

No experiment is claimed complete by writing this document.
