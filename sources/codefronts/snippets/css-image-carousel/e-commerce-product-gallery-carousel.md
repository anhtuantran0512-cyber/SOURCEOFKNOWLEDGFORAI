---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/e-commerce-product-gallery-carousel/"
title: "E-commerce Product Gallery Carousel"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "The product-page workhorse: one large main image with a strip of clickable thumbnails underneath."
has_js: "false"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-commerce Product Gallery Carousel
Source: https://codefronts.com/snippets/css-image-carousel/e-commerce-product-gallery-carousel/

The product-page workhorse: one large main image with a strip of clickable thumbnails underneath. Selecting a thumbnail cross-fades the main view — no JavaScript, no layout shift, and every thumbnail is a real keyboard-reachable control.
## HTML
```html
<section class="car-01" aria-label="Product image gallery">
  <div class="car-01__viewer">
    <input type="radio" name="car-01" id="car-01-1" class="car-01__radio" checked>
    <input type="radio" name="car-01" id="car-01-2" class="car-01__radio">
    <input type="radio" name="car-01" id="car-01-3" class="car-01__radio">
    <input type="radio" name="car-01" id="car-01-4" class="car-01__radio">
    <div class="car-01__stage">
      <img class="car-01__main" src="https://picsum.photos/seed/sneaker-a/800/800" width="800" height="800" alt="Trail runner, three-quarter view">
      <img class="car-01__main" src="https://picsum.photos/seed/sneaker-b/800/800" width="800" height="800" alt="Trail runner, sole detail">
      <img class="car-01__main" src="https://picsum.photos/seed/sneaker-c/800/800" width="800" height="800" alt="Trail runner, heel and laces">
      <img class="car-01__main" src="https://picsum.photos/seed/sneaker-d/800/800" width="800" height="800" alt="Trail runner, top-down view">
    </div>
    <div class="car-01__thumbs" role="presentation">
      <label class="car-01__thumb" for="car-01-1"><img src="https://picsum.photos/seed/sneaker-a/160/160" width="160" height="160" alt="" aria-hidden="true"></label>
      <label class="car-01__thumb" for="car-01-2"><img src="https://picsum.photos/seed/sneaker-b/160/160" width="160" height="160" alt="" aria-hidden="true"></label>
      <label class="car-01__thumb" for="car-01-3"><img src="https://picsum.photos/seed/sneaker-c/160/160" width="160" height="160" alt="" aria-hidden="true"></label>
      <label class="car-01__thumb" for="car-01-4"><img src="https://picsum.photos/seed/sneaker-d/160/160" width="160" height="160" alt="" aria-hidden="true"></label>
    </div>
  </div>
</section>
```
## CSS
```css
.car-01,
.car-01 *,
.car-01 *::before,
.car-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-01 ::selection {
  background: oklch(0.62 0.16 250);
  color: #fff;
}

.car-01 {
  --accent: oklch(0.62 0.16 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #f4f5f7;
  display: flex;
  align-items: center;
  justify-content: center;
}

.car-01__viewer {
  width: min(440px,100%);
}

.car-01__radio {
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

.car-01__stage {
  position: relative;
  aspect-ratio: 1/1;
  border-radius: 16px;
  overflow: hidden;
  background: #e6e8ec;
  box-shadow: 0 20px 45px -30px rgba(16,24,40,.6);
}

.car-01__main {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0;
  transition: opacity .45s ease;
}

.car-01__thumbs {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 10px;
  margin-top: 14px;
}

.car-01__thumb {
  display: block;
  aspect-ratio: 1/1;
  border-radius: 11px;
  overflow: hidden;
  cursor: pointer;
  border: 2px solid transparent;
  transition: border-color .2s,transform .2s;
  background: #e6e8ec;
}

.car-01__thumb img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.car-01__thumb:hover {
  transform: translateY(-2px);
}

.car-01__radio:nth-of-type(1):checked ~ .car-01__stage .car-01__main:nth-child(1),
.car-01__radio:nth-of-type(2):checked ~ .car-01__stage .car-01__main:nth-child(2),
.car-01__radio:nth-of-type(3):checked ~ .car-01__stage .car-01__main:nth-child(3),
.car-01__radio:nth-of-type(4):checked ~ .car-01__stage .car-01__main:nth-child(4) {
  opacity: 1;
}

.car-01__radio:nth-of-type(1):checked ~ .car-01__thumbs .car-01__thumb:nth-child(1),
.car-01__radio:nth-of-type(2):checked ~ .car-01__thumbs .car-01__thumb:nth-child(2),
.car-01__radio:nth-of-type(3):checked ~ .car-01__thumbs .car-01__thumb:nth-child(3),
.car-01__radio:nth-of-type(4):checked ~ .car-01__thumbs .car-01__thumb:nth-child(4) {
  border-color: var(--accent);
}

.car-01__radio:focus-visible ~ .car-01__thumbs .car-01__thumb {
  outline: 0;
}

.car-01__radio:nth-of-type(1):focus-visible ~ .car-01__thumbs .car-01__thumb:nth-child(1),
.car-01__radio:nth-of-type(2):focus-visible ~ .car-01__thumbs .car-01__thumb:nth-child(2),
.car-01__radio:nth-of-type(3):focus-visible ~ .car-01__thumbs .car-01__thumb:nth-child(3),
.car-01__radio:nth-of-type(4):focus-visible ~ .car-01__thumbs .car-01__thumb:nth-child(4) {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .car-01__main,
    .car-01__thumb {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a shared radio group cross-fades the stacked main images and highlights the active thumbnail via :checked sibling selectors. */
```
