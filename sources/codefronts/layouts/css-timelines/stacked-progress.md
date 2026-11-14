---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/stacked-progress/"
title: "Product Roadmap Timeline — Quarter Columns with Status Chips"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "The public-roadmap layout SaaS companies publish: four quarter columns of feature cards, each double-coded with a status chip (Shipped ✓ / In progress ◐ /…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Product Roadmap Timeline — Quarter Columns with Status Chips
Source: https://codefronts.com/layouts/css-timelines/stacked-progress/

The public-roadmap layout SaaS companies publish: four quarter columns of feature cards, each double-coded with a status chip (Shipped ✓ / In progress ◐ / Planned ○), and a 'today' line dropped precisely between quarters with a labeled flag — the format that turns 'when is dark mode coming' support tickets into a URL.
## HTML
```html
<section class="tls-25" aria-label="Product roadmap timeline demo">
  <div class="tls-25__inner">
    <header class="tls-25__head">
      <h3 class="tls-25__title">2026 Roadmap</h3>
      <p class="tls-25__legend"><span data-status="shipped" class="tls-25__chip">Shipped</span><span data-status="progress" class="tls-25__chip">In progress</span><span data-status="planned" class="tls-25__chip">Planned</span></p>
    </header>
    <div class="tls-25__boardWrap" style="--today:62.5%">
      <div class="tls-25__now" aria-hidden="true"><span class="tls-25__nowFlag">Today</span></div>
      <div class="tls-25__board">
      <section class="tls-25__q">
        <h4 class="tls-25__qh">Q1</h4>
        <article class="tls-25__card" data-status="shipped"><span class="tls-25__chip" data-status="shipped">Shipped</span><p class="tls-25__f">SSO &amp; SAML</p></article>
        <article class="tls-25__card" data-status="shipped"><span class="tls-25__chip" data-status="shipped">Shipped</span><p class="tls-25__f">Audit log export</p></article>
      </section>
      <section class="tls-25__q">
        <h4 class="tls-25__qh">Q2</h4>
        <article class="tls-25__card" data-status="shipped"><span class="tls-25__chip" data-status="shipped">Shipped</span><p class="tls-25__f">Mobile app (iOS + Android)</p></article>
        <article class="tls-25__card" data-status="shipped"><span class="tls-25__chip" data-status="shipped">Shipped</span><p class="tls-25__f">Workflow templates</p></article>
      </section>
      <section class="tls-25__q">
        <h4 class="tls-25__qh">Q3</h4>
        <article class="tls-25__card" data-status="progress"><span class="tls-25__chip" data-status="progress">In progress</span><p class="tls-25__f">Real-time collaboration</p></article>
        <article class="tls-25__card" data-status="progress"><span class="tls-25__chip" data-status="progress">In progress</span><p class="tls-25__f">Dark mode</p></article>
        <article class="tls-25__card" data-status="planned"><span class="tls-25__chip" data-status="planned">Planned</span><p class="tls-25__f">Public API v2</p></article>
      </section>
      <section class="tls-25__q">
        <h4 class="tls-25__qh">Q4</h4>
        <article class="tls-25__card" data-status="planned"><span class="tls-25__chip" data-status="planned">Planned</span><p class="tls-25__f">Self-hosted edition</p></article>
        <article class="tls-25__card" data-status="planned"><span class="tls-25__chip" data-status="planned">Planned</span><p class="tls-25__f">Plugin marketplace</p></article>
      </section>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.tls-25,
.tls-25 *,
.tls-25 *::before,
.tls-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-25 {
  min-height: 100vh;
  width: 100%;
  --tl-done: #15803d;
  --tl-prog: #b45309;
  --tl-plan: #64748b;
  --tl-line: #e2e8f0;
  --tl-ink: #0f172a;
  --tl-mut: #64748b;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f8fafc;
  padding: 64px 24px;
  display: grid;
  place-items: center;
}

.tls-25__inner {
  width: min(860px,100%);
}

.tls-25__head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
  margin-bottom: 26px;
}

.tls-25__title {
  font-size: clamp(22px,3.5vw,28px);
  font-weight: 800;
  color: var(--tl-ink);
  letter-spacing: -.02em;
}

.tls-25__legend {
  display: flex;
  gap: 8px;
}
/* Board wrapper is position:relative so the TODAY line — a direct
   absolute-positioned child of the wrapper, NOT a grid item — is
   positioned relative to the wrapper's padding-box (which stretches
   the full quarters grid width AND height). This avoids the CSS Grid
   quirk where an absolutely-positioned grid item auto-flows into
   cell 1,1 and its left offset resolves relative to that cell
   instead of the whole grid. */

.tls-25__boardWrap {
  position: relative;
}

.tls-25__board {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 16px;
}

.tls-25__now {
  position: absolute;
  left: var(--today,50%);
  top: 32px;
  bottom: 0;
  width: 2px;
  background: #dc2626;
  z-index: 2;
  pointer-events: none;
}

.tls-25__nowFlag {
  position: absolute;
  top: -14px;
  left: 50%;
  translate: -50% 0;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: #fff;
  background: #dc2626;
  border-radius: 4px;
  padding: 2px 9px;
  white-space: nowrap;
  box-shadow: 0 4px 12px -4px rgba(220,38,38,.5);
}
/* Each quarter is a vertical stack; align-content:start pushes cards
   to the top so a 2-card quarter and a 3-card quarter both start at
   the same y-coordinate. */

.tls-25__q {
  display: grid;
  grid-auto-rows: min-content;
  gap: 10px;
  align-content: start;
}

.tls-25__qh {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--tl-mut);
  border-bottom: 2px solid var(--tl-line);
  padding-bottom: 8px;
  margin-bottom: 2px;
}

.tls-25__card {
  background: #fff;
  border: 1px solid var(--tl-line);
  border-left-width: 3px;
  border-radius: 10px;
  padding: 12px 14px;
  display: grid;
  gap: 8px;
}

.tls-25__card[data-status="shipped"] {
  border-left-color: var(--tl-done);
  opacity: .75;
}

.tls-25__card[data-status="progress"] {
  border-left-color: var(--tl-prog);
}

.tls-25__card[data-status="planned"] {
  border-left-color: var(--tl-plan);
  border-style: solid solid solid dashed;
}

.tls-25__f {
  font-size: 13.5px;
  font-weight: 600;
  color: var(--tl-ink);
  line-height: 1.4;
  text-wrap: pretty;
}

.tls-25__chip {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  justify-self: start;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .04em;
  border-radius: 999px;
  padding: 2px 9px;
}

.tls-25__chip::before {
  content: '';
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.tls-25__chip[data-status="shipped"] {
  color: var(--tl-done);
  background: #f0fdf4;
}

.tls-25__chip[data-status="shipped"]::before {
  background: var(--tl-done);
}

.tls-25__chip[data-status="progress"] {
  color: var(--tl-prog);
  background: #fffbeb;
}

.tls-25__chip[data-status="progress"]::before {
  background: linear-gradient(90deg,var(--tl-prog) 50%,#fde68a 50%);
}

.tls-25__chip[data-status="planned"] {
  color: var(--tl-plan);
  background: #f1f5f9;
}

.tls-25__chip[data-status="planned"]::before {
  background: transparent;
  border: 2px solid var(--tl-plan);
  width: 8px;
  height: 8px;
}

@media (max-width: 640px) {
  .tls-25__board {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    padding-bottom: 8px;
  }

  .tls-25__q {
    flex: none;
    width: 75%;
    scroll-snap-align: start;
  }

  .tls-25__now,
    .tls-25__boardWrap>.tls-25__now {
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — status is a data-status attribute driving chip glyph, color and border via attribute selectors; the today line position is one --today custom property (compute it server-side for live dates). */
```
