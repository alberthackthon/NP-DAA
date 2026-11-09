# create_data.py
# Extract the 32 questions from the PDF OCR and prepare full question bank

PDF_32_QUESTIONS = [
    {
        "id": "pdf-1",
        "topic": "amortized",
        "topic_name": "Amortized Analysis",
        "paper": "Autumn End Sem 2024",
        "paper_tag": "Aut-2024",
        "q": "Q1(h)",
        "marks": 1,
        "type": "mcq",
        "question": "Which of these is NOT used for amortized analysis: accounting, potential function, sorting, aggregate?",
        "short_answer": "Sorting. The three methods are aggregate, accounting, and potential. (Ch 1)",
        "full_solution": """1. The three standard methods for amortized analysis in algorithms (CLRS Chapter 17) are:
   - Aggregate analysis: determine total cost T(n) for a sequence of n operations, then divide by n (T(n)/n).
   - Accounting method: assign different amortized charges to operations; unused credit pays for later expensive operations.
   - Potential method: associate an overall potential energy Φ with the data structure.
2. 'Sorting' is an algorithmic problem / technique, NOT a method of amortized analysis.
Correct answer: Sorting."""
    },
    {
        "id": "pdf-2",
        "topic": "amortized",
        "topic_name": "Amortized Analysis",
        "paper": "Autumn End Sem 2024",
        "paper_tag": "Aut-2024",
        "q": "Q5(b)",
        "marks": 5,
        "type": "numerical",
        "question": "Suppose we perform a sequence of n operations on a data structure in which the i-th operation costs i if i is an exact power of 2, and 1 otherwise. Use aggregate analysis or the accounting method to determine the amortized cost per operation.",
        "short_answer": "Total ≤ n + (1+2+4+...+2^k) < 3n → amortized cost ≤ 3 = O(1). (Ch 1)",
        "full_solution": """Method: Aggregate Analysis
1. Actual cost of operation i:
   - c(i) = i, if i = 2^k for integer k ≥ 0 (expensive operation)
   - c(i) = 1, otherwise (cheap operation)
2. In a sequence of n operations:
   - Total cost of all operations that are powers of 2:
     Sum = 1 + 2 + 4 + 8 + ... + 2^m, where 2^m ≤ n.
     Using the geometric progression sum formula: Sum = 2^(m+1) - 1 < 2n.
   - Total cost of all other operations:
     There are at most n operations, each costing at most 1, so their total is at most n.
3. Total cost T(n):
   T(n) < 2n + n = 3n.
4. Amortized cost per operation:
   T(n) / n < 3n / n = 3 = O(1).
Conclusion: The amortized cost per operation is O(1)."""
    },
    {
        "id": "pdf-3",
        "topic": "amortized",
        "topic_name": "Amortized Analysis",
        "paper": "Autumn End Sem 2024",
        "paper_tag": "Aut-2024",
        "q": "Q6(a)",
        "marks": 5,
        "type": "numerical",
        "question": "Syambahadur keeps an array to track customer purchases. Initially the array is empty. He doubles the size of the array whenever there is no more space. Each product costs Rs 5 and a customer buys one item at a time; out of Rs 5, Rs 2 is used to make an entry in the array and Rs 3 is reserved in a fund to copy previous data when the size is doubled. Calculate the amortized time complexity by showing detailed working.",
        "short_answer": "Each insert is charged 5 (2 actual + 3 saved); saved 3 pays for all copying → amortized O(1) per insertion, total O(n). (Ch 1)",
        "full_solution": """Method: Accounting Method
1. Problem analysis:
   - When the array has capacity s and is full, an insertion triggers array doubling to size 2s.
   - Cost of ordinary insertion = Rs 2 (writing the entry into the new slot).
   - Cost of table expansion = copying s existing elements to the new larger array, which takes s copy steps.
2. Credit assignment:
   - Syambahadur collects Rs 5 for each insertion.
   - Rs 2 pays for the immediate insertion itself.
   - Rs 3 is stored as credit in the bank fund for that newly inserted element.
3. Invariant proof (bank never goes negative):
   - The array was previously doubled from size s/2 to s.
   - Between size s/2 and size s, exactly s - s/2 = s/2 new items were inserted.
   - Each of these s/2 new items contributed Rs 3 to the fund.
   - Total accumulated credit = (s/2) × 3 = 1.5s ≥ s.
   - Since the cost of copying all s elements is s, the accumulated fund of 1.5s is strictly greater than the copy cost s.
   - Hence, the bank balance remains non-negative at all times.
4. Conclusion:
   - Amortized cost per insertion = Rs 5 = O(1).
   - Total cost of n insertions ≤ 5n = O(n)."""
    },
    {
        "id": "pdf-4",
        "topic": "amortized",
        "topic_name": "Amortized Analysis",
        "paper": "Autumn End Sem 2025",
        "paper_tag": "Aut-2025",
        "q": "Q3(a)+(b)",
        "marks": 10,
        "type": "numerical",
        "question": "Array A of size n. Push one-digit numbers in order into positions 1 to n. When pushing digit d to position i = 2^k (k ≥ 1), also update all earlier entries: A[p] ← 10·A[p] + d for p = i-1 down to 1. Find the amortized cost per operation by aggregate or accounting method.",
        "short_answer": "Updates cost i-1 only at i = 2, 4, 8...; total < n + 2n = 3n → amortized O(1). (Ch 1)",
        "full_solution": """1. Actual cost per operation:
   - If i is NOT a power of 2: writing digit d into A[i] costs 1.
   - If i = 2^k (k ≥ 1): writing A[i] costs 1, plus (i - 1) updates for p = 1 to i-1.
     Total cost for operation i = 1 + (i - 1) = i.
2. Aggregate Method Analysis:
   - Total cost of n operations:
     T(n) = (sum of write costs for all n elements) + (sum of updates at i = 2, 4, 8, ..., 2^m ≤ n)
     T(n) = n + Σ (2^k - 1) for 2^k ≤ n
     Since Σ 2^k for k=1 to m is 2^(m+1) - 2 < 2n:
     T(n) < n + 2n = 3n.
3. Amortized cost:
   T(n) / n < 3n / n = 3 = O(1) per operation.
4. Accounting Method (Alternative):
   - Charge an amortized fee of 3 per push.
   - 1 pays for the immediate push into A[i].
   - 2 is saved as credit. Between powers of 2 (i/2 pushes), the saved credit is 2 × (i/2) = i coins, which pays for the (i - 1) updates when reaching 2^k. Credit never drops below zero.
Conclusion: Amortized cost is O(1) per operation."""
    },
    {
        "id": "pdf-5",
        "topic": "amortized",
        "topic_name": "Amortized Analysis",
        "paper": "Autumn End Sem 2012",
        "paper_tag": "Aut-2012",
        "q": "Q1(i)",
        "marks": 1,
        "type": "mcq",
        "question": "Linked-list disjoint sets with weighted-union: a sequence of n MAKE-SET, UNION, FIND-SET operations takes...",
        "short_answer": "O(n log n) in total (each element is moved at most log n times). (Ch 1)",
        "full_solution": """In linked-list representation of disjoint sets with weighted-union heuristic:
- The smaller list is always appended to the larger list.
- Each time an element's pointer is updated, the size of the set containing it at least doubles.
- For a set of size at most n, an element's representative pointer can be updated at most ⌊log₂ n⌋ times.
- Therefore, for n operations, the total time spent updating pointers across all unions is O(n log n).
Correct answer: O(n log n)."""
    },
    {
        "id": "pdf-6",
        "topic": "randomized",
        "topic_name": "Randomized Algorithms",
        "paper": "Autumn End Sem 2024",
        "paper_tag": "Aut-2024",
        "q": "Q1(i)",
        "marks": 1,
        "type": "theory",
        "question": "Differentiate between Las Vegas and Monte Carlo algorithms with examples.",
        "short_answer": "LV: always correct, running time random (randomized quicksort). MC: fixed time, answer may be wrong with small probability (Miller-Rabin, pi estimation). (Ch 2)",
        "full_solution": """Comparison:
1. Las Vegas Algorithm:
   - Output correctness: ALWAYS terminates with the correct result.
   - Running time: Random variable depending on internal coin tosses (we analyze expected running time).
   - If unlucky: Algorithm takes more time / iterations, but never produces a wrong answer.
   - Examples: Randomized Quicksort, Randomized Selection (Quickselect).
2. Monte Carlo Algorithm:
   - Output correctness: May produce an incorrect result with small bounded probability ε ≤ 1/2.
   - Running time: Deterministic / bounded time (runs in fixed time).
   - If unlucky: May return an incorrect output; error probability is reduced by running k independent trials (shrinks to ε^k).
   - Examples: Miller-Rabin Primality Test, Karger's Min-Cut, Monte Carlo π estimation."""
    },
    {
        "id": "pdf-7",
        "topic": "randomized",
        "topic_name": "Randomized Algorithms",
        "paper": "Autumn End Sem 2025",
        "paper_tag": "Aut-2025",
        "q": "Q1(b)",
        "marks": 1,
        "type": "mcq",
        "question": "Which of the algorithm uses the random input to reduce the expected running time or memory usage, but always terminates with a correct result in a bounded amount of time?",
        "short_answer": "Las Vegas Algorithm. (Ch 2)",
        "full_solution": """By definition:
- Las Vegas algorithms use random choices to guarantee expected polynomial or efficient time while ensuring the result is ALWAYS 100% correct upon termination.
- Monte Carlo algorithms have bounded time but allow a small probability of error.
Correct answer: Las Vegas Algorithm."""
    },
    {
        "id": "pdf-8",
        "topic": "randomized",
        "topic_name": "Randomized Algorithms",
        "paper": "Spring End Sem 2024",
        "paper_tag": "Spr-2024",
        "q": "Q3(b)",
        "marks": 5,
        "type": "derivation",
        "question": "Write a Quick-Sort algorithm that randomly selects an element as pivot and derive the time complexity of this algorithm.",
        "short_answer": "Expected O(n log n) (≈ 2n ln n comparisons); worst case O(n²) with tiny probability. (Ch 2)",
        "full_solution": """1. Algorithm:
RAND-QUICKSORT(A, p, r)
  if p < r
    i = RANDOM(p, r)
    swap A[i] with A[r]
    q = PARTITION(A, p, r)
    RAND-QUICKSORT(A, p, q - 1)
    RAND-QUICKSORT(A, q + 1, r)

2. Mathematical Derivation of Expected Time:
- The random pivot choice makes all ranks k ∈ {1, 2, ..., n} equally likely with probability 1/n.
- If pivot has rank k, partitions have sizes k - 1 and n - k, with partition taking O(n) = cn work.
- Expected recurrence:
  E[T(n)] = (1/n) * Σ_{k=1}^n (E[T(k - 1)] + E[T(n - k)]) + cn
          = (2/n) * Σ_{k=0}^{n-1} E[T(k)] + cn
- Multiply by n: n E[T(n)] = 2 Σ E[T(k)] + cn²
- Subtract (n-1) E[T(n-1)]:
  n E[T(n)] - (n-1) E[T(n-1)] = 2 E[T(n-1)] + 2cn
  n E[T(n)] = (n+1) E[T(n-1)] + 2cn
- Divide by n(n+1):
  E[T(n)] / (n+1) = E[T(n-1)] / n + 2c / (n+1)
- Telescoping sum gives:
  E[T(n)] / (n+1) = 2c * Σ_{i=2}^{n+1} (1/i) = 2c * (H_{n+1} - 1) ≈ 2c ln n
- Therefore:
  E[T(n)] = 2c(n+1) ln n = O(n log n).
  In comparisons: E[comparisons] ≈ 2n ln n ≈ 1.39 n log₂ n."""
    },
    {
        "id": "pdf-9",
        "topic": "randomized",
        "topic_name": "Randomized Algorithms",
        "paper": "Autumn End Sem 2024",
        "paper_tag": "Aut-2024",
        "q": "Q6(b)",
        "marks": 5,
        "type": "derivation",
        "question": "Ramesh always picks the last element as pivot, Suresh picks any element at random. Whose algorithm has the lesser worst-case complexity? Prove.",
        "short_answer": "Neither: both are O(n²) in the worst case. Random pivot improves expected time, not the worst case. (Ch 2)",
        "full_solution": """Answer: NEITHER! Both algorithms have identical worst-case time complexity of Θ(n²).

Proof:
1. Ramesh (Deterministic Last-Element Pivot):
   - On an already sorted input (e.g., [1, 2, 3, ..., n]), the last element is always the maximum.
   - PARTITION always splits into subproblems of size n - 1 and 0.
   - Recurrence: T(n) = T(n - 1) + (n - 1)
   - T(n) = Σ_{i=1}^{n-1} i = n(n - 1)/2 = Θ(n²).
2. Suresh (Random Pivot Selection):
   - In Suresh's algorithm, a random pivot is chosen at each recursive step.
   - There exists a non-zero probability sequence of coin tosses where the random choice happens to pick the maximum or minimum element at EVERY SINGLE level!
   - Under that unfortunate random sequence, Suresh's partition sizes are also (n - 1) and 0 at each level.
   - Thus, Suresh's worst-case recurrence is also T(n) = T(n - 1) + Θ(n) = Θ(n²).
3. The Critical Distinction:
   - For Ramesh, an adversary can easily construct a fixed input (e.g. sorted array) that forces the Θ(n²) worst case 100% of the time.
   - For Suresh, no fixed input can force the worst case. The probability of hitting that worst case is 2^(n-1) / n! (which for n = 60 is ≈ 10^(-62)).
   - Randomization eliminates bad input instances and makes expected time O(n log n) for EVERY input, but it DOES NOT alter the mathematical worst-case upper bound of Θ(n²).
Conclusion: Neither has lesser worst-case complexity. Both are Θ(n²)."""
    },
    {
        "id": "pdf-10",
        "topic": "complexity",
        "topic_name": "P, NP, NP-Hard, NP-Complete",
        "paper": "Autumn End Sem 2012",
        "paper_tag": "Aut-2012",
        "q": "Q7(a)",
        "marks": 5,
        "type": "theory",
        "question": "Define P, NP and NPC classes of problems.",
        "short_answer": "P = solvable in poly time deterministically. NP = verifiable in poly time with certificate. NPC = NP ∩ NP-hard. (Ch 4)",
        "full_solution": """1. Class P:
   The class of all decision problems that can be SOLVED in polynomial time by a deterministic Turing machine (deterministic algorithm).
   Examples: Shortest Path (Dijkstra), Minimum Spanning Tree (Kruskal/Prim), Sorting, 2-SAT.
2. Class NP (Nondeterministic Polynomial Time):
   The class of all decision problems for which a YES-instance can be VERIFIED in polynomial time by a deterministic algorithm, given a polynomial-length certificate (proof).
   Equivalently: solvable in polynomial time on a non-deterministic Turing machine.
   Examples: 3-SAT, Clique, Vertex Cover, Hamiltonian Cycle, Decision TSP. P ⊆ NP.
3. Class NP-Complete (NPC):
   The set of the hardest problems in NP. A problem X is NP-complete if:
   (i) X ∈ NP, AND
   (ii) X is NP-hard (every problem L in NP reduces to X in polynomial time: L ≤p X).
   Examples: SAT, 3-SAT, Clique, Vertex Cover, TSP (decision version)."""
    },
    {
        "id": "pdf-11",
        "topic": "complexity",
        "topic_name": "P, NP, NP-Hard, NP-Complete",
        "paper": "Spring End Sem 2018",
        "paper_tag": "Spr-2018",
        "q": "Q1(j)",
        "marks": 2,
        "type": "mcq",
        "question": "Which of these are NP-complete: matrix-chain multiplication, MST, circuit satisfiability, binary knapsack, TSP, median finding?",
        "short_answer": "Circuit-SAT, binary (0/1) knapsack and TSP. The others are in P. (Ch 4)",
        "full_solution": """Classification:
- In P (solvable in deterministic polynomial time):
  1. Matrix-Chain Multiplication: O(n³) using Dynamic Programming.
  2. Minimum Spanning Tree (MST): O(E log V) using Kruskal / Prim.
  3. Median Finding: O(n) deterministic using Median-of-Medians.
- NP-Complete (decision versions):
  1. Circuit Satisfiability (Cook's foundational NPC problem).
  2. Binary (0/1) Knapsack decision problem (weakly NP-complete via subset sum reduction).
  3. Travelling Salesperson Problem (TSP) decision version.
Answer: Circuit Satisfiability, Binary Knapsack, and TSP."""
    },
    {
        "id": "pdf-12",
        "topic": "complexity",
        "topic_name": "P, NP, NP-Hard, NP-Complete",
        "paper": "Spring End Sem 2018",
        "paper_tag": "Spr-2018",
        "q": "Q8(b)",
        "marks": 3,
        "type": "theory",
        "question": "Define the classes P and NP. Mention one problem that belongs to NP but not to P.",
        "short_answer": "P = poly solvable; NP = poly verifiable. State: TSP / Clique is in NP and not known to be in P (in NP \\ P assuming P ≠ NP). (Ch 4)",
        "full_solution": """1. Definitions:
   - P: Decision problems solvable in polynomial time O(n^k) by a deterministic algorithm.
   - NP: Decision problems verifiable in polynomial time given a certificate.
2. Problem in NP but not in P:
   - Strictly, whether any problem exists in NP \\ P is mathematically equivalent to the millennium prize problem P ≠ NP, which remains unproven.
   - However, assuming P ≠ NP (the standard consensus in computer science), any NP-complete problem belongs to NP but not to P.
   - Standard exam answer: The Decision Travelling Salesperson Problem (or 3-SAT, Clique, Hamiltonian Cycle) belongs to NP and has no known polynomial-time algorithm; hence it belongs to NP \\ P assuming P ≠ NP."""
    },
    {
        "id": "pdf-13",
        "topic": "complexity",
        "topic_name": "P, NP, NP-Hard, NP-Complete",
        "paper": "Spring Sem Exam 2021",
        "paper_tag": "Spr-2021",
        "q": "QMCQ 7",
        "marks": 1,
        "type": "mcq",
        "question": "S is NPC; Q and R are not known to be in NP; Q ≤p S and S ≤p R. Which is true?",
        "short_answer": "R is NP-hard. (Ch 4)",
        "full_solution": """Analysis of relations:
1. S is NP-complete. By definition, S is NP-hard and S ∈ NP.
2. We are given S ≤p R:
   - A known NP-hard problem S reduces in polynomial time to R.
   - Therefore, R is at least as hard as S. Since every problem in NP reduces to S, and S reduces to R, every problem in NP reduces to R.
   - Hence, R is NP-hard. (R is not known to be in NP, so we cannot claim R is NPC).
3. We are given Q ≤p S:
   - Q reduces to an NP problem S. This implies Q ∈ NP. However, we cannot claim Q is NP-complete because we don't know if S ≤p Q.
Correct answer: R is NP-hard."""
    },
    {
        "id": "pdf-14",
        "topic": "complexity",
        "topic_name": "P, NP, NP-Hard, NP-Complete",
        "paper": "Spring Sem Exam 2021",
        "paper_tag": "Spr-2021",
        "q": "QMCQ 8",
        "marks": 1,
        "type": "mcq",
        "question": "X ∈ NP. Which is TRUE? (no poly algorithm / if solvable in poly time then P=NP / if X is NP-hard it is NPC / X may be undecidable)",
        "short_answer": "If X is NP-hard then it is NP-complete (X is already in NP). (Ch 4)",
        "full_solution": """By definition:
- NP-complete is the intersection: NPC = NP ∩ NP-hard.
- Since we are already given that X ∈ NP, if X is also NP-hard, then by definition X satisfies both conditions and must be NP-complete.
- The statement 'if X is NP-hard it is NPC' is unconditionally TRUE.
- 'No poly algorithm' is false (problems in P are in NP and have poly algorithms).
- 'If solvable in poly time then P=NP' is false (sorting is in NP and in P, but does not imply P=NP).
- 'X may be undecidable' is false (every problem in NP is decidable in exponential time).
Correct answer: If X is NP-hard then it is NP-complete."""
    },
    {
        "id": "pdf-15",
        "topic": "complexity",
        "topic_name": "P, NP, NP-Hard, NP-Complete",
        "paper": "Spring Sem Exam 2021",
        "paper_tag": "Spr-2021",
        "q": "QMCQ 9",
        "marks": 1,
        "type": "mcq",
        "question": "Cycle in an undirected graph is in P; in NP; an NPC problem has a non-deterministic poly algorithm. Which are TRUE?",
        "short_answer": "All three (1, 2, 3). (Ch 4)",
        "full_solution": """Evaluating each statement:
1. 'Cycle in an undirected graph is in P': TRUE. A simple cycle can be detected in O(V + E) time using BFS or DFS (detecting a back-edge).
2. 'Cycle in an undirected graph is in NP': TRUE. Since P ⊆ NP, any problem in P is automatically in NP.
3. 'An NPC problem has a non-deterministic polynomial algorithm': TRUE. By definition, NPC ⊆ NP, and NP is the exact class of problems solvable in polynomial time on a non-deterministic machine.
All three statements are TRUE."""
    },
    {
        "id": "pdf-16",
        "topic": "complexity",
        "topic_name": "P, NP, NP-Hard, NP-Complete",
        "paper": "Spring Sem Exam 2021",
        "paper_tag": "Spr-2021",
        "q": "QMCQ 10",
        "marks": 1,
        "type": "mcq",
        "question": "True about NPC and NP-hard: prove NP-hard by reducing a known NP-hard problem to X; first NPC problem was circuit-SAT; NPC ⊂ NP-hard.",
        "short_answer": "All of the above. (Ch 4)",
        "full_solution": """Evaluating statements:
1. To prove X is NP-hard, we reduce a known NP-hard problem Y to X (Y ≤p X). TRUE.
2. The first problem proven NP-complete was Circuit-SAT by Stephen Cook (1971). TRUE.
3. NPC ⊂ NP-hard because NPC = NP ∩ NP-hard and there exist NP-hard problems outside NP (e.g., Halting problem). TRUE.
Correct answer: All of the above."""
    },
    {
        "id": "pdf-17",
        "topic": "complexity",
        "topic_name": "P, NP, NP-Hard, NP-Complete",
        "paper": "Autumn End Sem 2022",
        "paper_tag": "Aut-2022",
        "q": "Q1(e)",
        "marks": 1,
        "type": "diagram",
        "question": "A polynomial-time algorithm is found that correctly computes the largest clique in a given graph. In this scenario, which one of the following Venn diagrams of the complexity classes P, NP and NP-Complete (NPC) is correct?",
        "short_answer": "P = NP = NPC (one collapsed region) or NPC inside merged P=NP. Diagram (C)/(D). (Ch 4)",
        "full_solution": """1. Clique is known to be NP-complete.
2. If a polynomial-time algorithm is found for Clique:
   - Since Clique is NP-complete, every problem in NP reduces to Clique in polynomial time.
   - Combining the polynomial reduction with the polynomial solver gives a polynomial-time solver for EVERY problem in NP.
   - Therefore, NP ⊆ P. Since P ⊆ NP always, we get P = NP!
3. Impact on Venn diagram:
   - The boundary between P and NP disappears: P and NP merge into a single region.
   - Every NP-complete problem now belongs to P.
   - In standard textbook representations (Option C/D), P, NP, and NPC collapse together, while NP-hard problems that are undecidable (like Halting problem) remain strictly outside."""
    },
    {
        "id": "pdf-18",
        "topic": "complexity",
        "topic_name": "P, NP, NP-Hard, NP-Complete",
        "paper": "Autumn End Sem 2022",
        "paper_tag": "Aut-2022",
        "q": "Q1(h)",
        "marks": 1,
        "type": "mcq",
        "question": "Consider two problems A and B. Problem B is NP-complete. Problem A reduces to problem B in polynomial time. Which statement is correct? (a) If A solved in poly time then B solved in poly time (b) A is NP-complete (c) A is NP-hard (d) A is in NP but not NP-complete",
        "short_answer": "A is in NP (option d). A solved in poly time says nothing about B. (Ch 4)",
        "full_solution": """Given: B ∈ NPC and A ≤p B.
1. Since B ∈ NPC, B ∈ NP.
2. Since A ≤p B, an instance of A can be converted into an instance of B in polynomial time.
3. Therefore, A can be verified in polynomial time using B's verifier, which proves A ∈ NP.
4. Does A ≤p B prove A is NP-hard? NO! The reduction is from A to B, meaning B is at least as hard as A, but A could be a trivial problem in P (like sorting).
5. Option (d) is the intended exam answer: A must be in NP, and cannot be claimed to be NP-complete without showing a reverse reduction."""
    },
    {
        "id": "pdf-19",
        "topic": "complexity",
        "topic_name": "P, NP, NP-Hard, NP-Complete",
        "paper": "Autumn End Sem 2023",
        "paper_tag": "Aut-2023",
        "q": "Q1(j)",
        "marks": 1,
        "type": "diagram",
        "question": "Draw the Venn diagram showing the relation among P, NP, NPC and NP-hard.",
        "short_answer": "Two pictures in chapter 4: P ⊂ NP, NPC = NP ∩ NP-hard, NP-hard extending outside NP. (Ch 4)",
        "full_solution": """Venn Diagram Description:
1. If P ≠ NP (widely believed):
   - Outer Universe: All decision problems.
   - A large oval represents NP.
   - Inside NP, a smaller region represents P.
   - A large region on the right represents NP-hard.
   - The intersection of NP and NP-hard is NPC (NP-complete).
   - The region of NP-hard outside NP contains problems like the Halting problem and Optimization TSP.
   - P and NPC are completely disjoint (P ∩ NPC = ∅).
2. If P = NP:
   - The circle for P and the oval for NP completely coincide (P = NP).
   - NPC sits inside this merged P = NP region."""
    },
    {
        "id": "pdf-20",
        "topic": "complexity",
        "topic_name": "P, NP, NP-Hard, NP-Complete",
        "paper": "Autumn End Sem 2023",
        "paper_tag": "Aut-2023",
        "q": "Q7(a)",
        "marks": 4,
        "type": "theory",
        "question": "Explain different ways of handling NP-complete problems.",
        "short_answer": "Approximation, heuristics, special cases, randomized, backtracking/branch & bound, small inputs. (Ch 4)",
        "full_solution": """Since NP-complete problems are intractable in the worst case (assuming P ≠ NP), practical coping strategies are:
1. Approximation Algorithms:
   - Run in polynomial time and guarantee an answer within a provable factor ρ of optimal.
   - Example: 2-approximation for Vertex Cover, 2-approximation for Metric TSP.
2. Heuristics:
   - Fast rules of thumb that find good solutions in practice with no theoretical worst-case guarantee.
   - Example: Nearest Neighbor for TSP, Greedy search, Simulated Annealing, Genetic Algorithms.
3. Special Cases / Input Restrictions:
   - Restricting the input to a domain where the problem becomes polynomial.
   - Example: 2-SAT is in P; Vertex Cover on bipartite graphs (Konig's theorem) or trees is in P.
4. Dynamic Programming for Small n:
   - Exact solutions feasible for small inputs.
   - Example: Held-Karp algorithm for TSP in O(n² 2^n) time vs O(n!) brute-force.
5. Backtracking and Branch & Bound:
   - Exponential worst-case, but aggressively prunes subtrees that cannot beat the best known bound.
   - Example: Branch and bound for 0/1 Knapsack, TSP.
6. Randomized Algorithms:
   - Utilize random choices to escape local optima or find good cuts.
   - Example: Random restarts, Karger's min-cut algorithm."""
    },
    {
        "id": "pdf-21",
        "topic": "complexity",
        "topic_name": "P, NP, NP-Hard, NP-Complete",
        "paper": "Autumn End Sem 2023",
        "paper_tag": "Aut-2023",
        "q": "Q7(b)",
        "marks": 4,
        "type": "theory",
        "question": "S is NPC; Q, R not known to be in NP; Q ≤p S and S ≤p R. What are the probable classes of Q and R?",
        "short_answer": "Q ∈ NP (reduces to S ∈ NP); R is NP-hard. (Ch 4)",
        "full_solution": """Given:
- S is NP-complete (so S ∈ NP and S is NP-hard).
- Q and R are decision problems not known to be in NP.
- Q ≤p S and S ≤p R.

1. Analysis for Q (Q ≤p S):
   - Q reduces in polynomial time to S.
   - Since S ∈ NP, any instance of Q can be transformed in polynomial time into an instance of S and verified in polynomial time.
   - Therefore, Q MUST belong to NP.
   - However, since we do not have a reduction from S to Q, Q is not necessarily NP-complete; it could be in P or NP-intermediate.

2. Analysis for R (S ≤p R):
   - A known NP-complete problem S reduces in polynomial time to R.
   - Every problem L in NP reduces to S (since S is NPC), and S reduces to R.
   - By transitivity of polynomial reductions, every problem in NP reduces to R (L ≤p S ≤p R ⇒ L ≤p R).
   - Therefore, R MUST be NP-hard.
   - Since R is not known to be in NP, R is not necessarily NP-complete (it may lie outside NP)."""
    },
    {
        "id": "pdf-22",
        "topic": "complexity",
        "topic_name": "P, NP, NP-Hard, NP-Complete",
        "paper": "Autumn End Sem 2023",
        "paper_tag": "Aut-2023",
        "q": "Q8(a)",
        "marks": 4,
        "type": "theory",
        "question": "Define an NPC problem with examples. How can P = NP be proved or disproved? What if a known NPC problem has a polynomial solution?",
        "short_answer": "P = NP if any NPC problem has polynomial solution; disproved by proving no poly algorithm exists for some NP problem. (Ch 4)",
        "full_solution": """1. Definition of NP-Complete:
   A problem X is NP-complete if:
   - X ∈ NP (solutions can be verified in polynomial time), and
   - X is NP-hard (every problem in NP polynomial-time reduces to X).
   Examples: 3-SAT, Clique, Hamiltonian Cycle, Vertex Cover.

2. Proving or Disproving P = NP:
   - To prove P = NP: Find a deterministic polynomial-time algorithm for ANY single NP-complete problem (e.g. 3-SAT in O(n^k)). Since all NP problems reduce to it, all NP problems would be solvable in polynomial time.
   - To prove P ≠ NP: Mathematically prove that for at least one problem in NP (such as 3-SAT), NO deterministic polynomial-time algorithm can ever exist. (Millennium Prize problem).

3. What if a known NPC problem gets a polynomial solution?
   If a polynomial-time algorithm is discovered for an NPC problem X:
   - Then P = NP!
   - Reason: For any problem L ∈ NP, L ≤p X via converter f in time O(n^a), and X can be solved in time O(n^b). The composition takes O((n^a)^b) = O(n^(ab)), which is strictly polynomial."""
    },
    {
        "id": "pdf-23",
        "topic": "complexity",
        "topic_name": "P, NP, NP-Hard, NP-Complete",
        "paper": "Spring End Sem 2023",
        "paper_tag": "Spr-2023",
        "q": "Q1(c)(ii)",
        "marks": 1,
        "type": "mcq",
        "question": "True or false: if X can be reduced to a known NP-hard problem, then X must be NP-hard.",
        "short_answer": "False - the reduction goes the wrong way! (Ch 4)",
        "full_solution": """Statement: 'If X ≤p H (where H is known NP-hard), then X is NP-hard.'
This statement is FALSE.
- The reduction X ≤p H means 'X is no harder than H'.
- A trivial problem in P (such as 2+2=4 or sorting an array) can easily be reduced to an NP-hard problem in polynomial time. That does NOT make sorting NP-hard!
- To prove X is NP-hard, the reduction MUST go in the opposite direction: Known_NP_Hard ≤p X (meaning X is at least as hard as the known hard problem)."""
    },
    {
        "id": "pdf-24",
        "topic": "complexity",
        "topic_name": "P, NP, NP-Hard, NP-Complete",
        "paper": "Spring End Sem 2023",
        "paper_tag": "Spr-2023",
        "q": "Q8(b)",
        "marks": 4,
        "type": "theory",
        "question": "Describe P, NP and NPC classes of problems through suitable examples.",
        "short_answer": "Chapter 4: P (Dijkstra, sorting), NP (verification with certificate), NPC (SAT, Clique, TSP). (Ch 4)",
        "full_solution": """1. Class P (Polynomial Time):
   - Problems solvable by a deterministic algorithm in O(n^c) time.
   - Example: Single-source shortest path (Dijkstra runs in O(E + V log V)), Matrix multiplication (Strassen O(n^2.81)), Finding Minimum Spanning Tree (Prim/Kruskal).
2. Class NP (Nondeterministic Polynomial Time):
   - Problems where a candidate certificate for a YES-instance can be checked in O(n^c) time.
   - Example: Subset Sum (given a subset, summing elements and checking target takes O(n)), Hamiltonian Cycle (given a sequence of vertices, verifying it forms a valid simple cycle of length n takes O(n)).
3. Class NPC (NP-Complete):
   - Hardest problems in NP. Both in NP and NP-hard.
   - Example: 3-CNF SAT, Clique, Vertex Cover, Travelling Salesperson Problem (decision version)."""
    },
    {
        "id": "pdf-25",
        "topic": "complexity",
        "topic_name": "P, NP, NP-Hard, NP-Complete",
        "paper": "Spring End Sem 2024",
        "paper_tag": "Spr-2024",
        "q": "Q6(b)",
        "marks": 5,
        "type": "theory",
        "question": "Define and differentiate between P, NP and NP-complete problems with examples.",
        "short_answer": "P = solve fast; NP = verify fast; NPC = hardest in NP. (Ch 4)",
        "full_solution": """1. Definitions:
   - P: Decision problems solvable in polynomial time deterministically.
   - NP: Decision problems verifiable in polynomial time given a certificate.
   - NPC: Decision problems X such that X ∈ NP and ∀ L ∈ NP, L ≤p X.
2. Differences:
   - Solvability: P is solvable in polynomial time; NP is not known to be solvable in polynomial time; NPC is believed to require exponential time.
   - Verification: All three can be verified in polynomial time (P ⊆ NP, NPC ⊆ NP).
   - Hardness: NPC problems are the hardest in NP; any polynomial algorithm for an NPC problem makes P = NP = NPC.
3. Examples:
   - P: Binary Search, Dijkstra, Kruskal MST, MergeSort.
   - NP: Factoring integers, Graph Isomorphism, TSP, Clique.
   - NPC: Circuit-SAT, 3-SAT, Clique, Vertex Cover, Hamiltonian Cycle."""
    },
    {
        "id": "pdf-26",
        "topic": "complexity",
        "topic_name": "P, NP, NP-Hard, NP-Complete",
        "paper": "Spring End Sem 2025",
        "paper_tag": "Spr-2025",
        "q": "Q8(b)",
        "marks": 4,
        "type": "theory",
        "question": "Define the P, NP, NP-hard and NP-complete problems and give the relation between them.",
        "short_answer": "Chapter 4: Four definitions, Venn diagrams, P ⊆ NP, NPC = NP ∩ NP-hard. (Ch 4)",
        "full_solution": """1. Four Definitions:
   - P: Problems solvable in polynomial time by a deterministic algorithm.
   - NP: Problems verifiable in polynomial time given a certificate.
   - NP-hard: Problems to which all problems in NP reduce in polynomial time. (Does not need to be in NP).
   - NP-complete: Problems that are both in NP and NP-hard.
2. Relationships:
   - P ⊆ NP.
   - NPC = NP ∩ NP-hard.
   - If P ≠ NP (consensus): P ∩ NPC = ∅. P is a strict subset of NP.
   - If P = NP: P = NP = NPC.
   - NP-hard contains NPC and also undecidable problems (e.g. Halting problem) and optimization problems."""
    },
    {
        "id": "pdf-27",
        "topic": "reductions",
        "topic_name": "Classic Reductions & 3-SAT",
        "paper": "Autumn End Sem 2024",
        "paper_tag": "Aut-2024",
        "q": "Q1(j)",
        "marks": 1,
        "type": "mcq",
        "question": "Shahrukh and Salman have been asked to show that a certain problem 'Superstar' is NP-complete. Shahrukh shows a polynomial time reduction from 3-SAT to 'Superstar' and Salman shows a polynomial time reduction from 'Superstar' to 3-SAT. Which can be inferred?",
        "short_answer": "'Superstar' is NP-complete. (Ch 5)",
        "full_solution": """1. Shahrukh shows 3-SAT ≤p Superstar:
   - 3-SAT is a known NP-complete (and therefore NP-hard) problem.
   - Since 3-SAT reduces to Superstar in polynomial time, Superstar is at least as hard as 3-SAT.
   - Thus, Superstar is NP-HARD.
2. Salman shows Superstar ≤p 3-SAT:
   - 3-SAT is in NP.
   - Since Superstar reduces to a problem in NP in polynomial time, Superstar can be verified in polynomial time.
   - Thus, Superstar is in NP.
3. Combining both:
   - Superstar is in NP AND Superstar is NP-hard.
   - By definition, Superstar is NP-COMPLETE!
Correct answer: (b) NP-complete."""
    },
    {
        "id": "pdf-28",
        "topic": "reductions",
        "topic_name": "Classic Reductions & 3-SAT",
        "paper": "Autumn End Sem 2025",
        "paper_tag": "Aut-2025",
        "q": "Q1(i)",
        "marks": 1,
        "type": "mcq",
        "question": "Consider a decision problem Q. 3CNF-SAT reduces in polynomial time to Q. Which one of the following is consistent with the above statement? (i) Q is in NP (ii) Q is in NP-hard (iii) Q is in NPC (iv) Q is in P",
        "short_answer": "Q is NP-hard (option ii). (Ch 5)",
        "full_solution": """1. 3-CNF SAT is a known NP-complete problem.
2. We are given: 3CNF-SAT ≤p Q.
3. Since a known NP-hard problem reduces to Q in polynomial time, Q is at least as hard as 3CNF-SAT, which means every problem in NP reduces to Q.
4. Therefore, Q is NP-hard.
5. Q is NOT guaranteed to be in NP (e.g. Q could be the Halting problem or an undecidable problem). Hence we cannot claim Q is in NPC or in NP.
Correct answer: (ii) Q is in NP-hard."""
    },
    {
        "id": "pdf-29",
        "topic": "clique",
        "topic_name": "Clique Problem",
        "paper": "Autumn End Sem 2024",
        "paper_tag": "Aut-2024",
        "q": "Q7(a)",
        "marks": 5,
        "type": "theory",
        "question": "Define NP. Write an algorithm to prove that the Clique decision problem is in NP.",
        "short_answer": "Definition of NP, certificate S of k vertices, verifier in O(k²) ≤ O(n²). (Ch 5)",
        "full_solution": """1. Definition of NP:
   A decision problem is in NP if, for every YES-instance x, there exists a polynomial-length certificate c that can be verified by a deterministic algorithm V(x, c) in polynomial time.

2. Clique Decision Problem (CDP):
   Given an undirected graph G = (V, E) and an integer k, does G contain a clique (a subset of vertices where every pair is connected by an edge) of size at least k?

3. Certificate:
   A candidate subset S ⊆ V claiming to be a clique of size k. Length of S is at most |V| = n, which is polynomial in the input size.

4. Verifier Algorithm:
VERIFY-CLIQUE(G = (V, E), k, S)
1. if |S| < k then
2.     return FALSE
3. for each pair of distinct vertices u, v in S do
4.     if (u, v) not in E then
5.         return FALSE
6. return TRUE

5. Time Complexity Analysis:
   - Step 1 takes O(1) time.
   - The number of pairs of vertices in S is k(k - 1) / 2 = O(k²).
   - Checking whether edge (u, v) ∈ E takes O(1) time using an adjacency matrix (or O(deg(u)) in adjacency list).
   - Total verification time = O(k²) ≤ O(|V|²) = O(n²).
   - Since O(n²) is polynomial in input size, CDP ∈ NP."""
    },
    {
        "id": "pdf-30",
        "topic": "clique",
        "topic_name": "Clique Problem",
        "paper": "Autumn End Sem 2025",
        "paper_tag": "Aut-2025",
        "q": "Q6(b)",
        "marks": 5,
        "type": "theory",
        "question": "Define NP with respect to the Clique Decision Problem (CDP). Write an algorithm to prove that CDP belongs to NP.",
        "short_answer": "Same verifier algorithm as Autumn 2024, running in O(k²) ≤ O(n²). (Ch 5)",
        "full_solution": """1. Definition of NP with respect to CDP:
   The Clique Decision Problem belongs to NP because for any graph G with a clique of size k, there exists a succinct certificate (the list of k vertices) that a deterministic polynomial-time verifier can check in O(n²) time.

2. Verifier Algorithm:
VERIFY-CLIQUE(G, k, S)
   if |S| != k return FALSE
   for each u in S:
       for each v in S (v != u):
           if (u, v) is not an edge in G:
               return FALSE
   return TRUE

3. Complexity:
   Pairs to check: k(k-1)/2. Each edge check takes O(1).
   Total time: O(k²) ≤ O(V²), which is deterministic polynomial time.
   Hence, CDP ∈ NP."""
    },
    {
        "id": "pdf-31",
        "topic": "hamiltonian",
        "topic_name": "Hamiltonian Cycle & TSP",
        "paper": "Autumn End Sem 2024",
        "paper_tag": "Aut-2024",
        "q": "Q7(b)",
        "marks": 5,
        "type": "derivation",
        "question": "Define the Hamiltonian Cycle Problem. Prove that the Decision Travelling Salesman Problem is in NPC assuming that the Hamiltonian Cycle Problem is in NPC.",
        "short_answer": "TSP ∈ NP (verify tour in O(n)) and HC ≤p TSP (cost 1 for edges, cost 2 for non-edges, k = n). (Ch 5)",
        "full_solution": """1. Definition of Hamiltonian Cycle (HC) Problem:
   Given an undirected graph G = (V, E), does G contain a simple cycle that visits every vertex v ∈ V exactly once and returns to the starting vertex? (HC is NP-complete).

2. Definition of Decision TSP:
   Given a complete graph G' = (V', E') with nonnegative edge costs c(u, v) and an integer k, is there a tour (Hamiltonian cycle) visiting every vertex with total cost ≤ k?

3. Step 1: Prove TSP ∈ NP
   - Certificate: A sequence of vertices <v_1, v_2, ..., v_n>.
   - Verifier: Check that all n vertices appear distinct, check that (v_i, v_{i+1}) and (v_n, v_1) are edges, and compute Total Cost = Σ c(v_i, v_{i+1}) + c(v_n, v_1).
   - If Total Cost ≤ k, return TRUE; else FALSE.
   - Verification takes O(n) time, which is polynomial. Thus, TSP ∈ NP.

4. Step 2: Prove TSP is NP-hard by Reduction (HC ≤p TSP)
   - Given an arbitrary instance of HC: graph G = (V, E) with n vertices.
   - Construct an instance of TSP (G', c, k) as follows:
     * V' = V (same vertices).
     * G' is a complete graph on V'.
     * For each pair of vertices (u, v):
       c(u, v) = 1, if (u, v) ∈ E (edge present in original graph G)
       c(u, v) = 2, if (u, v) ∉ E (edge absent in G)
     * Set target bound k = n.
   - Construction takes O(n²) time to assign weights, which is polynomial.

5. Correctness Proof (G has HC ⇔ G' has TSP tour of cost ≤ n):
   - (⇒) If G has a Hamiltonian cycle, that cycle visits n vertices using n edges of G.
     In G', each of these n edges has cost 1.
     Total tour cost = n × 1 = n ≤ k. Hence, G' has a TSP tour of cost ≤ n.
   - (⇐) Suppose G' has a tour of cost ≤ n.
     The tour has n edges. Every edge in G' has cost either 1 or 2.
     For n edges to sum to ≤ n, EVERY edge in the tour must have cost exactly 1!
     An edge has cost 1 in G' if and only if it was an edge in G.
     Therefore, the tour uses only edges of G, which forms a valid Hamiltonian cycle in G.
Conclusion: Since TSP ∈ NP and HC ≤p TSP with HC ∈ NPC, Decision TSP is NP-Complete."""
    },
    {
        "id": "pdf-32",
        "topic": "approximation",
        "topic_name": "Approximation Algorithms",
        "paper": "Autumn End Sem 2012",
        "paper_tag": "Aut-2012",
        "q": "Q7(b)",
        "marks": 5,
        "type": "theory",
        "question": "Explain with an example how the Travelling-Salesman Problem can be solved using an approximation algorithm.",
        "short_answer": "MST + preorder walk 2-approximation for Metric TSP, cost ≤ 2·OPT. (Ch 6)",
        "full_solution": """1. Metric TSP:
   Assumes edge costs satisfy the Triangle Inequality: c(u, w) ≤ c(u, v) + c(v, w) for all u, v, w.

2. 2-Approximation Algorithm (APPROX-TSP-TOUR):
   Step 1: Select an arbitrary root city r.
   Step 2: Compute a Minimum Spanning Tree (MST) T of G using Prim's or Kruskal's algorithm.
   Step 3: Perform a preorder depth-first search (DFS) walk of T, listing vertices in the order they are first visited.
   Step 4: Output the preorder cycle H returning back to root r.

3. Proof of Approximation Ratio ρ = 2:
   - Claim 1: Cost(MST) ≤ Cost(OPT_TSP).
     Proof: Deleting any single edge from the optimal TSP tour yields a spanning tree. Since MST has minimum possible cost among all spanning trees, Cost(MST) ≤ Cost(OPT) - edge_cost < Cost(OPT).
   - Claim 2: A full walk W traversing each edge of MST twice has Cost(W) = 2 · Cost(MST).
   - Claim 3: By the Triangle Inequality, taking shortcuts past previously visited vertices never increases the cost: Cost(H) ≤ Cost(W).
   - Combining these:
     Cost(H) ≤ Cost(W) = 2 · Cost(MST) ≤ 2 · Cost(OPT).
   - Thus, the algorithm guarantees a 2-approximation (ratio ≤ 2).

4. Example:
   For 7 cities with Euclidean coordinates:
   - MST cost = 485.6
   - Optimal tour = 655.9
   - Algorithm tour = 753.2
   - Ratio = 753.2 / 655.9 = 1.15 ≤ 2.0 (proven worst-case bound holds)."""
    }
]

print("Dataset prepared with", len(PDF_32_QUESTIONS), "questions.")

