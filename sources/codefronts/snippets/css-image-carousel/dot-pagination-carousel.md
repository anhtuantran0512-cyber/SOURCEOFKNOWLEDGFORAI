---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/dot-pagination-carousel/"
title: "Dot Pagination Carousel"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "A wide-format image carousel with bottom indicator dots that jump to their slide and light up when active — the standard pattern for hero banners,…"
has_js: "false"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dot Pagination Carousel
Source: https://codefronts.com/snippets/css-image-carousel/dot-pagination-carousel/

A wide-format image carousel with bottom indicator dots that jump to their slide and light up when active — the standard pattern for hero banners, destination galleries, and product showcases. Pure CSS using anchor links, scroll-snap, scroll-behavior:smooth, and :target + :has() to track the active dot. Works in every current browser.
## HTML
```html
<section class="car-16" aria-label="Destination gallery">
  <div class="car-16__frame">
    <ul class="car-16__scroller" tabindex="0" role="group" aria-label="Destinations, swipe or use arrow keys">
      <li class="car-16__slide" id="car-16-1"><img src="https://picsum.photos/seed/dot-1/1000/560" width="1000" height="560" alt="Amalfi coastline"><span class="car-16__cap">Amalfi Coast</span></li>
      <li class="car-16__slide" id="car-16-2"><img src="https://picsum.photos/seed/dot-2/1000/560" width="1000" height="560" alt="Santorini rooftops"><span class="car-16__cap">Santorini</span></li>
      <li class="car-16__slide" id="car-16-3"><img src="https://picsum.photos/seed/dot-3/1000/560" width="1000" height="560" alt="Kyoto temple garden"><span class="car-16__cap">Kyoto</span></li>
      <li class="car-16__slide" id="car-16-4"><img src="https://picsum.photos/seed/dot-4/1000/560" width="1000" height="560" alt="Patagonia peaks"><span class="car-16__cap">Patagonia</span></li>
    </ul>
    <nav class="car-16__dots" aria-label="Pagination">
      <a href="#car-16-1" class="car-16__dot" aria-label="Go to slide 1"></a>
      <a href="#car-16-2" class="car-16__dot" aria-label="Go to slide 2"></a>
      <a href="#car-16-3" class="car-16__dot" aria-label="Go to slide 3"></a>
      <a href="#car-16-4" class="car-16__dot" aria-label="Go to slide 4"></a>
    </nav>
  </div>
</section>
```
## CSS
```css
.car-16,
.car-16 *,
.car-16 *::before,
.car-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-16 ::selection {
  background: #f59e0b;
  color: #111;
}

.car-16 {
  --accent: #f59e0b;
  --dot: #e4d5b8;
  --dot-hover: #d4bd8c;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #faf6ee;
  display: flex;
  align-items: center;
  justify-content: center;
  scroll-behavior: smooth;
}

.car-16__frame {
  width: min(680px,100%);
  background: #fff;
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 24px 50px -34px rgba(90,60,10,.5);
}

.car-16__scroller {
  list-style: none;
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scrollbar-width: none;
  scroll-behavior: smooth;
}

.car-16__scroller::-webkit-scrollbar {
  display: none;
}

.car-16__scroller:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: -3px;
}

.car-16__slide {
  position: relative;
  flex: 0 0 100%;
  scroll-snap-align: center;
  scroll-margin-left: 0;
  aspect-ratio: 16/9;
  overflow: hidden;
}

.car-16__slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.car-16__cap {
  position: absolute;
  left: 0;
  bottom: 0;
  padding: 34px 20px 16px;
  color: #fff;
  font-size: 18px;
  font-weight: 700;
  background: linear-gradient(transparent,rgba(0,0,0,.6));
  width: 100%;
}

.car-16__dots {
  display: flex;
  justify-content: center;
  gap: 10px;
  padding: 16px;
  background: #fff;
}

.car-16__dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--dot);
  transition: transform .2s,background .2s;
  text-decoration: none;
  position: relative;
}

.car-16__dot::before {
  content: "";
  position: absolute;
  inset: -12px;
  border-radius: 50%;
}

.car-16__dot:hover {
  background: var(--dot-hover);
}

.car-16__dot:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.car-16__slide:target ~ .car-16__dots .car-16__dot[href$="1"] {
  background: var(--dot);
}

.car-16__frame:has(#car-16-1:target) .car-16__dot[href="#car-16-1"],
.car-16__frame:has(#car-16-2:target) .car-16__dot[href="#car-16-2"],
.car-16__frame:has(#car-16-3:target) .car-16__dot[href="#car-16-3"],
.car-16__frame:has(#car-16-4:target) .car-16__dot[href="#car-16-4"] {
  background: var(--accent);
  transform: scale(1.4);
}

@media (prefers-reduced-motion: reduce) {
  .car-16 {
    scroll-behavior: auto;
  }

  .car-16__scroller {
    scroll-behavior: auto;
  }

  .car-16__dot {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — anchor-link dots (`<a href="#car-16-N">`) navigate via scroll-behavior:smooth + scroll-snap; :target + :has() drive the active-dot highlight. */
```
