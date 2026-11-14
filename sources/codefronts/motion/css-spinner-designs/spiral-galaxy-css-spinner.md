---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/spiral-galaxy-css-spinner/"
title: "Spiral Galaxy CSS Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "Three overlapping conic-gradient arms spiral outward from a bright central core, blurred and rotated 120° apart to simulate a three-armed barred spiral galaxy."
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Spiral Galaxy CSS Spinner
Source: https://codefronts.com/motion/css-spinner-designs/spiral-galaxy-css-spinner/

Three overlapping conic-gradient arms spiral outward from a bright central core, blurred and rotated 120° apart to simulate a three-armed barred spiral galaxy.
## HTML
```html
<div class="sp-16">
  <div class="sp-16__galaxy">
    <div class="sp-16__arm"></div>
    <div class="sp-16__arm"></div>
    <div class="sp-16__arm"></div>
    <div class="sp-16__core"></div>
  </div>
</div>
```
## CSS
```css
.sp-16,
.sp-16 *,
.sp-16 *::before,
.sp-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-16 {
  --bg: #03010a;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-16__galaxy {
  position: relative;
  width: 100px;
  height: 100px;
  animation: sp-16-spin 3s linear infinite;
}

.sp-16__arm {
  position: absolute;
  inset: 0;
  border-radius: 50%;
}

.sp-16__arm:nth-child(1) {
  background: conic-gradient(
      transparent 0deg, transparent 40deg,
      rgba(99,102,241,0.8) 80deg, transparent 160deg,
      transparent 200deg, transparent 240deg,
      rgba(99,102,241,0.4) 280deg, transparent 360deg
    );
  filter: blur(2px);
}

.sp-16__arm:nth-child(2) {
  background: conic-gradient(
      transparent 0deg, transparent 120deg,
      rgba(168,85,247,0.7) 160deg, transparent 240deg,
      transparent 280deg, transparent 300deg,
      rgba(168,85,247,0.3) 340deg, transparent 360deg
    );
  filter: blur(1.5px);
  transform: rotate(120deg);
}

.sp-16__arm:nth-child(3) {
  background: conic-gradient(
      transparent 0deg, transparent 240deg,
      rgba(236,72,153,0.6) 280deg, transparent 360deg
    );
  filter: blur(1px);
  transform: rotate(240deg);
}

.sp-16__core {
  position: absolute;
  inset: 38px;
  border-radius: 50%;
  background: radial-gradient(circle,#fff 0%,rgba(168,85,247,0.8) 40%,transparent 80%);
  filter: blur(2px);
}

@keyframes sp-16-spin {
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-16__galaxy {
    animation: none;
  }
}
```
