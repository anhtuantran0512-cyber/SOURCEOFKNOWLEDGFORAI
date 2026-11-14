---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/video-mimicking-subtle-wave-overlays/"
title: "Animated SVG Wave Layers"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "Four wave bands sliding across each other at different speeds and amplitudes — the layered-ocean hero, built the way it should be."
has_js: "false"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated SVG Wave Layers
Source: https://codefronts.com/motion/css-background-animations/video-mimicking-subtle-wave-overlays/

Four wave bands sliding across each other at different speeds and amplitudes — the layered-ocean hero, built the way it should be. Each wave is one seamlessly tiling SVG path duplicated end to end inside a 200%-wide layer, translated by exactly 50%, so the loop is mathematically invisible. Layers also bob vertically on a longer, coprime period, which is what stops the parallax from ever repeating a composition.
## HTML
```html
<section class="bga-07" aria-label="Layered animated SVG wave background demo">
  <div class="bga-07__sky" aria-hidden="true"></div>
  <div class="bga-07__sun" aria-hidden="true"></div>

  <div class="bga-07__sea" aria-hidden="true">
    <div class="bga-07__wrap" style="--bga-07-bob:9s">
      <div class="bga-07__layer" style="--bga-07-t:43s;--bga-07-o:.34;--bga-07-y:0px">
        <svg viewBox="0 0 1440 200" preserveAspectRatio="none"><path d="M0,96 C240,168 480,24 720,96 C960,168 1200,24 1440,96 L1440,200 L0,200 Z"/></svg>
        <svg viewBox="0 0 1440 200" preserveAspectRatio="none"><path d="M0,96 C240,168 480,24 720,96 C960,168 1200,24 1440,96 L1440,200 L0,200 Z"/></svg>
      </div>
    </div>
    <div class="bga-07__wrap" style="--bga-07-bob:7s">
      <div class="bga-07__layer" style="--bga-07-t:31s;--bga-07-o:.46;--bga-07-y:26px">
        <svg viewBox="0 0 1440 200" preserveAspectRatio="none"><path d="M0,110 C180,50 420,170 720,110 C1020,50 1260,170 1440,110 L1440,200 L0,200 Z"/></svg>
        <svg viewBox="0 0 1440 200" preserveAspectRatio="none"><path d="M0,110 C180,50 420,170 720,110 C1020,50 1260,170 1440,110 L1440,200 L0,200 Z"/></svg>
      </div>
    </div>
    <div class="bga-07__wrap" style="--bga-07-bob:5.5s">
      <div class="bga-07__layer bga-07__layer--rev" style="--bga-07-t:25s;--bga-07-o:.62;--bga-07-y:56px">
        <svg viewBox="0 0 1440 200" preserveAspectRatio="none"><path d="M0,120 C300,190 540,40 720,120 C900,200 1140,50 1440,120 L1440,200 L0,200 Z"/></svg>
        <svg viewBox="0 0 1440 200" preserveAspectRatio="none"><path d="M0,120 C300,190 540,40 720,120 C900,200 1140,50 1440,120 L1440,200 L0,200 Z"/></svg>
      </div>
    </div>
    <div class="bga-07__wrap" style="--bga-07-bob:4s">
      <div class="bga-07__layer" style="--bga-07-t:18s;--bga-07-o:1;--bga-07-y:92px">
        <svg viewBox="0 0 1440 200" preserveAspectRatio="none"><path d="M0,140 C220,80 460,196 720,140 C980,84 1220,196 1440,140 L1440,200 L0,200 Z"/></svg>
        <svg viewBox="0 0 1440 200" preserveAspectRatio="none"><path d="M0,140 C220,80 460,196 720,140 C980,84 1220,196 1440,140 L1440,200 L0,200 Z"/></svg>
      </div>
    </div>
  </div>

  <div class="bga-07__stage">
    <div class="bga-07__copy">
      <p class="bga-07__eyebrow">Layered motion · 07</p>
      <h1 class="bga-07__title">Four waves.<br>Coprime periods.<br>Never repeats.</h1>
      <p class="bga-07__sub">18s, 25s, 31s and 43s share no common factor, so the composition you are looking at will not occur again for over four hours.</p>
      <div class="bga-07__depths" aria-hidden="true">
        <span>43s</span><span>31s</span><span>25s</span><span>18s</span>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.bga-07,
.bga-07 *,
.bga-07 *::before,
.bga-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-07 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-07-deep: oklch(0.32 0.1 236);
  --bga-07-mid: oklch(0.55 0.13 210);
  --bga-07-foam: oklch(0.86 0.09 190);
  --bga-07-acc: oklch(0.85 0.14 88);
  background: oklch(0.19 0.05 258);
  color: oklch(0.98 0.008 220);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-07__sky {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,oklch(0.19 0.05 258) 0%,oklch(0.3 0.08 268) 38%,oklch(0.45 0.11 300) 62%,oklch(0.66 0.14 40) 88%,oklch(0.78 0.15 62) 100%);
}

.bga-07__sun {
  position: absolute;
  left: 50%;
  bottom: 26%;
  translate: -50% 0;
  width: min(38vw,340px);
  aspect-ratio: 1;
  border-radius: 50%;
  background: radial-gradient(circle,oklch(0.95 0.12 80) 0 42%,color-mix(in oklab,var(--bga-07-acc) 55%,transparent) 55%,transparent 72%);
  filter: blur(2px);
  animation: bga-07-rise 16s ease-in-out infinite alternate;
}

@keyframes bga-07-rise {
  to {
    translate: -50% -22px;
    filter: blur(6px);
  }
}

.bga-07__sea {
  position: absolute;
  inset-inline: 0;
  inset-block-end: 0;
  height: min(62%,520px);
  display: grid;
}

.bga-07__wrap {
  position: absolute;
  inset: 0;
  animation: bga-07-swell var(--bga-07-bob,7s) ease-in-out infinite alternate;
}

@keyframes bga-07-swell {
  to {
    translate: 0 -16px;
  }
}

.bga-07__layer {
  position: absolute;
  inset-block-end: 0;
  inset-inline-start: 0;
  width: 200%;
  display: flex;
  translate: 0 var(--bga-07-y,0);
  opacity: var(--bga-07-o,1);
  animation: bga-07-roll var(--bga-07-t,20s) linear infinite;
}

.bga-07__layer--rev {
  animation-direction: reverse;
}

.bga-07__layer svg {
  width: 50%;
  height: min(38vh,240px);
  display: block;
  flex: none;
}

.bga-07__layer:nth-of-type(1) path {
  fill: var(--bga-07-deep);
}

.bga-07__wrap:nth-child(1) path {
  fill: color-mix(in oklab,var(--bga-07-foam) 70%,transparent);
}

.bga-07__wrap:nth-child(2) path {
  fill: var(--bga-07-mid);
}

.bga-07__wrap:nth-child(3) path {
  fill: color-mix(in oklab,var(--bga-07-deep) 82%,oklch(0.2 0.06 250));
}

.bga-07__wrap:nth-child(4) path {
  fill: oklch(0.2 0.06 252);
}

@keyframes bga-07-roll {
  from {
    translate: 0 var(--bga-07-y,0);
  }

  to {
    translate: -50% var(--bga-07-y,0);
  }
}

.bga-07__stage {
  position: relative;
  z-index: 3;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,68px) clamp(22px,5vw,68px) clamp(160px,26vh,300px);
}

.bga-07__copy {
  width: min(100%,680px);
  display: grid;
  gap: 15px;
  justify-items: center;
  text-align: center;
}

.bga-07__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--bga-07-acc);
}

.bga-07__title {
  font-size: clamp(30px,6.2vw,64px);
  font-weight: 660;
  line-height: 1;
  letter-spacing: -.05em;
  text-wrap: balance;
  text-shadow: 0 4px 40px oklch(0.15 0.05 250/.6);
}

.bga-07__sub {
  max-width: 46ch;
  font-size: clamp(13.5px,1.3vw,16.5px);
  line-height: 1.58;
  color: oklch(0.96 0.01 220/.82);
  text-wrap: pretty;
  text-shadow: 0 1px 14px oklch(0.15 0.05 250/.7);
}

.bga-07__depths {
  display: flex;
  gap: 8px;
  margin-top: 8px;
}

.bga-07__depths span {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  padding: 6px 12px;
  border-radius: 99px;
  background: oklch(1 0 0/.12);
  border: 1px solid oklch(1 0 0/.2);
  color: oklch(0.98 0 0/.85);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

@media (prefers-reduced-motion: reduce) {
  .bga-07__layer,
    .bga-07__wrap,
    .bga-07__sun {
    animation: none;
  }
}
```
