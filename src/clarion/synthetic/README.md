# src/clarion/synthetic/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Deterministic synthetic Bitcoin+wire L0–L3 scenario and hard-negative generator.

## Phase ownership
P1/P5

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **generator.py** | Generate legal SIH-format tx/wire records and truth sidecar. |
| **scenarios.py** | L0–L3, exchange, processor, CoinJoin, clock and sensor bias. |
| **ground_truth.py** | Hold independent labels/objectives sealed from model features. |

## Data/interfaces
**Inputs:** Scenario recipes and versioned random seeds.

**Outputs:** Separate raw samples, truth ledger, variation manifests.

## Security, testing and acceptance
Detect benchmark generator artifacts and label leakage.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
