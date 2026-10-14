# schemas/normalized/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Canonical chain, wire, label and economic-objective contracts with source linkage.

## Phase ownership
P1/P3

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **chain.schema.md** | TODO: transactions, inputs, outputs, outpoints, block time and fees. |
| **wire.schema.md** | TODO: observed TXID, host, session, ASN, timestamp precision. |
| **labels.schema.md** | TODO: label provenance, availability time, task granularity and split eligibility. |
| **objectives.schema.md** | TODO: Π cost goal, payees, controlled sets, constraints and abstention. |

## Data/interfaces
**Inputs:** See parent modules and the architecture specification.

**Outputs:** Versioned artifacts or typed interfaces; no implementation exists yet.

## Security, testing and acceptance
Require executable tests, provenance and review before marking complete.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
