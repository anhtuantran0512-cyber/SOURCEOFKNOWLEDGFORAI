---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/neon-text-outline-stroke-animation/"
title: "Neon Text Outline Stroke Animation"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "Hollow letters whose interiors stay dark while only the glass border glows — using -webkit-text-stroke — then an animated 'power-on' that lights the outline…"
has_js: "false"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Text Outline Stroke Animation
Source: https://codefronts.com/motion/css-neon-text-effect/neon-text-outline-stroke-animation/

Hollow letters whose interiors stay dark while only the glass border glows — using -webkit-text-stroke — then an animated 'power-on' that lights the outline segment by segment. The exact hollow-tube look devs search for.
## HTML
```html
<div class="cnt-09">
  <h2 class="cnt-09__word" aria-label="VOLTAGE">
    <span style="--i:0">V</span><span style="--i:1">O</span><span style="--i:2">L</span><span style="--i:3">T</span><span style="--i:4">A</span><span style="--i:5">G</span><span style="--i:6">E</span>
  </h2>
</div>
```
## CSS
```css
.cnt-09,
.cnt-09 *,
.cnt-09 *::before,
.cnt-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-09 ::selection {
  background: oklch(0.85 0.18 85);
  color: #140f02;
}

.cnt-09 {
  --accent: oklch(0.85 0.19 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: radial-gradient(110% 110% at 50% 30%,#12100a,#060503);
}

.cnt-09__word {
  display: flex;
  gap: .04em;
  font-size: clamp(52px,13vw,128px);
  font-weight: 900;
  letter-spacing: .02em;
}

.cnt-09__word span {
  color: transparent;
  -webkit-text-fill-color: transparent;
  -webkit-text-stroke: 2px color-mix(in oklch,var(--accent) 22%,#2a2410);
  animation: cnt-09-strike 1.2s ease forwards;
  animation-delay: calc(var(--i) * .16s);
}

@keyframes cnt-09-strike {
  0% {
    -webkit-text-stroke-color: color-mix(in oklch,var(--accent) 18%,#2a2410);
    text-shadow: none;
  }

  55% {
    -webkit-text-stroke-color: #fff;
    text-shadow: 0 0 6px #fff,0 0 16px var(--accent);
  }

  100% {
    -webkit-text-stroke-color: var(--accent);
    text-shadow: 0 0 5px #fff,0 0 14px var(--accent),0 0 34px var(--accent),0 0 66px var(--accent);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cnt-09__word span {
    animation: none;
    -webkit-text-stroke-color: var(--accent);
    text-shadow: 0 0 5px #fff,0 0 14px var(--accent),0 0 34px var(--accent);
  }
}
```

## JavaScript
```js
/* No JavaScript — hollow -webkit-text-stroke + a per-letter power-on @keyframes. */
```
