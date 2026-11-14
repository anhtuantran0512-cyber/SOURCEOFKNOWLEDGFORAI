---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-animations/css-perspective-text-rotation-animation/"
title: "CSS Perspective Text Tilt on Mousemove"
section: "motion"
category: "css-text-animations"
category_name: "CSS Text Animations"
description: "Hero type that leans with the cursor: a JS pointer-tracked tilt with true depth layers (a shadow plane and a floating chip at different translateZ), and a…"
has_js: "true"
---

Here's a working CSS Text Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Perspective Text Tilt on Mousemove
Source: https://codefronts.com/motion/css-text-animations/css-perspective-text-rotation-animation/

Hero type that leans with the cursor: a JS pointer-tracked tilt with true depth layers (a shadow plane and a floating chip at different translateZ), and a no-JS version steered by nine invisible hover zones and :has().
## HTML
```html
<div class="cat-18-group">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-18a" aria-label="Perspective tilt hero tracking the cursor">
  <div class="cat-18a__scene" id="cat-18a">
    <div class="cat-18a__group">
      <span class="cat-18a__ghost" aria-hidden="true">DEPTH OF FIELD</span>
      <h1 class="cat-18a__title">DEPTH OF FIELD</h1>
      <span class="cat-18a__chip" aria-hidden="true">✦ hover to tilt</span>
    </div>
  </div>
</section>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:[email protected]&display=swap" rel="stylesheet">
<section class="cat-18b" aria-label="Pure CSS hover zone tilt">
  <div class="cat-18b__stage">
    <div class="cat-18b__zones" aria-hidden="true"><i class="z1"></i><i class="z2"></i><i class="z3"></i><i class="z4"></i><i class="z5"></i><i class="z6"></i><i class="z7"></i><i class="z8"></i><i class="z9"></i></div>
    <h1 class="cat-18b__title">PARALLAX<em>zero javascript — 9 hover zones + :has()</em></h1>
  </div>
</section>
</div>
```
## CSS
```css
.cat-18-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  width: 100%;
}

.cat-18-group > section {
  flex: 1 1 480px;
  min-width: min(100%,360px);
}

.cat-18a,
.cat-18a *,
.cat-18a *::before,
.cat-18a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-18a {
  --px: 0;
  --py: 0;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(100% 90% at 50% 15%,#1a1f2c,#0b0d13 70%);
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-18a__scene {
  perspective: 950px;
  padding: 70px clamp(20px,6vw,90px);
  cursor: crosshair;
}

.cat-18a__group {
  position: relative;
  transform-style: preserve-3d;
  transform: rotateX(calc(var(--py)*-14deg)) rotateY(calc(var(--px)*18deg));
  transition: transform .5s cubic-bezier(.16,.84,.3,1);
}

.cat-18a__title {
  position: relative;
  font-size: clamp(34px,6.4vw,80px);
  font-weight: 700;
  letter-spacing: .01em;
  color: #eef3fc;
  text-wrap: balance;
  text-align: center;
  transform: translateZ(30px);
}

.cat-18a__ghost {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  font-size: clamp(34px,6.4vw,80px);
  font-weight: 700;
  letter-spacing: .01em;
  color: oklch(0.55 0.2 275/.35);
  filter: blur(10px);
  transform: translateZ(-60px) scale(1.02);
  text-align: center;
}

.cat-18a__chip {
  position: absolute;
  top: -2.2em;
  right: -1em;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .12em;
  color: #0b0d13;
  background: oklch(0.85 0.15 165);
  padding: 7px 13px;
  border-radius: 999px;
  transform: translateZ(70px);
  box-shadow: 0 14px 30px -12px oklch(0.85 0.15 165/.5);
}

@media (prefers-reduced-motion: reduce) {
  .cat-18a__group {
    transform: none;
    transition: none;
  }
}

.cat-18b,
.cat-18b *,
.cat-18b *::before,
.cat-18b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cat-18b {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #12100c;
  font-family: 'Space Grotesk','Segoe UI',system-ui,sans-serif;
}

.cat-18b__stage {
  position: relative;
  perspective: 900px;
  padding: 80px clamp(24px,7vw,110px);
}

.cat-18b__zones {
  position: absolute;
  inset: 0;
  display: grid;
  grid-template: repeat(3,1fr)/repeat(3,1fr);
  z-index: 2;
}

.cat-18b__zones i {
  cursor: crosshair;
}

.cat-18b__title {
  display: grid;
  gap: 14px;
  justify-items: center;
  font-size: clamp(38px,7.4vw,92px);
  font-weight: 700;
  letter-spacing: .04em;
  color: oklch(0.88 0.14 85);
  text-shadow: 0 24px 50px rgb(0 0 0/.55);
  transition: transform .45s cubic-bezier(.2,.8,.2,1);
  transform-style: preserve-3d;
}

.cat-18b__title em {
  font-style: normal;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 11px;
  letter-spacing: .18em;
  color: rgba(235,215,170,.45);
}

.cat-18b__stage:has(.z1:hover) .cat-18b__title {
  transform: rotateX(11deg) rotateY(-13deg);
}

.cat-18b__stage:has(.z2:hover) .cat-18b__title {
  transform: rotateX(13deg);
}

.cat-18b__stage:has(.z3:hover) .cat-18b__title {
  transform: rotateX(11deg) rotateY(13deg);
}

.cat-18b__stage:has(.z4:hover) .cat-18b__title {
  transform: rotateY(-14deg);
}

.cat-18b__stage:has(.z5:hover) .cat-18b__title {
  transform: translateZ(30px);
}

.cat-18b__stage:has(.z6:hover) .cat-18b__title {
  transform: rotateY(14deg);
}

.cat-18b__stage:has(.z7:hover) .cat-18b__title {
  transform: rotateX(-11deg) rotateY(-13deg);
}

.cat-18b__stage:has(.z8:hover) .cat-18b__title {
  transform: rotateX(-13deg);
}

.cat-18b__stage:has(.z9:hover) .cat-18b__title {
  transform: rotateX(-11deg) rotateY(13deg);
}

@media (prefers-reduced-motion: reduce) {
  .cat-18b__title {
    transition: none;
  }

  .cat-18b__stage:has(i:hover) .cat-18b__title {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const scene = document.querySelector('#cat-18a'); if (!scene) return;
  const host = scene.closest('.cat-18a') || scene;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  let raf = 0;
  scene.addEventListener('pointermove', (e) => {
    const r = scene.getBoundingClientRect();
    const px = (e.clientX - r.left) / r.width - 0.5;
    const py = (e.clientY - r.top) / r.height - 0.5;
    cancelAnimationFrame(raf);
    raf = requestAnimationFrame(() => {
      host.style.setProperty('--px', px.toFixed(3));
      host.style.setProperty('--py', py.toFixed(3));
    });
  });
  scene.addEventListener('pointerleave', () => {
    host.style.setProperty('--px', 0);
    host.style.setProperty('--py', 0);
  });
})();

/* No JavaScript — an invisible 3×3 grid overlays the stage; nine :has(.zN:hover) rules aim the headline at fixed rotateX/rotateY angles. */
```
