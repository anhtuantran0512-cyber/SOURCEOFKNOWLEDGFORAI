---
source: "codefronts"
url: "https://codefronts.com/motion/css-neon-text-effect/synchronized-box-shadow-text-glow/"
title: "Synchronized Box-Shadow + Text Glow"
section: "motion"
category: "css-neon-text-effect"
category_name: "CSS Neon Text Effects"
description: "A framed sign where the container's box-shadow outline and the text's text-shadow glow are driven from one variable so they light in perfect lockstep — the…"
has_js: "false"
---

Here's a working CSS Neon Text Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Synchronized Box-Shadow + Text Glow
Source: https://codefronts.com/motion/css-neon-text-effect/synchronized-box-shadow-text-glow/

A framed sign where the container's box-shadow outline and the text's text-shadow glow are driven from one variable so they light in perfect lockstep — the snippet pair devs want when a border and its label must match exactly.
## HTML
```html
<div class="cnt-11">
  <div class="cnt-11__frame">
    <span class="cnt-11__label">VACANCY</span>
  </div>
</div>
```
## CSS
```css
.cnt-11,
.cnt-11 *,
.cnt-11 *::before,
.cnt-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cnt-11 ::selection {
  background: oklch(0.8 0.16 250);
  color: #040a18;
}

.cnt-11 {
  --accent: oklch(0.8 0.17 250);
  --glow: 1;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  background: radial-gradient(110% 110% at 50% 30%,#0a0c14,#040509);
}

.cnt-11__frame {
  position: relative;
  padding: 34px 54px;
  border-radius: 14px;
  cursor: pointer;
  background: #070a12;
  border: 1.5px solid var(--accent);
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.5), inset 0 0 calc(14px * var(--glow)) color-mix(in oklch,var(--accent) 55%,transparent), 0 0 calc(6px * var(--glow)) var(--accent), 0 0 calc(30px * var(--glow)) color-mix(in oklch,var(--accent) 80%,transparent), 0 0 calc(70px * var(--glow)) color-mix(in oklch,var(--accent) 45%,transparent);
  transition: box-shadow .35s,--glow .35s;
}

.cnt-11__label {
  font-size: clamp(34px,8vw,64px);
  font-weight: 800;
  letter-spacing: .14em;
  color: #eef4ff;
  text-shadow: 0 0 calc(5px * var(--glow)) #fff, 0 0 calc(14px * var(--glow)) var(--accent), 0 0 calc(30px * var(--glow)) var(--accent), 0 0 calc(66px * var(--glow)) color-mix(in oklch,var(--accent) 55%,transparent);
  transition: text-shadow .35s;
}

.cnt-11__frame:hover {
  --glow: 1.7;
}

@property --glow {
  syntax: '<number>';
  inherits: true;
  initial-value: 1;
}

@media (prefers-reduced-motion: reduce) {
  .cnt-11__frame,
    .cnt-11__label {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — one --glow token (a registered @property) scales both shadow stacks. */
```
