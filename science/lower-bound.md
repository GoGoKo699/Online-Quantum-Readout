# Lower bound for sequentially revealed batches

This page proves the lower bound in [the model and main theorem](model-and-theorem.md). It counts every invocation of the source, including preprocessing and input-dependent stopping, and places no restriction on retained quantum memory. The request sizes $`b_1,\ldots,b_R`$ are fixed in advance. The request subsets used in the proof are independent uniform subsets of those sizes.

Write

```math
A=\sum_{r=1}^{R}\sqrt{b_r},
\qquad
c_* = 1-\frac{2\sqrt2}{3},
\qquad
0<\epsilon\leq\frac{1}{2\sqrt{2L}}.
```

We prove that the expected total number $`Q`$ of source calls, averaged over the hard inputs and requests specified below, satisfies

```math
Q\geq
\frac{c_*}{16\epsilon}
\frac{A}{1+A/\sqrt L}.
```

Since a worst-case expected cost is at least this average cost, this proves the minimax lower bound. A cap on every execution is also at least the average cost.

## 1. A specified hard source

Let the physical source space have orthonormal basis

```math
|\perp\rangle,\ |r\rangle,\ |1\rangle,\ldots,|L\rangle.
```

For $`x\in\{-1,+1\}^L`$, define

```math
s=2\epsilon\sqrt L,
\qquad
c=\sqrt{1-s^2},
\qquad
|v_x\rangle=\frac{1}{\sqrt L}\sum_{i=1}^{L}x_i|i\rangle,
\qquad
|\psi_x\rangle=c|r\rangle+s|v_x\rangle.
```

The precision assumption gives $`0<s\leq 1/\sqrt2`$ and $`c\geq 1/\sqrt2`$. Use the public observables

```math
O_i=|r\rangle\langle i|+|i\rangle\langle r|.
```

Each has norm one and rank two. Its expectation is

```math
\langle\psi_x|O_i|\psi_x\rangle
=\frac{2cs}{\sqrt L}x_i
=4c\epsilon x_i.
```

The magnitude is at least $`2\sqrt2\epsilon`$. Thus taking the sign of an $`\epsilon`$-accurate estimate recovers $`x_i`$. A fixed rule can resolve a zero estimate; an accurate estimate never reaches that tie.

Specify the complete preparation oracle by

```math
U_x
=I-|\perp\rangle\langle\perp|
  -|\psi_x\rangle\langle\psi_x|
  +|\psi_x\rangle\langle\perp|
  +|\perp\rangle\langle\psi_x|.
```

It swaps $`|\perp\rangle`$ and $`|\psi_x\rangle`$, fixes their orthogonal complement, and satisfies $`U_x^\dagger=U_x=U_x^{-1}`$. Both query directions therefore obey the same bounds below. The family, including this completion rule, may be known to the algorithm; the hidden string $`x`$ is not supplied.

The physical source dimension is $`L+2`$. It embeds in $`\lceil\log_2(L+2)\rceil`$ qubits by extending $`U_x`$ as the identity and each $`O_i`$ as zero on unused basis states. The much larger reference register introduced next belongs only to the proof.

## 2. Purifying the hidden input

Choose $`x`$ uniformly and purify it in an inaccessible register $`X`$ with basis $`|x\rangle`$. Let $`F_i`$ flip the hidden sign at coordinate $`i`$ and let $`Z_i`$ multiply by it:

```math
F_i|x\rangle=|x^{(i)}\rangle,
\qquad
Z_i|x\rangle=x_i|x\rangle.
```

Here $`x^{(i)}`$ equals $`x`$ except at coordinate $`i`$. Define

```math
K_i=\frac{I-F_i}{2},
\qquad
K_S=\sum_{i\in S}K_i,
\qquad
K=\sum_{i=1}^{L}K_i.
```

The $`K_i`$ are commuting projectors. In the Fourier basis of $`X`$, $`K`$ counts the number of occupied sign coordinates. The initial uniform reference state

```math
|\chi\rangle=2^{-L/2}\sum_x|x\rangle
```

has $`K|\chi\rangle=0`$.

All algorithm registers, measurement records, and purifications of discarded systems can be retained for the proof. This retention does not give the algorithm access to an environment it actually discarded. Source-independent operations act trivially on $`X`$ and preserve the expectation of any operator acting only on $`X`$. Measurement outcomes and input-dependent classical decisions are included as records; the proof does not condition on a particular observed algorithm transcript.

For a fixed external request history, a normalized purified state at a completed stage has the form

```math
|\Xi\rangle=2^{-L/2}\sum_x|x\rangle|\Phi_x\rangle.
```

The $`|\Phi_x\rangle`$ include all such records. We average over external request randomness separately. The input distribution is never assumed to remain uniform after conditioning on an observed transcript; no such conditioning is used.

## 3. Exact commutator bounds for a source call

Let the following maps be isometries from $`X`$ to $`X`$ tensored with the physical query register:

```math
\mathcal R=I_X\otimes|r\rangle,
\qquad
\mathcal B=I_X\otimes|\perp\rangle,
\qquad
\mathcal V=\frac{1}{\sqrt L}\sum_{i=1}^{L}Z_i\otimes|i\rangle,
\qquad
\mathcal A=c\mathcal R+s\mathcal V.
```

Thus $`\mathcal A|x\rangle=|x\rangle|\psi_x\rangle`$, $`\mathcal A^\dagger\mathcal A=\mathcal B^\dagger\mathcal B=I_X`$, and $`\mathcal A^\dagger\mathcal B=0`$. The input-controlled source is

```math
\mathcal U=\sum_x|x\rangle\langle x|\otimes U_x
=I-\mathcal B\mathcal B^\dagger-\mathcal A\mathcal A^\dagger
  +\mathcal A\mathcal B^\dagger+\mathcal B\mathcal A^\dagger.
```

For a rectangular isometry, the notation $`[G,\mathcal A]`$ means $`(G\otimes I)\mathcal A-\mathcal A G`$. For operators on the joint space, the identity on the physical query register is left implicit.

Fix a subset $`S`$ with $`|S|=b`$. Since $`K_j`$ commutes with $`Z_i`$ for $`j\neq i`$,

```math
[K_S,\mathcal V]
=\frac{1}{\sqrt L}\sum_{i\in S}[K_i,Z_i]\otimes|i\rangle.
```

The physical labels $`|i\rangle`$ are orthogonal, and $`[K_i,Z_i]^\dagger[K_i,Z_i]=I_X`$. Consequently,

```math
[K_S,\mathcal V]^\dagger[K_S,\mathcal V]=\frac{b}{L}I_X,
\qquad
\|[K_S,\mathcal A]\|=s\sqrt{\frac bL}.
```

The maps $`\mathcal R`$ and $`\mathcal B`$ commute with $`K_S`$ in the rectangular sense. The product rule therefore gives

```math
\|[K_S,\mathcal A\mathcal A^\dagger]\|
\leq 2s\sqrt{\frac bL},
```

```math
\|[K_S,\mathcal A\mathcal B^\dagger]\|
\leq s\sqrt{\frac bL},
\qquad
\|[K_S,\mathcal B\mathcal A^\dagger]\|
\leq s\sqrt{\frac bL}.
```

Thus the exact finite-dimensional bound is

```math
\boxed{\|[K_S,\mathcal U]\|\leq4s\sqrt{\frac bL}.}
```

In particular, $`\|[K,\mathcal U]\|\leq4s`$. Define the batch progress operator

```math
\Gamma_S=\frac1b\sum_{i\in S}F_i
=I-\frac{2K_S}{b}.
```

Then

```math
\boxed{\|[\Gamma_S,\mathcal U]\|
\leq\frac{8s}{\sqrt{bL}}.}
```

Tensoring with arbitrary working registers does not change these bounds. A controlled source call has the same bound: if its coherent control projector $`C`$ acts outside $`X`$ and the target register, then $`I-C+C\mathcal U`$ has commutator $`C[G,\mathcal U]`$ with $`G`$. Known routing operations before and after the call commute with operators on $`X`$.

## 4. Expected calls and classical stopping

This step distinguishes a classical decision to invoke an oracle from a quantum control inside an invocation.

First consider an algorithm with a finite cap on its source calls. Synchronize its classical branches at successive query slots or at the current round boundary. A branch that has already reached that boundary is frozen. Source-independent processing can be included between slots. Let $`P`$ be the classical active-invocation flag in one slot. It acts on a separate control record, so it commutes with the source target and every progress operator on $`X`$.

Let $`\mathcal V_0`$ denote the unitary source operation used in that slot, including any coherent source control. Different known routings or controls may be selected on orthogonal classical records. Their commutator bounds have the same maximum as the original source bound. The synchronized operation is

```math
\mathcal W=(I-P)+P\mathcal V_0,
\qquad
[P,G]=[P,\mathcal V_0]=0.
```

For $`G=K`$ or $`G=\Gamma_S`$,

```math
\mathcal W^\dagger G\mathcal W-G
=P(\mathcal V_0^\dagger G\mathcal V_0-G)P.
```

If $`\|[G,\mathcal V_0]\|\leq\gamma`$, the middle Hermitian operator has norm at most $`\gamma`$. Hence, for the current joint state $`\rho`$,

```math
\left|\mathrm{Tr}\rho
(\mathcal W^\dagger G\mathcal W-G)\right|
\leq\gamma\mathrm{Tr}(\rho P).
```

The last factor is the probability that the classical execution actually invokes the source in this slot. Summing those probabilities gives the expected number of physical invocations. A coherent controlled invocation still costs one query on every classical execution that makes that invocation; it is not discounted by the probability of its internal control being active. The displayed bound can be applied with the outer classical flag only, which preserves that charging convention.

The synchronized circuit is a mathematical dilation of the adaptive algorithm. It need not be physically run as a padded circuit. Its activity probabilities record the invocations of the original classical branches, including branches whose stopping decisions depend on information about $`x`$.

Let $`N_{<r}`$ count all source calls before $`S_r`$ is revealed. Starting from $`\langle K\rangle=0`$, the bound above implies

```math
\mathbb E\langle K\rangle_{<r}
\leq 4s\mathbb E N_{<r}
\leq4sQ.
```

Let $`q_r`$ count the calls after $`S_r`$ is revealed and before all its answers are returned. These intervals are disjoint, so

```math
\sum_{r=1}^{R}\mathbb E q_r\leq Q.
```

Calls made before a reveal but outside one of these intervals are still included in $`Q`$ and in the appropriate later $`N_{<r}`$. Keeping them outside the sum can only weaken the lower bound.

## 5. The next subset is independent of the entire prefix

For the hard request process, sample $`S_r`$ uniformly among all subsets of size $`b_r`$, independently of $`x`$, earlier requests, and all algorithm records, only when the protocol reaches its next reveal. Equivalently, all subsets can be sampled initially and kept inaccessible until their prescribed rounds.

For every fixed prefix state,

```math
\mathbb E_{S_r}\Gamma_{S_r}
=\frac1L\sum_{i=1}^{L}F_i
=I-\frac{2K}{L}.
```

Let $`W_{r,\mathrm{in}}`$ be the average expectation of $`\Gamma_{S_r}`$ immediately after its reveal, and $`W_{r,\mathrm{out}}`$ the average expectation when its answers have been returned. Revealing the independent classical subset does not otherwise alter the prefix state. Therefore,

```math
W_{r,\mathrm{in}}
=1-\frac{2}{L}\mathbb E\langle K\rangle_{<r}
\geq1-\frac{8sQ}{L}.
```

Previous records may depend arbitrarily on $`x`$. The independence needed here is solely that the next subset was not available to the algorithm before this reveal. Input-dependent stopping does not invalidate the identity: the subset is fresh at the protocol boundary at which the branch is ready for it.

Within the round, keep an immutable external copy of $`S_r`$ for analysis. Equivalently, condition on its value and then average. Source-independent processing preserves the corresponding progress, and the query bound from the preceding sections gives

```math
|W_{r,\mathrm{out}}-W_{r,\mathrm{in}}|
\leq\frac{8s}{\sqrt{b_rL}}\mathbb E q_r.
```

The fresh subsets may overlap earlier subsets. The proof does not assume distinct requests across rounds or discard the usefulness of earlier answers; all earlier information is already included in the prefix state and its occupation budget.

## 6. Correct outputs bound the remaining edge overlap

Fix a request history through the current round and an index $`i\in S_r`$. Append a source-independent decoder that records the sign of the returned estimate for $`i`$. Let $`e_{x,i}`$ be its error probability on input $`x`$. The two correct signs for $`x`$ and $`x^{(i)}`$ are opposite.

Let $`|\Phi_x\rangle`$ and $`|\Phi_{x^{(i)}}\rangle`$ be the normalized final purified states at this round boundary. Projecting their inner product onto the two possible sign records and applying Cauchy–Schwarz yields

```math
|\langle\Phi_x|\Phi_{x^{(i)}}\rangle|
\leq
\sqrt{(1-e_{x,i})e_{x^{(i)},i}}
+\sqrt{e_{x,i}(1-e_{x^{(i)},i})}.
```

This argument keeps all earlier output records, working memory, and measurement environments. It does not require the retained information to be classical.

Let $`\delta_r`$ be the average of $`e_{x,i}`$ over uniform $`x`$, the independent request history, and a uniform $`i\in S_r`$. The map $`x\mapsto x^{(i)}`$ preserves this averaging distribution. Applying Cauchy–Schwarz again to the two terms gives

```math
\mathbb E_{x,S_1,\ldots,S_r,i}
|\langle\Phi_x|\Phi_{x^{(i)}}\rangle|
\leq2\sqrt{\delta_r(1-\delta_r)}.
```

For the purified input state, the expectation of $`F_i`$ is the average neighboring-input inner product. Since $`\Gamma_{S_r}`$ averages those operators,

```math
W_{r,\mathrm{out}}
\leq2\sqrt{\delta_r(1-\delta_r)}.
```

If $`\delta_r\leq1/3`$, then

```math
W_{r,\mathrm{out}}\leq\frac{2\sqrt2}{3}.
```

The required joint accuracy for the numerical outputs implies this sign-error condition in every round. The proof only needs the per-round average condition. It does not replace it by an average error over all rounds with unequal weights.

## 7. Sum the round costs

Combining the preceding bounds gives, for every round,

```math
c_*
\leq\frac{8sQ}{L}
+\frac{8s}{\sqrt{b_rL}}\mathbb E q_r.
```

Multiply by $`\sqrt{b_rL}/(8s)`$ and sum over $`r`$. Using $`\sum_r\mathbb E q_r\leq Q`$ gives

```math
\frac{c_*\sqrt L}{8s}A
\leq\frac{A}{\sqrt L}Q+Q.
```

Since $`s=2\epsilon\sqrt L`$,

```math
\boxed{
Q\geq\frac{c_*}{16\epsilon}
\frac{A}{1+A/\sqrt L}.
}
```

This summation is valid even when the prefix budget is already large enough that an individual lower bound on $`\mathbb E q_r`$ becomes negative. No separate assumption that every round performs new work is made. The denominator accounts for the possibility of spending enough source calls to learn the entire menu before later requests arrive.

More generally, if every round has average sign error at most $`\delta<1/2`$, the same proof replaces $`c_*`$ by

```math
c(\delta)=1-2\sqrt{\delta(1-\delta)}.
```

## 8. Remove the finite query cap

Now consider an almost-surely terminating algorithm whose total number $`N`$ of paid source invocations has finite expectation $`Q`$ under the hard distribution. If that expectation is infinite, the lower bound is immediate.

For an integer $`n`$, truncate the algorithm just before it would make invocation number $`(n+1)`$. On a truncated execution, supply fixed numerical answers for all remaining requests. This uses no additional source calls. The request subsets are independent and can be coupled identically between the original and truncated algorithms. A truncated execution can differ from the original only on the event $`N>n`$, which has probability at most $`Q/(n+1)`$.

The truncated algorithm has expected query count $`Q_n\leq Q`$ and, in each round, average sign error at most

```math
\delta_n=\frac13+\frac{Q}{n+1}.
```

For sufficiently large $`n`$, $`\delta_n<1/2`$. Apply the finite-cap argument with $`c(\delta_n)`$ to obtain

```math
Q\geq Q_n
\geq\frac{c(\delta_n)}{16\epsilon}
\frac{A}{1+A/\sqrt L}.
```

Letting $`n`$ tend to infinity gives $`c(\delta_n)\to c_*`$. This proves the advertised lower bound for actual expected invocations, including classical, input-dependent stopping. The truncation argument uses average correctness under the hard distribution, so it does not require a uniform tail bound for every individual hidden input.

## 9. What the construction establishes

The hard requests are an oblivious randomized subclass of the legal online request policies. The lower bound therefore applies to algorithms that promise correctness for adaptive request policies as well. For a fixed algorithm, its average hard-distribution cost is bounded above by its worst-case expected cost, giving the minimax conclusion.

The canonical source completion is an explicit part of the hard instance. The result does not assert that every source unitary preparing $`|\psi_x\rangle`$ is hard. It also does not assert a memory limitation: arbitrary retained quantum and classical information is included throughout. The separate [commuting product-state construction](commuting-witness.md) shows that the same asymptotic bound can hold with a commuting, one-local observable menu under its specified canonical source completion.
