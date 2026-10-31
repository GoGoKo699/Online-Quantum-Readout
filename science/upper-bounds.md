# Upper bounds and the value of batching

The [model and theorem](model-and-theorem.md) distinguish source queries from the cost of implementing known observable operations. This page proves the source-query upper bounds by scheduling an established simultaneous estimator. The [lower bound](lower-bound.md) shows why unrestricted retained memory cannot generally improve their dependence on when requests are revealed.

## The imported simultaneous estimator

Huggins et al., *Physical Review Letters* **129**, 240501 (2022), [Theorem 1](https://storage.googleapis.com/gweb-research2023-media/pubtools/6446.pdf), give the following primitive. For a known list of $`M`$ Hermitian observables of norm at most one and a pure state prepared by $`U`$, an algorithm returns all $`M`$ expectations to additive accuracy $`\epsilon`$, jointly with probability at least $`2/3`$, using

```math
\widetilde O\!\left(\frac{\sqrt M}{\epsilon}\right)
```

calls to $`U`$ and its inverse. The bound does not require the observables to commute and does not acquire a factor polynomial in the state dimension. Its known-operator requirements are controlled exponentials of the individual observables; those operations are accounted for below and in the [resource ledger](resources-and-interpretation.md).

The construction encodes the desired expectation values as derivatives of a function evaluated by a quantum circuit and uses quantum gradient estimation. Both this algorithm and its fixed-list scaling are inherited results. The present contribution concerns online revelation and the lower bound that holds even with arbitrary persistent memory.

For failure target $`\delta`$, run the primitive independently an odd number $`k=O(\log(1/\delta))`$ of times and take the coordinatewise median. Whenever more than half the runs succeed on their entire lists, every coordinate median is accurate. A Chernoff bound therefore gives simultaneous failure at most $`\delta`$. This amplification uses fresh workspace and fresh source queries; it neither assumes independence between different observables nor divides the success probability by $`M`$ unnecessarily.

## Answer each current batch

Let the predetermined batch sizes be $`b_1,\ldots,b_R`$, with $`1\le b_r\le L`$, and put

```math
A=\sum_{r=1}^{R}\sqrt{b_r}.
```

In round $`r`$, apply the primitive only to the revealed batch, with failure probability $`\delta_r=1/(3R)`$. Output those estimates before accepting the next batch. The total source cost is

```math
Q_{\mathrm{batch}}
=\widetilde O\!\left(\frac{A}{\epsilon}\right).
```

This argument permits the next batch to depend arbitrarily on earlier outputs. Conditional on every realized preceding transcript, the newly selected observables form a valid known list, and the fresh run has failure probability at most $`\delta_r`$. Averaging over the transcript and taking a union bound over rounds bounds the probability of any inaccurate answer by $`1/3`$. There is no assumption that adaptively selected queries are independent of previous estimation errors.

The schedule does not use earlier quantum memory, although keeping such memory is allowed. That makes it a valid upper bound for the larger class of algorithms in the theorem, without suggesting that discarding memory is compulsory.

## Read the whole known menu once

Alternatively, apply the primitive to all $`L`$ observables before answering the first batch, at joint failure probability $`1/3`$. Store the resulting classical estimates. The source cost is

```math
Q_{\mathrm{menu}}
=\widetilde O\!\left(\frac{\sqrt L}{\epsilon}\right).
```

On the single event that the whole menu was estimated accurately, every later answer is accurate, however the requests are selected or repeated. This uniform event is why the finite known menu matters. The model imposes an information deadline between rounds, not an external wall-clock limit on processing the first round.

Choosing the less expensive schedule proves

```math
Q_{\mathrm{online}}
\le\widetilde O\!\left(
\frac{\min\{A,\sqrt L\}}{\epsilon}
\right).
```

The algorithm knows the announced sizes and number of rounds, so it can make this choice without seeing future batch identities. This upper bound holds more generally than the high-precision parameter regime in which the matching lower bound is proved. The tilde hides the estimator's logarithmic factors and confidence amplification; it does not hide a power of $`L`$, $`b_r`$, or $`R`$ in the source-query claim.

## Compare deadlines while holding the request count fixed

For equal-size batches, write $`T=Rb`$. Then $`A=R\sqrt b=\sqrt{RT}`$, and the matching frontier is

```math
Q_{\mathrm{online}}
=\widetilde\Theta\!\left(
\frac{\min\{\sqrt{RT},\sqrt L\}}{\epsilon}
\right),
\qquad 0\lt \epsilon\le\frac{1}{2\sqrt{2L}}.
```

The same total number of answers can therefore require different source access depending on how many answer deadlines intervene. Before saturation at the cost of the whole menu, splitting one batch into more rounds increases the worst-case source cost.

If an actual fixed request list of length $`T`$ is disclosed in advance, the simultaneous primitive needs at most $`\widetilde O(\sqrt T/\epsilon)`$ source calls. Repeated observables can be deduplicated, further reducing this bound. For a direct comparison on the same distribution of tasks, draw independent single-observable requests and either disclose all of them at the start or disclose one only after the previous answer. When $`L\ge T^2`$, the online lower bound is $`\Omega(T/\epsilon)`$, whereas offline disclosure admits the stated $`\widetilde O(\sqrt T/\epsilon)`$ upper bound. The separation is by order $`\sqrt T`$, up to logarithms.

This comparison is in a compatible high-precision regime. For example, choose $`L=T^2`$ and $`\epsilon=1/(4T)`$. The online lower scale is then $`T^2`$ source calls and the offline upper scale is $`T^{3/2}`$, up to logarithms and absolute constants. Keeping $`\epsilon`$ fixed while sending $`T`$ to infinity would leave the proved regime and is not a consequence of the theorem.

For an adaptively generated request process, revealing its eventual realized list in advance changes the interaction, since that list can depend on the algorithm's outputs. The explicit offline-versus-online separation above uses an oblivious request distribution and avoids this ambiguity.

## Known-observable operations remain charged

Theorem 1 of Huggins et al. uses $`\widetilde O(\sqrt M/\epsilon)`$ controlled exponentials **for each** of the $`M`$ observables, with evolution parameters of magnitude $`O(1/\sqrt M)`$. Thus its total number of controlled observable exponentials is

```math
\widetilde O\!\left(\frac{M^{3/2}}{\epsilon}\right).
```

Consequently the per-batch schedule has total known-exponential count $`\widetilde O(\sum_r b_r^{3/2}/\epsilon)`$, whereas the full-menu schedule has count $`\widetilde O(L^{3/2}/\epsilon)`$. The source-optimal schedule need not minimize the full implementation cost. A comparison that weights source preparation and known gates must include the actual implementation and precision cost of those exponentials.

Other simultaneous estimators can trade different known-oracle resources. The [resource ledger](resources-and-interpretation.md) states the SELECT/block-encoding charges and dimension logarithms in van Apeldoorn et al.'s alternative. No coherent lookup, QRAM, Hamiltonian simulation, or classical description-to-circuit compilation is free in an end-to-end runtime claim.

## What the two schedules do and do not establish

The upper bounds are constructive once the specified known-observable operations are available. Their contribution here is the schedule comparison; the estimator itself is credited to prior work. The lower theorem supplies the missing statement that a coherent online algorithm, even with unrestricted memory, must incur the per-batch cost until it has spent enough queries to cover the menu globally.

These are worst-case source-query bounds. Special menus, repeated requests, known state structure, or a particularly informative completion of the source unitary can be easier. The [commuting example](commuting-witness.md) makes the completion issue concrete. The result does not assert a separation at every precision or a universal wall-clock advantage for batching.
