---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/zoom-on-hover-gallery/"
title: "Zoom-on-Hover Gallery"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "A scroll-snap image rail where hovering (or focusing) any tile cleanly scales the photo up inside its fixed frame — a punchy, tactile gallery for products,…"
has_js: "false"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Zoom-on-Hover Gallery
Source: https://codefronts.com/snippets/css-image-carousel/zoom-on-hover-gallery/

A scroll-snap image rail where hovering (or focusing) any tile cleanly scales the photo up inside its fixed frame — a punchy, tactile gallery for products, food or travel. The zoom is masked by the frame so nothing overflows and the layout never moves.
## HTML
```html
<section class="car-21" aria-label="Dish gallery">
  <ul class="car-21__rail" tabindex="0" role="group" aria-label="Dishes, scrollable">
    <li class="car-21__tile"><a class="car-21__frame" href="#"><img src="https://picsum.photos/seed/zoom-1/600/600" width="600" height="600" alt="Ramen bowl"><span class="car-21__cap">Tonkotsu Ramen</span></a></li>
    <li class="car-21__tile"><a class="car-21__frame" href="#"><img src="https://picsum.photos/seed/zoom-2/600/600" width="600" height="600" alt="Stack of pancakes"><span class="car-21__cap">Buttermilk Stack</span></a></li>
    <li class="car-21__tile"><a class="car-21__frame" href="#"><img src="https://picsum.photos/seed/zoom-3/600/600" width="600" height="600" alt="Poke bowl"><span class="car-21__cap">Ahi Poke Bowl</span></a></li>
    <li class="car-21__tile"><a class="car-21__frame" href="#"><img src="https://picsum.photos/seed/zoom-4/600/600" width="600" height="600" alt="Berry tart"><span class="car-21__cap">Berry Tart</span></a></li>
    <li class="car-21__tile"><a class="car-21__frame" href="#"><img src="https://picsum.photos/seed/zoom-5/600/600" width="600" height="600" alt="Espresso"><span class="car-21__cap">Double Espresso</span></a></li>
  </ul>
</section>
```
## CSS
```css
.car-21,
.car-21 *,
.car-21 *::before,
.car-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-21 ::selection {
  background: #e11d48;
  color: #fff;
}

.car-21 {
  --accent: #e11d48;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 12px;
  background: #fbf5f2;
  display: flex;
  align-items: center;
  justify-content: center;
}

.car-21__rail {
  list-style: none;
  display: flex;
  gap: 16px;
  width: min(760px,100%);
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-padding: 12px;
  padding: 12px;
  scrollbar-width: thin;
  scrollbar-color: #e6cdc6 transparent;
}

.car-21__rail:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
  border-radius: 16px;
}

.car-21__tile {
  flex: 0 0 clamp(180px,60%,220px);
  scroll-snap-align: start;
}

.car-21__frame {
  position: relative;
  display: block;
  aspect-ratio: 1/1;
  border-radius: 16px;
  overflow: hidden;
  text-decoration: none;
  background: #eeddd7;
  box-shadow: 0 14px 30px -22px rgba(120,20,50,.6);
}

.car-21__frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform .55s cubic-bezier(.2,.8,.2,1);
}

.car-21__frame:hover img,
.car-21__frame:focus-visible img,
.car-21__tile:focus-within img {
  transform: scale(1.18);
}

.car-21__cap {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 32px 14px 12px;
  color: #fff;
  font-size: 14px;
  font-weight: 700;
  background: linear-gradient(transparent,rgba(60,10,25,.8));
  opacity: 0;
  transform: translateY(6px);
  transition: opacity .35s,transform .35s;
}

.car-21__frame:hover .car-21__cap,
.car-21__tile:focus-within .car-21__cap {
  opacity: 1;
  transform: translateY(0);
}

.car-21__frame:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .car-21__frame img,
    .car-21__cap {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — hover/focus scales the inner image inside an overflow:hidden frame, so it zooms without moving the layout. */
```
