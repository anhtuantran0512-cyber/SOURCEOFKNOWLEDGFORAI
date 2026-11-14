---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/dual-opposite-direction-slider/"
title: "Dual Opposite-Direction Slider"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "Two image tracks gliding in opposite directions — the top row drifts left while the bottom drifts right — for a dynamic, layered marquee band."
has_js: "false"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dual Opposite-Direction Slider
Source: https://codefronts.com/snippets/css-image-carousel/dual-opposite-direction-slider/

Two image tracks gliding in opposite directions — the top row drifts left while the bottom drifts right — for a dynamic, layered marquee band. A striking hero or footer strip built purely from CSS keyframes, paused on hover.
## HTML
```html
<section class="car-15" aria-label="Moodboard marquee">
  <div class="car-15__band">
    <ul class="car-15__track car-15__track--a">
      <li class="car-15__tile"><img src="https://picsum.photos/seed/du-1/300/220" width="300" height="220" alt="Studio still life"></li>
      <li class="car-15__tile"><img src="https://picsum.photos/seed/du-2/300/220" width="300" height="220" alt="Architectural detail"></li>
      <li class="car-15__tile"><img src="https://picsum.photos/seed/du-3/300/220" width="300" height="220" alt="Textile close-up"></li>
      <li class="car-15__tile"><img src="https://picsum.photos/seed/du-4/300/220" width="300" height="220" alt="Product on plinth"></li>
      <li class="car-15__tile" aria-hidden="true"><img src="https://picsum.photos/seed/du-1/300/220" width="300" height="220" alt=""></li>
      <li class="car-15__tile" aria-hidden="true"><img src="https://picsum.photos/seed/du-2/300/220" width="300" height="220" alt=""></li>
      <li class="car-15__tile" aria-hidden="true"><img src="https://picsum.photos/seed/du-3/300/220" width="300" height="220" alt=""></li>
      <li class="car-15__tile" aria-hidden="true"><img src="https://picsum.photos/seed/du-4/300/220" width="300" height="220" alt=""></li>
    </ul>
    <ul class="car-15__track car-15__track--b">
      <li class="car-15__tile"><img src="https://picsum.photos/seed/du-5/300/220" width="300" height="220" alt="Gradient backdrop"></li>
      <li class="car-15__tile"><img src="https://picsum.photos/seed/du-6/300/220" width="300" height="220" alt="Ceramic vessels"></li>
      <li class="car-15__tile"><img src="https://picsum.photos/seed/du-7/300/220" width="300" height="220" alt="Folded paper"></li>
      <li class="car-15__tile"><img src="https://picsum.photos/seed/du-8/300/220" width="300" height="220" alt="Woven basket"></li>
      <li class="car-15__tile" aria-hidden="true"><img src="https://picsum.photos/seed/du-5/300/220" width="300" height="220" alt=""></li>
      <li class="car-15__tile" aria-hidden="true"><img src="https://picsum.photos/seed/du-6/300/220" width="300" height="220" alt=""></li>
      <li class="car-15__tile" aria-hidden="true"><img src="https://picsum.photos/seed/du-7/300/220" width="300" height="220" alt=""></li>
      <li class="car-15__tile" aria-hidden="true"><img src="https://picsum.photos/seed/du-8/300/220" width="300" height="220" alt=""></li>
    </ul>
  </div>
</section>
```
## CSS
```css
.car-15,
.car-15 *,
.car-15 *::before,
.car-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-15 ::selection {
  background: #f43f5e;
  color: #fff;
}

.car-15 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 0;
  background: #14121a;
  display: flex;
  align-items: center;
  justify-content: center;
}

.car-15__band {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 16px;
  overflow: hidden;
  -webkit-mask: linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);
  mask: linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);
}

.car-15__track {
  list-style: none;
  display: flex;
  gap: 16px;
  width: max-content;
}

.car-15__track--a {
  animation: car-15-run 30s linear infinite;
}

.car-15__track--b {
  animation: car-15-run 30s linear infinite reverse;
}

.car-15__band:hover .car-15__track,
.car-15__band:focus-within .car-15__track {
  animation-play-state: paused;
}

.car-15__tile {
  flex: none;
  width: 210px;
  aspect-ratio: 15/11;
  border-radius: 12px;
  overflow: hidden;
  background: #221f2b;
}

.car-15__tile img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

@keyframes car-15-run {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(-50%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-15__track {
    animation: none;
    flex-wrap: wrap;
    justify-content: center;
    width: auto;
  }
}
```

## JavaScript
```js
/* No JavaScript — two duplicated tracks, one running the -50% keyframe forwards and one in reverse, counter-scroll seamlessly. */
```
