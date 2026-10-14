# src/clarion/patterns/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Interpretable Bitcoin motif matching plus learned temporal subgraph novelty.

## Phase ownership
P2

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **peel.py** | Peel-chain candidates with supporting UTXO path and change uncertainty. |
| **mixing.py** | Mixing-like, CoinJoin-like and benign service confounders. |
| **layering.py** | Rapid layering, circular flows, fan-in/out and temporal depth. |
| **novelty.py** | Subgraph pattern embedding and novel prototype candidates. |

## Data/interfaces
**Inputs:** Time-resolved transaction/UTXO graph + service constraints.

**Outputs:** Typed motif instances, paths, confidence and benign alternatives.

## Security, testing and acceptance
No motif is guilt; test exchange, custody, CoinJoin controls.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
