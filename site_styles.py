# site_styles.py

CSS_CONTENT = """
:root {
  --bg: #f4f6f8;
  --surface: #ffffff;
  --surface-raised: #fbfcfd;
  --sunk: #e8edf0;
  --ink: #111a24;
  --ink-secondary: #485766;
  --muted: #627282;
  --line: #d1d9e0;
  --line-light: #e4eaf0;
  
  --accent: #0d7a6a;
  --accent-ink: #ffffff;
  --accent-soft: #d5efe9;
  --accent-hover: #0a6356;
  
  --hard: #c4331f;
  --hard-soft: #fbe6e3;
  --hard-border: #f28b7b;
  
  --mark: #ffd84a;
  --mark-ink: #3a2e00;
  --amber-soft: #fff1bf;
  
  --ok: #1a8746;
  --ok-soft: #d3f3e0;
  --no: #c4331f;
  --no-soft: #fbe6e3;
  
  --blue: #2354cf;
  --blue-soft: #e3ebfd;
  --purple: #7033ba;
  --purple-soft: #efe4fc;
  
  --heat0: #eef2f5;
  --heat1: #c9dbfb;
  --heat2: #84aaf7;
  --heat3: #437bf2;
  --heat4: #1c52cc;
  
  --font-display: 'Bricolage Grotesque', 'Segoe UI', system-ui, sans-serif;
  --font-body: 'Atkinson Hyperlegible', 'Segoe UI', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', ui-monospace, Menlo, monospace;
  --shadow-sm: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
  --shadow-md: 0 4px 8px -1px rgba(0,0,0,0.08), 0 2px 4px -1px rgba(0,0,0,0.04);
  --shadow-lg: 0 10px 20px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05);
}

:root[data-theme="dark"] {
  --bg: #0b1317;
  --surface: #121e24;
  --surface-raised: #182830;
  --sunk: #070e11;
  --ink: #e6edf3;
  --ink-secondary: #9db2c2;
  --muted: #798f9e;
  --line: #223540;
  --line-light: #1c2b34;
  
  --accent: #4fd1b9;
  --accent-ink: #06201b;
  --accent-soft: #123832;
  --accent-hover: #67ddc7;
  
  --hard: #ff8a76;
  --hard-soft: #381a17;
  --hard-border: #6a2a22;
  
  --mark: #ffd84a;
  --mark-ink: #2a2000;
  --amber-soft: #382e0e;
  
  --ok: #5fd68b;
  --ok-soft: #133a23;
  --no: #ff8a76;
  --no-soft: #381a17;
  
  --blue: #84aaf7;
  --blue-soft: #142852;
  --purple: #bf91fa;
  --purple-soft: #2e1b4d;
  
  --heat0: #142129;
  --heat1: #1d3954;
  --heat2: #245484;
  --heat3: #2c72b8;
  --heat4: #549eed;
  color-scheme: dark;
}

:root[data-theme="sepia"] {
  --bg: #f5eedf;
  --surface: #fdfaf3;
  --surface-raised: #ffffff;
  --sunk: #eae1ce;
  --ink: #2b251a;
  --ink-secondary: #5e5445;
  --muted: #7d7260;
  --line: #ded2bd;
  --line-light: #e8decd;
  
  --accent: #8b5712;
  --accent-ink: #ffffff;
  --accent-soft: #f2e3cc;
  --accent-hover: #71450b;
  
  --hard: #a8331d;
  --hard-soft: #f8ded7;
  --hard-border: #e38d78;
  
  --mark: #e09f19;
  --mark-ink: #2b251a;
  --amber-soft: #faecc9;
  
  --ok: #287a41;
  --ok-soft: #d6eedc;
  --no: #a8331d;
  --no-soft: #f8ded7;
  
  --blue: #2354cf;
  --blue-soft: #e3ebfd;
  --purple: #7033ba;
  --purple-soft: #efe4fc;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  background: var(--bg);
  color: var(--ink);
  font: 16px/1.65 var(--font-body);
  transition: background 0.2s ease, color 0.2s ease;
  min-height: 100vh;
}

/* Master Top Navigation Bar */
.topbar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--surface);
  border-bottom: 1.5px solid var(--line);
  backdrop-filter: blur(10px);
  padding: 8px 16px;
  box-shadow: var(--shadow-sm);
}
.topbar-wrap {
  max-width: 1320px;
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}
.brand-area {
  display: flex;
  align-items: center;
  gap: 12px;
}
.brand-logo {
  width: 38px;
  height: 38px;
  border-radius: 10px;
  background: var(--ink);
  color: var(--surface);
  display: grid;
  place-items: center;
  font: 800 18px var(--font-display);
  letter-spacing: -0.03em;
}
.brand-title {
  font: 800 20px/1.1 var(--font-display);
  letter-spacing: -0.02em;
}
.brand-subtitle {
  font-size: 12px;
  color: var(--muted);
}

.mode-tabs {
  display: flex;
  background: var(--sunk);
  padding: 3px;
  border-radius: 10px;
  gap: 2px;
  overflow-x: auto;
}
.mode-tab {
  background: none;
  border: none;
  padding: 6px 14px;
  border-radius: 8px;
  font: 600 13px var(--font-body);
  color: var(--ink-secondary);
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 6px;
}
.mode-tab:hover {
  color: var(--ink);
}
.mode-tab.active {
  background: var(--surface);
  color: var(--ink);
  box-shadow: var(--shadow-sm);
}

.top-controls {
  display: flex;
  align-items: center;
  gap: 10px;
}
.theme-picker {
  display: flex;
  background: var(--sunk);
  padding: 2px;
  border-radius: 8px;
}
.theme-btn {
  background: none;
  border: none;
  padding: 5px 8px;
  border-radius: 6px;
  font-size: 13px;
  cursor: pointer;
  color: var(--muted);
}
.theme-btn.active {
  background: var(--surface);
  color: var(--ink);
  box-shadow: var(--shadow-sm);
}

.progress-widget {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  color: var(--muted);
  font-family: var(--font-mono);
}
.progress-bar {
  width: 70px;
  height: 6px;
  background: var(--sunk);
  border-radius: 3px;
  overflow: hidden;
}
.progress-fill {
  height: 100%;
  background: var(--accent);
  width: 0%;
  transition: width 0.3s ease;
}

/* Page Layout */
.page-container {
  max-width: 1320px;
  margin: 0 auto;
  padding: 20px 16px 60px;
}

/* Hero Section */
.hero {
  padding: 24px 0 20px;
  border-bottom: 1.5px solid var(--line);
  margin-bottom: 24px;
}
.hero h1 {
  font: 800 clamp(30px, 4.5vw, 48px)/1.08 var(--font-display);
  letter-spacing: -0.025em;
  margin-bottom: 12px;
}
.hero h1 .hl {
  background: linear-gradient(transparent 58%, var(--mark) 58% 92%, transparent 92%);
  padding: 0 4px;
}
.hero p.lead {
  font-size: 18px;
  color: var(--ink-secondary);
  max-width: 74ch;
  line-height: 1.6;
}

.stat-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 18px;
}
.stat-pill {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 10px 16px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  min-width: 140px;
  box-shadow: var(--shadow-sm);
}
.stat-pill b {
  font: 800 24px/1 var(--font-display);
  color: var(--ink);
}
.stat-pill span {
  font-size: 12px;
  color: var(--muted);
  font-weight: 500;
}

/* Two-column layout for course */
.course-layout {
  display: grid;
  grid-template-columns: 260px minmax(0, 1fr);
  gap: 32px;
  align-items: start;
}
@media (max-width: 900px) {
  .course-layout {
    grid-template-columns: 1fr;
    gap: 16px;
  }
}

/* Sticky TOC Sidebar */
aside.toc-sidebar {
  position: sticky;
  top: 72px;
  max-height: calc(100vh - 84px);
  overflow-y: auto;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 14px 12px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  box-shadow: var(--shadow-sm);
}
.toc-sidebar h3 {
  font: 800 13px var(--font-display);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--muted);
  padding: 4px 8px 8px;
  border-bottom: 1px solid var(--line-light);
  margin-bottom: 6px;
}
.toc-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 7px 10px;
  border-radius: 8px;
  text-decoration: none;
  color: var(--ink-secondary);
  font-size: 13.5px;
  font-weight: 500;
  transition: all 0.15s ease;
}
.toc-item:hover {
  background: var(--sunk);
  color: var(--ink);
}
.toc-item.active {
  background: var(--accent-soft);
  color: var(--ink);
  font-weight: 700;
}
.toc-num {
  font: 600 11px var(--font-mono);
  background: var(--sunk);
  color: var(--ink);
  width: 20px;
  height: 20px;
  border-radius: 6px;
  display: grid;
  place-items: center;
  flex-shrink: 0;
}
.toc-item.active .toc-num {
  background: var(--accent);
  color: var(--accent-ink);
}
.toc-check {
  margin-left: auto;
  font-size: 12px;
  color: var(--ok);
  opacity: 0;
}
.toc-item.completed .toc-check {
  opacity: 1;
}

/* Lesson Structure */
.lesson-card {
  background: var(--surface);
  border: 1.5px solid var(--line);
  border-radius: 18px;
  padding: 30px;
  margin-bottom: 32px;
  box-shadow: var(--shadow-sm);
  scroll-margin-top: 80px;
}
.lesson-header {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 18px;
}
.lesson-badge {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: var(--ink);
  color: var(--surface);
  display: grid;
  place-items: center;
  font: 800 20px var(--font-display);
  flex-shrink: 0;
}
.lesson-titles {
  flex: 1;
}
.lesson-unit {
  font: 600 12px var(--font-mono);
  text-transform: uppercase;
  color: var(--accent);
  letter-spacing: 0.05em;
  margin-bottom: 2px;
}
.lesson-title {
  font: 800 clamp(22px, 3.2vw, 30px)/1.15 var(--font-display);
  letter-spacing: -0.015em;
  margin-bottom: 4px;
}

/* Alerts & Callouts */
.say-box {
  background: var(--amber-soft);
  border-left: 4px solid var(--mark);
  border-radius: 0 10px 10px 0;
  padding: 12px 18px;
  margin: 16px 0;
  font-size: 15px;
}
.say-box b {
  font-family: var(--font-display);
  color: var(--ink);
}
.analogy-box {
  background: var(--accent-soft);
  border-left: 4px solid var(--accent);
  border-radius: 0 10px 10px 0;
  padding: 14px 18px;
  margin: 16px 0;
  font-size: 15px;
}
.analogy-title {
  font: 700 13px var(--font-mono);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--accent-hover);
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.exam-trap-box {
  background: var(--hard-soft);
  border-left: 4px solid var(--hard);
  border-radius: 0 10px 10px 0;
  padding: 14px 18px;
  margin: 16px 0;
  font-size: 15px;
}
.exam-trap-title {
  font: 700 13px var(--font-mono);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--hard);
  margin-bottom: 4px;
}

.exam-pill-strip {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  align-items: center;
  margin: 16px 0 6px;
  font-size: 13px;
  color: var(--muted);
}
.exam-chip {
  font: 600 11px var(--font-mono);
  background: var(--hard-soft);
  color: var(--hard);
  border: 1px solid var(--hard-border);
  padding: 2px 8px;
  border-radius: 6px;
  white-space: nowrap;
}

/* Simulation Containers */
.sim-container {
  background: var(--surface-raised);
  border: 1.5px solid var(--line);
  border-radius: 16px;
  padding: 20px;
  margin: 22px 0;
  box-shadow: var(--shadow-sm);
}
.sim-header {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  margin-bottom: 12px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--line-light);
}
.sim-title {
  font: 800 17px var(--font-display);
  display: flex;
  align-items: center;
  gap: 8px;
}
.sim-hint {
  font-size: 13.5px;
  color: var(--muted);
  margin-bottom: 14px;
}

/* Interactive Elements */
.btn {
  font: 700 14px var(--font-body);
  padding: 8px 16px;
  border-radius: 10px;
  border: 1.5px solid var(--line);
  background: var(--surface);
  color: var(--ink);
  cursor: pointer;
  transition: all 0.15s ease;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.btn:hover {
  background: var(--sunk);
  border-color: var(--ink);
}
.btn.pri {
  background: var(--accent);
  border-color: var(--accent);
  color: var(--accent-ink);
}
.btn.pri:hover {
  background: var(--accent-hover);
}
.btn.danger {
  background: var(--hard);
  border-color: var(--hard);
  color: #ffffff;
}
.btn[aria-pressed="true"], .btn.active {
  background: var(--ink);
  color: var(--surface);
  border-color: var(--ink);
}

.status-box {
  background: var(--sunk);
  border-radius: 10px;
  padding: 10px 14px;
  font-size: 14.5px;
  min-height: 44px;
  display: flex;
  align-items: center;
  margin: 10px 0;
  transition: all 0.2s ease;
}
.status-box.ok {
  background: var(--ok-soft);
  color: var(--ink);
  border: 1px solid var(--ok);
  font-weight: 600;
}
.status-box.bad {
  background: var(--no-soft);
  color: var(--ink);
  border: 1px solid var(--no);
  font-weight: 600;
}
.status-box.warm {
  background: var(--amber-soft);
  color: var(--ink);
  border: 1px solid var(--mark);
}

/* Form inputs */
input[type="range"] {
  accent-color: var(--accent);
  cursor: pointer;
}
.row {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  align-items: center;
  margin: 10px 0;
}
.cols-2 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 340px), 1fr));
  gap: 18px;
  align-items: start;
}

/* Graph SVG & Canvas Styling */
svg.interactive-fig {
  width: 100%;
  height: auto;
  max-height: 380px;
  display: block;
  background: var(--bg);
  border-radius: 12px;
  border: 1px solid var(--line);
}
svg text {
  font-family: var(--font-body);
  fill: var(--ink);
  user-select: none;
}
canvas.sim-canvas {
  width: 100%;
  max-width: 440px;
  height: auto;
  background: var(--bg);
  border-radius: 12px;
  border: 1px solid var(--line);
  display: block;
}

/* Graph Nodes & Edges */
.node circle {
  fill: var(--surface);
  stroke: var(--ink);
  stroke-width: 2.2;
  cursor: pointer;
  transition: all 0.15s ease;
}
.node:hover circle {
  stroke: var(--accent);
  stroke-width: 3.5;
}
.node.sel circle {
  fill: var(--accent);
  stroke: var(--accent-hover);
}
.node.sel text {
  fill: var(--accent-ink);
}
.node.match circle {
  fill: var(--mark);
  stroke: var(--ink);
}
.node.cover circle {
  fill: var(--hard);
  stroke: var(--hard);
}
.node.cover text {
  fill: #ffffff;
}
.node text {
  font-weight: 700;
  font-size: 15px;
  text-anchor: middle;
  dominant-baseline: central;
  pointer-events: none;
}

.edge {
  stroke: var(--muted);
  stroke-width: 2.5;
  stroke-linecap: round;
  transition: all 0.2s ease;
}
.edge.good {
  stroke: var(--ok);
  stroke-width: 5;
}
.edge.badl {
  stroke: var(--no);
  stroke-width: 5;
  stroke-dasharray: 6 5;
}
.edge.matched {
  stroke: var(--mark);
  stroke-width: 6;
}
.edge.tour {
  stroke: var(--ink);
  stroke-width: 5;
}
.edge.tree {
  stroke: var(--blue);
  stroke-width: 4;
}
.edge.zero {
  stroke: var(--accent);
  stroke-width: 3.5;
}
.edge.one {
  stroke: var(--hard);
  stroke-width: 2;
  stroke-dasharray: 5 4;
}
.edge.faint {
  opacity: 0.25;
}

/* Tables */
table.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
}
table.data-table th, table.data-table td {
  padding: 8px 12px;
  border-bottom: 1px solid var(--line);
  text-align: left;
}
table.data-table th {
  font: 700 12px var(--font-body);
  text-transform: uppercase;
  color: var(--muted);
  background: var(--sunk);
}
table.data-table td.num {
  text-align: right;
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
}
table.data-table tr.highlight td {
  background: var(--amber-soft);
  font-weight: 700;
}
table.data-table tr.danger td {
  color: var(--hard);
  font-weight: 700;
}

/* Expandable Details */
details.solution-detail {
  background: var(--surface);
  border: 1.5px solid var(--line);
  border-radius: 12px;
  margin: 12px 0;
  overflow: hidden;
}
details.solution-detail summary {
  padding: 12px 16px;
  font: 700 15px var(--font-display);
  cursor: pointer;
  background: var(--sunk);
  display: flex;
  align-items: center;
  justify-content: space-between;
  user-select: none;
}
details.solution-detail summary:hover {
  background: var(--line);
}
details.solution-detail[open] summary {
  border-bottom: 1.5px solid var(--line);
}
.solution-body {
  padding: 16px;
  font-size: 14.5px;
}
pre.code-block {
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 12px;
  font: 500 13px/1.5 var(--font-mono);
  overflow-x: auto;
  margin: 10px 0;
}

/* Cheat Sheet Grid */
.cheat-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 320px), 1fr));
  gap: 16px;
}
.cheat-card {
  background: var(--surface);
  border: 1.5px solid var(--line);
  border-radius: 14px;
  padding: 16px;
}
.cheat-card h4 {
  font: 800 16px var(--font-display);
  margin-bottom: 8px;
  padding-bottom: 6px;
  border-bottom: 1.5px solid var(--line-light);
  color: var(--accent);
}
.cheat-card ul {
  padding-left: 20px;
  font-size: 14px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}

/* Question Bank Cards */
.q-card {
  background: var(--surface);
  border: 1.5px solid var(--line);
  border-radius: 14px;
  padding: 18px 20px;
  margin-bottom: 14px;
  box-shadow: var(--shadow-sm);
  transition: all 0.15s ease;
}
.q-card:hover {
  border-color: var(--accent);
}
.q-card-head {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  justify-content: space-between;
  gap: 8px;
  margin-bottom: 8px;
}
.q-paper-badge {
  font: 700 12px var(--font-mono);
  background: var(--accent-soft);
  color: var(--accent-hover);
  padding: 3px 8px;
  border-radius: 6px;
}
.q-marks-badge {
  font: 700 12px var(--font-mono);
  background: var(--sunk);
  padding: 3px 8px;
  border-radius: 6px;
}
.q-text {
  font-size: 15.5px;
  font-weight: 600;
  line-height: 1.45;
  margin-bottom: 10px;
}

/* Heatmap Grid */
.heatmap-container {
  overflow-x: auto;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 14px;
  margin: 16px 0;
}
table.heat-table {
  border-collapse: collapse;
  width: 100%;
  font-size: 13px;
}
table.heat-table th, table.heat-table td {
  padding: 8px 10px;
  text-align: center;
  border-bottom: 1px solid var(--line);
}
table.heat-table th.tn, table.heat-table td.tn {
  text-align: left;
  font-weight: 600;
  position: sticky;
  left: 0;
  background: var(--surface);
  border-right: 1px solid var(--line);
  min-width: 200px;
}
td.heat-cell.h0 { background: var(--heat0); color: var(--muted); }
td.heat-cell.h1 { background: var(--heat1); color: var(--ink); }
td.heat-cell.h2 { background: var(--heat2); color: #fff; font-weight: 700; }
td.heat-cell.h3 { background: var(--heat3); color: #fff; font-weight: 700; }
td.heat-cell.h4 { background: var(--heat4); color: #fff; font-weight: 700; }

/* Interactive Flash MCQ */
.mcq-box {
  background: var(--surface);
  border: 1.5px solid var(--line);
  border-radius: 14px;
  padding: 18px 20px;
  margin-bottom: 16px;
}
.mcq-src {
  font: 600 11px var(--font-mono);
  color: var(--hard);
  margin-bottom: 6px;
}
.mcq-q {
  font: 700 16px var(--font-display);
  margin-bottom: 12px;
}
.mcq-opts {
  display: grid;
  gap: 8px;
}
.mcq-opt {
  text-align: left;
  background: var(--surface-raised);
  border: 1.5px solid var(--line);
  border-radius: 10px;
  padding: 10px 14px;
  font: 500 14.5px var(--font-body);
  cursor: pointer;
  transition: all 0.15s ease;
}
.mcq-opt:hover {
  border-color: var(--accent);
  background: var(--sunk);
}
.mcq-opt.correct {
  background: var(--ok-soft) !important;
  border-color: var(--ok) !important;
  font-weight: 700;
}
.mcq-opt.wrong {
  background: var(--no-soft) !important;
  border-color: var(--no) !important;
  font-weight: 700;
}
.mcq-why {
  margin-top: 12px;
  padding: 10px 14px;
  background: var(--sunk);
  border-radius: 8px;
  font-size: 14px;
  line-height: 1.5;
}
"""

print("site_styles.py created.")

