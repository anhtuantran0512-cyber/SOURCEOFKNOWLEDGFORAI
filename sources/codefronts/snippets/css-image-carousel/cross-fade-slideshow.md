---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/cross-fade-slideshow/"
title: "Cross-Fade Slideshow"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "A classic manual slideshow that dissolves between photos with pure opacity — no sliding, no reflow."
has_js: "false"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cross-Fade Slideshow
Source: https://codefronts.com/snippets/css-image-carousel/cross-fade-slideshow/

A classic manual slideshow that dissolves between photos with pure opacity — no sliding, no reflow. Radio-driven dots let visitors step through at their own pace, the calm alternative to an auto-advancing hero.
## HTML
```html
<section class="car-14" aria-label="Photo slideshow">
  <div class="car-14__box">
    <input type="radio" name="car-14" id="car-14-1" class="car-14__radio" checked>
    <input type="radio" name="car-14" id="car-14-2" class="car-14__radio">
    <input type="radio" name="car-14" id="car-14-3" class="car-14__radio">
    <input type="radio" name="car-14" id="car-14-4" class="car-14__radio">
    <div class="car-14__frame">
      <img class="car-14__img" src="https://picsum.photos/seed/fade-1/900/600" width="900" height="600" alt="Foggy harbour at dawn">
      <img class="car-14__img" src="https://picsum.photos/seed/fade-2/900/600" width="900" height="600" alt="Neon-lit alley at night">
      <img class="car-14__img" src="https://picsum.photos/seed/fade-3/900/600" width="900" height="600" alt="Snowy mountain village">
      <img class="car-14__img" src="https://picsum.photos/seed/fade-4/900/600" width="900" height="600" alt="Field of lavender">
    </div>
    <div class="car-14__dots">
      <label class="car-14__dot" for="car-14-1" aria-label="Slide 1"></label>
      <label class="car-14__dot" for="car-14-2" aria-label="Slide 2"></label>
      <label class="car-14__dot" for="car-14-3" aria-label="Slide 3"></label>
      <label class="car-14__dot" for="car-14-4" aria-label="Slide 4"></label>
    </div>
  </div>
</section>
```
## CSS
```css
.car-14,
.car-14 *,
.car-14 *::before,
.car-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-14 ::selection {
  background: #0ea5e9;
  color: #fff;
}

.car-14 {
  --accent: #0ea5e9;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #0f1720;
  display: flex;
  align-items: center;
  justify-content: center;
}

.car-14__box {
  width: min(620px,100%);
}

.car-14__radio {
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

.car-14__frame {
  position: relative;
  aspect-ratio: 3/2;
  border-radius: 16px;
  overflow: hidden;
  background: #1b2733;
  box-shadow: 0 26px 50px -32px rgba(0,0,0,.9);
}

.car-14__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0;
  transition: opacity .8s ease;
}

.car-14__radio:nth-of-type(1):checked ~ .car-14__frame .car-14__img:nth-child(1),
.car-14__radio:nth-of-type(2):checked ~ .car-14__frame .car-14__img:nth-child(2),
.car-14__radio:nth-of-type(3):checked ~ .car-14__frame .car-14__img:nth-child(3),
.car-14__radio:nth-of-type(4):checked ~ .car-14__frame .car-14__img:nth-child(4) {
  opacity: 1;
}

.car-14__dots {
  display: flex;
  gap: 10px;
  justify-content: center;
  margin-top: 16px;
}

.car-14__dot {
  width: 34px;
  height: 5px;
  border-radius: 999px;
  background: #31404f;
  cursor: pointer;
  transition: background .25s;
}

.car-14__dot:hover {
  background: #4a5a6a;
}

.car-14__radio:nth-of-type(1):checked ~ .car-14__dots .car-14__dot:nth-child(1),
.car-14__radio:nth-of-type(2):checked ~ .car-14__dots .car-14__dot:nth-child(2),
.car-14__radio:nth-of-type(3):checked ~ .car-14__dots .car-14__dot:nth-child(3),
.car-14__radio:nth-of-type(4):checked ~ .car-14__dots .car-14__dot:nth-child(4) {
  background: var(--accent);
}

.car-14__radio:nth-of-type(1):focus-visible ~ .car-14__dots .car-14__dot:nth-child(1),
.car-14__radio:nth-of-type(2):focus-visible ~ .car-14__dots .car-14__dot:nth-child(2),
.car-14__radio:nth-of-type(3):focus-visible ~ .car-14__dots .car-14__dot:nth-child(3),
.car-14__radio:nth-of-type(4):focus-visible ~ .car-14__dots .car-14__dot:nth-child(4) {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .car-14__img {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a radio group cross-fades stacked images via opacity and paints the active dot. */
```
