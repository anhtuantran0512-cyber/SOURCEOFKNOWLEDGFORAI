---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-ui/animated-mesh-aurora-gradient-background/"
title: "Animated Mesh / Aurora Gradient Background"
section: "design-styles"
category: "css-gradient-ui"
category_name: "CSS Gradient UI"
description: "A full-viewport aurora built from four drifting radial-gradient blobs, a conic wash and a film-grain overlay — the mesh-gradient look every 2026 landing page…"
has_js: "false"
---

Here's a working CSS Gradient UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Mesh / Aurora Gradient Background
Source: https://codefronts.com/design-styles/css-gradient-ui/animated-mesh-aurora-gradient-background/

A full-viewport aurora built from four drifting radial-gradient blobs, a conic wash and a film-grain overlay — the mesh-gradient look every 2026 landing page wants, hand-written in ~40 lines of CSS with no generator and no canvas.
## HTML
```html
<div class="cgu-07-group">
<section class="cgu-07" aria-label="Animated mesh aurora gradient background demo">
  <div class="cgu-07__sky" aria-hidden="true"></div>
  <div class="cgu-07__grain" aria-hidden="true"></div>
  <div class="cgu-07__content">
    <p class="cgu-07__eyebrow">07 · Mesh / aurora background</p>
    <h2 class="cgu-07__title">Four blobs.<br>One aurora.</h2>
    <p class="cgu-07__sub">This entire sky is four radial-gradients on a slowly drifting layer — no canvas, no WebGL, no generator export. View source; it fits on a screen.</p>
    <div class="cgu-07__row">
      <button class="cgu-07__btn" type="button">Copy the CSS</button>
      <button class="cgu-07__btn cgu-07__btn--ghost" type="button">Read the technique</button>
    </div>
    <dl class="cgu-07__stats">
      <div class="cgu-07__stat"><dt>Layers</dt><dd>4 + grain</dd></div>
      <div class="cgu-07__stat"><dt>JavaScript</dt><dd>0 bytes</dd></div>
      <div class="cgu-07__stat"><dt>Repaints</dt><dd>compositor-only</dd></div>
    </dl>
  </div>
</section>
</div>
```
## CSS
```css
.cgu-07-group {
  display: block;
  width: 100%;
}

.cgu-07,
.cgu-07 *,
.cgu-07 *::before,
.cgu-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgu-07 {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #f2f1ff;
  background: #07060d;
}

.cgu-07__sky {
  position: absolute;
  inset: -25%;
  z-index: -2;
  background: radial-gradient(38% 42% at 20% 25%,oklch(0.6 0.24 300 / .85),transparent 68%),radial-gradient(34% 38% at 78% 20%,oklch(0.7 0.19 200 / .8),transparent 66%),radial-gradient(40% 44% at 70% 78%,oklch(0.65 0.23 345 / .7),transparent 70%),radial-gradient(36% 40% at 25% 80%,oklch(0.72 0.17 150 / .55),transparent 68%),conic-gradient(from 200deg at 50% 50%,#0b0817,#120f22,#0b0817);
  filter: blur(42px) saturate(1.15);
  animation: cgu07-drift 60s ease-in-out infinite alternate;
}

.cgu-07__grain {
  position: absolute;
  inset: 0;
  z-index: -1;
  opacity: .16;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.55'/%3E%3C/svg%3E");
}

.cgu-07__content {
  position: relative;
  width: min(680px,100%);
  text-align: center;
  display: grid;
  gap: 20px;
  justify-items: center;
}

.cgu-07__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: rgba(242,241,255,.75);
}

.cgu-07__title {
  font-size: clamp(40px,7vw,84px);
  font-weight: 850;
  letter-spacing: -.03em;
  line-height: 1.0;
  text-wrap: balance;
  text-shadow: 0 2px 40px rgba(0,0,0,.45);
}

.cgu-07__sub {
  max-width: 52ch;
  font-size: 16px;
  line-height: 1.65;
  color: rgba(242,241,255,.82);
  text-wrap: pretty;
}

.cgu-07__row {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 6px;
}

.cgu-07__btn {
  font: inherit;
  font-size: 15px;
  font-weight: 700;
  color: #12081f;
  padding: 14px 30px;
  border: none;
  border-radius: 9999px;
  cursor: pointer;
  background: linear-gradient(120deg,#f0e7ff,#dcd0ff);
  transition: transform .3s,box-shadow .3s;
  box-shadow: 0 14px 34px -14px rgba(220,208,255,.5);
}

.cgu-07__btn:hover,
.cgu-07__btn:focus-visible {
  transform: translateY(-2px);
  box-shadow: 0 20px 40px -14px rgba(220,208,255,.65);
}

.cgu-07__btn--ghost {
  color: #f2f1ff;
  background: rgba(255,255,255,.08);
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.28);
}

.cgu-07__btn--ghost:hover,
.cgu-07__btn--ghost:focus-visible {
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.5);
}

.cgu-07__btn:focus-visible {
  outline: 3px solid #fff;
  outline-offset: 3px;
}

.cgu-07__stats {
  display: flex;
  gap: 34px;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 20px;
}

.cgu-07__stat {
  display: grid;
  gap: 3px;
}

.cgu-07__stat dt {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: rgba(242,241,255,.55);
}

.cgu-07__stat dd {
  font-size: 17px;
  font-weight: 750;
}

@keyframes cgu07-drift {
  0% {
    transform: translate(0,0) rotate(0deg) scale(1);
  }

  50% {
    transform: translate(4%,-3%) rotate(6deg) scale(1.06);
  }

  100% {
    transform: translate(-4%,3%) rotate(-5deg) scale(1.02);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cgu-07__sky {
    animation: none;
  }

  .cgu-07__btn {
    transition: box-shadow .2s;
  }
}
```

## JavaScript
```js
/* No JavaScript — four radial-gradient blobs + conic wash on a blurred, slowly-transforming layer; SVG turbulence data-URI supplies the grain. */
```
