---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/accordion-expanding-carousel/"
title: "Accordion Expanding Carousel"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "A row of tall image panels where hovering or focusing one expands it wide while the others shrink to slivers — the interactive 'accordion gallery' seen on…"
has_js: "false"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accordion Expanding Carousel
Source: https://codefronts.com/snippets/css-image-carousel/accordion-expanding-carousel/

A row of tall image panels where hovering or focusing one expands it wide while the others shrink to slivers — the interactive 'accordion gallery' seen on premium landing pages. Pure CSS flex, with a caption that reveals in the active panel.
## HTML
```html
<section class="car-19" aria-label="Expanding image panels">
  <ul class="car-19__row">
    <li class="car-19__panel"><a class="car-19__link" href="#"><img src="https://picsum.photos/seed/acc-1/700/900" width="700" height="900" alt="Modernist villa"><span class="car-19__cap"><b>Villa Sereno</b><small>Coastal retreat</small></span></a></li>
    <li class="car-19__panel"><a class="car-19__link" href="#"><img src="https://picsum.photos/seed/acc-2/700/900" width="700" height="900" alt="Loft interior"><span class="car-19__cap"><b>Union Loft</b><small>City living</small></span></a></li>
    <li class="car-19__panel"><a class="car-19__link" href="#"><img src="https://picsum.photos/seed/acc-3/700/900" width="700" height="900" alt="Cabin in the woods"><span class="car-19__cap"><b>Pine Cabin</b><small>Forest escape</small></span></a></li>
    <li class="car-19__panel"><a class="car-19__link" href="#"><img src="https://picsum.photos/seed/acc-4/700/900" width="700" height="900" alt="Desert house"><span class="car-19__cap"><b>Dune House</b><small>Desert calm</small></span></a></li>
    <li class="car-19__panel"><a class="car-19__link" href="#"><img src="https://picsum.photos/seed/acc-5/700/900" width="700" height="900" alt="Lakeside home"><span class="car-19__cap"><b>Still Water</b><small>Lakeside</small></span></a></li>
  </ul>
</section>
```
## CSS
```css
.car-19,
.car-19 *,
.car-19 *::before,
.car-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-19 ::selection {
  background: #d97706;
  color: #fff;
}

.car-19 {
  --accent: #d97706;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #17140f;
  display: flex;
  align-items: center;
  justify-content: center;
}

.car-19__row {
  list-style: none;
  display: flex;
  gap: 10px;
  width: min(820px,100%);
  height: min(440px,70vh);
}

.car-19__panel {
  flex: 1 1 0;
  min-width: 0;
  transition: flex-grow .5s cubic-bezier(.2,.8,.2,1);
}

.car-19__panel:hover,
.car-19__panel:focus-within {
  flex-grow: 5;
}

.car-19__link {
  position: relative;
  display: block;
  height: 100%;
  border-radius: 14px;
  overflow: hidden;
  text-decoration: none;
  background: #221d16;
}

.car-19__link img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  filter: brightness(.72);
  transition: filter .5s;
}

.car-19__panel:hover .car-19__link img,
.car-19__panel:focus-within .car-19__link img {
  filter: brightness(1);
}

.car-19__cap {
  position: absolute;
  left: 16px;
  bottom: 16px;
  right: 16px;
  color: #fff;
  opacity: 0;
  transform: translateY(10px);
  transition: opacity .4s .1s,transform .4s .1s;
  white-space: nowrap;
}

.car-19__panel:hover .car-19__cap,
.car-19__panel:focus-within .car-19__cap {
  opacity: 1;
  transform: translateY(0);
}

.car-19__cap b {
  display: block;
  font-size: 18px;
}

.car-19__cap small {
  display: block;
  font-size: 12.5px;
  color: #e9d3a8;
  margin-top: 2px;
}

.car-19__link:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .car-19__panel,
    .car-19__link img,
    .car-19__cap {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — hover/focus-within raises the active panel's flex-grow so it expands and neighbours shrink. */
```
