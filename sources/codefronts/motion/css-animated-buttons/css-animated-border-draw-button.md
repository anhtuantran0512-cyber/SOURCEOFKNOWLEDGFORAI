---
source: "codefronts"
url: "https://codefronts.com/motion/css-animated-buttons/css-animated-border-draw-button/"
title: "CSS Animated Border Draw Button"
section: "motion"
category: "css-animated-buttons"
category_name: "CSS Animated Buttons"
description: "Hover triggers a border that draws itself clockwise around the button perimeter using CSS clip-path transitions on pseudo-elements — no SVG required."
has_js: "false"
---

Here's a working CSS Animated Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Animated Border Draw Button
Source: https://codefronts.com/motion/css-animated-buttons/css-animated-border-draw-button/

Hover triggers a border that draws itself clockwise around the button perimeter using CSS clip-path transitions on pseudo-elements — no SVG required.
## HTML
```html
<div class="ab-04">
  <p class="ab-04__label">Hover to draw the border</p>
  <div class="ab-04__row">
    <button class="ab-04__btn"><span>Explore Docs</span></button>
    <button class="ab-04__btn ab-04__btn--green"><span>Start Building</span></button>
    <button class="ab-04__btn ab-04__btn--rose"><span>Contact Sales</span></button>
  </div>
</div>
```
## CSS
```css
.ab-04,
.ab-04 *,
.ab-04 *::before,
.ab-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ab-04 ::selection {
  background: #6366f1;
  color: #fff;
}

.ab-04 {
  --accent: #6366f1;
  --fill-bg: #6366f1;
  font-family: system-ui,sans-serif;
  background: #09090f;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2.5rem;
  padding: 2rem;
}

.ab-04__label {
  font-size: .78rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #818cf8;
  opacity: .65;
}

.ab-04__row {
  display: flex;
  gap: 1.25rem;
  flex-wrap: wrap;
  justify-content: center;
}

.ab-04__btn {
  position: relative;
  padding: .85rem 2.2rem;
  font-size: .95rem;
  font-weight: 700;
  color: #c7d2fe;
  background: transparent;
  border: none;
  outline: none;
  cursor: pointer;
  letter-spacing: .04em;
  transition: color .4s,background .4s;
}

.ab-04__btn--green {
  --accent: #10b981;
  --fill-bg: #10b981;
  color: #6ee7b7;
}

.ab-04__btn--rose {
  --accent: #f43f5e;
  --fill-bg: #f43f5e;
  color: #fda4af;
}

.ab-04__btn span {
  position: relative;
  z-index: 1;
}

.ab-04__btn::before,
.ab-04__btn::after {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
}
/* top + right */

.ab-04__btn::before {
  border-top: 2px solid var(--accent);
  border-right: 2px solid var(--accent);
  width: 0;
  height: 0;
  transition: width .2s ease,height .2s ease .2s;
}
/* bottom + left */

.ab-04__btn::after {
  border-bottom: 2px solid var(--accent);
  border-left: 2px solid var(--accent);
  width: 0;
  height: 0;
  top: auto;
  left: auto;
  right: 0;
  bottom: 0;
  transition: width .2s ease .4s,height .2s ease .2s;
}

.ab-04__btn:hover::before {
  width: 100%;
  height: 100%;
}

.ab-04__btn:hover::after {
  width: 100%;
  height: 100%;
}

.ab-04__btn:hover {
  color: #fff;
  background: rgba(99,102,241,.12);
}

.ab-04__btn--green:hover {
  background: rgba(16,185,129,.12);
}

.ab-04__btn--rose:hover {
  background: rgba(244,63,94,.12);
}

@media (prefers-reduced-motion: reduce) {
  .ab-04__btn::before,
    .ab-04__btn::after {
    transition: none;
    width: 100%;
    height: 100%;
  }
}
```
