# Multi-Level Risk Propagation (MLRP) — Detailed Score Architecture

> **Status: architecture only.** Uploaded diagram **§9–§10** calls this **risk propagation**, not a "reward" signal. The score measures auditable *exposure to a flagged path*, not reward, ownership, guilt or a claim that an address is criminal.

## 1. Exact purpose and six levels

| Level | Derived metric | Propagation semantics |
|---|---|---|
| Address | tainted depth, inbound/outbound value-share, provenance | receive/send are distinct; no automatic bad-actor designation |
| Transaction | value-weighted exposure of inputs and outputs | directed, time-valid funds flow through known prevouts |
| Entity | aggregation over candidate member addresses, own separately valid Δ/Π | MCER membership confidence, avoid blanket whole-entity spill |
| Host / IP | confidence-weighted context from transaction(s) observed relayed | only observed TXID association; **never ownership** |
| ASN | prevalence/normalization across observed hosts | contextual aggregation; **cannot re-emit** to unrelated customers |
| Country | geographic context shown in analyst UI | **never scored or re-emitted** |

Each level uses a separately documented scale, normalizer and uncertainty; do not copy transaction risk directly to hosts/ASNs/entities.

## 2. Required pass order and non-circular constraints

~~~mermaid
flowchart TD
  A["§6 OOF-trained local stack + §5 patterns + eligible Δ/Π"] --> B["§9 Pass 1: provisional LOCAL risk"]
  B --> C["Freeze hashed seed vector s and inference snapshot"]
  C --> D["§10 forward taint and backward provenance"]
  D --> E["Bounded edge-normalized causal diffusion (<=6 hops)"]
  E --> F["Top paths, exposure and degree/service-boundary audits"]
  F --> G["§9 Pass 2: local score + capped propagation prior"]
  B --> G
  G --> H["§11 lead queue, graph heat overlay and evidence dossier"]
~~~

**Never** let pass-2 results modify the seeds used for that same propagation run. Re-training learned pass-2 fusion needs chronological OOF predictions from earlier fitted models, including fold-specific MLRP.

## 3. Source equation and mathematical meaning

The uploaded diagram specifies a damped update of the form:

~~~text
r_i^(k+1) = (1 - α) * s_i
          + α * Σ_(j→i) [ w(e_ji) * φ(v_ji) * τ(Δt_ji) * r_j^(k) ]
~~~

- **s_i**: frozen §9 first-pass seed risk (not the final propagation-adjusted score).
- **α**: damping factor, configured and tested for stability.
- **w(e)**: conductance reflecting edge type and association confidence.
- **φ(v)**: fractional value share; sum allocated to receivers must not exceed source-value exposure.
- **τ(Δt)**: temporal-decay factor; causally backwards edges are disallowed.
- **k**: bounded propagation iteration or hop index; the source diagram proposes fixed-point-style power iteration and approximately 10–20 sweeps. Convergence/time budget must be measured, not promised.

### 3.1 Diagram's initial edge-conductance candidates

| Relation | Source-diagram proposal | Engineering safety policy |
|---|---|---|
| spends / funds | 1.0 | propagate value exposure only if valid time-ordered UTXO/flow evidence |
| broadcast-by (observed relay) | 0.6 × observation confidence | **separate network-context evidence**, never funds ownership; prevent host→address taint |
| co-session | 0.3 | context channel only; avoid co-session spreading alleged criminality |
| member-of | 0.8 | confidence-gated candidate membership; review before risk aggregation |
| hosted-in | 0.1 | host→ASN context only; ASN cannot re-emit |
| country | no risk conductance | display geographic context only |

**Important refinement:** rather than mixing network association risk with monetary taint, implement **two propagation evidence channels** internally: (a) chain value taint, (b) contextual/observational association strength. A combined *triage prior* may use calibrated and capped contextual strength, but cannot turn a relay or co-session into a wallet owner. The PDF's numeric conductances are **initial hypotheses for testing**, not verified posterior probabilities.

### 3.2 Proposed bounded implementation semantics

Within each as-of graph snapshot:
1. Freeze pass-1 seeds, scenario-level service tags and evidence manifest.
2. Enumerate typed causal edges; reject illegal direction and future timestamps.
3. For each source with multiple downstream recipients, allocate mass according to verified value shares of outpoints. For incomplete transaction graphs, bound shares conservatively or abstain.
4. Apply type conductance, observed evidence confidence, temporal decay, hop factor γ and non-re-emission rules.
5. Traverse at most **six hops** in the scoring graph. Beyond six, preserve *reachability* as descriptive context, not scored contamination.
6. Normalize outgoing influence so high fan-out (1-to-200) does not replicate the whole seed 200 times.
7. Compute **forward channel** ("where value flowed") and **backward provenance channel** ("what value came from") independently with their own graph semantics and directed interpretations.
8. Apply service boundaries: exchanges, custodians, CoinJoin coordinators become absorbing where supported; hosts/ASNs do not spread contamination across other customers; country is not scored.
9. Stop on documented bounded convergence/no-change tolerance and max-iteration guards; record nonconvergence and exclusions.
10. Return a per-level score, contributing source list and **minimum sufficient evidence path**. Deterministic baseline remains dossier-authoritative when it disagrees with learned attention.

### 3.3 Example calculation (illustrative, not a project result)

Suppose a frozen entity seed has local risk 0.8 and a *validated* transaction allocates 25% of traceable outflow to one downstream transaction, with a causal weight of 0.9 and time-decay 0.75. A **single-step contribution term** ignoring other incoming terms is 0.8 × 0.25 × 0.9 × 0.75 = **0.135** before global damping and per-level normalization.

This **is not** the receiving subject's final risk and is not a measured outcome. The calculation should not be reused for IP/ASN co-session edges as though they carried bitcoin value.

## 4. Risk score, propagation feature and final priority

The diagram specifies a **final risk range 0–100**, **P1–P4**, and **maximum 25 of 100 risk points from propagation**.

**Proposed auditable contract:**

~~~text
local_score_0_100       = independently validated / calibrated local triage score
propagation_exposure   = bounded contextual or value-flow signal per named channel
propagation_points     = clamp(validated_mapping(propagation_exposure), 0, 25)
final_score_0_100       = clamp(local_score_0_100 + propagation_points, 0, 100)
final_priority         = threshold_table(final_score, calibrated_for_review_budget)
~~~

This formula is an **engineering proposal**, not explicitly specified arithmetic in the PDF. Avoid treating local and propagated scores as independent calibrated probabilities; if the final scoring policy reserves 25 of 100 total points for propagation, use a consistent budget such as **local ≤75, propagation ≤25**, or separately justified rescaling before adding. Do not accidentally make it possible for propagation to dominate scores via threshold effects or repeated recomputation. In no-label mode, report **priority ranking only**, never a probability of illegal activity.

**Preferred interpretation of "propagation score":** bounded evidence exposure plus traceable contributing paths, **not a stand-alone detection verdict**.

### 4.1 Proposed output record

~~~text
PropagationResult:
  subject_id, subject_type, graph_cutoff, run_id, seed_snapshot_sha
  forward_value_exposure?, backward_provenance_exposure?
  context_association_exposure?          # source-linked relay/co-session, not wallet owner
  node_scale_version, path_hops, max_depth, damping, time_decay
  normalized_outgoing_fractions, boundary_decisions, confidence_masks
  top_contributing_seed_ids, minimal_evidence_paths, elapsed_time
  validated_propagation_points_0_25?, convergence_state
  abstain_reasons?, observations_used, risk_not_guilt_notice
~~~

### 4.2 Learned edge strengths (secondary model)

The uploaded §10D proposes a GAT-based learned attention alternative to hand-chosen conductances. Train this on **past** graph snapshots and validate against held-out evidence; measure edge-weight agreement, service spillover and calibration. The deterministic conservative evidence path remains authoritative for case reports until learned propagation passes reliability tests. Learned attention weights are not automatically causal explanations.

## 5. Mandatory safeguards and tests

- Directed causal time: no path can use an edge/feature from after cutoff; reject cycle-based amplification and graph backtracking.
- Value conservation: a split cannot replicate more influence than the mass leaving the source; property-based tests over high-degree fan-out.
- Boundaries: service and CoinJoin boundaries absorb; host/ASN/country cannot contaminate unrelated nodes.
- Seed freeze: pass-2 risk may not overwrite a frozen pass-1 seed.
- Cap: MLRP adds **at most 25/100** to the defined final score.
- False positives: contamination of legitimate one-hop neighbors evaluated by class/service cohort.
- Traceability: every nonzero contributing path contains ordered evidence IDs, timestamps, amounts where known and source confidence.
- Unknown flow: missing outpoints/fee/controlled set trigger increased uncertainty or abstention, not precise money-taint reconstruction.
- Country has **no risk score**. Distinguish inbound/outbound channels and per-level scales.

## 6. Module allocation

| Module | Role |
|---|---|
| src/clarion/propagation/edges.py | edge allowlist, conductance, value fraction, causal guard |
| src/clarion/propagation/diffusion.py | freeze seeds and bounded causal propagation engine |
| src/clarion/propagation/boundaries.py | service, infrastructure and country context safeguards |
| src/clarion/propagation/paths.py | path selection, evidence references and explanation |
| src/clarion/fusion/local.py | independently generated seed table |
| src/clarion/fusion/final.py | apply capped post-propagation adjustment once |
| src/clarion/explanations/dossiers.py | persist definitive deterministic evidence paths |
| frontend/src/features/graph/GraphPage.tsx | display level-aware risk heat overlay and selected causal path |

**Source:** uploaded CLARION v4 diagram, boxes 9, 10A–10D, 11. Risk normalization, channel separation and proposed score budgeting are engineering safeguards subject to tests, not measured results.

**Implementation folder map:** [production module structure](repository-structure.md). The path explorer is planned under frontend/src/features/graph/; these files are not yet executable.
