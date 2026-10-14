# src/clarion/propagation/ — Architecture contract

> **Documentation-only scaffold.** No module functionality is implemented. Follow the original v4 specification and root README; file stubs are comments describing future work.

## Responsibility
Value-conserving causal forward/backward MLRP with absorbing boundaries.

## Phase ownership
P4

## Planned files and their exact responsibilities

| File | What must be written during implementation |
|---|---|
| **__init__.py** | Declare package boundary. |
| **edges.py** | Typed conductances, value share, time/hop decay. |
| **diffusion.py** | Deterministic frozen-seed bounded propagation. |
| **boundaries.py** | Services, CoinJoin, ASN/country no-reemission policies. |
| **paths.py** | Trace minimal contributing causal paths and provenance. |

## Data/interfaces
**Inputs:** Frozen preliminary seeds + typed transaction graph.

**Outputs:** Per-level risk, provenance channels, bounded paths.

## Security, testing and acceptance
Test no blanket contamination across exchanges/hosts.

For all modules: preserve provenance, causal availability, explicit uncertainty/abstention, offline operation, real tests and realistic false-positive controls. Record status in docs/progress before claiming completion.

## Implementation handoff
Do not add executable logic before the assigned phase PR; update this README when actual public interfaces, dependencies and tests are verified.

---

## Full §10 MLRP architecture contract

**Levels:** Address, Transaction, Entity, Host, ASN and Country context-only. **Equation:** r_i(k+1)=(1−α)s_i+αΣ_(j→i) w(e_ji)φ(v_ji)τ(Δt)r_j(k). s is the hashed frozen pass-1 seed; current pass-2 score cannot re-enter diffusion.

**Diagram's initial edge conductances:** spends/funds 1.0; observed-broadcast 0.6 × confidence; co-session 0.3; candidate member-of 0.8; hosted-in 0.1. Require valid time/direction, and distinguish financial value-flow from non-ownership relay context.

**Controls:** hard six-hop scoring bound; hop γ decay, temporal τ decay; value share normalization and nonamplification; absorbing exchange/custody/CoinJoin boundaries; host/ASN never re-emit to other customers; Country receives no score; separate forward taint and backward provenance. Emit path evidence and confidence, not guilt.

**Score budget:** at most 25/100 points contributed to final triage by §10; report seed, per-level exposure, incoming/outgoing shares, minimal path, time, boundary decisions and convergence/abstention flags. Compare deterministic baseline against learned GAT but deterministic evidence paths remain the dossier explanation. See [MLRP architecture](../../../docs/architecture/risk-propagation-architecture.md).
