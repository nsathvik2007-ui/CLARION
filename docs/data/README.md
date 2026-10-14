# Evidence acquisition, schema and join contracts

> **Design documentation only.** The original uploaded CLARION v4 PDF supplies blocks 0–12; linked implementation choices and status are proposed and not verified as code. The docs listed below replace earlier TODOs where indicated.

## Detailed contracts

- [Canonical Bitcoin/UTXO/wire fields and missing values](data-dictionary.md)
- [Independent sources, synthetic truth and provenance](dataset-acquisition.md)
- [J0–J3 joins, statistical dependence/coverage and source clock policies](join-policy.md)

## Key gates

Review the [source-to-requirement audit](../architecture/REQUIREMENTS_AUDIT.md) before asserting cross-layer, labeled or economic-cost feasibility. Honest chain-only/unsupervised/abstained outputs remain mandatory whenever sources do not support the proposed model.
