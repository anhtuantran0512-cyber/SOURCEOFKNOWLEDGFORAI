---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/infinite-logo-scroller/"
title: "Infinite Logo Scroller"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "A seamless, endlessly looping marquee of partner or client logos — the 'trusted by' strip on almost every SaaS landing page."
has_js: "false"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Infinite Logo Scroller
Source: https://codefronts.com/snippets/css-image-carousel/infinite-logo-scroller/

A seamless, endlessly looping marquee of partner or client logos — the 'trusted by' strip on almost every SaaS landing page. Pure CSS keyframes translate a duplicated track, edges fade under a mask, and the animation pauses on hover.
## HTML
```html
<section class="car-03" aria-label="Trusted by leading teams">
  <p class="car-03__eyebrow">Trusted by 4,000+ teams</p>
  <div class="car-03__viewport">
    <ul class="car-03__track">
      <li class="car-03__item">NORTHWIND</li>
      <li class="car-03__item">Lumen&amp;Co</li>
      <li class="car-03__item">ARCADIA</li>
      <li class="car-03__item">Föhn</li>
      <li class="car-03__item">Kestrel</li>
      <li class="car-03__item">MONOLITH</li>
      <li class="car-03__item" aria-hidden="true">NORTHWIND</li>
      <li class="car-03__item" aria-hidden="true">Lumen&amp;Co</li>
      <li class="car-03__item" aria-hidden="true">ARCADIA</li>
      <li class="car-03__item" aria-hidden="true">Föhn</li>
      <li class="car-03__item" aria-hidden="true">Kestrel</li>
      <li class="car-03__item" aria-hidden="true">MONOLITH</li>
    </ul>
  </div>
</section>
```
## CSS
```css
.car-03,
.car-03 *,
.car-03 *::before,
.car-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-03 ::selection {
  background: #111827;
  color: #fff;
}

.car-03 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 0;
  background: #f6f7f9;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 22px;
}

.car-03__eyebrow {
  font-size: 12px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #9aa2b1;
}

.car-03__viewport {
  width: min(720px,100%);
  overflow: hidden;
  -webkit-mask: linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);
  mask: linear-gradient(90deg,transparent,#000 12%,#000 88%,transparent);
}

.car-03__track {
  list-style: none;
  display: flex;
  align-items: center;
  gap: 64px;
  width: max-content;
  animation: car-03-scroll 24s linear infinite;
}

.car-03__viewport:hover .car-03__track,
.car-03__viewport:focus-within .car-03__track {
  animation-play-state: paused;
}

.car-03__item {
  flex: none;
  font-size: 22px;
  font-weight: 800;
  letter-spacing: .02em;
  color: #4b5361;
  white-space: nowrap;
  font-family: Georgia,'Times New Roman',serif;
  opacity: .75;
}

@keyframes car-03-scroll {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(-50%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-03__track {
    animation: none;
    flex-wrap: wrap;
    justify-content: center;
    gap: 32px 48px;
    width: auto;
  }
}
```

## JavaScript
```js
/* No JavaScript — a duplicated track translated -50% loops seamlessly; hover/focus pauses it. */
```
