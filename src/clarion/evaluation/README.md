# src/clarion/evaluation/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Research metrics, ablations, temporal evaluation and subgroup FP audits.

## Phase ownership
P2–P5

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **metrics.py** | PR-AUC ROC-AUC precision-at-K calibration ARI/NMI abstention. |
| **ablations.py** | Chain-only +wire +graph +Δ/Π +MLRP controlled comparisons. |
| **leakage.py** | Split/embedding/graph future availability audits. |
| **robustness.py** | Hard negatives, sensor dropout, regime shift and poisoning probes. |

## Data/interfaces
**Inputs:** Holdout results, sealed truth and model manifests.

**Outputs:** Versioned experiment reports and known-limit statements.

## Security, testing and acceptance
No synthetic test may be marketed as real incident validation.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
