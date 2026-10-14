# Detailed architecture overview and source-aligned contracts

> **Design documentation only.** The original uploaded CLARION v4 PDF supplies blocks 0–12; linked implementation choices and status are proposed and not verified as code. The docs listed below replace earlier TODOs where indicated.

## Detailed contracts

- [Source PDF traceability + open decision register](REQUIREMENTS_AUDIT.md)
- [Canonical end-to-end execution modes and fallback behavior](architecture-overview.md)
- [Typed inter-module DTOs and invalid-edge rules](component-contracts.md)
- [Full original 33-section design reference (preserved)](architecture-v4-spec.md)
- [Stacking and OOF contract](stacking-architecture.md)
- [Two-pass MLRP and risk score contract](risk-propagation-architecture.md)
- [Offline dashboard/API/case dossier contract](investigator-dashboard-architecture.md)

## Key gates

Review the [source-to-requirement audit](REQUIREMENTS_AUDIT.md) before asserting cross-layer, labeled or economic-cost feasibility. Honest chain-only/unsupervised/abstained outputs remain mandatory whenever sources do not support the proposed model.
