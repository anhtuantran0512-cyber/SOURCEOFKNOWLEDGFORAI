---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/classic-deck/"
title: "Classic Deck"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "The timeless card deck: every card lies flush on top of the last, with depth implied purely through hairline borders, fine tonal contrast and crisp offset…"
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Classic Deck
Source: https://codefronts.com/components/css-stacked-cards/classic-deck/

The timeless card deck: every card lies flush on top of the last, with depth implied purely through hairline borders, fine tonal contrast and crisp offset drop-shadows. Hover lifts and slightly spreads the deck so you can feel the layers.
## HTML
```html
<section class="scd-10" aria-label="Classic card deck">
  <div class="scd-10__deck" tabindex="0">
    <div class="scd-10__card" aria-hidden="true" style="--i:3"></div>
    <div class="scd-10__card" aria-hidden="true" style="--i:2"></div>
    <div class="scd-10__card" aria-hidden="true" style="--i:1"></div>
    <div class="scd-10__card scd-10__card--top" style="--i:0">
      <p class="scd-10__k">Field Notes</p>
      <h3>Deck №7</h3>
      <p class="scd-10__d">Fifty-two ideas, shuffled weekly. Draw one and build it before Friday.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.scd-10,
.scd-10 *,
.scd-10 *::before,
.scd-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-10 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #e7e4dc;
}

.scd-10__deck {
  position: relative;
  width: min(320px,100%);
  height: 220px;
  outline: none;
}

.scd-10__card {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  background: #fdfcf9;
  border: 1px solid #e0dcd0;
  transform: translate(calc(var(--i) * 5px),calc(var(--i) * 6px));
  box-shadow: 0 2px 0 #d9d4c6,0 12px 24px -14px rgba(60,50,30,.5);
  transition: transform .4s cubic-bezier(.3,.9,.3,1);
}

.scd-10__card:not(.scd-10__card--top) {
  background: #f6f3ec;
}

.scd-10__card--top {
  padding: 28px;
  z-index: 5;
  box-shadow: 0 3px 0 #d9d4c6,0 20px 34px -18px rgba(60,50,30,.55);
}

.scd-10__k {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #a89b7c;
}

.scd-10__card--top h3 {
  font-size: 30px;
  font-weight: 800;
  color: #3a3324;
  margin: 8px 0 10px;
  letter-spacing: -.02em;
}

.scd-10__d {
  font-size: 15px;
  line-height: 1.6;
  color: #6a6250;
  max-width: 32ch;
}

.scd-10__deck:hover .scd-10__card,
.scd-10__deck:focus-visible .scd-10__card {
  transform: translate(calc(var(--i) * 12px),calc(var(--i) * 13px));
}

.scd-10__deck:focus-visible {
  outline: 3px solid #a89b7c;
  outline-offset: 8px;
  border-radius: 20px;
}

@media (prefers-reduced-motion: reduce) {
  .scd-10__card {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — stepped translate, tonal fills and layered offset box-shadows imply the deck's thickness; :hover spreads it. */
```
