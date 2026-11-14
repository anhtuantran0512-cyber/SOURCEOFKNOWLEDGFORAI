---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-holographic-text-animation/"
title: "CSS Rainbow Text Sweep Keyframes"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Spectral celebration without the clown factor: a per-letter hue ripple where one filter keyframe cascades a rainbow along the word (each letter…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Rainbow Text Sweep Keyframes
Source: https://codefronts.com/motion/css-text-animations/css-holographic-text-animation/

Spectral celebration without the clown factor: a per-letter hue ripple where one filter keyframe cascades a rainbow along the word (each letter phase-shifted), and a conic prism whose full spectrum rotates inside bold glyphs via one animated @property angle.
## HTML
```html
<div class="cat-27-group">
<link href="https://fonts.googleapis.com/css2?family=Fredoka:[email protected]&display=swap" rel="stylesheet">
<section class="cat-27a" aria-label="Rainbow ripple across letters">
  <div class="cat-27a__stage">
    <h1 class="cat-27a__word" aria-label="celebrate!">
      <span aria-hidden="true"><i style="--i:0">c</i><i style="--i:1">e</i><i style="--i:2">l</i><i style="--i:3">e</i><i style="--i:4">b</i><i style="--i:5">r</i><i style="--i:6">a</i><i style="--i:7">t</i><i style="--i:8">e</i><i style="--i:9">!</i></span>
    </h1>
    <p class="cat-27a__sub" aria-hidden="true">one hue-rotate keyframe · ten phase shifts</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,500..900;1,500..900&display=swap" rel="stylesheet">
<section class="cat-27b" aria-label="Conic rainbow rotating inside text">
  <div class="cat-27b__stage">
    <h1 class="cat-27b__word">PRISM</h1>
    <p class="cat-27b__sub" aria-hidden="true">the spectrum spins · the glyphs hold still</p>
  </div>
</section>
</div>
```
## CSS
```css
.cat-27-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-27-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-27a,
.cat-27a *,
.cat-27a *::before,
.cat-27a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-27a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #fdf9f0;
  font-family: 'Fredoka','Segoe UI',system-ui,sans-serif;
}

.cat-27a__stage {
  text-align: center;
}

.cat-27a__word {
  font-size: clamp(50px,9.6vw,120px);
  font-weight: 700;
  letter-spacing: .01em;
}

.cat-27a__word i {
  display: inline-block;
  font-style: normal;
  color: oklch(0.68 0.22 20);
  animation: cat-27a-hue 3s linear infinite;
  animation-delay: calc(var(--i)*-.22s);
}

.cat-27a__sub {
  margin-top: 16px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .15em;
  color: rgba(60,50,40,.45);
}

@keyframes cat-27a-hue {
  to {
    filter: hue-rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-27a__word i {
    animation: none;
    color: oklch(0.68 0.22 calc(20 + var(--i)*33));
  }
}

@property --cat27b-a {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.cat-27b,
.cat-27b *,
.cat-27b *::before,
.cat-27b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-27b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #101014;
}

.cat-27b__stage {
  text-align: center;
}

.cat-27b__word {
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
  font-size: clamp(60px,12vw,160px);
  font-weight: 900;
  letter-spacing: .02em;
  background: conic-gradient(from var(--cat27b-a) at 50% 50%,oklch(0.7 0.22 0),oklch(0.78 0.19 60),oklch(0.85 0.2 120),oklch(0.78 0.16 200),oklch(0.68 0.2 280),oklch(0.7 0.22 340),oklch(0.7 0.22 0));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: cat-27b-spin 5s linear infinite;
  filter: drop-shadow(0 8px 40px rgb(120 80 200/.25));
}

.cat-27b__sub {
  margin-top: 18px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .16em;
  color: rgba(200,200,225,.4);
}

@keyframes cat-27b-spin {
  to {
    --cat27b-a: 360deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-27b__word {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — every letter runs the same hue-rotate(360deg) loop from a saturated base; negative --i delays turn it into a travelling rainbow. Reduced motion freezes a static spectrum. */

/* No JavaScript — a full-spectrum conic-gradient clips to the glyphs; @property lets its from-angle animate so the rainbow rotates inside motionless letters. */
```
