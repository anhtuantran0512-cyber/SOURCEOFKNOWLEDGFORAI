---
source: "codefronts"
url: "https://codefronts.com/components/css-svg-stroke-buttons/stroke-draw-button-with-pathlength-normalization/"
title: "Stroke Draw Button with pathLength Normalization"
section: "components"
category: "css-svg-stroke-buttons"
category_name: "CSS SVG Stroke Buttons"
description: "An arcade menu where every entry is a different silhouette — hexagon, diamond, shield, octagon and ring — and every one is animated by the same three lines…"
has_js: "false"
---

Here's a working CSS SVG Stroke Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stroke Draw Button with pathLength Normalization
Source: https://codefronts.com/components/css-svg-stroke-buttons/stroke-draw-button-with-pathlength-normalization/

An arcade menu where every entry is a different silhouette — hexagon, diamond, shield, octagon and ring — and every one is animated by the same three lines of CSS. pathLength="1" tells the renderer to treat each path as one unit long, so stroke-dasharray: 1 is a complete outline whether the geometry is 96 units round or 600.
## HTML
```html
<section class="svgb-11">
  <input class="svgb-11__ti" type="checkbox" id="svgb-11-theme">
  <label class="svgb-11__toggle" for="svgb-11-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="svgb-11__sr">Switch colour scheme</span>
  </label>
  <div class="svgb-11__cab">
    <p class="svgb-11__coin">Insert coin &middot; 1 credit</p>
    <h1 class="svgb-11__logo">Vector<span>Runner</span></h1>
    <div class="svgb-11__menu">
      <button class="svgb-11__item svgb-11__item--hex" type="button">
        <svg class="svgb-11__frame" viewBox="0 0 200 96" aria-hidden="true">
          <path class="svgb-11__base" d="M40 4H160L196 48L160 92H40L4 48Z" pathLength="1"/>
          <path class="svgb-11__ink" d="M40 4H160L196 48L160 92H40L4 48Z" pathLength="1"/>
        </svg>
        <span class="svgb-11__label">Start</span>
      </button>
      <button class="svgb-11__item svgb-11__item--dia" type="button">
        <svg class="svgb-11__frame" viewBox="0 0 160 96" aria-hidden="true">
          <path class="svgb-11__base" d="M80 4L156 48L80 92L4 48Z" pathLength="1"/>
          <path class="svgb-11__ink" d="M80 4L156 48L80 92L4 48Z" pathLength="1"/>
        </svg>
        <span class="svgb-11__label">Co-op</span>
      </button>
      <button class="svgb-11__item svgb-11__item--shd" type="button">
        <svg class="svgb-11__frame" viewBox="0 0 160 104" aria-hidden="true">
          <path class="svgb-11__base" d="M80 4L152 24V58C152 82 118 96 80 100C42 96 8 82 8 58V24Z" pathLength="1"/>
          <path class="svgb-11__ink" d="M80 4L152 24V58C152 82 118 96 80 100C42 96 8 82 8 58V24Z" pathLength="1"/>
        </svg>
        <span class="svgb-11__label">Armory</span>
      </button>
      <button class="svgb-11__item svgb-11__item--oct" type="button">
        <svg class="svgb-11__frame" viewBox="0 0 200 96" aria-hidden="true">
          <path class="svgb-11__base" d="M28 4H172L196 28V68L172 92H28L4 68V28Z" pathLength="1"/>
          <path class="svgb-11__ink" d="M28 4H172L196 28V68L172 92H28L4 68V28Z" pathLength="1"/>
        </svg>
        <span class="svgb-11__label">Options</span>
      </button>
      <button class="svgb-11__item svgb-11__item--ring" type="button" aria-label="Quit to attract mode">
        <svg class="svgb-11__frame" viewBox="0 0 96 96" aria-hidden="true">
          <circle class="svgb-11__base" cx="48" cy="48" r="44" pathLength="1"/>
          <circle class="svgb-11__ink" cx="48" cy="48" r="44" pathLength="1"/>
        </svg>
        <span class="svgb-11__label svgb-11__label--x">&times;</span>
      </button>
    </div>
    <div class="svgb-11__hud">
      <span class="svgb-11__hk">dasharray</span><span class="svgb-11__hv">1</span>
      <span class="svgb-11__hk">dashoffset</span><span class="svgb-11__hv">1 &rarr; 0</span>
      <span class="svgb-11__hk">shapes</span><span class="svgb-11__hv">5</span>
      <span class="svgb-11__hk">constants</span><span class="svgb-11__hv">0</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

.svgb-11 {
  --svgb-11-bg: #06070d;
  --svgb-11-bg: oklch(0.145 0.02 265);
  --svgb-11-fg: #e8f6ff;
  --svgb-11-fg: oklch(0.96 0.02 220);
  --svgb-11-muted: #7d90a8;
  --svgb-11-muted: oklch(0.645 0.035 250);
  --svgb-11-rest: rgba(232, 246, 255, 0.16);
  --svgb-11-rest: oklch(0.96 0.02 220 / 0.16);
  --svgb-11-stroke: #22f0ff;
  --svgb-11-stroke: oklch(0.88 0.16 200);
  --svgb-11-alt: #ff3ecb;
  --svgb-11-alt: oklch(0.72 0.26 340);
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--svgb-11-bg);
  color: var(--svgb-11-fg);
  font-family: 'Chakra Petch', system-ui, sans-serif;
  overflow: hidden;
}

.svgb-11 *,
.svgb-11 *::before,
.svgb-11 *::after {
  box-sizing: border-box;
}

.svgb-11::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: 2;
  pointer-events: none;
  background: repeating-linear-gradient(0deg, oklch(0 0 0 / 0.34) 0 1px, transparent 1px 3px);
  opacity: 0.55;
}

.svgb-11::after {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(60% 50% at 50% 0%, color-mix(in oklab, var(--svgb-11-stroke) 14%, transparent), transparent 65%), radial-gradient(70% 60% at 50% 110%, color-mix(in oklab, var(--svgb-11-alt) 14%, transparent), transparent 65%);
}

.svgb-11__cab {
  position: relative;
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: clamp(14px, 3vh, 30px);
  padding: clamp(22px, 5vw, 70px);
  text-align: center;
}

.svgb-11__coin {
  margin: 0;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 11px;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--svgb-11-alt);
  animation: svgb-11-blink 1.8s steps(1, end) infinite;
}

@keyframes svgb-11-blink {
  0%,
    60% {
    opacity: 1;
  }

  61%,
    100% {
    opacity: 0.25;
  }
}

.svgb-11__logo {
  margin: 0;
  font-size: clamp(40px, 9vw, 96px);
  font-weight: 700;
  letter-spacing: -0.02em;
  text-transform: uppercase;
  line-height: 0.95;
  text-shadow: 0 0 22px color-mix(in oklab, var(--svgb-11-stroke) 55%, transparent);
}

.svgb-11__logo span {
  color: var(--svgb-11-stroke);
}

.svgb-11__menu {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(12px, 2.4vw, 26px);
  justify-content: center;
  align-items: center;
}

.svgb-11__item {
  position: relative;
  display: grid;
  place-items: center;
  border: 0;
  padding: 0;
  background: transparent;
  color: inherit;
  font: inherit;
  font-size: 15px;
  font-weight: 600;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  block-size: 96px;
}

.svgb-11__item--hex,
.svgb-11__item--oct {
  inline-size: 200px;
}

.svgb-11__item--dia {
  inline-size: 160px;
}

.svgb-11__item--shd {
  inline-size: 160px;
  block-size: 104px;
}

.svgb-11__item--ring {
  inline-size: 96px;
}

.svgb-11__label {
  position: relative;
  z-index: 1;
  transition: color 260ms ease, text-shadow 260ms ease;
}

.svgb-11__label--x {
  font-size: 26px;
  letter-spacing: 0;
}

.svgb-11__item:hover .svgb-11__label,
.svgb-11__item:focus-visible .svgb-11__label {
  color: var(--svgb-11-stroke);
  text-shadow: 0 0 14px color-mix(in oklab, var(--svgb-11-stroke) 70%, transparent);
}

.svgb-11__item:focus-visible {
  outline: 1px dashed var(--svgb-11-alt);
  outline-offset: 6px;
}

.svgb-11__frame {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-11__frame path,
.svgb-11__frame circle {
  fill: none;
}

.svgb-11__base {
  stroke: var(--svgb-11-rest);
  stroke-width: 1.6px;
}
/* one rule, five silhouettes */

.svgb-11__ink {
  stroke: var(--svgb-11-stroke);
  stroke-width: 2.4px;
  stroke-linecap: butt;
  stroke-linejoin: miter;
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  transition: stroke-dashoffset 620ms cubic-bezier(0.22, 1, 0.36, 1);
  filter: drop-shadow(0 0 7px color-mix(in oklab, var(--svgb-11-stroke) 60%, transparent));
}

.svgb-11__item:hover .svgb-11__ink,
.svgb-11__item:focus-visible .svgb-11__ink {
  stroke-dashoffset: 0;
}

.svgb-11__item--dia .svgb-11__ink,
.svgb-11__item--ring .svgb-11__ink {
  stroke: var(--svgb-11-alt);
  filter: drop-shadow(0 0 7px color-mix(in oklab, var(--svgb-11-alt) 60%, transparent));
}

.svgb-11__item--dia:hover .svgb-11__label,
.svgb-11__item--dia:focus-visible .svgb-11__label,
.svgb-11__item--ring:hover .svgb-11__label,
.svgb-11__item--ring:focus-visible .svgb-11__label {
  color: var(--svgb-11-alt);
  text-shadow: 0 0 14px color-mix(in oklab, var(--svgb-11-alt) 70%, transparent);
}

.svgb-11__hud {
  display: grid;
  grid-template-columns: repeat(4, auto);
  gap: 4px 14px;
  padding: 12px 18px;
  border: 1px solid var(--svgb-11-rest);
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 10.5px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.svgb-11__hk {
  color: var(--svgb-11-muted);
}

.svgb-11__hv {
  color: var(--svgb-11-stroke);
}

.svgb-11__ti {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-11__toggle {
  position: absolute;
  z-index: 5;
  inset-block-start: 16px;
  inset-inline-end: 16px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid color-mix(in oklab, currentColor 24%, transparent);
  background: color-mix(in oklab, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  transition: background 160ms ease, transform 160ms ease;
}

.svgb-11__toggle:hover {
  background: color-mix(in oklab, currentColor 16%, transparent);
}

.svgb-11__toggle:active {
  transform: scale(0.94);
}

.svgb-11__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 400ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.svgb-11__ti:checked + .svgb-11__toggle svg {
  transform: rotate(180deg);
}

.svgb-11__ti:focus-visible + .svgb-11__toggle {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.svgb-11__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.svgb-11:has(#svgb-11-theme:checked) {
  --svgb-11-bg: #eef2f6;
  --svgb-11-bg: oklch(0.95 0.008 235);
  --svgb-11-fg: #0b1220;
  --svgb-11-fg: oklch(0.19 0.025 260);
  --svgb-11-muted: #4f5f75;
  --svgb-11-muted: oklch(0.49 0.03 255);
  --svgb-11-rest: rgba(11, 18, 32, 0.2);
  --svgb-11-rest: oklch(0.19 0.025 260 / 0.2);
  --svgb-11-stroke: #006d8f;
  --svgb-11-stroke: oklch(0.47 0.11 218);
  --svgb-11-alt: #9c1173;
  --svgb-11-alt: oklch(0.44 0.20 340);
}

.svgb-11:has(#svgb-11-theme:checked)::before {
  opacity: 0.18;
}

.svgb-11:has(#svgb-11-theme:checked) .svgb-11__logo {
  text-shadow: none;
}

.svgb-11:has(#svgb-11-theme:checked) .svgb-11__ink {
  filter: none;
}

@media (prefers-reduced-motion: reduce) {
  .svgb-11__ink {
    transition: none;
    stroke-dasharray: none;
    stroke-dashoffset: 0;
    opacity: 0;
  }

  .svgb-11__item:hover .svgb-11__ink,
    .svgb-11__item:focus-visible .svgb-11__ink {
    opacity: 1;
  }

  .svgb-11__coin {
    animation: none;
  }

  .svgb-11__label,
    .svgb-11__toggle,
    .svgb-11__toggle svg {
    transition: none;
  }
}
```
