---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/testimonial-card-carousel/"
title: "Testimonial Card Carousel"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "A swipeable rail of review cards — each with a star rating, quote and avatar — snapping neatly one per view on mobile and two-up on wider screens."
has_js: "false"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Testimonial Card Carousel
Source: https://codefronts.com/snippets/css-image-carousel/testimonial-card-carousel/

A swipeable rail of review cards — each with a star rating, quote and avatar — snapping neatly one per view on mobile and two-up on wider screens. The social-proof carousel for landing pages, built on scroll-snap with no library.
## HTML
```html
<section class="car-06" aria-label="Customer testimonials">
  <ul class="car-06__rail" tabindex="0" role="group" aria-label="Customer reviews, scrollable">
    <li class="car-06__card">
      <div class="car-06__stars" role="img" aria-label="Rated 5 out of 5"><span class="car-06__fill" style="width:100%"></span></div>
      <p class="car-06__quote">"Swapped our slider library for this and shaved 40&nbsp;KB off the bundle. Scroll feel is better than what we replaced."</p>
      <div class="car-06__who"><img class="car-06__ava" src="https://picsum.photos/seed/ava-1/96/96" width="96" height="96" alt=""><span><b>Priya N.</b><small>Front-end Lead, UK</small></span></div>
    </li>
    <li class="car-06__card">
      <div class="car-06__stars" role="img" aria-label="Rated 4.5 out of 5"><span class="car-06__fill" style="width:90%"></span></div>
      <p class="car-06__quote">"Perfect CLS score after switching to the aspect-ratio pattern here. Copy-paste took ten minutes."</p>
      <div class="car-06__who"><img class="car-06__ava" src="https://picsum.photos/seed/ava-2/96/96" width="96" height="96" alt=""><span><b>Marcus T.</b><small>Web Dev, US</small></span></div>
    </li>
    <li class="car-06__card">
      <div class="car-06__stars" role="img" aria-label="Rated 5 out of 5"><span class="car-06__fill" style="width:100%"></span></div>
      <p class="car-06__quote">"Finally a carousel my keyboard users can actually operate. Focus ring and arrow keys just work."</p>
      <div class="car-06__who"><img class="car-06__ava" src="https://picsum.photos/seed/ava-3/96/96" width="96" height="96" alt=""><span><b>Alira K.</b><small>UX Engineer, AU</small></span></div>
    </li>
  </ul>
</section>
```
## CSS
```css
.car-06,
.car-06 *,
.car-06 *::before,
.car-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-06 ::selection {
  background: oklch(0.62 0.15 285);
  color: #fff;
}

.car-06 {
  --accent: oklch(0.62 0.15 285);
  --star: #f5a623;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 12px;
  background: #f5f4f9;
  display: flex;
  align-items: center;
  justify-content: center;
}

.car-06__rail {
  list-style: none;
  display: flex;
  gap: 18px;
  width: min(760px,100%);
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-padding: 10px;
  padding: 10px;
  scrollbar-width: thin;
  scrollbar-color: #d5d2e2 transparent;
}

.car-06__rail:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
  border-radius: 16px;
}

.car-06__card {
  flex: 0 0 clamp(240px,82%,320px);
  scroll-snap-align: center;
  background: #fff;
  border: 1px solid #e9e7f1;
  border-radius: 18px;
  padding: 24px 22px;
  box-shadow: 0 16px 34px -28px rgba(40,30,80,.7);
  transition: transform .25s;
}

.car-06__card:hover {
  transform: translateY(-4px);
}

.car-06__stars {
  position: relative;
  width: 112px;
  height: 18px;
  -webkit-mask: repeat-x left/22.4px 18px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 2l3 6.3 6.9.9-5 4.8 1.2 6.9L12 17.7 5.9 20.9 7.1 14 2.1 9.2 9 8.3z'/%3E%3C/svg%3E");
  mask: repeat-x left/22.4px 18px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 2l3 6.3 6.9.9-5 4.8 1.2 6.9L12 17.7 5.9 20.9 7.1 14 2.1 9.2 9 8.3z'/%3E%3C/svg%3E");
  background: #e4e2ee;
}

.car-06__fill {
  position: absolute;
  inset: 0;
  background: var(--star);
  display: block;
}

.car-06__quote {
  margin: 16px 0 20px;
  font-size: 15px;
  line-height: 1.55;
  color: #33303d;
  text-wrap: pretty;
}

.car-06__who {
  display: flex;
  align-items: center;
  gap: 12px;
}

.car-06__ava {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  object-fit: cover;
  flex: none;
  background: #e4e2ee;
}

.car-06__who b {
  display: block;
  font-size: 14px;
  color: #26232f;
}

.car-06__who small {
  display: block;
  font-size: 12px;
  color: #8b8797;
  margin-top: 1px;
}

@media (min-width: 600px) {
  .car-06__card {
    flex-basis: calc((100% - 18px)/2);
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-06__card {
    transition: none;
  }

  .car-06__rail {
    scroll-behavior: auto;
  }
}
```

## JavaScript
```js
/* No JavaScript — scroll-snap rail; star ratings are a masked gradient so half-stars work without images. */
```
