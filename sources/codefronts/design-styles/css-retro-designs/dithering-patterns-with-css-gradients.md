---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/dithering-patterns-with-css-gradients/"
title: "Dithering Patterns with CSS Gradients"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "Ordered dithering is how a limited palette fakes colours it does not have: alternate two available colours in a fixed pattern and the eye averages them."
has_js: "false"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dithering Patterns with CSS Gradients
Source: https://codefronts.com/design-styles/css-retro-designs/dithering-patterns-with-css-gradients/

Ordered dithering is how a limited palette fakes colours it does not have: alternate two available colours in a fixed pattern and the eye averages them. Built here from layered repeating-conic-gradient checkerboards over flat fills, with a smooth gradient beside Bayer ramps at 2, 4 and 8 colours &mdash; and an honest statement of where the CSS approximation stops.
## HTML
```html
<section class="rt-03" aria-labelledby="rt-03-title">
  <h2 class="rt-03__sr" id="rt-03-title">Ordered dithering ramps built from CSS gradients</h2>

  <div class="rt-03__theme">
    <input class="rt-03__theme-input" type="checkbox" id="rt-03-theme">
    <label class="rt-03__theme-label" for="rt-03-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-03__sr">Toggle dark surround</span>
    </label>
  </div>

  <div class="rt-03__stage">
    <header class="rt-03__head">
      <p class="rt-03__kicker">Palette &middot; Game Boy DMG-01 &middot; 4 tones, exact sRGB</p>
      <h3 class="rt-03__h">Four colours, twelve apparent tones</h3>
      <p class="rt-03__sub">Every band below contains only palette colours. The intermediate tones are patterns, not blends.</p>
    </header>

    <div class="rt-03__swatches">
      <span class="rt-03__sw rt-03__sw--0">#0f380f</span>
      <span class="rt-03__sw rt-03__sw--1">#306230</span>
      <span class="rt-03__sw rt-03__sw--2">#8bac0f</span>
      <span class="rt-03__sw rt-03__sw--3">#9bbc0f</span>
    </div>

    <div class="rt-03__ramps">
      <article class="rt-03__ramp" aria-labelledby="rt-03-r0">
        <h4 class="rt-03__ramp-h" id="rt-03-r0">Reference &middot; unlimited colour</h4>
        <div class="rt-03__bar rt-03__bar--smooth" aria-hidden="true"></div>
        <p class="rt-03__cap">A plain linear-gradient. Contains thousands of colours the hardware never had.</p>
      </article>

      <article class="rt-03__ramp" aria-labelledby="rt-03-r1">
        <h4 class="rt-03__ramp-h" id="rt-03-r1">2 colours &middot; 2&times;2 Bayer</h4>
        <div class="rt-03__bar" aria-hidden="true">
          <span class="rt-03__band rt-03__band--a0"></span>
          <span class="rt-03__band rt-03__band--a25"></span>
          <span class="rt-03__band rt-03__band--a50"></span>
          <span class="rt-03__band rt-03__band--a75"></span>
          <span class="rt-03__band rt-03__band--a100"></span>
        </div>
        <p class="rt-03__cap">Darkest and lightest tone only. Five apparent steps from two real ones.</p>
      </article>

      <article class="rt-03__ramp" aria-labelledby="rt-03-r2">
        <h4 class="rt-03__ramp-h" id="rt-03-r2">4 colours &middot; adjacent-pair dither</h4>
        <div class="rt-03__bar" aria-hidden="true">
          <span class="rt-03__band rt-03__band--b0"></span>
          <span class="rt-03__band rt-03__band--b1"></span>
          <span class="rt-03__band rt-03__band--b2"></span>
          <span class="rt-03__band rt-03__band--b3"></span>
          <span class="rt-03__band rt-03__band--b4"></span>
          <span class="rt-03__band rt-03__band--b5"></span>
          <span class="rt-03__band rt-03__band--b6"></span>
        </div>
        <p class="rt-03__cap">Each pattern mixes only its two neighbouring palette entries.</p>
      </article>

      <article class="rt-03__ramp" aria-labelledby="rt-03-r3">
        <h4 class="rt-03__ramp-h" id="rt-03-r3">8 steps &middot; 4px cell, fine mask</h4>
        <div class="rt-03__bar rt-03__bar--fine" aria-hidden="true">
          <span class="rt-03__band rt-03__band--b0"></span>
          <span class="rt-03__band rt-03__band--b1"></span>
          <span class="rt-03__band rt-03__band--b2"></span>
          <span class="rt-03__band rt-03__band--b3"></span>
          <span class="rt-03__band rt-03__band--b4"></span>
          <span class="rt-03__band rt-03__band--b5"></span>
          <span class="rt-03__band rt-03__band--b6"></span>
          <span class="rt-03__band rt-03__band--a100"></span>
        </div>
        <p class="rt-03__cap">Same construction at a 2px cell. Closer to a blend, further from a period-correct look.</p>
      </article>
    </div>

    <aside class="rt-03__panel">
      <h4 class="rt-03__panel-h">Coverage table</h4>
      <dl class="rt-03__dl">
        <div><dt>0%</dt><dd>flat base colour, no overlay</dd></div>
        <div><dt>25%</dt><dd>one quadrant of the 2&times;2 cell</dd></div>
        <div><dt>50%</dt><dd>two opposite quadrants &mdash; checkerboard</dd></div>
        <div><dt>75%</dt><dd>three quadrants, inverse of 25%</dd></div>
        <div><dt>100%</dt><dd>flat next palette colour</dd></div>
      </dl>
    </aside>
  </div>
</section>
```
## CSS
```css
.rt-03 {
  --rt-03-cell: 4px;
  --rt-03-p0: #0f380f;
  --rt-03-p1: #306230;
  --rt-03-p2: #8bac0f;
  --rt-03-p3: #9bbc0f;
  --rt-03-cond: ui-sans-serif, "Helvetica Neue", "Arial Narrow", Helvetica, Arial, sans-serif;
  --rt-03-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --rt-03-bg: #f2efe6;
  --rt-03-bg: oklch(95% 0.012 100);
  --rt-03-surface: #ffffff;
  --rt-03-surface: oklch(100% 0 0);
  --rt-03-ink: #15170f;
  --rt-03-ink: oklch(19% 0.012 120);
  --rt-03-ink-2: #4e5344;
  --rt-03-ink-2: oklch(45% 0.017 120);
  --rt-03-line: #b6b9a6;
  --rt-03-line: oklch(77% 0.02 118);
  --rt-03-acc: #2f6b12;
  --rt-03-acc: oklch(46% 0.14 133);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--rt-03-bg);
  color: var(--rt-03-ink);
  font-family: var(--rt-03-cond);
  -webkit-text-size-adjust: 100%;
}

.rt-03 *,
.rt-03 *::before,
.rt-03 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rt-03 {
    --rt-03-bg: #14160f;
    --rt-03-bg: oklch(19% 0.009 120);
    --rt-03-surface: #1e2117;
    --rt-03-surface: oklch(24% 0.012 120);
    --rt-03-ink: #f0f2e7;
    --rt-03-ink: oklch(96% 0.008 120);
    --rt-03-ink-2: #a8ad99;
    --rt-03-ink-2: oklch(74% 0.016 120);
    --rt-03-line: #414635;
    --rt-03-line: oklch(37% 0.018 120);
    --rt-03-acc: #a4d96a;
    --rt-03-acc: oklch(83% 0.15 133);
  }
}

.rt-03[data-theme="dark"],
.rt-03:has(.rt-03__theme-input:checked) {
  --rt-03-bg: #14160f;
  --rt-03-bg: oklch(19% 0.009 120);
  --rt-03-surface: #1e2117;
  --rt-03-surface: oklch(24% 0.012 120);
  --rt-03-ink: #f0f2e7;
  --rt-03-ink: oklch(96% 0.008 120);
  --rt-03-ink-2: #a8ad99;
  --rt-03-ink-2: oklch(74% 0.016 120);
  --rt-03-line: #414635;
  --rt-03-line: oklch(37% 0.018 120);
  --rt-03-acc: #a4d96a;
  --rt-03-acc: oklch(83% 0.15 133);
}

@media (prefers-color-scheme: light) {
  .rt-03:has(.rt-03__theme-input:checked) {
    --rt-03-bg: #14160f;
    --rt-03-bg: oklch(19% 0.009 120);
    --rt-03-surface: #1e2117;
    --rt-03-surface: oklch(24% 0.012 120);
    --rt-03-ink: #f0f2e7;
    --rt-03-ink: oklch(96% 0.008 120);
    --rt-03-ink-2: #a8ad99;
    --rt-03-ink-2: oklch(74% 0.016 120);
    --rt-03-line: #414635;
    --rt-03-line: oklch(37% 0.018 120);
    --rt-03-acc: #a4d96a;
    --rt-03-acc: oklch(83% 0.15 133);
  }
}

@media (prefers-color-scheme: dark) {
  .rt-03:has(.rt-03__theme-input:checked) {
    --rt-03-bg: #f2efe6;
    --rt-03-bg: oklch(95% 0.012 100);
    --rt-03-surface: #ffffff;
    --rt-03-surface: oklch(100% 0 0);
    --rt-03-ink: #15170f;
    --rt-03-ink: oklch(19% 0.012 120);
    --rt-03-ink-2: #4e5344;
    --rt-03-ink-2: oklch(45% 0.017 120);
    --rt-03-line: #b6b9a6;
    --rt-03-line: oklch(77% 0.02 118);
    --rt-03-acc: #2f6b12;
    --rt-03-acc: oklch(46% 0.14 133);
  }
}

.rt-03__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.rt-03__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 6;
}

.rt-03__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-03__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--rt-03-line);
  border-radius: 50%;
  background: var(--rt-03-surface);
  color: var(--rt-03-ink-2);
  cursor: pointer;
}

.rt-03__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-03__theme-input:focus-visible + .rt-03__theme-label {
  outline: 2px solid var(--rt-03-acc);
  outline-offset: 2px;
}

.rt-03__stage {
  max-inline-size: 68rem;
  margin-inline: auto;
  padding: clamp(3.5rem, 3rem + 3vw, 5rem) clamp(0.85rem, 0.5rem + 2vw, 2rem) 4rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: clamp(1.5rem, 1rem + 2vw, 2.25rem);
}

.rt-03__head {
  display: grid;
  gap: 0.45rem;
  min-inline-size: 0;
}

.rt-03__kicker {
  margin: 0;
  font-family: var(--rt-03-mono);
  font-size: 0.68rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--rt-03-ink-2);
}

.rt-03__h {
  margin: 0;
  font-size: clamp(1.35rem, 1rem + 2vw, 2.2rem);
  line-height: 1.08;
  letter-spacing: -0.03em;
  font-weight: 700;
  text-wrap: balance;
  min-inline-size: 0;
}

.rt-03__sub {
  margin: 0;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--rt-03-ink-2);
  max-inline-size: 52ch;
  text-wrap: pretty;
  min-inline-size: 0;
}

.rt-03__swatches {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.rt-03__sw {
  min-inline-size: 0;
  flex: none;
  font-family: var(--rt-03-mono);
  font-size: 0.7rem;
  padding: 0.55rem 0.7rem;
  border: 1px solid var(--rt-03-line);
  letter-spacing: 0.03em;
}

.rt-03__sw--0 {
  background: #0f380f;
  color: #9bbc0f;
}

.rt-03__sw--1 {
  background: #306230;
  color: #dff0a8;
}

.rt-03__sw--2 {
  background: #8bac0f;
  color: #10290a;
}

.rt-03__sw--3 {
  background: #9bbc0f;
  color: #10290a;
}

.rt-03__ramps {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.1rem;
}

.rt-03__ramp {
  min-inline-size: 0;
  display: grid;
  gap: 0.6rem;
  align-content: start;
  background: var(--rt-03-surface);
  border: 1px solid var(--rt-03-line);
  padding: clamp(0.8rem, 0.6rem + 0.8vw, 1.1rem);
}

.rt-03__ramp-h {
  margin: 0;
  font-family: var(--rt-03-mono);
  font-size: 0.7rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--rt-03-ink-2);
  min-inline-size: 0;
}

.rt-03__bar {
  display: flex;
  block-size: clamp(64px, 8vw, 92px);
  min-inline-size: 0;
  border: 2px solid #0f380f;
  overflow: hidden;
}

.rt-03__bar--smooth {
  background: linear-gradient(90deg, #0f380f, #306230, #8bac0f, #9bbc0f);
}

.rt-03__band {
  flex: 1 1 0;
  min-inline-size: 0;
  background-size: var(--rt-03-cell) var(--rt-03-cell);
}

.rt-03__bar--fine {
  --rt-03-cell: 2px;
}

.rt-03__band--a0 {
  background-color: var(--rt-03-p0);
}

.rt-03__band--a100 {
  background-color: var(--rt-03-p3);
}

.rt-03__band--a25 {
  background-color: var(--rt-03-p0);
  background-image: repeating-conic-gradient(var(--rt-03-p3) 0% 25%, rgba(0,0,0,0) 0% 100%);
}

.rt-03__band--a50 {
  background-color: var(--rt-03-p0);
  background-image: repeating-conic-gradient(var(--rt-03-p3) 0% 25%, rgba(0,0,0,0) 0% 50%, var(--rt-03-p3) 0% 75%, rgba(0,0,0,0) 0% 100%);
}

.rt-03__band--a75 {
  background-color: var(--rt-03-p3);
  background-image: repeating-conic-gradient(var(--rt-03-p0) 0% 25%, rgba(0,0,0,0) 0% 100%);
}

.rt-03__band--b0 {
  background-color: var(--rt-03-p0);
}

.rt-03__band--b1 {
  background-color: var(--rt-03-p0);
  background-image: repeating-conic-gradient(var(--rt-03-p1) 0% 25%, rgba(0,0,0,0) 0% 50%, var(--rt-03-p1) 0% 75%, rgba(0,0,0,0) 0% 100%);
}

.rt-03__band--b2 {
  background-color: var(--rt-03-p1);
}

.rt-03__band--b3 {
  background-color: var(--rt-03-p1);
  background-image: repeating-conic-gradient(var(--rt-03-p2) 0% 25%, rgba(0,0,0,0) 0% 50%, var(--rt-03-p2) 0% 75%, rgba(0,0,0,0) 0% 100%);
}

.rt-03__band--b4 {
  background-color: var(--rt-03-p2);
}

.rt-03__band--b5 {
  background-color: var(--rt-03-p2);
  background-image: repeating-conic-gradient(var(--rt-03-p3) 0% 25%, rgba(0,0,0,0) 0% 50%, var(--rt-03-p3) 0% 75%, rgba(0,0,0,0) 0% 100%);
}

.rt-03__band--b6 {
  background-color: var(--rt-03-p3);
}

@supports not (background: repeating-conic-gradient(#000 0% 25%, #fff 0% 50%)) {
  .rt-03__band--a25,
    .rt-03__band--a50,
    .rt-03__band--a75,
    .rt-03__band--b1,
    .rt-03__band--b3,
    .rt-03__band--b5 {
    background-image: repeating-linear-gradient(45deg, currentColor 0 2px, rgba(0,0,0,0) 2px 4px);
  }

  .rt-03__band--a25,
    .rt-03__band--a50 {
    color: var(--rt-03-p3);
  }

  .rt-03__band--a75 {
    color: var(--rt-03-p0);
  }

  .rt-03__band--b1 {
    color: var(--rt-03-p1);
  }

  .rt-03__band--b3 {
    color: var(--rt-03-p2);
  }

  .rt-03__band--b5 {
    color: var(--rt-03-p3);
  }
}

.rt-03__cap {
  margin: 0;
  font-size: 0.82rem;
  line-height: 1.5;
  color: var(--rt-03-ink-2);
  min-inline-size: 0;
  text-wrap: pretty;
}

.rt-03__panel {
  min-inline-size: 0;
  background: var(--rt-03-surface);
  border: 1px solid var(--rt-03-line);
  border-left: 4px solid var(--rt-03-acc);
  padding: clamp(0.85rem, 0.6rem + 1vw, 1.2rem);
  display: grid;
  gap: 0.65rem;
}

.rt-03__panel-h {
  margin: 0;
  font-family: var(--rt-03-mono);
  font-size: 0.7rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--rt-03-ink-2);
}

.rt-03__dl {
  margin: 0;
  display: grid;
  gap: 0.3rem;
  font-size: 0.85rem;
}

.rt-03__dl > div {
  display: flex;
  gap: 0.75rem;
  align-items: baseline;
  min-inline-size: 0;
}

.rt-03__dl dt {
  margin: 0;
  font-family: var(--rt-03-mono);
  font-variant-numeric: tabular-nums;
  inline-size: 3.5rem;
  flex: none;
  color: var(--rt-03-acc);
}

.rt-03__dl dd {
  margin: 0;
  color: var(--rt-03-ink-2);
  min-inline-size: 0;
}

@media (min-width: 54rem) {
  .rt-03__ramps {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
```
