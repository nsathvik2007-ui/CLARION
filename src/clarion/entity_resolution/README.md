# src/clarion/entity_resolution/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
MCER H1–H5 evidence scoring, signed constraints, temporal partitions and lineage.

## Phase ownership
P2

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **proposals.py** | Co-spend, change and behavioral graph candidate pairs. |
| **constraints.py** | Service/CoinJoin cautions and uncertain wire conflict ledger. |
| **optimizer.py** | Conservative merge/split with stable stopping and abstention. |
| **lineage.py** | Versioned cluster history and retrospective explainability. |

## Data/interfaces
**Inputs:** Snapshot graph, candidate links, embeddings and conflict evidence.

**Outputs:** Entity hypotheses + per-address membership confidence + history.

## Security, testing and acceptance
Prioritize false-merge protections and independence of evidence sources.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
