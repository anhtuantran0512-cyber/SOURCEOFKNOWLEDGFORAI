---
source: "codefronts"
url: "https://codefronts.com/motion/css-animated-buttons/css-3d-press-effect-button/"
title: "CSS 3D Press Effect Button"
section: "motion"
category: "css-animated-buttons"
category_name: "CSS Animated Buttons"
description: "A tactile 3D button that physically sinks into its own raised platform on click, simulating a keycap-style press using CSS transforms and layered box-shadows."
has_js: "false"
---

Here's a working CSS Animated Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS 3D Press Effect Button
Source: https://codefronts.com/motion/css-animated-buttons/css-3d-press-effect-button/

A tactile 3D button that physically sinks into its own raised platform on click, simulating a keycap-style press using CSS transforms and layered box-shadows.
## HTML
```html
<div class="ab-05">
  <p class="ab-05__label">Click or tap the buttons</p>
  <div class="ab-05__row">
    <button class="ab-05__btn ab-05__btn--indigo">Purchase Now</button>
    <button class="ab-05__btn ab-05__btn--emerald">Download App</button>
    <button class="ab-05__btn ab-05__btn--rose">Delete File</button>
  </div>
</div>
```
## CSS
```css
.ab-05,
.ab-05 *,
.ab-05 *::before,
.ab-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ab-05 ::selection {
  background: #4338ca;
  color: #fff;
}

.ab-05 {
  font-family: system-ui,sans-serif;
  background: #f8fafc;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2.5rem;
  padding: 2rem;
}

.ab-05__label {
  font-size: .78rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #64748b;
}

.ab-05__row {
  display: flex;
  gap: 1.25rem;
  flex-wrap: wrap;
  justify-content: center;
}

.ab-05__btn {
  --face: #6366f1;
  --depth: #3730a3;
  position: relative;
  padding: .85rem 2.2rem;
  font-size: 1rem;
  font-weight: 800;
  color: #fff;
  background: var(--face);
  border: none;
  border-radius: 10px;
  cursor: pointer;
  outline: none;
  letter-spacing: .03em;
  box-shadow: 0 6px 0 var(--depth),0 8px 12px rgba(0,0,0,.18);
  transition: transform .08s,box-shadow .08s;
  will-change: transform;
  user-select: none;
}

.ab-05__btn--indigo {
  --face: #6366f1;
  --depth: #3730a3;
}

.ab-05__btn--emerald {
  --face: #10b981;
  --depth: #065f46;
}

.ab-05__btn--rose {
  --face: #f43f5e;
  --depth: #9f1239;
}

.ab-05__btn:hover {
  filter: brightness(1.05);
}

.ab-05__btn:active {
  transform: translateY(4px);
  box-shadow: 0 2px 0 var(--depth),0 4px 6px rgba(0,0,0,.12);
}

@media (prefers-reduced-motion: reduce) {
  .ab-05__btn {
    transition: none;
  }
}
```
