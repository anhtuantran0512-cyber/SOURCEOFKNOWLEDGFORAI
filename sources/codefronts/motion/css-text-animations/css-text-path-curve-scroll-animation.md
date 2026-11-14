---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-text-path-curve-scroll-animation/"
title: "CSS Text Path Curve Scroll Animation"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Typography that rides geometry: a sentence surfing a rolling hill whose position is scrubbed by scroll (SVG textPath + 10 lines of JS), and a zero-JS…"
has_js: "true"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Text Path Curve Scroll Animation
Source: https://codefronts.com/motion/css-text-animations/css-text-path-curve-scroll-animation/

Typography that rides geometry: a sentence surfing a rolling hill whose position is scrubbed by scroll (SVG textPath + 10 lines of JS), and a zero-JS orbiting badge — circular text on a path, spun forever by one CSS rotation.
## HTML
```html
<div class="cat-04-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-04a" aria-label="Text rides a curved path while scrolling" id="cat-04a">
  <div class="cat-04a__pin">
    <p class="cat-04a__hint" aria-hidden="true">scroll — the sentence surfs the curve</p>
    <svg class="cat-04a__svg" viewBox="0 0 1000 420" role="img" aria-label="The scenic route to better typography">
      <path id="cat-04a-path" d="M -80 330 C 160 330 220 120 420 120 S 700 330 900 330 S 1180 140 1280 140" fill="none" stroke="rgba(60,80,120,.25)" stroke-width="1.5" stroke-dasharray="7 9"></path>
      <text class="cat-04a__text"><textPath id="cat-04a-tp" href="#cat-04a-path" startOffset="90%">✦ the scenic route to better typography ✦</textPath></text>
    </svg>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-04b" aria-label="Rotating circular text badge">
  <div class="cat-04b__stage">
    <div class="cat-04b__badge" role="img" aria-label="CSS text effects — Codefronts collection badge">
      <svg class="cat-04b__ring" viewBox="0 0 200 200" aria-hidden="true">
        <path id="cat-04b-circ" d="M 100,100 m -78,0 a 78,78 0 1,1 156,0 a 78,78 0 1,1 -156,0" fill="none"></path>
        <text class="cat-04b__rtext"><textPath href="#cat-04b-circ">★ CSS TEXT EFFECTS ★ CODEFRONTS COLLECTION&nbsp;</textPath></text>
      </svg>
      <span class="cat-04b__core" aria-hidden="true">↗</span>
    </div>
  </div>
</section>
</div>
```
## CSS
```css
.cat-04-group {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.cat-04-group > section {
  width: 100%;
}

.cat-04a,
.cat-04a *,
.cat-04a *::before,
.cat-04a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-04a {
  width: 100%;
  height: 240vh;
  background: linear-gradient(180deg,#eaf1f7,#d9e6f0);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-04a__pin {
  position: sticky;
  top: 0;
  height: 100vh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 10px;
  padding: 48px 24px;
  overflow: hidden;
}

.cat-04a__hint {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .2em;
  color: rgba(40,60,90,.5);
}

.cat-04a__svg {
  width: min(980px,96vw);
  height: auto;
  overflow: visible;
}

.cat-04a__text {
  font-size: 34px;
  font-weight: 600;
  fill: #1d2c44;
  letter-spacing: .06em;
}

@media (prefers-reduced-motion: reduce) {
  .cat-04a__hint {
    visibility: hidden;
  }
}

.cat-04b,
.cat-04b *,
.cat-04b *::before,
.cat-04b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-04b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #12141c;
}

.cat-04b__badge {
  position: relative;
  width: min(300px,70vw);
  aspect-ratio: 1;
  display: grid;
  place-items: center;
}

.cat-04b__ring {
  position: absolute;
  inset: 0;
  animation: cat-04b-spin 22s linear infinite;
}

.cat-04b__badge:hover .cat-04b__ring {
  animation-play-state: paused;
}

.cat-04b__rtext {
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
  font-size: 15.5px;
  font-weight: 600;
  letter-spacing: .32em;
  fill: oklch(0.87 0.13 95);
}

.cat-04b__core {
  display: grid;
  place-items: center;
  width: 38%;
  aspect-ratio: 1;
  border-radius: 50%;
  border: 1.5px solid rgba(240,230,200,.3);
  color: oklch(0.87 0.13 95);
  font-size: 34px;
  animation: cat-04b-spin 22s linear infinite reverse;
}

@keyframes cat-04b-spin {
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-04b__ring,
    .cat-04b__core {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const sec = document.querySelector('#cat-04a');
  const tp = document.querySelector('#cat-04a-tp');
  if (!sec || !tp) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) { tp.setAttribute('startOffset', '32%'); return; }
  let raf = 0;
  const update = () => {
    const r = sec.getBoundingClientRect();
    const total = r.height - innerHeight;
    const p = Math.min(1, Math.max(0, -r.top / total));
    tp.setAttribute('startOffset', (90 - p * 95).toFixed(2) + '%');
  };
  addEventListener('scroll', () => { cancelAnimationFrame(raf); raf = requestAnimationFrame(update); }, { passive: true });
  update();
})();

/* No JavaScript — circular textPath inside an SVG that CSS rotates forever; the center arrow counter-rotates to stay upright, and hover pauses the orbit. */
```
