# Online Quantum Readout

**How does the arrival order of observable requests change the cost of reading a quantum state?** This project gives a matching worst-case source-query law when each revealed batch must be answered before the next batch is known.

The full menu of $`L`$ bounded Hermitian observables is public. An unknown pure state remains available through its preparation unitary, its inverse, and controlled invocations. The algorithm can retain unlimited quantum and classical memory. The restriction is the timing of the requested observables.

For predetermined batch sizes $`b_1,\ldots,b_R`$, define $`A=\sum_{r=1}^{R}\sqrt{b_r}`$. In the high-precision regime, the optimal source-query scaling is

```math
Q_{\mathrm{online}}
=\widetilde\Theta\!\left(
\frac{\min\{A,\sqrt L\}}{\epsilon}
\right),
\qquad
0\lt \epsilon\le\frac{1}{2\sqrt{2L}}.
```

All requested expectations must be accurate to additive error $`\epsilon`$, jointly with probability at least $`2/3`$. The bound counts preprocessing and every later source invocation. It applies to worst-case expected cost and to a cap on every execution; logarithmic confidence and estimation factors are suppressed.

| Request schedule | Worst-case source-query scale, up to logarithms |
|---|---:|
| Predetermined unequal batches | $`\min\{\sum_r\sqrt{b_r},\sqrt L\}/\epsilon`$ |
| Equal batches of size $`b`$, with $`T=Rb`$ total answers | $`\min\{\sqrt{RT},\sqrt L\}/\epsilon`$ |
| One observable at a time | $`\min\{T,\sqrt L\}/\epsilon`$ |

An established simultaneous estimator supplies the two upper strategies: estimate each current batch or estimate the whole known menu once. The new lower bound tracks the information accumulated in arbitrary retained memory and the progress needed after a fresh batch is revealed. It shows why one cannot generally keep the fixed-list source advantage across a succession of answer deadlines.

For an oblivious list of $`T`$ requests with $`L\ge T^2`$, disclosure in advance permits $`\widetilde O(\sqrt T/\epsilon)`$ source calls, whereas sequential disclosure can require $`\Omega(T/\epsilon)`$. The precision condition remains essential; this is not a fixed-precision asymptotic separation. The [upper-bound account](science/upper-bounds.md) gives a compatible parameter example.

## Read the science

Start with the [scientific reading route](science/README.md) and the [exact model and theorem](science/model-and-theorem.md).

| Question | Authoritative account |
|---|---|
| What access, deadlines, success guarantee and costs are assumed? | [Model and theorem](science/model-and-theorem.md) |
| How are adaptive requests handled by the upper strategies? | [Upper bounds and batching](science/upper-bounds.md) |
| Why does the lower bound survive unlimited memory and adaptive stopping? | [Complete lower-bound proof](science/lower-bound.md) |
| Can the observables commute and the prepared state be a product? | [Commuting witness and source completion](science/commuting-witness.md) |
| How do source calls differ from total circuit cost? | [Resources and interpretation](science/resources-and-interpretation.md) |
| Which ingredients are inherited, and which nearby models differ? | [Related work](references/related-work.md) and [bibliography](references/bibliography.bib) |
| Which finite calculations can be reproduced? | [Verification](verification/README.md) |

The [LLM reading guide](llms.txt) maps scientific questions to these authoritative files.

## Two explicit witnesses

The main construction uses a source space of dimension $`L+2`$ and rank-two observables. An alternative uses $`L+1`$ physical qubits, product output states and commuting one-qubit Pauli observables. Thus noncommutation and entanglement in the prepared state are not necessary for the obstruction.

Both lower bounds specify the **full preparation unitary**, including its action away from the designated input. They are minimax statements over valid source implementations. A different, natural rotation implementation of the same product states permits all hidden signs to be read much more cheaply. The [explicit comparison](science/commuting-witness.md#5-why-the-oracle-completion-must-be-specified) is part of the scientific scope.

## Reproduce the finite checks

From the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_bounds.py --check verification/results.json
```

The deterministic suite constructs physical source matrices independently, changes to the Fourier representation, and checks the oracle identities, commutator bounds, sign margins, fresh-subset averaging and active-query accounting. The committed run contains 18 joint source oracles and 72 subset cases, with 3,083 scalar assertions. Its largest operator-identity residual is below $`9\times10^{-16}`$, with no bound violation. General query lower bounds and adaptive-stopping semantics are established by the written proof, not by finite enumeration.

## Resource scope and attribution

The simultaneous estimator is due to [Huggins et al., PRL 129, 240501 (2022)](https://storage.googleapis.com/gweb-research2023-media/pubtools/6446.pdf). For $`M`$ observables, it uses $`\widetilde O(\sqrt M/\epsilon)`$ source calls and the same number of controlled exponentials **per observable**, hence $`\widetilde O(M^{3/2}/\epsilon)`$ such known operations in total. Alternative block-encoding estimators have their own SELECT, dimension and gate costs. The [resource ledger](science/resources-and-interpretation.md) keeps those charges explicit.

This is a source-query frontier for a known finite menu, predetermined batch sizes, ideal unitary access and the stated precision range. Special menus or repeated requests can be easier. No QRAM, efficient source decomposition, optimal memory size, or end-to-end runtime separation is implied.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

