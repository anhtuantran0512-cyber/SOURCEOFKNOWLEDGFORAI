---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/when-not-to-use-neumorphism/"
title: "When Not to Use Neumorphism"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "The closing argument."
has_js: "false"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: When Not to Use Neumorphism
Source: https://codefronts.com/design-styles/css-neumorphism/when-not-to-use-neumorphism/

The closing argument. Four contexts where soft UI is the right call, four where it is actively harmful, and the hybrid that most production teams should actually ship: a flat, accessible base with soft-UI depth applied to the two or three controls that benefit. Includes the checklist to run before committing, and an honest account of what the style costs.
## HTML
```html
<section class="nm-22" aria-labelledby="nm-22-heading">
      <input type="checkbox" id="nm-22-theme" class="nm-22__themeinput">
      <label for="nm-22-theme" class="nm-22__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-22__stage">
    <header class="nm-22__head">
      <p class="nm-22__kicker">Verdict</p>
      <h2 class="nm-22__heading" id="nm-22-heading">Four yeses and one no</h2>
      <p class="nm-22__sub">Soft UI is a specialist tool. Here is where it earns its cost, where it does not, and what to ship instead.</p>
    </header>

    <div class="nm-22__cols">
      <div class="nm-22__col">
        <h3 class="nm-22__coltitle nm-22__coltitle--yes">Use it</h3>
        <ul class="nm-22__cases">
          <li class="nm-22__case"><b>Media and audio tools</b><span>Transport controls, mixers, faders. The user already knows the object.</span></li>
          <li class="nm-22__case"><b>Smart-home and device UI</b><span>Thermostats, lighting, appliance panels. Physical metaphor, small control count.</span></li>
          <li class="nm-22__case"><b>Calculators and keypads</b><span>Discrete keys with a real-world analogue and no reading load.</span></li>
          <li class="nm-22__case"><b>Marketing and portfolio surfaces</b><span>Low control count, no compliance requirement, character is the point.</span></li>
        </ul>
      </div>
      <div class="nm-22__col">
        <h3 class="nm-22__coltitle nm-22__coltitle--no">Do not</h3>
        <ul class="nm-22__cases">
          <li class="nm-22__case"><b>Data tables and admin tools</b><span>Dense rows, all-day use, and depth that turns to texture at scale.</span></li>
          <li class="nm-22__case"><b>Long-form reading</b><span>Low-contrast chrome around text is fatigue you do not need to add.</span></li>
          <li class="nm-22__case"><b>Regulated or public-sector work</b><span>The contrast cost is structural. It will be a finding.</span></li>
          <li class="nm-22__case"><b>Low-end hardware at scale</b><span>Dozens of blurred shadows on a budget Android is a real frame cost.</span></li>
        </ul>
      </div>
    </div>

    <div class="nm-22__hybrid">
      <div class="nm-22__hybridtext">
        <h3 class="nm-22__htitle">What most teams should ship</h3>
        <p class="nm-22__hbody">A flat, high-contrast base with soft-UI depth on the two or three controls that genuinely benefit. Character kept, findings avoided.</p>
      </div>
      <div class="nm-22__hybriddemo">
        <div class="nm-22__flat">
          <p class="nm-22__flabel">Export format</p>
          <p class="nm-22__fvalue">CSV · comma delimited</p>
        </div>
        <button class="nm-22__depthbtn" type="button">Run export</button>
      </div>
    </div>

    <ol class="nm-22__checklist">
      <li class="nm-22__check"><b>Can every interactive boundary reach 3:1?</b> If not, the style fails an audit before you start.</li>
      <li class="nm-22__check"><b>Is the page background a flat colour you control?</b> Any image or gradient and the illusion has nothing to stand on.</li>
      <li class="nm-22__check"><b>Fewer than about twenty shadowed elements on screen?</b> Beyond that, budget the paint or change technique.</li>
      <li class="nm-22__check"><b>Is there a physical metaphor to lean on?</b> Without one you are paying the cost for decoration alone.</li>
      <li class="nm-22__check"><b>Is there a legal accessibility requirement?</b> If yes, ship the hybrid — not the full style.</li>
    </ol>
  </div>
</section>
```
## CSS
```css
.nm-22 {
  position: relative;
  --nm-22-surface: #eceae6;
  --nm-22-dark: rgba(183,179,171,0.6);
  --nm-22-light: rgba(255,255,255,0.95);
  --nm-22-ink: #262420;
  --nm-22-muted: #55524a;
  --nm-22-border: #9c988f;
  --nm-22-yes: #35664a;
  --nm-22-no: #9c3b2c;
  --nm-22-accent: #3d5f8a;
  --nm-22-font-display: "Reckless", "Iowan Old Style", Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-22-surface);
  color: var(--nm-22-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.01 80)) {
  .nm-22 {
    --nm-22-surface: oklch(0.929 0.006 84);
    --nm-22-ink: oklch(0.26 0.009 74);
    --nm-22-muted: oklch(0.44 0.012 74);
    --nm-22-yes: oklch(0.45 0.09 155);
    --nm-22-no: oklch(0.46 0.14 32);
    --nm-22-accent: oklch(0.5 0.09 250);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-22 {
    --nm-22-dark: color-mix(in oklab, var(--nm-22-surface), #000 18%);
    --nm-22-light: color-mix(in oklab, var(--nm-22-surface), #fff 92%);
    --nm-22-border: color-mix(in oklab, var(--nm-22-surface), var(--nm-22-ink) 34%);
  }
}

.nm-22 *,
.nm-22 *::before,
.nm-22 *::after {
  box-sizing: border-box;
}

.nm-22__stage {
  max-width: 1000px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(26px, 5vw, 56px) clamp(16px, 4vw, 40px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(22px, 3.6vw, 34px);
}

.nm-22__head {
  max-width: 58ch;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.nm-22__kicker {
  margin: 0;
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--nm-22-muted);
}

.nm-22__heading {
  margin: 0;
  font-family: var(--nm-22-font-display);
  font-size: clamp(1.6rem, 4.4vw, 2.4rem);
  font-weight: 400;
  letter-spacing: -0.015em;
  line-height: 1.1;
  text-wrap: balance;
}

.nm-22__sub {
  margin: 0;
  font-size: 0.94rem;
  line-height: 1.62;
  color: var(--nm-22-muted);
  text-wrap: pretty;
}

.nm-22__cols {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(18px, 3vw, 28px);
}

@media (min-width: 700px) {
  .nm-22__cols {
    grid-template-columns: 1fr 1fr;
  }
}

.nm-22__col {
  display: flex;
  flex-direction: column;
  gap: 14px;
  min-inline-size: 0;
}

.nm-22__coltitle {
  margin: 0;
  font-family: var(--nm-22-font-display);
  font-size: 0.74rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  font-weight: 700;
}

.nm-22__coltitle--yes {
  color: var(--nm-22-yes);
}

.nm-22__coltitle--no {
  color: var(--nm-22-no);
}

.nm-22__cases {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 12px;
}

.nm-22__case {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding-bottom: 12px;
  border-bottom: 1px dotted var(--nm-22-border);
  min-inline-size: 0;
}

.nm-22__case b {
  font-size: 0.9rem;
  font-weight: 650;
}

.nm-22__case span {
  font-size: 0.8rem;
  line-height: 1.55;
  color: var(--nm-22-muted);
  text-wrap: pretty;
}

.nm-22__hybrid {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(18px, 3vw, 28px);
  align-items: center;
  border-radius: 22px;
  padding: clamp(20px, 3.4vw, 30px);
  background: var(--nm-22-surface);
  border: 1px solid var(--nm-22-border);
}

@media (min-width: 700px) {
  .nm-22__hybrid {
    grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr);
  }
}

.nm-22__hybridtext {
  display: flex;
  flex-direction: column;
  gap: 8px;
  min-inline-size: 0;
}

.nm-22__htitle {
  margin: 0;
  font-family: var(--nm-22-font-display);
  font-size: 1.2rem;
  font-weight: 400;
}

.nm-22__hbody {
  margin: 0;
  font-size: 0.86rem;
  line-height: 1.62;
  color: var(--nm-22-muted);
  text-wrap: pretty;
}

.nm-22__hybriddemo {
  display: flex;
  flex-direction: column;
  gap: 14px;
  align-items: flex-start;
  min-inline-size: 0;
}

.nm-22__flat {
  width: 100%;
  border-radius: 12px;
  padding: 16px 18px;
  border: 1px solid var(--nm-22-border);
  display: flex;
  flex-direction: column;
  gap: 4px;
  min-inline-size: 0;
}

.nm-22__flabel {
  margin: 0;
  font-size: 0.68rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--nm-22-muted);
  font-weight: 600;
}

.nm-22__fvalue {
  margin: 0;
  font-size: 0.92rem;
  font-weight: 500;
}

.nm-22__depthbtn {
  min-height: 48px;
  padding: 0 22px;
  border-radius: 14px;
  border: 1px solid var(--nm-22-accent);
  background: var(--nm-22-surface);
  color: var(--nm-22-accent);
  font: inherit;
  font-size: 0.9rem;
  font-weight: 650;
  cursor: pointer;
  box-shadow: 8px 8px 17px var(--nm-22-dark), -8px -8px 17px var(--nm-22-light);
  transition: box-shadow 160ms ease;
}

.nm-22__depthbtn:active {
  box-shadow: inset 5px 5px 11px var(--nm-22-dark), inset -5px -5px 11px var(--nm-22-light);
}

.nm-22__depthbtn:focus-visible {
  outline: 2px solid var(--nm-22-accent);
  outline-offset: 3px;
}

.nm-22__checklist {
  margin: 0;
  padding-left: 1.3em;
  display: grid;
  gap: 10px;
}

.nm-22__check {
  font-size: 0.85rem;
  line-height: 1.6;
  color: var(--nm-22-muted);
  text-wrap: pretty;
}

.nm-22__check b {
  color: var(--nm-22-ink);
  font-weight: 650;
}

@media (prefers-reduced-motion: reduce) {
  .nm-22__depthbtn {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .nm-22 {
    --nm-22-surface: #2a2825;
    --nm-22-dark: rgba(11,11,9,0.72);
    --nm-22-light: rgba(90,86,80,0.44);
    --nm-22-ink: #ebe9e4;
    --nm-22-muted: #a09c93;
    --nm-22-border: #878379;
    --nm-22-yes: #84c297;
    --nm-22-no: #e58a75;
    --nm-22-accent: #8cb0dd;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-22 {
      --nm-22-dark: color-mix(in oklab, var(--nm-22-surface), #000 55%);
      --nm-22-light: color-mix(in oklab, var(--nm-22-surface), #fff 14%);
    }
  }
}

.nm-22[data-theme="dark"] {
  --nm-22-surface: #2a2825;
  --nm-22-dark: rgba(11,11,9,0.72);
  --nm-22-light: rgba(90,86,80,0.44);
  --nm-22-ink: #ebe9e4;
  --nm-22-muted: #a09c93;
  --nm-22-border: #878379;
  --nm-22-yes: #84c297;
  --nm-22-no: #e58a75;
  --nm-22-accent: #8cb0dd;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-22[data-theme="dark"] {
    --nm-22-dark: color-mix(in oklab, var(--nm-22-surface), #000 55%);
    --nm-22-light: color-mix(in oklab, var(--nm-22-surface), #fff 14%);
  }
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-22__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-22__themebtn {
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
  background: var(--nm-22-surface);
  color: var(--nm-22-ink);
  border: 1px solid var(--nm-22-line);
  font: 600 11px/1 var(--nm-22-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-22-distance, 6px) var(--nm-22-distance, 6px) var(--nm-22-blur, 14px) var(--nm-22-dark), calc(-1 * var(--nm-22-distance, 6px)) calc(-1 * var(--nm-22-distance, 6px)) var(--nm-22-blur, 14px) var(--nm-22-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-22__themebtn:hover {
  color: var(--nm-22-ink);
}

.nm-22__themeinput:focus-visible + .nm-22__themebtn {
  outline: 2px solid var(--nm-22-ink);
  outline-offset: 3px;
}

.nm-22:has(#nm-22-theme:checked) .nm-22__themebtn {
  box-shadow: inset var(--nm-22-distance, 6px) var(--nm-22-distance, 6px) var(--nm-22-blur, 14px) var(--nm-22-dark), inset calc(-1 * var(--nm-22-distance, 6px)) calc(-1 * var(--nm-22-distance, 6px)) var(--nm-22-blur, 14px) var(--nm-22-light);
}

.nm-22__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-22:has(#nm-22-theme:checked) {
  --nm-22-surface: #2a2825;
  --nm-22-dark: rgba(11,11,9,0.72);
  --nm-22-light: rgba(90,86,80,0.44);
  --nm-22-ink: #ebe9e4;
  --nm-22-muted: #a09c93;
  --nm-22-border: #878379;
  --nm-22-yes: #84c297;
  --nm-22-no: #e58a75;
  --nm-22-accent: #8cb0dd;
}

@media (prefers-color-scheme: light) {
  .nm-22:has(#nm-22-theme:checked) {
    --nm-22-surface: #2a2825;
    --nm-22-dark: rgba(11,11,9,0.72);
    --nm-22-light: rgba(90,86,80,0.44);
    --nm-22-ink: #ebe9e4;
    --nm-22-muted: #a09c93;
    --nm-22-border: #878379;
    --nm-22-yes: #84c297;
    --nm-22-no: #e58a75;
    --nm-22-accent: #8cb0dd;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-22:has(#nm-22-theme:checked) {
    --nm-22-surface: #eceae6;
    --nm-22-dark: rgba(183,179,171,0.6);
    --nm-22-light: rgba(255,255,255,0.95);
    --nm-22-ink: #262420;
    --nm-22-muted: #55524a;
    --nm-22-border: #9c988f;
    --nm-22-yes: #35664a;
    --nm-22-no: #9c3b2c;
    --nm-22-accent: #3d5f8a;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-22__themebtn {
    transition: none;
  }
}
```
