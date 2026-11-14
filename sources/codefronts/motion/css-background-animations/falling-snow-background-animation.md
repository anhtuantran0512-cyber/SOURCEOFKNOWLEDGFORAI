---
source: "codefronts"
url: "https://codefronts.com/motion/css-background-animations/falling-snow-background-animation/"
title: "Falling Snow / Weather Effect"
section: "motion"
category: "css-background-animations"
category_name: "CSS Background Animations"
description: "A three-depth snowfall with real wind — and a pure-CSS weather switch that turns it into rain or a blizzard without a line of JavaScript."
has_js: "false"
---

Here's a working CSS Background Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Falling Snow / Weather Effect
Source: https://codefronts.com/motion/css-background-animations/falling-snow-background-animation/

A three-depth snowfall with real wind — and a pure-CSS weather switch that turns it into rain or a blizzard without a line of JavaScript. Flakes are tiled gradient layers, not hundreds of elements, so a dense storm costs three paint layers; a handful of larger foreground flakes are real elements that tumble as they fall.
## HTML
```html
<section class="bga-25" aria-label="Falling snow and weather background demo">
  <div class="bga-25__sky" aria-hidden="true"></div>
  <div class="bga-25__hills" aria-hidden="true"></div>
  <div class="bga-25__fog" aria-hidden="true"></div>

  <div class="bga-25__layer bga-25__layer--far" aria-hidden="true"></div>
  <div class="bga-25__layer bga-25__layer--mid" aria-hidden="true"></div>
  <div class="bga-25__layer bga-25__layer--near" aria-hidden="true"></div>

  <div class="bga-25__hero" aria-hidden="true">
    <span style="--bga-25-x:9%;--bga-25-t:11s;--bga-25-s:9px;--bga-25-d:-2s"></span>
    <span style="--bga-25-x:21%;--bga-25-t:15s;--bga-25-s:6px;--bga-25-d:-7s"></span>
    <span style="--bga-25-x:34%;--bga-25-t:9s;--bga-25-s:11px;--bga-25-d:-4s"></span>
    <span style="--bga-25-x:48%;--bga-25-t:13s;--bga-25-s:7px;--bga-25-d:-9s"></span>
    <span style="--bga-25-x:59%;--bga-25-t:17s;--bga-25-s:10px;--bga-25-d:-1s"></span>
    <span style="--bga-25-x:71%;--bga-25-t:10s;--bga-25-s:8px;--bga-25-d:-6s"></span>
    <span style="--bga-25-x:84%;--bga-25-t:14s;--bga-25-s:12px;--bga-25-d:-11s"></span>
    <span style="--bga-25-x:94%;--bga-25-t:12s;--bga-25-s:7px;--bga-25-d:-3s"></span>
  </div>

  <div class="bga-25__stage">
    <div class="bga-25__card">
      <p class="bga-25__eyebrow">Weather system · 25</p>
      <h1 class="bga-25__title">Three layers of snow.<br>One switch for rain.</h1>
      <p class="bga-25__sub">Bulk precipitation is tiled gradients; only the near flakes are real elements, so they can tumble. The mode switch is one <code>:has()</code> rule.</p>
      <div class="bga-25__switch" role="group" aria-label="Weather mode">
        <input class="bga-25__sr" type="radio" name="bga-25-w" id="bga-25-snow" checked>
        <label class="bga-25__chip" for="bga-25-snow">Snow</label>
        <input class="bga-25__sr" type="radio" name="bga-25-w" id="bga-25-blizzard">
        <label class="bga-25__chip" for="bga-25-blizzard">Blizzard</label>
        <input class="bga-25__sr" type="radio" name="bga-25-w" id="bga-25-rain">
        <label class="bga-25__chip" for="bga-25-rain">Rain</label>
        <input class="bga-25__sr" type="radio" name="bga-25-w" id="bga-25-clear">
        <label class="bga-25__chip" for="bga-25-clear">Clear</label>
      </div>
      <p class="bga-25__spec">tile-height translation · per-layer wind vector · :has() weather state</p>
    </div>
  </div>
</section>
```
## CSS
```css
.bga-25,
.bga-25 *,
.bga-25 *::before,
.bga-25 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bga-25 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  --bga-25-bg: oklch(0.28 0.04 250);
  --bga-25-flake: oklch(0.99 0.004 240);
  --bga-25-acc: oklch(0.84 0.1 230);
  --bga-25-op: 1;
  --bga-25-len: 2px;
  --bga-25-spd: 1;
  background: var(--bga-25-bg);
  color: oklch(0.97 0.008 240);
  font-family: ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  -webkit-font-smoothing: antialiased;
}

.bga-25__sky {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg,oklch(0.22 0.04 258) 0%,oklch(0.34 0.045 244) 54%,oklch(0.5 0.04 232) 100%);
}

.bga-25__hills {
  position: absolute;
  inset-inline: -6%;
  inset-block-end: -4%;
  height: 32%;
  background: radial-gradient(70% 130% at 18% 100%,oklch(0.9 0.012 232) 0 52%,transparent 54%), radial-gradient(64% 118% at 56% 100%,oklch(0.84 0.014 236) 0 52%,transparent 54%), radial-gradient(80% 140% at 92% 100%,oklch(0.94 0.01 230) 0 52%,transparent 54%);
}

.bga-25__fog {
  position: absolute;
  inset-inline: 0;
  inset-block-end: 0;
  height: 44%;
  pointer-events: none;
  background: linear-gradient(transparent,oklch(0.92 0.01 232/.28) 62%,oklch(0.96 0.008 230/.5));
  animation: bga-25-fog 22s ease-in-out infinite alternate;
}

@keyframes bga-25-fog {
  to {
    translate: -3% 0;
    opacity: .72;
  }
}

.bga-25__layer {
  position: absolute;
  inset: -8%;
  opacity: var(--bga-25-op);
  background-repeat: repeat;
  animation: bga-25-fall 14s linear infinite;
  animation-duration: calc(14s / var(--bga-25-spd));
}

.bga-25__layer--far {
  opacity: calc(var(--bga-25-op) * .45);
  background-image: radial-gradient(var(--bga-25-flake) 1px,transparent 1.4px);
  background-size: 97px 97px;
  animation-duration: calc(22s / var(--bga-25-spd));
}

.bga-25__layer--mid {
  opacity: calc(var(--bga-25-op) * .7);
  background-image: radial-gradient(var(--bga-25-flake) 1.4px,transparent 1.8px);
  background-size: 131px 131px;
  animation-duration: calc(16s / var(--bga-25-spd));
}

.bga-25__layer--near {
  filter: blur(.6px);
  background-image: radial-gradient(var(--bga-25-flake) 2px,transparent 2.5px);
  background-size: 173px 173px;
  animation-duration: calc(11s / var(--bga-25-spd));
}

@keyframes bga-25-fall {
  from {
    background-position: 0 0;
  }

  to {
    background-position: var(--bga-25-wind,40px) 173px;
  }
}

.bga-25__layer--far {
  --bga-25-wind: 18px;
}

.bga-25__layer--mid {
  --bga-25-wind: 36px;
}

.bga-25__layer--near {
  --bga-25-wind: 64px;
}

.bga-25__hero {
  position: absolute;
  inset: 0;
  opacity: var(--bga-25-op);
}

.bga-25__hero span {
  position: absolute;
  left: var(--bga-25-x);
  top: -8%;
  width: var(--bga-25-s);
  aspect-ratio: 1;
  border-radius: 50%;
  background: radial-gradient(circle at 34% 30%,oklch(1 0 0) 0 40%,oklch(0.94 0.01 230/.75) 70%,oklch(0.88 0.02 230/.2));
  box-shadow: 0 0 10px -1px oklch(1 0 0/.6);
  animation: bga-25-drop var(--bga-25-t) linear infinite,bga-25-tumble calc(var(--bga-25-t) * .27) ease-in-out infinite alternate;
  animation-delay: var(--bga-25-d,0s),0s;
}

@keyframes bga-25-drop {
  to {
    translate: 7vw 120vh;
  }
}

@keyframes bga-25-tumble {
  from {
    rotate: -40deg;
    scale: .85;
  }

  to {
    rotate: 40deg;
    scale: 1.12;
  }
}

.bga-25__stage {
  position: relative;
  z-index: 6;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  padding: clamp(22px,5vw,68px);
}

.bga-25__card {
  width: min(100%,660px);
  display: grid;
  gap: 15px;
  justify-items: center;
  text-align: center;
  padding: clamp(26px,3.8vw,48px);
  border-radius: 22px;
  background: oklch(0.24 0.04 250/.52);
  border: 1px solid oklch(1 0 0/.18);
  backdrop-filter: blur(20px) saturate(1.3);
  -webkit-backdrop-filter: blur(20px) saturate(1.3);
  box-shadow: 0 44px 100px -54px oklch(0.1 0.02 250/.9),inset 0 1px 0 oklch(1 0 0/.24);
}

.bga-25__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: var(--bga-25-acc);
}

.bga-25__title {
  font-size: clamp(26px,5.2vw,52px);
  font-weight: 620;
  line-height: 1.04;
  letter-spacing: -.05em;
  text-wrap: balance;
}

.bga-25__sub {
  max-width: 50ch;
  font-size: clamp(13.5px,1.3vw,16px);
  line-height: 1.6;
  color: oklch(0.95 0.008 240/.8);
  text-wrap: pretty;
}

.bga-25__sub code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  padding: 1px 5px;
  border-radius: 5px;
  background: oklch(1 0 0/.12);
}

.bga-25__switch {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  justify-content: center;
  margin-top: 4px;
}

.bga-25__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.bga-25__chip {
  display: inline-flex;
  align-items: center;
  min-height: 36px;
  padding: 0 16px;
  border-radius: 99px;
  cursor: pointer;
  font-size: 12.5px;
  font-weight: 560;
  color: oklch(1 0 0/.78);
  background: oklch(1 0 0/.08);
  border: 1px solid oklch(1 0 0/.16);
  transition: background .25s,color .25s,transform .25s;
}

.bga-25__chip:hover {
  background: oklch(1 0 0/.16);
  transform: translateY(-1px);
}

.bga-25__sr:checked + .bga-25__chip {
  background: oklch(0.99 0 0);
  color: oklch(0.26 0.04 250);
  border-color: transparent;
  font-weight: 660;
}

.bga-25__sr:focus-visible + .bga-25__chip {
  outline: 3px solid oklch(0.99 0 0);
  outline-offset: 3px;
}

.bga-25__spec {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: oklch(1 0 0/.42);
}

.bga-25:has(#bga-25-blizzard:checked) {
  --bga-25-op: 1.6;
  --bga-25-spd: 2.4;
}

.bga-25:has(#bga-25-blizzard:checked) .bga-25__layer {
  --bga-25-wind: 190px;
}

.bga-25:has(#bga-25-rain:checked) {
  --bga-25-spd: 11;
}

.bga-25:has(#bga-25-rain:checked) .bga-25__layer--far {
  background-image: linear-gradient(14deg,transparent 0 46%,oklch(0.9 0.02 230/.5) 46% 54%,transparent 54%);
  background-size: 97px 24px;
}

.bga-25:has(#bga-25-rain:checked) .bga-25__layer--mid {
  background-image: linear-gradient(14deg,transparent 0 47%,oklch(0.94 0.02 230/.6) 47% 53%,transparent 53%);
  background-size: 131px 32px;
}

.bga-25:has(#bga-25-rain:checked) .bga-25__layer--near {
  background-image: linear-gradient(14deg,transparent 0 48%,oklch(0.98 0.01 230/.7) 48% 52%,transparent 52%);
  background-size: 173px 44px;
}

.bga-25:has(#bga-25-rain:checked) .bga-25__hero {
  opacity: 0;
}

.bga-25:has(#bga-25-clear:checked) {
  --bga-25-op: 0;
}

@media (prefers-reduced-motion: reduce) {
  .bga-25__layer,
    .bga-25__hero span,
    .bga-25__fog {
    animation: none;
  }
}
```
