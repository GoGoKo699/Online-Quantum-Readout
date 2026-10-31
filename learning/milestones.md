# Thirty milestones for understanding online quantum readout

This map organizes the project's scientific account into exactly thirty understanding targets. It begins with a state, an observable, and a charged source call, then builds the argument that the timing of future questions changes the worst-case cost of coherent readout. The [scientific account](../science/README.md) remains the direct route to the authoritative theorem and proofs.

The sole educational anchor is Andrew M. Childs, [*Lecture Notes on Quantum Algorithms*, author PDF dated 17 April 2025](https://www.cs.umd.edu/~amchilds/qa/qa.pdf). Section and printed-page references below use that edition. The [Childs bridge](childs-bridge.md#the-selected-reading-route) translates its notation and oracle assumptions into this project's setting. Primary research results remain separately attributed in the scientific pages; in particular, the supplied-list estimator in M09 is an imported theorem of Huggins et al., not a result attributed to the lecture notes.

## Allocation and dependency structure

**M01–M12 are background/preliminaries; M13–M30 are narrative/innovation.** The twelve background targets assemble the necessary objects, access model, estimation baseline, and lower-bound framework into the complete online problem. The eighteen narrative targets give more space to this project's central argument: a local source-query rate, a global budget for previously acquired information, and a new request that connects the two. The final targets interpret the resulting frontier through the commuting witness, the easier oracle completion, and the full resource ledger.

This 12/18 allocation reflects a project that develops one connected query-complexity argument rather than joining two large prerequisite subjects. Each phase moves from individual objects and mechanisms toward a synthesis. The alternative witness near the end tests which features the global conclusion actually requires. The map covers the load-bearing ideas and limitations; specialist algebra and the full primary-literature comparison remain in the linked sources.

Dependencies identify earlier milestones. Each entry also states its role in the scientific story and the conceptual connection it makes. The phase endpoints are [M12](#m12-the-complete-online-readout-problem) and [M30](#m30-the-complete-scoped-contribution).

## Phase 1: Background and preliminaries

### M01: A state and a preparation

**Phase:** background/preliminaries.

**Central question:** What does it mean for a source to prepare an unknown quantum state from a known reference?

**Understanding target:** Distinguish a normalized state vector, its basis amplitudes, the known input state, and a unitary that maps that input to the target. Identify which information is known to the algorithm and which remains accessible only through source calls.

**Dependencies and story role:** None. This supplies the local object on which every later observable and oracle operation acts.

**Conceptual connection:** Childs's quantum-data description becomes the project's preparation promise, without supplying the target amplitudes as classical data.

**Source pointers:** [Childs §1.1, p. 1][childs-data]; [source access and the public menu](../science/model-and-theorem.md#1-source-access-and-the-public-menu); [the source-interface bridge](childs-bridge.md#from-childss-query-model-to-a-preparation-source).

### M02: An observable and its mean

**Phase:** background/preliminaries.

**Central question:** How does estimating an expectation value differ from obtaining one measurement outcome?

**Understanding target:** Interpret a Hermitian observable, its norm bound, and its expectation in the prepared state. Distinguish the random outcome of a measurement from the numerical mean to be estimated and from an additive error tolerance on that estimate.

**Dependencies and story role:** M01. This identifies the output of the readout task before considering how efficiently it can be produced.

**Conceptual connection:** The matrix norm and state-vector language support a bounded statistical quantity; the bridge supplies the measurement-to-expectation step used by this project.

**Source pointers:** [Childs §1.3, p. 2, Eq. (1.4)][childs-norm]; [observable and norm definitions in the bridge](childs-bridge.md#from-childss-query-model-to-a-preparation-source); [model §§1–2](../science/model-and-theorem.md#1-source-access-and-the-public-menu).

### M03: Overlap and distinguishability

**Phase:** background/preliminaries.

**Central question:** Why does successfully telling two hidden inputs apart constrain their final quantum-state overlap?

**Understanding target:** Explain why two nearly identical output states cannot reliably support opposite classical answers. Relate measurement success to an inner-product bound while allowing unused working registers to remain present.

**Dependencies and story role:** M01, M02. This introduces the endpoint condition needed by a lower bound on any algorithm, rather than only by a particular estimator.

**Conceptual connection:** A geometric relation between states turns a classical correctness requirement into a constraint on quantum information processing.

**Source pointers:** [Childs §23.1, p. 109, Fact 23.1][childs-superoracle]; [the project's output-overlap argument](../science/lower-bound.md#6-correct-outputs-bound-the-remaining-edge-overlap).

### M04: The complete reversible source interface

**Phase:** background/preliminaries.

**Central question:** What access is specified by a preparation unitary, its inverse, and its controlled versions?

**Understanding target:** Distinguish access to copies of a state from access to a full unitary on arbitrary inputs. Recognize that a preparation promise leaves the action on other inputs unspecified and that controlled access is an explicit allowed operation in this model.

**Dependencies and story role:** M01, M03. This fixes the local interface before drawing a speedup or lower-bound conclusion from it.

**Conceptual connection:** Childs's circuit and query descriptions provide the language for a source oracle whose whole action, not only one prepared column, can carry information.

**Source pointers:** [Childs §1.2, pp. 1–2][childs-circuits]; [Childs §§21.1–21.2, pp. 97–98][childs-query-model]; [the source-interface bridge](childs-bridge.md#from-childss-query-model-to-a-preparation-source); [the completion distinction](../science/resources-and-interpretation.md#5-a-preparation-map-does-not-specify-the-whole-oracle).

### M05: Coherent estimation of one value

**Phase:** background/preliminaries.

**Central question:** How can coherent repeated operations change the precision cost of estimating one quantity?

**Understanding target:** Explain the roles of reversible access, interference, and repeated controlled operations in phase or amplitude estimation. Distinguish their use of a source from independently preparing and measuring copies, while retaining the required known operations and their costs.

**Dependencies and story role:** M02, M04. This supplies the single-value intuition behind the coherent readout resource being studied.

**Conceptual connection:** Phase estimation and quantum counting show why the number of source invocations can scale differently from an independent-sampling count. They do not by themselves establish the multiple-observable online theorem.

**Source pointers:** [Childs §4.3, p. 19][childs-phase]; [Childs §19.3, pp. 88–89][childs-amplification]; [the estimation bridge](childs-bridge.md#from-estimation-to-an-online-contract).

### M06: Precision and simultaneous confidence

**Phase:** background/preliminaries.

**Central question:** What must be true for an entire list of numerical answers to count as accurate?

**Understanding target:** Distinguish additive precision, a single answer's success probability, joint success for all answers, and a mean-squared-error guarantee. Explain how independent repetitions and coordinatewise medians amplify a supplied-list estimator's simultaneous success.

**Dependencies and story role:** M02, M05. This makes correctness precise before several estimation tasks are combined.

**Conceptual connection:** The precision and success parameters of an estimation primitive become a transcript-wide requirement, with confidence overhead kept separate from the main source-query scaling.

**Source pointers:** [Childs §4.3, p. 19][childs-phase]; [model §2](../science/model-and-theorem.md#2-requests-deadlines-and-accuracy); [the imported estimator and its amplification](../science/upper-bounds.md#the-imported-simultaneous-estimator).

### M07: What the resource count includes

**Phase:** background/preliminaries.

**Central question:** What does a source-query bound measure, and what costs remain outside it?

**Understanding target:** Separate preparation calls from known-observable operations, circuit synthesis, coherent addressing, workspace, classical output, and elapsed time. Count preprocessing and failed attempts, and recognize that no free QRAM or unknown-data loading is provided.

**Dependencies and story role:** M04, M05, M06. This turns a local oracle invocation into an honest resource accounting for a complete task.

**Conceptual connection:** A query model isolates one expensive operation without declaring every other operation physically free in an implementation claim.

**Source pointers:** [Childs §21.1, p. 97][childs-query-model]; [the complete implementation ledger](../science/resources-and-interpretation.md#1-a-ledger-for-a-complete-implementation); [known-observable operations](../science/upper-bounds.md#known-observable-operations-remain-charged).

### M08: Retained memory and analytical purification

**Phase:** background/preliminaries.

**Central question:** How can a proof include all earlier quantum information without imposing a memory restriction?

**Understanding target:** Account for working registers, classical records, randomness, and measurement environments in an enlarged analytical state. Distinguish retaining an environment for a proof from giving the algorithm access to a system it actually discarded.

**Dependencies and story role:** M01, M03, M04. This prepares a global description that remains valid when information persists between answers.

**Conceptual connection:** Childs's inaccessible input-register perspective and a local dilation of the algorithm separate analytical bookkeeping from restrictions on its usable memory.

**Source pointers:** [Childs §23.1, p. 109][childs-superoracle]; [the record-dilation explanation in the bridge](childs-bridge.md#from-the-adversary-method-to-the-batch-frontier); [purifying the hidden input](../science/lower-bound.md#2-purifying-the-hidden-input).

### M09: The imported supplied-list estimator

**Phase:** background/preliminaries.

**Central question:** What advantage is already known when all requested observables are supplied together?

**Understanding target:** State the supplied-list interface and simultaneous guarantee of the Huggins et al. estimator, with source cost $`\widetilde O(\sqrt M/\epsilon)`$. Identify it as an imported research ingredient and keep its per-observable controlled-evolution costs separate.

**Dependencies and story role:** M04, M05, M06, M07. This establishes the prior algorithmic baseline that the online theorem will delimit.

**Conceptual connection:** The anchor's coherent-estimation foundations lead to a research-level multi-observable primitive; the latter is credited through its actual theorem rather than attributed to the anchor.

**Source pointers:** [Childs §19.3, pp. 88–89, for the coherent-estimation foundation][childs-amplification]; [Huggins's imported theorem and guarantee](../science/upper-bounds.md#the-imported-simultaneous-estimator); [primary attribution](../references/related-work.md#1-coherent-estimation-with-a-supplied-list).

### M10: A progress method for lower bounds

**Phase:** background/preliminaries.

**Central question:** How can a proof constrain every algorithm rather than analyze one chosen circuit?

**Understanding target:** Identify the initial progress value, the value forced by correct output, and the maximum change caused by one oracle call. Explain why source-independent operations can be harmless to a carefully chosen input-register progress quantity even when they are computationally complicated.

**Dependencies and story role:** M03, M04, M07, M08. This assembles the general lower-bound framework that will later account for retained information.

**Conceptual connection:** The quantum adversary method combines distinguishability with an oracle-dependent rate bound. The project's contribution uses this framework with progress operators tailored to fresh requests.

**Source pointers:** [Childs §§23.1–23.2, pp. 109–113][childs-superoracle]; [the adversary-to-frontier bridge](childs-bridge.md#from-the-adversary-method-to-the-batch-frontier).

### M11: The online reveal-and-answer contract

**Phase:** background/preliminaries.

**Central question:** What is unavailable when the whole menu is known but the next requested subset has not been revealed?

**Understanding target:** Distinguish the known menu of size $`L`$ from the currently revealed subset of predetermined size $`b_r`$. Explain the answer deadline, repeated indices across rounds, continued source access, and adaptive future requests without treating the batch sizes as adaptive.

**Dependencies and story role:** M04, M06, M07, M08, M09. This joins the access, accuracy, and information-timing rules into the actual problem.

**Conceptual connection:** An oracle-query model acquires an external information schedule. The schedule is neither a circuit-depth bound nor a demand that earlier memory be erased.

**Source pointers:** [Childs §§21.1–21.2, pp. 97–98][childs-query-model]; [requests, deadlines, and accuracy](../science/model-and-theorem.md#2-requests-deadlines-and-accuracy); [the online-contract bridge](childs-bridge.md#from-estimation-to-an-online-contract).

### M12: The complete online readout problem

**Phase:** background/preliminaries.

**Central question:** Once all the rules are combined, what is the unresolved possibility that a lower bound must exclude?

**Understanding target:** Describe the two available upper strategies—estimate each revealed batch or estimate the full known menu—and the possibility that an arbitrary memory-retaining algorithm could do better. State the high-precision, worst-case source-query scope without assuming the conclusion of the proof.

**Dependencies and story role:** M09, M10, M11. This is the background synthesis: the objects, resources, baseline, and correctness rules now form one well-defined scientific question.

**Conceptual connection:** Known coherent batching and unrestricted retained information meet a causal limitation on which objectives are available before an answer is due.

**Source pointers:** [Childs §21.1, p. 97][childs-query-model]; [the exact main theorem](../science/model-and-theorem.md#3-main-theorem); [the two schedules](../science/upper-bounds.md#what-the-two-schedules-do-and-do-not-establish).

## Phase 2: Narrative and innovation

### M13: Weak signed amplitudes as hard inputs

**Phase:** narrative/innovation.

**Central question:** How can many hidden signs be encoded so that an accurate requested mean reveals one sign?

**Understanding target:** Explain the reference amplitude and weak signed components of the star family. Connect state normalization, the choice $`s=2\epsilon\sqrt L`$, the rank-two observables, and the sign margin to the explicit condition $`0\lt\epsilon\leq1/(2\sqrt{2L})`$.

**Dependencies and story role:** M02, M06, M11. This introduces the local hard instance before any global information-budget argument.

**Conceptual connection:** An additive numerical-estimation task becomes hidden-bit recovery while its precision restriction follows from the geometry of the prepared states.

**Source pointers:** [Childs §1.1, p. 1][childs-data]; [the specified hard source and means](../science/lower-bound.md#1-a-specified-hard-source); [the four-observable example](childs-bridge.md#a-worked-four-observable-example).

### M14: The canonical swap source

**Phase:** narrative/innovation.

**Central question:** Which complete preparation unitary is used in the hard instance, and why must it be specified?

**Understanding target:** Explain how the canonical unitary swaps the known orthogonal input with the target state and fixes their orthogonal complement. Recognize its Hermitian inverse and distinguish a valid worst-case oracle from a lower bound for every circuit preparing the same state.

**Dependencies and story role:** M04, M13. This completes the local hard instance so that arbitrary-input, inverse, and controlled queries can all be analyzed.

**Conceptual connection:** The preparation promise from M01 becomes a full query interface; its completion is part of the information available to the algorithm.

**Source pointers:** [Childs §21.2, p. 98][childs-queries]; [the hard oracle definition](../science/lower-bound.md#1-a-specified-hard-source); [why a preparation map does not specify the oracle](../science/resources-and-interpretation.md#5-a-preparation-map-does-not-specify-the-whole-oracle).

### M15: Fourier occupation as information bookkeeping

**Phase:** narrative/innovation.

**Central question:** What quantity can track information about all hidden signs while allowing arbitrary retained memory?

**Understanding target:** Distinguish hidden-sign flips, multiplication by a sign, and the Fourier-occupation projectors. Explain why the initial uniform hidden-input reference has zero occupation and why the proof's reference register is not an extra physical input or a memory restriction on the algorithm.

**Dependencies and story role:** M08, M10, M14. This introduces the common bookkeeping space from which both global and batch-specific progress are constructed.

**Conceptual connection:** The superoracle and recording perspectives motivate the analysis; the actual source remains the specified preparation oracle, not the random-function oracle of the compressed-oracle chapter.

**Source pointers:** [Childs §23.1, p. 109][childs-superoracle]; [Childs §26.1, pp. 125–126, as a related recording perspective][childs-compressed]; [the project's input purification and occupation operators](../science/lower-bound.md#2-purifying-the-hidden-input).

### M16: The cost of changing a batch's progress

**Phase:** narrative/innovation.

**Central question:** Why does the one-call rate depend on the square root of the revealed batch size?

**Understanding target:** Explain how orthogonal physical labels make the squared norm of the isometry commutator add across requested coordinates. Follow that rate through the canonical source and the normalization of the batch progress operator, including inverse and controlled calls.

**Dependencies and story role:** M14, M15. This establishes the local quantitative bottleneck that will later be summed over rounds.

**Conceptual connection:** The adversary method's one-query change is determined by the geometry of this preparation source. It is not obtained by charging independent bits one at a time.

**Source pointers:** [Childs §23.2, pp. 110–113][childs-adversary]; [the exact source commutator bounds](../science/lower-bound.md#3-exact-commutator-bounds-for-a-source-call).

### M17: Charge an invocation, not a control amplitude

**Phase:** narrative/innovation.

**Central question:** How can input-dependent stopping be included without making coherent oracle calls fractionally free?

**Understanding target:** Distinguish an outer classical decision to invoke the source from a coherent control inside an invocation. Explain why the progress change is bounded by the rate times the probability of an actual invocation, while every executed controlled source call still costs one whole query.

**Dependencies and story role:** M04, M07, M08, M16. This turns the local rate into a charge that is valid for adaptive classical branches.

**Conceptual connection:** A commuting active-flag projector connects operator-norm progress bounds to expected physical query counts; it does not introduce an amplitude-weighted resource convention.

**Source pointers:** [Childs §21.2, p. 98, for the query interface][childs-queries]; [expected calls and classical stopping](../science/lower-bound.md#4-expected-calls-and-classical-stopping).

### M18: The global budget before a request

**Phase:** narrative/innovation.

**Central question:** How much progress about the whole hidden input can all earlier source calls have produced?

**Understanding target:** Use the full-coordinate occupation rate to bound the expected occupation before a reveal by the number of earlier paid calls. Include preprocessing, retained records, and unsuccessful attempts; do not require occupation to increase monotonically at every call.

**Dependencies and story role:** M15, M16, M17. This converts local query rates into a global constraint on everything already learned.

**Conceptual connection:** Unlimited memory can retain earlier information, but producing that information through this oracle still consumes the charged source resource.

**Source pointers:** [Childs §23.2, pp. 110–113][childs-adversary]; [the prefix occupation budget](../science/lower-bound.md#4-expected-calls-and-classical-stopping).

### M19: A fresh subset links local and global progress

**Phase:** narrative/innovation.

**Central question:** Why does an independently revealed subset expose a remaining deficit even when the entire earlier state is retained?

**Understanding target:** Explain the averaging identity that turns a fresh subset's progress into the full-coordinate progress. Distinguish independence of the next subset from the prefix from the false assumption that the hidden input remains uniform after conditioning on an observed transcript.

**Dependencies and story role:** M11, M15, M18. This is the central link between the information already available and the next batch's local bottleneck.

**Conceptual connection:** Fresh objective identities, rather than memory loss or adversarial statistical selection, make the same global budget relevant at successive answer deadlines. Overlap between different batches is allowed.

**Source pointers:** [Childs §23.2, pp. 110–113, for the progress framework][childs-adversary]; [fresh-subset averaging](../science/lower-bound.md#5-the-next-subset-is-independent-of-the-entire-prefix); [the adversary-to-frontier bridge](childs-bridge.md#from-the-adversary-method-to-the-batch-frontier).

### M20: Correct answers force an overlap decrease

**Phase:** narrative/innovation.

**Central question:** What endpoint does the algorithm have to reach to answer the currently requested signs correctly?

**Understanding target:** Pair inputs differing in one requested sign and connect the two possible output records to their state overlap. Explain why per-round average sign error at most one third yields the bound $`2\sqrt2/3`$, even with all earlier memory and environments retained.

**Dependencies and story role:** M03, M06, M13, M15. This supplies the correctness endpoint that makes the local query-rate bound operational.

**Conceptual connection:** Childs's distinguishability premise becomes an averaged edge-overlap condition for a requested batch. It is not replaced by an average error over unequally weighted rounds.

**Source pointers:** [Childs §23.1, p. 109, Fact 23.1][childs-superoracle]; [correct outputs and edge overlap](../science/lower-bound.md#6-correct-outputs-bound-the-remaining-edge-overlap).

### M21: The one-round cost inequality

**Phase:** narrative/innovation.

**Central question:** How can previous learning and new queries jointly pay for one batch's required progress?

**Understanding target:** Combine the initial progress from the prefix budget, the endpoint forced by accuracy, and the within-round rate. Explain the resulting tradeoff between prior source work and current calls, including why a sufficiently large prefix can remove a particular round's positive new-work requirement.

**Dependencies and story role:** M16, M17, M18, M19, M20. This assembles the local ingredients into the complete inequality for one deadline.

**Conceptual connection:** The lower bound charges retained information through its production cost instead of pretending that each round begins from scratch.

**Source pointers:** [Childs §23.2, pp. 110–113][childs-adversary]; [the first inequality in the round-cost summation](../science/lower-bound.md#7-sum-the-round-costs).

### M22: Summation and whole-menu saturation

**Phase:** narrative/innovation.

**Central question:** Why does summing the round inequalities produce both a batch-size sum and a saturation scale?

**Understanding target:** Explain the weighting by square roots of the predetermined batch sizes and the use of disjoint query intervals. Interpret $`A/(1+A/\sqrt L)`$, where $`A=\sum_r\sqrt{b_r}`$, as equivalent within constants to the smaller of the per-batch sum and the full-menu scale.

**Dependencies and story role:** M12, M21. This is the first global synthesis of the lower-bound mechanism across the entire protocol.

**Conceptual connection:** The same retained information that prevents a naive independent-round direct sum explains the denominator and the option of learning the menu globally.

**Source pointers:** [Childs §23.2, pp. 110–113, for the lower-bound framework][childs-adversary]; [the complete summation](../science/lower-bound.md#7-sum-the-round-costs); [the exact theorem](../science/model-and-theorem.md#3-main-theorem).

### M23: Finite expected cost without a fixed cap

**Phase:** narrative/innovation.

**Central question:** Why does the bound survive when an algorithm has finite expected query cost but no fixed maximum number of calls?

**Understanding target:** Explain truncation before invocation number $`n+1`$, the resulting error increase bounded by $`Q/(n+1)`$, and the limit that restores the original correctness constant. Keep almost-sure completion and actual expected invocations distinct from a fixed execution cap.

**Dependencies and story role:** M06, M17, M22. This closes the stopping-time scope of the global lower bound rather than changing its resource convention.

**Conceptual connection:** A controlled finite approximation transfers a bounded-query argument to expected cost without granting free postselection or requiring a uniform tail bound for every hidden input.

**Source pointers:** [Childs §21.1, p. 97, for query-complexity accounting][childs-query-model]; [removing the finite query cap](../science/lower-bound.md#8-remove-the-finite-query-cap); [the two cost conventions](../science/model-and-theorem.md#2-requests-deadlines-and-accuracy).

### M24: Matching schedules and adaptive confidence

**Phase:** narrative/innovation.

**Central question:** How do established batch estimators attain the lower frontier even when future requests depend on previous answers?

**Understanding target:** Explain the fresh conditional success guarantee for each revealed batch and the single simultaneous-success event for whole-menu estimation. Use the publicly fixed sizes to choose the cheaper schedule, while recognizing that the estimation primitive is inherited.

**Dependencies and story role:** M06, M09, M11, M22. This joins the lower bound to its constructive upper endpoints and establishes the complete source-query law.

**Conceptual connection:** Confidence allocation and a uniform event over the known menu make the offline primitive compatible with online decisions; no independence between adaptive requests and earlier estimation errors is assumed.

**Source pointers:** [Childs §19.3, pp. 88–89, for the coherent-estimation foundation][childs-amplification]; [answer each current batch](../science/upper-bounds.md#answer-each-current-batch); [read the whole menu once](../science/upper-bounds.md#read-the-whole-known-menu-once).

### M25: Compare timing on the same requests

**Phase:** narrative/innovation.

**Central question:** How can the cost of delayed objective identities be compared without changing the task being answered?

**Understanding target:** Compare a fixed or obliviously sampled request list disclosed all at once with the same request distribution disclosed one batch at a time. Preserve the menu-size and precision conditions, and explain why an adaptive interaction cannot simply be identified with its retrospectively realized list.

**Dependencies and story role:** M22, M23, M24. This turns the frontier into a concrete global statement about information timing.

**Conceptual connection:** The compatible example $`L=T^2`$, $`\epsilon=1/(4T)`$ makes the online and offline source-count scales comparable while staying inside the proved regime. It does not imply the same separation at fixed precision.

**Source pointers:** [Childs §21.1, p. 97][childs-query-model]; [the fixed-request comparison and example](../science/upper-bounds.md#compare-deadlines-while-holding-the-request-count-fixed); [consequences of the scheduling law](../science/model-and-theorem.md#5-consequences-of-the-scheduling-law).

### M26: What a commuting product witness establishes

**Phase:** narrative/innovation.

**Central question:** Are noncommuting observables or entanglement in the prepared state necessary for the lower-bound phenomenon?

**Understanding target:** Describe the weakly tilted product-state family and its commuting one-qubit Pauli observables. Account for the physical flag qubit, distinguish the resulting $`L+1`$-qubit source from the logarithmic-width star source, and retain the specified canonical completion.

**Dependencies and story role:** M02, M13, M14, M22. This tests the physical interpretation of the globally established law through an alternative witness.

**Conceptual connection:** A change in prepared-state and measurement structure isolates what the lower bound does not require, without assuming that the full preparation unitary is local.

**Source pointers:** [Childs §1.1, p. 1][childs-data]; [the product states, observables, and flag](../science/commuting-witness.md#1-product-states-physical-qubits-and-the-oracle-completion); [comparison of the two witnesses](../science/resources-and-interpretation.md#4-what-the-two-hard-witnesses-show).

### M27: Why the commuting witness has the same rate

**Phase:** narrative/innovation.

**Central question:** What replaces the star family's orthogonal-label calculation for the product-state source?

**Understanding target:** For a batch of size $`b`$, interpret the product amplitudes as Bernoulli weights with $`p=4\epsilon^2`$ and explain the variance-plus-squared-mean expression $`bp(1-p)+b^2p^2`$ for the squared commutator norm. Connect the bounded correction factor to the same high-precision regime and the same asymptotic online frontier.

**Dependencies and story role:** M15, M16, M22, M26. This supplies the quantitative justification for the alternative witness's interpretive role.

**Conceptual connection:** The geometry of a different prepared-state family changes the local rate by a bounded factor while leaving the global fresh-request argument intact.

**Source pointers:** [Childs §23.2, pp. 110–113, for the rate-bound framework][childs-adversary]; [the exact Fourier calculation](../science/commuting-witness.md#2-exact-fourier-occupation-calculation); [rates](../science/commuting-witness.md#3-source-query-rates) and [resulting lower bound](../science/commuting-witness.md#4-resulting-online-lower-bound).

### M28: The easier completion of the same states

**Phase:** narrative/innovation.

**Central question:** Why can another unitary preparing exactly the same product states make all the signs easier to learn?

**Understanding target:** Explain how repeated calls to the natural product-rotation completion amplify all weak rotations simultaneously. Reconcile its nearly inverse-precision source cost with the canonical-swap lower bound by identifying which full-oracle behavior changed.

**Dependencies and story role:** M04, M14, M26, M27. This establishes the most important oracle-quantifier limitation of the global result.

**Conceptual connection:** Repeated coherent access depends on the complete unitary, not solely on its output from the reference state. The explicit easier completion prevents a worst-case theorem from becoming an assertion about every preparation circuit.

**Source pointers:** [Childs §4.3, p. 19, for repeated coherent unitary access][childs-phase]; [the natural-rotation calculation](../science/commuting-witness.md#5-why-the-oracle-completion-must-be-specified); [the full-oracle distinction](../science/resources-and-interpretation.md#5-a-preparation-map-does-not-specify-the-whole-oracle).

### M29: Full costs and copy-based comparators

**Phase:** narrative/innovation.

**Central question:** What survives when the source-query law is compared with a complete implementation and with reusable classical estimates?

**Understanding target:** Include the known-observable primitives, SELECT construction where used, auxiliary gates, output size, and state-preparation cost. Explain why whole-menu copy strategies remain valid competitors and why their inverse-square precision dependence does not contradict the high-precision coherent frontier.

**Dependencies and story role:** M07, M09, M24, M25, M28. This combines the mathematical result with its operational accounting and strongest elementary alternatives.

**Conceptual connection:** A reduction in expensive source invocations can matter without establishing optimal gate complexity, and a reusable classical record can coexist with a lower bound on the coherent queries needed to create it.

**Source pointers:** [Childs §21.1, p. 97][childs-query-model]; [resource ledger §§1–3](../science/resources-and-interpretation.md#1-a-ledger-for-a-complete-implementation); [copy strategies](../science/resources-and-interpretation.md#6-copy-strategies-remain-meaningful-comparators); [copy-access research comparisons](../references/related-work.md#2-online-and-adaptive-estimation-from-copies).

### M30: The complete scoped contribution

**Phase:** narrative/innovation.

**Central question:** What does the completed theorem establish about the value of knowing future objectives, and where does that conclusion stop?

**Understanding target:** Explain the matching source-query frontier as a whole, identify the inherited estimator and the online lower-bound contribution, and retain all consequential qualifications: known finite menu, predetermined sizes, high precision, full-oracle minimax scope, unrestricted memory, continued source access, and separately charged implementation costs.

**Dependencies and story role:** M12, M22, M23, M24, M25, M27, M28, M29. This is the narrative synthesis, connecting the proof, its witnesses, its comparison, and its limits into one scientific account.

**Conceptual connection:** Future objective availability is a resource in the specified coherent-source model. The theorem does not turn it into a memory bound, a universal statement about local preparation circuits, a constant-precision law, or an end-to-end runtime separation.

**Source pointers:** [Childs §23.2, pp. 110–113, for the underlying lower-bound framework][childs-adversary]; [the main theorem](../science/model-and-theorem.md#3-main-theorem) and [its scope](../science/model-and-theorem.md#6-scope-of-the-theorem); [what the lower bound adds](../references/related-work.md#5-what-the-lower-bound-adds); [research dependencies and further source detail](childs-bridge.md#research-dependencies-and-what-remains-to-be-read).

[childs-data]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=9
[childs-circuits]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=9
[childs-norm]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=10
[childs-phase]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=27
[childs-amplification]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=96
[childs-query-model]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=105
[childs-queries]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=106
[childs-superoracle]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=117
[childs-adversary]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=118
[childs-compressed]: https://www.cs.umd.edu/~amchilds/qa/qa.pdf#page=133
