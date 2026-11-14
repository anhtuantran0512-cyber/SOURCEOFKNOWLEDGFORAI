---
source: "codefronts"
url: "https://codefronts.com/motion/css-fade-in-animation/scale-up-zoom-in-fade/"
title: "Scale-Up Zoom In Fade"
section: "motion"
category: "css-fade-in-animation"
category_name: "CSS Fade In Animation Designs"
description: "Four metric stat cards pop into view from scale(0.5) using a spring cubic-bezier(.34,1.56,.64,1) overshoot curve — a satisfying organic scale-up growth…"
has_js: "false"
---

Here's a working CSS Fade In Animation Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scale-Up Zoom In Fade
Source: https://codefronts.com/motion/css-fade-in-animation/scale-up-zoom-in-fade/

Four metric stat cards pop into view from scale(0.5) using a spring cubic-bezier(.34,1.56,.64,1) overshoot curve — a satisfying organic scale-up growth entrance.
## HTML
```html
<div class="fi-07">
  <div class="fi-07__card">
    <div class="fi-07__num">2.4B</div>
    <div class="fi-07__label">Requests</div>
    <div class="fi-07__ring"></div>
  </div>
  <div class="fi-07__card">
    <div class="fi-07__num">99.9</div>
    <div class="fi-07__label">Uptime %</div>
    <div class="fi-07__ring"></div>
  </div>
  <div class="fi-07__card">
    <div class="fi-07__num">0.4ms</div>
    <div class="fi-07__label">Latency</div>
    <div class="fi-07__ring"></div>
  </div>
  <div class="fi-07__card">
    <div class="fi-07__num">140+</div>
    <div class="fi-07__label">Countries</div>
    <div class="fi-07__ring"></div>
  </div>
</div>
```
## CSS
```css
.fi-07 {
  --bg: #060d0d;
  --teal: #2dd4bf;
  --cyan: #06b6d4;
  --text: #f0fdfa;
  font-family: 'Inter',sans-serif;
  min-height: 340px;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 24px;
  flex-wrap: wrap;
  padding: 40px;
  overflow: hidden;
}

.fi-07 *,
.fi-07 *::before,
.fi-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fi-07 ::selection {
  background: var(--teal);
  color: #000;
}
/* scale-up fade: scale(.5) opacity:0 → scale(1) opacity:1 */

.fi-07__card {
  width: 140px;
  border-radius: 16px;
  padding: 24px 16px;
  text-align: center;
  opacity: 0;
  transform: scale(.5);
  animation: fi-07-zoom-in .6s cubic-bezier(.34,1.56,.64,1) forwards;
}

.fi-07__card:nth-child(1) {
  --d: .05s;
  background: linear-gradient(135deg,rgba(45,212,191,.15),rgba(6,182,212,.08));
  border: 1px solid rgba(45,212,191,.3);
}

.fi-07__card:nth-child(2) {
  --d: .18s;
  background: linear-gradient(135deg,rgba(6,182,212,.15),rgba(59,130,246,.08));
  border: 1px solid rgba(6,182,212,.3);
}

.fi-07__card:nth-child(3) {
  --d: .31s;
  background: linear-gradient(135deg,rgba(45,212,191,.12),rgba(52,211,153,.08));
  border: 1px solid rgba(45,212,191,.25);
}

.fi-07__card:nth-child(4) {
  --d: .44s;
  background: linear-gradient(135deg,rgba(6,182,212,.12),rgba(14,165,233,.08));
  border: 1px solid rgba(6,182,212,.25);
}

.fi-07__card {
  animation-delay: var(--d);
}

.fi-07__card:hover {
  transform: scale(1.04)!important;
  transition: transform .2s;
}

.fi-07__num {
  font-family: 'Orbitron',monospace;
  font-size: 2rem;
  font-weight: 900;
  background: linear-gradient(135deg,var(--teal),var(--cyan));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1;
  margin-bottom: 6px;
}

.fi-07__label {
  font-size: .68rem;
  font-weight: 500;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(240,253,250,.45);
  margin-bottom: 12px;
}

.fi-07__ring {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: 3px solid rgba(45,212,191,.15);
  border-top-color: var(--teal);
  margin: 0 auto;
}

@keyframes fi-07-zoom-in {
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .fi-07 * {
    animation: none!important;
    opacity: 1!important;
    transform: scale(1)!important;
  }
}
```
