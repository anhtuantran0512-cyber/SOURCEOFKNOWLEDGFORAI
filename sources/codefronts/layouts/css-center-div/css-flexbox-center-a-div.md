---
source: "codefronts"
url: "https://codefronts.com/layouts/css-center-div/css-flexbox-center-a-div/"
title: "CSS Flexbox Center a Div"
section: "layouts"
category: "css-center-div"
category_name: "CSS Ways to Center a Div"
description: "Three flex centering patterns showing how display:flex with align-items and justify-content centers a div both horizontally and vertically, as a row, and as…"
has_js: "false"
---

Here's a working CSS Ways to Center a Div from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Flexbox Center a Div
Source: https://codefronts.com/layouts/css-center-div/css-flexbox-center-a-div/

Three flex centering patterns showing how display:flex with align-items and justify-content centers a div both horizontally and vertically, as a row, and as a stacked column.
## HTML
```html
<div class="cd-01">
  <div class="cd-01__header">
    <div class="cd-01__badge">Pure CSS</div>
    <h2>CSS Flexbox Center a Div</h2>
    <p>Three flex centering patterns — single element, row of cards, and column stack</p>
  </div>

  <div class="cd-01__viewport">

    <!-- Demo 1: flex center both axes -->
    <div class="cd-01__demo">
      <div class="cd-01__demo-label">
        <span>Center both axes</span>
        <code>display:flex; align-items:center; justify-content:center</code>
      </div>
      <div class="cd-01__stage cd-01__stage--flex">
        <div class="cd-01__axis"></div>
        <div class="cd-01__grid-guide"></div>
        <div class="cd-01__card">
          <h3>Perfectly Centered</h3>
          <p>Both axes, one declaration</p>
        </div>
      </div>
    </div>

    <!-- Demo 2: flex row with gap -->
    <div class="cd-01__demo">
      <div class="cd-01__demo-label">
        <span>Row of items centered</span>
        <code>display:flex; justify-content:center; gap:20px</code>
      </div>
      <div class="cd-01__stage cd-01__stage--flex-row">
        <div class="cd-01__axis"></div>
        <div class="cd-01__card cd-01__card--sm">
          <h3>Card One</h3>
          <p>Auto aligned</p>
        </div>
        <div class="cd-01__card cd-01__card--sm">
          <h3>Card Two</h3>
          <p>Equal spacing</p>
        </div>
        <div class="cd-01__card cd-01__card--sm">
          <h3>Card Three</h3>
          <p>Via gap</p>
        </div>
      </div>
    </div>

    <!-- Demo 3: flex column center -->
    <div class="cd-01__demo">
      <div class="cd-01__demo-label">
        <span>Column stack centered</span>
        <code>flex-direction:column; align-items:center</code>
      </div>
      <div class="cd-01__stage cd-01__stage--flex-col">
        <div class="cd-01__axis"></div>
        <div class="cd-01__card">
          <h3>Stacked &amp; Centered</h3>
          <p>Column direction + align-items</p>
        </div>
        <div class="cd-01__pill">Call to Action</div>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.cd-01,
.cd-01 *,
.cd-01 *::before,
.cd-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cd-01 ::selection {
  background: #6366f1;
  color: #fff;
}

.cd-01 {
  --bg: #0a0a0f;
  --surface: #13131a;
  --border: rgba(255,255,255,.08);
  --accent: #6366f1;
  --accent2: #a78bfa;
  --text: #f1f0ff;
  --muted: rgba(241,240,255,.45);
  font-family: 'Segoe UI', system-ui, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 40px 24px;
  color: var(--text);
}
/* ── Label strip ── */

.cd-01__header {
  text-align: center;
  margin-bottom: 40px;
}

.cd-01__header h2 {
  font-size: clamp(1.4rem, 4vw, 2rem);
  font-weight: 700;
  letter-spacing: -.02em;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.cd-01__header p {
  margin-top: 8px;
  color: var(--muted);
  font-size: .9rem;
}
/* ── Code badge ── */

.cd-01__badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(99,102,241,.12);
  border: 1px solid rgba(99,102,241,.3);
  border-radius: 6px;
  padding: 4px 12px;
  font-size: .75rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--accent2);
  margin-bottom: 16px;
}
/* ── Main showcase container ── */

.cd-01__viewport {
  max-width: 900px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 32px;
}
/* ── Single demo cell ── */

.cd-01__demo {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 20px;
  overflow: hidden;
}

.cd-01__demo-label {
  padding: 14px 24px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.cd-01__demo-label span {
  font-size: .78rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: .1em;
  color: var(--muted);
}

.cd-01__demo-label code {
  font-size: .78rem;
  background: rgba(99,102,241,.15);
  color: var(--accent2);
  padding: 2px 8px;
  border-radius: 4px;
  font-family: 'Cascadia Code', 'Fira Code', monospace;
}
/* ── The actual centering playgrounds ── */

.cd-01__stage {
  height: 260px;
  position: relative;
}
/* Flexbox center both axes */

.cd-01__stage--flex {
  display: flex;
  align-items: center;
  justify-content: center;
}
/* Flex row with gap */

.cd-01__stage--flex-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 20px;
  flex-wrap: wrap;
  padding: 24px;
}
/* Flex column center */

.cd-01__stage--flex-col {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 12px;
}
/* ── Cards inside stages ── */

.cd-01__card {
  background: linear-gradient(135deg, rgba(99,102,241,.2), rgba(167,139,250,.15));
  border: 1px solid rgba(99,102,241,.3);
  border-radius: 16px;
  padding: 28px 36px;
  text-align: center;
  backdrop-filter: blur(12px);
  box-shadow: 0 8px 32px rgba(99,102,241,.15);
}

.cd-01__card h3 {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 6px;
}

.cd-01__card p {
  font-size: .82rem;
  color: var(--muted);
}

.cd-01__card--sm {
  padding: 20px 24px;
}

.cd-01__card--sm h3 {
  font-size: .95rem;
}

.cd-01__pill {
  background: linear-gradient(90deg, var(--accent), var(--accent2));
  border-radius: 50px;
  padding: 10px 28px;
  font-size: .85rem;
  font-weight: 600;
  color: #fff;
  box-shadow: 0 4px 20px rgba(99,102,241,.4);
}
/* ── Axis lines overlay ── */

.cd-01__axis {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.cd-01__axis::before,
.cd-01__axis::after {
  content: '';
  position: absolute;
  background: rgba(99,102,241,.12);
}

.cd-01__axis::before {
  width: 1px;
  height: 100%;
  left: 50%;
}

.cd-01__axis::after {
  width: 100%;
  height: 1px;
  top: 50%;
}
/* ── Grid guide ── */

.cd-01__grid-guide {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image: linear-gradient(rgba(99,102,241,.06) 1px, transparent 1px), linear-gradient(90deg, rgba(99,102,241,.06) 1px, transparent 1px);
  background-size: 40px 40px;
}

@media (max-width: 600px) {
  .cd-01__demo-label {
    flex-direction: column;
    align-items: flex-start;
    gap: 6px;
  }

  .cd-01__stage {
    height: auto;
    min-height: 200px;
    padding: 24px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cd-01 * {
    animation: none !important;
    transition: none !important;
  }
}
```
