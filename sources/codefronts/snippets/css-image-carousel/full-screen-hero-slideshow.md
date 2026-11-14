---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/full-screen-hero-slideshow/"
title: "Full-Screen Hero Slideshow"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "A high-impact, auto-advancing hero banner that cross-fades between full-bleed images with a headline on top — the above-the-fold slideshow for agency and…"
has_js: "false"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full-Screen Hero Slideshow
Source: https://codefronts.com/snippets/css-image-carousel/full-screen-hero-slideshow/

A high-impact, auto-advancing hero banner that cross-fades between full-bleed images with a headline on top — the above-the-fold slideshow for agency and product landing pages. Runs on a single CSS keyframe timeline, pauses on hover, and freezes for reduced-motion users.
## HTML
```html
<section class="car-05" aria-label="Featured highlights slideshow" aria-roledescription="carousel">
  <div class="car-05__deck">
    <div class="car-05__slide"><img src="https://picsum.photos/seed/hero-peaks/1600/900" width="1600" height="900" alt="Mist over mountain peaks at dawn"></div>
    <div class="car-05__slide"><img src="https://picsum.photos/seed/hero-coast/1600/900" width="1600" height="900" alt="Rugged coastline at golden hour"></div>
    <div class="car-05__slide"><img src="https://picsum.photos/seed/hero-forest/1600/900" width="1600" height="900" alt="Sun beams through a pine forest"></div>
    <div class="car-05__overlay">
      <p class="car-05__kicker">New Season</p>
      <h2 class="car-05__title">Go further,<br>pack lighter</h2>
      <a class="car-05__cta" href="#">Explore the collection</a>
    </div>
  </div>
</section>
```
## CSS
```css
.car-05,
.car-05 *,
.car-05 *::before,
.car-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-05 ::selection {
  background: #fff;
  color: #111;
}

.car-05 {
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.car-05__deck {
  position: relative;
  height: 100vh;
  min-height: 520px;
  overflow: hidden;
  background: #0d0f12;
}

.car-05__slide {
  position: absolute;
  inset: 0;
  opacity: 0;
  animation: car-05-fade 15s ease-in-out infinite;
}

.car-05__slide:nth-child(1) {
  animation-delay: 0s;
}

.car-05__slide:nth-child(2) {
  animation-delay: -5s;
}

.car-05__slide:nth-child(3) {
  animation-delay: -10s;
}

.car-05__slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.car-05__slide::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg,rgba(8,10,14,.72),rgba(8,10,14,.15) 60%,transparent);
}

.car-05__deck:hover .car-05__slide,
.car-05__deck:focus-within .car-05__slide {
  animation-play-state: paused;
}

.car-05__overlay {
  position: absolute;
  left: 0;
  bottom: 0;
  z-index: 2;
  padding: clamp(28px,6vw,72px);
  max-width: 640px;
  color: #fff;
}

.car-05__kicker {
  font-size: 13px;
  letter-spacing: .24em;
  text-transform: uppercase;
  opacity: .85;
  margin-bottom: 14px;
}

.car-05__title {
  font-size: clamp(38px,7vw,72px);
  line-height: 1.02;
  font-weight: 800;
  letter-spacing: -.02em;
  text-shadow: 0 2px 30px rgba(0,0,0,.4);
}

.car-05__cta {
  display: inline-block;
  margin-top: 26px;
  padding: 14px 26px;
  border-radius: 999px;
  background: #fff;
  color: #111;
  font-weight: 700;
  font-size: 14px;
  text-decoration: none;
  transition: transform .2s,box-shadow .2s;
}

.car-05__cta:hover {
  transform: translateY(-2px);
  box-shadow: 0 14px 30px -14px rgba(0,0,0,.6);
}

@keyframes car-05-fade {
  0% {
    opacity: 0;
  }

  5% {
    opacity: 1;
  }

  28% {
    opacity: 1;
  }

  33% {
    opacity: 0;
  }

  100% {
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-05__slide {
    animation: none;
  }

  .car-05__slide:first-child {
    opacity: 1;
  }

  .car-05__cta {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a shared staggered opacity keyframe (negative animation-delay per slide) drives the auto cross-fade; hover/focus pauses it. */
```
