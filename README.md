# CLARION v4
## Offline AI-Powered Monitoring and Investigation of Bitcoin Transaction Traffic

**Project:** Smart India Hackathon 2026 — SIH26146  
**Problem owner:** National Technical Research Organisation (NTRO)  
**Theme:** Blockchain & Cybersecurity  
**Target platform:** Linux; entirely offline at inference and investigation time  
**Repository status:** **ARCHITECTURE / IMPLEMENTATION PLAN ONLY.** This README defines what must be built. It does not claim that any application, model, dataset, dashboard, benchmark, or test already exists in this repository.

> **Mission:** Transform bulk, locally supplied Bitcoin blockchain and P2P-network metadata into reproducible, uncertainty-aware, prioritized investigative leads. CLARION identifies patterns and connections for review; an anomaly or network correlation is **not** proof of crime, wallet ownership, or real-world identity.

**Architecture source of truth:** the uploaded *CLARION v4 Architecture* diagram (sections 0–12), together with the SIH26146 problem statement supplied for this project. The problem statement refers to an additional “AI/ML Focus Areas” table that was not supplied; no requirements from that table are assumed here. This README is the intended implementation contract, not evidence of completed work. Architecture changes require a documented decision and corresponding tests.

---

## 1. Goals, scope, and non-negotiable rules

### 1.1 Required final capabilities

1. Import bulk CSV, JSON, and XML files containing transaction, address, amount, time, and available network metadata.
2. Normalize and validate chain and wire data without inventing cross-layer associations.
3. Build a typed, directed, temporal **cross-layer evidence graph** with provenance and uncertainty.
4. Create interpretable chain/wire features and learned graph embeddings.
5. Infer **candidate** address/entity groups with Mutual-Constraint Entity Resolution (**MCER**), confidence, and reasons.
6. Detect transaction motifs, including peel-chain candidates, unusual fan-in/out, mixing-like patterns, circular flows, and layering.
7. Train and evaluate actual AI/ML anomaly detectors, combining heterogeneous base learners with a leakage-safe stacked meta-model where labels support it.
8. Produce **cross-layer divergence (Δ)** and **obfuscation expenditure (Π)** as distinct, interpretable signals; abstain where their assumptions fail.
9. Fuse local evidence into prioritized risk, apply bounded Multi-Level Risk Propagation (**MLRP**), and perform a controlled second-pass re-ranking.
10. Provide an offline investigator dashboard, temporal link analysis, explanations, provenance, and CSV/PDF case export.
11. Benchmark with reproducible synthetic truth, legitimate-service controls, temporal testing, ablations, and explicitly documented limitations.

### 1.2 Explicit non-goals

- No live blockchain service, online geolocation service, blockchain explorer, cloud model API, or mandatory internet connectivity during inference.
- No unsupported mapping from a relay IP address to the owner of a transaction or Bitcoin address.
- No automatic accusation, de-anonymization of a person, or inference that CoinJoin/privacy use is criminal.
- No “98% accuracy” or similar performance claim without a specified, independently evaluated dataset and split.
- No substitute rule-only detector presented as trained AI; rules are an interpretable baseline and supplementary evidence.
- No fake dataset labels silently treated as verified real-world incident labels.
- No assumption that a conventional multi-input heuristic always establishes common ownership.

### 1.3 Core forensic invariants

- **Provenance first:** every record, inferred edge, cluster decision, anomaly, and propagated path points to source evidence, algorithm version, and processing run.
- **Temporal causality:** features, joins, model splits, and propagation obey event-time order; observation time and block time are different concepts.
- **Association is not attribution:** TXID-linked P2P relay evidence implies observation of propagation, not that a host originated a transaction or controls its addresses.
- **Confidence is typed:** distinguish a model score, calibrated probability, association confidence, uncertainty interval, and data-coverage indicator.
- **Abstention is an output:** if cross-layer support, labels, economic objectives, or calibration are inadequate, return an explicit unavailable/abstained result and the reason.
- **Privacy is not guilt:** protect legitimate exchanges, custodians, payment processors, mobile wallets, VPN users, and CoinJoin participants from automatic blanket alerts.
- **Reproducibility:** datasets and models are locally versioned; seeds, parameters, environment, split boundaries, and hashes are recorded.

---

## 2. Complete architecture overview

CLARION v4 retains the original architecture's three scoring views over one shared graph: graph-informed stacking, cross-layer divergence Δ, and execution-cost expenditure Π. The final output is a **ranked lead with evidence**, not merely an anomaly label.

~~~mermaid
flowchart TD
    A["0. Readiness: CSV / JSON / XML, validation, provenance"] --> B["1A. Blockchain processing"]
    A --> C["1B. Network processing"]
    B --> G["2. Heterogeneous temporal evidence graph"]
    C --> G
    G --> F["3. Features + shared graph representation learning"]
    F --> E["4. MCER entity-resolution loop"]
    E --> G
    F --> M["5. Pattern and motif engine"]
    F --> S["6. Base ML models and out-of-fold stacking"]
    F --> D["7. Cross-layer divergence Δ"]
    F --> P["8. Obfuscation expenditure Π"]
    M --> U["9. Pass 1: calibrated local evidence fusion"]
    S --> U
    D --> U
    P --> U
    U --> R["10. MLRP: frozen seeds, bounded causal diffusion"]
    R --> V["9. Pass 2: capped, non-circular final fusion"]
    U --> V
    V --> I["11. Offline dashboard and evidence dossiers"]
    I --> T["12. Evaluation, ablations, reproducibility"]
    A -. "insufficient wire quality: chain-only" .-> B
~~~

**Important sequencing correction:** the source diagram lists graph-propagation scores among possible stacking meta-features while also seeding propagation from fused model output. To avoid circular dependence, **pass 1 must not depend on pass-1 propagation**. Train pass-1 models from data available at their prediction time, freeze the provisional seeds, run propagation once, and only then use a **capped** propagation feature in pass 2. Any learned pass-2 method must also be fitted with time-respecting out-of-fold propagated features; otherwise use a documented deterministic cap.

### 2.1 Architecture-block traceability

| Block | Design unit | Planned outputs | Key acceptance condition |
|---|---|---|---|
| 0 | Data readiness & cross-layer validation | normalized records, audit, routing decision | malformed data rejected; uncertain joins not fabricated |
| 1A | Blockchain layer | parsed inputs/outputs, transaction metadata | integer satoshis, valid value-flow semantics |
| 1B | Network layer | parsed observations, sessions, offline enrichment | source fields and time uncertainty preserved |
| 2 | Evidence graph | temporal typed nodes/edges + provenance | six canonical node types and bounded evidence associations |
| 3 | Features & representation learning | chain/wire features and embeddings | leakage-safe baseline and graph-ML comparisons |
| 4 | MCER | candidate entity partitions and confidence | false-merge audit and constraint rationale |
| 5 | Pattern engine | pattern instances and supporting subgraphs | pattern tests include benign counterexamples |
| 6 | Stacked anomaly detection | base scores, meta-score, calibration | chronological OOF; no trained-probability fiction |
| 7 | Δ engine | divergence components, uncertainty, abstention | meaningful chain–wire pairs required |
| 8 | Π engine | itemized economic-cost differences | economic objective/baseline justified or abstain |
| 9 | Fusion | provisional and final lead risk, typology, priority | Δ and Π not summed as raw, incompatible quantities |
| 10 | MLRP | forward/backward risk, paths and exposure | causal, non-amplifying, service-boundary aware |
| 11 | Investigator console | graph views, timeline, dossier, exports | fully local, every lead traceable |
| 12 | Validation | metrics, ablations, control-group failures | temporal holdout + legitimate-user FP analysis |

---

## 3. Data contracts and storage design

### 3.1 Supported inputs

**Transaction record:** transaction identifier (TXID); available event timestamp and its meaning; input address list; output address list; corresponding input/output amounts; transaction fee; script types where present; optional block height and block timestamp; optional output index, sequence/locktime, confirmation and virtual size/weight. A transaction may have multiple inputs and outputs.

**Network observation:** observation ID; capture timestamp with time zone and precision; source/destination IP and port; observed TXID **only when actually present in source data**; observation kind/direction; capture sensor and source file; optional session ID, protocol, country/ASN and uncertainty metadata. A network observation must not be treated as blockchain spending evidence.

**Ground-truth/label table:** subject ID (transaction, address, entity, or scenario); label and label semantics; valid observation date; provenance (synthetic, confirmed, unverified); annotator/source; confidence; and split eligibility. Labels remain isolated from feature generation and investigator predictions.

**GeoIP/ASN resources:** locally supplied licensed/offline country and ASN databases with version, date and coverage metadata. Enrichment is optional; absent lookups remain unknown rather than guessed.

**Economic objective table for Π:** where available, independently supported controlled-set assumptions, intended payee(s), settlement window, allowed constraints, fee environment, and baseline method. Unidentifiable goals do not receive Π numbers.

### 3.2 Canonical normalized records

All normalized tables must have a common **run_id**, immutable source reference, ingestion timestamp, parser/schema version, event-time field(s), missingness flags, and row-level validation state.

| Table | Primary keys / fields |
|---|---|
| transactions | txid, block_height?, event_time?, block_time?, fee_sats?, vsize?, script_summary? |
| transaction_inputs | txid, vin_index, previous_outpoint?, address?, amount_sats?, script_type? |
| transaction_outputs | txid, vout_index, address?, amount_sats, script_type? |
| network_observations | observation_id, observed_at, src/dst IP/port, observed_txid?, sensor_id, accuracy |
| network_sessions | session_id, endpoint pair, start/end, count, capture provenance |
| enrichment | IP, offline ASN/country, database version, lookup status |
| entity_candidates | candidate_id, address membership, method, supporting/conflicting evidence |
| graph_nodes / graph_edges | stable IDs, type, time, confidence, provenance, graph-window version |
| labels | subject_id, level, class, source, certainty, effective_at |
| investigation_results | subject_id, model/run IDs, scores, abstentions, evidence paths |

**Money:** use exact integer **satoshis** internally. Reject silently rounded floating-point amounts. **Time:** store UTC plus source precision and whether a value is observation time, first-seen time, block time, or synthetic time. **Identifiers:** preserve stable Bitcoin TXID and outpoint semantics; provide an explicitly marked synthetic-ID mode only for generated examples. **Nulls:** missing does not mean zero.

### 3.3 Required ingestion and join checks

1. Validate CSV/JSON/XML structures and arrays; reject invalid ports, IPs, amounts and impossible timestamps with row-specific diagnostics.
2. Detect duplicates, contradictory TXIDs, missing values, monetary/fee inconsistencies, and reusable UTXO outpoint conflicts when sufficient information is supplied.
3. Quantify field availability and source-specific sampling bias; record any corrected or dropped rows.
4. Join wire records to transactions **only by observed exact TXID** or another explicitly recorded and reviewed evidence mechanism; never by amount/timing/IP proximity alone.
5. Validate event-time ordering using the capture's time precision and clock-skew budget; avoid assuming block inclusion time equals transaction broadcast time.
6. Calculate coverage, valid join rate, uncertainty and chain–wire dependence using train-window-only statistical tests (e.g., permutation-validated mutual information where adequate observations exist).
7. Record explicit **GO_CROSS_LAYER**, **CHAIN_ONLY**, or **INSUFFICIENT_DATA** routing with reasons. Also record **SUPERVISED_ALLOWED** vs **UNSUPERVISED_ONLY** from a separate label audit.
8. Include adversarial quality fixtures: repeated relays, forwarded TXIDs, NAT, misaligned clocks, malformed fields, duplicate captures and spurious correlations.

**Go/no-go policy:** thresholds and significance tests must be pre-registered in configuration and examined under coverage/sensitivity analyses. No single arbitrary mutual-information threshold proves a real-world link.

### 3.4 Offline storage

Use **Parquet** for immutable normalized/batch artifacts and **DuckDB** for fast local queries and repeatable SQL. Use deterministic, time-partitioned graph edge/node tables as the system of record; convert selected windows to in-memory/network or tensor graphs for algorithms. Data snapshots are content-hashed. UI caches and model checkpoints are rebuildable and never overwrite raw evidence.

---

## 4. Blockchain and network processing

### 4.1 Blockchain chain layer (1A)

- Parse multi-input/multi-output transactions; model address → transaction spending and transaction → address funding as **directed, value-bearing edges**.
- Prefer UTXO-level outpoints for exact flow tracking when supplied. When only address-level bulk metadata exists, mark attribution of exact coin flow as **approximate**.
- Derive input/output count, value sums, fees, script-type distribution, apparent change candidates, address reuse, value velocity, fan-in/out, amounts and temporal burst characteristics.
- Derive per-window fee environment and script weight only from supported data; do not invent weight from an absent script.
- Keep uncertainty around change outputs, shared custody, and CoinJoin-like transactions.

### 4.2 Network wire layer (1B)

- Normalize source/destination hosts, ports, observations and TCP-like sessions; preserve source sensors and time windows.
- Derive prefix (/24 for IPv4 as a feature, with separate IPv6 handling), ephemeral-port entropy, session burstiness, inter-arrival statistics, country/ASN stability, host type where evidence exists, and daily activity rhythms.
- Perform local GeoIP/ASN lookup only with a versioned offline file. **Geography is context, not asserted physical location or identity.**
- Model host-host co-session observations and host/transaction **observed-broadcast** edges with time and confidence; multiple peers can relay a single TXID.
- Do not assume VPN, Tor, hosting provider, NAT, or changing IPs indicate suspicious behavior without validated contextual features.

---

## 5. Shared heterogeneous temporal evidence graph (2)

**Canonical six node types:** **Transaction, Address, Entity, Host/IP, ASN, Country**. Session identity is represented in the network observation/session tables and edge evidence; adding a seventh persistent node type requires an architecture decision.

**Edges:** spends, funds, observed-broadcast (TXID evidence), co-session, hosted-in/geo-located, and member-of candidate entity. Each edge has stable ID, direction, observation/effective time, evidence source, method, uncertainty/confidence, and optional value share.

**Graph windows:** maintain event-level records, daily/weekly snapshots, and time-windowed training views. Learned representations and query results must be derived from the appropriate time cutoff; no full-future graph during historical evaluation.

**Graph outputs:** typed node/edge tables, graph snapshot manifest, chain-only view, wire-only view, cross-layer view, neighborhood query service, and reproducible graph hashes.

**Graph privacy principle:** a Host—Transaction observation is *not* a Host—Address or Host—Entity ownership edge.

---

## 6. Feature engineering and graph representation learning (3)

### 6.1 Hand-built interpretable feature families

- **Chain features:** in/out degree, centrality, reuse, fan-in/fan-out, flows, fee/weight, roundness, balance proxies, burst/dormancy, path depth and motif indicators.
- **Wire features:** ASN and network-prefix stability, dispersion, endpoint/port behavior, session duration, inter-arrivals, diurnal patterns and local enrichment flags.
- **Temporal features:** time-window velocity, rolling-window changes, shift/dormancy and causally ordered neighborhood exposure.
- **Uncertainty features:** percentage of joined events, timestamp uncertainty, enrichment availability, address-control ambiguity and source sensor coverage.
- **Boundary/context features:** known legitimate service categories and privacy-sensitive patterns, without letting assumed service labels become ground truth.

Every feature must document: subject level, formula or learning method, units, data requirements, causal availability, missing-value fallback, provenance and potential leakage.

### 6.2 Representation-learning ladder

1. Non-learned graph statistics and **random-walk / Node2Vec** baselines.
2. Inductive **GraphSAGE** and graph-attention **GAT** encoders on valid graph snapshots.
3. Typed, heterogeneous and temporally aware message passing over chain and **supported** wire associations.
4. Self-supervised masked-feature reconstruction, edge reconstruction and contrastive views as applicable.
5. Optional link-prediction head for *association candidates*, explicitly **not** ownership conclusions.

Produce versioned address/transaction/entity/subgraph embeddings and chain/wire feature views. Shared embedding size and alignment rules must be versioned. Compare against chain-only embeddings to establish the incremental utility of wire data.

**Fallback:** when cross-layer quality fails, graph training and inference run on the validated **chain-only graph** with missing wire features masked; do not synthesize fictitious pairings.

---

## 7. Mutual-Constraint Entity Resolution — MCER (4)

Entity resolution outputs **hypothetical groups of addresses under common control** with uncertainty; an entity ID is not a real person.

- **H1 — Co-spend proposal:** use common-input evidence with conservative multi-party/CoinJoin exclusion rules.
- **H2 — Change candidates:** score address/script/amount/context evidence, retaining competing alternatives.
- **H3 — Embedding similarity:** use GraphSAGE/GAT or graph-baseline similarity plus behavioral features; compare Leiden/Louvain where valid.
- **H4 — Wire conflict review:** conflicting wire evidence can reduce confidence or trigger review, but relayed TXIDs, rapid multi-country sightings, NAT, and routing artifacts **cannot automatically prove** distinct controllers or justify an unconditional hard split.
- **H5 — Fingerprint re-link:** propose re-links from stable behavior and local network patterns only when source independence and confounders are evaluated.

**Mutual-constraint iteration:** propose → score evidence → detect contradictions → split/merge cautiously → re-evaluate → stop on stable assignments, a fixed iteration limit, or unresolved conflict. Preserve before/after partitions and each changed decision. Guard against self-reinforcing loops where a model is trained on clusters that it then treats as independent truth.

**Evaluation:** adjusted Rand index (ARI), normalized mutual information (NMI), pairwise precision/recall, **false-merge rate** (highest priority), abstention and uncertainty by type of service or scenario.

---

## 8. Transaction pattern and motif engine (5)

**Defined motifs:** peel-chain candidates (dominant continuing output plus smaller exit), high fan-in and fan-out/mixing-like transactions, rapid multi-hop layering, circular flows, repeated funding patterns, transaction bursts and interaction with a *locally supplied and provenance-checked* known-service indicator.

**Learned discovery:** temporal motif counts, subgraph-embedding similarity, deviations from benign-window profiles, graph novelty search and pattern prototypes.

For every pattern instance return pattern ID/type, subject IDs, time interval, supporting node/edge path, amounts where supported, evidence confidence, benign alternatives and reason for a score. A pattern is not a definitive laundering verdict.

**Required negative controls:** legitimate exchange batching, coin consolidation, custodial movements, payment processors and CoinJoin participation.

---

## 9. Stacked anomaly detection (6)

### 9.1 Model families

| Family | Planned candidates | Role |
|---|---|---|
| Interpretable rule baseline | explicit pattern/behavior scores | transparent comparator, never marketed as learned ML |
| Supervised classic ML | logistic regression, random forest, optional LightGBM | predict risk only from verified eligible labels |
| Unsupervised ML | Isolation Forest, One-Class SVM, Gaussian Mixture; DBSCAN/hierarchical novelty where useful | novelty ranking when labels absent |
| Graph-ML | GraphSAGE/GAT heads, embedding novelty, temporal GNN where justified | exploit graph and temporal structure |
| Meta-learner | regularized logistic regression; optional LightGBM | combine eligible, leakage-safe base predictions |

### 9.2 Training discipline

- Establish simple chain-only and interpretable baselines first, then justify every additional model with measured incremental value.
- Separate by **chronological data cutoffs**, with appropriate gap/purge rules and grouped-scenario/entity sensitivity checks. Fit feature normalization, graph embeddings, cluster assignments, imputation and feature selection **inside each training fold**.
- Use **expanding-window, time-respecting out-of-fold predictions** to fit supervised stacking; use later untouched holdouts for evaluation.
- Never include final labels, incident annotations, future graph edges, or test period activity in training-period representations.
- Keep Δ components, Π bills and motif evidence as separately named meta-features. Do not feed a propagation value that depends on the current unvalidated local prediction back into that prediction.
- Calibrate a probability only when adequate independent, representative labels/calibration sets exist. Use split/conformal prediction intervals or sets only where their assumptions and coverage can be tested.
- With unusable labels, run a documented **unsupervised multi-detector stack** returning novelty ranking and uncertainty, **not** a calibrated criminal probability.

**Model artifacts:** feature schema and version; model family and hyperparameters; fitted preprocessors; time splits; training data fingerprint; metrics; calibration information; known applicability limits; offline load and inference compatibility.

**Metrics:** precision/recall/F1 at investigator-relevant alert budgets, AUROC/AUPRC where labels support them, precision@K, per-tier/per-category false positives, calibration error and uncertainty coverage. Synthetic scores are never represented as operational performance.

---

## 10. Cross-Layer Divergence — Δ (7)

**Question:** when reliable chain–wire pairs are observed, how inconsistent are the behavioral representations of those two layers?

**Baseline:** carefully validated paired-view correlation or canonical correlation analysis (CCA), with train-only normalization and held-out residuals. **Advanced:** graph-encoder/contrastive alignment using only trustworthy pairs. Output a normalized residual/novelty measure and component explanations, not a claim of identity mismatch.

The PDF proposes five interpretable Δ families:

- **Δ1 Sybil collapse:** many chain identities apparently associated with the same infrastructure — account for shared services.
- **Δ2 Identity spray:** a candidate entity appears across dispersed hosts — account for relays, VPNs, NAT and capture bias.
- **Δ3 Machine rhythm:** different temporal patterns across observed chain/wire activity — test precision and sampling artifacts.
- **Δ4 Route inconsistency:** incompatible timing/geography assertions — only assert when clock/location uncertainty and network delays can actually support it.
- **Δ5 Infrastructure reuse:** apparently unrelated chain groups share infrastructure — retain alternative explanation of hosting/custody/relays.

**Prerequisites:** enough independent, correctly timestamped, joined observations and evidence of non-spurious chain–wire dependence. Do not score Δ from geographical intuition alone.

**Output contract:** Δ available flag; residual; named components; sample/coverage counts; uncertainty; counterevidence; abstention reason. A consistent cover story can produce low Δ: that is an explicit blind spot.

---

## 11. Obfuscation Expenditure — Π (8)

**Question:** relative to a defensible minimum-cost alternative achieving the **same established economic objective**, how much observable fee, time, transaction complexity or infrastructure expenditure occurred?

**Itemized components:**

- **Π_fee:** observed fee expenditure minus a defensible fee/weight baseline, in satoshis; require local fee environment and justified comparison.
- **Π_hop:** unnecessary additional transaction hops under stated feasible transfer constraints.
- **Π_time:** settlement delay premium relative to an agreed time baseline, with on-chain timing uncertainty.
- **Π_frag:** extra outputs/addresses beyond verified payee requirements, if payees and controlled sets are actually known.
- **Π_infra:** infrastructure cost/dispersion proxies only when observed and independently distinguished from Δ2; usually missing in a basic SIH dataset.

**Hard abstention rule:** if the economic goal, controlled set, destination, fee environment or comparison constraints cannot be supported, report component-level or overall **ABSTAIN**, not invented numerical cost.

Keep Π **signed where appropriate** (e.g., batching may be cost-saving), itemized with physical units and independent evidence. If a later model needs a scaled premium, train and validate that transformation; **never add raw Π to raw Δ**. Spending on privacy does not establish illicit intent.

---

## 12. Fusion, typology and calibrated triage (9)

### 12.1 Pass 1 — local risk

Consume eligible base/meta anomaly outputs, pattern evidence, Δ components and Π components. Apply individually documented calibration or comparable evidence transformations **only where their prerequisites hold**. Unavailable signals remain missing with explicit gating; they are never replaced by arbitrary zeros implying innocence.

Produce:
- provisional risk score or rank appropriate to calibration state;
- Δ and Π as **separate explanatory axes**;
- category/quadrant description with low/high thresholds justified against control groups;
- confidence/uncertainty, evidence sources and priority P1–P4;
- investigator-friendly explanation of the strongest contributors and benign alternatives.

### 12.2 Π–Δ typology

| | Low Π | High Π |
|---|---|---|
| **High Δ** | inconsistent but inexpensive behavior; investigate context | expensive behavior with cross-layer mismatch; investigate |
| **Low Δ** | relatively ordinary/consistent behavior | deliberate privacy expenditure can fit; do **not** presume illicitness |

High/low classifications apply only when **both** axes are valid and separately normalized. Otherwise use **typology unavailable**. Investigative priority is calibrated against legitimate-user false positives, not a claim of adversarial motive.

### 12.3 Pass 2 — after bounded propagation

Freeze the complete pass-1 seed table. Run MLRP using those seeds only. Re-rank from pass-1 signals plus **at most 25/100 points** attributable to propagation. Prevent a subject's own propagated result from flowing back into its seed. Record base, propagated contribution, final score, uncertainty and exact justification; if no calibrated probabilities exist, present the output honestly as a prioritization score.

---

## 13. Multi-Level Risk Propagation — MLRP (10)

Risk/exposure is evaluated at **Address, Transaction, Entity, Host, ASN**, with **Country shown as context only and never scored**.

**Baseline mechanism:** bounded, causally forward, edge-type-aware and value-share-normalized diffusion with explicit damping, temporal decay, hop decay (default target: hard six-hop cap), and service boundaries. For exact UTXO availability, propagate value shares; for address-only aggregates, report additional uncertainty and conservative bounds.

**Two separate channels:** (a) **forward taint/exposure** — where observed value moved; and (b) **backward provenance** — where observed value originated. Never merge their meanings.

**Anti-amplification:** outgoing influence is allocated rather than replicated; high-degree hosts and ASNs cannot re-radiate contamination; known exchanges/custodians and CoinJoin coordinating services become explicitly recorded absorbing boundaries where justified. Stop cycles via time ordering, damping, visited-path controls and fixed-point convergence limits.

**Graph-learned alternative:** explore attention-based edge weights, but the deterministic audited propagation remains the dossier's authoritative path explanation until the learned version is independently validated.

**Outputs:** per-level exposure on separately defined scales, forward/backward shares, influence indicators, top contributing frozen seed(s), minimal sufficient causal path, hop count, time elapsed, value fractions, confidence and boundary decisions. Propagated exposure is **a reason to review a connection**, not a finding of wrongdoing.

---

## 14. Investigator application and evidence dossiers (11)

### 14.1 Offline investigator experience

- **Investigation overview:** data readiness; chain-only/cross-layer mode; label/model quality; sample/coverage status; priority P1–P4 counts.
- **Lead queue:** sorted transaction/entity leads, search, filters, confidence, signal availability and review state.
- **Graph explorer:** typed chain/wire layers, link confidence/provenance, selected time-window overlay, zoomed relevant subgraph and connection-path tracing.
- **Transaction-flow timeline:** amount, hops, fees, observation times and causality; warnings when UTXO-level linkage is unavailable.
- **Entity investigation:** candidate cluster, competing cluster hypotheses, MCER decisions, risk and legitimate-service context.
- **Δ/Π panel:** individual evidence components, abstentions, Π bill by unit, Π–Δ quadrant only when valid.
- **MLRP tracing:** seed, forward/backward risk channel, bounded graph path, value shares and protected service boundaries.
- **Explainability and comparison:** model contributions (e.g., SHAP when supported), chain-only counterfactual/ablation, model version and data limitations.
- **Export:** standalone local case dossier (PDF/CSV/JSON), including evidence references, hashes, versioned assumptions, uncertainty, investigator annotations and non-attribution warning.

### 14.2 Suggested technology and runtime

**Backend:** Python/FastAPI, local job runner, DuckDB/Parquet, typed schemas, immutable generated artifacts. **Frontend:** React/TypeScript with local bundled graph/timeline visualization (e.g., Cytoscape.js); no external fonts, maps, APIs, CDNs or third-party runtime calls. **Optional PDF export:** local PDF library. **Network binding:** localhost by default, documented authentication/security requirement before any remote use.

### 14.3 Planned API contract families

- Run management and readiness: dataset inspection, ingest job, validation decision, execution status.
- Graph: time-bounded neighborhoods, node/edge evidence, transaction value paths, temporal graph slices.
- ML: local model registry, approved training/evaluation runs, offline inference summaries.
- MCER: candidate groups, evidence decisions, merge/split history.
- Patterns/Δ/Π: per-subject components, available/abstain reasons, supporting records.
- Leads/MLRP: ranked results, risk channels, seed/path explanations and boundaries.
- Cases: annotations, immutable result snapshots, PDF/CSV/JSON export and manifest verification.

Final endpoint names, DTOs, pagination limits and authentication are to be frozen as versioned OpenAPI contracts before frontend implementation.

---

## 15. Offline application architecture and technology plan

| Layer | Preferred implementation | Notes |
|---|---|---|
| Python runtime | Python 3.11 or 3.12 | pin and test exact versions |
| Schemas | Pydantic or dataclass/Arrow-compatible contracts | fail closed on required evidence |
| Batch data | Polars or pandas + PyArrow | benchmark memory/performance before final choice |
| Analytical persistence | DuckDB + Parquet | local, portable and partitioned |
| Traditional graph algorithms | NetworkX for small fixtures, scalable alternatives for larger windows | isolate backend behind graph interface |
| ML baselines and calibration | scikit-learn | CPU-compatible |
| Advanced classifiers | LightGBM (optional) | license/build compatibility audited |
| Graph representation | PyTorch + PyTorch Geometric | offline wheels and CPU fallback |
| Temporal/heterogeneous GNN | PyG heterogeneous message passing / temporal extension | version and memory requirements must be tested |
| Clustering and graph communities | Leiden/Louvain where suitable | constraints override naive similarity |
| Investigator backend | FastAPI | local-first |
| Investigator UI | React + TypeScript | static assets bundled locally |
| Visualization | Cytoscape.js or equivalent bundled library | limit graph sizes and paginate |
| Tests and reproducibility | pytest, ruff, mypy, GitHub Actions | CI is development-time, not inference-time |
| Deployment | Linux virtual environment and/or local container | pre-downloaded dependencies, weights and GeoIP DB |

**Decision rule:** these libraries are recommended starting choices, not a substitute for compatibility, performance, license, offline-package and GPU/CPU verification. Isolate them behind interfaces so a backend can be replaced without changing evidence semantics.

### 15.1 Inference profiles

- **Minimum:** Linux CPU, chain-only mode, classic features, deterministic motifs and baselines, local dashboard.
- **Standard:** Linux CPU or CUDA GPU, full graph pipeline where quality permits, batch GNN inference and dashboard.
- **Training:** optional CUDA GPU for advanced GNNs, with resumable checkpoints; all datasets and downloaded weights are prepared *before* offline deployment.
- **Graceful degradation:** unavailable optional dependencies, labels, GeoIP, joined wire fields or economic-cost evidence disable **specific** features rather than causing fabricated outputs.

---

## 16. Proposed repository layout (planned; not implemented)

~~~text
CLARION/
├── README.md                         # this architecture and delivery contract
├── pyproject.toml                     # planned
├── configs/                           # profile, risk, gating, model configs
├── schemas/                           # machine-readable, versioned data contracts
├── src/clarion/
│   ├── ingestion/                     # CSV/JSON/XML, validation, provenance
│   ├── chain/                         # transactions, outpoints, fee context
│   ├── wire/                          # sessions and local GeoIP/ASN
│   ├── readiness/                     # coverage, dependence, routing decisions
│   ├── graph/                         # temporal heterogeneous evidence graph
│   ├── features/                      # causal chain/wire/graph features
│   ├── representation/                # random-walk, GraphSAGE, GAT, temporal
│   ├── entity_resolution/             # MCER and confidence history
│   ├── patterns/                      # motifs, graph novelty
│   ├── detection/                     # supervised/unsupervised stacking
│   ├── divergence/                    # Δ and paired-view residuals
│   ├── expenditure/                   # Π components and abstention
│   ├── fusion/                        # passes 1 and 2, calibration
│   ├── propagation/                   # bounded forward/backward MLRP
│   ├── explanations/                  # feature, path, attribution details
│   ├── evaluation/                    # metrics, leakage audits, ablations
│   ├── synthetic/                     # L0–L3 generation and truth ledger
│   ├── api/                           # offline API and job control
│   └── cli/                           # offline workflows
├── frontend/                          # offline investigator web interface
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── leakage/
│   ├── adversarial/
│   ├── offline/
│   └── e2e/
├── docs/                              # ADRs, data dictionary, runbooks
├── scripts/                           # packaging/reproducibility helpers
├── sample_data/                       # safe, small synthetic fixtures
└── .github/workflows/                 # lint, tests, audit (planned)
~~~

**Never commit** confidential third-party captures, private credentials, real personal investigative case data, unlicensed GeoIP files, large training data or trained binaries by default. Use manifest references and hashes.

### 16.1 Planned reproducible artifact layout

~~~text
runs/<run_id>/
  manifest.json                        # inputs, code, model and config fingerprints
  readiness_report.json
  normalized/                           # typed Parquet tables
  graph/                                # nodes, edges, temporal snapshots
  features/                             # feature matrices and dictionaries
  models/                               # locally serialized compatible weights
  entities/                             # MCER candidates and decisions
  patterns/                             # supporting motif instances
  divergence/                           # Δ scores and abstentions
  expenditure/                          # Π bills and abstentions
  predictions/                          # OOF and held-out results
  risk/                                 # pass-1 seeds, propagation, pass-2
  leads/                                # ranked evidence-based leads
  dossiers/                             # PDF/CSV/JSON exports
  evaluation/                           # metrics, ablations and negative controls
~~~

---

## 17. Data, model, and investigator workflow

**User flow:** (1) load local dataset → (2) inspect schema/coverage and quality → (3) receive chain-only/cross-layer and supervised/unsupervised routing decision → (4) choose or train eligible local model on authorized training data → (5) run frozen offline investigation → (6) inspect evidence and uncertainty → (7) export reproducible dossier.

**Training flow:** validate timestamp meaning and label provenance → build chronological folds → fit fold-specific preprocessing/features/embeddings/MCER candidates → train and score base models OOF → fit eligible meta-model → validate/calibrate on independent later data → run Δ/Π where feasible → freeze model/version → evaluate dedicated temporal holdout and legitimate controls → publish local model manifest.

**Inference flow:** load immutable raw file(s) → validate and hash → normalize chain/wire → quality gates → graph/snapshots → features/embeddings → MCER and motifs → model outputs → Δ and Π with abstention → pass-1 fusion → frozen-seed propagation → capped pass-2 fusion → dashboard and dossiers. No hidden runtime download or network request.

**Research flow:** compare chain-only vs +wire vs +graph ML vs +MCER vs +Δ vs +Π vs +MLRP; run targeted ablations to distinguish incremental signal from complexity and leakage.

---

## 18. Synthetic dataset and evaluation program (12)

### 18.1 Synthetic truth and behavior tiers

Build a seed-controlled data generator with a **separate ground-truth ledger** describing controlled addresses, economic intent (when known), origin/capture relationships, transaction paths, labels and observation uncertainties.

**L0:** plain transfers with minimal privacy effort; **L1:** simple address changes and ordinary transaction splitting; **L2:** more sophisticated multi-hop or coordinated behavior; **L3:** carefully controlled synthetic concealment strategies. These are evaluation scenarios, **not** assumptions about specific real users.

Generate benign hard negatives: exchange batching, legitimate consolidation, hosted infrastructure, custodial transactions, payment processors, CoinJoin users, VPN/mobile users, clock errors, missing wire, relayed TXIDs and misleading geography. Vary class prevalence, scale, noise and censoring, rather than allowing easy generator fingerprints.

### 18.2 Scientific evaluation

| Subsystem | Metrics / tests |
|---|---|
| Ingestion/correlation | valid parse %, duplicates, join precision on synthetic truth, coverage, time-uncertainty errors |
| Graph/representation | snapshot stability, embedding reproducibility, link prediction under honest evidence |
| MCER | ARI, NMI, pairwise precision/recall, false-merge/split by scenario |
| Motifs | event precision/recall, valid supporting paths, benign false positives |
| Supervised detection | PR-AUC, ROC-AUC, precision@K, recall/F1, calibration, held-out error |
| Unsupervised detection | ranking precision@K against separately held synthetic truth; do not claim calibration |
| Δ | residual behavior vs true controlled pair/coverage, abstention and spurious-correlate robustness |
| Π | correctness of itemized accounting, sensitivity to baseline, abstention rate |
| Π–Δ crossing hypothesis | assess whether better synthetic operational discipline reduces Δ and increases Π; do not assume |
| MLRP | value conservation, temporal direction, 6-hop cap, service contamination, traceability |
| Dashboard/dossiers | complete evidence paths, offline behavior, export integrity, usability |
| End-to-end | reproducible outputs and whole-system/ablation evaluations |

**Mandatory tests:** chronological holdouts; subgroup controls; multiple random seeds; significance/uncertainty; no training on ground-truth metadata unintentionally exposed as features; explicit false-positive reporting on first-hop neighbors of seeds; GPU/CPU reproducibility tolerances; inference with internet connectivity disabled.

**Release interpretation:** high synthetic accuracy is not a real-world crime-detection guarantee. Any real or benchmark dataset needs clear provenance, permitted use, relevant labels and external-validity discussion.

---

## 19. Five-phase implementation roadmap

Development is **phase-gated**. This initial README commit is **Phase 0: architecture plan only**. No implementation phase is complete at creation.

### Phase 1 — Foundations, data contracts and deterministic offline baseline

**Covers:** blocks 0, 1A, 1B, 2; foundational chain-only result path.

- [ ] **P1.1** Project, packaging, configuration, reproducibility manifest, lint/type/test CI.
- [ ] **P1.2** Strict CSV/JSON/XML schema parsers, exact satoshi and time normalization, error audit.
- [ ] **P1.3** Chain and wire typed processing, optional offline GeoIP/ASN and source provenance.
- [ ] **P1.4** TXID join, time precision checks, coverage and statistical-dependence go/no-go gate.
- [ ] **P1.5** Six-type graph with timestamped source-linked edges and daily/weekly snapshots.
- [ ] **P1.6** Small deterministic synthetic truth fixture, chain-only interpretable baseline, CLI export.
- [ ] **P1.7** Unit/integration/regression and fully disconnected inference smoke tests.

**Gate:** Linux fresh install loads all three formats; generates reproducible chain-only graph and baseline leads; questionable wire data correctly routes to chain-only; no identity claim is fabricated.

### Phase 2 — Shared graph intelligence, MCER and motifs

**Covers:** blocks 3, 4, 5.

- [ ] **P2.1** Document and implement causal, typed graph/chain/wire feature registry.
- [ ] **P2.2** Random-walk embedding baseline, GraphSAGE/GAT and heterogeneous/temporal encoders with resource-aware fallbacks.
- [ ] **P2.3** Train/evaluate self-supervised embeddings, link proposals and graph snapshot leakage guards.
- [ ] **P2.4** MCER H1–H5 evidence scoring, constraint-aware fixed-point loop, partition history.
- [ ] **P2.5** Motif/rule patterns and graph-novelty candidates with explanations and hard negatives.
- [ ] **P2.6** ARI/NMI/false-merge reports, motif metrics and complete Phase 1 compatibility tests.

**Gate:** candidate clusters, embeddings and suspicious-pattern instances are reproducible and include uncertainty/evidence; false-merge tests and CoinJoin/service controls pass.

### Phase 3 — Detection, Δ, Π and first-pass fusion

**Covers:** blocks 6, 7, 8, 9 pass 1.

- [ ] **P3.1** Supervised classic ML plus unsupervised baselines and graph-ML heads; documented training data eligibility.
- [ ] **P3.2** Expanding chronological OOF stacking, honest holdouts, train-fold embeddings, calibration tests.
- [ ] **P3.3** Paired-view CCA baseline, cross-layer divergence components Δ1–Δ5 and valid/abstain gate.
- [ ] **P3.4** Π_fee/hop/time/frag/infra accounting with goal/baseline prerequisites and explicit abstentions.
- [ ] **P3.5** Signal-specific scaling and pass-1 risk, separate Π–Δ typology, uncertainty and P1–P4.
- [ ] **P3.6** Evaluate chain-only vs chain+wire vs graph+stack vs Δ/Π and legitimate service false positives.

**Gate:** actual trained predictors or documented unsupervised fallback; no chronological leakage; invalid Δ/Π never receives invented numbers; local risk output is auditable.

### Phase 4 — Bounded MLRP, final fusion, API and console

**Covers:** blocks 9 pass 2, 10, 11.

- [ ] **P4.1** Frozen-seed forward/backward value-flow risk and evidence-path algorithm.
- [ ] **P4.2** Causal decay, six-hop bound, fan-out conservation, service and infrastructure boundaries.
- [ ] **P4.3** Per-level risk channels and audited deterministic-vs-learned comparison.
- [ ] **P4.4** Capped second-pass fusion (at most 25 points of 100), reproducible non-circular tests.
- [ ] **P4.5** Local FastAPI interfaces, job status, evidence and model manifests.
- [ ] **P4.6** Offline React dashboard, link analysis, temporal flows, lead queue, Δ/Π view and MCER audit.
- [ ] **P4.7** Self-contained PDF/CSV/JSON case export, provenance hashes and no-external-request tests.

**Gate:** investigator opens a local Linux dashboard, can trace every leading risk contribution to evidence, export dossiers and reproduce results; service-boundary and propagation tests pass.

### Phase 5 — Robust validation, optimization and release

**Covers:** block 12 and system-wide acceptance.

- [ ] **P5.1** Larger multi-seed synthetic L0–L3 scenario generator with independent ground truth.
- [ ] **P5.2** Benchmark matrices across graph ML, MCER, patterns, stack, Δ, Π and MLRP.
- [ ] **P5.3** Temporal holdout, class imbalance, abstention and legitimate-user false-positive analysis.
- [ ] **P5.4** Incremental ablations and propagation contamination/security/privacy audits.
- [ ] **P5.5** Linux CPU/GPU and fully disconnected deployment reproducibility, performance limits and memory budget.
- [ ] **P5.6** User manual, installation guide, sample offline walk-through, API specification and short SIH technical write-up.
- [ ] **P5.7** Final acceptance matrix with actual commands, passing CI and clearly enumerated open limitations.

**Gate:** each final requirement is linked to a real artifact/test; performance claims are restricted to evidence; all core flows work offline.

### 19.1 Phase completion report (required at every handoff)

Every phase PR/handoff must state: **objective; blocks touched; specific files changed; configuration/data schemas changed; commands run; actual passing/failing tests; benchmark artifacts; known limitations; architecture decisions; requirement checklist; and exact next step.** Do not mark a box complete without objective verification. Obtain review/confirmation before beginning the next major phase.

---

## 20. Quality engineering and Git workflow

- Use a clean branch per major phase, smaller PRs for substantial submodules, and reviewable commits.
- Protect the existing working baseline: schema/interface changes require migrations and backward-compatibility tests.
- GitHub Actions will run Python tests, lint/type checks, reproducibility checks and frontend builds after those components are implemented. External CI is not part of the offline investigator runtime.
- Each phase adds meaningful unit, integration, adversarial/negative-control and pipeline tests. Real tests are run and their outputs recorded; no fabricated “passed” statuses.
- Pin dependencies; scan licenses and known vulnerabilities before release; package required assets and models for Linux disconnected operation.
- Store no secrets or sensitive investigative data in the repository. Use local-only binding and authorization for investigator access; enforce file upload limits, read-only evidence, safe serialization/model loading, audit logs and path sanitization.
- Make dataset transformations, risk explanations and case exports reviewable and reproducible by run ID.

---

## 21. Final SIH26146 acceptance checklist

The project is complete **only** when these are demonstrated using an installable Linux application and verifiable evaluation outputs:

- [ ] Reproducible, fully offline CSV/JSON/XML → normalized data → graph → investigation pipeline.
- [ ] Reliable exact TXID-based cross-layer correlation where evidence exists; chain-only fallback otherwise.
- [ ] Candidate entity clusters with confidence, provenance and controlled false-merge rate.
- [ ] Real ML models, time-safe training/evaluation and appropriately calibrated anomaly or novelty outputs.
- [ ] Peel-chain, mixing-like, layering and related pattern detection with supporting transaction paths.
- [ ] Independent interpretable **Δ** and **Π** results plus explicit abstention and Π–Δ typology.
- [ ] Bounded, non-circular multi-level propagation and traceable value-weighted contributing paths.
- [ ] Prioritized P1–P4 leads with confidence, evidence, alternative explanations and limits.
- [ ] Interactive offline investigator dashboard and independent PDF/CSV case reports.
- [ ] Synthetic and control-group evaluation, time holdouts, ablations, FPR analysis, documented limitations.
- [ ] Reproducible Linux installation, model artifacts, local sample data, technical write-up and verified tests.

**Definition of done:** do not claim “fully working,” “production ready,” “accurate,” or “novel” merely because modules exist. Completion requires connected execution, measured verification, and transparent limitations.

---

## 22. Open research decisions and risk register

| Decision / risk | Planned resolution | Decision deadline |
|---|---|---|
| Real SIH dataset shape and completeness unknown | canonical schema + import adapters; quality/coverage audit before ML | Phase 1 |
| Authentic chain–wire dependence may be absent | statistical gate, exact evidence association, chain-only fallback | Phase 1 |
| Observation timestamps may not reflect origination | preserve timing semantics and relay uncertainty | Phase 1 |
| Dataset may omit UTXOs and fee environment | address-level uncertainty, Π partial/abstain and conservative flow | Phases 1/3 |
| CoinJoin and custody may break common-input heuristic | explicit exceptions, conservative constraints, false-merge audit | Phase 2 |
| High geographical dispersion does not imply distinct owners | change MCER H4 from unconditional veto to evidence-review constraint unless independently justified | Phase 2 |
| Shared graph/representation alignment is difficult | measured baselines before hetero temporal GNN | Phase 2 |
| Training labels may be absent/biased | verified label audit; unsupervised ranking without fake probabilities | Phase 3 |
| Δ residual may reflect sensor or sampling artifacts | permutation/coverage controls and abstention | Phase 3 |
| Π cheapest valid route may be unknowable | signed, component-wise economic baselines or abstain | Phase 3 |
| Meta-score and propagation can form circular dependency | two-pass frozen seeds, capped second pass, chronological OOF | Phases 3/4 |
| Shared infrastructure can contaminate graph risk | absorbing service boundaries, ASN no re-emission, six-hop cap | Phase 4 |
| Synthetic performance can be overstated | L0–L3 controls, generator shift tests and honest external validity | Phase 5 |
| Fully offline dependency packaging can fail | disconnected Linux install/inference acceptance test | Phase 5 |

**Current project state:** Architecture and five-phase work plan defined in this README. **All implementation and validation checkboxes remain open.** The next action is to review this specification, then start **P1.1** on a separate implementation branch.
