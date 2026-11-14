---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-text-decryption-animation/"
title: "CSS Holographic Foil Text Reflection Animation"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Trading-card foil for the web: a tiltable membership card whose holo lettering re-angles its iridescence to the pointer (gradient position + card rotation…"
has_js: "true"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Holographic Foil Text Reflection Animation
Source: https://codefronts.com/motion/css-text-animations/css-text-decryption-animation/

Trading-card foil for the web: a tiltable membership card whose holo lettering re-angles its iridescence to the pointer (gradient position + card rotation from two custom properties), and an ambient oil-slick wordmark cycling pastel interference colors with a passing reflection — no JS.
## HTML
```html
<div class="cat-29-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-29a" aria-label="Holographic card tilting with the cursor">
  <div class="cat-29a__scene" id="cat-29a">
    <div class="cat-29a__card">
      <span class="cat-29a__glare" aria-hidden="true"></span>
      <p class="cat-29a__brand">CODEFRONTS</p>
      <h1 class="cat-29a__holo">HOLO&nbsp;MEMBER</h1>
      <div class="cat-29a__row"><span class="cat-29a__chip" aria-hidden="true"></span><p class="cat-29a__num">2027 · 0042 · FOIL</p></div>
    </div>
    <p class="cat-29a__hint" aria-hidden="true">move across the card — the rainbow slides against the tilt</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:[email protected]&display=swap" rel="stylesheet">
<section class="cat-29b" aria-label="Iridescent holographic wordmark">
  <div class="cat-29b__stage">
    <h1 class="cat-29b__word">HOLOGRAM</h1>
    <p class="cat-29b__sub" aria-hidden="true">interference pastels cycle · a reflection band passes</p>
  </div>
</section>
</div>
```
## CSS
```css
.cat-29-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-29-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-29a,
.cat-29a *,
.cat-29a *::before,
.cat-29a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-29a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(110% 90% at 50% 0%,#141824,#0a0c13 70%);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-29a__scene {
  --px: .5;
  --py: .5;
  display: grid;
  gap: 26px;
  justify-items: center;
  perspective: 1000px;
  cursor: crosshair;
}

.cat-29a__card {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  width: min(430px,86vw);
  aspect-ratio: 8/5;
  border-radius: 20px;
  padding: 26px 28px;
  display: grid;
  align-content: space-between;
  background: linear-gradient(155deg,#1b202e,#12151f 60%);
  border: 1px solid rgba(180,200,255,.16);
  box-shadow: 0 50px 90px -40px rgb(0 0 0/.9),inset 0 1px 0 rgba(255,255,255,.08);
  transform: rotateX(calc((var(--py) - .5)*-16deg)) rotateY(calc((var(--px) - .5)*20deg));
  transition: transform .18s ease-out;
}

.cat-29a__scene:hover .cat-29a__card {
  transition: transform .06s linear;
}

.cat-29a__glare {
  position: absolute;
  inset: 0;
  background: radial-gradient(60% 60% at calc(var(--px)*100%) calc(var(--py)*100%),rgba(255,255,255,.16),transparent 70%);
  z-index: 1;
  pointer-events: none;
}

.cat-29a__brand {
  font-size: 11px;
  letter-spacing: .42em;
  color: rgba(210,220,245,.55);
}

.cat-29a__holo {
  font-size: clamp(26px,5.6vw,40px);
  font-weight: 700;
  letter-spacing: .06em;
  background: linear-gradient(110deg,#ff9de0,#ffd88a 18%,#a4ffd0 38%,#8ad4ff 56%,#c3a0ff 76%,#ff9de0 94%) calc(var(--px)*100%) calc(var(--py)*100%)/300% 300%;
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  filter: drop-shadow(0 2px 10px rgb(160 140 255/.35));
}

.cat-29a__row {
  display: flex;
  align-items: center;
  gap: 14px;
}

.cat-29a__chip {
  width: 38px;
  height: 28px;
  border-radius: 6px;
  background: linear-gradient(140deg,#e8c877,#a8842e);
  box-shadow: inset 0 0 0 1px rgb(60 40 0/.35),inset 0 6px 0 rgb(255 255 255/.18);
}

.cat-29a__num {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 13px;
  letter-spacing: .22em;
  color: rgba(220,228,248,.75);
}

.cat-29a__hint {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .16em;
  color: rgba(180,195,230,.38);
}

@media (prefers-reduced-motion: reduce) {
  .cat-29a__card {
    transform: none;
    transition: none;
  }
}

@property --cat29b-h {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.cat-29b,
.cat-29b *,
.cat-29b *::before,
.cat-29b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-29b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0c0b11;
}

.cat-29b__stage {
  text-align: center;
}

.cat-29b__word {
  font-family: 'Unbounded','Segoe UI',system-ui,sans-serif;
  font-size: clamp(34px,7vw,92px);
  font-weight: 700;
  letter-spacing: .04em;
  background: linear-gradient(115deg,transparent 40%,rgba(255,255,255,.85) 50%,transparent 60%) -200% 0/250% 100% no-repeat,linear-gradient(110deg,oklch(0.85 0.09 var(--cat29b-h)),oklch(0.87 0.1 calc(var(--cat29b-h) + 70deg)) 30%,oklch(0.84 0.11 calc(var(--cat29b-h) + 150deg)) 55%,oklch(0.86 0.09 calc(var(--cat29b-h) + 230deg)) 80%,oklch(0.85 0.09 calc(var(--cat29b-h) + 320deg)));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  animation: cat-29b-cycle 9s linear infinite,cat-29b-flash 5.5s ease-in-out 1.2s infinite;
  filter: drop-shadow(0 6px 30px rgb(150 130 255/.3));
}

.cat-29b__sub {
  margin-top: 20px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .16em;
  color: rgba(200,200,235,.4);
}

@keyframes cat-29b-cycle {
  to {
    --cat29b-h: 360deg;
  }
}

@keyframes cat-29b-flash {
  0% {
    background-position: -200% 0,0 0;
  }

  45%,
    100% {
    background-position: 200% 0,0 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-29b__word {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const scene = document.querySelector('#cat-29a'); if (!scene) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  let raf = 0;
  scene.addEventListener('pointermove', (e) => {
    const card = scene.querySelector('.cat-29a__card');
    const r = card.getBoundingClientRect();
    const px = Math.min(1, Math.max(0, (e.clientX - r.left) / r.width));
    const py = Math.min(1, Math.max(0, (e.clientY - r.top) / r.height));
    cancelAnimationFrame(raf);
    raf = requestAnimationFrame(() => {
      scene.style.setProperty('--px', px.toFixed(3));
      scene.style.setProperty('--py', py.toFixed(3));
    });
  });
  scene.addEventListener('pointerleave', () => {
    scene.style.setProperty('--px', 0.5);
    scene.style.setProperty('--py', 0.5);
  });
})();

/* No JavaScript — pastel interference stops derive from one @property hue that cycles 360°, while a diagonal reflection band sweeps on its own keyframe. */
```
