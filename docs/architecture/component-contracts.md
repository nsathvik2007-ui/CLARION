# Cross-component contracts, dependency DAG and failure semantics (design v1)

**Architecture only; interface field names are PROPOSED** and must be frozen as machine-readable versioned schemas during Phase 1. Source is the uploaded v4 PDF blocks 0–12; no code exists.

## 1. Common envelope for every derived artifact

Every derivation must contain: \`run_id\`, \`schema_version\`, \`artifact_id\`, \`source_evidence_ids[]\`, \`snapshot_cutoff_utc\`, \`produced_at_utc\`, \`code_version\`, \`config_hash\`, \`data_hash\`, \`method\`, \`confidence_kind\` and \`limitations[]\`. Keep raw original time, source capture time, block time and derived feature-availability time distinct.

Use \`status=AVAILABLE | PARTIAL | ABSTAIN | ERROR\`. Only AVAILABLE/PARTIAL records can have supported numeric fields. ABSTAIN has \`reason_codes[]\`, \`missing_prerequisites[]\`, and \`evidence_count\`; never substitute zero. Separate label provenance and withheld ground truth from feature/serving fields.

## 2. Module interfaces (types here are schematic)

| Producer → consumer | Named versioned record | Required contents | Contract guard |
|---|---|---|---|
| Ingest → readiness/chain/wire | NormalizedBatchV1 | typed tx/inputs/outputs/observations; source/time and invalid-row report | exact sats, canonical time; no unapproved coercion |
| Chain → graph/features | ChainFlowV1 | outpoint links, value_sats, time and UTXO completeness | missing prevout signals unknown, not a fabricated input |
| Wire → graph/features | WireEventV1 | sensor ID, src/dst IP-port, observed_txid?, time precision, source hash | observed relay is not ownership |
| Readiness → orchestrator | ReadinessDecisionV1 | CHAIN_ONLY/CROSS_LAYER, quality/coverage, SUPERVISED/UNSUPERVISED and per-component abstention | no cross-layer model on invalid paired views |
| Graph → ML/MCER/motifs | EvidenceGraphSnapshotV1 | six typed node tables, relation allowlist, dated directed edges, provenance, valid cutoff | no post-cutoff edges; no host→address owner edge |
| Features → learners | FeatureFrameV1 | subject level/id, cutoff, feature_name/version/units, masks, evidence refs | no training-period future leakage |
| Representation → downstream | EmbeddingSetV1 | subject id/type, encoder checkpoint/version, dimension, view, fold cutoff, uncertainty/masks | type-aware dimensions and train-fold fit |
| MCER → graph/fusion | EntityHypothesisV1 | cluster version, member addresses, H1–H5 evidence, constraints, confidence, lineage | uncertain candidates never asserted identity |
| Patterns → stack/fusion | MotifEvidenceV1 | motif kind, subject, time span, score type, witness path, benign alternatives | no pattern called a legal finding |
| Base models → stack | OOFBasePredictionV1 | model id, subject/time, fitted fold ID, prediction score type, OOF status | meta training rejects in-sample predictions |
| Stack → fusion | AnomalyEstimateV1 | calibrated_probability? or novelty_rank, base/model versions, validity, uncertainty | mutually exclusive probability/novelty representations |
| Δ → fusion | DivergenceEvidenceV1 | paired-view coverage, residual, Δ1–Δ5, uncertainty, abstention | no invented cross-view operator |
| Π → fusion | ExpenditureBillV1 | goal/baseline IDs, cost items with units, signed premiums, abstentions | no mixed-unit raw sum |
| Fusion 1 → MLRP | FrozenSeedManifestV1 | immutable subject provisional risks, hash, cutoff, source evidence | cannot be mutated by MLRP |
| MLRP → fusion 2 | PropagationResultV1 | five scored levels, contextual Country, forward/backward, value/context channels, paths, contributing seeds | ≤6 scored hops; service blocks; no circular feedback |
| Fusion 2 → API | LeadV1 | local/propgated/final component scores, priority, calibration type, model/evidence IDs | propagation contribution ≤25/100 |
| API → UI/export | InvestigatorCaseV1 | time-bounded graph, explanations, linked evidence, redaction and audit | offline, role-gated, no ownership claims |

## 3. Graph relation semantics: allowed and forbidden

**Allowed factual edges:** Address → spends → Transaction (interpret address from spending script cautiously); Transaction → funds → Address (or script output), Host → observed_broadcast_of → Transaction with explicit observed TXID, Host ↔ co_session ↔ Host (observed network interaction), Host → hosted_in → ASN, Host/ASN → geographical_context → Country.

**Candidate only:** Address → member_of_candidate → Entity with MCER evidence and valid time; change_address_candidate; cross-layer embedding-suggested association. Neither implies legal identity.

**Forbidden:** Host owns Address or Entity from observed TXID; ASN owns wallet; Country carries illicit risk; an inferred cross-layer link promoted to factual record; risk edges backwards in time; propagation back into its own pass-1 seed.

## 4. Risk and score semantics

- A **raw base score** is model-specific and may be unbounded.
- A **novelty rank** is relative to a reference population and is not a probability.
- A **calibrated anomaly probability** requires held-out trustworthy labels and measured calibration.
- A **conformal p-value/interval** requires valid calibration/exchangeability assumptions; cannot simply combine as independent p-values.
- **Δ** is a cross-view residual with component explanation; **Π** is an itemized cost with independent units and goal.
- **MLRP** is exposure to a frozen seed/path, not guilt and not a new independent label.
- A **priority score** is an investigator-review ranking calibrated/validated against false positive budgets where possible.
- A **priority band** P1–P4 is a routing policy and thresholds must be versioned.

## 5. Operational errors and contract migration

Structural parsing failure quarantines input, row error accumulates when safe. Unavailable optional evidence -> PARTIAL/ABSTAIN; invalid model artifact -> ERROR and no inference. Mismatched feature versions -> no silent fallback. Schema migrations use semantic compatibility tests and retain the old artifacts. Treat all IDs as opaque strings with validated formats; do not expose private raw paths in API.

## 6. Contracts that remain unfrozen

Byte-exact JSON/Arrow schemas and the precise confidence-calibration math are a **Phase 1 deliverable** after real SIH sample inspection. These prose contracts are not machine-readable APIs and do not imply production readiness. See [REQUIREMENTS_AUDIT.md](REQUIREMENTS_AUDIT.md) decisions D01–D12.
