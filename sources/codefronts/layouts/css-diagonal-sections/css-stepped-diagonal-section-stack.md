---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-stepped-diagonal-section-stack/"
title: "CSS Stepped Diagonal Section Stack"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "Four stacked bands in different colours whose cuts alternate direction, producing a staircase down the page."
has_js: "false"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Stepped Diagonal Section Stack
Source: https://codefronts.com/layouts/css-diagonal-sections/css-stepped-diagonal-section-stack/

Four stacked bands in different colours whose cuts alternate direction, producing a staircase down the page. One --cut token, one polygon, and :nth-child(even) flipping the slope — which is the whole trick: alternating the sign is what keeps a multi-band stack rhythmic instead of looking like a page that slid sideways.
## HTML
```html
<div class="dgs-12">
  <input class="dgs-12__sronly" type="checkbox" id="dgs-12-dark">
  <label class="dgs-12__theme" for="dgs-12-dark">
    <svg class="dgs-12__i dgs-12__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-12__i dgs-12__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-12__srtext">Toggle dark theme</span>
  </label>
  <fieldset class="dgs-12__ctl">
    <legend class="dgs-12__vh">Stair controls</legend>
    <input class="dgs-12__sr" type="radio" name="dgs-12-d" id="dgs-12-d1"><label for="dgs-12-d1">Shallow</label>
    <input class="dgs-12__sr" type="radio" name="dgs-12-d" id="dgs-12-d2" checked><label for="dgs-12-d2">Even</label>
    <input class="dgs-12__sr" type="radio" name="dgs-12-d" id="dgs-12-d3"><label for="dgs-12-d3">Steep</label>
    <input class="dgs-12__sr" type="checkbox" id="dgs-12-zig"><label for="dgs-12-zig">Zigzag</label>
  </fieldset>

  <div class="dgs-12__stage">
    <section class="dgs-12__top" aria-labelledby="dgs-12-a">
      <div class="dgs-12__wrap">
        <p class="dgs-12__eyebrow">Tidewater &mdash; payroll onboarding</p>
        <h2 class="dgs-12__display" id="dgs-12-a">Four steps from signed contract to first payslip</h2>
        <p class="dgs-12__lede">Each step is its own band, and each band steps down a little further than the one above it.</p>
      </div>
    </section>

    <section class="dgs-12__step dgs-12__step--1" aria-labelledby="dgs-12-s1">
      <div class="dgs-12__wrap dgs-12__row">
        <p class="dgs-12__no">01</p>
        <div>
          <h2 class="dgs-12__h2" id="dgs-12-s1">Connect your entity</h2>
          <p class="dgs-12__body">Company number, bank mandate and pay calendar. Two minutes, and we verify with Companies House in the background.</p>
        </div>
        <p class="dgs-12__eta">~2 min</p>
      </div>
    </section>

    <section class="dgs-12__step dgs-12__step--2" aria-labelledby="dgs-12-s2">
      <div class="dgs-12__wrap dgs-12__row">
        <p class="dgs-12__no">02</p>
        <div>
          <h2 class="dgs-12__h2" id="dgs-12-s2">Import the team</h2>
          <p class="dgs-12__body">A CSV or a direct pull from your HR system. Duplicate national insurance numbers are flagged before anything is saved.</p>
        </div>
        <p class="dgs-12__eta">~6 min</p>
      </div>
    </section>

    <section class="dgs-12__step dgs-12__step--3" aria-labelledby="dgs-12-s3">
      <div class="dgs-12__wrap dgs-12__row">
        <p class="dgs-12__no">03</p>
        <div>
          <h2 class="dgs-12__h2" id="dgs-12-s3">Approve the first run</h2>
          <p class="dgs-12__body">A dry run with real numbers and no money moved. Sign off, and the same figures are what leave the account.</p>
        </div>
        <p class="dgs-12__eta">~4 min</p>
      </div>
    </section>

    <section class="dgs-12__step dgs-12__step--4" aria-labelledby="dgs-12-s4">
      <div class="dgs-12__wrap dgs-12__row">
        <p class="dgs-12__no">04</p>
        <div>
          <h2 class="dgs-12__h2" id="dgs-12-s4">Payslips out</h2>
          <p class="dgs-12__body">Filed with HMRC, pension provider notified, and payslips in inboxes at 09:00 on your pay date.</p>
        </div>
        <p class="dgs-12__eta">Automatic</p>
      </div>
    </section>

    <section class="dgs-12__after" aria-labelledby="dgs-12-c">
      <div class="dgs-12__wrap dgs-12__cols">
        <h2 class="dgs-12__h3" id="dgs-12-c">How the staircase is built</h2>
        <p class="dgs-12__note">Every band shares one clip and one pull-up, and <code class="dgs-12__code">:nth-child()</code> hands each one a slightly deeper cut. Because the depth is a single custom property per band, the whole staircase re-flows from four lines of CSS.</p>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700&display=swap');

.dgs-12 {
  --unit: clamp(.9rem, 2.6vw, 2.6rem);
  --page: #f7fafa;
  --page2: #eef4f4;
  --ink: #08201f;
  --muted: #4e6a68;
  --line: #d8e6e5;
  --t1: #d4efec;
  --t2: #9fdcd6;
  --t3: #4fb8b0;
  --t4: #16716c;
  --on4: #eafaf8;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--page);
  color: var(--ink);
  font-family: 'Figtree', system-ui, -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

.dgs-12 *,
.dgs-12 *::before,
.dgs-12 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.6 0.1 185)) {
  .dgs-12 {
    --page: oklch(0.985 0.005 190);
    --page2: oklch(0.962 0.01 190);
    --ink: oklch(0.21 0.03 190);
    --muted: oklch(0.475 0.03 190);
    --line: oklch(0.9 0.015 190);
    --t1: oklch(0.925 0.04 185);
    --t2: oklch(0.855 0.075 185);
    --t3: oklch(0.7 0.1 187);
    --t4: oklch(0.46 0.085 187);
    --on4: oklch(0.965 0.015 185);
  }
}

.dgs-12__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-12__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.dgs-12__ctl {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 40;
  margin: 0;
  padding: .28rem;
  display: flex;
  gap: .2rem;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: rgba(247,250,250,.92);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
}

.dgs-12__ctl label {
  min-inline-size: 3rem;
  min-block-size: 2.5rem;
  display: grid;
  place-items: center;
  padding-inline: .8rem;
  border-radius: 9px;
  font-size: .77rem;
  font-weight: 500;
  color: var(--muted);
  cursor: pointer;
  transition: background .2s ease, color .2s ease;
}

.dgs-12__ctl label:hover {
  color: var(--ink);
  background: var(--page2);
}

.dgs-12__sr:checked + label {
  background: var(--t4);
  color: var(--on4);
}

.dgs-12__sr:focus-visible + label {
  outline: 2px solid var(--t4);
  outline-offset: 2px;
}

.dgs-12__stage {
  display: flow-root;
}

.dgs-12__wrap {
  inline-size: min(72rem, 100%);
  margin-inline: auto;
}

.dgs-12__top {
  padding: clamp(3.5rem, 8vw, 6rem) clamp(1.25rem, 5vw, 4rem) calc(var(--unit) + clamp(2rem, 5vw, 3.5rem));
}

.dgs-12__eyebrow {
  margin: 0 0 .9rem;
  font-size: .75rem;
  font-weight: 600;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--t4);
}

.dgs-12__display {
  margin: 0 0 .9rem;
  max-inline-size: 24ch;
  font-size: clamp(2rem, 6vw, 3.6rem);
  font-weight: 700;
  line-height: 1.04;
  letter-spacing: -.04em;
  text-wrap: balance;
}

.dgs-12__lede {
  margin: 0;
  max-inline-size: 46ch;
  font-size: clamp(1rem, 2vw, 1.15rem);
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-12__step {
  position: relative;
  background: var(--fill);
  clip-path: polygon(0 var(--d), 100% 0, 100% 100%, 0 100%);
  margin-block-start: calc(var(--d) * -1 - 1px);
  padding: calc(var(--d) + clamp(1.75rem, 4vw, 3rem)) clamp(1.25rem, 5vw, 4rem) clamp(1.75rem, 4vw, 3rem);
}

.dgs-12__step--1 {
  --fill: var(--t1);
  --d: calc(var(--unit) * 1);
  z-index: 1;
}

.dgs-12__step--2 {
  --fill: var(--t2);
  --d: calc(var(--unit) * 1.6);
  z-index: 2;
}

.dgs-12__step--3 {
  --fill: var(--t3);
  --d: calc(var(--unit) * 2.2);
  z-index: 3;
}

.dgs-12__step--4 {
  --fill: var(--t4);
  --d: calc(var(--unit) * 2.8);
  z-index: 4;
  color: var(--on4);
}

.dgs-12__row {
  display: grid;
  gap: .5rem clamp(1.25rem, 3vw, 2.25rem);
  grid-template-columns: auto minmax(0, 1fr) auto;
  align-items: baseline;
}

.dgs-12__no {
  margin: 0;
  font-size: clamp(1.05rem, 2.6vw, 1.5rem);
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  opacity: .55;
}

.dgs-12__h2 {
  margin: 0 0 .35rem;
  font-size: clamp(1.2rem, 3.2vw, 1.75rem);
  font-weight: 700;
  letter-spacing: -.03em;
}

.dgs-12__body {
  margin: 0;
  max-inline-size: 60ch;
  font-size: .96rem;
  opacity: .82;
  text-wrap: pretty;
}

.dgs-12__eta {
  margin: 0;
  font-size: .8rem;
  font-weight: 600;
  letter-spacing: .04em;
  opacity: .7;
  white-space: nowrap;
}

.dgs-12__step--3 .dgs-12__body,
.dgs-12__step--4 .dgs-12__body {
  opacity: .88;
}

.dgs-12__after {
  background: var(--page2);
  padding: clamp(3rem, 7vw, 4.5rem) clamp(1.25rem, 5vw, 4rem) clamp(4rem, 9vw, 6rem);
}

.dgs-12__cols {
  display: grid;
  gap: 1rem clamp(2rem, 6vw, 4rem);
  grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
  align-items: start;
}

.dgs-12__h3 {
  margin: 0;
  font-size: clamp(1.25rem, 3.2vw, 1.8rem);
  font-weight: 700;
  letter-spacing: -.03em;
}

.dgs-12__note {
  margin: 0;
  max-inline-size: 58ch;
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-12__code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .86em;
  padding: .1em .35em;
  border-radius: 4px;
  background: rgba(8,32,31,.07);
}

.dgs-12:has(#dgs-12-d1:checked) {
  --unit: clamp(.5rem, 1.4vw, 1.3rem);
}

.dgs-12:has(#dgs-12-d3:checked) {
  --unit: clamp(1.4rem, 4.2vw, 4rem);
}

.dgs-12:has(#dgs-12-zig:checked) .dgs-12__step--2,
.dgs-12:has(#dgs-12-zig:checked) .dgs-12__step--4 {
  clip-path: polygon(0 0, 100% var(--d), 100% 100%, 0 100%);
}

@media (prefers-reduced-motion: reduce) {
  .dgs-12 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-12__step {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
    border-block-start: 1px solid CanvasText;
  }

  .dgs-12__ctl label {
    border: 1px solid CanvasText;
  }

  .dgs-12__sr:checked + label {
    background: Highlight;
    color: HighlightText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-12__sronly,
.dgs-12__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-12__theme {
  position: absolute;
  inset-block-start: clamp(.85rem, 2.2vw, 1.5rem);
  inset-inline-end: clamp(.85rem, 2.2vw, 1.5rem);
  z-index: 60;
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border-radius: 999px;
  border: 1px solid currentColor;
  color: inherit;
  background: rgba(127,127,127,.16);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  cursor: pointer;
  transition: translate .2s ease;
}

.dgs-12__theme:hover {
  translate: 0 -1px;
}

.dgs-12__sronly:focus-visible + .dgs-12__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-12__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-12__i--sun {
  display: none;
}

.dgs-12:has(#dgs-12-dark:checked) .dgs-12__i--moon {
  display: none;
}

.dgs-12:has(#dgs-12-dark:checked) .dgs-12__i--sun {
  display: block;
}

.dgs-12:has(#dgs-12-dark:checked) {
  --page: #0b0e13;
  --page2: #131820;
  --ink: #eef2f7;
  --muted: #96a0ac;
  --line: #222833;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-12__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-12__theme {
    border-color: CanvasText;
  }
}
```
