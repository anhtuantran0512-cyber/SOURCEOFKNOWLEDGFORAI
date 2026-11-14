---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/portfolio-overlay-gallery/"
title: "Portfolio Overlay Gallery"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "A case-study / portfolio rail where each project screenshot reveals its title and category on hover, sliding up from the bottom edge."
has_js: "false"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Portfolio Overlay Gallery
Source: https://codefronts.com/snippets/css-image-carousel/portfolio-overlay-gallery/

A case-study / portfolio rail where each project screenshot reveals its title and category on hover, sliding up from the bottom edge. The classic agency showcase — pure CSS transitions, keyboard-accessible via focus-within.
## HTML
```html
<section class="car-08" aria-label="Selected work">
  <ul class="car-08__rail" tabindex="0" role="group" aria-label="Portfolio projects, scrollable">
    <li class="car-08__card"><a class="car-08__link" href="#"><span class="car-08__frame"><img src="https://picsum.photos/seed/work-1/640/800" width="640" height="800" alt="Fintech dashboard redesign"></span><span class="car-08__cap"><span class="car-08__tag">Product</span><span class="car-08__title">Ledger — Fintech Dashboard</span></span></a></li>
    <li class="car-08__card"><a class="car-08__link" href="#"><span class="car-08__frame"><img src="https://picsum.photos/seed/work-2/640/800" width="640" height="800" alt="Coffee brand identity"></span><span class="car-08__cap"><span class="car-08__tag">Branding</span><span class="car-08__title">Cùrrent — Coffee Identity</span></span></a></li>
    <li class="car-08__card"><a class="car-08__link" href="#"><span class="car-08__frame"><img src="https://picsum.photos/seed/work-3/640/800" width="640" height="800" alt="Travel app case study"></span><span class="car-08__cap"><span class="car-08__tag">Mobile</span><span class="car-08__title">Wander — Travel App</span></span></a></li>
    <li class="car-08__card"><a class="car-08__link" href="#"><span class="car-08__frame"><img src="https://picsum.photos/seed/work-4/640/800" width="640" height="800" alt="E-commerce replatform"></span><span class="car-08__cap"><span class="car-08__tag">Web</span><span class="car-08__title">Maison — E-commerce</span></span></a></li>
  </ul>
</section>
```
## CSS
```css
.car-08,
.car-08 *,
.car-08 *::before,
.car-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-08 ::selection {
  background: #e6ff4d;
  color: #111;
}

.car-08 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 12px;
  background: #111318;
  display: flex;
  align-items: center;
  justify-content: center;
}

.car-08__rail {
  list-style: none;
  display: flex;
  gap: 18px;
  width: min(820px,100%);
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  scroll-padding: 14px;
  padding: 14px;
  scrollbar-width: thin;
  scrollbar-color: #333842 transparent;
}

.car-08__rail:focus-visible {
  outline: 3px solid #e6ff4d;
  outline-offset: 2px;
  border-radius: 16px;
}

.car-08__card {
  flex: 0 0 clamp(220px,72%,260px);
  scroll-snap-align: start;
}

.car-08__link {
  display: block;
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  text-decoration: none;
  background: #1a1d24;
  box-shadow: 0 20px 40px -30px rgba(0,0,0,.9);
}

.car-08__frame {
  display: block;
  aspect-ratio: 4/5;
  overflow: hidden;
}

.car-08__frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform .5s ease;
}

.car-08__link:hover .car-08__frame img,
.car-08__link:focus-visible .car-08__frame img {
  transform: scale(1.07);
}

.car-08__cap {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 44px 18px 18px;
  background: linear-gradient(transparent,rgba(10,11,14,.9));
  transform: translateY(101%);
  opacity: 0;
  transition: transform .4s cubic-bezier(.2,.8,.2,1),opacity .4s;
}

.car-08__link:hover .car-08__cap,
.car-08__link:focus-within .car-08__cap {
  transform: translateY(0);
  opacity: 1;
}

.car-08__tag {
  display: inline-block;
  font-size: 11px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #e6ff4d;
  margin-bottom: 6px;
}

.car-08__title {
  display: block;
  font-size: 16px;
  font-weight: 700;
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .car-08__frame img,
    .car-08__cap {
    transition: none;
  }

  .car-08__cap {
    transform: none;
    opacity: 1;
  }
}
```

## JavaScript
```js
/* No JavaScript — hover/focus-within slides the caption up (translateY) and zooms the image (transform). */
```
