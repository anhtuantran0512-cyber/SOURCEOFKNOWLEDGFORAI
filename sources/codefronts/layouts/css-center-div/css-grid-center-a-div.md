---
source: "codefronts"
url: "https://codefronts.com/layouts/css-center-div/css-grid-center-a-div/"
title: "CSS Grid Center a Div"
section: "layouts"
category: "css-center-div"
category_name: "CSS Ways to Center a Div"
description: "Three CSS Grid centering techniques — place-items shorthand, a 3×3 named template that puts the child at column 2/row 2, and the grid-absorbs-free-space…"
has_js: "false"
---

Here's a working CSS Ways to Center a Div from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Grid Center a Div
Source: https://codefronts.com/layouts/css-center-div/css-grid-center-a-div/

Three CSS Grid centering techniques — place-items shorthand, a 3×3 named template that puts the child at column 2/row 2, and the grid-absorbs-free-space margin:auto pattern.
## HTML
```html
<div class="cd-02">
  <div class="cd-02__header">
    <div class="cd-02__badge">Pure CSS</div>
    <h2>CSS Grid Center a Div</h2>
    <p>Three grid centering techniques — place-items, named template areas, and auto margins</p>
  </div>

  <div class="cd-02__viewport">

    <!-- Demo 1: place-items: center -->
    <div class="cd-02__demo">
      <div class="cd-02__demo-label">
        <span>place-items shorthand</span>
        <code>display:grid; place-items:center</code>
      </div>
      <div class="cd-02__stage cd-02__stage--place">
        <div class="cd-02__dots"></div>
        <div class="cd-02__lines"></div>
        <div class="cd-02__card cd-02__center">
          <h3>Grid Centered</h3>
          <p>Two properties, total control</p>
        </div>
      </div>
    </div>

    <!-- Demo 2: 3-col 3-row template -->
    <div class="cd-02__demo">
      <div class="cd-02__demo-label">
        <span>3-col / 3-row template</span>
        <code>grid-template: 1fr auto 1fr / 1fr auto 1fr</code>
      </div>
      <div class="cd-02__stage cd-02__stage--template">
        <div class="cd-02__dots"></div>
        <div class="cd-02__lines"></div>
        <div class="cd-02__card cd-02__center">
          <h3>Column 2 · Row 2</h3>
          <p>Exact grid placement</p>
        </div>
      </div>
    </div>

    <!-- Demo 3: margin auto inside grid -->
    <div class="cd-02__demo">
      <div class="cd-02__demo-label">
        <span>Auto margins inside grid</span>
        <code>display:grid → margin:auto on child</code>
      </div>
      <div class="cd-02__stage cd-02__stage--margins">
        <div class="cd-02__dots"></div>
        <div class="cd-02__lines"></div>
        <div class="cd-02__card cd-02__center">
          <h3>Margin Auto Magic</h3>
          <p>Grid absorbs free space</p>
        </div>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.cd-02,
.cd-02 *,
.cd-02 *::before,
.cd-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cd-02 ::selection {
  background: #f59e0b;
  color: #000;
}

.cd-02 {
  --bg: #0c0a00;
  --surface: #151200;
  --border: rgba(245,158,11,.12);
  --accent: #f59e0b;
  --accent2: #fcd34d;
  --text: #fefce8;
  --muted: rgba(254,252,232,.45);
  font-family: 'Segoe UI', system-ui, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 40px 24px;
  color: var(--text);
}

.cd-02__header {
  text-align: center;
  margin-bottom: 40px;
}

.cd-02__badge {
  display: inline-flex;
  align-items: center;
  background: rgba(245,158,11,.12);
  border: 1px solid rgba(245,158,11,.3);
  border-radius: 6px;
  padding: 4px 12px;
  font-size: .75rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--accent2);
  margin-bottom: 16px;
}

.cd-02__header h2 {
  font-size: clamp(1.4rem, 4vw, 2rem);
  font-weight: 700;
  letter-spacing: -.02em;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.cd-02__header p {
  margin-top: 8px;
  color: var(--muted);
  font-size: .9rem;
}

.cd-02__viewport {
  max-width: 900px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.cd-02__demo {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 20px;
  overflow: hidden;
}

.cd-02__demo-label {
  padding: 14px 24px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.cd-02__demo-label span {
  font-size: .78rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: .1em;
  color: var(--muted);
}

.cd-02__demo-label code {
  font-size: .78rem;
  background: rgba(245,158,11,.15);
  color: var(--accent2);
  padding: 2px 8px;
  border-radius: 4px;
  font-family: 'Cascadia Code', 'Fira Code', monospace;
}

.cd-02__stage {
  height: 280px;
  position: relative;
}
/* ── Grid center: place-items shorthand ── */

.cd-02__stage--place {
  display: grid;
  place-items: center;
}
/* ── Grid center: named template ── */

.cd-02__stage--template {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  grid-template-rows: 1fr auto 1fr;
  gap: 0;
}

.cd-02__stage--template .cd-02__center {
  grid-column: 2;
  grid-row: 2;
}
/* ── Grid center: auto margins ── */

.cd-02__stage--margins {
  display: grid;
}

.cd-02__stage--margins .cd-02__center {
  margin: auto;
}
/* ── Cards ── */

.cd-02__card {
  background: linear-gradient(135deg, rgba(245,158,11,.18), rgba(252,211,77,.1));
  border: 1px solid rgba(245,158,11,.3);
  border-radius: 16px;
  padding: 28px 36px;
  text-align: center;
  box-shadow: 0 8px 32px rgba(245,158,11,.12);
  position: relative;
  z-index: 1;
}

.cd-02__card h3 {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 6px;
}

.cd-02__card p {
  font-size: .82rem;
  color: var(--muted);
}
/* ── Dot grid ── */

.cd-02__dots {
  position: absolute;
  inset: 0;
  background-image: radial-gradient(rgba(245,158,11,.18) 1px, transparent 1px);
  background-size: 28px 28px;
  pointer-events: none;
}
/* ── Grid lines overlay ── */

.cd-02__lines {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.cd-02__lines::before,
.cd-02__lines::after {
  content: '';
  position: absolute;
  background: rgba(245,158,11,.1);
}

.cd-02__lines::before {
  width: 1px;
  height: 100%;
  left: 50%;
}

.cd-02__lines::after {
  width: 100%;
  height: 1px;
  top: 50%;
}
/* ── Grid cell highlight visual ── */

.cd-02__cell-markers {
  position: absolute;
  inset: 0;
  pointer-events: none;
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  grid-template-rows: 1fr auto 1fr;
}

.cd-02__cell-markers span {
  border: 1px dashed rgba(245,158,11,.08);
}

@media (max-width: 600px) {
  .cd-02__demo-label {
    flex-direction: column;
    align-items: flex-start;
    gap: 6px;
  }

  .cd-02__stage {
    height: auto;
    min-height: 200px;
    padding: 32px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cd-02 * {
    animation: none !important;
    transition: none !important;
  }
}
```
