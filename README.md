# CLARION v4
> **CLARION — Offline, Explainable Bitcoin Transaction and Network-Traffic Intelligence.** An evidence-first investigator platform for SIH26146; uses graph ML and classical learning to prioritize reviewable leads **without claiming that a relay IP owns a wallet**.

**Project:** Smart India Hackathon 2026 · SIH26146 · NTRO · Blockchain & Cybersecurity  
**Target:** Linux, fully offline at inference time · **Repository status: architecture and documentation scaffold ONLY**  
**Current branch of delivery:** Production module plan · **No executable application, training or benchmark is represented as complete.**

---

## 1. Product vision

CLARION ingests authorized local Bitcoin chain and P2P observations (CSV, JSON and XML), validates evidence, reconstructs temporal value flow, learns graph and tabular behavior, proposes explainable entity clusters, detects pattern candidates, scores discrepancies, and produces ranked investigator leads with verifiable context. The SIH task calls for a **working offline AI/ML prototype**, not only rules or a diagram; implementation follows the phase roadmap after review.

**What investigators should eventually receive:** risk-band-filtered leads; time-bounded interactive graph; candidate entity membership and uncertainty; peel/mixing/layering paths; separately itemized **Δ** divergence and **Π** cost; forward/backward bounded exposure paths; exportable case dossier; clear explanation and source trail.

## 2. Evidence, ethics and product boundaries

- A peer observing or relaying a TXID **does not** prove ownership, origination, identity or guilt.
- Heuristic entity clusters are hypotheses. CoinJoin and multi-party spending invalidate careless common-input linking.
- Exchanges, custodians, processors, VPNs and privacy users require explicit false-positive controls.
- Unknown timestamps, outpoints, network observations, trusted labels and economic objectives trigger **abstention** or chain-only/unsupervised fallback, not invented data.
- Calibrated suspiciousness probabilities require valid labeled independent holdouts; novelty scores are reported as **novelty**.
- No Internet API, telemetry, CDN or live explorer can be required in deployed Linux inference.
- Do not upload confidential captures, real IP data or externally licensed datasets to Git.

## 3. Complete investigator workflow

~~~mermaid
flowchart TD
  A["Locally supplied chain/wire CSV JSON XML"] --> B["0. Validate schema, units, source/time + go/no-go"]
  B --> C["1A. Bitcoin UTXO and value-flow layer"]
  B --> D["1B. Source-tagged P2P observation layer"]
  C --> E["2. Temporal six-type heterogeneous evidence graph"]
  D --> E
  E --> F["3. Chain/wire features + shared graph encoder"]
  F --> G["4. Temporal MCER clustering"]
  G --> E
  F --> H["5. Transaction motifs"]
  F --> I["6. Leakage-safe anomaly stack"]
  F --> J["7. Cross-layer divergence Δ"]
  F --> K["8. Obfuscation expenditure Π"]
  H --> L["9. Calibrated local first-pass fusion"]
  I --> L
  J --> L
  K --> L
  L --> M["Freeze seed risk"]
  M --> N["10. Bounded causal MLRP"]
  N --> O["9. Capped final fusion"]
  L --> O
  O --> P["11. Offline dashboard + evidence dossiers"]
  P --> Q["12. Synthetic/temporal validation + ablations"]
~~~

**Gates:** missing observed TXID or weak dependence → chain-only; unusable incident labels → unsupervised ranking; unknown economic objective → Π abstains; no reliable paired chain/wire views → Δ abstains.

## 4. High-level engineering architecture

~~~mermaid
flowchart LR
  subgraph Ingest["Data and evidence plane"]
    RAW["Immutable raw + hashes"] --> PARSE["Source adapters"]
    PARSE --> DUCK["Parquet + DuckDB"]
    PARSE --> GATE["Quality and label gates"]
  end
  subgraph Intelligence["Analytics and ML plane"]
    GATE --> GRAPH["Temporal typed graph"]
    GRAPH --> FEAT["Causal features + learned embeddings"]
    FEAT --> MCER["MCER"]
    FEAT --> PAT["Motifs"]
    FEAT --> MODEL["Base learners + OOF meta"]
    FEAT --> DELTA["Δ engine"]
    FEAT --> PI["Π engine"]
    MODEL --> FUS["Frozen seeds / fusion"]
    PAT --> FUS
    DELTA --> FUS
    PI --> FUS
    FUS --> PROP["MLRP"]
  end
  subgraph Serving["Local investigation plane"]
    PROP --> API["FastAPI"]
    API --> WEB["Bundled React dashboard"]
    API --> CASE["Case export + audit"]
  end
~~~

For the complete research design and numbered block contracts, see [Architecture specification](docs/architecture/architecture-v4-spec.md). Each implemented module must preserve the specified evidence semantics.

## 5. Recommended technology stack

| Area | Preferred stack / rationale |
|---|---|
| Backend | Python 3.11/3.12 · typed schemas (Pydantic) · FastAPI |
| Parsing and batch analytics | strict CSV/JSON/XML · PyArrow/Parquet · DuckDB |
| Bitcoin chain | locally imported Bitcoin Core RPC/export data; precise UTXO outpoints |
| Wire observations | source-tagged TXID relays, offline local sessionization, optional GeoLite2 ASN/country |
| Graph | canonical typed Parquet nodes/edges; NetworkX for small fixtures; PyTorch Geometric for learning |
| Graph/ML | PyTorch · PyG GraphSAGE/GAT; scikit-learn · optional LightGBM |
| Model registry | local signed/hashed manifests; immutable train/validation cutoffs |
| API | FastAPI + versioned contracts; loopback-only initially |
| Web | React · TypeScript · Cytoscape.js · bundled local static assets |
| Reproducibility | pytest · Ruff · mypy · Linux offline wheel/model bundle |
| Case export | locally generated PDF/CSV/JSON with evidence hashes |

All technology choices are **planned**, pending compatibility, license, security and benchmark review.

## 6. Dataset and feature strategy

**Track A — real graph benchmarks:** Elliptic++ for transaction/address graph research; BitcoinHeist for additional address-level behavior; local Bitcoin Core block/UTXO samples for authentic value-flow and scripts. None supplies trustworthy historic originating relay IP for each Bitcoin wallet.

**Track B — controlled synthetic scenarios:** deterministic SIH-format chain/wire records, separate ground-truth ledger, 0–3 operational-complexity tiers and benign exchanges/custodians/CoinJoin/hosted relays.

**Track C — actual SIH input:** import organizer-provided files after auditing field semantics, source coverage and labels. No authentic cross-layer benchmark is claimed before such data is audited.

**Canonical tables:** evidence_sources, blocks, transactions, inputs, outputs, network_observations, sessions, ip_enrichment, graph_nodes, graph_edges, entity_hypotheses, motif_instances, labels, economic_objectives, scores_and_leads, case_audit. Internal amounts are integer satoshis. Time types/precision remain distinct. Full schema planning: [Schemas](schemas/README.md) and [Data dictionary](docs/data/README.md).

## 7. Blockchain and wire correlation

**Chain:** exact prevout/outpoint links, address spends/funds, input-output amount/fee balance, script/weight, temporal snapshots. **Wire:** capture sensor, source/destination host and port, observed TXID, first-seen time accuracy, session/ASN/GeoIP data.

**Join tiers:** J0 exact on-chain outpoint flow; J1 observed TXID relay; J2 context co-session/ASN/behavior; J3 hypothetical embedding links (not owner evidence). Only J1 directly associates a host observation with a transaction; none directly establishes an owning entity.

## 8. Graph representation and entity inference

Six node types: **Transaction · Address · Entity · Host · ASN · Country**. Edges must carry source evidence, confidence, direction and time. Graph learning progresses from hand-built features and random walks to GraphSAGE/GAT and tested heterogeneous temporal encoding.

**MCER H1–H5:** co-spend proposals, change candidates, learned behavioral similarity, uncertain wire conflicts, stable-fingerprint re-link hypotheses → signed constraints → conservative iterative partition → time-versioned clusters with lineage, confidence and abstentions.

## 9. Bitcoin pattern intelligence

Track peel-chain candidate, mixing-like fan-in/out, CoinJoin-like structure, circular paths, rapid multi-hop layering, changing output fragmentation, bursts, fee/weight anomalies and interactions with locally documented service categories. Require supporting subgraphs **and legitimate alternative interpretations**; nothing is proof of laundering.

## 10. Stacked anomaly detector and lifecycle

**Baselines:** logistic regression, random forest, isolation forest, One-Class SVM and GMM. **Upgrades:** optional LightGBM, GraphSAGE/GAT classification or novelty heads and temporal GNN research. **Stack:** expanding chronological out-of-fold base predictions → regularized meta-learner → separate later calibration → untouched temporal test.

No label → ensemble of novelty ranks, **not** crime probabilities. No random leakage across future graph edges/MCER state; keep experiments under [experiments/](experiments/README.md), model recipes under [configs/models/](configs/models/README.md), training under [src/clarion/training/](src/clarion/training/README.md).

## 11. Cross-layer Δ and obfuscation Π

**Δ divergence:** eligible paired chain/wire views → CCA baseline → residual score + Δ1–Δ5 explanations → quality gate and abstention when wire evidence is weak.

**Π expenditure:** independently identified economic outcome and admissible cheapest execution → itemized fee, hop, time, fragmentation and infrastructure premiums; retain original units and signed values; abstain when goal or fee context is not defensible.

**Fusion:** no raw Δ + Π sum. Calibrate only supported features; use separate Π–Δ typology when both axes valid. Freeze first-pass risk seeds, diffuse risk causally, then cap propagation contribution at **25 of 100** points.

## 12. Multi-level risk propagation

Value-weighted and hop/time-decayed diffusion with a hard six-hop target; forward taint and backward provenance are separately displayed. Known service boundaries absorb, high-degree hosts and ASNs do not broadcast blanket contamination, Country is context-only. Every result must show a traceable contributing path from frozen seed evidence.

## 13. Investigator dashboard and export

Local-only FastAPI plus React/TypeScript: dataset readiness, ranked lead queue, time-bounded multi-layer graph, candidate clusters, pattern timelines, Δ/Π panel, MLRP path explanation, what-if chain-only comparison, model confidence and evidence dossier export. Build UI with offline assets, paginated nodes and filters; never display unsupported ownership claims.

## 14. Privacy, security and forensic integrity

Threat model covers malicious CSV/JSON/XML, XXE/billion-laughs, CSV formula injection, unsafe model deserialization, raw capture exposure, poisoned labels and weights, future leakage, unauthorized case export, supply-chain tampering and runtime network egress. Use immutable raw files with SHA-256, role-limited case access, redaction, input ceilings, safe model formats and tamper-evident audit logs. See [Security](docs/security/README.md).

## 15. Proposed production repository structure

Every currently planned folder is materialized on the architecture branch with its own **README.md** documenting purpose, files, contracts, security constraints and acceptance. **Non-README file stubs contain comments only**; they are implementation instructions, not runnable application code.

~~~text
CLARION/
├── README.md                         # product overview; this document
├── docs/                             # specification, ADRs, progress, security, ML
├── schemas/                          # versioned raw/normalized/graph/API contracts
├── configs/                          # offline profiles, model/security recipes
├── src/clarion/                      # ingestion → graph → learning → fusion → API
├── frontend/src/                     # app, components, screens, API client, styles
├── data/                             # small safe samples, manifests, external mount
├── artifacts/                        # local models/reports (not in Git)
├── tests/                            # unit, integration, leakage, adversarial, offline, E2E
├── experiments/                      # reproducible benchmark and ablation protocols
├── scripts/                          # pre-offline data/training/release helpers
├── deploy/                           # Linux workstation and optional container plans
└── .github/                          # PR templates and future CI descriptions
~~~

Review the **per-folder README** before implementing any module. The previous 33-section technical specification is preserved unmodified in [docs/architecture/architecture-v4-spec.md](docs/architecture/architecture-v4-spec.md).

## 16. Planned core public contracts

- **EvidenceSource / NormalizedTransaction / UTXO / NetworkObservation:** immutable typed record plus source ID and time accuracy.
- **ReadinessDecision:** chain/wire and supervised/unsupervised mode with coverage, statistical quality and reasons.
- **TemporalGraphSnapshot:** typed node/edge records, evidence IDs, graph window and causal cutoff.
- **EntityHypothesis:** versioned address members, signed pair evidence, conflicts, merge/split history.
- **PatternInstance:** motif type, confidence and minimal supporting path.
- **ModelScore:** score type (probability vs novelty), split/model ID, calibration status and uncertainty.
- **DivergenceResult / ExpenditureBill:** independent Δ and Π values with component availability and abstentions.
- **RiskLead / PropagationPath / CaseDossier:** frozen seed, contribution, rank/P1–P4, evidence and redaction.

Define versioned machine-readable schemas in Phase 1 before implementing data consumers; do not silently change contracts.

## 17. Five implementation phases and gates

| Phase | Blocks | Release gate |
|---|---|---|
| **P1: Foundations** | 0, 1A/1B, 2 | all three input formats → typed graph → chain-only baseline, offline tests |
| **P2: Graph and entities** | 3, 4, 5 | leakage-safe embeddings, MCER + motif proofs and false-merge controls |
| **P3: ML and evidence** | 6, 7, 8, first-pass 9 | trained models, time-safe OOF, Δ/Π abstentions, eligible calibration |
| **P4: Product integration** | second-pass 9, 10, 11 | bounded causal risk, dashboard, local API, case evidence export |
| **P5: Research and release** | 12 + all | temporal evaluations, hard-negative FPR, ablations, air-gap Linux package |

**Architecture-first state:** none of the five phases is implemented or validated. See [phase progress](docs/progress/README.md) and [full acceptance criteria](docs/architecture/architecture-v4-spec.md).

## 18. Modular engineering principles

Adopt VoiceDoc's **product-first architecture documentation style**: clear mission, boundaries, end-to-end diagram, module responsibilities, interface contracts, technology alternatives, constraints, measured validation, release criteria and explicit project status. That is a documentation style reference, **not** a reusable technology stack or functional design for this project.

Modules may depend on lower-layer evidence contracts, not circular imports. Prefer typed data interfaces, snapshot-aware functions, model wrappers, immutable run artifacts and additive migrations. No module may fabricate network ownership, use unavailable future data or erase evidence uncertainty.

## 19. Test matrix and release definition

Require parser fuzz/XXE defense, satoshi/time correctness, TXID joins, chain-wire dependence, strict temporal folds and OOF, MCER false-merge/CoinJoin controls, motif benign controls, Δ/Π abstention, conservation and service barriers, role-based reports, disconnected inference and CPU/GPU compatibility. Synthetic L0–L3 results must be labeled synthetic.

**Production-grade aspiration ≠ production-ready status.** A module is complete only after implementation, integrated passing tests, measured claims, evidence links and review signoff.

## 20. Engineering and Git workflow

Architecture scaffolding occurs in a single documentation-only PR. Subsequent implementation phases use separate feature branches and reviewable PRs; never merge unverified executable components or pretend comment stubs are working modules. Protect existing contracts and preserve a transparent phase tracker.

**First executable action after approving architecture:** P1.1 establish actual Python packaging, pinned dependencies, schema registry, secure ingestion fixtures and CI, replacing comment stubs module by module.

## 21. Project status

| Item | Current status |
|---|---|
| SIH architecture and requirement mapping | Documented for review |
| Original CLARION v4 long technical specification | Preserved under docs/architecture |
| VoiceDoc-inspired high-level README and module layout | Documented design scaffold |
| Functional code, trained models, installed dashboard | **Not implemented in this repository** |
| Tests run, model benchmark results and production release | **None claimed** |

## 22. References and licensing

- [SIH26146 architecture and full component design](docs/architecture/architecture-v4-spec.md).
- [VoiceDoc README — reference for **documentation organization only**](https://github.com/shanmukhdatta/VoiceDoc/blob/main/README.md).
- [Elliptic++ researcher dataset](https://github.com/juicy-candy/Elliptic); [BitcoinHeist (UCI)](https://archive.ics.uci.edu/dataset/526/bitcoinheistransomwareaddressdataset); [Bitcoin Core docs](https://developer.bitcoin.org/); [GeoLite2 terms](https://www.maxmind.com/en/geolite/eula).
- [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/), [scikit-learn](https://scikit-learn.org/).

**Licensing:** choose a repository code license only after checking dependency, dataset and offline GeoIP terms; dataset/model weights may use different licenses.

---

**CLARION — Evidence first. Graph intelligence second. Investigative judgment always.**
