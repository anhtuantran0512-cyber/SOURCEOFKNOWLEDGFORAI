---
source: "codefronts"
url: "https://codefronts.com/components/css-product-cards/slide-up-details-panel-card/"
title: "Slide-Up Details Panel Card"
section: "components"
category: "css-product-cards"
category_name: "CSS Product Cards"
description: "A compact grid-friendly card showing only name and price at rest; on hover a details panel slides up from the bottom over the image to reveal the description…"
has_js: "false"
---

Here's a working CSS Product Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Slide-Up Details Panel Card
Source: https://codefronts.com/components/css-product-cards/slide-up-details-panel-card/

A compact grid-friendly card showing only name and price at rest; on hover a details panel slides up from the bottom over the image to reveal the description and variant chips. The space-saving overlay pattern dense catalogs rely on.
## HTML
```html
<article class="cpc-05">
  <div class="cpc-05__card">
    <div class="cpc-05__img" role="img" aria-label="Product photo: Field canvas jacket"><span>product shot</span></div>
    <div class="cpc-05__panel">
      <div class="cpc-05__head"><h3 class="cpc-05__name">Field Canvas Jacket</h3><p class="cpc-05__price">$128</p></div>
      <p class="cpc-05__desc">Waxed 12oz cotton canvas with a corduroy collar and a relaxed field cut.</p>
      <div class="cpc-05__sizes" role="group" aria-label="Available sizes">
        <button type="button">S</button><button type="button">M</button><button type="button">L</button><button type="button">XL</button>
      </div>
      <button class="cpc-05__cta" type="button">Add to Cart</button>
    </div>
  </div>
</article>
```
## CSS
```css
.cpc-05,
.cpc-05 *,
.cpc-05 *::before,
.cpc-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpc-05 ::selection {
  background: oklch(0.6 0.12 60);
  color: #fff;
}

.cpc-05 {
  --accent: oklch(0.5 0.11 60);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #f2efe9;
}

.cpc-05__card {
  position: relative;
  width: 300px;
  aspect-ratio: 3/4;
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 18px 40px -22px rgba(50,40,20,.55);
}

.cpc-05__img {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg,#ddd3c4,#c9bca8),repeating-linear-gradient(-45deg,rgba(255,255,255,.4) 0 14px,transparent 14px 28px);
}

.cpc-05__img {
  background-image: url("https://images.unsplash.com/photo-1482938289607-e9573fc25ebb?q=80&w=600&h=600&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.cpc-05__img span {
  display: none;
}

.cpc-05__panel {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 18px 20px 20px;
  background: rgba(255,255,255,.96);
  backdrop-filter: blur(4px);
  border-top-left-radius: 18px;
  border-top-right-radius: 18px;
  transform: translateY(calc(100% - 66px));
  transition: transform .45s cubic-bezier(.2,.7,.2,1);
}

.cpc-05__card:hover .cpc-05__panel,
.cpc-05__card:focus-within .cpc-05__panel {
  transform: translateY(0);
}

.cpc-05__head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 10px;
}

.cpc-05__name {
  font-size: 17px;
  font-weight: 600;
  color: #2a2213;
}

.cpc-05__price {
  font-size: 17px;
  font-weight: 700;
  color: var(--accent);
}

.cpc-05__desc {
  margin-top: 12px;
  font-size: 13.5px;
  line-height: 1.55;
  color: #6b6252;
}

.cpc-05__sizes {
  margin-top: 14px;
  display: flex;
  gap: 8px;
}

.cpc-05__sizes button {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  cursor: pointer;
  border: 1px solid #d8cebd;
  background: #fff;
  color: #3a3020;
  font-size: 13px;
  font-weight: 600;
}

.cpc-05__sizes button:hover {
  border-color: var(--accent);
  color: var(--accent);
}

.cpc-05__sizes button:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.cpc-05__cta {
  margin-top: 14px;
  width: 100%;
  height: 44px;
  border: none;
  border-radius: 11px;
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 14px;
  font-weight: 600;
}

.cpc-05__cta:hover {
  background: color-mix(in oklch,var(--accent) 88%,#000);
}

@media (prefers-reduced-motion: reduce) {
  .cpc-05__panel {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the panel slides via a transform transition on :hover/:focus-within. */
```
