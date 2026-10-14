# End-to-end CLARION v4 architecture and execution modes

**Status: proposed implementation plan only.** The uploaded v4 PDF (blocks 0–12) remains the governing functional source. Technical policies below are engineering decisions, not claims from the PDF.

## 1. System topology and runtime isolation

~~~mermaid
flowchart TB
  A["Authorized local CSV/JSON/XML, Bitcoin Core exports, benchmark samples"] --> B["Immutable evidence ingest + schema/version/hash"]
  B --> C["Readiness and label gates"]
  C --> D["Chain/UTXO processor"]
  C --> E["Wire observation and offline GeoIP processor"]
  D --> F["Timestamped graph (six types)"]
  E --> F
  F --> G["Causal feature store + graph embeddings"]
  G --> H["MCER as-of candidate clusters"]
  H -. "versioned member-of hypotheses" .-> F
  G --> I["Peel/mix/layering motif engine"]
  G --> J["OOF supervised / unsupervised / graph anomaly stack"]
  G --> K["Δ chain-wire residual when joined"]
  G --> L["Π economic cost when goal supported"]
  I --> M["First-pass fusion"]
  J --> M
  K --> M
  L --> M
  M --> N["Freeze seed manifest"]
  N --> O["Bounded MLRP: financial + observational channels"]
  O --> P["Second-pass capped risk"]
  M --> P
  P --> Q["Local FastAPI read/query/export"]
  Q --> R["Bundled offline React investigator UI"]
  Q --> S["Evidence dossier with hashes, redaction and audit"]
  S --> T["Research audits and synthetic/real benchmarks"]
~~~

**Training is a separate developer-initiated pipeline**, not an inference-time online service. Dataset acquisition, GPU fitting, model selection and license checks occur before the Linux offline package is built. All artifacts and dependencies are local at runtime.

## 2. Four execution decisions, independently determined

- **Cross-layer decision:** GO only if raw wire fields contain genuine source-tagged observed TXIDs, viable alignment and cross-view coverage/dependence. Else CHAIN_ONLY.
- **Supervision decision:** use verified time-available labels with independent held-out data, else UNSUPERVISED_ONLY.
- **Δ decision:** compute cross-view residuals only with enough independent validated paired observations; else ABSTAIN.
- **Π decision:** score only components with identifiable economic goals and reasonable cost baseline; otherwise component-wise ABSTAIN.

The decisions are **independent**: e.g., calibrated chain-only ML may be possible without network observations, and Π_fee may be missing while a fee anomaly feature exists.

## 3. Data plane: source-of-truth and cache tiers

- **L0 raw evidence:** read-only original bytes, SHA-256, source/capture manifest, license; immutable.
- **L1 normalized:** Parquet tables: transaction, block, input/outpoint, output, observation, session, ASN/country and labels (separate restricted store).
- **L2 graph facts:** typed nodes and directed evidence edges, time window, provenance and confidence type.
- **L3 derived models:** feature matrices, model checkpoints, cluster hypotheses, motif instances and per-run outputs, all rebuildable and versioned.
- **L4 investigator:** paginated, time-bounded, role-filtered API DTOs, dossier snapshot and audit log.
- Use DuckDB queries over Parquet as default batch/interactive storage; avoid unbounded NetworkX graphs and client-side loading of an entire Bitcoin graph.

## 4. Bitcoin and P2P interpretation

Bitcoin uses UTXO outpoints, not direct balances per address. A source address is an uncertain script/address annotation in a transaction input; exact transfer lineage comes from previous TXID and vout where available. Some outputs are not conventional addresses; script types, coinbase, multi-signature transactions, Taproot, mempool status, chain reorganizations and unknown prevouts must be handled explicitly. Do not calculate "wallet balance" from raw transaction samples without global history.

P2P network observations record what a local sensor *saw*, not who originated or controlled it. Relay propagation, capture bias, NAT, VPN, clock skew and potentially unavailable TXIDs limit association claims. A genuine observed-TXID join supports Host—observed relay—Transaction only.

## 5. Component public dependency rules

- Parsers produce typed canonical data; graph builder never parses arbitrary raw files.
- Graph readers operate on **as-of snapshots** and evidence links; graph models may read snapshots but may not mutate raw evidence.
- Feature and embedding outputs include model/schema IDs, cutoff time, missingness masks and source IDs.
- MCER emits *candidate member-of edges*, not confirmed identity.
- Motifs emit candidate behavior patterns with witness paths and known benign alternatives.
- Stack reads eligible features; pass-1 fusion reads independent signals; propagation reads **only** frozen pass-1 seeds; pass-2 can read propagated exposure.
- API may read run results but never reinterpret novelty as crime probability or discard Δ/Π abstention.

## 6. Failure-mode contract

| Failure | Pipeline behavior | UI/report behavior |
|---|---|---|
| malformed CSV/JSON/XML | row quarantine with provenance or atomic rejection for structural damage | show counts, field failures and source |
| invalid/unobserved TXID | no cross-layer join | no IP-to-address inference; chain-only mode |
| low sensor coverage or dependence | cross-layer gate fails | Δ disabled and reason |
| labels missing/tainted | unsupervised track | novelty rank, no anomaly probability |
| unknown economic goal | Π abstains | itemized unavailability and evidence needed |
| partial outpoints | degrade flow to conservative approximation | explain unresolved funds lineage |
| suspicious CoinJoin heuristic | MCER evidence conflict | prevent false co-spend group ownership |
| large graph | partition into time windows, sampled query/embedding | browser limits nodes/edges; pagination |
| model invalid/unknown version | block inference of incompatible model | explain artifact mismatch |
| egress unavailable | execute with bundled wheels/models/GeoIP/assets | all core screens function offline |
| no confidence calibration | show score/rank only | suppress percentage claims |

## 7. Subsystem acceptance interfaces

Read [component-contracts.md](component-contracts.md) for proposed typed DTOs and schema versioning, [REQUIREMENTS_AUDIT.md](REQUIREMENTS_AUDIT.md) for outstanding decisions, and the source-preserving [architecture-v4-spec.md](architecture-v4-spec.md). Every phase must demonstrate a connected end-to-end slice, not a model notebook detached from evidence ingestion.
