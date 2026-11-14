---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/tilted-polaroids/"
title: "Tilted Polaroids"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A casual scatter of Polaroid-style photos — thick white borders, hand-written captions, and slight random rotations — as if tossed onto a table."
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tilted Polaroids
Source: https://codefronts.com/components/css-stacked-cards/tilted-polaroids/

A casual scatter of Polaroid-style photos — thick white borders, hand-written captions, and slight random rotations — as if tossed onto a table. Hover a snap and it straightens and rises to the top of the pile.
## HTML
```html
<section class="scd-12" aria-label="Scattered Polaroid photos">
  <div class="scd-12__board">
    <figure class="scd-12__snap" tabindex="0" style="--x:-90px;--y:-30px;--r:-8deg"><img src="https://picsum.photos/seed/pola-1/300/300" width="300" height="300" alt="Campsite at dawn"><figcaption>Dawn, day 3</figcaption></figure>
    <figure class="scd-12__snap" tabindex="0" style="--x:30px;--y:-50px;--r:6deg"><img src="https://picsum.photos/seed/pola-2/300/300" width="300" height="300" alt="Two mugs of coffee"><figcaption>First light coffee</figcaption></figure>
    <figure class="scd-12__snap" tabindex="0" style="--x:-40px;--y:40px;--r:4deg"><img src="https://picsum.photos/seed/pola-3/300/300" width="300" height="300" alt="Mountain trail marker"><figcaption>Km 14</figcaption></figure>
    <figure class="scd-12__snap" tabindex="0" style="--x:80px;--y:30px;--r:-5deg"><img src="https://picsum.photos/seed/pola-4/300/300" width="300" height="300" alt="Sunset over ridge"><figcaption>Golden hour</figcaption></figure>
  </div>
</section>
```
## CSS
```css
.scd-12,
.scd-12 *,
.scd-12 *::before,
.scd-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-12 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #cdbfa8;
}

.scd-12__board {
  position: relative;
  width: min(360px,90vw);
  height: 340px;
}

.scd-12__snap {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 180px;
  margin: -110px 0 0 -90px;
  background: #fff;
  padding: 12px 12px 0;
  border-radius: 3px;
  box-shadow: 0 16px 30px -14px rgba(40,30,10,.6);
  transform: translate(var(--x),var(--y)) rotate(var(--r));
  transition: transform .35s cubic-bezier(.3,.9,.3,1),box-shadow .3s;
  cursor: pointer;
  outline: none;
}

.scd-12__snap img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  display: block;
}

.scd-12__snap figcaption {
  padding: 12px 4px 14px;
  text-align: center;
  font-family: 'Bradley Hand','Segoe Script',cursive;
  font-size: 16px;
  color: #4a4030;
}

.scd-12__snap:hover,
.scd-12__snap:focus-visible {
  transform: translate(var(--x),var(--y)) rotate(0deg) scale(1.08);
  box-shadow: 0 30px 50px -18px rgba(40,30,10,.75);
  z-index: 10;
}

.scd-12__snap:focus-visible {
  box-shadow: 0 0 0 3px oklch(0.6 0.17 250),0 30px 50px -18px rgba(40,30,10,.75);
}

@media (prefers-reduced-motion: reduce) {
  .scd-12__snap {
    transition: box-shadow .2s;
  }

  .scd-12__snap:hover,
    .scd-12__snap:focus-visible {
    transform: translate(var(--x),var(--y)) rotate(0deg);
  }
}
```

## JavaScript
```js
/* No JavaScript — per-card --x/--y/--r scatter the snaps; :hover/:focus-visible straightens and raises the one in focus. */
```
