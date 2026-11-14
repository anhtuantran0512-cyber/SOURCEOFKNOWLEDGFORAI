---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-lava-lamp-radial-gradient-text/"
title: "CSS Lava Lamp Radial Gradient Text"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "A slowly drifting radial gradient simulates molten lava inside the text glyphs, using animated CSS custom properties to move the gradient hotspot."
has_js: "false"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Lava Lamp Radial Gradient Text
Source: https://codefronts.com/design-styles/css-gradient-text/css-lava-lamp-radial-gradient-text/

A slowly drifting radial gradient simulates molten lava inside the text glyphs, using animated CSS custom properties to move the gradient hotspot.
## HTML
```html
<div class="gt-05">
  <span class="gt-05__label">Lava lamp radial gradient</span>
  <h1 class="gt-05__blob">MAGMA</h1>
  <p class="gt-05__tagline">Molten radial gradient text</p>
  <div class="gt-05__orbs">
    <div class="gt-05__orb"></div>
    <div class="gt-05__orb"></div>
    <div class="gt-05__orb"></div>
  </div>
  <span class="gt-05__orb-label">radial motion</span>
</div>
```
## CSS
```css
.gt-05,
.gt-05 *,
.gt-05 *::before,
.gt-05 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-05 {
  --bg: #0d0208;
  --hot1: #ff3b00;
  --hot2: #ff8800;
  --hot3: #ffcc00;
  --cool: #3b0a0a;
  font-family: 'Syne', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2.5rem;
  padding: 3rem 2rem;
}

.gt-05__label {
  font-family: 'Syne Mono', monospace;
  font-size: .65rem;
  letter-spacing: .25em;
  text-transform: uppercase;
  color: #ff330040;
}

.gt-05__blob {
  font-size: clamp(3rem, 12vw, 8rem);
  font-weight: 800;
  line-height: 1;
  background: radial-gradient(
      circle at var(--x, 30%) var(--y, 40%),
      var(--hot3) 0%,
      var(--hot2) 25%,
      var(--hot1) 55%,
      #6b0000 100%
    );
  background-size: 200% 200%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-05-blob 6s ease-in-out infinite;
}

.gt-05__tagline {
  font-family: 'Syne Mono', monospace;
  font-size: clamp(.7rem, 2vw, 1rem);
  background: linear-gradient(90deg, var(--hot1), var(--hot2), var(--hot3));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-05-pulse 3s ease-in-out infinite alternate;
  letter-spacing: .15em;
}

.gt-05__orbs {
  display: flex;
  gap: 1.5rem;
  align-items: flex-end;
}

.gt-05__orb {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%, var(--hot3), var(--hot1));
  animation: gt-05-rise 3s ease-in-out infinite;
  position: relative;
}

.gt-05__orb::after {
  content: '';
  position: absolute;
  inset: 15% 20% 40% 20%;
  background: rgba(255,255,255,.25);
  border-radius: 50%;
  transform: rotate(-30deg);
}

.gt-05__orb:nth-child(1) {
  width: 40px;
  height: 40px;
  animation-delay: -.5s;
}

.gt-05__orb:nth-child(2) {
  width: 70px;
  height: 70px;
  animation-delay: -1s;
}

.gt-05__orb:nth-child(3) {
  width: 50px;
  height: 50px;
  animation-delay: -1.8s;
}

.gt-05__orb-label {
  font-family: 'Syne Mono', monospace;
  font-size: .6rem;
  letter-spacing: .1em;
  color: var(--hot2);
  background: linear-gradient(90deg, var(--hot1), var(--hot3));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

@keyframes gt-05-blob {
  0% {
    --x: 30%;
    --y: 40%;
  }

  25% {
    --x: 60%;
    --y: 70%;
  }

  50% {
    --x: 70%;
    --y: 30%;
  }

  75% {
    --x: 40%;
    --y: 60%;
  }

  100% {
    --x: 30%;
    --y: 40%;
  }
}

@keyframes gt-05-pulse {
  0% {
    opacity: .6;
  }

  100% {
    opacity: 1;
  }
}

@keyframes gt-05-rise {
  0%,
    100% {
    transform: translateY(0) scale(1);
  }

  50% {
    transform: translateY(-20px) scale(1.05);
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-05__blob,
    .gt-05__tagline,
    .gt-05__orb {
    animation: none;
  }
}
```
