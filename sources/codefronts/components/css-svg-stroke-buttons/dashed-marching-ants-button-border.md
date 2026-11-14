---
source: "codefronts"
url: "https://codefronts.com/components/css-svg-stroke-buttons/dashed-marching-ants-button-border/"
title: "Dashed Marching Ants Button Border"
section: "components"
category: "css-svg-stroke-buttons"
category_name: "CSS SVG Stroke Buttons"
description: "Marching ants in the one place they were invented for: a crop selection over a real photograph, with corner handles, a rule-of-thirds grid and a dimension…"
has_js: "false"
---

Here's a working CSS SVG Stroke Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dashed Marching Ants Button Border
Source: https://codefronts.com/components/css-svg-stroke-buttons/dashed-marching-ants-button-border/

Marching ants in the one place they were invented for: a crop selection over a real photograph, with corner handles, a rule-of-thirds grid and a dimension readout. The selection marches permanently because it is a live region; the Apply button next to it marches only while you are pointing at it — the same 18-unit loop, two completely different jobs.
## HTML
```html
<section class="svgb-06">
  <input class="svgb-06__ti" type="checkbox" id="svgb-06-theme">
  <label class="svgb-06__toggle" for="svgb-06-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="svgb-06__sr">Switch colour scheme</span>
  </label>
  <div class="svgb-06__app">
    <div class="svgb-06__tools">
      <button class="svgb-06__tool svgb-06__tool--on" type="button" aria-label="Crop">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M6 2v14a2 2 0 0 0 2 2h14M2 6h14a2 2 0 0 1 2 2v14"/></svg>
      </button>
      <button class="svgb-06__tool" type="button" aria-label="Straighten">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M3 17 17 3m-6 0h6v6"/></svg>
      </button>
      <button class="svgb-06__tool" type="button" aria-label="Levels">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M4 19V9m5 10V5m5 14v-7m5 7V8"/></svg>
      </button>
      <button class="svgb-06__tool" type="button" aria-label="Mask">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="10" cy="12" r="7"/><circle cx="15" cy="12" r="7"/></svg>
      </button>
    </div>

    <div class="svgb-06__canvas">
      <img class="svgb-06__img" src="https://picsum.photos/seed/svgb06ridge/1400/950" alt="Mountain ridge at dusk" width="1400" height="950" loading="lazy" decoding="async">
      <div class="svgb-06__sel">
        <svg class="svgb-06__marq" viewBox="0 0 400 260" preserveAspectRatio="none" aria-hidden="true">
          <rect class="svgb-06__ants-b" x="1" y="1" width="398" height="258" vector-effect="non-scaling-stroke"/>
          <rect class="svgb-06__ants" x="1" y="1" width="398" height="258" vector-effect="non-scaling-stroke"/>
        </svg>
        <span class="svgb-06__thirds" aria-hidden="true"></span>
        <span class="svgb-06__h svgb-06__h--tl" aria-hidden="true"></span>
        <span class="svgb-06__h svgb-06__h--tr" aria-hidden="true"></span>
        <span class="svgb-06__h svgb-06__h--bl" aria-hidden="true"></span>
        <span class="svgb-06__h svgb-06__h--br" aria-hidden="true"></span>
        <span class="svgb-06__dims">1620 &times; 1053</span>
      </div>
    </div>

    <div class="svgb-06__bar">
      <span class="svgb-06__ratio">3 : 2</span>
      <div class="svgb-06__actions">
        <button class="svgb-06__btn svgb-06__btn--ghost" type="button">
          <svg class="svgb-06__frame" viewBox="0 0 120 46" aria-hidden="true">
            <rect class="svgb-06__bants" x="1" y="1" width="118" height="44" rx="10" vector-effect="non-scaling-stroke"/>
          </svg>
          <span class="svgb-06__label">Reset</span>
        </button>
        <button class="svgb-06__btn" type="button">
          <svg class="svgb-06__frame" viewBox="0 0 168 46" aria-hidden="true">
            <rect class="svgb-06__bants" x="1" y="1" width="166" height="44" rx="10" vector-effect="non-scaling-stroke"/>
          </svg>
          <span class="svgb-06__label">Apply crop</span>
        </button>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=JetBrains+Mono:wght@400;500&display=swap');

.svgb-06 {
  --svgb-06-bg: #121316;
  --svgb-06-bg: oklch(0.19 0.005 260);
  --svgb-06-chrome: #1b1d22;
  --svgb-06-chrome: oklch(0.245 0.008 260);
  --svgb-06-fg: #eceef1;
  --svgb-06-fg: oklch(0.95 0.004 260);
  --svgb-06-muted: #8b9099;
  --svgb-06-muted: oklch(0.67 0.011 260);
  --svgb-06-rest: rgba(236, 238, 241, 0.16);
  --svgb-06-rest: oklch(0.95 0.004 260 / 0.16);
  --svgb-06-stroke: #4ce0a0;
  --svgb-06-stroke: oklch(0.85 0.16 160);
  --svgb-06-speed: 700ms;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--svgb-06-bg);
  color: var(--svgb-06-fg);
  font-family: 'DM Sans', system-ui, sans-serif;
}

.svgb-06 *,
.svgb-06 *::before,
.svgb-06 *::after {
  box-sizing: border-box;
}

.svgb-06__app {
  min-height: 100svh;
  display: grid;
  grid-template-columns: 64px 1fr;
  grid-template-rows: 1fr auto;
  gap: 1px;
  background: color-mix(in oklab, var(--svgb-06-fg) 8%, transparent);
}

.svgb-06__tools {
  grid-row: 1 / span 2;
  display: flex;
  flex-direction: column;
  gap: 8px;
  align-items: center;
  padding: 14px 0;
  background: var(--svgb-06-chrome);
}

.svgb-06__tool {
  inline-size: 44px;
  block-size: 44px;
  display: grid;
  place-items: center;
  border: 0;
  border-radius: 10px;
  background: transparent;
  color: var(--svgb-06-muted);
  cursor: pointer;
  transition: background 160ms ease, color 160ms ease;
}

.svgb-06__tool:hover {
  background: color-mix(in oklab, var(--svgb-06-fg) 8%, transparent);
  color: var(--svgb-06-fg);
}

.svgb-06__tool--on {
  background: color-mix(in oklab, var(--svgb-06-stroke) 16%, transparent);
  color: var(--svgb-06-stroke);
}

.svgb-06__tool:focus-visible {
  outline: 2px solid var(--svgb-06-stroke);
  outline-offset: -2px;
}

.svgb-06__tool svg {
  inline-size: 20px;
  block-size: 20px;
}

.svgb-06__canvas {
  position: relative;
  display: grid;
  place-items: center;
  padding: clamp(20px, 4vw, 54px);
  background: repeating-conic-gradient(oklch(0.24 0 0) 0% 25%, oklch(0.21 0 0) 0% 50%) 0 0 / 22px 22px;
  overflow: hidden;
}

.svgb-06__img {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  opacity: 0.5;
  filter: saturate(0.8);
}

.svgb-06__sel {
  position: relative;
  inline-size: min(400px, 76vw);
  aspect-ratio: 400 / 260;
  box-shadow: 0 0 0 9999px oklch(0 0 0 / 0.55);
}

.svgb-06__marq {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-06__marq rect {
  fill: none;
}

@keyframes svgb-06-march {
  to {
    stroke-dashoffset: -18;
  }
}

.svgb-06__ants-b {
  stroke: oklch(0 0 0 / 0.75);
  stroke-width: 1.6px;
  stroke-dasharray: 10 8;
}

.svgb-06__ants {
  stroke: #fff;
  stroke-width: 1.6px;
  stroke-dasharray: 10 8;
  stroke-dashoffset: -9;
  animation: svgb-06-march var(--svgb-06-speed) linear infinite;
}

.svgb-06__thirds {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: linear-gradient(90deg, transparent 33.2%, oklch(1 0 0 / 0.3) 33.2% 33.4%, transparent 33.4%), linear-gradient(90deg, transparent 66.5%, oklch(1 0 0 / 0.3) 66.5% 66.7%, transparent 66.7%), linear-gradient(transparent 33.2%, oklch(1 0 0 / 0.3) 33.2% 33.4%, transparent 33.4%), linear-gradient(transparent 66.5%, oklch(1 0 0 / 0.3) 66.5% 66.7%, transparent 66.7%);
}

.svgb-06__h {
  position: absolute;
  inline-size: 13px;
  block-size: 13px;
  border: 2px solid #fff;
  background: oklch(0 0 0 / 0.4);
}

.svgb-06__h--tl {
  inset-block-start: -7px;
  inset-inline-start: -7px;
}

.svgb-06__h--tr {
  inset-block-start: -7px;
  inset-inline-end: -7px;
}

.svgb-06__h--bl {
  inset-block-end: -7px;
  inset-inline-start: -7px;
}

.svgb-06__h--br {
  inset-block-end: -7px;
  inset-inline-end: -7px;
}

.svgb-06__dims {
  position: absolute;
  inset-block-end: -34px;
  inset-inline-start: 0;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 11px;
  padding: 4px 8px;
  border-radius: 6px;
  background: oklch(0 0 0 / 0.6);
  color: #fff;
  font-variant-numeric: tabular-nums;
}

.svgb-06__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 14px clamp(14px, 3vw, 26px);
  background: var(--svgb-06-chrome);
}

.svgb-06__ratio {
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: 12px;
  color: var(--svgb-06-muted);
}

.svgb-06__actions {
  display: flex;
  gap: 12px;
}

.svgb-06__btn {
  position: relative;
  inline-size: 168px;
  block-size: 46px;
  display: grid;
  place-items: center;
  border: 0;
  padding: 0;
  border-radius: 10px;
  background: color-mix(in oklab, var(--svgb-06-stroke) 14%, transparent);
  color: inherit;
  font: inherit;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.svgb-06__btn--ghost {
  inline-size: 120px;
  background: color-mix(in oklab, var(--svgb-06-fg) 6%, transparent);
}

.svgb-06__btn:focus-visible {
  outline: 2px solid var(--svgb-06-stroke);
  outline-offset: 3px;
}

.svgb-06__label {
  position: relative;
  z-index: 1;
}

.svgb-06__frame {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-06__frame rect {
  fill: none;
}

.svgb-06__bants {
  stroke: var(--svgb-06-rest);
  stroke-width: 1.6px;
  stroke-dasharray: 10 8;
  animation: svgb-06-march var(--svgb-06-speed) linear infinite;
  animation-play-state: paused;
  transition: stroke 200ms ease;
}

.svgb-06__btn:hover .svgb-06__bants,
.svgb-06__btn:focus-visible .svgb-06__bants {
  animation-play-state: running;
  stroke: var(--svgb-06-stroke);
}

.svgb-06__ti {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-06__toggle {
  position: absolute;
  z-index: 5;
  inset-block-start: 14px;
  inset-inline-end: 14px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab, currentColor 20%, transparent);
  background: color-mix(in oklab, currentColor 12%, transparent);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  color: inherit;
  cursor: pointer;
  transition: background 160ms ease, transform 160ms ease;
}

.svgb-06__toggle:hover {
  background: color-mix(in oklab, currentColor 18%, transparent);
}

.svgb-06__toggle:active {
  transform: scale(0.94);
}

.svgb-06__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 400ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.svgb-06__ti:checked + .svgb-06__toggle svg {
  transform: rotate(180deg);
}

.svgb-06__ti:focus-visible + .svgb-06__toggle {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.svgb-06__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.svgb-06:has(#svgb-06-theme:checked) {
  --svgb-06-bg: #eceef0;
  --svgb-06-bg: oklch(0.945 0.004 260);
  --svgb-06-chrome: #ffffff;
  --svgb-06-chrome: oklch(1 0 0);
  --svgb-06-fg: #14171b;
  --svgb-06-fg: oklch(0.20 0.006 260);
  --svgb-06-muted: #5c626b;
  --svgb-06-muted: oklch(0.505 0.011 260);
  --svgb-06-rest: rgba(20, 23, 27, 0.18);
  --svgb-06-rest: oklch(0.20 0.006 260 / 0.18);
  --svgb-06-stroke: #0a7a52;
  --svgb-06-stroke: oklch(0.50 0.13 162);
}

.svgb-06:has(#svgb-06-theme:checked) .svgb-06__img {
  opacity: 0.85;
}

.svgb-06:has(#svgb-06-theme:checked) .svgb-06__sel {
  box-shadow: 0 0 0 9999px oklch(1 0 0 / 0.55);
}

.svgb-06:has(#svgb-06-theme:checked) .svgb-06__ants {
  stroke: #0b0d10;
}

.svgb-06:has(#svgb-06-theme:checked) .svgb-06__ants-b {
  stroke: oklch(1 0 0 / 0.85);
}

.svgb-06:has(#svgb-06-theme:checked) .svgb-06__h {
  border-color: #0b0d10;
  background: oklch(1 0 0 / 0.6);
}

.svgb-06:has(#svgb-06-theme:checked) .svgb-06__thirds {
  background: linear-gradient(90deg, transparent 33.2%, oklch(0 0 0 / 0.28) 33.2% 33.4%, transparent 33.4%), linear-gradient(90deg, transparent 66.5%, oklch(0 0 0 / 0.28) 66.5% 66.7%, transparent 66.7%), linear-gradient(transparent 33.2%, oklch(0 0 0 / 0.28) 33.2% 33.4%, transparent 33.4%), linear-gradient(transparent 66.5%, oklch(0 0 0 / 0.28) 66.5% 66.7%, transparent 66.7%);
}

@media (prefers-reduced-motion: reduce) {
  .svgb-06__ants,
    .svgb-06__bants {
    animation: none;
  }

  .svgb-06__ants {
    stroke-dashoffset: 0;
  }

  .svgb-06__btn:hover .svgb-06__bants {
    stroke-dasharray: 6 4;
  }

  .svgb-06__tool,
    .svgb-06__toggle,
    .svgb-06__toggle svg {
    transition: none;
  }
}
```
