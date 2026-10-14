# Canonical evidence data dictionary — schema design v1

**Status: PROPOSED interface, not observed SIH data.** Derived from uploaded CLARION v4 diagram blocks 0/1A/1B/2/4/7/8/11 and SIH26146 minimum fields. Input samples and field units must be checked before a versioned parser is frozen.

## 1. Raw SIH input contract vs canonical normalized store

**SIH minimum:** timestamp, src_ip, dst_ip, src_port, dst_port, txid, input_addresses[], output_addresses[], input_amounts[], output_amounts[], geo_country/asn where available. Original diagram additionally mentions transaction fee, script type, block height (when supplied) and precise time. A single SIH row may combine a transaction and one observation; it can also have multiple network rows for one TXID. Do **not** deduplicate away independent sensor observations.

Raw fields are not enough to reconstruct Bitcoin ownership, exact UTXO history, complete fee/weight data, or originating peer. Split mixed rows into canonical **Transaction**, **Inputs/Outputs** and **NetworkObservation** events and keep \`source_row_id\` linkage.

### Raw CSV/JSON/XML adapter requirements

- CSV: preserve arrays using declared format (escaped JSON array preferred; comma-splitting addresses is unsafe); detect duplicate headers and Excel formula injection in later export.
- JSON: document top-level list vs object, nested arrays, duplicate keys and maximum depth/size; malformed values produce contextual errors.
- XML: secure bounded parse with external entities and DTD disabled; list elements have stable positional index; validate schema before creating graph edges.
- Timestamps: define ISO-8601 with UTC offsets for canonical; raw epoch sec/ms formats require explicit declared units, sensor precision and time source.
- Amounts: input BTC decimal strings convert exactly to signed? **non-negative integer satoshis** with fixed 8 decimal places; reject float rounding, NaN, infinities, negative output values and overflowing values. A zero-value output may exist (e.g. OP_RETURN) and is not a missing amount.

## 2. Minimal canonical tables

| Table | Keys | Fields and types | Invariant |
|---|---|---|---|
| evidence_sources | source_id string | file_sha256, capture_sensor_id?, dataset/source version, license, clock_accuracy_ms?, imported_at, parser_ver | immutable origin; never expose sensitive local path in UI |
| blocks | block_hash string, height int | header_time_utc, median_time_past?, chain_status, orphaned_at? | block time ≠ first seen transaction time; reorgs versioned |
| transactions | txid bytes32/hex | source_id, block_hash?, height?, block_time?, first_seen_time?, fee_sats?, vsize?, weight?, locktime?, status | synthetic fake IDs must be explicitly marked; unmatched block does not imply mempool state |
| tx_inputs | (txid, vin_index) | prev_txid?, prev_vout?, address_annotation?, prev_value_sats?, sequence?, script_type? | exact lineage needs prevout; missing value is unknown |
| tx_outputs | (txid, vout_index) | value_sats int64, script_pubkey_hex?, address_annotation?, script_type?, spendable? | not all Bitcoin scripts have a conventional address |
| network_observations | observation_id | sensor_id, observed_at_utc, accuracy_ms?, src/dst_ip, src/dst_port, observed_txid?, event_type?, direction?, source_id | may be a relay, not origin; exact TXID claim requires decoded message provenance |
| sessions | session_id | sensor_id, endpoints, protocol, first_seen, last_seen, event_count, capture_coverage | source of co-session evidence, not proof of ownership |
| ip_enrichment | (ip_or_prefix, db_version) | asn?, country?, category?, lookup_status, confidence_source | offline licensed DB; country is approximate context |
| graph_nodes | (snapshot_id, node_id) | node_type, valid_from, source_refs[], label? | exactly six canonical node types |
| graph_edges | edge_id | from_id, to_id, type, valid_time, amount_sats?, evidence_refs[], confidence_type, confidence_value? | only allow direction-typed observed/candidate links |
| entities | (entity_id, version) | member_address_ids[], as_of, merge/split parent_ids[], evidence/conflicts, membership_confidence | candidate clusters not real identities |
| motif_instances | motif_id | kind, as_of, actor?, txids[], witness_edge_ids[], confidence, benign_alternatives | only a candidate pattern |
| labels | (dataset, subject, label_version) | value, subject_level, source, available_at, unknown_flag, reviewed_status, split_role | confidential truth never joined into predictors |
| economic_objectives | goal_id | verified controlled_inputs?, intended_payees?, cutoff, fee_environment_id?, constraints, provenance, confidence | incomplete means Π partially or fully abstains |
| runs | run_id | input hashes, code/config/model hashes, timestamp policy, gates, artifact paths | reproducibility and safe resume |
| risk_results | (run_id, subject) | stack score_type/value, Δ?/Π?, frozen local, forward/backward exposure, final points?, priority?, abstention | never coerce missing to 0 |
| audit_events | event_id | case/run, investigator role, action, timestamp, artifact/evidence hash | tamper-evident review ledger |

## 3. Valid addresses, UTXOs and monetary constraints

Bitcoin transaction inputs spend **outpoints** (prev_txid, prev_vout); common-input address heuristics are *uncertain control hypotheses*. For nonstandard outputs store script bytes when supported and \`address_annotation=null\`. If complete resolved inputs are available on standard non-coinbase transactions, \`sum(input_sats) = sum(output_sats) + fee_sats\`; otherwise fee remains unknown/partial, not fabricated. Chain reorganizations and double-spend/replacement transactions require a versioned chain-state view.

Optional \`vsize/weight\` should be derived from actual transaction encoding when available, not guessed from an address prefix. Per-window fee environment needs representative local sample and block/mempool context. Reuse a stable outpoint identity even if the address is reused.

## 4. Time semantics

| Name | Meaning | May be used as |
|---|---|---|
| observed_at | sensor logged relayed message | wire behavior within capture precision |
| first_seen_at | node-specific first observed TXID event if supplied | observational ordering, **not global origin** |
| block_header_time | miner-supplied header time | approximate block ordering/context, not broadcast time |
| median_time_past | Bitcoin chain consensus context | temporal rule checks where validated |
| imported_at | ingestion clock | pipeline audit only; **never** behavioral timing |
| label_available_at | time annotation became available | eligibility boundary in training |
| as_of/cutoff | latest allowed event time in an analysis | must be enforced across all features/models |

Do not infer a P2P impossibility from two country codes without clock precision, evidence of sensor location, and reliable timing model.

## 5. Exact graph type contract

**Node types:** Transaction, Address (script/address annotation), Entity (candidate), Host, ASN, Country.

**Edges and semantic class:** spending and funding (value-flow), Host→Transaction observed_broadcast (network observation), Host↔Host co_session (network), Host→ASN hosted_in (enrichment), Host/ASN→Country geo_context (enrichment), Address→Entity member_of_candidate (inferred).

Per edge: event time, type, source evidence, confidence **kind** (observed vs inferred vs geographic lookup), optional normalized numeric confidence, snapshot cutoff. Country is not risk-scored. Inferred Host→wallet ownership edge is explicitly forbidden.

## 6. Nulls and validation boundaries

- Required \`txid\` in a chain row; observed_txid may be null in wire row.
- Missing address annotation means unknown/nonstandard script, not ownership absence.
- Missing input/outpoint fee/value means unknown, not zero.
- Missing country/ASN is allowed; infer neither from public address nor from a geolocation guess.
- IP accepts IPv4 and IPv6; '/24' prefix is an IPv4 **feature proposal**, not correct for all network types.
- Port int 0–65535 technically representable; distinguish invalid source data/ephemeral range by observation semantics.
- Unique source line ID + file hash; duplicate data within captures may be preserved but duplicate *same sensor event* is explicitly classified.

## 7. Source & confidence record

\`EvidenceReference = {source_id, original_row_id, raw_hash, parser_version, observation_kind, recorded_time?, precision?, uncertainty_flags[]}\`. Never copy raw secrets into a report and never promote inferred attributes into source evidence.

**Next required implementation artifact:** exact versioned JSON/Arrow schema files, v1 CSV/JSON/XML fixtures, expected normalized outputs, robust false-association tests. These cannot be fully frozen without the organizer's actual file examples.
