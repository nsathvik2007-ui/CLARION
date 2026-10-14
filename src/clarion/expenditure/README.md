# src/clarion/expenditure/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Π fee, hop, delay, fragmentation and infrastructure itemized baselines.

## Phase ownership
P3

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **objectives.py** | Identify controlled set, same economic outcome, feasibility. |
| **baseline.py** | Counterfactual minimum-cost plan under constraints. |
| **components.py** | Calculate signed bill components in original units. |
| **abstain.py** | Reject unsupported payee/fee/infrastructure assumptions. |

## Data/interfaces
**Inputs:** UTXO flow + supported goals and fee environment.

**Outputs:** Itemized Π or per-component abstention with assumptions.

## Security, testing and acceptance
Never sum mixed units or equate paid privacy with wrongdoing.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
