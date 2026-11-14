---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-animated-gradient-text-flow/"
title: "CSS Animated Gradient Text Flow"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "A flowing rainbow gradient sweeps across bold display text using a horizontally-extended linear-gradient and background-position animation for a seamless loop."
has_js: "false"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Gradient Text Flow
Source: https://codefronts.com/design-styles/css-gradient-text/css-animated-gradient-text-flow/

A flowing rainbow gradient sweeps across bold display text using a horizontally-extended linear-gradient and background-position animation for a seamless loop.
## HTML
```html
<div class="gt-01">
  <span class="gt-01__label">Animated gradient text</span>
  <h1 class="gt-01__hero">CHROMATIC</h1>
  <p class="gt-01__subtitle">Infinite colour in motion</p>
  <div class="gt-01__words">
    <span class="gt-01__word">Design</span>
    <span class="gt-01__word">Create</span>
    <span class="gt-01__word">Inspire</span>
    <span class="gt-01__word">Build</span>
    <span class="gt-01__word">Ship</span>
  </div>
</div>
```
## CSS
```css
.gt-01,
.gt-01 *,
.gt-01 *::before,
.gt-01 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-01 {
  --bg: #0a0a0f;
  --c1: #ff6b6b;
  --c2: #ffd93d;
  --c3: #6bcb77;
  --c4: #4d96ff;
  --c5: #ff6bcd;
  font-family: 'Syne', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3rem;
  padding: 3rem 2rem;
}

.gt-01__label {
  font-size: .75rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #444;
}

.gt-01__hero {
  font-size: clamp(3rem, 12vw, 8rem);
  font-weight: 800;
  line-height: 1;
  background: linear-gradient(90deg, var(--c1), var(--c2), var(--c3), var(--c4), var(--c5), var(--c1));
  background-size: 300% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-01-flow 4s linear infinite;
}

.gt-01__subtitle {
  font-size: clamp(1rem, 3vw, 1.5rem);
  font-weight: 700;
  background: linear-gradient(90deg, var(--c4), var(--c5), var(--c1), var(--c2));
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-01-flow 6s linear infinite reverse;
  letter-spacing: .05em;
}

.gt-01__words {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem 2rem;
  justify-content: center;
}

.gt-01__word {
  font-size: clamp(1.4rem, 4vw, 2.2rem);
  font-weight: 800;
  background: linear-gradient(90deg, var(--c1), var(--c2), var(--c3), var(--c4), var(--c5), var(--c1));
  background-size: 300% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-01-flow 4s linear infinite;
}

.gt-01__word:nth-child(2) {
  animation-delay: -.8s;
}

.gt-01__word:nth-child(3) {
  animation-delay: -1.6s;
}

.gt-01__word:nth-child(4) {
  animation-delay: -2.4s;
}

.gt-01__word:nth-child(5) {
  animation-delay: -3.2s;
}

@keyframes gt-01-flow {
  0% {
    background-position: 0% center;
  }

  100% {
    background-position: 300% center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-01__hero,
    .gt-01__subtitle,
    .gt-01__word {
    animation: none;
    background-position: 0% center;
  }
}
```
