---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-conic-gradient-text-hue-spin/"
title: "CSS Conic Gradient Text Hue Spin"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "Full-spectrum hue rotation applied to conic-gradient-filled text, creating a continuously spinning rainbow prism effect driven by a CSS filter animation."
has_js: "false"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Conic Gradient Text Hue Spin
Source: https://codefronts.com/design-styles/css-gradient-text/css-conic-gradient-text-hue-spin/

Full-spectrum hue rotation applied to conic-gradient-filled text, creating a continuously spinning rainbow prism effect driven by a CSS filter animation.
## HTML
```html
<div class="gt-03">
  <span class="gt-03__label">Conic gradient text</span>
  <h1 class="gt-03__conic">PRISM</h1>
  <p class="gt-03__sub">Full-spectrum hue rotation</p>
  <div class="gt-03__trio">
    <div class="gt-03__item">
      <span class="gt-03__big">RED</span>
      <span class="gt-03__caption">0°</span>
    </div>
    <div class="gt-03__item">
      <span class="gt-03__big">GREEN</span>
      <span class="gt-03__caption">120°</span>
    </div>
    <div class="gt-03__item">
      <span class="gt-03__big">BLUE</span>
      <span class="gt-03__caption">240°</span>
    </div>
  </div>
</div>
```
## CSS
```css
.gt-03,
.gt-03 *,
.gt-03 *::before,
.gt-03 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-03 {
  --bg: #111118;
  font-family: 'Plus Jakarta Sans', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3rem;
  padding: 3rem 2rem;
}

.gt-03__label {
  font-size: .7rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #555;
}

.gt-03__conic {
  font-size: clamp(3rem, 12vw, 8rem);
  font-weight: 900;
  line-height: 1;
  background: conic-gradient(
      from 0deg,
      #ff0080, #ff8c00, #ffe100, #40ff00,
      #00cfff, #8000ff, #ff0080
    );
  background-size: 100% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-03-spin 3s linear infinite;
}

.gt-03__sub {
  font-size: clamp(1rem, 3vw, 1.6rem);
  font-weight: 800;
  background: conic-gradient(from 180deg, #ff8c00, #ffe100, #40ff00, #00cfff, #8000ff, #ff8c00);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-03-spin 5s linear infinite reverse;
  letter-spacing: .04em;
}

.gt-03__trio {
  display: flex;
  gap: 2.5rem;
  flex-wrap: wrap;
  justify-content: center;
}

.gt-03__item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .5rem;
}

.gt-03__big {
  font-size: clamp(2rem, 6vw, 4rem);
  font-weight: 900;
  background: conic-gradient(from 90deg, #ff0080, #ff8c00, #ffe100, #40ff00, #00cfff, #ff0080);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-03-spin 4s linear infinite;
}

.gt-03__item:nth-child(2) .gt-03__big {
  animation-delay: -1.3s;
}

.gt-03__item:nth-child(3) .gt-03__big {
  animation-delay: -2.6s;
}

.gt-03__caption {
  font-size: .65rem;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: #555;
}

@keyframes gt-03-spin {
  0% {
    filter: hue-rotate(0deg);
  }

  100% {
    filter: hue-rotate(360deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-03__conic,
    .gt-03__sub,
    .gt-03__big {
    animation: none;
  }
}
```
