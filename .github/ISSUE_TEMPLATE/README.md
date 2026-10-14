# .github/ISSUE_TEMPLATE/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Templates for architecture decision, technical work, bug and research tasks.

## Phase ownership
cross-phase

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **implementation.md** | TODO: phase, input/output contract, acceptance tests, owner and risks. |
| **research.md** | TODO: hypothesis, dataset provenance, validation split and negative controls. |

## Data/interfaces
**Inputs:** See parent modules and the architecture specification.

**Outputs:** Versioned artifacts or typed interfaces; no implementation exists yet.

## Security, testing and acceptance
Require executable tests, provenance and review before marking complete.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
