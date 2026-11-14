---
source: "codefronts"
url: "https://codefronts.com/components/css-svg-stroke-buttons/icon-plus-border-stroke-draw-together/"
title: "Icon Plus Border Stroke Draw Together"
section: "components"
category: "css-svg-stroke-buttons"
category_name: "CSS SVG Stroke Buttons"
description: "A seven-day forecast strip where each day is a ring and a hand-drawn weather glyph — and both draw at once."
has_js: "false"
---

Here's a working CSS SVG Stroke Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Icon Plus Border Stroke Draw Together
Source: https://codefronts.com/components/css-svg-stroke-buttons/icon-plus-border-stroke-draw-together/

A seven-day forecast strip where each day is a ring and a hand-drawn weather glyph — and both draw at once. The ring is hundreds of units long, the glyphs are a few dozen, so both carry pathLength="1" and one duration keeps them in step. Multi-stroke glyphs are split into separate paths so the shaft can lead the arrowhead by 60ms.
## HTML
```html
<section class="svgb-14">
  <input class="svgb-14__ti" type="checkbox" id="svgb-14-theme">
  <label class="svgb-14__toggle" for="svgb-14-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="svgb-14__sr">Switch colour scheme</span>
  </label>
  <div class="svgb-14__stage">
    <div class="svgb-14__wrap">
      <div class="svgb-14__head">
        <h1 class="svgb-14__place">Fjord House</h1>
        <p class="svgb-14__cond">Light rain easing after noon &middot; 11&deg;</p>
      </div>
      <div class="svgb-14__strip">
        <button class="svgb-14__day" type="button">
          <span class="svgb-14__dl">Mon</span>
          <span class="svgb-14__pod">
            <svg class="svgb-14__ring" viewBox="0 0 88 88" aria-hidden="true">
              <path class="svgb-14__base" d="M44.00 6.00A19 19 0 0 1 63.00 11.09A19 19 0 0 1 76.91 25.00A19 19 0 0 1 82.00 44.00A19 19 0 0 1 76.91 63.00A19 19 0 0 1 63.00 76.91A19 19 0 0 1 44.00 82.00A19 19 0 0 1 25.00 76.91A19 19 0 0 1 11.09 63.00A19 19 0 0 1 6.00 44.00A19 19 0 0 1 11.09 25.00A19 19 0 0 1 25.00 11.09A19 19 0 0 1 44.00 6.00Z" pathLength="1"/>
              <path class="svgb-14__draw" d="M44.00 6.00A19 19 0 0 1 63.00 11.09A19 19 0 0 1 76.91 25.00A19 19 0 0 1 82.00 44.00A19 19 0 0 1 76.91 63.00A19 19 0 0 1 63.00 76.91A19 19 0 0 1 44.00 82.00A19 19 0 0 1 25.00 76.91A19 19 0 0 1 11.09 63.00A19 19 0 0 1 6.00 44.00A19 19 0 0 1 11.09 25.00A19 19 0 0 1 25.00 11.09A19 19 0 0 1 44.00 6.00Z" pathLength="1"/>
            </svg>
            <svg class="svgb-14__icon" viewBox="0 0 32 32" aria-hidden="true">
              <circle class="svgb-14__gbase" cx="16" cy="16" r="7" pathLength="1"/>
              <path class="svgb-14__gbase" d="M16 3v3m0 20v3M3 16h3m20 0h3M6.8 6.8l2.1 2.1m14.3 14.3 2.1 2.1M25.2 6.8l-2.1 2.1M8.9 23.1l-2.1 2.1" pathLength="1"/>
              <circle class="svgb-14__draw svgb-14__draw--i1" cx="16" cy="16" r="7" pathLength="1"/>
              <path class="svgb-14__draw svgb-14__draw--i2" d="M16 3v3m0 20v3M3 16h3m20 0h3M6.8 6.8l2.1 2.1m14.3 14.3 2.1 2.1M25.2 6.8l-2.1 2.1M8.9 23.1l-2.1 2.1" pathLength="1"/>
            </svg>
          </span>
          <span class="svgb-14__temp">14&deg;</span>
        </button>
        <button class="svgb-14__day" type="button">
          <span class="svgb-14__dl">Tue</span>
          <span class="svgb-14__pod">
            <svg class="svgb-14__ring" viewBox="0 0 88 88" aria-hidden="true">
              <path class="svgb-14__base" d="M44.00 6.00A19 19 0 0 1 63.00 11.09A19 19 0 0 1 76.91 25.00A19 19 0 0 1 82.00 44.00A19 19 0 0 1 76.91 63.00A19 19 0 0 1 63.00 76.91A19 19 0 0 1 44.00 82.00A19 19 0 0 1 25.00 76.91A19 19 0 0 1 11.09 63.00A19 19 0 0 1 6.00 44.00A19 19 0 0 1 11.09 25.00A19 19 0 0 1 25.00 11.09A19 19 0 0 1 44.00 6.00Z" pathLength="1"/>
              <path class="svgb-14__draw" d="M44.00 6.00A19 19 0 0 1 63.00 11.09A19 19 0 0 1 76.91 25.00A19 19 0 0 1 82.00 44.00A19 19 0 0 1 76.91 63.00A19 19 0 0 1 63.00 76.91A19 19 0 0 1 44.00 82.00A19 19 0 0 1 25.00 76.91A19 19 0 0 1 11.09 63.00A19 19 0 0 1 6.00 44.00A19 19 0 0 1 11.09 25.00A19 19 0 0 1 25.00 11.09A19 19 0 0 1 44.00 6.00Z" pathLength="1"/>
            </svg>
            <svg class="svgb-14__icon" viewBox="0 0 32 32" aria-hidden="true">
              <path class="svgb-14__gbase" d="M9 19a5.5 5.5 0 0 1 .8-11A7 7 0 0 1 23 10.5a4.3 4.3 0 0 1 0 8.5Z" pathLength="1"/>
              <path class="svgb-14__gbase" d="M12 23l-1.5 4M18 23l-1.5 4M24 23l-1.5 4" pathLength="1"/>
              <path class="svgb-14__draw svgb-14__draw--i1" d="M9 19a5.5 5.5 0 0 1 .8-11A7 7 0 0 1 23 10.5a4.3 4.3 0 0 1 0 8.5Z" pathLength="1"/>
              <path class="svgb-14__draw svgb-14__draw--i2" d="M12 23l-1.5 4M18 23l-1.5 4M24 23l-1.5 4" pathLength="1"/>
            </svg>
          </span>
          <span class="svgb-14__temp">11&deg;</span>
        </button>
        <button class="svgb-14__day" type="button">
          <span class="svgb-14__dl">Wed</span>
          <span class="svgb-14__pod">
            <svg class="svgb-14__ring" viewBox="0 0 88 88" aria-hidden="true">
              <path class="svgb-14__base" d="M44.00 6.00A19 19 0 0 1 63.00 11.09A19 19 0 0 1 76.91 25.00A19 19 0 0 1 82.00 44.00A19 19 0 0 1 76.91 63.00A19 19 0 0 1 63.00 76.91A19 19 0 0 1 44.00 82.00A19 19 0 0 1 25.00 76.91A19 19 0 0 1 11.09 63.00A19 19 0 0 1 6.00 44.00A19 19 0 0 1 11.09 25.00A19 19 0 0 1 25.00 11.09A19 19 0 0 1 44.00 6.00Z" pathLength="1"/>
              <path class="svgb-14__draw" d="M44.00 6.00A19 19 0 0 1 63.00 11.09A19 19 0 0 1 76.91 25.00A19 19 0 0 1 82.00 44.00A19 19 0 0 1 76.91 63.00A19 19 0 0 1 63.00 76.91A19 19 0 0 1 44.00 82.00A19 19 0 0 1 25.00 76.91A19 19 0 0 1 11.09 63.00A19 19 0 0 1 6.00 44.00A19 19 0 0 1 11.09 25.00A19 19 0 0 1 25.00 11.09A19 19 0 0 1 44.00 6.00Z" pathLength="1"/>
            </svg>
            <svg class="svgb-14__icon" viewBox="0 0 32 32" aria-hidden="true">
              <path class="svgb-14__gbase" d="M3 12h15a4 4 0 1 0-4-4" pathLength="1"/>
              <path class="svgb-14__gbase" d="M3 20h20a4 4 0 1 1-4 4" pathLength="1"/>
              <path class="svgb-14__draw svgb-14__draw--i1" d="M3 12h15a4 4 0 1 0-4-4" pathLength="1"/>
              <path class="svgb-14__draw svgb-14__draw--i2" d="M3 20h20a4 4 0 1 1-4 4" pathLength="1"/>
            </svg>
          </span>
          <span class="svgb-14__temp">9&deg;</span>
        </button>
        <button class="svgb-14__day" type="button">
          <span class="svgb-14__dl">Thu</span>
          <span class="svgb-14__pod">
            <svg class="svgb-14__ring" viewBox="0 0 88 88" aria-hidden="true">
              <path class="svgb-14__base" d="M44.00 6.00A19 19 0 0 1 63.00 11.09A19 19 0 0 1 76.91 25.00A19 19 0 0 1 82.00 44.00A19 19 0 0 1 76.91 63.00A19 19 0 0 1 63.00 76.91A19 19 0 0 1 44.00 82.00A19 19 0 0 1 25.00 76.91A19 19 0 0 1 11.09 63.00A19 19 0 0 1 6.00 44.00A19 19 0 0 1 11.09 25.00A19 19 0 0 1 25.00 11.09A19 19 0 0 1 44.00 6.00Z" pathLength="1"/>
              <path class="svgb-14__draw" d="M44.00 6.00A19 19 0 0 1 63.00 11.09A19 19 0 0 1 76.91 25.00A19 19 0 0 1 82.00 44.00A19 19 0 0 1 76.91 63.00A19 19 0 0 1 63.00 76.91A19 19 0 0 1 44.00 82.00A19 19 0 0 1 25.00 76.91A19 19 0 0 1 11.09 63.00A19 19 0 0 1 6.00 44.00A19 19 0 0 1 11.09 25.00A19 19 0 0 1 25.00 11.09A19 19 0 0 1 44.00 6.00Z" pathLength="1"/>
            </svg>
            <svg class="svgb-14__icon" viewBox="0 0 32 32" aria-hidden="true">
              <path class="svgb-14__gbase" d="M16 5v22M6.5 10.5l19 11M25.5 10.5l-19 11" pathLength="1"/>
              <path class="svgb-14__gbase" d="M16 5l-3 3m3-3 3 3m-3 22-3-3m3 3 3-3" pathLength="1"/>
              <path class="svgb-14__draw svgb-14__draw--i1" d="M16 5v22M6.5 10.5l19 11M25.5 10.5l-19 11" pathLength="1"/>
              <path class="svgb-14__draw svgb-14__draw--i2" d="M16 5l-3 3m3-3 3 3m-3 22-3-3m3 3 3-3" pathLength="1"/>
            </svg>
          </span>
          <span class="svgb-14__temp">4&deg;</span>
        </button>
      </div>
      <div class="svgb-14__legend">
        <span class="svgb-14__lg">scalloped ring &middot; 12 lobes</span>
        <span class="svgb-14__lg">glyph 40&ndash;90 units</span>
        <span class="svgb-14__lg">pathLength 1 &middot; one duration</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap');

.svgb-14 {
  --svgb-14-bg: #eef1e9;
  --svgb-14-bg: oklch(0.945 0.015 130);
  --svgb-14-fg: #1a201a;
  --svgb-14-fg: oklch(0.225 0.015 145);
  --svgb-14-muted: #6b7568;
  --svgb-14-muted: oklch(0.545 0.018 140);
  --svgb-14-panel: #f8faf5;
  --svgb-14-panel: oklch(0.982 0.008 130);
  --svgb-14-rest: rgba(26, 32, 26, 0.14);
  --svgb-14-rest: oklch(0.225 0.015 145 / 0.14);
  --svgb-14-stroke: #2f6b4f;
  --svgb-14-stroke: oklch(0.47 0.10 158);
  --svgb-14-dur: 640ms;
  --svgb-14-ease: cubic-bezier(0.22, 1, 0.36, 1);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--svgb-14-bg);
  position: relative;
  color: var(--svgb-14-fg);
  font-family: 'Nunito', system-ui, sans-serif;
}

.svgb-14 *,
.svgb-14 *::before,
.svgb-14 *::after {
  box-sizing: border-box;
}

.svgb-14__stage {
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(22px, 5vw, 70px);
}

.svgb-14__wrap {
  width: 100%;
  max-width: 860px;
  display: flex;
  flex-direction: column;
  gap: clamp(20px, 3.5vw, 34px);
}

.svgb-14__head {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.svgb-14__place {
  margin: 0;
  font-size: clamp(28px, 4.6vw, 46px);
  font-weight: 600;
  letter-spacing: -0.03em;
}

.svgb-14__cond {
  margin: 0;
  font-size: 15px;
  color: var(--svgb-14-muted);
}

.svgb-14__strip {
  display: grid;
  gap: clamp(12px, 2vw, 20px);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 150px), 1fr));
}

.svgb-14__day {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
  padding: clamp(18px, 3vw, 26px) 12px;
  border: 0;
  border-radius: 22px;
  background: var(--svgb-14-panel);
  color: inherit;
  font: inherit;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  box-shadow: 0 1px 2px oklch(0 0 0 / 0.04);
  transition: transform 320ms var(--svgb-14-ease), box-shadow 320ms ease;
}

.svgb-14__day:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 26px -18px oklch(0 0 0 / 0.4);
}

.svgb-14__day:focus-visible {
  outline: 2px solid var(--svgb-14-stroke);
  outline-offset: 3px;
}

.svgb-14__dl {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 11px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--svgb-14-muted);
}

.svgb-14__pod {
  position: relative;
  inline-size: 88px;
  block-size: 88px;
  display: grid;
  place-items: center;
}

.svgb-14__ring {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-14__ring path,
.svgb-14__icon path,
.svgb-14__icon circle {
  fill: none;
}

.svgb-14__ring path {
  stroke-linejoin: round;
}

.svgb-14__base {
  stroke: var(--svgb-14-rest);
  stroke-width: 1.4px;
}

.svgb-14__gbase {
  stroke: var(--svgb-14-rest);
  stroke-width: 1.6px;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.svgb-14__icon {
  position: relative;
  inline-size: 40px;
  block-size: 40px;
  overflow: visible;
  color: var(--svgb-14-stroke);
}

.svgb-14__temp {
  font-size: 21px;
  font-weight: 600;
  letter-spacing: -0.02em;
  font-variant-numeric: tabular-nums;
  transition: color 300ms ease;
}

.svgb-14__day:hover .svgb-14__temp,
.svgb-14__day:focus-visible .svgb-14__temp {
  color: var(--svgb-14-stroke);
}

.svgb-14__draw {
  stroke: var(--svgb-14-stroke);
  stroke-width: 2px;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  transition: stroke-dashoffset var(--svgb-14-dur) var(--svgb-14-ease);
}

.svgb-14__icon .svgb-14__draw {
  stroke-width: 1.8px;
}

.svgb-14__draw--i2 {
  transition-delay: 60ms;
}

.svgb-14__day:hover .svgb-14__draw,
.svgb-14__day:focus-visible .svgb-14__draw {
  stroke-dashoffset: 0;
}

.svgb-14__legend {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.svgb-14__lg {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 10.5px;
  color: var(--svgb-14-muted);
}

.svgb-14__ti {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-14__toggle {
  position: absolute;
  z-index: 5;
  inset-block-start: 16px;
  inset-inline-end: 16px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab, currentColor 20%, transparent);
  background: color-mix(in oklab, currentColor 7%, transparent);
  color: inherit;
  cursor: pointer;
  transition: background 160ms ease, transform 160ms ease;
}

.svgb-14__toggle:hover {
  background: color-mix(in oklab, currentColor 14%, transparent);
}

.svgb-14__toggle:active {
  transform: scale(0.94);
}

.svgb-14__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 400ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.svgb-14__ti:checked + .svgb-14__toggle svg {
  transform: rotate(180deg);
}

.svgb-14__ti:focus-visible + .svgb-14__toggle {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.svgb-14__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.svgb-14:has(#svgb-14-theme:checked) {
  --svgb-14-bg: #101410;
  --svgb-14-bg: oklch(0.185 0.012 145);
  --svgb-14-fg: #eaf0e8;
  --svgb-14-fg: oklch(0.945 0.012 140);
  --svgb-14-muted: #8b978a;
  --svgb-14-muted: oklch(0.665 0.018 140);
  --svgb-14-panel: #171d17;
  --svgb-14-panel: oklch(0.235 0.014 145);
  --svgb-14-rest: rgba(234, 240, 232, 0.16);
  --svgb-14-rest: oklch(0.945 0.012 140 / 0.16);
  --svgb-14-stroke: #86e0ac;
  --svgb-14-stroke: oklch(0.86 0.13 155);
}

.svgb-14:has(#svgb-14-theme:checked) .svgb-14__day {
  box-shadow: inset 0 0 0 1px oklch(1 0 0 / 0.05);
}

.svgb-14:has(#svgb-14-theme:checked) .svgb-14__day:hover {
  box-shadow: inset 0 0 0 1px oklch(1 0 0 / 0.08), 0 14px 30px -22px #000;
}

@media (prefers-reduced-motion: reduce) {
  .svgb-14__draw {
    transition: none !important;
    transition-delay: 0ms !important;
    stroke-dasharray: none;
    stroke-dashoffset: 0;
    opacity: 0;
  }

  .svgb-14__day:hover .svgb-14__draw,
    .svgb-14__day:focus-visible .svgb-14__draw {
    opacity: 1;
  }

  .svgb-14__day,
    .svgb-14__temp,
    .svgb-14__toggle,
    .svgb-14__toggle svg {
    transition: none;
  }

  .svgb-14__day:hover {
    transform: none;
  }
}
```
