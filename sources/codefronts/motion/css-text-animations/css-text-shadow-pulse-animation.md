---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-text-shadow-pulse-animation/"
title: "CSS 3D Extrude Shadow Text Animation"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Fake 3D that fools everyone: a synthwave arcade logo whose stacked text-shadow extrusion stretches and squashes as the word floats over a perspective grid,…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS 3D Extrude Shadow Text Animation
Source: https://codefronts.com/motion/css-text-animations/css-text-shadow-pulse-animation/

Fake 3D that fools everyone: a synthwave arcade logo whose stacked text-shadow extrusion stretches and squashes as the word floats over a perspective grid, and a trigonometry build where cos()/sin() aim the extrusion at a light that orbits the text.
## HTML
```html
<div class="cat-23-group">
<link href="https://fonts.googleapis.com/css2?family=Bungee&display=swap" rel="stylesheet">
<section class="cat-23a" aria-label="Retro 80s extruded text">
  <div class="cat-23a__scene">
    <h1 class="cat-23a__word">ARCADE</h1>
    <p class="cat-23a__sub" aria-hidden="true">INSERT COIN · 1988</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,500..900;1,500..900&display=swap" rel="stylesheet">
<section class="cat-23b" aria-label="Extruded text lit by an orbiting light">
  <div class="cat-23b__stage">
    <h1 class="cat-23b__word">SUNDIAL</h1>
    <p class="cat-23b__sub" aria-hidden="true">text-shadow offsets = cos(--a)·n / sin(--a)·n — the light orbits</p>
  </div>
</section>
</div>
```
## CSS
```css
.cat-23-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-23-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-23a,
.cat-23a *,
.cat-23a *::before,
.cat-23a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-23a {
  position: relative;
  isolation: isolate;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,#160a2e 0%,#3d1259 46%,#c2337a 60%,#1a0b30 60.5%);
  overflow: hidden;
}

.cat-23a::before {
  content: "";
  position: absolute;
  left: -20%;
  right: -20%;
  top: 60%;
  bottom: -4%;
  background: repeating-linear-gradient(0deg,rgba(255,120,220,.4) 0 1.5px,transparent 1.5px 34px),repeating-linear-gradient(90deg,rgba(255,120,220,.4) 0 1.5px,transparent 1.5px 60px);
  transform: perspective(320px) rotateX(58deg);
  transform-origin: 50% 0;
  z-index: -1;
}

.cat-23a__scene {
  text-align: center;
}

.cat-23a__word {
  font-family: 'Bungee','Arial Black',sans-serif;
  font-size: clamp(44px,9vw,116px);
  letter-spacing: .02em;
  color: #ffd9f2;
  background: linear-gradient(180deg,#fff6fb 18%,#ff9de4 45%,#c94fd8 52%,#ffd9f2 55%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 2px 0 #7a1ba8) drop-shadow(0 5px 0 #4d1273) drop-shadow(0 9px 0 #2b0a49) drop-shadow(0 18px 26px rgba(0,0,0,.6));
  animation: cat-23a-float 3.4s ease-in-out infinite;
}

.cat-23a__sub {
  margin-top: 34px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
  letter-spacing: .5em;
  color: rgba(255,205,240,.65);
  animation: cat-23a-blink 1.6s step-end infinite;
}

@keyframes cat-23a-float {
  0%,
    100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-12px);
  }
}

@keyframes cat-23a-blink {
  50% {
    opacity: .25;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-23a__word,
    .cat-23a__sub {
    animation: none;
  }
}

@property --cat23b-a {
  syntax: '<angle>';
  initial-value: 35deg;
  inherits: true;
}

.cat-23b,
.cat-23b *,
.cat-23b *::before,
.cat-23b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-23b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #e8ded0;
}

.cat-23b__stage {
  text-align: center;
  --cat23b-a: 35deg;
  animation: cat-23b-orbit 9s linear infinite;
}

.cat-23b__word {
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
  font-size: clamp(46px,9vw,118px);
  font-weight: 900;
  letter-spacing: .01em;
  color: #f7f1e6;
  text-shadow: calc(cos(var(--cat23b-a))*2px) calc(sin(var(--cat23b-a))*2px) 0 #c9553e,calc(cos(var(--cat23b-a))*5px) calc(sin(var(--cat23b-a))*5px) 0 #a8432f,calc(cos(var(--cat23b-a))*8px) calc(sin(var(--cat23b-a))*8px) 0 #7e3324,calc(cos(var(--cat23b-a))*11px) calc(sin(var(--cat23b-a))*11px) 0 #58251b,calc(cos(var(--cat23b-a))*22px) calc(sin(var(--cat23b-a))*22px) 34px rgb(70 35 20/.35);
}

.cat-23b__sub {
  margin-top: 26px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .14em;
  color: rgba(60,40,25,.5);
}

@keyframes cat-23b-orbit {
  to {
    --cat23b-a: 395deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-23b__stage {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a chrome gradient clips to the glyphs while stacked drop-shadows build the slab; the word floats over a rotateX perspective grid drawn with repeating gradients. */

/* No JavaScript — @property registers --a as an <angle>; five shadow layers offset by cos(--a)·n / sin(--a)·n so the extrusion always points away from an orbiting light. */
```
