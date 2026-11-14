---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/parallax-product-showcase-with-pinned-scene/"
title: "Parallax Product Showcase with Pinned Scene"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "A product sequence pinned to the viewport: the unit rotates and lifts as the reader scrolls while three feature callouts hand off to one another at fixed…"
has_js: "false"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Parallax Product Showcase with Pinned Scene
Source: https://codefronts.com/motion/css-parallax-designs/parallax-product-showcase-with-pinned-scene/

A product sequence pinned to the viewport: the unit rotates and lifts as the reader scrolls while three feature callouts hand off to one another at fixed points in the scroll range. One sticky stage, one timeline, four elements with different animation-range windows — the whole choreography is declarative.
## HTML
```html
<div class="plx-09">
  <div class="plx-09__runway">
    <div class="plx-09__stage">
      <div class="plx-09__spot" aria-hidden="true"></div>
      <div class="plx-09__product" aria-hidden="true">
        <span class="plx-09__band"></span>
        <span class="plx-09__cup plx-09__cup--l"></span>
        <span class="plx-09__cup plx-09__cup--r"></span>
      </div>
      <div class="plx-09__hud">
        <p class="plx-09__brand">Kestrel Audio</p>
        <h1 class="plx-09__h1">Field 02</h1>
        <p class="plx-09__price">Shipping March · $349</p>
      </div>
      <div class="plx-09__callouts">
        <article class="plx-09__callout plx-09__callout--1">
          <p class="plx-09__step">01 · Driver</p>
          <h2 class="plx-09__h2">40mm beryllium-coated dome</h2>
          <p class="plx-09__p">Tuned flat to 12kHz, then given back 1.5dB at the top so field recordings stop sounding closed.</p>
        </article>
        <article class="plx-09__callout plx-09__callout--2">
          <p class="plx-09__step">02 · Chassis</p>
          <h2 class="plx-09__h2">Cast magnesium yoke</h2>
          <p class="plx-09__p">Two moving parts per side. The band pivots inside the cup rather than over it, so nothing to fatigue.</p>
        </article>
        <article class="plx-09__callout plx-09__callout--3">
          <p class="plx-09__step">03 · Power</p>
          <h2 class="plx-09__h2">62 hours, wired passthrough</h2>
          <p class="plx-09__p">Runs dead-battery on a cable at full spec. Charge port is USB-C on the left cup.</p>
        </article>
      </div>
    </div>
  </div>
  <section class="plx-09__specs">
    <h2 class="plx-09__h3">Specification</h2>
    <dl class="plx-09__grid">
      <div class="plx-09__cell"><dt>Impedance</dt><dd>32 Ω</dd></div>
      <div class="plx-09__cell"><dt>Weight</dt><dd>286 g</dd></div>
      <div class="plx-09__cell"><dt>Cable</dt><dd>2 m braided, 3.5mm</dd></div>
      <div class="plx-09__cell"><dt>Warranty</dt><dd>5 years, parts stocked 10</dd></div>
    </dl>
    <p class="plx-09__foot">Photography by Alex Chen. Pre-orders open to registered field kits first.</p>
  </section>
</div>
```
## CSS
```css
.plx-09 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "Geist", "Inter", system-ui, -apple-system, sans-serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --s0: #0e0f11;
  --s1: #16181c;
  --s2: #1f2228;
  --ink: #f0f1f3;
  --muted: #969ba5;
  --accent: #ff6a2b;
  background: var(--s0);
  color: var(--ink);
  font-family: var(--font-body);
  overflow-x: clip;
}

.plx-09 * {
  box-sizing: border-box;
}

.plx-09__runway {
  block-size: 320svh;
}

.plx-09__stage {
  position: sticky;
  top: 0;
  block-size: 100svh;
  overflow: clip;
  display: grid;
  place-items: center;
}

.plx-09__spot {
  position: absolute;
  inset: -20% -10%;
  background: radial-gradient(45% 40% at 50% 42%, rgba(255,106,43,0.34), rgba(255,106,43,0) 70%), radial-gradient(60% 50% at 50% 58%, rgba(120,140,200,0.16), rgba(0,0,0,0) 72%);
  will-change: transform;
}

.plx-09__product {
  position: relative;
  inline-size: clamp(150px, 34vmin, 300px);
  aspect-ratio: 1;
  will-change: transform;
}

.plx-09__band {
  position: absolute;
  inset: 0 12% auto;
  block-size: 62%;
  border: clamp(10px, 3vmin, 20px) solid #d9dde4;
  border-bottom-color: transparent;
  border-radius: 50% 50% 0 0 / 70% 70% 0 0;
}

.plx-09__cup {
  position: absolute;
  bottom: 6%;
  inline-size: 30%;
  block-size: 42%;
  border-radius: 22% / 30%;
  background: linear-gradient(160deg, #3b4048 0%, #14161a 62%, #24272d 100%);
  box-shadow: inset 0 0 0 clamp(4px, 1.2vmin, 8px) #d9dde4;
}

.plx-09__cup--l {
  left: 4%;
}

.plx-09__cup--r {
  right: 4%;
}

.plx-09__hud {
  position: absolute;
  inset-block-start: clamp(20px, 5vh, 54px);
  inset-inline-start: clamp(18px, 5vw, 56px);
  min-inline-size: 0;
}

.plx-09__brand {
  margin: 0 0 8px;
  font: 600 10px/1 var(--font-body);
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--accent);
}

.plx-09__h1 {
  margin: 0 0 6px;
  font-family: var(--font-display);
  font-size: clamp(26px, 6vw, 54px);
  font-weight: 650;
  letter-spacing: -0.035em;
}

.plx-09__price {
  margin: 0;
  font-size: 13px;
  color: var(--muted);
}

.plx-09__callouts {
  position: absolute;
  inset-block-end: clamp(20px, 5vh, 56px);
  inset-inline: clamp(18px, 5vw, 56px);
  min-block-size: 168px;
}

.plx-09__callout {
  position: absolute;
  inset-inline: 0;
  inset-block-end: 0;
  max-inline-size: 26rem;
  min-inline-size: 0;
  padding: 16px 18px;
  border-radius: 14px;
  border: 1px solid #2a2e36;
  background: var(--s1);
  will-change: transform, opacity;
}

.plx-09__step {
  margin: 0 0 8px;
  font: 600 10px/1 var(--font-body);
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--accent);
}

.plx-09__h2 {
  margin: 0 0 8px;
  font-family: var(--font-display);
  font-size: clamp(17px, 3.4vw, 24px);
  font-weight: 620;
  line-height: 1.16;
  letter-spacing: -0.02em;
}

.plx-09__p {
  margin: 0;
  font-size: 14px;
  line-height: 1.62;
  color: var(--muted);
  text-wrap: pretty;
}

.plx-09__specs {
  position: relative;
  background: var(--s0);
  border-top: 1px solid #24272d;
  padding: clamp(40px, 8vw, 96px) clamp(18px, 5vw, 56px) 120px;
}

.plx-09__h3 {
  margin: 0 0 22px;
  font-family: var(--font-display);
  font-size: 12px;
  font-weight: 620;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

.plx-09__grid {
  margin: 0 0 30px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 170px), 1fr));
  gap: 1px;
  background: #24272d;
  border: 1px solid #24272d;
}

.plx-09__cell {
  background: var(--s1);
  padding: 16px;
  min-inline-size: 0;
}

.plx-09__cell dt {
  font-size: 11px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--muted);
}

.plx-09__cell dd {
  margin: 8px 0 0;
  font-family: var(--font-display);
  font-size: 19px;
  letter-spacing: -0.02em;
}

.plx-09__foot {
  margin: 0;
  font-size: 13px;
  color: var(--muted);
  max-inline-size: 34rem;
}

@supports (animation-timeline: scroll()) {
  .plx-09__callout {
    opacity: 0;
    transform: translateY(18px);
  }

  .plx-09__spot {
    animation: plx-09-spot linear both;
    animation-timeline: scroll(root);
    animation-range: 0 80%;
  }

  .plx-09__product {
    animation: plx-09-turn linear both;
    animation-timeline: scroll(root);
    animation-range: 0 80%;
  }

  .plx-09__callout--1 {
    animation: plx-09-card linear both;
    animation-timeline: scroll(root);
    animation-range: 10% 30%;
  }

  .plx-09__callout--2 {
    animation: plx-09-card linear both;
    animation-timeline: scroll(root);
    animation-range: 34% 54%;
  }

  .plx-09__callout--3 {
    animation: plx-09-card linear both;
    animation-timeline: scroll(root);
    animation-range: 58% 78%;
  }
}

@keyframes plx-09-spot {
  to {
    transform: translateY(-46px) scale(1.08);
  }
}

@keyframes plx-09-turn {
  0% {
    transform: translateY(28px) rotate(-9deg) scale(0.94);
  }

  100% {
    transform: translateY(-34px) rotate(9deg) scale(1.06);
  }
}

@keyframes plx-09-card {
  0% {
    opacity: 0;
    transform: translateY(20px);
  }

  18%,
    82% {
    opacity: 1;
    transform: translateY(0);
  }

  100% {
    opacity: 0;
    transform: translateY(-14px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-09__spot,
    .plx-09__product,
    .plx-09__callout {
    animation: none !important;
    transform: none !important;
    opacity: 1 !important;
    will-change: auto;
  }

  .plx-09__callouts {
    position: static;
    display: grid;
    gap: 12px;
    margin-top: 24px;
  }

  .plx-09__callout {
    position: static;
  }

  .plx-09__stage {
    block-size: auto;
    min-block-size: 100svh;
    padding: 90px 0 40px;
  }
}
```
