---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/variant-picker-slider/"
title: "Variant Picker Slider"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "Click a colour swatch to swap the product photo instantly — the interactive size/colour variant picker every apparel and furniture store needs."
has_js: "false"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Variant Picker Slider
Source: https://codefronts.com/snippets/css-image-carousel/variant-picker-slider/

Click a colour swatch to swap the product photo instantly — the interactive size/colour variant picker every apparel and furniture store needs. Pure CSS radio state cross-fades the hero image and marks the active swatch, no page reload and no script.
## HTML
```html
<section class="car-04" aria-label="Product colour variant picker">
  <div class="car-04__card">
    <input type="radio" name="car-04" id="car-04-1" class="car-04__radio" checked>
    <input type="radio" name="car-04" id="car-04-2" class="car-04__radio">
    <input type="radio" name="car-04" id="car-04-3" class="car-04__radio">
    <div class="car-04__stage">
      <img class="car-04__img" src="https://picsum.photos/seed/chair-slate/700/700" width="700" height="700" alt="Lounge chair in slate">
      <img class="car-04__img" src="https://picsum.photos/seed/chair-ochre/700/700" width="700" height="700" alt="Lounge chair in ochre">
      <img class="car-04__img" src="https://picsum.photos/seed/chair-moss/700/700" width="700" height="700" alt="Lounge chair in moss">
    </div>
    <div class="car-04__foot">
      <p class="car-04__cap"><span class="car-04__label">Colour:</span> <span class="car-04__val car-04__val--1">Slate</span><span class="car-04__val car-04__val--2">Ochre</span><span class="car-04__val car-04__val--3">Moss</span></p>
      <div class="car-04__swatches">
        <label class="car-04__sw" for="car-04-1" style="background:#5b6470" aria-label="Slate"></label>
        <label class="car-04__sw" for="car-04-2" style="background:#c98a2b" aria-label="Ochre"></label>
        <label class="car-04__sw" for="car-04-3" style="background:#6f8256" aria-label="Moss"></label>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.car-04,
.car-04 *,
.car-04 *::before,
.car-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-04 ::selection {
  background: #1f2430;
  color: #fff;
}

.car-04 {
  --accent: #1f2430;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #f2f0ec;
  display: flex;
  align-items: center;
  justify-content: center;
}

.car-04__card {
  width: min(400px,100%);
  background: #fff;
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 24px 50px -34px rgba(16,24,40,.6);
}

.car-04__radio {
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

.car-04__stage {
  position: relative;
  aspect-ratio: 1/1;
  background: #e9e6e1;
}

.car-04__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0;
  transition: opacity .5s ease;
}

.car-04__radio:nth-of-type(1):checked ~ .car-04__stage .car-04__img:nth-child(1),
.car-04__radio:nth-of-type(2):checked ~ .car-04__stage .car-04__img:nth-child(2),
.car-04__radio:nth-of-type(3):checked ~ .car-04__stage .car-04__img:nth-child(3) {
  opacity: 1;
}

.car-04__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  padding: 16px 20px 20px;
}

.car-04__cap {
  font-size: 14px;
  color: #5a5f68;
}

.car-04__label {
  font-weight: 600;
  color: #20242c;
}

.car-04__val {
  display: none;
  font-weight: 600;
  color: #20242c;
}

.car-04__radio:nth-of-type(1):checked ~ .car-04__foot .car-04__val--1,
.car-04__radio:nth-of-type(2):checked ~ .car-04__foot .car-04__val--2,
.car-04__radio:nth-of-type(3):checked ~ .car-04__foot .car-04__val--3 {
  display: inline;
}

.car-04__swatches {
  display: flex;
  gap: 10px;
}

.car-04__sw {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  cursor: pointer;
  border: 2px solid #fff;
  box-shadow: 0 0 0 1px rgba(0,0,0,.14);
  transition: transform .2s,box-shadow .2s;
}

.car-04__sw:hover {
  transform: scale(1.08);
}

.car-04__radio:nth-of-type(1):checked ~ .car-04__foot .car-04__sw:nth-child(1),
.car-04__radio:nth-of-type(2):checked ~ .car-04__foot .car-04__sw:nth-child(2),
.car-04__radio:nth-of-type(3):checked ~ .car-04__foot .car-04__sw:nth-child(3) {
  box-shadow: 0 0 0 2px var(--accent);
  transform: scale(1.12);
}

.car-04__radio:nth-of-type(1):focus-visible ~ .car-04__foot .car-04__sw:nth-child(1),
.car-04__radio:nth-of-type(2):focus-visible ~ .car-04__foot .car-04__sw:nth-child(2),
.car-04__radio:nth-of-type(3):focus-visible ~ .car-04__foot .car-04__sw:nth-child(3) {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .car-04__img,
    .car-04__sw {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the radio group cross-fades the stacked variant photos and updates the swatch ring + colour caption via :checked selectors. */
```
