---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/zoom-on-hover-expanding-accordion-gallery/"
title: "Zoom-on-Hover Expanding Accordion Gallery"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: "Zoom-on-hover expanding accordion image gallery in pure CSS — a horizontal row where every panel shares width equally until you hover one, which smoothly…"
has_js: "false"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Zoom-on-Hover Expanding Accordion Gallery
Source: https://codefronts.com/components/css-image-slider/zoom-on-hover-expanding-accordion-gallery/

Zoom-on-hover expanding accordion image gallery in pure CSS — a horizontal row where every panel shares width equally until you hover one, which smoothly expands to reveal its caption while the others gracefully collapse. Flexbox only, no JavaScript. The Apple-store product gallery and Everlane collection page pattern, useful for portfolio grids, restaurant menu galleries, and hospitality resort photo strips.
## HTML
```html
<div class="cis-11">
  <div class="cis-11__row">
    <figure class="cis-11__panel" tabindex="0"><img src="https://picsum.photos/seed/cis11a/900/1200" alt="Canyon"><figcaption><span>01</span>Red Canyon</figcaption></figure>
    <figure class="cis-11__panel" tabindex="0"><img src="https://picsum.photos/seed/cis11b/900/1200" alt="Harbor"><figcaption><span>02</span>Old Harbor</figcaption></figure>
    <figure class="cis-11__panel" tabindex="0"><img src="https://picsum.photos/seed/cis11c/900/1200" alt="Forest"><figcaption><span>03</span>Cloud Forest</figcaption></figure>
    <figure class="cis-11__panel" tabindex="0"><img src="https://picsum.photos/seed/cis11d/900/1200" alt="Dunes"><figcaption><span>04</span>White Dunes</figcaption></figure>
    <figure class="cis-11__panel" tabindex="0"><img src="https://picsum.photos/seed/cis11e/900/1200" alt="Reef"><figcaption><span>05</span>Coral Reef</figcaption></figure>
  </div>
</div>
```
## CSS
```css
.cis-11,
.cis-11 *,
.cis-11 *::before,
.cis-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-11 ::selection {
  background: oklch(0.83 0.15 20);
  color: #180404;
}

.cis-11 {
  --h: min(440px,68vh);
  --radius: 16px;
  --accent: oklch(0.8 0.15 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #f5efec;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  background: radial-gradient(120% 120% at 50% 0%,#180d0b,#0a0605);
}

.cis-11__row {
  display: flex;
  gap: 10px;
  width: min(940px,96vw);
  height: var(--h);
}

.cis-11__panel {
  position: relative;
  flex: 1;
  min-width: 0;
  border-radius: var(--radius);
  overflow: hidden;
  cursor: pointer;
  border: 1px solid rgba(255,255,255,.08);
  transition: flex .55s cubic-bezier(.2,.8,.2,1);
  outline: none;
}

.cis-11__panel img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform .6s,filter .4s;
  filter: brightness(.72);
}

.cis-11__panel:hover,
.cis-11__panel:focus-visible {
  flex: 5;
}

.cis-11__panel:hover img,
.cis-11__panel:focus-visible img {
  filter: brightness(.92);
  transform: scale(1.05);
}

.cis-11__panel figcaption {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 44px 18px 16px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  font-size: 18px;
  font-weight: 700;
  white-space: nowrap;
  background: linear-gradient(transparent,rgba(8,4,3,.82));
  opacity: 0;
  transform: translateY(12px);
  transition: opacity .4s .1s,transform .4s .1s;
}

.cis-11__panel figcaption span {
  font: 700 11px ui-monospace,Menlo,monospace;
  letter-spacing: .2em;
  color: var(--accent);
}

.cis-11__panel:hover figcaption,
.cis-11__panel:focus-visible figcaption {
  opacity: 1;
  transform: none;
}

@media (prefers-reduced-motion: reduce) {
  .cis-11__panel,
    .cis-11__panel img,
    .cis-11__panel figcaption {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — flex:1 → flex:5 on hover/focus drives the accordion. */
```
