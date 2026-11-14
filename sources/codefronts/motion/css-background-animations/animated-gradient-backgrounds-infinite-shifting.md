---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/animated-gradient-backgrounds-infinite-shifting/"
title: "Full-Screen Linear Gradient Shift"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "The animated gradient every landing page reaches for — done properly."
has_js: "false"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full-Screen Linear Gradient Shift
Source: https://codefronts.com/motion/css-background-animations/animated-gradient-backgrounds-infinite-shifting/

The animated gradient every landing page reaches for — done properly. Instead of the usual 400% background-size hack that scrubs a static gradient sideways, this registers the angle and the colour stops themselves as typed custom properties with @property, so the browser interpolates real colour and real rotation on the compositor. Four palettes and three speeds are wired with radio chips and :has() — zero JavaScript, and the reader can feel each value before copying it.
## HTML
```html
<section class="bga-01" aria-label="Full-screen animated linear gradient background demo">
  <div class="bga-01__sky" aria-hidden="true"></div>
  <div class="bga-01__grain" aria-hidden="true"></div>

  <div class="bga-01__stage">
    <div class="bga-01__panel">
      <p class="bga-01__eyebrow">Ambient surface · 01</p>
      <h1 class="bga-01__title">Backgrounds that breathe, not blink.</h1>
      <p class="bga-01__sub">A single full-bleed layer, four registered custom properties, and eighteen seconds of colour that never repeats where you are looking.</p>
      <div class="bga-01__cta">
        <a class="bga-01__btn" href="#bga-01-demo">Copy the snippet</a>
        <a class="bga-01__btn bga-01__btn--ghost" href="#bga-01-demo">How it works</a>
      </div>
    </div>

    <div class="bga-01__controls" role="group" aria-label="Background options">
      <fieldset class="bga-01__set">
        <legend>Palette</legend>
        <input class="bga-01__sr" type="radio" name="bga-01-p" id="bga-01-p1" checked>
        <label class="bga-01__chip" for="bga-01-p1"><i style="background:linear-gradient(90deg,oklch(.62 .21 12),oklch(.6 .2 300))"></i>Ember</label>
        <input class="bga-01__sr" type="radio" name="bga-01-p" id="bga-01-p2">
        <label class="bga-01__chip" for="bga-01-p2"><i style="background:linear-gradient(90deg,oklch(.55 .16 240),oklch(.72 .14 190))"></i>Deep sea</label>
        <input class="bga-01__sr" type="radio" name="bga-01-p" id="bga-01-p3">
        <label class="bga-01__chip" for="bga-01-p3"><i style="background:linear-gradient(90deg,oklch(.74 .16 85),oklch(.6 .17 30))"></i>Citrus</label>
        <input class="bga-01__sr" type="radio" name="bga-01-p" id="bga-01-p4">
        <label class="bga-01__chip" for="bga-01-p4"><i style="background:linear-gradient(90deg,oklch(.3 .04 280),oklch(.5 .09 320))"></i>Graphite</label>
      </fieldset>
      <fieldset class="bga-01__set">
        <legend>Speed</legend>
        <input class="bga-01__sr" type="radio" name="bga-01-s" id="bga-01-s1">
        <label class="bga-01__chip" for="bga-01-s1">Glacial</label>
        <input class="bga-01__sr" type="radio" name="bga-01-s" id="bga-01-s2" checked>
        <label class="bga-01__chip" for="bga-01-s2">Default</label>
        <input class="bga-01__sr" type="radio" name="bga-01-s" id="bga-01-s3">
        <label class="bga-01__chip" for="bga-01-s3">Restless</label>
      </fieldset>
      <p class="bga-01__spec" id="bga-01-demo">@property &lt;color&gt; + &lt;angle&gt; interpolation · oklch stops · :has() state · grain dither</p>
    </div>
  </div>
</section>
```
## CSS
```css
@property --bga-01-a {
  syntax: '<angle>';
  inherits: false;
  initial-value: 120deg;
}

@property --bga-01-c1 {
  syntax: '<color>';
  inherits: false;
  initial-value: oklch(0.62 0.21 12);
}

@property --bga-01-c2 {
  syntax: '<color>';
  inherits: false;
  initial-value: oklch(0.55 0.19 330);
}

@property --bga-01-c3 {
  syntax: '<color>';
  inherits: false;
  initial-value: oklch(0.48 0.17 268);
}

.bga-01,
.bga-01 *,
.bga-01 *::before,
.bga-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-01 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-01-k1: oklch(0.62 0.21 12);
  --bga-01-k2: oklch(0.55 0.19 330);
  --bga-01-k3: oklch(0.48 0.17 268);
  --bga-01-dur: 18s;
  --bga-01-ink: oklch(0.99 0 0);
  background: var(--bga-01-k3);
  color: var(--bga-01-ink);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-01__sky {
  position: absolute;
  inset: -10%;
  --bga-01-a: 120deg;
  --bga-01-c1: var(--bga-01-k1);
  --bga-01-c2: var(--bga-01-k2);
  --bga-01-c3: var(--bga-01-k3);
  background: linear-gradient(var(--bga-01-a),var(--bga-01-c1) 0%,var(--bga-01-c2) 48%,var(--bga-01-c3) 100%);
  animation: bga-01-drift var(--bga-01-dur) linear infinite;
}

@keyframes bga-01-drift {
  25% {
    --bga-01-c1: var(--bga-01-k2);
    --bga-01-c2: var(--bga-01-k3);
    --bga-01-c3: var(--bga-01-k1);
  }

  50% {
    --bga-01-c1: var(--bga-01-k3);
    --bga-01-c2: var(--bga-01-k1);
    --bga-01-c3: var(--bga-01-k2);
  }

  75% {
    --bga-01-c1: var(--bga-01-k1);
    --bga-01-c2: var(--bga-01-k3);
    --bga-01-c3: var(--bga-01-k2);
  }

  100% {
    --bga-01-a: 480deg;
    --bga-01-c1: var(--bga-01-k1);
    --bga-01-c2: var(--bga-01-k2);
    --bga-01-c3: var(--bga-01-k3);
  }
}

.bga-01__grain {
  position: absolute;
  inset: 0;
  pointer-events: none;
  mix-blend-mode: overlay;
  opacity: .5;
  background-image: radial-gradient(oklch(1 0 0/.5) .5px,transparent .6px),radial-gradient(oklch(0 0 0/.5) .5px,transparent .6px);
  background-size: 3px 3px,4px 4px;
  background-position: 0 0,1px 2px;
  animation: bga-01-grain 1.1s steps(3) infinite;
}

@keyframes bga-01-grain {
  33% {
    background-position: 1px 2px,2px 0;
  }

  66% {
    background-position: 2px 1px,0 1px;
  }
}

.bga-01__stage {
  position: relative;
  z-index: 2;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(20px,3vw,34px);
  padding: clamp(22px,5vw,68px);
  text-align: center;
}

.bga-01__panel {
  width: min(100%,760px);
  display: grid;
  gap: clamp(12px,1.6vw,18px);
  justify-items: center;
  padding: clamp(24px,3.4vw,44px);
  border-radius: 26px;
  background: oklch(0.15 0.03 285/.3);
  border: 1px solid oklch(1 0 0/.18);
  backdrop-filter: blur(22px) saturate(1.4);
  -webkit-backdrop-filter: blur(22px) saturate(1.4);
  box-shadow: 0 30px 80px -30px oklch(0.1 0.04 280/.7),inset 0 1px 0 oklch(1 0 0/.24);
}

.bga-01__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: oklch(1 0 0/.72);
}

.bga-01__title {
  font-size: clamp(30px,6.4vw,66px);
  font-weight: 640;
  line-height: 1.02;
  letter-spacing: -.045em;
  text-wrap: balance;
  text-shadow: 0 2px 30px oklch(0.15 0.05 290/.45);
}

.bga-01__sub {
  max-width: 52ch;
  font-size: clamp(14px,1.35vw,17px);
  line-height: 1.55;
  color: oklch(1 0 0/.8);
  text-wrap: pretty;
}

.bga-01__cta {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  justify-content: center;
  margin-top: 6px;
}

.bga-01__btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 46px;
  padding: 0 24px;
  border-radius: 99px;
  font-size: 14.5px;
  font-weight: 600;
  letter-spacing: -.01em;
  text-decoration: none;
  background: oklch(0.99 0 0);
  color: oklch(0.2 0.03 285);
  transition: transform .4s cubic-bezier(.16,1,.3,1),box-shadow .4s,background .3s;
}

.bga-01__btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 14px 30px -12px oklch(0 0 0/.6);
}

.bga-01__btn--ghost {
  background: oklch(1 0 0/.1);
  color: oklch(0.99 0 0);
  border: 1px solid oklch(1 0 0/.35);
}

.bga-01__btn--ghost:hover {
  background: oklch(1 0 0/.2);
}

.bga-01__btn:focus-visible,
.bga-01__chip:focus-visible {
  outline: 3px solid oklch(0.99 0 0);
  outline-offset: 3px;
}

.bga-01__controls {
  display: flex;
  flex-wrap: wrap;
  gap: 10px 18px;
  align-items: center;
  justify-content: center;
}

.bga-01__set {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 7px;
  border: 0;
}

.bga-01__set legend {
  float: left;
  margin-inline-end: 10px;
  padding-top: 9px;
  font-size: 10.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: oklch(1 0 0/.6);
}

.bga-01__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.bga-01__chip {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  min-height: 34px;
  padding: 0 14px;
  border-radius: 99px;
  cursor: pointer;
  font-size: 12.5px;
  font-weight: 550;
  color: oklch(1 0 0/.78);
  background: oklch(1 0 0/.08);
  border: 1px solid oklch(1 0 0/.16);
  transition: background .25s,color .25s,border-color .25s,transform .25s;
}

.bga-01__chip:hover {
  background: oklch(1 0 0/.16);
  transform: translateY(-1px);
}

.bga-01__chip i {
  width: 14px;
  height: 14px;
  border-radius: 5px;
  box-shadow: inset 0 0 0 1px oklch(0 0 0/.2);
}

.bga-01__sr:checked + .bga-01__chip {
  background: oklch(0.99 0 0);
  color: oklch(0.2 0.03 285);
  border-color: transparent;
  font-weight: 640;
}

.bga-01__sr:focus-visible + .bga-01__chip {
  outline: 3px solid oklch(0.99 0 0);
  outline-offset: 3px;
}

.bga-01__spec {
  width: 100%;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: oklch(1 0 0/.55);
  text-align: center;
  padding-top: 4px;
}

.bga-01:has(#bga-01-p2:checked) {
  --bga-01-k1: oklch(0.55 0.16 240);
  --bga-01-k2: oklch(0.72 0.14 190);
  --bga-01-k3: oklch(0.34 0.1 258);
}

.bga-01:has(#bga-01-p3:checked) {
  --bga-01-k1: oklch(0.74 0.16 85);
  --bga-01-k2: oklch(0.6 0.17 30);
  --bga-01-k3: oklch(0.42 0.12 55);
}

.bga-01:has(#bga-01-p4:checked) {
  --bga-01-k1: oklch(0.3 0.04 280);
  --bga-01-k2: oklch(0.5 0.09 320);
  --bga-01-k3: oklch(0.22 0.03 270);
}

.bga-01:has(#bga-01-s1:checked) {
  --bga-01-dur: 46s;
}

.bga-01:has(#bga-01-s3:checked) {
  --bga-01-dur: 6s;
}

@media (max-width: 640px) {
  .bga-01__set legend {
    width: 100%;
    float: none;
    padding: 0 0 2px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bga-01__sky,
    .bga-01__grain {
    animation: none;
  }

  .bga-01__btn {
    transition: none;
  }
}
```
