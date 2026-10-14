# ADR-001 — Offline, evidence-first and uncertainty-preserving architecture

**Status:** Proposed for review; not operationally verified.  
**Drivers:** SIH26146 requires Linux offline bulk analysis, cross-layer correlation and working AI/ML. Uploaded CLARION v4 diagram requires provenance, uncertainty and risk safeguards.

## Context

Chain TXIDs and wire observation messages can be correlated when the wire capture **actually contains a decoded TXID**. However, a Bitcoin transaction can be relayed by many nodes, and IP metadata cannot alone establish the address owner or transaction origin. Public transaction-only benchmarks rarely contain authenticated P2P network observations. Source diagram §6/§10 creates a potential modeling cycle unless fusion is sequenced.

## Proposed decisions

1. **Data:** immutable locally imported evidence, explicit time/source/sensor provenance, exact integer satoshis and outpoint-first graph semantics.
2. **Graph:** six node types, time-valid directed edges, source/association provenance, no Host→wallet ownership inference.
3. **Model routing:** independently gate cross-layer, trusted supervision, Δ paired-view residual and Π economic-cost scoring; abstain rather than invent features.
4. **MLP/MCER:** temporal features and candidate entity clusters cannot include future samples; stop false merges in shared/hosted/CoinJoin cases.
5. **Fusion:** pass-1 local stack/pattern/Δ/Π → freeze seeds → MLRP with financial/contextual channels and service boundaries → capped pass-2 score (≤25 propagated points of 100).
6. **Serving:** offline localhost investigator console with provenance-bound explanations and versioned case exports.
7. **Research:** public chain benchmarks, controlled synthetic cross-layer cases and real SIH-format inputs are evaluated **separately**, not pooled into fictitious real-life accuracy.

## Rejected alternatives

- *Infer wallet owners from a common observed IP*: source data proves a relay event, not ownership.
- *Create synthetic wire on real graph benchmarks and claim measured cross-layer accuracy*: fabrication.
- *Train stacking meta-model on base in-sample predictions*: leakage.
- *Use current propagation as pass-1 stack meta-feature*: circular risk.
- *Add raw Π_fee + Π_hop + Δ*: incompatible scales/units.
- *Treat absence as zero risk*: hides missing evidence.
- *Spread risk through shared exchange/ASN*: blanket false positives.
- *Assume an advanced hetero-GNN beats a simple baseline*: requires held-out evidence.

## Consequences

The platform may offer a strong chain-only baseline while research-dependent cross-layer scores abstain. Some original diagram heuristics become soft hypotheses until evidence validates them; changes must be traceable to [REQUIREMENTS_AUDIT](../architecture/REQUIREMENTS_AUDIT.md). Development must measure uncertainty, compute cost and benign false positives rather than promise all desired model claims.

**Required follow-up:** approve open decisions D01–D12 as feasible/gated; implement schema and exact join policy; record Phase 1 real input sample evidence.
