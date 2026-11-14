---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-3d-shake-transform/"
title: "CSS 3D Shake Transform"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "The Z-axis joins the shake: a holo boarding pass whose layers sit at real translateZ depths inside a perspective camera — jitter the card and parallax…"
has_js: "false"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS 3D Shake Transform
Source: https://codefronts.com/motion/css-shake-animation/css-3d-shake-transform/

The Z-axis joins the shake: a holo boarding pass whose layers sit at real translateZ depths inside a perspective camera — jitter the card and parallax happens for free — and a coin that wobbles on rotate3d like it was dropped on a table, settling from wild precession to flat.
## HTML
```html
<div class="shk-28-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
<section class="shk-28a" aria-label="Layered boarding pass that judders in 3D on hover">
  <div class="shk-28a__scene">
    <div class="shk-28a__pass" tabindex="0">
      <div class="shk-28a__glow" aria-hidden="true"></div>
      <p class="shk-28a__route">SEA <span aria-hidden="true">⟶</span> TYO</p>
      <div class="shk-28a__chip" aria-hidden="true"></div>
      <p class="shk-28a__name">M. OKAFOR</p>
      <p class="shk-28a__meta"><span>GATE D14</span><span>SEAT 02A</span><span>BOARD 21:40</span></p>
      <p class="shk-28a__strip" aria-hidden="true">|||‖|‖|||‖||‖‖|||‖|||‖‖||</p>
    </div>
  </div>
  <p class="shk-28a__hint" aria-hidden="true">hover — layers live at translateZ 12–36px, so the judder parallaxes them for free</p>
</section>
<link href="https://fonts.googleapis.com/css2?family=Archivo:[email protected]&display=swap" rel="stylesheet">
<section class="shk-28b" aria-label="Coin wobbling like it was dropped on a table">
  <div class="shk-28b__table">
    <div class="shk-28b__scene">
      <div class="shk-28b__coin" tabindex="0"><span class="shk-28b__face">¤</span></div>
      <div class="shk-28b__shadow" aria-hidden="true"></div>
    </div>
    <p class="shk-28b__hint" aria-hidden="true">rotate3d(1,1,0,…) with decaying angle — a diagonal axis is what makes it precess, not flip · replays every 3s, hover to pause</p>
  </div>
</section>
</div>
```
## CSS
```css
.shk-28-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-28-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-28a,
.shk-28a *,
.shk-28a *::before,
.shk-28a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-28a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-content: center;
  gap: 22px;
  padding: 48px 24px;
  background: radial-gradient(120% 120% at 50% 0%,#131829,#0a0d18 60%);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-28a__scene {
  perspective: 1000px;
}

.shk-28a__pass {
  position: relative;
  width: min(360px,86vw);
  padding: 28px 30px;
  border-radius: 20px;
  background: linear-gradient(140deg,#1b2338,#141a2c);
  border: 1px solid rgba(140,190,255,.28);
  transform-style: preserve-3d;
  transform: rotateX(1deg) rotateY(-2.4deg);
  box-shadow: 0 40px 80px -40px rgba(0,0,0,.95);
  outline: none;
}

.shk-28a__pass:hover,
.shk-28a__pass:focus-visible {
  animation: shk-28a-judder .55s ease-in-out infinite;
}

.shk-28a__glow {
  position: absolute;
  inset: 0;
  border-radius: 20px;
  background: linear-gradient(115deg,transparent 30%,oklch(0.8 0.12 200 / .18) 45%,oklch(0.8 0.14 320 / .18) 55%,transparent 70%);
}

.shk-28a__route {
  font-size: 30px;
  font-weight: 700;
  letter-spacing: .04em;
  color: #eaf2ff;
  translate: 0 0 36px;
}

.shk-28a__route span {
  color: oklch(0.8 0.13 210);
}

.shk-28a__chip {
  width: 44px;
  height: 32px;
  margin-top: 18px;
  border-radius: 7px;
  background: linear-gradient(140deg,oklch(0.85 0.1 90),oklch(0.7 0.12 70));
  translate: 0 0 28px;
  box-shadow: 0 6px 14px -6px rgba(0,0,0,.7);
}

.shk-28a__name {
  margin-top: 16px;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 13px;
  letter-spacing: .24em;
  color: rgba(214,228,250,.85);
  translate: 0 0 20px;
}

.shk-28a__meta {
  margin-top: 10px;
  display: flex;
  gap: 16px;
  font-family: 'JetBrains Mono',ui-monospace,monospace;
  font-size: 10.5px;
  color: rgba(214,228,250,.5);
  translate: 0 0 14px;
}

.shk-28a__strip {
  margin-top: 18px;
  font-size: 15px;
  letter-spacing: .06em;
  color: rgba(214,228,250,.4);
  translate: 0 0 10px;
  overflow: hidden;
  white-space: nowrap;
}

.shk-28a__hint {
  text-align: center;
  font-size: 12px;
  color: rgba(214,228,250,.4);
  max-width: 440px;
  justify-self: center;
}

@keyframes shk-28a-judder {
  0%,
    100% {
    transform: rotateX(1deg) rotateY(-2.4deg);
  }

  25% {
    transform: rotateX(-1.4deg) rotateY(2deg);
  }

  50% {
    transform: rotateX(1deg) rotateY(-1.6deg);
  }

  75% {
    transform: rotateX(-.8deg) rotateY(2.4deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-28a__pass:hover,
    .shk-28a__pass:focus-visible {
    animation: none;
  }
}

.shk-28b,
.shk-28b *,
.shk-28b *::before,
.shk-28b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-28b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#123227,#0b241b);
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
}

.shk-28b__table {
  display: grid;
  justify-items: center;
  gap: 26px;
}

.shk-28b__scene {
  perspective: 800px;
  display: grid;
  justify-items: center;
}

.shk-28b__coin {
  width: 130px;
  height: 130px;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: radial-gradient(85% 85% at 35% 30%,oklch(0.88 0.12 90),oklch(0.72 0.13 80) 60%,oklch(0.6 0.12 70));
  border: 6px solid oklch(0.62 0.12 75);
  box-shadow: inset 0 0 0 4px oklch(0.85 0.11 88 / .6);
  animation: shk-28b-settle 3s cubic-bezier(.25,.6,.35,1) infinite;
  outline: none;
}

.shk-28b__coin:hover,
.shk-28b__coin:focus-visible {
  animation-play-state: paused;
}

.shk-28b__face {
  font-size: 56px;
  font-weight: 900;
  color: oklch(0.45 0.1 70);
  text-shadow: 0 2px 0 oklch(0.9 0.1 90 / .5);
}

.shk-28b__shadow {
  width: 120px;
  height: 16px;
  margin-top: 12px;
  border-radius: 50%;
  background: rgba(0,0,0,.5);
  filter: blur(6px);
  animation: shk-28b-shsettle 3s cubic-bezier(.25,.6,.35,1) infinite;
}

.shk-28b__hint {
  font-size: 12px;
  color: rgba(215,240,225,.45);
  max-width: 460px;
  text-align: center;
}

@keyframes shk-28b-settle {
  0% {
    transform: rotate3d(1,1,0,24deg);
  }

  12% {
    transform: rotate3d(1,-1,0,19deg);
  }

  26% {
    transform: rotate3d(-1,-1,0,14deg);
  }

  40% {
    transform: rotate3d(-1,1,0,10deg);
  }

  54% {
    transform: rotate3d(1,1,0,6deg);
  }

  68% {
    transform: rotate3d(1,-1,0,3deg);
  }

  80% {
    transform: rotate3d(-1,-1,0,1deg);
  }

  88%,
    100% {
    transform: rotate3d(1,1,0,0deg);
  }
}

@keyframes shk-28b-shsettle {
  0% {
    scale: .82 1;
    opacity: .35;
  }

  40% {
    scale: .92 1;
    opacity: .42;
  }

  88%,
    100% {
    scale: 1 1;
    opacity: .5;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-28b__coin,
    .shk-28b__shadow {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — perspective lives on the scene, preserve-3d on the pass, and each layer holds a real translateZ depth. The judder only animates two rotations; the parallax between layers is geometry doing the work. */

/* No JavaScript — the rotation AXIS walks around the coin (1,1 → 1,-1 → -1,-1 → -1,1) while the angle decays 24° → 0°: that axis-walk is precession, the wobble of every real dropped coin. */
```
