---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/morph-square-to-circle-spinner/"
title: "Morph Square-to-Circle Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "A hollow square morphs fluidly through four asymmetric border-radius stages into a perfect circle and back, while simultaneously rotating — a classic CSS…"
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Morph Square-to-Circle Spinner
Source: https://codefronts.com/motion/css-spinner-designs/morph-square-to-circle-spinner/

A hollow square morphs fluidly through four asymmetric border-radius stages into a perfect circle and back, while simultaneously rotating — a classic CSS shape-morphing technique.
## HTML
```html
<div class="sp-08">
  <div class="sp-08__outer">
    <div class="sp-08__track"></div>
    <div class="sp-08__shape"></div>
  </div>
</div>
```
## CSS
```css
.sp-08,
.sp-08 *,
.sp-08 *::before,
.sp-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-08 {
  --bg: #0e0e12;
  --c: #ff9100;
  --glow: rgba(255,145,0,0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-08__shape {
  width: 60px;
  height: 60px;
  background: transparent;
  border: 4px solid var(--c);
  filter: drop-shadow(0 0 8px var(--glow));
  animation: sp-08-morph 2s ease-in-out infinite, sp-08-spin 2s linear infinite;
}

@keyframes sp-08-morph {
  0%,
    100% {
    border-radius: 4px;
    transform: rotate(0deg) scale(1);
  }

  25% {
    border-radius: 50% 4px 50% 4px;
  }

  50% {
    border-radius: 50%;
    transform: rotate(180deg) scale(1.15);
  }

  75% {
    border-radius: 4px 50% 4px 50%;
  }
}

@keyframes sp-08-spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

.sp-08__outer {
  position: relative;
  width: 80px;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.sp-08__track {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 1px solid rgba(255,145,0,0.1);
}

@media (prefers-reduced-motion: reduce) {
  .sp-08__shape {
    animation: none;
    border-radius: 8px;
  }
}
```
