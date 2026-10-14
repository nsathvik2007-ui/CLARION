# schemas/graph/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Graph snapshot, node, edge, entity and association-confidence contract.

## Phase ownership
P1/P2

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **graph.schema.md** | TODO: six node types, allowed directed relations, evidence path and causal time. |
| **entities.schema.md** | TODO: candidate membership, confidence, competing proposals, version lineage. |

## Data/interfaces
**Inputs:** See parent modules and the architecture specification.

**Outputs:** Versioned artifacts or typed interfaces; no implementation exists yet.

## Security, testing and acceptance
Require executable tests, provenance and review before marking complete.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
