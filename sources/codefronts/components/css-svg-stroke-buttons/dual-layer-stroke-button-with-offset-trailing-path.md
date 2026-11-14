---
source: "codefronts"
url: "https://codefronts.com/components/css-svg-stroke-buttons/dual-layer-stroke-button-with-offset-trailing-path/"
title: "Dual Layer Stroke Button with Offset Trailing Path"
section: "components"
category: "css-svg-stroke-buttons"
category_name: "CSS SVG Stroke Buttons"
description: "A telemetry panel where the lap button is a skewed blade, not a rectangle, and its outline is drawn twice: a crisp 2px leader and a wide, blurred follower…"
has_js: "false"
---

Here's a working CSS SVG Stroke Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dual Layer Stroke Button with Offset Trailing Path
Source: https://codefronts.com/components/css-svg-stroke-buttons/dual-layer-stroke-button-with-offset-trailing-path/

A telemetry panel where the lap button is a skewed blade, not a rectangle, and its outline is drawn twice: a crisp 2px leader and a wide, blurred follower running 90ms behind it. The gap between them opens mid-draw and closes at the end, which the eye reads as speed rather than as two separate lines.
## HTML
```html
<section class="svgb-12">
  <input class="svgb-12__ti" type="checkbox" id="svgb-12-theme">
  <label class="svgb-12__toggle" for="svgb-12-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="svgb-12__sr">Switch colour scheme</span>
  </label>
  <div class="svgb-12__stage">
    <div class="svgb-12__panel">
      <div class="svgb-12__telem">
        <div class="svgb-12__t"><span class="svgb-12__tk">Lap</span><span class="svgb-12__tv">14</span></div>
        <div class="svgb-12__t"><span class="svgb-12__tk">Delta</span><span class="svgb-12__tv svgb-12__tv--good">-0.412</span></div>
        <div class="svgb-12__t"><span class="svgb-12__tk">Tyre</span><span class="svgb-12__tv">C3 &middot; 62%</span></div>
        <div class="svgb-12__t"><span class="svgb-12__tk">ERS</span><span class="svgb-12__tv">2.1 MJ</span></div>
      </div>

      <button class="svgb-12__blade" type="button">
        <svg class="svgb-12__frame" viewBox="0 0 340 78" aria-hidden="true">
          <path class="svgb-12__base" d="M26 3H337L314 75H3Z" pathLength="1" vector-effect="non-scaling-stroke"/>
          <path class="svgb-12__trail" d="M26 3H337L314 75H3Z" pathLength="1" vector-effect="non-scaling-stroke"/>
          <path class="svgb-12__lead" d="M26 3H337L314 75H3Z" pathLength="1" vector-effect="non-scaling-stroke"/>
        </svg>
        <span class="svgb-12__btext">Push lap</span>
      </button>

      <button class="svgb-12__blade svgb-12__blade--comet" type="button">
        <svg class="svgb-12__frame" viewBox="0 0 340 78" aria-hidden="true">
          <path class="svgb-12__base" d="M26 3H337L314 75H3Z" pathLength="1" vector-effect="non-scaling-stroke"/>
          <path class="svgb-12__comet" d="M26 3H337L314 75H3Z" pathLength="1" vector-effect="non-scaling-stroke"/>
          <path class="svgb-12__spark" d="M26 3H337L314 75H3Z" pathLength="1" vector-effect="non-scaling-stroke"/>
        </svg>
        <span class="svgb-12__btext">Deploy overtake</span>
      </button>

      <p class="svgb-12__note">leader 620ms &middot; trail 800ms + 90ms &middot; paint order: trail first</p>
    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@400;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

.svgb-12 {
  --svgb-12-bg: #08090a;
  --svgb-12-bg: oklch(0.145 0.002 250);
  --svgb-12-fg: #edeff1;
  --svgb-12-fg: oklch(0.95 0.003 250);
  --svgb-12-muted: #83878d;
  --svgb-12-muted: oklch(0.645 0.008 250);
  --svgb-12-rest: rgba(237, 239, 241, 0.14);
  --svgb-12-rest: oklch(0.95 0.003 250 / 0.14);
  --svgb-12-stroke: #00e5ff;
  --svgb-12-stroke: oklch(0.85 0.15 205);
  --svgb-12-good: #7cff8f;
  --svgb-12-good: oklch(0.89 0.18 145);
  --svgb-12-blend: screen;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--svgb-12-bg);
  color: var(--svgb-12-fg);
  font-family: 'Saira Condensed', system-ui, sans-serif;
  overflow: hidden;
}

.svgb-12 *,
.svgb-12 *::before,
.svgb-12 *::after {
  box-sizing: border-box;
}

.svgb-12::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(45deg, oklch(1 0 0 / 0.022) 0 2px, transparent 2px 5px), repeating-linear-gradient(-45deg, oklch(1 0 0 / 0.022) 0 2px, transparent 2px 5px), radial-gradient(70% 60% at 50% 40%, color-mix(in oklab, var(--svgb-12-stroke) 8%, transparent), transparent 70%);
}

.svgb-12__stage {
  position: relative;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(22px, 5vw, 70px);
}

.svgb-12__panel {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: clamp(16px, 3vw, 26px);
  width: 100%;
  max-width: 420px;
}

.svgb-12__telem {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px 20px;
  width: 100%;
}

.svgb-12__t {
  display: flex;
  flex-direction: column;
  gap: 2px;
  padding-block-end: 8px;
  border-block-end: 1px solid var(--svgb-12-rest);
}

.svgb-12__tk {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 9.5px;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--svgb-12-muted);
}

.svgb-12__tv {
  font-size: 26px;
  font-weight: 700;
  font-style: italic;
  letter-spacing: -0.01em;
  font-variant-numeric: tabular-nums;
}

.svgb-12__tv--good {
  color: var(--svgb-12-good);
}

.svgb-12__blade {
  position: relative;
  inline-size: min(340px, 92vw);
  block-size: 78px;
  display: grid;
  place-items: center;
  border: 0;
  padding: 0;
  background: transparent;
  color: inherit;
  font: inherit;
  font-size: 20px;
  font-weight: 600;
  font-style: italic;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  isolation: isolate;
}

.svgb-12__btext {
  position: relative;
  z-index: 2;
  transition: color 300ms ease, letter-spacing 400ms cubic-bezier(0.22, 1, 0.36, 1);
}

.svgb-12__blade:hover .svgb-12__btext,
.svgb-12__blade:focus-visible .svgb-12__btext {
  color: var(--svgb-12-stroke);
  letter-spacing: 0.16em;
}

.svgb-12__blade:focus-visible {
  outline: none;
  box-shadow: 0 0 0 3px color-mix(in oklab, var(--svgb-12-stroke) 34%, transparent);
}

.svgb-12__frame {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-12__frame path {
  fill: none;
  stroke-linejoin: miter;
}

.svgb-12__base {
  stroke: var(--svgb-12-rest);
  stroke-width: 1.4px;
}

.svgb-12__trail {
  stroke: var(--svgb-12-stroke);
  stroke-width: 7px;
  opacity: 0.36;
  color: var(--svgb-12-stroke);
  filter: drop-shadow(0 0 10px currentColor);
  mix-blend-mode: var(--svgb-12-blend);
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  transition: stroke-dashoffset 800ms cubic-bezier(0.22, 1, 0.36, 1) 90ms;
}

.svgb-12__lead {
  stroke: var(--svgb-12-stroke);
  stroke-width: 2px;
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  transition: stroke-dashoffset 620ms cubic-bezier(0.22, 1, 0.36, 1);
}

.svgb-12__blade:hover .svgb-12__trail,
.svgb-12__blade:focus-visible .svgb-12__trail,
.svgb-12__blade:hover .svgb-12__lead,
.svgb-12__blade:focus-visible .svgb-12__lead {
  stroke-dashoffset: 0;
}

.svgb-12__comet {
  stroke: var(--svgb-12-stroke);
  stroke-width: 6px;
  opacity: 0.32;
  color: var(--svgb-12-stroke);
  filter: drop-shadow(0 0 12px currentColor);
  mix-blend-mode: var(--svgb-12-blend);
  stroke-dasharray: 0.16 0.84;
  stroke-dashoffset: 0.16;
  transition: stroke-dashoffset 900ms linear;
}

.svgb-12__spark {
  stroke: var(--svgb-12-fg);
  stroke-width: 2.4px;
  stroke-dasharray: 0.045 0.955;
  stroke-dashoffset: 0.045;
  transition: stroke-dashoffset 900ms linear;
}

.svgb-12__blade--comet:hover .svgb-12__comet,
.svgb-12__blade--comet:focus-visible .svgb-12__comet {
  stroke-dashoffset: -0.84;
}

.svgb-12__blade--comet:hover .svgb-12__spark,
.svgb-12__blade--comet:focus-visible .svgb-12__spark {
  stroke-dashoffset: -0.955;
}

.svgb-12__note {
  margin: 0;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 10.5px;
  letter-spacing: 0.04em;
  color: var(--svgb-12-muted);
}

.svgb-12__ti {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-12__toggle {
  position: absolute;
  z-index: 5;
  inset-block-start: 16px;
  inset-inline-end: 16px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 4px;
  border: 1px solid color-mix(in oklab, currentColor 22%, transparent);
  background: color-mix(in oklab, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  transition: background 160ms ease, transform 160ms ease;
}

.svgb-12__toggle:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
}

.svgb-12__toggle:active {
  transform: scale(0.94);
}

.svgb-12__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 400ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.svgb-12__ti:checked + .svgb-12__toggle svg {
  transform: rotate(180deg);
}

.svgb-12__ti:focus-visible + .svgb-12__toggle {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.svgb-12__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.svgb-12:has(#svgb-12-theme:checked) {
  --svgb-12-bg: #f1f2f4;
  --svgb-12-bg: oklch(0.955 0.003 250);
  --svgb-12-fg: #101214;
  --svgb-12-fg: oklch(0.185 0.004 250);
  --svgb-12-muted: #555a60;
  --svgb-12-muted: oklch(0.49 0.008 250);
  --svgb-12-rest: rgba(16, 18, 20, 0.16);
  --svgb-12-rest: oklch(0.185 0.004 250 / 0.16);
  --svgb-12-stroke: #00647f;
  --svgb-12-stroke: oklch(0.45 0.11 215);
  --svgb-12-good: #0d6b2c;
  --svgb-12-good: oklch(0.46 0.14 148);
  --svgb-12-blend: multiply;
}

.svgb-12:has(#svgb-12-theme:checked)::before {
  background: repeating-linear-gradient(45deg, oklch(0 0 0 / 0.03) 0 2px, transparent 2px 5px), repeating-linear-gradient(-45deg, oklch(0 0 0 / 0.03) 0 2px, transparent 2px 5px);
}

@media (prefers-reduced-motion: reduce) {
  .svgb-12__trail,
    .svgb-12__lead,
    .svgb-12__comet,
    .svgb-12__spark,
    .svgb-12__btext {
    transition: none;
    filter: none;
  }

  .svgb-12__trail,
    .svgb-12__comet,
    .svgb-12__spark {
    opacity: 0;
  }

  .svgb-12__lead {
    stroke-dasharray: none;
    stroke-dashoffset: 0;
    opacity: 0;
  }

  .svgb-12__blade:hover .svgb-12__lead,
    .svgb-12__blade:focus-visible .svgb-12__lead {
    opacity: 1;
  }

  .svgb-12__toggle,
    .svgb-12__toggle svg {
    transition: none;
  }
}
```
