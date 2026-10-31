#!/usr/bin/env python3
"""Finite, deterministic checks of the online-readout lower-bound operators.

These checks validate small matrices, not the asymptotic theorem, novelty, or an
algorithm's resource accounting. See README.md in this directory.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import platform
import sys
from pathlib import Path

import numpy as np

DIMENSIONS = (2, 3, 4)
PRECISION_FRACTIONS = (0.1, 0.5, 1.0)
SUBSETS = {
    2: ((0,), (1,), (0, 1)),
    3: ((0,), (2,), (0, 2), (0, 1, 2)),
    4: ((0,), (3,), (0, 1), (1, 3), (0, 1, 2, 3)),
}
ACTIVITIES = (0.0, 0.125, 0.5, 1.0)
SEED = 20261031
ATOL = 5e-11
RTOL = 5e-11


class Checks:
    def __init__(self) -> None:
        self.count = 0
        self.failures: list[str] = []

    def close(self, actual: float, expected: float, label: str) -> None:
        self.count += 1
        allowed = ATOL + RTOL * abs(expected)
        if not (math.isfinite(actual) and abs(actual - expected) <= allowed):
            self.failures.append(
                f"{label}: actual={actual:.17g}, expected={expected:.17g}, "
                f"tolerance={allowed:.3g}"
            )

    def upper(self, actual: float, bound: float, label: str) -> None:
        self.count += 1
        if not (math.isfinite(actual) and actual <= bound + ATOL + RTOL * abs(bound)):
            self.failures.append(f"{label}: {actual:.17g} exceeds {bound:.17g}")

    def lower(self, actual: float, bound: float, label: str) -> None:
        self.upper(-actual, -bound, label)


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix)))


def rectangular_norm(matrix: np.ndarray) -> float:
    """Spectral norm, through the small input-side Gram matrix."""
    eigenvalues = np.linalg.eigvalsh(matrix.conj().T @ matrix)
    return math.sqrt(max(0.0, float(eigenvalues[-1])))


def commutator_norm(commutator: np.ndarray) -> float:
    """For a commutator of Hermitian matrices, i times it is Hermitian."""
    return float(np.max(np.abs(np.linalg.eigvalsh(1j * commutator))))


def update_max(metrics: dict, key: str, value: float) -> None:
    metrics[key] = max(metrics.get(key, 0.0), float(value))


def update_min(metrics: dict, key: str, value: float) -> None:
    metrics[key] = min(metrics.get(key, float("inf")), float(value))


def hadamard_matrix(L: int) -> np.ndarray:
    n = 1 << L
    return np.array(
        [[(-1.0) ** ((w & x).bit_count()) / math.sqrt(n) for x in range(n)]
         for w in range(n)],
        dtype=np.complex128,
    )


def bit_flip(n: int, mask: int) -> np.ndarray:
    out = np.zeros((n, n), dtype=np.complex128)
    out[np.arange(n) ^ mask, np.arange(n)] = 1.0
    return out


def occupation(L: int, subset: tuple[int, ...]) -> np.ndarray:
    return np.array(
        [sum((w >> j) & 1 for j in subset) for w in range(1 << L)],
        dtype=float,
    )


def canonical_swap(psi: np.ndarray) -> np.ndarray:
    """Householder construction, independent of the joint isometry formula."""
    difference = -psi.copy()
    difference[0] += 1.0  # |perp> is source basis vector zero.
    return np.eye(psi.size, dtype=np.complex128) - np.outer(
        difference, difference.conj()
    )


def physical_states(family: str, L: int, epsilon: float) -> np.ndarray:
    states = []
    if family == "star":
        s = 2.0 * epsilon * math.sqrt(L)
        c = math.sqrt(1.0 - s * s)
        for x in range(1 << L):
            signs = np.array([1.0 - 2.0 * ((x >> j) & 1) for j in range(L)])
            states.append(np.r_[0.0, c, s * signs / math.sqrt(L)])
    else:
        a = 2.0 * epsilon
        c = math.sqrt(1.0 - a * a)
        for x in range(1 << L):
            psi = np.array([1.0])
            # Source bit j is the j-th least significant computational bit.
            for j in reversed(range(L)):
                sign = 1.0 - 2.0 * ((x >> j) & 1)
                psi = np.kron(psi, np.array([c, a * sign]))
            states.append(np.r_[0.0, psi])
    return np.asarray(states, dtype=np.complex128)


def physical_observables(family: str, L: int) -> list[np.ndarray]:
    d = L + 2 if family == "star" else (1 << L) + 1
    observables = []
    for j in range(L):
        O = np.zeros((d, d), dtype=np.complex128)
        if family == "star":
            O[1, 2 + j] = O[2 + j, 1] = 1.0
        else:
            labels = np.arange(1 << L)
            O[1 + (labels ^ (1 << j)), 1 + labels] = 1.0
        observables.append(O)
    return observables


def formula_isometries(
    family: str, L: int, epsilon: float, d: int
) -> tuple[np.ndarray, np.ndarray, np.ndarray | None]:
    n = 1 << L
    A = np.zeros((n * d, n), dtype=np.complex128)
    B = np.zeros_like(A)
    B[np.arange(n) * d, np.arange(n)] = 1.0
    if family == "star":
        R = np.zeros_like(A)
        R[np.arange(n) * d + 1, np.arange(n)] = 1.0
        V = np.zeros_like(A)
        for j in range(L):
            V[(np.arange(n) ^ (1 << j)) * d + 2 + j, np.arange(n)] = (
                1.0 / math.sqrt(L)
            )
        s = 2.0 * epsilon * math.sqrt(L)
        A = math.sqrt(1.0 - s * s) * R + s * V
        return A, B, V
    a = 2.0 * epsilon
    c = math.sqrt(1.0 - a * a)
    for z in range(n):
        weight = z.bit_count()
        coefficient = (c ** (L - weight)) * (a ** weight)
        A[(np.arange(n) ^ z) * d + 1 + z, np.arange(n)] = coefficient
    return A, B, None


def random_unit_vector(d: int, rng: np.random.Generator) -> np.ndarray:
    vector = rng.standard_normal(d) + 1j * rng.standard_normal(d)
    return vector / np.linalg.norm(vector)


def expectation(diagonal: np.ndarray, branches: np.ndarray) -> float:
    return float(np.sum(np.abs(branches) ** 2 * diagonal[None, :]).real)


def active_flag_checks(
    U: np.ndarray,
    gamma: np.ndarray,
    analytic_bound: float,
    checks: Checks,
    rng: np.random.Generator,
    metrics: dict,
    label: str,
    *,
    extremal: bool = False,
) -> list[dict]:
    """Check actual controlled-state evolution, with active and inactive branches."""
    dim = U.shape[0]
    inactive = random_unit_vector(dim, rng)
    if extremal:
        progress_change = U.conj().T @ (gamma[:, None] * U) - np.diag(gamma)
        values, vectors = np.linalg.eigh(progress_change)
        index = int(np.argmax(np.abs(values)))
        active = vectors[:, index]
        exact_norm = float(abs(values[index]))
    else:
        active = random_unit_vector(dim, rng)
        exact_norm = None
    active_after = U @ active
    full_change = float(
        np.vdot(active_after, gamma * active_after).real
        - np.vdot(active, gamma * active).real
    )
    samples = []
    for probability in ACTIVITIES:
        before = np.stack(
            (math.sqrt(1.0 - probability) * inactive, math.sqrt(probability) * active)
        )
        after = before.copy()
        after[1] = U @ before[1]
        actual_probability = float(np.vdot(before[1], before[1]).real)
        change = expectation(gamma, after) - expectation(gamma, before)
        expected_change = probability * full_change
        residual = abs(change - expected_change)
        checks.close(actual_probability, probability, label + " active weight")
        checks.close(change, expected_change, label + " activity-linear progress")
        checks.upper(
            abs(change), analytic_bound * probability, label + " paid-query bound"
        )
        update_max(metrics, "activity_identity_residual_max", residual)
        update_max(
            metrics, "activity_weight_residual_max", abs(actual_probability - probability)
        )
        update_max(
            metrics, "activity_bound_violation_max",
            max(0.0, abs(change) - analytic_bound * probability),
        )
        metrics["samples"] = metrics.get("samples", 0) + 1
        if extremal:
            checks.close(
                abs(change), probability * exact_norm,
                label + " extremal progress saturation",
            )
            samples.append(
                {
                    "activity_probability": probability,
                    "absolute_progress_change": abs(change),
                    "activity_times_exact_norm": probability * exact_norm,
                    "activity_times_proved_bound": probability * analytic_bound,
                }
            )
    return samples


def check_fresh_subset_averaging(checks: Checks) -> dict:
    metrics = {"cases": 0, "matrix_residual_max": 0.0}
    for L in DIMENSIONS:
        n = 1 << L
        flips = [bit_flip(n, 1 << j) for j in range(L)]
        global_gamma = sum(flips) / L
        for b in sorted({len(S) for S in SUBSETS[L]}):
            subsets = list(itertools.combinations(range(L), b))
            average = sum(sum(flips[j] for j in S) / b for S in subsets) / len(subsets)
            residual = max_abs(average - global_gamma)
            checks.close(residual, 0.0, f"fresh subset average L={L}, b={b}")
            update_max(metrics, "matrix_residual_max", residual)
            metrics["cases"] += 1
    return metrics


def run_checks() -> dict:
    checks = Checks()
    rng = np.random.default_rng(SEED)
    source_cases = []
    subset_cases = []
    extremal_cases = []
    family_metrics = {"star": {}, "product": {}}
    activity_metrics = {"random": {}, "extremal": {}}
    counts = {
        "source_oracles": 0,
        "hidden_input_states": 0,
        "mean_values": 0,
        "subset_operator_cases": 0,
    }

    for family in ("star", "product"):
        metrics = family_metrics[family]
        for L in DIMENSIONS:
            n = 1 << L
            H = hadamard_matrix(L)
            observables = physical_observables(family, L)
            flips = [bit_flip(n, 1 << j) for j in range(L)]
            if family == "product":
                for j in range(L):
                    for k in range(j):
                        residual = max_abs(
                            observables[j] @ observables[k]
                            - observables[k] @ observables[j]
                        )
                        checks.close(residual, 0.0, f"Pauli commutation L={L}, {j},{k}")
                        update_max(metrics, "observable_commutation_residual_max", residual)
            for j, O in enumerate(observables):
                norm = float(np.max(np.abs(np.linalg.eigvalsh(O))))
                checks.close(norm, 1.0, f"observable norm {family}, L={L}, j={j}")

            for fraction in PRECISION_FRACTIONS:
                epsilon = fraction / (2.0 * math.sqrt(2.0 * L))
                states = physical_states(family, L, epsilon)
                d = states.shape[1]
                blocks = np.asarray([canonical_swap(psi) for psi in states])
                label = f"{family}, L={L}, precision fraction={fraction}"
                perp = np.zeros(d, dtype=np.complex128)
                perp[0] = 1.0
                parameter = 2.0 * epsilon * (math.sqrt(L) if family == "star" else 1.0)
                mean_magnitude = (
                    2.0 * math.sqrt(1.0 - parameter * parameter) * parameter
                    / (math.sqrt(L) if family == "star" else 1.0)
                )
                for x, (psi, block) in enumerate(zip(states, blocks)):
                    checks.close(float(np.vdot(psi, psi).real), 1.0, label + " state norm")
                    prep_residual = max_abs(block @ perp - psi)
                    unprep_residual = max_abs(block @ psi - perp)
                    checks.close(prep_residual, 0.0, label + " preparation action")
                    checks.close(unprep_residual, 0.0, label + " inverse action")
                    update_max(metrics, "preparation_action_residual_max", prep_residual)
                    update_max(metrics, "inverse_action_residual_max", unprep_residual)
                    for j, O in enumerate(observables):
                        observed = float(np.vdot(psi, O @ psi).real)
                        expected = mean_magnitude * (1.0 - 2.0 * ((x >> j) & 1))
                        checks.close(observed, expected, label + f" mean x={x},j={j}")
                        checks.lower(
                            abs(observed) / epsilon, 2.0 * math.sqrt(2.0),
                            label + " sign margin",
                        )
                        update_max(metrics, "mean_formula_residual_max", abs(observed - expected))
                        update_min(metrics, "mean_margin_over_epsilon_min", abs(observed) / epsilon)
                        counts["mean_values"] += 1
                    counts["hidden_input_states"] += 1

                # Transform the explicit input-controlled physical oracle and isometry.
                # This route does not use the commutator formulas being tested.
                U = np.einsum("wx,xab,vx->wavb", H, blocks, H, optimize=True).reshape(n*d, n*d)
                A = np.einsum("wx,xa,vx->wav", H, states, H, optimize=True).reshape(n*d, n)
                A_formula, B, V_formula = formula_isometries(family, L, epsilon, d)
                U_formula = (
                    np.eye(n*d) - A_formula @ A_formula.conj().T - B @ B.conj().T
                    + A_formula @ B.conj().T + B @ A_formula.conj().T
                )
                residuals = {
                    "oracle_hermiticity_residual": max_abs(U - U.conj().T),
                    "oracle_unitarity_residual": max_abs(U.conj().T @ U - np.eye(n*d)),
                    "fourier_isometry_residual": max_abs(A - A_formula),
                    "fourier_oracle_residual": max_abs(U - U_formula),
                    "isometry_normalization_residual": max_abs(A.conj().T @ A - np.eye(n)),
                }
                for key, value in residuals.items():
                    checks.close(value, 0.0, label + " " + key)
                    update_max(metrics, key + "_max", value)
                source_cases.append(
                    {
                        "family": family, "L": L, "precision_fraction": fraction,
                        "epsilon": epsilon, "source_dimension": d,
                        "joint_input_source_dimension": n*d,
                        "mean_margin_over_epsilon": mean_magnitude / epsilon,
                        **residuals,
                    }
                )
                counts["source_oracles"] += 1

                if family == "star":
                    R = np.zeros_like(A)
                    R[np.arange(n)*d + 1, np.arange(n)] = 1.0
                    V = (A - math.sqrt(1.0-parameter*parameter)*R) / parameter
                    checks.close(max_abs(V - V_formula), 0.0, label + " extracted V")
                else:
                    V = None

                for S in SUBSETS[L]:
                    b = len(S)
                    ks = occupation(L, S)
                    kout = np.repeat(ks, d)
                    comm_A = kout[:, None]*A - A*ks[None, :]
                    comm_U = (kout[:, None] - kout[None, :])*U
                    U_norm = commutator_norm(comm_U)
                    gamma_input = H @ (sum(flips[j] for j in S) / b) @ H
                    gamma_expected = 1.0 - 2.0*ks/b
                    gamma_residual = max_abs(gamma_input - np.diag(gamma_expected))
                    checks.close(gamma_residual, 0.0, label + f" Gamma identity {S}")
                    gamma = np.repeat(gamma_expected, d)
                    comm_gamma = (gamma[:, None]-gamma[None, :])*U
                    gamma_norm = commutator_norm(comm_gamma)
                    checks.close(
                        gamma_norm, 2.0*U_norm/b, label + f" Gamma commutator relation {S}"
                    )
                    case = {
                        "family": family, "L": L, "precision_fraction": fraction,
                        "epsilon": epsilon, "subset_zero_based": list(S), "b": b,
                        "Gamma_affine_identity_residual": gamma_residual,
                    }
                    if family == "star":
                        comm_V = kout[:, None]*V - V*ks[None, :]
                        measured = rectangular_norm(comm_V)
                        expected = math.sqrt(b/L)
                        checks.close(measured, expected, label + f" exact V norm {S}")
                        update_max(
                            metrics, "V_commutator_norm_residual_max", abs(measured-expected)
                        )
                        U_bound = 4.0*parameter*math.sqrt(b/L)
                        case.update(
                            {"isometry_commutator_norm": measured,
                             "isometry_commutator_norm_formula": expected}
                        )
                    else:
                        p = parameter*parameter
                        gram = comm_A.conj().T @ comm_A
                        expected_diagonal = b*p*(1.0-p) + p*p*(b-2.0*ks)**2
                        gram_residual = max_abs(gram - np.diag(expected_diagonal))
                        measured_squared = float(np.linalg.eigvalsh(gram)[-1])
                        expected_squared = b*p*(1.0-p) + b*b*p*p
                        checks.close(
                            gram_residual, 0.0, label + f" product Gram diagonal {S}"
                        )
                        checks.close(
                            measured_squared, expected_squared,
                            label + f" exact product squared norm {S}",
                        )
                        update_max(
                            metrics, "A_commutator_gram_residual_max", gram_residual
                        )
                        update_max(
                            metrics, "A_commutator_squared_norm_residual_max",
                            abs(measured_squared-expected_squared),
                        )
                        U_bound = 4.0*math.sqrt(expected_squared)
                        case.update(
                            {"isometry_commutator_squared_norm": measured_squared,
                             "isometry_commutator_squared_norm_formula": expected_squared,
                             "isometry_commutator_gram_residual": gram_residual}
                        )
                    gamma_bound = 2.0*U_bound/b
                    checks.upper(U_norm, U_bound, label + f" source commutator bound {S}")
                    checks.upper(gamma_norm, gamma_bound, label + f" Gamma bound {S}")
                    update_max(metrics, "U_commutator_bound_ratio_max", U_norm/U_bound)
                    update_max(metrics, "Gamma_commutator_bound_ratio_max", gamma_norm/gamma_bound)
                    update_max(
                        metrics, "commutator_bound_violation_max",
                        max(0.0, U_norm-U_bound, gamma_norm-gamma_bound),
                    )
                    update_max(metrics, "Gamma_affine_identity_residual_max", gamma_residual)
                    case.update(
                        {"source_commutator_norm": U_norm, "source_commutator_bound": U_bound,
                         "Gamma_commutator_norm": gamma_norm,
                         "Gamma_commutator_bound": gamma_bound}
                    )
                    subset_cases.append(case)
                    counts["subset_operator_cases"] += 1
                    active_flag_checks(
                        U, gamma, gamma_bound, checks, rng, activity_metrics["random"],
                        label + f" active flag {S}",
                    )
                    if L == 2 and fraction == 1.0 and S == (0,):
                        samples = active_flag_checks(
                            U, gamma, gamma_bound, checks, rng, activity_metrics["extremal"],
                            label + " extremal active flag", extremal=True,
                        )
                        extremal_cases.append({"family": family, "samples": samples})

    averaging = check_fresh_subset_averaging(checks)
    counts["fresh_subset_averaging_cases"] = averaging["cases"]
    counts["random_active_flag_samples"] = activity_metrics["random"]["samples"]
    counts["extremal_active_flag_samples"] = activity_metrics["extremal"]["samples"]
    counts["scalar_assertions"] = checks.count
    return {
        "schema_version": 1,
        "status": "pass" if not checks.failures else "fail",
        "scope": "Finite operator checks; not a proof of the general theorem or a novelty test.",
        "configuration": {
            "L_values": list(DIMENSIONS),
            "precision_fractions_of_upper_bound": list(PRECISION_FRACTIONS),
            "precision_upper_bound": "1/(2*sqrt(2*L))",
            "subsets_zero_based": {str(L): [list(S) for S in SUBSETS[L]] for L in DIMENSIONS},
            "random_seed": SEED,
            "activity_probabilities": list(ACTIVITIES),
            "absolute_tolerance": ATOL, "relative_tolerance": RTOL,
        },
        "environment": {
            "python": platform.python_version(), "numpy": np.__version__,
            "system": platform.system(), "machine": platform.machine(),
            "dtype": "complex128 / float64",
        },
        "counts": counts, "metrics": family_metrics,
        "active_flag_metrics": activity_metrics,
        "fresh_subset_averaging": averaging,
        "source_cases": source_cases, "subset_cases": subset_cases,
        "extremal_active_flag_cases": extremal_cases,
        "failures": checks.failures,
    }


def report_differences(actual: object, expected: object, path: str = "") -> list[str]:
    """Compare a recomputation with a saved report, tolerating floating roundoff."""
    if path == "environment":
        return []  # Report it, but do not require the same operating system/build.
    if isinstance(actual, dict) and isinstance(expected, dict):
        if actual.keys() != expected.keys():
            return [f"{path or '<root>'}: JSON keys differ"]
        return [
            error
            for key in actual
            for error in report_differences(actual[key], expected[key], f"{path}.{key}".lstrip("."))
        ]
    if isinstance(actual, list) and isinstance(expected, list):
        if len(actual) != len(expected):
            return [f"{path}: list lengths differ"]
        return [
            error for index, (a, e) in enumerate(zip(actual, expected))
            for error in report_differences(a, e, f"{path}[{index}]")
        ]
    if isinstance(actual, (float, int)) and isinstance(expected, (float, int)):
        if isinstance(actual, int) and isinstance(expected, int):
            return [] if actual == expected else [f"{path}: integer differs"]
        good = math.isfinite(float(actual)) and math.isfinite(float(expected))
        if good and abs(actual-expected) <= ATOL + RTOL*abs(expected):
            return []
        return [f"{path}: numerical value differs ({actual} versus {expected})"]
    return [] if actual == expected else [f"{path}: value differs"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    destination = parser.add_mutually_exclusive_group()
    destination.add_argument("--output", type=Path, help="write the deterministic JSON report")
    destination.add_argument("--check", type=Path, help="recompute and compare a saved JSON report")
    args = parser.parse_args()
    report = run_checks()
    differences = []
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8"
        )
    if args.check:
        try:
            expected = json.loads(args.check.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            parser.error(f"cannot read reference report: {error}")
        differences = report_differences(report, expected)
    print(f"Operator validation: {report['status'].upper()}")
    print(f"Python {report['environment']['python']}; NumPy {report['environment']['numpy']}")
    print(
        f"{report['counts']['source_oracles']} source oracles; "
        f"{report['counts']['subset_operator_cases']} subset cases; "
        f"{report['counts']['hidden_input_states']} hidden-input states; "
        f"{report['counts']['mean_values']} mean values"
    )
    print(
        f"{report['counts']['random_active_flag_samples']} random active-flag samples; "
        f"{report['counts']['extremal_active_flag_samples']} extremal samples; "
        f"{report['counts']['fresh_subset_averaging_cases']} fresh-subset averages; "
        f"{report['counts']['scalar_assertions']} assertions"
    )
    for family, metrics in report["metrics"].items():
        residuals = [v for k, v in metrics.items() if "residual" in k]
        print(
            f"{family}: max recorded identity residual={max(residuals):.3e}; "
            f"max source-bound ratio={metrics['U_commutator_bound_ratio_max']:.6f}; "
            f"min sign margin/epsilon={metrics['mean_margin_over_epsilon_min']:.6f}"
        )
    if args.output:
        print(f"Report written: {args.output}")
    if args.check:
        print("Saved report comparison: " + ("FAIL" if differences else "PASS"))
        if report["environment"] != expected.get("environment"):
            print("Environment differs from reference; numerical tolerances were applied.")
    for failure in report["failures"] + differences:
        print("FAIL: " + failure, file=sys.stderr)
    print("Finite checks only; the general result is proved in the science pages.")
    return 1 if report["failures"] or differences else 0


if __name__ == "__main__":
    raise SystemExit(main())

