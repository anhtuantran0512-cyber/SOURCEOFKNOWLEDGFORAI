---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/aurora-map/"
title: "Aurora Map"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "A stylized ops-center map interface: latitude/longitude grid lines from repeating gradients, aurora light fields blended with background-blend-mode, and…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Aurora Map
Source: https://codefronts.com/layouts/css-grid-layouts/aurora-map/

A stylized ops-center map interface: latitude/longitude grid lines from repeating gradients, aurora light fields blended with background-blend-mode, and location markers PLACED ON GRID CELLS — so 'pins' are grid coordinates you can read in the stylesheet, not magic-number percentages.
## HTML
```html
<section class="cgl-28" aria-label="Aurora map interface demo">
  <div class="cgl-28__map">
    <button type="button" class="cgl-28__pin" style="grid-area:3/9"><i></i><span>Reykjavík relay · 42ms</span></button>
    <button type="button" class="cgl-28__pin" style="grid-area:5/3"><i></i><span>Denver edge · 18ms</span></button>
    <button type="button" class="cgl-28__pin cgl-28__pin--alert" style="grid-area:6/11"><i></i><span>Sydney edge · degraded</span></button>
    <button type="button" class="cgl-28__pin" style="grid-area:4/6"><i></i><span>Azores buoy · 61ms</span></button>
    <p class="cgl-28__legend">markers are grid coordinates — grid-area: row / column</p>
  </div>
</section>
```
## CSS
```css
.cgl-28,
.cgl-28 *,
.cgl-28 *::before,
.cgl-28 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-28 {
  width: 100%;
  min-height: 100vh;
  --aur-a: oklch(0.6 0.14 190);
  --aur-b: oklch(0.5 0.16 300);
  --line: oklch(0.6 0.1 200);
  font-family: ui-monospace,'Cascadia Code',Menlo,monospace;
  background: oklch(0.13 0.02 240);
  padding: 1.4rem;
}

.cgl-28 .cgl-28__map {
  position: relative;
  display: grid;
  grid-template-columns: repeat(12,1fr);
  grid-template-rows: repeat(8,1fr);
  aspect-ratio: 12/7;
  border-radius: 16px;
  border: 1px solid oklch(0.6 0.1 200/.25);
  overflow: hidden;
  background: repeating-linear-gradient(90deg,oklch(0.6 0.1 200/.1) 0 1px,transparent 1px calc(100%/12)),repeating-linear-gradient(0deg,oklch(0.6 0.1 200/.1) 0 1px,transparent 1px calc(100%/8)),radial-gradient(70% 90% at 20% 15%,color-mix(in oklab,var(--aur-a) 45%,transparent),transparent 60%),radial-gradient(60% 80% at 85% 75%,color-mix(in oklab,var(--aur-b) 40%,transparent),transparent 60%),oklch(0.16 0.03 240);
  background-blend-mode: normal,normal,screen,screen,normal;
}

.cgl-28 .cgl-28__pin {
  position: relative;
  place-self: center;
  background: none;
  border: none;
  cursor: pointer;
  display: grid;
  place-items: center;
  min-inline-size: 44px;
  min-block-size: 44px;
}

.cgl-28 .cgl-28__pin i {
  inline-size: 12px;
  aspect-ratio: 1;
  border-radius: 50%;
  background: var(--aur-a);
  box-shadow: 0 0 12px var(--aur-a);
  position: relative;
}

.cgl-28 .cgl-28__pin i::after {
  content: "";
  position: absolute;
  inset: -4px;
  border-radius: 50%;
  border: 1.5px solid var(--aur-a);
  animation: cgl-28-ping 2.2s ease-out infinite;
}

@keyframes cgl-28-ping {
  75%,
    100% {
    scale: 2.4;
    opacity: 0;
  }
}

.cgl-28 .cgl-28__pin--alert i {
  background: oklch(0.72 0.19 30);
  box-shadow: 0 0 12px oklch(0.72 0.19 30);
}

.cgl-28 .cgl-28__pin--alert i::after {
  border-color: oklch(0.72 0.19 30);
}

.cgl-28 .cgl-28__pin span {
  position: absolute;
  inset-block-end: 100%;
  font-size: .62rem;
  white-space: nowrap;
  color: oklch(0.95 0.02 200);
  background: oklch(0.2 0.03 240/.9);
  border: 1px solid oklch(0.6 0.1 200/.35);
  border-radius: 6px;
  padding: .3rem .55rem;
  opacity: 0;
  translate: 0 4px;
  transition: opacity .25s ease,translate .25s ease;
  pointer-events: none;
}

.cgl-28 .cgl-28__pin:hover span,
.cgl-28 .cgl-28__pin:focus-visible span {
  opacity: 1;
  translate: 0 0;
}

.cgl-28 .cgl-28__pin:focus-visible {
  outline: 2px solid var(--aur-a);
  outline-offset: 2px;
  border-radius: 8px;
}

.cgl-28 .cgl-28__legend {
  position: absolute;
  inset-block-end: .6rem;
  inset-inline-start: .8rem;
  font-size: .6rem;
  letter-spacing: .06em;
  color: oklch(0.65 0.05 200);
}

@media (prefers-reduced-motion: reduce) {
  .cgl-28 .cgl-28__pin i::after {
    animation: none;
    opacity: 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — gradients draw the graticule, blend-mode paints the aurora, and pins are literal grid coordinates. */
```
