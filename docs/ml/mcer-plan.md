# MCER — Mutual-Constraint Temporal Entity Resolution

**Design only, not fitted or verified.** Uploaded v4 PDF §4 specifies **H1 common input, H2 change candidate, H3 graph embedding, H4 wire conflict, H5 fingerprint re-link**, iterative refinement to a stable partition, confidence, provenance and **entity ≠ person**. Engineering below preserves that order but replaces unsupported hard geographic inference with an audited soft constraint.

## 1. Inputs and trust tiers

From an as-of graph snapshot: Bitcoin input/outpoint facts (factual), address annotations (may be absent), coinjoin/service pattern cautions (heuristic), change candidates (heuristic), trained embedding similarities (model inference), true source-tagged TXID relay observations (relay fact, NOT control), and sensor clock/coverage quality.

Key data: \`AddressLinkProposal{a,b,H1..H5,cutoff,positive_score?,conflict_score?,source_evidence_ids[],confidence_kind,source_independence_id}\` and \`EntityVersion{entity_id,version,member_id,as_of,confidence,unresolved_pairs,parent_versions,reason_codes}\`.

## 2. Candidate evidence H1–H5 (same architecture families as the PDF)

**H1 Common-input:** multiple inputs in the same transaction suggest common controller under typical wallet spending, but multi-party CoinJoin, custodial aggregation, scripted collaborative spends and address/script ambiguity can invalidate it. Start positive *candidates*, not unconditional union-find closure. Unknown input address doesn't become fabricated wallet.

**H2 Change-address:** propose outputs whose script, novelty, amount, path and economic context fit ordinary wallet change; preserve alternative change assignments with score and uncertainty. Do not assume smallest output or new address means change.

**H3 Graph-ML similarity:** learn address/transaction/temporal behavior embeddings as-of cutoff. Build candidate pairs among near neighbors, constrain by evidence independence; compare graph communities or Leiden/Louvain as baselines. High cosine similarity is not verified common control.

**H4 Wire conflict/veto:** source diagram suggests >2 ASNs/countries within ~100ms supports a CoinJoin false-merge split. This is **not generally logically valid** because one TXID is relayed by many peers and endpoint geolocation/clock may be noisy. Treat it as a *conflicting observational hypothesis* requiring independently validated sensors, not a hard identity veto. A validated multi-party spending transaction provides a safer anti-merge hint.

**H5 Fingerprint re-link:** IP rotation with stable ASN, port rhythm, diurnal cycle and graph context may be evidence of operator continuity **only as a candidate**; relays, shared hosted infrastructure, NAT, VPN and temporal capture gaps are confounders. Demand multiple independent supporting facts before re-link.

## 3. Temporal optimizer (proposed)

~~~mermaid
flowchart TD
  A["As-of graph snapshot T; no future edges"] --> B["H1/H2/H3 positive pair proposals"]
  A --> C["H4/H5 uncertainty, service and conflict evidence"]
  B --> D["Evidence ledger + source independence grouping"]
  C --> D
  D --> E["Constraint-aware weighted partition, avoid forced merges"]
  E --> F{"Partition stable? Evidence contradictory?"}
  F -->|bounded refine| E
  F -->|stable / limit| G["Versioned candidate clusters + abstained links"]
  G --> H["Next T: incremental lineage and split/merge report"]
~~~

1. Create candidate pair universe with bounded neighborhood/search rules and timestamps.
2. Preserve signed evidence, not one aggregate opaque score. Suppress duplicates originating in the same model/relay sensor/path.
3. Apply **hard negative** constraints only to logically verified disjoint control facts; apply ambiguous wire/heuristic conflicts as **soft** penalties.
4. Optimize weighted partition consistency; prefer leaving an ambiguous pair separate/UNKNOWN over a high-impact false merge. Explore correlation clustering or signed modularity; use union-find only where constraints permit.
5. Recompute aggregate entity features for the new version without reusing a model's own speculative links as independent data. Iterate until partition change below a predeclared tolerance or max iterations; otherwise flag NONCONVERGED.
6. Store before/after cluster lineage (merges, splits, unchanged), exact evidence IDs, confidence band calibration source and unresolved pairs.
7. Never reassign an older historical cluster based on later information when presenting an as-of past score.

## 4. Explicit confidence and abstention

- Pair confidence only if externally calibrated against labeled **pair** truth with appropriate hard negatives; otherwise label \`heuristic_strength\`.
- Cluster confidence based on worst-supported critical merge, known-conflict count, coverage, age/window stability and independence; not simply average cosine similarities.
- An entity cluster is a candidate control hypothesis, not natural person identification.
- UNRESOLVED decision is a valid result. Reject unsupported H4 hard veto, and do not force all addresses into some multi-address entity.

## 5. Anti-feedback tests

- MCER of training fold F must use only records available at F cutoff.
- Embedding learner trained on MCER candidates must not treat these same candidates as independent verified labels in a self-fulfilling loop.
- Shared-service addresses and equal-output collaborative spending must not automatically merge.
- Multi-sensor relay appearances must not automatically split.
- Later re-link can create version N+1 without altering version N history.
- Combining 3 copies of the same underlying evidence must not triple certainty.
- Stable convergence, maximum-iteration fail-safe and deterministic seed must be measured.

## 6. Model alternatives and evaluation

**Baselines:** single-input/very-conservative common-input; proposed change heuristics; graph community baselines. **Advanced:** pairwise embedding scorer + signed-constraint temporal resolution. Track ARI/NMI, pairwise precision/recall, false-merge rate, false-split rate, instability after each snapshot and abstention, separately on exchanges, custodians, mixers/CoinJoin, ordinary multi-input spending.

**Phase 2 exit:** each cluster displays a witness path and conflicting evidence, full version lineage, test results and unknown memberships. Cross-layer benefit only claimed if observed wire pairs were validated under the [join policy](../data/join-policy.md).
