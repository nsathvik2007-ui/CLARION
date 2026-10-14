# docs/data/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Data dictionary, provenance, dataset adapter/legal-use notes and quality gates.

## Phase ownership
P1

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **data-dictionary.md** | TODO: fields, units, null meaning, legal provenance and sample shapes. |
| **dataset-acquisition.md** | TODO: three-track benchmark/synthetic/SIH strategy and licensing. |
| **join-policy.md** | TODO: J0-J3 association tiers and no wallet IP attribution. |

## Data/interfaces
**Inputs:** See parent modules and the architecture specification.

**Outputs:** Versioned artifacts or typed interfaces; no implementation exists yet.

## Security, testing and acceptance
Require executable tests, provenance and review before marking complete.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
