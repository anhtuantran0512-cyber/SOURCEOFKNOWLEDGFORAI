---
source: "codefronts"
url: "https://codefronts.com/components/css-svg-stroke-buttons/corner-start-perimeter-draw-button/"
title: "Corner Start Perimeter Draw Button"
section: "components"
category: "css-svg-stroke-buttons"
category_name: "CSS SVG Stroke Buttons"
description: "A cyanotype drawing sheet where the border does not simply appear &mdash; it is measured."
has_js: "false"
---

Here's a working CSS SVG Stroke Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Corner Start Perimeter Draw Button
Source: https://codefronts.com/components/css-svg-stroke-buttons/corner-start-perimeter-draw-button/

A cyanotype drawing sheet where the border does not simply appear &mdash; it is measured. A crosshair head leaves the origin corner, rides the perimeter on a CSS motion path, and unrolls a surveyor&rsquo;s tape of tick marks behind it while the hairline inks the edge underneath. Because the head, the tape and the ink all read the same d attribute, moving one M command moves all three origins at once &mdash; which is the whole point of the sheet.
## HTML
```html
<section class="svgb-03">
  <input class="svgb-03__ti" type="checkbox" id="svgb-03-theme">
  <label class="svgb-03__toggle" for="svgb-03-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="svgb-03__sr">Switch colour scheme</span>
  </label>
  <div class="svgb-03__sheet">
    <div class="svgb-03__plate">
      <div class="svgb-03__cell">
        <button class="svgb-03__btn" type="button">
          <svg class="svgb-03__frame" viewBox="0 0 240 64" aria-hidden="true">
            <defs>
              <mask id="svgb-03-m-tl" maskUnits="userSpaceOnUse" x="-30" y="-30" width="300" height="124">
                <path class="svgb-03__reveal" d="M-8 -8H248V72H-8V-8"/>
              </mask>
            </defs>
            <path class="svgb-03__base" d="M2 2H238V62H2Z" vector-effect="non-scaling-stroke"/>
            <g mask="url(#svgb-03-m-tl)">
              <path class="svgb-03__ticks" d="M-8 -8H248V72H-8V-8"/>
            </g>
            <path class="svgb-03__ink" d="M2 2H238V62H2V2" vector-effect="non-scaling-stroke"/>
            <g class="svgb-03__mark"><path d="M2 -8V12M-8 2H12" vector-effect="non-scaling-stroke"/></g>
            <g class="svgb-03__pen svgb-03__pen--tl">
              <path d="M0 -6V6M-6 0H6" vector-effect="non-scaling-stroke"/>
              <circle r="2.4"/>
            </g>
          </svg>
          <span class="svgb-03__label">Elevation A</span>
        </button>
        <span class="svgb-03__meta">P1 2,2 &middot; CW &middot; 592</span>
      </div>
      <div class="svgb-03__cell">
        <button class="svgb-03__btn" type="button">
          <svg class="svgb-03__frame" viewBox="0 0 240 64" aria-hidden="true">
            <defs>
              <mask id="svgb-03-m-tr" maskUnits="userSpaceOnUse" x="-30" y="-30" width="300" height="124">
                <path class="svgb-03__reveal" d="M248 -8V72H-8V-8H248"/>
              </mask>
            </defs>
            <path class="svgb-03__base" d="M2 2H238V62H2Z" vector-effect="non-scaling-stroke"/>
            <g mask="url(#svgb-03-m-tr)">
              <path class="svgb-03__ticks" d="M248 -8V72H-8V-8H248"/>
            </g>
            <path class="svgb-03__ink" d="M238 2V62H2V2H238" vector-effect="non-scaling-stroke"/>
            <g class="svgb-03__mark"><path d="M238 -8V12M228 2H248" vector-effect="non-scaling-stroke"/></g>
            <g class="svgb-03__pen svgb-03__pen--tr">
              <path d="M0 -6V6M-6 0H6" vector-effect="non-scaling-stroke"/>
              <circle r="2.4"/>
            </g>
          </svg>
          <span class="svgb-03__label">Elevation B</span>
        </button>
        <span class="svgb-03__meta">P1 238,2 &middot; CW &middot; 592</span>
      </div>
      <div class="svgb-03__cell">
        <button class="svgb-03__btn" type="button">
          <svg class="svgb-03__frame" viewBox="0 0 240 64" aria-hidden="true">
            <defs>
              <mask id="svgb-03-m-br" maskUnits="userSpaceOnUse" x="-30" y="-30" width="300" height="124">
                <path class="svgb-03__reveal" d="M248 72H-8V-8H248V72"/>
              </mask>
            </defs>
            <path class="svgb-03__base" d="M2 2H238V62H2Z" vector-effect="non-scaling-stroke"/>
            <g mask="url(#svgb-03-m-br)">
              <path class="svgb-03__ticks" d="M248 72H-8V-8H248V72"/>
            </g>
            <path class="svgb-03__ink" d="M238 62H2V2H238V62" vector-effect="non-scaling-stroke"/>
            <g class="svgb-03__mark"><path d="M238 52V72M228 62H248" vector-effect="non-scaling-stroke"/></g>
            <g class="svgb-03__pen svgb-03__pen--br">
              <path d="M0 -6V6M-6 0H6" vector-effect="non-scaling-stroke"/>
              <circle r="2.4"/>
            </g>
          </svg>
          <span class="svgb-03__label">Section C</span>
        </button>
        <span class="svgb-03__meta">P1 238,62 &middot; CCW &middot; 592</span>
      </div>
      <div class="svgb-03__cell">
        <button class="svgb-03__btn svgb-03__btn--rev" type="button">
          <svg class="svgb-03__frame" viewBox="0 0 240 64" aria-hidden="true">
            <defs>
              <mask id="svgb-03-m-bl" maskUnits="userSpaceOnUse" x="-30" y="-30" width="300" height="124">
                <path class="svgb-03__reveal" d="M-8 72V-8H248V72H-8"/>
              </mask>
            </defs>
            <path class="svgb-03__base" d="M2 2H238V62H2Z" vector-effect="non-scaling-stroke"/>
            <g mask="url(#svgb-03-m-bl)">
              <path class="svgb-03__ticks" d="M-8 72V-8H248V72H-8"/>
            </g>
            <path class="svgb-03__ink" d="M2 62V2H238V62H2" vector-effect="non-scaling-stroke"/>
            <g class="svgb-03__mark"><path d="M2 52V72M-8 62H12" vector-effect="non-scaling-stroke"/></g>
            <g class="svgb-03__pen svgb-03__pen--bl">
              <path d="M0 -6V6M-6 0H6" vector-effect="non-scaling-stroke"/>
              <circle r="2.4"/>
            </g>
          </svg>
          <span class="svgb-03__label">Section D</span>
        </button>
        <span class="svgb-03__meta">P1 2,62 &middot; negative offset</span>
      </div>
    </div>
    <div class="svgb-03__block">
      <span class="svgb-03__bk">Drawing</span><span class="svgb-03__bv">Corner-start perimeter &middot; surveyor&rsquo;s tape</span>
      <span class="svgb-03__bk">Tape</span><span class="svgb-03__bv">1&times;7 tick dash on a 672-unit offset path, mask-revealed</span>
      <span class="svgb-03__bk">Head</span><span class="svgb-03__bv">offset-path rides the same path from P1</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

.svgb-03 {
  --svgb-03-bg: #0d2233;
  --svgb-03-bg: oklch(0.27 0.055 245);
  --svgb-03-fg: #dcecf7;
  --svgb-03-fg: oklch(0.92 0.025 230);
  --svgb-03-muted: #8fb3c9;
  --svgb-03-muted: oklch(0.735 0.04 235);
  --svgb-03-grid: rgba(220, 236, 247, 0.09);
  --svgb-03-grid: oklch(0.92 0.025 230 / 0.09);
  --svgb-03-rest: rgba(220, 236, 247, 0.26);
  --svgb-03-rest: oklch(0.92 0.025 230 / 0.26);
  --svgb-03-stroke: #ffffff;
  --svgb-03-stroke: oklch(0.99 0.01 230);
  --svgb-03-peri: 592;
  --svgb-03-tape: 672;
  --svgb-03-dur: 760ms;
  --svgb-03-ease: cubic-bezier(0.36, 0, 0.24, 1);
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--svgb-03-bg);
  color: var(--svgb-03-fg);
  font-family: 'Archivo', system-ui, sans-serif;
}

.svgb-03 *,
.svgb-03 *::before,
.svgb-03 *::after {
  box-sizing: border-box;
}

.svgb-03::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: linear-gradient(var(--svgb-03-grid) 1px, transparent 1px) 0 0 / 100% 24px, linear-gradient(90deg, var(--svgb-03-grid) 1px, transparent 1px) 0 0 / 24px 100%, linear-gradient(var(--svgb-03-grid) 1px, transparent 1px) 0 0 / 100% 120px, linear-gradient(90deg, var(--svgb-03-grid) 1px, transparent 1px) 0 0 / 120px 100%;
}

.svgb-03__sheet {
  position: relative;
  min-height: 100svh;
  display: grid;
  align-content: center;
  justify-items: center;
  gap: clamp(24px, 5vh, 48px);
  padding: clamp(22px, 5vw, 70px);
}

.svgb-03__plate {
  display: grid;
  gap: clamp(34px, 5vw, 62px);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 290px), 1fr));
  width: 100%;
  max-width: 800px;
  padding: clamp(36px, 5.5vw, 60px);
  border: 1px solid var(--svgb-03-rest);
  outline: 1px solid var(--svgb-03-grid);
  outline-offset: 5px;
}

.svgb-03__cell {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.svgb-03__meta {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 10.5px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--svgb-03-muted);
}

.svgb-03__btn {
  position: relative;
  inline-size: 100%;
  max-inline-size: 240px;
  block-size: 64px;
  display: grid;
  place-items: center;
  border: 0;
  padding: 0;
  border-radius: 0;
  background: color-mix(in oklab, var(--svgb-03-fg) 5%, transparent);
  color: inherit;
  font: inherit;
  font-size: 15px;
  font-weight: 500;
  letter-spacing: 0.01em;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.svgb-03__label {
  position: relative;
  z-index: 1;
  transition: letter-spacing 400ms ease, color 300ms ease;
}

.svgb-03__btn:hover .svgb-03__label,
.svgb-03__btn:focus-visible .svgb-03__label {
  letter-spacing: 0.06em;
  color: var(--svgb-03-stroke);
}

.svgb-03__btn:focus-visible {
  outline: 1px dashed var(--svgb-03-stroke);
  outline-offset: 16px;
}

.svgb-03__frame {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-03__frame path {
  fill: none;
}

.svgb-03__base {
  stroke: var(--svgb-03-rest);
  stroke-width: 1px;
}
/* the tape: a 1-unit dash on a 7-unit-wide stroke reads as a perpendicular tick */

.svgb-03__ticks {
  stroke: var(--svgb-03-stroke);
  stroke-width: 7;
  stroke-dasharray: 1 7;
  stroke-linecap: butt;
  opacity: 0.5;
  pointer-events: none;
}
/* the mask that wipes the tape on from P1 */

.svgb-03__reveal {
  fill: none;
  stroke: #fff;
  stroke-width: 18;
  stroke-linecap: butt;
  stroke-dasharray: var(--svgb-03-tape);
  stroke-dashoffset: var(--svgb-03-tape);
  transition: stroke-dashoffset var(--svgb-03-dur) var(--svgb-03-ease);
}

.svgb-03__btn:hover .svgb-03__reveal,
.svgb-03__btn:focus-visible .svgb-03__reveal {
  stroke-dashoffset: 0;
}

.svgb-03__ink {
  stroke: var(--svgb-03-stroke);
  stroke-width: 1.6px;
  stroke-dasharray: var(--svgb-03-peri);
  stroke-dashoffset: var(--svgb-03-peri);
  transition: stroke-dashoffset var(--svgb-03-dur) var(--svgb-03-ease);
}

.svgb-03__btn--rev .svgb-03__ink {
  stroke-dashoffset: calc(var(--svgb-03-peri) * -1);
}

.svgb-03__btn--rev .svgb-03__reveal {
  stroke-dashoffset: calc(var(--svgb-03-tape) * -1);
}

.svgb-03__btn:hover .svgb-03__ink,
.svgb-03__btn:focus-visible .svgb-03__ink {
  stroke-dashoffset: 0;
}

.svgb-03__mark path {
  stroke: var(--svgb-03-stroke);
  stroke-width: 1px;
  opacity: 0.5;
}

.svgb-03__mark {
  opacity: 0.85;
  transition: opacity 300ms ease;
}

.svgb-03__btn:hover .svgb-03__mark {
  opacity: 1;
}
/* the head: rides the identical path data, so it always leaves from P1 */

.svgb-03__pen {
  opacity: 0;
}

@supports (offset-path: path('M0 0H1')) {
  .svgb-03__pen {
    offset-distance: 0%;
    offset-rotate: 0deg;
    transition: offset-distance var(--svgb-03-dur) var(--svgb-03-ease), opacity 220ms ease calc(var(--svgb-03-dur) - 220ms);
  }

  .svgb-03__pen path {
    stroke: var(--svgb-03-stroke);
    stroke-width: 1.2px;
  }

  .svgb-03__pen circle {
    fill: var(--svgb-03-stroke);
    stroke: none;
  }

  .svgb-03__btn:hover .svgb-03__pen,
    .svgb-03__btn:focus-visible .svgb-03__pen {
    opacity: 1;
    offset-distance: 100%;
    transition-delay: 0s, 0s;
  }

  .svgb-03__pen--tl {
    offset-path: path('M-8 -8H248V72H-8V-8');
  }

  .svgb-03__pen--tr {
    offset-path: path('M248 -8V72H-8V-8H248');
  }

  .svgb-03__pen--br {
    offset-path: path('M248 72H-8V-8H248V72');
  }

  .svgb-03__pen--bl {
    offset-path: path('M-8 72V-8H248V72H-8');
  }

  .svgb-03__btn--rev .svgb-03__pen {
    offset-distance: 100%;
  }

  .svgb-03__btn--rev:hover .svgb-03__pen,
    .svgb-03__btn--rev:focus-visible .svgb-03__pen {
    offset-distance: 0%;
  }
}

.svgb-03__block {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 4px 18px;
  width: 100%;
  max-width: 800px;
  padding: 14px 18px;
  border: 1px solid var(--svgb-03-rest);
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 10.5px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.svgb-03__bk {
  color: var(--svgb-03-muted);
}

.svgb-03__bv {
  color: var(--svgb-03-fg);
}

.svgb-03__ti {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-03__toggle {
  position: absolute;
  z-index: 5;
  inset-block-start: 16px;
  inset-inline-end: 16px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid color-mix(in oklab, currentColor 26%, transparent);
  background: color-mix(in oklab, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  transition: background 160ms ease, transform 160ms ease;
}

.svgb-03__toggle:hover {
  background: color-mix(in oklab, currentColor 16%, transparent);
}

.svgb-03__toggle:active {
  transform: scale(0.94);
}

.svgb-03__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 400ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.svgb-03__ti:checked + .svgb-03__toggle svg {
  transform: rotate(180deg);
}

.svgb-03__ti:focus-visible + .svgb-03__toggle {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.svgb-03__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.svgb-03:has(#svgb-03-theme:checked) {
  --svgb-03-bg: #eef3f7;
  --svgb-03-bg: oklch(0.955 0.008 235);
  --svgb-03-fg: #0e2a3d;
  --svgb-03-fg: oklch(0.29 0.05 240);
  --svgb-03-muted: #4e6d80;
  --svgb-03-muted: oklch(0.505 0.04 235);
  --svgb-03-grid: rgba(14, 42, 61, 0.09);
  --svgb-03-grid: oklch(0.29 0.05 240 / 0.09);
  --svgb-03-rest: rgba(14, 42, 61, 0.28);
  --svgb-03-rest: oklch(0.29 0.05 240 / 0.28);
  --svgb-03-stroke: #0a3f8f;
  --svgb-03-stroke: oklch(0.40 0.18 262);
}

@media (prefers-reduced-motion: reduce) {
  .svgb-03__ink,
    .svgb-03__reveal {
    transition: none;
    stroke-dasharray: none;
    stroke-dashoffset: 0;
  }

  .svgb-03__ink {
    opacity: 0;
  }

  .svgb-03__btn:hover .svgb-03__ink,
    .svgb-03__btn:focus-visible .svgb-03__ink {
    opacity: 1;
  }

  .svgb-03__ticks {
    opacity: 0;
  }

  .svgb-03__btn:hover .svgb-03__ticks,
    .svgb-03__btn:focus-visible .svgb-03__ticks {
    opacity: 0.5;
  }

  .svgb-03__pen {
    display: none;
  }

  .svgb-03__label,
    .svgb-03__mark,
    .svgb-03__toggle,
    .svgb-03__toggle svg {
    transition: none;
  }
}
```
