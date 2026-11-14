---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/scroll-snap-touch-image-carousel/"
title: "Scroll-Snap Touch Image Carousel"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: "Scroll-snap touch image carousel — mobile-first swipe gallery that feels like a native app on iOS Safari and Chrome Android."
has_js: "false"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll-Snap Touch Image Carousel
Source: https://codefronts.com/components/css-image-slider/scroll-snap-touch-image-carousel/

Scroll-snap touch image carousel — mobile-first swipe gallery that feels like a native app on iOS Safari and Chrome Android. Works with mouse wheel, keyboard, and touch inertia out of the box, and layers on scroll-driven entrance animations plus the new CSS Carousel markers. Zero JavaScript, zero gesture library, screen-reader friendly.
## HTML
```html
<div class="cis-02">
  <div class="cis-02__rail" tabindex="0" aria-label="Photo carousel, scroll or swipe">
    <figure class="cis-02__slide"><img src="https://picsum.photos/seed/cis02a/900/1100" alt="Concrete staircase spiral"><figcaption>Spiral</figcaption></figure>
    <figure class="cis-02__slide"><img src="https://picsum.photos/seed/cis02b/900/1100" alt="Neon-lit alley at night"><figcaption>After hours</figcaption></figure>
    <figure class="cis-02__slide"><img src="https://picsum.photos/seed/cis02c/900/1100" alt="Sand dunes with sharp shadow line"><figcaption>Dunes</figcaption></figure>
    <figure class="cis-02__slide"><img src="https://picsum.photos/seed/cis02d/900/1100" alt="Glass facade reflecting clouds"><figcaption>Facade</figcaption></figure>
    <figure class="cis-02__slide"><img src="https://picsum.photos/seed/cis02e/900/1100" alt="Forest path in heavy mist"><figcaption>Understory</figcaption></figure>
  </div>
  <p class="cis-02__hint">swipe · scroll · arrow keys</p>
</div>
```
## CSS
```css
.cis-02,
.cis-02 *,
.cis-02 *::before,
.cis-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-02 ::selection {
  background: #7cf;
  color: #04121a;
}

.cis-02 {
  --fade: 9%;
  --accent: oklch(0.82 0.13 220);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #e9eef2;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 18px;
  padding: 40px 0;
  background: linear-gradient(160deg,#0a1016,#0f1a22 60%,#0a1016);
}

.cis-02__rail {
  display: flex;
  gap: 18px;
  width: min(880px,96vw);
  padding: 14px calc(11% - 9px);
  overflow-x: auto;
  overscroll-behavior-x: contain;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  scrollbar-width: none;
  -webkit-mask-image: linear-gradient(90deg,transparent,#000 var(--fade),#000 calc(100% - var(--fade)),transparent);
  mask-image: linear-gradient(90deg,transparent,#000 var(--fade),#000 calc(100% - var(--fade)),transparent);
}

.cis-02__rail::-webkit-scrollbar {
  display: none;
}

.cis-02__rail:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 6px;
  border-radius: 24px;
}

.cis-02__slide {
  position: relative;
  flex: 0 0 66%;
  scroll-snap-align: center;
  aspect-ratio: 9/11;
  border-radius: 22px;
  overflow: hidden;
  border: 1px solid rgba(255,255,255,.1);
  box-shadow: 0 30px 60px -30px rgba(0,0,0,.85);
}

.cis-02__slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.cis-02__slide figcaption {
  position: absolute;
  left: 16px;
  bottom: 14px;
  padding: 7px 13px;
  font-size: 13px;
  font-weight: 600;
  border-radius: 999px;
  background: color-mix(in oklab,#0a1016 55%,transparent);
  border: 1px solid rgba(255,255,255,.18);
  backdrop-filter: blur(10px);
}

.cis-02__hint {
  font-size: 11px;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: #6f8494;
}
/* scroll-driven entrance — progressive enhancement */

@supports (animation-timeline: view()) {
  .cis-02__slide {
    animation: cis-02-pop linear both;
    animation-timeline: view(inline);
    animation-range: entry 0% cover 34%;
  }

  @keyframes cis-02-pop {
    from {
      opacity: .25;
      transform: scale(.86) translateY(10px);
    }

    to {
      opacity: 1;
      transform: none;
    }
  }
}
/* CSS Carousel spec markers — auto pagination dots */

@supports (scroll-marker-group: after) {
  .cis-02__rail {
    scroll-marker-group: after;
    padding-bottom: 26px;
  }

  .cis-02__rail::scroll-marker-group {
    display: flex;
    gap: 9px;
    justify-content: center;
    margin-top: 14px;
  }

  .cis-02__slide::scroll-marker {
    content: "";
    width: 9px;
    height: 9px;
    border-radius: 50%;
    background: rgba(255,255,255,.28);
    border: 0;
    cursor: pointer;
    transition: background .25s,width .25s;
  }

  .cis-02__slide::scroll-marker:hover {
    background: rgba(255,255,255,.6);
  }

  .cis-02__slide::scroll-marker:target-current {
    background: var(--accent);
    width: 24px;
    border-radius: 5px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cis-02__rail {
    scroll-behavior: auto;
  }

  .cis-02__slide {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — native scroll-snap plus CSS scroll-driven animations. */
```
