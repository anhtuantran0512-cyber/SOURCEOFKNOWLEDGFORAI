---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/thumbnail-grid-pagination-slider/"
title: "Thumbnail Grid Pagination Slider"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: "Thumbnail grid pagination slider — a big main stage with a clickable thumbnail grid beneath it."
has_js: "false"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Thumbnail Grid Pagination Slider
Source: https://codefronts.com/components/css-image-slider/thumbnail-grid-pagination-slider/

Thumbnail grid pagination slider — a big main stage with a clickable thumbnail grid beneath it. Selecting a thumbnail swaps the main image and highlights the active preview, mapped through radio labels with no JavaScript. The exact pattern Zillow, Redfin, Realtor.com, Airbnb, and Vrbo use for their real-estate listing photo galleries; also drops into e-commerce product pages and portfolio case studies.
## HTML
```html
<div class="cis-10">
  <input type="radio" name="cis-10" id="cis-10-1" checked>
  <input type="radio" name="cis-10" id="cis-10-2">
  <input type="radio" name="cis-10" id="cis-10-3">
  <input type="radio" name="cis-10" id="cis-10-4">
  <input type="radio" name="cis-10" id="cis-10-5">
  <input type="radio" name="cis-10" id="cis-10-6">
  <div class="cis-10__stage">
    <img class="cis-10__slide" src="https://picsum.photos/seed/cis10a/1000/640" alt="Living room">
    <img class="cis-10__slide" src="https://picsum.photos/seed/cis10b/1000/640" alt="Kitchen">
    <img class="cis-10__slide" src="https://picsum.photos/seed/cis10c/1000/640" alt="Bedroom">
    <img class="cis-10__slide" src="https://picsum.photos/seed/cis10d/1000/640" alt="Bathroom">
    <img class="cis-10__slide" src="https://picsum.photos/seed/cis10e/1000/640" alt="Garden">
    <img class="cis-10__slide" src="https://picsum.photos/seed/cis10f/1000/640" alt="Facade">
  </div>
  <div class="cis-10__thumbs">
    <label for="cis-10-1" style="--t:url(https://picsum.photos/seed/cis10a/200/150)" aria-label="View 1"></label>
    <label for="cis-10-2" style="--t:url(https://picsum.photos/seed/cis10b/200/150)" aria-label="View 2"></label>
    <label for="cis-10-3" style="--t:url(https://picsum.photos/seed/cis10c/200/150)" aria-label="View 3"></label>
    <label for="cis-10-4" style="--t:url(https://picsum.photos/seed/cis10d/200/150)" aria-label="View 4"></label>
    <label for="cis-10-5" style="--t:url(https://picsum.photos/seed/cis10e/200/150)" aria-label="View 5"></label>
    <label for="cis-10-6" style="--t:url(https://picsum.photos/seed/cis10f/200/150)" aria-label="View 6"></label>
  </div>
</div>
```
## CSS
```css
.cis-10,
.cis-10 *,
.cis-10 *::before,
.cis-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-10 ::selection {
  background: oklch(0.8 0.13 150);
  color: #04140c;
}

.cis-10 {
  --accent: oklch(0.78 0.13 155);
  --line: #242a2a;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #eef2f0;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 14px;
  padding: 40px 20px;
  background: radial-gradient(120% 110% at 50% 0%,#101815,#080b0a);
}

.cis-10 input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cis-10__stage {
  position: relative;
  width: min(680px,94vw);
  aspect-ratio: 1000/640;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid var(--line);
  box-shadow: 0 30px 70px -40px #000;
}

.cis-10__slide {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0;
  transition: opacity .5s ease;
}

#cis-10-1:checked ~ .cis-10__stage .cis-10__slide:nth-child(1),
#cis-10-2:checked ~ .cis-10__stage .cis-10__slide:nth-child(2),
#cis-10-3:checked ~ .cis-10__stage .cis-10__slide:nth-child(3),
#cis-10-4:checked ~ .cis-10__stage .cis-10__slide:nth-child(4),
#cis-10-5:checked ~ .cis-10__stage .cis-10__slide:nth-child(5),
#cis-10-6:checked ~ .cis-10__stage .cis-10__slide:nth-child(6) {
  opacity: 1;
}

.cis-10__thumbs {
  display: grid;
  grid-template-columns: repeat(6,1fr);
  gap: 8px;
  width: min(680px,94vw);
}

.cis-10__thumbs label {
  aspect-ratio: 4/3;
  border-radius: 9px;
  cursor: pointer;
  background-image: var(--t);
  background-size: cover;
  background-position: center;
  opacity: .55;
  border: 2px solid transparent;
  transition: opacity .25s,border-color .25s;
}

.cis-10__thumbs label:hover {
  opacity: .85;
}

#cis-10-1:checked ~ .cis-10__thumbs label:nth-child(1),
#cis-10-2:checked ~ .cis-10__thumbs label:nth-child(2),
#cis-10-3:checked ~ .cis-10__thumbs label:nth-child(3),
#cis-10-4:checked ~ .cis-10__thumbs label:nth-child(4),
#cis-10-5:checked ~ .cis-10__thumbs label:nth-child(5),
#cis-10-6:checked ~ .cis-10__thumbs label:nth-child(6) {
  opacity: 1;
  border-color: var(--accent);
}

@media (max-width: 520px) {
  .cis-10__thumbs {
    grid-template-columns: repeat(3,1fr);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cis-10__slide {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — radio labels double as thumbnails; :checked cross-fades the stage. */
```
