---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-diagonal-gradient-overlay-section/"
title: "CSS Diagonal Gradient Overlay Section"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "An angled gradient band that overlaps the section above it and blends where the two meet — the overlap is the subject, not decoration."
has_js: "false"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Diagonal Gradient Overlay Section
Source: https://codefronts.com/layouts/css-diagonal-sections/css-diagonal-gradient-overlay-section/

An angled gradient band that overlaps the section above it and blends where the two meet — the overlap is the subject, not decoration. The gradient rides a pseudo-element with mix-blend-mode: multiply, so the cards it crosses stay visible through it and the intersection does real work; the band's own text sits above the blend and stays crisp.
## HTML
```html
<div class="dgs-14">
  <input class="dgs-14__sronly" type="checkbox" id="dgs-14-dark">
  <label class="dgs-14__theme" for="dgs-14-dark">
    <svg class="dgs-14__i dgs-14__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-14__i dgs-14__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-14__srtext">Toggle dark theme</span>
  </label>
  <fieldset class="dgs-14__ctl">
    <legend class="dgs-14__vh">Overlay controls</legend>
    <input class="dgs-14__sr" type="radio" name="dgs-14-o" id="dgs-14-o1"><label for="dgs-14-o1">Sheer</label>
    <input class="dgs-14__sr" type="radio" name="dgs-14-o" id="dgs-14-o2" checked><label for="dgs-14-o2">Aurora</label>
    <input class="dgs-14__sr" type="radio" name="dgs-14-o" id="dgs-14-o3"><label for="dgs-14-o3">Solid</label>
  </fieldset>

  <div class="dgs-14__stage">
    <section class="dgs-14__data" aria-labelledby="dgs-14-a">
      <div class="dgs-14__grid" aria-hidden="true"></div>
      <div class="dgs-14__wrap">
        <p class="dgs-14__eyebrow">Wavelength &mdash; traces</p>
        <h2 class="dgs-14__display" id="dgs-14-a">Latency, per span, per deploy</h2>
        <p class="dgs-14__lede">Sampling at the edge, full traces for anything over your budget, and a diff against the previous release.</p>
        <ul class="dgs-14__series" aria-label="p95 latency by service">
          <li><span>checkout</span><b style="--v: 82%"></b><em>412 ms</em></li>
          <li><span>catalog</span><b style="--v: 46%"></b><em>228 ms</em></li>
          <li><span>identity</span><b style="--v: 28%"></b><em>139 ms</em></li>
          <li><span>search</span><b style="--v: 64%"></b><em>318 ms</em></li>
        </ul>
      </div>
    </section>

    <section class="dgs-14__overlay" aria-labelledby="dgs-14-b">
      <div class="dgs-14__wrap">
        <p class="dgs-14__eyebrow dgs-14__eyebrow--on">Translucent, not opaque</p>
        <h2 class="dgs-14__h2" id="dgs-14-b">The overlay rides over the chart it is cutting</h2>
        <p class="dgs-14__body">This band is angled <em>and</em> semi-transparent, so the section above shows through the top of the overlap — the grid lines and the bars keep going under the diagonal. That is the point of a gradient overlay rather than a flat cut: the join reads as one continuous surface being tinted, not two blocks butted together.</p>
        <p class="dgs-14__mono" aria-hidden="true">background: linear-gradient(168deg, oklch(0.62 .21 292 / .55), oklch(0.2 .05 250 / .96))</p>
        <dl class="dgs-14__legend">
          <div><dt>Overlap</dt><dd>clamp(3rem, 9vw, 11rem)</dd></div>
          <div><dt>Top alpha</dt><dd>0.55</dd></div>
          <div><dt>Base alpha</dt><dd>0.96</dd></div>
        </dl>
      </div>
    </section>

    <section class="dgs-14__after" aria-labelledby="dgs-14-c">
      <div class="dgs-14__wrap">
        <h2 class="dgs-14__h3" id="dgs-14-c">Keeping text legible over a see-through band</h2>
        <p class="dgs-14__body dgs-14__body--dim">Alpha ramps from light at the diagonal to nearly solid where the copy sits, so contrast never depends on what is underneath. Test it against your busiest chart, not an empty section.</p>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&display=swap');

.dgs-14 {
  --over: clamp(3rem, 9vw, 11rem);
  --a1: rgba(124,92,255,.55);
  --a2: rgba(15,22,48,.96);
  --void: #070b18;
  --void2: #0b1226;
  --on: #eef1ff;
  --dim: #93a0c8;
  --cyan: #55e6d0;
  --violet: #8b6bff;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--void);
  color: var(--on);
  font-family: 'Space Grotesk', system-ui, -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

.dgs-14 *,
.dgs-14 *::before,
.dgs-14 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.6 0.2 292)) {
  .dgs-14 {
    --void: oklch(0.14 0.03 265);
    --void2: oklch(0.19 0.04 265);
    --on: oklch(0.96 0.012 265);
    --dim: oklch(0.71 0.04 265);
    --cyan: oklch(0.85 0.12 178);
    --violet: oklch(0.66 0.19 292);
    --a1: oklch(0.62 0.21 292 / .55);
    --a2: oklch(0.2 0.05 260 / .96);
  }
}

.dgs-14__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-14__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.dgs-14__ctl {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 40;
  margin: 0;
  padding: .28rem;
  display: flex;
  gap: .2rem;
  border: 1px solid rgba(238,241,255,.16);
  border-radius: 10px;
  background: rgba(7,11,24,.7);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
}

.dgs-14__ctl label {
  min-inline-size: 3rem;
  min-block-size: 2.5rem;
  display: grid;
  place-items: center;
  padding-inline: .8rem;
  border-radius: 7px;
  font-size: .77rem;
  font-weight: 500;
  color: var(--dim);
  cursor: pointer;
  transition: background .2s ease, color .2s ease;
}

.dgs-14__ctl label:hover {
  color: var(--on);
}

.dgs-14__sr:checked + label {
  background: var(--violet);
  color: #0a0718;
}

.dgs-14__sr:focus-visible + label {
  outline: 2px solid var(--cyan);
  outline-offset: 2px;
}

.dgs-14__stage {
  display: flow-root;
}

.dgs-14__wrap {
  inline-size: min(72rem, 100%);
  margin-inline: auto;
}

.dgs-14__data {
  position: relative;
  isolation: isolate;
  background: var(--void);
  padding: clamp(3.5rem, 8vw, 6rem) clamp(1.25rem, 5vw, 4rem) calc(var(--over) + clamp(2.5rem, 6vw, 4rem));
}

.dgs-14__grid {
  position: absolute;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  opacity: .5;
  background: linear-gradient(rgba(147,160,200,.14) 1px, transparent 1px) 0 0 / 100% 3.25rem, linear-gradient(90deg, rgba(147,160,200,.1) 1px, transparent 1px) 0 0 / 4.5rem 100%, radial-gradient(40rem 22rem at 78% 6%, rgba(85,230,208,.12), transparent 70%);
}

.dgs-14__eyebrow {
  margin: 0 0 .9rem;
  font-family: ui-monospace, Menlo, monospace;
  font-size: .74rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--cyan);
}

.dgs-14__eyebrow--on {
  color: #d7ccff;
}

.dgs-14__display {
  margin: 0 0 1rem;
  max-inline-size: 22ch;
  font-size: clamp(2.1rem, 6.4vw, 3.9rem);
  font-weight: 600;
  line-height: 1.04;
  letter-spacing: -.04em;
  text-wrap: balance;
}

.dgs-14__lede {
  margin: 0 0 clamp(2rem, 5vw, 3rem);
  max-inline-size: 48ch;
  font-size: clamp(1.02rem, 2vw, 1.18rem);
  color: var(--dim);
  text-wrap: pretty;
}

.dgs-14__series {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .7rem;
  max-inline-size: 40rem;
}

.dgs-14__series li {
  display: grid;
  gap: .75rem;
  grid-template-columns: 6rem minmax(0, 1fr) 4.5rem;
  align-items: center;
  font-family: ui-monospace, Menlo, monospace;
  font-size: .78rem;
}

.dgs-14__series span {
  color: var(--dim);
}

.dgs-14__series b {
  display: block;
  block-size: .7rem;
  border-radius: 999px;
  background: rgba(147,160,200,.16);
  position: relative;
  overflow: clip;
}

.dgs-14__series b::after {
  content: '';
  position: absolute;
  inset: 0 auto 0 0;
  inline-size: var(--v);
  border-radius: 999px;
  background: linear-gradient(90deg, var(--cyan), var(--violet));
  animation: dgs-14-grow 1.2s cubic-bezier(.2,.8,.3,1) both;
}

@keyframes dgs-14-grow {
  from {
    inline-size: 0;
  }
}

.dgs-14__series em {
  font-style: normal;
  text-align: end;
  color: var(--on);
  font-variant-numeric: tabular-nums;
}

.dgs-14__overlay {
  position: relative;
  z-index: 2;
  background: linear-gradient(168deg, var(--a1) 0%, var(--a2) 78%);
  -webkit-backdrop-filter: blur(2px);
  backdrop-filter: blur(2px);
  clip-path: polygon(0 var(--over), 100% 0, 100% 100%, 0 100%);
  margin-block-start: calc(var(--over) * -1);
  padding: calc(var(--over) + clamp(2.5rem, 6vw, 4rem)) clamp(1.25rem, 5vw, 4rem) clamp(3.5rem, 8vw, 5.5rem);
}

.dgs-14__h2 {
  margin: 0 0 1rem;
  max-inline-size: 26ch;
  font-size: clamp(1.6rem, 4.4vw, 2.6rem);
  font-weight: 600;
  line-height: 1.06;
  letter-spacing: -.035em;
  text-wrap: balance;
}

.dgs-14__body {
  margin: 0 0 1.1rem;
  max-inline-size: 58ch;
  color: rgba(238,241,255,.84);
  text-wrap: pretty;
}

.dgs-14__body--dim {
  color: var(--dim);
}

.dgs-14__mono {
  margin: 0 0 clamp(2rem, 5vw, 2.75rem);
  font-family: ui-monospace, Menlo, monospace;
  font-size: clamp(.6rem, 1.5vw, .74rem);
  color: #d7ccff;
  overflow-wrap: anywhere;
}

.dgs-14__legend {
  margin: 0;
  display: grid;
  gap: 1px;
  grid-template-columns: repeat(auto-fit, minmax(10rem, 1fr));
  background: rgba(238,241,255,.14);
  border: 1px solid rgba(238,241,255,.14);
  border-radius: 12px;
  overflow: clip;
}

.dgs-14__legend > div {
  padding: .9rem 1rem;
  background: rgba(9,13,30,.6);
}

.dgs-14__legend dt {
  font-size: .7rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--dim);
}

.dgs-14__legend dd {
  margin: .25rem 0 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: .82rem;
}

.dgs-14__after {
  position: relative;
  z-index: 1;
  background: var(--void2);
  padding: clamp(3rem, 7vw, 4.5rem) clamp(1.25rem, 5vw, 4rem) clamp(4rem, 9vw, 6rem);
}

.dgs-14__h3 {
  margin: 0 0 .8rem;
  font-size: clamp(1.3rem, 3.4vw, 1.9rem);
  font-weight: 600;
  letter-spacing: -.03em;
}

.dgs-14:has(#dgs-14-o1:checked) {
  --a1: rgba(124,92,255,.22);
  --a2: rgba(15,22,48,.72);
}

.dgs-14:has(#dgs-14-o3:checked) {
  --a1: #241a54;
  --a2: #0d1330;
}

@supports (color: oklch(0.6 0.2 292)) {
  .dgs-14:has(#dgs-14-o1:checked) {
    --a1: oklch(0.62 0.21 292 / .22);
    --a2: oklch(0.2 0.05 260 / .72);
  }

  .dgs-14:has(#dgs-14-o3:checked) {
    --a1: oklch(0.34 0.13 292);
    --a2: oklch(0.21 0.06 262);
  }
}

@media (prefers-reduced-motion: reduce) {
  .dgs-14 *,
    .dgs-14 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-14__grid {
    display: none;
  }

  .dgs-14__overlay {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
    border-block-start: 1px solid CanvasText;
  }

  .dgs-14__legend,
    .dgs-14__ctl label {
    border: 1px solid CanvasText;
  }

  .dgs-14__sr:checked + label {
    background: Highlight;
    color: HighlightText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-14__sronly,
.dgs-14__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-14__theme {
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

.dgs-14__theme:hover {
  translate: 0 -1px;
}

.dgs-14__sronly:focus-visible + .dgs-14__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-14__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-14__i--sun {
  display: none;
}

.dgs-14:has(#dgs-14-dark:checked) .dgs-14__i--moon {
  display: none;
}

.dgs-14:has(#dgs-14-dark:checked) .dgs-14__i--sun {
  display: block;
}

.dgs-14:has(#dgs-14-dark:checked) {
  --void: #f5f6f8;
  --ink: #0d1016;
  --muted: #5c636e;
  --line: rgba(13,16,22,.14);
}

@media (prefers-reduced-motion: reduce) {
  .dgs-14__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-14__theme {
    border-color: CanvasText;
  }
}
```
