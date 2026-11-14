---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/glow-on-svg-paths-and-stroke-elements/"
title: "Glow on SVG Paths and Stroke Elements"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "Glow on SVG has two routes with different trade-offs."
has_js: "false"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glow on SVG Paths and Stroke Elements
Source: https://codefronts.com/design-styles/css-neon/glow-on-svg-paths-and-stroke-elements/

Glow on SVG has two routes with different trade-offs. CSS filter: drop-shadow() on the element is simpler and inherits currentColor; a native <filter> with <feGaussianBlur> and <feMerge> allows a true multi-layer merge inside the SVG. One stroked route is lit both ways, labelled, including the filter-region trap that clips a glow at the edge.
## HTML
```html
<section class="nn-06" aria-labelledby="nn-06-heading">
  <div class="nn-06__stage">
    <div class="nn-06__theme">
      <input class="nn-06__tin" type="checkbox" id="nn-06-theme">
      <label class="nn-06__tlab" for="nn-06-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-06__head">
      <p class="nn-06__kicker">Two routes, one path</p>
      <h2 class="nn-06__heading" id="nn-06-heading">Lighting a stroke: CSS filter or native feMerge</h2>
      <p class="nn-06__sub">The same route geometry, the same hue. One is two lines of CSS; the other keeps the stroke crisp under three layers.</p>
    </header>

    <div class="nn-06__compare">
      <figure class="nn-06__cell">
        <figcaption class="nn-06__caption">
          <span class="nn-06__tag">CSS route</span>
          filter: drop-shadow() &times;2 &mdash; inherits currentColor, softens the stroke
        </figcaption>
        <div class="nn-06__well">
          <svg class="nn-06__svg nn-06__svg--css" viewBox="0 0 240 120" role="img" aria-label="Route line lit with two stacked CSS drop shadows">
            <path d="M12 96 C 60 96, 62 30, 108 30 S 176 96, 228 40" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
            <circle cx="12" cy="96" r="5" fill="currentColor"></circle>
            <circle cx="228" cy="40" r="5" fill="currentColor"></circle>
          </svg>
        </div>
        <p class="nn-06__mono">filter: drop-shadow(0 0 4px) drop-shadow(0 0 14px)</p>
      </figure>

      <figure class="nn-06__cell">
        <figcaption class="nn-06__caption">
          <span class="nn-06__tag nn-06__tag--good">Native route</span>
          feGaussianBlur &times;2 + feMerge &mdash; crisp stroke over its own blurs
        </figcaption>
        <div class="nn-06__well">
          <svg class="nn-06__svg" viewBox="0 0 240 120" role="img" aria-label="Route line lit with two blurred copies merged under the sharp stroke">
            <defs>
              <filter id="nn-06-merge-glow" x="-50%" y="-50%" width="200%" height="200%" filterUnits="objectBoundingBox">
                <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="nn06core"></feGaussianBlur>
                <feGaussianBlur in="SourceGraphic" stdDeviation="7" result="nn06halo"></feGaussianBlur>
                <feMerge>
                  <feMergeNode in="nn06halo"></feMergeNode>
                  <feMergeNode in="nn06halo"></feMergeNode>
                  <feMergeNode in="nn06core"></feMergeNode>
                  <feMergeNode in="SourceGraphic"></feMergeNode>
                </feMerge>
              </filter>
            </defs>
            <g filter="url(#nn-06-merge-glow)">
              <path d="M12 96 C 60 96, 62 30, 108 30 S 176 96, 228 40" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" vector-effect="non-scaling-stroke"></path>
              <circle cx="12" cy="96" r="5" fill="currentColor"></circle>
              <circle cx="228" cy="40" r="5" fill="currentColor"></circle>
            </g>
          </svg>
        </div>
        <p class="nn-06__mono">filter id="nn-06-merge-glow" x="-50%" width="200%"</p>
      </figure>
    </div>

    <div class="nn-06__trap">
      <div class="nn-06__trapcell">
        <p class="nn-06__tlabel"><span class="nn-06__tag nn-06__tag--bad">Region too small</span> default region, blur sliced off</p>
        <svg class="nn-06__svg nn-06__svg--sm" viewBox="0 0 160 90" role="img" aria-label="The same glow clipped into a straight edge by a default filter region">
          <defs>
            <filter id="nn-06-clipped-glow">
              <feGaussianBlur in="SourceGraphic" stdDeviation="6" result="nn06b"></feGaussianBlur>
              <feMerge>
                <feMergeNode in="nn06b"></feMergeNode>
                <feMergeNode in="SourceGraphic"></feMergeNode>
              </feMerge>
            </filter>
          </defs>
          <g filter="url(#nn-06-clipped-glow)">
            <path d="M16 68 L 78 24 L 144 60" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"></path>
          </g>
        </svg>
      </div>
      <div class="nn-06__trapcell">
        <p class="nn-06__tlabel"><span class="nn-06__tag nn-06__tag--good">Region widened</span> x="-50%" y="-50%" width="200%" height="200%"</p>
        <svg class="nn-06__svg nn-06__svg--sm" viewBox="0 0 160 90" role="img" aria-label="The same glow rendered fully with a widened filter region">
          <defs>
            <filter id="nn-06-wide-glow" x="-50%" y="-50%" width="200%" height="200%">
              <feGaussianBlur in="SourceGraphic" stdDeviation="6" result="nn06c"></feGaussianBlur>
              <feMerge>
                <feMergeNode in="nn06c"></feMergeNode>
                <feMergeNode in="SourceGraphic"></feMergeNode>
              </feMerge>
            </filter>
          </defs>
          <g filter="url(#nn-06-wide-glow)">
            <path d="M16 68 L 78 24 L 144 60" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round"></path>
          </g>
        </svg>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.nn-06 {
  --nn-06-bad: #f4a4a4;
  --nn-06-warn: #f0c88a;
  --nn-06-spec-neon: #6f8cff;
}

@media (prefers-color-scheme: light) {
  .nn-06 {
    --nn-06-bad: #a12a20;
    --nn-06-warn: #78490a;
  }

  .nn-06:has(#nn-06-theme:checked) {
    --nn-06-bad: #f4a4a4;
    --nn-06-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-06:has(#nn-06-theme:checked) {
    --nn-06-bad: #a12a20;
    --nn-06-warn: #78490a;
  }
}

.nn-06[data-theme="light"] {
  --nn-06-bad: #a12a20;
  --nn-06-warn: #78490a;
}

.nn-06 {
  --nn-06-spec-ink: #eaeeff;
  --nn-06-spec-dim: #939ec4;
}

.nn-06__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-06__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-06__tlab {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 44px;
  padding: 0 .8rem;
  border: 1px solid currentColor;
  font-size: .7rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  cursor: pointer;
  opacity: .7;
}

.nn-06__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-06__tlab:hover {
  opacity: 1;
}

.nn-06__tin:focus-visible + .nn-06__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-06:has(#nn-06-theme:checked) {
    --nn-06-bg: #0b1020;
    --nn-06-well: #101733;
    --nn-06-line: #212c52;
    --nn-06-ink: #eaeeff;
    --nn-06-muted: #939ec4;
    --nn-06-neon: #6f8cff;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-06:has(#nn-06-theme:checked) {
    --nn-06-bg: #e8eaf2;
    --nn-06-well: #161d38;
    --nn-06-line: #c3c9db;
    --nn-06-ink: #121629;
    --nn-06-muted: #4c5474;
    --nn-06-neon: #3b46a8;
  }
}

.nn-06 {
  --nn-06-hue: 262;
  --nn-06-bg: #0b1020;
  --nn-06-well: #101733;
  --nn-06-line: #212c52;
  --nn-06-ink: #eaeeff;
  --nn-06-muted: #939ec4;
  --nn-06-neon: #6f8cff;
  --nn-06-core: rgba(111, 140, 255, .9);
  --nn-06-halo: rgba(111, 140, 255, .45);
  --nn-06-font-display: "Gill Sans", "Trebuchet MS", Optima, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-06-bg);
  color: var(--nn-06-ink);
  font-family: system-ui, sans-serif;
}

.nn-06 *,
.nn-06 *::before,
.nn-06 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-06 {
    --nn-06-bg: oklch(18% 0.045 270);
    --nn-06-well: oklch(23% 0.055 270);
    --nn-06-line: oklch(33% 0.06 270);
    --nn-06-ink: oklch(96% 0.016 270);
    --nn-06-muted: oklch(74% 0.035 270);
    --nn-06-neon: oklch(76% 0.17 var(--nn-06-hue));
    --nn-06-core: oklch(78% 0.18 var(--nn-06-hue) / .9);
    --nn-06-halo: oklch(74% 0.17 var(--nn-06-hue) / .45);
  }
}

@media (prefers-color-scheme: light) {
  .nn-06 {
    --nn-06-bg: #e8eaf2;
    --nn-06-well: #161d38;
    --nn-06-line: #c3c9db;
    --nn-06-ink: #121629;
    --nn-06-muted: #4c5474;
    --nn-06-neon: #3b46a8;
  }
}

.nn-06[data-theme="light"] {
  --nn-06-bg: #e8eaf2;
  --nn-06-well: #161d38;
  --nn-06-line: #c3c9db;
  --nn-06-ink: #121629;
  --nn-06-muted: #4c5474;
  --nn-06-neon: #3b46a8;
}

.nn-06[data-theme="dark"] {
  --nn-06-bad: #f4a4a4;
  --nn-06-warn: #f0c88a;
  --nn-06-bg: #0b1020;
  --nn-06-well: #101733;
  --nn-06-line: #212c52;
  --nn-06-ink: #eaeeff;
  --nn-06-muted: #939ec4;
  --nn-06-neon: #6f8cff;
}

.nn-06__stage {
  max-width: 68rem;
  margin: 0 auto;
  padding: clamp(1.25rem, 4vw, 1.85rem) clamp(1rem, 4vw, 1.85rem) clamp(1.75rem, 5vw, 2.4rem);
  display: grid;
  gap: clamp(1.25rem, 3.5vw, 1.75rem);
}

.nn-06__kicker {
  margin: 0 0 .4rem;
  font-family: var(--nn-06-font-display);
  font-size: .78rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--nn-06-neon);
}

.nn-06__heading {
  margin: 0;
  font-family: var(--nn-06-font-display);
  font-size: clamp(1.4rem, 4.8vw, 2.05rem);
  font-weight: 500;
  letter-spacing: 0;
  text-wrap: balance;
}

.nn-06__sub {
  margin: .55rem 0 0;
  max-width: 42rem;
  font-size: .9rem;
  line-height: 1.6;
  color: var(--nn-06-muted);
  text-wrap: pretty;
}

.nn-06__compare {
  display: grid;
  gap: 1.15rem;
  grid-template-columns: 1fr;
}

@media (min-width: 54rem) {
  .nn-06__compare {
    grid-template-columns: 1fr 1fr;
  }
}

.nn-06__cell {
  margin: 0;
  display: grid;
  gap: .6rem;
  min-inline-size: 0;
}

.nn-06__caption {
  display: flex;
  align-items: center;
  gap: .55rem;
  flex-wrap: wrap;
  font-size: .78rem;
  color: var(--nn-06-muted);
  min-inline-size: 0;
}

.nn-06__tag {
  padding: .2rem .5rem;
  border-radius: .25rem;
  border: 1px solid var(--nn-06-line);
  font-family: var(--nn-06-font-display);
  font-size: .66rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--nn-06-muted);
}

.nn-06__tag--good {
  color: var(--nn-06-neon);
  border-color: color-mix(in srgb, var(--nn-06-neon) 45%, transparent);
}

.nn-06__tag--bad {
  color: var(--nn-06-bad);
  border-color: #472a34;
}

.nn-06__well {
  display: grid;
  place-items: center;
  padding: clamp(1.25rem, 5vw, 2.25rem);
  border-radius: .25rem;
  border: 1px solid var(--nn-06-line);
  background: var(--nn-06-well);
  overflow: hidden;
}

.nn-06__svg {
  width: 100%;
  max-width: 22rem;
  height: auto;
  display: block;
  color: var(--nn-06-spec-neon);
  overflow: visible;
}

.nn-06__svg--css {
  filter: drop-shadow(0 0 .25rem var(--nn-06-core)) drop-shadow(0 0 clamp(.6rem, 2.5vw, .9rem) var(--nn-06-halo));
}

.nn-06__svg--sm {
  max-width: 14rem;
}

.nn-06__mono {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: .68rem;
  line-height: 1.5;
  color: var(--nn-06-muted);
  overflow-wrap: anywhere;
}

.nn-06__trap {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr;
  padding: 1rem;
  border: 1px solid var(--nn-06-line);
  border-radius: .25rem;
}

@media (min-width: 40rem) {
  .nn-06__trap {
    grid-template-columns: 1fr 1fr;
  }
}

.nn-06__trapcell {
  display: grid;
  gap: .6rem;
  justify-items: start;
  min-inline-size: 0;
}

.nn-06__tlabel {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .5rem;
  flex-wrap: wrap;
  font-family: ui-monospace, Menlo, monospace;
  font-size: .68rem;
  color: var(--nn-06-muted);
  min-inline-size: 0;
}
```
