---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/stacked-ring-helix-spinner/"
title: "Stacked Ring Helix Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "Three concentric rings in blue, indigo, and violet spin at alternating speeds and directions, with each ring using different border-side pairs to create a…"
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stacked Ring Helix Spinner
Source: https://codefronts.com/motion/css-spinner-designs/stacked-ring-helix-spinner/

Three concentric rings in blue, indigo, and violet spin at alternating speeds and directions, with each ring using different border-side pairs to create a three-axis helix illusion.
## HTML
```html
<div class="sp-07">
  <div class="sp-07__helix">
    <div class="sp-07__ring"></div>
    <div class="sp-07__ring"></div>
    <div class="sp-07__ring"></div>
    <div class="sp-07__core"></div>
  </div>
</div>
```
## CSS
```css
.sp-07,
.sp-07 *,
.sp-07 *::before,
.sp-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-07 {
  --bg: #080c18;
  --c1: #40c4ff;
  --c2: #7986cb;
  --c3: #ce93d8;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-07__helix {
  position: relative;
  width: 72px;
  height: 72px;
  transform-style: preserve-3d;
  perspective: 200px;
}

.sp-07__ring {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 3px solid transparent;
}

.sp-07__ring:nth-child(1) {
  border-top-color: var(--c1);
  border-bottom-color: var(--c1);
  filter: drop-shadow(0 0 5px var(--c1));
  animation: sp-07-spin 1.4s linear infinite;
}

.sp-07__ring:nth-child(2) {
  inset: 10px;
  border-left-color: var(--c2);
  border-right-color: var(--c2);
  filter: drop-shadow(0 0 5px var(--c2));
  animation: sp-07-spin 1.4s linear infinite reverse;
  animation-delay: -0.23s;
}

.sp-07__ring:nth-child(3) {
  inset: 20px;
  border-top-color: var(--c3);
  border-bottom-color: var(--c3);
  filter: drop-shadow(0 0 5px var(--c3));
  animation: sp-07-spin 1.4s linear infinite;
  animation-delay: -0.46s;
}

.sp-07__core {
  position: absolute;
  inset: 30px;
  border-radius: 50%;
  background: radial-gradient(var(--c3),transparent);
  opacity: 0.5;
}

@keyframes sp-07-spin {
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-07__ring {
    animation: none;
  }
}
```
