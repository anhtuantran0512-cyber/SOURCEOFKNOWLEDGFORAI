---
source: "codefronts"
url: "https://codefronts.com/components/css-stacked-cards/photos-pinch/"
title: "Photos Pinch"
section: "components"
category: "css-stacked-cards"
category_name: "CSS Stacked Cards"
description: "A scattered cluster of photos that, on hover of any single image, gathers inward toward a shared centre line while that photo brightens and lifts — a 'pinch…"
has_js: "false"
---

Here's a working CSS Stacked Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Photos Pinch
Source: https://codefronts.com/components/css-stacked-cards/photos-pinch/

A scattered cluster of photos that, on hover of any single image, gathers inward toward a shared centre line while that photo brightens and lifts — a 'pinch to focus' gesture rendered entirely in CSS transforms.
## HTML
```html
<section class="scd-19" aria-label="Pinch-to-focus photo cluster">
  <div class="scd-19__cluster">
    <a class="scd-19__ph" href="#" style="--x:-120px;--y:-40px;--r:-7deg"><img src="https://picsum.photos/seed/pinch-1/260/260" width="260" height="260" alt="Street market"></a>
    <a class="scd-19__ph" href="#" style="--x:110px;--y:-60px;--r:6deg"><img src="https://picsum.photos/seed/pinch-2/260/260" width="260" height="260" alt="Neon alley"></a>
    <a class="scd-19__ph" href="#" style="--x:-90px;--y:70px;--r:5deg"><img src="https://picsum.photos/seed/pinch-3/260/260" width="260" height="260" alt="Rooftop garden"></a>
    <a class="scd-19__ph" href="#" style="--x:120px;--y:60px;--r:-6deg"><img src="https://picsum.photos/seed/pinch-4/260/260" width="260" height="260" alt="Harbour lights"></a>
    <a class="scd-19__ph" href="#" style="--x:0px;--y:0px;--r:2deg"><img src="https://picsum.photos/seed/pinch-5/260/260" width="260" height="260" alt="Train window"></a>
  </div>
</section>
```
## CSS
```css
.scd-19,
.scd-19 *,
.scd-19 *::before,
.scd-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.scd-19 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: #0c0d13;
}

.scd-19__cluster {
  position: relative;
  width: min(360px,90vw);
  height: 340px;
}

.scd-19__ph {
  position: absolute;
  left: 50%;
  top: 50%;
  width: 150px;
  height: 150px;
  margin: -75px 0 0 -75px;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 16px 34px -18px rgba(0,0,0,.8);
  transform: translate(var(--x),var(--y)) rotate(var(--r));
  transition: transform .45s cubic-bezier(.3,.9,.3,1),filter .35s;
  outline: none;
}

.scd-19__ph img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.scd-19__cluster:has(.scd-19__ph:hover) .scd-19__ph,
.scd-19__cluster:has(.scd-19__ph:focus-visible) .scd-19__ph {
  transform: translate(calc(var(--x) * .3),calc(var(--y) * .3)) rotate(0);
  filter: brightness(.5);
}

.scd-19__ph:hover,
.scd-19__ph:focus-visible {
  transform: translate(0,0) rotate(0) scale(1.25)!important;
  filter: brightness(1.1)!important;
  z-index: 10;
}

.scd-19__ph:focus-visible {
  box-shadow: 0 0 0 3px oklch(0.7 0.15 250),0 24px 44px -18px rgba(0,0,0,.9);
}

@media (prefers-reduced-motion: reduce) {
  .scd-19__ph {
    transition: filter .25s;
  }

  .scd-19__cluster:has(.scd-19__ph:hover) .scd-19__ph {
    transform: translate(var(--x),var(--y)) rotate(var(--r));
  }

  .scd-19__ph:hover {
    transform: translate(var(--x),var(--y)) rotate(var(--r)) scale(1.1)!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — :has(:hover) on the cluster pulls every photo toward centre and dims the group, while the hovered photo overrides to brighten, scale and rise. */
```
