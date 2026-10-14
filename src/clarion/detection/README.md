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
