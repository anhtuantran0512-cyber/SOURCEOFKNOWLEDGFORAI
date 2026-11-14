---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/autoplay-css-slider/"
title: "Autoplay CSS Slider"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "A hands-off carousel that advances itself, translating a single track through each slide on a CSS keyframe loop and pausing the moment a user hovers or…"
has_js: "false"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Autoplay CSS Slider
Source: https://codefronts.com/snippets/css-image-carousel/autoplay-css-slider/

A hands-off carousel that advances itself, translating a single track through each slide on a CSS keyframe loop and pausing the moment a user hovers or focuses it. The lightweight auto-rotating banner — zero JavaScript, zero timers.
## HTML
```html
<section class="car-20" aria-label="Auto-rotating banner" aria-roledescription="carousel">
  <div class="car-20__viewport">
    <div class="car-20__track">
      <div class="car-20__slide"><img src="https://picsum.photos/seed/auto-1/1000/500" width="1000" height="500" alt="Summer sale banner"></div>
      <div class="car-20__slide"><img src="https://picsum.photos/seed/auto-2/1000/500" width="1000" height="500" alt="New arrivals banner"></div>
      <div class="car-20__slide"><img src="https://picsum.photos/seed/auto-3/1000/500" width="1000" height="500" alt="Free shipping banner"></div>
    </div>
    <div class="car-20__bars" aria-hidden="true"><span></span><span></span><span></span></div>
  </div>
</section>
```
## CSS
```css
.car-20,
.car-20 *,
.car-20 *::before,
.car-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-20 ::selection {
  background: #db2777;
  color: #fff;
}

.car-20 {
  --accent: #db2777;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #1a0f18;
  display: flex;
  align-items: center;
  justify-content: center;
}

.car-20__viewport {
  position: relative;
  width: min(680px,100%);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 26px 50px -32px rgba(0,0,0,.9);
}

.car-20__track {
  display: flex;
  width: 300%;
  animation: car-20-slide 15s infinite;
}

.car-20__viewport:hover .car-20__track,
.car-20__viewport:focus-within .car-20__track,
.car-20__viewport:hover .car-20__bars span,
.car-20__viewport:focus-within .car-20__bars span {
  animation-play-state: paused;
}

.car-20__slide {
  width: calc(100%/3);
  aspect-ratio: 2/1;
}

.car-20__slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.car-20__bars {
  position: absolute;
  left: 14px;
  right: 14px;
  bottom: 14px;
  display: flex;
  gap: 8px;
}

.car-20__bars span {
  flex: 1;
  height: 4px;
  border-radius: 999px;
  background: rgba(255,255,255,.35);
  overflow: hidden;
  position: relative;
}

.car-20__bars span::after {
  content: "";
  position: absolute;
  inset: 0;
  background: var(--accent);
  transform-origin: left;
  transform: scaleX(0);
}

.car-20__bars span:nth-child(1)::after {
  animation: car-20-bar 15s infinite;
  animation-delay: 0s;
}

.car-20__bars span:nth-child(2)::after {
  animation: car-20-bar 15s infinite;
  animation-delay: -10s;
}

.car-20__bars span:nth-child(3)::after {
  animation: car-20-bar 15s infinite;
  animation-delay: -5s;
}

@keyframes car-20-slide {
  0%,
    28% {
    transform: translateX(0);
  }

  33%,
    61% {
    transform: translateX(-33.3333%);
  }

  66%,
    94% {
    transform: translateX(-66.6666%);
  }

  100% {
    transform: translateX(0);
  }
}

@keyframes car-20-bar {
  0% {
    transform: scaleX(0);
  }

  28% {
    transform: scaleX(1);
  }

  33%,
    100% {
    transform: scaleX(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-20__track {
    animation: none;
  }

  .car-20__bars {
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a single keyframe steps the track's translateX through each slide; hover/focus pauses playback and the progress bars. */
```
