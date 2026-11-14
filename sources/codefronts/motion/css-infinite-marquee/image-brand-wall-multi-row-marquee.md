---
source: "codefronts"
url: "https://codefronts.com/motion/css-infinite-marquee/image-brand-wall-multi-row-marquee/"
title: "Image-Heavy Brand Wall — Multi-Row Masonry Marquee Background"
section: "motion"
category: "css-infinite-marquee"
category_name: "CSS Infinite Marquee Designs"
description: "A full-bleed, three-row wall of mixed-width imagery drifting at three different speeds and directions — the 'living moodboard' agencies and creator brands…"
has_js: "false"
---

Here's a working CSS Infinite Marquee Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Image-Heavy Brand Wall — Multi-Row Masonry Marquee Background
Source: https://codefronts.com/motion/css-infinite-marquee/image-brand-wall-multi-row-marquee/

A full-bleed, three-row wall of mixed-width imagery drifting at three different speeds and directions — the 'living moodboard' agencies and creator brands run behind hero copy. Rows use varied tile widths and subtle tilts so it reads masonry, a dark scrim keeps foreground text at AAA contrast, and the whole wall is aria-hidden because it is decoration by design.
## HTML
```html
<section class="mqs-09" aria-label="Image brand wall marquee demo">
  <div class="mqs-09__wall" aria-hidden="true">
    <div class="mqs-09__viewport">
      <div class="mqs-09__group" style="--speed:48s">
        <span class="mqs-09__tile" style="width:220px;--g:linear-gradient(135deg,#f472b6,#c026d3)"></span>
        <span class="mqs-09__tile" style="width:150px;--g:linear-gradient(135deg,#38bdf8,#1d4ed8)"></span>
        <span class="mqs-09__tile" style="width:260px;--g:linear-gradient(135deg,#fbbf24,#ea580c)"></span>
        <span class="mqs-09__tile" style="width:170px;--g:linear-gradient(135deg,#34d399,#0f766e)"></span>
        <span class="mqs-09__tile" style="width:200px;--g:linear-gradient(135deg,#a78bfa,#6d28d9)"></span>
      </div>
      <div class="mqs-09__group" style="--speed:48s">
        <span class="mqs-09__tile" style="width:220px;--g:linear-gradient(135deg,#f472b6,#c026d3)"></span>
        <span class="mqs-09__tile" style="width:150px;--g:linear-gradient(135deg,#38bdf8,#1d4ed8)"></span>
        <span class="mqs-09__tile" style="width:260px;--g:linear-gradient(135deg,#fbbf24,#ea580c)"></span>
        <span class="mqs-09__tile" style="width:170px;--g:linear-gradient(135deg,#34d399,#0f766e)"></span>
        <span class="mqs-09__tile" style="width:200px;--g:linear-gradient(135deg,#a78bfa,#6d28d9)"></span>
      </div>
    </div>
    <div class="mqs-09__viewport">
      <div class="mqs-09__group mqs-09__group--rev" style="--speed:62s">
        <span class="mqs-09__tile" style="width:180px;--g:linear-gradient(135deg,#fb7185,#be123c)"></span>
        <span class="mqs-09__tile" style="width:240px;--g:linear-gradient(135deg,#4ade80,#15803d)"></span>
        <span class="mqs-09__tile" style="width:140px;--g:linear-gradient(135deg,#facc15,#a16207)"></span>
        <span class="mqs-09__tile" style="width:210px;--g:linear-gradient(135deg,#22d3ee,#0e7490)"></span>
        <span class="mqs-09__tile" style="width:160px;--g:linear-gradient(135deg,#c084fc,#7e22ce)"></span>
      </div>
      <div class="mqs-09__group mqs-09__group--rev" style="--speed:62s">
        <span class="mqs-09__tile" style="width:180px;--g:linear-gradient(135deg,#fb7185,#be123c)"></span>
        <span class="mqs-09__tile" style="width:240px;--g:linear-gradient(135deg,#4ade80,#15803d)"></span>
        <span class="mqs-09__tile" style="width:140px;--g:linear-gradient(135deg,#facc15,#a16207)"></span>
        <span class="mqs-09__tile" style="width:210px;--g:linear-gradient(135deg,#22d3ee,#0e7490)"></span>
        <span class="mqs-09__tile" style="width:160px;--g:linear-gradient(135deg,#c084fc,#7e22ce)"></span>
      </div>
    </div>
    <div class="mqs-09__viewport">
      <div class="mqs-09__group" style="--speed:55s">
        <span class="mqs-09__tile" style="width:200px;--g:linear-gradient(135deg,#818cf8,#3730a3)"></span>
        <span class="mqs-09__tile" style="width:160px;--g:linear-gradient(135deg,#f97316,#9a3412)"></span>
        <span class="mqs-09__tile" style="width:250px;--g:linear-gradient(135deg,#2dd4bf,#115e59)"></span>
        <span class="mqs-09__tile" style="width:145px;--g:linear-gradient(135deg,#e879f9,#a21caf)"></span>
        <span class="mqs-09__tile" style="width:190px;--g:linear-gradient(135deg,#94a3b8,#334155)"></span>
      </div>
      <div class="mqs-09__group" style="--speed:55s">
        <span class="mqs-09__tile" style="width:200px;--g:linear-gradient(135deg,#818cf8,#3730a3)"></span>
        <span class="mqs-09__tile" style="width:160px;--g:linear-gradient(135deg,#f97316,#9a3412)"></span>
        <span class="mqs-09__tile" style="width:250px;--g:linear-gradient(135deg,#2dd4bf,#115e59)"></span>
        <span class="mqs-09__tile" style="width:145px;--g:linear-gradient(135deg,#e879f9,#a21caf)"></span>
        <span class="mqs-09__tile" style="width:190px;--g:linear-gradient(135deg,#94a3b8,#334155)"></span>
      </div>
    </div>
  </div>
  <div class="mqs-09__fore">
    <h3 class="mqs-09__hero">Made with the brands you love</h3>
    <p class="mqs-09__sub">Swap the gradient tiles for campaign imagery — the wall is pure decoration, invisible to screen readers.</p>
  </div>
</section>
```
## CSS
```css
.mqs-09,
.mqs-09 *,
.mqs-09 *::before,
.mqs-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.mqs-09 {
  width: 100%;
  --gap: 18px;
  position: relative;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #09090b;
  overflow: hidden;
  min-height: 100vh;
  display: grid;
}

.mqs-09__wall {
  position: absolute;
  inset: -30px 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: var(--gap);
}

.mqs-09__viewport {
  display: flex;
  gap: var(--gap);
  overflow: hidden;
}

.mqs-09__group {
  flex: none;
  display: flex;
  gap: var(--gap);
  animation: mqs-09-scroll var(--speed) linear infinite;
  will-change: transform;
}

.mqs-09__group--rev {
  animation-direction: reverse;
}

@keyframes mqs-09-scroll {
  to {
    transform: translateX(calc(-100% - var(--gap)));
  }
}

.mqs-09__tile {
  flex: none;
  aspect-ratio: 3/2;
  border-radius: 14px;
  background: var(--g);
  opacity: .8;
}

.mqs-09__tile:nth-child(odd) {
  rotate: 1.2deg;
}

.mqs-09__tile:nth-child(even) {
  rotate: -1.2deg;
}

.mqs-09__fore {
  position: relative;
  z-index: 1;
  display: grid;
  place-content: center;
  gap: 12px;
  text-align: center;
  padding: 64px 24px;
  background: radial-gradient(ellipse 70% 80% at 50% 50%,rgba(9,9,11,.92) 30%,rgba(9,9,11,.55) 70%,rgba(9,9,11,.25));
}

.mqs-09__hero {
  font-size: clamp(26px,5vw,44px);
  font-weight: 800;
  color: #fafafa;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.mqs-09__sub {
  font-size: 14px;
  color: #a1a1aa;
  max-width: 52ch;
  margin-inline: auto;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .mqs-09__group {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — three counter-phased rows (--speed + animation-direction each) create the faux-parallax depth; the wall is aria-hidden decoration behind a scrim. */
```
