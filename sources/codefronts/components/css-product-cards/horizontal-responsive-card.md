---
source: "codefronts"
url: "https://codefronts.com/components/css-product-cards/horizontal-responsive-card/"
title: "Horizontal Responsive Card"
section: "components"
category: "css-product-cards"
category_name: "CSS Product Cards"
description: "A horizontal image-left / details-right card for cart pages, comparison rows and mobile search listings — that automatically stacks to vertical when its…"
has_js: "false"
---

Here's a working CSS Product Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Horizontal Responsive Card
Source: https://codefronts.com/components/css-product-cards/horizontal-responsive-card/

A horizontal image-left / details-right card for cart pages, comparison rows and mobile search listings — that automatically stacks to vertical when its container gets narrow, using a container query rather than a viewport media query.
## HTML
```html
<div class="cpc-11">
  <article class="cpc-11__wrap">
    <div class="cpc-11__card">
      <div class="cpc-11__img" role="img" aria-label="Product photo: Ridge insulated bottle"><span>product shot</span></div>
      <div class="cpc-11__body">
        <div><h3 class="cpc-11__name">Ridge Insulated Bottle · 750ml</h3><p class="cpc-11__meta">Slate · Keeps cold 24h</p></div>
        <div class="cpc-11__foot">
          <p class="cpc-11__price">$35</p>
          <div class="cpc-11__actions">
            <button type="button" class="cpc-11__ghost">Save</button>
            <button type="button" class="cpc-11__cta">Add to Cart</button>
          </div>
        </div>
      </div>
    </div>
  </article>
</div>
```
## CSS
```css
.cpc-11,
.cpc-11 *,
.cpc-11 *::before,
.cpc-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpc-11 ::selection {
  background: oklch(0.6 0.13 230);
  color: #fff;
}

.cpc-11 {
  --accent: oklch(0.52 0.14 235);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #eef1f5;
}

.cpc-11__wrap {
  container-type: inline-size;
  width: min(520px,100%);
}

.cpc-11__card {
  display: flex;
  gap: 0;
  background: #fff;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 14px 36px -20px rgba(16,24,40,.4);
}

.cpc-11__img {
  flex: 0 0 40%;
  aspect-ratio: 1/1;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg,#dbe3ee,#c9d5e6),repeating-linear-gradient(45deg,rgba(255,255,255,.45) 0 12px,transparent 12px 24px);
}

.cpc-11__img {
  background-image: url("https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?q=80&w=600&h=600&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.cpc-11__img span {
  display: none;
}

.cpc-11__body {
  flex: 1;
  padding: 20px 22px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 18px;
}

.cpc-11__name {
  font-size: 17px;
  font-weight: 600;
  color: #101828;
  line-height: 1.35;
}

.cpc-11__meta {
  margin-top: 4px;
  font-size: 13px;
  color: #667085;
}

.cpc-11__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
}

.cpc-11__price {
  font-size: 20px;
  font-weight: 800;
  color: #101828;
}

.cpc-11__actions {
  display: flex;
  gap: 8px;
}

.cpc-11__ghost {
  height: 42px;
  padding: 0 16px;
  border: 1px solid #d0d5dd;
  border-radius: 10px;
  cursor: pointer;
  background: #fff;
  color: #344054;
  font-size: 13px;
  font-weight: 600;
}

.cpc-11__ghost:hover {
  border-color: var(--accent);
  color: var(--accent);
}

.cpc-11__cta {
  height: 42px;
  padding: 0 18px;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  background: var(--accent);
  color: #fff;
  font-size: 13px;
  font-weight: 600;
}

.cpc-11__cta:hover {
  background: color-mix(in oklch,var(--accent) 88%,#000);
}

.cpc-11__ghost:focus-visible,
.cpc-11__cta:focus-visible {
  outline: 3px solid color-mix(in oklch,var(--accent) 45%,#fff);
  outline-offset: 2px;
}

@container (max-width: 420px) {
  .cpc-11__card {
    flex-direction: column;
  }

  .cpc-11__img {
    flex: none;
    width: 100%;
    aspect-ratio: 16/9;
  }
}

@media (prefers-reduced-motion: reduce) {
}
```

## JavaScript
```js
/* No JavaScript — a @container query stacks the horizontal card when its wrapper narrows. */
```
