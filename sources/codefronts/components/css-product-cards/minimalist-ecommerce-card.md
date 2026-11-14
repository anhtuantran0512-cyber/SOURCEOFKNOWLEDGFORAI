---
source: "codefronts"
url: "https://codefronts.com/components/css-product-cards/minimalist-ecommerce-card/"
title: "Minimalist eCommerce Card"
section: "components"
category: "css-product-cards"
category_name: "CSS Product Cards"
description: "Airy, borderless, type-led — massive whitespace, light-weight type and a whisper-quiet underline CTA."
has_js: "false"
---

Here's a working CSS Product Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist eCommerce Card
Source: https://codefronts.com/components/css-product-cards/minimalist-ecommerce-card/

Airy, borderless, type-led — massive whitespace, light-weight type and a whisper-quiet underline CTA. The high-end fashion, jewellery and lifestyle aesthetic upmarket brands search for when 'card' shouldn't look like a box.
## HTML
```html
<article class="cpc-06">
  <div class="cpc-06__card">
    <div class="cpc-06__img" role="img" aria-label="Product photo: Fine gold hoop earrings"><span>product shot</span></div>
    <div class="cpc-06__body">
      <h3 class="cpc-06__name">Fine Gold Hoops</h3>
      <p class="cpc-06__price">$320</p>
      <a class="cpc-06__cta" href="#">View product</a>
    </div>
  </div>
</article>
```
## CSS
```css
.cpc-06,
.cpc-06 *,
.cpc-06 *::before,
.cpc-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpc-06 ::selection {
  background: #111;
  color: #fff;
}

.cpc-06 {
  --ink: #1a1a1a;
  --muted: #8a8378;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 56px 20px;
  background: #faf9f6;
}

.cpc-06__card {
  width: 320px;
  padding: 20px;
  border-radius: 6px;
  background: transparent;
  transition: box-shadow .4s,background .4s;
}

.cpc-06__card:hover {
  background: #fff;
  box-shadow: 0 24px 60px -34px rgba(0,0,0,.28);
}

.cpc-06__img {
  aspect-ratio: 4/5;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(160deg,#f0ece4,#e6ded1);
}

.cpc-06__img {
  background-image: url("https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?q=80&w=600&h=600&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.cpc-06__img span {
  display: none;
}

.cpc-06__body {
  padding: 22px 4px 6px;
  text-align: center;
}

.cpc-06__name {
  font-size: 17px;
  font-weight: 400;
  letter-spacing: .04em;
  color: var(--ink);
}

.cpc-06__price {
  margin-top: 8px;
  font-size: 14px;
  font-weight: 300;
  letter-spacing: .06em;
  color: var(--muted);
}

.cpc-06__cta {
  display: inline-block;
  margin-top: 18px;
  font-size: 12px;
  font-weight: 500;
  letter-spacing: .22em;
  text-transform: uppercase;
  text-decoration: none;
  color: var(--ink);
  padding-bottom: 3px;
  background: linear-gradient(currentColor,currentColor) 0 100%/0 1px no-repeat;
  transition: background-size .4s;
}

.cpc-06__cta:hover,
.cpc-06__cta:focus-visible {
  background-size: 100% 1px;
  outline: none;
}

.cpc-06__cta:focus-visible {
  background-size: 100% 1px;
  outline: 1px dotted var(--ink);
  outline-offset: 6px;
}

@media (prefers-reduced-motion: reduce) {
  .cpc-06__card,
    .cpc-06__cta {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — an animated background-size underline is the only interaction. */
```
