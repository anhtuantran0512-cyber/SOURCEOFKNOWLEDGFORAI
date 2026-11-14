---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-ui/radial-spotlight-cursor-tracking-card/"
title: "Radial Spotlight / Cursor-Tracking Card"
section: "design-styles"
category: "css-gradient-ui"
category_name: "CSS Gradient UI"
description: "The signature \"AI dashboard\" card grid: a radial spotlight follows your cursor across each card while a gradient seam glows on the borders nearest the…"
has_js: "true"
---

Here's a working CSS Gradient UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Radial Spotlight / Cursor-Tracking Card
Source: https://codefronts.com/design-styles/css-gradient-ui/radial-spotlight-cursor-tracking-card/

The signature "AI dashboard" card grid: a radial spotlight follows your cursor across each card while a gradient seam glows on the borders nearest the pointer — 12 lines of JS write two custom properties; CSS does everything else.
## HTML
```html
<div class="cgu-16-group">
<section class="cgu-16" aria-label="Radial spotlight cursor tracking card demos">
  <div class="cgu-16__inner">
    <header class="cgu-16__head">
      <p class="cgu-16__eyebrow">16 · Cursor spotlight</p>
      <h2 class="cgu-16__title">One light source, four cards</h2>
      <p class="cgu-16__sub">Move your cursor across the grid — the spotlight and border seam track it continuously, bleeding across card edges like a single lamp.</p>
    </header>
    <div class="cgu-16__grid" id="cgu-16-grid">
      <article class="cgu-16__card">
        <p class="cgu-16__label">Model</p>
        <h3 class="cgu-16__name">forge-2.1-large</h3>
        <p class="cgu-16__desc">General reasoning · 400k context</p>
        <p class="cgu-16__stat">18.4k <span>req/day</span></p>
      </article>
      <article class="cgu-16__card">
        <p class="cgu-16__label">Latency p95</p>
        <h3 class="cgu-16__name">312 ms</h3>
        <p class="cgu-16__desc">All regions, streaming first token</p>
        <p class="cgu-16__stat">▼ 9% <span>vs last week</span></p>
      </article>
      <article class="cgu-16__card">
        <p class="cgu-16__label">Spend</p>
        <h3 class="cgu-16__name">$4,218</h3>
        <p class="cgu-16__desc">Month to date · cap $6,000</p>
        <p class="cgu-16__stat">70% <span>of budget</span></p>
      </article>
      <article class="cgu-16__card">
        <p class="cgu-16__label">Fine-tunes</p>
        <h3 class="cgu-16__name">7 active</h3>
        <p class="cgu-16__desc">2 training · 1 queued</p>
        <p class="cgu-16__stat">98.1% <span>eval pass</span></p>
      </article>
    </div>
    <p class="cgu-16__foot">JS writes two custom properties per card; both the face spotlight and the border seam are plain CSS gradients reading them.</p>
  </div>
</section>
</div>
```
## CSS
```css
.cgu-16-group {
  display: block;
  width: 100%;
}

.cgu-16,
.cgu-16 *,
.cgu-16 *::before,
.cgu-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgu-16 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 64px 24px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: #eef0ff;
  background: #08090f;
}

.cgu-16__inner {
  width: min(940px,100%);
  display: grid;
  gap: 38px;
}

.cgu-16__head {
  text-align: center;
  display: grid;
  gap: 13px;
  justify-items: center;
}

.cgu-16__eyebrow {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: #818cf8;
}

.cgu-16__title {
  font-size: clamp(27px,4.2vw,46px);
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1.08;
  text-wrap: balance;
}

.cgu-16__sub {
  max-width: 58ch;
  font-size: 15.5px;
  line-height: 1.6;
  color: #a7abc8;
  text-wrap: pretty;
}

.cgu-16__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(210px,1fr));
  gap: 16px;
}

.cgu-16__card {
  --x: 50%;
  --y: 50%;
  position: relative;
  isolation: isolate;
  display: grid;
  gap: 8px;
  align-content: start;
  padding: 26px 24px;
  border-radius: 18px;
  background: #0d0f1a;
  overflow: hidden;
}

.cgu-16__card::after {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(360px circle at var(--x) var(--y),rgba(199,210,254,.07),transparent 65%);
  pointer-events: none;
}

.cgu-16__card::before {
  content: "";
  position: absolute;
  inset: 0;
  padding: 1px;
  border-radius: inherit;
  background: radial-gradient(300px circle at var(--x) var(--y),rgba(129,140,248,.9),rgba(232,121,249,.35) 45%,rgba(255,255,255,.07) 75%);
  -webkit-mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  mask: linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  pointer-events: none;
}

.cgu-16__label {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #6f7495;
}

.cgu-16__name {
  font-size: 22px;
  font-weight: 800;
  letter-spacing: -.01em;
}

.cgu-16__desc {
  font-size: 13px;
  line-height: 1.55;
  color: #9aa0c0;
}

.cgu-16__stat {
  margin-top: 10px;
  font-size: 15px;
  font-weight: 750;
  color: #c7d2fe;
}

.cgu-16__stat span {
  font-size: 12px;
  font-weight: 600;
  color: #6f7495;
  margin-left: 4px;
}

.cgu-16__foot {
  text-align: center;
  font-size: 13px;
  color: #7c81a3;
  max-width: 70ch;
  justify-self: center;
}

@media (hover: none),(pointer: coarse) {
  .cgu-16__card::after {
    background: radial-gradient(360px circle at 50% 0%,rgba(199,210,254,.05),transparent 65%);
  }
}
```

## JavaScript
```js
(() => {
  const grid = document.getElementById('cgu-16-grid'); if (!grid) return;
  if (!matchMedia('(hover: hover) and (pointer: fine)').matches) return;
  const cards = [...grid.querySelectorAll('.cgu-16__card')];
  let raf = 0, ev = null;
  grid.addEventListener('pointermove', e => {
    ev = e;
    if (!raf) raf = requestAnimationFrame(() => {
      raf = 0;
      for (const card of cards) {
        const r = card.getBoundingClientRect();
        card.style.setProperty('--x', (ev.clientX - r.left).toFixed(0) + 'px');
        card.style.setProperty('--y', (ev.clientY - r.top).toFixed(0) + 'px');
      }
    });
  });
})();
```
