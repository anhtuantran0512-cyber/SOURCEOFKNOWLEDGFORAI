---
source: "codefronts"
url: "https://codefronts.com/layouts/css-center-div/css-center-a-div-all-methods/"
title: "CSS Center a Div All Methods"
section: "layouts"
category: "css-center-div"
category_name: "CSS Ways to Center a Div"
description: "Side-by-side comparison of every major CSS centering technique — Flexbox, Grid, Absolute+Transform, Table-cell, and the Writing-mode trick — each in its own…"
has_js: "false"
---

Here's a working CSS Ways to Center a Div from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Center a Div All Methods
Source: https://codefronts.com/layouts/css-center-div/css-center-a-div-all-methods/

Side-by-side comparison of every major CSS centering technique — Flexbox, Grid, Absolute+Transform, Table-cell, and the Writing-mode trick — each in its own live tile with browser support chips.
## HTML
```html
<div class="cd-05">
  <div class="cd-05__header">
    <div class="cd-05__badge">Pure CSS</div>
    <h2>CSS Center a Div — All 5 Methods</h2>
    <p>Flexbox, Grid, Absolute, Table-cell, and Writing-mode — every technique side by side</p>
  </div>

  <div class="cd-05__grid">

    <!-- 1: Flexbox -->
    <div class="cd-05__tile">
      <div class="cd-05__tile-label">
        <h3>1 · Flexbox</h3>
        <code>display:flex; align-items:center; justify-content:center</code>
      </div>
      <div class="cd-05__stage cd-05__stage--flex">
        <div class="cd-05__cross"></div>
        <div class="cd-05__box cd-05__box--flex">Flexbox</div>
      </div>
      <div class="cd-05__support">
        <span class="cd-05__chip cd-05__chip--green">Modern ✓</span>
        <span class="cd-05__chip cd-05__chip--green">2-axis</span>
        <span class="cd-05__chip cd-05__chip--blue">Chrome 21+</span>
      </div>
    </div>

    <!-- 2: Grid place-items -->
    <div class="cd-05__tile">
      <div class="cd-05__tile-label">
        <h3>2 · CSS Grid</h3>
        <code>display:grid; place-items:center</code>
      </div>
      <div class="cd-05__stage cd-05__stage--grid">
        <div class="cd-05__cross"></div>
        <div class="cd-05__box cd-05__box--grid">Grid</div>
      </div>
      <div class="cd-05__support">
        <span class="cd-05__chip cd-05__chip--green">Modern ✓</span>
        <span class="cd-05__chip cd-05__chip--green">Shortest</span>
        <span class="cd-05__chip cd-05__chip--blue">Chrome 57+</span>
      </div>
    </div>

    <!-- 3: Absolute + translate -->
    <div class="cd-05__tile">
      <div class="cd-05__tile-label">
        <h3>3 · Absolute + Transform</h3>
        <code>position:absolute; top:50%; left:50%; transform:translate(-50%,-50%)</code>
      </div>
      <div class="cd-05__stage cd-05__stage--abs">
        <div class="cd-05__cross"></div>
        <div class="cd-05__box cd-05__box--abs cd-05__abs-child">Absolute</div>
      </div>
      <div class="cd-05__support">
        <span class="cd-05__chip cd-05__chip--green">Universal ✓</span>
        <span class="cd-05__chip cd-05__chip--warn">Needs parent</span>
        <span class="cd-05__chip cd-05__chip--blue">IE9+</span>
      </div>
    </div>

    <!-- 4: table-cell -->
    <div class="cd-05__tile">
      <div class="cd-05__tile-label">
        <h3>4 · Table-Cell</h3>
        <code>display:table-cell; vertical-align:middle; text-align:center</code>
      </div>
      <div class="cd-05__table-wrap">
        <div class="cd-05__stage cd-05__stage--table">
          <div class="cd-05__cross"></div>
          <div class="cd-05__box cd-05__box--table" style="display:inline-block">Table Cell</div>
        </div>
      </div>
      <div class="cd-05__support">
        <span class="cd-05__chip cd-05__chip--warn">Legacy</span>
        <span class="cd-05__chip cd-05__chip--warn">Semantic cost</span>
        <span class="cd-05__chip cd-05__chip--blue">IE8+</span>
      </div>
    </div>

    <!-- 5: Writing-mode trick -->
    <div class="cd-05__tile">
      <div class="cd-05__tile-label">
        <h3>5 · Writing-Mode Trick</h3>
        <code>writing-mode → inline-block child → reset writing-mode</code>
      </div>
      <div class="cd-05__stage cd-05__stage--writing">
        <div class="cd-05__cross"></div>
        <div class="cd-05__box cd-05__box--writing">Writing-Mode</div>
      </div>
      <div class="cd-05__support">
        <span class="cd-05__chip cd-05__chip--warn">Obscure</span>
        <span class="cd-05__chip cd-05__chip--warn">RTL care needed</span>
        <span class="cd-05__chip cd-05__chip--blue">Chrome 25+</span>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.cd-05,
.cd-05 *,
.cd-05 *::before,
.cd-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cd-05 ::selection {
  background: #8b5cf6;
  color: #fff;
}

.cd-05 {
  --bg: #08060f;
  --surface: #0e0b1a;
  --border: rgba(139,92,246,.1);
  --accent: #8b5cf6;
  --accent2: #c4b5fd;
  --orange: #fb923c;
  --teal: #2dd4bf;
  --text: #f5f3ff;
  --muted: rgba(245,243,255,.45);
  font-family: 'Segoe UI', system-ui, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 40px 24px;
  color: var(--text);
}

.cd-05__header {
  text-align: center;
  margin-bottom: 40px;
}

.cd-05__badge {
  display: inline-flex;
  align-items: center;
  background: rgba(139,92,246,.12);
  border: 1px solid rgba(139,92,246,.3);
  border-radius: 6px;
  padding: 4px 12px;
  font-size: .75rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--accent2);
  margin-bottom: 16px;
}

.cd-05__header h2 {
  font-size: clamp(1.4rem, 4vw, 2rem);
  font-weight: 700;
  letter-spacing: -.02em;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.cd-05__header p {
  margin-top: 8px;
  color: var(--muted);
  font-size: .9rem;
}
/* ── Comparison grid ── */

.cd-05__grid {
  max-width: 960px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 20px;
}

.cd-05__tile {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 20px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.cd-05__tile-label {
  padding: 16px 20px 12px;
  border-bottom: 1px solid var(--border);
}

.cd-05__tile-label h3 {
  font-size: .88rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 4px;
}

.cd-05__tile-label code {
  font-size: .72rem;
  background: rgba(139,92,246,.15);
  color: var(--accent2);
  padding: 2px 8px;
  border-radius: 4px;
  font-family: 'Cascadia Code', 'Fira Code', monospace;
  word-break: break-all;
}

.cd-05__stage {
  flex: 1;
  height: 200px;
  position: relative;
}
/* ── Crosshair ── */

.cd-05__cross {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.cd-05__cross::before,
.cd-05__cross::after {
  content: '';
  position: absolute;
  background: rgba(139,92,246,.1);
}

.cd-05__cross::before {
  width: 1px;
  height: 100%;
  left: 50%;
}

.cd-05__cross::after {
  width: 100%;
  height: 1px;
  top: 50%;
}
/* ── METHOD 1: Flexbox ── */

.cd-05__stage--flex {
  display: flex;
  align-items: center;
  justify-content: center;
}
/* ── METHOD 2: Grid place-items ── */

.cd-05__stage--grid {
  display: grid;
  place-items: center;
}
/* ── METHOD 3: Absolute + translate ── */

.cd-05__stage--abs {
  position: relative;
}

.cd-05__abs-child {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
/* ── METHOD 4: table-cell (legacy) ── */

.cd-05__table-wrap {
  display: table;
  width: 100%;
  height: 200px;
}

.cd-05__stage--table {
  display: table-cell;
  vertical-align: middle;
  text-align: center;
  height: 200px;
}
/* ── METHOD 5: sticky/sticky scroll snap (CSS-only modal-like center) ── */

.cd-05__stage--writing {
  writing-mode: horizontal-tb;
  display: flex;
  align-items: center;
  justify-content: center;
}
/* ── Boxes inside stages ── */

.cd-05__box {
  border-radius: 12px;
  padding: 18px 24px;
  text-align: center;
  font-size: .85rem;
  font-weight: 600;
  color: var(--text);
  white-space: nowrap;
  border: 1px solid;
}

.cd-05__box--flex {
  background: rgba(99,102,241,.2);
  border-color: rgba(99,102,241,.4);
  box-shadow: 0 0 20px rgba(99,102,241,.2);
}

.cd-05__box--grid {
  background: rgba(245,158,11,.15);
  border-color: rgba(245,158,11,.35);
  box-shadow: 0 0 20px rgba(245,158,11,.15);
}

.cd-05__box--abs {
  background: rgba(236,72,153,.15);
  border-color: rgba(236,72,153,.35);
  box-shadow: 0 0 20px rgba(236,72,153,.15);
}

.cd-05__box--table {
  background: rgba(16,185,129,.15);
  border-color: rgba(16,185,129,.35);
  box-shadow: 0 0 20px rgba(16,185,129,.15);
}

.cd-05__box--writing {
  background: rgba(251,146,60,.15);
  border-color: rgba(251,146,60,.35);
  box-shadow: 0 0 20px rgba(251,146,60,.15);
}
/* ── Support indicator ── */

.cd-05__support {
  padding: 10px 20px 14px;
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}

.cd-05__chip {
  font-size: .68rem;
  padding: 2px 8px;
  border-radius: 20px;
  font-weight: 600;
  letter-spacing: .04em;
}

.cd-05__chip--green {
  background: rgba(16,185,129,.15);
  color: #6ee7b7;
}

.cd-05__chip--blue {
  background: rgba(99,102,241,.15);
  color: #a5b4fc;
}

.cd-05__chip--warn {
  background: rgba(245,158,11,.15);
  color: #fcd34d;
}

@media (max-width: 480px) {
  .cd-05__stage {
    height: 160px;
  }

  .cd-05__table-wrap {
    height: 160px;
  }

  .cd-05__stage--table {
    height: 160px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cd-05 * {
    animation: none !important;
    transition: none !important;
  }
}
```
