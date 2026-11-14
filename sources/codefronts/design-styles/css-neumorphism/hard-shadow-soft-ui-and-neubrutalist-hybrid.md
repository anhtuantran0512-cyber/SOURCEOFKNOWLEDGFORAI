---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/hard-shadow-soft-ui-and-neubrutalist-hybrid/"
title: "Hard Shadow Soft UI and Neubrutalist Hybrid"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "Take the mirrored shadow pair and set blur to zero."
has_js: "false"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hard Shadow Soft UI and Neubrutalist Hybrid
Source: https://codefronts.com/design-styles/css-neumorphism/hard-shadow-soft-ui-and-neubrutalist-hybrid/

Take the mirrored shadow pair and set blur to zero. What comes out is a legible, high-contrast cousin of soft UI that keeps the extrusion logic but reads clearly on cheap screens and in sunlight — a practical middle ground between neumorphism and neubrutalism. Three depths, an interactive press that slides the object into its own shadow, and a direct comparison against the blurred original.
## HTML
```html
<section class="nm-09" aria-labelledby="nm-09-heading">
      <input type="checkbox" id="nm-09-theme" class="nm-09__themeinput">
      <label for="nm-09-theme" class="nm-09__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-09__stage">
    <header class="nm-09__head">
      <p class="nm-09__kicker">Variant · hard edge</p>
      <h2 class="nm-09__heading" id="nm-09-heading">Same shadow pair, zero blur</h2>
      <p class="nm-09__sub">The extrusion logic survives. The contrast problem does not.</p>
    </header>

    <div class="nm-09__levels">
      <div class="nm-09__level nm-09__level--1"><span>Depth 1</span><em>2px offset</em></div>
      <div class="nm-09__level nm-09__level--2"><span>Depth 2</span><em>5px offset</em></div>
      <div class="nm-09__level nm-09__level--3"><span>Depth 3</span><em>9px offset</em></div>
    </div>

    <div class="nm-09__split">
      <div class="nm-09__col">
        <p class="nm-09__collabel">Hard — press to drop</p>
        <button class="nm-09__hardbtn" type="button">Archive project</button>
        <p class="nm-09__meta">Boundary contrast 4.4:1 · legible in sunlight · survives greyscale</p>
      </div>
      <div class="nm-09__col">
        <p class="nm-09__collabel">Blurred — same offsets</p>
        <button class="nm-09__softbtn" type="button">Archive project</button>
        <p class="nm-09__meta">Boundary contrast 1.0:1 · needs an added border to be compliant</p>
      </div>
    </div>

    <div class="nm-09__cardrow">
      <article class="nm-09__card">
        <p class="nm-09__ctitle">Ledger</p>
        <p class="nm-09__cvalue">£4,820</p>
        <p class="nm-09__cmeta">outstanding across 6 invoices</p>
      </article>
      <article class="nm-09__card nm-09__card--accent">
        <p class="nm-09__ctitle">Cleared</p>
        <p class="nm-09__cvalue">£31,400</p>
        <p class="nm-09__cmeta">this quarter, net of fees</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.nm-09 {
  position: relative;
  --nm-09-surface: #ece9e1;
  --nm-09-ink: #1d1c19;
  --nm-09-muted: #56534c;
  --nm-09-shadow: #1d1c19;
  --nm-09-accent: #c25b2e;
  --nm-09-soft-dark: rgba(176,170,155,0.7);
  --nm-09-soft-light: rgba(255,255,255,0.95);
  --nm-09-depth: 5px;
  --nm-09-radius: 6px;
  --nm-09-font-display: "Archivo", "Helvetica Neue", Impact, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-09-surface);
  color: var(--nm-09-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.01 90)) {
  .nm-09 {
    --nm-09-surface: oklch(0.925 0.013 90);
    --nm-09-ink: oklch(0.22 0.008 80);
    --nm-09-muted: oklch(0.44 0.012 80);
    --nm-09-shadow: oklch(0.22 0.008 80);
    --nm-09-accent: oklch(0.58 0.15 45);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-09 {
    --nm-09-soft-dark: color-mix(in oklab, var(--nm-09-surface), #000 22%);
    --nm-09-soft-light: color-mix(in oklab, var(--nm-09-surface), #fff 90%);
  }
}

.nm-09 *,
.nm-09 *::before,
.nm-09 *::after {
  box-sizing: border-box;
}

.nm-09__stage {
  max-width: 940px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(26px, 5vw, 58px) clamp(16px, 4vw, 42px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(24px, 4vw, 40px);
}

.nm-09__head {
  max-width: 54ch;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.nm-09__kicker {
  margin: 0;
  font-family: var(--nm-09-font-display);
  font-size: 0.7rem;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--nm-09-accent);
  font-weight: 700;
}

.nm-09__heading {
  margin: 0;
  font-family: var(--nm-09-font-display);
  font-size: clamp(1.7rem, 5vw, 2.7rem);
  font-weight: 800;
  letter-spacing: -0.03em;
  line-height: 1.03;
  text-transform: uppercase;
  text-wrap: balance;
}

.nm-09__sub {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--nm-09-muted);
  text-wrap: pretty;
}

.nm-09__levels {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 160px), 1fr));
  gap: clamp(16px, 3vw, 26px);
}

.nm-09__level {
  border: 2px solid var(--nm-09-ink);
  border-radius: var(--nm-09-radius);
  background: var(--nm-09-surface);
  padding: 18px 16px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  min-inline-size: 0;
}

.nm-09__level span {
  font-family: var(--nm-09-font-display);
  font-size: 0.95rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.nm-09__level em {
  font-style: normal;
  font-size: 0.74rem;
  color: var(--nm-09-muted);
}

.nm-09__level--1 {
  box-shadow: 2px 2px 0 var(--nm-09-shadow);
}

.nm-09__level--2 {
  box-shadow: 5px 5px 0 var(--nm-09-shadow);
}

.nm-09__level--3 {
  box-shadow: 9px 9px 0 var(--nm-09-shadow);
}

.nm-09__split {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(18px, 3vw, 28px);
}

@media (min-width: 680px) {
  .nm-09__split {
    grid-template-columns: 1fr 1fr;
  }
}

.nm-09__col {
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: flex-start;
  min-inline-size: 0;
}

.nm-09__collabel {
  margin: 0;
  font-family: var(--nm-09-font-display);
  font-size: 0.72rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  font-weight: 700;
  color: var(--nm-09-muted);
}

.nm-09__hardbtn {
  min-height: 48px;
  padding: 0 22px;
  border: 2px solid var(--nm-09-ink);
  border-radius: var(--nm-09-radius);
  background: var(--nm-09-surface);
  color: var(--nm-09-ink);
  font: inherit;
  font-family: var(--nm-09-font-display);
  font-size: 0.92rem;
  font-weight: 700;
  letter-spacing: 0.02em;
  cursor: pointer;
  box-shadow: var(--nm-09-depth) var(--nm-09-depth) 0 var(--nm-09-shadow);
  transition: transform 110ms ease, box-shadow 110ms ease;
}

.nm-09__hardbtn:hover {
  background: var(--nm-09-accent);
  color: #fff;
}

.nm-09__hardbtn:active {
  transform: translate(var(--nm-09-depth), var(--nm-09-depth));
  box-shadow: 0 0 0 var(--nm-09-shadow);
}

.nm-09__hardbtn:focus-visible {
  outline: 3px solid var(--nm-09-accent);
  outline-offset: 3px;
}

.nm-09__softbtn {
  min-height: 48px;
  padding: 0 22px;
  border: 0;
  border-radius: 14px;
  background: var(--nm-09-surface);
  color: var(--nm-09-muted);
  font: inherit;
  font-family: var(--nm-09-font-display);
  font-size: 0.92rem;
  font-weight: 700;
  cursor: pointer;
  box-shadow: var(--nm-09-depth) var(--nm-09-depth) calc(var(--nm-09-depth) * 2.2) var(--nm-09-soft-dark), calc(var(--nm-09-depth) * -1) calc(var(--nm-09-depth) * -1) calc(var(--nm-09-depth) * 2.2) var(--nm-09-soft-light);
}

.nm-09__softbtn:active {
  box-shadow: inset 4px 4px 9px var(--nm-09-soft-dark), inset -4px -4px 9px var(--nm-09-soft-light);
}

.nm-09__softbtn:focus-visible {
  outline: 3px solid var(--nm-09-accent);
  outline-offset: 3px;
}

.nm-09__meta {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.5;
  color: var(--nm-09-muted);
  text-wrap: pretty;
}

.nm-09__cardrow {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(16px, 3vw, 24px);
}

@media (min-width: 620px) {
  .nm-09__cardrow {
    grid-template-columns: 1fr 1fr;
  }
}

.nm-09__card {
  border: 2px solid var(--nm-09-ink);
  border-radius: var(--nm-09-radius);
  background: var(--nm-09-surface);
  padding: clamp(18px, 3vw, 24px);
  box-shadow: 7px 7px 0 var(--nm-09-shadow);
  min-inline-size: 0;
}

.nm-09__card--accent {
  background: var(--nm-09-accent);
  color: #fff;
  border-color: var(--nm-09-ink);
}

.nm-09__ctitle {
  margin: 0 0 6px;
  font-family: var(--nm-09-font-display);
  font-size: 0.72rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  font-weight: 700;
}

.nm-09__cvalue {
  margin: 0 0 4px;
  font-family: var(--nm-09-font-display);
  font-size: clamp(1.8rem, 5.5vw, 2.5rem);
  font-weight: 800;
  letter-spacing: -0.03em;
  font-variant-numeric: tabular-nums;
}

.nm-09__cmeta {
  margin: 0;
  font-size: 0.78rem;
  color: var(--nm-09-muted);
}

.nm-09__card--accent .nm-09__cmeta {
  color: rgba(255,255,255,0.86);
}

@media (prefers-reduced-motion: reduce) {
  .nm-09__hardbtn {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .nm-09 {
    --nm-09-surface: #2a2823;
    --nm-09-ink: #f0ece2;
    --nm-09-muted: #ada799;
    --nm-09-shadow: #0e0d0b;
    --nm-09-accent: #e58453;
    --nm-09-soft-dark: rgba(12,11,9,0.7);
    --nm-09-soft-light: rgba(92,87,78,0.44);
  }

  .nm-09__hardbtn:hover,
    .nm-09__card--accent {
    color: #1c1a16;
  }
}

.nm-09[data-theme="dark"] {
  --nm-09-surface: #2a2823;
  --nm-09-ink: #f0ece2;
  --nm-09-muted: #ada799;
  --nm-09-shadow: #0e0d0b;
  --nm-09-accent: #e58453;
  --nm-09-soft-dark: rgba(12,11,9,0.7);
  --nm-09-soft-light: rgba(92,87,78,0.44);
}

.nm-09[data-theme="dark"] .nm-09__hardbtn:hover,
.nm-09[data-theme="dark"] .nm-09__card--accent {
  color: #1c1a16;
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-09__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-09__themebtn {
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
  background: var(--nm-09-surface);
  color: var(--nm-09-ink);
  border: 1px solid var(--nm-09-line);
  font: 600 11px/1 var(--nm-09-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-09-distance, 6px) var(--nm-09-distance, 6px) var(--nm-09-blur, 14px) var(--nm-09-dark), calc(-1 * var(--nm-09-distance, 6px)) calc(-1 * var(--nm-09-distance, 6px)) var(--nm-09-blur, 14px) var(--nm-09-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-09__themebtn:hover {
  color: var(--nm-09-ink);
}

.nm-09__themeinput:focus-visible + .nm-09__themebtn {
  outline: 2px solid var(--nm-09-ink);
  outline-offset: 3px;
}

.nm-09:has(#nm-09-theme:checked) .nm-09__themebtn {
  box-shadow: inset var(--nm-09-distance, 6px) var(--nm-09-distance, 6px) var(--nm-09-blur, 14px) var(--nm-09-dark), inset calc(-1 * var(--nm-09-distance, 6px)) calc(-1 * var(--nm-09-distance, 6px)) var(--nm-09-blur, 14px) var(--nm-09-light);
}

.nm-09__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-09:has(#nm-09-theme:checked) {
  --nm-09-surface: #2a2823;
  --nm-09-ink: #f0ece2;
  --nm-09-muted: #ada799;
  --nm-09-shadow: #0e0d0b;
  --nm-09-accent: #e58453;
  --nm-09-soft-dark: rgba(12,11,9,0.7);
  --nm-09-soft-light: rgba(92,87,78,0.44);
}

@media (prefers-color-scheme: light) {
  .nm-09:has(#nm-09-theme:checked) {
    --nm-09-surface: #2a2823;
    --nm-09-ink: #f0ece2;
    --nm-09-muted: #ada799;
    --nm-09-shadow: #0e0d0b;
    --nm-09-accent: #e58453;
    --nm-09-soft-dark: rgba(12,11,9,0.7);
    --nm-09-soft-light: rgba(92,87,78,0.44);
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-09:has(#nm-09-theme:checked) {
    --nm-09-surface: #ece9e1;
    --nm-09-ink: #1d1c19;
    --nm-09-muted: #56534c;
    --nm-09-shadow: #1d1c19;
    --nm-09-accent: #c25b2e;
    --nm-09-soft-dark: rgba(176,170,155,0.7);
    --nm-09-soft-light: rgba(255,255,255,0.95);
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-09__themebtn {
    transition: none;
  }
}
```
