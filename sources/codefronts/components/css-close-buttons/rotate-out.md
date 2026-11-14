---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/rotate-out/"
title: "Rotate Out Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "The workhorse hover spin, done right: the × rotates a clean 180° on hover, GPU-composited, centred by CSS grid so it can never drift a subpixel mid-spin."
has_js: "false"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rotate Out Close Button
Source: https://codefronts.com/components/css-close-buttons/rotate-out/

The workhorse hover spin, done right: the × rotates a clean 180° on hover, GPU-composited, centred by CSS grid so it can never drift a subpixel mid-spin. This is the demo to learn the three rules every rotating icon needs — grid centring, transform-only motion, and will-change discipline.
## HTML
```html
<section class="ccb-13" aria-label="Rotating close button demo">
  <button class="ccb-13__close" type="button" aria-label="Close">
    <span class="ccb-13__x" aria-hidden="true"></span>
  </button>
</section>
```
## CSS
```css
.ccb-13,
.ccb-13 *,
.ccb-13 *::before,
.ccb-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-13 {
  --ink: oklch(0.35 0.03 265);
  --accent: oklch(0.55 0.18 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: linear-gradient(180deg,oklch(0.97 0.006 265),oklch(0.93 0.014 265));
}

.ccb-13 .ccb-13__close {
  display: grid;
  place-items: center;
  width: 60px;
  height: 60px;
  border: 2px solid color-mix(in oklab,var(--ink) 30%,transparent);
  border-radius: 50%;
  background: #fff;
  cursor: pointer;
  transition: border-color .25s ease,transform .2s ease;
  box-shadow: 0 12px 28px -16px oklch(0.4 0.06 265 / .5);
}

.ccb-13 .ccb-13__x {
  position: relative;
  width: 22px;
  height: 22px;
  transition: transform .45s cubic-bezier(.22,1,.36,1);
}

.ccb-13 .ccb-13__x::before,
.ccb-13 .ccb-13__x::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 22px;
  height: 2.5px;
  border-radius: 2px;
  background: var(--ink);
  transition: background .25s ease;
}

.ccb-13 .ccb-13__x::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-13 .ccb-13__x::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

@media (hover: hover) {
  .ccb-13 .ccb-13__x {
    will-change: transform;
  }

  .ccb-13 .ccb-13__close:hover .ccb-13__x {
    transform: rotate(180deg);
  }

  .ccb-13 .ccb-13__close:hover {
    border-color: var(--accent);
  }

  .ccb-13 .ccb-13__close:hover .ccb-13__x::before,
    .ccb-13 .ccb-13__close:hover .ccb-13__x::after {
    background: var(--accent);
  }
}

.ccb-13 .ccb-13__close:active {
  transform: scale(.92);
}

.ccb-13 .ccb-13__close:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .ccb-13 .ccb-13__x,
    .ccb-13 .ccb-13__close {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — grid centring kills subpixel wobble; transform-only rotation composites on the GPU; will-change is hover-gated. */
```
