# src/clarion/detection/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Classic supervised and unsupervised detectors plus OOF meta-learning.

## Phase ownership
P3

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **supervised.py** | LR RF optional LightGBM base learners and feature fit. |
| **unsupervised.py** | Isolation Forest OCSVM GMM and honest novelty ranking. |
| **graph_heads.py** | GNN classifier/novelty head on model-valid embeddings. |
| **stacking.py** | Chronological OOF stacking, calibrator and abstention handling. |

## Data/interfaces
**Inputs:** Validated train folds and representations.

**Outputs:** Scores, calibrated probabilities only if eligible, uncertainty manifests.

## Security, testing and acceptance
Meta-model cannot train on in-sample base predictions.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.

---

## Detailed §6 stacking engineering contract

**Source-derived architecture:** four base learner families; rule score 0–1; supervised LR/RF/LightGBM; unsupervised IF/OCSVM/GMM plus density diagnostics; GraphSAGE/GAT and temporal graph heads; chronological OOF predictions; regularized LR/LightGBM meta learner; eligible Δ/Π/motif meta-features; anomaly probability only with valid labels/calibration and conformal diagnostics.

**Do not** include graph propagation in pass-1, even though the uploaded diagram lists it among possible meta-features: seeds originate in pass-1. Put this score into capped pass-2 §9 after frozen §10 propagation.

**Inputs:** subject-level cutoff graph snapshot, causal feature registry, eligible labels, fold boundaries, embeddings, motif/Δ/Π feature availability and masks. **Outputs:** base score table (score types), OOF table, meta-model and calibration versions, likelihood/novelty, confidence/abstention, feature contributions.

**Required tests:** no in-sample meta-features; no future graph features or MCER state; no leakage from imputation/normalization; no false calibrated probability in unsupervised mode; false-positive cohorts and temporal holdout. Complete design: [Stacking architecture](../../../docs/architecture/stacking-architecture.md).
