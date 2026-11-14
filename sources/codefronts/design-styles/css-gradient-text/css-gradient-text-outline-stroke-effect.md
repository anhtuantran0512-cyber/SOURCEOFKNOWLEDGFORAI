---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-gradient-text/css-gradient-text-outline-stroke-effect/"
title: "CSS Gradient Text Outline Stroke Effect"
section: "design-styles"
category: "css-gradient-text"
category_name: "CSS Gradient Text Designs"
description: "A gradient is applied as the stroke colour of outlined text using -webkit-text-stroke combined with background-clip:text, creating crisp gradient-coloured…"
has_js: "false"
---

Here's a working CSS Gradient Text Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Gradient Text Outline Stroke Effect
Source: https://codefronts.com/design-styles/css-gradient-text/css-gradient-text-outline-stroke-effect/

A gradient is applied as the stroke colour of outlined text using -webkit-text-stroke combined with background-clip:text, creating crisp gradient-coloured letterform outlines.
## HTML
```html
<div class="gt-07">
  <span class="gt-07__label">Gradient text stroke / outline</span>
  <div class="gt-07__outlined">OUTLINED</div>
  <div class="gt-07__css-stroke">GRADIENT FILL</div>
  <div class="gt-07__row">
    <span class="gt-07__pill">Purple</span>
    <span class="gt-07__pill">Pink</span>
    <span class="gt-07__pill">Orange</span>
  </div>
</div>
```
## CSS
```css
.gt-07,
.gt-07 *,
.gt-07 *::before,
.gt-07 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.gt-07 {
  --bg: #fff;
  --g1: #7c3aed;
  --g2: #db2777;
  --g3: #ea580c;
  font-family: 'Space Grotesk', sans-serif;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 3rem;
  padding: 3rem 2rem;
}

.gt-07__label {
  font-size: .7rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #ddd;
}
/* Stroke via SVG text linearGradient inside an inline SVG */

.gt-07__svg-wrap {
  width: 100%;
  max-width: 700px;
  overflow: visible;
}

.gt-07__stroke {
  font-family: 'Space Grotesk', sans-serif;
  font-size: clamp(3rem, 12vw, 7rem);
  font-weight: 700;
}
/* CSS-only outline technique using -webkit-text-stroke + transparent fill */

.gt-07__css-stroke {
  font-size: clamp(3rem, 12vw, 7rem);
  font-weight: 700;
  line-height: 1;
  -webkit-text-stroke: 3px transparent;
  background: linear-gradient(135deg, var(--g1), var(--g2), var(--g3));
  background-size: 200% 200%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  /* Paint background behind the text-stroke so stroke uses gradient */
  paint-order: stroke fill;
  animation: gt-07-shift 5s ease-in-out infinite alternate;
}

.gt-07__outlined {
  font-size: clamp(3rem, 12vw, 7rem);
  font-weight: 700;
  line-height: 1;
  -webkit-text-stroke: 4px;
  -webkit-text-stroke-color: transparent;
  background: linear-gradient(90deg, var(--g1), var(--g2), var(--g3), var(--g1));
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gt-07-scroll 4s linear infinite;
  letter-spacing: .05em;
}

.gt-07__row {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
  justify-content: center;
}

.gt-07__pill {
  font-size: clamp(1.2rem, 4vw, 2rem);
  font-weight: 700;
  line-height: 1;
  -webkit-text-stroke: 2px;
  -webkit-text-stroke-color: transparent;
  background: linear-gradient(135deg, var(--g1), var(--g2), var(--g3));
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  padding: .4em .8em;
  border: 2px solid;
  border-image: linear-gradient(135deg, var(--g1), var(--g2), var(--g3)) 1;
  border-radius: 999px;
  /* Compat: border-image doesn't work with border-radius, use outline trick */
  border: none;
  box-shadow: 0 0 0 2px var(--g1);
}

@keyframes gt-07-shift {
  0% {
    background-position: 0% 0%;
  }

  100% {
    background-position: 100% 100%;
  }
}

@keyframes gt-07-scroll {
  0% {
    background-position: 0% center;
  }

  100% {
    background-position: 200% center;
  }
}

@media (prefers-reduced-motion: reduce) {
  .gt-07__css-stroke,
    .gt-07__outlined {
    animation: none;
  }
}
```
