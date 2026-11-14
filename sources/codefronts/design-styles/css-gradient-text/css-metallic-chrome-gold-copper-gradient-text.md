---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-metallic-chrome-gold-copper-gradient-text/"
title: "CSS Metallic Chrome Gold Copper Gradient Text"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "Vertical multi-stop linear gradients mimic the specular highlights of chrome, gold, and copper metal surfaces clipped to display text."
has_js: "false"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Metallic Chrome Gold Copper Gradient Text
Source: https://codefronts.com/design-styles/css-gradient-text/css-metallic-chrome-gold-copper-gradient-text/

Vertical multi-stop linear gradients mimic the specular highlights of chrome, gold, and copper metal surfaces clipped to display text.
## HTML
```html
<div class="gt-08">
  <span class="gt-08__label">Metallic gradient text</span>
  <div class="gt-08__chrome">CHROME</div>
  <div class="gt-08__divider"></div>
  <div class="gt-08__gold">GOLD</div>
  <div class="gt-08__divider"></div>
  <div class="gt-08__copper">COPPER</div>
</div>
```
## CSS
```css
.gt-08,
.gt-08 *,
.gt-08 *::before,
.gt-08 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-08 {
  --bg: #0c0c0c;
  font-family: 'Bebas Neue', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3rem;
  padding: 3rem 2rem;
}

.gt-08__label {
  font-size: .65rem;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: #333;
  font-family: monospace;
}

.gt-08__chrome {
  font-size: clamp(4rem, 15vw, 10rem);
  font-weight: 400;
  line-height: 1;
  letter-spacing: .08em;
  background: linear-gradient(180deg,
      #ffffff 0%,
      #e8e8e8 15%,
      #a0a0a0 30%,
      #ffffff 45%,
      #707070 55%,
      #c8c8c8 70%,
      #404040 85%,
      #b0b0b0 100%
    );
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-08-shimmer 3s ease-in-out infinite;
}

.gt-08__gold {
  font-size: clamp(2rem, 8vw, 5rem);
  font-weight: 400;
  line-height: 1;
  letter-spacing: .1em;
  background: linear-gradient(180deg,
      #fff4d0 0%,
      #f5c842 15%,
      #c8962a 30%,
      #ffe680 50%,
      #b07c20 65%,
      #e6b830 80%,
      #7a5010 100%
    );
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-08-shimmer 4s ease-in-out infinite reverse;
}

.gt-08__copper {
  font-size: clamp(1.5rem, 5vw, 3rem);
  font-weight: 400;
  line-height: 1;
  letter-spacing: .12em;
  background: linear-gradient(180deg,
      #ffcba4 0%,
      #cd7a3a 20%,
      #a0522d 40%,
      #e8955a 55%,
      #7a3a18 70%,
      #d4814a 85%,
      #8b4513 100%
    );
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-08-shimmer 5s ease-in-out infinite;
}

.gt-08__divider {
  width: 200px;
  height: 1px;
  background: linear-gradient(90deg, transparent, #ffffff30, transparent);
}

@keyframes gt-08-shimmer {
  0%,
    100% {
    background-position: center 0%;
  }

  50% {
    background-position: center 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-08__chrome,
    .gt-08__gold,
    .gt-08__copper {
    animation: none;
  }
}
```
