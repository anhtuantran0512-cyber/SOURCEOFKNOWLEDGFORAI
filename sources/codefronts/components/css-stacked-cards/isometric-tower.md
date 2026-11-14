---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/isometric-tower/"
title: "Isometric Tower"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A vertical structural column of cards layered tightly along a steep 3D plane, so the whole component reads like a sleek modern skyscraper."
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Isometric Tower
Source: https://codefronts.com/components/css-stacked-cards/isometric-tower/

A vertical structural column of cards layered tightly along a steep 3D plane, so the whole component reads like a sleek modern skyscraper. Hover to lift the tower's floors apart and inspect each level.
## HTML
```html
<section class="scd-22" aria-label="Isometric tower of cards">
  <div class="scd-22__scene"><div class="scd-22__tower" tabindex="0">
    <div class="scd-22__floor" style="--i:0"><b>Rooftop</b></div>
    <div class="scd-22__floor" style="--i:1"><b>Sky lounge</b></div>
    <div class="scd-22__floor" style="--i:2"><b>Offices</b></div>
    <div class="scd-22__floor" style="--i:3"><b>Atrium</b></div>
    <div class="scd-22__floor" style="--i:4"><b>Lobby</b></div>
  </div></div>
</section>
```
## CSS
```css
.scd-22,
.scd-22 *,
.scd-22 *::before,
.scd-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-22 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 8vh 20px;
  background: radial-gradient(circle at 50% 30%,#1a2030,#0a0d15);
}

.scd-22__scene {
  perspective: 1200px;
}

.scd-22__tower {
  position: relative;
  width: 200px;
  height: 300px;
  transform-style: preserve-3d;
  transform: rotateX(58deg) rotateZ(-42deg);
  transition: transform .5s;
}

.scd-22__floor {
  position: absolute;
  left: 0;
  top: 0;
  width: 180px;
  height: 180px;
  border-radius: 10px;
  background: linear-gradient(160deg,oklch(calc(0.78 - var(--i) * .05) 0.09 240),oklch(calc(0.64 - var(--i) * .05) 0.11 250));
  transform: translateZ(calc(var(--i) * 34px));
  box-shadow: 0 20px 30px -16px rgba(0,0,0,.6);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 14px;
  transition: transform .5s cubic-bezier(.3,.9,.3,1);
}

.scd-22__floor::before {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 34px;
  background: oklch(calc(0.5 - var(--i) * .04) 0.1 250);
  transform: translateZ(-34px);
  border-radius: 0 0 10px 10px;
}

.scd-22__floor b {
  color: #fff;
  font-weight: 800;
  font-size: 15px;
  letter-spacing: .02em;
  text-shadow: 0 1px 2px rgba(0,0,0,.35),0 0 12px rgba(0,0,0,.15);
  text-align: center;
}

.scd-22__tower:hover .scd-22__floor,
.scd-22__tower:focus-visible .scd-22__floor {
  transform: translateZ(calc(var(--i) * 60px + 10px));
}

.scd-22__tower:focus-visible {
  outline: 3px solid oklch(0.7 0.12 240);
  outline-offset: 26px;
  border-radius: 8px;
}

@media (prefers-reduced-motion: reduce) {
  .scd-22__floor,
    .scd-22__tower {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a steep shared isometric rotation plus per-floor translateZ builds the tower; :hover widens the gaps to separate the floors. */
```
