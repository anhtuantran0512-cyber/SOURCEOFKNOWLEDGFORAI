---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/mountain-parallax-layers/"
title: "Layered Depth with Divergent Ranges"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "Five elements, one named timeline, five different ranges."
has_js: "false"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Layered Depth with Divergent Ranges
Source: https://codefronts.com/motion/css-scroll-animations/mountain-parallax-layers/

Five elements, one named timeline, five different ranges. The apparent depth comes entirely from range divergence — no extra timelines, no per-element scrollers, no duplicated bindings. The lesson is that ranges, not timelines, are the unit you reach for when several things should move at different rates.
## HTML
```html
<section class="sa-20" aria-labelledby="sa-20-h">
  <fieldset class="sa-20__theme">
    <legend class="sa-20__themelegend">Theme</legend>
    <input class="sa-20__themeinput" type="radio" name="sa-20-theme" id="sa-20-theme-auto" checked>
    <label class="sa-20__themeopt" for="sa-20-theme-auto">Auto</label>
    <input class="sa-20__themeinput" type="radio" name="sa-20-theme" id="sa-20-theme-light">
    <label class="sa-20__themeopt" for="sa-20-theme-light">Light</label>
    <input class="sa-20__themeinput" type="radio" name="sa-20-theme" id="sa-20-theme-dark">
    <label class="sa-20__themeopt" for="sa-20-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-20__stage">
    <header class="sa-20__head">
      <p class="sa-20__eyebrow">One timeline · five ranges</p>
      <h2 class="sa-20__h" id="sa-20-h">Depth from range divergence</h2>
      <p class="sa-20__sub">All five plates read <span class="sa-20__mono">--sa-20-deck</span>. Nothing else differs between them except the range printed in the table.</p>
    </header>

    <div class="sa-20__layout">
      <div class="sa-20__scroller" tabindex="0" role="region" aria-label="Layered plates on one timeline, scrollable">
        <div class="sa-20__deck">
          <span class="sa-20__plate sa-20__plate--1" aria-hidden="true">Ledger</span>
          <span class="sa-20__plate sa-20__plate--2" aria-hidden="true">Payouts</span>
          <span class="sa-20__plate sa-20__plate--3" aria-hidden="true">Reconciliation</span>
          <span class="sa-20__plate sa-20__plate--4" aria-hidden="true">Disputes</span>
          <span class="sa-20__plate sa-20__plate--5" aria-hidden="true">Settlement</span>
        </div>
        <div class="sa-20__copy">
          <p class="sa-20__p">Meridian's settlement stack, drawn as five plates. Keep scrolling: the spacing between them changes because their ranges do, not because they are on separate timelines.</p>
          <p class="sa-20__p">Phase lock is the practical benefit. However fast the reader scrolls, or flings, or drags the scrollbar, the five plates stay in a fixed relationship.</p>
          <p class="sa-20__p">Independent triggered animations cannot promise that. Five observers firing at five thresholds will drift the moment the scroll is fast.</p>
          <p class="sa-20__p">Retuning is a single-column edit. Change one range in the table and only that plate moves; nothing else in the stack needs revisiting.</p>
          <p class="sa-20__p">Adding a sixth plate means adding a sixth range. The scroller, the name and the axis are already declared and stay untouched.</p>
          <p class="sa-20__p">Because every plate shares a fill mode of both, the arrangement holds at the top and bottom of the scroll rather than collapsing at the ends.</p>
          <p class="sa-20__p">The same pattern drives staged dashboards: one timeline, one range per panel, no coordination code between them.</p>
          <p class="sa-20__p">Where a plate should stop early and stay put, give it a range that ends before the others and let fill mode hold it.</p>
          <p class="sa-20__p">Keep one animation per property per element. Two ranges fighting over the same transform is the one way this pattern goes wrong.</p>
          <p class="sa-20__p">If two plates must move on different properties, that is fine — one on transform, one on opacity, both on the same name and both phase locked.</p>
          <p class="sa-20__p">The table beside the stack is not decoration. Printing the ranges is how this stays maintainable once there are more than three consumers.</p>
          <p class="sa-20__p">Names are global. A second collection publishing a bare timeline name on the same page will collide with yours, which is why every name here is prefixed.</p>
          <p class="sa-20__p">Meridian runs this pattern across the settlement dashboard: one timeline per panel, one range per row, no coordination code anywhere.</p>
          <p class="sa-20__p">Sam Rivera's rule of thumb — if two elements should never disagree, they belong on one timeline.</p>
        </div>
      </div>

      <table class="sa-20__table">
        <caption class="sa-20__caption">Range per plate</caption>
        <tbody class="sa-20__tbody">
          <tr class="sa-20__tr"><th class="sa-20__th" scope="row">Ledger</th><td class="sa-20__td">0% 100%</td><td class="sa-20__td sa-20__td--rate">slowest</td></tr>
          <tr class="sa-20__tr"><th class="sa-20__th" scope="row">Payouts</th><td class="sa-20__td">5% 90%</td><td class="sa-20__td sa-20__td--rate">slow</td></tr>
          <tr class="sa-20__tr"><th class="sa-20__th" scope="row">Reconciliation</th><td class="sa-20__td">15% 80%</td><td class="sa-20__td sa-20__td--rate">mid</td></tr>
          <tr class="sa-20__tr"><th class="sa-20__th" scope="row">Disputes</th><td class="sa-20__td">30% 70%</td><td class="sa-20__td sa-20__td--rate">fast</td></tr>
          <tr class="sa-20__tr"><th class="sa-20__th" scope="row">Settlement</th><td class="sa-20__td">45% 65%</td><td class="sa-20__td sa-20__td--rate">fastest</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>
```
## CSS
```css
.sa-20 {
  --page: #f2f5f4;
  --s1: #ffffff;
  --s2: #e9eeed;
  --s3: #dbe3e1;
  --ink: #12211f;
  --muted: #4f635f;
  --accent: #12a37a;
  --page: oklch(96% 0.006 175);
  --s1: oklch(100% 0 0);
  --s2: oklch(93% 0.008 175);
  --s3: oklch(88% 0.01 175);
  --ink: oklch(20% 0.02 180);
  --muted: oklch(47% 0.025 180);
  --accent: oklch(62% 0.13 165);
  --sa-20-travel: 3.5rem;
  --font-display: "Segoe UI", Tahoma, "Trebuchet MS", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  position: relative;
  padding: 3.5rem 1rem 2.75rem;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

.sa-20 *,
.sa-20 *::before,
.sa-20 *::after {
  box-sizing: border-box;
}

.sa-20__stage {
  max-inline-size: 60rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.sa-20__head {
  display: flex;
  flex-direction: column;
  gap: 0.375rem;
}

.sa-20__eyebrow {
  margin: 0;
  font-size: 0.625rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sa-20__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.375rem, 4vw, 2rem);
  font-weight: 600;
  letter-spacing: -0.02em;
  line-height: 1.1;
}

.sa-20__sub {
  margin: 0;
  max-inline-size: 42rem;
  font-size: 0.875rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-20__mono {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.85em;
  color: var(--accent);
}

.sa-20__layout {
  display: grid;
  grid-template-columns: minmax(0, 1.6fr) minmax(0, 1fr);
  gap: 0.75rem;
  align-items: start;
}

.sa-20__scroller {
  block-size: 60vh;
  min-block-size: 20rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  background: var(--s1);
  scroll-timeline: --sa-20-deck block;
}

.sa-20__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.sa-20__deck {
  position: sticky;
  inset-block-start: 0;
  z-index: 2;
  block-size: 12rem;
  padding: 0.75rem;
  background: var(--s2);
  overflow: hidden;
}

.sa-20__plate {
  position: absolute;
  inset-inline: 0.75rem;
  display: flex;
  align-items: center;
  padding-inline: 0.75rem;
  block-size: 2rem;
  background: var(--s3);
  color: var(--ink);
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  will-change: transform;
}

.sa-20__plate--1 {
  inset-block-start: 0.75rem;
  transform: translate3d(0, calc(var(--sa-20-travel) * 0.2), 0);
}

.sa-20__plate--2 {
  inset-block-start: 2.75rem;
  background: color-mix(in srgb, var(--accent) 12%, var(--s3));
  transform: translate3d(0, calc(var(--sa-20-travel) * 0.4), 0);
}

.sa-20__plate--3 {
  inset-block-start: 4.75rem;
  background: color-mix(in srgb, var(--accent) 24%, var(--s3));
  transform: translate3d(0, calc(var(--sa-20-travel) * 0.6), 0);
}

.sa-20__plate--4 {
  inset-block-start: 6.75rem;
  background: color-mix(in srgb, var(--accent) 40%, var(--s3));
  transform: translate3d(0, calc(var(--sa-20-travel) * 0.8), 0);
}

.sa-20__plate--5 {
  inset-block-start: 8.75rem;
  background: var(--accent);
  color: var(--s1);
  font-weight: 700;
  transform: translate3d(0, var(--sa-20-travel), 0);
}

.sa-20__copy {
  display: flex;
  flex-direction: column;
  gap: 0.625rem;
  min-block-size: calc(100% + 4rem);
  padding: 1rem 1rem 3rem;
}

.sa-20__p {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-20__table {
  inline-size: 100%;
  border-collapse: collapse;
  background: var(--s1);
  font-size: 0.75rem;
}

.sa-20__caption {
  padding: 0.625rem 0.75rem;
  background: var(--s2);
  font-size: 0.625rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  text-align: start;
  color: var(--muted);
}

.sa-20__tr {
  border-block-end: 1px solid var(--s2);
}

.sa-20__th {
  padding: 0.625rem 0.75rem;
  text-align: start;
  font-weight: 600;
  min-inline-size: 0;
}

.sa-20__td {
  padding: 0.625rem 0.5rem;
  font-family: ui-monospace, Menlo, monospace;
  color: var(--muted);
}

.sa-20__td--rate {
  text-align: end;
  color: var(--accent);
  font-family: system-ui, sans-serif;
  font-weight: 600;
}

@keyframes sa-20-p1 {
  from {
    transform: translate3d(0, 0, 0);
  }

  to {
    transform: translate3d(0, calc(var(--sa-20-travel) * 0.2), 0);
  }
}

@keyframes sa-20-p2 {
  from {
    transform: translate3d(0, 0, 0);
  }

  to {
    transform: translate3d(0, calc(var(--sa-20-travel) * 0.4), 0);
  }
}

@keyframes sa-20-p3 {
  from {
    transform: translate3d(0, 0, 0);
  }

  to {
    transform: translate3d(0, calc(var(--sa-20-travel) * 0.6), 0);
  }
}

@keyframes sa-20-p4 {
  from {
    transform: translate3d(0, 0, 0);
  }

  to {
    transform: translate3d(0, calc(var(--sa-20-travel) * 0.8), 0);
  }
}

@keyframes sa-20-p5 {
  from {
    transform: translate3d(0, 0, 0);
  }

  to {
    transform: translate3d(0, var(--sa-20-travel), 0);
  }
}

@supports (animation-timeline: scroll()) {
  .sa-20__plate {
    animation-timing-function: linear;
    animation-fill-mode: both;
    animation-timeline: --sa-20-deck;
  }

  .sa-20__plate--1 {
    animation-name: sa-20-p1;
    animation-range: 0% 100%;
  }

  .sa-20__plate--2 {
    animation-name: sa-20-p2;
    animation-range: 5% 90%;
  }

  .sa-20__plate--3 {
    animation-name: sa-20-p3;
    animation-range: 15% 80%;
  }

  .sa-20__plate--4 {
    animation-name: sa-20-p4;
    animation-range: 30% 70%;
  }

  .sa-20__plate--5 {
    animation-name: sa-20-p5;
    animation-range: 45% 65%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sa-20__plate {
    animation: none;
  }
}

.sa-20__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 9;
  display: inline-flex;
  gap: 0;
  margin: 0;
  padding: 0;
  border: 0;
  background: var(--s1);
}

.sa-20__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-20__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-20__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.625rem;
  font-size: 0.625rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-20__themeinput:checked + .sa-20__themeopt {
  color: var(--s1);
  background: var(--accent);
}

.sa-20__themeinput:focus-visible + .sa-20__themeopt {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 48rem) {
  .sa-20__layout {
    grid-template-columns: minmax(0, 1fr);
  }

  .sa-20 {
    padding-block-start: 4.25rem;
  }
}

@media (forced-colors: active) {
  .sa-20__plate {
    border: 1px solid CanvasText;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-20:not(:has(#sa-20-theme-light:checked)) {
    --page: #0c1211;
    --s1: #131a19;
    --s2: #1a2322;
    --s3: #24302e;
    --ink: #e6efec;
    --muted: #92a5a1;
    --accent: #35d6a4;
  }

  .sa-20:not(:has(#sa-20-theme-light:checked)) .sa-20__plate--5,
    .sa-20:not(:has(#sa-20-theme-light:checked)) .sa-20__themeinput:checked + .sa-20__themeopt {
    color: #0c1211;
  }
}

@media (prefers-color-scheme: light) {
  .sa-20:has(#sa-20-theme-dark:checked) {
    --page: #0c1211;
    --s1: #131a19;
    --s2: #1a2322;
    --s3: #24302e;
    --ink: #e6efec;
    --muted: #92a5a1;
    --accent: #35d6a4;
  }

  .sa-20:has(#sa-20-theme-dark:checked) .sa-20__plate--5,
    .sa-20:has(#sa-20-theme-dark:checked) .sa-20__themeinput:checked + .sa-20__themeopt {
    color: #0c1211;
  }
}

[data-theme="dark"] .sa-20:not(:has(#sa-20-theme-light:checked)) {
  --page: #0c1211;
  --s1: #131a19;
  --s2: #1a2322;
  --s3: #24302e;
  --ink: #e6efec;
  --muted: #92a5a1;
  --accent: #35d6a4;
}

.sa-20:has(#sa-20-theme-dark:checked) {
  --page: #0c1211;
  --s1: #131a19;
  --s2: #1a2322;
  --s3: #24302e;
  --ink: #e6efec;
  --muted: #92a5a1;
  --accent: #35d6a4;
}

.sa-20:has(#sa-20-theme-dark:checked) .sa-20__plate--5,
.sa-20:has(#sa-20-theme-dark:checked) .sa-20__themeinput:checked + .sa-20__themeopt {
  color: #0c1211;
}

.sa-20:has(#sa-20-theme-light:checked) {
  --page: #f2f5f4;
  --s1: #ffffff;
  --s2: #e9eeed;
  --s3: #dbe3e1;
  --ink: #12211f;
  --muted: #4f635f;
  --accent: #12a37a;
}
```
