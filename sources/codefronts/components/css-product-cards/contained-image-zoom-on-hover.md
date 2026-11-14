---
source: "codefronts"
url: "https://codefronts.com/components/css-product-cards/contained-image-zoom-on-hover/"
title: "Contained Image Zoom on Hover"
section: "components"
category: "css-product-cards"
category_name: "CSS Product Cards"
description: "The classic CRO image-zoom: the product photo scales up smoothly inside its frame on hover without ever spilling past the card's rounded corners, while a…"
has_js: "false"
---

Here's a working CSS Product Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Contained Image Zoom on Hover
Source: https://codefronts.com/components/css-product-cards/contained-image-zoom-on-hover/

The classic CRO image-zoom: the product photo scales up smoothly inside its frame on hover without ever spilling past the card's rounded corners, while a subtle 'Quick view' overlay fades in. The most-requested micro-interaction on catalog grids.
## HTML
```html
<article class="cpc-03">
  <div class="cpc-03__card">
    <a class="cpc-03__frame" href="#" aria-label="Quick view: Meridian leather tote">
      <span class="cpc-03__img" role="img" aria-label="Product photo: Meridian leather tote"><span>product shot</span></span>
      <span class="cpc-03__overlay"><span class="cpc-03__chip">Quick view</span></span>
    </a>
    <div class="cpc-03__body">
      <h3 class="cpc-03__name">Meridian Leather Tote</h3>
      <p class="cpc-03__price">$240</p>
    </div>
  </div>
</article>
```
## CSS
```css
.cpc-03,
.cpc-03 *,
.cpc-03 *::before,
.cpc-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpc-03 ::selection {
  background: oklch(0.6 0.12 40);
  color: #fff;
}

.cpc-03 {
  --accent: oklch(0.42 0.09 40);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #f6f3ef;
}

.cpc-03__card {
  width: 300px;
}

.cpc-03__frame {
  position: relative;
  display: block;
  aspect-ratio: 4/5;
  border-radius: 16px;
  overflow: hidden;
  text-decoration: none;
  box-shadow: 0 14px 34px -20px rgba(60,40,20,.5);
}

.cpc-03__img {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg,#e8ddd0,#d8c7b3),repeating-linear-gradient(45deg,rgba(255,255,255,.45) 0 14px,transparent 14px 28px);
  transform: scale(1);
  transition: transform .5s cubic-bezier(.2,.7,.2,1);
}

.cpc-03__img {
  background-image: url("https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=600&h=600&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.cpc-03__img span {
  display: none;
}

.cpc-03__overlay {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding-bottom: 22px;
  background: linear-gradient(0deg,rgba(40,26,14,.42),transparent 55%);
  opacity: 0;
  transition: opacity .4s;
}

.cpc-03__chip {
  padding: 10px 20px;
  border-radius: 999px;
  background: rgba(255,255,255,.94);
  color: #3a2a1a;
  font-size: 13px;
  font-weight: 600;
  letter-spacing: .02em;
  transform: translateY(8px);
  transition: transform .4s;
}

.cpc-03__frame:hover .cpc-03__img,
.cpc-03__frame:focus-visible .cpc-03__img {
  transform: scale(1.09);
}

.cpc-03__frame:hover .cpc-03__overlay,
.cpc-03__frame:focus-visible .cpc-03__overlay {
  opacity: 1;
}

.cpc-03__frame:hover .cpc-03__chip,
.cpc-03__frame:focus-visible .cpc-03__chip {
  transform: translateY(0);
}

.cpc-03__frame:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.cpc-03__body {
  padding: 16px 4px 0;
  display: flex;
  align-items: baseline;
  justify-content: space-between;
}

.cpc-03__name {
  font-size: 16px;
  font-weight: 600;
  color: #2c2115;
}

.cpc-03__price {
  font-size: 16px;
  font-weight: 700;
  color: var(--accent);
}

@media (prefers-reduced-motion: reduce) {
  .cpc-03__img,
    .cpc-03__overlay,
    .cpc-03__chip {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — contained scale() zoom + fade-in overlay, clipped by overflow:hidden. */
```
