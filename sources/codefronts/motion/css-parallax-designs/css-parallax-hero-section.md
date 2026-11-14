---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/css-parallax-hero-section/"
title: "CSS Parallax Hero Section with Layered Scroll"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "A photographer's hero built from three photographic planes that separate as the page scrolls: a wide plate behind, a portrait plate mid-depth, and the type…"
has_js: "false"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Parallax Hero Section with Layered Scroll
Source: https://codefronts.com/motion/css-parallax-designs/css-parallax-hero-section/

A photographer's hero built from three photographic planes that separate as the page scrolls: a wide plate behind, a portrait plate mid-depth, and the type block anchored in front. The scrim under the type is fixed to the copy rather than the image, so the headline holds contrast at every point in the parallax range.
## HTML
```html
<div class="plx-13">
  <header class="plx-13__hero">
    <div class="plx-13__frame plx-13__frame--back">
      <img class="plx-13__plate plx-13__plate--back" src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1600&auto=format&fit=crop" alt="Ridge line above a bank of cloud at first light" loading="eager" decoding="async">
    </div>
    <div class="plx-13__frame plx-13__frame--mid">
      <img class="plx-13__plate plx-13__plate--mid" src="https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=1200&auto=format&fit=crop" alt="Sunlight breaking across a steep green valley" loading="eager" decoding="async">
    </div>
    <div class="plx-13__grain" aria-hidden="true"></div>
    <div class="plx-13__copy">
      <p class="plx-13__eyebrow">Alex Chen · Selected landscape</p>
      <h1 class="plx-13__h1">Above the cloud line, before anyone else is awake</h1>
      <p class="plx-13__lede">Eighteen months on the eastern ranges. Large format, no filters, one exposure per morning.</p>
      <a class="plx-13__cta" href="#plx-13-work">View the series</a>
    </div>
  </header>
  <main class="plx-13__body" id="plx-13-work">
    <section class="plx-13__row">
      <h2 class="plx-13__h2">The series</h2>
      <p class="plx-13__p">Forty-one plates, printed at 60 by 90 centimetres on baryta. The sequence follows altitude rather than date, which means the weather jumps around and the light does not.</p>
    </section>
    <section class="plx-13__row">
      <h2 class="plx-13__h2">Process</h2>
      <p class="plx-13__p">A 4x5 field camera, two lenses, and a tripod that has been rebuilt twice. Exposures run from a fifteenth of a second to four minutes; the long ones are almost always fog.</p>
    </section>
    <section class="plx-13__row">
      <h2 class="plx-13__h2">Prints and licensing</h2>
      <p class="plx-13__p">Editions of nine, signed on the verso. Licensing handled directly — studio enquiries to Priya Sharma.</p>
    </section>
  </main>
</div>
```
## CSS
```css
.plx-13 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "Iowan Old Style", "Times New Roman", Georgia, serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --bg: #17110f;
  --ink: #f6ece4;
  --muted: #b09a8d;
  --accent: #ffb27a;
  --rule: #35262010;
  --travel: 0.6;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-body);
  overflow-x: clip;
}

.plx-13 * {
  box-sizing: border-box;
}

@media (min-width: 760px) {
  .plx-13 {
    --travel: 0.8;
  }
}

@media (min-width: 1180px) {
  .plx-13 {
    --travel: 1;
  }
}

.plx-13__hero {
  position: relative;
  min-height: 100svh;
  overflow: clip;
  display: flex;
  align-items: flex-end;
}

.plx-13__frame {
  position: absolute;
  overflow: clip;
}

.plx-13__frame--back {
  inset: 0;
}

.plx-13__frame--mid {
  inset-block: 12% 18%;
  inset-inline-end: clamp(-4%, 2vw, 6%);
  inline-size: clamp(180px, 40vw, 520px);
  border: 1px solid rgba(246,236,228,0.28);
}

.plx-13__plate {
  display: block;
  inline-size: 100%;
  block-size: 122%;
  object-fit: cover;
  will-change: transform;
}

.plx-13__plate--back {
  filter: brightness(0.72) saturate(0.9);
}

.plx-13__grain {
  position: absolute;
  inset: -10%;
  pointer-events: none;
  opacity: 0.5;
  background-image: radial-gradient(rgba(255,255,255,0.14) 0.5px, transparent 0.6px);
  background-size: 3px 3px;
  will-change: transform;
}

.plx-13__copy {
  position: relative;
  z-index: 3;
  inline-size: 100%;
  min-inline-size: 0;
  max-inline-size: 46rem;
  padding: clamp(90px, 22vh, 240px) clamp(22px, 5vw, 68px) clamp(30px, 6vw, 70px);
  background: linear-gradient(to top, rgba(14,9,8,0.94) 0%, rgba(14,9,8,0.78) 46%, rgba(14,9,8,0) 100%);
}

.plx-13__eyebrow {
  margin: 0 0 16px;
  font: 600 10px/1 var(--font-body);
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--accent);
}

.plx-13__h1 {
  margin: 0 0 16px;
  max-inline-size: 28rem;
  font-family: var(--font-display);
  font-size: clamp(30px, 6.6vw, 62px);
  font-weight: 400;
  line-height: 1.04;
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.plx-13__lede {
  margin: 0 0 26px;
  max-inline-size: 30rem;
  font-size: clamp(15px, 3.4vw, 17px);
  line-height: 1.68;
  color: var(--muted);
  text-wrap: pretty;
}

.plx-13__cta {
  display: inline-flex;
  align-items: center;
  min-height: 46px;
  padding: 0 22px;
  border: 1px solid var(--accent);
  border-radius: 2px;
  color: var(--accent);
  font: 600 12px/1 var(--font-body);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  text-decoration: none;
}

.plx-13__cta:hover {
  background: var(--accent);
  color: #241511;
}

.plx-13__cta:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.plx-13__body {
  position: relative;
  z-index: 4;
  background: var(--bg);
  padding: clamp(44px, 8vw, 104px) clamp(22px, 5vw, 68px) 130px;
}

.plx-13__row {
  max-inline-size: 40rem;
  min-inline-size: 0;
  padding-block: clamp(22px, 4vw, 34px);
  border-top: 1px solid #33241f;
}

.plx-13__h2 {
  margin: 0 0 12px;
  font-family: var(--font-display);
  font-size: clamp(20px, 4vw, 30px);
  font-weight: 400;
  letter-spacing: -0.01em;
}

.plx-13__p {
  margin: 0;
  font-size: clamp(15px, 3.4vw, 17px);
  line-height: 1.74;
  color: #cbb6a9;
  text-wrap: pretty;
}

@supports (animation-timeline: scroll()) {
  .plx-13__plate--back {
    animation: plx-13-back linear both;
    animation-timeline: scroll(root);
  }

  .plx-13__plate--mid {
    animation: plx-13-mid linear both;
    animation-timeline: scroll(root);
  }

  .plx-13__grain {
    animation: plx-13-grain linear both;
    animation-timeline: scroll(root);
  }
}

@keyframes plx-13-back {
  to {
    transform: translateY(calc(-60px * var(--travel)));
  }
}

@keyframes plx-13-mid {
  to {
    transform: translateY(calc(-130px * var(--travel)));
  }
}

@keyframes plx-13-grain {
  to {
    transform: translateY(calc(-210px * var(--travel)));
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-13__plate,
    .plx-13__grain {
    animation: none !important;
    transform: none !important;
    will-change: auto;
  }

  .plx-13__plate {
    block-size: 100%;
  }
}

@media (max-width: 620px) {
  .plx-13__frame--mid {
    inset-block: 8% 40%;
    inline-size: 52vw;
  }
}
```
