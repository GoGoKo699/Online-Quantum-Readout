# Scientific account

An expensive quantum state preparation can support many expectation-value queries. Existing simultaneous estimators exploit advance knowledge of the requested observables. This project asks what changes when an answer must be returned before the next request is known, even though the state source remains available and all earlier quantum information can be retained.

The answer is a worst-case source-query frontier controlled by the sum of square roots of the revealed batch sizes, capped by the cost of estimating the full known menu. The restriction comes from the timing of task information. It does not impose a bound on quantum memory, coherent computation, or the number of source revisits.

## Reading route

1. [Model and exact theorem](model-and-theorem.md): oracle access, success and cost conventions, quantifiers, precision regime, and the stated frontier.
2. [Upper bounds and batching](upper-bounds.md): the inherited simultaneous-estimation primitive, adaptive requests, the full-menu alternative, and a compatible offline comparison.
3. [Lower bound with retained quantum memory](lower-bound.md): the star family, exact oracle commutators, global information progress, fresh requests, and adaptive stopping.
4. [A commuting product-state witness](commuting-witness.md): the same obstruction for one-local commuting observables, together with an easier source completion for the same prepared states.
5. [Resources and interpretation](resources-and-interpretation.md): source queries versus known gates, physical meaning, examples, and consequential limits.

The theorem has one authoritative statement in the model page. The lower-bound pages prove its two witnesses. The upper-bound page credits the imported algorithm instead of presenting it as a new estimator.

## Attribution and verification

The [related-work account](../references/related-work.md) compares the closest batch-estimation, online shadow-tomography, deferred-objective, quantum-advice and consumable-data models. The [bibliography](../references/bibliography.bib) records primary sources and versions.

The [verification suite](../verification/README.md) independently constructs finite oracle matrices and compares them with the proof's commutator identities and bounds. These finite checks support the conventions and calculations; the written argument and its cited ingredients establish the general theorem.
