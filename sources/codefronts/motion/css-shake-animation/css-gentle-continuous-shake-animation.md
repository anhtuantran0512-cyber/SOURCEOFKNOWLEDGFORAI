---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-gentle-continuous-shake-animation/"
title: "CSS Gentle Continuous Shake Animation"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "Shake as atmosphere: a handheld-camera badge that drifts ±1px on a slow irregular loop (the motion you sense rather than see), and a lounge of cards…"
has_js: "false"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gentle Continuous Shake Animation
Source: https://codefronts.com/motion/css-shake-animation/css-gentle-continuous-shake-animation/

Shake as atmosphere: a handheld-camera badge that drifts ±1px on a slow irregular loop (the motion you sense rather than see), and a lounge of cards trembling at different phases and periods — nth-child desync that makes a whole layout feel alive without a single synchronized frame.
## HTML
```html
<div class="shk-26-group">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:[email protected]&display=swap" rel="stylesheet">
<section class="shk-26a" aria-label="Badge drifting like handheld camera footage">
  <div class="shk-26a__stage">
    <div class="shk-26a__badge">
      <p class="shk-26a__est">EST. 2027</p>
      <p class="shk-26a__name">Drift <em>Coffee</em></p>
      <p class="shk-26a__tag">never quite still</p>
    </div>
    <p class="shk-26a__hint" aria-hidden="true">±3px, ±0.9°, 6s loop on prime-spaced frames — never quite still, never in a rhythm</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="shk-26b" aria-label="Cards trembling at different phases">
  <div class="shk-26b__stage">
    <div class="shk-26b__row">
      <div class="shk-26b__card" style="--i:0"><span class="shk-26b__k">01</span>Ambient</div>
      <div class="shk-26b__card" style="--i:1"><span class="shk-26b__k">02</span>Motion</div>
      <div class="shk-26b__card" style="--i:2"><span class="shk-26b__k">03</span>Without</div>
      <div class="shk-26b__card" style="--i:3"><span class="shk-26b__k">04</span>Rhythm</div>
    </div>
    <p class="shk-26b__hint" aria-hidden="true">duration 4s + i·.35s, delay i·-1.3s — same keyframes, four phases, zero unison</p>
  </div>
</section>
</div>
```
## CSS
```css
.shk-26-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-26-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-26a,
.shk-26a *,
.shk-26a *::before,
.shk-26a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-26a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#f2ede4,#e7dfd0);
  font-family: 'Manrope','Segoe UI',system-ui,sans-serif;
}

.shk-26a__stage {
  text-align: center;
}

.shk-26a__badge {
  display: inline-grid;
  gap: 6px;
  padding: 44px 52px;
  background: #fbf8f1;
  border: 2px solid #2e2618;
  border-radius: 50%;
  box-shadow: 0 22px 44px -24px rgba(46,38,24,.6);
  animation: shk-26a-drift 6s ease-in-out infinite;
}

.shk-26a__badge:hover {
  animation-play-state: paused;
}

.shk-26a__est {
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: .3em;
  color: rgba(46,38,24,.55);
}

.shk-26a__name {
  font-family: 'Instrument Serif',Georgia,serif;
  font-weight: 400;
  font-size: 40px;
  color: #2e2618;
  letter-spacing: -.01em;
}

.shk-26a__name em {
  font-style: italic;
}

.shk-26a__tag {
  font-size: 11.5px;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: rgba(46,38,24,.5);
}

.shk-26a__hint {
  margin-top: 26px;
  font-size: 12px;
  color: rgba(46,38,24,.5);
  max-width: 420px;
  margin-inline: auto;
}

@keyframes shk-26a-drift {
  0%,
    100% {
    translate: 0 0;
    rotate: 0deg;
  }

  23% {
    translate: 2.5px -2px;
    rotate: .9deg;
  }

  41% {
    translate: -2.2px 1.4px;
    rotate: -.75deg;
  }

  67% {
    translate: 1.6px 2.4px;
    rotate: .6deg;
  }

  86% {
    translate: -2px -1.8px;
    rotate: -.9deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-26a__badge {
    animation: none;
  }
}

.shk-26b,
.shk-26b *,
.shk-26b *::before,
.shk-26b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-26b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(120% 120% at 50% 0%,#141824,#0c0e16 65%);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-26b__stage {
  text-align: center;
}

.shk-26b__row {
  display: flex;
  flex-wrap: wrap;
  gap: 18px;
  justify-content: center;
}

.shk-26b__card {
  display: grid;
  gap: 10px;
  justify-items: start;
  width: 150px;
  padding: 20px 18px;
  border-radius: 16px;
  background: rgba(255,255,255,.05);
  border: 1px solid rgba(160,185,230,.16);
  color: #e7edfa;
  font-size: 16px;
  font-weight: 600;
  animation: shk-26b-tremble calc(4s + var(--i) * .35s) ease-in-out calc(var(--i) * -1.3s) infinite;
}

.shk-26b__card:hover {
  animation-play-state: paused;
}

.shk-26b__k {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .14em;
  color: oklch(0.75 0.12 250);
  background: oklch(0.75 0.12 250 / .12);
  padding: 3px 8px;
  border-radius: 999px;
}

.shk-26b__hint {
  margin-top: 26px;
  font-size: 12px;
  color: rgba(231,237,250,.4);
}

@keyframes shk-26b-tremble {
  0%,
    100% {
    translate: 0 0;
    rotate: 0deg;
  }

  19% {
    translate: 3px -2.4px;
    rotate: 1deg;
  }

  43% {
    translate: -2.7px 1.8px;
    rotate: -.85deg;
  }

  61% {
    translate: 2.1px 2.7px;
    rotate: .7deg;
  }

  83% {
    translate: -2.4px -2.1px;
    rotate: -1deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-26b__card {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — keyframes sit on primes (23/41/67/86%) so the drift never resolves into a rhythm the eye can lock onto. That's the difference between “alive” and “blinking”. */

/* No JavaScript — one keyframe rule, four phases: each card computes its own duration and negative delay from --i, so the ensemble drifts forever without two cards ever breathing together. */
```
