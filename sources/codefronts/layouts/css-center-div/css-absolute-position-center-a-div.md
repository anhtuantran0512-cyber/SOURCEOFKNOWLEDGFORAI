---
source: "codefronts"
url: "https://codefronts.com/layouts/css-center-div/css-absolute-position-center-a-div/"
title: "CSS Absolute Position Center a Div"
section: "layouts"
category: "css-center-div"
category_name: "CSS Ways to Center a Div"
description: "Three absolute-positioning centering methods demonstrated inside a glassmorphism UI — the classic top/left 50% + translate trick, inset:0 with margin:auto,…"
has_js: "false"
---

Here's a working CSS Ways to Center a Div from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Absolute Position Center a Div
Source: https://codefronts.com/layouts/css-center-div/css-absolute-position-center-a-div/

Three absolute-positioning centering methods demonstrated inside a glassmorphism UI — the classic top/left 50% + translate trick, inset:0 with margin:auto, and known-size calc offset.
## HTML
```html
<div class="cd-03">
  <div class="cd-03__blob cd-03__blob--a"></div>
  <div class="cd-03__blob cd-03__blob--b"></div>

  <div class="cd-03__header">
    <div class="cd-03__badge">Pure CSS</div>
    <h2>CSS Absolute Position Center a Div</h2>
    <p>Classic centering via position:absolute — translate trick, inset auto, and calc variants</p>
  </div>

  <div class="cd-03__viewport">

    <!-- Method 1: top/left 50% + translate -->
    <div class="cd-03__demo">
      <div class="cd-03__demo-label">
        <span>Top/Left 50% + translate</span>
        <code>top:50%; left:50%; transform:translate(-50%,-50%)</code>
      </div>
      <div class="cd-03__stage">
        <div class="cd-03__cross"></div>
        <div class="cd-03__corner cd-03__corner--tl"></div>
        <div class="cd-03__corner cd-03__corner--tr"></div>
        <div class="cd-03__corner cd-03__corner--bl"></div>
        <div class="cd-03__corner cd-03__corner--br"></div>
        <div class="cd-03__glass cd-03__center--translate">
          <h3>Translate Trick</h3>
          <p>Works at any unknown size</p>
        </div>
      </div>
    </div>

    <!-- Method 2: inset:0 + margin:auto -->
    <div class="cd-03__demo">
      <div class="cd-03__demo-label">
        <span>Inset 0 + margin auto</span>
        <code>position:absolute; inset:0; margin:auto; width:fit-content</code>
      </div>
      <div class="cd-03__stage">
        <div class="cd-03__cross"></div>
        <div class="cd-03__corner cd-03__corner--tl"></div>
        <div class="cd-03__corner cd-03__corner--tr"></div>
        <div class="cd-03__corner cd-03__corner--bl"></div>
        <div class="cd-03__corner cd-03__corner--br"></div>
        <div class="cd-03__glass cd-03__center--inset">
          <h3>Inset + Margin Auto</h3>
          <p>Modern, readable, no translate</p>
        </div>
      </div>
    </div>

    <!-- Method 3: percentage anchor with calc reminder -->
    <div class="cd-03__demo">
      <div class="cd-03__demo-label">
        <span>Anchor with calc offset</span>
        <code>top:calc(50% - Npx); left:calc(50% - Npx)</code>
      </div>
      <div class="cd-03__stage">
        <div class="cd-03__cross"></div>
        <div class="cd-03__corner cd-03__corner--tl"></div>
        <div class="cd-03__corner cd-03__corner--tr"></div>
        <div class="cd-03__corner cd-03__corner--bl"></div>
        <div class="cd-03__corner cd-03__corner--br"></div>
        <div class="cd-03__glass cd-03__center--calc">
          <h3>Calc Offset</h3>
          <p>Precise when dimensions are known</p>
        </div>
      </div>
    </div>

  </div>
</div>
```
## CSS
```css
.cd-03,
.cd-03 *,
.cd-03 *::before,
.cd-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cd-03 ::selection {
  background: #ec4899;
  color: #fff;
}

.cd-03 {
  --bg: #0d0818;
  --surface: #130f22;
  --border: rgba(236,72,153,.1);
  --accent: #ec4899;
  --accent2: #f9a8d4;
  --blue: #818cf8;
  --text: #fdf2f8;
  --muted: rgba(253,242,248,.45);
  font-family: 'Segoe UI', system-ui, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  padding: 40px 24px;
  color: var(--text);
}
/* ── Ambient glow blobs (decorative background) ── */

.cd-03__blob {
  position: fixed;
  border-radius: 50%;
  filter: blur(80px);
  opacity: .25;
  pointer-events: none;
  z-index: 0;
}

.cd-03__blob--a {
  width: 500px;
  height: 500px;
  background: var(--accent);
  top: -120px;
  left: -100px;
}

.cd-03__blob--b {
  width: 400px;
  height: 400px;
  background: var(--blue);
  bottom: -100px;
  right: -80px;
}

.cd-03__header {
  text-align: center;
  margin-bottom: 40px;
  position: relative;
  z-index: 1;
}

.cd-03__badge {
  display: inline-flex;
  align-items: center;
  background: rgba(236,72,153,.12);
  border: 1px solid rgba(236,72,153,.3);
  border-radius: 6px;
  padding: 4px 12px;
  font-size: .75rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--accent2);
  margin-bottom: 16px;
}

.cd-03__header h2 {
  font-size: clamp(1.4rem, 4vw, 2rem);
  font-weight: 700;
  letter-spacing: -.02em;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.cd-03__header p {
  margin-top: 8px;
  color: var(--muted);
  font-size: .9rem;
}

.cd-03__viewport {
  max-width: 900px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 32px;
  position: relative;
  z-index: 1;
}

.cd-03__demo {
  background: rgba(19,15,34,.6);
  border: 1px solid var(--border);
  border-radius: 20px;
  overflow: hidden;
  backdrop-filter: blur(20px);
}

.cd-03__demo-label {
  padding: 14px 24px;
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.cd-03__demo-label span {
  font-size: .78rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: .1em;
  color: var(--muted);
}

.cd-03__demo-label code {
  font-size: .78rem;
  background: rgba(236,72,153,.15);
  color: var(--accent2);
  padding: 2px 8px;
  border-radius: 4px;
  font-family: 'Cascadia Code', 'Fira Code', monospace;
}

.cd-03__stage {
  height: 280px;
  position: relative;
  overflow: hidden;
}
/* ── Method 1: top/left 50% + translate(-50%,-50%) ── */

.cd-03__center--translate {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
/* ── Method 2: inset:0 + margin:auto ── */

.cd-03__center--inset {
  position: absolute;
  inset: 0;
  margin: auto;
  width: fit-content;
  height: fit-content;
}
/* ── Method 3: calc center ── */

.cd-03__center--calc {
  position: absolute;
  /* centering via calc without knowing exact size — uses transform */
  top: calc(50% - 0px);
  left: calc(50% - 0px);
  transform: translate(-50%, -50%);
}
/* ── Glassmorphism cards ── */

.cd-03__glass {
  background: rgba(255,255,255,.06);
  border: 1px solid rgba(255,255,255,.15);
  border-radius: 20px;
  padding: 32px 40px;
  text-align: center;
  backdrop-filter: blur(24px);
  box-shadow: 0 8px 32px rgba(236,72,153,.15), inset 0 1px 0 rgba(255,255,255,.1);
  white-space: nowrap;
}

.cd-03__glass h3 {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 6px;
}

.cd-03__glass p {
  font-size: .82rem;
  color: var(--muted);
}
/* ── Crosshair lines ── */

.cd-03__cross {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.cd-03__cross::before,
.cd-03__cross::after {
  content: '';
  position: absolute;
  background: rgba(236,72,153,.1);
}

.cd-03__cross::before {
  width: 1px;
  height: 100%;
  left: 50%;
}

.cd-03__cross::after {
  width: 100%;
  height: 1px;
  top: 50%;
}
/* ── Corner tick marks ── */

.cd-03__corner {
  position: absolute;
  width: 14px;
  height: 14px;
  pointer-events: none;
}

.cd-03__corner--tl {
  top: 16px;
  left: 16px;
  border-top: 1px solid rgba(236,72,153,.3);
  border-left: 1px solid rgba(236,72,153,.3);
}

.cd-03__corner--tr {
  top: 16px;
  right: 16px;
  border-top: 1px solid rgba(236,72,153,.3);
  border-right: 1px solid rgba(236,72,153,.3);
}

.cd-03__corner--bl {
  bottom: 16px;
  left: 16px;
  border-bottom: 1px solid rgba(236,72,153,.3);
  border-left: 1px solid rgba(236,72,153,.3);
}

.cd-03__corner--br {
  bottom: 16px;
  right: 16px;
  border-bottom: 1px solid rgba(236,72,153,.3);
  border-right: 1px solid rgba(236,72,153,.3);
}

@media (max-width: 600px) {
  .cd-03__demo-label {
    flex-direction: column;
    align-items: flex-start;
    gap: 6px;
  }

  .cd-03__stage {
    height: 200px;
  }

  .cd-03__glass {
    padding: 20px 24px;
    white-space: normal;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cd-03 * {
    animation: none !important;
    transition: none !important;
  }
}
```
