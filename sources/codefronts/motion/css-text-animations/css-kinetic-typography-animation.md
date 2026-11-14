---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-kinetic-typography-animation/"
title: "CSS Spotlight Text Reveal Mask"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Light as an interface: a cursor-held torch whose radial mask uncovers a hidden message (radius eased open by a registered @property), and a self-panning beam…"
has_js: "true"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Spotlight Text Reveal Mask
Source: https://codefronts.com/motion/css-text-animations/css-kinetic-typography-animation/

Light as an interface: a cursor-held torch whose radial mask uncovers a hidden message (radius eased open by a registered @property), and a self-panning beam that sweeps a headline forever with zero JavaScript — both keep a faint base layer so the copy is never truly invisible.
## HTML
```html
<div class="cat-26-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-26a" aria-label="Spotlight follows the cursor to reveal text">
  <div class="cat-26a__stage" id="cat-26a">
    <p class="cat-26a__msg cat-26a__msg--base">Some things only appear when you look for them.</p>
    <p class="cat-26a__msg cat-26a__msg--lit" aria-hidden="true">Some things only appear when you look for them.</p>
    <p class="cat-26a__hint" aria-hidden="true">move your cursor across the dark</p>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Archivo:ital,wght@0,500..900;1,500..900&display=swap" rel="stylesheet">
<section class="cat-26b" aria-label="Beam pans across hidden headline">
  <div class="cat-26b__stage">
    <h1 class="cat-26b__word cat-26b__word--base">HIDDEN IN PLAIN SIGHT</h1>
    <h1 class="cat-26b__word cat-26b__word--lit" aria-hidden="true">HIDDEN IN PLAIN SIGHT</h1>
  </div>
</section>
</div>
```
## CSS
```css
.cat-26-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-26-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

@property --cat26a-r {
  syntax: '<length>';
  initial-value: 0px;
  inherits: true;
}

.cat-26a,
.cat-26a *,
.cat-26a *::before,
.cat-26a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-26a {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #08090c;
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-26a__stage {
  position: relative;
  width: min(860px,100%);
  padding: 110px clamp(28px,7vw,90px);
  cursor: crosshair;
  --cat26a-r: 0px;
  --mx: 50%;
  --my: 50%;
}

.cat-26a__stage:hover {
  --cat26a-r: 190px;
}

.cat-26a__msg {
  font-size: clamp(28px,4.6vw,52px);
  font-weight: 600;
  line-height: 1.3;
  letter-spacing: -.015em;
  text-align: center;
  text-wrap: balance;
}

.cat-26a__msg--base {
  color: rgba(226,232,245,.1);
}

.cat-26a__msg--lit {
  position: absolute;
  inset: 110px clamp(28px,7vw,90px);
  display: grid;
  align-content: center;
  color: #f2f5fc;
  text-shadow: 0 0 30px rgba(160,190,255,.35);
  -webkit-mask-image: radial-gradient(circle var(--cat26a-r) at var(--mx) var(--my),#000 34%,transparent 78%);
  mask-image: radial-gradient(circle var(--cat26a-r) at var(--mx) var(--my),#000 34%,transparent 78%);
  transition: --cat26a-r .5s cubic-bezier(.2,.8,.3,1);
  pointer-events: none;
}

.cat-26a__hint {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 34px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .2em;
  text-align: center;
  color: rgba(190,205,235,.3);
}

@media (prefers-reduced-motion: reduce) {
  .cat-26a__msg--base {
    color: rgba(226,232,245,.85);
  }

  .cat-26a__msg--lit {
    display: none;
  }
}

@property --cat26b-x {
  syntax: '<percentage>';
  initial-value: 8%;
  inherits: true;
}

.cat-26b,
.cat-26b *,
.cat-26b *::before,
.cat-26b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-26b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #0b0a08;
  font-family: 'Archivo','Segoe UI',system-ui,sans-serif;
}

.cat-26b__stage {
  position: relative;
  text-align: center;
  --cat26b-x: 8%;
  animation: cat-26b-pan 7s ease-in-out infinite alternate;
}

.cat-26b__word {
  font-size: clamp(34px,6.4vw,84px);
  font-weight: 900;
  line-height: 1.06;
  letter-spacing: .01em;
  max-width: 12ch;
  text-wrap: balance;
}

.cat-26b__word--base {
  color: rgba(240,230,205,.09);
}

.cat-26b__word--lit {
  position: absolute;
  inset: 0;
  color: oklch(0.92 0.08 90);
  text-shadow: 0 0 34px rgba(255,220,140,.3);
  -webkit-mask-image: radial-gradient(46% 130% at var(--cat26b-x) 50%,#000 26%,transparent 66%);
  mask-image: radial-gradient(46% 130% at var(--cat26b-x) 50%,#000 26%,transparent 66%);
}

@keyframes cat-26b-pan {
  to {
    --cat26b-x: 92%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cat-26b__stage {
    animation: none;
  }

  .cat-26b__word--base {
    color: rgba(240,230,205,.75);
  }

  .cat-26b__word--lit {
    display: none;
  }
}
```

## JavaScript
```js
(() => {
  const stage = document.querySelector('#cat-26a'); if (!stage) return;
  stage.addEventListener('pointermove', (e) => {
    const r = stage.getBoundingClientRect();
    stage.style.setProperty('--mx', (e.clientX - r.left) + 'px');
    stage.style.setProperty('--my', (e.clientY - r.top) + 'px');
  });
})();

/* No JavaScript — the mask's focal X is a registered percentage animated 8%→92% and back; the faint base copy keeps the headline readable at all times. */
```
