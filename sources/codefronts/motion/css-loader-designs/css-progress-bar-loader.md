---
source: "codefronts"
url: "https://codefronts.com/motion/css-loader-designs/css-progress-bar-loader/"
title: "CSS Progress Bar Loader"
section: "motion"
category: "css-loader-designs"
category_name: "CSS Loaders"
description: "Five animated CSS progress bars — fill sweep, animated stripes, gradient shimmer, indeterminate bounce, and segmented pulse — covering the most common…"
has_js: "false"
---

Here's a working CSS Loader from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Progress Bar Loader
Source: https://codefronts.com/motion/css-loader-designs/css-progress-bar-loader/

Five animated CSS progress bars — fill sweep, animated stripes, gradient shimmer, indeterminate bounce, and segmented pulse — covering the most common loading-state UI patterns.
## HTML
```html
<div class="ld-04">
  <div class="ld-04__stage">
    <div class="ld-04__item">
      <div class="ld-04__label"><span>Uploading file…</span><span>78%</span></div>
      <div class="ld-04__track"><div class="ld-04__fill"></div></div>
```
## CSS
```css
.ld-04,
.ld-04 *,
.ld-04 *::before,
.ld-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ld-04 {
  --bg: #0c0c1d;
  --c1: #a78bfa;
  --c2: #06b6d4;
  --c3: #f472b6;
  --c4: #34d399;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  font-family: 'Segoe UI',sans-serif;
  padding: 40px;
}

.ld-04__stage {
  display: flex;
  flex-direction: column;
  gap: 36px;
  width: 100%;
  max-width: 480px;
}

.ld-04__item {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.ld-04__label {
  display: flex;
  justify-content: space-between;
  color: rgba(255,255,255,.6);
  font-size: 12px;
  letter-spacing: .5px;
}

.ld-04__track {
  height: 8px;
  background: rgba(255,255,255,.08);
  border-radius: 99px;
  overflow: hidden;
  position: relative;
}
/* Standard fill */

.ld-04__fill {
  height: 100%;
  border-radius: 99px;
  background: var(--c1);
  animation: ld-04-fill1 2.5s ease-in-out infinite;
}

@keyframes ld-04-fill1 {
  0% {
    width: 0%;
  }

  60% {
    width: 78%;
  }

  100% {
    width: 78%;
  }
}
/* Striped animated */

.ld-04__striped {
  height: 100%;
  border-radius: 99px;
  background: repeating-linear-gradient(45deg,var(--c2) 0,var(--c2) 10px,rgba(255,255,255,.15) 10px,rgba(255,255,255,.15) 20px);
  background-size: 200% 100%;
  width: 60%;
  animation: ld-04-stripes 1s linear infinite;
}

@keyframes ld-04-stripes {
  to {
    background-position: -200% 0;
  }
}
/* Gradient shimmer */

.ld-04__gfill {
  height: 100%;
  border-radius: 99px;
  width: 55%;
  background: linear-gradient(90deg,var(--c3),var(--c1),var(--c3));
  background-size: 200% 100%;
  animation: ld-04-glow 1.5s ease-in-out infinite;
}

@keyframes ld-04-glow {
  0% {
    background-position: 100% 0;
  }

  100% {
    background-position: -100% 0;
  }
}
/* Indeterminate bounce */

.ld-04__bounce {
  height: 100%;
  border-radius: 99px;
  background: var(--c4);
  width: 40%;
  animation: ld-04-bounce 1.8s ease-in-out infinite;
}

@keyframes ld-04-bounce {
  0% {
    transform: translateX(-100%);
  }

  50% {
    transform: translateX(150%);
  }

  100% {
    transform: translateX(-100%);
  }
}
/* Segmented */

.ld-04__seg-track {
  display: flex;
  gap: 4px;
}

.ld-04__seg {
  flex: 1;
  height: 8px;
  border-radius: 4px;
  background: rgba(255,255,255,.08);
  animation: ld-04-seg 2s ease-in-out infinite;
}

.ld-04__seg:nth-child(1) {
  animation-delay: 0s;
}

.ld-04__seg:nth-child(2) {
  animation-delay: .2s;
}

.ld-04__seg:nth-child(3) {
  animation-delay: .4s;
}

.ld-04__seg:nth-child(4) {
  animation-delay: .6s;
}

.ld-04__seg:nth-child(5) {
  animation-delay: .8s;
}

@keyframes ld-04-seg {
  0%,
    100% {
    background: rgba(255,255,255,.08);
  }

  50% {
    background: var(--c1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ld-04__fill,
    .ld-04__striped,
    .ld-04__gfill,
    .ld-04__bounce,
    .ld-04__seg {
    animation: none;
    width: 60%;
  }
}
```
