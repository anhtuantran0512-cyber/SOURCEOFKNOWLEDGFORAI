---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/shop-the-look-card-slider/"
title: "Shop the Look Card Slider"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "A horizontal product-card rail that shows three to four cards on desktop and glides one-per-view on mobile — the 'complete the look' / 'you may also like'…"
has_js: "false"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Shop the Look Card Slider
Source: https://codefronts.com/snippets/css-image-carousel/shop-the-look-card-slider/

A horizontal product-card rail that shows three to four cards on desktop and glides one-per-view on mobile — the 'complete the look' / 'you may also like' pattern. Built entirely on CSS scroll-snap, so it's flick-scrollable on touch and keyboard-scrollable on desktop.
## HTML
```html
<section class="car-02" aria-label="Shop the look product rail">
  <div class="car-02__wrap">
    <h3 class="car-02__head">Complete the look</h3>
    <ul class="car-02__rail" tabindex="0" role="group" aria-label="Recommended products, scrollable">
      <li class="car-02__card"><div class="car-02__ph"><img src="https://picsum.photos/seed/look-1/500/600" width="500" height="600" alt="Oversized wool coat"></div><div class="car-02__meta"><span class="car-02__name">Wool Overcoat</span><span class="car-02__price">$248</span></div></li>
      <li class="car-02__card"><div class="car-02__ph"><img src="https://picsum.photos/seed/look-2/500/600" width="500" height="600" alt="Ribbed knit scarf"></div><div class="car-02__meta"><span class="car-02__name">Ribbed Scarf</span><span class="car-02__price">$54</span></div></li>
      <li class="car-02__card"><div class="car-02__ph"><img src="https://picsum.photos/seed/look-3/500/600" width="500" height="600" alt="Leather ankle boots"></div><div class="car-02__meta"><span class="car-02__name">Ankle Boots</span><span class="car-02__price">$189</span></div></li>
      <li class="car-02__card"><div class="car-02__ph"><img src="https://picsum.photos/seed/look-4/500/600" width="500" height="600" alt="Canvas crossbody bag"></div><div class="car-02__meta"><span class="car-02__name">Crossbody Bag</span><span class="car-02__price">$96</span></div></li>
      <li class="car-02__card"><div class="car-02__ph"><img src="https://picsum.photos/seed/look-5/500/600" width="500" height="600" alt="Round tortoiseshell sunglasses"></div><div class="car-02__meta"><span class="car-02__name">Sunglasses</span><span class="car-02__price">$72</span></div></li>
    </ul>
  </div>
</section>
```
## CSS
```css
.car-02,
.car-02 *,
.car-02 *::before,
.car-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-02 ::selection {
  background: oklch(0.55 0.14 25);
  color: #fff;
}

.car-02 {
  --accent: oklch(0.55 0.14 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 12px;
  background: #faf7f5;
  display: flex;
  align-items: center;
  justify-content: center;
}

.car-02__wrap {
  width: min(760px,100%);
}

.car-02__head {
  font-size: 15px;
  font-weight: 700;
  letter-spacing: .02em;
  color: #2a211d;
  margin: 0 8px 14px;
}

.car-02__rail {
  list-style: none;
  display: flex;
  gap: 16px;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-padding-left: 8px;
  padding: 6px 8px 16px;
  scrollbar-width: thin;
  scrollbar-color: #d9cfc9 transparent;
}

.car-02__rail:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
  border-radius: 12px;
}

.car-02__card {
  flex: 0 0 clamp(200px,70%,236px);
  scroll-snap-align: start;
  background: #fff;
  border: 1px solid #eee3dd;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 12px 30px -26px rgba(60,30,20,.7);
  transition: transform .25s,box-shadow .25s;
}

.car-02__card:hover {
  transform: translateY(-4px);
  box-shadow: 0 18px 36px -24px rgba(60,30,20,.6);
}

.car-02__ph {
  aspect-ratio: 5/6;
  background: #efe6e0;
}

.car-02__ph img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.car-02__meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 12px 14px 14px;
}

.car-02__name {
  font-size: 14px;
  font-weight: 600;
  color: #2a211d;
}

.car-02__price {
  font-size: 14px;
  font-weight: 700;
  color: var(--accent);
}

@media (min-width: 560px) {
  .car-02__card {
    flex-basis: calc((100% - 32px)/3);
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-02__card {
    transition: none;
  }

  .car-02__rail {
    scroll-behavior: auto;
  }
}
```

## JavaScript
```js
/* No JavaScript — CSS scroll-snap (x mandatory) plus a focusable, arrow-key-scrollable rail. */
```
