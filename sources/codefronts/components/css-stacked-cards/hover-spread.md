---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/hover-spread/"
title: "Hover Spread"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A compact overlapping pile that stays small by default and, the moment your pointer enters, springs open horizontally across the container with an elegant…"
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hover Spread
Source: https://codefronts.com/components/css-stacked-cards/hover-spread/

A compact overlapping pile that stays small by default and, the moment your pointer enters, springs open horizontally across the container with an elegant bounce — then snaps back when you leave. Great for avatar rows and quick galleries.
## HTML
```html
<section class="scd-14" aria-label="Hover-spread avatar pile">
  <div class="scd-14__pile" tabindex="0">
    <button class="scd-14__card" style="--i:0;background:oklch(0.68 0.16 20)">AR</button>
    <button class="scd-14__card" style="--i:1;background:oklch(0.7 0.15 90)">JL</button>
    <button class="scd-14__card" style="--i:2;background:oklch(0.7 0.15 155)">MK</button>
    <button class="scd-14__card" style="--i:3;background:oklch(0.68 0.15 235)">SV</button>
    <button class="scd-14__card" style="--i:4;background:oklch(0.66 0.16 300)">TN</button>
    <button class="scd-14__card scd-14__card--more" style="--i:5">+6</button>
  </div>
</section>
```
## CSS
```css
.scd-14,
.scd-14 *,
.scd-14 *::before,
.scd-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-14 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #0f1118;
}

.scd-14__pile {
  display: flex;
  padding: 20px;
  border-radius: 99px;
  outline: none;
}

.scd-14__card {
  width: 64px;
  height: 64px;
  flex: none;
  border: 3px solid #0f1118;
  border-radius: 50%;
  color: #fff;
  font-weight: 800;
  font-size: 17px;
  cursor: pointer;
  margin-left: -28px;
  box-shadow: 0 8px 18px -8px rgba(0,0,0,.7);
  transition: margin .45s cubic-bezier(.34,1.56,.5,1),transform .3s;
  transition-delay: calc(var(--i) * .03s);
}

.scd-14__card:first-child {
  margin-left: 0;
}

.scd-14__card--more {
  background: #2a2f40;
  color: #c3c7de;
}

.scd-14__pile:hover .scd-14__card,
.scd-14__pile:focus-within .scd-14__card {
  margin-left: 14px;
}

.scd-14__pile:hover .scd-14__card:first-child,
.scd-14__pile:focus-within .scd-14__card:first-child {
  margin-left: 0;
}

.scd-14__card:hover,
.scd-14__card:focus-visible {
  transform: translateY(-8px) scale(1.08);
  z-index: 5;
  outline: none;
}

.scd-14__card:focus-visible {
  box-shadow: 0 0 0 3px #fff;
}

.scd-14__pile:focus-visible {
  box-shadow: 0 0 0 3px oklch(0.66 0.16 300);
}

@media (prefers-reduced-motion: reduce) {
  .scd-14__card {
    transition: margin .25s linear;
  }
}
```

## JavaScript
```js
/* No JavaScript — cards overlap with negative margins and spring open on :hover/:focus-within via a bouncy cubic-bezier, staggered by a per-card delay. */
```
