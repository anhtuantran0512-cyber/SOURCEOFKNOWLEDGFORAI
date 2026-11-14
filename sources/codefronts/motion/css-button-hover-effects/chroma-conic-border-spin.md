---
source: "codefronts"
url: "https://codefronts.com/motion/css-button-hover-effects/chroma-conic-border-spin/"
title: "Chroma Conic Border Spin"
section: "motion"
category: "css-button-hover-effects"
category_name: "CSS Button Hover Effects"
description: "A dark premium CTA wrapped in a razor-thin conic-gradient border that spins continuously like a rotating light source — the AI/fintech 'live' look."
has_js: "false"
---

Here's a working CSS Button Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Chroma Conic Border Spin
Source: https://codefronts.com/motion/css-button-hover-effects/chroma-conic-border-spin/

A dark premium CTA wrapped in a razor-thin conic-gradient border that spins continuously like a rotating light source — the AI/fintech 'live' look. Uses a typed @property angle.
## HTML
```html
<div class="bhe-08-group">
<section class="bhe-08a" aria-label="Conic border spin button">
  <button class="bhe-08a__btn" type="button"><span>Launch app</span></button>
</section>
<section class="bhe-08b" aria-label="Dual arc border button">
  <button class="bhe-08b__btn" type="button"><span>Connect wallet</span></button>
</section>
</div>
```
## CSS
```css
.bhe-08-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-wrap: wrap;
}

.bhe-08-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

@property --bhe-08a-angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.bhe-08a,
.bhe-08a *,
.bhe-08a *::before,
.bhe-08a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-08a {
  --card: #12101c;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #08070f;
}

.bhe-08a__btn {
  position: relative;
  isolation: isolate;
  font-size: 16px;
  font-weight: 700;
  color: #fff;
  padding: 16px 38px;
  border: none;
  border-radius: 14px;
  cursor: pointer;
  background: var(--card);
  transition: transform .2s;
}

.bhe-08a__btn span {
  position: relative;
  z-index: 1;
}

.bhe-08a__btn::before {
  content: "";
  position: absolute;
  inset: -2px;
  border-radius: 16px;
  z-index: 0;
  background: conic-gradient(from var(--bhe-08a-angle),#22e3ff,#7c5cff,#ff2bd6,#22e3ff);
  animation: bhe-08a-spin 4s linear infinite;
}

.bhe-08a__btn::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 14px;
  background: var(--card);
  z-index: 0;
}

.bhe-08a__btn:hover {
  transform: translateY(-2px);
}

.bhe-08a__btn:hover::before {
  animation-duration: 1.6s;
  filter: brightness(1.25) saturate(1.2);
}

.bhe-08a__btn:focus-visible {
  outline: 3px solid #22e3ff;
  outline-offset: 4px;
}

@keyframes bhe-08a-spin {
  to {
    --bhe-08a-angle: 360deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-08a__btn::before {
    animation: none;
  }
}

@property --bhe-08b-angle {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.bhe-08b,
.bhe-08b *,
.bhe-08b *::before,
.bhe-08b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.bhe-08b {
  --card: #0c1618;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 56px 24px;
  background: #050b0c;
}

.bhe-08b__btn {
  position: relative;
  isolation: isolate;
  font-size: 16px;
  font-weight: 700;
  color: #eafff8;
  padding: 16px 40px;
  border: none;
  border-radius: 9999px;
  cursor: pointer;
  background: var(--card);
  transition: transform .2s;
}

.bhe-08b__btn span {
  position: relative;
  z-index: 1;
}

.bhe-08b__btn::before {
  content: "";
  position: absolute;
  inset: -2px;
  border-radius: 9999px;
  z-index: 0;
  background: conic-gradient(from var(--bhe-08b-angle),transparent 0 25%,#2ff5c8 35% 40%,transparent 50% 75%,#2ff5c8 85% 90%,transparent);
  animation: bhe-08b-spin 3s linear infinite;
}

.bhe-08b__btn::after {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: 9999px;
  background: var(--card);
  z-index: 0;
}

.bhe-08b__btn:hover {
  transform: translateY(-2px);
}

.bhe-08b__btn:hover::before {
  animation-duration: 1.2s;
}

.bhe-08b__btn:focus-visible {
  outline: 3px solid #2ff5c8;
  outline-offset: 4px;
}

@keyframes bhe-08b-spin {
  to {
    --bhe-08b-angle: 360deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bhe-08b__btn::before {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — pure CSS; all designs for this title are driven entirely by the css field. */
```
