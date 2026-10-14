# CLARION v4 — Architecture completeness audit and unresolved decisions

**Status: architecture review, not implementation or evidence of model performance.** Audited against the uploaded one-page **CLARION v4 Architecture**, source sections **0–12**, and the supplied SIH26146 description. Source-derived requirements are marked **PDF**; engineering recommendations are **DESIGN**. Do not silently replace or claim to have implemented a PDF block.

## 1. Why an audit is necessary

The previous long v4 specification enumerates most components. However, multiple linked documents were empty TODO placeholders, implementation interfaces had not been agreed, and several proposed algorithms require evidence that may not exist. This document replaces the claim that "the architecture is completely ready" with explicit gates. A checked design document is not a tested running feature.

## 2. Source-traceable block matrix

| PDF block | Source requirement | Concrete required contract | Detailed document | Implementation stage |
|---|---|---|---|---|
| 0 | CSV/JSON/XML; field, clock, fee, TXID, coverage, label/dependence go/no-go | source adapters, strict schema, statistical decision report, chain-only and unsupervised routing | data dictionary; join policy | P1 |
| 1A | transaction multi-in/out, change, script weight, fee environment | transaction/UTXO/outpoint decoder and causal value-flow builder | data dictionary; component contracts | P1 |
| 1B | IP/ports/TXID, GeoIP/ASN, /24, sessionization, port entropy | typed wire observation and optional offline enrichment; absence means null | data dictionary; join policy | P1 |
| 2 | six-type evidence graph; directed timestamped edges and provenance | node/edge allowlist, valid-time snapshots, confidence *type* and evidence IDs | component contracts; architecture overview | P1 |
| 3 | chain+wire features, Node2Vec, GraphSAGE/GAT, hetero temporal message passing, link prediction | causal feature/embedding manifests, separate chain/wire views and node-level outputs | model selection; experiment plan | P2 |
| 4 | MCER H1 common input H2 change H3 embedding H4 wire conflict H5 relink; fixed point | signed pair evidence, conservative entity partitioning and lineage/confidence | MCER plan | P2 |
| 5 | peel, mixing, circular/layering and learned motif novelty | match definition, supporting UTXO witness path, service/benign controls | component contracts; experiment plan | P2 |
| 6 | four-family base learners, OOF stacking, meta-features and justified anomaly probability | fit/OOF/holdout discipline, label gate, uncertainty, unsupervised route | stacking architecture; model selection | P3 |
| 7 | Δ residual mapping CCA→contrastive, Δ1–Δ5 | paired-view eligibility, held-out residual, component diagnoses and abstention | join policy; experiment plan | P3 |
| 8 | Π fee/hop/time/frag/infra, rational minimum cost per goal | typed economic-goal and comparison baseline, independent unit-bearing components, abstention | data dictionary; experiment plan | P3 |
| 9 | separate stack/Δ/Π/pattern fusion; typology; score 0–100 P1–P4; capped pass 2 | provisional local score, frozen seed, propagation mapping, final explanation | risk propagation architecture | P3–P4 |
| 10 | six-level MLRP; causal value-weighted time/hop decay; service boundaries; deterministic vs learned | distinct financial/context channels, per-level scale, pathways and no circular risk | risk propagation architecture; component contracts | P4 |
| 11 | link analysis, heat map, timeline, SHAP, source-linked dossier, PDF/CSV | screen/API view models, access control, offline asset inventory, export hashes | investigator dashboard architecture | P4 |
| 12 | L0–L3 synthetic, legitimate service controls, per-tier precision, ARI/NMI, AUROC/AUPRC, propagation audit | independently sealed truth, temporal split, ablation matrix, bootstrap CIs and failure register | experiment plan; definition of done | P5 |

The full source-derived detail lives in [architecture-v4-spec.md](architecture-v4-spec.md). This table is an index, not a replacement.

## 3. Critical contradictions and proposed resolutions

| ID | Problem in/around the original architecture | Decision proposed (not source claim) | Validation required |
|---|---|---|---|
| C01 | §6 meta-features mention graph propagation, but §10 seeds propagation from §9 | pass-1 stack excludes current propagation; freeze seeds; only pass-2 takes bounded propagation | assert no circular dependency and no repeated score inflation |
| C02 | §10 says six risk levels but Country should never be scored | five scored levels + Country contextual sixth node level | API/UI schema and tests reject numeric Country risk |
| C03 | §1B observed-TXID relay can occur at many peers | wire observations never prove transaction origination or address owner | adversarial multi-relay, NAT, co-host, VPN fixtures |
| C04 | §4 H4 geographic/timing veto assumes controller location | mark as uncertain conflict hypothesis; do not hard-split solely on ASNs/countries | CoinJoin, timezone/clock drift and relay simulations |
| C05 | §7 premise assumes a common operator explains both chain/wire | measure whether paired views are predictive on held-out events; default ABSTAIN otherwise | dependence permutation null, capture source sensitivity |
| C06 | §8 cheapest "same outcome" cannot usually be inferred from public chain data | require verified controlled set/payees/fee conditions or item-level ABSTAIN | cost counterfactual checks and abstention rate |
| C07 | §9 suggests combining separately calibrated p-values | p-value combination requires an explicit dependency/control method; cannot naively multiply/average | separate validation, correlation, false positive audit |
| C08 | §10 money-taint diffusion includes host co-session / infrastructure | keep financial-flow and non-financial association **separate**; no host→wallet guilt propagation | no host/ASN cross-customer contamination |
| C09 | §6 "anomaly probability" when labels missing | unsupervised ranking only, never calibrated likelihood of crime | unsupervised output cannot have probability flag |
| C10 | Entity cluster is dynamic and could be trained on future edges | version as-of clusters and embeddings inside each temporal fold | future-feature leakage tests |
| C11 | graph links at address level can overstate individual UTXO flows | prefer outpoint tracking; partial reconstruction carries explicit uncertainty | value conservation and missing-prevout tests |
| C12 | GAT attention is not a causal proof | deterministic evidence path authoritative for dossiers; learned path a separate comparison | agreement, contamination, human review |

## 4. Open decisions (NOT resolved by PDF)

**D01 — Input schema and SIH capture meaning:** Are network records direct observed Bitcoin relay messages with actual TXIDs? Which Bitcoin protocol version, capture sensors, precision and permitted data? Needs genuine sample and provider documentation.

**D02 — Data availability:** Public Elliptic++/BitcoinHeist datasets do not provide authenticated wallet↔relay IP labels. Do not fabricate them. Confirm local Bitcoin Core fixture size and permitted SIH data.

**D03 — Subject-level labels:** Transaction vs address vs entity vs subgraph? Label definition, available-at time, uncertainty and independent audit must be specified per benchmark.

**D04 — Graph model capacity and compute:** Validate CPU baseline, GraphSAGE/GAT baseline and heterogeneous temporal upgrade with actual memory/time benchmarks.

**D05 — MCER constraint calibration:** Minimum positive/negative evidence, false-merge target, ambiguous state, algorithm stability and use of overlapping custody identities.

**D06 — Δ pairing and windowing:** Minimum number of *independent* chain–wire observations, dependence null model, clock tolerance and coverage gates.

**D07 — Π economic objective:** Source and confidence of intended destination and controlled set; exact fee/weight and time baselines; cannot be guessed from appearance.

**D08 — Fusion calibration and priority:** Identify independently labeled holdout, comparable evidence scale, dependence of Δ/Π/motif and P1–P4 thresholds; unresolved without labeled evidence.

**D09 — Service boundaries:** Evidence-backed allowlist/provenance, expiry/version, mixed-service uncertainty; never whitelist suspects solely by a self-declared service label.

**D10 — Security and deployment:** Linux distributions, CPU minimum, optional GPU, offline wheelhouse, local-user authorization, malicious uploads and key management requirements.

**D11 — Synthetic realism:** Sampling distributions from real chain *without* copying label leakage or claiming genuine cross-layer validity; varied generator shifts.

**D12 — Case/report integrity:** Event-time meaning, source hashes, evidence IDs, review status, PDF/CSV integrity and redaction roles.

## 5. Complete product definition of "architecture ready"

To approve **design only**, require: [ ] this matrix accepted; [ ] canonical schemas frozen; [ ] chain–wire J0–J3 join contract; [ ] typed graph and interfaces; [ ] MCER objective/constraints and confidence; [ ] stack OOF and calibration policy; [ ] Δ/Π abstention contracts; [ ] frozen-seed MLRP math and output; [ ] screen/API/export contracts; [ ] privacy/offline threat policy; [ ] each subsystem's tests and negative controls; [ ] open decisions assigned with mitigation.

**Project state:** critical decisions D01, D03, D06, D07 and D08 require evidence not contained in the PDF. No design document can truthfully certify their real-world feasibility before data inspection. Phase 1 should be allowed to run as an *evidence-gathering gate* without asserting those research hypotheses are already proven.
