# Cross-layer correlation contract and quantitative go/no-go procedure

**Architecture only — no real observations have been evaluated.** Required by CLARION PDF block 0 (TXID, temporal alignment, coverage, chain–wire dependence) and blocks 1B/2/7/4. A network TXID observation is evidence that a peer *relayed/was observed discussing* a transaction, **never proof the peer originated it, controls the input addresses, or is one person**.

## 1. Allowed evidence tiers (in descending factual strength)

- **J0 exact on-chain:** Bitcoin input references prior TXID+vout, subject to chain-state and parser verification. This is value flow and independent of P2P.
- **J1 observed transaction relay:** network row contains an actually decoded **exact observed TXID**, event type, sensor, observed_at/precision, endpoints and source hash. Create Host→observed_broadcast→Transaction edge; no ownership edge.
- **J2 contextual co-observations:** host-host session, subnet, ASN, country, time rhythm or proximity. Only graph feature/context; cannot create Wallet↔Host ownership.
- **J3 research candidate:** embedding/link predictor suggests host/address association. Must remain a distinct **hypothesis**, reviewed/calibrated, and never merged into J0/J1 ground truth.

One TXID can be seen at hundreds of hosts. Do not count repeated relay sightings as independent originating-peer evidence. A single sensor may observe duplicate events, timeouts and retransmissions.

## 2. Validation stages before J1 graph edge

1. **Source:** sensor/capture ID, file hash, legal provenance, protocol decoder, observation message class and confirmation the packet metadata truly exposes TXID (not merely a guessed connection).
2. **Syntax:** exact TXID normalized under declared byte order; valid timestamp, IP family, IP/port and sensor precision.
3. **Join:** equality with known chain TXID, not amount/temporal/geo heuristic. Multiple sensors produce multiple observation records (dedup exact repeat within a sensor).
4. **Temporal:** compare *compatible event-time meanings*. A genuine broadcast should generally precede first block inclusion, but Bitcoin re-relays/reorgs and clock faults can violate naive rules; flag anomalies and classify confidence rather than enforcing universal first-seen assumptions.
5. **Coverage:** count captured wire observations, TXID-present fraction, distinct joined transactions, sensor diversity, time-span overlap, number of hosts and missingness by period.
6. **Association uncertainty:** provenance/precision/conflicting reports, relay types, source independence and sensor overlap. High confidence in *observing a relay* does not imply high confidence in *originating the transaction*.
7. **Routing:** if data lacks real TXID observations, valid overlap, or trustworthy coverage, **CHAIN_ONLY** and Δ abstention. Never fill missing links with synthetic pretend-real associations.

## 3. Statistical dependence test (design protocol, not arbitrary known threshold)

**Question:** do paired chain/wire features predict anything beyond sampling artifacts, chance and identity/time confounds? This is a utility gate, **not an ownership proof**.

Pre-register:
- as-of analysis unit (transaction/time-window/selected address cluster) and valid feature pairing;
- paired samples counted as *independent units*, with sensors/hosts/transactions grouped to avoid pseudo-replication;
- null models preserving within-day activity levels and capture sensor/host frequency (e.g., constrained time permutation);
- MI/CCA baseline and held-out predictive improvement over shuffled/control pairing;
- coverage thresholds, significance levels, correction for multiple comparisons, minimum effect size and fallback policy;
- withholding extreme high-degree relay nodes and evaluating robustness to NAT/hosting/exchange-like controls.

Perform all thresholds/model fits in the training period only. Report paired N, independent N, observed and shuffled performance, confidence intervals/sensor stratification and exact null construction. **Non-significant or unstable dependence → cross-layer Δ/paired learning abstain.** A significant MI does not imply common wallet controller.

## 4. Temporal alignment and capture bias

Record \`observed_at\`, \`accuracy_ms\`, sensor drift correction source, block_header_time, first_seen semantics and analysis cutoff. Only compare source-congruent timestamps. Source IP vs destination IP depends on sensor placement and message direction; do not assign "sender wallet" labels. GeoIP region may reflect VPN or data-center egress, not human location.

For routing "impossibility" Δ4, demand independent physical/network constraints and calibrated uncertainty; ordinary multi-ASN/time-zone sightings cannot be called physically impossible.

## 5. Label gate, independent from wire gate

Valid labels need documented source, subject granularity, available_at, class definitions, and enough samples in chronological OOF folds and an untouched future holdout. If missing, run **UNSUPERVISED_ONLY** even if chain/wire is valid. If wire absent but labels valid, supervised **CHAIN_ONLY** can still run.

## 6. Result contract for every run

~~~text
JoinAudit:
  source_hashes, schema_versions, sensor_inventory
  chain_count, wire_count, observed_txid_count, exact_joined_txid_count
  paired_independent_n, overlap_window, distinct_host_count
  precision_error_counts, source_duplication_counts, coverage_by_sensor
  shuffled_null_method, dependence_estimate?, confidence_interval?, p_value?
  cross_layer_route = VALIDATED | CHAIN_ONLY | INSUFFICIENT_DATA
  delta_route = AVAILABLE | ABSTAIN
  label_route = SUPERVISED_ALLOWED | UNSUPERVISED_ONLY
  reasons[], quality_flags[], error_artifact_hash
~~~

## 7. Required adversarial and regression tests

- missing observed TXID cannot produce any chain–wire edge;
- exact same TXID from many hosts produces observation edges but **zero** ownership edges;
- replay/dup capture from same sensor does not inflate independent N;
- clock-offset/timezone/unit tests preserve uncertainty;
- shuffled chain–wire pairs fail a meaningful dependence gate;
- Tor/VPN/NAT, common ASN, hosted service, false country conflicts cannot veto ownership with certainty;
- false multi-input entity merge in CoinJoin-like transaction stays contested;
- no label leakage or derived-timestamp leakage into split/correlation models.

**Unresolved until real dataset:** capture protocol/packet decoding details, training-window coverage threshold, null distribution, sensor accuracy model and cross-view subject grain. See [Architecture audit](../architecture/REQUIREMENTS_AUDIT.md).
