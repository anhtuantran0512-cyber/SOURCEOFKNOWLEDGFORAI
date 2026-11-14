---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/diagonal-moving-stripes-pattern/"
title: "Diagonal Moving Stripes Pattern"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "The barber-pole stripe, engineered instead of hacked."
has_js: "false"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Diagonal Moving Stripes Pattern
Source: https://codefronts.com/motion/css-background-animations/diagonal-moving-stripes-pattern/

The barber-pole stripe, engineered instead of hacked. Because the stripe angle is a registered <angle> property it can be animated, not just set — so the pattern can rotate mid-loop, something the classic repeating-linear-gradient(45deg,…) approach can never do. Two counter-moving stripe layers with a soft-light blend create the moiré depth, and stripe width, pitch and speed are all live controls.
## HTML
```html
<section class="bga-06" aria-label="Diagonal moving stripes background demo">
  <div class="bga-06__a" aria-hidden="true"></div>
  <div class="bga-06__b" aria-hidden="true"></div>
  <div class="bga-06__sheen" aria-hidden="true"></div>

  <div class="bga-06__stage">
    <div class="bga-06__plate">
      <p class="bga-06__kicker">Pattern engine · 06</p>
      <h1 class="bga-06__title">Stripes that actually<br>loop seamlessly.</h1>
      <p class="bga-06__sub">Translate by one period times sec(θ) and the seam disappears. Everything else is two gradients and a blend mode.</p>

      <div class="bga-06__controls" role="group" aria-label="Stripe options">
        <div class="bga-06__set">
          <span class="bga-06__lab">Pitch</span>
          <input class="bga-06__sr" type="radio" name="bga-06-w" id="bga-06-w1">
          <label class="bga-06__chip" for="bga-06-w1">Fine</label>
          <input class="bga-06__sr" type="radio" name="bga-06-w" id="bga-06-w2" checked>
          <label class="bga-06__chip" for="bga-06-w2">Medium</label>
          <input class="bga-06__sr" type="radio" name="bga-06-w" id="bga-06-w3">
          <label class="bga-06__chip" for="bga-06-w3">Awning</label>
        </div>
        <div class="bga-06__set">
          <span class="bga-06__lab">Tempo</span>
          <input class="bga-06__sr" type="radio" name="bga-06-s" id="bga-06-s1">
          <label class="bga-06__chip" for="bga-06-s1">Slow</label>
          <input class="bga-06__sr" type="radio" name="bga-06-s" id="bga-06-s2" checked>
          <label class="bga-06__chip" for="bga-06-s2">Steady</label>
          <input class="bga-06__sr" type="radio" name="bga-06-s" id="bga-06-s3">
          <label class="bga-06__chip" for="bga-06-s3">Rush</label>
        </div>
      </div>
      <p class="bga-06__spec">period × sec(45°) = 1.4142 · soft-light moiré · registered &lt;angle&gt;</p>
    </div>
  </div>
</section>
```
## CSS
```css
@property --bga-06-a {
  syntax: '<angle>';
  inherits: true;
  initial-value: 45deg;
}

.bga-06,
.bga-06 *,
.bga-06 *::before,
.bga-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-06 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-06-a: 45deg;
  --bga-06-w: 26px;
  --bga-06-dur: 7s;
  --bga-06-c1: oklch(0.22 0.03 275);
  --bga-06-c2: oklch(0.27 0.05 285);
  --bga-06-acc: oklch(0.82 0.17 96);
  background: var(--bga-06-c1);
  color: oklch(0.97 0.01 280);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-06__a,
.bga-06__b {
  position: absolute;
  inset: -10%;
  background-size: 200% 200%;
}

.bga-06__a {
  background-image: repeating-linear-gradient(var(--bga-06-a),
      var(--bga-06-c1) 0 var(--bga-06-w),var(--bga-06-c2) var(--bga-06-w) calc(var(--bga-06-w) * 2));
  animation: bga-06-slide var(--bga-06-dur) linear infinite;
}

.bga-06__b {
  mix-blend-mode: soft-light;
  opacity: .85;
  background-image: repeating-linear-gradient(var(--bga-06-a),
      color-mix(in oklab,var(--bga-06-acc) 26%,transparent) 0 calc(var(--bga-06-w) * 1.62),
      transparent calc(var(--bga-06-w) * 1.62) calc(var(--bga-06-w) * 3.24));
  animation: bga-06-slide-r calc(var(--bga-06-dur) * 1.7) linear infinite;
}

@keyframes bga-06-slide {
  to {
    background-position: calc(var(--bga-06-w) * 2.8284) 0;
  }
}

@keyframes bga-06-slide-r {
  to {
    background-position: calc(var(--bga-06-w) * -4.5820) 0;
  }
}

.bga-06__sheen {
  position: absolute;
  inset: 0;
  pointer-events: none;
  mix-blend-mode: screen;
  background: linear-gradient(var(--bga-06-a),transparent 35%,color-mix(in oklab,var(--bga-06-acc) 20%,transparent) 50%,transparent 65%);
  background-size: 260% 260%;
  animation: bga-06-sheen 11s ease-in-out infinite;
}

@keyframes bga-06-sheen {
  0% {
    background-position: 0% 0%;
  }

  50% {
    background-position: 100% 100%;
  }

  100% {
    background-position: 0% 0%;
  }
}

.bga-06__stage {
  position: relative;
  z-index: 2;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,68px);
}

.bga-06__plate {
  width: min(100%,720px);
  display: grid;
  gap: 16px;
  padding: clamp(26px,3.8vw,50px);
  background: oklch(0.13 0.02 280/.78);
  border: 1px solid oklch(1 0 0/.12);
  border-radius: 2px;
  border-inline-start: 5px solid var(--bga-06-acc);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  box-shadow: 0 40px 90px -46px oklch(0 0 0/.95);
}

.bga-06__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--bga-06-acc);
}

.bga-06__title {
  font-size: clamp(28px,5.4vw,56px);
  font-weight: 660;
  line-height: 1.03;
  letter-spacing: -.05em;
  text-wrap: balance;
}

.bga-06__sub {
  max-width: 50ch;
  font-size: clamp(13.5px,1.3vw,16px);
  line-height: 1.6;
  color: oklch(0.92 0.01 280/.76);
  text-wrap: pretty;
}

.bga-06__controls {
  display: flex;
  flex-wrap: wrap;
  gap: 12px 24px;
  margin-top: 6px;
}

.bga-06__set {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 7px;
}

.bga-06__lab {
  font-size: 10.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(1 0 0/.5);
}

.bga-06__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.bga-06__chip {
  display: inline-flex;
  align-items: center;
  min-height: 34px;
  padding: 0 14px;
  cursor: pointer;
  font-size: 12.5px;
  font-weight: 550;
  color: oklch(1 0 0/.75);
  background: oklch(1 0 0/.06);
  border: 1px solid oklch(1 0 0/.16);
  transition: background .22s,color .22s;
}

.bga-06__chip:hover {
  background: oklch(1 0 0/.14);
}

.bga-06__sr:checked + .bga-06__chip {
  background: var(--bga-06-acc);
  color: oklch(0.2 0.04 90);
  border-color: transparent;
  font-weight: 660;
}

.bga-06__sr:focus-visible + .bga-06__chip {
  outline: 3px solid var(--bga-06-acc);
  outline-offset: 3px;
}

.bga-06__spec {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: oklch(1 0 0/.42);
  padding-top: 4px;
}

.bga-06:has(#bga-06-w1:checked) {
  --bga-06-w: 12px;
}

.bga-06:has(#bga-06-w3:checked) {
  --bga-06-w: 54px;
}

.bga-06:has(#bga-06-s1:checked) {
  --bga-06-dur: 18s;
}

.bga-06:has(#bga-06-s3:checked) {
  --bga-06-dur: 2.6s;
}

@media (prefers-reduced-motion: reduce) {
  .bga-06__a,
    .bga-06__b,
    .bga-06__sheen {
    animation: none;
  }
}
```
