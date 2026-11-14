---
source: "codefronts"
url: "https://codefronts.com/motion/css-animated-buttons/css-background-slide-hover-button/"
title: "CSS Background Slide Hover Button"
section: "motion"
category: "css-animated-buttons"
category_name: "CSS Animated Buttons"
description: "Four directional background-slide hover buttons — left, right, top, and bottom — where a solid fill sweeps across the button face on hover using CSS…"
has_js: "false"
---

Here's a working CSS Animated Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Background Slide Hover Button
Source: https://codefronts.com/motion/css-animated-buttons/css-background-slide-hover-button/

Four directional background-slide hover buttons — left, right, top, and bottom — where a solid fill sweeps across the button face on hover using CSS pseudo-element transforms.
## HTML
```html
<div class="ab-02">
  <p class="ab-02__title">Background Slide Directions</p>
  <div class="ab-02__grid">
    <button class="ab-02__btn ab-02__btn--left"><span>Slide Left</span></button>
    <button class="ab-02__btn ab-02__btn--right"><span>Slide Right</span></button>
    <button class="ab-02__btn ab-02__btn--top"><span>Slide Top</span></button>
    <button class="ab-02__btn ab-02__btn--bottom"><span>Slide Bottom</span></button>
  </div>
</div>
```
## CSS
```css
.ab-02,
.ab-02 *,
.ab-02 *::before,
.ab-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ab-02 ::selection {
  background: #6c63ff;
  color: #fff;
}

.ab-02 {
  --fill: #6c63ff;
  --text: #1a1a2e;
  --border: #6c63ff;
  font-family: system-ui,sans-serif;
  background: #f0eeff;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  padding: 2rem;
}

.ab-02__title {
  font-size: .8rem;
  font-weight: 600;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #6c63ff;
  opacity: .7;
}

.ab-02__grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}

.ab-02__btn {
  position: relative;
  overflow: hidden;
  padding: .8rem 2rem;
  font-size: .95rem;
  font-weight: 700;
  color: var(--fill);
  background: transparent;
  border: 2px solid var(--border);
  border-radius: 8px;
  cursor: pointer;
  outline: none;
  transition: color .35s;
  letter-spacing: .03em;
}

.ab-02__btn span {
  position: relative;
  z-index: 1;
}

.ab-02__btn::before {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--fill);
  transition: transform .35s cubic-bezier(.4,0,.2,1);
  z-index: 0;
}

.ab-02__btn:hover {
  color: #fff;
}

.ab-02__btn--left::before {
  transform: translateX(-100%);
}

.ab-02__btn--left:hover::before {
  transform: translateX(0);
}

.ab-02__btn--right::before {
  transform: translateX(100%);
}

.ab-02__btn--right:hover::before {
  transform: translateX(0);
}

.ab-02__btn--top::before {
  transform: translateY(-100%);
}

.ab-02__btn--top:hover::before {
  transform: translateY(0);
}

.ab-02__btn--bottom::before {
  transform: translateY(100%);
}

.ab-02__btn--bottom:hover::before {
  transform: translateY(0);
}

.ab-02__btn:active {
  transform: scale(.97);
}

@media (prefers-reduced-motion: reduce) {
  .ab-02__btn::before {
    transition: none;
  }

  .ab-02__btn {
    transition: none;
  }
}
```
