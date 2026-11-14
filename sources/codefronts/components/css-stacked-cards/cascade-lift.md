---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/cascade-lift/"
title: "Cascade Lift"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A vertical stack of cards gently resting on one another."
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cascade Lift
Source: https://codefronts.com/components/css-stacked-cards/cascade-lift/

A vertical stack of cards gently resting on one another. Hover any card and it slides upward while sibling selectors push the cards below it down and out of the way — a clean, physical way to preview one item without leaving the stack.
## HTML
```html
<section class="scd-15" aria-label="Cascade-lift card stack">
  <div class="scd-15__stack">
    <a class="scd-15__card" href="#" style="--c:oklch(0.64 0.16 20)"><b>Espresso</b><span>Single origin · 30ml</span></a>
    <a class="scd-15__card" href="#" style="--c:oklch(0.62 0.14 50)"><b>Cortado</b><span>Equal parts · 90ml</span></a>
    <a class="scd-15__card" href="#" style="--c:oklch(0.6 0.12 80)"><b>Flat white</b><span>Micro-foam · 160ml</span></a>
    <a class="scd-15__card" href="#" style="--c:oklch(0.58 0.1 110)"><b>Cold brew</b><span>18h steep · 240ml</span></a>
  </div>
</section>
```
## CSS
```css
.scd-15,
.scd-15 *,
.scd-15 *::before,
.scd-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-15 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #161310;
}

.scd-15__stack {
  width: min(320px,100%);
}

.scd-15__card {
  display: flex;
  flex-direction: column;
  gap: 5px;
  padding: 20px 24px;
  margin-top: -16px;
  border-radius: 16px;
  color: #fff;
  text-decoration: none;
  background: var(--c);
  box-shadow: 0 14px 30px -18px rgba(0,0,0,.8);
  transition: transform .35s cubic-bezier(.3,.9,.3,1),box-shadow .3s;
}

.scd-15__card:first-child {
  margin-top: 0;
}

.scd-15__card b {
  font-size: 18px;
  font-weight: 800;
}

.scd-15__card span {
  font-size: 13px;
  opacity: .9;
}

.scd-15__card:hover,
.scd-15__card:focus-visible {
  transform: translateY(-18px) scale(1.03);
  box-shadow: 0 26px 44px -20px rgba(0,0,0,.9);
  z-index: 5;
  outline: none;
}

.scd-15__card:focus-visible {
  box-shadow: 0 0 0 3px #fff,0 26px 44px -20px rgba(0,0,0,.9);
}

.scd-15__card:hover ~ .scd-15__card,
.scd-15__card:focus-visible ~ .scd-15__card {
  transform: translateY(30px);
}

@media (prefers-reduced-motion: reduce) {
  .scd-15__card {
    transition: box-shadow .2s;
  }
}
```

## JavaScript
```js
/* No JavaScript — the general-sibling combinator (:hover ~ .card) pushes every card below the hovered one down while it lifts up. */
```
