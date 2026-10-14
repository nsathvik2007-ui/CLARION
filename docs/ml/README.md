# Graph-ML, temporal entity clustering, stacking and experiment selection

> **Design documentation only.** The original uploaded CLARION v4 PDF supplies blocks 0–12; linked implementation choices and status are proposed and not verified as code. The docs listed below replace earlier TODOs where indicated.

## Detailed contracts

- [H1–H5 MCER signed constraint, temporal lineage and false-merge tests](mcer-plan.md)
- [Shared graph representation and model-selection rubric](model-selection.md)
- [L0–L3, OOF, honest holdouts, per-service false positives and ablations](experiment-plan.md)
- [Source-derived §6 model stack architecture](../architecture/stacking-architecture.md)
- [Source-derived §9/§10 diffusion/fusion plan](../architecture/risk-propagation-architecture.md)

## Key gates

Review the [source-to-requirement audit](../architecture/REQUIREMENTS_AUDIT.md) before asserting cross-layer, labeled or economic-cost feasibility. Honest chain-only/unsupervised/abstained outputs remain mandatory whenever sources do not support the proposed model.
