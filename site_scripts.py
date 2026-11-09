# site_scripts.py
# All interactive simulation engines, PYQ Atlas engine, MCQ trainer, and UI controllers

SCRIPTS_JS = """
// ==========================================
// CORE HELPERS & UTILITIES
// ==========================================
const NS = 'http://www.w3.org/2000/svg';
const $ = id => document.getElementById(id);
function S(tag, attrs, parent, text) {
  const e = document.createElementNS(NS, tag);
  for (const k in (attrs || {})) e.setAttribute(k, attrs[k]);
  if (text != null) e.textContent = text;
  if (parent) parent.appendChild(e);
  return e;
}
function H(tag, cls, txt, parent) {
  const e = document.createElement(tag);
  if (cls) e.className = cls;
  if (txt != null) e.textContent = txt;
  if (parent) parent.appendChild(e);
  return e;
}
const sup = s => String(s).replace(/[-0-9+]/g, c => ({'-':'⁻','+':'','0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹'}[c]));
function fmt(x) {
  if (x < 1e6) return Math.round(x).toLocaleString('en-US');
  const [m, e] = x.toExponential(1).split('e');
  return m + ' × 10' + sup(parseInt(e, 10));
}
function human(sec) {
  if (sec < 1e-3) return 'instant';
  if (sec < 1) return 'under a second';
  if (sec < 60) return sec.toFixed(1) + ' sec';
  if (sec < 3600) return (sec / 60).toFixed(1) + ' min';
  if (sec < 86400) return (sec / 3600).toFixed(1) + ' hours';
  if (sec < 31557600) return (sec / 86400).toFixed(1) + ' days';
  const y = sec / 31557600;
  if (y > 1.4e10) return 'longer than universe age';
  if (y < 1e6) return Math.round(y).toLocaleString('en-US') + ' years';
  return fmt(y) + ' years';
}

// ==========================================
// THEME & NAVIGATION CONTROLLERS
// ==========================================
let currentTheme = localStorage.getItem('np_theme') || 'light';
function setTheme(t) {
  currentTheme = t;
  document.documentElement.setAttribute('data-theme', t);
  localStorage.setItem('np_theme', t);
  document.querySelectorAll('.theme-btn').forEach(b => b.classList.toggle('active', b.dataset.theme === t));
}
document.querySelectorAll('.theme-btn').forEach(b => {
  b.onclick = () => setTheme(b.dataset.theme);
});
setTheme(currentTheme);

// View Switching
function switchView(viewName) {
  document.querySelectorAll('.mode-tab').forEach(t => t.classList.toggle('active', t.dataset.view === viewName));
  $('view-course').style.display = (viewName === 'course') ? 'block' : 'none';
  $('view-simlab').style.display = (viewName === 'simlab') ? 'block' : 'none';
  $('view-pyq').style.display = (viewName === 'pyq') ? 'block' : 'none';
  $('view-mcq').style.display = (viewName === 'mcq') ? 'block' : 'none';
  $('view-cheat').style.display = (viewName === 'cheat') ? 'block' : 'none';
  window.scrollTo({top: 0, behavior: 'smooth'});
}
document.querySelectorAll('.mode-tab').forEach(t => {
  t.onclick = () => switchView(t.dataset.view);
});

// Progress persistence
let lessonDone = {};
try { lessonDone = JSON.parse(localStorage.getItem('np_lessons_done') || '{}'); } catch(e){}
function updateProgress() {
  const all = document.querySelectorAll('.lesson-card');
  let doneCount = 0;
  all.forEach(l => {
    if (lessonDone[l.id]) doneCount++;
  });
  const pct = Math.round((doneCount / all.length) * 100);
  $('prog-text').textContent = pct + '%';
  $('prog-bar-fill').style.width = pct + '%';
  document.querySelectorAll('.toc-item').forEach(ti => {
    ti.classList.toggle('completed', !!lessonDone[ti.dataset.id]);
  });
  try { localStorage.setItem('np_lessons_done', JSON.stringify(lessonDone)); } catch(e){}
}

// Build TOC
const tocContainer = $('toc-sidebar-items');
document.querySelectorAll('.lesson-card').forEach((l, idx) => {
  const item = H('a', 'toc-item', null, tocContainer);
  item.href = '#' + l.id;
  item.dataset.id = l.id;
  H('span', 'toc-num', String(idx + 1), item);
  H('span', null, l.dataset.title, item);
  H('span', 'toc-check', '✓', item);
  
  item.onclick = (e) => {
    e.preventDefault();
    l.scrollIntoView({behavior: 'smooth', block: 'start'});
    document.querySelectorAll('.toc-item').forEach(x => x.classList.remove('active'));
    item.classList.add('active');
  };

  // Add done button to lesson footer
  const ft = H('div', 'row', null, l);
  ft.style.marginTop = '18px';
  ft.style.borderTop = '1px solid var(--line-light)';
  ft.style.paddingTop = '12px';
  
  const doneBtn = H('button', 'btn', lessonDone[l.id] ? 'Lesson Completed ✓' : 'Mark Lesson as Completed', ft);
  doneBtn.type = 'button';
  doneBtn.classList.toggle('active', !!lessonDone[l.id]);
  doneBtn.onclick = () => {
    lessonDone[l.id] = !lessonDone[l.id];
    doneBtn.classList.toggle('active', !!lessonDone[l.id]);
    doneBtn.textContent = lessonDone[l.id] ? 'Lesson Completed ✓' : 'Mark Lesson as Completed';
    updateProgress();
  };
});
updateProgress();

// Active TOC scroll spy
const obs = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      document.querySelectorAll('.toc-item').forEach(x => {
        x.classList.toggle('active', x.dataset.id === e.target.id);
      });
    }
  });
}, {rootMargin: '-20% 0px -70% 0px'});
document.querySelectorAll('.lesson-card').forEach(l => obs.observe(l));


// ==========================================
// SIMULATION 1: GROWTH RATES
// ==========================================
const fact = n => { let r = 1; for (let i = 2; i <= n; i++) r *= i; return r; };
const GF = [
  ['n', n => n, 0],
  ['n log₂ n', n => n * Math.log2(Math.max(n, 1)), 0],
  ['n²', n => n * n, 0],
  ['n³', n => Math.pow(n, 3), 0],
  ['2ⁿ', n => Math.pow(2, n), 1],
  ['n!', fact, 1]
];
function growth() {
  const n = +$('gn').value;
  $('gnv').textContent = n;
  const t = $('gt');
  t.innerHTML = '';
  const hr = H('tr', null, null, t);
  ['Complexity', 'Operations Required', 'Time @ 10⁹ steps/sec'].forEach((h, i) => H('th', i ? 'num' : '', h, hr));
  
  GF.forEach(([name, f, hard]) => {
    const v = f(n);
    const r = H('tr', hard ? 'danger' : '', null, t);
    H('td', null, name, r);
    H('td', 'num', fmt(v), r);
    H('td', 'num', human(v / 1e9), r);
  });
  
  const svg = $('gchart');
  svg.innerHTML = '';
  const L = 44, R = 10, T = 12, B = 28, W = 420, Hh = 270, X0 = 1, X1 = 30, Ymax = 34;
  const x = v => L + (v - X0) / (X1 - X0) * (W - L - R);
  const y = v => Hh - B - v / Ymax * (Hh - T - B);
  
  for (let g = 0; g <= 30; g += 6) {
    S('line', {x1: L, x2: W - R, y1: y(g), y2: y(g), stroke: 'var(--line)'}, svg);
    S('text', {x: L - 6, y: y(g) + 4, 'text-anchor': 'end', 'font-size': 11}, svg, '10' + sup(g));
  }
  for (let g = 5; g <= 30; g += 5) {
    S('text', {x: x(g), y: Hh - 10, 'text-anchor': 'middle', 'font-size': 11}, svg, g);
  }
  S('text', {x: W - R, y: Hh - 2, 'text-anchor': 'end', 'font-size': 11, style: 'fill:var(--muted);'}, svg, 'n');
  
  // 1-second benchmark line
  S('line', {x1: L, x2: W - R, y1: y(9), y2: y(9), stroke: 'var(--ink)', 'stroke-dasharray': '4 4'}, svg);
  S('text', {x: L + 4, y: y(9) - 4, 'font-size': 11, style: 'fill:var(--ink); font-weight:700;'}, svg, '1 Second Threshold (10⁹ ops)');
  
  GF.forEach(([name, f, hard], i) => {
    let pts = '';
    for (let k = 1; k <= X1; k++) {
      pts += x(k) + ',' + y(Math.log10(Math.max(f(k), 1))) + ' ';
    }
    S('polyline', {points: pts, fill: 'none', stroke: hard ? 'var(--hard)' : 'var(--accent)', 'stroke-width': hard ? 3.5 : 2.5, opacity: hard ? 1 : [0.5, 0.7, 0.9, 1][i]}, svg);
  });
  
  const xm = Math.min(n, X1);
  S('line', {x1: x(xm), x2: x(xm), y1: T, y2: Hh - B, stroke: 'var(--ink)', 'stroke-width': 1.5}, svg);
  S('text', {x: Math.min(x(xm) + 4, W - 70), y: T + 12, 'font-size': 11, 'font-weight': 700}, svg, 'n = ' + n + (n > X1 ? ' (off-scale)' : ''));
}
$('gn').oninput = growth;
growth();


// ==========================================
// SIMULATION 2: DECISION VS OPTIMIZATION
// ==========================================
const DEC_OPT_DATA = [
  {name: 'Travelling Salesperson (TSP)', dec: 'Is there a tour of cities with total cost ≤ k?', opt: 'Find the tour that achieves the minimum total distance.', notes: 'Decision version is in NP; Optimization is NP-hard outside NP.'},
  {name: 'Vertex Cover', dec: 'Is there a subset of vertices of size ≤ k that touches every edge?', opt: 'Find the vertex cover with the minimum possible number of vertices.', notes: 'Decision version is NP-complete.'},
  {name: 'Clique Problem', dec: 'Does the graph contain a complete subgraph of size ≥ k?', opt: 'Find the largest clique in the graph.', notes: 'Equivalence via binary search on k.'},
  {name: '0/1 Knapsack', dec: 'Can we achieve total profit ≥ P with weight ≤ W?', opt: 'Find the subset of items that maximizes profit with weight ≤ W.', notes: 'Decision is NP-complete; weakly NP-hard.'}
];
const decOptContainer = $('dec-opt-btns');
DEC_OPT_DATA.forEach((item, idx) => {
  const b = H('button', 'btn' + (idx === 0 ? ' active' : ''), item.name, decOptContainer);
  b.onclick = () => {
    decOptContainer.querySelectorAll('.btn').forEach(x => x.classList.remove('active'));
    b.classList.add('active');
    $('dec-opt-status').innerHTML = '<b>' + item.name + '</b><br><span style="color:var(--accent);">Decision:</span> ' + item.dec + '<br><span style="color:var(--hard);">Optimization:</span> ' + item.opt + '<br><small style="color:var(--muted);">' + item.notes + '</small>';
  };
});
$('dec-opt-status').innerHTML = '<b>' + DEC_OPT_DATA[0].name + '</b><br><span style="color:var(--accent);">Decision:</span> ' + DEC_OPT_DATA[0].dec + '<br><span style="color:var(--hard);">Optimization:</span> ' + DEC_OPT_DATA[0].opt + '<br><small style="color:var(--muted);">' + DEC_OPT_DATA[0].notes + '</small>';


// ==========================================
// SIMULATION 3: CLIQUE VERIFIER (k = 4)
// ==========================================
const CQN = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
const CQE = [[2,4],[2,5],[2,6],[4,5],[4,6],[5,6],[0,1],[0,2],[1,2],[0,3],[3,4],[3,5]];
const CQP = CQN.map((_, i) => {
  const a = -Math.PI / 2 + i * 2 * Math.PI / 7;
  return [200 + 125 * Math.cos(a), 160 + 125 * Math.sin(a)];
});
const adj = (a, b) => CQE.some(e => (e[0] === a && e[1] === b) || (e[0] === b && e[1] === a));
let cqSel = [], cqTimer = null, cqMark = {};

function combos(n, k) {
  const out = [];
  (function r(s, c) {
    if (c.length === k) { out.push(c.slice()); return; }
    for (let i = s; i < n; i++) { c.push(i); r(i + 1, c); c.pop(); }
  })(0, []);
  return out;
}
const cqAll = combos(7, 4);
const binom = (n, k) => {
  let r = 1; for (let i = 1; i <= k; i++) r = r * (n - k + i) / i; return Math.round(r);
};

function cqDraw() {
  const svg = $('cq'); svg.innerHTML = '';
  CQE.forEach(([a, b]) => {
    const key = Math.min(a, b) + '-' + Math.max(a, b);
    S('line', {x1: CQP[a][0], y1: CQP[a][1], x2: CQP[b][0], y2: CQP[b][1], class: 'edge ' + (cqMark[key] || '')}, svg);
  });
  Object.keys(cqMark).forEach(k => {
    if (!CQE.some(e => (Math.min(e[0],e[1])+'-'+Math.max(e[0],e[1])) === k)) {
      const [a, b] = k.split('-').map(Number);
      S('line', {x1: CQP[a][0], y1: CQP[a][1], x2: CQP[b][0], y2: CQP[b][1], class: 'edge ' + cqMark[k]}, svg);
    }
  });
  CQN.forEach((n, i) => {
    const g = S('g', {class: 'node' + (cqSel.includes(i) ? ' sel' : ''), tabindex: 0, role: 'button'}, svg);
    S('circle', {cx: CQP[i][0], cy: CQP[i][1], r: 22}, g);
    S('text', {x: CQP[i][0], y: CQP[i][1]}, g, n);
    g.onclick = () => {
      if (cqTimer) return;
      cqMark = {};
      cqSel = cqSel.includes(i) ? cqSel.filter(v => v !== i) : [...cqSel, i].sort((a,b)=>a-b);
      cqDraw();
      $('cqs').className = 'status-box';
      $('cqs').textContent = cqSel.length ? 'Candidate Certificate: {' + cqSel.map(v => CQN[v]).join(', ') + '} (size ' + cqSel.length + '). Click Verify.' : 'Pick 4 vertices to create your certificate.';
    };
  });
}

function cqVerify() {
  if (cqTimer) return;
  cqMark = {}; cqDraw();
  const st = $('cqs');
  if (cqSel.length !== 4) {
    st.className = 'status-box bad';
    st.textContent = 'A certificate for k = 4 requires exactly 4 vertices. You selected ' + cqSel.length + '.';
    return;
  }
  const pairs = [];
  for (let i = 0; i < 4; i++) {
    for (let j = i + 1; j < 4; j++) {
      pairs.push([cqSel[i], cqSel[j]]);
    }
  }
  let idx = 0, bad = false;
  st.className = 'status-box';
  st.textContent = 'Running Polynomial Verifier: testing all pairwise edges...';
  
  cqTimer = setInterval(() => {
    if (idx >= pairs.length || bad) {
      clearInterval(cqTimer); cqTimer = null;
      st.className = 'status-box ' + (bad ? 'bad' : 'ok');
      st.textContent = bad ? 'Verification Failed: pair ' + CQN[pairs[idx-1][0]] + '-' + CQN[pairs[idx-1][1]] + ' is NOT connected! Certificate rejected in ' + idx + ' pair checks.' : 'Verification Successful! All 6 pairs are connected by edges. This is a valid 4-clique! (Verified in O(k²) = 6 steps).';
      return;
    }
    const [a, b] = pairs[idx];
    const ok = adj(a, b);
    cqMark[Math.min(a, b) + '-' + Math.max(a, b)] = ok ? 'good' : 'badl';
    if (!ok) bad = true;
    idx++;
    cqDraw();
    st.textContent = 'Checking edge (' + CQN[a] + ', ' + CQN[b] + '): ' + (ok ? 'Present ✓' : 'MISSING ✗');
  }, 480);
}

function cqBrute() {
  if (cqTimer) return;
  cqMark = {};
  const st = $('cqs');
  let tried = 0, found = null;
  for (const c of cqAll) {
    tried++;
    let ok = true;
    for (let i = 0; i < 4 && ok; i++) {
      for (let j = i + 1; j < 4; j++) {
        if (!adj(c[i], c[j])) { ok = false; break; }
      }
    }
    if (ok) { found = c; break; }
  }
  cqSel = found || [];
  cqDraw();
  st.className = 'status-box ok';
  st.textContent = 'Brute-force searched ' + tried + ' of ' + cqAll.length + ' possible combinations before finding 4-clique: {' + found.map(v => CQN[v]).join(', ') + '}. Verifying it took only 6 checks!';
}

$('cqv').onclick = cqVerify;
$('cqb').onclick = cqBrute;
$('cqr').onclick = () => {
  if (cqTimer) { clearInterval(cqTimer); cqTimer = null; }
  cqSel = []; cqMark = {}; cqDraw();
  $('cqs').className = 'status-box';
  $('cqs').textContent = 'Pick 4 vertices to create your certificate.';
};

(function() {
  const t = $('cqt');
  const hr = H('tr', null, null, t);
  ['Graph Size n, Target k', 'Subsets to Search (Brute Force)', 'Pairs to Check (Verifier)'].forEach((h, i) => H('th', i ? 'num' : '', h, hr));
  [[7, 4], [20, 10], [50, 25], [100, 50]].forEach(([n, k]) => {
    const r = H('tr', null, null, t);
    H('td', null, 'n = ' + n + ', k = ' + k, r);
    H('td', 'num', fmt(binom(n, k)), r);
    H('td', 'num', fmt(k * (k - 1) / 2), r);
  });
})();
cqDraw();


// ==========================================
// SIMULATION 4: VENN DIAGRAM
// ==========================================
let vmode = 'ne';
function venn() {
  const svg = $('venn'); svg.innerHTML = '';
  const defs = S('defs', {}, svg);
  const cp = S('clipPath', {id: 'cpNP'}, defs);
  S('ellipse', {cx: 240, cy: 165, rx: 200, ry: 130}, cp);
  
  S('ellipse', {cx: 240, cy: 165, rx: 200, ry: 130, fill: 'var(--accent-soft)', stroke: 'var(--accent)', 'stroke-width': 3}, svg);
  S('ellipse', {cx: 420, cy: 165, rx: 190, ry: 130, fill: 'var(--hard-soft)', stroke: 'var(--hard)', 'stroke-width': 3, opacity: 0.95}, svg);
  S('ellipse', {cx: 420, cy: 165, rx: 190, ry: 130, fill: 'var(--mark)', 'fill-opacity': 0.55, 'clip-path': 'url(#cpNP)'}, svg);
  S('ellipse', {cx: 240, cy: 165, rx: 200, ry: 130, fill: 'none', stroke: 'var(--accent)', 'stroke-width': 3}, svg);
  
  const t = (x, y, s, o = {}) => S('text', Object.assign({x, y, 'text-anchor': 'middle', 'font-size': 15}, o), svg, s);
  t(200, 78, 'Class NP', {'font-weight': 800, 'font-size': 20});
  t(520, 80, 'Class NP-Hard', {'font-weight': 800, 'font-size': 20});
  
  t(330, 150, 'NP-Complete (NPC)', {'font-weight': 800, 'font-size': 16});
  t(330, 172, '3-SAT, Clique,', {'font-size': 13});
  t(330, 190, 'Hamiltonian Cycle,', {'font-size': 13});
  t(330, 208, 'Decision TSP', {'font-size': 13});
  
  t(535, 150, 'Optimization TSP,', {'font-size': 13});
  t(535, 170, 'Halting Problem', {'font-size': 13});
  t(535, 190, '(Outside NP!)', {'font-size': 12, style: 'fill:var(--hard); font-weight:700;'});
  
  if (vmode === 'ne') {
    S('ellipse', {cx: 128, cy: 178, rx: 80, ry: 60, fill: 'var(--surface)', stroke: 'var(--accent)', 'stroke-width': 2.5}, svg);
    t(128, 168, 'Class P', {'font-weight': 800, 'font-size': 19});
    t(128, 190, 'Dijkstra, Kruskal,', {'font-size': 12});
    t(128, 206, 'MergeSort, 2-SAT', {'font-size': 12});
  } else {
    t(128, 178, 'P = NP = NPC', {'font-weight': 800, 'font-size': 22, style: 'fill:var(--accent);'});
    t(128, 202, 'All NP collapses to P', {'font-size': 13});
  }
  $('v1').classList.toggle('active', vmode === 'ne');
  $('v2').classList.toggle('active', vmode === 'eq');
}
function vsay(msg, cls) {
  const s = $('vs'); s.className = 'status-box ' + (cls || ''); s.innerHTML = msg;
}
$('v1').onclick = () => {
  vmode = 'ne'; venn();
  vsay('<b>Universe 1: P ≠ NP.</b> What 99% of computer scientists believe. P sits strictly inside NP without reaching the hardest problems. NPC = NP ∩ NP-hard.');
};
$('v2').onclick = () => {
  vmode = 'eq'; venn();
  vsay('<b>Universe 2: P = NP.</b> Every problem whose answer can be verified quickly can also be solved quickly! All NPC problems collapse into P.');
};
$('v3').onclick = () => {
  vmode = 'eq'; venn();
  vsay('<b>Autumn 2022 Q1e Solution:</b> Clique is known to be NP-complete. Finding a polynomial algorithm for largest clique implies that <i>every</i> problem in NP reduces to a polynomial algorithm, collapsing the classes so that <b>P = NP = NPC</b> (Option C / D).', 'ok');
};
venn();
vsay('Click Universe 1, Universe 2, or the Autumn 2022 exam question button above.');


// ==========================================
// SIMULATION 5: REDUCTION RULES MATRIX
// ==========================================
const RULES = [
  {q: "B ∈ P (B is solvable in polynomial time)", yes: true, a: "A ∈ P. You can transform instance x of A into f(x) of B in poly time, then run B solver. Both steps are polynomial."},
  {q: "A is NP-hard", yes: true, a: "B is NP-hard. If B were easy, A would be easy, which contradicts A being NP-hard. Hardness is inherited!"},
  {q: "B is NP-hard", yes: false, a: "NOTHING FOLLOWS about A! A is only no harder than B. A could be trivially easy (like 2+2=4). The direction trap! (Spring 2023 Q1c(ii))."},
  {q: "A ∈ P (A has a polynomial-time algorithm)", yes: false, a: "NOTHING FOLLOWS about B! Knowing A is easy gives zero information about how hard B might be."},
  {q: "B ∈ NP", yes: true, a: "A ∈ NP. Transform input x to f(x) in polynomial time, then verify with B verifier."},
  {q: "A is NP-complete and B ∈ NP", yes: true, a: "B is NP-complete! Since A is NPC, every problem in NP reduces to A, and A reduces to B, so every problem in NP reduces to B (B is NP-hard). Since B ∈ NP, B is NPC! (Autumn 2024 Q1j Superstar)."},
  {q: "S is NPC, Q ≤p S ≤p R", yes: true, a: "Q ∈ NP (it reduces to S ∈ NP), and R is NP-hard (S is NPC and reduces to R). Neither Q is necessarily NPC nor is R necessarily in NP! (Autumn 2023 Q7b)."}
];
const rulesGrid = $('rules-grid');
RULES.forEach(r => {
  const card = H('div', 'cheat-card', null, rulesGrid);
  card.style.cursor = 'pointer';
  card.style.borderLeft = '4px solid var(--line)';
  H('h4', null, 'If A ≤p B and: ' + r.q, card);
  const clickHint = H('p', 'sim-hint', '👉 Click to reveal exam deduction', card);
  
  card.onclick = () => {
    if (card.querySelector('.rule-ans')) return;
    clickHint.remove();
    card.style.borderLeftColor = r.yes ? 'var(--ok)' : 'var(--no)';
    const ans = H('div', 'rule-ans', null, card);
    H('div', null, (r.yes ? '✅ VALID CONCLUSION' : '❌ TRAP / NOTHING FOLLOWS'), ans);
    ans.firstChild.style.color = r.yes ? 'var(--ok)' : 'var(--no)';
    ans.firstChild.style.fontWeight = '800';
    ans.firstChild.style.marginBottom = '4px';
    H('p', null, r.a, ans);
  };
});


// ==========================================
// SIMULATION 6: 3-CNF SAT SOLVER
// ==========================================
const SAT1 = [[1, -2, 3], [-1, 2, 3], [-1, -2, -3], [1, 2, -3]];
const SAT2 = [[1,2,3],[1,2,-3],[1,-2,3],[1,-2,-3],[-1,2,3],[-1,2,-3],[-1,-2,3],[-1,-2,-3]];
let curSat = SAT1, satVals = [true, false, true], showSatTable = false;
const evalLit = (l, v) => l > 0 ? v[l - 1] : !v[-l - 1];

function satDraw() {
  const vr = $('satvars'); vr.innerHTML = '';
  [0, 1, 2].forEach(i => {
    const d = H('div', 'row', null, vr);
    H('b', null, 'x' + (i + 1) + ' = ', d);
    const b = H('button', 'btn' + (satVals[i] ? ' active' : ''), satVals[i] ? 'TRUE' : 'FALSE', d);
    b.onclick = () => { satVals[i] = !satVals[i]; satDraw(); };
  });
  
  const cl = $('satcl'); cl.innerHTML = '';
  let allSat = true;
  curSat.forEach(c => {
    const ok = c.some(l => evalLit(l, satVals));
    if (!ok) allSat = false;
    const r = H('div', 'row', null, cl);
    r.style.padding = '6px 10px';
    r.style.border = '1px solid ' + (ok ? 'var(--ok)' : 'var(--no)');
    r.style.borderRadius = '8px';
    r.style.background = ok ? 'var(--ok-soft)' : 'var(--no-soft)';
    r.style.margin = '4px 0';
    
    let expr = '(';
    c.forEach((l, j) => {
      if (j) expr += ' ∨ ';
      expr += (l < 0 ? '¬' : '') + 'x' + Math.abs(l);
    });
    expr += ')';
    H('span', 'mono', expr, r);
    H('span', null, ok ? ' ✓ Satisfied' : ' ✗ Falsified', r);
    r.lastChild.style.marginLeft = 'auto';
    r.lastChild.style.fontWeight = '700';
    r.lastChild.style.color = ok ? 'var(--ok)' : 'var(--no)';
  });
  
  const st = $('sats');
  st.className = 'status-box ' + (allSat ? 'ok' : 'bad');
  st.textContent = allSat ? 'Formula SATISFIED by this assignment! Verification took 1 pass over clauses (O(m) time).' : 'Formula NOT satisfied. At least one clause evaluates to FALSE.';
  
  const tb = $('sattab'); tb.innerHTML = '';
  if (showSatTable) {
    const t = H('table', 'data-table', null, tb);
    const hr = H('tr', null, null, t);
    ['x1', 'x2', 'x3', 'Formula Status'].forEach(h => H('th', null, h, hr));
    for (let m = 0; m < 8; m++) {
      const v = [!!(m & 4), !!(m & 2), !!(m & 1)];
      const ok = curSat.every(c => c.some(l => evalLit(l, v)));
      const r = H('tr', ok ? 'highlight' : '', null, t);
      v.forEach(b => H('td', null, b ? 'T' : 'F', r));
      H('td', null, ok ? 'SATISFIED ✓' : 'Falsified', r);
    }
  }
}
$('satall').onclick = () => { showSatTable = !showSatTable; satDraw(); };
$('satun').onclick = () => { curSat = SAT2; satDraw(); };
$('satre').onclick = () => { curSat = SAT1; satDraw(); };
satDraw();


// ==========================================
// SIMULATION 7: TRIAD DUAL GRAPH
// ==========================================
const CV_NODES = [[40, 50], [110, 22], [40, 150], [110, 178], [190, 55], [250, 150]];
const CV_NAMES = ['1', '2', '3', '4', '5', '6'];
const CV_EDGES = [[0,1],[0,2],[1,2],[1,3],[2,3],[3,4],[3,5],[4,5]];
const cvAdj = (a, b) => CV_EDGES.some(e => (e[0]===a && e[1]===b) || (e[0]===b && e[1]===a));
let cvSel = [];

function drawTriadGraph(id, isComplement) {
  const svg = $(id); svg.innerHTML = '';
  for (let a = 0; a < 6; a++) {
    for (let b = a + 1; b < 6; b++) {
      const e = cvAdj(a, b);
      if (isComplement ? !e : e) {
        S('line', {x1: CV_NODES[a][0], y1: CV_NODES[a][1], x2: CV_NODES[b][0], y2: CV_NODES[b][1], class: 'edge ' + (isComplement ? 'one' : '')}, svg);
      }
    }
  }
  CV_NAMES.forEach((n, i) => {
    const g = S('g', {class: 'node' + (cvSel.includes(i) ? ' sel' : ''), tabindex: 0, role: 'button'}, svg);
    S('circle', {cx: CV_NODES[i][0], cy: CV_NODES[i][1], r: 19}, g);
    S('text', {x: CV_NODES[i][0], y: CV_NODES[i][1]}, g, n);
    g.onclick = () => {
      cvSel = cvSel.includes(i) ? cvSel.filter(v => v !== i) : [...cvSel, i].sort();
      updateTriad();
    };
  });
}

function updateTriad() {
  drawTriadGraph('g1', false);
  drawTriadGraph('g2', true);
  const S_ = cvSel;
  const pairs = [];
  for (let i = 0; i < S_.length; i++) {
    for (let j = i + 1; j < S_.length; j++) pairs.push([S_[i], S_[j]]);
  }
  const isCliqueInG = S_.length > 0 && pairs.every(([a, b]) => cvAdj(a, b));
  const isIndepInGBar = S_.length > 0 && pairs.every(([a, b]) => !(!cvAdj(a, b)));
  const rest = [0, 1, 2, 3, 4, 5].filter(v => !S_.includes(v));
  
  // Check if rest covers all edges in G bar
  let isVCCoverInGBar = true;
  for (let a = 0; a < 6; a++) {
    for (let b = a + 1; b < 6; b++) {
      if (!cvAdj(a, b)) { // edge in G bar
        if (!rest.includes(a) && !rest.includes(b)) {
          isVCCoverInGBar = false;
        }
      }
    }
  }
  
  const box = $('civ'); box.innerHTML = '';
  if (!S_.length) {
    box.className = 'status-box';
    box.textContent = 'Tap vertices on either graph to pick subset S.';
    return;
  }
  box.className = 'status-box ' + (isCliqueInG ? 'ok' : 'warm');
  box.innerHTML = '<b>Selected S = {' + S_.map(v => CV_NAMES[v]).join(', ') + '} (size k = ' + S_.length + ')</b><br>' +
    '• S is a <b>Clique in G</b>: ' + (isCliqueInG ? '<span style="color:var(--ok);">YES ✓</span>' : 'NO ✗') + '<br>' +
    '• S is an <b>Independent Set in Ḡ</b>: ' + (isCliqueInG ? '<span style="color:var(--ok);">YES ✓</span>' : 'NO ✗') + '<br>' +
    '• V \\ S = {' + rest.map(v => CV_NAMES[v]).join(', ') + '} is a <b>Vertex Cover in Ḡ</b> of size n - k = ' + (6 - S_.length) + ': ' + (isVCCoverInGBar ? '<span style="color:var(--ok);">YES ✓</span>' : 'NO ✗');
}
$('civ3').onclick = () => { cvSel = [0, 1, 2]; updateTriad(); };
$('civr').onclick = () => { cvSel = []; updateTriad(); };
updateTriad();


// ==========================================
// SIMULATION 8: HAMILTONIAN TO TSP
// ==========================================
const HP_NODES = [[150, 28], [262, 108], [220, 222], [80, 222], [38, 108]];
const HG_DATA = [
  {name: 'hasHC', edges: [[0,1],[1,2],[2,3],[3,4],[4,0],[1,3]]},
  {name: 'noHC', edges: [[0,1],[1,2],[2,3],[3,4],[1,3],[0,2]]}
];
let hgMode = 0, userTour = [];
const hAdj = (a, b) => HG_DATA[hgMode].edges.some(e => (e[0]===a && e[1]===b) || (e[0]===b && e[1]===a));

function perms(a) {
  if (a.length <= 1) return [a];
  const o = [];
  a.forEach((x, i) => perms([...a.slice(0, i), ...a.slice(i + 1)]).forEach(p => o.push([x, ...p])));
  return o;
}
function calcTourCost(t) {
  let c = 0;
  for (let i = 0; i < t.length; i++) {
    const a = t[i], b = t[(i + 1) % t.length];
    if (!hAdj(a, b)) c++;
  }
  return c;
}
function getBestTour() {
  let best = null, minC = 99;
  perms([1, 2, 3, 4]).forEach(p => {
    const t = [0, ...p];
    const c = calcTourCost(t);
    if (c < minC) { minC = c; best = t; }
  });
  return [best, minC];
}

function hcDraw() {
  const g1 = $('h1'); g1.innerHTML = '';
  HG_DATA[hgMode].edges.forEach(([a, b]) => {
    S('line', {x1: HP_NODES[a][0], y1: HP_NODES[a][1], x2: HP_NODES[b][0], y2: HP_NODES[b][1], class: 'edge'}, g1);
  });
  HP_NODES.forEach((p, i) => {
    const g = S('g', {class: 'node'}, g1);
    S('circle', {cx: p[0], cy: p[1], r: 18}, g);
    S('text', {x: p[0], y: p[1]}, g, i + 1);
  });
  
  const g2 = $('h2'); g2.innerHTML = '';
  for (let a = 0; a < 5; a++) {
    for (let b = a + 1; b < 5; b++) {
      S('line', {x1: HP_NODES[a][0], y1: HP_NODES[a][1], x2: HP_NODES[b][0], y2: HP_NODES[b][1], class: 'edge ' + (hAdj(a, b) ? 'zero' : 'one') + (userTour.length ? ' faint' : '')}, g2);
    }
  }
  
  const full = userTour.length === 5;
  for (let i = 0; i < userTour.length - 1 + (full ? 1 : 0); i++) {
    const a = userTour[i], b = userTour[(i + 1) % userTour.length];
    S('line', {x1: HP_NODES[a][0], y1: HP_NODES[a][1], x2: HP_NODES[b][0], y2: HP_NODES[b][1], class: 'edge tour'}, g2);
  }
  
  HP_NODES.forEach((p, i) => {
    const idx = userTour.indexOf(i);
    const g = S('g', {class: 'node' + (idx >= 0 ? ' sel' : ''), tabindex: 0, role: 'button'}, g2);
    S('circle', {cx: p[0], cy: p[1], r: 18}, g);
    S('text', {x: p[0], y: p[1]}, g, idx >= 0 ? (idx + 1) : (i + 1));
    g.onclick = () => {
      if (full || userTour.includes(i)) return;
      userTour.push(i);
      hcDraw();
    };
  });
  
  const st = $('hcs');
  if (!userTour.length) {
    st.className = 'status-box';
    st.textContent = 'Click cities on the right to build your tour in order.';
  } else if (!full) {
    st.className = 'status-box';
    st.textContent = 'Visited ' + userTour.length + ' of 5 cities: [' + userTour.map(x=>x+1).join(' → ') + ']. Continue picking.';
  } else {
    const c = calcTourCost(userTour);
    st.className = 'status-box ' + (c === 0 ? 'ok' : 'bad');
    st.innerHTML = 'Tour Completed: [' + userTour.map(x=>x+1).join(' → ') + ' → ' + (userTour[0]+1) + ']. Total Cost = <b>' + c + '</b> (Threshold k = 0). ' +
      (c === 0 ? "Cost = 0 ≤ k → Every edge was in G! This is a valid <b>Hamiltonian Cycle</b>!" : "Cost > 0 → Uses " + c + " non-edge(s). Does NOT yield a Hamiltonian Cycle.");
  }
}
$('hc1').onclick = () => { hgMode = 0; userTour = []; $('hc1').classList.add('active'); $('hc2').classList.remove('active'); hcDraw(); };
$('hc2').onclick = () => { hgMode = 1; userTour = []; $('hc2').classList.add('active'); $('hc1').classList.remove('active'); hcDraw(); };
$('hcr').onclick = () => { userTour = []; hcDraw(); };
$('hcb').onclick = () => {
  const [bestT, cost] = getBestTour();
  userTour = bestT.slice();
  hcDraw();
  $('hcs').className = 'status-box ' + (cost === 0 ? 'ok' : 'bad');
  $('hcs').innerHTML = 'Best possible TSP tour has cost = <b>' + cost + '</b>. ' +
    (cost === 0 ? 'G has a Hamiltonian Cycle!' : 'Even the optimal tour has cost > 0. G has NO Hamiltonian Cycle!');
};
hcDraw();


// ==========================================
// SIMULATION 10A: VERTEX COVER 2-APPROX
// ==========================================
const VC_PTS = [[60, 60], [140, 40], [80, 180], [180, 160], [260, 60], [330, 130], [270, 210]];
const VC_EDGES = [[0,1],[0,2],[1,2],[1,3],[2,3],[3,4],[4,5],[4,6],[5,6]];
let vcE = [], vcM = [], vcC = [];

function initVC() {
  vcE = VC_EDGES.map(e => [...e]);
  vcM = [];
  vcC = [];
  drawVC();
  $('vc-status').className = 'status-box';
  $('vc-status').textContent = "Click 'Pick Next Matching Edge' to execute APPROX-VERTEX-COVER.";
  updateVCMetrics();
}
function drawVC() {
  const svg = $('vc-svg'); svg.innerHTML = '';
  VC_EDGES.forEach(([u, v]) => {
    const isMatched = vcM.some(e => (e[0]===u && e[1]===v) || (e[0]===v && e[1]===u));
    S('line', {x1: VC_PTS[u][0], y1: VC_PTS[u][1], x2: VC_PTS[v][0], y2: VC_PTS[v][1], class: 'edge ' + (isMatched ? 'matched' : '')}, svg);
  });
  VC_PTS.forEach((p, i) => {
    const isCover = vcC.includes(i);
    const g = S('g', {class: 'node' + (isCover ? ' cover' : '')}, svg);
    S('circle', {cx: p[0], cy: p[1], r: 18}, g);
    S('text', {x: p[0], y: p[1]}, g, i + 1);
  });
}
function updateVCMetrics() {
  const optSize = 3; // Brute force optimum for this graph is 3
  const ratio = vcC.length ? (vcC.length / optSize).toFixed(2) : '-';
  const t = $('vc-metrics-table'); t.innerHTML = '';
  const hr = H('tr', null, null, t);
  ['Metric', 'Value', 'Formula / Guarantee'].forEach(h => H('th', null, h, hr));
  
  [['Matching Size |M|', vcM.length, 'Independent edges picked'],
   ['Algorithm Cover Size |C|', vcC.length, '|C| = 2|M|'],
   ['Optimal Cover Size |OPT|', optSize, '|OPT| ≥ |M| (each edge needs ≥1 vertex)'],
   ['Current Ratio |C| / |OPT|', ratio, 'Guaranteed ≤ 2.00']
  ].forEach(([m, v, g]) => {
    const r = H('tr', null, null, t);
    H('td', null, m, r);
    H('td', 'num', String(v), r);
    H('td', null, g, r);
  });
}
$('vc-step-btn').onclick = () => {
  if (!vcE.length) {
    $('vc-status').className = 'status-box ok';
    $('vc-status').textContent = 'Algorithm Terminated! All edges are covered. Cover size = ' + vcC.length + ' (Optimal = 3, Ratio = ' + (vcC.length / 3).toFixed(2) + ' ≤ 2.0).';
    return;
  }
  const [u, v] = vcE[0];
  vcM.push([u, v]);
  if (!vcC.includes(u)) vcC.push(u);
  if (!vcC.includes(v)) vcC.push(v);
  vcE = vcE.filter(e => e[0] !== u && e[0] !== v && e[1] !== u && e[1] !== v);
  drawVC();
  updateVCMetrics();
  $('vc-status').className = 'status-box ok';
  $('vc-status').textContent = 'Picked matching edge (' + (u+1) + ', ' + (v+1) + '). Added both vertices to cover C. ' + vcE.length + ' edges remain.';
};
$('vc-reset-btn').onclick = initVC;
initVC();


// ==========================================
// SIMULATION 10B: METRIC TSP 2-APPROX
// ==========================================
const TSP_CITIES = [[60, 100], [160, 40], [300, 70], [330, 190], [210, 220], [130, 170], [200, 130]];
const TSP_MST_EDGES = [[0,1],[1,6],[6,4],[4,3],[3,2],[0,5]]; // Prim/Kruskal MST
const TSP_WALK = [0, 1, 6, 4, 3, 2, 3, 4, 6, 1, 0, 5, 0];
const TSP_TOUR = [0, 1, 6, 4, 3, 2, 5, 0];
let tspStep = 1;

function drawTSPApprox() {
  const svg = $('tsp-approx-svg'); svg.innerHTML = '';
  // Draw all faint complete edges
  for (let i = 0; i < 7; i++) {
    for (let j = i + 1; j < 7; j++) {
      S('line', {x1: TSP_CITIES[i][0], y1: TSP_CITIES[i][1], x2: TSP_CITIES[j][0], y2: TSP_CITIES[j][1], stroke: 'var(--line-light)', 'stroke-width': 1.5}, svg);
    }
  }
  
  if (tspStep === 1) {
    TSP_MST_EDGES.forEach(([u, v]) => {
      S('line', {x1: TSP_CITIES[u][0], y1: TSP_CITIES[u][1], x2: TSP_CITIES[v][0], y2: TSP_CITIES[v][1], class: 'edge tree'}, svg);
    });
  } else if (tspStep === 2) {
    for (let i = 0; i < TSP_WALK.length - 1; i++) {
      const u = TSP_WALK[i], v = TSP_WALK[i+1];
      S('line', {x1: TSP_CITIES[u][0], y1: TSP_CITIES[u][1], x2: TSP_CITIES[v][0], y2: TSP_CITIES[v][1], class: 'edge tour'}, svg);
    }
  } else if (tspStep === 3) {
    for (let i = 0; i < TSP_TOUR.length - 1; i++) {
      const u = TSP_TOUR[i], v = TSP_TOUR[i+1];
      S('line', {x1: TSP_CITIES[u][0], y1: TSP_CITIES[u][1], x2: TSP_CITIES[v][0], y2: TSP_CITIES[v][1], class: 'edge good'}, svg);
    }
  }
  
  TSP_CITIES.forEach((p, i) => {
    const g = S('g', {class: 'node'}, svg);
    S('circle', {cx: p[0], cy: p[1], r: 16}, g);
    S('text', {x: p[0], y: p[1]}, g, i + 1);
  });
  
  const st = $('tsp-approx-status');
  if (tspStep === 1) st.innerHTML = '<b>Step 1: Compute Minimum Spanning Tree (MST).</b> Cost = <b>485.6</b>. By definition, MST Cost ≤ Optimal TSP Tour Cost.';
  else if (tspStep === 2) st.innerHTML = '<b>Step 2: Full Euler Walk of MST.</b> Every edge is traversed twice. Cost = 2 × 485.6 = <b>971.2</b>.';
  else if (tspStep === 3) st.innerHTML = '<b>Step 3: Preorder Shortcut Tour.</b> By the Triangle Inequality, skipping repeated cities cannot increase distance. Tour Cost = <b>753.2</b> (Optimal = 655.9, Ratio = <b>1.15 ≤ 2.0</b>).';
  
  const t = $('tsp-approx-table'); t.innerHTML = '';
  const hr = H('tr', null, null, t);
  ['Quantity', 'Cost', 'Ratio to Optimal'].forEach(h => H('th', null, h, hr));
  [['MST Cost', '485.6', '≤ OPT'],
   ['Full Tree Walk (2 × MST)', '971.2', '≤ 2.0 × OPT'],
   ['Algorithm Preorder Tour', '753.2', '1.15 × OPT (≤ 2.0)'],
   ['Brute-Force Optimal Tour', '655.9', '1.00 (Benchmark)']
  ].forEach(([q, c, r]) => {
    const row = H('tr', null, null, t);
    H('td', null, q, row);
    H('td', 'num', c, row);
    H('td', null, r, row);
  });
}
$('tsp-st1').onclick = () => { tspStep = 1; $('tsp-st1').classList.add('active'); $('tsp-st2').classList.remove('active'); $('tsp-st3').classList.remove('active'); drawTSPApprox(); };
$('tsp-st2').onclick = () => { tspStep = 2; $('tsp-st2').classList.add('active'); $('tsp-st1').classList.remove('active'); $('tsp-st3').classList.remove('active'); drawTSPApprox(); };
$('tsp-st3').onclick = () => { tspStep = 3; $('tsp-st3').classList.add('active'); $('tsp-st1').classList.remove('active'); $('tsp-st2').classList.remove('active'); drawTSPApprox(); };
drawTSPApprox();


// ==========================================
// SIMULATION 11: AMORTIZED BINARY COUNTER
// ==========================================
let cntVal = 0, cntTotalFlips = 0;
const cntBitsHistory = [0, 0, 0, 0, 0, 0];

function updateCounterDisplay() {
  const container = $('cnt-bits'); container.innerHTML = '';
  for (let i = 5; i >= 0; i--) {
    const bit = (cntVal >> i) & 1;
    const box = H('div', 'row', null, container);
    box.style.flexDirection = 'column';
    box.style.padding = '8px 12px';
    box.style.borderRadius = '8px';
    box.style.border = '1.5px solid var(--line)';
    box.style.background = bit ? 'var(--accent-soft)' : 'var(--sunk)';
    H('span', 'mono', String(bit), box);
    box.firstChild.style.fontSize = '24px';
    box.firstChild.style.fontWeight = '800';
    H('small', null, 'Bit ' + i, box);
    box.lastChild.style.color = 'var(--muted)';
  }
  const avg = cntVal ? (cntTotalFlips / cntVal).toFixed(2) : '0.00';
  $('cnt-status').textContent = 'Counter: ' + cntVal + ' | Total Bit Flips: ' + cntTotalFlips + ' | Running Average Flips/Increment: ' + avg + ' (< 2.0 guaranteed!)';
  drawCounterSVG();
}

function incCounter() {
  cntVal++;
  let flips = 0;
  for (let i = 0; i < 6; i++) {
    if (cntVal % (1 << i) === 0) {
      flips++;
      cntBitsHistory[i]++;
    }
  }
  cntTotalFlips += flips;
  updateCounterDisplay();
}

function drawCounterSVG() {
  const svg = $('cnt-svg'); svg.innerHTML = '';
  const W = 420, Hh = 180;
  S('line', {x1: 40, x2: W - 10, y1: Hh - 30, y2: Hh - 30, stroke: 'var(--line)'}, svg);
  const maxF = Math.max(...cntBitsHistory, 1);
  
  cntBitsHistory.forEach((f, i) => {
    const bw = 36;
    const bx = 60 + i * 54;
    const bh = (f / maxF) * 110;
    const by = Hh - 30 - bh;
    S('rect', {x: bx, y: by, width: bw, height: bh, fill: 'var(--accent)', rx: 4}, svg);
    S('text', {x: bx + bw/2, y: by - 6, 'text-anchor': 'middle', 'font-size': 11, 'font-weight': 700}, svg, String(f));
    S('text', {x: bx + bw/2, y: Hh - 12, 'text-anchor': 'middle', 'font-size': 11}, svg, 'b' + i);
  });
}
$('cnt-step-btn').onclick = incCounter;
$('cnt-step10-btn').onclick = () => { for (let i = 0; i < 10; i++) incCounter(); };
$('cnt-reset-btn').onclick = () => {
  cntVal = 0; cntTotalFlips = 0;
  for (let i = 0; i < 6; i++) cntBitsHistory[i] = 0;
  updateCounterDisplay();
};
updateCounterDisplay();


// ==========================================
// SIMULATION 12: ARRAY DOUBLING (SHOPKEEPER)
// ==========================================
let arrSize = 0, arrCap = 1, arrCredit = 0;
const arrCosts = [];

function drawArraySVG() {
  const svg = $('arr-svg'); svg.innerHTML = '';
  const W = 420, Hh = 180;
  S('line', {x1: 30, x2: W - 10, y1: Hh - 25, y2: Hh - 25, stroke: 'var(--line)'}, svg);
  S('line', {x1: 30, x2: W - 10, y1: Hh - 25 - (3/32)*130, y2: Hh - 25 - (3/32)*130, stroke: 'var(--ok)', 'stroke-dasharray': '4 4'}, svg);
  S('text', {x: W - 15, y: Hh - 25 - (3/32)*130 - 4, 'text-anchor': 'end', 'font-size': 10, style: 'fill:var(--ok); font-weight:700;'}, svg, 'Amortized Bound = 3');
  
  if (!arrCosts.length) return;
  const n = arrCosts.length;
  arrCosts.forEach(([actual, runningAvg], idx) => {
    const x = 35 + (idx / Math.max(n, 32)) * (W - 55);
    const yBar = Hh - 25 - (actual / 34) * 130;
    S('line', {x1: x, x2: x, y1: Hh - 25, y2: yBar, stroke: actual > 2 ? 'var(--hard)' : 'var(--accent)', 'stroke-width': 2}, svg);
  });
}

function insertItem() {
  arrSize++;
  let actualCost = 2; // Rs 2 write
  if (arrSize > arrCap) {
    const copyCost = arrCap;
    arrCap *= 2;
    actualCost += copyCost;
  }
  arrCredit += (5 - actualCost); // Rs 5 charged
  
  const totalActual = arrCosts.reduce((s, c) => s + c[0], 0) + actualCost;
  const runningAvg = (totalActual / arrSize).toFixed(2);
  arrCosts.push([actualCost, runningAvg]);
  
  $('arr-size').textContent = arrSize;
  $('arr-cap').textContent = arrCap;
  $('arr-credit').textContent = 'Rs ' + arrCredit + ' (Bank ≥ 0 ✓)';
  
  const container = $('arr-blocks');
  container.innerHTML = '';
  for (let i = 0; i < Math.min(arrCap, 32); i++) {
    const b = H('div', null, null, container);
    b.style.width = '12px'; b.style.height = '18px';
    b.style.borderRadius = '3px';
    b.style.border = '1px solid var(--line)';
    b.style.background = i < arrSize ? 'var(--accent)' : 'var(--sunk)';
  }
  $('arr-status').className = 'status-box ' + (arrCredit >= 0 ? 'ok' : 'bad');
  $('arr-status').textContent = 'Sale #' + arrSize + ': Actual Cost = ' + actualCost + (actualCost > 2 ? ' (EXPENSIVE COPY SPIKE!)' : ' (Regular write)') + ' | Running Average: ' + runningAvg + ' / sale.';
  drawArraySVG();
}

$('arr-insert-btn').onclick = insertItem;
$('arr-insert10-btn').onclick = () => { for (let i = 0; i < 10; i++) insertItem(); };
$('arr-reset-btn').onclick = () => {
  arrSize = 0; arrCap = 1; arrCredit = 0; arrCosts.length = 0;
  $('arr-size').textContent = '0';
  $('arr-cap').textContent = '1';
  $('arr-credit').textContent = 'Rs 0';
  $('arr-blocks').innerHTML = '';
  $('arr-status').className = 'status-box';
  $('arr-status').textContent = 'Insert sales to observe array doubling and bank credit.';
  drawArraySVG();
};


// ==========================================
// SIMULATION 13: MONTE CARLO PI DARTBOARD
// ==========================================
let piTotal = 0, piHits = 0;
const piCanvas = $('pi-canvas');
const piCtx = piCanvas.getContext('2d');

function initPiCanvas() {
  piCtx.fillStyle = '#f8fafc';
  piCtx.fillRect(0, 0, 300, 300);
  piCtx.strokeStyle = '#0d7a6a';
  piCtx.lineWidth = 2.5;
  piCtx.beginPath();
  piCtx.arc(0, 300, 300, -Math.PI / 2, 0);
  piCtx.stroke();
}
initPiCanvas();

function throwDarts(count) {
  for (let i = 0; i < count; i++) {
    const x = Math.random();
    const y = Math.random();
    const hit = (x * x + y * y) <= 1.0;
    piTotal++;
    if (hit) piHits++;
    
    // Draw dot on canvas (inverted y)
    piCtx.fillStyle = hit ? '#0d7a6a' : '#c4331f';
    piCtx.fillRect(x * 300, (1 - y) * 300, 2, 2);
  }
  const estPi = (4 * piHits / piTotal).toFixed(4);
  const err = (Math.abs(estPi - Math.PI) / Math.PI * 100).toFixed(2);
  $('pi-status').textContent = 'Darts: ' + piTotal.toLocaleString() + ' | Inside: ' + piHits.toLocaleString() + ' | Estimated π: ' + estPi + ' (Error: ' + err + '%)';
  updatePiTable();
}
function updatePiTable() {
  const t = $('pi-table'); t.innerHTML = '';
  const hr = H('tr', null, null, t);
  ['Sample Size N', 'Est. π', 'Absolute Error'].forEach(h => H('th', null, h, hr));
  [[100, 3.1200, 0.0216], [1000, 3.1480, 0.0064], [10000, 3.1428, 0.0012], [100000, 3.1419, 0.0003]].forEach(([n, est, err]) => {
    const r = H('tr', null, null, t);
    H('td', 'num', n.toLocaleString(), r);
    H('td', 'num', est.toFixed(4), r);
    H('td', 'num', err.toFixed(4), r);
  });
}
$('pi-throw100-btn').onclick = () => throwDarts(500);
$('pi-throw5000-btn').onclick = () => throwDarts(5000);
$('pi-reset-btn').onclick = () => {
  piTotal = 0; piHits = 0;
  initPiCanvas();
  $('pi-status').textContent = 'Darts: 0 | Hits: 0 | Estimated π: 0.0000';
  updatePiTable();
};
updatePiTable();


// ==========================================
// SIMULATION 14: QUICKSORT DUEL (RAMESH VS SURESH)
// ==========================================
let duelInputType = 'sorted';
let sureshRunsHistory = [];

function countQuicksortComparisons(arr, isRandom) {
  let comps = 0;
  const a = arr.slice();
  function qs(p, r) {
    if (p < r) {
      if (isRandom) {
        const randIdx = p + Math.floor(Math.random() * (r - p + 1));
        const temp = a[randIdx]; a[randIdx] = a[r]; a[r] = temp;
      }
      const pivot = a[r];
      let i = p - 1;
      for (let j = p; j < r; j++) {
        comps++;
        if (a[j] <= pivot) {
          i++;
          const t = a[i]; a[i] = a[j]; a[j] = t;
        }
      }
      const t = a[i + 1]; a[i + 1] = a[r]; a[r] = t;
      const q = i + 1;
      qs(p, q - 1);
      qs(q + 1, r);
    }
  }
  qs(0, a.length - 1);
  return comps;
}

function runDuel() {
  const n = 50;
  let testArr = [];
  if (duelInputType === 'sorted') {
    for (let i = 1; i <= n; i++) testArr.push(i);
  } else if (duelInputType === 'reverse') {
    for (let i = n; i >= 1; i--) testArr.push(i);
  } else {
    for (let i = 1; i <= n; i++) testArr.push(Math.floor(Math.random() * 500));
  }
  
  const rameshComps = countQuicksortComparisons(testArr, false);
  const sureshComps = countQuicksortComparisons(testArr, true);
  sureshRunsHistory.push(sureshComps);
  
  const t = $('duel-table'); t.innerHTML = '';
  const hr = H('tr', null, null, t);
  ['Student & Pivot Strategy', 'Comparisons (n=50)', 'Time Order'].forEach(h => H('th', null, h, hr));
  
  const r1 = H('tr', rameshComps > 1000 ? 'danger' : '', null, t);
  H('td', null, 'Ramesh (Last Element)', r1);
  H('td', 'num', rameshComps.toLocaleString(), r1);
  H('td', null, rameshComps > 1000 ? 'Θ(n²) Worst Case!' : 'O(n log n)', r1);
  
  const r2 = H('tr', 'highlight', null, t);
  H('td', null, 'Suresh (Random Pivot)', r2);
  H('td', 'num', sureshComps.toLocaleString(), r2);
  H('td', null, 'O(n log n) Expected', r2);
  
  drawDuelHistogram();
}

function drawDuelHistogram() {
  const svg = $('duel-svg'); svg.innerHTML = '';
  const W = 380, Hh = 200;
  S('line', {x1: 30, x2: W - 10, y1: Hh - 25, y2: Hh - 25, stroke: 'var(--line)'}, svg);
  S('text', {x: W - 10, y: Hh - 8, 'text-anchor': 'end', 'font-size': 11, style: 'fill:var(--muted);'}, svg, 'Comparisons');
  
  if (!sureshRunsHistory.length) return;
  const buckets = {};
  sureshRunsHistory.forEach(c => {
    const b = Math.floor(c / 50) * 50;
    buckets[b] = (buckets[b] || 0) + 1;
  });
  const maxCount = Math.max(...Object.values(buckets), 1);
  const keys = Object.keys(buckets).map(Number).sort((a,b)=>a-b);
  
  keys.forEach((bVal, i) => {
    const cnt = buckets[bVal];
    const bw = Math.min(26, (W - 60) / keys.length - 4);
    const bx = 40 + i * (bw + 4);
    const bh = (cnt / maxCount) * 120;
    const by = Hh - 25 - bh;
    S('rect', {x: bx, y: by, width: bw, height: bh, fill: 'var(--accent)', rx: 3}, svg);
    S('text', {x: bx + bw/2, y: Hh - 10, 'text-anchor': 'middle', 'font-size': 9}, svg, String(bVal));
  });
}

$('duel-sorted').onclick = () => { duelInputType = 'sorted'; $('duel-sorted').classList.add('active'); $('duel-reverse').classList.remove('active'); $('duel-random').classList.remove('active'); runDuel(); };
$('duel-reverse').onclick = () => { duelInputType = 'reverse'; $('duel-reverse').classList.add('active'); $('duel-sorted').classList.remove('active'); $('duel-random').classList.remove('active'); runDuel(); };
$('duel-random').onclick = () => { duelInputType = 'random'; $('duel-random').classList.add('active'); $('duel-sorted').classList.remove('active'); $('duel-reverse').classList.remove('active'); runDuel(); };
$('duel-run-btn').onclick = runDuel;
$('duel-multi-btn').onclick = () => {
  for (let i = 0; i < 100; i++) runDuel();
};
runDuel();


// ==========================================
// MASTER QUESTION BANK RENDERER (ALL 32 PYQS)
// ==========================================
function renderPDFQBank() {
  const container = $('pdf-qbank-list');
  if (!container) return;
  container.innerHTML = '';
  
  const searchQ = ($('pyq-search-input')?.value || '').toLowerCase().trim();
  const topicFilter = $('pyq-topic-filter')?.value || 'all';
  
  const filtered = PDF_32_QUESTIONS.filter(q => {
    if (topicFilter !== 'all' && q.topic !== topicFilter) return false;
    if (searchQ) {
      const hay = (q.question + ' ' + q.paper + ' ' + q.short_answer + ' ' + q.full_solution).toLowerCase();
      if (!hay.includes(searchQ)) return false;
    }
    return true;
  });
  
  if (!filtered.length) {
    container.innerHTML = '<div class="status-box">No past-exam questions match your filter. Try clearing the search.</div>';
    return;
  }
  
  filtered.forEach(q => {
    const card = H('div', 'q-card', null, container);
    const head = H('div', 'q-card-head', null, card);
    H('span', 'q-paper-badge', q.paper + ' · ' + q.q, head);
    H('span', 'q-marks-badge', q.marks + ' Marks · ' + q.topic_name, head);
    
    H('div', 'q-text', q.question, card);
    
    const say = H('div', 'say-box', null, card);
    say.style.margin = '8px 0';
    say.innerHTML = '<b>Short Answer:</b> ' + q.short_answer;
    
    const dt = H('details', 'solution-detail', null, card);
    H('summary', null, 'View Full Model Answer (Exam Ready)', dt);
    const body = H('div', 'solution-body', null, dt);
    H('pre', 'code-block', q.full_solution, body);
  });
}
$('pyq-search-input')?.addEventListener('input', renderPDFQBank);
$('pyq-topic-filter')?.addEventListener('change', renderPDFQBank);
renderPDFQBank();


// ==========================================
// INTERACTIVE EXAM MCQ TRAINER
// ==========================================
const MCQS_DATA = [
  {
    src: 'Autumn 2024 Q1(h) · 1 Mark',
    q: 'Which of the following methods is NOT used for amortized analysis of algorithms?',
    opts: ['Accounting method', 'Potential function method', 'Sorting method', 'Aggregate method'],
    ans: 2,
    why: 'Correct! The three standard CLRS methods for amortized analysis are Aggregate, Accounting, and Potential function methods. Sorting is an algorithmic problem, not an amortized technique.'
  },
  {
    src: 'Autumn 2025 Q1(b) · 1 Mark',
    q: 'Which algorithm uses random input to reduce expected running time or memory usage, but ALWAYS terminates with a correct result in bounded time?',
    opts: ['Las Vegas Algorithm', 'Monte Carlo Algorithm', 'Dynamic Algorithm', 'Approximation Algorithm'],
    ans: 0,
    why: 'Correct! Las Vegas algorithms always produce the 100% correct answer (e.g. Randomized Quicksort). Monte Carlo algorithms have bounded time but carry a small probability of error.'
  },
  {
    src: 'Autumn 2025 Q1(i) · 1 Mark',
    q: 'Consider a decision problem Q. 3CNF-SAT reduces in polynomial time to Q (3-SAT ≤p Q). Which one of the following is consistent with this statement?',
    opts: ['Q is in NP', 'Q is in NP-hard', 'Q is in NPC', 'Q is in P'],
    ans: 1,
    why: 'Correct! 3-SAT is a known NP-complete problem. Since 3-SAT ≤p Q, Q is at least as hard as 3-SAT, making Q NP-hard. Q is not guaranteed to be in NP (it could be undecidable), so NPC is not guaranteed.'
  },
  {
    src: 'Autumn 2024 Q1(j) · 1 Mark',
    q: 'Shahrukh shows 3-SAT ≤p Superstar. Salman shows Superstar ≤p 3-SAT. What can be inferred about Superstar?',
    opts: ['NP-hard but not NP-complete', 'NP-complete', 'In NP but not NP-complete', 'Neither NP-hard nor in NP'],
    ans: 1,
    why: 'Correct! 3-SAT ≤p Superstar proves Superstar is NP-hard. Superstar ≤p 3-SAT (which is in NP) proves Superstar ∈ NP. By definition, being in NP and NP-hard means Superstar is NP-complete!'
  },
  {
    src: 'Spring 2023 Q1(c)(ii) · 1 Mark',
    q: 'True or False: If problem X can be reduced to a known NP-hard problem in polynomial time (X ≤p Known_NP_Hard), then X must be NP-hard.',
    opts: ['True', 'False'],
    ans: 1,
    why: 'Correct! FALSE! This is the classic Direction Trap. X ≤p H only means X is no harder than H. A trivial problem in P (like 1+1=2) reduces to 3-SAT, but that does not make 1+1 NP-hard! To prove X is NP-hard, the reduction must go the other way: Known_NP_Hard ≤p X.'
  },
  {
    src: 'Autumn 2022 Q1(e) · 1 Mark',
    q: 'A polynomial-time algorithm is discovered that correctly computes the largest clique in a graph. Which Venn diagram of P, NP and NPC is correct?',
    opts: ['(A) NPC inside NP, with P inside NP separately', '(B) P and NP overlapping, with NPC in the overlap', '(C) One merged region P = NP, with NPC drawn inside it', '(D) P = NP = NPC (all three collapsed)'],
    ans: 2,
    why: 'Correct! Since Clique is NP-complete, a polynomial algorithm for it implies P = NP. Both classes merge into one. NPC sits inside this merged region (or is equal to it except for trivial always-yes/always-no problems). Diagram C.'
  }
];

function renderMCQs() {
  const container = $('mcq-trainer-list');
  if (!container) return;
  container.innerHTML = '';
  
  MCQS_DATA.forEach((m, idx) => {
    const box = H('div', 'mcq-box', null, container);
    H('div', 'mcq-src', m.src, box);
    H('div', 'mcq-q', (idx + 1) + '. ' + m.q, box);
    
    const ob = H('div', 'mcq-opts', null, box);
    let answered = false;
    
    m.opts.forEach((optText, oIdx) => {
      const b = H('button', 'mcq-opt', optText, ob);
      b.onclick = () => {
        if (answered) return;
        answered = true;
        ob.querySelectorAll('.mcq-opt').forEach((x, k) => {
          if (k === m.ans) x.classList.add('correct');
          else if (x === b) x.classList.add('wrong');
        });
        const w = H('div', 'mcq-why', (oIdx === m.ans ? '🎉 ' : '⚠️ ') + m.why, box);
      };
    });
  });
}
renderMCQs();


// ==========================================
// PYQ ATLAS INTEGRATED ENGINE (ALL 6 SUBJECTS)
// ==========================================
let atlasSubj = 'DAA';
let atlasTopic = 'all';

function renderAtlas() {
  const nav = $('atlas-subject-nav');
  if (!nav) return;
  nav.innerHTML = '';
  
  const subjects = ['DAA', 'DOS', 'CN', 'DMDW', 'SE', 'EE'];
  subjects.forEach(sid => {
    const sData = PYQ_DATABASE[sid];
    if (!sData) return;
    const b = H('button', 'btn' + (sid === atlasSubj ? ' active' : ''), null, nav);
    H('span', null, sData.shortName || sData.name, b);
    H('small', 'mono', ' (' + (sData.questions?.length || 0) + ' Qs)', b);
    b.onclick = () => {
      atlasSubj = sid;
      atlasTopic = 'all';
      renderAtlas();
    };
  });
  
  const curr = PYQ_DATABASE[atlasSubj];
  if (!curr) return;
  
  $('atlas-title').textContent = curr.name + ' (' + curr.code + ')';
  $('atlas-desc').textContent = curr.description || 'Complete official question bank and topic blueprint.';
  
  // Topic Filter Select
  const topicSel = $('atlas-topic-select');
  topicSel.innerHTML = '<option value="all">All Topics (' + (curr.questions?.length || 0) + ' questions)</option>';
  (curr.topics || []).forEach(t => {
    const opt = H('option', null, t.name + ' (' + (t.weightPercent || t.weight || '') + '%)', topicSel);
    opt.value = t.id;
  });
  topicSel.value = atlasTopic;
  topicSel.onchange = () => {
    atlasTopic = topicSel.value;
    renderAtlasCards();
  };
  
  renderAtlasHeatmap(curr);
  renderAtlasCards();
}

function renderAtlasHeatmap(sData) {
  const container = $('atlas-heatmap-area');
  if (!container) return;
  container.innerHTML = '';
  
  const wrap = H('div', 'heatmap-container', null, container);
  const t = H('table', 'heat-table', null, wrap);
  const hr = H('tr', null, null, t);
  H('th', 'tn', 'Topic / Concept', hr);
  
  const papers = sData.yearsCovered || [];
  papers.forEach(p => H('th', null, p.replace('Autumn ', 'Aut ').replace('Spring ', 'Spr '), hr));
  H('th', null, 'Total Qs', hr);
  
  (sData.topics || []).forEach(tp => {
    const r = H('tr', null, null, t);
    H('td', 'tn', tp.name, r);
    let totalInTopic = 0;
    papers.forEach(p => {
      const count = (sData.questions || []).filter(q => q.topicId === tp.id && q.year === p).length;
      totalInTopic += count;
      const lv = count === 0 ? 0 : Math.min(4, count);
      const cell = H('td', 'heat-cell h' + lv, count ? String(count) : '·', r);
    });
    H('td', 'heat-cell', String(totalInTopic), r);
  });
}

function renderAtlasCards() {
  const container = $('atlas-questions-list');
  if (!container) return;
  container.innerHTML = '';
  
  const curr = PYQ_DATABASE[atlasSubj];
  if (!curr) return;
  
  const searchTxt = ($('atlas-search-input')?.value || '').toLowerCase().trim();
  const qList = (curr.questions || []).filter(q => {
    if (atlasTopic !== 'all' && q.topicId !== atlasTopic) return false;
    if (searchTxt) {
      const hay = (q.text + ' ' + q.concept + ' ' + (q.blueprint || '')).toLowerCase();
      if (!hay.includes(searchTxt)) return false;
    }
    return true;
  });
  
  $('atlas-count-badge').textContent = qList.length + ' Questions Found';
  
  if (!qList.length) {
    container.innerHTML = '<div class="status-box">No questions match your filter.</div>';
    return;
  }
  
  qList.forEach(q => {
    const card = H('div', 'q-card', null, container);
    const head = H('div', 'q-card-head', null, card);
    H('span', 'q-paper-badge', q.year + ' · Q' + q.qNumber + (q.subPart ? '(' + q.subPart + ')' : ''), head);
    H('span', 'q-marks-badge', (q.marks || 5) + ' Marks · ' + (q.frequency || 'Regular'), head);
    
    H('div', 'q-text', q.text, card);
    
    if (q.blueprint) {
      const dt = H('details', 'solution-detail', null, card);
      H('summary', null, 'View Solution Blueprint & Steps', dt);
      const body = H('div', 'solution-body', null, dt);
      H('pre', 'code-block', q.blueprint, body);
    }
  });
}
$('atlas-search-input')?.addEventListener('input', renderAtlasCards);
renderAtlas();
"""

print("site_scripts.py created.")
