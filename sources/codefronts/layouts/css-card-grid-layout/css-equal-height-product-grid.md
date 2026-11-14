---
source: "codefronts"
url: "https://codefronts.com/layouts/css-card-grid-layout/css-equal-height-product-grid/"
title: "CSS Equal-Height Product Grid"
section: "layouts"
category: "css-card-grid-layout"
category_name: "CSS Card Grid Layouts"
description: "An e-commerce grid where mismatched title and description lengths never break alignment, because every card is a column-flex item so its Add-to-Cart button…"
has_js: "false"
---

Here's a working CSS Card Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Equal-Height Product Grid
Source: https://codefronts.com/layouts/css-card-grid-layout/css-equal-height-product-grid/

An e-commerce grid where mismatched title and description lengths never break alignment, because every card is a column-flex item so its Add-to-Cart button always lands on the same horizontal axis.
## HTML
```html
<div class="cg-03">
  <div class="cg-03__grid">
    <article class="cg-03__card">
      <div class="cg-03__img" style="background:linear-gradient(135deg,#fde68a,#f59e0b)"></div>
      <h3 class="cg-03__name">Ceramic Pour-Over Set</h3>
      <p class="cg-03__desc">Hand-glazed dripper and carafe.</p>
      <div class="cg-03__bottom">
        <span class="cg-03__price">$48</span>
        <button class="cg-03__cta">Add to Cart</button>
      </div>
    </article>
    <article class="cg-03__card">
      <div class="cg-03__img" style="background:linear-gradient(135deg,#a7f3d0,#10b981)"></div>
      <h3 class="cg-03__name">Walnut Cutting Board With Reversible Edge and Juice Groove</h3>
      <p class="cg-03__desc">FSC-certified solid walnut, oiled and ready for daily use in any kitchen.</p>
      <div class="cg-03__bottom">
        <span class="cg-03__price">$72</span>
        <button class="cg-03__cta">Add to Cart</button>
      </div>
    </article>
    <article class="cg-03__card">
      <div class="cg-03__img" style="background:linear-gradient(135deg,#bfdbfe,#3b82f6)"></div>
      <h3 class="cg-03__name">Linen Napkin Set</h3>
      <p class="cg-03__desc">Set of four, stonewashed for softness.</p>
      <div class="cg-03__bottom">
        <span class="cg-03__price">$34</span>
        <button class="cg-03__cta">Add to Cart</button>
      </div>
    </article>
  </div>
</div>
```
## CSS
```css
.cg-03,
.cg-03 *,
.cg-03 *::before,
.cg-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cg-03 ::selection {
  background: #f59e0b;
  color: #1a1a1a;
}

.cg-03 {
  --pad: 20px;
  background: #f8f7f4;
  min-height: 100vh;
  font-family: -apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  padding: 48px 24px;
  color: #1f2937;
}

.cg-03__grid {
  max-width: 980px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fill,minmax(220px,1fr));
  gap: 24px;
  align-items: stretch;
}

.cg-03__card {
  height: 100%;
  display: flex;
  flex-direction: column;
  background: #fff;
  border: 1px solid #e7e4dd;
  border-radius: 14px;
  padding: var(--pad);
  transition: box-shadow .25s ease, transform .25s ease;
}

.cg-03__card:hover {
  transform: translateY(-3px);
  box-shadow: 0 14px 30px -18px rgba(31,41,55,.25);
}

.cg-03__img {
  width: 100%;
  aspect-ratio: 4/3;
  border-radius: 10px;
  margin-bottom: 14px;
}

.cg-03__name {
  font-size: .98rem;
  font-weight: 700;
  line-height: 1.35;
  margin-bottom: 6px;
}

.cg-03__desc {
  font-size: .82rem;
  color: #6b7280;
  line-height: 1.5;
}

.cg-03__bottom {
  margin-top: auto;
  padding-top: 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
}

.cg-03__price {
  font-weight: 800;
  font-size: 1.05rem;
}

.cg-03__cta {
  border: none;
  border-radius: 8px;
  background: #1f2937;
  color: #fff;
  font-size: .78rem;
  font-weight: 700;
  padding: 9px 14px;
  cursor: pointer;
  transition: background .2s ease;
}

.cg-03__cta:hover {
  background: #111827;
}

@media (prefers-reduced-motion: reduce) {
  .cg-03__card,
    .cg-03__cta {
    transition: none;
  }

  .cg-03__card:hover {
    transform: none;
  }
}
```
