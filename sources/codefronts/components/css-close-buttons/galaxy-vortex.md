---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/galaxy-vortex/"
title: "Galaxy Vortex Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "A cosmic dismissal: the × floats at the eye of a spiral galaxy built from three counter-rotating conic-gradient layers and a starfield of box-shadow points."
has_js: "false"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Galaxy Vortex Close Button
Source: https://codefronts.com/components/css-close-buttons/galaxy-vortex/

A cosmic dismissal: the × floats at the eye of a spiral galaxy built from three counter-rotating conic-gradient layers and a starfield of box-shadow points. Hover accelerates the vortex and the cross slowly twists inward with a shrinking scale — content being pulled toward the singularity. Peak decorative CSS for 404s and game UI.
## HTML
```html
<section class="ccb-28" aria-label="Galaxy vortex close button demo">
  <button class="ccb-28__close" type="button" aria-label="Close">
    <span class="ccb-28__spiral ccb-28__spiral--slow" aria-hidden="true"></span>
    <span class="ccb-28__spiral ccb-28__spiral--fast" aria-hidden="true"></span>
    <span class="ccb-28__stars" aria-hidden="true"></span>
    <span class="ccb-28__x" aria-hidden="true"></span>
  </button>
</section>
```
## CSS
```css
@property --ccb-28-a {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

@property --ccb-28-b {
  syntax: "<angle>";
  inherits: false;
  initial-value: 0deg;
}

.ccb-28,
.ccb-28 *,
.ccb-28 *::before,
.ccb-28 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-28 {
  --arm-a: oklch(0.6 0.2 300);
  --arm-b: oklch(0.7 0.14 220);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(100% 120% at 50% 0%,oklch(0.17 0.03 290),oklch(0.1 0.015 280));
}

.ccb-28 .ccb-28__close {
  position: relative;
  display: grid;
  place-items: center;
  width: 110px;
  height: 110px;
  border: none;
  border-radius: 50%;
  background: oklch(0.14 0.02 290);
  cursor: pointer;
  overflow: hidden;
  box-shadow: 0 0 0 1px oklch(0.6 0.2 300 / .25),0 24px 60px -24px oklch(0.5 0.2 300 / .6);
}

.ccb-28 .ccb-28__spiral {
  position: absolute;
  inset: 0;
  border-radius: 50%;
}

.ccb-28 .ccb-28__spiral--slow {
  background: conic-gradient(from var(--ccb-28-a),transparent 0 40deg,oklch(0.6 0.2 300 / .35) 60deg 80deg,transparent 100deg 160deg,oklch(0.6 0.2 300 / .3) 185deg 205deg,transparent 225deg 290deg,oklch(0.6 0.2 300 / .32) 310deg 330deg,transparent 350deg);
  animation: ccb-28-spinA 11s linear infinite;
  -webkit-mask: radial-gradient(circle,#000 0 70%,transparent 71%);
  mask: radial-gradient(circle,#000 0 70%,transparent 71%);
}

.ccb-28 .ccb-28__spiral--fast {
  background: conic-gradient(from var(--ccb-28-b),transparent 0 70deg,oklch(0.7 0.14 220 / .3) 90deg 105deg,transparent 125deg 200deg,oklch(0.7 0.14 220 / .28) 225deg 245deg,transparent 265deg);
  animation: ccb-28-spinB 7s linear infinite reverse;
  -webkit-mask: radial-gradient(circle,#000 0 55%,transparent 56%);
  mask: radial-gradient(circle,#000 0 55%,transparent 56%);
}

@keyframes ccb-28-spinA {
  to {
    --ccb-28-a: 360deg;
  }
}

@keyframes ccb-28-spinB {
  to {
    --ccb-28-b: 360deg;
  }
}

.ccb-28 .ccb-28__close:hover .ccb-28__spiral--slow {
  animation-duration: 3.5s;
}

.ccb-28 .ccb-28__close:hover .ccb-28__spiral--fast {
  animation-duration: 2.2s;
}

.ccb-28 .ccb-28__stars {
  position: absolute;
  top: 18%;
  left: 22%;
  width: 1.5px;
  height: 1.5px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 12px 30px 0 0 rgba(255,255,255,.8),34px 8px 0 -.4px rgba(255,255,255,.6),55px 42px 0 0 rgba(255,255,255,.9),70px 15px 0 -.5px rgba(255,255,255,.5),20px 58px 0 -.4px rgba(255,255,255,.7),46px 66px 0 0 rgba(255,255,255,.6),64px 55px 0 -.6px rgba(255,255,255,.45),6px 44px 0 -.5px rgba(255,255,255,.55),40px 24px 0 -.6px rgba(255,255,255,.5),58px 4px 0 -.4px rgba(255,255,255,.65);
}

.ccb-28 .ccb-28__x {
  position: relative;
  width: 22px;
  height: 22px;
  transition: transform 2.2s cubic-bezier(.3,0,.2,1);
  filter: drop-shadow(0 0 6px oklch(0.7 0.14 220 / .8));
}

.ccb-28 .ccb-28__x::before,
.ccb-28 .ccb-28__x::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 22px;
  height: 2.5px;
  border-radius: 2px;
  background: #fff;
}

.ccb-28 .ccb-28__x::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-28 .ccb-28__x::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-28 .ccb-28__close:hover .ccb-28__x {
  transform: rotate(180deg) scale(.75);
}

.ccb-28 .ccb-28__close:active {
  transform: scale(.94);
}

.ccb-28 .ccb-28__close:focus-visible {
  outline: 2.5px solid var(--arm-b);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .ccb-28 .ccb-28__spiral--slow,
    .ccb-28 .ccb-28__spiral--fast {
    animation: none;
  }

  .ccb-28 .ccb-28__x {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — two counter-rotating conic spirals at co-prime speeds + a box-shadow starfield; @property animates the angles. */
```
