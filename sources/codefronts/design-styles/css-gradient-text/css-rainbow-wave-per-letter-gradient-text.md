---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-rainbow-wave-per-letter-gradient-text/"
title: "CSS Rainbow Wave Per-Letter Gradient Text"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "Each letter bounces on its own phase-offset translateY wave while carrying a unique hue-stop pair, producing a travelling rainbow wave entirely in CSS."
has_js: "false"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Rainbow Wave Per-Letter Gradient Text
Source: https://codefronts.com/design-styles/css-gradient-text/css-rainbow-wave-per-letter-gradient-text/

Each letter bounces on its own phase-offset translateY wave while carrying a unique hue-stop pair, producing a travelling rainbow wave entirely in CSS.
## HTML
```html
<div class="gt-04">
  <span class="gt-04__label">Rainbow wave per-letter</span>
  <div class="gt-04__wave-wrap" aria-label="RAINBOW">
    <span class="gt-04__letter">R</span>
    <span class="gt-04__letter">A</span>
    <span class="gt-04__letter">I</span>
    <span class="gt-04__letter">N</span>
    <span class="gt-04__letter">B</span>
    <span class="gt-04__letter">O</span>
    <span class="gt-04__letter">W</span>
  </div>
  <p class="gt-04__subtitle">Per-letter hue offset animation</p>
  <div class="gt-04__bar"></div>
</div>
```
## CSS
```css
.gt-04,
.gt-04 *,
.gt-04 *::before,
.gt-04 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-04 {
  --bg: #f8f4f0;
  font-family: 'DM Sans', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2.5rem;
  padding: 3rem 2rem;
}

.gt-04__label {
  font-size: .7rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #bbb;
}

.gt-04__wave-wrap {
  display: flex;
  gap: 0;
}

.gt-04__letter {
  font-size: clamp(3rem, 11vw, 7.5rem);
  font-weight: 900;
  line-height: 1;
  display: inline-block;
  background: linear-gradient(180deg,
      hsl(calc(var(--hue) + 0deg), 90%, 55%) 0%,
      hsl(calc(var(--hue) + 60deg), 90%, 45%) 100%
    );
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-04-wave 2.4s ease-in-out infinite;
}
/* stagger each letter's hue + delay */

.gt-04__letter:nth-child(1) {
  --hue: 0deg;
  animation-delay: 0s;
}

.gt-04__letter:nth-child(2) {
  --hue: 30deg;
  animation-delay: -.2s;
}

.gt-04__letter:nth-child(3) {
  --hue: 60deg;
  animation-delay: -.4s;
}

.gt-04__letter:nth-child(4) {
  --hue: 90deg;
  animation-delay: -.6s;
}

.gt-04__letter:nth-child(5) {
  --hue: 120deg;
  animation-delay: -.8s;
}

.gt-04__letter:nth-child(6) {
  --hue: 150deg;
  animation-delay: -1s;
}

.gt-04__letter:nth-child(7) {
  --hue: 180deg;
  animation-delay: -1.2s;
}

.gt-04__subtitle {
  font-size: clamp(1rem, 2.5vw, 1.3rem);
  font-weight: 700;
  color: #ccc;
  letter-spacing: .1em;
}

.gt-04__bar {
  width: min(500px, 80vw);
  height: 6px;
  border-radius: 3px;
  background: linear-gradient(90deg,
      #ff595e, #ffca3a, #6a4c93, #1982c4, #8ac926, #ff595e);
  background-size: 200% 100%;
  animation: gt-04-barscroll 3s linear infinite;
}

@keyframes gt-04-wave {
  0%,
    100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-14px);
  }
}

@keyframes gt-04-barscroll {
  0% {
    background-position: 0% center;
  }

  100% {
    background-position: 200% center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-04__letter,
    .gt-04__bar {
    animation: none;
    transform: none;
  }
}
```
