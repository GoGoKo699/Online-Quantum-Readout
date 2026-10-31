# Online quantum readout: model and main theorem

The full menu of possible observables can be known while the particular questions arrive over time. This distinction matters when an answer is due before the next question is revealed. The result below characterizes the worst-case number of calls to a coherent state-preparation source in this setting. It permits arbitrary retained quantum memory and continued source access between answers.

## 1. Source access and the public menu

Let $`L`$ be a positive integer. The public input contains a finite-dimensional source register, a known reference state $`|\perp\rangle`$, and a menu of Hermitian observables $`O_1,\ldots,O_L`$ on that register, with

```math
\|O_i\|\leq 1\qquad (1\leq i\leq L).
```

The unknown pure state is supplied through a unitary oracle $`U`$ satisfying

```math
U|\perp\rangle=|\psi\rangle.
```

The allowed source operations are $`U`$, $`U^\dagger`$, and their controlled versions. Each invocation costs one source query. The algorithm may apply the source to arbitrary inputs; the oracle is the full unitary, not only its action on $`|\perp\rangle`$. Its classical matrix description is not supplied. A fixed, known change of basis can replace $`|\perp\rangle`$ by a conventional all-zero input without changing the source-query count.

The menu is supplied through known, implementable descriptions. The upper bound uses controlled exponentials of these known observables, or a suitable block-encoding implementation of an established batch estimator. Those operations, their compilation, arithmetic, memory, and classical output costs are separate resources. They are not additional free state-preparation calls, and this result does not assert optimal total gate complexity. No QRAM or uncharged loading of the unknown state is assumed.

Arbitrary finite quantum and classical working memory is allowed, with no bound imposed as a function of $`L`$. The algorithm may retain all earlier data. Source-independent computation, measurements, classical feedback, and restarts are allowed. Every source call made during preprocessing, an unsuccessful attempt, or a later round is charged. Conditioning on a favorable measurement outcome does not erase the cost or failure probability of the other outcomes.

## 2. Requests, deadlines, and accuracy

Fix positive integers $`R`$ and $`b_1,\ldots,b_R`$, with $`1\leq b_r\leq L`$. The batch sizes are predetermined and public. Define

```math
T=\sum_{r=1}^{R}b_r,
\qquad
A=\sum_{r=1}^{R}\sqrt{b_r}.
```

In round $`r`$, a subset $`S_r\subseteq\{1,\ldots,L\}`$ of cardinality $`b_r`$ is revealed. The algorithm must return a classical numerical estimate $`\widehat\mu_{r,i}`$ for each $`i\in S_r`$ before $`S_{r+1}`$ is revealed. Indices within a batch are distinct; an index may recur in later batches. Source access is available before the first reveal and throughout the protocol. Any source calls made in an optional interval before a later reveal also count.

A requester may choose future batches as a function of the public menu, its own randomness, and earlier returned answers. It cannot reveal a later batch before the current deadline. The theorem permits such adaptive requests, but it does not permit the batch sizes themselves to be chosen adaptively.

For every admissible source, public menu, and request policy, the algorithm must return all answers and satisfy

```math
\Pr\left[
\left|\widehat\mu_{r,i}-\langle\psi|O_i|\psi\rangle\right|\leq\epsilon
\text{ for every }r\text{ and }i\in S_r
\right]\geq\frac23.
```

The probability includes algorithmic measurements and randomness, together with any randomized request policy. Algorithms must complete the protocol almost surely. The lower bound also holds under a weaker correctness hypothesis: in each round of its specified hard distribution, the average error probability of a uniformly chosen requested hidden sign is at most $`1/3`$.

Let $`Q_{\mathrm{exp}}(L,(b_r),\epsilon)`$ be the infimum, over correct algorithms, of the worst-case expected number of source invocations. The worst case ranges over the source unitary, source dimension, public menu, and admissible request policy. Let $`Q_{\mathrm{cap}}`$ be the analogous complexity with a cap on the total number of invocations on every execution. In particular,

```math
Q_{\mathrm{exp}}\leq Q_{\mathrm{cap}}.
```

An invocation controlled by a quantum register costs one whole query, even when that register has small amplitude on its active value. A classical branch on which the algorithm does not invoke the source costs zero queries. The distinction is used explicitly in the expected-query proof.

## 3. Main theorem

**Theorem.** Suppose

```math
0<\epsilon\leq\frac{1}{2\sqrt{2L}},
\qquad
c_* = 1-\frac{2\sqrt2}{3}>0.
```

Then

```math
\frac{c_*}{16\epsilon}
\frac{A}{1+A/\sqrt L}
\leq Q_{\mathrm{exp}}(L,(b_r),\epsilon)
\leq Q_{\mathrm{cap}}(L,(b_r),\epsilon)
\leq
\widetilde O\!\left(\frac{\min\{A,\sqrt L\}}{\epsilon}\right).
```

Here the tilde suppresses logarithmic factors from the established batch estimator and the required confidence. Consequently, for both cost conventions,

```math
Q_{\mathrm{online}}(L,(b_r),\epsilon)
=\widetilde\Theta\!\left(
\frac{\min\{\sum_{r=1}^{R}\sqrt{b_r},\sqrt L\}}{\epsilon}
\right).
```

The explicit lower bound follows from a pure-state family in dimension $`L+2`$ and a known menu of rank-two observables. The lower-bound request process chooses each $`S_r`$ independently and uniformly among all $`b_r`$-subsets. Thus no adversarial adaptation of the requests is needed for the lower bound. The source unitary is a specified canonical swap completion of the preparation map. See [the complete lower bound](lower-bound.md).

The same asymptotic lower bound is witnessed by product states and a commuting menu of one-qubit Pauli observables. That construction uses $`L+1`$ physical source qubits and has an explicit constant-factor change. See [the commuting witness](commuting-witness.md).

The elementary comparison

```math
\frac12\min\{A,\sqrt L\}
\leq\frac{A}{1+A/\sqrt L}
\leq\min\{A,\sqrt L\}
```

relates the explicit lower bound to the stated frontier.

## 4. Upper bound and adaptive requests

The upper bound uses existing multi-observable estimation. Theorem 1 of Huggins et al., *Nearly Optimal Quantum Algorithm for Estimating Multiple Expectation Values*, gives a batch estimator with source-query complexity $`\widetilde O(\sqrt M/\epsilon)`$ for $`M`$ supplied norm-bounded observables. The paper also separately counts the required controlled observable exponentials. Its theorem can be amplified to failure probability $`\delta`$ with a logarithmic confidence overhead. See the [published primary paper](https://storage.googleapis.com/gweb-research2023-media/pubtools/6446.pdf).

There are two admissible schedules.

1. **Estimate the current batch.** After $`S_r`$ is revealed, run the batch estimator on its $`b_r`$ observables, with conditional failure probability at most $`1/(3R)`$. Summing its source calls gives $`\widetilde O(A/\epsilon)`$. For every realized earlier history, the current batch is now a supplied list and the estimator's guarantee applies to that list. A union bound over rounds therefore gives the required joint success even when future batches depend on earlier answers.
2. **Estimate the whole menu.** Before returning the first batch, estimate all $`L`$ menu entries with joint failure probability at most $`1/3`$, using $`\widetilde O(\sqrt L/\epsilon)`$ source calls. Return the stored estimates whenever an index is requested. On the event that the entire menu is accurate, every later answer is accurate, including answers selected adaptively.

Because the sizes are public, the algorithm can choose the cheaper schedule in advance. These are existing batch estimators arranged according to the request protocol; no new batch-estimation algorithm is required.

The query statement should not be read as a gate statement. In particular, Huggins et al. count $`\widetilde O(\sqrt M/\epsilon)`$ controlled exponentials **for each** of the $`M`$ observables, giving $`\widetilde O(M^{3/2}/\epsilon)`$ such operations in total. The block-encoding formulation in Theorem 37 of [van Apeldoorn et al., *Quantum tomography using state-preparation unitaries*](https://arxiv.org/pdf/2207.08800) has a different observable-access and additional-gate ledger. Any end-to-end application must specify which implementation it supplies and charge those costs as well.

## 5. Consequences of the scheduling law

For equal batches, $`b_r=b`$ and $`T=Rb`$, the numerator before menu saturation is

```math
A=R\sqrt b=\sqrt{RT}.
```

For one observable per round, $`T=R`$ and

```math
Q_{\mathrm{online}}
=\widetilde\Theta\!\left(
\frac{\min\{T,\sqrt L\}}{\epsilon}
\right).
```

For a list of $`T`$ observables drawn independently of the algorithm's answers, disclosing the complete list before any answers are due permits the known batch upper bound $`\widetilde O(\sqrt T/\epsilon)`$. Disclosing the same oblivious requests one at a time instead has worst-case online cost $`\Omega(T/\epsilon)`$ when $`L\geq T^2`$, yielding a square-root separation in $`T`$, up to logarithms. Both the menu-size condition and the precision condition are part of this comparison. It does not assert the same separation at fixed nonzero precision as $`T`$ grows, or identify an adaptive interaction with its retrospectively realized list. See the [explicit comparison](upper-bounds.md#compare-deadlines-while-holding-the-request-count-fixed).

The source remains coherent and reversible in both tasks, and memory remains unrestricted. The differing resource is how much of the requested list is available before an answer must be returned. The $`\sqrt L/\epsilon`$ endpoint expresses the alternative of estimating the entire known menu in advance.

## 6. Scope of the theorem

This is a worst-case source-query result. The hard source is one valid completion of a state-preparation map; the theorem does not claim that every unitary preparing the same output state has the same difficulty. The commuting-witness page gives an explicit, much easier completion for the same product-state family.

The menu is known and finite, the batch sizes are predetermined, the outputs are classical numerical estimates, and the accuracy range is stated explicitly. The theorem does not establish a law for an unknown future menu, adaptively chosen batch sizes, approximate inverses, noisy source calls, or larger-error regimes. It does not impose a memory bound, and it does not turn a source-query separation into a total-runtime separation without further implementation assumptions.
