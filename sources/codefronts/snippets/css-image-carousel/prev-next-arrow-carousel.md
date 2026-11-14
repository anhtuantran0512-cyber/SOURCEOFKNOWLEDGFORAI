---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/prev-next-arrow-carousel/"
title: "Prev / Next Arrow Carousel"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "A carousel with real previous/next arrow buttons that step one slide at a time — no library."
has_js: "false"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Prev / Next Arrow Carousel
Source: https://codefronts.com/snippets/css-image-carousel/prev-next-arrow-carousel/

A carousel with real previous/next arrow buttons that step one slide at a time — no library. Uses the new CSS ::scroll-button() pseudo-elements for native, accessible arrows, with an anchor-link fallback so older browsers still get working controls.
## HTML
```html
<section class="car-17" aria-label="Featured shots">
  <div class="car-17__wrap">
    <ul class="car-17__scroller" id="car-17-scroller" tabindex="0" role="group" aria-label="Shots, use the arrow buttons or arrow keys">
      <li class="car-17__slide" id="car-17-s1"><img src="https://picsum.photos/seed/arrow-1/900/560" width="900" height="560" alt="City skyline"></li>
      <li class="car-17__slide" id="car-17-s2"><img src="https://picsum.photos/seed/arrow-2/900/560" width="900" height="560" alt="Desert highway"></li>
      <li class="car-17__slide" id="car-17-s3"><img src="https://picsum.photos/seed/arrow-3/900/560" width="900" height="560" alt="Rainforest canopy"></li>
      <li class="car-17__slide" id="car-17-s4"><img src="https://picsum.photos/seed/arrow-4/900/560" width="900" height="560" alt="Frozen lake"></li>
    </ul>
    <nav class="car-17__fallback" aria-label="Slide navigation (fallback)">
      <a class="car-17__arrow" href="#car-17-s1" aria-label="Previous">‹</a>
      <a class="car-17__arrow" href="#car-17-s4" aria-label="Next">›</a>
    </nav>
  </div>
</section>
```
## CSS
```css
.car-17,
.car-17 *,
.car-17 *::before,
.car-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-17 ::selection {
  background: #2563eb;
  color: #fff;
}

.car-17 {
  --accent: #2563eb;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #eef2fb;
  display: flex;
  align-items: center;
  justify-content: center;
}

.car-17__wrap {
  width: min(620px,100%);
  position: relative;
}

.car-17__scroller {
  list-style: none;
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  border-radius: 16px;
  scrollbar-width: none;
  box-shadow: 0 24px 50px -34px rgba(20,40,120,.5);
}

.car-17__scroller::-webkit-scrollbar {
  display: none;
}

.car-17__scroller:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.car-17__slide {
  flex: 0 0 100%;
  scroll-snap-align: center;
  scroll-margin: 0;
  aspect-ratio: 16/10;
  overflow: hidden;
}

.car-17__slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.car-17__scroller::scroll-button(left),
.car-17__scroller::scroll-button(right) {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 3;
  width: 44px;
  height: 44px;
  border: 0;
  border-radius: 50%;
  cursor: pointer;
  background: #fff;
  color: var(--accent);
  font-size: 22px;
  font-weight: 700;
  line-height: 1;
  box-shadow: 0 8px 20px -8px rgba(20,40,120,.6);
  transition: transform .2s,opacity .2s;
}

.car-17__scroller::scroll-button(left) {
  content: "‹";
  left: 12px;
}

.car-17__scroller::scroll-button(right) {
  content: "›";
  right: 12px;
}

.car-17__scroller::scroll-button(left):hover,
.car-17__scroller::scroll-button(right):hover {
  transform: translateY(-50%) scale(1.08);
}

.car-17__scroller::scroll-button(left):disabled,
.car-17__scroller::scroll-button(right):disabled {
  opacity: .35;
  cursor: default;
}

.car-17__scroller::scroll-button(left):focus-visible,
.car-17__scroller::scroll-button(right):focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}
/* Anchor-link fallback arrows (hidden where ::scroll-button is supported) */

.car-17__fallback {
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.car-17__arrow {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  pointer-events: auto;
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: #fff;
  color: var(--accent);
  font-size: 26px;
  font-weight: 700;
  text-decoration: none;
  box-shadow: 0 8px 20px -8px rgba(20,40,120,.6);
  transition: transform .2s;
}

.car-17__arrow:first-child {
  left: 12px;
}

.car-17__arrow:last-child {
  right: 12px;
}

.car-17__arrow:hover {
  transform: translateY(-50%) scale(1.08);
}

.car-17__arrow:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@supports selector(::scroll-button(right)) {
  .car-17__fallback {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-17__scroller {
    scroll-behavior: auto;
  }
}
```

## JavaScript
```js
/* No JavaScript — native ::scroll-button(left/right) page the scroll-snap scroller (Chromium 135+); anchor-link arrows (#slide-n) are the universal fallback, hidden via @supports where the pseudo is available. */
```
