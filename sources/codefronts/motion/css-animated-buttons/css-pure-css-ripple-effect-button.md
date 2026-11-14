---
source: "codefronts"
url: "https://codefronts.com/motion/css-animated-buttons/css-pure-css-ripple-effect-button/"
title: "CSS Pure CSS Ripple Effect Button"
section: "motion"
category: "css-animated-buttons"
category_name: "CSS Animated Buttons"
description: "A Material Design-inspired ripple effect on button click, achieved entirely with CSS pseudo-elements and the :active state — no JavaScript required."
has_js: "false"
---

Here's a working CSS Animated Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Pure CSS Ripple Effect Button
Source: https://codefronts.com/motion/css-animated-buttons/css-pure-css-ripple-effect-button/

A Material Design-inspired ripple effect on button click, achieved entirely with CSS pseudo-elements and the :active state — no JavaScript required.
## HTML
```html
<div class="ab-03">
  <p class="ab-03__label">Click or tap to trigger</p>
  <div class="ab-03__row">
    <button class="ab-03__btn ab-03__btn--violet">Get Started</button>
    <button class="ab-03__btn ab-03__btn--teal">Learn More</button>
    <button class="ab-03__btn ab-03__btn--rose">Subscribe</button>
  </div>
</div>
```
## CSS
```css
.ab-03,
.ab-03 *,
.ab-03 *::before,
.ab-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ab-03 ::selection {
  background: #7c3aed;
  color: #fff;
}

.ab-03 {
  font-family: system-ui,sans-serif;
  background: #0f0c1a;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  padding: 2rem;
}

.ab-03__label {
  font-size: .78rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #a78bfa;
  opacity: .6;
}

.ab-03__row {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
}

.ab-03__btn {
  position: relative;
  overflow: hidden;
  padding: .85rem 2rem;
  font-size: .95rem;
  font-weight: 700;
  color: #fff;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  outline: none;
  letter-spacing: .03em;
  transition: filter .2s;
}

.ab-03__btn:hover {
  filter: brightness(1.1);
}

.ab-03__btn:active {
  filter: brightness(.9);
}

.ab-03__btn--violet {
  background: #7c3aed;
}

.ab-03__btn--teal {
  background: #0d9488;
}

.ab-03__btn--rose {
  background: #e11d48;
}

.ab-03__btn::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  background: rgba(255,255,255,.4);
  border-radius: 50%;
  transform: translate(-50%,-50%);
  pointer-events: none;
  opacity: 0;
}

.ab-03__btn:active::after {
  animation: ab-03-ripple .6s linear forwards;
}

@keyframes ab-03-ripple {
  0% {
    width: 0;
    height: 0;
    opacity: .4;
  }

  80% {
    width: 400%;
    height: 400%;
    opacity: .1;
  }

  100% {
    width: 500%;
    height: 500%;
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ab-03__btn:active::after {
    animation: none;
  }
}
```
