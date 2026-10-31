# Reproducible finite checks

This directory contains small-matrix checks of the operators used in the lower bound. The script constructs the physical source oracle for every hidden input, transforms that oracle into the Fourier basis, and compares the result with the proof's isometry representation. It then evaluates the relevant commutators and sign margins.

The general theorem is proved in [the lower-bound page](../science/lower-bound.md), under the contract in [the model and theorem](../science/model-and-theorem.md). The alternative local, commuting family is proved in [the commuting-witness page](../science/commuting-witness.md). Numerical agreement on these instances does not establish the general theorem or the novelty of the contribution.

## Run the checks

The recorded environment is Python **3.12.14**, NumPy **2.3.5**, Linux `x86_64`, with `complex128` matrices and `float64` real values. NumPy is the only third-party dependency.

From the repository root, install the pinned dependency if needed:

```bash
python -m pip install -r verification/requirements.txt
```

The following commands were run successfully:

```bash
python verification/check_bounds.py --output verification/results.json
python verification/check_bounds.py --check verification/results.json
```

The first command writes the machine-readable report. The second recomputes every check and compares the result with the saved report. Running without either option performs the checks and prints the summary without writing a file. A failed mathematical check or a mismatched reference report returns a nonzero exit status.

The random seed is fixed at `20261031`. The report contains no timestamp or elapsed time. A second JSON generation in the recorded environment was compared byte for byte with the first and was identical. Cross-environment comparisons permit floating-point differences using absolute and relative tolerances of $5\times10^{-11}$; environment metadata is displayed but is not required to match.

## What is checked

| Check | Numerical construction and assertion |
|---|---|
| Physical preparation oracle | For each hidden string, construct the Householder swap $I-(\lvert\perp\rangle-\lvert\psi_x\rangle)(\langle\perp\rvert-\langle\psi_x\rvert)$. Check preparation, inverse action, Hermiticity and unitarity. |
| Fourier representation | Transform the explicit input-controlled physical oracle and preparation isometry with a Hadamard matrix. Compare them with the independently assembled isometries $A,B,V$ and the formula $I-AA^\dagger-BB^\dagger+AB^\dagger+BA^\dagger$. |
| Star-family rate | Evaluate the spectral norm of the rectangular commutator and check $\lVert[K_S,V]\rVert=\sqrt{b/L}$, then evaluate $\lVert[K_S,U]\rVert\le 4s\sqrt{b/L}$. |
| Edge-progress rate | Assemble the average hidden-input bit-flip operator, transform it to the Fourier basis, and check $\Gamma_S=I-2K_S/b$ and the corresponding source-query commutator bound. |
| Product-family rate | Compute the entire Gram matrix of $[K_S,A]$. Check its diagonal formula and the exact maximum $\lVert[K_S,A]\rVert^2=bp(1-p)+b^2p^2$, where $p=4\epsilon^2$. Check the resulting oracle and progress bounds. |
| Means and sign margins | Evaluate every requested mean directly on every hidden-input state. Compare with its formula and check $\lvert\langle O_j\rangle\rvert/\epsilon\ge2\sqrt2$. The product family's compressed Pauli observables are also checked to commute. |
| Fresh-subset averaging | Enumerate all subsets of each tested size and average the actual bit-flip matrices. Check $\mathbb E_S\Gamma_S=L^{-1}\sum_j F_j$. |
| Active-query flag | Evolve a normalized state with separate active and inactive control branches. Check that its progress change equals the active probability times the active branch's change and obeys the weighted operator bound. Random states and extremal eigenstates are both used. |

For the star family, $s=2\epsilon\sqrt L$. For the product family, the single-qubit coefficient is $a=2\epsilon$ and $p=a^2$. The product Gram calculation also checks the individual eigenvalue formula
$$
bp(1-p)+p^2\bigl(b-2|w\cap S|\bigr)^2,
$$
rather than checking only its largest eigenvalue.

The active-flag cases use probabilities $0,\tfrac18,\tfrac12,1$. In the extremal cases, the active branch is an eigenvector of $U^\dagger\Gamma_SU-\Gamma_S$ with largest absolute eigenvalue. This checks the probability dependence at saturation of the *exact* operator norm, as well as on random states. It does not assign fractional physical query cost to a coherently controlled invocation: that invocation still costs one full call in the theorem's model.

## Instance grid and matrix sizes

The grid uses $L=2,3,4$, with
$$
\epsilon=f\,\epsilon_{\max}(L),\qquad
f\in\{0.1,0.5,1\},\qquad
\epsilon_{\max}(L)=\frac{1}{2\sqrt{2L}}.
$$
Thus the numerical instances include low, intermediate and boundary precision. All $2^L$ hidden strings are enumerated for every family and precision.

The subset labels in the code and JSON are **zero-based**.

| $L$ | Tested subsets |
|---:|---|
| 2 | $\{0\},\{1\},\{0,1\}$ |
| 3 | $\{0\},\{2\},\{0,2\},\{0,1,2\}$ |
| 4 | $\{0\},\{3\},\{0,1\},\{1,3\},\{0,1,2,3\}$ |

Nonleading and nonconsecutive subsets check the index conventions. Subset averaging separately enumerates *all* subsets at each tested size.

The star source has dimension $L+2$. The product calculations retain the active source subspace
$$
\operatorname{span}\{|\perp\rangle\}\ \oplus\ (\mathbb C^2)^{\otimes L},
$$
of dimension $1+2^L$. Including the hidden-input reference, the largest matrix dimension is **272**.

In a physical flag-qubit embedding of the product family, the additional unused source states have an identity oracle action. They add zero commutator blocks and do not change the prepared-state means. The script uses the compressed Pauli operators on the active subspace; the statement that the full observables are one-local Pauli operators follows from the explicit flag embedding in the proof.

## Recorded result

The saved [results.json](results.json) reports **PASS**:

| Coverage | Count |
|---|---:|
| Joint source oracles | 18 |
| Hidden-input states across both families and precisions | 168 |
| Directly evaluated mean values | 576 |
| Subset/operator cases | 72 |
| Random active-flag samples | 288 |
| Extremal active-flag samples | 8 |
| Fresh-subset averages | 8 |
| Scalar assertions | 3,083 |

Representative maximum residuals from that run are:

| Quantity | Star family | Product family |
|---|---:|---:|
| Unitarity residual | $6.66\times10^{-16}$ | $8.88\times10^{-16}$ |
| Fourier oracle representation residual | $3.33\times10^{-16}$ | $4.44\times10^{-16}$ |
| Exact isometry commutator identity residual | $6.66\times10^{-16}$, norm | $4.44\times10^{-16}$, squared norm |
| Maximum ratio of measured source commutator norm to proved bound | 0.353553 | 0.353443 |
| Minimum observed $\lvert\langle O_j\rangle\rvert/\epsilon$ | 2.828427 | 3.464102 |

Matrix residuals are maximum absolute entry differences unless a spectral norm is explicitly specified. The largest active-progress linearity residual was $1.67\times10^{-16}$. The largest active-weight normalization residual was $1.11\times10^{-15}$. Fresh-subset averaging had zero recorded residual. No commutator or active-progress bound was violated.

The bound ratios quantify the tested instances only; they are not a proposed improvement to the theorem's constants.

## What the checks do not establish

These finite calculations do not simulate arbitrary online algorithms or prove the treatment of unrestricted memory, adaptive stopping, conditional correctness or expected physical query costs. Those statements require the argument in the proof pages.

The product witness is a lower bound for the specified canonical preparation-oracle completion. The natural tensor product of exposed single-qubit rotations is a different, stronger oracle. The checks do not support transferring the lower bound to that access model.

The script also does not establish novelty, optimal gate complexity, a practical crossover, or behavior outside the stated high-precision regime. Its role is to make the small-instance operator calculations reproducible and to catch errors in representations, signs, normalization and resource-related progress identities.

