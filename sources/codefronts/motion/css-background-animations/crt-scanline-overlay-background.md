---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/crt-scanline-overlay-background/"
title: "CRT Scanline Overlay Background"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "A CRT that actually behaves like one: an aperture-grille RGB triad at sub-pixel scale, horizontal scanlines at a different pitch, a rolling refresh bar that…"
has_js: "false"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CRT Scanline Overlay Background
Source: https://codefronts.com/motion/css-background-animations/crt-scanline-overlay-background/

A CRT that actually behaves like one: an aperture-grille RGB triad at sub-pixel scale, horizontal scanlines at a different pitch, a rolling refresh bar that drifts down the tube, phosphor bloom, barrel-vignette curvature, and a chromatic-aberration text shadow. Every layer is a gradient — no images, no canvas, no JavaScript.
## HTML
```html
<section class="bga-12" aria-label="CRT scanline retro monitor background demo">
  <div class="bga-12__phosphor" aria-hidden="true"></div>
  <div class="bga-12__grille" aria-hidden="true"></div>
  <div class="bga-12__scan" aria-hidden="true"></div>
  <div class="bga-12__roll" aria-hidden="true"></div>
  <div class="bga-12__glass" aria-hidden="true"></div>

  <div class="bga-12__stage">
    <div class="bga-12__term">
      <p class="bga-12__line bga-12__line--dim">CODEFRONTS CRT EMULATOR v2.7 — 640×480 @ 60Hz</p>
      <h1 class="bga-12__title">READY.</h1>
      <p class="bga-12__body">Aperture grille at 3px. Scanlines at 4px. Coprime pitches, so the two grids never resolve into a checkerboard.</p>
      <ul class="bga-12__list">
        <li><span>MASK</span>RGB triad · repeating-linear-gradient 90deg</li>
        <li><span>SCAN</span>2px on / 2px off · 34% black</li>
        <li><span>ROLL</span>translate 9s linear · vertical hold drift</li>
        <li><span>CONV</span>±1px red / cyan text-shadow</li>
      </ul>
      <p class="bga-12__prompt">&gt;&nbsp;<span class="bga-12__caret"></span></p>
    </div>
  </div>
</section>
```
## CSS
```css
.bga-12,
.bga-12 *,
.bga-12 *::before,
.bga-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-12 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-12-ph: oklch(0.86 0.19 148);
  --bga-12-bg: oklch(0.16 0.035 155);
  background: oklch(0.09 0.02 155);
  color: var(--bga-12-ph);
  font-family: ui-monospace,'SFMono-Regular',Menlo,Consolas,monospace;
  -webkit-font-smoothing: antialiased;
}

.bga-12__phosphor {
  position: absolute;
  inset: 0;
  background: radial-gradient(100% 82% at 50% 46%,var(--bga-12-bg),oklch(0.08 0.015 155) 78%);
  animation: bga-12-hum 5.2s steps(6) infinite;
}

@keyframes bga-12-hum {
  0%,
    100% {
    filter: brightness(.96);
  }

  50% {
    filter: brightness(1.12);
  }
}

.bga-12__grille {
  position: absolute;
  inset: 0;
  pointer-events: none;
  mix-blend-mode: overlay;
  opacity: .85;
  background: repeating-linear-gradient(90deg,
      oklch(0.62 0.22 25/.2) 0 1px,oklch(0.75 0.22 145/.2) 1px 2px,oklch(0.6 0.22 265/.2) 2px 3px);
}

.bga-12__scan {
  position: absolute;
  inset: -4px 0 0;
  pointer-events: none;
  background: repeating-linear-gradient(oklch(0 0 0/.4) 0 2px,transparent 2px 4px);
  animation: bga-12-scan 2.6s linear infinite;
}

@keyframes bga-12-scan {
  to {
    background-position: 0 4px;
  }
}

.bga-12__roll {
  position: absolute;
  inset-inline: 0;
  top: -34%;
  height: 30%;
  pointer-events: none;
  mix-blend-mode: screen;
  opacity: .62;
  background: linear-gradient(oklch(1 0 0/0) 0 6%,oklch(0.9 0.06 150/.3) 44%,oklch(0.97 0.05 150/.5) 84%,oklch(1 0 0/.34) 96%,oklch(1 0 0/0));
  animation: bga-12-roll 6.5s linear infinite;
}

@keyframes bga-12-roll {
  to {
    translate: 0 460%;
  }
}

.bga-12__glass {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(60% 40% at 26% 6%,oklch(1 0 0/.07),transparent 62%), radial-gradient(132% 112% at 50% 50%,transparent 52%,oklch(0 0 0/.86) 100%);
}

.bga-12__stage {
  position: relative;
  z-index: 4;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,70px);
}

.bga-12__term {
  width: min(100%,720px);
  display: grid;
  gap: 14px;
  animation: bga-12-track 7.4s steps(1) infinite;
  text-shadow: 1px 0 0 oklch(0.6 0.22 25/.55),-1px 0 0 oklch(0.7 0.16 210/.55),0 0 18px color-mix(in oklab,var(--bga-12-ph) 55%,transparent);
}

.bga-12__line {
  font-size: clamp(10.5px,1.1vw,12.5px);
  letter-spacing: .12em;
  text-transform: uppercase;
}

.bga-12__line--dim {
  color: color-mix(in oklab,var(--bga-12-ph) 58%,transparent);
}

.bga-12__title {
  font-size: clamp(34px,8vw,86px);
  font-weight: 700;
  letter-spacing: .02em;
  line-height: 1;
}

.bga-12__body {
  max-width: 56ch;
  font-size: clamp(12.5px,1.25vw,15px);
  line-height: 1.65;
  color: color-mix(in oklab,var(--bga-12-ph) 82%,transparent);
  text-wrap: pretty;
}

.bga-12__list {
  list-style: none;
  display: grid;
  gap: 6px;
  margin-top: 6px;
  padding: 16px;
  border: 1px solid color-mix(in oklab,var(--bga-12-ph) 26%,transparent);
  background: oklch(0.12 0.03 155/.5);
}

.bga-12__list li {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  font-size: clamp(11px,1.1vw,13px);
  color: color-mix(in oklab,var(--bga-12-ph) 78%,transparent);
}

.bga-12__list span {
  min-width: 56px;
  font-weight: 700;
  color: var(--bga-12-ph);
}

.bga-12__prompt {
  display: flex;
  align-items: center;
  font-size: clamp(14px,1.6vw,20px);
}

.bga-12__caret {
  display: inline-block;
  width: .62em;
  height: 1.05em;
  background: var(--bga-12-ph);
  animation: bga-12-blink 1.06s steps(1) infinite;
}

@keyframes bga-12-blink {
  50% {
    opacity: 0;
  }
}

@keyframes bga-12-track {
  0%,
    42% {
    translate: 0 0;
  }

  43% {
    translate: -3px 1px;
  }

  44%,
    86% {
    translate: 0 0;
  }

  87% {
    translate: 2px -1px;
  }

  88%,
    100% {
    translate: 0 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bga-12__phosphor,
    .bga-12__roll,
    .bga-12__caret,
    .bga-12__scan,
    .bga-12__term {
    animation: none;
  }

  .bga-12__roll {
    opacity: .18;
    top: 22%;
  }
}
```
