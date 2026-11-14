---
source: "codefronts"
url: "https://codefronts.com/motion/css-slide-in-animation/e-commerce-product-card-grid-animation/"
title: "E-commerce Product Card Grid Animation"
section: "motion"
category: "css-slide-in-animation"
category_name: "CSS Slide In Animation Templates"
description: "A clean-white product grid where six e-commerce cards cascade in from below, each with product image, category, name, price, and \"Add to cart\" hover — the…"
has_js: "false"
---

Here's a working CSS Slide In Animation Template from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-commerce Product Card Grid Animation
Source: https://codefronts.com/motion/css-slide-in-animation/e-commerce-product-card-grid-animation/

A clean-white product grid where six e-commerce cards cascade in from below, each with product image, category, name, price, and "Add to cart" hover — the layout used by Shopify, Squarespace Commerce, and modern DTC brands.
## HTML
```html
<div class="sl-02">
  <div class="sl-02__inner">
    <div class="sl-02__head">
      <p class="sl-02__kicker">Bestsellers</p>
      <h2 class="sl-02__title">Shop the collection</h2>
    </div>
    <div class="sl-02__grid">
      <article class="sl-02__card">
        <div class="sl-02__img" style="--g:linear-gradient(135deg,#f5c6cb,#f56565)"><span class="sl-02__sale">Sale</span></div>
        <span class="sl-02__cat">Outerwear</span>
        <h3>Puffer Jacket</h3>
        <div class="sl-02__price"><strong>$189</strong><del>$249</del></div>
      </article>
      <article class="sl-02__card">
        <div class="sl-02__img" style="--g:linear-gradient(135deg,#d4e5ff,#7c9dff)"></div>
        <span class="sl-02__cat">Shoes</span>
        <h3>Runner Low</h3>
        <div class="sl-02__price"><strong>$128</strong></div>
      </article>
      <article class="sl-02__card">
        <div class="sl-02__img" style="--g:linear-gradient(135deg,#c9e7d3,#5eb377)"></div>
        <span class="sl-02__cat">Bags</span>
        <h3>Canvas Tote</h3>
        <div class="sl-02__price"><strong>$74</strong></div>
      </article>
      <article class="sl-02__card">
        <div class="sl-02__img" style="--g:linear-gradient(135deg,#f5e0c9,#c8955c)"><span class="sl-02__sale">Sale</span></div>
        <span class="sl-02__cat">Accessories</span>
        <h3>Leather Wallet</h3>
        <div class="sl-02__price"><strong>$52</strong><del>$68</del></div>
      </article>
      <article class="sl-02__card">
        <div class="sl-02__img" style="--g:linear-gradient(135deg,#e0d0f5,#a78bfa)"></div>
        <span class="sl-02__cat">Tops</span>
        <h3>Merino Crew</h3>
        <div class="sl-02__price"><strong>$88</strong></div>
      </article>
      <article class="sl-02__card">
        <div class="sl-02__img" style="--g:linear-gradient(135deg,#333,#0a0a0a)"></div>
        <span class="sl-02__cat">Denim</span>
        <h3>Selvedge Jeans</h3>
        <div class="sl-02__price"><strong>$168</strong></div>
      </article>
    </div>
  </div>
</div>
```
## CSS
```css
.sl-02 {
  --bg: #fafafa;
  --card: #fff;
  --accent: #f56565;
  --ink: #1a1a1a;
  --sub: #666;
  --line: #e8e8e8;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 24px;
  background: var(--bg);
  color: var(--ink);
}

.sl-02 *,
.sl-02 *::before,
.sl-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sl-02 ::selection {
  background: var(--accent);
  color: #fff;
}

.sl-02__inner {
  width: 100%;
  max-width: 960px;
}

.sl-02__head {
  margin-bottom: 28px;
}

.sl-02__kicker {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 6px;
}

.sl-02__title {
  font-size: clamp(1.5rem,3vw,1.9rem);
  font-weight: 700;
  letter-spacing: -.02em;
}

.sl-02__grid {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 16px;
}

.sl-02__card {
  padding: 0;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 8px;
  overflow: hidden;
  opacity: 0;
  transform: translateY(30px);
  animation: sl-02-card .55s cubic-bezier(.22,1,.36,1) forwards;
  transition: transform .2s ease,box-shadow .2s ease;
}

.sl-02__card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px -8px rgba(0,0,0,.12);
}

.sl-02__card:nth-child(1) {
  animation-delay: .08s;
}

.sl-02__card:nth-child(2) {
  animation-delay: .16s;
}

.sl-02__card:nth-child(3) {
  animation-delay: .24s;
}

.sl-02__card:nth-child(4) {
  animation-delay: .32s;
}

.sl-02__card:nth-child(5) {
  animation-delay: .4s;
}

.sl-02__card:nth-child(6) {
  animation-delay: .48s;
}

.sl-02__img {
  position: relative;
  aspect-ratio: 4/5;
  background: var(--g,#eee);
}

.sl-02__sale {
  position: absolute;
  top: 10px;
  left: 10px;
  padding: 3px 8px;
  border-radius: 4px;
  background: var(--accent);
  color: #fff;
  font-size: .65rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.sl-02__cat {
  display: block;
  padding: 12px 14px 2px;
  font-size: .68rem;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sub);
}

.sl-02__card h3 {
  padding: 0 14px 4px;
  font-size: .95rem;
  font-weight: 600;
  letter-spacing: -.01em;
}

.sl-02__price {
  padding: 0 14px 14px;
  display: flex;
  align-items: baseline;
  gap: 8px;
}

.sl-02__price strong {
  font-size: 1rem;
  font-weight: 700;
  color: var(--ink);
  font-variant-numeric: tabular-nums;
}

.sl-02__price del {
  font-size: .82rem;
  color: var(--sub);
  text-decoration: line-through;
  font-variant-numeric: tabular-nums;
}

@keyframes sl-02-card {
  from {
    opacity: 0;
    transform: translateY(30px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sl-02__card {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}

@media (max-width: 720px) {
  .sl-02__grid {
    grid-template-columns: repeat(2,1fr);
  }
}

@media (max-width: 480px) {
  .sl-02__grid {
    grid-template-columns: 1fr;
  }
}
```
