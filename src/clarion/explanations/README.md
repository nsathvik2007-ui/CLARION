# src/clarion/explanations/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Evidence-centered interpretability and minimal sufficient proof subgraphs.

## Phase ownership
P4

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **contributions.py** | SHAP/model contributions and signal/gating bars. |
| **dossiers.py** | Assemble local, signed and redactable case evidence. |
| **counterfactual.py** | Time-valid chain-only vs cross-layer ablation comparison. |

## Data/interfaces
**Inputs:** Model outputs, evidence graph, typed uncertainty and manifest.

**Outputs:** Case dossier data with human-readable evidence paths.

## Security, testing and acceptance
Never export unauthorized IP identifiers or unreviewed attribution.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.
