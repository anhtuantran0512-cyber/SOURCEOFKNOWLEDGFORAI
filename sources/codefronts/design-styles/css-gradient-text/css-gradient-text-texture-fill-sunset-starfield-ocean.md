---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-gradient-text-texture-fill-sunset-starfield-ocean/"
title: "CSS Gradient Text Texture Fill — Sunset Starfield Ocean"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "Multi-stop gradients simulate natural texture fills — a sunset sky, a star-dotted night, and an ocean depth — each clipped to large display text."
has_js: "false"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Text Texture Fill — Sunset Starfield Ocean
Source: https://codefronts.com/design-styles/css-gradient-text/css-gradient-text-texture-fill-sunset-starfield-ocean/

Multi-stop gradients simulate natural texture fills — a sunset sky, a star-dotted night, and an ocean depth — each clipped to large display text.
## HTML
```html
<div class="gt-11">
  <span class="gt-11__label">Texture gradient fill</span>
  <div class="gt-11__sunset">SUNSET</div>
  <div class="gt-11__divider"></div>
  <div class="gt-11__night">STARFIELD</div>
  <div class="gt-11__divider"></div>
  <div class="gt-11__ocean">OCEAN DEPTH</div>
</div>
```
## CSS
```css
.gt-11,
.gt-11 *,
.gt-11 *::before,
.gt-11 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-11 {
  --bg: #111;
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

.gt-11__label {
  font-size: .7rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #444;
}
/* Sunset gradient acting as "image" fill */

.gt-11__sunset {
  font-size: clamp(3rem, 13vw, 9rem);
  font-weight: 900;
  line-height: 1;
  letter-spacing: .02em;
  background: linear-gradient(180deg,
        #1a0533 0%,
        #5c0a7c 15%,
        #c0273a 35%,
        #e8612a 55%,
        #f5a623 75%,
        #ffd700 100%
      );
  background-size: 100% 200%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-11-sunrise 6s ease-in-out infinite alternate;
}
/* Night sky gradient fill */

.gt-11__night {
  font-size: clamp(2rem, 8vw, 5rem);
  font-weight: 800;
  line-height: 1;
  letter-spacing: .06em;
  background: radial-gradient(ellipse at 20% 30%, #ffffff 1px, transparent 1px), radial-gradient(ellipse at 70% 20%, #ffffff 1px, transparent 1px), radial-gradient(ellipse at 50% 60%, #ffffff 1px, transparent 1px), radial-gradient(ellipse at 85% 50%, #ffffff 1px, transparent 1px), linear-gradient(180deg, #03001e 0%, #7303c0 50%, #ec38bc 100%);
  background-size: 80px 80px, 120px 120px, 60px 60px, 100px 100px, 100% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-11-star 4s ease-in-out infinite;
}
/* Ocean gradient fill */

.gt-11__ocean {
  font-size: clamp(1.5rem, 5vw, 3rem);
  font-weight: 800;
  line-height: 1;
  letter-spacing: .1em;
  background: linear-gradient(135deg,
      #006994 0%,
      #0099cc 25%,
      #00d4ff 50%,
      #40e0ff 75%,
      #a0f0ff 100%
    );
  background-size: 200% 200%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-11-ocean 3s ease-in-out infinite alternate;
}

.gt-11__divider {
  width: 3px;
  height: 40px;
  background: linear-gradient(180deg, transparent, #ffffff20, transparent);
  border-radius: 2px;
}

@keyframes gt-11-sunrise {
  0% {
    background-position: center 100%;
  }

  100% {
    background-position: center 0%;
  }
}

@keyframes gt-11-star {
  0%,
    100% {
    background-position: 0 0, 0 0, 0 0, 0 0, 0 0;
  }

  50% {
    background-position: 10px 5px, -10px 8px, 5px -5px, -8px 3px, 0 0;
  }
}

@keyframes gt-11-ocean {
  0% {
    background-position: 0% 0%;
  }

  100% {
    background-position: 100% 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-11__sunset,
    .gt-11__night,
    .gt-11__ocean {
    animation: none;
  }
}
```
