# src/clarion/readiness/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Chain/wire feasibility routing based on exact joins, time and statistical dependence.

## Phase ownership
P1

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **joins.py** | TXID evidence tiers, sensor confidence and time alignment. |
| **coverage.py** | Missingness, join coverage, null/permutation controls and label audit. |
| **routing.py** | CHAIN_ONLY / CROSS_LAYER / UNSUPERVISED routing with reasons. |

## Data/interfaces
**Inputs:** Validated chain/wire tables and label provenance.

**Outputs:** Gate decisions + numeric diagnostics + explicit abstention causes.

## Security, testing and acceptance
Prove no missing TXID creates a host ownership association.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
