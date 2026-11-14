---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/rotate-transform-origin-pivot/"
title: "Rotate Transform Origin Pivot"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "One element, one rotation angle, nine different pivots, laid out in a labelled three-by-three grid — every corner, every edge midpoint and the centre."
has_js: "false"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rotate Transform Origin Pivot
Source: https://codefronts.com/motion/css-rotate-animation/rotate-transform-origin-pivot/

One element, one rotation angle, nine different pivots, laid out in a labelled three-by-three grid — every corner, every edge midpoint and the centre. Then the three cases you actually reach for: 50% 100% for a needle or pendulum, 0 50% for a hinged door, top center for a hanging sign. Most "my rotation looks wrong" bugs are this property.
## HTML
```html
<section class="rot-18" aria-labelledby="rot-18-h">
  <fieldset class="rot-18__theme">
    <legend class="rot-18__themelegend">Theme</legend>
    <input class="rot-18__themeinput" type="radio" name="rot-18-theme" id="rot-18-theme-auto" checked>
    <label class="rot-18__themeopt" for="rot-18-theme-auto">Auto</label>
    <input class="rot-18__themeinput" type="radio" name="rot-18-theme" id="rot-18-theme-light">
    <label class="rot-18__themeopt" for="rot-18-theme-light">Light</label>
    <input class="rot-18__themeinput" type="radio" name="rot-18-theme" id="rot-18-theme-dark">
    <label class="rot-18__themeopt" for="rot-18-theme-dark">Dark</label>
  </fieldset>

  <div class="rot-18__stage">
    <header class="rot-18__head">
      <p class="rot-18__eyebrow">Reference · transform-origin</p>
      <h2 class="rot-18__h" id="rot-18-h">Nine pivots. One angle. Nothing else changed.</h2>
      <p class="rot-18__sub">Every tile below takes the same <span class="rot-18__code">rotate(28deg)</span>. The dashed outline marks where each one started.</p>
    </header>

    <div class="rot-18__grid">
      <div class="rot-18__cell"><div class="rot-18__well"><span class="rot-18__ghost"></span><span class="rot-18__tile" style="--o: 0 0"></span></div><p class="rot-18__label">0 0<span class="rot-18__alias">top left</span></p></div>
      <div class="rot-18__cell"><div class="rot-18__well"><span class="rot-18__ghost"></span><span class="rot-18__tile" style="--o: 50% 0"></span></div><p class="rot-18__label">50% 0<span class="rot-18__alias">top center</span></p></div>
      <div class="rot-18__cell"><div class="rot-18__well"><span class="rot-18__ghost"></span><span class="rot-18__tile" style="--o: 100% 0"></span></div><p class="rot-18__label">100% 0<span class="rot-18__alias">top right</span></p></div>
      <div class="rot-18__cell"><div class="rot-18__well"><span class="rot-18__ghost"></span><span class="rot-18__tile" style="--o: 0 50%"></span></div><p class="rot-18__label">0 50%<span class="rot-18__alias">left center</span></p></div>
      <div class="rot-18__cell"><div class="rot-18__well"><span class="rot-18__ghost"></span><span class="rot-18__tile" style="--o: 50% 50%"></span></div><p class="rot-18__label">50% 50%<span class="rot-18__alias">the default</span></p></div>
      <div class="rot-18__cell"><div class="rot-18__well"><span class="rot-18__ghost"></span><span class="rot-18__tile" style="--o: 100% 50%"></span></div><p class="rot-18__label">100% 50%<span class="rot-18__alias">right center</span></p></div>
      <div class="rot-18__cell"><div class="rot-18__well"><span class="rot-18__ghost"></span><span class="rot-18__tile" style="--o: 0 100%"></span></div><p class="rot-18__label">0 100%<span class="rot-18__alias">bottom left</span></p></div>
      <div class="rot-18__cell"><div class="rot-18__well"><span class="rot-18__ghost"></span><span class="rot-18__tile" style="--o: 50% 100%"></span></div><p class="rot-18__label">50% 100%<span class="rot-18__alias">bottom center</span></p></div>
      <div class="rot-18__cell"><div class="rot-18__well"><span class="rot-18__ghost"></span><span class="rot-18__tile rot-18__tile--thick" style="--o: 50% 100%"></span></div><p class="rot-18__label">50% 100%<span class="rot-18__alias">thick border, same origin</span></p></div>
    </div>

    <div class="rot-18__applied">
      <article class="rot-18__case">
        <h3 class="rot-18__caseh">50% 100% · pendulum</h3>
        <div class="rot-18__casewell"><span class="rot-18__pend"></span></div>
        <p class="rot-18__casep">Pivots at the bottom edge. Needles, blades, wipers, anything hinged at its base.</p>
      </article>
      <article class="rot-18__case">
        <h3 class="rot-18__caseh">0 50% · hinge</h3>
        <div class="rot-18__casewell"><span class="rot-18__door"></span></div>
        <p class="rot-18__casep">Pivots at the left edge. Doors, book covers, panels that swing open from a spine.</p>
      </article>
      <article class="rot-18__case">
        <h3 class="rot-18__caseh">top center · hanging sign</h3>
        <div class="rot-18__casewell"><span class="rot-18__sign"></span></div>
        <p class="rot-18__casep">Pivots at the top. Pendant lamps, hanging signs, anything that dangles and settles.</p>
      </article>
    </div>

    <p class="rot-18__fine">Percentages resolve against the element's own size; keywords are aliases for them; absolute lengths are measured from the top-left corner and do not scale. All three resolve against the <em>border box</em>, which is why the ninth tile with the heavy rule pivots slightly differently from its twin.</p>
  </div>
</section>
```
## CSS
```css
.rot-18 {
  --page: #ffffff;
  --surface: #ffffff;
  --ink: #101010;
  --muted: #626262;
  --rule: #e2e2e2;
  --accent: #101010;
  --fill: #1a1a1a;
  --a: 28deg;
  --swing: 34deg;
  --dur: 700ms;
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
  .rot-18 {
    --fill: oklch(0.25 0 0);
  }
}

.rot-18 *,
.rot-18 *::before,
.rot-18 *::after {
  box-sizing: border-box;
}

.rot-18__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.5rem, 3.5vw, 2.25rem);
  padding: clamp(1rem, 3.5vw, 2.5rem);
  padding-block-start: 5.25rem;
}

.rot-18__head {
  max-inline-size: 40rem;
  min-inline-size: 0;
}

.rot-18__eyebrow {
  margin: 0 0 0.5rem;
  font-size: 0.6875rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.rot-18__h {
  margin: 0 0 0.5rem;
  font-size: clamp(1.25rem, 4.2vw, 1.875rem);
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.18;
}

.rot-18__sub {
  margin: 0;
  font-family: system-ui, sans-serif;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-18__code {
  font-size: 0.9em;
  padding: 0.05em 0.3em;
  background: #f0f0f0;
  border-radius: 0.2rem;
}

.rot-18__grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1px;
  inline-size: min(100%, 34rem);
  background: var(--rule);
  border: 1px solid var(--rule);
}

.rot-18__cell {
  min-inline-size: 0;
  display: grid;
  gap: 0.5rem;
  justify-items: center;
  padding: 0.75rem 0.5rem;
  background: var(--surface);
}

.rot-18__well {
  position: relative;
  inline-size: 100%;
  aspect-ratio: 1;
  display: grid;
  place-items: center;
}

.rot-18__ghost {
  position: absolute;
  inline-size: 52%;
  aspect-ratio: 1;
  border: 1px dashed color-mix(in srgb, var(--ink) 30%, transparent);
}

.rot-18__tile {
  position: absolute;
  inline-size: 52%;
  aspect-ratio: 1;
  background: var(--fill);
  transform-origin: var(--o, 50% 50%);
  transform: rotate(var(--a));
}

.rot-18__tile--thick {
  border: 0.35rem solid color-mix(in srgb, var(--ink) 45%, transparent);
}

.rot-18__label {
  margin: 0;
  display: grid;
  gap: 0.1rem;
  justify-items: center;
  font-size: 0.6875rem;
  text-align: center;
  min-inline-size: 0;
}

.rot-18__alias {
  font-family: system-ui, sans-serif;
  font-size: 0.625rem;
  color: var(--muted);
}

.rot-18__applied {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(12rem, 1fr));
  gap: 1rem;
  inline-size: min(100%, 46rem);
}

.rot-18__case {
  min-inline-size: 0;
  display: grid;
  gap: 0.6rem;
  padding: 0.875rem;
  border: 1px solid var(--rule);
}

.rot-18__caseh {
  margin: 0;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.01em;
}

.rot-18__casewell {
  position: relative;
  block-size: 6.5rem;
  display: grid;
  place-items: start center;
  overflow: hidden;
}

.rot-18__pend {
  inline-size: 0.4rem;
  block-size: 4.5rem;
  margin-block-start: 0.75rem;
  background: var(--fill);
  border-radius: 999px 999px 0.2rem 0.2rem;
  transform-origin: 50% 0;
  animation: rot-18-pend 3.2s ease-in-out infinite alternate;
}

.rot-18__door {
  inline-size: 3.25rem;
  block-size: 4.5rem;
  margin-block-start: 0.75rem;
  background: var(--fill);
  transform-origin: 0 50%;
  animation: rot-18-door 3.2s ease-in-out infinite alternate;
}

.rot-18__sign {
  inline-size: 4rem;
  block-size: 2.5rem;
  margin-block-start: 1.25rem;
  background: var(--fill);
  transform-origin: 50% 0;
  animation: rot-18-sign 3.2s ease-in-out infinite alternate;
}

@keyframes rot-18-pend {
  from {
    transform: rotate(calc(var(--swing) * -1));
  }

  to {
    transform: rotate(var(--swing));
  }
}

@keyframes rot-18-door {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(-42deg);
  }
}

@keyframes rot-18-sign {
  from {
    transform: rotate(-9deg);
  }

  to {
    transform: rotate(9deg);
  }
}

.rot-18__casep {
  margin: 0;
  font-family: system-ui, sans-serif;
  font-size: 0.8125rem;
  line-height: 1.6;
  color: var(--muted);
  min-inline-size: 0;
}

.rot-18__fine {
  inline-size: min(100%, 46rem);
  margin: 0;
  font-family: system-ui, sans-serif;
  font-size: 0.8125rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

@media (max-width: 26rem) {
  .rot-18__label {
    font-size: 0.625rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rot-18__pend {
    animation: none;
    transform: rotate(var(--swing));
  }

  .rot-18__door {
    animation: none;
    transform: rotate(-42deg);
  }

  .rot-18__sign {
    animation: none;
    transform: rotate(9deg);
  }
}

.rot-18__theme {
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

.rot-18__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-18__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-18__themeopt {
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

.rot-18__themeopt:hover {
  opacity: 0.85;
}

.rot-18__themeinput:checked + .rot-18__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-18__themeinput:focus-visible + .rot-18__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .rot-18__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-18__themeinput:checked + .rot-18__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: dark) {
  .rot-18:not(:has(#rot-18-theme-light:checked)) {
    --page: #0b0b0b;
    --surface: #111111;
    --ink: #f2f2f2;
    --muted: #9a9a9a;
    --rule: #262626;
    --fill: #e8e8e8;
  }

  .rot-18:not(:has(#rot-18-theme-light:checked)) .rot-18__code {
    background: #1d1d1d;
  }
}

@media (prefers-color-scheme: light) {
  .rot-18:has(#rot-18-theme-dark:checked) {
    --page: #0b0b0b;
    --surface: #111111;
    --ink: #f2f2f2;
    --muted: #9a9a9a;
    --rule: #262626;
    --fill: #e8e8e8;
  }

  .rot-18:has(#rot-18-theme-dark:checked) .rot-18__code {
    background: #1d1d1d;
  }
}

[data-theme="dark"] .rot-18:not(:has(#rot-18-theme-light:checked)) {
  --page: #0b0b0b;
  --surface: #111111;
  --ink: #f2f2f2;
  --muted: #9a9a9a;
  --rule: #262626;
  --fill: #e8e8e8;
}

[data-theme="dark"] .rot-18:not(:has(#rot-18-theme-light:checked)) .rot-18__code {
  background: #1d1d1d;
}

.rot-18:has(#rot-18-theme-dark:checked) {
  --page: #0b0b0b;
  --surface: #111111;
  --ink: #f2f2f2;
  --muted: #9a9a9a;
  --rule: #262626;
  --fill: #e8e8e8;
}

.rot-18:has(#rot-18-theme-dark:checked) .rot-18__code {
  background: #1d1d1d;
}

.rot-18:has(#rot-18-theme-light:checked) {
  --page: #ffffff;
  --surface: #ffffff;
  --ink: #101010;
  --muted: #626262;
  --rule: #e2e2e2;
  --fill: #1a1a1a;
}

.rot-18:has(#rot-18-theme-light:checked) .rot-18__code {
  background: #f0f0f0;
}
```
