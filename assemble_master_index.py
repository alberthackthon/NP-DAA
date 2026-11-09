# assemble_master_index.py
"""
Assembles index.html for NP & DAA Made Simple Master Suite.
"""

import json
from site_styles import CSS_CONTENT
from site_lessons import LESSONS_HTML
from site_scripts import SCRIPTS_JS
from create_data import PDF_32_QUESTIONS

# Read PYQ_DATABASE JS block
with open('pyq_db_block.js', 'r', encoding='utf-8') as f:
    pyq_db_js = f.read()

# Serialize PDF_32_QUESTIONS as JSON
pdf_questions_json = json.dumps(PDF_32_QUESTIONS)

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>NP & Advanced DAA Made Simple | Interactive Simulation & PYQ Atlas Suite</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=JetBrains+Mono:wght@500;700&display=swap">
  <style>
/* CSS_CONTENT_PLACEHOLDER */
  </style>
</head>
<body>

<!-- Master Sticky Header -->
<header class="topbar">
  <div class="topbar-wrap">
    <div class="brand-area">
      <div class="brand-logo">NP</div>
      <div>
        <div class="brand-title">NP & Advanced DAA <span style="color:var(--accent);">Made Simple</span></div>
        <div class="brand-subtitle">Interactive Simulations, Deep Theory & Complete PYQ Atlas</div>
      </div>
    </div>
    
    <nav class="mode-tabs" role="tablist" aria-label="Views">
      <button class="mode-tab active" data-view="course" role="tab">📘 Master Course</button>
      <button class="mode-tab" data-view="simlab" role="tab">⚡ Simulation Lab</button>
      <button class="mode-tab" data-view="pyq" role="tab">🗺️ PYQ Atlas & Bank</button>
      <button class="mode-tab" data-view="mcq" role="tab">🎯 Exam Traps & MCQs</button>
      <button class="mode-tab" data-view="cheat" role="tab">📑 1-Page Cheat Sheet</button>
    </nav>
    
    <div class="top-controls">
      <div class="progress-widget" title="Course Completion Progress">
        <div class="progress-bar"><div class="progress-fill" id="prog-bar-fill"></div></div>
        <span id="prog-text">0%</span>
      </div>
      
      <div class="theme-picker" aria-label="Theme selector">
        <button class="theme-btn active" data-theme="light" title="Light Mode">☀️</button>
        <button class="theme-btn" data-theme="dark" title="Dark Mode">🌙</button>
        <button class="theme-btn" data-theme="sepia" title="Sepia Mode">📖</button>
      </div>
    </div>
  </div>
</header>

<div class="page-container">
  
  <!-- ============================================== -->
  <!-- VIEW 1: MASTER COURSE (17 UNITS WITH SIDEBAR)   -->
  <!-- ============================================== -->
  <main id="view-course">
    <header class="hero">
      <h1>Amortized, Randomized, and <span class="hl">NP-Hard</span> Made Simple</h1>
      <p class="lead">Every single concept from DAA Units 5 & 6 taught through plain-English explanations, real-life analogies, interactive clickable simulations, and exact model answers for every question from 26 past exam papers.</p>
      
      <div class="stat-pills">
        <div class="stat-pill"><b>17</b><span>Deep-Dive Lessons</span></div>
        <div class="stat-pill"><b>14</b><span>Interactive Live Simulators</span></div>
        <div class="stat-pill"><b>32</b><span>Exam PYQs with Solutions</span></div>
        <div class="stat-pill"><b>100%</b><span>Units 5 & 6 Syllabus Coverage</span></div>
      </div>
    </header>

    <div class="course-layout">
      <aside class="toc-sidebar">
        <h3>Curriculum Index</h3>
        <div id="toc-sidebar-items"></div>
      </aside>
      
      <div class="lessons-stream">
/* LESSONS_HTML_PLACEHOLDER */
      </div>
    </div>
  </main>

  <!-- ============================================== -->
  <!-- VIEW 2: SIMULATION LAB (ALL 14 SIMS)           -->
  <!-- ============================================== -->
  <main id="view-simlab" style="display:none;">
    <header class="hero">
      <h1>Interactive <span class="hl">Simulation Lab</span></h1>
      <p class="lead">Hands-on visual playgrounds for every complex algorithmic concept. Experiment with inputs, test certificates, watch running averages settle, and explore reduction pipelines.</p>
    </header>
    
    <div class="cheat-grid" style="margin-bottom:24px;">
      <a href="#l1" onclick="switchView('course');" class="cheat-card" style="text-decoration:none; color:inherit;">
        <h4>⚡ 1. Growth Rates & Time Complexity</h4>
        <p style="font-size:14px;">Log-scale growth curve comparing n, n log n, n², n³, 2ⁿ, n! with computer clock steps.</p>
      </a>
      <a href="#l3" onclick="switchView('course');" class="cheat-card" style="text-decoration:none; color:inherit;">
        <h4>🔍 2. Clique Polynomial Verifier</h4>
        <p style="font-size:14px;">Interactive 7-vertex graph tester demonstrating O(k²) verification vs binomial brute-force search.</p>
      </a>
      <a href="#l4" onclick="switchView('course');" class="cheat-card" style="text-decoration:none; color:inherit;">
        <h4>📊 3. Complexity Classes Venn Diagram</h4>
        <p style="font-size:14px;">Explore P ≠ NP, P = NP, and the Autumn 2022 Q1e clique polynomial collapse.</p>
      </a>
      <a href="#l5" onclick="switchView('course');" class="cheat-card" style="text-decoration:none; color:inherit;">
        <h4>⚖️ 4. Reduction Rules Matrix</h4>
        <p style="font-size:14px;">Test deductions and avoid exam direction traps on polynomial reductions A ≤p B.</p>
      </a>
      <a href="#l6" onclick="switchView('course');" class="cheat-card" style="text-decoration:none; color:inherit;">
        <h4>🧩 5. 3-CNF SAT Circuit & Truth Table</h4>
        <p style="font-size:14px;">Toggle boolean inputs, view clause satisfaction states, and inspect full truth tables.</p>
      </a>
      <a href="#l7" onclick="switchView('course');" class="cheat-card" style="text-decoration:none; color:inherit;">
        <h4>🔄 6. The Triad: Dual-Graph Explorer</h4>
        <p style="font-size:14px;">Synchronized visualization of Graph G and Complement G-bar testing Clique, Independent Set, and Vertex Cover.</p>
      </a>
      <a href="#l8" onclick="switchView('course');" class="cheat-card" style="text-decoration:none; color:inherit;">
        <h4>🚚 7. Hamiltonian Cycle to TSP Tour Builder</h4>
        <p style="font-size:14px;">Build tours on the complete reduction graph with costs 0 and 1; verify if total cost ≤ k.</p>
      </a>
      <a href="#l10" onclick="switchView('course');" class="cheat-card" style="text-decoration:none; color:inherit;">
        <h4>🛡️ 8. Vertex Cover 2-Approximation</h4>
        <p style="font-size:14px;">Step through the maximal matching algorithm and verify that |C| = 2|M| ≤ 2 · |OPT|.</p>
      </a>
      <a href="#l10" onclick="switchView('course');" class="cheat-card" style="text-decoration:none; color:inherit;">
        <h4>🗺️ 9. Metric TSP 2-Approximation</h4>
        <p style="font-size:14px;">3-step walkthrough: Prim MST, full tree walk, and triangle inequality preorder shortcut tour.</p>
      </a>
      <a href="#l11" onclick="switchView('course');" class="cheat-card" style="text-decoration:none; color:inherit;">
        <h4>🔢 10. Amortized Binary Counter</h4>
        <p style="font-size:14px;">Step through bit increments and observe flips-per-bit settling to guaranteed &lt; 2.0 flips/op.</p>
      </a>
      <a href="#l12" onclick="switchView('course');" class="cheat-card" style="text-decoration:none; color:inherit;">
        <h4>🏦 11. Shopkeeper Doubling Array</h4>
        <p style="font-size:14px;">Simulate customer sales, capacity doubling spikes, and bank credit ensuring positive balance.</p>
      </a>
      <a href="#l13" onclick="switchView('course');" class="cheat-card" style="text-decoration:none; color:inherit;">
        <h4>🎯 12. Monte Carlo π Dartboard</h4>
        <p style="font-size:14px;">Throw thousands of random points onto a canvas to estimate π and analyze error reduction.</p>
      </a>
      <a href="#l14" onclick="switchView('course');" class="cheat-card" style="text-decoration:none; color:inherit;">
        <h4>⚔️ 13. Quicksort Duel: Ramesh vs Suresh</h4>
        <p style="font-size:14px;">Benchmark deterministic vs random pivot on sorted inputs, proving both worst-case Θ(n²).</p>
      </a>
    </div>
  </main>

  <!-- ============================================== -->
  <!-- VIEW 3: PYQ ATLAS & QUESTION BANK              -->
  <!-- ============================================== -->
  <main id="view-pyq" style="display:none;">
    <header class="hero">
      <h1>PYQ <span class="hl">Atlas</span> & Question Vault</h1>
      <p class="lead">Past-year end-semester questions across 6 core subjects. Filter by topic, search questions, view recurring frequency metrics, and check official paper heatmaps.</p>
    </header>
    
    <nav class="row" id="atlas-subject-nav" style="margin-bottom:16px;"></nav>
    
    <div style="background:var(--surface); border:1.5px solid var(--line); border-radius:16px; padding:20px; margin-bottom:20px;">
      <h2 id="atlas-title" style="font:800 24px var(--font-display); margin-bottom:4px;"></h2>
      <p id="atlas-desc" style="color:var(--muted); font-size:14px; margin-bottom:16px;"></p>
      
      <div class="row">
        <input type="search" id="atlas-search-input" placeholder="Search questions in this subject..." style="flex:2; padding:9px 12px; border-radius:10px; border:1.5px solid var(--line); background:var(--surface);">
        <select id="atlas-topic-select" style="flex:1; padding:9px 12px; border-radius:10px; border:1.5px solid var(--line); background:var(--surface);"></select>
        <span class="exam-chip" id="atlas-count-badge" style="font-size:13px; padding:6px 12px;"></span>
      </div>
      
      <h4 style="font:800 16px var(--font-display); margin:20px 0 8px;">Topic Frequency by Exam Session (Heatmap)</h4>
      <div id="atlas-heatmap-area"></div>
      
      <h4 style="font:800 16px var(--font-display); margin:24px 0 12px;">Questions & Solution Blueprints</h4>
      <div id="atlas-questions-list"></div>
    </div>
  </main>

  <!-- ============================================== -->
  <!-- VIEW 4: EXAM TRAPS & MCQS                      -->
  <!-- ============================================== -->
  <main id="view-mcq" style="display:none;">
    <header class="hero">
      <h1>Exam Traps & <span class="hl">MCQ Trainer</span></h1>
      <p class="lead">Real 1-mark and 2-mark questions from recent university exams (2021–2025). Test your understanding of reductions, amortized methods, and algorithm classifications with instant feedback.</p>
    </header>
    
    <div id="mcq-trainer-view-list"></div>
  </main>

  <!-- ============================================== -->
  <!-- VIEW 5: 1-PAGE CHEAT SHEET                     -->
  <!-- ============================================== -->
  <main id="view-cheat" style="display:none;">
    <header class="hero">
      <h1>Ultimate 1-Page <span class="hl">Cheat Sheet</span></h1>
      <p class="lead">Everything you need to know for DAA Units 5 & 6 compressed onto a single page. High-yield formulas, reduction directions, approximations, and verification algorithms.</p>
    </header>
    
    <div class="cheat-grid">
      <div class="cheat-card">
        <h4>Amortized Analysis</h4>
        <ul>
          <li><b>Definition:</b> Guaranteed average cost per operation over any worst-case sequence of n operations. (No probability involved!).</li>
          <li><b>Aggregate Method:</b> Find total cost T(n) for n operations, divide: T(n)/n.</li>
          <li><b>Binary Counter:</b> Bit i flips ⌊n/2ⁱ⌋ times. Total flips &lt; 2n. Amortized cost &lt; 2 = O(1).</li>
          <li><b>Accounting Method:</b> Assign amortized charge ĉ_i. Difference ĉ_i - c_i stored as credit in bank. Invariant: Bank balance ≥ 0 always!</li>
          <li><b>Doubling Array:</b> Charge Rs 5 (Rs 2 write, Rs 3 bank). Bank pays all copy spikes. Amortized cost O(1).</li>
          <li><b>Push Digits at 2ᵏ:</b> Updates cost i-1 at powers of 2. Total cost &lt; 3n ⟹ O(1).</li>
        </ul>
      </div>

      <div class="cheat-card">
        <h4>Randomized Algorithms</h4>
        <ul>
          <li><b>Las Vegas:</b> ALWAYS correct result; running time is a random variable. Example: Randomized Quicksort, Quickselect.</li>
          <li><b>Monte Carlo:</b> Deterministic/bounded running time; small error probability ε. Repeat k independent runs to shrink error to ε^k. Example: Miller-Rabin, π estimation.</li>
          <li><b>Rand Quicksort:</b> Expected comparisons ≈ 2n ln n ≈ 1.39 n log₂ n = Θ(n log n).</li>
          <li><b>Ramesh vs Suresh Trap:</b> BOTH algorithms have worst-case Θ(n²)! Randomization does not change the worst-case bound; it makes the worst-case exponentially improbable.</li>
        </ul>
      </div>

      <div class="cheat-card">
        <h4>Complexity Classes</h4>
        <ul>
          <li><b>P:</b> Decision problems solvable in deterministic polynomial time O(nᶜ). (Dijkstra, Kruskal, 2-SAT).</li>
          <li><b>NP:</b> Decision problems verifiable in deterministic polynomial time given a certificate. P ⊆ NP.</li>
          <li><b>NP-Hard:</b> At least as hard as every problem in NP. (Halting problem, Optimization TSP).</li>
          <li><b>NP-Complete (NPC):</b> Hardest problems in NP (NPC = NP ∩ NP-hard). Cook's theorem: Circuit-SAT was first NPC.</li>
          <li><b>If ANY NPC problem gets a polynomial solution:</b> P = NP.</li>
        </ul>
      </div>

      <div class="cheat-card">
        <h4>Reduction Rules (A ≤p B)</h4>
        <ul>
          <li><b>Rule 1:</b> B ∈ P ⟹ A ∈ P. (If easy on right, easy on left).</li>
          <li><b>Rule 2:</b> A is NP-hard ⟹ B is NP-hard. (Hardness moves right).</li>
          <li><b>Rule 3 (TRAP):</b> B is NP-hard ⟹ NOTHING about A.</li>
          <li><b>Rule 4 (TRAP):</b> A ∈ P ⟹ NOTHING about B.</li>
          <li><b>Rule 5:</b> B ∈ NP ⟹ A ∈ NP.</li>
          <li><b>Rule 6:</b> A ∈ NPC and B ∈ NP ⟹ B ∈ NPC.</li>
          <li><b>Chain:</b> Circuit-SAT ➔ SAT ➔ 3-SAT ➔ Clique ➔ Vertex Cover ➔ HC ➔ TSP.</li>
        </ul>
      </div>

      <div class="cheat-card">
        <h4>Approximation Algorithms</h4>
        <ul>
          <li><b>Ratio ρ:</b> Cost(Algo) ≤ ρ · Cost(OPT) for minimization.</li>
          <li><b>Vertex Cover 2-Approx:</b> Pick maximal matching edges M, add both endpoints to C = 2|M|. Since |OPT| ≥ |M| ⟹ |C| ≤ 2 · |OPT|.</li>
          <li><b>Metric TSP 2-Approx:</b> Compute Prim/Kruskal MST T ⟹ full tree walk 2 · MST ⟹ preorder shortcut tour. Tour ≤ 2 · MST ≤ 2 · OPT.</li>
          <li><b>Christofides Algorithm:</b> 1.5-approximation for metric TSP using MST + minimum-weight perfect matching on odd-degree vertices.</li>
          <li><b>General TSP:</b> Has NO constant-factor approximation unless P = NP.</li>
        </ul>
      </div>

      <div class="cheat-card">
        <h4>Verification Algorithms</h4>
        <ul>
          <li><b>Clique ∈ NP:</b> Certificate = subset S of k vertices. Check |S| = k and check all k(k-1)/2 pairs share an edge. Time O(k²) ≤ O(n²).</li>
          <li><b>Decision TSP ∈ NP:</b> Certificate = sequence of n cities. Check all cities distinct, sum n edge costs, check ≤ k. Time O(n).</li>
          <li><b>Vertex Cover ∈ NP:</b> Certificate = subset of k vertices. Check all E edges have at least one endpoint in S. Time O(E).</li>
          <li><b>3-SAT ∈ NP:</b> Certificate = truth assignment to variables. Evaluate all m clauses. Time O(m).</li>
        </ul>
      </div>
    </div>
  </main>

  <footer style="margin-top:60px; padding-top:20px; border-top:1px solid var(--line); color:var(--muted); font-size:13px; text-align:center;">
    Built for KIIT School of Computer Engineering · DAA Units 5 & 6 Master Revision Suite · Sourced from 26 Question Papers (2012–2025).
  </footer>
</div>

<script>
/* PYQ_DB_PLACEHOLDER */
const PDF_32_QUESTIONS = /* PDF_QUESTIONS_PLACEHOLDER */;
/* SCRIPTS_JS_PLACEHOLDER */
// Wire up duplicate containers for secondary views
if ($('mcq-trainer-view-list')) {
  $('mcq-trainer-view-list').innerHTML = $('mcq-trainer-list').innerHTML;
}
</script>

</body>
</html>
"""

final_html = TEMPLATE.replace('/* CSS_CONTENT_PLACEHOLDER */', CSS_CONTENT)
final_html = final_html.replace('/* LESSONS_HTML_PLACEHOLDER */', LESSONS_HTML)
final_html = final_html.replace('/* PYQ_DB_PLACEHOLDER */', pyq_db_js)
final_html = final_html.replace('/* PDF_QUESTIONS_PLACEHOLDER */', pdf_questions_json)
final_html = final_html.replace('/* SCRIPTS_JS_PLACEHOLDER */', SCRIPTS_JS)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Successfully generated index.html ({len(final_html):,} bytes).")
