---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/parallax-text-over-image-slider/"
title: "Parallax Text-Over-Image Slider"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "A presentation carousel where, on each transition, the background photo and the foreground text travel at different speeds and distances — creating depth and…"
has_js: "false"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Parallax Text-Over-Image Slider
Source: https://codefronts.com/snippets/css-image-carousel/parallax-text-over-image-slider/

A presentation carousel where, on each transition, the background photo and the foreground text travel at different speeds and distances — creating depth and drama. Radio-controlled, fully pure CSS, with a headline that leads and an image that trails.
## HTML
```html
<section class="car-22" aria-label="Parallax story slider">
  <div class="car-22__stage">
    <input type="radio" name="car-22" id="car-22-1" class="car-22__radio" checked>
    <input type="radio" name="car-22" id="car-22-2" class="car-22__radio">
    <input type="radio" name="car-22" id="car-22-3" class="car-22__radio">
    <div class="car-22__slides">
      <article class="car-22__slide"><img class="car-22__bg" src="https://picsum.photos/seed/plx-1/1200/700" width="1200" height="700" alt="Canyon at sunrise"><div class="car-22__body"><p class="car-22__kick">Chapter 01</p><h3 class="car-22__title">Into the canyon</h3><p class="car-22__lead">Where light carves the rock a little differently every hour.</p></div></article>
      <article class="car-22__slide"><img class="car-22__bg" src="https://picsum.photos/seed/plx-2/1200/700" width="1200" height="700" alt="Open ocean"><div class="car-22__body"><p class="car-22__kick">Chapter 02</p><h3 class="car-22__title">Beyond the shore</h3><p class="car-22__lead">Nothing but horizon, and the sound of the hull.</p></div></article>
      <article class="car-22__slide"><img class="car-22__bg" src="https://picsum.photos/seed/plx-3/1200/700" width="1200" height="700" alt="Alpine ridge"><div class="car-22__body"><p class="car-22__kick">Chapter 03</p><h3 class="car-22__title">Above the clouds</h3><p class="car-22__lead">The last ridge before the summit, and the quiet up there.</p></div></article>
    </div>
    <div class="car-22__nav">
      <label class="car-22__pip" for="car-22-1" aria-label="Chapter 1"></label>
      <label class="car-22__pip" for="car-22-2" aria-label="Chapter 2"></label>
      <label class="car-22__pip" for="car-22-3" aria-label="Chapter 3"></label>
    </div>
  </div>
</section>
```
## CSS
```css
.car-22,
.car-22 *,
.car-22 *::before,
.car-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-22 ::selection {
  background: #fff;
  color: #111;
}

.car-22 {
  --accent: #f5c542;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #0c0d10;
  display: flex;
  align-items: center;
  justify-content: center;
}

.car-22__stage {
  position: relative;
  width: min(760px,100%);
}

.car-22__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
}

.car-22__slides {
  position: relative;
  aspect-ratio: 12/7;
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 30px 60px -34px rgba(0,0,0,.9);
}

.car-22__slide {
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity .7s ease;
  pointer-events: none;
}

.car-22__slide::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg,rgba(6,7,10,.78),transparent 65%);
}

.car-22__bg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  transform: scale(1.12) translateX(6%);
  transition: transform 1s cubic-bezier(.2,.8,.2,1);
}

.car-22__body {
  position: absolute;
  left: 0;
  bottom: 0;
  z-index: 2;
  padding: clamp(22px,5vw,52px);
  max-width: 70%;
  color: #fff;
  transform: translateX(-14%);
  opacity: 0;
  transition: transform .8s cubic-bezier(.2,.8,.2,1) .12s,opacity .8s .12s;
}

.car-22__kick {
  font-size: 12px;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 10px;
}

.car-22__title {
  font-size: clamp(26px,5vw,44px);
  font-weight: 800;
  line-height: 1.05;
  letter-spacing: -.01em;
  text-shadow: 0 2px 20px rgba(0,0,0,.5);
}

.car-22__lead {
  font-size: 15px;
  line-height: 1.55;
  color: #dfe2e8;
  margin-top: 12px;
  max-width: 36ch;
}

.car-22__radio:nth-of-type(1):checked ~ .car-22__slides .car-22__slide:nth-child(1),
.car-22__radio:nth-of-type(2):checked ~ .car-22__slides .car-22__slide:nth-child(2),
.car-22__radio:nth-of-type(3):checked ~ .car-22__slides .car-22__slide:nth-child(3) {
  opacity: 1;
  pointer-events: auto;
}

.car-22__radio:nth-of-type(1):checked ~ .car-22__slides .car-22__slide:nth-child(1) .car-22__bg,
.car-22__radio:nth-of-type(2):checked ~ .car-22__slides .car-22__slide:nth-child(2) .car-22__bg,
.car-22__radio:nth-of-type(3):checked ~ .car-22__slides .car-22__slide:nth-child(3) .car-22__bg {
  transform: scale(1.06) translateX(0);
}

.car-22__radio:nth-of-type(1):checked ~ .car-22__slides .car-22__slide:nth-child(1) .car-22__body,
.car-22__radio:nth-of-type(2):checked ~ .car-22__slides .car-22__slide:nth-child(2) .car-22__body,
.car-22__radio:nth-of-type(3):checked ~ .car-22__slides .car-22__slide:nth-child(3) .car-22__body {
  transform: translateX(0);
  opacity: 1;
}

.car-22__nav {
  position: absolute;
  right: clamp(18px,4vw,40px);
  bottom: clamp(18px,4vw,40px);
  z-index: 3;
  display: flex;
  gap: 9px;
}

.car-22__pip {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(255,255,255,.35);
  cursor: pointer;
  transition: transform .2s,background .2s;
}

.car-22__pip:hover {
  background: rgba(255,255,255,.6);
}

.car-22__radio:nth-of-type(1):checked ~ .car-22__nav .car-22__pip:nth-child(1),
.car-22__radio:nth-of-type(2):checked ~ .car-22__nav .car-22__pip:nth-child(2),
.car-22__radio:nth-of-type(3):checked ~ .car-22__nav .car-22__pip:nth-child(3) {
  background: var(--accent);
  transform: scale(1.3);
}

.car-22__radio:nth-of-type(1):focus-visible ~ .car-22__nav .car-22__pip:nth-child(1),
.car-22__radio:nth-of-type(2):focus-visible ~ .car-22__nav .car-22__pip:nth-child(2),
.car-22__radio:nth-of-type(3):focus-visible ~ .car-22__nav .car-22__pip:nth-child(3) {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .car-22__slide,
    .car-22__bg,
    .car-22__body {
    transition: opacity .3s;
  }

  .car-22__bg {
    transform: none!important;
  }

  .car-22__body {
    transform: none!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — on :checked, the background image and the text layer ease in from different offsets/timings, producing the parallax depth. */
```
