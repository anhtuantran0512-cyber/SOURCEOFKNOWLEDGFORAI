---
source: "codefronts"
url: "https://codefronts.com/components/css-svg-stroke-buttons/two-path-split-border-draw-button/"
title: "Two Path Split Border Draw Button"
section: "components"
category: "css-svg-stroke-buttons"
category_name: "CSS SVG Stroke Buttons"
description: "A cinema ticket, notches and perforation included, where the outline is genuinely two paths: from the perforation each half runs its own way round the stub…"
has_js: "false"
---

Here's a working CSS SVG Stroke Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Two Path Split Border Draw Button
Source: https://codefronts.com/components/css-svg-stroke-buttons/two-path-split-border-draw-button/

A cinema ticket, notches and perforation included, where the outline is genuinely two paths: from the perforation each half runs its own way round the stub and both land together on the opposite edge. The shape is not a rectangle, so the halves are measured rather than guessed — 392 units each — and the seam is exactly where the ticket is meant to tear.
## HTML
```html
<section class="svgb-04">
  <input class="svgb-04__ti" type="checkbox" id="svgb-04-theme">
  <label class="svgb-04__toggle" for="svgb-04-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="svgb-04__sr">Switch colour scheme</span>
  </label>
  <div class="svgb-04__stage">
    <div class="svgb-04__marquee">
      <p class="svgb-04__now">Now showing</p>
      <h1 class="svgb-04__film">The Long<br>Exposure</h1>
      <p class="svgb-04__reel">70mm &middot; 142 min &middot; Screen 4 &middot; 20:45</p>

      <button class="svgb-04__ticket" type="button">
        <svg class="svgb-04__frame" viewBox="0 0 300 92" aria-hidden="true">
          <path class="svgb-04__base" d="M150 2H290A8 8 0 0 1 298 10V37A9 9 0 0 0 298 55V82A8 8 0 0 1 290 90H150" vector-effect="non-scaling-stroke"/>
          <path class="svgb-04__base" d="M150 2H10A8 8 0 0 0 2 10V37A9 9 0 0 1 2 55V82A8 8 0 0 0 10 90H150" vector-effect="non-scaling-stroke"/>
          <path class="svgb-04__perf" d="M150 12V80" vector-effect="non-scaling-stroke"/>
          <path class="svgb-04__half" d="M150 2H290A8 8 0 0 1 298 10V37A9 9 0 0 0 298 55V82A8 8 0 0 1 290 90H150" vector-effect="non-scaling-stroke"/>
          <path class="svgb-04__half" d="M150 2H10A8 8 0 0 0 2 10V37A9 9 0 0 1 2 55V82A8 8 0 0 0 10 90H150" vector-effect="non-scaling-stroke"/>
        </svg>
        <span class="svgb-04__stub">
          <span class="svgb-04__row">Seat</span>
          <span class="svgb-04__big">J-14</span>
        </span>
        <span class="svgb-04__stub svgb-04__stub--main">
          <span class="svgb-04__row">Admit one</span>
          <span class="svgb-04__big">Reserve</span>
        </span>
      </button>

      <div class="svgb-04__minor">
        <button class="svgb-04__chip" type="button">
          <svg class="svgb-04__cframe" viewBox="0 0 176 52" aria-hidden="true">
            <path class="svgb-04__base" d="M2 26V10A8 8 0 0 1 10 2H166A8 8 0 0 1 174 10V26" vector-effect="non-scaling-stroke"/>
            <path class="svgb-04__base" d="M2 26V42A8 8 0 0 0 10 50H166A8 8 0 0 0 174 42V26" vector-effect="non-scaling-stroke"/>
            <path class="svgb-04__chalf" d="M2 26V10A8 8 0 0 1 10 2H166A8 8 0 0 1 174 10V26" vector-effect="non-scaling-stroke"/>
            <path class="svgb-04__chalf" d="M2 26V42A8 8 0 0 0 10 50H166A8 8 0 0 0 174 42V26" vector-effect="non-scaling-stroke"/>
          </svg>
          <span class="svgb-04__chiptext">Add to calendar</span>
        </button>
        <span class="svgb-04__note">side seam &middot; 213.1 measured &rarr; 218 + 218</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Manrope:wght@400;500;700&family=IBM+Plex+Mono:wght@400&display=swap');

.svgb-04 {
  --svgb-04-bg: #1b0e0c;
  --svgb-04-bg: oklch(0.20 0.04 30);
  --svgb-04-fg: #f6ece0;
  --svgb-04-fg: oklch(0.95 0.02 70);
  --svgb-04-muted: #b09287;
  --svgb-04-muted: oklch(0.70 0.035 40);
  --svgb-04-rest: rgba(246, 236, 224, 0.2);
  --svgb-04-rest: oklch(0.95 0.02 70 / 0.2);
  --svgb-04-stroke: #ffb84d;
  --svgb-04-stroke: oklch(0.83 0.14 70);
  --svgb-04-half: 392;
  --svgb-04-chalf: 218;
  --svgb-04-dur: 620ms;
  --svgb-04-ease: cubic-bezier(0.33, 1, 0.68, 1);
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--svgb-04-bg);
  color: var(--svgb-04-fg);
  font-family: 'Manrope', system-ui, sans-serif;
  overflow: hidden;
}

.svgb-04 *,
.svgb-04 *::before,
.svgb-04 *::after {
  box-sizing: border-box;
}

.svgb-04::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(120% 80% at 50% -10%, color-mix(in oklab, var(--svgb-04-stroke) 16%, transparent), transparent 60%), repeating-linear-gradient(0deg, oklch(0 0 0 / 0.14) 0 1px, transparent 1px 4px);
}

.svgb-04__stage {
  position: relative;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(24px, 6vw, 72px);
}

.svgb-04__marquee {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: clamp(12px, 2vw, 18px);
  text-align: center;
}

.svgb-04__now {
  margin: 0;
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 11px;
  letter-spacing: 0.34em;
  text-transform: uppercase;
  color: var(--svgb-04-stroke);
}

.svgb-04__film {
  margin: 0;
  font-family: 'Anton', 'Archivo', system-ui, sans-serif;
  font-size: clamp(46px, 11vw, 116px);
  line-height: 0.88;
  letter-spacing: -0.02em;
  text-transform: uppercase;
}

.svgb-04__reel {
  margin: 0 0 clamp(10px, 2vw, 18px);
  font-size: 13px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--svgb-04-muted);
}

.svgb-04__ticket {
  position: relative;
  inline-size: min(300px, 92vw);
  block-size: 92px;
  display: flex;
  align-items: stretch;
  border: 0;
  padding: 0;
  background: color-mix(in oklab, var(--svgb-04-fg) 5%, transparent);
  color: inherit;
  font: inherit;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.svgb-04__ticket:focus-visible {
  outline: 2px solid var(--svgb-04-stroke);
  outline-offset: 5px;
}

.svgb-04__stub {
  position: relative;
  z-index: 1;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 4px;
}

.svgb-04__stub--main {
  flex: 1.4;
}

.svgb-04__row {
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 9.5px;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--svgb-04-muted);
}

.svgb-04__big {
  font-size: 19px;
  font-weight: 700;
  letter-spacing: -0.01em;
  transition: color 300ms ease;
}

.svgb-04__ticket:hover .svgb-04__big,
.svgb-04__ticket:focus-visible .svgb-04__big {
  color: var(--svgb-04-stroke);
}

.svgb-04__frame,
.svgb-04__cframe {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-04__frame path,
.svgb-04__cframe path {
  fill: none;
}

.svgb-04__base {
  stroke: var(--svgb-04-rest);
  stroke-width: 1.4px;
}

.svgb-04__perf {
  stroke: var(--svgb-04-rest);
  stroke-width: 1.4px;
  stroke-dasharray: 3 5;
  stroke-linecap: round;
}

.svgb-04__half {
  stroke: var(--svgb-04-stroke);
  stroke-width: 2px;
  stroke-linecap: butt;
  stroke-dasharray: var(--svgb-04-half);
  stroke-dashoffset: var(--svgb-04-half);
  transition: stroke-dashoffset var(--svgb-04-dur) var(--svgb-04-ease);
}

.svgb-04__ticket:hover .svgb-04__half,
.svgb-04__ticket:focus-visible .svgb-04__half {
  stroke-dashoffset: 0;
}

.svgb-04__ticket::after {
  content: '';
  position: absolute;
  inset-inline: 42%;
  inset-block-end: -7px;
  block-size: 2px;
  background: var(--svgb-04-stroke);
  opacity: 0;
  transform: scaleX(0.2);
  transition: opacity 200ms ease, transform 320ms var(--svgb-04-ease);
}

.svgb-04__ticket:hover::after,
.svgb-04__ticket:focus-visible::after {
  opacity: 0.9;
  transform: scaleX(1);
  transition-delay: var(--svgb-04-dur);
}

.svgb-04__minor {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  margin-block-start: clamp(14px, 3vw, 24px);
}

.svgb-04__chip {
  position: relative;
  inline-size: 176px;
  block-size: 52px;
  display: grid;
  place-items: center;
  border: 0;
  padding: 0;
  background: transparent;
  color: inherit;
  font: inherit;
  font-size: 13.5px;
  font-weight: 500;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.svgb-04__chip:focus-visible {
  outline: 2px solid var(--svgb-04-stroke);
  outline-offset: 4px;
}

.svgb-04__chiptext {
  position: relative;
  z-index: 1;
}

.svgb-04__chalf {
  stroke: var(--svgb-04-fg);
  stroke-width: 1.8px;
  stroke-linecap: butt;
  stroke-dasharray: var(--svgb-04-chalf);
  stroke-dashoffset: var(--svgb-04-chalf);
  transition: stroke-dashoffset 520ms var(--svgb-04-ease);
}

.svgb-04__chip:hover .svgb-04__chalf,
.svgb-04__chip:focus-visible .svgb-04__chalf {
  stroke-dashoffset: 0;
}

.svgb-04__note {
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 10.5px;
  letter-spacing: 0.08em;
  color: var(--svgb-04-muted);
}

.svgb-04__ti {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-04__toggle {
  position: absolute;
  z-index: 5;
  inset-block-start: 16px;
  inset-inline-end: 16px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab, currentColor 22%, transparent);
  background: color-mix(in oklab, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  transition: background 160ms ease, transform 160ms ease;
}

.svgb-04__toggle:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
}

.svgb-04__toggle:active {
  transform: scale(0.94);
}

.svgb-04__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 400ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.svgb-04__ti:checked + .svgb-04__toggle svg {
  transform: rotate(180deg);
}

.svgb-04__ti:focus-visible + .svgb-04__toggle {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.svgb-04__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.svgb-04:has(#svgb-04-theme:checked) {
  --svgb-04-bg: #f7efe4;
  --svgb-04-bg: oklch(0.955 0.02 75);
  --svgb-04-fg: #24110d;
  --svgb-04-fg: oklch(0.235 0.045 32);
  --svgb-04-muted: #7a5346;
  --svgb-04-muted: oklch(0.50 0.05 40);
  --svgb-04-rest: rgba(36, 17, 13, 0.24);
  --svgb-04-rest: oklch(0.235 0.045 32 / 0.24);
  --svgb-04-stroke: #b62d0e;
  --svgb-04-stroke: oklch(0.51 0.19 33);
}

@media (prefers-reduced-motion: reduce) {
  .svgb-04__half,
    .svgb-04__chalf {
    transition: none;
    stroke-dasharray: none;
    stroke-dashoffset: 0;
    opacity: 0;
  }

  .svgb-04__ticket:hover .svgb-04__half,
    .svgb-04__ticket:focus-visible .svgb-04__half,
    .svgb-04__chip:hover .svgb-04__chalf,
    .svgb-04__chip:focus-visible .svgb-04__chalf {
    opacity: 1;
  }

  .svgb-04__ticket::after,
    .svgb-04__big,
    .svgb-04__toggle,
    .svgb-04__toggle svg {
    transition: none;
  }
}
```
