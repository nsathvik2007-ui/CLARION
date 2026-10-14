# docs/progress/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Phase status ledger: no phase may be reported complete without evidence.

## Phase ownership
P0–P5

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **phase-00-architecture.md** | Architecture review only; no code implemented. |
| **phase-01-foundation.md** | TODO: step status, commands, tests, risks and P2 handoff. |
| **phase-02-graph-entity-patterns.md** | TODO: model/MCER/motif verification and acceptance. |
| **phase-03-ml-cross-layer.md** | TODO: OOF stack, Δ/Π validity and performance. |
| **phase-04-console-propagation.md** | TODO: MLRP, UI and case dossier acceptance. |
| **phase-05-release.md** | TODO: Linux offline and scientific validation. |

## Data/interfaces
**Inputs:** See parent modules and the architecture specification.

**Outputs:** Versioned artifacts or typed interfaces; no implementation exists yet.

## Security, testing and acceptance
Require executable tests, provenance and review before marking complete.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
