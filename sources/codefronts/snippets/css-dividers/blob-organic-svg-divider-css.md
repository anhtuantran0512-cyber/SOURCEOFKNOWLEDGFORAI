---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/blob-organic-svg-divider-css/"
title: "Blob Organic SVG Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "Fluid, non-geometric shapes for portfolio and product pages — plus the thing most blob tutorials skip: where the curve numbers come from."
has_js: "true"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Blob Organic SVG Divider CSS
Source: https://codefronts.com/snippets/css-dividers/blob-organic-svg-divider-css/

Fluid, non-geometric shapes for portfolio and product pages — plus the thing most blob tutorials skip: where the curve numbers come from. A 22-line generator walks a circle, jitters each radius, and emits a smooth cubic path, so "Reshuffle" gives you an infinite supply of on-brand blobs. A second, purely-CSS blob morphs forever using animated border-radius, for when you want organic motion with zero script.
## HTML
```html
<section class="div-07" aria-label="Organic blob SVG divider demo">
  <div class="div-07__top">
    <div class="div-07__blob" aria-hidden="true"></div>
    <p class="div-07__eyebrow">generated path · morphing radius</p>
    <h2 class="div-07__title">Shapes that never repeat</h2>
    <div class="div-07__wrap" aria-hidden="true">
      <svg class="div-07__svg" id="div-07-svg" viewBox="0 0 1200 160" preserveAspectRatio="none" focusable="false">
        <path id="div-07-path" d="M0,90 C200,140 380,40 620,78 C860,116 1010,150 1200,96 L1200,160 L0,160 Z"></path>
      </svg>
    </div>
  </div>
  <div class="div-07__bottom">
    <p class="div-07__lede">Each reshuffle walks a circle, jitters every radius, then smooths the vertices into cubic segments.</p>
    <button class="div-07__btn" id="div-07-shuffle" type="button">Reshuffle the blob</button>
    <p class="div-07__chip">Catmull-Rom smoothing · 8-value border-radius morph</p>
  </div>
</section>
```
## CSS
```css
.div-07 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-07-bg);
  --div-07-bg: oklch(0.96 0.03 190);
  --div-07-top: oklch(0.35 0.11 300);
  --div-07-ink: oklch(0.98 0.01 300);
  --div-07-dark: oklch(0.28 0.04 290);
  --div-07-mut: oklch(0.53 0.03 290);
  --div-07-acc: oklch(0.74 0.17 340);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--div-07-dark);
}

.div-07 *,
.div-07 *::before,
.div-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-07__top {
  position: relative;
  min-height: 56svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: 12px;
  text-align: center;
  color: var(--div-07-ink);
  background: linear-gradient(150deg,var(--div-07-top),oklch(0.28 0.09 265));
  padding: clamp(34px,7vw,80px) clamp(20px,5vw,56px) clamp(80px,13vw,150px);
  overflow: hidden;
}

.div-07__blob {
  position: absolute;
  width: min(40vw,300px);
  aspect-ratio: 1;
  top: -16%;
  right: -11%;
  background: radial-gradient(circle at 35% 30%,var(--div-07-acc),oklch(0.55 0.19 320/.35));
  filter: blur(3px);
  opacity: .4;
  border-radius: 42% 58% 63% 37%/41% 44% 56% 59%;
  animation: div-07-morph 14s ease-in-out infinite,div-07-spin 32s linear infinite;
}

@keyframes div-07-morph {
  0%,
    100% {
    border-radius: 42% 58% 63% 37%/41% 44% 56% 59%;
  }

  33% {
    border-radius: 63% 37% 41% 59%/57% 63% 37% 43%;
  }

  66% {
    border-radius: 36% 64% 55% 45%/62% 38% 62% 38%;
  }
}

@keyframes div-07-spin {
  to {
    transform: rotate(360deg);
  }
}

.div-07__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--div-07-acc);
}

.div-07__title {
  font-size: clamp(28px,5vw,52px);
  line-height: 1.05;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.div-07__wrap {
  position: absolute;
  inset: auto 0 -1px;
  height: clamp(72px,11vw,160px);
  line-height: 0;
  pointer-events: none;
}

.div-07__svg {
  width: 100%;
  height: 100%;
  display: block;
}

.div-07__svg path {
  fill: var(--div-07-bg);
  transition: d .8s cubic-bezier(.65,0,.35,1);
}

.div-07__bottom {
  min-height: 44svh;
  display: grid;
  place-content: center;
  justify-items: center;
  gap: 18px;
  text-align: center;
  padding: clamp(28px,5vw,60px) clamp(20px,5vw,56px);
}

.div-07__lede {
  max-width: 52ch;
  font-size: clamp(15px,1.9vw,19px);
  line-height: 1.62;
  text-wrap: pretty;
}

.div-07__btn {
  min-height: 46px;
  padding: 0 24px;
  border: 0;
  border-radius: 99px;
  background: linear-gradient(120deg,var(--div-07-acc),oklch(0.62 0.19 300));
  color: oklch(0.99 0.01 340);
  font-family: inherit;
  font-size: 14.5px;
  font-weight: 650;
  cursor: pointer;
  box-shadow: 0 8px 22px oklch(0.62 0.19 320/.32);
  transition: transform .18s ease,box-shadow .18s ease;
}

.div-07__btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 28px oklch(0.62 0.19 320/.42);
}

.div-07__btn:active {
  transform: translateY(0);
}

.div-07__btn:focus-visible {
  outline: 2px solid var(--div-07-top);
  outline-offset: 3px;
}

.div-07__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  color: var(--div-07-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.28 0.04 290/.16);
  border-radius: 99px;
}

@media (prefers-reduced-motion: reduce) {
  .div-07__blob {
    animation: none;
  }

  .div-07__svg path {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  const svg = document.getElementById('div-07-svg');
  const path = document.getElementById('div-07-path');
  const btn = document.getElementById('div-07-shuffle');
  if (!svg || !path || !btn || btn.dataset.ppWired) return;
  btn.dataset.ppWired = '1';
  const W = 1200, H = 160, N = 7, WOBBLE = 0.42;
  const build = () => {
    const ys = Array.from({ length: N + 1 }, () => 30 + Math.random() * WOBBLE * 150);
    ys[N] = ys[0];
    const step = W / N;
    let d = 'M0,' + ys[0].toFixed(1);
    for (let i = 0; i < N; i++) {
      const x0 = i * step, x1 = (i + 1) * step, cx = step * 0.42;
      d += ' C' + (x0 + cx).toFixed(1) + ',' + ys[i].toFixed(1) +
           ' ' + (x1 - cx).toFixed(1) + ',' + ys[i + 1].toFixed(1) +
           ' ' + x1.toFixed(1) + ',' + ys[i + 1].toFixed(1);
    }
    path.setAttribute('d', d + ' L' + W + ',' + H + ' L0,' + H + ' Z');
  };
  btn.addEventListener('click', build);
  build();
})();
```
