# Related work and the role of objective timing

The result studied here concerns a coherent source that remains available while requests arrive. A public menu contains $L$ observables. In round $r$, only the requested subset of size $b_r$ is revealed, and its answers are due before the next subset is disclosed. With arbitrary retained memory and all source calls charged, the [main theorem](../science/model-and-theorem.md) gives the worst-case frontier

$$
Q=\widetilde\Theta\!\left(
\frac{\min\{\sum_r\sqrt{b_r},\sqrt L\}}{\epsilon}
\right)
\quad\text{for }\epsilon=O(L^{-1/2}).
$$

The upper bounds are applications of established multi-observable estimators. The contribution is the matching lower bound when the identities of future requested observables are unavailable before earlier answers are due. It accounts for information retained across rounds, preprocessing, and continued coherent source access. It does not claim a new offline estimator, a new adversary method, or the first quantum penalty associated with adaptive questions.

## Models that should be distinguished

| Literature or setting | What is available, and when? | Principal resource | Relation to this result |
|---|---|---|---|
| Offline coherent expectation estimation | A supplied list and a preparation unitary with inverse access | Source calls, with observable operations counted separately | Supplies both upper-bound schedules; does not require answering before the rest of the list is disclosed |
| Online shadow tomography | Copies of one state; later observables may depend on earlier answers | Number of copies | Has closely related answer deadlines, but lacks the coherent inverse-query resource |
| Quantum consumable data | A message encoding a sender's input; receivers request functions of that input | Communication or encoding size | Already studies serving several objectives from one quantum encoding; continued preparation queries are a different resource |
| Preprocessing advice | Preprocessing followed by a challenge, bounded advice, and later oracle queries | Advice space and postprocessing queries | Allows retained information, but the present theorem instead permits unlimited memory and charges its source-query production cost |
| Quantum online learning | A learner predicts and receives examples or feedback over time | Mistakes, loss, or regret | Feedback and a coherent oracle for one fixed unknown state are different interfaces |
| This result | Known finite menu, externally revealed batches, persistent $U,U^\dagger$ access | Total source calls before and between answers | Quantifies how the visible batch sizes determine the benefit of coherent batching |

One call to a preparation source can produce a copy. Consequently, applicable copy algorithms remain valid upper-bound competitors. A lower bound proved for copy access does not automatically apply to the stronger coherent-source model. Conversely, a source-query advantage does not by itself establish a gate-count or elapsed-time advantage. The [resource accounting](../science/resources-and-interpretation.md) makes these distinctions explicit.

## 1. Coherent estimation with a supplied list

**Huggins et al. (2022), _Nearly Optimal Quantum Algorithm for Estimating Multiple Expectation Values_.** Theorem 1 of [arXiv:2111.09283v3](https://arxiv.org/html/2111.09283v3), published in [Physical Review Letters 129, 240501](https://doi.org/10.1103/PhysRevLett.129.240501), gives $\widetilde O(\sqrt M/\epsilon)$ source calls for $M$ supplied norm-bounded observables. Its controlled-observable operations have a separate cost: that many controlled exponentials are used **per observable**. Theorem 2 and Corollary 3 give the associated high-precision lower bound, including commuting observables. These results establish the fixed-list scaling used here. Our two upper schedules either apply that estimator to each revealed batch or estimate the full known menu before answering. The lower bound must additionally prevent earlier queries and retained quantum information from eliminating the cost of later, undisclosed requests.

**van Apeldoorn et al. (2023), _Quantum tomography using state-preparation unitaries_.** Section 7.2, Theorem 37 of [arXiv:2207.08800v1](https://arxiv.org/html/2207.08800v1), published in [SODA 2023, pp. 1265–1318](https://doi.org/10.1137/1.9781611977554.ch47), supplies an overlap-sensitive alternative with source, block-encoding, and additional-gate costs. The dependence on $\|\sum_j E_j^2/\epsilon_j^2\|$ can improve some structured instances. It also contains a factor involving $\log d$, where $d$ is the state dimension; this is not uniformly harmless for a system with $L$ qubits. The [resource page](../science/resources-and-interpretation.md#3-an-alternative-with-explicit-select-and-gate-costs) records the theorem's parameters without treating a coherent SELECT operation as free.

**Wada, Yamamoto, and Yoshioka (2025), _Heisenberg-Limited Adaptive Gradient Estimation for Multiple Observables_.** The [published abstract](https://doi.org/10.1103/PRXQuantum.6.020308) gives a simultaneous-estimation algorithm for a supplied set of $M$ observables, with source complexity $O(\epsilon^{-1}\sqrt M\log M)$ for its stated root-mean-square error criterion. Here “adaptive” concerns the estimator's refinement procedure. It does not impose the externally delayed objective identities of the present model. Its error criterion should also be distinguished from a joint high-probability guarantee for every requested value.

## 2. Online and adaptive estimation from copies

**Chen, O'Donnell, Pelecanos, and Wright (2026), _Online Shadow Tomography Matching the Classical Bounds_.** Definition 1.1 of [arXiv:2607.29686v2](https://arxiv.org/html/2607.29686v2) supplies copies and then reveals observables sequentially. Its Theorem 1.2 uses

$$
n=O\!\left(\frac{\sqrt K\log(m+K)}{\epsilon^2}\right),
\qquad K=\Theta\!\left(\frac{\log d}{\epsilon^2}\right),
$$

and Theorem 1.3 gives $n=O(\sqrt m/\epsilon^2)$, with the stated joint success guarantee. This is a close predecessor for the temporal task. Its charged input consists of copies, rather than a unitary and its inverse that can be queried between answers. The distinction concerns available operations, not merely terminology.

**Huang, Lewis, Huang, and Preskill (2026), _Predicting Adaptively Chosen Observables in Quantum Systems_.** The [published paper](https://www.preskill.caltech.edu/pubs/preskill-2026-predicting.pdf), PRX Quantum 7, 010347, establishes sample penalties for adaptively selected local and Pauli observables. In the [arXiv text](https://arxiv.org/html/2410.15501v1), Theorems 1–2 give the relevant $\Omega(\sqrt M)$ dependence. Theorems 3–4 also identify easier observable classes: the stated bounds include $\widetilde O(\log M/\epsilon^4)$ copies for bounded Frobenius norm and $\widetilde O(R^2\log M/\epsilon^3)$ for rank at most $R$. Those precision factors matter. The present lower bound already uses independent random requests, so statistically adversarial selection is unnecessary for its coherent-query penalty.

**Huang, Kueng, and Preskill (2020), _Predicting Many Properties of a Quantum System from Very Few Measurements_.** [Theorem 1 and the Clifford-measurement bounds](https://arxiv.org/html/2002.08953v2) imply $O(\log(L/\delta)/\epsilon^2)$ copies for simultaneously estimating a fixed menu of $L$ observables with uniformly bounded squared Frobenius norm. That applies to the rank-two menu in the small-dimensional witness. A simultaneous guarantee for the entire known menu also covers future choices of indices from that menu. Thus delayed indices alone do not invalidate classical shadows. In the precision range of our theorem, $\epsilon^{-2}$ is at least a constant multiple of $\sqrt L/\epsilon$, so this copy strategy is consistent with the source-query lower bound.

## 3. Consumable quantum data and replenishment

**Gilboa, Jain, and McClean (2025), _Consumable Data via Quantum Communication_.** The [RANDOM 2025 proceedings paper](https://drops.dagstuhl.de/storage/00lipics/lipics-vol353-approx-random2025/html/LIPIcs.APPROX-RANDOM.2025.39/LIPIcs.APPROX-RANDOM.2025.39.html) already studies a fixed sender input serving multiple function requests. The resource is one-way communication. Section 4.3, Theorem 24 and Lemma 6, use shadow tomography to establish nonconsumability for unrestricted two-party decision and observable-estimation tasks. Their linear expectation-estimation lower bound imposes restrictions on receivers and measurements. The present protocol instead permits unrestricted joint memory and repeated access to a charged coherent source. The general idea of quantum-data consumption is therefore a predecessor, while the resource law here concerns replenishment through source queries under answer deadlines.

**Voronova (2026), _Random Order in Quantum Streaming: Replenishment and Robust Lower Bounds_.** The authoritative abstract of [arXiv:2610.06727](https://arxiv.org/abs/2610.06727) describes encoding-space lower bounds for multiple independent Hidden Matching requests, compares simultaneous and sequential revelation, and considers replenishment by classical stream updates. This is a close conceptual comparison: objective timing and replenishment are already present in that setting. The stated resource is encoding space, rather than calls to a continually available state-preparation unitary. The comparison here is limited to the abstract; the full theorem text was not available for inspection.

## 4. Preprocessing, direct products, and online learning

**Dong and Lombardi (2026), _Lower Bounds for Preprocessing Attacks on Quantum Cryptography_.** The introduction, Theorem 1.1, and Sections 2.2 and 10 of [arXiv:2610.02101v2](https://arxiv.org/html/2610.02101v2) study preprocessing, quantum advice, and later random-oracle queries. Such results are relevant to retained information and two-stage protocols. Their bounded advice and random-function interface differ from unrestricted memory produced by charged preparation-source calls. They do not directly state the $\sum_r\sqrt{b_r}$ scheduling law.

**Beame, Kornerup, and Whitmeyer (2026), _Strong Selective and List-Decoding Direct Product Theorems for Quantum Query Complexity_.** The [author-listed preprint](https://homes.cs.washington.edu/~beame/site/publications-by-year/), [arXiv:2609.26678v2](https://arxiv.org/abs/2609.26678v2), concerns independent function instances and selective or list-decoding outputs. Its abstract does not state a model in which fresh external requests interrogate one shared weak preparation source. Full-text retrieval was unavailable, so this is an abstract-level comparison, not an assertion that every theorem or proof ingredient has been ruled out as relevant.

**Beame, Holman, and Kornerup (2026), _A Noise Operator Approach to Quantum Query Complexity and Time-Space Tradeoff Lower Bounds_.** The introduction and model sections of [arXiv:2609.40334v2](https://arxiv.org/html/2609.40334v2) treat input-query problems with time-space restrictions and permit adaptive output schedules. Choosing when to emit outputs differs from receiving new externally chosen objectives. Fourier or recording perspectives are nevertheless related lower-bound tools.

**Mohan and Tewari (2025), _Quantum Learning Theory Beyond Batch Binary Classification_.** Section 5.1 of [arXiv:2302.07409v5](https://arxiv.org/html/2302.07409v5), published in [Quantum 9, 1813](https://doi.org/10.22331/q-2025-07-29-1813), defines an online learner that predicts and then receives a quantum example. The principal guarantees concern learning performance and combinatorial dimensions. The example-and-feedback interface does not already supply the charged coherent source required here.

## 5. What the lower bound adds

An offline lower bound for one supplied list cannot simply be added over rounds: a protocol may carry quantum information from every earlier query into every later answer. The proof here uses a global progress quantity to account for that retained information. A newly and independently selected batch has a progress operator whose average equals the global one. The limited change per source invocation then charges the work needed to answer each fresh batch. See the [complete lower bound](../science/lower-bound.md).

For equal batches, $T=Rb$ requested values are returned in $R$ rounds. Before full-menu saturation, the frontier is $R\sqrt b/\epsilon$. For an oblivious request list, disclosure of the whole list in advance permits the known upper bound $\widetilde O(\sqrt{Rb}/\epsilon)$. When $L\geq R^2b$ and the precision condition holds, this is a factor $\sqrt R$ separation, up to logarithms. Arbitrary memory and continued inverse-source access are allowed on both sides. The [commuting product-state witness](../science/commuting-witness.md) shows that noncommuting observables and entanglement in the prepared state are not necessary for this separation; the specified full source oracle remains essential.

The proof uses established quantum adversary ideas, including a purified input and progress under oracle calls; an early primary reference is [Ambainis, _Quantum lower bounds by quantum arguments_](https://arxiv.org/abs/quant-ph/0002066). The new claim is the operational frontier under external batch revelation, not a new general lower-bound formalism.

## Source coverage

The comparisons above identify their primary versions and theorem locations. The two explicitly marked abstract-only comparisons, Beame–Kornerup–Whitmeyer and Voronova, should not be represented as full-text reviews. This record reflects sources checked through 31 October 2026 and is not an exhaustive priority certificate. Bibliographic records are in [bibliography.bib](bibliography.bib).
