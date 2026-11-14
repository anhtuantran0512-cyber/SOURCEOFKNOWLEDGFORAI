---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/netflix-style-row-carousel/"
title: "Netflix-Style Row Carousel"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "The canonical Netflix / Disney+ / HBO Max / Prime Video content row: horizontal-scrolling 16:9 title cards that scale up and reveal metadata on hover, with…"
has_js: "true"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Netflix-Style Row Carousel
Source: https://codefronts.com/snippets/css-image-carousel/netflix-style-row-carousel/

The canonical Netflix / Disney+ / HBO Max / Prime Video content row: horizontal-scrolling 16:9 title cards that scale up and reveal metadata on hover, with side prev/next arrow buttons that appear on row-hover and edge-fade gradients that hint at off-screen content. CSS handles the scroll-snap layout and hover zoom; a 5-line vanilla JS handler steps the row by one viewport-width per arrow click (exactly Netflix's paging behaviour).
## HTML
```html
<section class="car-09" aria-label="Trending now">
  <h3 class="car-09__head">Trending now</h3>
  <div class="car-09__wrap">
    <button type="button" class="car-09__nav car-09__nav--prev" data-dir="-1" aria-label="Scroll row left">
      <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M15 6l-6 6 6 6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </button>
    <div class="car-09__edge">
      <ul class="car-09__row" tabindex="0" role="group" aria-label="Trending titles, scrollable">
        <li class="car-09__tile"><a href="#"><span class="car-09__thumb"><img src="https://picsum.photos/seed/flix-a/640/360" width="640" height="360" alt="Nightfall"></span><span class="car-09__meta"><span class="car-09__title">Nightfall</span><span class="car-09__sub">Series · 2025 · Thriller</span></span></a></li>
        <li class="car-09__tile"><a href="#"><span class="car-09__thumb"><img src="https://picsum.photos/seed/flix-b/640/360" width="640" height="360" alt="The Long Coast"></span><span class="car-09__meta"><span class="car-09__title">The Long Coast</span><span class="car-09__sub">Film · 2024 · Drama</span></span></a></li>
        <li class="car-09__tile"><a href="#"><span class="car-09__thumb"><img src="https://picsum.photos/seed/flix-c/640/360" width="640" height="360" alt="Ember"></span><span class="car-09__meta"><span class="car-09__title">Ember</span><span class="car-09__sub">Series · 2025 · Sci-Fi</span></span></a></li>
        <li class="car-09__tile"><a href="#"><span class="car-09__thumb"><img src="https://picsum.photos/seed/flix-d/640/360" width="640" height="360" alt="Static"></span><span class="car-09__meta"><span class="car-09__title">Static</span><span class="car-09__sub">Series · 2023 · Mystery</span></span></a></li>
        <li class="car-09__tile"><a href="#"><span class="car-09__thumb"><img src="https://picsum.photos/seed/flix-e/640/360" width="640" height="360" alt="Meridian"></span><span class="car-09__meta"><span class="car-09__title">Meridian</span><span class="car-09__sub">Film · 2025 · Adventure</span></span></a></li>
        <li class="car-09__tile"><a href="#"><span class="car-09__thumb"><img src="https://picsum.photos/seed/flix-f/640/360" width="640" height="360" alt="Halflight"></span><span class="car-09__meta"><span class="car-09__title">Halflight</span><span class="car-09__sub">Series · 2024 · Horror</span></span></a></li>
        <li class="car-09__tile"><a href="#"><span class="car-09__thumb"><img src="https://picsum.photos/seed/flix-g/640/360" width="640" height="360" alt="Undertow"></span><span class="car-09__meta"><span class="car-09__title">Undertow</span><span class="car-09__sub">Film · 2025 · Thriller</span></span></a></li>
        <li class="car-09__tile"><a href="#"><span class="car-09__thumb"><img src="https://picsum.photos/seed/flix-h/640/360" width="640" height="360" alt="Blackwater"></span><span class="car-09__meta"><span class="car-09__title">Blackwater</span><span class="car-09__sub">Series · 2024 · Crime</span></span></a></li>
      </ul>
    </div>
    <button type="button" class="car-09__nav car-09__nav--next" data-dir="1" aria-label="Scroll row right">
      <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M9 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
    </button>
  </div>
</section>
```
## CSS
```css
.car-09,
.car-09 *,
.car-09 *::before,
.car-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-09 ::selection {
  background: #e50914;
  color: #fff;
}

.car-09 {
  --accent: #e50914;
  --tile-w: clamp(220px,28vw,300px);
  font-family: 'Netflix Sans','Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 0;
  background: #0b0b0f;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.car-09__head {
  color: #f5f5f7;
  font-size: 20px;
  font-weight: 800;
  margin: 0 0 14px;
  padding: 0 clamp(16px,5vw,48px);
  letter-spacing: -0.02em;
}

.car-09__wrap {
  position: relative;
}

.car-09__edge {
  -webkit-mask: linear-gradient(90deg,transparent,#000 4%,#000 96%,transparent);
  mask: linear-gradient(90deg,transparent,#000 4%,#000 96%,transparent);
}

.car-09__row {
  list-style: none;
  display: flex;
  gap: 6px;
  overflow-x: auto;
  scroll-snap-type: x proximity;
  scroll-behavior: smooth;
  padding: 34px clamp(16px,5vw,48px);
  scrollbar-width: none;
}

.car-09__row::-webkit-scrollbar {
  display: none;
}

.car-09__row:focus-visible {
  outline: none;
}

.car-09__tile {
  flex: 0 0 var(--tile-w);
  scroll-snap-align: start;
  position: relative;
  transition: transform .32s cubic-bezier(.2,.8,.2,1);
  transform-origin: center center;
}

.car-09__tile a {
  display: block;
  position: relative;
  border-radius: 6px;
  overflow: hidden;
  text-decoration: none;
  background: #1a1a20;
  box-shadow: 0 12px 26px -18px #000;
}

.car-09__tile a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.car-09__thumb {
  display: block;
  position: relative;
  width: 100%;
  aspect-ratio: 16/9;
  overflow: hidden;
  background: #1a1a20;
}

.car-09__thumb img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.car-09__tile:hover,
.car-09__tile:focus-within {
  transform: scale(1.32);
  z-index: 3;
}

.car-09__tile:hover:first-child,
.car-09__tile:focus-within:first-child {
  transform-origin: left center;
  transform: scale(1.32) translateX(2%);
}

.car-09__tile:hover:last-child,
.car-09__tile:focus-within:last-child {
  transform-origin: right center;
  transform: scale(1.32) translateX(-2%);
}

.car-09__tile:hover a,
.car-09__tile:focus-within a {
  box-shadow: 0 24px 48px -16px rgba(0,0,0,.9),0 0 0 2px rgba(255,255,255,.06);
}

.car-09__meta {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 44px 12px 10px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  background: linear-gradient(transparent,rgba(0,0,0,.85) 55%,rgba(0,0,0,.95));
  opacity: 0;
  transition: opacity .28s ease .06s;
  pointer-events: none;
}

.car-09__title {
  font-size: 14px;
  font-weight: 700;
  color: #fff;
  letter-spacing: -0.01em;
  line-height: 1.2;
}

.car-09__sub {
  font-size: 10.5px;
  font-weight: 600;
  color: rgba(255,255,255,.7);
  letter-spacing: 0.02em;
}

.car-09__tile:hover .car-09__meta,
.car-09__tile:focus-within .car-09__meta {
  opacity: 1;
}

.car-09__nav {
  position: absolute;
  top: 15px;
  z-index: 4;
  width: 38px;
  height: calc(100% - 30px);
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(20,20,20,.5);
  color: #fff;
  border: 0;
  padding: 0;
  cursor: pointer;
  font: inherit;
  opacity: 0;
  transition: opacity .2s,background .2s;
}

.car-09__nav--prev {
  left: 0;
}

.car-09__nav--next {
  right: 0;
}

.car-09__wrap:hover .car-09__nav,
.car-09__wrap:focus-within .car-09__nav {
  opacity: 1;
}

.car-09__nav:hover {
  background: rgba(20,20,20,.85);
}

.car-09__nav:focus-visible {
  opacity: 1;
  outline: 2px solid var(--accent);
  outline-offset: -4px;
}

@media (max-width: 640px) {
  .car-09 {
    --tile-w: clamp(180px,60vw,240px);
  }

  .car-09__nav {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-09__tile,
    .car-09__meta,
    .car-09__row,
    .car-09__nav {
    transition: none;
    scroll-behavior: auto;
  }
}
```

## JavaScript
```js
const row = document.querySelector('.car-09__row');
document.querySelectorAll('.car-09__nav').forEach((btn) => {
  btn.addEventListener('click', () => {
    const dir = Number(btn.dataset.dir);
    row.scrollBy({ left: dir * row.clientWidth * 0.9, behavior: 'smooth' });
  });
});
```
