---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-3d-text-flip-animation/"
title: "CSS 3D Flip Text Reveal Animation"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Real 3D typography: a split-flap departures board whose tiles slam upright one by one on load, and an endlessly turning four-sided word prism for…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS 3D Flip Text Reveal Animation
Source: https://codefronts.com/motion/css-text-animations/css-3d-text-flip-animation/

Real 3D typography: a split-flap departures board whose tiles slam upright one by one on load, and an endlessly turning four-sided word prism for slide-change moments — both driven only by perspective, rotateX and transform-style:preserve-3d.
## HTML
```html
<div class="cat-13-group">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:[email protected]&display=swap" rel="stylesheet">
<section class="cat-13a" aria-label="Split flap board text reveal">
  <div class="cat-13a__board">
    <p class="cat-13a__label" aria-hidden="true">NOW BOARDING — GATE 27</p>
    <h1 class="cat-13a__row" aria-label="AMSTERDAM">
      <span aria-hidden="true"><i style="--i:0">A</i><i style="--i:1">M</i><i style="--i:2">S</i><i style="--i:3">T</i><i style="--i:4">E</i><i style="--i:5">R</i><i style="--i:6">D</i><i style="--i:7">A</i><i style="--i:8">M</i></span>
    </h1>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-13b" aria-label="Rotating 3D word prism">
  <div class="cat-13b__stage">
    <h1 class="cat-13b__line" aria-label="We help you build, ship, scale, repeat">We help you
      <span class="cat-13b__scene" aria-hidden="true"><span class="cat-13b__drum"><span class="cat-13b__face" style="--n:0">build.</span><span class="cat-13b__face" style="--n:1">ship.</span><span class="cat-13b__face" style="--n:2">scale.</span><span class="cat-13b__face" style="--n:3">repeat.</span></span></span>
    </h1>
  </div>
</section>
</div>
```
## CSS
```css
.cat-13-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-13-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-13a,
.cat-13a *,
.cat-13a *::before,
.cat-13a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-13a {
  --amber: oklch(0.82 0.15 80);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #101216;
  font-family: 'JetBrains Mono',ui-monospace,Menlo,monospace;
}

.cat-13a__board {
  background: #181b21;
  border: 1px solid rgba(255,255,255,.07);
  border-radius: 16px;
  padding: 34px 34px 40px;
  box-shadow: 0 40px 80px -40px rgba(0,0,0,.9),inset 0 1px 0 rgba(255,255,255,.05);
}

.cat-13a__label {
  font-size: 10.5px;
  letter-spacing: .3em;
  color: rgba(235,200,120,.55);
  margin-bottom: 20px;
}

.cat-13a__row span {
  display: flex;
  gap: 6px;
  perspective: 700px;
}

.cat-13a__row i {
  display: grid;
  place-items: center;
  width: 1.5em;
  height: 2em;
  font-size: clamp(20px,3.6vw,40px);
  font-style: normal;
  font-weight: 700;
  color: var(--amber);
  background: linear-gradient(180deg,#23272f 48.5%,#191c22 48.5% 51.5%,#20242b 51.5%);
  border-radius: 6px;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.06),0 4px 10px -4px rgba(0,0,0,.8);
  transform: rotateX(-88deg);
  animation: cat-13a-flip .65s cubic-bezier(.3,1.4,.5,1) calc(var(--i)*95ms + .4s) both;
}

@keyframes cat-13a-flip {
  to {
    transform: rotateX(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-13a__row i {
    animation: none;
    transform: none;
  }
}

.cat-13b,
.cat-13b *,
.cat-13b *::before,
.cat-13b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-13b {
  --pink: oklch(0.74 0.19 350);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(170deg,#131018,#0b0a10);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-13b__line {
  font-size: clamp(30px,5.4vw,62px);
  font-weight: 600;
  color: #efeaf7;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: .35em;
  align-items: baseline;
}

.cat-13b__scene {
  display: inline-block;
  perspective: 800px;
  height: 1.3em;
  line-height: 1.3;
}

.cat-13b__drum {
  position: relative;
  display: inline-block;
  min-width: 4.6ch;
  height: 100%;
  transform-style: preserve-3d;
  animation: cat-13b-turn 8s cubic-bezier(.68,-0.3,.32,1.3) infinite;
}

.cat-13b__face {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  color: var(--pink);
  font-weight: 700;
  backface-visibility: hidden;
  transform: rotateX(calc(var(--n)*90deg)) translateZ(.65em);
}

@keyframes cat-13b-turn {
  0%,
    17% {
    transform: rotateX(0);
  }

  25%,
    42% {
    transform: rotateX(-90deg);
  }

  50%,
    67% {
    transform: rotateX(-180deg);
  }

  75%,
    92% {
    transform: rotateX(-270deg);
  }

  100% {
    transform: rotateX(-360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-13b__drum {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — tiles share one perspective, start edge-on at rotateX(-88deg) and flip upright with overshoot, staggered 95ms apart; the gradient stripe fakes the flap hinge. */

/* No JavaScript — four faces sit at rotateX(n*90deg) translateZ(.65em) inside a preserve-3d drum; a hold-segment keyframe turns it one face at a time. */
```
