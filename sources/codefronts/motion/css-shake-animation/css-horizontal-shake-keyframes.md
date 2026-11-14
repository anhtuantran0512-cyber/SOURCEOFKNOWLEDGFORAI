---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-horizontal-shake-keyframes/"
title: "CSS Horizontal Shake Keyframes"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "The X-axis shake as a wall chart: a large specimen looping the canonical decaying keyframes above a live amplitude graph (each bar = one keyframe's offset,…"
has_js: "false"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Horizontal Shake Keyframes
Source: https://codefronts.com/motion/css-shake-animation/css-horizontal-shake-keyframes/

The X-axis shake as a wall chart: a large specimen looping the canonical decaying keyframes above a live amplitude graph (each bar = one keyframe's offset, drawn in CSS), and a side-by-side of the two horizontal personalities — eased decay ('human') versus steps() buzz ('machine') — so you can feel why easing choice matters more than pixel values.
## HTML
```html
<div class="shk-22-group">
<link href="https://fonts.googleapis.com/css2?family=Archivo:[email protected]&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
<section class="shk-22a" aria-label="Canonical horizontal shake with amplitude graph">
  <div class="shk-22a__chart">
    <p class="shk-22a__no">Fig. 01 — shake-x</p>
    <div class="shk-22a__stage"><div class="shk-22a__spec">SHAKE</div></div>
    <div class="shk-22a__graph" aria-label="Amplitude per keyframe: -8, 7, -6, 4, -2, 1 pixels">
      <div class="shk-22a__axis" aria-hidden="true"></div>
      <div class="shk-22a__bars" aria-hidden="true">
        <i style="--v:-8px"></i><i style="--v:7px"></i><i style="--v:-6px"></i><i style="--v:4px"></i><i style="--v:-2px"></i><i style="--v:1px"></i>
      </div>
      <p class="shk-22a__ticks" aria-hidden="true"><span>10%</span><span>25%</span><span>40%</span><span>55%</span><span>70%</span><span>85%</span></p>
    </div>
    <p class="shk-22a__read">alternate the sign · shrink the magnitude · let keyframes interpolate the zero-crossings</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
<section class="shk-22b" aria-label="Eased decay versus stepped buzz comparison">
  <div class="shk-22b__duo">
    <div class="shk-22b__cell">
      <div class="shk-22b__box shk-22b__box--human" tabindex="0">HUMAN</div>
      <code class="shk-22b__code">cubic-bezier(.36,.07,.19,.97)<br>6 decaying frames</code>
    </div>
    <div class="shk-22b__cell">
      <div class="shk-22b__box shk-22b__box--machine" tabindex="0">MACHINE</div>
      <code class="shk-22b__code">steps(2, jump-none)<br>2 symmetric frames</code>
    </div>
  </div>
  <p class="shk-22b__hint" aria-hidden="true">hover each — same axis, same amplitude family, opposite soul</p>
</section>
</div>
```
## CSS
```css
.shk-22-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-22-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-22a,
.shk-22a *,
.shk-22a *::before,
.shk-22a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-22a {
  --ink: #191d16;
  --acid: oklch(0.85 0.19 128);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #e8ebe3;
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
}

.shk-22a__chart {
  width: min(520px,100%);
  padding: 34px 36px;
  background: #f6f8f2;
  border: 2px solid var(--ink);
  border-radius: 4px;
  box-shadow: 8px 8px 0 var(--ink);
}

.shk-22a__no {
  font-family: 'IBM Plex Mono',ui-monospace,monospace;
  font-size: 11.5px;
  font-weight: 600;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--ink);
}

.shk-22a__stage {
  margin-top: 18px;
  display: grid;
  place-items: center;
  padding: 34px;
  background: var(--ink);
  border-radius: 3px;
}

.shk-22a__spec {
  padding: 16px 34px;
  font-size: 26px;
  font-weight: 900;
  letter-spacing: .06em;
  color: var(--ink);
  background: var(--acid);
  border-radius: 3px;
  animation: shk-22a-x 2.6s cubic-bezier(.36,.07,.19,.97) infinite;
}

.shk-22a__graph {
  margin-top: 22px;
  position: relative;
}

.shk-22a__axis {
  position: absolute;
  left: 0;
  right: 0;
  top: 34px;
  height: 1.5px;
  background: rgba(25,29,22,.25);
}

.shk-22a__bars {
  display: flex;
  gap: 14px;
  justify-content: center;
  height: 68px;
}

.shk-22a__bars i {
  align-self: flex-start;
  margin-top: 34px;
  width: 26px;
  height: calc(max(var(--v), var(--v) * -1) * 4);
  translate: 0 calc(max(var(--v), 0px) * -4);
  background: var(--ink);
  border-radius: 2px;
}

.shk-22a__bars i:nth-child(even) {
  background: oklch(0.55 0.14 128);
}

.shk-22a__ticks {
  display: flex;
  gap: 14px;
  justify-content: center;
  font-family: 'IBM Plex Mono',ui-monospace,monospace;
  font-size: 9.5px;
  color: rgba(25,29,22,.55);
}

.shk-22a__ticks span {
  width: 26px;
  text-align: center;
}

.shk-22a__read {
  margin-top: 18px;
  font-size: 12.5px;
  font-weight: 600;
  color: rgba(25,29,22,.65);
  text-align: center;
  text-wrap: pretty;
}

@keyframes shk-22a-x {
  2% {
    translate: -8px 0;
  }

  5% {
    translate: 7px 0;
  }

  8% {
    translate: -6px 0;
  }

  11% {
    translate: 4px 0;
  }

  14% {
    translate: -2px 0;
  }

  17% {
    translate: 1px 0;
  }

  19%,
    100% {
    translate: 0 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-22a__spec {
    animation: none;
  }
}

.shk-22b,
.shk-22b *,
.shk-22b *::before,
.shk-22b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-22b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-content: center;
  gap: 26px;
  padding: 48px 24px;
  background: linear-gradient(180deg,#111318,#0b0d11);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-22b__duo {
  display: flex;
  flex-wrap: wrap;
  gap: 26px;
  justify-content: center;
}

.shk-22b__cell {
  display: grid;
  gap: 14px;
  justify-items: center;
}

.shk-22b__box {
  display: grid;
  place-items: center;
  width: min(230px,70vw);
  height: 120px;
  border-radius: 16px;
  font-size: 20px;
  font-weight: 700;
  letter-spacing: .08em;
  cursor: default;
  outline: none;
}

.shk-22b__box--human {
  color: #101318;
  background: linear-gradient(180deg,oklch(0.88 0.1 165),oklch(0.78 0.13 165));
}

.shk-22b__box--machine {
  color: oklch(0.85 0.15 25);
  background: #181114;
  border: 1.5px solid oklch(0.6 0.2 25 / .5);
}

.shk-22b__box--human:hover,
.shk-22b__box--human:focus-visible {
  animation: shk-22b-human .55s cubic-bezier(.36,.07,.19,.97);
}

.shk-22b__box--machine:hover,
.shk-22b__box--machine:focus-visible {
  animation: shk-22b-machine .1s steps(2,jump-none) infinite;
}

.shk-22b__code {
  font-family: 'IBM Plex Mono',ui-monospace,monospace;
  font-size: 11.5px;
  line-height: 1.7;
  text-align: center;
  color: rgba(220,230,245,.55);
}

.shk-22b__hint {
  text-align: center;
  font-size: 12px;
  color: rgba(220,230,245,.4);
}

@keyframes shk-22b-human {
  10% {
    translate: -8px 0;
  }

  25% {
    translate: 7px 0;
  }

  40% {
    translate: -6px 0;
  }

  55% {
    translate: 4px 0;
  }

  70% {
    translate: -2px 0;
  }

  85% {
    translate: 1px 0;
  }
}

@keyframes shk-22b-machine {
  0% {
    translate: -3px 0;
  }

  100% {
    translate: 3px 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-22b__box:hover,
    .shk-22b__box:focus-visible {
    animation: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — the bar chart IS the keyframe table: each bar's height/offset derives from its --v via calc(), so the graph and the animation can never disagree. */

/* No JavaScript — HUMAN plays once and decays (feedback); MACHINE loops steps(2) until the cursor leaves (malfunction). Choosing between them is choosing what story the motion tells. */
```
