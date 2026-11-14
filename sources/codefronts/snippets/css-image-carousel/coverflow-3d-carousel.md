---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/coverflow-3d-carousel/"
title: "Coverflow 3D Carousel"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "The iconic Cover Flow effect: the centre image faces you full-size while the flanking images tilt back in 3D perspective."
has_js: "false"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Coverflow 3D Carousel
Source: https://codefronts.com/snippets/css-image-carousel/coverflow-3d-carousel/

The iconic Cover Flow effect: the centre image faces you full-size while the flanking images tilt back in 3D perspective. Entirely pure CSS — radio inputs and 3D transforms, no JavaScript — with clickable side covers and keyboard support.
## HTML
```html
<section class="car-13" aria-label="Album coverflow">
  <div class="car-13__stage">
    <input type="radio" name="car-13" id="car-13-1" class="car-13__radio">
    <input type="radio" name="car-13" id="car-13-2" class="car-13__radio">
    <input type="radio" name="car-13" id="car-13-3" class="car-13__radio" checked>
    <input type="radio" name="car-13" id="car-13-4" class="car-13__radio">
    <input type="radio" name="car-13" id="car-13-5" class="car-13__radio">
    <div class="car-13__deck">
      <figure class="car-13__cover"><img src="https://picsum.photos/seed/cover-1/500/500" width="500" height="500" alt="Album: Nocturne"><label class="car-13__hit" for="car-13-1" aria-label="Show cover 1"></label></figure>
      <figure class="car-13__cover"><img src="https://picsum.photos/seed/cover-2/500/500" width="500" height="500" alt="Album: Parallel"><label class="car-13__hit" for="car-13-2" aria-label="Show cover 2"></label></figure>
      <figure class="car-13__cover"><img src="https://picsum.photos/seed/cover-3/500/500" width="500" height="500" alt="Album: Solstice"><label class="car-13__hit" for="car-13-3" aria-label="Show cover 3"></label></figure>
      <figure class="car-13__cover"><img src="https://picsum.photos/seed/cover-4/500/500" width="500" height="500" alt="Album: Undertow"><label class="car-13__hit" for="car-13-4" aria-label="Show cover 4"></label></figure>
      <figure class="car-13__cover"><img src="https://picsum.photos/seed/cover-5/500/500" width="500" height="500" alt="Album: Vantage"><label class="car-13__hit" for="car-13-5" aria-label="Show cover 5"></label></figure>
    </div>
  </div>
</section>
```
## CSS
```css
.car-13,
.car-13 *,
.car-13 *::before,
.car-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-13 ::selection {
  background: #7c5cff;
  color: #fff;
}

.car-13 {
  --accent: #7c5cff;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #111018;
  display: flex;
  align-items: center;
  justify-content: center;
}

.car-13__stage {
  width: min(560px,100%);
  perspective: 1200px;
}

.car-13__radio {
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

.car-13__deck {
  position: relative;
  height: 300px;
  transform-style: preserve-3d;
}

.car-13__cover {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 220px;
  height: 220px;
  margin: -110px 0 0 -110px;
  border-radius: 10px;
  overflow: hidden;
  transform-style: preserve-3d;
  box-shadow: 0 24px 40px -20px rgba(0,0,0,.8);
  transition: transform .5s cubic-bezier(.2,.8,.2,1),opacity .5s;
  opacity: .55;
}

.car-13__cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  pointer-events: none;
}

.car-13__hit {
  position: absolute;
  inset: 0;
  cursor: pointer;
}
/* default rest = deck focused on #3 handled by checked below */

.car-13__radio:nth-of-type(1):checked ~ .car-13__deck .car-13__cover:nth-child(1),
.car-13__radio:nth-of-type(2):checked ~ .car-13__deck .car-13__cover:nth-child(2),
.car-13__radio:nth-of-type(3):checked ~ .car-13__deck .car-13__cover:nth-child(3),
.car-13__radio:nth-of-type(4):checked ~ .car-13__deck .car-13__cover:nth-child(4),
.car-13__radio:nth-of-type(5):checked ~ .car-13__deck .car-13__cover:nth-child(5) {
  transform: translateX(0) rotateY(0) scale(1);
  opacity: 1;
  z-index: 5;
}
/* checked #1 */

.car-13__radio:nth-of-type(1):checked ~ .car-13__deck .car-13__cover:nth-child(2) {
  transform: translateX(120px) rotateY(-42deg) scale(.82);
  opacity: .75;
  z-index: 4;
}

.car-13__radio:nth-of-type(1):checked ~ .car-13__deck .car-13__cover:nth-child(3) {
  transform: translateX(210px) rotateY(-48deg) scale(.66);
  z-index: 3;
}

.car-13__radio:nth-of-type(1):checked ~ .car-13__deck .car-13__cover:nth-child(4) {
  transform: translateX(285px) rotateY(-52deg) scale(.52);
  opacity: .35;
  z-index: 2;
}

.car-13__radio:nth-of-type(1):checked ~ .car-13__deck .car-13__cover:nth-child(5) {
  transform: translateX(345px) rotateY(-54deg) scale(.42);
  opacity: .2;
  z-index: 1;
}
/* checked #2 */

.car-13__radio:nth-of-type(2):checked ~ .car-13__deck .car-13__cover:nth-child(1) {
  transform: translateX(-120px) rotateY(42deg) scale(.82);
  opacity: .75;
  z-index: 4;
}

.car-13__radio:nth-of-type(2):checked ~ .car-13__deck .car-13__cover:nth-child(3) {
  transform: translateX(120px) rotateY(-42deg) scale(.82);
  opacity: .75;
  z-index: 4;
}

.car-13__radio:nth-of-type(2):checked ~ .car-13__deck .car-13__cover:nth-child(4) {
  transform: translateX(210px) rotateY(-48deg) scale(.66);
  z-index: 3;
}

.car-13__radio:nth-of-type(2):checked ~ .car-13__deck .car-13__cover:nth-child(5) {
  transform: translateX(285px) rotateY(-52deg) scale(.52);
  opacity: .35;
  z-index: 2;
}
/* checked #3 */

.car-13__radio:nth-of-type(3):checked ~ .car-13__deck .car-13__cover:nth-child(1) {
  transform: translateX(-210px) rotateY(48deg) scale(.66);
  z-index: 3;
}

.car-13__radio:nth-of-type(3):checked ~ .car-13__deck .car-13__cover:nth-child(2) {
  transform: translateX(-120px) rotateY(42deg) scale(.82);
  opacity: .75;
  z-index: 4;
}

.car-13__radio:nth-of-type(3):checked ~ .car-13__deck .car-13__cover:nth-child(4) {
  transform: translateX(120px) rotateY(-42deg) scale(.82);
  opacity: .75;
  z-index: 4;
}

.car-13__radio:nth-of-type(3):checked ~ .car-13__deck .car-13__cover:nth-child(5) {
  transform: translateX(210px) rotateY(-48deg) scale(.66);
  z-index: 3;
}
/* checked #4 */

.car-13__radio:nth-of-type(4):checked ~ .car-13__deck .car-13__cover:nth-child(1) {
  transform: translateX(-285px) rotateY(52deg) scale(.52);
  opacity: .35;
  z-index: 2;
}

.car-13__radio:nth-of-type(4):checked ~ .car-13__deck .car-13__cover:nth-child(2) {
  transform: translateX(-210px) rotateY(48deg) scale(.66);
  z-index: 3;
}

.car-13__radio:nth-of-type(4):checked ~ .car-13__deck .car-13__cover:nth-child(3) {
  transform: translateX(-120px) rotateY(42deg) scale(.82);
  opacity: .75;
  z-index: 4;
}

.car-13__radio:nth-of-type(4):checked ~ .car-13__deck .car-13__cover:nth-child(5) {
  transform: translateX(120px) rotateY(-42deg) scale(.82);
  opacity: .75;
  z-index: 4;
}
/* checked #5 */

.car-13__radio:nth-of-type(5):checked ~ .car-13__deck .car-13__cover:nth-child(1) {
  transform: translateX(-345px) rotateY(54deg) scale(.42);
  opacity: .2;
  z-index: 1;
}

.car-13__radio:nth-of-type(5):checked ~ .car-13__deck .car-13__cover:nth-child(2) {
  transform: translateX(-285px) rotateY(52deg) scale(.52);
  opacity: .35;
  z-index: 2;
}

.car-13__radio:nth-of-type(5):checked ~ .car-13__deck .car-13__cover:nth-child(3) {
  transform: translateX(-210px) rotateY(48deg) scale(.66);
  z-index: 3;
}

.car-13__radio:nth-of-type(5):checked ~ .car-13__deck .car-13__cover:nth-child(4) {
  transform: translateX(-120px) rotateY(42deg) scale(.82);
  opacity: .75;
  z-index: 4;
}

.car-13__radio:focus-visible ~ .car-13__deck .car-13__cover:nth-child(1) {
  outline: 0;
}

.car-13__radio:nth-of-type(1):focus-visible ~ .car-13__deck .car-13__cover:nth-child(1),
.car-13__radio:nth-of-type(2):focus-visible ~ .car-13__deck .car-13__cover:nth-child(2),
.car-13__radio:nth-of-type(3):focus-visible ~ .car-13__deck .car-13__cover:nth-child(3),
.car-13__radio:nth-of-type(4):focus-visible ~ .car-13__deck .car-13__cover:nth-child(4),
.car-13__radio:nth-of-type(5):focus-visible ~ .car-13__deck .car-13__cover:nth-child(5) {
  outline: 3px solid var(--accent);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .car-13__cover {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a radio group drives a per-slide 3D transform map (translateX + rotateY + scale) under CSS perspective. */
```
