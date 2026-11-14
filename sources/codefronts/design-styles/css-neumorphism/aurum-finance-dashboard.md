---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/aurum-finance-dashboard/"
title: "Neumorphic Card Grid with Depth Hierarchy"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "Soft UI's hardest layout problem: everything is the same colour, so hierarchy has to come from depth alone — and depth runs out of range after about three…"
has_js: "false"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Card Grid with Depth Hierarchy
Source: https://codefronts.com/design-styles/css-neumorphism/aurum-finance-dashboard/

Soft UI's hardest layout problem: everything is the same colour, so hierarchy has to come from depth alone — and depth runs out of range after about three levels. A grid of cards on an explicit three-step elevation scale, with nested surfaces showing where the scale breaks, and the compensations that let a nested inset well read clearly inside a raised card.
## HTML
```html
<section class="nm-10" aria-labelledby="nm-10-heading">
      <input type="checkbox" id="nm-10-theme" class="nm-10__themeinput">
      <label for="nm-10-theme" class="nm-10__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-10__stage">
    <header class="nm-10__head">
      <p class="nm-10__kicker">Layout · hierarchy</p>
      <h2 class="nm-10__heading" id="nm-10-heading">Three levels, then you are out of depth</h2>
      <p class="nm-10__sub">Everything is one colour, so elevation is the only structural signal — and it has a very short scale.</p>
    </header>

    <div class="nm-10__grid">
      <article class="nm-10__card nm-10__card--l3">
        <p class="nm-10__badge">Level 3 · 14px</p>
        <h3 class="nm-10__ctitle">Quarterly close</h3>
        <p class="nm-10__cbody">The highest surface in the layout. Reserve it for one element per screen — a modal, a primary panel, the thing you want read first.</p>
        <div class="nm-10__well">
          <div class="nm-10__wellrow"><span>Reconciled</span><b>92%</b></div>
          <div class="nm-10__bar"><span class="nm-10__barfill" style="width:92%"></span></div>
          <p class="nm-10__wellnote">An inset well inside a raised card — the direction change is what keeps both readable.</p>
        </div>
      </article>

      <article class="nm-10__card nm-10__card--l2">
        <p class="nm-10__badge">Level 2 · 8px</p>
        <h3 class="nm-10__ctitle">Open items</h3>
        <p class="nm-10__cbody">The workhorse level. Most cards in a soft-UI layout should sit here.</p>
        <ul class="nm-10__list">
          <li class="nm-10__item"><span>Invoice 4821</span><b>£1,240</b></li>
          <li class="nm-10__item"><span>Invoice 4822</span><b>£860</b></li>
          <li class="nm-10__item"><span>Invoice 4830</span><b>£2,720</b></li>
        </ul>
      </article>

      <article class="nm-10__card nm-10__card--l1">
        <p class="nm-10__badge">Level 1 · 4px</p>
        <h3 class="nm-10__ctitle">Archive</h3>
        <p class="nm-10__cbody">Barely lifted. Use for secondary or dismissed content that should still read as an object.</p>
      </article>

      <article class="nm-10__card nm-10__card--l4">
        <p class="nm-10__badge nm-10__badge--warn">Level 4 · 22px — too far</p>
        <h3 class="nm-10__ctitle">Out of range</h3>
        <p class="nm-10__cbody">The shadow has left the element's neighbourhood. It no longer reads as the same material as everything around it, which is where the scale ends.</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.nm-10 {
  position: relative;
  --nm-10-surface: #e8e6e1;
  --nm-10-dark: rgba(177,173,164,0.62);
  --nm-10-light: rgba(255,255,255,0.93);
  --nm-10-ink: #2a2925;
  --nm-10-muted: #5e5b53;
  --nm-10-border: #a19d94;
  --nm-10-accent: #4a6b8a;
  --nm-10-warn: #9c5227;
  --nm-10-dist: 8px;
  --nm-10-font-display: "Söhne", "Helvetica Neue", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-10-surface);
  color: var(--nm-10-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.01 85)) {
  .nm-10 {
    --nm-10-surface: oklch(0.915 0.006 85);
    --nm-10-ink: oklch(0.27 0.008 80);
    --nm-10-muted: oklch(0.46 0.011 80);
    --nm-10-accent: oklch(0.52 0.07 245);
    --nm-10-warn: oklch(0.5 0.12 50);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-10 {
    --nm-10-dark: color-mix(in oklab, var(--nm-10-surface), #000 19%);
    --nm-10-light: color-mix(in oklab, var(--nm-10-surface), #fff 92%);
    --nm-10-border: color-mix(in oklab, var(--nm-10-surface), var(--nm-10-ink) 33%);
  }
}

.nm-10 *,
.nm-10 *::before,
.nm-10 *::after {
  box-sizing: border-box;
}

.nm-10__stage {
  max-width: 1100px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(26px, 5vw, 58px) clamp(16px, 4vw, 42px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(22px, 3.6vw, 36px);
}

.nm-10__head {
  max-width: 60ch;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.nm-10__kicker {
  margin: 0;
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--nm-10-muted);
}

.nm-10__heading {
  margin: 0;
  font-family: var(--nm-10-font-display);
  font-size: clamp(1.5rem, 4.2vw, 2.3rem);
  font-weight: 600;
  letter-spacing: -0.025em;
  line-height: 1.1;
  text-wrap: balance;
}

.nm-10__sub {
  margin: 0;
  font-size: 0.94rem;
  line-height: 1.6;
  color: var(--nm-10-muted);
  text-wrap: pretty;
}

.nm-10__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr));
  gap: clamp(18px, 3vw, 28px);
  align-items: start;
}

.nm-10__card {
  border-radius: 22px;
  padding: clamp(18px, 3vw, 26px);
  background: var(--nm-10-surface);
  border: 1px solid var(--nm-10-border);
  display: flex;
  flex-direction: column;
  gap: 10px;
  min-inline-size: 0;
}

.nm-10__card--l1 {
  box-shadow: calc(var(--nm-10-dist) * 0.5) calc(var(--nm-10-dist) * 0.5) calc(var(--nm-10-dist) * 1) var(--nm-10-dark), calc(var(--nm-10-dist) * -0.5) calc(var(--nm-10-dist) * -0.5) calc(var(--nm-10-dist) * 1) var(--nm-10-light);
}

.nm-10__card--l2 {
  box-shadow: var(--nm-10-dist) var(--nm-10-dist) calc(var(--nm-10-dist) * 2) var(--nm-10-dark), calc(var(--nm-10-dist) * -1) calc(var(--nm-10-dist) * -1) calc(var(--nm-10-dist) * 2) var(--nm-10-light);
}

.nm-10__card--l3 {
  box-shadow: calc(var(--nm-10-dist) * 1.8) calc(var(--nm-10-dist) * 1.8) calc(var(--nm-10-dist) * 3.6) var(--nm-10-dark), calc(var(--nm-10-dist) * -1.8) calc(var(--nm-10-dist) * -1.8) calc(var(--nm-10-dist) * 3.6) var(--nm-10-light);
}

.nm-10__card--l4 {
  box-shadow: calc(var(--nm-10-dist) * 2.8) calc(var(--nm-10-dist) * 2.8) calc(var(--nm-10-dist) * 5.6) var(--nm-10-dark), calc(var(--nm-10-dist) * -2.8) calc(var(--nm-10-dist) * -2.8) calc(var(--nm-10-dist) * 5.6) var(--nm-10-light);
}

.nm-10__badge {
  margin: 0;
  font-size: 0.66rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  font-weight: 700;
  color: var(--nm-10-accent);
}

.nm-10__badge--warn {
  color: var(--nm-10-warn);
}

.nm-10__ctitle {
  margin: 0;
  font-family: var(--nm-10-font-display);
  font-size: 1.12rem;
  font-weight: 600;
  letter-spacing: -0.015em;
}

.nm-10__cbody {
  margin: 0;
  font-size: 0.84rem;
  line-height: 1.6;
  color: var(--nm-10-muted);
  text-wrap: pretty;
}

.nm-10__well {
  margin-top: 6px;
  border-radius: 16px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  min-inline-size: 0;
  box-shadow: inset 5px 5px 10px var(--nm-10-dark), inset -5px -5px 10px var(--nm-10-light);
}

.nm-10__wellrow {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  font-size: 0.8rem;
  min-inline-size: 0;
}

.nm-10__wellrow b {
  font-variant-numeric: tabular-nums;
}

.nm-10__bar {
  height: 10px;
  border-radius: 999px;
  background: var(--nm-10-surface);
  box-shadow: inset 2px 2px 5px var(--nm-10-dark), inset -2px -2px 5px var(--nm-10-light);
  overflow: hidden;
}

.nm-10__barfill {
  display: block;
  height: 100%;
  border-radius: 999px;
  background: var(--nm-10-accent);
}

.nm-10__wellnote {
  margin: 0;
  font-size: 0.72rem;
  line-height: 1.5;
  color: var(--nm-10-muted);
  text-wrap: pretty;
}

.nm-10__list {
  list-style: none;
  margin: 6px 0 0;
  padding: 0;
  display: grid;
  gap: 8px;
}

.nm-10__item {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  font-size: 0.83rem;
  padding-bottom: 8px;
  border-bottom: 1px dotted var(--nm-10-border);
  min-inline-size: 0;
}

.nm-10__item b {
  font-variant-numeric: tabular-nums;
}

@media (prefers-color-scheme: dark) {
  .nm-10 {
    --nm-10-surface: #2b2a26;
    --nm-10-dark: rgba(12,12,10,0.7);
    --nm-10-light: rgba(92,90,84,0.44);
    --nm-10-ink: #ecebe5;
    --nm-10-muted: #a5a196;
    --nm-10-border: #858177;
    --nm-10-accent: #8fb3d6;
    --nm-10-warn: #dd9059;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-10 {
      --nm-10-dark: color-mix(in oklab, var(--nm-10-surface), #000 55%);
      --nm-10-light: color-mix(in oklab, var(--nm-10-surface), #fff 14%);
    }
  }
}

.nm-10[data-theme="dark"] {
  --nm-10-surface: #2b2a26;
  --nm-10-dark: rgba(12,12,10,0.7);
  --nm-10-light: rgba(92,90,84,0.44);
  --nm-10-ink: #ecebe5;
  --nm-10-muted: #a5a196;
  --nm-10-border: #858177;
  --nm-10-accent: #8fb3d6;
  --nm-10-warn: #dd9059;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-10[data-theme="dark"] {
    --nm-10-dark: color-mix(in oklab, var(--nm-10-surface), #000 55%);
    --nm-10-light: color-mix(in oklab, var(--nm-10-surface), #fff 14%);
  }
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-10__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-10__themebtn {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 999px;
  background: var(--nm-10-surface);
  color: var(--nm-10-ink);
  border: 1px solid var(--nm-10-line);
  font: 600 11px/1 var(--nm-10-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-10-distance, 6px) var(--nm-10-distance, 6px) var(--nm-10-blur, 14px) var(--nm-10-dark), calc(-1 * var(--nm-10-distance, 6px)) calc(-1 * var(--nm-10-distance, 6px)) var(--nm-10-blur, 14px) var(--nm-10-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-10__themebtn:hover {
  color: var(--nm-10-ink);
}

.nm-10__themeinput:focus-visible + .nm-10__themebtn {
  outline: 2px solid var(--nm-10-ink);
  outline-offset: 3px;
}

.nm-10:has(#nm-10-theme:checked) .nm-10__themebtn {
  box-shadow: inset var(--nm-10-distance, 6px) var(--nm-10-distance, 6px) var(--nm-10-blur, 14px) var(--nm-10-dark), inset calc(-1 * var(--nm-10-distance, 6px)) calc(-1 * var(--nm-10-distance, 6px)) var(--nm-10-blur, 14px) var(--nm-10-light);
}

.nm-10__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-10:has(#nm-10-theme:checked) {
  --nm-10-surface: #2b2a26;
  --nm-10-dark: rgba(12,12,10,0.7);
  --nm-10-light: rgba(92,90,84,0.44);
  --nm-10-ink: #ecebe5;
  --nm-10-muted: #a5a196;
  --nm-10-border: #858177;
  --nm-10-accent: #8fb3d6;
  --nm-10-warn: #dd9059;
}

@media (prefers-color-scheme: light) {
  .nm-10:has(#nm-10-theme:checked) {
    --nm-10-surface: #2b2a26;
    --nm-10-dark: rgba(12,12,10,0.7);
    --nm-10-light: rgba(92,90,84,0.44);
    --nm-10-ink: #ecebe5;
    --nm-10-muted: #a5a196;
    --nm-10-border: #858177;
    --nm-10-accent: #8fb3d6;
    --nm-10-warn: #dd9059;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-10:has(#nm-10-theme:checked) {
    --nm-10-surface: #e8e6e1;
    --nm-10-dark: rgba(177,173,164,0.62);
    --nm-10-light: rgba(255,255,255,0.93);
    --nm-10-ink: #2a2925;
    --nm-10-muted: #5e5b53;
    --nm-10-border: #a19d94;
    --nm-10-accent: #4a6b8a;
    --nm-10-warn: #9c5227;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-10__themebtn {
    transition: none;
  }
}
```
