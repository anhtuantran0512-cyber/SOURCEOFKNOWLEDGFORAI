---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/fan-spread/"
title: "Fan Spread"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A hand of cards: all sharing one base anchor and rotated at progressive increments (−10°, −5°, 0°, 5°, 10°) so they splay like a poker hand ready to be picked."
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fan Spread
Source: https://codefronts.com/components/css-stacked-cards/fan-spread/

A hand of cards: all sharing one base anchor and rotated at progressive increments (−10°, −5°, 0°, 5°, 10°) so they splay like a poker hand ready to be picked. Hover a card and it lifts proud of the fan.
## HTML
```html
<section class="scd-11" aria-label="Fanned hand of cards">
  <div class="scd-11__hand">
    <button class="scd-11__card" style="--a:-10deg;--c:oklch(0.64 0.16 20)">A<small>♠</small></button>
    <button class="scd-11__card" style="--a:-5deg;--c:oklch(0.66 0.15 60)">K<small>♥</small></button>
    <button class="scd-11__card" style="--a:0deg;--c:oklch(0.66 0.15 150)">Q<small>♦</small></button>
    <button class="scd-11__card" style="--a:5deg;--c:oklch(0.64 0.16 235)">J<small>♣</small></button>
    <button class="scd-11__card" style="--a:10deg;--c:oklch(0.64 0.16 300)">10<small>★</small></button>
  </div>
</section>
```
## CSS
```css
.scd-11,
.scd-11 *,
.scd-11 *::before,
.scd-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-11 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding: 60px 20px 22vh;
  background: radial-gradient(circle at 50% 120%,#1f5136,#0d281c);
}

.scd-11__hand {
  position: relative;
  width: 200px;
  height: 200px;
}

.scd-11__card {
  position: absolute;
  left: 50%;
  bottom: 0;
  width: 120px;
  height: 170px;
  margin-left: -60px;
  border: none;
  cursor: pointer;
  border-radius: 14px;
  background: #fff;
  color: var(--c);
  font-size: 30px;
  font-weight: 800;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: space-between;
  padding: 14px 16px;
  box-shadow: 0 14px 30px -14px rgba(0,0,0,.7);
  transform-origin: 50% 130%;
  transform: rotate(var(--a));
  transition: transform .35s cubic-bezier(.3,.9,.3,1),box-shadow .3s;
}

.scd-11__card small {
  align-self: flex-end;
  font-size: 28px;
}

.scd-11__card:hover,
.scd-11__card:focus-visible {
  transform: rotate(var(--a)) translateY(-40px) scale(1.05);
  box-shadow: 0 26px 44px -18px rgba(0,0,0,.8);
  z-index: 10;
  outline: none;
}

.scd-11__card:focus-visible {
  box-shadow: 0 0 0 3px oklch(0.8 0.14 90),0 26px 44px -18px rgba(0,0,0,.8);
}

@media (prefers-reduced-motion: reduce) {
  .scd-11__card {
    transition: box-shadow .2s;
  }

  .scd-11__card:hover,
    .scd-11__card:focus-visible {
    transform: rotate(var(--a)) translateY(-40px);
  }
}
```

## JavaScript
```js
/* No JavaScript — a shared bottom-centre transform-origin plus a per-card --a angle fans the hand; :hover lifts a single card proud of the arc. */
```
