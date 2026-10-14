# src/clarion/representation/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Graph-ML baselines and shared hetero-temporal embedding research.

## Phase ownership
P2

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **random_walk.py** | Node2Vec/random-walk candidate baselines and evaluation. |
| **graphsage.py** | Inductive GraphSAGE encoder proposal and training contract. |
| **gat.py** | GAT encoder and interpretable attention diagnostics. |
| **hetero_temporal.py** | Temporal/typed encoder plus cross-view alignment heads. |

## Data/interfaces
**Inputs:** Train-period graph/tensor snapshots and feature masks.

**Outputs:** Embedding arrays, model checkpoints and training manifests.

## Security, testing and acceptance
Train embeddings within folds; compare improvements vs simpler baselines.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
