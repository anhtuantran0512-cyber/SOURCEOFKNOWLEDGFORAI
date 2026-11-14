---
source: "codefronts"
url: "https://codefronts.com/snippets/css-image-carousel/before-after-comparison-slider/"
title: "Before / After Comparison Slider"
section: "snippets"
category: "css-image-carousel"
category_name: "CSS Image Carousels"
description: "A draggable divider that wipes between a 'before' and 'after' version of the same photo — the retouch, renovation and design-comparison pattern."
has_js: "true"
---

Here's a working CSS Image Carousel from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Before / After Comparison Slider
Source: https://codefronts.com/snippets/css-image-carousel/before-after-comparison-slider/

A draggable divider that wipes between a 'before' and 'after' version of the same photo — the retouch, renovation and design-comparison pattern. A single accessible range input drives one CSS custom property; everything visual is CSS clip-path.
## HTML
```html
<section class="car-18" aria-label="Before and after comparison">
  <figure class="car-18__cmp" style="--pos:50">
    <img class="car-18__img car-18__img--after" src="https://picsum.photos/seed/edit-after/900/600" width="900" height="600" alt="After: colour-graded edit">
    <img class="car-18__img car-18__img--before" src="https://picsum.photos/seed/edit-before/900/600?grayscale" width="900" height="600" alt="Before: original photo">
    <span class="car-18__line" aria-hidden="true"><span class="car-18__knob">⇔</span></span>
    <span class="car-18__tag car-18__tag--b" aria-hidden="true">Before</span>
    <span class="car-18__tag car-18__tag--a" aria-hidden="true">After</span>
    <input class="car-18__range" type="range" min="0" max="100" value="50" aria-label="Reveal amount: drag to compare before and after">
  </figure>
</section>
```
## CSS
```css
.car-18,
.car-18 *,
.car-18 *::before,
.car-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-18 ::selection {
  background: #10b981;
  color: #fff;
}

.car-18 {
  --accent: #10b981;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #0d1412;
  display: flex;
  align-items: center;
  justify-content: center;
}

.car-18__cmp {
  position: relative;
  width: min(620px,100%);
  aspect-ratio: 3/2;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 26px 50px -32px rgba(0,0,0,.9);
  user-select: none;
}

.car-18__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.car-18__img--before {
  clip-path: inset(0 0 0 calc(var(--pos) * 1%));
}

.car-18__line {
  position: absolute;
  top: 0;
  bottom: 0;
  left: calc(var(--pos) * 1%);
  width: 2px;
  background: #fff;
  transform: translateX(-1px);
  box-shadow: 0 0 0 1px rgba(0,0,0,.25);
  pointer-events: none;
}

.car-18__knob {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: #fff;
  color: var(--accent);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  font-weight: 700;
  box-shadow: 0 4px 12px rgba(0,0,0,.4);
}

.car-18__tag {
  position: absolute;
  bottom: 14px;
  padding: 5px 11px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: #fff;
  background: rgba(10,14,13,.6);
  backdrop-filter: blur(4px);
}

.car-18__tag--b {
  left: 14px;
}

.car-18__tag--a {
  right: 14px;
}

.car-18__range {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  margin: 0;
  opacity: 0;
  cursor: ew-resize;
}

.car-18__range:focus-visible ~ .car-18__line {
  outline: none;
  box-shadow: 0 0 0 3px var(--accent);
}

.car-18__range:focus-visible ~ .car-18__line .car-18__knob {
  box-shadow: 0 0 0 3px var(--accent),0 4px 12px rgba(0,0,0,.4);
}

@media (prefers-reduced-motion: reduce) {
  .car-18__img--before,
    .car-18__line {
    transition: none;
  }
}
```

## JavaScript
```js
// One listener syncs the accessible range input's value into the --pos custom property.
// CSS clip-path + the divider position read --pos; keyboard (arrows/Home/End) works for free.
document.querySelectorAll('.car-18__cmp').forEach(function (cmp) {
  var range = cmp.querySelector('.car-18__range');
  var sync = function () { cmp.style.setProperty('--pos', range.value); };
  range.addEventListener('input', sync);
  sync();
});
```
