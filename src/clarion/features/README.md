# src/clarion/features/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Feature registry with availability times, masks, units and reproducible transformations.

## Phase ownership
P2

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **registry.py** | Formal typed feature definitions and missingness handling. |
| **chain.py** | Spend flow, fan-in/out, bursts, fees, motifs and value summaries. |
| **wire.py** | ASN stability, port entropy, sessions, skew and coverage. |
| **temporal.py** | Time-causal rolling neighborhoods, dormancy, velocity. |

## Data/interfaces
**Inputs:** Graph snapshots + cutoff + valid observations.

**Outputs:** Chain/wire/snapshot feature tensors with availability masks.

## Security, testing and acceptance
Any future observation included in historical features must fail tests.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
