# src/clarion/propagation/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Value-conserving causal forward/backward MLRP with absorbing boundaries.

## Phase ownership
P4

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **edges.py** | Typed conductances, value share, time/hop decay. |
| **diffusion.py** | Deterministic frozen-seed bounded propagation. |
| **boundaries.py** | Services, CoinJoin, ASN/country no-reemission policies. |
| **paths.py** | Trace minimal contributing causal paths and provenance. |

## Data/interfaces
**Inputs:** Frozen preliminary seeds + typed transaction graph.

**Outputs:** Per-level risk, provenance channels, bounded paths.

## Security, testing and acceptance
Test no blanket contamination across exchanges/hosts.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
