---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-card-with-hover-refraction/"
title: "Liquid Glass Card with Hover Refraction"
section: "design-styles"
category: "css-liquid-glass-effects"
category_name: "CSS Liquid Glass Effects"
description: "The premium replacement for flat product / dashboard cards: a translucent glass panel floats over a photographic background, and on hover a specular gloss…"
has_js: "true"
---

Here's a working CSS Liquid Glass Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Glass Card with Hover Refraction
Source: https://codefronts.com/design-styles/css-liquid-glass-effects/liquid-glass-card-with-hover-refraction/

The premium replacement for flat product / dashboard cards: a translucent glass panel floats over a photographic background, and on hover a specular gloss highlight tracks the cursor while the whole card tilts in 3D — so the light appears to refract through real glass instead of just blurring what's behind it.
## HTML
```html
<section class="lg-01" aria-label="Liquid glass card with hover refraction">
  <article class="lg-01__card" id="lg-01-card" tabindex="0">
    <div class="lg-01__badge">New</div>
    <div class="lg-01__spec" aria-hidden="true"></div>
    <h3 class="lg-01__title">Aurora Headphones</h3>
    <p class="lg-01__body">Spatial audio, 40-hour battery, and a machined-glass shell that catches the light like the UI around it.</p>
    <div class="lg-01__foot"><span class="lg-01__price">$299</span><span class="lg-01__cta">View →</span></div>
  </article>
</section>
```
## CSS
```css
.lg-01,
.lg-01 *,
.lg-01 *::before,
.lg-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.lg-01 {
  --tint: color-mix(in oklab,white 12%,transparent);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  perspective: 1100px;
  background: url('https://picsum.photos/seed/lgcard/1200/900') center/cover fixed,#1a1330;
}

.lg-01__card {
  position: relative;
  isolation: isolate;
  width: min(340px,90vw);
  padding: 26px 26px 22px;
  border-radius: 26px;
  color: #fff;
  transform: rotateX(var(--ry,0deg)) rotateY(var(--rx,0deg));
  transform-style: preserve-3d;
  background: var(--tint);
  border: 1px solid rgba(255,255,255,.35);
  box-shadow: 0 30px 60px -30px rgba(0,0,0,.65),inset 0 1px 0 rgba(255,255,255,.5);
  backdrop-filter: blur(18px) saturate(180%);
  -webkit-backdrop-filter: blur(18px) saturate(180%);
  transition: transform .5s cubic-bezier(.2,.9,.2,1),box-shadow .4s;
  cursor: pointer;
  overflow: hidden;
}

.lg-01__card::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: radial-gradient(220px 220px at var(--mx,30%) var(--my,20%),rgba(255,255,255,.55),rgba(255,255,255,0) 60%);
  opacity: var(--gloss,.5);
  transition: opacity .3s;
  pointer-events: none;
  z-index: 2;
}

.lg-01__spec {
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: linear-gradient(120deg,transparent 30%,rgba(255,255,255,.18) 46%,transparent 62%);
  pointer-events: none;
  z-index: 1;
}

.lg-01__badge {
  position: relative;
  z-index: 3;
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  padding: 5px 11px;
  border-radius: 999px;
  background: rgba(255,255,255,.22);
  border: 1px solid rgba(255,255,255,.4);
}

.lg-01__title {
  position: relative;
  z-index: 3;
  font-size: 24px;
  font-weight: 800;
  letter-spacing: -.02em;
  margin: 64px 0 8px;
}

.lg-01__body {
  position: relative;
  z-index: 3;
  font-size: 14px;
  line-height: 1.6;
  color: rgba(255,255,255,.9);
  text-shadow: 0 1px 8px rgba(0,0,0,.35);
}

.lg-01__foot {
  position: relative;
  z-index: 3;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 20px;
}

.lg-01__price {
  font-size: 22px;
  font-weight: 800;
}

.lg-01__cta {
  font-size: 14px;
  font-weight: 600;
  padding: 8px 16px;
  border-radius: 999px;
  background: rgba(255,255,255,.9);
  color: #1a1330;
}

.lg-01__card:hover,
.lg-01__card:focus-visible {
  box-shadow: 0 40px 80px -28px rgba(0,0,0,.7),inset 0 1px 0 rgba(255,255,255,.6);
}

.lg-01__card:focus-visible {
  outline: 3px solid rgba(255,255,255,.9);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .lg-01__card {
    transition: box-shadow .2s;
  }

  .lg-01__spec {
    display: none;
  }
}
```

## JavaScript
```js
(() => {
  const card = document.querySelector('#lg-01-card');
  if (!card) return;
  const MAX_TILT = 8;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  card.addEventListener('pointermove', e => {
    const r = card.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width;
    const py = (e.clientY - r.top) / r.height;
    card.style.setProperty('--mx', (px*100).toFixed(1) + '%');
    card.style.setProperty('--my', (py*100).toFixed(1) + '%');
    card.style.setProperty('--gloss', '.85');
    if (!reduce){
      card.style.setProperty('--rx', ((px-.5)*MAX_TILT*2).toFixed(2) + 'deg');
      card.style.setProperty('--ry', (-(py-.5)*MAX_TILT*2).toFixed(2) + 'deg');
    }
  });
  card.addEventListener('pointerleave', () => {
    card.style.setProperty('--gloss', '.5');
    card.style.setProperty('--rx', '0deg');
    card.style.setProperty('--ry', '0deg');
  });
})();
```
