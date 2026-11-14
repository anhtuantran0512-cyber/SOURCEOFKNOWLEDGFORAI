---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neumorphism/breathe/"
title: "Circular Progress Ring in Soft UI"
section: "design-styles"
category: "css-neumorphism"
category_name: "CSS Neumorphism"
description: "Circular gauges as rings carved into the surface with a coloured arc filling the groove."
has_js: "false"
---

Here's a working CSS Neumorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Circular Progress Ring in Soft UI
Source: https://codefronts.com/design-styles/css-neumorphism/breathe/

Circular gauges as rings carved into the surface with a coloured arc filling the groove. Built on conic-gradient with a radial mask for the hole, an inset shadow for the channel, and a registered custom property so the arc can animate smoothly. Three sizes, an activity-ring stack, and the mask-versus-inner-circle trade-off spelled out.
## HTML
```html
<section class="nm-14" aria-labelledby="nm-14-heading">
      <input type="checkbox" id="nm-14-theme" class="nm-14__themeinput">
      <label for="nm-14-theme" class="nm-14__themebtn">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9Z"/></svg>
        Theme
      </label>
  <div class="nm-14__stage">
    <header class="nm-14__head">
      <p class="nm-14__kicker">Component · gauge</p>
      <h2 class="nm-14__heading" id="nm-14-heading">Arcs filling a carved channel</h2>
      <p class="nm-14__sub">One conic gradient, one radial mask, and an inset groove underneath doing the soft-UI work.</p>
    </header>

    <div class="nm-14__rings">
      <figure class="nm-14__gauge" style="--nm-14-angle:268deg">
        <div class="nm-14__ring">
          <div class="nm-14__hub"><b>74%</b><em>uptime</em></div>
        </div>
        <figcaption class="nm-14__cap">Service availability, 30 days</figcaption>
      </figure>
      <figure class="nm-14__gauge nm-14__gauge--alt" style="--nm-14-angle:158deg">
        <div class="nm-14__ring">
          <div class="nm-14__hub"><b>44%</b><em>storage</em></div>
        </div>
        <figcaption class="nm-14__cap">56 GB of 128 GB in use</figcaption>
      </figure>
      <figure class="nm-14__gauge nm-14__gauge--warn" style="--nm-14-angle:331deg">
        <div class="nm-14__ring">
          <div class="nm-14__hub"><b>92%</b><em>budget</em></div>
        </div>
        <figcaption class="nm-14__cap">£4,600 of £5,000 committed</figcaption>
      </figure>
    </div>

    <div class="nm-14__stack">
      <div class="nm-14__stackrings">
        <div class="nm-14__ring nm-14__ring--s1" style="--nm-14-angle:300deg"></div>
        <div class="nm-14__ring nm-14__ring--s2" style="--nm-14-angle:214deg"></div>
        <div class="nm-14__ring nm-14__ring--s3" style="--nm-14-angle:126deg"></div>
      </div>
      <dl class="nm-14__legend">
        <div class="nm-14__lrow"><dt><span class="nm-14__swatch nm-14__swatch--1"></span>Deep work</dt><dd>5h 00m</dd></div>
        <div class="nm-14__lrow"><dt><span class="nm-14__swatch nm-14__swatch--2"></span>Meetings</dt><dd>3h 34m</dd></div>
        <div class="nm-14__lrow"><dt><span class="nm-14__swatch nm-14__swatch--3"></span>Admin</dt><dd>2h 06m</dd></div>
      </dl>
    </div>
  </div>
</section>
```
## CSS
```css
@property --nm-14-angle {
  syntax: '<angle>';
  inherits: true;
  initial-value: 0deg;
}

.nm-14 {
  position: relative;
  --nm-14-surface: #e6e8e5;
  --nm-14-dark: rgba(170,176,167,0.64);
  --nm-14-light: rgba(255,255,255,0.94);
  --nm-14-ink: #262a24;
  --nm-14-muted: #575c53;
  --nm-14-border: #979c92;
  --nm-14-fill: #3b6f52;
  --nm-14-fill2: #40668c;
  --nm-14-fill3: #9a5f2c;
  --nm-14-size: clamp(140px, 26vw, 176px);
  --nm-14-track: 22px;
  --nm-14-angle: 0deg;
  --nm-14-font-display: "Karla", "Helvetica Neue", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--nm-14-surface);
  color: var(--nm-14-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
}

@supports (color: oklch(0.9 0.01 140)) {
  .nm-14 {
    --nm-14-surface: oklch(0.918 0.008 140);
    --nm-14-ink: oklch(0.27 0.015 140);
    --nm-14-muted: oklch(0.45 0.016 140);
    --nm-14-fill: oklch(0.5 0.09 158);
    --nm-14-fill2: oklch(0.5 0.08 245);
    --nm-14-fill3: oklch(0.52 0.11 62);
  }
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-14 {
    --nm-14-dark: color-mix(in oklab, var(--nm-14-surface), #000 20%);
    --nm-14-light: color-mix(in oklab, var(--nm-14-surface), #fff 92%);
    --nm-14-border: color-mix(in oklab, var(--nm-14-surface), var(--nm-14-ink) 32%);
  }
}

.nm-14 *,
.nm-14 *::before,
.nm-14 *::after {
  box-sizing: border-box;
}

.nm-14__stage {
  max-width: 980px;
  margin: 0 auto;
  min-height: 100vh;
  padding: clamp(26px, 5vw, 56px) clamp(16px, 4vw, 40px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: clamp(24px, 4vw, 40px);
}

.nm-14__head {
  max-width: 56ch;
  display: flex;
  flex-direction: column;
  gap: 9px;
}

.nm-14__kicker {
  margin: 0;
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--nm-14-muted);
}

.nm-14__heading {
  margin: 0;
  font-family: var(--nm-14-font-display);
  font-size: clamp(1.5rem, 4.2vw, 2.25rem);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.12;
  text-wrap: balance;
}

.nm-14__sub {
  margin: 0;
  font-size: 0.94rem;
  line-height: 1.6;
  color: var(--nm-14-muted);
  text-wrap: pretty;
}

.nm-14__rings {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(20px, 4vw, 40px);
  justify-content: flex-start;
}

.nm-14__gauge {
  margin: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
  min-inline-size: 0;
}

.nm-14__gauge--alt {
  --nm-14-fill: var(--nm-14-fill2);
}

.nm-14__gauge--warn {
  --nm-14-fill: var(--nm-14-fill3);
}

.nm-14__ring {
  position: relative;
  width: var(--nm-14-size);
  height: var(--nm-14-size);
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: conic-gradient(var(--nm-14-fill) 0 var(--nm-14-angle), rgba(0,0,0,0) var(--nm-14-angle)), var(--nm-14-surface);
  box-shadow: inset 5px 5px 11px var(--nm-14-dark), inset -5px -5px 11px var(--nm-14-light);
}

.nm-14__ring::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 50%;
  box-shadow: inset 3px 3px 7px var(--nm-14-dark), inset -3px -3px 7px var(--nm-14-light);
  -webkit-mask: radial-gradient(farthest-side, #000 calc(100% - var(--nm-14-track) - 1px), rgba(0,0,0,0) calc(100% - var(--nm-14-track)));
  mask: radial-gradient(farthest-side, #000 calc(100% - var(--nm-14-track) - 1px), rgba(0,0,0,0) calc(100% - var(--nm-14-track)));
  pointer-events: none;
}

@supports ((-webkit-mask: radial-gradient(#000, #000)) or (mask: radial-gradient(#000, #000))) {
  .nm-14__ring {
    -webkit-mask: radial-gradient(farthest-side, rgba(0,0,0,0) calc(100% - var(--nm-14-track) - 1px), #000 calc(100% - var(--nm-14-track)));
    mask: radial-gradient(farthest-side, rgba(0,0,0,0) calc(100% - var(--nm-14-track) - 1px), #000 calc(100% - var(--nm-14-track)));
  }

  .nm-14__ring::after {
    display: none;
  }
}

.nm-14__hub {
  position: absolute;
  inset: calc(var(--nm-14-track) + 8px);
  border-radius: 50%;
  display: grid;
  place-content: center;
  gap: 2px;
  text-align: center;
  background: var(--nm-14-surface);
  border: 1px solid var(--nm-14-border);
  box-shadow: 5px 5px 12px var(--nm-14-dark), -5px -5px 12px var(--nm-14-light);
  -webkit-mask: none;
  mask: none;
}

.nm-14__hub b {
  font-family: var(--nm-14-font-display);
  font-size: 1.35rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.nm-14__hub em {
  font-style: normal;
  font-size: 0.66rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--nm-14-muted);
}

.nm-14__cap {
  font-size: 0.78rem;
  line-height: 1.5;
  color: var(--nm-14-muted);
  text-align: center;
  max-width: 20ch;
  text-wrap: pretty;
}

.nm-14__stack {
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(18px, 3vw, 30px);
  align-items: center;
}

@media (min-width: 620px) {
  .nm-14__stack {
    grid-template-columns: auto minmax(0, 1fr);
  }
}

.nm-14__stackrings {
  position: relative;
  width: 172px;
  height: 172px;
}

.nm-14__stackrings .nm-14__ring {
  position: absolute;
  box-shadow: inset 4px 4px 9px var(--nm-14-dark), inset -4px -4px 9px var(--nm-14-light);
}

.nm-14__ring--s1 {
  --nm-14-track: 16px;
  --nm-14-fill: #3b6f52;
  inset: 0;
  width: auto;
  height: auto;
}

.nm-14__ring--s2 {
  --nm-14-track: 14px;
  --nm-14-fill: #40668c;
  inset: 22px;
  width: auto;
  height: auto;
}

.nm-14__ring--s3 {
  --nm-14-track: 12px;
  --nm-14-fill: #9a5f2c;
  inset: 44px;
  width: auto;
  height: auto;
}

@supports (color: oklch(0.5 0.09 158)) {
  .nm-14__ring--s1 {
    --nm-14-fill: oklch(0.5 0.09 158);
  }

  .nm-14__ring--s2 {
    --nm-14-fill: oklch(0.5 0.08 245);
  }

  .nm-14__ring--s3 {
    --nm-14-fill: oklch(0.52 0.11 62);
  }
}

.nm-14__legend {
  margin: 0;
  display: grid;
  gap: 10px;
  min-inline-size: 0;
}

.nm-14__lrow {
  display: flex;
  justify-content: space-between;
  gap: 14px;
  align-items: center;
  padding-bottom: 9px;
  border-bottom: 1px dotted var(--nm-14-border);
  min-inline-size: 0;
}

.nm-14__lrow dt {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.85rem;
  font-weight: 500;
  min-inline-size: 0;
}

.nm-14__lrow dd {
  margin: 0;
  font-size: 0.85rem;
  font-variant-numeric: tabular-nums;
  color: var(--nm-14-muted);
}

.nm-14__swatch {
  width: 12px;
  height: 12px;
  border-radius: 3px;
  flex: none;
}

.nm-14__swatch--1 {
  background: var(--nm-14-fill);
}

.nm-14__swatch--2 {
  background: var(--nm-14-fill2);
}

.nm-14__swatch--3 {
  background: var(--nm-14-fill3);
}

@media (prefers-color-scheme: dark) {
  .nm-14 {
    --nm-14-surface: #272a26;
    --nm-14-dark: rgba(11,12,10,0.72);
    --nm-14-light: rgba(88,93,85,0.44);
    --nm-14-ink: #e8eae5;
    --nm-14-muted: #9ba095;
    --nm-14-border: #858a80;
    --nm-14-fill: #77c295;
    --nm-14-fill2: #85b0dd;
    --nm-14-fill3: #dda069;
  }

  @supports (color: color-mix(in oklab, #fff, #000)) {
    .nm-14 {
      --nm-14-dark: color-mix(in oklab, var(--nm-14-surface), #000 55%);
      --nm-14-light: color-mix(in oklab, var(--nm-14-surface), #fff 14%);
    }
  }

  .nm-14__ring--s1 {
    --nm-14-fill: #77c295;
  }

  .nm-14__ring--s2 {
    --nm-14-fill: #85b0dd;
  }

  .nm-14__ring--s3 {
    --nm-14-fill: #dda069;
  }
}

.nm-14[data-theme="dark"] {
  --nm-14-surface: #272a26;
  --nm-14-dark: rgba(11,12,10,0.72);
  --nm-14-light: rgba(88,93,85,0.44);
  --nm-14-ink: #e8eae5;
  --nm-14-muted: #9ba095;
  --nm-14-border: #858a80;
  --nm-14-fill: #77c295;
  --nm-14-fill2: #85b0dd;
  --nm-14-fill3: #dda069;
}

@supports (color: color-mix(in oklab, #fff, #000)) {
  .nm-14[data-theme="dark"] {
    --nm-14-dark: color-mix(in oklab, var(--nm-14-surface), #000 55%);
    --nm-14-light: color-mix(in oklab, var(--nm-14-surface), #fff 14%);
  }
}

.nm-14[data-theme="dark"] .nm-14__ring--s1 {
  --nm-14-fill: #77c295;
}

.nm-14[data-theme="dark"] .nm-14__ring--s2 {
  --nm-14-fill: #85b0dd;
}

.nm-14[data-theme="dark"] .nm-14__ring--s3 {
  --nm-14-fill: #dda069;
}
/* Pure-CSS theme toggle. Mirrors the [data-theme="dark"] rules above so
   the demo's own dark palette is reachable from inside the demo. */

.nm-14__themeinput {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: 0;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.nm-14__themebtn {
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
  background: var(--nm-14-surface);
  color: var(--nm-14-ink);
  border: 1px solid var(--nm-14-line);
  font: 600 11px/1 var(--nm-14-font-display, system-ui);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
  box-shadow: var(--nm-14-distance, 6px) var(--nm-14-distance, 6px) var(--nm-14-blur, 14px) var(--nm-14-dark), calc(-1 * var(--nm-14-distance, 6px)) calc(-1 * var(--nm-14-distance, 6px)) var(--nm-14-blur, 14px) var(--nm-14-light);
  transition: box-shadow 180ms ease, color 180ms ease;
}

.nm-14__themebtn:hover {
  color: var(--nm-14-ink);
}

.nm-14__themeinput:focus-visible + .nm-14__themebtn {
  outline: 2px solid var(--nm-14-ink);
  outline-offset: 3px;
}

.nm-14:has(#nm-14-theme:checked) .nm-14__themebtn {
  box-shadow: inset var(--nm-14-distance, 6px) var(--nm-14-distance, 6px) var(--nm-14-blur, 14px) var(--nm-14-dark), inset calc(-1 * var(--nm-14-distance, 6px)) calc(-1 * var(--nm-14-distance, 6px)) var(--nm-14-blur, 14px) var(--nm-14-light);
}

.nm-14__themebtn svg {
  inline-size: 13px;
  block-size: 13px;
  flex: none;
}

.nm-14:has(#nm-14-theme:checked) {
  --nm-14-surface: #272a26;
  --nm-14-dark: rgba(11,12,10,0.72);
  --nm-14-light: rgba(88,93,85,0.44);
  --nm-14-ink: #e8eae5;
  --nm-14-muted: #9ba095;
  --nm-14-border: #858a80;
  --nm-14-fill: #77c295;
  --nm-14-fill2: #85b0dd;
  --nm-14-fill3: #dda069;
}

@media (prefers-color-scheme: light) {
  .nm-14:has(#nm-14-theme:checked) {
    --nm-14-surface: #272a26;
    --nm-14-dark: rgba(11,12,10,0.72);
    --nm-14-light: rgba(88,93,85,0.44);
    --nm-14-ink: #e8eae5;
    --nm-14-muted: #9ba095;
    --nm-14-border: #858a80;
    --nm-14-fill: #77c295;
    --nm-14-fill2: #85b0dd;
    --nm-14-fill3: #dda069;
  }
}

@media (prefers-color-scheme: dark) {
  /* Base already resolves dark here, so :checked restores light —
       without this the toggle is inert for dark-OS visitors. */

  .nm-14:has(#nm-14-theme:checked) {
    --nm-14-surface: #e6e8e5;
    --nm-14-dark: rgba(170,176,167,0.64);
    --nm-14-light: rgba(255,255,255,0.94);
    --nm-14-ink: #262a24;
    --nm-14-muted: #575c53;
    --nm-14-border: #979c92;
    --nm-14-fill: #3b6f52;
    --nm-14-fill2: #40668c;
    --nm-14-fill3: #9a5f2c;
  }
}

@media (prefers-reduced-motion: reduce) {
  .nm-14__themebtn {
    transition: none;
  }
}
```
