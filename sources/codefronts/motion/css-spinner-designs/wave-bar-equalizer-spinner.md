---
source: "codefronts"
url: "https://codefronts.com/motion/css-spinner-designs/wave-bar-equalizer-spinner/"
title: "Wave Bar Equalizer Spinner"
section: "motion"
category: "css-spinner-designs"
category_name: "CSS Spinners"
description: "Seven vertical bars oscillate like an audio level meter, scaling from a flat line to full height in a symmetric wave pattern using staggered CSS animation…"
has_js: "false"
---

Here's a working CSS Spinner from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Wave Bar Equalizer Spinner
Source: https://codefronts.com/motion/css-spinner-designs/wave-bar-equalizer-spinner/

Seven vertical bars oscillate like an audio level meter, scaling from a flat line to full height in a symmetric wave pattern using staggered CSS animation delays.
## HTML
```html
<div class="sp-06">
  <div class="sp-06__bars">
    <div class="sp-06__bar"></div>
    <div class="sp-06__bar"></div>
    <div class="sp-06__bar"></div>
    <div class="sp-06__bar"></div>
    <div class="sp-06__bar"></div>
    <div class="sp-06__bar"></div>
    <div class="sp-06__bar"></div>
  </div>
</div>
```
## CSS
```css
.sp-06,
.sp-06 *,
.sp-06 *::before,
.sp-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sp-06 {
  --bg: #020c14;
  --c1: #00e676;
  --c2: #00bcd4;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: var(--bg);
}

.sp-06__bars {
  display: flex;
  align-items: flex-end;
  gap: 5px;
  height: 56px;
}

.sp-06__bar {
  width: 8px;
  border-radius: 4px 4px 2px 2px;
  background: linear-gradient(to top,var(--c1),var(--c2));
  box-shadow: 0 0 6px var(--c1);
  animation: sp-06-eq 1s ease-in-out infinite;
}

.sp-06__bar:nth-child(1) {
  animation-delay: 0s;
  height: 20px;
}

.sp-06__bar:nth-child(2) {
  animation-delay: 0.1s;
  height: 35px;
}

.sp-06__bar:nth-child(3) {
  animation-delay: 0.2s;
  height: 50px;
}

.sp-06__bar:nth-child(4) {
  animation-delay: 0.3s;
  height: 35px;
}

.sp-06__bar:nth-child(5) {
  animation-delay: 0.4s;
  height: 20px;
}

.sp-06__bar:nth-child(6) {
  animation-delay: 0.3s;
  height: 35px;
}

.sp-06__bar:nth-child(7) {
  animation-delay: 0.2s;
  height: 50px;
}

@keyframes sp-06-eq {
  0%,
    100% {
    transform: scaleY(0.3);
  }

  50% {
    transform: scaleY(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sp-06__bar {
    animation: none;
    transform: scaleY(0.6);
  }
}
```
