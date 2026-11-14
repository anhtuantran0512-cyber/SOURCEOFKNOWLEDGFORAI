---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-neon-pulse-gradient-text-glow/"
title: "CSS Neon Pulse Gradient Text Glow"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "A scrolling cyan-magenta-lime gradient combined with a pulsing drop-shadow glow recreates the flickering neon sign aesthetic entirely in CSS."
has_js: "false"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Neon Pulse Gradient Text Glow
Source: https://codefronts.com/design-styles/css-gradient-text/css-neon-pulse-gradient-text-glow/

A scrolling cyan-magenta-lime gradient combined with a pulsing drop-shadow glow recreates the flickering neon sign aesthetic entirely in CSS.
## HTML
```html
<div class="gt-06">
  <span class="gt-06__label">Neon pulse gradient</span>
  <h1 class="gt-06__neon">NEON</h1>
  <div class="gt-06__bar">
    <div class="gt-06__seg"></div>
    <div class="gt-06__seg"></div>
    <div class="gt-06__seg"></div>
    <div class="gt-06__seg"></div>
    <div class="gt-06__seg"></div>
  </div>
  <p class="gt-06__tagline">Glowing gradient pulse</p>
</div>
```
## CSS
```css
.gt-06,
.gt-06 *,
.gt-06 *::before,
.gt-06 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-06 {
  --bg: #030a10;
  --n1: #00f5ff;
  --n2: #ff00e4;
  --n3: #b8ff00;
  font-family: 'Exo 2', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2.5rem;
  padding: 3rem 2rem;
  position: relative;
  overflow: hidden;
}

.gt-06::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse 60% 40% at 20% 50%, #00f5ff0a, transparent), radial-gradient(ellipse 60% 40% at 80% 50%, #ff00e40a, transparent);
  pointer-events: none;
}

.gt-06__label {
  font-family: 'Rajdhani', sans-serif;
  font-size: .7rem;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: #00f5ff30;
}

.gt-06__neon {
  font-size: clamp(3rem, 12vw, 8rem);
  font-weight: 900;
  line-height: 1;
  background: linear-gradient(90deg, var(--n1), var(--n2), var(--n3), var(--n1));
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 0 20px #00f5ff80) drop-shadow(0 0 40px #ff00e440);
  animation: gt-06-neonflow 4s linear infinite, gt-06-pulse 2s ease-in-out infinite;
  letter-spacing: .08em;
}

.gt-06__bar {
  display: flex;
  gap: .5rem;
  align-items: center;
}

.gt-06__seg {
  height: 4px;
  border-radius: 2px;
  background: linear-gradient(90deg, var(--n1), var(--n2));
  animation: gt-06-barpulse 1.5s ease-in-out infinite;
}

.gt-06__seg:nth-child(1) {
  width: 40px;
  animation-delay: 0s;
}

.gt-06__seg:nth-child(2) {
  width: 80px;
  animation-delay: -.3s;
}

.gt-06__seg:nth-child(3) {
  width: 120px;
  animation-delay: -.6s;
  background: linear-gradient(90deg, var(--n2), var(--n3));
}

.gt-06__seg:nth-child(4) {
  width: 80px;
  animation-delay: -.9s;
}

.gt-06__seg:nth-child(5) {
  width: 40px;
  animation-delay: -1.2s;
}

.gt-06__tagline {
  font-family: 'Rajdhani', sans-serif;
  font-size: clamp(.9rem, 2.5vw, 1.2rem);
  font-weight: 700;
  letter-spacing: .25em;
  text-transform: uppercase;
  background: linear-gradient(90deg, var(--n2), var(--n3));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-06-fade 2s ease-in-out infinite alternate;
}

@keyframes gt-06-neonflow {
  0% {
    background-position: 0% center;
  }

  100% {
    background-position: 200% center;
  }
}

@keyframes gt-06-pulse {
  0%,
    100% {
    filter: drop-shadow(0 0 20px #00f5ff80) drop-shadow(0 0 40px #ff00e440);
  }

  50% {
    filter: drop-shadow(0 0 35px #00f5ffcc) drop-shadow(0 0 70px #ff00e460);
  }
}

@keyframes gt-06-barpulse {
  0%,
    100% {
    opacity: .4;
  }

  50% {
    opacity: 1;
  }
}

@keyframes gt-06-fade {
  0% {
    opacity: .6;
  }

  100% {
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-06__neon,
    .gt-06__seg,
    .gt-06__tagline {
    animation: none;
    filter: none;
  }
}
```
