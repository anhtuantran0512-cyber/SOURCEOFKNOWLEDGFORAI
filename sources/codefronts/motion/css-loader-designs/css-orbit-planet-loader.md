---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-orbit-planet-loader/"
title: "CSS Orbit Planet Loader"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Three space-themed CSS loaders — a multi-orbit solar system, a conic-gradient comet trail, and binary orbiting stars — evoking astronomy dashboards and data…"
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Orbit Planet Loader
Source: https://codefronts.com/motion/css-loader-designs/css-orbit-planet-loader/

Three space-themed CSS loaders — a multi-orbit solar system, a conic-gradient comet trail, and binary orbiting stars — evoking astronomy dashboards and data pipeline visualisations.
## HTML
```html
<div class="ld-15">
  <div class="ld-15__stage">
    <div class="ld-15__cell">
      <div class="ld-15__solar">
        <div class="ld-15__sun"></div>
        <div class="ld-15__orbit-ring"><div class="ld-15__planet"></div></div>
```
## CSS
```css
.ld-15,
.ld-15 *,
.ld-15 *::before,
.ld-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-15 {
  --bg: #01020a;
  --c1: #4fc3f7;
  --c2: #f48fb1;
  --c3: #a5d6a7;
  --c4: #ffe082;
  --c5: #cf94da;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Segoe UI',sans-serif;
}

.ld-15__stage {
  display: flex;
  gap: 80px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 40px;
  align-items: center;
}

.ld-15__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
}

.ld-15__label {
  color: rgba(255,255,255,.3);
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}
/* Multi-orbit solar */

.ld-15__solar {
  width: 120px;
  height: 120px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ld-15__sun {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: var(--c4);
  box-shadow: 0 0 16px var(--c4),0 0 32px rgba(255,224,130,.3);
}

.ld-15__orbit-ring {
  position: absolute;
  border-radius: 50%;
  border: 1px solid rgba(255,255,255,.08);
}

.ld-15__orbit-ring:nth-child(2) {
  width: 44px;
  height: 44px;
  animation: ld-15-orbit 1.2s linear infinite;
}

.ld-15__orbit-ring:nth-child(3) {
  width: 72px;
  height: 72px;
  animation: ld-15-orbit 2s linear infinite;
}

.ld-15__orbit-ring:nth-child(4) {
  width: 100px;
  height: 100px;
  animation: ld-15-orbit 3s linear infinite;
}

.ld-15__planet {
  position: absolute;
  border-radius: 50%;
  top: -5px;
  left: 50%;
  transform: translateX(-50%);
}

.ld-15__orbit-ring:nth-child(2) .ld-15__planet {
  width: 8px;
  height: 8px;
  background: var(--c1);
  box-shadow: 0 0 6px var(--c1);
}

.ld-15__orbit-ring:nth-child(3) .ld-15__planet {
  width: 10px;
  height: 10px;
  background: var(--c2);
  box-shadow: 0 0 8px var(--c2);
}

.ld-15__orbit-ring:nth-child(4) .ld-15__planet {
  width: 7px;
  height: 7px;
  background: var(--c3);
  box-shadow: 0 0 6px var(--c3);
}

@keyframes ld-15-orbit {
  to {
    transform: rotate(360deg);
  }
}
/* Comet orbit */

.ld-15__comet-orbit {
  width: 90px;
  height: 90px;
  position: relative;
}

.ld-15__comet-orbit::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 1px solid rgba(255,255,255,.06);
}

.ld-15__comet-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--c5);
  box-shadow: 0 0 10px var(--c5);
  position: absolute;
  top: -5px;
  left: 50%;
  transform: translateX(-50%);
  transform-origin: 45px 50px;
  animation: ld-15-orbit 1.8s linear infinite;
}

.ld-15__comet-trail {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  background: conic-gradient(transparent 75%,rgba(207,148,218,.3));
  animation: ld-15-orbit 1.8s linear infinite;
  -webkit-mask: radial-gradient(farthest-side,#0000 calc(100% - 2px),#000 0);
}
/* Binary stars */

.ld-15__binary {
  width: 90px;
  height: 90px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ld-15__binary-wrap {
  width: 60px;
  height: 60px;
  position: relative;
  animation: ld-15-orbit 2s linear infinite;
}

.ld-15__star {
  position: absolute;
  border-radius: 50%;
  top: 50%;
  transform: translateY(-50%);
}

.ld-15__star:nth-child(1) {
  left: 0;
  width: 14px;
  height: 14px;
  background: var(--c4);
  box-shadow: 0 0 10px var(--c4);
  margin-top: -7px;
}

.ld-15__star:nth-child(2) {
  right: 0;
  width: 10px;
  height: 10px;
  background: var(--c1);
  box-shadow: 0 0 8px var(--c1);
  margin-top: -5px;
}

@media (prefers-reduced-motion: reduce) {
  .ld-15__orbit-ring,
    .ld-15__comet-dot,
    .ld-15__comet-trail,
    .ld-15__binary-wrap {
    animation: none;
  }
}
```
