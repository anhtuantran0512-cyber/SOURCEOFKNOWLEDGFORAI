---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/vertical-image-carousel/"
title: "Vertical Image Carousel"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "A carousel that scrolls up and down instead of left to right — ideal for sidebar widgets, story-style feeds and creative portfolios."
has_js: "false"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Image Carousel
Source: https://codefronts.com/snippets/css-image-carousel/vertical-image-carousel/

A carousel that scrolls up and down instead of left to right — ideal for sidebar widgets, story-style feeds and creative portfolios. Vertical scroll-snap locks each frame into view; a captioned overlay rides along with every image.
## HTML
```html
<section class="car-12" aria-label="Vertical image carousel">
  <ul class="car-12__scroller" tabindex="0" role="group" aria-label="Gallery, scroll up and down">
    <li class="car-12__frame"><img src="https://picsum.photos/seed/vert-1/700/900" width="700" height="900" alt="Desert dunes at sunset"><span class="car-12__cap">Sahara, Morocco</span></li>
    <li class="car-12__frame"><img src="https://picsum.photos/seed/vert-2/700/900" width="700" height="900" alt="Glacier lagoon"><span class="car-12__cap">Jökulsárlón, Iceland</span></li>
    <li class="car-12__frame"><img src="https://picsum.photos/seed/vert-3/700/900" width="700" height="900" alt="Terraced rice fields"><span class="car-12__cap">Bali, Indonesia</span></li>
    <li class="car-12__frame"><img src="https://picsum.photos/seed/vert-4/700/900" width="700" height="900" alt="Autumn forest path"><span class="car-12__cap">Kyoto, Japan</span></li>
  </ul>
</section>
```
## CSS
```css
.car-12,
.car-12 *,
.car-12 *::before,
.car-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-12 ::selection {
  background: #0f766e;
  color: #fff;
}

.car-12 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #0e1513;
  display: flex;
  align-items: center;
  justify-content: center;
}

.car-12__scroller {
  list-style: none;
  width: min(340px,100%);
  height: min(560px,80vh);
  overflow-y: auto;
  scroll-snap-type: y mandatory;
  overscroll-behavior: contain;
  border-radius: 20px;
  box-shadow: 0 30px 60px -34px rgba(0,0,0,.9);
  scrollbar-width: none;
}

.car-12__scroller::-webkit-scrollbar {
  display: none;
}

.car-12__scroller:focus-visible {
  outline: 3px solid #2dd4bf;
  outline-offset: 3px;
}

.car-12__frame {
  position: relative;
  height: 100%;
  scroll-snap-align: start;
  overflow: hidden;
}

.car-12__frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.car-12__cap {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 40px 20px 20px;
  font-size: 15px;
  font-weight: 600;
  color: #fff;
  letter-spacing: .01em;
  background: linear-gradient(transparent,rgba(6,10,9,.85));
}

@media (prefers-reduced-motion: reduce) {
  .car-12__scroller {
    scroll-behavior: auto;
  }
}
```

## JavaScript
```js
/* No JavaScript — vertical scroll-snap (y mandatory) with a fixed-height, focusable, keyboard-scrollable window. */
```
