---
source: "codefronts"
url: "https://codefronts.com/motion/css-parallax-designs/mouse-position-parallax-card-grid/"
title: "Mouse Position Parallax Card Grid"
section: "motion"
category: "css-parallax-designs"
category_name: "CSS Parallax Effects"
description: "A bento grid whose cards hold two planes that answer to the cursor: the artwork slides toward the pointer while the label slides away, so the whole board…"
has_js: "true"
---

Here's a working CSS Parallax Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mouse Position Parallax Card Grid
Source: https://codefronts.com/motion/css-parallax-designs/mouse-position-parallax-card-grid/

A bento grid whose cards hold two planes that answer to the cursor: the artwork slides toward the pointer while the label slides away, so the whole board tilts in place without anything actually rotating. Fifteen lines of pointer tracking write two custom properties; every pixel of movement is CSS. Good for portfolio boards, feature grids and product bento sections.
## HTML
```html
<div class="plx-07">
  <header class="plx-07__head">
    <p class="plx-07__eyebrow">Studio Halcyon · Selected work</p>
    <h1 class="plx-07__h1">Six projects, one cursor</h1>
    <p class="plx-07__lede">Move the pointer across the board. Artwork drifts toward it, labels drift away — two planes per card, no rotation anywhere.</p>
  </header>
  <div class="plx-07__grid" id="plx-07-grid">
    <article class="plx-07__card plx-07__card--tall" style="--depth: 16">
      <img class="plx-07__art" src="https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?w=1200&auto=format&fit=crop" alt="Low sun over open farmland" loading="lazy" decoding="async">
      <div class="plx-07__label"><h2 class="plx-07__h2">Sunrise Bank</h2><p class="plx-07__meta">Identity · 2026</p></div>
    </article>
    <article class="plx-07__card" style="--depth: 10">
      <img class="plx-07__art" src="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=900&auto=format&fit=crop" alt="Two white watches laid out on a pale surface" loading="lazy" decoding="async">
      <div class="plx-07__label"><h2 class="plx-07__h2">Kettle &amp; Co.</h2><p class="plx-07__meta">Packaging</p></div>
    </article>
    <article class="plx-07__card plx-07__card--wide" style="--depth: 22">
      <img class="plx-07__art" src="https://images.unsplash.com/photo-1483729558449-99ef09a8c325?w=1400&auto=format&fit=crop" alt="Coastal city seen from a hillside at dusk" loading="lazy" decoding="async">
      <div class="plx-07__label"><h2 class="plx-07__h2">Meridian Festival</h2><p class="plx-07__meta">Campaign · with Priya Sharma</p></div>
    </article>
    <article class="plx-07__card" style="--depth: 8">
      <img class="plx-07__art" src="https://images.unsplash.com/photo-1518005020951-eccb494ad742?w=900&auto=format&fit=crop" alt="Curved glass facade against daylight" loading="lazy" decoding="async">
      <div class="plx-07__label"><h2 class="plx-07__h2">Fold Studio</h2><p class="plx-07__meta">Web</p></div>
    </article>
    <article class="plx-07__card" style="--depth: 14">
      <img class="plx-07__art" src="https://images.unsplash.com/photo-1524678606370-a47ad25cb82a?w=900&auto=format&fit=crop" alt="Pastel headphones on a two-tone background" loading="lazy" decoding="async">
      <div class="plx-07__label"><h2 class="plx-07__h2">Postcard Radio</h2><p class="plx-07__meta">Sound &amp; motion</p></div>
    </article>
    <article class="plx-07__card plx-07__card--wide" style="--depth: 18">
      <img class="plx-07__art" src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=1400&auto=format&fit=crop" alt="Tall conifers in flat forest light" loading="lazy" decoding="async">
      <div class="plx-07__label"><h2 class="plx-07__h2">Almanac 2027</h2><p class="plx-07__meta">Editorial · 268 pages</p></div>
    </article>
  </div>
  <footer class="plx-07__foot"><p>Enquiries: [email protected] · Board updated monthly by Jordan Lee</p></footer>
</div>
```
## CSS
```css
.plx-07 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --font-display: "SF Pro Rounded", ui-rounded, "Nunito", "Trebuchet MS", system-ui, sans-serif;
  --font-body: system-ui, -apple-system, "Segoe UI", sans-serif;
  --ink: #2b1c33;
  --muted: #6f5a78;
  --card: #fffdfb;
  --mx: 0;
  --my: 0;
  background: linear-gradient(168deg, #ffe6cf 0%, #ffd2d8 42%, #e2d3ff 100%);
  color: var(--ink);
  font-family: var(--font-body);
  padding: clamp(26px, 5vw, 72px) clamp(16px, 4vw, 56px) 120px;
  overflow-x: clip;
}

.plx-07 * {
  box-sizing: border-box;
}

.plx-07__head {
  max-inline-size: 44rem;
  margin-bottom: clamp(26px, 5vw, 52px);
}

.plx-07__eyebrow {
  margin: 0 0 14px;
  font: 700 10px/1 var(--font-body);
  letter-spacing: 0.26em;
  text-transform: uppercase;
  color: #a2568a;
}

.plx-07__h1 {
  margin: 0 0 14px;
  font-family: var(--font-display);
  font-size: clamp(30px, 6.4vw, 58px);
  font-weight: 700;
  line-height: 1.02;
  letter-spacing: -0.03em;
}

.plx-07__lede {
  margin: 0;
  max-inline-size: 32rem;
  font-size: clamp(15px, 3.2vw, 17px);
  line-height: 1.62;
  color: var(--muted);
  text-wrap: pretty;
}

.plx-07__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr));
  gap: clamp(14px, 2.4vw, 22px);
}

.plx-07__card {
  position: relative;
  min-inline-size: 0;
  min-block-size: 240px;
  border-radius: 20px;
  overflow: clip;
  background: var(--card);
  box-shadow: 0 14px 0 -6px rgba(80,40,90,0.14), 0 26px 44px -28px rgba(60,20,70,0.55);
  display: flex;
  align-items: flex-end;
  padding: 18px;
}

.plx-07__art {
  position: absolute;
  inset: -8%;
  inline-size: 116%;
  block-size: 116%;
  object-fit: cover;
  background: #efe4dc;
  will-change: transform;
}

.plx-07__label {
  position: relative;
  z-index: 2;
  min-inline-size: 0;
  padding: 12px 14px;
  border-radius: 14px;
  background: rgba(255,253,251,0.9);
  will-change: transform;
}

.plx-07__h2 {
  margin: 0 0 4px;
  font-family: var(--font-display);
  font-size: clamp(16px, 2.4vw, 21px);
  font-weight: 700;
  letter-spacing: -0.015em;
}

.plx-07__meta {
  margin: 0;
  font-size: 12.5px;
  line-height: 1.4;
  color: var(--muted);
}

.plx-07__card--tall {
  min-block-size: 380px;
}

.plx-07__foot {
  margin-top: clamp(30px, 5vw, 56px);
  font-size: 13px;
  color: var(--muted);
}

.plx-07__foot p {
  margin: 0;
}

@media (min-width: 900px) {
  .plx-07__grid {
    grid-template-columns: repeat(4, 1fr);
    grid-auto-rows: 200px;
  }

  .plx-07__card {
    min-block-size: 0;
  }

  .plx-07__card--tall {
    grid-row: span 2;
  }

  .plx-07__card--wide {
    grid-column: span 2;
  }
}

@media (pointer: fine) {
  .plx-07__art {
    transform: translate3d(calc(var(--mx) * var(--depth) * 1px), calc(var(--my) * var(--depth) * 1px), 0) scale(1.06);
  }

  .plx-07__label {
    transform: translate3d(calc(var(--mx) * var(--depth) * -0.35px), calc(var(--my) * var(--depth) * -0.35px), 0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .plx-07__art,
    .plx-07__label {
    transform: none !important;
    will-change: auto;
  }
}
```

## JavaScript
```js
const grid = document.getElementById('plx-07-grid');
if (grid && matchMedia('(pointer: fine)').matches) {
  let queued = false, nx = 0, ny = 0;
  const write = () => {
    grid.style.setProperty('--mx', nx.toFixed(3));
    grid.style.setProperty('--my', ny.toFixed(3));
    queued = false;
  };
  grid.addEventListener('pointermove', (e) => {
    const r = grid.getBoundingClientRect();
    nx = (e.clientX - r.left) / r.width - 0.5;
    ny = (e.clientY - r.top) / r.height - 0.5;
    if (!queued) { queued = true; requestAnimationFrame(write); }
  });
  grid.addEventListener('pointerleave', () => { nx = 0; ny = 0; requestAnimationFrame(write); });
}
```
