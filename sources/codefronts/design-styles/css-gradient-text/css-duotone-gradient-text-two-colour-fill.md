---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-duotone-gradient-text-two-colour-fill/"
title: "CSS Duotone Gradient Text Two-Colour Fill"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "Bold typography filled with two-stop duotone linear gradients, with animated letter-spacing expansion that makes each pairing feel alive and cinematic."
has_js: "false"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Duotone Gradient Text Two-Colour Fill
Source: https://codefronts.com/design-styles/css-gradient-text/css-duotone-gradient-text-two-colour-fill/

Bold typography filled with two-stop duotone linear gradients, with animated letter-spacing expansion that makes each pairing feel alive and cinematic.
## HTML
```html
<div class="gt-10">
  <span class="gt-10__label">Duotone gradient text</span>
  <div class="gt-10__pair">
    <div class="gt-10__duo gt-10__duo--blue-red">DUOTONE</div>
    <div class="gt-10__duo gt-10__duo--green-violet">BLEND MODE</div>
    <div class="gt-10__duo gt-10__duo--yellow-magenta">TWO COLOUR GRADIENT</div>
  </div>
  <span class="gt-10__caption">Two-stop linear gradient fills</span>
  <div class="gt-10__swatch-row">
    <div class="gt-10__swatch"></div>
    <div class="gt-10__swatch"></div>
    <div class="gt-10__swatch"></div>
  </div>
</div>
```
## CSS
```css
.gt-10,
.gt-10 *,
.gt-10 *::before,
.gt-10 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-10 {
  --bg: #f5f5f0;
  font-family: 'Inter', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3rem;
  padding: 3rem 2rem;
}

.gt-10__label {
  font-size: .7rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #ccc;
}

.gt-10__pair {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
  width: 100%;
}

.gt-10__duo {
  font-size: clamp(3rem, 12vw, 8rem);
  font-weight: 900;
  line-height: 1;
  letter-spacing: -.02em;
}

.gt-10__duo--blue-red {
  background: linear-gradient(90deg, #003fff 0%, #ff003f 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-10-expand 5s ease-in-out infinite alternate;
}

.gt-10__duo--green-violet {
  background: linear-gradient(90deg, #00c896 0%, #6600ff 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-size: clamp(2rem, 8vw, 5rem);
  animation: gt-10-expand 5s ease-in-out infinite alternate reverse;
}

.gt-10__duo--yellow-magenta {
  background: linear-gradient(90deg, #f5c800 0%, #ff00aa 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  font-size: clamp(1.5rem, 5vw, 3rem);
  animation: gt-10-expand 5s ease-in-out infinite alternate;
}

.gt-10__caption {
  font-size: .65rem;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: #bbb;
}

.gt-10__swatch-row {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.gt-10__swatch {
  width: 60px;
  height: 8px;
  border-radius: 4px;
}

.gt-10__swatch:nth-child(1) {
  background: linear-gradient(90deg, #003fff, #ff003f);
}

.gt-10__swatch:nth-child(2) {
  background: linear-gradient(90deg, #00c896, #6600ff);
}

.gt-10__swatch:nth-child(3) {
  background: linear-gradient(90deg, #f5c800, #ff00aa);
}

@keyframes gt-10-expand {
  0% {
    letter-spacing: -.02em;
  }

  100% {
    letter-spacing: .08em;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-10__duo {
    animation: none;
  }
}
```
