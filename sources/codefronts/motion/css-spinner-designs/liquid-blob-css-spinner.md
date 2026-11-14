---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/liquid-blob-css-spinner/"
title: "Liquid Blob CSS Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "A fluid-blue gradient blob morphs organically through six distinct multi-value border-radius shapes while slowly rotating, creating an amorphous liquid…"
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Blob CSS Spinner
Source: https://codefronts.com/motion/css-spinner-designs/liquid-blob-css-spinner/

A fluid-blue gradient blob morphs organically through six distinct multi-value border-radius shapes while slowly rotating, creating an amorphous liquid motion effect.
## HTML
```html
<div class="sp-22">
  <div class="sp-22__blob"></div>
</div>
```
## CSS
```css
.sp-22,
.sp-22 *,
.sp-22 *::before,
.sp-22 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-22 {
  --bg: #020911;
  --c1: #00c6fb;
  --c2: #005bea;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-22__blob {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg,var(--c1),var(--c2));
  box-shadow: 0 0 20px rgba(0,198,251,0.4),0 0 40px rgba(0,91,234,0.2);
  animation: sp-22-morph 3s ease-in-out infinite, sp-22-spin 6s linear infinite;
}

@keyframes sp-22-morph {
  0%,
    100% {
    border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%;
  }

  20% {
    border-radius: 30% 60% 70% 40% / 50% 60% 30% 60%;
  }

  40% {
    border-radius: 70% 30% 50% 50% / 30% 70% 60% 40%;
  }

  60% {
    border-radius: 40% 60% 30% 70% / 70% 40% 50% 60%;
  }

  80% {
    border-radius: 50% 50% 60% 40% / 40% 50% 70% 60%;
  }
}

@keyframes sp-22-spin {
  to {
    transform: rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-22__blob {
    animation: none;
    border-radius: 50%;
  }
}
```
