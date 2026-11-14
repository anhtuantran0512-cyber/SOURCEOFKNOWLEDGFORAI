---
source: "codefronts"
url: "https://codefronts.com/motion/css-gradient-animation/css-retro-vaporwave-cyberpunk-mesh/"
title: "CSS Retro Vaporwave Cyberpunk Mesh"
section: "motion"
category: "css-gradient-animation"
category_name: "CSS Gradient Animations"
description: "A high-contrast, fast-rotating mesh gradient in neon magenta, cyan, and violet layered with a CSS grid overlay and CRT scanlines, creating a brutalist…"
has_js: "true"
---

Here's a working CSS Gradient Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Retro Vaporwave Cyberpunk Mesh
Source: https://codefronts.com/motion/css-gradient-animation/css-retro-vaporwave-cyberpunk-mesh/

A high-contrast, fast-rotating mesh gradient in neon magenta, cyan, and violet layered with a CSS grid overlay and CRT scanlines, creating a brutalist retro-futuristic aesthetic popular in vaporwave and cyberpunk design.
## HTML
```html
<div class="ga-12">
  <div class="ga-12__grid"></div>
  <div class="ga-12__scan"></div>

  <div class="ga-12__content">
    <span class="ga-12__year">∴ 1989 — 2089 ∴</span>
    <h1 class="ga-12__title">VAPORWAVE</h1>
    <p class="ga-12__sub">Aesthetics · Interface · Future · Retro</p>
    <div class="ga-12__divider"></div>
    <div class="ga-12__pills">
      <span class="ga-12__pill ga-12__pill--m">Neon Magenta</span>
      <span class="ga-12__pill ga-12__pill--c">Cyber Cyan</span>
      <span class="ga-12__pill ga-12__pill--p">Deep Violet</span>
    </div>
  </div>

  <div class="ga-12__ctrl">
    <button class="ga-12__ctrl-btn" data-dur="12s">Slow</button>
    <button class="ga-12__ctrl-btn active" data-dur="6s">Normal</button>
    <button class="ga-12__ctrl-btn" data-dur="2.5s">Fast</button>
  </div>
</div>
```
## CSS
```css
.ga-12,
.ga-12 *,
.ga-12 *::before,
.ga-12 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ga-12 ::selection {
  background: rgba(236,72,153,.5);
  color: #fff;
}

.ga-12 {
  --bg: #06010f;
  --c1: #ff00ff;
  --c2: #00ffff;
  --c3: #bf00ff;
  --c4: #ff006e;
  --dur: 6s;
  position: relative;
  width: 100%;
  min-height: 100vh;
  overflow: hidden;
  background: var(--bg);
  font-family: system-ui, -apple-system, sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 32px;
  padding: 48px 24px;
}
/* ── Fast-moving high-contrast mesh ── */

.ga-12::before {
  content: '';
  position: absolute;
  inset: -20%;
  background: radial-gradient(ellipse 50% 40% at 20% 30%, color-mix(in srgb, var(--c1) 35%, transparent), transparent 60%), radial-gradient(ellipse 45% 45% at 80% 70%, color-mix(in srgb, var(--c2) 30%, transparent), transparent 60%), radial-gradient(ellipse 40% 50% at 60% 20%, color-mix(in srgb, var(--c3) 28%, transparent), transparent 55%), radial-gradient(ellipse 55% 35% at 30% 80%, color-mix(in srgb, var(--c4) 25%, transparent), transparent 55%);
  animation: ga-12-mesh var(--dur) linear infinite;
  mix-blend-mode: screen;
}
/* Second mesh layer — faster, different direction */

.ga-12::after {
  content: '';
  position: absolute;
  inset: -20%;
  background: radial-gradient(ellipse 30% 50% at 70% 40%, color-mix(in srgb, var(--c2) 20%, transparent), transparent 55%), radial-gradient(ellipse 40% 30% at 15% 60%, color-mix(in srgb, var(--c1) 18%, transparent), transparent 50%);
  animation: ga-12-mesh2 calc(var(--dur) * .7) linear infinite reverse;
  mix-blend-mode: screen;
}

@keyframes ga-12-mesh {
  0% {
    transform: rotate(0deg) scale(1);
  }

  100% {
    transform: rotate(360deg) scale(1.05);
  }
}

@keyframes ga-12-mesh2 {
  0% {
    transform: rotate(0deg) translate(0, 0);
  }

  33% {
    transform: rotate(120deg) translate(5%, -5%);
  }

  66% {
    transform: rotate(240deg) translate(-5%, 5%);
  }

  100% {
    transform: rotate(360deg) translate(0, 0);
  }
}
/* Scan-line grid overlay */

.ga-12__grid {
  position: absolute;
  inset: 0;
  background-image: linear-gradient(rgba(0,255,255,.03) 1px, transparent 1px), linear-gradient(90deg, rgba(0,255,255,.03) 1px, transparent 1px);
  background-size: 40px 40px;
  pointer-events: none;
  z-index: 1;
}
/* CRT scanline overlay */

.ga-12__scan {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
      to bottom,
      transparent 0px,
      transparent 2px,
      rgba(0,0,0,.08) 2px,
      rgba(0,0,0,.08) 4px
    );
  pointer-events: none;
  z-index: 2;
}
/* Content */

.ga-12__content {
  position: relative;
  z-index: 3;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
}

.ga-12__year {
  font-size: .72rem;
  font-weight: 900;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: var(--c2);
  text-shadow: 0 0 10px var(--c2), 0 0 20px var(--c2);
  animation: ga-12-flicker 4s ease-in-out infinite;
}

@keyframes ga-12-flicker {
  0%,
    95%,
    100% {
    opacity: 1;
  }

  96% {
    opacity: .6;
  }

  97% {
    opacity: 1;
  }

  98% {
    opacity: .4;
  }
}

.ga-12__title {
  font-size: clamp(2.4rem, 7vw, 5rem);
  font-weight: 900;
  line-height: 1;
  letter-spacing: -.02em;
  text-transform: uppercase;
  background: linear-gradient(180deg, var(--c1) 0%, var(--c2) 55%, var(--c3) 100%);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 0 16px rgba(255,0,255,.6)) drop-shadow(0 0 32px rgba(0,255,255,.3));
}

.ga-12__sub {
  font-size: .95rem;
  font-weight: 600;
  color: rgba(0,255,255,.7);
  letter-spacing: .08em;
  text-shadow: 0 0 8px rgba(0,255,255,.5);
}

.ga-12__divider {
  width: 200px;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--c1), var(--c2), transparent);
  position: relative;
}

.ga-12__divider::after {
  content: '';
  position: absolute;
  inset: 0;
  background: inherit;
  filter: blur(4px);
  opacity: .7;
}
/* Stat pills */

.ga-12__pills {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 4px;
}

.ga-12__pill {
  padding: 6px 16px;
  border-radius: 4px;
  font-size: .72rem;
  font-weight: 800;
  letter-spacing: .1em;
  text-transform: uppercase;
  border: 1px solid;
  cursor: pointer;
  transition: all .2s;
}

.ga-12__pill--m {
  color: var(--c1);
  border-color: rgba(255,0,255,.35);
  background: rgba(255,0,255,.07);
}

.ga-12__pill--m:hover {
  background: rgba(255,0,255,.15);
  box-shadow: 0 0 12px rgba(255,0,255,.3);
}

.ga-12__pill--c {
  color: var(--c2);
  border-color: rgba(0,255,255,.35);
  background: rgba(0,255,255,.06);
}

.ga-12__pill--c:hover {
  background: rgba(0,255,255,.12);
  box-shadow: 0 0 12px rgba(0,255,255,.25);
}

.ga-12__pill--p {
  color: var(--c3);
  border-color: rgba(191,0,255,.3);
  background: rgba(191,0,255,.06);
}

.ga-12__pill--p:hover {
  background: rgba(191,0,255,.13);
  box-shadow: 0 0 12px rgba(191,0,255,.25);
}
/* Speed control */

.ga-12__ctrl {
  position: absolute;
  bottom: 14px;
  right: 14px;
  z-index: 10;
  display: flex;
  gap: 5px;
}

.ga-12__ctrl-btn {
  padding: 4px 10px;
  font-size: .68rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: .07em;
  border-radius: 3px;
  border: 1px solid rgba(0,255,255,.2);
  background: rgba(0,0,0,.4);
  color: rgba(0,255,255,.4);
  cursor: pointer;
  transition: all .15s;
}

.ga-12__ctrl-btn.active,
.ga-12__ctrl-btn:hover {
  border-color: var(--c2);
  color: var(--c2);
  text-shadow: 0 0 6px var(--c2);
}

@media (prefers-reduced-motion: reduce) {
  .ga-12::before,
    .ga-12::after {
    animation: none;
  }

  .ga-12__year {
    animation: none;
  }
}
```

## JavaScript
```js
(function() {
  const w = document.querySelector('.ga-12');
  w.querySelectorAll('.ga-12__ctrl-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      w.querySelectorAll('.ga-12__ctrl-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      w.style.setProperty('--dur', btn.dataset.dur);
    });
  });
})();
```
