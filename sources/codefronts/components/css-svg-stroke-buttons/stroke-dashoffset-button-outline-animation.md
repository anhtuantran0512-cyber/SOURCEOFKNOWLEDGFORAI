---
source: "codefronts"
url: "https://codefronts.com/components/css-svg-stroke-buttons/stroke-dashoffset-button-outline-animation/"
title: "Stroke Dashoffset Button Outline Animation"
section: "components"
category: "css-svg-stroke-buttons"
category_name: "CSS SVG Stroke Buttons"
description: "A studio transport bar, where the dash offset does three different jobs on three circular pads: play draws its ring once, record sends a single 40-unit…"
has_js: "false"
---

Here's a working CSS SVG Stroke Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stroke Dashoffset Button Outline Animation
Source: https://codefronts.com/components/css-svg-stroke-buttons/stroke-dashoffset-button-outline-animation/

A studio transport bar, where the dash offset does three different jobs on three circular pads: play draws its ring once, record sends a single 40-unit runner orbiting forever, and the loop pad splits the circumference into a two-segment chase. The scrub line underneath uses the same property travelling in a straight line — same maths, no perimeter, no corners.
## HTML
```html
<section class="svgb-02">
  <input class="svgb-02__ti" type="checkbox" id="svgb-02-theme">
  <label class="svgb-02__toggle" for="svgb-02-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="svgb-02__sr">Switch colour scheme</span>
  </label>
  <div class="svgb-02__stage">
    <div class="svgb-02__rack">
      <div class="svgb-02__head">
        <span class="svgb-02__take">Take 07</span>
        <span class="svgb-02__tc">00:02:41:18</span>
      </div>
      <div class="svgb-02__wave" aria-hidden="true">
        <span style="--h:22%"></span><span style="--h:54%"></span><span style="--h:38%"></span><span style="--h:76%"></span>
        <span style="--h:92%"></span><span style="--h:61%"></span><span style="--h:44%"></span><span style="--h:83%"></span>
        <span style="--h:35%"></span><span style="--h:67%"></span><span style="--h:96%"></span><span style="--h:52%"></span>
        <span style="--h:29%"></span><span style="--h:71%"></span><span style="--h:48%"></span><span style="--h:88%"></span>
        <span style="--h:33%"></span><span style="--h:59%"></span><span style="--h:41%"></span><span style="--h:24%"></span>
      </div>
      <div class="svgb-02__scrub">
        <svg class="svgb-02__sline" viewBox="0 0 560 6" preserveAspectRatio="none" aria-hidden="true">
          <line class="svgb-02__strack" x1="1" y1="3" x2="559" y2="3" vector-effect="non-scaling-stroke"/>
          <line class="svgb-02__srun" x1="1" y1="3" x2="559" y2="3" vector-effect="non-scaling-stroke"/>
        </svg>
      </div>
      <div class="svgb-02__pads">
        <div class="svgb-02__pad">
          <button class="svgb-02__pd svgb-02__pd--draw" type="button" aria-label="Play take">
            <svg class="svgb-02__ring" viewBox="0 0 120 120" aria-hidden="true">
              <circle class="svgb-02__base" cx="60" cy="60" r="57"/>
              <circle class="svgb-02__ink" cx="60" cy="60" r="57"/>
            </svg>
            <svg class="svgb-02__glyph" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6.5 18 12l-9 5.5Z"/></svg>
          </button>
          <span class="svgb-02__cap">dasharray 360<br>offset &rarr; 0</span>
        </div>
        <div class="svgb-02__pad">
          <button class="svgb-02__pd svgb-02__pd--run" type="button" aria-label="Arm recording">
            <svg class="svgb-02__ring" viewBox="0 0 120 120" aria-hidden="true">
              <circle class="svgb-02__base" cx="60" cy="60" r="57"/>
              <circle class="svgb-02__ink" cx="60" cy="60" r="57"/>
            </svg>
            <svg class="svgb-02__glyph" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="5.5"/></svg>
          </button>
          <span class="svgb-02__cap">dasharray 40 320<br>offset &rarr; -360</span>
        </div>
        <div class="svgb-02__pad">
          <button class="svgb-02__pd svgb-02__pd--chase" type="button" aria-label="Loop region">
            <svg class="svgb-02__ring" viewBox="0 0 120 120" aria-hidden="true">
              <circle class="svgb-02__base" cx="60" cy="60" r="57"/>
              <circle class="svgb-02__ink" cx="60" cy="60" r="57"/>
            </svg>
            <svg class="svgb-02__glyph" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 9.5A5 5 0 0 1 10 5h8m0 0-3-3m3 3-3 3M19 14.5A5 5 0 0 1 14 19H6m0 0 3 3m-3-3 3-3"/></svg>
          </button>
          <span class="svgb-02__cap">dasharray 180 180<br>offset &rarr; -360</span>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap');

@property --svgb-02-phase {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}

.svgb-02 {
  --svgb-02-bg: #0a0a0b;
  --svgb-02-bg: oklch(0.15 0.002 60);
  --svgb-02-fg: #f2efe9;
  --svgb-02-fg: oklch(0.955 0.008 80);
  --svgb-02-muted: #8e8981;
  --svgb-02-muted: oklch(0.665 0.012 80);
  --svgb-02-rack: #131211;
  --svgb-02-rack: oklch(0.20 0.004 70);
  --svgb-02-rest: rgba(242, 239, 233, 0.16);
  --svgb-02-rest: oklch(0.955 0.008 80 / 0.16);
  --svgb-02-stroke: #ffb020;
  --svgb-02-stroke: oklch(0.81 0.16 76);
  --svgb-02-dur: 2.6s;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--svgb-02-bg);
  color: var(--svgb-02-fg);
  font-family: 'Sora', system-ui, sans-serif;
}

.svgb-02 *,
.svgb-02 *::before,
.svgb-02 *::after {
  box-sizing: border-box;
}

.svgb-02__stage {
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(20px, 5vw, 64px);
}

.svgb-02__rack {
  width: 100%;
  max-width: 640px;
  display: flex;
  flex-direction: column;
  gap: clamp(18px, 3vw, 28px);
  padding: clamp(22px, 4vw, 36px);
  border-radius: 6px;
  background: linear-gradient(var(--svgb-02-rack), color-mix(in oklab, var(--svgb-02-rack) 80%, #000));
  box-shadow: inset 0 1px 0 oklch(1 0 0 / 0.07), 0 40px 80px -50px #000;
}

.svgb-02__head {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
}

.svgb-02__take {
  font-size: 13px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--svgb-02-muted);
}

.svgb-02__tc {
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: clamp(20px, 3.4vw, 30px);
  letter-spacing: -0.01em;
  color: var(--svgb-02-stroke);
  font-variant-numeric: tabular-nums;
}

.svgb-02__wave {
  display: flex;
  align-items: flex-end;
  gap: 4px;
  block-size: 84px;
}

.svgb-02__wave span {
  flex: 1;
  block-size: var(--h);
  border-radius: 1px;
  background: color-mix(in oklab, var(--svgb-02-fg) 22%, transparent);
}

.svgb-02__scrub {
  block-size: 6px;
}

.svgb-02__sline {
  inline-size: 100%;
  block-size: 6px;
  overflow: visible;
}

.svgb-02__strack {
  stroke: var(--svgb-02-rest);
  stroke-width: 2px;
}

.svgb-02__srun {
  stroke: var(--svgb-02-stroke);
  stroke-width: 2px;
  stroke-linecap: round;
  stroke-dasharray: 26 534;
  stroke-dashoffset: var(--svgb-02-phase);
  animation: svgb-02-run var(--svgb-02-dur) linear infinite;
}

@keyframes svgb-02-run {
  to {
    --svgb-02-phase: -560;
  }
}

@keyframes svgb-02-run-fb {
  to {
    stroke-dashoffset: -560;
  }
}

@supports not (background: paint(x)) {
  .svgb-02__srun {
    animation-name: svgb-02-run-fb;
  }
}

.svgb-02__pads {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(18px, 4vw, 40px);
  justify-content: space-between;
  padding-block-start: 6px;
}

.svgb-02__pad {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}

.svgb-02__pd {
  position: relative;
  inline-size: 120px;
  block-size: 120px;
  display: grid;
  place-items: center;
  border: 0;
  padding: 0;
  border-radius: 50%;
  background: radial-gradient(circle at 50% 30%, color-mix(in oklab, var(--svgb-02-fg) 7%, transparent), transparent 70%);
  color: inherit;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.svgb-02__pd:focus-visible {
  outline: 2px solid var(--svgb-02-stroke);
  outline-offset: 4px;
}

.svgb-02__glyph {
  position: relative;
  z-index: 1;
  inline-size: 30px;
  block-size: 30px;
  fill: none;
  stroke: var(--svgb-02-fg);
  stroke-width: 1.6px;
  stroke-linecap: round;
  stroke-linejoin: round;
  transition: stroke 300ms ease;
}

.svgb-02__pd--draw .svgb-02__glyph {
  fill: var(--svgb-02-fg);
  stroke: none;
}

.svgb-02__pd:hover .svgb-02__glyph,
.svgb-02__pd:focus-visible .svgb-02__glyph {
  stroke: var(--svgb-02-stroke);
}

.svgb-02__pd--draw:hover .svgb-02__glyph,
.svgb-02__pd--draw:focus-visible .svgb-02__glyph {
  fill: var(--svgb-02-stroke);
}

.svgb-02__ring {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-02__ring circle {
  fill: none;
}

.svgb-02__base {
  stroke: var(--svgb-02-rest);
  stroke-width: 1.5px;
}

.svgb-02__ink {
  stroke: var(--svgb-02-stroke);
  stroke-width: 2.4px;
  stroke-linecap: round;
}

.svgb-02__cap {
  font-family: 'IBM Plex Mono', ui-monospace, monospace;
  font-size: 10.5px;
  line-height: 1.55;
  text-align: center;
  color: var(--svgb-02-muted);
}

.svgb-02__pd--draw .svgb-02__ink {
  stroke-dasharray: 360;
  stroke-dashoffset: 360;
  transition: stroke-dashoffset 760ms cubic-bezier(0.16, 1, 0.3, 1);
}

.svgb-02__pd--draw:hover .svgb-02__ink,
.svgb-02__pd--draw:focus-visible .svgb-02__ink {
  stroke-dashoffset: 0;
}

@keyframes svgb-02-orbit {
  to {
    --svgb-02-phase: -360;
  }
}

@keyframes svgb-02-orbit-fb {
  to {
    stroke-dashoffset: -360;
  }
}

.svgb-02__pd--run .svgb-02__ink,
.svgb-02__pd--chase .svgb-02__ink {
  stroke-dashoffset: var(--svgb-02-phase);
  animation: svgb-02-orbit 2.4s linear infinite;
  animation-play-state: paused;
}

@supports not (background: paint(x)) {
  .svgb-02__pd--run .svgb-02__ink,
    .svgb-02__pd--chase .svgb-02__ink {
    animation-name: svgb-02-orbit-fb;
  }
}

.svgb-02__pd--run .svgb-02__ink {
  stroke-dasharray: 40 320;
}

.svgb-02__pd--chase .svgb-02__ink {
  stroke-dasharray: 180 180;
}

.svgb-02__pd--run:hover .svgb-02__ink,
.svgb-02__pd--run:focus-visible .svgb-02__ink,
.svgb-02__pd--chase:hover .svgb-02__ink,
.svgb-02__pd--chase:focus-visible .svgb-02__ink {
  animation-play-state: running;
}

.svgb-02__ti {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-02__toggle {
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

.svgb-02__toggle:hover {
  background: color-mix(in oklab, currentColor 14%, transparent);
}

.svgb-02__toggle:active {
  transform: scale(0.94);
}

.svgb-02__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 400ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.svgb-02__ti:checked + .svgb-02__toggle svg {
  transform: rotate(180deg);
}

.svgb-02__ti:focus-visible + .svgb-02__toggle {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.svgb-02__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.svgb-02:has(#svgb-02-theme:checked) {
  --svgb-02-bg: #edeae4;
  --svgb-02-bg: oklch(0.94 0.008 85);
  --svgb-02-fg: #14130f;
  --svgb-02-fg: oklch(0.19 0.006 80);
  --svgb-02-muted: #6a655d;
  --svgb-02-muted: oklch(0.535 0.012 80);
  --svgb-02-rack: #fbfaf7;
  --svgb-02-rack: oklch(0.985 0.004 85);
  --svgb-02-rest: rgba(20, 19, 15, 0.16);
  --svgb-02-rest: oklch(0.19 0.006 80 / 0.16);
  --svgb-02-stroke: #8a4b00;
  --svgb-02-stroke: oklch(0.50 0.13 62);
}

.svgb-02:has(#svgb-02-theme:checked) .svgb-02__rack {
  box-shadow: 0 1px 2px oklch(0 0 0 / 0.06), 0 30px 70px -50px oklch(0 0 0 / 0.5);
}

@media (prefers-reduced-motion: reduce) {
  .svgb-02__ink,
    .svgb-02__srun {
    animation: none !important;
  }

  .svgb-02__ink {
    transition: none;
    stroke-dasharray: none;
    stroke-dashoffset: 0;
    opacity: 0;
  }

  .svgb-02__pd:hover .svgb-02__ink,
    .svgb-02__pd:focus-visible .svgb-02__ink {
    opacity: 1;
  }

  .svgb-02__srun {
    stroke-dasharray: 140 420;
    stroke-dashoffset: 0;
  }

  .svgb-02__glyph,
    .svgb-02__toggle,
    .svgb-02__toggle svg {
    transition: none;
  }
}
```
