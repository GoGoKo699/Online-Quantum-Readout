# A commuting, one-local observable witness

The [main lower bound](lower-bound.md) uses rank-two observables that need not commute. The same asymptotic online frontier also has a witness whose prepared states are product states and whose requested observables are commuting single-qubit Pauli operators. This removes measurement incompatibility as a necessary feature of the hard instance. The full state-preparation unitary remains an essential part of its specification.

Throughout, let

```math
0\lt \epsilon\leq\frac{1}{2\sqrt{2L}},
\qquad
A=\sum_{r=1}^{R}\sqrt{b_r},
\qquad
c_*=1-\frac{2\sqrt2}{3}.
```

The batch sizes $`b_r`$ are predetermined, and the proof uses independent uniform subsets of those sizes, exactly as in the main lower bound.

## 1. Product states, physical qubits, and the oracle completion

Set

```math
a=2\epsilon,
\qquad
p=a^2,
\qquad
c_0=\sqrt{1-a^2}.
```

For $`x\in\{-1,+1\}^L`$, define the state on $`L`$ data qubits

```math
|\phi_x\rangle
=\bigotimes_{j=1}^{L}
\left(c_0|0\rangle+a x_j|1\rangle\right).
```

Use one additional physical flag qubit $`f`$ and define

```math
|\perp\rangle=|1\rangle_f|0\rangle^{\otimes L},
\qquad
|\psi_x\rangle=|0\rangle_f|\phi_x\rangle.
```

The flag makes the known source input orthogonal to every target state. The source register therefore contains **$`L+1`$ physical qubits**. This is different from the $`\lceil\log_2(L+2)\rceil`$-qubit rank-two witness. The inaccessible hidden-input reference used in the proof is not counted as part of either physical source.

Let $`X_j`$ denote Pauli $`X`$ on data qubit $`j`$, and supply the public menu

```math
O_j=I_f\otimes X_j.
```

Identities on the other data qubits are implicit. These observables have norm one, are pairwise commuting, and each acts nontrivially on only one physical qubit. Their expectations are

```math
\langle\psi_x|O_j|\psi_x\rangle
=2c_0a x_j
=4c_0\epsilon x_j.
```

Because $`p\leq1/(2L)\leq1/2`$, we have $`c_0\geq1/\sqrt2`$. The expectation magnitude is at least $`2\sqrt2\epsilon`$, so an $`\epsilon`$-accurate estimate determines $`x_j`$.

The hard source is the complete unitary

```math
U_x
=I-|\perp\rangle\langle\perp|
  -|\psi_x\rangle\langle\psi_x|
  +|\psi_x\rangle\langle\perp|
  +|\perp\rangle\langle\psi_x|.
```

It swaps the known input with the product target state and acts as the identity on their orthogonal complement. It is Hermitian and unitary, so $`U_x^\dagger=U_x`$. No geometrical locality or efficient gate decomposition of this source unitary is promised. Locality of the observable menu and product structure of its prepared output do not imply locality of the entire preparation oracle.

## 2. Exact Fourier-occupation calculation

Use the hidden-input operators from the main proof:

```math
F_i|x\rangle=|x^{(i)}\rangle,
\qquad
Z_i|x\rangle=x_i|x\rangle,
\qquad
K_i=\frac{I-F_i}{2},
\qquad
K_S=\sum_{i\in S}K_i.
```

For a bit string $`z\in\{0,1\}^L`$, let $`|z|`$ be its Hamming weight and write

```math
\alpha_z=c_0^{L-|z|}a^{|z|},
\qquad
Z^z=\prod_{j=1}^{L}Z_j^{z_j}.
```

The controlled preparation isometry and the fixed-input isometry are

```math
\mathcal A=\sum_{z\in\{0,1\}^L}
\alpha_z Z^z\otimes|0\rangle_f|z\rangle,
\qquad
\mathcal B=I_X\otimes|\perp\rangle.
```

They satisfy $`\mathcal A^\dagger\mathcal A=\mathcal B^\dagger\mathcal B=I_X`$ and $`\mathcal A^\dagger\mathcal B=0`$. The squared amplitudes $`\alpha_z^2`$ are the probabilities of independent Bernoulli($`p`$) bits $`z_1,\ldots,z_L`$.

In the Fourier basis $`|w\rangle_F`$ of the hidden-input register,

```math
K_i|w\rangle_F=w_i|w\rangle_F,
\qquad
Z^z|w\rangle_F=|w\mathbin{\oplus}z\rangle_F.
```

For a subset $`S`$ of size $`b`$,

```math
[K_S,Z^z]|w\rangle_F
=\left(\sum_{j\in S}z_j(1-2w_j)\right)
|w\mathbin{\oplus}z\rangle_F.
```

Here and below a commutator with an isometry means the output operator times the isometry minus the isometry times the input operator. The physical output labels $`|z\rangle`$ are orthogonal. Hence $`[K_S,\mathcal A]^\dagger[K_S,\mathcal A]`$ is diagonal in $`w`$, with eigenvalue

```math
\mathbb E_z\left[
\left(\sum_{j\in S}z_j(1-2w_j)\right)^2
\right]
=bp(1-p)+p^2\left(b-2\sum_{j\in S}w_j\right)^2.
```

The maximum occurs when all $`w_j`$ in $`S`$ agree. Therefore the exact norm identity is

```math
\boxed{
\|[K_S,\mathcal A]\|^2
=bp(1-p)+b^2p^2
=a^2b\bigl(1+(b-1)p\bigr).
}
```

This is an operator identity calculation, with no perturbative expansion in $`a`$ or assumption about the algorithm's retained state.

## 3. Source-query rates

The hidden-input-controlled source again has the form

```math
\mathcal U
=I-\mathcal B\mathcal B^\dagger-\mathcal A\mathcal A^\dagger
  +\mathcal A\mathcal B^\dagger+\mathcal B\mathcal A^\dagger.
```

Since $`[K_S,\mathcal B]=0`$, the same product-rule argument as in the main proof gives

```math
\|[K_S,\mathcal U]\|
\leq4a\sqrt b\sqrt{1+(b-1)p}.
```

Define

```math
\kappa=\sqrt{1+(L-1)p}.
```

The precision assumption implies $`Lp=4L\epsilon^2\leq1/2`$, so

```math
1\leq\kappa\leq\sqrt{\frac32}.
```

For the full occupation $`K=\sum_iK_i`$ and the batch progress $`\Gamma_S=I-2K_S/b`$, the uniform bounds are

```math
\|[K,\mathcal U]\|\leq4a\sqrt L\kappa,
\qquad
\|[\Gamma_S,\mathcal U]\|
\leq\frac{8a\kappa}{\sqrt b}.
```

They also hold for inverse queries and controlled queries. The active-invocation calculation in [Section 4 of the main proof](lower-bound.md#4-expected-calls-and-classical-stopping) applies without change.

## 4. Resulting online lower bound

Let $`Q`$ be the expected total number of source calls under uniform hidden inputs and independent uniform request subsets. Let $`q_r`$ count the invocations made after the reveal in round $`r`$ and before its answers are returned. The global occupation budget now gives

```math
\mathbb E\langle K\rangle_{\lt r}
\leq4a\sqrt L\kappa Q.
```

Freshness of the next subset still gives $`\mathbb E_{S_r}\Gamma_{S_r}=I-2K/L`$. Thus

```math
W_{r,\mathrm{in}}
\geq1-\frac{8a\kappa Q}{\sqrt L}.
```

Correct sign outputs give $`W_{r,\mathrm{out}}\leq2\sqrt2/3`$ by the same neighboring-input overlap argument. Within the round,

```math
|W_{r,\mathrm{out}}-W_{r,\mathrm{in}}|
\leq\frac{8a\kappa}{\sqrt{b_r}}\mathbb E q_r.
```

Consequently,

```math
c_*
\leq\frac{8a\kappa Q}{\sqrt L}
+\frac{8a\kappa}{\sqrt{b_r}}\mathbb E q_r.
```

Multiply by $`\sqrt{b_r}/(8a\kappa)`$, sum over rounds, and use $`\sum_r\mathbb E q_r\leq Q`$. With $`a=2\epsilon`$, this yields

```math
\boxed{
Q\geq\frac{c_*}{16\epsilon\kappa}
\frac{A}{1+A/\sqrt L}.
}
```

Since $`\kappa\leq\sqrt{3/2}`$, this is

```math
Q=\Omega\!\left(
\frac{\min\{\sum_r\sqrt{b_r},\sqrt L\}}{\epsilon}
\right).
```

The argument includes arbitrary retained memory and classical, input-dependent stopping. Finite-expected-cost algorithms are covered by the same truncation and error-limit argument as in [Section 8 of the main proof](lower-bound.md#8-remove-the-finite-query-cap).

## 5. Why the oracle completion must be specified

There is a much easier preparation completion for the same product states. This demonstrates why the lower bound is minimax over valid source unitaries, rather than a claim about every implementation of a given output state.

Let

```math
\theta=\arcsin a,
\qquad
R_y(\varphi)=\exp(-i\varphi Y/2),
```

where $`Y`$ is the single-qubit Pauli matrix. Consider the different source oracle

```math
V_x=X_f\otimes\bigotimes_{j=1}^{L}R_y(2x_j\theta).
```

It also prepares the target from the same known reference state:

```math
V_x|\perp\rangle=|0\rangle_f|\phi_x\rangle=|\psi_x\rangle.
```

For this completion, repeated calls amplify all the small rotations at once. Choose $`m`$ to be an integer nearest to $`\pi/(4\theta)`$. Since $`0\lt \theta\leq\pi/4`$, $`m\geq1`$ and

```math
\left|m\theta-\frac\pi4\right|\leq\frac\theta2.
```

After applying $`V_x`$ exactly $`m`$ times to $`|\perp\rangle`$, the data qubits are

```math
\bigotimes_{j=1}^{L}
\left(\cos(m\theta)|0\rangle+x_j\sin(m\theta)|1\rangle\right).
```

The flag has a known parity-dependent value and can be ignored. Measuring all the commuting $`X_j`$ observables gives, for every $`j`$, a sign with expectation

```math
x_j\sin(2m\theta),
\qquad
\sin(2m\theta)\geq\cos\theta\geq\frac1{\sqrt2}.
```

Each sign is therefore correct with probability at least $`(1+1/\sqrt2)/2`$. Repeating this experiment $`O(\log(L/\delta))`$ times and taking the majority separately for every qubit recovers all $`L`$ signs with failure probability at most $`\delta`$. Because $`m=O(1/\epsilon)`$, the source-call cost is

```math
O\!\left(\frac{\log(L/\delta)}{\epsilon}\right).
```

The expectation magnitudes $`2c_0a`$ are known, so recovered signs determine every expectation in this family. This procedure uses neither an inverse source call nor controlled source access. Its success relies on the rotation completion $`V_x`$; the canonical hard oracle instead satisfies $`U_x^2=I`$.

The distinction concerns what the source does on other inputs and under repeated applications. Product structure of $`U|\perp\rangle`$ alone does not specify that behavior. With the hard completion explicitly included, the commuting witness establishes that the online penalty does not require entanglement in the prepared state or noncommutativity among the requested observables. It remains a source-query statement with the stated precision regime and oracle access contract.
