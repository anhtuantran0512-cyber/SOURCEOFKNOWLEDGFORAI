---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/css-transform-rotate-property-basics/"
title: "CSS Transform Rotate Property Basics"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "A reference panel for the rotate function itself: positive angles turn clockwise, negative anticlockwise, and the four angle units are shown side by side at…"
has_js: "false"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Transform Rotate Property Basics
Source: https://codefronts.com/motion/css-rotate-animation/css-transform-rotate-property-basics/

A reference panel for the rotate function itself: positive angles turn clockwise, negative anticlockwise, and the four angle units are shown side by side at equivalent values so 0.25turn, 90deg, 1.5708rad and 100grad land in exactly the same place. It closes with the modern independent rotate property and what it composes with that the shorthand does not.
## HTML
```html
<section class="rot-03" aria-labelledby="rot-03-h">
  <fieldset class="rot-03__theme">
    <legend class="rot-03__themelegend">Theme</legend>
    <input class="rot-03__themeinput" type="radio" name="rot-03-theme" id="rot-03-theme-auto" checked>
    <label class="rot-03__themeopt" for="rot-03-theme-auto">Auto</label>
    <input class="rot-03__themeinput" type="radio" name="rot-03-theme" id="rot-03-theme-light">
    <label class="rot-03__themeopt" for="rot-03-theme-light">Light</label>
    <input class="rot-03__themeinput" type="radio" name="rot-03-theme" id="rot-03-theme-dark">
    <label class="rot-03__themeopt" for="rot-03-theme-dark">Dark</label>
  </fieldset>

  <div class="rot-03__stage">
    <header class="rot-03__head">
      <p class="rot-03__eyebrow">Reference · transform: rotate()</p>
      <h2 class="rot-03__h" id="rot-03-h">Every angle unit, at the same angle</h2>
      <p class="rot-03__sub">Each row holds one quarter turn written four ways. If the conversions are right, all four tiles in a row point the same direction.</p>
    </header>

    <div class="rot-03__panel">
      <div class="rot-03__grid">
        <div class="rot-03__row">
          <p class="rot-03__rowlabel">Quarter turn</p>
          <div class="rot-03__cell"><div class="rot-03__tile" style="--a: 90deg" aria-hidden="true"></div><span class="rot-03__val">90deg</span></div>
          <div class="rot-03__cell"><div class="rot-03__tile" style="--a: 0.25turn" aria-hidden="true"></div><span class="rot-03__val">0.25turn</span></div>
          <div class="rot-03__cell"><div class="rot-03__tile" style="--a: 1.5708rad" aria-hidden="true"></div><span class="rot-03__val">1.5708rad</span></div>
          <div class="rot-03__cell"><div class="rot-03__tile" style="--a: 100grad" aria-hidden="true"></div><span class="rot-03__val">100grad</span></div>
        </div>
        <div class="rot-03__row">
          <p class="rot-03__rowlabel">Eighth turn</p>
          <div class="rot-03__cell"><div class="rot-03__tile" style="--a: 45deg" aria-hidden="true"></div><span class="rot-03__val">45deg</span></div>
          <div class="rot-03__cell"><div class="rot-03__tile" style="--a: 0.125turn" aria-hidden="true"></div><span class="rot-03__val">0.125turn</span></div>
          <div class="rot-03__cell"><div class="rot-03__tile" style="--a: 0.7854rad" aria-hidden="true"></div><span class="rot-03__val">0.7854rad</span></div>
          <div class="rot-03__cell"><div class="rot-03__tile" style="--a: 50grad" aria-hidden="true"></div><span class="rot-03__val">50grad</span></div>
        </div>
        <div class="rot-03__row">
          <p class="rot-03__rowlabel">Anticlockwise</p>
          <div class="rot-03__cell"><div class="rot-03__tile" style="--a: -30deg" aria-hidden="true"></div><span class="rot-03__val">-30deg</span></div>
          <div class="rot-03__cell"><div class="rot-03__tile" style="--a: -0.0833turn" aria-hidden="true"></div><span class="rot-03__val">-0.0833turn</span></div>
          <div class="rot-03__cell"><div class="rot-03__tile" style="--a: -0.5236rad" aria-hidden="true"></div><span class="rot-03__val">-0.5236rad</span></div>
          <div class="rot-03__cell"><div class="rot-03__tile" style="--a: -33.33grad" aria-hidden="true"></div><span class="rot-03__val">-33.33grad</span></div>
        </div>
        <div class="rot-03__row">
          <p class="rot-03__rowlabel">Past a full turn</p>
          <div class="rot-03__cell"><div class="rot-03__tile" style="--a: 405deg" aria-hidden="true"></div><span class="rot-03__val">405deg</span></div>
          <div class="rot-03__cell"><div class="rot-03__tile" style="--a: 1.125turn" aria-hidden="true"></div><span class="rot-03__val">1.125turn</span></div>
          <div class="rot-03__cell"><div class="rot-03__tile" style="--a: 7.0686rad" aria-hidden="true"></div><span class="rot-03__val">7.0686rad</span></div>
          <div class="rot-03__cell"><div class="rot-03__tile" style="--a: 450grad" aria-hidden="true"></div><span class="rot-03__val">450grad</span></div>
        </div>
      </div>
    </div>

    <div class="rot-03__pair">
      <article class="rot-03__note">
        <h3 class="rot-03__noteh">transform: rotate(45deg)</h3>
        <div class="rot-03__cell rot-03__cell--wide"><div class="rot-03__tile rot-03__tile--legacy" aria-hidden="true"></div></div>
        <p class="rot-03__notep">One property holds the whole transform list. A hover that rewrites <span class="rot-03__code">transform</span> to add a scale must restate the rotation or lose it.</p>
      </article>
      <article class="rot-03__note rot-03__note--modern">
        <h3 class="rot-03__noteh">rotate: 45deg</h3>
        <div class="rot-03__cell rot-03__cell--wide"><div class="rot-03__tile rot-03__tile--modern" aria-hidden="true"></div></div>
        <p class="rot-03__notep">Its own property, applied alongside <span class="rot-03__code">scale</span> and <span class="rot-03__code">translate</span> in a fixed order. Each can be animated on its own without touching the others.</p>
      </article>
    </div>

    <p class="rot-03__fine">Unitless angles are invalid — <span class="rot-03__code">rotate(45)</span> drops the declaration and the element renders flat. <span class="rot-03__code">rotate(0)</span> is the one legal exception.</p>
  </div>
</section>
```
## CSS
```css
.rot-03 {
  --page: #fbfbfc;
  --surface: #ffffff;
  --ink: #0d0f12;
  --muted: #5d6470;
  --rule: #e4e7ec;
  --accent: #0e8f9c;
  --tile: clamp(2.5rem, 8vw, 3.25rem);
  --font-display: ui-monospace, "SF Mono", "SFMono-Regular", Menlo, Consolas, monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-display);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(0 0 0)) {
  .rot-03 {
    --accent: oklch(0.6 0.11 195);
  }
}

.rot-03 *,
.rot-03 *::before,
.rot-03 *::after {
  box-sizing: border-box;
}

.rot-03__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.25rem, 3vw, 2rem);
  padding: clamp(1rem, 3vw, 2.5rem);
  padding-block-start: 5.25rem;
}

.rot-03__head {
  max-inline-size: 42rem;
  min-inline-size: 0;
}

.rot-03__eyebrow {
  margin: 0 0 0.5rem;
  font-size: 0.6875rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--accent);
}

.rot-03__h {
  margin: 0 0 0.5rem;
  font-size: clamp(1.25rem, 4vw, 1.875rem);
  font-weight: 600;
  letter-spacing: -0.02em;
}

.rot-03__sub {
  margin: 0;
  font-family: system-ui, sans-serif;
  font-size: 0.875rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-03__code {
  font-size: 0.9em;
  padding: 0.05em 0.3em;
  background: color-mix(in srgb, var(--accent) 10%, transparent);
  color: var(--accent);
  border-radius: 0.2rem;
}

.rot-03__panel {
  inline-size: min(100%, 52rem);
  border: 1px solid var(--rule);
  border-radius: 0.5rem;
  background: var(--surface);
  overflow: hidden;
}

.rot-03__grid {
  display: grid;
}

.rot-03__row {
  display: grid;
  grid-template-columns: minmax(0, 7rem) repeat(4, minmax(0, 1fr));
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem clamp(0.5rem, 2vw, 1rem);
  border-block-start: 1px solid var(--rule);
}

.rot-03__row:first-child {
  border-block-start: 0;
}

.rot-03__rowlabel {
  margin: 0;
  font-size: 0.6875rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  min-inline-size: 0;
}

.rot-03__cell {
  display: grid;
  place-items: center;
  gap: 0.45rem;
  min-inline-size: 0;
  padding-block: 0.35rem;
}

.rot-03__cell--wide {
  inline-size: 100%;
  block-size: calc(var(--tile) * 1.6);
}

.rot-03__tile {
  position: relative;
  inline-size: var(--tile);
  block-size: var(--tile);
  border: 1px solid var(--ink);
  background: color-mix(in srgb, var(--accent) 14%, transparent);
  transform: rotate(var(--a, 0deg));
}

.rot-03__tile::before {
  content: "";
  position: absolute;
  inset-block-start: 0;
  inset-inline-start: 50%;
  inline-size: 2px;
  block-size: 42%;
  translate: -50% 0;
  background: var(--accent);
}

.rot-03__tile::after {
  content: "";
  position: absolute;
  inset-block-start: 6%;
  inset-inline-start: 6%;
  inline-size: 0.35rem;
  block-size: 0.35rem;
  background: var(--ink);
}

.rot-03__tile--legacy {
  transform: rotate(45deg);
}

.rot-03__tile--modern {
  transform: none;
  rotate: 45deg;
}

.rot-03__val {
  font-size: 0.6875rem;
  letter-spacing: 0.01em;
  color: var(--muted);
  white-space: nowrap;
}

.rot-03__pair {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr));
  gap: 1rem;
  inline-size: min(100%, 52rem);
}

.rot-03__note {
  min-inline-size: 0;
  display: grid;
  gap: 0.75rem;
  padding: 1rem;
  border: 1px solid var(--rule);
  border-radius: 0.5rem;
  background: var(--surface);
}

.rot-03__note--modern {
  border-color: color-mix(in srgb, var(--accent) 45%, var(--rule));
}

.rot-03__noteh {
  margin: 0;
  font-size: 0.8125rem;
  font-weight: 600;
  letter-spacing: 0.01em;
}

.rot-03__notep {
  margin: 0;
  font-family: system-ui, sans-serif;
  font-size: 0.8125rem;
  line-height: 1.6;
  color: var(--muted);
  min-inline-size: 0;
}

.rot-03__fine {
  inline-size: min(100%, 52rem);
  margin: 0;
  font-family: system-ui, sans-serif;
  font-size: 0.75rem;
  line-height: 1.6;
  color: var(--muted);
}

@media (max-width: 40rem) {
  .rot-03__row {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .rot-03__rowlabel {
    grid-column: 1 / -1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rot-03__tile,
    .rot-03__tile--legacy,
    .rot-03__tile--modern {
    transition: none;
    animation: none;
  }
}

.rot-03__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 9;
  display: flex;
  align-items: center;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 8%, transparent);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  font-family: system-ui, sans-serif;
}

.rot-03__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-03__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-03__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.6875rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: inherit;
  opacity: 0.55;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}

.rot-03__themeopt:hover {
  opacity: 0.85;
}

.rot-03__themeinput:checked + .rot-03__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-03__themeinput:focus-visible + .rot-03__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .rot-03__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-03__themeinput:checked + .rot-03__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: dark) {
  .rot-03:not(:has(#rot-03-theme-light:checked)) {
    --page: #0a0b0d;
    --surface: #101216;
    --ink: #e9ecf1;
    --muted: #8d949f;
    --rule: #21242b;
    --accent: #35d6e2;
  }

  .rot-03:not(:has(#rot-03-theme-light:checked)) .rot-03__tile {
    border-color: #3a4048;
  }

  .rot-03:not(:has(#rot-03-theme-light:checked)) .rot-03__tile::after {
    background: #e9ecf1;
  }
}

@media (prefers-color-scheme: light) {
  .rot-03:has(#rot-03-theme-dark:checked) {
    --page: #0a0b0d;
    --surface: #101216;
    --ink: #e9ecf1;
    --muted: #8d949f;
    --rule: #21242b;
    --accent: #35d6e2;
  }
}

[data-theme="dark"] .rot-03:not(:has(#rot-03-theme-light:checked)) {
  --page: #0a0b0d;
  --surface: #101216;
  --ink: #e9ecf1;
  --muted: #8d949f;
  --rule: #21242b;
  --accent: #35d6e2;
}

[data-theme="dark"] .rot-03:not(:has(#rot-03-theme-light:checked)) .rot-03__tile {
  border-color: #3a4048;
}

.rot-03:has(#rot-03-theme-dark:checked) {
  --page: #0a0b0d;
  --surface: #101216;
  --ink: #e9ecf1;
  --muted: #8d949f;
  --rule: #21242b;
  --accent: #35d6e2;
}

.rot-03:has(#rot-03-theme-dark:checked) .rot-03__tile {
  border-color: #3a4048;
}

.rot-03:has(#rot-03-theme-dark:checked) .rot-03__tile::after {
  background: #e9ecf1;
}

.rot-03:has(#rot-03-theme-light:checked) {
  --page: #fbfbfc;
  --surface: #ffffff;
  --ink: #0d0f12;
  --muted: #5d6470;
  --rule: #e4e7ec;
  --accent: #0e8f9c;
}

.rot-03:has(#rot-03-theme-light:checked) .rot-03__tile {
  border-color: #0d0f12;
}

.rot-03:has(#rot-03-theme-light:checked) .rot-03__tile::after {
  background: #0d0f12;
}
```
