---
source: "codefronts"
url: "https://codefronts.com/navigation/css-liquid-glass-navbars/cursor-warp-interactive-nav/"
title: "Cursor-Warp Interactive Nav"
section: "navigation"
category: "css-liquid-glass-navbars"
category_name: "CSS Liquid Glass Navbars"
description: "A high-end glass nav where a soft refraction lens follows the cursor across the bar, warping and brightening the frosted surface beneath the pointer — the…"
has_js: "true"
---

Here's a working CSS Liquid Glass Navbar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cursor-Warp Interactive Nav
Source: https://codefronts.com/navigation/css-liquid-glass-navbars/cursor-warp-interactive-nav/

A high-end glass nav where a soft refraction lens follows the cursor across the bar, warping and brightening the frosted surface beneath the pointer — the effect people reach for GSAP to build. Here it's done with lightweight pointer tracking and CSS custom properties; the tailwind/notes show the GSAP quickTo upgrade path.
## HTML
```html
<section class="nb-15" aria-label="Cursor warp interactive glass nav demo">
  <nav class="nb-15__bar" id="nb-15-bar" aria-label="Primary">
    <span class="nb-15__lens" aria-hidden="true"></span>
    <span class="nb-15__brand">◇ Refract</span>
    <div class="nb-15__links">
      <a class="nb-15__link" href="#nb-15" aria-current="page">Work</a>
      <a class="nb-15__link" href="#nb-15">Studio</a>
      <a class="nb-15__link" href="#nb-15">Lab</a>
      <a class="nb-15__link" href="#nb-15">Contact</a>
    </div>
  </nav>
</section>
```
## CSS
```css
.nb-15,
.nb-15 *,
.nb-15 *::before,
.nb-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.nb-15 {
  display: grid;
  place-items: center;
  width: 100%;
  min-height: 100vh;
  padding: 20px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: conic-gradient(from 90deg at 50% 50%,#ff8a00,#e52e71,#7f00ff,#ff8a00);
  background-size: 200% 200%;
  animation: nb-15-bg 22s ease-in-out infinite;
}

@keyframes nb-15-bg {
  50% {
    background-position: 100% 100%;
  }
}

.nb-15__bar {
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  gap: 22px;
  padding: 14px 20px;
  border-radius: 20px;
  isolation: isolate;
  color: #fff;
  background: color-mix(in oklab,white 12%,transparent);
  border: 1px solid rgba(255,255,255,.34);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5),0 22px 46px -24px rgba(0,0,0,.6);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
}

.nb-15__lens {
  position: absolute;
  inset: 0;
  z-index: 0;
  border-radius: inherit;
  pointer-events: none;
  background: radial-gradient(140px 140px at var(--mx,50%) var(--my,50%),rgba(255,255,255,.55),rgba(255,255,255,.12) 40%,transparent 65%);
  opacity: var(--on,0);
  transition: opacity .3s;
}

.nb-15__brand,
.nb-15__links {
  position: relative;
  z-index: 1;
}

.nb-15__brand {
  font-size: 16px;
  font-weight: 800;
}

.nb-15__links {
  display: flex;
  gap: 6px;
}

.nb-15__link {
  min-height: 40px;
  display: flex;
  align-items: center;
  padding: 0 16px;
  border-radius: 12px;
  text-decoration: none;
  color: #fff;
  opacity: .9;
  font-size: 14.5px;
  font-weight: 600;
  transition: background .2s,opacity .2s;
}

.nb-15__link:hover,
.nb-15__link[aria-current] {
  opacity: 1;
  background: rgba(255,255,255,.18);
}

.nb-15__link:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .nb-15,
    .nb-15__lens {
    animation: none;
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const bar = document.querySelector('#nb-15-bar');
  if (!bar) return;
  let tx = 50, ty = 50, cx = 50, cy = 50, raf;
  // GSAP upgrade: const qx = gsap.quickTo(bar,'--mx',{duration:.4,unit:'%'}) ...
  function loop(){
    cx += (tx - cx) * .18; cy += (ty - cy) * .18;
    bar.style.setProperty('--mx', cx.toFixed(1) + '%');
    bar.style.setProperty('--my', cy.toFixed(1) + '%');
    if (Math.abs(tx - cx) > .1 || Math.abs(ty - cy) > .1) raf = requestAnimationFrame(loop); else raf = null;
  }
  bar.addEventListener('pointermove', e => {
    const r = bar.getBoundingClientRect();
    tx = ((e.clientX - r.left) / r.width) * 100;
    ty = ((e.clientY - r.top) / r.height) * 100;
    bar.style.setProperty('--on', '1');
    if (!raf) raf = requestAnimationFrame(loop);
  });
  bar.addEventListener('pointerleave', () => bar.style.setProperty('--on', '0'));
})();
```
