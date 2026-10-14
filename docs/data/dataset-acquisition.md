# Dataset strategy, acquisition and evaluation separation

**Design only.** The uploaded SIH problem specifies a **synthetic metadata dataset** in CSV/JSON/XML and requests an offline Linux system with working ML. It does not provide all file definitions, licenses, independent labels or authentic P2P captures. Acquisition must not be misrepresented as proof of useful cross-layer attribution.

## 1. Three independently evaluated tracks

| Track | Candidate input | Supports | Cannot support without new data |
|---|---|---|---|
| A — real on-chain graph | Elliptic++ transaction/actor benchmark; UCI BitcoinHeist address data; local Bitcoin Core block/UTXO exports | tabular/graph anomaly experiments, on-chain transaction/UTXO motifs where raw data permits, temporal splits | arbitrary real IP↔address control, true P2P broadcast-origin labels, PI infra |
| B — CLARION controlled synthetic | deterministic v4 SIH-format generator with chain and source-tagged wire observations, sealed entity/incident goals and perturbations | joining/coverage, clock tests, MCER truth, Δ/Π identifiability, MLRP bounds, dashboard integration | real-world illicit precision or claim of generalizable IP ownership |
| C — official SIH sample | actual organizer-provided CSV/JSON/XML when available | direct problem format compliance and integration | anything not actually in fields, credible labels/dependence until audit |

Possible public references (verify licenses, exact field inventories and versions **before download**): https://github.com/juicy-candy/Elliptic ; https://archive.ics.uci.edu/dataset/526/bitcoinheistransomwareaddressdataset ; https://developer.bitcoin.org/reference/rpc/ ; https://dev.maxmind.com/geoip/geolite2-free-geolocation-data/

**Do not** supply made-up wire fields to Elliptic++ or BitcoinHeist and call it measured cross-layer performance. Do not assume unknown/unlabeled records are benign.

## 2. Source registry for every dataset

Required manifest: \`dataset_id, publisher, retrieval/source URI, legal usage/license, permitted redistribution, original archive hash, imported_at, schema_version, record_count, date range, timezone/time precision, unit declarations, source sensor definition, TXID availability, entity-label provenance, missingness per field\`. Attach personally sensitive dataset handling policy before work begins. Do not automatically download during deployed inference.

### Intended ingestion process

Legal/source review → externally acquire data → cryptographic hash → immutable restricted local raw directory → adapter import without field fabrication → schema and valid-time checks → normalized Parquet → readiness report → graph snapshots → model/evaluation subsets.

## 3. Synthetic generator design and independent truth

Create six separate generator components: (a) transaction/UTXO objects with conservation; (b) actor/entity wallet control ground truth; (c) independent observed P2P relay sensor/capture network graph; (d) fee/latency/goal constraints when supporting Π; (e) hard negatives; (f) corruption/missingness/clock skew.

**Scenario tiers L0–L3** must be named as synthetic operational complexity, not adjudicated guilt. Gradually change address reuse, hop count, transaction splitting, timing irregularity, relay surface and infrastructure use. Disclose whether the generator's own mechanisms make classification artificially easy.

**Benign hard negatives:** payment processor batching, exchange aggregation/disbursement, custody, coin consolidation, known collaborative CoinJoin, ordinary VPN/hosting, shared ASN, relayed same TXID by many peers, NAT, mobile network migration, exchange hot/cold rotations.

**Anti-leakage:** generator latent actor IDs, suspiciousness templates, scenario type and labels live in a *separate truth table* inaccessible to feature generation and the serving API; train/test generator parameters differ deliberately.

## 4. Label governance

Labels have subject level (transaction/address/entity/subgraph), source (independently confirmed, benchmark, synthetic), available_at, confidence and unknown flag. Allow positive, negative and unknown as distinct. For a supervised task, labels from later periods cannot be used to derive earlier features or MCER candidates.

Do not promise a crime-probability model from a dataset that only offers heuristic or partial labels. Where validation labels are unavailable, report separate novelty ranking and abstention.

## 5. Evaluation plan per track

- **Track A:** benchmark-defined splits vs chronological holdout when timestamps support it; PR-AUC/ROC-AUC, precision@K, calibration only for credible labels; graph-baseline ablation.
- **Track B:** exact TXID join precision, time alignment, false entity merges, motif recall, Δ residual validity, Π component accounting/abstention, path propagation conservation, UI/end-to-end checks.
- **Track C:** measured field coverage, correct offline parser operation, valid graph/dossier output and only scientifically supported metrics.
- **Across tracks:** never aggregate metrics from fundamentally different tasks and label quality into one accuracy figure.

## 6. Practical data-readiness checklist

[ ] organizers’ sample and field semantics reviewed; [ ] legal conditions recorded; [ ] TXID join validity assessed; [ ] sensor time precision documented; [ ] exact outpoints present or partial-flow caveat; [ ] label eligibility audited; [ ] chronology/splits preserved; [ ] GeoIP licensed local file optional; [ ] sealed synthetic truth and legitimate controls available; [ ] no runtime downloads.

**Exit condition:** a truthful availability matrix for every required component. A missing real network layer triggers documented chain-only mode, not cancellation of all other functionality.
