---
source: "codefronts"
url: "https://codefronts.com/motion/css-shake-animation/css-card-shake-effect-on-hover/"
title: "CSS Card Shake Effect on Hover"
section: "motion"
category: "css-shake-animation"
category_name: "CSS Shake Animations"
description: "Card-scale shake in two temperaments: a polaroid that jiggles like it was just picked off a desk (rotation around its center, shadow deepening as it lifts),…"
has_js: "false"
---

Here's a working CSS Shake Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Card Shake Effect on Hover
Source: https://codefronts.com/motion/css-shake-animation/css-card-shake-effect-on-hover/

Card-scale shake in two temperaments: a polaroid that jiggles like it was just picked off a desk (rotation around its center, shadow deepening as it lifts), and a glass feature tile that shivers in 3D — rotateY jitter inside a perspective parent with a specular highlight racing across on the same clock.
## HTML
```html
<div class="shk-18-group">
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;600&family=Manrope:[email protected]&display=swap" rel="stylesheet">
<section class="shk-18a" aria-label="Polaroid photos that jiggle on hover">
  <div class="shk-18a__desk">
    <figure class="shk-18a__pol" style="--r:-2.5deg">
      <img class="shk-18a__img" src="https://picsum.photos/id/1025/360/300" alt="A pug wrapped in a blanket" loading="lazy">
      <figcaption class="shk-18a__cap">office manager, probably</figcaption>
    </figure>
    <figure class="shk-18a__pol" style="--r:1.8deg">
      <img class="shk-18a__img" src="https://picsum.photos/id/1015/360/300" alt="A river winding through mountains" loading="lazy">
      <figcaption class="shk-18a__cap">offsite, day 2</figcaption>
    </figure>
    <figure class="shk-18a__pol" style="--r:3.2deg">
      <img class="shk-18a__img" src="https://picsum.photos/id/1011/360/300" alt="A person canoeing on a lake" loading="lazy">
      <figcaption class="shk-18a__cap">shipping v1 felt like this</figcaption>
    </figure>
  </div>
  <p class="shk-18a__hint" aria-hidden="true">hover — transition lifts, animation jiggles; separate properties, zero conflict</p>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="shk-18b" aria-label="Glass feature tile with 3D shiver on hover">
  <div class="shk-18b__scene">
    <a class="shk-18b__tile" href="#" onclick="return false">
      <p class="shk-18b__chip">New · Motion engine</p>
      <h2 class="shk-18b__title">Shake, physically.</h2>
      <p class="shk-18b__sub">Spring-based micro-interactions, now in the design kit.</p>
      <span class="shk-18b__go" aria-hidden="true">Explore →</span>
    </a>
  </div>
  <p class="shk-18b__hint" aria-hidden="true">hover — rotateY jitters ±2° inside a 900px perspective while the highlight sweeps on the same clock</p>
</section>
</div>
```
## CSS
```css
.shk-18-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.shk-18-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.shk-18a,
.shk-18a *,
.shk-18a *::before,
.shk-18a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-18a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-content: center;
  gap: 26px;
  padding: 48px 24px;
  background: #c9b99a linear-gradient(180deg,rgba(255,255,255,.16),rgba(94,74,42,.18));
  font-family: 'Manrope','Segoe UI',system-ui,sans-serif;
}

.shk-18a__desk {
  display: flex;
  flex-wrap: wrap;
  gap: 26px;
  justify-content: center;
}

.shk-18a__pol {
  background: #fdfcf8;
  padding: 12px 12px 14px;
  border-radius: 4px;
  rotate: var(--r,0deg);
  box-shadow: 0 12px 24px -12px rgba(50,38,20,.55);
  cursor: grab;
  transition: translate .25s,box-shadow .25s,scale .25s;
}

.shk-18a__pol:hover {
  translate: 0 -8px;
  scale: 1.03;
  box-shadow: 0 34px 50px -22px rgba(50,38,20,.6);
  animation: shk-18a-jiggle .8s ease-in-out .1s infinite;
}

.shk-18a__pol:active {
  cursor: grabbing;
}

.shk-18a__img {
  display: block;
  width: min(230px,62vw);
  aspect-ratio: 6/5;
  object-fit: cover;
  filter: saturate(1.05) contrast(1.02);
}

.shk-18a__cap {
  margin-top: 10px;
  text-align: center;
  font-family: 'Caveat',cursive;
  font-size: 19px;
  color: #4a3a22;
}

.shk-18a__hint {
  text-align: center;
  font-size: 12px;
  color: rgba(58,44,22,.6);
}

@keyframes shk-18a-jiggle {
  0%,
    100% {
    rotate: calc(var(--r,0deg) - 1.4deg);
  }

  50% {
    rotate: calc(var(--r,0deg) + 1.4deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-18a__pol:hover {
    animation: none;
  }
}

.shk-18b,
.shk-18b *,
.shk-18b *::before,
.shk-18b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.shk-18b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-content: center;
  gap: 22px;
  padding: 48px 24px;
  background: radial-gradient(120% 120% at 20% 0%,#16203a,#0b0f1d 60%);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.shk-18b__scene {
  perspective: 900px;
}

.shk-18b__tile {
  display: block;
  width: min(400px,88vw);
  padding: 32px;
  border-radius: 22px;
  text-decoration: none;
  background: linear-gradient(115deg,rgba(255,255,255,.12),rgba(255,255,255,.04) 40%,rgba(255,255,255,.14) 50%,rgba(255,255,255,.04) 60%);
  background-size: 250% 100%;
  background-position: 100% 0;
  border: 1px solid rgba(170,200,255,.22);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  box-shadow: 0 40px 80px -40px rgba(0,0,0,.9),inset 0 1px 0 rgba(255,255,255,.12);
  transition: border-color .25s;
}

.shk-18b__tile:hover {
  border-color: rgba(170,200,255,.45);
  animation: shk-18b-shiver 1.2s ease-in-out infinite,shk-18b-sheen 1.2s ease-in-out infinite;
}

.shk-18b__tile:focus-visible {
  outline: 2px solid #9fc0ff;
  outline-offset: 4px;
}

.shk-18b__chip {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: oklch(0.8 0.11 250);
  background: oklch(0.8 0.11 250 / .12);
  border: 1px solid oklch(0.8 0.11 250 / .3);
  padding: 5px 11px;
  border-radius: 999px;
}

.shk-18b__title {
  margin-top: 16px;
  font-size: 30px;
  font-weight: 700;
  letter-spacing: -.02em;
  color: #eef3ff;
}

.shk-18b__sub {
  margin-top: 9px;
  font-size: 14px;
  line-height: 1.6;
  color: rgba(222,232,252,.6);
}

.shk-18b__go {
  display: inline-block;
  margin-top: 20px;
  font-size: 14px;
  font-weight: 700;
  color: #9fc0ff;
}

.shk-18b__hint {
  text-align: center;
  font-size: 12px;
  color: rgba(222,232,252,.4);
  max-width: 440px;
  justify-self: center;
}

@keyframes shk-18b-shiver {
  0%,
    100% {
    transform: rotateY(-2deg) rotateX(.6deg);
  }

  25% {
    transform: rotateY(2deg) rotateX(-.4deg);
  }

  50% {
    transform: rotateY(-1.4deg) rotateX(.5deg);
  }

  75% {
    transform: rotateY(1.6deg) rotateX(-.6deg);
  }
}

@keyframes shk-18b-sheen {
  0% {
    background-position: 100% 0;
  }

  55%,
    100% {
    background-position: 0% 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .shk-18b__tile:hover {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — each polaroid keeps its resting pose in --r; the hover jiggle swings ±1.4° AROUND that pose via calc(), while translate/scale/shadow ride a separate transition. */

/* No JavaScript — perspective on the PARENT gives the jitter a vanishing point; rotateY/rotateX shiver and the background-position sheen share one 1.2s clock so light and motion feel like a single material. */
```
