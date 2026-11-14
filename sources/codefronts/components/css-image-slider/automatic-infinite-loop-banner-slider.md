---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/automatic-infinite-loop-banner-slider/"
title: "Automatic Infinite-Loop Banner Slider"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: "Automatic infinite-loop CSS banner slider that runs forever from one @keyframes transform — perfect for hero strips, promotional banners, and scrolling…"
has_js: "false"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Automatic Infinite-Loop Banner Slider
Source: https://codefronts.com/components/css-image-slider/automatic-infinite-loop-banner-slider/

Automatic infinite-loop CSS banner slider that runs forever from one @keyframes transform — perfect for hero strips, promotional banners, and scrolling gallery marquees. Feathered mask edges hide the loop seam, pauses on hover, and honours prefers-reduced-motion. No JavaScript, no autoplay interval hack, no visible reset frame.
## HTML
```html
<div class="cis-05">
  <div class="cis-05__stage" aria-label="Auto-scrolling image banner">
    <div class="cis-05__marquee">
      <figure class="cis-05__item"><img src="https://picsum.photos/seed/cis05a/600/400" alt="Studio still life"></figure>
      <figure class="cis-05__item"><img src="https://picsum.photos/seed/cis05b/600/400" alt="Mountain switchback road"></figure>
      <figure class="cis-05__item"><img src="https://picsum.photos/seed/cis05c/600/400" alt="Coastline from above"></figure>
      <figure class="cis-05__item"><img src="https://picsum.photos/seed/cis05d/600/400" alt="Architectural detail"></figure>
      <figure class="cis-05__item"><img src="https://picsum.photos/seed/cis05e/600/400" alt="Field at golden hour"></figure>
      <figure class="cis-05__item" aria-hidden="true"><img src="https://picsum.photos/seed/cis05a/600/400" alt=""></figure>
      <figure class="cis-05__item" aria-hidden="true"><img src="https://picsum.photos/seed/cis05b/600/400" alt=""></figure>
      <figure class="cis-05__item" aria-hidden="true"><img src="https://picsum.photos/seed/cis05c/600/400" alt=""></figure>
      <figure class="cis-05__item" aria-hidden="true"><img src="https://picsum.photos/seed/cis05d/600/400" alt=""></figure>
      <figure class="cis-05__item" aria-hidden="true"><img src="https://picsum.photos/seed/cis05e/600/400" alt=""></figure>
    </div>
  </div>
  <p class="cis-05__hint">hover to pause</p>
</div>
```
## CSS
```css
.cis-05,
.cis-05 *,
.cis-05 *::before,
.cis-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-05 ::selection {
  background: oklch(0.85 0.16 160);
  color: #04140c;
}

.cis-05 {
  --speed: 34s;
  --item: 300px;
  --gap: 18px;
  --fade: 12%;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #e8f0ea;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 16px;
  background: linear-gradient(120deg,#08120c,#0c1a12 55%,#08120c);
}

.cis-05__stage {
  width: min(960px,98vw);
  overflow: hidden;
  -webkit-mask-image: linear-gradient(90deg,transparent,#000 var(--fade),#000 calc(100% - var(--fade)),transparent);
  mask-image: linear-gradient(90deg,transparent,#000 var(--fade),#000 calc(100% - var(--fade)),transparent);
}

.cis-05__marquee {
  display: flex;
  gap: var(--gap);
  width: max-content;
  animation: cis-05-scroll var(--speed) linear infinite;
  will-change: transform;
}

.cis-05__stage:hover .cis-05__marquee {
  animation-play-state: paused;
}

.cis-05__item {
  flex: 0 0 var(--item);
  aspect-ratio: 3/2;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid rgba(255,255,255,.08);
  box-shadow: 0 20px 40px -24px rgba(0,0,0,.8);
  transition: transform .4s;
}

.cis-05__item:hover {
  transform: translateY(-6px) scale(1.02);
}

.cis-05__item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.cis-05__hint {
  font-size: 11px;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: #5f7a68;
}

@keyframes cis-05-scroll {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(-50%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cis-05__marquee {
    animation: none;
  }

  .cis-05__item {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — one @keyframes translateX loop over a doubled image strip. */
```
