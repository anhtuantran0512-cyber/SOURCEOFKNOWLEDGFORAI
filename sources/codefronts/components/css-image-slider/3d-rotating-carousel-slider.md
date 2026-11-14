---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/3d-rotating-carousel-slider/"
title: "3D Rotating Carousel Slider"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: "3D rotating CSS carousel slider — spatial image carousel built from real CSS 3D transforms with four faces arranged around a virtual prism that rotates on…"
has_js: "false"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Rotating Carousel Slider
Source: https://codefronts.com/components/css-image-slider/3d-rotating-carousel-slider/

3D rotating CSS carousel slider — spatial image carousel built from real CSS 3D transforms with four faces arranged around a virtual prism that rotates on its Y axis as you navigate. Perspective, rotateY, and translateZ do all the work; no JavaScript, no Three.js, no WebGL. Great for portfolio hero showcases and product-tour landing pages.
## HTML
```html
<div class="cis-13">
  <input type="radio" name="cis-13" id="cis-13-1" checked>
  <input type="radio" name="cis-13" id="cis-13-2">
  <input type="radio" name="cis-13" id="cis-13-3">
  <input type="radio" name="cis-13" id="cis-13-4">
  <div class="cis-13__scene">
    <div class="cis-13__cube">
      <figure class="cis-13__face f1"><img src="https://picsum.photos/seed/cis13a/700/700" alt="Face 1"></figure>
      <figure class="cis-13__face f2"><img src="https://picsum.photos/seed/cis13b/700/700" alt="Face 2"></figure>
      <figure class="cis-13__face f3"><img src="https://picsum.photos/seed/cis13c/700/700" alt="Face 3"></figure>
      <figure class="cis-13__face f4"><img src="https://picsum.photos/seed/cis13d/700/700" alt="Face 4"></figure>
    </div>
  </div>
  <div class="cis-13__nav">
    <label for="cis-13-1" aria-label="Face 1"></label>
    <label for="cis-13-2" aria-label="Face 2"></label>
    <label for="cis-13-3" aria-label="Face 3"></label>
    <label for="cis-13-4" aria-label="Face 4"></label>
  </div>
</div>
```
## CSS
```css
.cis-13,
.cis-13 *,
.cis-13 *::before,
.cis-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-13 ::selection {
  background: oklch(0.82 0.15 300);
  color: #12041a;
}

.cis-13 {
  --tz: 150px;
  --dur: .9s;
  --accent: oklch(0.78 0.15 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #f2ecf6;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 40px;
  padding: 40px 20px;
  background: radial-gradient(120% 120% at 50% 40%,#160a20,#08060d);
}

.cis-13 input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cis-13__scene {
  perspective: 1100px;
  width: 300px;
  height: 300px;
}

.cis-13__cube {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform var(--dur) cubic-bezier(.6,0,.2,1);
  transform: rotateY(0);
}

.cis-13__face {
  position: absolute;
  inset: 0;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid rgba(255,255,255,.14);
  box-shadow: 0 0 0 1px rgba(255,255,255,.04);
  backface-visibility: hidden;
  transition: filter var(--dur);
}

.cis-13__face img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.f1 {
  transform: rotateY(0deg) translateZ(var(--tz));
}

.f2 {
  transform: rotateY(90deg) translateZ(var(--tz));
}

.f3 {
  transform: rotateY(180deg) translateZ(var(--tz));
}

.f4 {
  transform: rotateY(270deg) translateZ(var(--tz));
}

#cis-13-1:checked ~ .cis-13__scene .cis-13__cube {
  transform: rotateY(0deg);
}

#cis-13-2:checked ~ .cis-13__scene .cis-13__cube {
  transform: rotateY(-90deg);
}

#cis-13-3:checked ~ .cis-13__scene .cis-13__cube {
  transform: rotateY(-180deg);
}

#cis-13-4:checked ~ .cis-13__scene .cis-13__cube {
  transform: rotateY(-270deg);
}

.cis-13__nav {
  display: flex;
  gap: 12px;
}

.cis-13__nav label {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  cursor: pointer;
  background: rgba(255,255,255,.25);
  transition: background .3s,width .3s;
}

.cis-13__nav label:hover {
  background: rgba(255,255,255,.55);
}

#cis-13-1:checked ~ .cis-13__nav label[for="cis-13-1"],
#cis-13-2:checked ~ .cis-13__nav label[for="cis-13-2"],
#cis-13-3:checked ~ .cis-13__nav label[for="cis-13-3"],
#cis-13-4:checked ~ .cis-13__nav label[for="cis-13-4"] {
  background: var(--accent);
  width: 30px;
  border-radius: 6px;
}

@media (prefers-reduced-motion: reduce) {
  .cis-13__cube {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — radios drive rotateY on a preserve-3d prism. */
```
