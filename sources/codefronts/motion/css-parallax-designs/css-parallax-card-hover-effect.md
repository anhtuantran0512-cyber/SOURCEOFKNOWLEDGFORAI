---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/css-parallax-card-hover-effect/"
title: "Parallax Card Hover with Mouse Tracking"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "A product card that comes apart under the cursor: the photograph tilts on two axes, the badge and title lift toward the viewer, and a specular sheen tracks…"
has_js: "true"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Parallax Card Hover with Mouse Tracking
Source: https://codefronts.com/motion/css-parallax-designs/css-parallax-card-hover-effect/

A product card that comes apart under the cursor: the photograph tilts on two axes, the badge and title lift toward the viewer, and a specular sheen tracks the pointer. Roughly fifteen lines of pointer maths write three custom properties; the rest is CSS, and keyboard focus gets the same lifted state.
## HTML
```html
<div class="plx-20">
  <header class="plx-20__head">
    <p class="plx-20__eyebrow">Kestrel Audio · Field 02</p>
    <h1 class="plx-20__h1">The card, taken apart by your cursor</h1>
    <p class="plx-20__lede">Move the pointer over the card. Photograph tilts, badge and title lift, sheen follows. Tab to it for the same state without a mouse.</p>
  </header>
  <div class="plx-20__stage">
    <article class="plx-20__card" id="plx-20-card">
      <div class="plx-20__media">
        <img class="plx-20__photo" src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=1000&auto=format&fit=crop" alt="Over-ear headphones on a bright yellow background" loading="lazy" decoding="async">
        <span class="plx-20__sheen" aria-hidden="true"></span>
        <p class="plx-20__badge">New</p>
      </div>
      <div class="plx-20__body">
        <h2 class="plx-20__h2">Field 02 Reference</h2>
        <p class="plx-20__desc">Closed-back, 32 ohm, 62 hours. Cast magnesium yoke with two moving parts per side.</p>
        <div class="plx-20__row">
          <p class="plx-20__price">$349</p>
          <a class="plx-20__buy" href="#plx-20-specs">Add to bag</a>
        </div>
      </div>
    </article>
  </div>
  <section class="plx-20__specs" id="plx-20-specs">
    <h2 class="plx-20__h3">Details</h2>
    <dl class="plx-20__grid">
      <div class="plx-20__cell"><dt>Drivers</dt><dd>40mm beryllium-coated dome</dd></div>
      <div class="plx-20__cell"><dt>Weight</dt><dd>286 g with cable</dd></div>
      <div class="plx-20__cell"><dt>Cable</dt><dd>2 m braided, replaceable</dd></div>
      <div class="plx-20__cell"><dt>Warranty</dt><dd>5 years, parts stocked 10</dd></div>
    </dl>
    <p class="plx-20__foot">Ships in three working days. Reviewed for us by Jordan Lee.</p>
  </section>
</div>
```
## CSS
```css
.plx-20 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "Geist", "Inter", system-ui, -apple-system, sans-serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --paper: #ffffff;
  --ink: #0b1020;
  --muted: #5c6478;
  --accent: #1d4ed8;
  --rule: #e6e8ef;
  --px: 0;
  --py: 0;
  --hover: 0;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--font-body);
  overflow-x: clip;
}

.plx-20 * {
  box-sizing: border-box;
}

.plx-20__head {
  padding: clamp(36px, 7vw, 92px) clamp(20px, 5vw, 64px) clamp(18px, 3vw, 34px);
  max-inline-size: 46rem;
}

.plx-20__eyebrow {
  margin: 0 0 14px;
  font: 600 10px/1 var(--font-body);
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: var(--accent);
}

.plx-20__h1 {
  margin: 0 0 14px;
  font-family: var(--font-display);
  font-size: clamp(28px, 6vw, 52px);
  font-weight: 640;
  line-height: 1.04;
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.plx-20__lede {
  margin: 0;
  max-inline-size: 32rem;
  font-size: clamp(15px, 3.2vw, 17px);
  line-height: 1.62;
  color: var(--muted);
  text-wrap: pretty;
}

.plx-20__stage {
  display: grid;
  place-items: center;
  padding: clamp(26px, 6vw, 70px) clamp(20px, 5vw, 64px);
  min-block-size: 74svh;
}

.plx-20__card {
  inline-size: 100%;
  max-inline-size: 25rem;
  min-inline-size: 0;
  border-radius: 20px;
  border: 1px solid var(--rule);
  background: var(--paper);
  perspective: 900px;
  transition: box-shadow 260ms ease, transform 260ms ease;
  box-shadow: 0 calc(10px + var(--hover) * 16px) calc(24px + var(--hover) * 30px) calc(-14px - var(--hover) * 6px) rgba(11,16,32,0.4);
  transform: translateY(calc(var(--hover) * -4px));
}

.plx-20__card:focus-within {
  --hover: 1;
}

.plx-20__media {
  position: relative;
  overflow: clip;
  border-radius: 19px 19px 0 0;
  aspect-ratio: 4 / 3;
  background: #ffd400;
  transform-style: preserve-3d;
}

.plx-20__photo {
  display: block;
  inline-size: 106%;
  block-size: 106%;
  margin: -3% 0 0 -3%;
  object-fit: cover;
  will-change: transform;
  transition: transform 220ms ease;
}

.plx-20__sheen {
  position: absolute;
  inset: -30%;
  pointer-events: none;
  background: radial-gradient(28% 28% at calc(50% + var(--px) * 60%) calc(50% + var(--py) * 60%), rgba(255,255,255,0.65), rgba(255,255,255,0) 70%);
  opacity: calc(var(--hover) * 0.9);
  transition: opacity 220ms ease;
}

.plx-20__badge {
  position: absolute;
  inset-block-start: 12px;
  inset-inline-start: 12px;
  margin: 0;
  padding: 6px 11px;
  border-radius: 999px;
  background: var(--accent);
  color: #f4f7ff;
  font: 700 10px/1 var(--font-body);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  transition: transform 220ms ease;
}

.plx-20__body {
  padding: 18px;
}

.plx-20__h2 {
  margin: 0 0 8px;
  font-family: var(--font-display);
  font-size: 20px;
  font-weight: 640;
  letter-spacing: -0.02em;
  transition: transform 220ms ease;
}

.plx-20__desc {
  margin: 0 0 16px;
  font-size: 14px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.plx-20__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  min-inline-size: 0;
}

.plx-20__price {
  margin: 0;
  font-family: var(--font-display);
  font-size: 20px;
  font-weight: 640;
  letter-spacing: -0.02em;
}

.plx-20__buy {
  display: inline-flex;
  align-items: center;
  min-height: 44px;
  padding: 0 18px;
  border-radius: 10px;
  background: var(--accent);
  color: #f4f7ff;
  font: 600 14px/1 var(--font-body);
  text-decoration: none;
}

.plx-20__buy:hover {
  background: #1740b8;
}

.plx-20__buy:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.plx-20__specs {
  padding: clamp(36px, 7vw, 90px) clamp(20px, 5vw, 64px) 130px;
  border-top: 1px solid var(--rule);
}

.plx-20__h3 {
  margin: 0 0 20px;
  font-family: var(--font-display);
  font-size: 12px;
  font-weight: 640;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

.plx-20__grid {
  margin: 0 0 26px;
  display: grid;
  gap: 14px;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr));
}

.plx-20__cell {
  min-inline-size: 0;
  padding-block-end: 14px;
  border-bottom: 1px solid var(--rule);
}

.plx-20__cell dt {
  font: 600 10px/1 var(--font-body);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--muted);
}

.plx-20__cell dd {
  margin: 8px 0 0;
  font-family: var(--font-display);
  font-size: 16px;
}

.plx-20__foot {
  margin: 0;
  font-size: 13px;
  color: var(--muted);
}

@media (pointer: fine) {
  .plx-20__photo {
    transform: rotate3d(calc(var(--py) * -1), var(--px), 0, calc(var(--hover) * 9deg)) scale(calc(1 + var(--hover) * 0.04));
  }

  .plx-20__badge {
    transform: translate3d(calc(var(--px) * 14px), calc(var(--py) * 14px), 40px);
  }

  .plx-20__h2 {
    transform: translate3d(calc(var(--px) * 6px), 0, 22px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-20__photo,
    .plx-20__badge,
    .plx-20__h2 {
    transform: none !important;
    transition: none;
    will-change: auto;
  }

  .plx-20__card {
    transition: none;
  }

  .plx-20__sheen {
    display: none;
  }
}
```

## JavaScript
```js
const card = document.getElementById('plx-20-card');
if (card && matchMedia('(pointer: fine)').matches) {
  let queued = false, px = 0, py = 0, hover = 0;
  const write = () => {
    card.style.setProperty('--px', px.toFixed(3));
    card.style.setProperty('--py', py.toFixed(3));
    card.style.setProperty('--hover', String(hover));
    queued = false;
  };
  const schedule = () => { if (!queued) { queued = true; requestAnimationFrame(write); } };
  card.addEventListener('pointermove', (e) => {
    const r = card.getBoundingClientRect();
    px = (e.clientX - r.left) / r.width - 0.5;
    py = (e.clientY - r.top) / r.height - 0.5;
    hover = 1;
    schedule();
  });
  card.addEventListener('pointerleave', () => { px = 0; py = 0; hover = 0; schedule(); });
}
```
