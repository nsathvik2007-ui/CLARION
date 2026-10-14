# Stacked Graph-ML Anomaly Detection — Detailed Design

> **Status: architecture only; no model has been trained.** This plan expands **§6** and related §3/§5/§7/§8/§9 blocks of the uploaded CLARION v4 diagram. Recommended engineering choices below are proposals; base model families, OOF stacking, meta-feature families and the calibrated anomaly score are **from the diagram**.

## 1. Purpose and prediction levels

For each **transaction** (primary), **address**, **candidate entity** and selected **subgraph** (secondary), produce a time-valid, reviewable anomaly/novelty signal with evidence, evaluation context, coverage and uncertainty. Never conflate "unusual" with "illicit". A model operating on one level must not be silently interpreted at another level.

### 1.1 Input/output contract

**Inputs:** immutable evidence graph snapshot at cutoff T; chain features, wire features when validated, graph embeddings; candidate MCER membership version; motif scores; optional eligible Δ residual/components and Π component bills; valid labels with availability time; training masks and coverage scores.

**Local stack output record (proposed):**
- subject_id, subject_type, event_cutoff, evidence_run_id, graph_snapshot_id, mcer_version, feature_schema_version;
- mode: SUPERVISED_CALIBRATED | SUPERVISED_UNCALIBRATED | UNSUPERVISED_RANK | ABSTAIN;
- base_predictions: per-model score **type**, value, training-version and source availability;
- local_meta_score and (only when justified) calibrated_probability and uncertainty method/interval or prediction set;
- feature availability masks and explicit abstention reasons;
- explanations: top meta-features, model versions and motif references;
- **no** current subject propagated risk in the pass-1 score.

**Distinct score types:** raw decision values, unsupervised novelty ranks, calibrated anomaly probability, conformal p-values/prediction sets and priority score are **not interchangeable**.

## 2. Exact four-family base learner architecture

| Family in uploaded diagram | Planned implementation | Primary input | Output | Gating |
|---|---|---|---|---|
| Rule scoring | PAN-in/PAN-out, rapid high-value movements, known risky *pattern hypotheses* | chain/motif windows | interpretable rule score 0–1 and witness edges | always possible if supporting fields exist; not a trained model |
| Supervised | Logistic Regression; Random Forest; LightGBM (optional) | causal tabular/graph features | supervised decision score; probability only after validation | trustworthy, temporally eligible labels only |
| Unsupervised | Isolation Forest; One-Class SVM; Gaussian Mixture; density/clustering support via DBSCAN/hierarchical | chain features + embeddings | novelty/anomaly rank and density/cluster diagnostic | valid unlabeled training window; no illicit probability |
| Graph ML | GraphSAGE/GAT classifier head; temporal graph model; embedding novelty or reconstruction error | typed graph snapshots with cutoff masks | node/subgraph representation-dependent score | enough graph support, versioned encoder, leakage tests |

Node2Vec/random-walk features and static GNN baselines precede a heterogeneous temporal GNN. Prefer measured improvements over merely adding architecture complexity.

## 3. Leakage-safe training and stacked meta-model

~~~mermaid
flowchart TD
  A["Eligible evidence, labels and temporal snapshots"] --> B["Chronological train | calibration | untouched holdout"]
  B --> C["Expanding train-only folds F1...Fk (purged where needed)"]
  C --> D["Fit preprocessing, graph encoders, MCER state, base models in each fold"]
  D --> E["Predict next held-out fold: OOF base predictions"]
  E --> F["Attach time-valid motif, Δ, Π features and availability masks"]
  F --> G["Fit regularized Logistic Regression meta-learner"]
  G --> H["Optional LightGBM meta-learner comparison"]
  H --> I["Independent calibration / conformal validity check"]
  I --> J["Untouched later holdout; test FPR by benign cohort"]
  J --> K["Promote model only if all criteria pass"]
~~~

**Fold example (illustrative, not a required dataset clock):** train windows 1–4 → predict 5; train 1–5 → predict 6; train 1–6 → predict 7. Store each fold's exact cutoff, group leakage controls, label availability and graph snapshot ID. Feature imputation/normalization, encoders, MCER partitions and Δ/Π models must also be trained only on the fold's earlier data, not precomputed using the full dataset.

**OOF meta-feature vector** for subject i at time T may be:

~~~text
X_meta(i,T) = [
  p_LR_oof?, p_RF_oof?, p_LGBM_oof?,
  score_IF_oof?, score_OCSVM_oof?, score_GMM_oof?,
  score_GraphSAGE_oof?, score_GAT_oof?, score_temporalGNN_oof?,
  rule_pattern_score(T), motif_peel(T), motif_mix(T), motif_novelty(T),
  Δ_residual(T)?, Δ1..Δ5(T)?, Π_fee/hop/time/frag/infra(T)?,
  quality_masks, source_count, time_precision, feature_availability
]
~~~

Question marks mean feature **may be absent**. Mask and calibrate appropriately. Π costs remain separately itemized and in their original units; do **not** simply add their values to Δ or to other costs. Avoid per-model overcounting if many learners are near-identical. Store probability calibration method and empirical reliability/coverage.

**Critical non-circular correction:** the uploaded §6 box also proposes a graph-propagation meta-feature, while §10 seeds propagation from §9 fusion. Therefore:
1. The **pass-1 stack** uses NO output of the pass-1-seeded MLRP.
2. **Freeze and hash** pass-1 local risk per entity; propagation reads only those seeds.
3. **Pass-2 fusion** may read the propagated score **once**, with **max 25/100 points** and no feedback into the frozen seeds.
4. If learning pass-2 weights, its MLRP meta-features must be created out-of-fold, with historical trained pass-1 models; otherwise use an auditable deterministic cap.
5. Training/validation reports explicitly state this resolution of the diagram's circular dependency.

### 3.1 Supervision and abstention

- Trusted labels: use supervised base predictions, chronological OOF stack and qualified probability calibration on held-out data.
- No trusted labels: learn distinct unsupervised novelty detectors and rank their outputs using training-only reference distributions; no meta-logistic probability of illegality.
- No valid wire: chain-only graph stack; Δ and cross-layer wire features **ABSTAIN**, not zero.
- No reliable Π objectives: Π components **ABSTAIN**, not zero.
- If a fold lacks enough positive/negative labels or adequate temporal support, remove that supervised learner from the eligible experiment and document why.

## 4. Model evolution (offline training lifecycle)

Dataset/label ledger → schema and availability audit → chronological folds → baseline fit → fold-local GNN/MCER + features → base OOF prediction table → meta-learner training → later calibration → untouched future holdout → subgroup false-positive audit → model card and signed/hash manifest → packaged offline inference artifact → drift diagnostics → challenger retraining and manual promotion.

**Artifacts:** base model files, encoder checkpoints, OOF prediction Parquet, fold manifest, fitted scalers, feature/label schema hashes, calibration diagnostics, threshold selection, model card, license/SBOM references, CPU/GPU compatibility and rollback version.

### 4.1 Statistical evaluation and reporting

- PR-AUC (primary in imbalanced labeled tasks), ROC-AUC, recall, precision, F1, precision@K and detection delay where timestamps support it.
- Error/false-positive breakdown for ordinary wallets, exchanges, custodial services, processors, CoinJoin participants, mobile/VPN users.
- Calibration diagrams/Brier/ECE if valid; abstention rate; uncertainty interval coverage when assumptions hold.
- Baseline-vs-GraphSAGE-vs-GAT-vs-hetero/temporal and chain-only-vs-cross-layer ablations using the **same** chronological cuts.
- If no validated real incident labels exist, report descriptive synthetic or benchmark metrics **only** for the named evaluation domain, with no operational accuracy claims.

## 5. Component ownership and implementation checklist

| Planned module | Responsibilities | Planned tests |
|---|---|---|
| src/clarion/detection/supervised.py | LR/RF/LightGBM wrappers; robust probabilities only as supported | class balance, train-only fit and serialization |
| src/clarion/detection/unsupervised.py | IF/OCSVM/GMM novelty with window normalization | ranks, missing-label behavior and stability |
| src/clarion/detection/graph_heads.py | GNN classifier/novelty heads on frozen graph snapshots | future-neighbor exclusion, graph batching |
| src/clarion/detection/stacking.py | time-respecting OOF prediction and meta-features | no in-sample training for meta-learner |
| src/clarion/training/splits.py | temporal folds, purge/group controls | leakage fixtures across address/entity overlap |
| src/clarion/training/trainer.py | pipeline orchestration and staged artifacts | stable resuming + fresh offline train runs |
| src/clarion/training/registry.py | model hashes/metadata and safe promotion | reject untrusted/mismatched artifacts |
| src/clarion/fusion/local.py | calibrated pass-1 combining supported signals | risk-only signal gate, no propagation circularity |

## 6. Acceptance gate before Phase 3 is complete

- [ ] OOF predictions documented for every trained base learner; no in-sample predictions in meta train table.
- [ ] Matching as-of snapshot, embeddings, MCER and feature cutoffs for each fold.
- [ ] Baseline + graph ML comparisons on held-out time splits.
- [ ] Supervised/calibrated vs unsupervised/uncalibrated modes explicitly differentiated.
- [ ] Δ/Π included only when valid; missingness is visible.
- [ ] Real source labels provenance checked; false-positive audit reported.
- [ ] No pass-1 dependency on pass-1-derived MLRP; phase-4 integration verified later.

**Primary source:** uploaded CLARION v4 Architecture (page 1), boxes 3, 5, 6, 7, 8, 9, 10 and 12. Numerical examples and software breakdown are implementation proposals.
