---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/transform-origin-in-three-dimensions/"
title: "Transform Origin in Three Dimensions"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "transform-origin takes a third value, and that value decides whether a rotation is a spin or an orbit."
has_js: "false"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Transform Origin in Three Dimensions
Source: https://codefronts.com/design-styles/css-3d/transform-origin-in-three-dimensions/

transform-origin takes a third value, and that value decides whether a rotation is a spin or an orbit. The same rotateY runs on three identical panels &mdash; origin at the centre, at the left edge, and pushed back along Z &mdash; each labelled with its value, so the change from turning in place to swinging around a distant pivot is visible in one frame.
## HTML
```html
<section class="d3-08" aria-labelledby="d3-08-title">
  <h2 class="d3-08__sr" id="d3-08-title">Transform origin in three dimensions</h2>

  <div class="d3-08__theme">
    <input class="d3-08__theme-input" type="checkbox" id="d3-08-theme">
    <label class="d3-08__theme-label" for="d3-08-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="d3-08__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="d3-08__stage">
    <div class="d3-08__viewport">
      <header class="d3-08__head">
        <div class="d3-08__intro">
          <span class="d3-08__kicker">Kestrel Bank &middot; interaction library</span>
          <strong>Three components.<br>One rotation. Three pivots.</strong>
          <p>Every motion below is <code>rotateY</code>. The only thing that changes is where the axis sits &mdash; and that decides whether a component flips, opens, or orbits.</p>
        </div>
        <span class="d3-08__meta"><i></i>live spec &middot; 9s loop</span>
      </header>

      <div class="d3-08__grid">
        <article class="d3-08__cell">
          <div class="d3-08__scene">
            <span class="d3-08__axis" aria-hidden="true"></span>
            <div class="d3-08__pivot" aria-hidden="true"></div>
            <div class="d3-08__slab d3-08__slab--spin">
              <div class="d3-08__card">
                <span class="d3-08__brand">Kestrel</span>
                <span class="d3-08__bal"><em>Available</em><b>&pound;4,820.15</b></span>
                <span class="d3-08__pan">&bull;&bull;&bull;&bull; 4471</span>
              </div>
            </div>
          </div>
          <div class="d3-08__meta-row"><span class="d3-08__idx">01</span><h3>Balance card flip</h3></div>
          <code>transform-origin: 50% 50% 0</code>
          <p>Axis through the middle: the card turns in place to reveal its reverse. Front and back stay the same size, so nothing in the layout moves.</p>
        </article>

        <article class="d3-08__cell">
          <div class="d3-08__scene">
            <div class="d3-08__list" aria-hidden="true">
              <span></span><span></span><span></span><span></span>
            </div>
            <span class="d3-08__axis d3-08__axis--edge" aria-hidden="true"></span>
            <div class="d3-08__pivot d3-08__pivot--edge" aria-hidden="true"></div>
            <div class="d3-08__slab d3-08__slab--hinge">
              <div class="d3-08__panel">
                <b>Filters</b>
                <span class="d3-08__chip d3-08__chip--on">This month</span>
                <span class="d3-08__chip">Card only</span>
                <span class="d3-08__chip">Over &pound;50</span>
              </div>
            </div>
          </div>
          <div class="d3-08__meta-row"><span class="d3-08__idx">02</span><h3>Filter drawer</h3></div>
          <code>transform-origin: 0% 50% 0</code>
          <p>Axis on the leading edge: the panel swings like a door over the transaction list. The hinge is what makes it read as a surface, not a fade.</p>
        </article>

        <article class="d3-08__cell">
          <div class="d3-08__scene">
            <div class="d3-08__pivot d3-08__pivot--deep" aria-hidden="true"></div>
            <div class="d3-08__slab d3-08__slab--orbit">
              <div class="d3-08__tile">
                <span class="d3-08__ava"></span>
                <b>Send again</b>
                <em>Mira &middot; &pound;24.00</em>
              </div>
            </div>
          </div>
          <div class="d3-08__meta-row"><span class="d3-08__idx">03</span><h3>Recents carousel</h3></div>
          <code>transform-origin: 50% 50% -120px</code>
          <p>Axis pushed behind the tile: it orbits a point in the distance, sweeping in and out of the frame the way a ring of shortcuts should.</p>
        </article>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.d3-08 {
  --d3-08-bg: #04120f;
  --d3-08-surf: #0a201c;
  --d3-08-glass: rgba(255, 255, 255, 0.05);
  --d3-08-line: #16403a;
  --d3-08-ink: #ecfff8;
  --d3-08-mut: #86ada4;
  --d3-08-acc: #3bf0a5;
  --d3-08-acc: oklch(85% 0.19 158);
  --d3-08-acc2: #ff7a5c;
  --d3-08-acc2: oklch(74% 0.16 35);
  --d3-08-acc3: #8ab4ff;
  --d3-08-acc3: oklch(78% 0.12 262);
  --d3-08-font-display: "Inter Tight", "Inter", "Segoe UI", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: radial-gradient(60rem 30rem at 8% -12%, color-mix(in oklab, var(--d3-08-acc) 26%, transparent), transparent 58%), radial-gradient(44rem 26rem at 98% 8%, color-mix(in oklab, var(--d3-08-acc3) 20%, transparent), transparent 58%), radial-gradient(46rem 24rem at 50% 112%, color-mix(in oklab, var(--d3-08-acc2) 18%, transparent), transparent 60%), var(--d3-08-bg);
  color: var(--d3-08-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.d3-08 *,
.d3-08 *::before,
.d3-08 *::after {
  box-sizing: border-box;
}

.d3-08__sr {
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

.d3-08:has(.d3-08__theme-input:checked) {
  --d3-08-bg: #f2f6f4;
  --d3-08-surf: #ffffff;
  --d3-08-glass: rgba(9, 32, 27, 0.04);
  --d3-08-line: #d3e2dc;
  --d3-08-ink: #04140f;
  --d3-08-mut: #4c665e;
  --d3-08-acc: #01804f;
  --d3-08-acc: oklch(52% 0.14 158);
  --d3-08-acc2: #c0442a;
  --d3-08-acc2: oklch(54% 0.16 35);
  --d3-08-acc3: #2f5fd0;
  --d3-08-acc3: oklch(50% 0.18 262);
}

@media (prefers-color-scheme: light) {
  .d3-08:has(.d3-08__theme-input:checked) {
    --d3-08-bg: #f2f6f4;
    --d3-08-surf: #ffffff;
    --d3-08-glass: rgba(9, 32, 27, 0.04);
    --d3-08-line: #d3e2dc;
    --d3-08-ink: #04140f;
    --d3-08-mut: #4c665e;
    --d3-08-acc: #01804f;
    --d3-08-acc: oklch(52% 0.14 158);
    --d3-08-acc2: #c0442a;
    --d3-08-acc2: oklch(54% 0.16 35);
    --d3-08-acc3: #2f5fd0;
    --d3-08-acc3: oklch(50% 0.18 262);
  }
}

@media (prefers-color-scheme: dark) {
  .d3-08:has(.d3-08__theme-input:checked) {
    --d3-08-bg: #f2f6f4;
    --d3-08-surf: #ffffff;
    --d3-08-glass: rgba(9, 32, 27, 0.04);
    --d3-08-line: #d3e2dc;
    --d3-08-ink: #04140f;
    --d3-08-mut: #4c665e;
    --d3-08-acc: #01804f;
    --d3-08-acc: oklch(52% 0.14 158);
    --d3-08-acc2: #c0442a;
    --d3-08-acc2: oklch(54% 0.16 35);
    --d3-08-acc3: #2f5fd0;
    --d3-08-acc3: oklch(50% 0.18 262);
  }
}

.d3-08__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 20;
}

.d3-08__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.d3-08__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--d3-08-line);
  border-radius: 999px;
  background: color-mix(in oklab, var(--d3-08-surf) 70%, transparent);
  color: var(--d3-08-ink);
  cursor: pointer;
}

.d3-08__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-08__theme-input:focus-visible + .d3-08__theme-label {
  outline: 2px solid var(--d3-08-acc);
  outline-offset: 3px;
}

.d3-08__stage {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(3.5rem, 9vw, 5rem) clamp(0.75rem, 4vw, 2.5rem);
}

.d3-08__viewport {
  inline-size: 100%;
  max-inline-size: 68rem;
  overflow: hidden;
  display: grid;
  gap: clamp(1.2rem, 4vw, 2.2rem);
}

.d3-08__head {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
}

.d3-08__intro {
  display: grid;
  gap: 0.45rem;
  max-inline-size: 42ch;
}

.d3-08__kicker {
  font: 600 0.66rem/1.4 ui-monospace, Menlo, monospace;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--d3-08-acc);
}

.d3-08__head strong {
  font: 600 clamp(1.6rem, 5.6vw, 3.1rem)/1.02 var(--d3-08-font-display);
  letter-spacing: -0.045em;
}

.d3-08__intro p {
  margin: 0.2rem 0 0;
  font: 450 clamp(0.78rem, 2.1vw, 0.92rem)/1.55 system-ui, sans-serif;
  color: var(--d3-08-mut);
  text-wrap: pretty;
}

.d3-08__intro code {
  font: 600 0.94em/1 ui-monospace, Menlo, monospace;
  color: var(--d3-08-ink);
}

.d3-08__meta {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.4rem 0.8rem;
  border-radius: 999px;
  border: 1px solid var(--d3-08-line);
  background: var(--d3-08-glass);
  font: 500 0.68rem/1.2 ui-monospace, Menlo, monospace;
  letter-spacing: 0.08em;
  color: var(--d3-08-mut);
}

.d3-08__meta i {
  inline-size: 7px;
  block-size: 7px;
  border-radius: 999px;
  background: var(--d3-08-acc);
  box-shadow: 0 0 0 4px color-mix(in oklab, var(--d3-08-acc) 22%, transparent);
}

.d3-08__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
  gap: clamp(0.75rem, 2.5vw, 1.25rem);
}

.d3-08__cell {
  display: grid;
  align-content: start;
  gap: 0.4rem;
  padding: clamp(0.9rem, 2.8vw, 1.25rem);
  border: 1px solid var(--d3-08-line);
  border-radius: 26px;
  background: linear-gradient(165deg, color-mix(in oklab, var(--d3-08-surf) 88%, transparent), color-mix(in oklab, var(--d3-08-surf) 52%, transparent));
  box-shadow: 0 30px 60px -40px #000, inset 0 1px 0 color-mix(in oklab, var(--d3-08-ink) 8%, transparent);
}

.d3-08__meta-row {
  display: flex;
  align-items: baseline;
  gap: 0.55rem;
  margin-block-start: 0.5rem;
}

.d3-08__idx {
  font: 600 0.68rem/1 ui-monospace, Menlo, monospace;
  color: var(--d3-08-acc2);
}

.d3-08__cell h3 {
  margin: 0;
  font: 600 clamp(1rem, 2.8vw, 1.15rem)/1.15 var(--d3-08-font-display);
  letter-spacing: -0.03em;
}

.d3-08__cell code {
  font: 600 clamp(0.66rem, 1.8vw, 0.74rem)/1.3 ui-monospace, Menlo, monospace;
  color: var(--d3-08-acc);
  overflow-wrap: anywhere;
}

.d3-08__cell p {
  margin: 0.2rem 0 0;
  font: 450 clamp(0.72rem, 1.95vw, 0.8rem)/1.5 system-ui, sans-serif;
  color: var(--d3-08-mut);
  text-wrap: pretty;
}

.d3-08__scene {
  position: relative;
  perspective: 820px;
  perspective-origin: 50% 42%;
  block-size: clamp(10rem, 27vw, 12.5rem);
  border-radius: 20px;
  display: grid;
  place-items: center;
  overflow: hidden;
  background: radial-gradient(closest-side, color-mix(in oklab, var(--d3-08-acc) 14%, transparent), transparent 76%), var(--d3-08-glass);
}

.d3-08__axis {
  position: absolute;
  inset-block: 12%;
  inset-inline-start: 50%;
  inline-size: 1px;
  background: repeating-linear-gradient(180deg, color-mix(in oklab, var(--d3-08-acc2) 70%, transparent) 0 5px, transparent 5px 10px);
}

.d3-08__axis--edge {
  inset-inline-start: calc(50% - clamp(2.9rem, 8vw, 3.9rem));
}

.d3-08__pivot {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: 8px;
  block-size: 8px;
  margin: -4px 0 0 -4px;
  border-radius: 999px;
  background: var(--d3-08-acc2);
  box-shadow: 0 0 0 5px color-mix(in oklab, var(--d3-08-acc2) 22%, transparent);
  z-index: 3;
}

.d3-08__pivot--edge {
  inset-inline-start: calc(50% - clamp(2.9rem, 8vw, 3.9rem));
}

.d3-08__pivot--deep {
  opacity: 0.4;
}

.d3-08__slab {
  transform-style: preserve-3d;
}

.d3-08__card,
.d3-08__panel,
.d3-08__tile {
  backface-visibility: hidden;
}

.d3-08__slab--spin {
  transform-origin: 50% 50% 0;
  animation: d3-08-turn 9s cubic-bezier(0.45, 0, 0.25, 1) infinite;
}

.d3-08__slab--hinge {
  transform-origin: 0% 50% 0;
  animation: d3-08-turn 9s cubic-bezier(0.45, 0, 0.25, 1) infinite;
}

.d3-08__slab--orbit {
  transform-origin: 50% 50% -120px;
  animation: d3-08-turn 9s cubic-bezier(0.45, 0, 0.25, 1) infinite;
}

@keyframes d3-08-turn {
  0% {
    transform: rotateY(-70deg);
  }

  50% {
    transform: rotateY(70deg);
  }

  100% {
    transform: rotateY(-70deg);
  }
}

.d3-08__card {
  inline-size: clamp(8.5rem, 24vw, 11rem);
  aspect-ratio: 1.586;
  padding: 0.7rem 0.8rem;
  display: grid;
  align-content: space-between;
  border-radius: 14px;
  color: #04140f;
  background: linear-gradient(150deg, var(--d3-08-acc) 0%, color-mix(in oklab, var(--d3-08-acc) 55%, var(--d3-08-acc3)) 100%);
  box-shadow: 0 22px 36px -20px #000, inset 0 1px 0 rgba(255, 255, 255, 0.45);
}

.d3-08__brand {
  font: 700 0.68rem/1 var(--d3-08-font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  opacity: 0.8;
}

.d3-08__bal {
  display: grid;
  gap: 0.05rem;
}

.d3-08__bal em {
  font: 600 0.56rem/1.2 ui-monospace, Menlo, monospace;
  font-style: normal;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  opacity: 0.7;
}

.d3-08__bal b {
  font: 650 clamp(0.95rem, 2.8vw, 1.2rem)/1 var(--d3-08-font-display);
  letter-spacing: -0.03em;
}

.d3-08__pan {
  font: 600 0.62rem/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.12em;
  opacity: 0.72;
}

.d3-08__list {
  position: absolute;
  inset: 16% 12% 16% 18%;
  display: grid;
  align-content: center;
  gap: 0.5rem;
}

.d3-08__list span {
  display: block;
  block-size: 0.5rem;
  border-radius: 999px;
  background: color-mix(in oklab, var(--d3-08-ink) 14%, transparent);
}

.d3-08__list span:nth-child(2) {
  inline-size: 74%;
}

.d3-08__list span:nth-child(3) {
  inline-size: 88%;
}

.d3-08__list span:nth-child(4) {
  inline-size: 62%;
}

.d3-08__panel {
  inline-size: clamp(6.5rem, 18vw, 8.5rem);
  padding: 0.65rem 0.7rem;
  display: grid;
  gap: 0.3rem;
  justify-items: start;
  border-radius: 14px;
  background: color-mix(in oklab, var(--d3-08-surf) 96%, var(--d3-08-ink));
  border: 1px solid var(--d3-08-line);
  box-shadow: 22px 22px 40px -22px #000;
}

.d3-08__panel b {
  font: 650 0.78rem/1 var(--d3-08-font-display);
  letter-spacing: -0.02em;
}

.d3-08__chip {
  padding: 0.22rem 0.5rem;
  border-radius: 999px;
  border: 1px solid var(--d3-08-line);
  font: 500 0.58rem/1.3 ui-monospace, Menlo, monospace;
  color: var(--d3-08-mut);
}

.d3-08__chip--on {
  background: var(--d3-08-acc);
  border-color: transparent;
  color: #04140f;
}

.d3-08__tile {
  inline-size: clamp(5.6rem, 15vw, 7rem);
  padding: 0.7rem;
  display: grid;
  justify-items: center;
  gap: 0.3rem;
  text-align: center;
  border-radius: 18px;
  background: color-mix(in oklab, var(--d3-08-surf) 92%, var(--d3-08-ink));
  border: 1px solid var(--d3-08-line);
  box-shadow: 0 22px 36px -22px #000;
}

.d3-08__ava {
  inline-size: 2.1rem;
  block-size: 2.1rem;
  border-radius: 999px;
  background: conic-gradient(from 210deg, var(--d3-08-acc), var(--d3-08-acc3), var(--d3-08-acc2), var(--d3-08-acc));
}

.d3-08__tile b {
  font: 650 0.72rem/1.1 var(--d3-08-font-display);
  letter-spacing: -0.02em;
}

.d3-08__tile em {
  font: 500 0.58rem/1.2 ui-monospace, Menlo, monospace;
  font-style: normal;
  color: var(--d3-08-mut);
}

@media (prefers-reduced-motion: reduce) {
  .d3-08__slab--spin,
    .d3-08__slab--hinge,
    .d3-08__slab--orbit {
    animation: none;
    transform: rotateY(34deg);
  }
}
```
