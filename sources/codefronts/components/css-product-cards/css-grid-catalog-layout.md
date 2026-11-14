---
source: "codefronts"
url: "https://codefronts.com/components/css-product-cards/css-grid-catalog-layout/"
title: "CSS-Grid Catalog Layout"
section: "components"
category: "css-product-cards"
category_name: "CSS Product Cards"
description: "Not one card but the responsive container: a fluid product grid that auto-fits as many cards per row as fit, with no media queries, using…"
has_js: "false"
---

Here's a working CSS Product Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS-Grid Catalog Layout
Source: https://codefronts.com/components/css-product-cards/css-grid-catalog-layout/

Not one card but the responsive container: a fluid product grid that auto-fits as many cards per row as fit, with no media queries, using grid-template-columns: repeat(auto-fit, minmax()). The catalog-layout snippet devs actually search for.
## HTML
```html
<div class="cpc-12">
  <div class="cpc-12__grid">
    <article class="cpc-12__card"><div class="cpc-12__img" role="img" aria-label="Product photo: item 1"><span>shot</span></div><h3 class="cpc-12__name">Canvas Sneaker</h3><div class="cpc-12__foot"><span class="cpc-12__price">$68</span><button type="button" aria-label="Add Canvas Sneaker to cart">+</button></div></article>
    <article class="cpc-12__card"><div class="cpc-12__img" role="img" aria-label="Product photo: item 2"><span>shot</span></div><h3 class="cpc-12__name">Wool Beanie</h3><div class="cpc-12__foot"><span class="cpc-12__price">$24</span><button type="button" aria-label="Add Wool Beanie to cart">+</button></div></article>
    <article class="cpc-12__card"><div class="cpc-12__img" role="img" aria-label="Product photo: item 3"><span>shot</span></div><h3 class="cpc-12__name">Denim Jacket</h3><div class="cpc-12__foot"><span class="cpc-12__price">$96</span><button type="button" aria-label="Add Denim Jacket to cart">+</button></div></article>
    <article class="cpc-12__card"><div class="cpc-12__img" role="img" aria-label="Product photo: item 4"><span>shot</span></div><h3 class="cpc-12__name">Linen Shirt</h3><div class="cpc-12__foot"><span class="cpc-12__price">$54</span><button type="button" aria-label="Add Linen Shirt to cart">+</button></div></article>
    <article class="cpc-12__card"><div class="cpc-12__img" role="img" aria-label="Product photo: item 5"><span>shot</span></div><h3 class="cpc-12__name">Trail Cap</h3><div class="cpc-12__foot"><span class="cpc-12__price">$29</span><button type="button" aria-label="Add Trail Cap to cart">+</button></div></article>
    <article class="cpc-12__card"><div class="cpc-12__img" role="img" aria-label="Product photo: item 6"><span>shot</span></div><h3 class="cpc-12__name">Suede Loafer</h3><div class="cpc-12__foot"><span class="cpc-12__price">$120</span><button type="button" aria-label="Add Suede Loafer to cart">+</button></div></article>
  </div>
</div>
```
## CSS
```css
.cpc-12,
.cpc-12 *,
.cpc-12 *::before,
.cpc-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpc-12 ::selection {
  background: oklch(0.6 0.14 20);
  color: #fff;
}

.cpc-12 {
  --accent: oklch(0.55 0.16 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #f5f4f2;
}

.cpc-12__grid {
  width: min(920px,100%);
  display: grid;
  gap: 20px;
  grid-template-columns: repeat(auto-fit,minmax(200px,1fr));
}

.cpc-12__card {
  background: #fff;
  border-radius: 14px;
  overflow: hidden;
  padding-bottom: 14px;
  box-shadow: 0 10px 26px -18px rgba(16,24,40,.4);
  transition: transform .25s,box-shadow .25s;
}

.cpc-12__card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 40px -20px rgba(16,24,40,.45);
}

.cpc-12__img {
  aspect-ratio: 1/1;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg,#ece7e2,#ddd4cb),repeating-linear-gradient(45deg,rgba(255,255,255,.45) 0 12px,transparent 12px 24px);
}

.cpc-12__img {
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.cpc-12__img span {
  display: none;
}

.cpc-12__card:nth-child(1) .cpc-12__img {
  background-image: url("https://images.unsplash.com/photo-1457369804613-52c61a468e7d?q=80&w=600&h=600&auto=format&fit=crop");
}

.cpc-12__card:nth-child(2) .cpc-12__img {
  background-image: url("https://images.unsplash.com/photo-1578749556568-bc2c40e68b61?q=80&w=600&h=600&auto=format&fit=crop");
}

.cpc-12__card:nth-child(3) .cpc-12__img {
  background-image: url("https://images.unsplash.com/photo-1504608524841-42fe6f032b4b?q=80&w=600&h=600&auto=format&fit=crop");
}

.cpc-12__card:nth-child(4) .cpc-12__img {
  background-image: url("https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?q=80&w=600&h=600&auto=format&fit=crop");
}

.cpc-12__card:nth-child(5) .cpc-12__img {
  background-image: url("https://images.unsplash.com/photo-1498049794561-7780e7231661?q=80&w=600&h=600&auto=format&fit=crop");
}

.cpc-12__card:nth-child(6) .cpc-12__img {
  background-image: url("https://images.unsplash.com/photo-1523362628745-0c100150b504?q=80&w=600&h=600&auto=format&fit=crop");
}

.cpc-12__name {
  padding: 14px 14px 0;
  font-size: 15px;
  font-weight: 600;
  color: #2a2118;
}

.cpc-12__foot {
  padding: 8px 14px 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.cpc-12__price {
  font-size: 16px;
  font-weight: 800;
  color: var(--accent);
}

.cpc-12__foot button {
  width: 40px;
  height: 40px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 22px;
  font-weight: 600;
  line-height: 1;
}

.cpc-12__foot button:hover {
  background: color-mix(in oklch,var(--accent) 88%,#000);
}

.cpc-12__foot button:focus-visible {
  outline: 3px solid color-mix(in oklch,var(--accent) 45%,#fff);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .cpc-12__card {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — repeat(auto-fit,minmax()) reflows the whole catalog with zero media queries. */
```
