# configs/profiles/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Offline CPU, GPU, chain-only, cross-layer and synthetic execution profiles.

## Phase ownership
P1/P5

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **cpu.yaml** | TODO: safe offline CPU mode; explicit resource and latency ceilings. |
| **gpu.yaml** | TODO: accelerator device selection with CPU fallback. |
| **chain_only.yaml** | TODO: disable unsupported cross-layer models and display abstentions. |
| **cross_layer.yaml** | TODO: quality gates and evidence requirements. |

## Data/interfaces
**Inputs:** See parent modules and the architecture specification.

**Outputs:** Versioned artifacts or typed interfaces; no implementation exists yet.

## Security, testing and acceptance
Require executable tests, provenance and review before marking complete.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
