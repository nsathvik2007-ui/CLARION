# src/clarion/chain/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Bitcoin UTXO, transactions, scripts, fees and directed value flow.

## Phase ownership
P1

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **transactions.py** | Parse input/output details, fee, time and vsize without assumptions. |
| **utxo.py** | Resolve prevout lineage and chain-state uncertainty. |
| **features.py** | Deterministic chain-specific primitives, change hypotheses and reuse. |

## Data/interfaces
**Inputs:** Validated on-chain transactions and optional prevouts.

**Outputs:** Temporal spends/funds facts, fee environment, UTXO flow.

## Security, testing and acceptance
Handle coinbase, partial prevouts, multisig, Taproot and reorg uncertainty.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
