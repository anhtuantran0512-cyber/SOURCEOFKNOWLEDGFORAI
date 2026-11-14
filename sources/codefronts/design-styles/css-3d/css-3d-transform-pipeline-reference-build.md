---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/css-3d-transform-pipeline-reference-build/"
title: "CSS 3D Transform Pipeline Reference Build"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "The reference scene the rest of this collection borrows from: a viewing frustum declared with perspective on the parent, a preserve-3d world so children keep…"
has_js: "false"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS 3D Transform Pipeline Reference Build
Source: https://codefronts.com/design-styles/css-3d/css-3d-transform-pipeline-reference-build/

The reference scene the rest of this collection borrows from: a viewing frustum declared with perspective on the parent, a preserve-3d world so children keep their own depth, a child transform, and perspective-origin acting as the camera. An axis gizmo and live property chips make each piece of the pipeline visible instead of implied.
## HTML
```html
<section class="d3-01" aria-labelledby="d3-01-title">
  <h2 class="d3-01__sr" id="d3-01-title">Transform pipeline scene</h2>

  <div class="d3-01__theme">
    <input class="d3-01__theme-input" type="checkbox" id="d3-01-theme">
    <label class="d3-01__theme-label" for="d3-01-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="d3-01__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="d3-01__stage">
    <div class="d3-01__viewport">
      <header class="d3-01__head">
        <span class="d3-01__dot" aria-hidden="true"></span>
        <b>Meridian deploy console</b>
        <span class="d3-01__crumb">eu-west-2 &middot; production</span>
      </header>

      <div class="d3-01__scene">
        <div class="d3-01__world">
          <div class="d3-01__gizmo" aria-hidden="true">
            <span class="d3-01__axis d3-01__axis--x"><i class="d3-01__axis-tick">X</i></span>
            <span class="d3-01__axis d3-01__axis--y"><i class="d3-01__axis-tick">Y</i></span>
            <span class="d3-01__axis d3-01__axis--z"><i class="d3-01__axis-tick">Z</i></span>
          </div>

          <div class="d3-01__slab">
            <article class="d3-01__slab-face d3-01__slab-face--front">
              <div class="d3-01__card-top">
                <span class="d3-01__pill">Deploying</span>
                <span class="d3-01__ver">v4.2.0</span>
                <strong class="d3-01__title">Checkout&nbsp;service</strong>
                <span class="d3-01__sub">18 services &middot; canary 25%</span>
              </div>
              <div class="d3-01__card-body">
                <div class="d3-01__bar" aria-hidden="true"><i style="--d3-01-p: 68%"></i></div>
                <ul class="d3-01__stats">
                  <li><b>68%</b><span>rolled</span></li>
                  <li><b>142ms</b><span>p95</span></li>
                  <li><b>0</b><span>errors</span></li>
                </ul>
                <div class="d3-01__spark" aria-hidden="true">
                  <span style="--d3-01-h: 34%"></span><span style="--d3-01-h: 52%"></span><span style="--d3-01-h: 41%"></span><span style="--d3-01-h: 74%"></span><span style="--d3-01-h: 58%"></span><span style="--d3-01-h: 88%"></span><span style="--d3-01-h: 63%"></span><span style="--d3-01-h: 96%"></span>
                </div>
              </div>
            </article>

            <article class="d3-01__slab-face d3-01__slab-face--rear">
              <span class="d3-01__pill d3-01__pill--warn">Rollback ready</span>
              <strong class="d3-01__title">v4.1.8</strong>
              <span class="d3-01__sub">snapshot 09:41 &middot; 2.4 GB</span>
            </article>
          </div>

          <div class="d3-01__floor" aria-hidden="true"></div>
        </div>
      </div>

      <ul class="d3-01__chips">
        <li class="d3-01__chip"><b>parent</b> perspective: 1100px</li>
        <li class="d3-01__chip"><b>parent</b> perspective-origin: 50% 38%</li>
        <li class="d3-01__chip"><b>world</b> transform-style: preserve-3d</li>
        <li class="d3-01__chip"><b>child</b> translateZ(&plusmn;28px)</li>
      </ul>
    </div>
  </div>
</section>
```
## CSS
```css
.d3-01 {
  --d3-01-bg: #eef2f9;
  --d3-01-surf: #ffffff;
  --d3-01-line: #d3dceb;
  --d3-01-grid: #e2e9f4;
  --d3-01-ink: #0b1220;
  --d3-01-mut: #5d6a7a;
  --d3-01-acc: #2f5bff;
  --d3-01-acc: oklch(55% 0.23 267);
  --d3-01-acc2: #7b3ff2;
  --d3-01-acc2: oklch(52% 0.24 296);
  --d3-01-lime: #35c26a;
  --d3-01-lime: oklch(70% 0.18 150);
  --d3-01-amber: #f59f0b;
  --d3-01-amber: oklch(78% 0.16 78);
  --d3-01-slab: #ffffff;
  --d3-01-thick: 56px;
  --d3-01-depth: clamp(560px, 78vw, 1100px);
  --d3-01-spin: 22s;
  --d3-01-font-display: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background-color: var(--d3-01-bg);
  background-image: radial-gradient(90rem 40rem at 78% -10%, color-mix(in oklab, var(--d3-01-acc) 16%, transparent), transparent 60%), radial-gradient(60rem 30rem at 5% 105%, color-mix(in oklab, var(--d3-01-acc2) 14%, transparent), transparent 60%), linear-gradient(var(--d3-01-grid) 1px, transparent 1px), linear-gradient(90deg, var(--d3-01-grid) 1px, transparent 1px);
  background-size: auto, auto, 28px 28px, 28px 28px;
  color: var(--d3-01-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.d3-01 *,
.d3-01 *::before,
.d3-01 *::after {
  box-sizing: border-box;
}

.d3-01__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.d3-01:has(.d3-01__theme-input:checked) {
  --d3-01-bg: #080c14;
  --d3-01-surf: #121a27;
  --d3-01-line: #26344a;
  --d3-01-grid: #121a26;
  --d3-01-ink: #eaf0f6;
  --d3-01-mut: #94a4bb;
  --d3-01-acc: #7f9dff;
  --d3-01-acc: oklch(74% 0.16 267);
  --d3-01-acc2: #b98bff;
  --d3-01-acc2: oklch(73% 0.16 296);
  --d3-01-lime: #4ade80;
  --d3-01-lime: oklch(80% 0.18 150);
  --d3-01-slab: #121a27;
}

@media (prefers-color-scheme: dark) {
  .d3-01 {
    --d3-01-bg: #080c14;
    --d3-01-surf: #121a27;
    --d3-01-line: #26344a;
    --d3-01-grid: #121a26;
    --d3-01-ink: #eaf0f6;
    --d3-01-mut: #94a4bb;
    --d3-01-acc: #7f9dff;
    --d3-01-acc: oklch(74% 0.16 267);
    --d3-01-acc2: #b98bff;
    --d3-01-acc2: oklch(73% 0.16 296);
    --d3-01-lime: #4ade80;
    --d3-01-lime: oklch(80% 0.18 150);
    --d3-01-slab: #121a27;
  }

  .d3-01:has(.d3-01__theme-input:checked) {
    --d3-01-bg: #eef2f9;
    --d3-01-surf: #ffffff;
    --d3-01-line: #d3dceb;
    --d3-01-grid: #e2e9f4;
    --d3-01-ink: #0b1220;
    --d3-01-mut: #5d6a7a;
    --d3-01-acc: #2f5bff;
    --d3-01-acc: oklch(55% 0.23 267);
    --d3-01-acc2: #7b3ff2;
    --d3-01-acc2: oklch(52% 0.24 296);
    --d3-01-lime: #35c26a;
    --d3-01-lime: oklch(70% 0.18 150);
    --d3-01-slab: #ffffff;
  }
}

@media (prefers-color-scheme: light) {
  .d3-01:has(.d3-01__theme-input:checked) {
    --d3-01-bg: #080c14;
    --d3-01-surf: #121a27;
    --d3-01-line: #26344a;
    --d3-01-grid: #121a26;
    --d3-01-ink: #eaf0f6;
    --d3-01-mut: #94a4bb;
    --d3-01-acc: #7f9dff;
    --d3-01-acc: oklch(74% 0.16 267);
    --d3-01-acc2: #b98bff;
    --d3-01-acc2: oklch(73% 0.16 296);
    --d3-01-lime: #4ade80;
    --d3-01-lime: oklch(80% 0.18 150);
    --d3-01-slab: #121a27;
  }
}

.d3-01__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 20;
}

.d3-01__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.d3-01__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--d3-01-line);
  border-radius: 14px;
  background: var(--d3-01-surf);
  color: var(--d3-01-ink);
  cursor: pointer;
  box-shadow: 0 6px 18px rgba(11, 18, 32, 0.12);
}

.d3-01__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-01__theme-input:focus-visible + .d3-01__theme-label {
  outline: 2px solid var(--d3-01-acc);
  outline-offset: 3px;
}

.d3-01__stage {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(3.5rem, 9vw, 5rem) clamp(0.75rem, 4vw, 2.5rem);
}

.d3-01__viewport {
  inline-size: 100%;
  max-inline-size: 62rem;
  overflow: hidden;
  border: 1px solid var(--d3-01-line);
  border-radius: 24px;
  background: color-mix(in oklab, var(--d3-01-surf) 72%, transparent);
  backdrop-filter: blur(6px);
  padding: clamp(1rem, 3vw, 1.75rem);
  box-shadow: 0 30px 70px -30px rgba(11, 18, 32, 0.45);
}

.d3-01__head {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  padding-block-end: 0.9rem;
  border-block-end: 1px solid var(--d3-01-line);
  font: 600 clamp(0.8rem, 2.2vw, 0.95rem)/1 system-ui, sans-serif;
}

.d3-01__dot {
  inline-size: 9px;
  block-size: 9px;
  border-radius: 999px;
  background: var(--d3-01-lime);
  box-shadow: 0 0 0 4px color-mix(in oklab, var(--d3-01-lime) 25%, transparent);
}

.d3-01__crumb {
  margin-inline-start: auto;
  color: var(--d3-01-mut);
  font: 500 clamp(0.66rem, 1.8vw, 0.76rem)/1 var(--d3-01-font-display);
}

.d3-01__scene {
  perspective: var(--d3-01-depth);
  perspective-origin: 50% 38%;
  block-size: clamp(17rem, 46vw, 23rem);
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  place-items: center;
}

.d3-01__world {
  position: relative;
  inline-size: clamp(15rem, 40vw, 21rem);
  block-size: clamp(13rem, 34vw, 17rem);
  transform-style: preserve-3d;
  transform: rotateX(14deg);
  animation: d3-01-survey var(--d3-01-spin) linear infinite;
}

@keyframes d3-01-survey {
  from {
    transform: rotateX(14deg) rotateY(-22deg);
  }

  50% {
    transform: rotateX(14deg) rotateY(22deg);
  }

  to {
    transform: rotateX(14deg) rotateY(-22deg);
  }
}

.d3-01__slab {
  position: absolute;
  inset: -6% 2%;
  transform-style: preserve-3d;
}

.d3-01__slab-face {
  position: absolute;
  inset: 0;
  overflow: hidden;
  border-radius: 20px;
  border: 1px solid var(--d3-01-line);
  background: var(--d3-01-slab);
  color: var(--d3-01-ink);
  backface-visibility: hidden;
  box-shadow: 0 30px 60px -24px rgba(11, 18, 32, 0.55);
}

.d3-01__slab-face--front {
  transform: translateZ(calc(var(--d3-01-thick) / 2));
  display: grid;
  grid-template-rows: auto 1fr;
}

.d3-01__slab-face--rear {
  transform: translateZ(calc(var(--d3-01-thick) / -2)) rotateY(180deg);
  display: grid;
  align-content: center;
  justify-items: start;
  gap: 0.35rem;
  padding: clamp(1rem, 3vw, 1.5rem);
  background: linear-gradient(150deg, color-mix(in oklab, var(--d3-01-amber) 22%, var(--d3-01-slab)), var(--d3-01-slab));
}

.d3-01__card-top {
  padding: clamp(0.9rem, 2.6vw, 1.25rem);
  display: grid;
  justify-items: start;
  gap: 0.3rem;
  color: #fff;
  background: linear-gradient(135deg, var(--d3-01-acc), var(--d3-01-acc2));
}

.d3-01__pill {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.22rem 0.6rem;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.22);
  font: 700 clamp(0.6rem, 1.7vw, 0.68rem)/1.4 var(--d3-01-font-display);
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.d3-01__pill--warn {
  background: color-mix(in oklab, var(--d3-01-amber) 32%, transparent);
  color: var(--d3-01-ink);
}

.d3-01__ver {
  position: absolute;
  inset-block-start: clamp(0.9rem, 2.6vw, 1.25rem);
  inset-inline-end: clamp(0.9rem, 2.6vw, 1.25rem);
  font: 600 clamp(0.66rem, 1.8vw, 0.76rem)/1 var(--d3-01-font-display);
  color: rgba(255, 255, 255, 0.85);
}

.d3-01__title {
  font: 700 clamp(1.05rem, 3.2vw, 1.45rem)/1.1 system-ui, sans-serif;
  letter-spacing: -0.02em;
}

.d3-01__sub {
  font: 500 clamp(0.68rem, 1.9vw, 0.78rem)/1.2 var(--d3-01-font-display);
  color: rgba(255, 255, 255, 0.8);
}

.d3-01__slab-face--rear .d3-01__sub {
  color: var(--d3-01-mut);
}

.d3-01__card-body {
  padding: clamp(0.9rem, 2.6vw, 1.25rem);
  display: grid;
  align-content: start;
  gap: clamp(0.6rem, 2vw, 0.9rem);
}

.d3-01__bar {
  block-size: 8px;
  border-radius: 999px;
  background: color-mix(in oklab, var(--d3-01-ink) 10%, transparent);
  overflow: hidden;
}

.d3-01__bar i {
  display: block;
  block-size: 100%;
  inline-size: var(--d3-01-p);
  border-radius: 999px;
  background: linear-gradient(90deg, var(--d3-01-acc), var(--d3-01-lime));
}

.d3-01__stats {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 0.5rem;
}

.d3-01__stats li {
  display: grid;
  gap: 0.1rem;
  padding: 0.5rem 0.6rem;
  border-radius: 12px;
  background: color-mix(in oklab, var(--d3-01-acc) 8%, transparent);
}

.d3-01__stats b {
  font: 700 clamp(0.85rem, 2.4vw, 1rem)/1 var(--d3-01-font-display);
}

.d3-01__stats span {
  font: 600 0.62rem/1 var(--d3-01-font-display);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--d3-01-mut);
}

.d3-01__spark {
  display: grid;
  grid-template-columns: repeat(8, minmax(0, 1fr));
  align-items: end;
  gap: 4px;
  block-size: 2.6rem;
}

.d3-01__spark span {
  display: block;
  block-size: var(--d3-01-h);
  border-radius: 3px;
  background: linear-gradient(var(--d3-01-acc2), color-mix(in oklab, var(--d3-01-acc) 35%, transparent));
}

.d3-01__floor {
  position: absolute;
  inset-inline: -22%;
  inset-block-end: -14%;
  block-size: 60%;
  transform: rotateX(90deg) translateZ(-3.2rem);
  background-image: linear-gradient(color-mix(in oklab, var(--d3-01-acc) 35%, transparent) 1px, transparent 1px), linear-gradient(90deg, color-mix(in oklab, var(--d3-01-acc) 35%, transparent) 1px, transparent 1px);
  background-size: 22px 22px;
  opacity: 0.5;
}

.d3-01__gizmo {
  position: absolute;
  inset: 0;
  transform-style: preserve-3d;
}

.d3-01__axis {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: 52%;
  block-size: 1px;
  background: color-mix(in oklab, var(--d3-01-mut) 55%, transparent);
  transform-origin: 0 50%;
}

.d3-01__axis-tick {
  position: absolute;
  inset-inline-end: -1.1rem;
  inset-block-start: -0.7rem;
  font: 700 0.68rem/1 var(--d3-01-font-display);
  font-style: normal;
  color: var(--d3-01-mut);
}

.d3-01__axis--x {
  transform: none;
}

.d3-01__axis--y {
  transform: rotateZ(-90deg);
}

.d3-01__axis--z {
  transform: rotateY(-90deg);
  background: var(--d3-01-acc);
}

.d3-01__chips {
  list-style: none;
  margin: clamp(0.9rem, 3vw, 1.4rem) 0 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
}

.d3-01__chip {
  border: 1px solid var(--d3-01-line);
  border-radius: 999px;
  padding: 0.38rem 0.7rem;
  font: 500 clamp(0.66rem, 1.8vw, 0.76rem)/1.2 var(--d3-01-font-display);
  color: var(--d3-01-mut);
  background: var(--d3-01-surf);
}

.d3-01__chip b {
  color: var(--d3-01-acc);
  font-weight: 700;
}

@media (prefers-reduced-motion: reduce) {
  .d3-01__world {
    animation: none;
    transform: rotateX(14deg) rotateY(-18deg);
  }
}
```
