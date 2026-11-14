---
source: "codefronts"
url: "https://codefronts.com/motion/css-card-hover-effects/gradient-border-draw/"
title: "Gradient Border Draw"
section: "motion"
category: "css-card-hover-effects"
category_name: "CSS Card Hover Effects"
description: "A dark edge-compute product card where a multi-color conic gradient traces a live circuit around the border on hover, powered by the modern @property…"
has_js: "false"
---

Here's a working CSS Card Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Border Draw
Source: https://codefronts.com/motion/css-card-hover-effects/gradient-border-draw/

A dark edge-compute product card where a multi-color conic gradient traces a live circuit around the border on hover, powered by the modern @property animated angle. Great for tech, SaaS, or developer-tool cards that want a premium "powered-on" signal without distracting from the content.
## HTML
```html
<div class="card-08">
  <article class="card-08__card">
    <div class="card-08__inner">
      <span class="card-08__eyebrow">/ Edge Compute</span>
      <h2 class="card-08__title">Halo<br>Runtime</h2>
      <p class="card-08__desc">A serverless mesh that traces a live circuit around every active deployment region.</p>
      <div class="card-08__meta">
        <span>v3.2.0</span>
        <span>99.99% SLA</span>
      </div>
    </div>
  </article>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@600;800&family=DM+Mono:wght@400;500&display=swap');

@property --card-08-angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}

.card-08,
.card-08 *,
.card-08 *::before,
.card-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.card-08 {
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: #07080d;
  font-family: 'DM Mono', monospace;
  padding: 2rem;
}

.card-08__card {
  --card-08-b: 2px;
  position: relative;
  width: 340px;
  height: 420px;
  border-radius: 20px;
  background: #0d0f17;
  cursor: pointer;
  isolation: isolate;
}

.card-08__card::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: var(--card-08-b);
  background: conic-gradient(
      from var(--card-08-angle, 0deg),
      transparent 0deg,
      transparent 70deg,
      #00f0ff 130deg,
      #7b5cff 200deg,
      #ff4dd8 250deg,
      transparent 320deg,
      transparent 360deg
    );
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  opacity: 0;
  transition: opacity 0.4s ease;
  animation: card-08-spin 4s linear infinite paused;
}

@keyframes card-08-spin {
  to {
    --card-08-angle: 360deg;
  }
}

.card-08__card:hover::before {
  opacity: 1;
  animation-play-state: running;
}

.card-08__card::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  border: var(--card-08-b) solid rgba(255,255,255,0.06);
  pointer-events: none;
}

.card-08__inner {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 2.4rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: #e8eaf2;
}

.card-08__eyebrow {
  font-size: 0.7rem;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: #6f7488;
}

.card-08__title {
  font-family: 'Syne', sans-serif;
  font-weight: 800;
  font-size: 2.3rem;
  line-height: 1.05;
  background: linear-gradient(90deg, #00f0ff, #7b5cff, #ff4dd8);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-08__desc {
  font-size: 0.82rem;
  line-height: 1.65;
  color: #9499ab;
}

.card-08__meta {
  display: flex;
  justify-content: space-between;
  font-size: 0.72rem;
  color: #6f7488;
  border-top: 1px solid rgba(255,255,255,0.08);
  padding-top: 1rem;
}

@media (prefers-reduced-motion: reduce) {
  .card-08__card::before {
    animation: none !important;
  }
}
```
