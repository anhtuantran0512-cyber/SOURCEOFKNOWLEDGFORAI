---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/glowing-gradient-glassmorphic-borders/"
title: "Glowing Gradient & Glassmorphic Borders"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A dark web3/crypto wallet card on a frosted-glass surface where a vibrant teal-to-violet radial glow blooms behind the blur and a matching neon border lights…"
has_js: "true"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glowing Gradient & Glassmorphic Borders
Source: https://codefronts.com/motion/css-card-hover-effects/glowing-gradient-glassmorphic-borders/

A dark web3/crypto wallet card on a frosted-glass surface where a vibrant teal-to-violet radial glow blooms behind the blur and a matching neon border lights up, both tracking the cursor around the edges. Built with backdrop-filter and a masked gradient ring, perfect for crypto dashboards, staking widgets, and dark-themed SaaS landing pages that want an energetic, high-tech edge.
## HTML
```html
<div class="card-02">
  <article class="card-02__card" data-card-02="root">
    <div class="card-02__inner">
      <div class="card-02__row">
        <div class="card-02__coin"></div>
        <span class="card-02__net">// MAINNET</span>
      </div>
      <div>
        <p class="card-02__balance">STAKED BALANCE</p>
        <p class="card-02__amount">48.20 Ξ</p>
      </div>
      <p class="card-02__desc">Self-custody vault with live yield. The neon edge ignites and follows your cursor around the glass.</p>
      <div class="card-02__btn">STAKE MORE →</div>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Azeret+Mono:wght@400;500&display=swap');

.card-02,
.card-02 *,
.card-02 *::before,
.card-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-02 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: radial-gradient(circle at 25% 25%, #1a1140 0 20%, transparent 21%), radial-gradient(circle at 80% 70%, #06343f 0 24%, transparent 25%), #06060e;
  font-family: 'Space Grotesk', sans-serif;
  padding: 2rem;
}

.card-02__card {
  --card-02-x: 50%;
  --card-02-y: 50%;
  position: relative;
  width: 340px;
  height: 440px;
  border-radius: 22px;
  cursor: pointer;
  background: rgba(255,255,255,0.05);
  -webkit-backdrop-filter: blur(14px) saturate(1.3);
  backdrop-filter: blur(14px) saturate(1.3);
  border: 1px solid rgba(255,255,255,0.1);
  overflow: hidden;
  transition: transform 0.4s ease;
}

.card-02__card:hover {
  transform: translateY(-4px);
}
/* radial glow that tracks the cursor, behind the glass */

.card-02__card::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 0;
  background: radial-gradient(
      320px circle at var(--card-02-x) var(--card-02-y),
      rgba(0,240,200,0.35),
      rgba(120,80,255,0.18) 40%,
      transparent 65%
    );
  opacity: 0;
  transition: opacity 0.4s ease;
}

.card-02__card:hover::before {
  opacity: 1;
}
/* neon border that lights up around the cursor */

.card-02__card::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1.5px;
  background: radial-gradient(
      260px circle at var(--card-02-x) var(--card-02-y),
      #00f0c8,
      #7a50ff 45%,
      transparent 60%
    );
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  opacity: 0;
  transition: opacity 0.4s ease;
  z-index: 3;
  pointer-events: none;
}

.card-02__card:hover::after {
  opacity: 1;
}

.card-02__inner {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 2.2rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #e8f7f4;
}

.card-02__row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.card-02__coin {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: conic-gradient(#00f0c8, #7a50ff, #00f0c8);
  box-shadow: 0 0 22px rgba(0,240,200,0.4);
}

.card-02__net {
  font-family: 'Azeret Mono', monospace;
  font-size: 0.7rem;
  letter-spacing: 0.16em;
  color: #7af0db;
  border: 1px solid rgba(122,240,219,0.35);
  padding: 0.3rem 0.7rem;
  border-radius: 999px;
}

.card-02__balance {
  font-family: 'Azeret Mono', monospace;
  font-size: 0.74rem;
  letter-spacing: 0.1em;
  color: #8fa0bd;
}

.card-02__amount {
  font-weight: 700;
  font-size: 2.8rem;
  line-height: 1;
  background: linear-gradient(90deg, #00f0c8, #9d7bff);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-02__desc {
  font-size: 0.84rem;
  line-height: 1.6;
  color: #9aa6bf;
}

.card-02__btn {
  text-align: center;
  font-family: 'Azeret Mono', monospace;
  font-size: 0.82rem;
  letter-spacing: 0.08em;
  padding: 0.85rem;
  border-radius: 12px;
  background: rgba(0,240,200,0.12);
  border: 1px solid rgba(0,240,200,0.3);
  color: #5ff5d8;
}

@media (prefers-reduced-motion: reduce) {
  .card-02__card,
    .card-02__card::before,
    .card-02__card::after {
    transition: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.card-02');
  if (!root) return;
  const c = root.querySelector('[data-card-02="root"]');
  if (!c) return;
  c.addEventListener('mousemove', (e) => {
    const r = c.getBoundingClientRect();
    c.style.setProperty('--card-02-x', `${e.clientX - r.left}px`);
    c.style.setProperty('--card-02-y', `${e.clientY - r.top}px`);
  });
})();
```
