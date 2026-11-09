# site_lessons.py
# Detailed lesson contents for all 17 chapters

LESSONS_HTML = """
<!-- ========================================== -->
<!-- LESSON 1: FAST AND SLOW (TRACTABILITY)     -->
<!-- ========================================== -->
<section class="lesson-card" id="l1" data-title="Fast & Slow Algorithms">
  <div class="lesson-header">
    <div class="lesson-badge">1</div>
    <div class="lesson-titles">
      <div class="lesson-unit">Unit 5 · Complexity Foundations</div>
      <h2 class="lesson-title">Fast and Slow Algorithms: Growth Rates & Tractability</h2>
    </div>
  </div>
  
  <p>In algorithm design, execution speed is not measured in seconds, but in how running time scales as input size n grows. We classify problems into two worlds:</p>
  <ul style="margin: 8px 0 14px 24px;">
    <li><b>Tractable (Polynomial Time):</b> Algorithms with time complexity bounded by a polynomial: O(n), O(n log n), O(n²), O(n³). Even for large inputs (n = 100,000), modern processors complete in milliseconds or seconds.</li>
    <li><b>Intractable (Exponential Time):</b> Algorithms requiring O(2ⁿ), O(3ⁿ), O(n!) steps. While they run fine for n = 15, an input of n = 50 requires more steps than seconds elapsed since the Big Bang!</li>
  </ul>

  <div class="say-box">
    <b>In One Line:</b> "Polynomial" (nᶜ) means practical and scalable. "Exponential" (2ⁿ) means it hits a computational brick wall the moment n exceeds 40.
  </div>

  <div class="analogy-box">
    <div class="analogy-title">💡 Real-Life Analogy: Intercity Train vs Rocket to the Edge of the Galaxy</div>
    If an input of n=10 takes 1 second, increasing n to 50 on an O(n²) algorithm takes 25 seconds (a pleasant train commute). On an O(2ⁿ) algorithm, it takes over <b>13 days</b>. At n=60, it takes <b>365 centuries</b>!
  </div>

  <!-- Simulation 1: Growth Rates -->
  <div class="sim-container" id="sim-growth-container">
    <div class="sim-header">
      <div class="sim-title">⚡ Interactive Simulation: Growth of Functions on a Log Scale</div>
      <span class="exam-chip">Visual Lab</span>
    </div>
    <p class="sim-hint">Drag the slider for n and observe how exponential curves shoot into infinity while polynomial curves remain flat. Assumes a CPU executing 10⁹ steps/sec.</p>
    
    <div class="row">
      <label for="gn" style="font-weight:700;">Input Size n = <span id="gnv" class="mono" style="font-size:18px; color:var(--accent);">20</span></label>
      <input id="gn" type="range" min="1" max="60" value="20" style="flex:1; max-width:320px;">
    </div>
    
    <div class="cols-2" style="margin-top:14px;">
      <div style="overflow-x:auto;">
        <table class="data-table" id="gt"></table>
      </div>
      <div>
        <svg class="interactive-fig" id="gchart" viewBox="0 0 420 270" role="img" aria-label="Growth chart on log scale"></svg>
        <div class="row" style="font-size:12px; color:var(--muted); justify-content:center; margin-top:6px;">
          <span><i style="display:inline-block; width:12px; height:4px; background:var(--accent); vertical-align:middle; margin-right:4px;"></i> n, n², n³ (Polynomial)</span>
          <span style="margin-left:14px;"><i style="display:inline-block; width:12px; height:4px; background:var(--hard); vertical-align:middle; margin-right:4px;"></i> 2ⁿ, n! (Exponential)</span>
        </div>
      </div>
    </div>
  </div>

  <div class="exam-pill-strip">
    <span>Asked in:</span>
    <span class="exam-chip">Spring 2024 Q6b</span>
    <span class="exam-chip">Spring 2025 Q8b</span>
    <span class="exam-chip">Autumn 2022 Q1e</span>
  </div>
</section>

<!-- ========================================== -->
<!-- LESSON 2: DECISION VS OPTIMIZATION         -->
<!-- ========================================== -->
<section class="lesson-card" id="l2" data-title="Decision vs Optimization">
  <div class="lesson-header">
    <div class="lesson-badge">2</div>
    <div class="lesson-titles">
      <div class="lesson-unit">Unit 5 · Foundations</div>
      <h2 class="lesson-title">Decision Problems vs Optimization Problems</h2>
    </div>
  </div>

  <p>Theoretical computer science and NP-completeness exclusively analyze <b>Decision Problems</b>: problems whose output is strictly <b>YES</b> or <b>NO</b>. In industry, we usually care about <b>Optimization Problems</b> (finding the best tour, lowest cost, or highest profit).</p>

  <div class="cols-2" style="margin: 16px 0;">
    <div style="background:var(--sunk); border-radius:12px; padding:16px;">
      <h4 style="font:800 16px var(--font-display); margin-bottom:8px; color:var(--accent);">Decision Problem</h4>
      <p style="font-size:14px;">Answers a binary question: "Does there exist a solution with value ≤ k (or ≥ k)?"</p>
      <p style="font-size:13px; color:var(--muted); margin-top:6px;">Example: "Is there a TSP tour of length ≤ 500 km?"</p>
    </div>
    <div style="background:var(--sunk); border-radius:12px; padding:16px;">
      <h4 style="font:800 16px var(--font-display); margin-bottom:8px; color:var(--hard);">Optimization Problem</h4>
      <p style="font-size:14px;">Finds the absolute optimal configuration (minimum cost or maximum profit).</p>
      <p style="font-size:13px; color:var(--muted); margin-top:6px;">Example: "Find the tour with the minimum total distance."</p>
    </div>
  </div>

  <div class="say-box">
    <b>Why Complexity Theory Uses Decision Problems:</b>
    <ul style="padding-left:18px; margin-top:6px;">
      <li>An optimization problem is <b>at least as hard</b> as its decision version. If you can find the minimum tour cost in polynomial time, you can answer "is cost ≤ k?" in O(1) comparison.</li>
      <li>Conversely, using binary search on k, a polynomial decision solver can solve the optimization problem in polynomial time!</li>
      <li>Therefore, proving the decision problem is NP-hard automatically proves the optimization problem is NP-hard.</li>
    </ul>
  </div>

  <div class="analogy-box">
    <div class="analogy-title">💡 Real-Life Analogy: Buying a Laptop</div>
    "Can I buy a laptop with 16GB RAM for under Rs 50,000?" is a <b>Decision Problem</b>. "Find the cheapest laptop in the market with 16GB RAM" is an <b>Optimization Problem</b>.
  </div>

  <div class="sim-container">
    <div class="sim-header">
      <div class="sim-title">🔄 Interactive Problem Formulator: Decision vs Optimization</div>
    </div>
    <div class="row" id="dec-opt-btns"></div>
    <div class="status-box" id="dec-opt-status" style="margin-top:10px;"></div>
  </div>
</section>

<!-- ========================================== -->
<!-- LESSON 3: DETERMINISTIC & NON-DETERMINISTIC-->
<!-- ========================================== -->
<section class="lesson-card" id="l3" data-title="Deterministic vs Non-Deterministic">
  <div class="lesson-header">
    <div class="lesson-badge">3</div>
    <div class="lesson-titles">
      <div class="lesson-unit">Unit 5 · Complexity Theory</div>
      <h2 class="lesson-title">Deterministic vs Non-Deterministic Algorithms & Certificates</h2>
    </div>
  </div>

  <p>To define the class NP, we compare two theoretical computing paradigms:</p>
  <ul style="margin: 8px 0 14px 24px;">
    <li><b>Deterministic Algorithm:</b> At each step, given the current state and input, there is exactly <b>one</b> unique next operation. This models real computers.</li>
    <li><b>Non-Deterministic Algorithm:</b> Consists of two stages:
      <ol style="margin-top:4px;">
        <li><b>Guessing stage:</b> Magically generates a candidate certificate / solution string c in O(1) time using a special <code>choice()</code> primitive.</li>
        <li><b>Verification stage:</b> Runs a deterministic polynomial algorithm V(x, c) to verify if the candidate solves the problem. If ANY guess produces a YES, the algorithm accepts!</li>
      </ol>
    </li>
  </ul>

  <div class="say-box">
    <b>What is a Certificate?</b> A certificate (witness or proof) is a piece of evidence that allows a verifier to confirm a YES-instance in polynomial time. For Sudoku, the certificate is the completed grid. For Hamiltonian Cycle, it is the sequence of vertices in the cycle.
  </div>

  <!-- Simulation 3: Clique Verifier -->
  <div class="sim-container" id="sim-clique-container">
    <div class="sim-header">
      <div class="sim-title">🔍 Interactive Lab: Clique Verification vs Brute Force</div>
      <span class="exam-chip">Asked 2× in Exams! (5 marks)</span>
    </div>
    <p class="sim-hint">Problem: Does this 7-vertex graph contain a <b>clique of size k = 4</b>? Click 4 vertices to supply your candidate certificate, then click <b>Verify My Certificate</b>.</p>
    
    <div class="cols-2">
      <svg class="interactive-fig" id="cq" viewBox="0 0 400 320" role="img" aria-label="Graph for Clique Verification"></svg>
      <div>
        <div class="row">
          <button class="btn pri" id="cqv">Verify My Certificate</button>
          <button class="btn" id="cqb">Run Brute-Force Search</button>
          <button class="btn" id="cqr">Reset</button>
        </div>
        <div class="status-box" id="cqs">Pick 4 vertices to create your certificate.</div>
        <p class="sim-hint" style="margin-top:12px;"><b>Verification Time:</b> Checking your 4 vertices takes just C(4, 2) = 6 pair checks (O(k²)). Brute force must check C(7, 4) = 35 combinations!</p>
        <table class="data-table" id="cqt"></table>
      </div>
    </div>
  </div>

  <div class="exam-pill-strip">
    <span>Asked in:</span>
    <span class="exam-chip">Autumn 2024 Q7a (5m)</span>
    <span class="exam-chip">Autumn 2025 Q6b (5m)</span>
  </div>
</section>

<!-- ========================================== -->
<!-- LESSON 4: THE FOUR CORE CLASSES            -->
<!-- ========================================== -->
<section class="lesson-card" id="l4" data-title="P, NP, NP-Hard, NP-Complete">
  <div class="lesson-header">
    <div class="lesson-badge">4</div>
    <div class="lesson-titles">
      <div class="lesson-unit">Unit 5 · The Big Picture</div>
      <h2 class="lesson-title">P, NP, NP-Hard, and NP-Complete</h2>
    </div>
  </div>

  <p>This is the <b>most frequently repeated topic</b> across KIIT end-semester question papers (appearing in 17 of 32 exam questions!). Memorize the four exact definitions:</p>

  <div class="cheat-grid" style="margin: 16px 0;">
    <div class="cheat-card" style="border-top:4px solid var(--ok);">
      <h4 style="color:var(--ok);">Class P</h4>
      <p style="font-size:14px;">Decision problems that can be <b>SOLVED</b> in polynomial time by a deterministic algorithm.</p>
      <p style="font-size:12px; color:var(--muted); margin-top:6px;"><b>Examples:</b> Dijkstra Shortest Path, Kruskal/Prim MST, MergeSort, 2-SAT, Cycle Detection.</p>
    </div>
    <div class="cheat-card" style="border-top:4px solid var(--accent);">
      <h4 style="color:var(--accent);">Class NP</h4>
      <p style="font-size:14px;">Decision problems whose YES-instance can be <b>VERIFIED</b> in polynomial time given a certificate. P ⊆ NP.</p>
      <p style="font-size:12px; color:var(--muted); margin-top:6px;"><b>Examples:</b> 3-SAT, Clique, Hamiltonian Cycle, Subset Sum, 0/1 Knapsack decision.</p>
    </div>
    <div class="cheat-card" style="border-top:4px solid var(--hard);">
      <h4 style="color:var(--hard);">Class NP-Hard</h4>
      <p style="font-size:14px;">Problems at least as hard as every problem in NP. Every problem in NP polynomial-time reduces to it. <b>Need not be in NP.</b></p>
      <p style="font-size:12px; color:var(--muted); margin-top:6px;"><b>Examples:</b> Halting Problem (undecidable), Optimization TSP.</p>
    </div>
    <div class="cheat-card" style="border-top:4px solid var(--purple);">
      <h4 style="color:var(--purple);">Class NP-Complete (NPC)</h4>
      <p style="font-size:14px;">The hardest problems in NP: NPC = NP ∩ NP-hard. Solvable in poly time non-deterministically.</p>
      <p style="font-size:12px; color:var(--muted); margin-top:6px;"><b>Examples:</b> Circuit-SAT (Cook's theorem), 3-SAT, Vertex Cover, Clique, TSP decision.</p>
    </div>
  </div>

  <!-- Simulation 4: Venn Diagram -->
  <div class="sim-container" id="sim-venn-container">
    <div class="sim-header">
      <div class="sim-title">📊 Interactive Venn Diagram: P vs NP vs NP-Complete</div>
      <span class="exam-chip">Autumn 2022 Q1e Trap</span>
    </div>
    <p class="sim-hint">Toggle between the two universes: what researchers believe (P ≠ NP) vs what happens if someone solves an NPC problem in polynomial time (P = NP).</p>
    
    <div class="row">
      <button class="btn active" id="v1" aria-pressed="true">Universe 1: P ≠ NP (Consensus)</button>
      <button class="btn" id="v2" aria-pressed="false">Universe 2: P = NP (Hypothetical)</button>
      <button class="btn pri" id="v3">Autumn 2022 Q1e: "Fast Clique Discovered!"</button>
    </div>
    
    <svg class="interactive-fig" id="venn" viewBox="0 0 640 330" role="img" aria-label="Venn diagram of complexity classes"></svg>
    <div class="status-box" id="vs"></div>
  </div>

  <div class="exam-pill-strip">
    <span>Asked in:</span>
    <span class="exam-chip">Autumn 2022 Q1e (1m)</span>
    <span class="exam-chip">Autumn 2023 Q1j (1m)</span>
    <span class="exam-chip">Spring 2024 Q6b (5m)</span>
    <span class="exam-chip">Spring 2025 Q8b (4m)</span>
  </div>
</section>

<!-- ========================================== -->
<!-- LESSON 5: REDUCTIONS & THE MCQ RULES       -->
<!-- ========================================== -->
<section class="lesson-card" id="l5" data-title="Reductions & MCQ Rules">
  <div class="lesson-header">
    <div class="lesson-badge">5</div>
    <div class="lesson-titles">
      <div class="lesson-unit">Unit 5 · Polynomial Reductions</div>
      <h2 class="lesson-title">Polynomial Reductions (A ≤ₚ B) & The Direction Trap</h2>
    </div>
  </div>

  <p>A polynomial-time reduction A ≤ₚ B (read "A reduces to B") is an algorithm that converts an instance x of problem A into an instance f(x) of problem B in polynomial time, such that:</p>
  <div style="text-align:center; margin:10px 0; font-family:var(--font-mono); font-size:17px; background:var(--sunk); padding:8px; border-radius:8px;">
    x ∈ A ⟺ f(x) ∈ B (YES maps to YES, NO maps to NO)
  </div>

  <p><b>Core Intuition:</b> A ≤ₚ B means <b>"Problem A is NO HARDER than problem B"</b>. If you have a fast subroutine to solve B, you can solve A in fast time!</p>

  <div class="exam-trap-box">
    <div class="exam-trap-title">⚠️ THE DIRECTION TRAP (Spring 2023 Q1c(ii))</div>
    To prove that a new problem X is NP-hard, you MUST reduce a <b>known NP-hard problem K to X</b>:
    <div style="text-align:center; font-weight:700; font-size:16px; margin:6px 0;">K_known_hard ≤ₚ X_new</div>
    Reducing X ≤ₚ K proves NOTHING about the hardness of X! (A trivial problem like 2+2=4 reduces to 3-SAT, but that doesn't make addition hard!).
  </div>

  <!-- Simulation 5: Reduction Rules MCQ Matrix -->
  <div class="sim-container">
    <div class="sim-header">
      <div class="sim-title">⚡ Interactive Reduction Rules Trainer: Tap to Test Deductions</div>
      <span class="exam-chip">Tested in 5 End-Sem Papers</span>
    </div>
    <p class="sim-hint">Assume A ≤ₚ B. Tap each card to discover whether the deduction is valid or an exam trap.</p>
    <div class="cheat-grid" id="rules-grid"></div>
  </div>

  <div class="exam-pill-strip">
    <span>Asked in:</span>
    <span class="exam-chip">Autumn 2022 Q1h (1m)</span>
    <span class="exam-chip">Spring 2023 Q1c(ii) (1m)</span>
    <span class="exam-chip">Autumn 2024 Q1j (1m)</span>
    <span class="exam-chip">Autumn 2025 Q1i (1m)</span>
  </div>
</section>

<!-- ========================================== -->
<!-- LESSON 6: SAT AND 3-CNF-SAT                -->
<!-- ========================================== -->
<section class="lesson-card" id="l6" data-title="SAT & 3-CNF-SAT">
  <div class="lesson-header">
    <div class="lesson-badge">6</div>
    <div class="lesson-titles">
      <div class="lesson-unit">Unit 5 · Foundational Problems</div>
      <h2 class="lesson-title">Cook's Theorem, SAT and 3-CNF-SAT</h2>
    </div>
  </div>

  <p>In 1971, Stephen Cook proved the monumental <b>Cook-Levin Theorem</b>: Boolean Satisfiability (SAT) is NP-complete. Because this was the very first NP-complete problem, all subsequent NP-completeness proofs branch out from SAT.</p>

  <div class="cols-2" style="margin: 14px 0;">
    <div>
      <h4 style="font:800 16px var(--font-display); margin-bottom:6px;">Terminology:</h4>
      <ul style="padding-left:18px; font-size:14.5px;">
        <li><b>Literal:</b> A boolean variable x or its negation ≠g x.</li>
        <li><b>Clause:</b> An OR (∨) of literals: (x_1 ∨ ≠g x_2 ∨ x_3).</li>
        <li><b>CNF (Conjunctive Normal Form):</b> An AND (∧) of clauses.</li>
        <li><b>3-CNF-SAT:</b> A CNF formula where <b>every clause has exactly 3 literals</b>.</li>
      </ul>
    </div>
    <div class="say-box" style="margin:0;">
      <b>2-SAT vs 3-SAT: The Razor's Edge!</b><br>
      • <b>2-SAT</b> (2 literals per clause) is in <b>P</b>! It is solvable in linear O(V+E) time using an implication graph and strongly connected components (SCC).<br>
      • <b>3-SAT</b> (3 literals per clause) jumps immediately to <b>NP-Complete</b>!
    </div>
  </div>

  <!-- Simulation 6: 3-SAT Solver -->
  <div class="sim-container" id="sim-sat-container">
    <div class="sim-header">
      <div class="sim-title">⚡ Interactive 3-CNF SAT Circuit & Truth Table Simulator</div>
    </div>
    <p class="sim-hint">Toggle variables x_1, x_2, x_3 below. A clause turns green when at least one literal evaluates to TRUE. The formula is satisfied when all clauses turn green.</p>
    
    <div class="row" id="satvars"></div>
    <div id="satcl" style="margin:12px 0;"></div>
    <div class="status-box" id="sats"></div>
    
    <div class="row" style="margin-top:14px;">
      <button class="btn" id="satall">Generate Full Truth Table (2³ = 8 rows)</button>
      <button class="btn" id="satun">Load Unsatisfiable Formula (All 8 minterms)</button>
      <button class="btn" id="satre">Reset to Default Formula</button>
    </div>
    <div id="sattab" style="margin-top:12px; overflow-x:auto;"></div>
  </div>

  <div class="exam-pill-strip">
    <span>Asked in:</span>
    <span class="exam-chip">Autumn 2024 Q1j</span>
    <span class="exam-chip">Autumn 2025 Q1i</span>
  </div>
</section>

<!-- ========================================== -->
<!-- LESSON 7: THE TRIAD (CLIQUE, IS, VC)       -->
<!-- ========================================== -->
<section class="lesson-card" id="l7" data-title="Clique, Indep Set & Vertex Cover">
  <div class="lesson-header">
    <div class="lesson-badge">7</div>
    <div class="lesson-titles">
      <div class="lesson-unit">Unit 5 · The Equivalence Triad</div>
      <h2 class="lesson-title">Clique, Independent Set, and Vertex Cover</h2>
    </div>
  </div>

  <p>These three classic graph problems form an intimately connected family. Understanding their complement mapping makes reduction proofs effortless:</p>
  <ul style="margin: 8px 0 14px 24px;">
    <li><b>Clique:</b> A subset of vertices S ⊆ V where every pair is joined by an edge (everyone knows everyone).</li>
    <li><b>Independent Set (IS):</b> A subset of vertices S ⊆ V where no two vertices share an edge (no one knows each other).</li>
    <li><b>Vertex Cover (VC):</b> A subset of vertices C ⊆ V such that every edge in E has at least one endpoint in C.</li>
  </ul>

  <div class="say-box">
    <b>The Fundamental Theorem of Complements:</b><br>
    For any graph G = (V, E) with |V| = n vertices and its complement graph Ḡ = (V, Ē):
    <ol style="margin-top:4px; padding-left:20px;">
      <li>S is an <b>Independent Set</b> in G ⟺ S is a <b>Clique</b> in Ḡ.</li>
      <li>S is a <b>Vertex Cover</b> in G ⟺ V \\ S is an <b>Independent Set</b> in G.</li>
      <li>Therefore, G has a <b>clique of size k</b> ⟺ Ḡ has a <b>vertex cover of size n - k</b>!</li>
    </ol>
  </div>

  <!-- Simulation 7: Triad Dual Graph -->
  <div class="sim-container" id="sim-triad-container">
    <div class="sim-header">
      <div class="sim-title">🔄 Dual Graph Simulator: Graph G vs Complement Ḡ</div>
    </div>
    <p class="sim-hint">Tap vertices on either graph to select subset S. Dashed lines in the right graph represent non-edges of G. Watch how Clique in G, Independent Set in Ḡ, and Vertex Cover in Ḡ synchronize perfectly!</p>
    
    <div class="cols-2">
      <div>
        <b>Graph G</b>
        <svg class="interactive-fig" id="g1" viewBox="0 0 300 220" role="img" aria-label="Original graph G"></svg>
      </div>
      <div>
        <b>Complement Graph Ḡ</b>
        <svg class="interactive-fig" id="g2" viewBox="0 0 300 220" role="img" aria-label="Complement graph G bar"></svg>
      </div>
    </div>
    <div class="status-box" id="civ" style="margin-top:10px;"></div>
    <div class="row">
      <button class="btn" id="civ3">Auto-Select 3-Clique {1, 2, 3}</button>
      <button class="btn" id="civr">Clear Selection</button>
    </div>
  </div>

  <div class="exam-pill-strip">
    <span>Asked in:</span>
    <span class="exam-chip">Autumn 2024 Q7a (5m)</span>
    <span class="exam-chip">Autumn 2025 Q6b (5m)</span>
    <span class="exam-chip">Chapter 5 Syllabus</span>
  </div>
</section>

<!-- ========================================== -->
<!-- LESSON 8: HAMILTONIAN CYCLE & TSP          -->
<!-- ========================================== -->
<section class="lesson-card" id="l8" data-title="Hamiltonian Cycle & TSP">
  <div class="lesson-header">
    <div class="lesson-badge">8</div>
    <div class="lesson-titles">
      <div class="lesson-unit">Unit 5 · NP-Complete Reductions</div>
      <h2 class="lesson-title">Hamiltonian Cycle & Travelling Salesperson Problem</h2>
    </div>
  </div>

  <div class="cols-2" style="margin-bottom:14px;">
    <div>
      <h4 style="font:800 16px var(--font-display); color:var(--accent);">Hamiltonian Cycle (HC)</h4>
      <p style="font-size:14px;">Given graph G=(V,E), does there exist a simple cycle visiting every vertex <b>exactly once</b> and returning to start? (NP-complete).</p>
      <p style="font-size:12px; color:var(--muted); margin-top:4px;">Do not confuse with <b>Euler Tour</b> (visits every <i>edge</i> once), which is easily solvable in O(E) in class P!</p>
    </div>
    <div>
      <h4 style="font:800 16px var(--font-display); color:var(--purple);">Decision TSP</h4>
      <p style="font-size:14px;">Given complete graph with edge weights c(u,v) and integer k, is there a tour visiting all cities with total cost ≤ k? (NP-complete).</p>
    </div>
  </div>

  <div class="say-box">
    <b>The Standard Exam Reduction Proof: HC ≤ₚ TSP (Autumn 2024 Q7b - 5 Marks)</b>
    <ol style="padding-left:20px; margin-top:6px;">
      <li><b>Construct complete graph G' on the same vertices V:</b>
        <br>For every pair of vertices (u, v):
        <br>• If (u, v) ∈ E (original edge): set cost c(u, v) = 1 (or 0)
        <br>• If (u, v) ∉ E (non-edge): set cost c(u, v) = 2 (or 1)
        <br>• Set budget threshold k = n (or 0).
      </li>
      <li><b>Correctness:</b>
        <br>• If G has an HC, the same cycle in G' uses n edges of cost 1 ⟹ Total cost = n ≤ k.
        <br>• If G' has a tour of cost ≤ n, since all edges cost ≥ 1, every edge in the tour must cost exactly 1. Hence, the tour uses only original edges of G, yielding a valid Hamiltonian Cycle!
      </li>
    </ol>
  </div>

  <!-- Simulation 8: HC to TSP Tour Builder -->
  <div class="sim-container" id="sim-hc-tsp-container">
    <div class="sim-header">
      <div class="sim-title">🚚 Interactive HC to TSP Tour Builder & Verifier</div>
    </div>
    <div class="row">
      <button class="btn active" id="hc1" aria-pressed="true">Graph 1: Has Hamiltonian Cycle</button>
      <button class="btn" id="hc2" aria-pressed="false">Graph 2: No Hamiltonian Cycle</button>
    </div>
    
    <div class="cols-2" style="margin-top:12px;">
      <div>
        <b>Original Graph G</b>
        <svg class="interactive-fig" id="h1" viewBox="0 0 300 250" role="img" aria-label="Original graph"></svg>
      </div>
      <div>
        <b>TSP Instance (Cost 0 = Solid Teal, Cost 1 = Dashed Red)</b>
        <svg class="interactive-fig" id="h2" viewBox="0 0 300 250" role="img" aria-label="TSP graph"></svg>
      </div>
    </div>
    
    <div class="row" style="margin-top:12px;">
      <button class="btn pri" id="hcb">Find Optimal TSP Tour (Brute Force)</button>
      <button class="btn" id="hcr">Clear Tour</button>
    </div>
    <div class="status-box" id="hcs">Click cities on the right in visiting order to construct a tour.</div>
  </div>

  <div class="exam-pill-strip">
    <span>Asked in:</span>
    <span class="exam-chip">Autumn 2024 Q7b (5m)</span>
  </div>
</section>

<!-- ========================================== -->
<!-- LESSON 9: COPING WITH NP-COMPLETENESS      -->
<!-- ========================================== -->
<section class="lesson-card" id="l9" data-title="Coping with NP-Completeness">
  <div class="lesson-header">
    <div class="lesson-badge">9</div>
    <div class="lesson-titles">
      <div class="lesson-unit">Unit 6 · Coping Strategies</div>
      <h2 class="lesson-title">Six Practical Ways of Handling NP-Complete Problems</h2>
    </div>
  </div>

  <p>In industry and exams (Autumn 2023 Q7a), when a problem is NP-complete, you cannot simply give up. You apply one of <b>six established strategies</b>:</p>

  <div class="cheat-grid" style="margin: 16px 0;">
    <div class="cheat-card">
      <h4>1. Approximation Algorithms</h4>
      <p style="font-size:14px;">Polynomial-time algorithms that guarantee a solution within a provable factor ρ of the optimal answer.</p>
      <p style="font-size:12px; color:var(--muted); margin-top:4px;"><b>Examples:</b> 2-approx Vertex Cover, 2-approx Metric TSP.</p>
    </div>
    <div class="cheat-card">
      <h4>2. Heuristics</h4>
      <p style="font-size:14px;">Intuitive rules of thumb that perform well in practice on typical data, but have no mathematical worst-case guarantee.</p>
      <p style="font-size:12px; color:var(--muted); margin-top:4px;"><b>Examples:</b> Nearest Neighbor for TSP, Greedy search, Simulated Annealing.</p>
    </div>
    <div class="cheat-card">
      <h4>3. Special Cases & Restrictions</h4>
      <p style="font-size:14px;">Restricting input structures to domains where the problem becomes polynomial.</p>
      <p style="font-size:12px; color:var(--muted); margin-top:4px;"><b>Examples:</b> Vertex cover on trees (dynamic programming in O(n)), 2-SAT (linear time).</p>
    </div>
    <div class="cheat-card">
      <h4>4. Dynamic Programming (Small n)</h4>
      <p style="font-size:14px;">Exact exponential algorithms that replace brute-force O(n!) with much faster exponential time.</p>
      <p style="font-size:12px; color:var(--muted); margin-top:4px;"><b>Examples:</b> Held-Karp algorithm for TSP in O(n² 2ⁿ), 0/1 Knapsack pseudo-polynomial DP.</p>
    </div>
    <div class="cheat-card">
      <h4>5. Backtracking & Branch and Bound</h4>
      <p style="font-size:14px;">Systematically searches the solution tree while aggressively pruning branches that cannot beat the current upper/lower bound.</p>
      <p style="font-size:12px; color:var(--muted); margin-top:4px;"><b>Examples:</b> Branch and bound for TSP, 0/1 Knapsack, SAT solvers (CDCL).</p>
    </div>
    <div class="cheat-card">
      <h4>6. Randomized Algorithms</h4>
      <p style="font-size:14px;">Tosses coins to escape local minima or find high-probability good answers.</p>
      <p style="font-size:12px; color:var(--muted); margin-top:4px;"><b>Examples:</b> Random restarts, Monte Carlo algorithms, Karger's Min-Cut.</p>
    </div>
  </div>

  <div class="exam-pill-strip">
    <span>Asked in:</span>
    <span class="exam-chip">Autumn 2023 Q7a (4m)</span>
  </div>
</section>

<!-- ========================================== -->
<!-- LESSON 10: APPROXIMATION ALGORITHMS        -->
<!-- ========================================== -->
<section class="lesson-card" id="l10" data-title="Approximation Algorithms">
  <div class="lesson-header">
    <div class="lesson-badge">10</div>
    <div class="lesson-titles">
      <div class="lesson-unit">Unit 6 · Approximation Algorithms</div>
      <h2 class="lesson-title">Approximation Algorithms: Vertex Cover & Metric TSP</h2>
    </div>
  </div>

  <p>An algorithm has an <b>approximation ratio ρ</b> if for all inputs:
  <div class="code-block" style="text-align:center; font-weight:700; margin:10px 0; color:var(--accent);">max(C / C*, C* / C) ≤ ρ</div>
  For minimization problems, Cost(Algo) ≤ ρ · Cost(OPT).</p>

  <h3 style="margin: 18px 0 8px; font:800 20px var(--font-display);">1. Vertex Cover: 2-Approximation via Maximal Matching</h3>
  <pre class="code-block">APPROX-VERTEX-COVER(G):
1. C = empty set
2. M = empty set (matching)
3. while there are edges in E:
4.     pick any arbitrary edge (u, v) in E
5.     add u and v to C
6.     add (u, v) to M
7.     remove all edges incident to u or v from E
8. return C</pre>

  <div class="say-box">
    <b>Why the Ratio is At Most 2:</b>
    <ul style="padding-left:18px;">
      <li>The edges picked in M share no endpoints (they form a <b>matching</b>).</li>
      <li>Any valid vertex cover (including optimal C^*) MUST pick at least one endpoint from each edge in M. Hence, |C^*| ≥ |M|.</li>
      <li>Our algorithm adds both endpoints: |C| = 2|M|.</li>
      <li>Therefore: |C| = 2|M| ≤ 2|C^*|. The ratio is strictly ≤ 2!</li>
    </ul>
  </div>

  <!-- Simulation 10A: Vertex Cover Approx -->
  <div class="sim-container" id="sim-vc-container">
    <div class="sim-header">
      <div class="sim-title">🛡️ Interactive 2-Approximation for Vertex Cover (Maximal Matching)</div>
    </div>
    <p class="sim-hint">Step through the maximal matching algorithm. Selected matching edges M are highlighted in yellow, while endpoints added to the cover C are highlighted in red.</p>
    <div class="cols-2">
      <svg class="interactive-fig" id="vc-svg" viewBox="0 0 380 260"></svg>
      <div>
        <div class="row">
          <button class="btn pri" id="vc-step-btn">Pick Next Matching Edge</button>
          <button class="btn" id="vc-reset-btn">Reset</button>
        </div>
        <div class="status-box" id="vc-status">Click 'Pick Next Matching Edge' to begin.</div>
        <table class="data-table" id="vc-metrics-table"></table>
      </div>
    </div>
  </div>

  <h3 style="margin: 24px 0 8px; font:800 20px var(--font-display);">2. Metric TSP: 2-Approximation via MST & Preorder Walk</h3>
  <p>Requires the <b>Triangle Inequality</b>: c(u, w) ≤ c(u, v) + c(v, w) for all cities. Without the triangle inequality, general TSP cannot be approximated within ANY constant factor ρ unless P = NP!</p>

  <!-- Simulation 10B: Metric TSP Approx -->
  <div class="sim-container" id="sim-tsp-approx-container">
    <div class="sim-header">
      <div class="sim-title">🗺️ Interactive 2-Approximation for Metric TSP (7 Cities)</div>
      <span class="exam-chip">Autumn 2012 Q7b</span>
    </div>
    <p class="sim-hint">Toggle through the 3 algorithmic steps below to see how MST doubling and preorder shortcutting guarantee a tour ≤ 2 · OPT.</p>
    
    <div class="row">
      <button class="btn active" id="tsp-st1">Step 1: Build MST (Cost 485.6)</button>
      <button class="btn" id="tsp-st2">Step 2: Full Tree Walk (Cost 971.2)</button>
      <button class="btn" id="tsp-st3">Step 3: Preorder Shortcut Tour (Cost 753.2)</button>
    </div>
    
    <div class="cols-2" style="margin-top:12px;">
      <svg class="interactive-fig" id="tsp-approx-svg" viewBox="0 0 380 260"></svg>
      <div>
        <div class="status-box ok" id="tsp-approx-status"></div>
        <table class="data-table" id="tsp-approx-table"></table>
        <div class="say-box" style="margin-top:10px; font-size:13.5px;">
          <b>3-Line Exam Proof:</b><br>
          1. c(T_{MST}) ≤ c(OPT) (dropping one edge from optimal tour gives a spanning tree).<br>
          2. Full tree walk visits every edge twice: c(W) = 2 · c(T_{MST}).<br>
          3. Skipping repeated cities via triangle inequality never adds cost: c(Tour) ≤ c(W) ≤ 2 · c(OPT).
        </div>
      </div>
    </div>
  </div>

  <div class="exam-pill-strip">
    <span>Asked in:</span>
    <span class="exam-chip">Autumn 2012 Q7b (5m)</span>
    <span class="exam-chip">Chapter 6 Syllabus</span>
  </div>
</section>

<!-- ========================================== -->
<!-- LESSON 11: AMORTIZED ANALYSIS: AGGREGATE   -->
<!-- ========================================== -->
<section class="lesson-card" id="l11" data-title="Amortized: Aggregate Method">
  <div class="lesson-header">
    <div class="lesson-badge">11</div>
    <div class="lesson-titles">
      <div class="lesson-unit">Unit 6 · Amortized Analysis</div>
      <h2 class="lesson-title">Amortized Analysis: The Aggregate Method</h2>
    </div>
  </div>

  <p>Amortized analysis guarantees the <b>average performance of each operation in the worst-case sequence of n operations</b>. Unlike average-case analysis, <b>NO probability or random inputs are involved</b>: it is a deterministic guarantee on any sequence!</p>

  <div class="analogy-box">
    <div class="analogy-title">💡 Real-Life Analogy: Annual Gym Membership</div>
    Paying Rs 12,000 once a year feels like a huge single expense (expensive worst-case operation). But spread over 12 months, it is Rs 1,000/month. The big cost is <b>amortized</b> over the cheap months!
  </div>

  <h3 style="margin: 18px 0 8px; font:800 18px var(--font-display);">Case 1: The Binary Counter (Increment)</h3>
  <p>In an k-bit counter, incrementing <code>0111</code> to <code>1000</code> flips 4 bits, which costs O(k). But over n increments:
  <div class="code-block" style="text-align:center; font-weight:700; margin:10px 0; color:var(--accent);">Total Flips = ∑(i=0 to ⌊log₂ n⌋) ⌊n/2ⁱ⌋ &lt; n · ∑(i=0 to ∞) (1/2ⁱ) = 2n</div>
  Amortized cost per increment = T(n)/n < 2n/n = 2 = O(1)!</p>

  <!-- Simulation 11: Binary Counter -->
  <div class="sim-container" id="sim-counter-container">
    <div class="sim-header">
      <div class="sim-title">🔢 Live Binary Counter Flips Simulator</div>
    </div>
    <div class="row">
      <button class="btn pri" id="cnt-step-btn">+1 Increment</button>
      <button class="btn" id="cnt-step10-btn">+10 Increments</button>
      <button class="btn" id="cnt-reset-btn">Reset</button>
    </div>
    
    <div style="display:flex; gap:8px; justify-content:center; margin:14px 0;" id="cnt-bits"></div>
    <div class="status-box ok" id="cnt-status">Value: 0 | Total flips: 0 | Average flips/op: 0.00</div>
    
    <div style="margin-top:10px;">
      <svg class="interactive-fig" id="cnt-svg" viewBox="0 0 420 180" style="max-height:200px;"></svg>
    </div>
  </div>

  <h3 style="margin: 22px 0 8px; font:800 18px var(--font-display);">Case 2: The 2ᵏ Operation Cost Question (Autumn 2024 Q5b - 5 Marks)</h3>
  <div class="say-box">
    <b>Problem Statement:</b> Operation i costs i if i is a power of 2, and 1 otherwise. Show amortized cost is O(1).<br>
    <b>Proof:</b><br>
    1. Sum of expensive operations: 1 + 2 + 4 + 8 + ... + 2ᵐ = 2ᵐ⁺¹ - 1 < 2n.<br>
    2. Sum of cheap operations: at most n operations costing 1 each ≤ n.<br>
    3. Total cost T(n) < 2n + n = 3n.<br>
    4. Amortized cost = T(n)/n < 3n/n ≤ 3 = O(1).
  </div>

  <div class="exam-pill-strip">
    <span>Asked in:</span>
    <span class="exam-chip">Autumn 2024 Q1h (1m)</span>
    <span class="exam-chip">Autumn 2024 Q5b (5m)</span>
    <span class="exam-chip">Autumn 2025 Q3b (4m)</span>
  </div>
</section>

<!-- ========================================== -->
<!-- LESSON 12: ACCOUNTING & POTENTIAL METHODS  -->
<!-- ========================================== -->
<section class="lesson-card" id="l12" data-title="Amortized: Accounting & Potential">
  <div class="lesson-header">
    <div class="lesson-badge">12</div>
    <div class="lesson-titles">
      <div class="lesson-unit">Unit 6 · Amortized Analysis</div>
      <h2 class="lesson-title">Accounting Method, Piggy Banks, & The Shopkeeper Question</h2>
    </div>
  </div>

  <p>In the <b>Accounting Method</b>, we charge each operation an amortized fee ĉᵢ:</p>
  <ul style="margin: 8px 0 14px 24px;">
    <li>If ĉᵢ > c_i (actual cost), the excess is deposited into a <b>bank account (credit)</b> associated with specific data items.</li>
    <li>If ĉᵢ < c_i, the deficit is withdrawn from the bank account to pay for the expensive operation.</li>
    <li><b>Crucial Invariant:</b> The bank balance must <b>NEVER go negative</b> at any step!
    <div class="code-block" style="text-align:center; font-weight:700; margin:10px 0; color:var(--accent);">∑(i=1 to n) ĉᵢ − ∑(i=1 to n) cᵢ ≥ 0  ⟹  Total Actual Cost ≤ ∑(i=1 to n) ĉᵢ</div>
    </li>
  </ul>

  <!-- Simulation 12: Shopkeeper Doubling Array -->
  <div class="sim-container" id="sim-array-container">
    <div class="sim-header">
      <div class="sim-title">🏦 The Shopkeeper & Doubling Array Piggy Bank (Autumn 2024 Q6a - 5 Marks)</div>
    </div>
    <p class="sim-hint">Array doubles when full. Customer pays Rs 5 per sale: Rs 2 pays the insertion, Rs 3 is stored in the bank. Watch how the bank pays for the expensive copy spikes when the array doubles!</p>
    
    <div class="row">
      <button class="btn pri" id="arr-insert-btn">Insert Customer Sale (+1)</button>
      <button class="btn" id="arr-insert10-btn">Insert 10 Sales</button>
      <button class="btn" id="arr-reset-btn">Reset</button>
    </div>
    
    <div class="row" style="margin:12px 0;">
      <div style="background:var(--sunk); padding:8px 14px; border-radius:8px; font-weight:700;">Array Size: <span id="arr-size" class="mono" style="color:var(--accent);">0</span> / Capacity: <span id="arr-cap" class="mono">1</span></div>
      <div style="background:var(--amber-soft); padding:8px 14px; border-radius:8px; font-weight:700;">Piggy Bank Credit: <span id="arr-credit" class="mono" style="color:var(--mark-ink);">Rs 0</span></div>
    </div>
    
    <div id="arr-blocks" style="display:flex; flex-wrap:wrap; gap:4px; margin:12px 0;"></div>
    <div class="status-box" id="arr-status">Insert sales to observe array doubling and bank credit.</div>
    
    <div style="margin-top:12px;">
      <svg class="interactive-fig" id="arr-svg" viewBox="0 0 420 180" style="max-height:210px;"></svg>
    </div>
  </div>

  <div class="exam-pill-strip">
    <span>Asked in:</span>
    <span class="exam-chip">Autumn 2024 Q6a (5m)</span>
    <span class="exam-chip">Autumn 2025 Q3a/b (10m)</span>
  </div>
</section>

<!-- ========================================== -->
<!-- LESSON 13: RANDOMIZED ALGORITHMS           -->
<!-- ========================================== -->
<section class="lesson-card" id="l13" data-title="Las Vegas vs Monte Carlo">
  <div class="lesson-header">
    <div class="lesson-badge">13</div>
    <div class="lesson-titles">
      <div class="lesson-unit">Unit 6 · Randomized Algorithms</div>
      <h2 class="lesson-title">Randomized Algorithms: Las Vegas vs Monte Carlo</h2>
    </div>
  </div>

  <p>A randomized algorithm tosses coins during execution. This prevents an adversary from designing a fixed worst-case input. There are two fundamentally distinct types:</p>

  <div class="cols-2" style="margin: 16px 0;">
    <div style="background:var(--accent-soft); border-radius:12px; padding:16px;">
      <h4 style="font:800 16px var(--font-display); color:var(--accent-hover);">Las Vegas Algorithm</h4>
      <ul style="padding-left:18px; font-size:14px; margin-top:6px;">
        <li><b>Correctness:</b> ALWAYS produces the 100% correct answer upon termination.</li>
        <li><b>Running Time:</b> Random variable (we compute the <i>expected</i> time).</li>
        <li><b>If Unlucky:</b> Simply runs longer (never outputs a wrong answer).</li>
        <li><b>Examples:</b> Randomized Quicksort, Randomized Selection (Quickselect).</li>
      </ul>
    </div>
    <div style="background:var(--hard-soft); border-radius:12px; padding:16px;">
      <h4 style="font:800 16px var(--font-display); color:var(--hard);">Monte Carlo Algorithm</h4>
      <ul style="padding-left:18px; font-size:14px; margin-top:6px;">
        <li><b>Correctness:</b> May output an incorrect answer with small probability ε.</li>
        <li><b>Running Time:</b> Fixed / deterministic bound.</li>
        <li><b>Error Reduction:</b> Repeating k times shrinks error to ε^k (e.g. (1/2)ᵏ or (1/4)ᵏ).</li>
        <li><b>Examples:</b> Miller-Rabin Primality Test, Monte Carlo π Estimation, Karger's Min-Cut.</li>
      </ul>
    </div>
  </div>

  <!-- Simulation 13: Monte Carlo Pi Dartboard -->
  <div class="sim-container" id="sim-mc-container">
    <div class="sim-header">
      <div class="sim-title">🎯 Live Canvas Lab: Monte Carlo π Dartboard Simulation</div>
    </div>
    <p class="sim-hint">Throw random points into a unit square. The fraction landing inside the quarter circle (x² + y² ≤ 1) is π / 4. Therefore π ≈ 4 × frac{Hits}{Total}.</p>
    
    <div class="cols-2">
      <canvas class="sim-canvas" id="pi-canvas" width="300" height="300"></canvas>
      <div>
        <div class="row">
          <button class="btn pri" id="pi-throw100-btn">Throw 500 Darts</button>
          <button class="btn" id="pi-throw5000-btn">Throw 5,000 Darts</button>
          <button class="btn" id="pi-reset-btn">Reset</button>
        </div>
        <div class="status-box ok" id="pi-status">Darts: 0 | Hits: 0 | Estimated π: 0.0000</div>
        <table class="data-table" id="pi-table" style="margin-top:10px;"></table>
      </div>
    </div>
  </div>

  <div class="exam-pill-strip">
    <span>Asked in:</span>
    <span class="exam-chip">Autumn 2024 Q1i (1m)</span>
    <span class="exam-chip">Autumn 2025 Q1b (1m)</span>
  </div>
</section>

<!-- ========================================== -->
<!-- LESSON 14: RANDOMIZED QUICKSORT & DUEL     -->
<!-- ========================================== -->
<section class="lesson-card" id="l14" data-title="Randomized Quicksort">
  <div class="lesson-header">
    <div class="lesson-badge">14</div>
    <div class="lesson-titles">
      <div class="lesson-unit">Unit 6 · Randomized Quicksort</div>
      <h2 class="lesson-title">Randomized Quicksort & The Ramesh vs Suresh Showdown</h2>
    </div>
  </div>

  <p>Deterministic Quicksort with the last element as pivot degrades to Θ(n²) on already-sorted arrays. <b>Randomized Quicksort</b> swaps a uniformly chosen random element with the last element before calling <code>PARTITION</code>.</p>

  <div class="say-box">
    <b>Expected Time Derivation:</b>
    <div class="code-block" style="text-align:center; font-weight:700; margin:10px 0; color:var(--accent);">E[T(n)] = (2/n) · ∑(k=0 to n−1) E[T(k)] + cn = Θ(n log n) ≈ 2n ln n ≈ 1.39 n log₂ n</div>
    <b>Good Splits Intuition:</b> With probability 1/2, the pivot lands in the middle half of elements (a split no worse than 3n/4). On average, every 2 levels shrinks problem size to 3/4 ⟹ ≈ 2.4 log₂ n levels, with O(n) work per level ⟹ O(n log n).
  </div>

  <div class="exam-trap-box">
    <div class="exam-trap-title">🎯 THE FAMOUS EXAM TRICK: Ramesh vs Suresh (Autumn 2024 Q6b - 5 Marks)</div>
    <b>Question:</b> Ramesh picks the last element as pivot. Suresh picks a random element as pivot. Whose algorithm has the lesser worst-case time complexity? Prove.<br>
    <b>Answer:</b> <b>NEITHER! BOTH HAVE WORST-CASE TIME COMPLEXITY Θ(n²)!</b><br>
    <b>Proof:</b> For Suresh, there exists a tiny probability sequence of random draws that picks the maximum or minimum element at every single partition step. Under that unlucky sequence, Suresh's recurrence is also T(n) = T(n-1) + n = Θ(n²). Randomization improves the <i>expected</i> time to O(n log n) on ALL inputs, but does NOT alter the mathematical worst case!
  </div>

  <!-- Simulation 14: Quicksort Duel -->
  <div class="sim-container" id="sim-duel-container">
    <div class="sim-header">
      <div class="sim-title">⚔️ The Quicksort Duel: Ramesh (Deterministic) vs Suresh (Random Pivot)</div>
    </div>
    <p class="sim-hint">Select an array configuration of n = 50 elements. Watch Ramesh choke on sorted inputs while Suresh breezily finishes in O(n log n) comparisons!</p>
    
    <div class="row">
      <button class="btn active" id="duel-sorted">Input: Already Sorted Array</button>
      <button class="btn" id="duel-reverse">Input: Reverse Sorted Array</button>
      <button class="btn" id="duel-random">Input: Random Array</button>
    </div>
    <div class="row" style="margin-top:10px;">
      <button class="btn pri" id="duel-run-btn">Run Duel Benchmark</button>
      <button class="btn" id="duel-multi-btn">Simulate 100 Random Runs for Suresh</button>
    </div>
    
    <div class="cols-2" style="margin-top:14px;">
      <div>
        <table class="data-table" id="duel-table"></table>
      </div>
      <div>
        <svg class="interactive-fig" id="duel-svg" viewBox="0 0 380 200" style="max-height:220px;"></svg>
      </div>
    </div>
  </div>

  <div class="exam-pill-strip">
    <span>Asked in:</span>
    <span class="exam-chip">Spring 2024 Q3b (5m)</span>
    <span class="exam-chip">Autumn 2024 Q6b (5m)</span>
  </div>
</section>

<!-- ========================================== -->
<!-- LESSON 15: MASTER QUESTION BANK            -->
<!-- ========================================== -->
<section class="lesson-card" id="l15" data-title="Master PYQ Bank (All 32)">
  <div class="lesson-header">
    <div class="lesson-badge">15</div>
    <div class="lesson-titles">
      <div class="lesson-unit">Unit 7 · Comprehensive Question Bank</div>
      <h2 class="lesson-title">Master Question Bank: Every Exam Question from 2012–2025</h2>
    </div>
  </div>

  <p>Here is every single question asked on DAA Units 5–6 across 26 past question papers, with paper names, marks, short answers, and expandable 8–10 line model solutions:</p>

  <div class="row" style="margin-bottom:14px;">
    <input type="search" id="pyq-search-input" placeholder="Search by question text, paper, or keyword..." style="flex:2; padding:9px 12px; border-radius:10px; border:1.5px solid var(--line); background:var(--surface);">
    <select id="pyq-topic-filter" style="flex:1; padding:9px 12px; border-radius:10px; border:1.5px solid var(--line); background:var(--surface);">
      <option value="all">All Topics (32 Questions)</option>
      <option value="amortized">Amortized Analysis (5 Qs)</option>
      <option value="randomized">Randomized Algorithms (4 Qs)</option>
      <option value="complexity">P, NP, NP-Hard, NPC (17 Qs)</option>
      <option value="reductions">Reductions & 3-SAT (2 Qs)</option>
      <option value="clique">Clique Problem (2 Qs)</option>
      <option value="hamiltonian">Hamiltonian & TSP (1 Q)</option>
      <option value="approximation">Approximation Algorithms (1 Q)</option>
    </select>
  </div>

  <div id="pdf-qbank-list"></div>
</section>

<!-- ========================================== -->
<!-- LESSON 16: INTERACTIVE EXAM MCQS           -->
<!-- ========================================== -->
<section class="lesson-card" id="l16" data-title="Interactive Exam MCQs">
  <div class="lesson-header">
    <div class="lesson-badge">16</div>
    <div class="lesson-titles">
      <div class="lesson-unit">Unit 7 · Active Recall</div>
      <h2 class="lesson-title">Interactive Exam MCQs & Tricky Reduction Traps</h2>
    </div>
  </div>

  <p>Test yourself on the exact 1-mark and 2-mark MCQs from past exams. Click an option for immediate feedback and full reasoning:</p>
  <div id="mcq-trainer-list"></div>
</section>

<!-- ========================================== -->
<!-- LESSON 17: ONE-PAGE CHEAT SHEET            -->
<!-- ========================================== -->
<section class="lesson-card" id="l17" data-title="One-Page Cheat Sheet">
  <div class="lesson-header">
    <div class="lesson-badge">17</div>
    <div class="lesson-titles">
      <div class="lesson-unit">Unit 7 · High-Yield Summary</div>
      <h2 class="lesson-title">One-Page Exam-Night Master Cheat Sheet</h2>
    </div>
  </div>

  <div class="cheat-grid">
    <div class="cheat-card">
      <h4>Amortized Analysis</h4>
      <ul>
        <li><b>Idea:</b> Guaranteed worst-case average over n operations. No probability!</li>
        <li><b>Aggregate:</b> T(n)/n. Stack Multipop ≤ 2n/n = O(1). Binary Counter < 2n/n = O(1).</li>
        <li><b>Accounting:</b> ∑ ĉᵢ ≥ ∑ c_i (bank ≥ 0). Doubling array: charge Rs 5 (Rs 2 write, Rs 3 bank).</li>
        <li><b>Push Digits at 2ᵏ:</b> updates cost i-1 at powers of 2. Total < 3n ⟹ O(1).</li>
      </ul>
    </div>
    <div class="cheat-card">
      <h4>Randomized Algorithms</h4>
      <ul>
        <li><b>Las Vegas:</b> ALWAYS correct output; time is a random variable. (Randomized Quicksort).</li>
        <li><b>Monte Carlo:</b> Bounded time; small error probability ε. Repeat k times → ε^k. (Miller-Rabin, π darts).</li>
        <li><b>Rand Quicksort:</b> Expected O(n log n) ≈ 2n ln n. Worst case is still O(n²).</li>
        <li><b>Ramesh vs Suresh:</b> BOTH have Θ(n²) worst case! Random pivot improves expected time only.</li>
      </ul>
    </div>
    <div class="cheat-card">
      <h4>Complexity Classes</h4>
      <ul>
        <li><b>P:</b> Solvable in polynomial time deterministically. (Dijkstra, Kruskal, 2-SAT).</li>
        <li><b>NP:</b> Verifiable in polynomial time with certificate. P ⊆ NP.</li>
        <li><b>NP-Hard:</b> Every problem in NP reduces to it. (Halting problem, TSP optimization).</li>
        <li><b>NP-Complete:</b> In NP and NP-Hard. First problem: Circuit-SAT (Cook's theorem).</li>
        <li><b>If ANY NPC problem gets poly solution:</b> P = NP.</li>
      </ul>
    </div>
    <div class="cheat-card">
      <h4>Reductions & The Famous Chain</h4>
      <ul>
        <li><b>Reduction A ≤ₚ B:</b> B in P ⟹ A in P; A NP-hard ⟹ B NP-hard.</li>
        <li><b>Direction Trap:</b> Known NP-hard ≤ₚ New proves New is NP-hard.</li>
        <li><b>Chain:</b> Circuit-SAT → SAT → 3-SAT → Clique → Vertex Cover → HC → TSP.</li>
        <li><b>Triad:</b> Clique in G ⟺ Indep Set in Ḡ ⟺ Vertex Cover of size n-k in Ḡ.</li>
      </ul>
    </div>
    <div class="cheat-card">
      <h4>Approximations</h4>
      <ul>
        <li><b>Vertex Cover 2-Approx:</b> Maximal matching edges M, cover C = 2|M|. Since |OPT| ≥ |M| ⟹ |C| ≤ 2 · |OPT|.</li>
        <li><b>Metric TSP 2-Approx:</b> Prim/Kruskal MST → full walk (2 · MST) → preorder shortcutting. Cost ≤ 2 · MST ≤ 2 · OPT.</li>
        <li><b>Christofides Algorithm:</b> 1.5-approximation for metric TSP (MST + minimum weight perfect matching on odd-degree vertices).</li>
        <li><b>General TSP:</b> Has NO constant factor approximation unless P = NP.</li>
      </ul>
    </div>
    <div class="cheat-card">
      <h4>Verification Algorithms</h4>
      <ul>
        <li><b>Clique ∈ NP:</b> Certificate is set of k vertices. Check all C(k, 2) pairs share an edge. Time O(k²) ≤ O(n²).</li>
        <li><b>TSP ∈ NP:</b> Certificate is vertex sequence. Check all n visited and sum weights ≤ k. Time O(n).</li>
        <li><b>Vertex Cover ∈ NP:</b> Certificate is k vertices. Check all E edges touched. Time O(E).</li>
      </ul>
    </div>
  </div>
</section>
"""

print("site_lessons.py created.")

