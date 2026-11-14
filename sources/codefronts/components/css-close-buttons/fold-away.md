---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/fold-away/"
title: "Fold Away Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "A 3D vanishing act: hovering splits the × horizontally into two half-tiles that hinge backward in perspective — the top half folds up and away, the bottom…"
has_js: "false"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fold Away Close Button
Source: https://codefronts.com/components/css-close-buttons/fold-away/

A 3D vanishing act: hovering splits the × horizontally into two half-tiles that hinge backward in perspective — the top half folds up and away, the bottom folds down — like a greeting card closing into the screen. Each half carries a clipped copy of the same glyph, so the seam is invisible until the fold begins.
## HTML
```html
<section class="ccb-23" aria-label="Fold away close button demo">
  <button class="ccb-23__close" type="button" aria-label="Close">
    <span class="ccb-23__half ccb-23__half--top" aria-hidden="true"><i class="ccb-23__glyph"></i></span>
    <span class="ccb-23__half ccb-23__half--bot" aria-hidden="true"><i class="ccb-23__glyph"></i></span>
  </button>
</section>
```
## CSS
```css
.ccb-23,
.ccb-23 *,
.ccb-23 *::before,
.ccb-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-23 {
  --fold: 78deg;
  --ink: oklch(0.3 0.03 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,oklch(0.95 0.012 240),oklch(0.9 0.02 245));
}

.ccb-23 .ccb-23__close {
  position: relative;
  width: 76px;
  height: 76px;
  border: 1.5px solid oklch(0.85 0.02 245);
  border-radius: 18px;
  background: #fff;
  cursor: pointer;
  perspective: 500px;
  box-shadow: 0 18px 40px -24px oklch(0.4 0.06 245 / .6);
  transition: box-shadow .3s ease;
}

.ccb-23 .ccb-23__half {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  transition: transform .45s cubic-bezier(.4,0,.2,1),filter .45s ease;
}

.ccb-23 .ccb-23__half--top {
  clip-path: inset(0 0 50% 0);
  transform-origin: 50% 50%;
}

.ccb-23 .ccb-23__half--bot {
  clip-path: inset(50% 0 0 0);
  transform-origin: 50% 50%;
  transition-delay: .04s;
}

.ccb-23 .ccb-23__glyph {
  position: relative;
  width: 26px;
  height: 26px;
  display: block;
}

.ccb-23 .ccb-23__glyph::before,
.ccb-23 .ccb-23__glyph::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 26px;
  height: 3px;
  border-radius: 2px;
  background: var(--ink);
}

.ccb-23 .ccb-23__glyph::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-23 .ccb-23__glyph::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-23 .ccb-23__close:hover .ccb-23__half--top {
  transform: rotateX(var(--fold));
  filter: brightness(.72);
}

.ccb-23 .ccb-23__close:hover .ccb-23__half--bot {
  transform: rotateX(calc(var(--fold) * -1));
  filter: brightness(.82);
}

.ccb-23 .ccb-23__close:hover {
  box-shadow: 0 10px 22px -16px oklch(0.4 0.06 245 / .5);
}

.ccb-23 .ccb-23__close:active {
  transform: scale(.95);
}

.ccb-23 .ccb-23__close:focus-visible {
  outline: 3px solid oklch(0.55 0.15 250);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .ccb-23 .ccb-23__half {
    transition: none;
  }

  .ccb-23 .ccb-23__close:hover .ccb-23__half--top,
    .ccb-23 .ccb-23__close:hover .ccb-23__half--bot {
    transform: none;
    filter: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — two clip-path halves of one glyph hinge on rotateX from seam-edge origins; brightness fades sell the depth. */
```
