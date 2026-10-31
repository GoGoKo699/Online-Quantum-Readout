# Resources and interpretation

The [main theorem](model-and-theorem.md) characterizes calls to a coherent state-preparation source. It does not identify source calls with logical gates, measurement shots, classical output size, or elapsed time. Those distinctions matter when the theorem is used to assess a complete algorithm.

Write

```math
T=\sum_{r=1}^{R}b_r,
\qquad A=\sum_{r=1}^{R}\sqrt{b_r}.
```

For a known menu of $`L`$ norm-bounded observables and predetermined batch sizes, the worst-case source complexity is

```math
Q=\widetilde\Theta\!\left(\frac{\min\{A,\sqrt L\}}{\epsilon}\right),
\qquad 0\lt \epsilon\leq\frac{1}{2\sqrt{2L}}.
```

This includes preprocessing and every invocation of $`U`$, $`U^\dagger`$, or an allowed controlled version. The lower bound permits arbitrary persistent quantum and classical memory. The [upper bounds](upper-bounds.md) use existing batch estimators.

## 1. A ledger for a complete implementation

| Resource | What must be charged | What this theorem establishes |
|---|---|---|
| Preparation source | Every use of $`U`$, its inverse, or a controlled version, before and between requests | Matching worst-case scaling, up to logarithms |
| Observable access | Controlled exponentials, block encodings, or SELECT calls required by the chosen estimator | Separate counts inherited from that estimator |
| Circuit implementation | Synthesis of source and observable operations, arithmetic, routing, and ancillary operations | No universal gate-count optimum |
| Data access | Construction and coherent addressing of the known observable descriptions | No free QRAM or free SELECT assumption |
| Retained information | Quantum workspace, classical estimates, and transcripts | No memory restriction in the lower bound; no claim of optimal memory usage |
| Classical output | $`T`$ requested numerical answers | At least $`T`$ output words; ordinary fixed-point encoding uses $`O(\log(1/\epsilon))`$ bits per answer |
| Confidence | A joint error probability for the entire transcript | Amplification or confidence allocation contributes logarithmic factors |
| Timing | Work performed before each answer deadline and before the first answer | Revelation rounds are specified; physical latency and oracle circuit depth are not |

A preparation call may be an expensive subroutine of a larger algorithm. A reduction in its count can therefore be consequential even when other costs grow. An end-to-end advantage requires charging those other costs on the same instance.

## 2. Huggins's upper bound: observable operations are per observable

For $`m`$ supplied observables, Theorem 1 of [Huggins et al.](https://arxiv.org/html/2111.09283v3) uses $`\widetilde O(\sqrt m/\epsilon)`$ source calls. It also uses $`\widetilde O(\sqrt m/\epsilon)`$ controlled exponentials for **each** observable, with evolution parameter of magnitude $`O(m^{-1/2})`$. Summing over the list gives $`\widetilde O(m^{3/2}/\epsilon)`$ controlled-exponential primitives.

Applying that statement to the present schedules gives the following derived accounting.

| Schedule | Source calls | Controlled-exponential primitives, summed over observables |
|---|---:|---:|
| Estimate each revealed batch | $`\widetilde O(A/\epsilon)`$ | $`\widetilde O(\sum_r b_r^{3/2}/\epsilon)`$ |
| Estimate the whole menu before the first answer | $`\widetilde O(\sqrt L/\epsilon)`$ | $`\widetilde O(L^{3/2}/\epsilon)`$ |
| Supply the actual list of $`T`$ requested values in advance | $`\widetilde O(\sqrt T/\epsilon)`$ | $`\widetilde O(T^{3/2}/\epsilon)`$ |

Repeated indices can be removed from the supplied offline list, making its cost smaller. The last row is a convenient upper bound in terms of the number of requested outputs.

These are counts of primitives, not lower bounds on logical gates. An implementation of $`\exp(-ixO_j)`$ can depend on $`x`$, the description of $`O_j`$, and its target synthesis error. In particular, a smaller evolution parameter need not cost as much as a unit-time evolution. If a source invocation costs $`C_\psi`$ gates and controlled exponential number $`k`$ costs $`C_{\exp,k}`$, an implementation must at least account for

```math
Q_\psi C_\psi+\sum_k C_{\exp,k}
+C_{\mathrm{auxiliary}}+C_{\mathrm{classical}}.
```

The source-minimizing schedule need not minimize this complete expression. Computing the whole menu also stores values that might never be requested. Conversely, answering one batch at a time need not retain every unrequested menu value.

For adaptive requests, a fresh batch run can be assigned conditional failure probability $`\delta/R`$. Its guarantee applies to the supplied list after any earlier history; a union bound gives overall failure at most $`\delta`$. Full-menu estimation instead uses one simultaneous guarantee for all $`L`$ values. These observations justify the query schedules without assuming that an adaptive transcript is an independent list.

## 3. An alternative with explicit SELECT and gate costs

Theorem 37 in Section 7.2 of [van Apeldoorn et al., arXiv:2207.08800v1](https://arxiv.org/html/2207.08800v1) uses a different observable interface. For $`m`$ Hermitian operators $`E_j`$ on a $`d`$-dimensional system, with $`\|E_j\|\leq1`$ and individual errors $`\epsilon_j\in(0,2]`$, define

```math
\nu=\sum_{j=1}^{m}\frac1{\epsilon_j},
\qquad
\sigma\geq
\max\!\left\{
\sqrt{2\left\|\sum_{j=1}^{m}\frac{E_j^2}{\epsilon_j^2}\right\|
\ln\!\frac{2d}{\delta}},\ 1
\right\},
\qquad
\sigma'=\min\{\nu,\sigma\},
```

where the theorem takes $`\delta\in(0,1/6]`$. Its access assumptions include a state-preparation unitary $`U_\rho`$ for a purification and a coherent selection of block encodings,

```math
U_E=\sum_{j=1}^{m}|j\rangle\langle j|\otimes U_{E_j}.
```

The theorem's resource accounting, suppressing its logarithmic factors, is

```math
\begin{array}{ll}
\text{source calls:} & \widetilde O(\sigma'),\\
\text{SELECT calls:} & \widetilde O(\nu),\\
\text{additional two-qubit gates:} &
\widetilde O(\sigma'a_\rho+\nu a_E+\nu m).
\end{array}
```

Here $`a_\rho`$ and $`a_E`$ are register-size parameters in the source and block-encoding interfaces, not gate costs for implementing those oracles. The source-call expression before suppressing logarithms is

```math
O\!\left((\sigma'+\log(\log m/\delta))\log(m/\delta)\right)
```

for the nondegenerate multi-observable setting. A single observable can instead be handled by the usual single-value estimator. A circuit realization with source cost $`C_\rho`$ and SELECT cost $`C_{\mathrm{SELECT}}`$ must add those costs, giving the schematic total

```math
\widetilde O\!\left(
\sigma'C_\rho+\nu C_{\mathrm{SELECT}}
+\sigma'a_\rho+\nu a_E+\nu m
\right).
```

Knowing a classical list of observables does not make its coherent multiplexor a constant-cost operation. Its construction, routing, workspace, and gate synthesis must be supplied by the application. Alternatively, the Huggins formulation can be used with separately implemented controlled evolutions. Neither route licenses free loading of unknown state data.

For equal precision, $`\nu=m/\epsilon`$. Writing $`\kappa=\|\sum_j E_j^2\|`$, the smallest allowed $`\sigma`$ is

```math
\max\!\left\{\frac{\sqrt{2\kappa\ln(2d/\delta)}}{\epsilon},1\right\}.
```

This can be useful when $`\kappa`$ is small. It is not automatically a dimension-independent improvement on Huggins's source bound. For both hard menus below, a subset of size $`b`$ has $`\kappa=b`$. The star witness has $`d=O(L)`$, so its dimension factor is logarithmic in $`L`$. The commuting witness has $`\log d=\Theta(L)`$; that factor can remove the apparent square-root benefit of this particular theorem. The dimension-independent Huggins estimator supplies the matching source upper bound for both witnesses. Also, the additional-gate term $`\nu m`$ is $`m^2/\epsilon`$ at uniform precision, even before implementing SELECT.

## 4. What the two hard witnesses show

| Property | Star witness | Commuting product-state witness |
|---|---|---|
| Source register | Dimension $`L+2`$, embedded in $`O(\log L)`$ qubits | $`L`$ data qubits and one flag qubit |
| Prepared state | A reference amplitude and $`L`$ weak signed amplitudes | A tensor product of weakly tilted one-qubit states, with a fixed flag |
| Observable menu | $`O_j=\lvert r\rangle\langle j\rvert+\lvert j\rangle\langle r\rvert`$ | One-qubit Pauli $`X_j`$ operators on the data |
| Commutativity | Generally noncommuting | All commute |
| Operator norm | One | One |
| Squared Frobenius norm | Two | Exponential in the number of data qubits |
| Subset overlap norm $`\lVert\sum_{j\in S}O_j^2\rVert`$ | $`\lvert S\rvert`$ | $`\lvert S\rvert`$ |
| Source completion used in the lower bound | Canonical swap with an orthogonal input | Canonical swap with an orthogonal input |

The [star proof](lower-bound.md) obtains $`L`$ recoverable signs while using only $`O(\log L)`$ source qubits. The [commuting proof](commuting-witness.md) shows that the phenomenon does not require noncommuting requests or entanglement in the prepared state. These are alternative worst-case witnesses, not one construction with all of their favorable properties simultaneously.

The precision restriction has a geometric role. In the star state,

```math
|\psi_x\rangle=c|r\rangle+
\frac{s}{\sqrt L}\sum_{j=1}^{L}x_j|j\rangle,
\qquad s=2\epsilon\sqrt L,
\qquad c=\sqrt{1-s^2},
```

normalization and a nonvanishing reference amplitude require bounded $`L\epsilon^2`$. The commuting construction uses local amplitudes of order $`\epsilon`$, and its Fourier-progress bound likewise uses bounded $`L\epsilon^2`$. These arguments do not establish the same scheduling frontier at fixed nonzero precision for arbitrarily large menus.

## 5. A preparation map does not specify the whole oracle

The oracle promise $`U|\perp\rangle=|\psi\rangle`$ leaves its action on other inputs unspecified. Algorithms in this model may apply the full oracle to arbitrary inputs. The lower bound therefore states an explicit hard completion:

```math
U_x=I-|\perp\rangle\langle\perp|-|\psi_x\rangle\langle\psi_x|
+|\perp\rangle\langle\psi_x|+|\psi_x\rangle\langle\perp|,
\qquad \langle\perp|\psi_x\rangle=0.
```

It swaps the input and prepared state, fixes their orthogonal complement, and satisfies $`U_x^\dagger=U_x`$. Its full action is part of the witness. A worst-case result over allowed source oracles may use this completion; it cannot be reinterpreted as a lower bound for every circuit preparing the same state.

For example, consider the product state with local amplitude $`a=2\epsilon`$ and set $`\theta=\arcsin a`$. The oracle

```math
V_x=X_{\mathrm{flag}}\otimes
\bigotimes_{j=1}^{L}R_y(2\theta x_j)
```

prepares the same flagged product-state family from the known reference $`|\perp\rangle=|1\rangle_{\mathrm{flag}}|0\rangle^{\otimes L}`$. However, $`k`$ repeated calls rotate each data qubit by $`2k\theta x_j`$. Choosing $`k`$ nearest to $`\pi/(4\theta)`$ gives a constant-bias $`X`$-basis estimate of **every** sign in parallel. Repeating this experiment $`O(\log(L/\delta))`$ times recovers the whole sign vector with failure at most $`\delta`$, using $`\widetilde O(1/\epsilon)`$ calls. This easier completion demonstrates why the source unitary, rather than only its prepared state, must appear in the theorem's specification.

A supplied classical circuit description that reveals the signs or allows free classical simulation would also change the model. The result concerns black-box source calls; it assumes neither hidden-sign loading into free QRAM nor uncharged access to the source's internal gate description.

## 6. Copy strategies remain meaningful comparators

The rank-two star menu has bounded squared Frobenius norm. The [classical-shadow guarantee of Huang, Kueng, and Preskill](https://arxiv.org/html/2002.08953v2) therefore estimates its entire known menu using $`O(\log(L/\delta)/\epsilon^2)`$ copies. For the product witness, measuring all data qubits in the $`X`$ basis yields one sample of every commuting expectation at once; concentration and a union bound give the same copy scaling. Either can be implemented with one preparation call per copy.

On the simultaneous-success event, all later indices from the known menu can be answered, even if selected using earlier answers. Thus it would be incorrect to claim that delayed questions necessarily destroy the reusability of a classical record. The distinction here is the number of coherent source calls at high precision. If $`\epsilon\leq c/\sqrt L`$, then

```math
\frac1{\epsilon^2}\geq\frac1c\frac{\sqrt L}{\epsilon},
```

so these copy upper bounds are consistent with the full-menu endpoint of the coherent frontier.

The [related-work page](../references/related-work.md) also compares algorithms designed specifically for adaptive copy-based tomography. Their sample guarantees should not be substituted for source-query lower bounds or quoted with their precision factors suppressed when comparing resource costs.

## 7. Operational limits of the conclusion

For equal batches, the unsaturated cost is $`R\sqrt b/\epsilon`$, while the supplied-list upper bound for the same $`T=Rb`$ outputs is $`\widetilde O(\sqrt T/\epsilon)`$. The resulting factor $`\sqrt R`$ requires a menu large enough to avoid saturation, $`L\geq R^2b`$, and the theorem's precision condition. It is a worst-case comparison: predictable requests, repeated indices, or a more informative source completion can be easier.

The round count describes external revelation of objectives. It is not the depth of a parallel quantum query circuit. Unlimited memory does not remove the lower bound, but the theorem does not prove optimal memory usage. Ideal inverse and controlled-source access are included in the model; noise, approximate inverses, fault-tolerant synthesis, and application-specific state-preparation costs require their own accounting. No total-runtime separation is asserted without that additional implementation model.
