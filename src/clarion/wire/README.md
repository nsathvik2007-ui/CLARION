# src/clarion/wire/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Network observation, session and optional offline IP-enrichment processing.

## Phase ownership
P1

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **observations.py** | Normalize legal, source-tagged TXID relay observations. |
| **sessions.py** | Time-bounded sessionization and repeated-relay de-duplication. |
| **enrichment.py** | Versioned offline ASN/GeoIP lookup with optional unknown status. |

## Data/interfaces
**Inputs:** Observed TXID relays, ports, clocks, sensor IDs and local GeoIP.

**Outputs:** Source-linked host/session edges, data coverage and wire features.

## Security, testing and acceptance
Ensure relay never becomes wallet ownership; no egress at runtime.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
