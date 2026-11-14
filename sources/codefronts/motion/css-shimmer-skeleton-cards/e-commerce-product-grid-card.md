---
source: "codefronts"
url: "https://codefronts.com/motion/css-shimmer-skeleton-cards/e-commerce-product-grid-card/"
title: "E-commerce Product Grid Card"
section: "motion"
category: "css-shimmer-skeleton-cards"
category_name: "CSS Shimmer Skeleton Cards"
description: "A boutique three-up product grid skeleton: square image slots (aspect-ratio:1), a title line, a copper-tinted price bar and a button rectangle — each card…"
has_js: "false"
---

Here's a working CSS Shimmer Skeleton Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-commerce Product Grid Card
Source: https://codefronts.com/motion/css-shimmer-skeleton-cards/e-commerce-product-grid-card/

A boutique three-up product grid skeleton: square image slots (aspect-ratio:1), a title line, a copper-tinted price bar and a button rectangle — each card framed by a gradient hairline border built with the background-clip trick. Warm oklch sand tones replace default gray, so the loading state already smells like the brand.
## HTML
```html
<section class="ssc-02" aria-label="E-commerce product grid skeleton demo">
  <div class="ssc-02__grid" role="status" aria-busy="true">
    <span class="ssc-sr">Loading products…</span>
    <div class="ssc-02__card" aria-hidden="true">
      <div class="ssc-sk ssc-02__img"></div>
      <div class="ssc-sk ssc-02__title"></div>
      <div class="ssc-sk ssc-02__price"></div>
      <div class="ssc-sk ssc-02__btn"></div>
    </div>
    <div class="ssc-02__card" aria-hidden="true">
      <div class="ssc-sk ssc-02__img"></div>
      <div class="ssc-sk ssc-02__title"></div>
      <div class="ssc-sk ssc-02__price"></div>
      <div class="ssc-sk ssc-02__btn"></div>
    </div>
    <div class="ssc-02__card" aria-hidden="true">
      <div class="ssc-sk ssc-02__img"></div>
      <div class="ssc-sk ssc-02__title"></div>
      <div class="ssc-sk ssc-02__price"></div>
      <div class="ssc-sk ssc-02__btn"></div>
    </div>
  </div>
</section>
```
## CSS
```css
.ssc-02,
.ssc-02 *,
.ssc-02 *::before,
.ssc-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ssc-02 {
  --copper: oklch(0.72 0.09 60);
  --sk-bg: oklch(0.93 0.012 75);
  --sk-shine: rgba(255,255,255,.85);
  --btn-radius: 10px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,oklch(0.97 0.008 80),oklch(0.94 0.014 70));
}

.ssc-02 .ssc-sk {
  position: relative;
  overflow: hidden;
  background: var(--sk-bg);
  border-radius: 8px;
}

.ssc-02 .ssc-sk::after {
  content: "";
  position: absolute;
  inset: 0;
  transform: translateX(-100%);
  background: linear-gradient(105deg,transparent 30%,var(--sk-shine) 50%,transparent 70%);
  animation: ssc-02-shimmer 1.8s ease-in-out infinite;
}

@keyframes ssc-02-shimmer {
  100% {
    transform: translateX(100%);
  }
}

.ssc-02 .ssc-sr {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
}

.ssc-02 .ssc-02__grid {
  position: relative;
  width: min(620px,100%);
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(160px,1fr));
  gap: 16px;
}

.ssc-02 .ssc-02__card {
  border: 1px solid transparent;
  border-radius: 18px;
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  background: linear-gradient(oklch(0.99 0.004 80),oklch(0.99 0.004 80)) padding-box,linear-gradient(150deg,color-mix(in oklab,var(--copper) 55%,white),white 45%,color-mix(in oklab,var(--copper) 45%,white)) border-box;
  box-shadow: 0 14px 34px -22px oklch(0.45 0.06 60 / .5);
}

.ssc-02 .ssc-02__card:nth-child(3) .ssc-sk::after {
  animation-delay: .09s;
}

.ssc-02 .ssc-02__card:nth-child(4) .ssc-sk::after {
  animation-delay: .18s;
}

.ssc-02 .ssc-02__img {
  width: 100%;
  aspect-ratio: 1;
  border-radius: 12px;
}

.ssc-02 .ssc-02__title {
  height: 14px;
  width: 85%;
}

.ssc-02 .ssc-02__price {
  height: 12px;
  width: 40%;
  background: color-mix(in oklab,var(--copper) 30%,var(--sk-bg));
}

.ssc-02 .ssc-02__btn {
  height: 38px;
  width: 100%;
  border-radius: var(--btn-radius);
  margin-top: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .ssc-02 .ssc-sk::after {
    animation: none;
    opacity: 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — aspect-ratio reserves the image box; padding-box/border-box gradients draw the copper hairline frame. */
```
