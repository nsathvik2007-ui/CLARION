# scripts/train/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Explicit developer-initiated model training and experiment reproduction.

## Phase ownership
P3

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **run_baselines.py** | TODO: command-line chronological base model evaluation. |
| **run_gnn.py** | TODO: graph-encoder fit/evaluate with checkpoint manifests. |

## Data/interfaces
**Inputs:** See parent modules and the architecture specification.

**Outputs:** Versioned artifacts or typed interfaces; no implementation exists yet.

## Security, testing and acceptance
Require executable tests, provenance and review before marking complete.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
