# Graph ML, stacking, motif and alternative model selection

**Architecture design, not a leaderboard.** The PDF §3 describes a **shared graph representation** consumed by MCER (§4), motifs (§5), stacked anomaly detection (§6) and Δ (§7); §10D proposes a learned GAT edge-strength comparator. Selection must optimize *incremental held-out utility, calibration, cost and explainability*, not merely sophistication.

## 1. Distinct model jobs

| Job | Baseline candidate | Advanced candidate | Output level | Acceptance |
|---|---|---|---|---|
| Causal tabular features | deterministic features / logistic regression | random forest, optional LightGBM | tx/address/entity | demonstrable holdout uplift and no leakage |
| Graph embeddings | random walk / Node2Vec, degree statistics | inductive GraphSAGE | address/tx/entity/subgraph | stable snapshots and generalization to new nodes |
| Heterogeneous graph encoder | type-specific shallow projections | typed GraphSAGE / heterogeneous GAT | six-type graph | valid relation masks and no fabricated cross-layer edges |
| Temporal graph encoder | rolling window feature snapshots | temporal message passing with time-aware edge sampling | subject at cutoff T | no future neighbor access and measured lift |
| Graph classifier | LR on embeddings | GraphSAGE/GAT classification head | labeled transaction/address | PR-AUC/precision@K gain on future windows |
| Novelty | IF/OCSVM/GMM | graph reconstruction error and contrastive novelty | all valid subjects | interpret score as rank without labels |
| Motif discovery | deterministic witness patterns | motif graph embedding similarity/search | candidate subgraph | real benign negative and hand-audited witness |
| MCER pair similarity | cautious co-input/change heuristics | embedding pair scorer + signed constraints | address pairs | lower false merge than baseline |
| Δ paired-view mapping | CCA with train-only scaling | contrastive paired-view graph encoder | eligible chain↔wire pair | held-out residual robustness to shuffled null |
| MLRP edge importance | deterministic edge policy | learned GAT weights comparator | edge evidence | no increased service contamination, explainability |

**LightGBM, heterogeneous temporal GNN and contrastive encoders are options**, not guaranteed required libraries/models. Exact stack, CUDA toolkit, Python and licenses must be pinned after compatibility tests.

## 2. Shared representation: how the graph connects the three scoring views

- Produce \`z_chain\` from chain nodes/edges, \`z_wire\` from wire events when observed and sufficiently joined, and \`z_graph\` from the typed temporal graph where permitted.
- Project type-specific feature spaces into a common dimension with a versioned encoder. Shared embedding **does not imply shared individual identity**; a link prediction score is an association candidate only.
- Generate transaction, address, candidate entity and subgraph embeddings at a defined cutoff. Candidate entity embeddings need versioned MCER membership; no future cluster leakage.
- MCER uses embeddings as H3 candidate evidence; motif engine uses subgraph nearest-neighbor/novelty; stack uses trained graph heads or embeddings; Δ learns chain/wire predictability of *valid paired observations*.
- Repeat graph training within chronological folds; persist snapshot, node/edge feature schema, missingness masks, neighbor sampler seed and model checkpoint.

## 3. Resource tiers (all targets to measure)

**CPU-first:** Parquet/DuckDB, hand features, a small NetworkX fixture, random-walk baseline, classic ML. **GPU-enabled:** PyTorch Geometric graph mini-batches with bounded fan-out; optional heterogeneous encoder. **Research-tier:** temporal heterograph encoder + contrastive alignment only if authentic paired data and memory permit. None of these is proven to run on the user's hardware before benchmark.

Never train the entire huge Bitcoin graph in memory by default. Partition windows, fetch bounded temporal neighbors and store immutable feature tables. Measure peak RSS/VRAM, rows/s, graph build, per-subject inference latency and model size.

## 4. Stacking eligibility and comparison

Four source diagram families:
1. rule-defined patterns (non-ML);
2. supervised LR/RF/LightGBM on valid labels;
3. unsupervised IF/OCSVM/GMM/DBSCAN novelty;
4. GraphSAGE/GAT/temporal heads and reconstruction novelty.

Chronological OOF base prediction table feeds LR (or justified LightGBM) meta-learner; add valid Δ/Π/motifs + mask features; **exclude MLRP from pass-1**. Test each model family separately and compare against tabular/chain-only controls. Data gaps -> unsupervised ranking, no claimed anomaly probability.

## 5. Selection and rejection rubric

A challenger model can replace baseline only with measured improvement on **untouched future data**, stable calibration (if probability), tolerable false positive rate for legitimate service cohorts, manageable CPU/GPU latency, valid offline packaging, model artifact safety and reasonable explanation. Report comparative uncertainty, training cost and known failure modes.

Do not select a model solely from a Kaggle leaderboard or static synthetic accuracy; do not train on artificial labels and call it Bitcoin crime detection.

For exact training and OOF discipline see [stacking architecture](../architecture/stacking-architecture.md) and [experiment plan](experiment-plan.md).
