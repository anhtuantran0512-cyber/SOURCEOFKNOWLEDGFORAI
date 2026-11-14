---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-fade-up-stagger-text-animation/"
title: "CSS Staggered Text Letter Reveal Keyframes"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Per-letter choreography for luxury brand intros: a masked serif cascade with a gold rule that draws itself, and a center-out spring assemble powered by the…"
has_js: "false"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Staggered Text Letter Reveal Keyframes
Source: https://codefronts.com/motion/css-text-animations/css-fade-up-stagger-text-animation/

Per-letter choreography for luxury brand intros: a masked serif cascade with a gold rule that draws itself, and a center-out spring assemble powered by the modern linear() easing function.
## HTML
```html
<div class="cat-08-group">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;600;700&display=swap" rel="stylesheet">
<section class="cat-08a" aria-label="Luxury letter cascade reveal">
  <div class="cat-08a__stage">
    <h1 class="cat-08a__word" aria-label="VELOUR">
      <span class="cat-08a__mask" aria-hidden="true"><i style="--i:0">V</i><i style="--i:1">E</i><i style="--i:2">L</i><i style="--i:3">O</i><i style="--i:4">U</i><i style="--i:5">R</i></span>
    </h1>
    <p class="cat-08a__tag" aria-hidden="true"><span>MAISON DE COUTURE — PARIS</span></p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-08b" aria-label="Center out spring letter reveal">
  <div class="cat-08b__stage">
    <h1 class="cat-08b__word" aria-label="GATHERED">
      <span aria-hidden="true"><i style="--i:3">G</i><i style="--i:2">A</i><i style="--i:1">T</i><i style="--i:0">H</i><i style="--i:0">E</i><i style="--i:1">R</i><i style="--i:2">E</i><i style="--i:3">D</i></span>
    </h1>
    <p class="cat-08b__sub" aria-hidden="true">indices radiate from the middle · linear() spring easing</p>
  </div>
</section>
</div>
```
## CSS
```css
.cat-08-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-08-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-08a,
.cat-08a *,
.cat-08a *::before,
.cat-08a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-08a {
  --gold: oklch(0.78 0.11 85);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #101014;
  font-family: 'Cormorant Garamond',Georgia,serif;
}

.cat-08a__stage {
  text-align: center;
}

.cat-08a__word {
  font-size: clamp(52px,9vw,120px);
  font-weight: 600;
  color: #ece7dd;
  letter-spacing: .14em;
  margin-right: -.14em;
}

.cat-08a__mask {
  display: inline-block;
  overflow: hidden;
  vertical-align: bottom;
  padding: 0 .05em;
}

.cat-08a__mask i {
  display: inline-block;
  font-style: normal;
  transform: translateY(110%) rotate(4deg);
  animation: cat-08a-up 1s cubic-bezier(.19,.8,.22,1) calc(var(--i)*85ms + .3s) both;
}

.cat-08a__tag {
  margin-top: 18px;
  overflow: hidden;
}

.cat-08a__tag span {
  display: inline-block;
  font-family: 'Segoe UI',system-ui,sans-serif;
  font-size: 10.5px;
  letter-spacing: .42em;
  color: var(--gold);
  transform: translateY(120%);
  animation: cat-08a-up .8s cubic-bezier(.19,.8,.22,1) 1s both;
}

@keyframes cat-08a-up {
  to {
    transform: translateY(0) rotate(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-08a__mask i,
    .cat-08a__tag span {
    animation: none;
    transform: none;
  }
}

.cat-08b,
.cat-08b *,
.cat-08b *::before,
.cat-08b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-08b {
  --vio: oklch(0.72 0.19 300);
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(160deg,#14101f,#0b0912);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-08b__stage {
  text-align: center;
}

.cat-08b__word {
  font-size: clamp(44px,8vw,104px);
  font-weight: 700;
  letter-spacing: .06em;
  margin-right: -.06em;
  color: #f0ecfa;
}

.cat-08b__word i {
  display: inline-block;
  font-style: normal;
  opacity: 0;
  transform: translateY(46px) scale(.7);
  animation: cat-08b-pop .9s calc(var(--i)*110ms + .25s) both;
  animation-timing-function: cubic-bezier(.34,1.56,.64,1);
  animation-timing-function: linear(0,0.004 4.7%,0.147 15.4%,0.581 30.8%,1.09 46%,1.18 55%,1.07 66%,0.96 75%,0.99 87%,1);
}

.cat-08b__word i:nth-child(odd) {
  color: var(--vio);
}

.cat-08b__sub {
  margin-top: 22px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .16em;
  color: rgba(200,190,230,.4);
}

@keyframes cat-08b-pop {
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-08b__word i {
    animation: cat-08b-fade .4s ease both;
  }
}

@keyframes cat-08b-fade {
  to {
    opacity: 1;
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — six letter spans share one keyframe; inline --i indices shift each start by 85ms behind an overflow mask. */

/* No JavaScript — symmetric --i values make letters spring in from the center outward; linear() supplies a real spring curve over a cubic-bezier fallback. */
```
