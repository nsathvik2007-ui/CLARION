# CLARION v4 — Production Project Structure and Module Ownership

> This is an **architecture scaffold**, not working code. Every planned module has its own README and comment-only source stubs. The original CLARION v4 specification (sections 0–12), detailed stacking, risk propagation and dashboard architecture documents remain authoritative.

## 1. Architectural style and dependency rule

CLARION is designed as a **single-machine, offline Linux modular monolith**. Use strongly typed domain contracts, an orchestrated run pipeline, isolated research engines, immutable evidence snapshots and a localhost investigator application rather than premature microservices or disconnected notebooks.

~~~mermaid
flowchart LR
 A["Authorized local evidence"] --> B["Adapters + validation"]
 B --> C["Readiness + immutable storage"]
 C --> D["Temporal graph + features"]
 D --> E["MCER / motifs / GNN / anomaly stack"]
 E --> F["Independent Δ and Π + pass-1 fusion"]
 F --> G["Frozen seed vector"]
 G --> H["Bounded MLRP"]
 H --> I["Pass-2 capped final score"]
 I --> J["Explanation + reporting"]
 J --> K["Local FastAPI + React"]
~~~

**Single dependency direction:** low-level domain and evidence types never import graph ML, FastAPI, application orchestration or frontend; the application orchestrator depends on service interfaces, but stages never depend on the orchestrator. Case reporting never calculates scores or invents evidence.

## 2. Planned physical tree

~~~text
CLARION/
├── README.md, SECURITY.md, CONTRIBUTING.md, pyproject.toml
├── configs/
│   ├── profiles/                  # cpu, gpu, chain-only, validated cross-layer
│   ├── models/                    # GNN, MCER and OOF stack recipes
│   └── security/                  # access, privacy and offline enforcement
├── schemas/
│   ├── raw/ normalized/ graph/ api/
├── src/clarion/
│   ├── domain/                    # NEW: immutable Bitcoin/evidence/score contracts
│   ├── core/                      # IDs, clocks, provenance and errors
│   ├── application/               # NEW: orchestrated DAG, run state, mode policy
│   ├── ingestion/
│   │   └── adapters/             # NEW: SIH, Bitcoin Core, Elliptic++, BitcoinHeist
│   ├── readiness/ chain/ wire/ storage/
│   ├── graph/ features/ representation/ entity_resolution/ patterns/
│   ├── training/ detection/ divergence/ expenditure/
│   ├── fusion/ propagation/ explanations/
│   ├── reporting/                 # NEW: safe PDF/CSV/JSON export + provenance
│   ├── security/ observability/  # NEW: local event/metric tracking
│   ├── synthetic/ evaluation/
│   ├── api/
│   │   ├── main.py               # local FastAPI app factory
│   │   ├── schemas.py, dependencies.py
│   │   └── routers/              # NEW: small route modules by read-only domain
│   └── cli/
├── frontend/
│   ├── src/
│   │   ├── app/ components/ lib/ styles/
│   │   └── features/
│   │       ├── readiness/ leads/ graph/ entities/ patterns/
│   │       ├── signals/ propagation/ timeline/ cases/
│   │       └── models/ audit/     # NEW: one documented screen per folder
│   └── public/                    # local assets; no CDN
├── tests/
│   ├── unit/ contracts/ integration/ property/ leakage/
│   ├── adversarial/ offline/ e2e/ performance/ fixtures/
├── docs/
│   ├── architecture/ data/ ml/ security/ operations/
│   ├── adr/ development/ progress/
├── data/
│   ├── samples/ manifests/ external/
├── artifacts/
│   ├── models/ reports/          # not committed (licensed/private data)
├── experiments/
│   ├── benchmarks/ ablations/
├── scripts/
│   ├── data/ train/ release/
├── deploy/
│   ├── linux/ containers/
└── .github/                      # issue/PR and future workflow documentation
~~~

The existing full scientific specification and the three detailed scoring/UI documents are retained unchanged. Comment-only pyproject and workflow files are **not** installed dependencies or passing CI.

## 3. Explicit ownership per architecture block

| Block | Owner | Required output and strict boundary |
|---|---|---|
| 0 — data readiness | ingestion, adapters, readiness, domain | validated raw-to-normalized records, join/clock/label routing decision; no fabricated correlation |
| 1A — blockchain | chain, domain | exact Bitcoin satoshis and directed UTXO spend/fund edges |
| 1B — network | wire, adapters | observed TXID relays, session/ASN context; no address/IP ownership |
| 2 — evidence graph | graph, storage | six-type directed temporal snapshots with provenance |
| 3 — feature and graph representation | features, representation | fold-causal handcrafted and Node2Vec/GraphSAGE/GAT embeddings |
| 4 — MCER | entity_resolution | versioned uncertain clusters, false-merge protections and lineage |
| 5 — motifs | patterns | peel, mixing-like, layering candidate witness graphs |
| 6 — ML stack | training, detection | actual chronological OOF base/meta predictions, calibration if eligible |
| 7 — Δ | divergence | paired cross-view residual or abstention |
| 8 — Π | expenditure | economically justified fee/hop/time/frag/infra bill or abstention |
| 9 — fusion | fusion | separate Δ/Π axes, pass-1 frozen risk, pass-2 at most 25 propagation points |
| 10 — MLRP | propagation | non-amplifying causal paths, separate value/context and fwd/back channels |
| 11 — investigator | explanations, reporting, api, frontend | verified reason, authorized dossier, offline graph/UI |
| 12 — evaluation | evaluation, synthetic, experiments, tests | temporal holdout, ARI/NMI, FPR, ablations, limitations |

Crosscutting ownership: security guards input/export and access; observability records only redacted local run events; application is the only orchestrator.

## 4. Restructuring decisions and moved placeholders

| Removed comment-only stub | Replacement location | Reason |
|---|---|---|
| src/clarion/ingestion/adapters.py | src/clarion/ingestion/adapters/ | isolate dataset-specific schema, rights and capabilities |
| src/clarion/api/routes.py | src/clarion/api/routers/ | avoid one huge route file and unsafe cross-feature coupling |
| frontend/src/features/leadExplorer.tsx | frontend/src/features/leads/LeadsPage.tsx | one vertical module per investigator view |
| frontend/src/features/graphExplorer.tsx | frontend/src/features/graph/GraphPage.tsx | graph rendering, time/evidence and bounded queries |
| frontend/src/features/caseDossier.tsx | frontend/src/features/cases/CaseDossier.tsx | role-aware dossier/export separate from anomaly scoring |

Previously missing: domain (shared typed contracts), application (end-to-end DAG and run ledger), reporting (file export), observability (local-only diagnostics), operations (air-gap runbooks), contract/property/performance test folders. The removed files are **comment-only stubs**, not existing working functionality.

## 5. Run and training contracts

### Inference-time run order

1. Source adapter → raw SHA-256 and safe canonical records.
2. Readiness tests TXID join/clock coverage, independence and eligible labels → chain-only/cross-layer and unsupervised/supervised routing.
3. Immutable graph snapshots at analysis cutoff → features and valid embeddings.
4. MCER and motifs → valid per-subject stacked anomaly score plus separately gated Δ and Π.
5. Pass-1 local fusion **without** same-run propagation → freeze signed/hashed seeds.
6. Deterministic bounded MLRP: financial value-share and network observation context stay separate; no host/ASN blanket spillover.
7. Pass-2 fusion: add at most **25 out of 100 risk points** once → ranked leads with score type and uncertainty.
8. Explanation assembles evidence and potential benign alternatives → reporting sanitizes CSV/PDF/JSON → API/React displays only supported findings.

### Training-time lifecycle

Source/label audit → chronological purged folds → per-fold train-only feature/MCER/embedding fit → OOF base predictions → meta-model → later calibration when eligible → untouched future holdout → legitimate-service FP audit → locally versioned model manifest → explicit reviewed promotion. Model training is separate from the investigator API; no source snapshots can leak future graph edges into training folds.

## 6. Technical responsibilities

**Domain + schemas:** versioned contract fields and nullable vs abstained semantics; do not maintain two incompatible DTO definitions.  
**Application:** checkpoint/resume, route modes, stage ordering, immutable manifest; no algorithmic duplication.  
**Storage:** Parquet/ DuckDB, run ID and source/model/config checksums; only raw-source snapshots are immutable evidence, model caches are rebuildable.  
**API:** localhost by default; time-/hop-/page-bounded read-only queries; authorization required before nonlocal exposure.  
**Frontend:** typed generated API interfaces, evidence provenance, accessible offline icons/fonts, screen-level feature modules and safe export state.  
**Reporting:** assemble only reviewed evidence; redact, escape formula injection, produce hashed local reports.  
**Operations:** offline wheels/weights/GeoIP handling, restore and access/retention procedures.  
**Tests:** attack parsers, temporal leakage, Graph/ML uncertainty and legitimate service boundaries before claiming release readiness.

## 7. Phase ownership and acceptance

- **P1:** domain, core, application, ingestion/adapters, readiness, chain/wire, storage/graph, synthetic, unit/contracts/integration, first executable CLI.
- **P2:** graph features and representations, MCER, motifs, leakage and property validation.
- **P3:** training, detection/OOF, Δ, Π, local fusion, calibration and research holdouts.
- **P4:** MLRP, final fusion, explanations, reporting, API routers, frontend feature screens and authorized case review.
- **P5:** evaluation ablations, false-positive controls, performance/air-gap release, operations runbooks, reproducible Linux packaging.

A phase is complete only when real code, independently executed tests and data/model artifacts are present and the phase progress record contains actual results.

## 8. Project-structure verification requirements

- Every nested materialized folder must have its own README with purpose, specific file responsibilities and acceptance tests.
- No duplicate deprecated placeholders remain; root README links to this design.
- The preserved 33-section CLARION spec, stacked anomaly, propagation and dashboard details cannot be silently changed.
- No fitted model, unknown-label claim, fake UI functionality or runtime internet dependency is introduced by this scaffold.
- Keep .github/ARCHITECTURE.md; do **not** add .github/README.md because it overrides GitHub's root README display.

**Next:** approve this file ownership map; begin P1.1 implementation on a separate branch with genuine packaging, schema validators and CI instead of relying on current comment-only stubs.
