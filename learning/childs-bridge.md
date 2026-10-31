# From Childs's quantum algorithms to online quantum readout

A coherent simulation may prepare the same unknown state many times. A classical user wants numerical expectations of known observables, but supplies the requests in batches: the current answers are due before the next batch is revealed. The source remains available, and the algorithm may keep all earlier quantum and classical information. The question is how this disclosure schedule affects the number of source calls.

The selected educational anchor is Andrew M. Childs, *Lecture Notes on Quantum Algorithms*, **17 April 2025 edition**: [author's page](https://www.cs.umd.edu/~amchilds/qa/) and [author's PDF](https://www.cs.umd.edu/~amchilds/qa/qa.pdf). This bridge connects a small set of its sections to the project. The [30-milestone map](milestones.md) organizes the common understanding targets; the [scientific account](../science/README.md) contains the authoritative theorem and complete proofs.

## The selected reading route

Page numbers below are printed page numbers. The linked PDF has 191 pages, and its viewer page number is the printed number plus eight. The page links use that viewer numbering.

| Childs section | Printed pages | Connection to this project |
|---|---:|---|
| §§1.1–1.3, *Quantum data*, *Quantum circuits*, *Universal gate sets* | [1–2](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=9) | State vectors, reversible operations, and the operator norm |
| §4.3, *Phase estimation* | [19](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=27) | Extracting a numerical parameter from controlled evolution |
| §19.3, *Amplitude amplification and quantum counting* | [88–89](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=96) | Turning a probability into a coherently estimated quantity |
| §§21.1–21.2, *Quantum query complexity*, *Quantum queries* | [97–98](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=105) | Separating oracle invocations from other computation |
| §23.1, *Quantum adversaries* | [109](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=117) | An inaccessible input register and output distinguishability |
| §23.2, *The adversary method* | [110–113](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=118) | Bounding the change of a progress quantity per query |
| §26.1, *The compressed oracle* | [125–126](https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=133) | A useful comparison for recording information in an oracle register |

The query-model sections connect first to the source interface below. The phase-estimation and counting sections then motivate the single-value construction. The adversary sections support the lower-bound route. Section 26.1 is a comparison that helps interpret the hidden register; its compressed-oracle theorem is not an imported ingredient of this project's proof. No whole-book prerequisite is needed.

## From Childs's query model to a preparation source

A pure state $`|\psi\rangle`$ is a unit vector. Its coordinates are amplitudes; a measurement in an orthonormal basis returns a basis label with probability equal to the squared magnitude of its amplitude. A unitary $`U`$ preserves inner products and has inverse $`U^\dagger`$. A Hermitian observable $`O`$ has real eigenvalues: measuring it returns an eigenvalue, with probabilities determined by the state's projections onto the corresponding eigenspaces. Its mean is $`\langle\psi|O|\psi\rangle`$.

The operator norm $`\|B\|`$ is the largest value of $`\|B|v\rangle\|`$ over unit vectors $`|v\rangle`$. Thus $`\|O\|\leq1`$ places every possible measurement outcome in $`[-1,1]`$. A small inner product means two pure states can be distinguished well; Section 23.1, Fact 23.1, gives the precise binary relation used in the adversary argument.

Several symbols change roles between the notes and this project.

| In the selected sections | In this project |
|---|---|
| $`O_x`$ is an oracle encoding an unknown input string | $`U`$, or $`U_x`$ in a hard family, is the unknown preparation oracle; $`O_i`$ is a known observable |
| $`U_1,\ldots,U_t`$ are input-independent operations between queries | Known computation may include memory, measurement, feedback, and observable implementation |
| A standard query addresses a coordinate of a bit string | One source call applies the supplied full unitary to any chosen quantum input |
| $`\epsilon`$ in $`Q_\epsilon(f)`$ is a failure probability | $`\epsilon`$ is additive numerical error; $`\delta`$ denotes failure probability |
| Bit-valued inputs use $`0,1`$ | The hard family uses signs $`x_i\in\{-1,+1\}`$; a bit $`y_i`$ corresponds to $`x_i=(-1)^{y_i}`$ |
| The adversary's input register is inaccessible to the algorithm | The register $`X`$ below is also a proof device, separate from physical source qubits |

The preparation promise is

```math
U|\perp\rangle=|\psi\rangle.
```

Here $`|\perp\rangle`$ is a known reference state. The model supplies $`U`$, $`U^\dagger`$, and their controlled versions; each actual invocation costs one source query. It supplies neither the hidden state's amplitudes nor the oracle's classical circuit description. Preprocessing calls count. The algorithm can query the full unitary on inputs other than $`|\perp\rangle`$.

That last permission makes the **completion of the preparation map** essential. Two unitaries can agree on $`|\perp\rangle`$ and reveal very different information on other inputs or after repeated applications. A lower bound must specify a hard full unitary. The worked example does so explicitly, and the [commuting witness](../science/commuting-witness.md#5-why-the-oracle-completion-must-be-specified) exhibits an easier completion of the same product-state preparation map.

The distinction between source queries and ordinary operations follows the query-complexity viewpoint. It does not make ordinary operations costless in a complete implementation. In particular, a controlled source invocation costs one whole call even when its internal quantum control has a small active amplitude. A classical branch that makes no invocation costs zero calls. The [model](../science/model-and-theorem.md#1-source-access-and-the-public-menu) and [resource ledger](../science/resources-and-interpretation.md#1-a-ledger-for-a-complete-implementation) state the complete conventions.

## From estimation to an online contract

### A local bridge from an observable to a probability

For a known norm-bounded Hermitian $`O_j`$, define

```math
E_j=\frac{I+O_j}{2},
\qquad
\mu_j=\langle\psi|O_j|\psi\rangle.
```

Every eigenvalue of $`E_j`$ lies between zero and one. A known unitary $`W_j`$ can coherently attach a flag whose probability of being one is the expectation of $`E_j`$. On an eigenvector $`|e\rangle`$ of $`E_j`$ with eigenvalue $`e`$, it acts as

```math
W_j|0\rangle|e\rangle
=\sqrt{1-e}\,|0\rangle|e\rangle
 +\sqrt e\,|1\rangle|e\rangle.
```

For example, the second column of the flag rotation can be chosen as $`-\sqrt e\,|0\rangle+\sqrt{1-e}\,|1\rangle`$, making each two-dimensional block unitary. Diagonalizing the known observable and applying these rotations therefore specifies a construction. Its gate cost may be large; this argument does not assume an efficient or free implementation for an arbitrary description.

Let $`B_j=W_j(I\otimes U)`$. Applying it to $`|0\rangle|\perp\rangle`$ gives a flag-one probability

```math
p_j=\langle\psi|E_j|\psi\rangle
=\frac{1+\mu_j}{2}.
```

Consequently, estimating $`p_j`$ to error $`\epsilon/2`$ estimates $`\mu_j=2p_j-1`$ to error $`\epsilon`$. One use of $`B_j`$ uses one source call and the known operation $`W_j`$; its inverse uses one inverse source call and $`W_j^\dagger`$.

This is where the phase-estimation and counting ideas connect. Write $`p_j=\sin^2\theta_j`$, let $`|\Psi_j\rangle=B_j|0,\perp\rangle`$, and let $`\Pi_1`$ project onto flag one. The product of reflections

```math
G_j=(2|\Psi_j\rangle\langle\Psi_j|-I)(I-2\Pi_1)
```

has eigenphases $`\pm2\theta_j`$ in the subspace spanned by the flag-zero and flag-one components of $`|\Psi_j\rangle`$. Their endpoint cases are understood by continuity. For either phase $`\varphi`$,

```math
p_j=\frac{1-\cos\varphi}{2}.
```

Phase estimation to order $`\epsilon`$ accuracy therefore suffices for additive estimation of the mean. A reflection about the prepared state uses $`B_j`$ and $`B_j^\dagger`$, so each such iterate uses two source calls. A power of that iterate costs the corresponding repeated calls; a high power is not a single source query. The resulting single-value source cost is $`O(1/\epsilon)`$ at constant success probability, with confidence amplification adding logarithmic overhead. These equations supply the local expectation-to-probability translation; they do not supply a multi-observable estimator.

### What changes when answers have deadlines

The public menu contains $`L`$ observables. There are $`R`$ rounds with predetermined sizes $`b_1,\ldots,b_R`$, each between one and $`L`$. In round $`r`$, the revealed subset $`S_r`$ has $`b_r`$ distinct indices. Its answers must be returned before $`S_{r+1}`$ is disclosed. Repeated indices in different rounds are allowed. Define

```math
T=\sum_{r=1}^{R}b_r,
\qquad
A=\sum_{r=1}^{R}\sqrt{b_r}.
```

Here $`T`$ counts requested outputs; $`A`$ summarizes the disclosure schedule. Correctness requires **all** numerical answers to be within $`\epsilon`$ simultaneously with probability at least $`2/3`$. The algorithm must complete the protocol almost surely.

Estimating every value separately would give a source upper bound of order $`T/\epsilon`$, apart from confidence factors. The stronger fixed-list estimator of Huggins et al. is a research-level ingredient: a supplied list of $`m`$ observables costs $`\widetilde O(\sqrt m/\epsilon)`$ source calls. Applying it to each newly revealed batch gives $`\widetilde O(A/\epsilon)`$. Applying it once to the entire known menu gives $`\widetilde O(\sqrt L/\epsilon)`$ and a stored table for all later requests.

For adaptive requests, each new batch run is assigned failure probability $`1/(3R)`$ conditional on the previous history. A union bound supplies joint success. Full-menu estimation instead uses one event on which all menu values are accurate, which also covers any later adaptive selection. These are the two schedules in the [upper-bound proof](../science/upper-bounds.md).

The project's matching lower bound establishes the worst-case frontier

```math
Q_{\mathrm{online}}
=\widetilde\Theta\!\left(
\frac{\min\{A,\sqrt L\}}{\epsilon}
\right),
\qquad
0\lt\epsilon\leq\frac{1}{2\sqrt{2L}}.
```

This statement holds for both worst-case expected source cost and a cap on every execution, up to logarithmic factors. The [exact theorem](../science/model-and-theorem.md#3-main-theorem) supplies the constants and quantifiers. The logarithms and unspecified constants mean that these scale expressions are not predictions of exact finite query counts.

## A worked four-observable example

Take $`L=4`$ and $`\epsilon=1/8`$, which satisfy the precision condition. Use orthonormal basis states $`|\perp\rangle,|r\rangle,|1\rangle,\ldots,|4\rangle`$ and a hidden sign string $`x\in\{-1,+1\}^4`$. Define

```math
|\psi_x\rangle
=\frac{\sqrt3}{2}|r\rangle
 +\frac14\sum_{j=1}^{4}x_j|j\rangle.
```

The state is normalized because $`3/4+4(1/16)=1`$. This is the main proof's star family with $`s=1/2`$ and $`c=\sqrt3/2`$. The six-dimensional source can be embedded in three qubits.

Specify the full source by exchanging $`|\perp\rangle`$ and $`|\psi_x\rangle`$ and fixing every vector orthogonal to both. This defines a unitary on the entire source space, with $`U_x^\dagger=U_x`$. In a three-qubit embedding it also fixes the two unused basis states. The hidden string is unknown, even though the definition of this family is public.

The known menu is

```math
O_j=|r\rangle\langle j|+|j\rangle\langle r|,
\qquad j=1,2,3,4.
```

Each observable exchanges the two indicated basis states and is zero on their orthogonal complement. Its eigenvectors with nonzero eigenvalues are

```math
|+_j\rangle=\frac{|r\rangle+|j\rangle}{\sqrt2},
\qquad
|-_j\rangle=\frac{|r\rangle-|j\rangle}{\sqrt2},
```

with eigenvalues $`+1`$ and $`-1`$, respectively. Hence measuring $`O_j`$ after one preparation gives

```math
\begin{aligned}
\Pr(+1)&=\frac{13}{32}+\frac{\sqrt3}{8}x_j,\\
\Pr(-1)&=\frac{13}{32}-\frac{\sqrt3}{8}x_j,\\
\Pr(0)&=\frac{3}{16}.
\end{aligned}
```

The probabilities sum to one. Subtracting the second from the first gives the mean

```math
\mu_j=\frac{\sqrt3}{4}x_j.
```

For instance, if the hidden string happens to be $`(+1,-1,+1,-1)`$, the four means are $`(\sqrt3/4,-\sqrt3/4,\sqrt3/4,-\sqrt3/4)`$. The algorithm receives no such string. It must return estimates from its source access.

An $`\epsilon=1/8`$ estimate determines the requested sign, since

```math
\frac{\sqrt3}{4}-\frac18\gt0.
```

Thus even the lower endpoint of the accurate interval for a positive mean is positive, and the entire accurate interval for a negative mean is negative. This is the reduction from numerical readout to sign recovery used in the lower bound.

The coherent flag construction is explicit here. In the eigenbasis of $`O_j`$, put flag one on the $`+1`$ eigenvector, flag zero on the $`-1`$ eigenvector, and an equal superposition of the flag values on the zero-eigenvalue subspace. Measuring the flag would give

```math
p_j=\Pr(+1)+\frac12\Pr(0)
=\frac12+\frac{\sqrt3}{8}x_j.
```

Keeping this flag coherent allows the preceding phase-estimation construction; measuring it gives one Bernoulli sample. A single sample is not an accurate mean estimate. The known basis changes and flag rotations contain no hidden signs, and their implementation is a separate cost from calls to $`U_x`$.

This example exhibits the state, complete source, measurements, numerical outputs, and sign decoder. Its small size does not establish an asymptotic schedule separation. That conclusion comes from the general family and the next argument, which also permits retained quantum memory.

## From the adversary method to the batch frontier

### Retaining records without granting access to the hidden input

For the proof, represent a uniformly random hidden string by an inaccessible register $`X`$. The source then acts through the input-controlled unitary

```math
\mathcal U=\sum_x|x\rangle\langle x|\otimes U_x.
```

This is the source analogue of the super-oracle in Childs §23.1. The algorithm still acts only on its own registers. The $`2^L`$-dimensional hidden register is a mathematical representation of the input distribution, not an additional physical resource supplied to the algorithm.

Measurements and discarded systems can also be retained in a purification. Explicitly, measurement operators $`M_z`$ satisfying $`\sum_zM_z^\dagger M_z=I`$ define the isometry

```math
|\phi\rangle\longmapsto
\sum_z|z\rangle M_z|\phi\rangle.
```

Tracing out the record gives the measurement with its outcome forgotten. Copying the basis label $`z`$ to a second environment also models a retained classical outcome and feedback controlled by it. This local dilation explains why the proof can retain a pure joint state while covering measured algorithms. It does not let an actual algorithm recover an environment it discarded.

### What the progress quantity records

Let $`F_i`$ flip hidden sign $`i`$ in $`X`$, and define

```math
K_i=\frac{I-F_i}{2},
\qquad
K=\sum_{i=1}^{L}K_i,
\qquad
\Gamma_S=\frac1b\sum_{i\in S}F_i
=I-\frac{2}{b}\sum_{i\in S}K_i
\quad (|S|=b).
```

The $`K_i`$ are commuting projectors. In the Fourier basis of the sign register, they indicate which coordinates are occupied; $`K`$ counts those occupied coordinates. Initially the uniform superposition has occupation zero. Occupation is a progress observable, not a count of exactly decoded classical bits or a bound on physical memory.

For a progress operator $`G`$, one unitary call changes its expectation by at most

```math
\bigl|\langle G\rangle_{\mathrm{after}}
      -\langle G\rangle_{\mathrm{before}}\bigr|
\leq\|\mathcal U^\dagger G\mathcal U-G\|
=\|[G,\mathcal U]\|.
```

The commutator $`[G,\mathcal U]=G\mathcal U-\mathcal U G`$ measures how much the source can change this observable. Source-independent operations commute with operators on $`X`$ and leave their expectations unchanged.

For the canonical star source, [the explicit calculation](../science/lower-bound.md#3-exact-commutator-bounds-for-a-source-call) gives

```math
\|[K,\mathcal U]\|\leq4s,
\qquad
\|[\Gamma_S,\mathcal U]\|
\leq\frac{8s}{\sqrt{bL}},
\qquad
s=2\epsilon\sqrt L.
```

These are bounds for this full unitary, including inverse and controlled calls. Standard addressed-query bounds from the textbook cannot simply be substituted for them. Likewise, the recording interpretation in §26.1 helps explain the choice of representation, but it does not identify one preparation call with one random-function query.

### The missing online step: a fresh subset tests the whole prefix

The lower bound chooses each new subset independently and uniformly among subsets of its announced size. Each index lies in such a subset with probability $`b/L`$, so

```math
\mathbb E_S\Gamma_S
=\frac1b\sum_{i=1}^{L}\Pr(i\in S)F_i
=\frac1L\sum_{i=1}^{L}F_i
=I-\frac{2K}{L}.
```

For the four-observable example and a singleton request, this is simply $`(\Gamma_{\{1\}}+\Gamma_{\{2\}}+\Gamma_{\{3\}}+\Gamma_{\{4\}})/4=I-K/2`$. It holds on any prefix state.

This identity connects future objectives to earlier work. All memory and past answers remain in the prefix. Their ability to help with a newly random subset is controlled by total occupation, which earlier source calls could increase only at a bounded rate. Nothing is reset, and the input is not assumed uniform after conditioning on a particular observed transcript. The proof works with the full purified records and the independent next request.

Finally, correctly decoded signs force the states for neighboring strings $`x`$ and $`x^{(i)}`$ to have limited overlap. Childs's binary distinguishability fact explains the mechanism. The project additionally averages over requested bits and histories: the output-record calculation in [Section 6 of the proof](../science/lower-bound.md#6-correct-outputs-bound-the-remaining-edge-overlap) gives

```math
W_{r,\mathrm{out}}\leq2\sqrt{\delta_r(1-\delta_r)}
\leq\frac{2\sqrt2}{3}
\qquad(\delta_r\leq1/3).
```

Here $`W_{r,\mathrm{out}}`$ is the final average expectation of the batch progress, and $`\delta_r`$ is that round's average sign error. Joint numerical correctness implies this weaker error condition.

Let $`Q`$ be expected total source calls, including preprocessing, and $`q_r`$ the calls made after the current reveal and before its answers. The resulting round inequality is

```math
c_*
\leq\frac{16\epsilon Q}{\sqrt L}
 +\frac{16\epsilon}{\sqrt{b_r}}\,\mathbb E q_r,
\qquad
c_*=1-\frac{2\sqrt2}{3}.
```

The first term accounts for information accumulated anywhere in the prefix; the second accounts for work after the current request becomes known. Weighting by $`\sqrt{b_r}`$ and summing produces the [harmonic lower bound](../science/lower-bound.md#7-sum-the-round-costs), with numerator $`A`$ and denominator $`1+A/\sqrt L`$. It permits some rounds to need no new calls after sufficient global preprocessing.

Two technical steps remain in the canonical proof. [Classical activity flags](../science/lower-bound.md#4-expected-calls-and-classical-stopping) charge the expected number of actual invocations while preserving the full cost of a quantum-controlled invocation. [Truncation](../science/lower-bound.md#8-remove-the-finite-query-cap) extends the capped argument to almost-sure termination with finite expected cost. These steps are necessary for the stated algorithm class; the elementary fixed-length adversary picture alone does not cover it.

## Research dependencies and what remains to be read

The source route separates three roles.

| Role | Source and boundary |
|---|---|
| Educational foundations | Childs supplies the selected query, estimation, and adversary framework. The relevant sections are listed above. |
| Explanatory derivations and project proof | This bridge supplies the expectation-to-probability conversion, the complete small example, and the record-dilation explanation. The [lower bound](../science/lower-bound.md) supplies the exact oracle calculation, fresh-subset argument, and expected-cost proof. |
| Imported algorithmic ingredients | [Huggins et al., Theorem 1](https://storage.googleapis.com/gweb-research2023-media/pubtools/6446.pdf), supplies simultaneous estimation. [Van Apeldoorn et al., Theorem 37](https://arxiv.org/pdf/2207.08800v1), supplies an alternative with different observable-access and gate costs. These are primary research dependencies, not additional educational anchors. |

The single-value construction above does not explain the $`\sqrt m`$ simultaneous-estimation advantage. That ingredient must be read in its cited research source or through the [upper-bound account](../science/upper-bounds.md#the-imported-simultaneous-estimator). In Huggins's theorem, the $`\widetilde O(\sqrt m/\epsilon)`$ controlled-exponential count is **per observable**, giving $`\widetilde O(m^{3/2}/\epsilon)`$ such primitives overall. Van Apeldoorn's formulation separately charges SELECT and additional gates; coherent lookup is not free. The [resource ledger](../science/resources-and-interpretation.md) gives the precise alternatives, including their dimension dependence.

The interpretation also depends on the hard source. The star witness uses $`O(\log L)`$ source qubits and generally noncommuting observables. The alternative [commuting witness](../science/commuting-witness.md) uses $`L`$ data qubits and one flag; its output is a product state, and the menu consists of one-qubit Pauli observables. Its specified canonical swap is still a full oracle without a locality promise. A tensor product of small sign-dependent rotations can prepare the same output family while allowing all signs to be learned in $`\widetilde O(1/\epsilon)`$ calls. Thus the theorem concerns the worst case over permitted full sources, not every circuit preparing those states.

The precision restriction is also substantive: $`L\epsilon^2`$ must remain bounded in these constructions. The offline comparison holds for an oblivious actual request list supplied in advance; retrospectively exposing an adaptive interaction's eventual list would change the task. Revelation rounds describe when objectives become available, rather than parallel quantum circuit depth. The [scope statement](../science/model-and-theorem.md#6-scope-of-the-theorem) and [related-work comparison](../references/related-work.md) retain these boundaries.

The [milestone map](milestones.md) connects the background targets M01–M12 to the narrative targets M13–M30. For a direct specialist route, the [exact theorem](../science/model-and-theorem.md), [proof](../science/lower-bound.md), [commuting construction](../science/commuting-witness.md), and [verification instructions](../verification/README.md) remain the canonical destinations.
