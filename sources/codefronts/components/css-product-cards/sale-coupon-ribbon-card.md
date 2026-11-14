---
source: "codefronts"
url: "https://codefronts.com/components/css-product-cards/sale-coupon-ribbon-card/"
title: "Sale / Coupon Ribbon Card"
section: "components"
category: "css-product-cards"
category_name: "CSS Product Cards"
description: "A product card with a corner-wrapped diagonal ribbon ('SALE −50%') plus a 'Best Seller' pill and a struck-through original price — the badge/coupon layout…"
has_js: "false"
---

Here's a working CSS Product Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sale / Coupon Ribbon Card
Source: https://codefronts.com/components/css-product-cards/sale-coupon-ribbon-card/

A product card with a corner-wrapped diagonal ribbon ('SALE −50%') plus a 'Best Seller' pill and a struck-through original price — the badge/coupon layout promotion and clearance pages search for, built with clip-path and absolute positioning.
## HTML
```html
<article class="cpc-13">
  <div class="cpc-13__card">
    <span class="cpc-13__ribbon">SALE −50%</span>
    <span class="cpc-13__pill">Best Seller</span>
    <div class="cpc-13__img" role="img" aria-label="Product photo: Halcyon bluetooth speaker"><span>product shot</span></div>
    <div class="cpc-13__body">
      <h3 class="cpc-13__name">Halcyon Bluetooth Speaker</h3>
      <p class="cpc-13__rating" aria-label="Rated 4.8 out of 5"><span aria-hidden="true">★★★★★</span> 4.8 (2,140)</p>
      <div class="cpc-13__prices"><span class="cpc-13__was">$120</span><span class="cpc-13__now">$60</span></div>
      <button class="cpc-13__cta" type="button">Add to Cart</button>
    </div>
  </div>
</article>
```
## CSS
```css
.cpc-13,
.cpc-13 *,
.cpc-13 *::before,
.cpc-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpc-13 ::selection {
  background: oklch(0.62 0.2 25);
  color: #fff;
}

.cpc-13 {
  --accent: oklch(0.55 0.16 260);
  --sale: oklch(0.58 0.2 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #f1f2f6;
}

.cpc-13__card {
  position: relative;
  width: 300px;
  border-radius: 16px;
  overflow: hidden;
  background: #fff;
  box-shadow: 0 16px 40px -22px rgba(16,24,40,.45);
}

.cpc-13__ribbon {
  position: absolute;
  top: 18px;
  right: -42px;
  z-index: 2;
  width: 170px;
  text-align: center;
  transform: rotate(45deg);
  background: var(--sale);
  color: #fff;
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .06em;
  padding: 7px 0;
  box-shadow: 0 6px 14px -6px rgba(0,0,0,.4);
}

.cpc-13__pill {
  position: absolute;
  top: 14px;
  left: 14px;
  z-index: 2;
  padding: 5px 12px;
  border-radius: 999px;
  background: #111827;
  color: #fff;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .04em;
}

.cpc-13__img {
  aspect-ratio: 1/1;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg,#e4e7ee,#d3d8e4),repeating-linear-gradient(45deg,rgba(255,255,255,.45) 0 12px,transparent 12px 24px);
}

.cpc-13__img {
  background-image: url("https://images.unsplash.com/photo-1509440159596-0249088772ff?q=80&w=600&h=600&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.cpc-13__img span {
  display: none;
}

.cpc-13__body {
  padding: 18px 20px 20px;
}

.cpc-13__name {
  font-size: 17px;
  font-weight: 600;
  color: #101828;
}

.cpc-13__rating {
  margin-top: 8px;
  font-size: 13px;
  color: #667085;
}

.cpc-13__rating span {
  color: oklch(0.78 0.15 80);
  letter-spacing: .05em;
}

.cpc-13__prices {
  margin-top: 12px;
  display: flex;
  align-items: baseline;
  gap: 10px;
}

.cpc-13__was {
  font-size: 15px;
  color: #98a2b8;
  text-decoration: line-through;
}

.cpc-13__now {
  font-size: 24px;
  font-weight: 800;
  color: var(--sale);
}

.cpc-13__cta {
  margin-top: 14px;
  width: 100%;
  height: 46px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 600;
}

.cpc-13__cta:hover {
  background: color-mix(in oklch,var(--accent) 88%,#000);
}

.cpc-13__cta:focus-visible {
  outline: 3px solid color-mix(in oklch,var(--accent) 45%,#fff);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
}
```

## JavaScript
```js
/* No JavaScript — a rotated absolute ribbon + pill, clipped by the card's overflow. */
```
