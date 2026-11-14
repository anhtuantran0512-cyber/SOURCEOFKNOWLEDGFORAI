---
source: "codefronts"
url: "https://codefronts.com/components/css-image-slider/scroll-driven-viewport-timeline-gallery/"
title: "Scroll-Driven Viewport Timeline Gallery"
section: "components"
category: "css-image-slider"
category_name: "CSS Image Sliders"
description: "Scroll-driven viewport timeline gallery — images scale, rotate, and fade in lockstep with how far they have travelled through the viewport, bound directly to…"
has_js: "false"
---

Here's a working CSS Image Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll-Driven Viewport Timeline Gallery
Source: https://codefronts.com/components/css-image-slider/scroll-driven-viewport-timeline-gallery/

Scroll-driven viewport timeline gallery — images scale, rotate, and fade in lockstep with how far they have travelled through the viewport, bound directly to the page's scroll via native CSS animation-timeline: view(). Buttery, JS-free motion tied to scroll position with no IntersectionObserver, GSAP ScrollTrigger (30KB), Locomotive Scroll (18KB), or rellax.js dependency. The future of scroll-driven UI, shipping in Chrome 115+ and Safari 26+ today.
## HTML
```html
<div class="cis-20">
  <div class="cis-20__scroller">
    <p class="cis-20__hint">↓ scroll this panel ↓</p>
    <div class="cis-20__grid">
      <figure class="cis-20__item"><img src="https://picsum.photos/seed/cis20a/800/600" alt="Gallery 1"></figure>
      <figure class="cis-20__item"><img src="https://picsum.photos/seed/cis20b/800/1000" alt="Gallery 2"></figure>
      <figure class="cis-20__item"><img src="https://picsum.photos/seed/cis20c/800/600" alt="Gallery 3"></figure>
      <figure class="cis-20__item"><img src="https://picsum.photos/seed/cis20d/800/900" alt="Gallery 4"></figure>
      <figure class="cis-20__item"><img src="https://picsum.photos/seed/cis20e/800/650" alt="Gallery 5"></figure>
      <figure class="cis-20__item"><img src="https://picsum.photos/seed/cis20f/800/850" alt="Gallery 6"></figure>
    </div>
  </div>
</div>
```
## CSS
```css
.cis-20,
.cis-20 *,
.cis-20 *::before,
.cis-20 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cis-20 ::selection {
  background: oklch(0.84 0.15 30);
  color: #180604;
}

.cis-20 {
  --accent: oklch(0.8 0.15 30);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #f4ede9;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 30px 20px;
  background: radial-gradient(120% 120% at 50% 0%,#17100c,#0a0705);
}

.cis-20__scroller {
  width: min(720px,94vw);
  height: min(600px,84vh);
  overflow-y: auto;
  border-radius: 20px;
  border: 1px solid #2a201a;
  padding: 20px;
  scrollbar-width: thin;
  background: #0d0906;
  box-shadow: 0 30px 70px -44px #000;
  scroll-behavior: smooth;
}

.cis-20__hint {
  text-align: center;
  font: 11px ui-monospace,Menlo,monospace;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: var(--accent);
  padding: 8px 0 18px;
}

.cis-20__grid {
  columns: 2;
  column-gap: 16px;
}

.cis-20__item {
  break-inside: avoid;
  margin-bottom: 16px;
  border-radius: 14px;
  overflow: hidden;
  border: 1px solid #2a201a;
}

.cis-20__item img {
  width: 100%;
  height: auto;
  display: block;
}

@supports (animation-timeline: view()) {
  .cis-20__item {
    animation: cis-20-reveal linear both;
    animation-timeline: view();
    animation-range: entry 0% cover 42%;
  }

  @keyframes cis-20-reveal {
    from {
      opacity: 0;
      transform: scale(.82) rotate(-4deg) translateY(30px);
      filter: blur(6px);
    }

    to {
      opacity: 1;
      transform: none;
      filter: blur(0);
    }
  }
}

@media (prefers-reduced-motion: reduce) {
  .cis-20__item {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — animation-timeline: view() binds each image's reveal to scroll. */
```
