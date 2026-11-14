---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-morphing-square-loader/"
title: "CSS Morphing Square Loader"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Four square-based CSS loaders — a border-radius morph, a corner-orbit rotation, a four-square chase path, and a perspective 3D flip — demonstrating CSS…"
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Morphing Square Loader
Source: https://codefronts.com/motion/css-loader-designs/css-morphing-square-loader/

Four square-based CSS loaders — a border-radius morph, a corner-orbit rotation, a four-square chase path, and a perspective 3D flip — demonstrating CSS shape-shifting and spatial transforms.
## HTML
```html
<div class="ld-14">
  <div class="ld-14__stage">
    <div class="ld-14__cell"><div class="ld-14__morph"></div><span class="ld-14__label">Morphing</span></div>
    <div class="ld-14__cell"><div class="ld-14__sq-orbit"><span></span><span></span><span></span><span></span></div><span class="ld-14__label">Corner Orbit</span></div>
    <div class="ld-14__cell"><div class="ld-14__chase-sq"><span></span><span></span><span></span><span></span></div><span class="ld-14__label">Chase Squares</span></div>
    <div class="ld-14__cell"><div class="ld-14__sq-spin"></div><span class="ld-14__label">3D Flip</span></div>
  </div>
```
## CSS
```css
.ld-14,
.ld-14 *,
.ld-14 *::before,
.ld-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-14 {
  --bg: #1a0533;
  --c1: #d63af9;
  --c2: #7c3aed;
  --c3: #ec4899;
  --c4: #f59e0b;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Segoe UI',sans-serif;
}

.ld-14__stage {
  display: flex;
  gap: 70px;
  flex-wrap: wrap;
  justify-content: center;
  padding: 40px;
  align-items: center;
}

.ld-14__cell {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.ld-14__label {
  color: rgba(255,255,255,.35);
  font-size: 11px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
}
/* Morph shape */

.ld-14__morph {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg,var(--c1),var(--c2));
  animation: ld-14-morph 3s ease-in-out infinite;
}

@keyframes ld-14-morph {
  0% {
    border-radius: 4px;
    transform: rotate(0);
  }

  25% {
    border-radius: 50%;
    transform: rotate(90deg);
  }

  50% {
    border-radius: 4px;
    transform: rotate(180deg);
  }

  75% {
    border-radius: 50% 4px;
    transform: rotate(270deg);
  }

  100% {
    border-radius: 4px;
    transform: rotate(360deg);
  }
}
/* Square orbit */

.ld-14__sq-orbit {
  width: 60px;
  height: 60px;
  position: relative;
  animation: ld-14-orbit 2s linear infinite;
}

.ld-14__sq-orbit span {
  position: absolute;
  width: 14px;
  height: 14px;
  background: var(--c3);
  border-radius: 2px;
}

.ld-14__sq-orbit span:nth-child(1) {
  top: 0;
  left: 0;
}

.ld-14__sq-orbit span:nth-child(2) {
  top: 0;
  right: 0;
  background: var(--c1);
  animation: ld-14-sq-pulse .5s ease-in-out infinite alternate;
}

.ld-14__sq-orbit span:nth-child(3) {
  bottom: 0;
  right: 0;
  background: var(--c4);
}

.ld-14__sq-orbit span:nth-child(4) {
  bottom: 0;
  left: 0;
  background: var(--c2);
}

@keyframes ld-14-orbit {
  to {
    transform: rotate(360deg);
  }
}

@keyframes ld-14-sq-pulse {
  to {
    border-radius: 50%;
  }
}
/* Chase squares */

.ld-14__chase-sq {
  width: 60px;
  height: 60px;
  position: relative;
}

.ld-14__chase-sq span {
  position: absolute;
  width: 20px;
  height: 20px;
  border-radius: 3px;
  animation: ld-14-chase-sq 1.5s ease-in-out infinite;
}

.ld-14__chase-sq span:nth-child(1) {
  background: var(--c1);
  animation-delay: 0s;
}

.ld-14__chase-sq span:nth-child(2) {
  background: var(--c2);
  animation-delay: .375s;
}

.ld-14__chase-sq span:nth-child(3) {
  background: var(--c3);
  animation-delay: .75s;
}

.ld-14__chase-sq span:nth-child(4) {
  background: var(--c4);
  animation-delay: 1.125s;
}

@keyframes ld-14-chase-sq {
  0% {
    transform: translate(0,0);
  }

  25% {
    transform: translate(40px,0);
  }

  50% {
    transform: translate(40px,40px);
  }

  75% {
    transform: translate(0,40px);
  }

  100% {
    transform: translate(0,0);
  }
}
/* Spinner square */

.ld-14__sq-spin {
  width: 44px;
  height: 44px;
  border: 4px solid var(--c4);
  border-radius: 4px;
  animation: ld-14-sq-spin 1.2s ease-in-out infinite;
}

@keyframes ld-14-sq-spin {
  0% {
    transform: perspective(120px) rotateX(0) rotateY(0);
  }

  50% {
    transform: perspective(120px) rotateX(-180deg) rotateY(0);
  }

  100% {
    transform: perspective(120px) rotateX(-180deg) rotateY(-180deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ld-14__morph,
    .ld-14__sq-orbit,
    .ld-14__sq-orbit span,
    .ld-14__chase-sq span,
    .ld-14__sq-spin {
    animation: none;
  }
}
```
