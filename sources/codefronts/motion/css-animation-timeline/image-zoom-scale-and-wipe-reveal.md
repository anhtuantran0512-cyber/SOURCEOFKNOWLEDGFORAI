---
source: "codefronts"
url: "https://codefronts.com/motion/css-animation-timeline/image-zoom-scale-and-wipe-reveal/"
title: "Image Zoom / Scale and Wipe Reveal"
section: "motion"
category: "css-animation-timeline"
category_name: "CSS animation-timeline Demos"
description: "The e-commerce lookbook finisher: product photography enters the viewport clipped and slightly zoomed, then wipes open and settles to crisp 100% exactly as…"
has_js: "false"
---

Here's a working CSS animation-timeline Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Image Zoom / Scale and Wipe Reveal
Source: https://codefronts.com/motion/css-animation-timeline/image-zoom-scale-and-wipe-reveal/

The e-commerce lookbook finisher: product photography enters the viewport clipped and slightly zoomed, then wipes open and settles to crisp 100% exactly as it crosses into view — clip-path inset + counter-scale on view() timelines, thumb-locked at 120fps because it never leaves the compositor.
## HTML
```html
<section class="sda-11" aria-label="Product gallery with wipe and zoom reveals" role="region" tabindex="0">
  <header class="sda-11__head"><p class="sda-11__kicker">Lookbook · SS26</p><h2>Resolve on arrival</h2><p class="sda-11__sub">Each image wipes open and settles to 1:1 as it enters — scrubbed by its own view timeline.</p></header>
  <div class="sda-11__gallery">
    <figure class="sda-11__item sda-11__item--l"><div class="sda-11__frame"><img src="https://picsum.photos/seed/look-01/900/640" width="900" height="640" alt="Ceramic vase collection on linen"></div><figcaption><span>01</span> Stoneware, matte glaze</figcaption></figure>
    <figure class="sda-11__item sda-11__item--r"><div class="sda-11__frame"><img src="https://picsum.photos/seed/look-02/900/640" width="900" height="640" alt="Folded textiles in earth tones"></div><figcaption><span>02</span> Hand-loomed throws</figcaption></figure>
    <figure class="sda-11__item sda-11__item--l"><div class="sda-11__frame"><img src="https://picsum.photos/seed/look-03/900/640" width="900" height="640" alt="Oak stool in raking light"></div><figcaption><span>03</span> Oak, oiled finish</figcaption></figure>
    <figure class="sda-11__item sda-11__item--r"><div class="sda-11__frame"><img src="https://picsum.photos/seed/look-04/900/640" width="900" height="640" alt="Brass fixtures on dark stone"></div><figcaption><span>04</span> Brass, living patina</figcaption></figure>
  </div>
  <p class="sda-11__end">Scroll back up — every reveal runs in reverse.</p>
</section>
```
## CSS
```css
.sda-11,
.sda-11 *,
.sda-11 *::before,
.sda-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sda-11 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: oklch(0.94 0.006 80);
  color: oklch(0.24 0.015 60);
  width: 100%;
  height: 100vh;
  overflow-y: auto;
}

.sda-11__head {
  width: min(640px,100%);
  margin: 0 auto;
  text-align: center;
  padding: 14vh 24px 8vh;
}

.sda-11__kicker {
  font: 700 11px ui-monospace,Menlo,monospace;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: oklch(0.5 0.09 50);
  margin-bottom: 14px;
}

.sda-11__head h2 {
  font-size: clamp(30px,4.5vw,46px);
  font-weight: 800;
  letter-spacing: -.02em;
}

.sda-11__sub {
  margin-top: 14px;
  font-size: 15.5px;
  color: oklch(0.45 0.02 60);
  line-height: 1.6;
}

.sda-11__gallery {
  width: min(760px,100%);
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 12vh;
  padding: 0 24px 8vh;
}

.sda-11__item {
  width: min(560px,100%);
}

.sda-11__item--r {
  align-self: flex-end;
}

.sda-11__frame {
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 24px 50px -28px rgba(40,30,15,.5);
}

.sda-11__frame img {
  display: block;
  width: 100%;
  height: auto;
}

.sda-11__item figcaption {
  font-size: 13.5px;
  color: oklch(0.45 0.02 60);
  padding-top: 10px;
}

.sda-11__item figcaption span {
  font: 700 11px ui-monospace,Menlo,monospace;
  letter-spacing: .14em;
  color: oklch(0.5 0.09 50);
  margin-right: 8px;
}

.sda-11__end {
  text-align: center;
  font-size: 13.5px;
  color: oklch(0.5 0.02 60);
  padding-bottom: 20vh;
}

.sda-11:focus-visible {
  outline: 3px solid oklch(0.5 0.09 50);
  outline-offset: -3px;
}

@supports (animation-timeline: view()) {
  .sda-11__frame {
    animation: linear both;
    animation-timeline: view();
    animation-range: entry 0% cover 45%;
  }

  .sda-11__frame img {
    animation: sda-11-zoom linear both;
    animation-timeline: view();
    animation-range: entry 0% cover 45%;
  }

  .sda-11__item--l .sda-11__frame {
    animation-name: sda-11-wipe-l;
  }

  .sda-11__item--r .sda-11__frame {
    animation-name: sda-11-wipe-r;
  }
}

@keyframes sda-11-wipe-l {
  from {
    clip-path: inset(0 88% 0 0);
  }

  to {
    clip-path: inset(0 0 0 0);
  }
}

@keyframes sda-11-wipe-r {
  from {
    clip-path: inset(0 0 0 88%);
  }

  to {
    clip-path: inset(0 0 0 0);
  }
}

@keyframes sda-11-zoom {
  from {
    transform: scale(1.28);
  }

  to {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sda-11__frame,
    .sda-11__frame img {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — clip-path inset() wipes the frame open while the image counter-zooms from 1.28 to 1, both scrubbed by the figure's own view() timeline over entry 0% → cover 45%. */
```
