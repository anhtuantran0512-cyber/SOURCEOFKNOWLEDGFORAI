---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/low-inp-compositor-neon-animation/"
title: "Low-INP Compositor Neon Animation"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "A continuously-pulsing neon headline engineered to keep Interaction-to-Next-Paint low: the glow is a pre-rendered ::after layer that animates only opacity —…"
has_js: "false"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Low-INP Compositor Neon Animation
Source: https://codefronts.com/motion/css-neon-text-effect/low-inp-compositor-neon-animation/

A continuously-pulsing neon headline engineered to keep Interaction-to-Next-Paint low: the glow is a pre-rendered ::after layer that animates only opacity — never blur — so the pulse lives on the compositor, off the main thread.
## HTML
```html
<div class="cnt-15">
  <h2 class="cnt-15__h" data-text="LOW INP">LOW INP</h2>
  <p class="cnt-15__note">pulse animates opacity only — off the main thread</p>
</div>
```
## CSS
```css
.cnt-15,
.cnt-15 *,
.cnt-15 *::before,
.cnt-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-15 ::selection {
  background: oklch(0.86 0.18 175);
  color: #03130f;
}

.cnt-15 {
  --accent: oklch(0.86 0.18 175);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 20px;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: radial-gradient(120% 120% at 50% 30%,#08110f,#040807);
}

.cnt-15__h {
  position: relative;
  font-size: clamp(46px,12vw,112px);
  font-weight: 900;
  letter-spacing: .05em;
  color: #eafffb;
  text-shadow: 0 0 2px #fff;
}

.cnt-15__h::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  pointer-events: none;
  color: var(--accent);
  will-change: opacity;
  text-shadow: 0 0 6px #fff,0 0 16px var(--accent),0 0 40px var(--accent),0 0 84px color-mix(in oklch,var(--accent) 55%,transparent);
  animation: cnt-15-pulse 2s ease-in-out infinite;
}

@keyframes cnt-15-pulse {
  0%,
    100% {
    opacity: .4;
  }

  50% {
    opacity: 1;
  }
}

.cnt-15__note {
  font: 12px ui-monospace,Menlo,monospace;
  letter-spacing: .18em;
  color: #5f7a74;
}

@media (prefers-reduced-motion: reduce) {
  .cnt-15__h::after {
    animation: none;
    opacity: 1;
  }
}
```

## JavaScript
```js
/* No JavaScript — the glow is a baked ::after layer; only its opacity animates. */
```
