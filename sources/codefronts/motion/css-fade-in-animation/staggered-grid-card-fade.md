---
source: "codefronts"
url: "https://codefronts.com/motion/css-fade-in-animation/staggered-grid-card-fade/"
title: "Staggered Grid Card Fade"
section: "motion"
category: "css-fade-in-animation"
category_name: "CSS Fade In Animation Designs"
description: "A dashboard metrics grid where six stat cards stagger into view with nth-child animation-delay offsets, each sliding up from translateY(16px) to its resting…"
has_js: "false"
---

Here's a working CSS Fade In Animation Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Staggered Grid Card Fade
Source: https://codefronts.com/motion/css-fade-in-animation/staggered-grid-card-fade/

A dashboard metrics grid where six stat cards stagger into view with nth-child animation-delay offsets, each sliding up from translateY(16px) to its resting position.
## HTML
```html
<div class="fi-04">
  <div class="fi-04__label">Dashboard Metrics</div>
  <div class="fi-04__grid">
    <div class="fi-04__card">
      <div class="fi-04__num">$84K</div>
      <div class="fi-04__metric">Revenue</div>
      <div class="fi-04__bar-bg"><div class="fi-04__bar"></div></div>
    </div>
    <div class="fi-04__card">
      <div class="fi-04__num">12.4K</div>
      <div class="fi-04__metric">Users</div>
      <div class="fi-04__bar-bg"><div class="fi-04__bar"></div></div>
    </div>
    <div class="fi-04__card">
      <div class="fi-04__num">91%</div>
      <div class="fi-04__metric">Uptime</div>
      <div class="fi-04__bar-bg"><div class="fi-04__bar"></div></div>
    </div>
    <div class="fi-04__card">
      <div class="fi-04__num">3.2s</div>
      <div class="fi-04__metric">Avg Load</div>
      <div class="fi-04__bar-bg"><div class="fi-04__bar"></div></div>
    </div>
    <div class="fi-04__card">
      <div class="fi-04__num">73%</div>
      <div class="fi-04__metric">Retention</div>
      <div class="fi-04__bar-bg"><div class="fi-04__bar"></div></div>
    </div>
    <div class="fi-04__card">
      <div class="fi-04__num">4.2★</div>
      <div class="fi-04__metric">Rating</div>
      <div class="fi-04__bar-bg"><div class="fi-04__bar"></div></div>
    </div>
  </div>
</div>
```
## CSS
```css
.fi-04 {
  --bg: #0c0e16;
  --c1: #f97316;
  --c2: #ef4444;
  --c3: #a855f7;
  --c4: #3b82f6;
  --c5: #10b981;
  --c6: #f59e0b;
  --text: #f5f5f0;
  font-family: 'DM Sans',sans-serif;
  min-height: 340px;
  border-radius: 20px;
  padding: 32px;
  overflow: hidden;
}

.fi-04 *,
.fi-04 *::before,
.fi-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fi-04 ::selection {
  background: #f97316;
  color: #000;
}

.fi-04__label {
  font-family: 'Syne',sans-serif;
  font-size: .75rem;
  font-weight: 600;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: rgba(245,245,240,.4);
  margin-bottom: 20px;
}

.fi-04__grid {
  display: grid;
  grid-template-columns: repeat(auto-fill,minmax(130px,1fr));
  gap: 14px;
}

.fi-04__card {
  border-radius: 14px;
  padding: 20px 16px;
  opacity: 0;
  transform: translateY(16px);
  animation: fi-04-stagger .6s cubic-bezier(.16,1,.3,1) forwards;
}

.fi-04__card:nth-child(1) {
  --delay: .05s;
  background: linear-gradient(135deg,rgba(249,115,22,.15),rgba(239,68,68,.08));
  border: 1px solid rgba(249,115,22,.25);
}

.fi-04__card:nth-child(2) {
  --delay: .12s;
  background: linear-gradient(135deg,rgba(168,85,247,.15),rgba(99,102,241,.08));
  border: 1px solid rgba(168,85,247,.25);
}

.fi-04__card:nth-child(3) {
  --delay: .19s;
  background: linear-gradient(135deg,rgba(59,130,246,.15),rgba(6,182,212,.08));
  border: 1px solid rgba(59,130,246,.25);
}

.fi-04__card:nth-child(4) {
  --delay: .26s;
  background: linear-gradient(135deg,rgba(16,185,129,.15),rgba(5,150,105,.08));
  border: 1px solid rgba(16,185,129,.25);
}

.fi-04__card:nth-child(5) {
  --delay: .33s;
  background: linear-gradient(135deg,rgba(245,158,11,.15),rgba(234,179,8,.08));
  border: 1px solid rgba(245,158,11,.25);
}

.fi-04__card:nth-child(6) {
  --delay: .40s;
  background: linear-gradient(135deg,rgba(239,68,68,.15),rgba(236,72,153,.08));
  border: 1px solid rgba(239,68,68,.25);
}

.fi-04__card {
  animation-delay: var(--delay);
}

.fi-04__num {
  font-family: 'Syne',sans-serif;
  font-size: 1.6rem;
  font-weight: 800;
  line-height: 1;
  margin-bottom: 4px;
}

.fi-04__card:nth-child(1) .fi-04__num {
  color: var(--c1);
}

.fi-04__card:nth-child(2) .fi-04__num {
  color: var(--c3);
}

.fi-04__card:nth-child(3) .fi-04__num {
  color: var(--c4);
}

.fi-04__card:nth-child(4) .fi-04__num {
  color: var(--c5);
}

.fi-04__card:nth-child(5) .fi-04__num {
  color: var(--c6);
}

.fi-04__card:nth-child(6) .fi-04__num {
  color: var(--c2);
}

.fi-04__metric {
  font-size: .72rem;
  color: rgba(245,245,240,.5);
  letter-spacing: .05em;
  text-transform: uppercase;
  margin-bottom: 12px;
}

.fi-04__bar-bg {
  height: 4px;
  background: rgba(255,255,255,.07);
  border-radius: 2px;
}

.fi-04__bar {
  height: 4px;
  border-radius: 2px;
  transition: width .6s cubic-bezier(.16,1,.3,1);
}

.fi-04__card:nth-child(1) .fi-04__bar {
  background: var(--c1);
  width: 84%;
}

.fi-04__card:nth-child(2) .fi-04__bar {
  background: var(--c3);
  width: 67%;
}

.fi-04__card:nth-child(3) .fi-04__bar {
  background: var(--c4);
  width: 91%;
}

.fi-04__card:nth-child(4) .fi-04__bar {
  background: var(--c5);
  width: 55%;
}

.fi-04__card:nth-child(5) .fi-04__bar {
  background: var(--c6);
  width: 73%;
}

.fi-04__card:nth-child(6) .fi-04__bar {
  background: var(--c2);
  width: 42%;
}

@keyframes fi-04-stagger {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (prefers-reduced-motion: reduce) {
  .fi-04 * {
    animation: none!important;
    opacity: 1!important;
    transform: none!important;
  }
}
```
