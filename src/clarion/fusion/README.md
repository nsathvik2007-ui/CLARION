# src/clarion/fusion/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Two-pass calibrated local and capped propagation fusion and typology.

## Phase ownership
P3/P4

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **local.py** | Calibrate eligible local evidence without raw Π+Δ addition. |
| **typology.py** | Π–Δ quadrants, only when both axes valid. |
| **final.py** | Freeze seeds, cap MLRP <=25/100, priority P1–P4. |

## Data/interfaces
**Inputs:** Stack, patterns, Δ/Π, then independent frozen MLRP exposure.

**Outputs:** Provisional/final lead score with contribution explanation.

## Security, testing and acceptance
No circular propagation feeding pass-1 predictor.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
