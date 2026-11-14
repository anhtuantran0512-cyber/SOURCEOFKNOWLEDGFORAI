---
source: "codefronts"
url: "https://codefronts.com/motion/css-animated-buttons/css-shine-sweep-hover-button/"
title: "CSS Shine Sweep Hover Button"
section: "motion"
category: "css-animated-buttons"
category_name: "CSS Animated Buttons"
description: "A metallic light-streak sweeps diagonally across the button surface on hover, simulating a premium gloss reflection using a CSS pseudo-element gradient and…"
has_js: "false"
---

Here's a working CSS Animated Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Shine Sweep Hover Button
Source: https://codefronts.com/motion/css-animated-buttons/css-shine-sweep-hover-button/

A metallic light-streak sweeps diagonally across the button surface on hover, simulating a premium gloss reflection using a CSS pseudo-element gradient and translate animation.
## HTML
```html
<div class="ab-08">
  <p class="ab-08__label">Hover over the buttons</p>
  <div class="ab-08__row">
    <button class="ab-08__btn ab-08__btn--dark">Pro Features</button>
    <button class="ab-08__btn ab-08__btn--gold">Upgrade Now</button>
    <button class="ab-08__btn ab-08__btn--violet">Get Premium</button>
  </div>
</div>
```
## CSS
```css
.ab-08,
.ab-08 *,
.ab-08 *::before,
.ab-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ab-08 ::selection {
  background: #1e293b;
  color: #fff;
}

.ab-08 {
  font-family: system-ui,sans-serif;
  background: #f1f5f9;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  padding: 2rem;
}

.ab-08__label {
  font-size: .78rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #64748b;
}

.ab-08__row {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
}

.ab-08__btn {
  position: relative;
  overflow: hidden;
  padding: .85rem 2.2rem;
  font-size: .95rem;
  font-weight: 700;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  outline: none;
  letter-spacing: .04em;
  transition: filter .2s,transform .15s;
}

.ab-08__btn--dark {
  background: #1e293b;
  color: #e2e8f0;
}

.ab-08__btn--gold {
  background: linear-gradient(135deg,#b45309,#d97706,#fbbf24);
  color: #fff;
}

.ab-08__btn--violet {
  background: linear-gradient(135deg,#4c1d95,#7c3aed,#a78bfa);
  color: #fff;
}

.ab-08__btn:hover {
  filter: brightness(1.1);
  transform: translateY(-2px);
}

.ab-08__btn:active {
  transform: translateY(0);
  filter: brightness(.95);
}

.ab-08__btn::before {
  content: '';
  position: absolute;
  top: -10%;
  left: -20%;
  width: 60%;
  height: 120%;
  background: linear-gradient(105deg,transparent 30%,rgba(255,255,255,.55) 50%,transparent 70%);
  transform: translateX(-100%) skewX(-15deg);
  pointer-events: none;
}

.ab-08__btn:hover::before {
  animation: ab-08-shine .55s ease-in-out forwards;
}

@keyframes ab-08-shine {
  0% {
    transform: translateX(-100%) skewX(-15deg);
  }

  100% {
    transform: translateX(400%) skewX(-15deg);
  }
}

@media (prefers-reduced-motion: reduce) {
  .ab-08__btn:hover::before {
    animation: none;
  }
}
```
