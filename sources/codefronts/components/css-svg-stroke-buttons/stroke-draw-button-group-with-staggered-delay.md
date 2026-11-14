---
source: "codefronts"
url: "https://codefronts.com/components/css-svg-stroke-buttons/stroke-draw-button-group-with-staggered-delay/"
title: "Stroke Draw Button Group with Staggered Delay"
section: "components"
category: "css-svg-stroke-buttons"
category_name: "CSS SVG Stroke Buttons"
description: "A departure board where hovering the platform rail sends the outlines out as a wave, and hovering one platform makes that platform the origin so the wave…"
has_js: "false"
---

Here's a working CSS SVG Stroke Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stroke Draw Button Group with Staggered Delay
Source: https://codefronts.com/components/css-svg-stroke-buttons/stroke-draw-button-group-with-staggered-delay/

A departure board where hovering the platform rail sends the outlines out as a wave, and hovering one platform makes that platform the origin so the wave spreads outward from your pointer in both directions. Each tab carries its index as --i; every delay in the file is calc() on that one number.
## HTML
```html
<section class="svgb-18">
  <input class="svgb-18__ti" type="checkbox" id="svgb-18-theme">
  <label class="svgb-18__toggle" for="svgb-18-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="svgb-18__sr">Switch colour scheme</span>
  </label>
  <div class="svgb-18__hall">
    <div class="svgb-18__board">
      <div class="svgb-18__brow svgb-18__brow--head">
        <span>Time</span><span>Destination</span><span>Plat</span><span>Status</span>
      </div>
      <div class="svgb-18__brow"><span>19:42</span><span>Gent Sint-Pieters</span><span>3</span><span class="svgb-18__ok">On time</span></div>
      <div class="svgb-18__brow"><span>19:55</span><span>Antwerpen Centraal</span><span>1</span><span class="svgb-18__ok">Boarding</span></div>
      <div class="svgb-18__brow"><span>20:04</span><span>Maastricht</span><span>6</span><span class="svgb-18__late">+8 min</span></div>
    </div>

    <div class="svgb-18__rail" role="group" aria-label="Platforms">
      <button class="svgb-18__tab" type="button" style="--i:0">
        <svg class="svgb-18__frame" viewBox="0 0 120 116" aria-hidden="true">
          <path class="svgb-18__base" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
          <path class="svgb-18__ink" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
        </svg>
        <span class="svgb-18__num">1</span>
        <span class="svgb-18__cap">Plat</span>
      </button>
      <button class="svgb-18__tab" type="button" style="--i:1">
        <svg class="svgb-18__frame" viewBox="0 0 120 116" aria-hidden="true">
          <path class="svgb-18__base" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
          <path class="svgb-18__ink" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
        </svg>
        <span class="svgb-18__num">2</span>
        <span class="svgb-18__cap">Plat</span>
      </button>
      <button class="svgb-18__tab" type="button" style="--i:2">
        <svg class="svgb-18__frame" viewBox="0 0 120 116" aria-hidden="true">
          <path class="svgb-18__base" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
          <path class="svgb-18__ink" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
        </svg>
        <span class="svgb-18__num">3</span>
        <span class="svgb-18__cap">Plat</span>
      </button>
      <button class="svgb-18__tab" type="button" style="--i:3">
        <svg class="svgb-18__frame" viewBox="0 0 120 116" aria-hidden="true">
          <path class="svgb-18__base" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
          <path class="svgb-18__ink" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
        </svg>
        <span class="svgb-18__num">4</span>
        <span class="svgb-18__cap">Plat</span>
      </button>
      <button class="svgb-18__tab" type="button" style="--i:4">
        <svg class="svgb-18__frame" viewBox="0 0 120 116" aria-hidden="true">
          <path class="svgb-18__base" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
          <path class="svgb-18__ink" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
        </svg>
        <span class="svgb-18__num">5</span>
        <span class="svgb-18__cap">Plat</span>
      </button>
      <button class="svgb-18__tab" type="button" style="--i:5">
        <svg class="svgb-18__frame" viewBox="0 0 120 116" aria-hidden="true">
          <path class="svgb-18__base" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
          <path class="svgb-18__ink" d="M4 20L24 4H96L116 20V112H4Z" pathLength="1"/>
        </svg>
        <span class="svgb-18__num">6</span>
        <span class="svgb-18__cap">Plat</span>
      </button>
    </div>
    <div class="svgb-18__legend">
      <span class="svgb-18__lg">hover the rail &rarr; index wave &middot; 70ms step</span>
      <span class="svgb-18__lg">hover one tab &rarr; wave from that tab</span>
    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

.svgb-18 {
  --svgb-18-bg: #0a0a09;
  --svgb-18-bg: oklch(0.145 0.004 90);
  --svgb-18-fg: #f0eee6;
  --svgb-18-fg: oklch(0.95 0.01 95);
  --svgb-18-muted: #8b887c;
  --svgb-18-muted: oklch(0.66 0.014 95);
  --svgb-18-rest: rgba(240, 238, 230, 0.14);
  --svgb-18-rest: oklch(0.95 0.01 95 / 0.14);
  --svgb-18-stroke: #ffc400;
  --svgb-18-stroke: oklch(0.85 0.18 90);
  --svgb-18-late: #ff7043;
  --svgb-18-late: oklch(0.72 0.17 42);
  --svgb-18-step: 70ms;
  --svgb-18-out: 40ms;
  --svgb-18-ease: cubic-bezier(0.22, 1, 0.36, 1);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--svgb-18-bg);
  position: relative;
  color: var(--svgb-18-fg);
  font-family: 'Barlow Condensed', system-ui, sans-serif;
}

.svgb-18 *,
.svgb-18 *::before,
.svgb-18 *::after {
  box-sizing: border-box;
}

.svgb-18__hall {
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: clamp(22px, 4vh, 42px);
  padding: clamp(20px, 5vw, 64px);
}

.svgb-18__board {
  width: 100%;
  max-width: 820px;
  display: flex;
  flex-direction: column;
}

.svgb-18__brow {
  display: grid;
  grid-template-columns: 74px 1fr 52px 110px;
  gap: 12px;
  align-items: baseline;
  padding-block: 11px;
  border-block-end: 1px solid var(--svgb-18-rest);
  font-size: clamp(17px, 2.4vw, 23px);
  letter-spacing: 0.02em;
  text-transform: uppercase;
  font-variant-numeric: tabular-nums;
}

.svgb-18__brow--head {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 10px;
  letter-spacing: 0.2em;
  color: var(--svgb-18-muted);
  text-transform: uppercase;
}

.svgb-18__brow span:nth-child(3) {
  color: var(--svgb-18-stroke);
}

.svgb-18__ok {
  color: var(--svgb-18-muted);
  font-size: 0.72em;
  letter-spacing: 0.14em;
}

.svgb-18__late {
  color: var(--svgb-18-late);
  font-size: 0.72em;
  letter-spacing: 0.14em;
}

.svgb-18__rail {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(8px, 1.6vw, 16px);
  justify-content: center;
}

.svgb-18__tab {
  position: relative;
  inline-size: 120px;
  block-size: 116px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2px;
  border: 0;
  padding: 0;
  background: transparent;
  color: inherit;
  font: inherit;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.svgb-18__tab:focus-visible {
  outline: 2px solid var(--svgb-18-stroke);
  outline-offset: 4px;
}

.svgb-18__num {
  position: relative;
  z-index: 1;
  order: 2;
  font-size: 46px;
  font-weight: 600;
  line-height: 1;
  font-variant-numeric: tabular-nums;
  transition: color 300ms ease, translate 380ms var(--svgb-18-ease);
}

.svgb-18__cap {
  position: relative;
  z-index: 1;
  order: 1;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 9.5px;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--svgb-18-muted);
}

.svgb-18__frame {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-18__frame path {
  fill: none;
  stroke-linejoin: miter;
}

.svgb-18__base {
  stroke: var(--svgb-18-rest);
  stroke-width: 1.4px;
}

.svgb-18__ink {
  stroke: var(--svgb-18-stroke);
  stroke-width: 2.2px;
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  transition: stroke-dashoffset 520ms var(--svgb-18-ease);
  transition-delay: calc((5 - var(--i, 0)) * var(--svgb-18-out));
}

.svgb-18__rail:hover .svgb-18__ink,
.svgb-18__rail:focus-within .svgb-18__ink {
  stroke-dashoffset: 0;
  transition-delay: calc(var(--i, 0) * var(--svgb-18-step));
}

.svgb-18__rail:hover .svgb-18__num,
.svgb-18__rail:focus-within .svgb-18__num {
  color: var(--svgb-18-stroke);
}

.svgb-18__tab:hover .svgb-18__ink {
  transition-delay: 0ms;
}

.svgb-18__tab:hover + .svgb-18__tab .svgb-18__ink {
  transition-delay: var(--svgb-18-step);
}

.svgb-18__tab:hover + .svgb-18__tab + .svgb-18__tab .svgb-18__ink {
  transition-delay: calc(var(--svgb-18-step) * 2);
}

.svgb-18__tab:hover + .svgb-18__tab + .svgb-18__tab + .svgb-18__tab .svgb-18__ink {
  transition-delay: calc(var(--svgb-18-step) * 3);
}

.svgb-18__tab:has(+ .svgb-18__tab:hover) .svgb-18__ink {
  transition-delay: var(--svgb-18-step);
}

.svgb-18__tab:has(+ .svgb-18__tab + .svgb-18__tab:hover) .svgb-18__ink {
  transition-delay: calc(var(--svgb-18-step) * 2);
}

.svgb-18__tab:has(+ .svgb-18__tab + .svgb-18__tab + .svgb-18__tab:hover) .svgb-18__ink {
  transition-delay: calc(var(--svgb-18-step) * 3);
}

.svgb-18__tab:hover .svgb-18__num {
  translate: 0 -3px;
}

.svgb-18__legend {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
  justify-content: center;
}

.svgb-18__lg {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 10.5px;
  color: var(--svgb-18-muted);
}

.svgb-18__ti {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-18__toggle {
  position: absolute;
  z-index: 5;
  inset-block-start: 16px;
  inset-inline-end: 16px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 2px;
  border: 1px solid color-mix(in oklab, currentColor 22%, transparent);
  background: color-mix(in oklab, currentColor 7%, transparent);
  color: inherit;
  cursor: pointer;
  transition: background 160ms ease, transform 160ms ease;
}

.svgb-18__toggle:hover {
  background: color-mix(in oklab, currentColor 14%, transparent);
}

.svgb-18__toggle:active {
  transform: scale(0.94);
}

.svgb-18__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 400ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.svgb-18__ti:checked + .svgb-18__toggle svg {
  transform: rotate(180deg);
}

.svgb-18__ti:focus-visible + .svgb-18__toggle {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.svgb-18__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.svgb-18:has(#svgb-18-theme:checked) {
  --svgb-18-bg: #f3f2ec;
  --svgb-18-bg: oklch(0.958 0.008 95);
  --svgb-18-fg: #14140f;
  --svgb-18-fg: oklch(0.195 0.008 95);
  --svgb-18-muted: #5d5b50;
  --svgb-18-muted: oklch(0.49 0.014 95);
  --svgb-18-rest: rgba(20, 20, 15, 0.16);
  --svgb-18-rest: oklch(0.195 0.008 95 / 0.16);
  --svgb-18-stroke: #7a5200;
  --svgb-18-stroke: oklch(0.49 0.13 84);
  --svgb-18-late: #a5401c;
  --svgb-18-late: oklch(0.48 0.16 42);
}

@media (prefers-reduced-motion: reduce) {
  .svgb-18__ink {
    transition: none !important;
    transition-delay: 0ms !important;
    stroke-dasharray: none;
    stroke-dashoffset: 0;
    opacity: 0;
  }

  .svgb-18__rail:hover .svgb-18__ink,
    .svgb-18__rail:focus-within .svgb-18__ink {
    opacity: 1;
  }

  .svgb-18__num,
    .svgb-18__toggle,
    .svgb-18__toggle svg {
    transition: none;
  }

  .svgb-18__tab:hover .svgb-18__num {
    translate: 0 0;
  }
}
```
