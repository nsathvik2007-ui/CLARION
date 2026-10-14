# src/clarion/graph/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Six-type heterogeneous temporal evidence graph and snapshot conversion.

## Phase ownership
P1/P2

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **types.py** | Allowlist Transaction Address Entity Host ASN Country and edge kinds. |
| **builder.py** | Build only observed edges with provenance and time. |
| **snapshots.py** | Causal daily/weekly views; stable IDs and graph hashes. |
| **pyg_adapter.py** | Convert valid windows into PyG HeteroData with masks. |

## Data/interfaces
**Inputs:** Chain/wire edges, candidate clusters, snapshot cutoff.

**Outputs:** Versioned time-aware graph and subgraph/neighbor interfaces.

## Security, testing and acceptance
Test illegal host-address ownership links and future leakage.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
