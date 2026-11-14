---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/ribbon-tag/"
title: "Ribbon Tag Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "A corner-ribbon dismiss for cards, coupons and promo tiles: the close control IS a folded ribbon clipped diagonally across the card's top-right corner with…"
has_js: "false"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ribbon Tag Close Button
Source: https://codefronts.com/components/css-close-buttons/ribbon-tag/

A corner-ribbon dismiss for cards, coupons and promo tiles: the close control IS a folded ribbon clipped diagonally across the card's top-right corner with clip-path:polygon(), complete with a darker fold-under triangle that sells the wrap. Hover slides the ribbon outward a notch; the whole diagonal band is the hit area.
## HTML
```html
<section class="ccb-22" aria-label="Ribbon tag close button demo">
  <article class="ccb-22__card">
    <button class="ccb-22__ribbon" type="button" aria-label="Dismiss offer">
      <span class="ccb-22__x" aria-hidden="true"></span>
    </button>
    <span class="ccb-22__fold" aria-hidden="true"></span>
    <h3 class="ccb-22__title">Spring offer</h3>
    <p class="ccb-22__text">3 months free on annual plans — ends Sunday.</p>
  </article>
</section>
```
## CSS
```css
.ccb-22,
.ccb-22 *,
.ccb-22 *::before,
.ccb-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-22 {
  --ribbon: oklch(0.62 0.19 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,oklch(0.96 0.01 25),oklch(0.93 0.02 30));
}

.ccb-22 .ccb-22__card {
  position: relative;
  width: min(340px,100%);
  background: #fff;
  border: 1px solid oklch(0.9 0.015 25);
  border-radius: 16px;
  padding: 26px 24px;
  overflow: hidden;
  box-shadow: 0 20px 46px -26px oklch(0.45 0.1 25 / .5);
}

.ccb-22 .ccb-22__title {
  font-size: 17px;
  color: oklch(0.3 0.03 25);
  margin-bottom: 8px;
}

.ccb-22 .ccb-22__text {
  font-size: 13.5px;
  line-height: 1.55;
  color: oklch(0.5 0.02 25);
  max-width: 24ch;
}

.ccb-22 .ccb-22__ribbon {
  position: absolute;
  top: 18px;
  inset-inline-end: -38px;
  width: 150px;
  height: 34px;
  border: none;
  display: grid;
  place-items: center;
  background: linear-gradient(180deg,color-mix(in oklab,var(--ribbon) 85%,white),var(--ribbon));
  color: #fff;
  cursor: pointer;
  transform: rotate(45deg);
  box-shadow: 0 4px 10px -4px color-mix(in oklab,var(--ribbon) 70%,black);
  transition: transform .2s ease;
  z-index: 1;
}

.ccb-22 .ccb-22__ribbon:hover {
  transform: translateY(-3px) rotate(45deg);
}

.ccb-22 .ccb-22__ribbon:active {
  transform: translateY(0) rotate(45deg) scale(.97);
}

.ccb-22 .ccb-22__ribbon:focus-visible {
  outline: 2.5px solid oklch(0.35 0.1 25);
  outline-offset: -5px;
}

.ccb-22 .ccb-22__x {
  position: relative;
  width: 14px;
  height: 14px;
  transform: rotate(-45deg);
}

.ccb-22 .ccb-22__x::before,
.ccb-22 .ccb-22__x::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 14px;
  height: 2px;
  border-radius: 2px;
  background: #fff;
}

.ccb-22 .ccb-22__x::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-22 .ccb-22__x::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-22 .ccb-22__fold {
  position: absolute;
  top: 0;
  inset-inline-end: 0;
  width: 12px;
  height: 12px;
  background: color-mix(in oklab,var(--ribbon) 55%,black);
  clip-path: polygon(0 0,100% 100%,0 100%);
  opacity: 0;
}

@media (prefers-reduced-motion: reduce) {
  .ccb-22 .ccb-22__ribbon {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the button IS a 45°-rotated band clipped by the card; the × counter-rotates to stay upright. */
```
