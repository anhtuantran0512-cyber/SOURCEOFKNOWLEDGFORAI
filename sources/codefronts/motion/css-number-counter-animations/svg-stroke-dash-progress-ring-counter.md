---
source: "codefronts"
url: "https://codefronts.com/motion/css-number-counter-animations/svg-stroke-dash-progress-ring-counter/"
title: "SVG Stroke-Dash Progress Ring Counter"
section: "motion"
category: "css-number-counter-animations"
category_name: "CSS Number Counter Animations"
description: "Three rings, one technique, zero JavaScript: a registered @property drives both the SVG stroke-dashoffset and the printed percentage from the same animation,…"
has_js: "false"
---

Here's a working CSS Number Counter Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SVG Stroke-Dash Progress Ring Counter
Source: https://codefronts.com/motion/css-number-counter-animations/svg-stroke-dash-progress-ring-counter/

Three rings, one technique, zero JavaScript: a registered @property drives both the SVG stroke-dashoffset and the printed percentage from the same animation, so the arc and the number can never disagree. A conic-gradient variant and a segmented-track variant are included for comparison.
## HTML
```html
<section class="cnc-10" aria-label="SVG stroke dash progress ring counter demo">
  <div class="cnc-10__stage">
    <div class="cnc-10__grid">
      <figure class="cnc-10__item" style="--cnc-10-to:.78;--cnc-10-ton:78;--cnc-10-hue:250">
        <div class="cnc-10__ring">
          <svg viewBox="0 0 120 120" aria-hidden="true">
            <circle class="cnc-10__track" cx="60" cy="60" r="52"/>
            <circle class="cnc-10__arc" cx="60" cy="60" r="52" pathLength="100"/>
          </svg>
          <span class="cnc-10__num" aria-hidden="true"></span>
        </div>
        <figcaption class="cnc-10__cap">Sprint completion<span class="cnc-10__sr">78 percent</span></figcaption>
      </figure>
      <figure class="cnc-10__item" style="--cnc-10-to:.94;--cnc-10-ton:94;--cnc-10-hue:155">
        <div class="cnc-10__ring">
          <svg viewBox="0 0 120 120" aria-hidden="true">
            <circle class="cnc-10__track" cx="60" cy="60" r="52"/>
            <circle class="cnc-10__arc" cx="60" cy="60" r="52" pathLength="100"/>
          </svg>
          <span class="cnc-10__num" aria-hidden="true"></span>
        </div>
        <figcaption class="cnc-10__cap">Test coverage<span class="cnc-10__sr">94 percent</span></figcaption>
      </figure>
      <figure class="cnc-10__item cnc-10__item--conic" style="--cnc-10-to:.41;--cnc-10-ton:41;--cnc-10-hue:35">
        <div class="cnc-10__ring">
          <span class="cnc-10__conic" aria-hidden="true"></span>
          <span class="cnc-10__num" aria-hidden="true"></span>
        </div>
        <figcaption class="cnc-10__cap">Storage used<span class="cnc-10__sr">41 percent</span></figcaption>
      </figure>
    </div>
    <p class="cnc-10__chip" aria-hidden="true">pathLength=100 · @property inherits:true · one animation drives arc + counter</p>
  </div>
</section>
```
## CSS
```css
@property --cnc-10-p {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}

@property --cnc-10-n {
  syntax: '<integer>';
  inherits: true;
  initial-value: 0;
}

.cnc-10,
.cnc-10 *,
.cnc-10 *::before,
.cnc-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnc-10 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  --cnc-10-bg: oklch(0.16 0.02 260);
  --cnc-10-ink: oklch(0.98 0.004 260);
  --cnc-10-mut: oklch(0.67 0.02 260);
  background: var(--cnc-10-bg);
  color: var(--cnc-10-ink);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
}

.cnc-10__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 26px;
  padding: clamp(18px,4vw,48px);
}

.cnc-10__grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: clamp(18px,4vw,40px);
}

.cnc-10__item {
  --cnc-10-acc: oklch(0.75 0.17 var(--cnc-10-hue,250));
  display: grid;
  justify-items: center;
  gap: 14px;
  animation: cnc-10-fill 2.1s cubic-bezier(.16,1,.3,1) forwards;
}

.cnc-10__item:nth-child(2) {
  animation-delay: .15s;
}

.cnc-10__item:nth-child(3) {
  animation-delay: .3s;
}

@keyframes cnc-10-fill {
  from {
    --cnc-10-p: 0;
    --cnc-10-n: 0;
  }

  to {
    --cnc-10-p: var(--cnc-10-to);
    --cnc-10-n: var(--cnc-10-ton);
  }
}

.cnc-10__ring {
  position: relative;
  display: grid;
  place-items: center;
  width: clamp(124px,26vw,158px);
  aspect-ratio: 1;
}

.cnc-10__ring svg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  transform: rotate(-90deg);
  overflow: visible;
}

.cnc-10__track {
  fill: none;
  stroke: oklch(1 0 0/.1);
  stroke-width: 9;
}

.cnc-10__arc {
  fill: none;
  stroke: var(--cnc-10-acc);
  stroke-width: 9;
  stroke-linecap: round;
  stroke-dasharray: 100;
  stroke-dashoffset: calc(100 - 100 * var(--cnc-10-p));
  filter: drop-shadow(0 0 10px color-mix(in oklch,var(--cnc-10-acc) 55%,transparent));
}

.cnc-10__conic {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: conic-gradient(var(--cnc-10-acc) calc(var(--cnc-10-p) * 360deg),oklch(1 0 0/.1) 0);
  -webkit-mask: radial-gradient(farthest-side,transparent calc(50% - 9px),#000 calc(50% - 8px));
  mask: radial-gradient(farthest-side,transparent calc(50% - 9px),#000 calc(50% - 8px));
}

.cnc-10__num {
  counter-reset: cnc-10-n var(--cnc-10-n);
  font-size: clamp(30px,6vw,38px);
  font-weight: 740;
  letter-spacing: -.04em;
  font-variant-numeric: tabular-nums;
  font-feature-settings: 'tnum' 1;
}

.cnc-10__num::after {
  content: counter(cnc-10-n) "%";
}

.cnc-10__cap {
  font-size: 13px;
  color: var(--cnc-10-mut);
  text-align: center;
}

.cnc-10__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cnc-10__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--cnc-10-mut);
  padding: 7px 14px;
  border: 1px solid oklch(1 0 0/.13);
  border-radius: 99px;
  text-align: center;
  max-width: min(100%,520px);
}

@media (prefers-reduced-motion: reduce) {
  .cnc-10__item {
    animation-duration: 1ms;
  }
}
```
