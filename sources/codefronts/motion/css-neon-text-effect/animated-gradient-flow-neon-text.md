---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/animated-gradient-flow-neon-text/"
title: "Animated Gradient-Flow Neon Text"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "A headline whose letters are filled with a living, flowing multi-hue gradient while a matching coloured glow pours off the edges — the animated-gradient neon…"
has_js: "false"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Gradient-Flow Neon Text
Source: https://codefronts.com/motion/css-neon-text-effect/animated-gradient-flow-neon-text/

A headline whose letters are filled with a living, flowing multi-hue gradient while a matching coloured glow pours off the edges — the animated-gradient neon look, built with background-clip:text and a moving background-position.
## HTML
```html
<div class="cnt-19">
  <h2 class="cnt-19__h">AURORA</h2>
</div>
```
## CSS
```css
.cnt-19,
.cnt-19 *,
.cnt-19 *::before,
.cnt-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-19 ::selection {
  background: oklch(0.82 0.16 300);
  color: #0d0416;
}

.cnt-19 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: radial-gradient(120% 120% at 50% 30%,#080b12,#040507);
}

.cnt-19__h {
  font-size: clamp(52px,14vw,140px);
  font-weight: 900;
  letter-spacing: .03em;
  line-height: 1;
  background: linear-gradient(90deg,
      oklch(0.85 0.16 200),oklch(0.8 0.2 300),oklch(0.72 0.24 340),
      oklch(0.85 0.18 90),oklch(0.85 0.16 200));
  background-size: 300% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  filter: drop-shadow(0 0 6px rgba(255,255,255,.5)) drop-shadow(0 0 22px oklch(0.8 0.2 300 / .8)) drop-shadow(0 0 52px oklch(0.75 0.22 320 / .6));
  animation: cnt-19-flow 6s linear infinite;
}

@keyframes cnt-19-flow {
  to {
    background-position: 300% 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cnt-19__h {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a clipped gradient fill flows via background-position; glow is drop-shadow. */
```
