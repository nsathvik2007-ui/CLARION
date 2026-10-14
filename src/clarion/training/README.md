# src/clarion/training/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Chronological fold construction, fitting, artifact registry and drift comparison.

## Phase ownership
P3/P5

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **splits.py** | Expanding folds, gaps, entity/scenario leakage diagnostics. |
| **trainer.py** | Training orchestrator with base and meta-model stages. |
| **registry.py** | Offline signed/hashes model manifest, champion/challenger decisions. |
| **drift.py** | Shift/coverage diagnostics and human-approved promotion. |

## Data/interfaces
**Inputs:** Eligible labels, time-safe features, model recipes.

**Outputs:** OOF predictions, validated model artifacts, model cards.

## Security, testing and acceptance
No synthetic/unknown labels silently treated as confirmed truth.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
