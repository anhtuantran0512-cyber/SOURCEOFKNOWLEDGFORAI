---
source: "codefronts"
url: "https://codefronts.com/components/css-gradient-buttons/css-neon-glowing-gradient-button/"
title: "CSS Neon Glowing Gradient Button"
section: "components"
category: "css-gradient-buttons"
category_name: "CSS Gradient Buttons"
description: "A dark-arcade Insert Coin button rendered as a neon tube — gradient border, glowing text, and two blurred gradient copies breathing behind it as tight halo…"
has_js: "false"
---

Here's a working CSS Gradient Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Neon Glowing Gradient Button
Source: https://codefronts.com/components/css-gradient-buttons/css-neon-glowing-gradient-button/

A dark-arcade Insert Coin button rendered as a neon tube — gradient border, glowing text, and two blurred gradient copies breathing behind it as tight halo and wide ambient wash.
## HTML
```html
<div class="gb-11">
  <p class="gb-11__sign">Night Arcade <b>// open till 4am</b></p>
  <button class="gb-11__btn" type="button">Insert Coin</button>
  <p class="gb-11__credits">Credits: <b>03</b> · High score 128,540</p>
</div>
```
## CSS
```css
.gb-11,
.gb-11 *,
.gb-11 *::before,
.gb-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.gb-11 ::selection {
  background: #f0abfc;
  color: #0d0517;
}

.gb-11 {
  --neon-a: #f0abfc;
  --neon-b: #e879f9;
  --neon-c: #22d3ee;
  --tube: #0d0517;
  font-family: ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  background: linear-gradient(rgba(232,121,249,.05) 1px,transparent 1px), linear-gradient(90deg,rgba(34,211,238,.05) 1px,transparent 1px), var(--tube);
  background-size: 34px 34px,34px 34px,auto;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 38px;
  padding: 48px 24px;
}

.gb-11__sign {
  font-size: 13px;
  letter-spacing: 6px;
  text-transform: uppercase;
  color: #a78bba;
}

.gb-11__sign b {
  color: var(--neon-c);
  text-shadow: 0 0 8px rgba(34,211,238,.9),0 0 24px rgba(34,211,238,.5);
}
/* The tube: gradient border via background-clip, and TWO blurred
   copies of the gradient stacked behind — a tight halo and a huge
   ambient wash — breathing on alternating keyframes. */

.gb-11__btn {
  position: relative;
  padding: 20px 52px;
  border: 2px solid transparent;
  border-radius: 18px;
  font-family: inherit;
  font-size: 19px;
  font-weight: 700;
  letter-spacing: 5px;
  text-transform: uppercase;
  cursor: pointer;
  color: #fbe7ff;
  text-shadow: 0 0 10px rgba(240,171,252,.9),0 0 30px rgba(232,121,249,.5);
  background: linear-gradient(rgba(13,5,23,.92),rgba(13,5,23,.92)) padding-box, linear-gradient(100deg,var(--neon-b),var(--neon-c)) border-box;
  transition: transform .25s ease,letter-spacing .3s ease;
  -webkit-tap-highlight-color: transparent;
}

.gb-11__btn::before,
.gb-11__btn::after {
  content: "";
  position: absolute;
  inset: -2px;
  z-index: -1;
  border-radius: inherit;
  background: linear-gradient(100deg,var(--neon-b),var(--neon-c));
  pointer-events: none;
}

.gb-11__btn::before {
  filter: blur(14px);
  opacity: .7;
  animation: gb-11-breathe 2.6s ease-in-out infinite;
}

.gb-11__btn::after {
  filter: blur(46px);
  opacity: .4;
  animation: gb-11-breathe 2.6s ease-in-out -1.3s infinite;
}

@keyframes gb-11-breathe {
  0%,
    100% {
    opacity: .35;
    transform: scale(.99);
  }

  50% {
    opacity: .8;
    transform: scale(1.02);
  }
}

.gb-11__btn:hover {
  transform: translateY(-2px);
  letter-spacing: 7px;
}

.gb-11__btn:hover::before {
  opacity: 1;
  animation-duration: 1.1s;
}

.gb-11__btn:hover::after {
  opacity: .65;
  animation-duration: 1.1s;
}

.gb-11__btn:active {
  transform: translateY(0) scale(.97);
}

.gb-11__btn:focus-visible {
  outline: 3px solid var(--neon-c);
  outline-offset: 5px;
}

.gb-11__credits {
  font-size: 12px;
  letter-spacing: 2px;
  color: #5b4a6e;
}

.gb-11__credits b {
  color: var(--neon-a);
}

@media (prefers-reduced-motion: reduce) {
  .gb-11__btn {
    transition: none;
  }

  .gb-11__btn::before,
    .gb-11__btn::after {
    animation: none;
    opacity: .55;
  }

  .gb-11__btn:hover {
    transform: none;
    letter-spacing: 5px;
  }
}
```
