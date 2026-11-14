---
source: "codefronts"
url: "https://codefronts.com/layouts/css-center-div/css-margin-auto-center-a-div/"
title: "CSS Margin Auto Center a Div"
section: "layouts"
category: "css-center-div"
category_name: "CSS Ways to Center a Div"
description: "Horizontal and block centering via the classic margin:0 auto, the modern logical margin-inline:auto equivalent, and the real-world max-width +…"
has_js: "false"
---

Here's a working CSS Ways to Center a Div from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Margin Auto Center a Div
Source: https://codefronts.com/layouts/css-center-div/css-margin-auto-center-a-div/

Horizontal and block centering via the classic margin:0 auto, the modern logical margin-inline:auto equivalent, and the real-world max-width + margin-inline:auto content-column pattern.
## HTML
```html
<div class="cd-04">
  <div class="cd-04__header">
    <div class="cd-04__badge">Pure CSS</div>
    <h2>CSS Margin Auto Center a Div</h2>
    <p>Horizontal centering via margin auto, logical properties, and max-width content blocks</p>
  </div>

  <div class="cd-04__viewport">

    <!-- Method 1: margin: 0 auto -->
    <div class="cd-04__demo">
      <div class="cd-04__demo-label">
        <span>Classic margin auto</span>
        <code>width:fit-content; margin:0 auto</code>
      </div>
      <div class="cd-04__stage cd-04__stage--h-center">
        <div class="cd-04__rail"></div>
        <div class="cd-04__card cd-04__center--margin-auto">
          <h3>Margin Auto</h3>
          <p>The original horizontal centerer</p>
        </div>
      </div>
    </div>

    <!-- Method 2: margin-inline: auto (logical properties) -->
    <div class="cd-04__demo">
      <div class="cd-04__demo-label">
        <span>Logical properties</span>
        <code>margin-inline:auto; margin-block:auto</code>
      </div>
      <div class="cd-04__stage cd-04__stage--logical">
        <div class="cd-04__rail"></div>
        <div class="cd-04__card cd-04__center--logical">
          <h3>margin-inline: auto</h3>
          <p>Writing-mode aware, direction-safe</p>
        </div>
      </div>
    </div>

    <!-- Method 3: max-width + margin-inline auto -->
    <div class="cd-04__demo">
      <div class="cd-04__demo-label">
        <span>Max-width content centering</span>
        <code>max-width:560px; margin-inline:auto</code>
      </div>
      <div class="cd-04__stage cd-04__stage--content">
        <div class="cd-04__maxw-guide"></div>
        <div class="cd-04__content-wrapper">
          <div class="cd-04__content-block">
            <h3>Page Content Block</h3>
            <p>This is the real-world pattern — constrain width, auto-center inline</p>
          </div>
          <div class="cd-04__content-block">
            <h3>Works at Any Viewport</h3>
            <p>Centered on wide screens, full-bleed on mobile</p>
          </div>
        </div>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.cd-04,
.cd-04 *,
.cd-04 *::before,
.cd-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cd-04 ::selection {
  background: #10b981;
  color: #000;
}

.cd-04 {
  --bg: #020c08;
  --surface: #071410;
  --border: rgba(16,185,129,.1);
  --accent: #10b981;
  --accent2: #6ee7b7;
  --text: #ecfdf5;
  --muted: rgba(236,253,245,.45);
  font-family: 'Segoe UI', system-ui, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 40px 24px;
  color: var(--text);
}

.cd-04__header {
  text-align: center;
  margin-bottom: 40px;
}

.cd-04__badge {
  display: inline-flex;
  align-items: center;
  background: rgba(16,185,129,.12);
  border: 1px solid rgba(16,185,129,.3);
  border-radius: 6px;
  padding: 4px 12px;
  font-size: .75rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--accent2);
  margin-bottom: 16px;
}

.cd-04__header h2 {
  font-size: clamp(1.4rem, 4vw, 2rem);
  font-weight: 700;
  letter-spacing: -.02em;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.cd-04__header p {
  margin-top: 8px;
  color: var(--muted);
  font-size: .9rem;
}

.cd-04__viewport {
  max-width: 900px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.cd-04__demo {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 20px;
  overflow: hidden;
}

.cd-04__demo-label {
  padding: 14px 24px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.cd-04__demo-label span {
  font-size: .78rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: .1em;
  color: var(--muted);
}

.cd-04__demo-label code {
  font-size: .78rem;
  background: rgba(16,185,129,.15);
  color: var(--accent2);
  padding: 2px 8px;
  border-radius: 4px;
  font-family: 'Cascadia Code', 'Fira Code', monospace;
}

.cd-04__stage {
  height: 240px;
  position: relative;
  padding: 24px;
  display: flex;
  align-items: center;
}
/* ── Method 1: margin: 0 auto (horizontal only) ── */

.cd-04__stage--h-center {
  display: block;
  overflow: auto;
}

.cd-04__center--margin-auto {
  margin: 0 auto;
  width: fit-content;
  /* vertical centering via line-height trick */
  position: relative;
  top: 50%;
  transform: translateY(-50%);
}
/* ── Method 2: margin-inline: auto (logical) ── */

.cd-04__stage--logical {
  display: block;
  overflow: auto;
}

.cd-04__center--logical {
  margin-inline: auto;
  margin-block: auto;
  width: fit-content;
  /* Needs a block formatting context — use absolute parent here */
  position: relative;
  top: 50%;
  transform: translateY(-50%);
}
/* ── Method 3: max-width + margin auto (content centering) ── */

.cd-04__stage--content {
  display: block;
  padding: 0;
}

.cd-04__content-wrapper {
  max-width: 560px;
  width: 100%;
  margin-inline: auto;
  padding: 40px 32px;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 12px;
}
/* ── Cards ── */

.cd-04__card {
  background: linear-gradient(135deg, rgba(16,185,129,.18), rgba(110,231,183,.1));
  border: 1px solid rgba(16,185,129,.3);
  border-radius: 16px;
  padding: 24px 32px;
  text-align: center;
  box-shadow: 0 8px 32px rgba(16,185,129,.1);
}

.cd-04__card h3 {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 6px;
}

.cd-04__card p {
  font-size: .82rem;
  color: var(--muted);
}
/* ── Content block ── */

.cd-04__content-block {
  border-left: 3px solid var(--accent);
  padding: 16px 20px;
  background: rgba(16,185,129,.06);
  border-radius: 0 12px 12px 0;
}

.cd-04__content-block h3 {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 4px;
}

.cd-04__content-block p {
  font-size: .82rem;
  color: var(--muted);
}
/* ── Rail lines ── */

.cd-04__rail {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.cd-04__rail::before,
.cd-04__rail::after {
  content: '';
  position: absolute;
  background: rgba(16,185,129,.08);
}

.cd-04__rail::before {
  width: 1px;
  height: 100%;
  left: 50%;
}

.cd-04__rail::after {
  width: 100%;
  height: 1px;
  top: 50%;
}
/* ── Max-width borders ── */

.cd-04__maxw-guide {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 50%;
  width: 560px;
  transform: translateX(-50%);
  border-left: 1px dashed rgba(16,185,129,.2);
  border-right: 1px dashed rgba(16,185,129,.2);
  pointer-events: none;
}

@media (max-width: 600px) {
  .cd-04__demo-label {
    flex-direction: column;
    align-items: flex-start;
    gap: 6px;
  }

  .cd-04__stage {
    height: auto;
    min-height: 180px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cd-04 * {
    animation: none !important;
    transition: none !important;
  }
}
```
