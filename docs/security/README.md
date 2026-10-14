# Offline privacy/security threat model and acceptance

> **Design documentation only.** The original uploaded CLARION v4 PDF supplies blocks 0–12; linked implementation choices and status are proposed and not verified as code. The docs listed below replace earlier TODOs where indicated.

## Detailed contracts

- [Assets, trust boundaries, threats and threat-led regression tests](threat-model.md)
- [Privacy and retention plan (separate document: still must be finalized)](privacy-policy.md)
- [Air-gapped runtime checklist (separate document: still must be finalized)](offline-checklist.md)

## Key gates

Review the [source-to-requirement audit](../architecture/REQUIREMENTS_AUDIT.md) before asserting cross-layer, labeled or economic-cost feasibility. Honest chain-only/unsupervised/abstained outputs remain mandatory whenever sources do not support the proposed model.
