---
source: "codefronts"
url: "https://codefronts.com/motion/css-animated-buttons/css-liquid-fill-button-animation/"
title: "CSS Liquid Fill Button Animation"
section: "motion"
category: "css-animated-buttons"
category_name: "CSS Animated Buttons"
description: "A button whose interior fills with a rising liquid wave on hover, created entirely with a CSS pseudo-element, SVG-like border-radius shaping, and a…"
has_js: "false"
---

Here's a working CSS Animated Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Liquid Fill Button Animation
Source: https://codefronts.com/motion/css-animated-buttons/css-liquid-fill-button-animation/

A button whose interior fills with a rising liquid wave on hover, created entirely with a CSS pseudo-element, SVG-like border-radius shaping, and a translateY animation.
## HTML
```html
<div class="ab-06">
  <p class="ab-06__label">Hover to fill</p>
  <div class="ab-06__row">
    <button class="ab-06__btn ab-06__btn--cyan"><span>Explore</span></button>
    <button class="ab-06__btn ab-06__btn--violet"><span>Subscribe</span></button>
    <button class="ab-06__btn ab-06__btn--amber"><span>Upgrade</span></button>
  </div>
</div>
```
## CSS
```css
.ab-06,
.ab-06 *,
.ab-06 *::before,
.ab-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ab-06 ::selection {
  background: #0891b2;
  color: #fff;
}

.ab-06 {
  font-family: system-ui,sans-serif;
  background: #0f172a;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2.5rem;
  padding: 2rem;
}

.ab-06__label {
  font-size: .78rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #94a3b8;
  opacity: .6;
}

.ab-06__row {
  display: flex;
  gap: 1.25rem;
  flex-wrap: wrap;
  justify-content: center;
}

.ab-06__btn {
  --liquid: #0891b2;
  --border-col: #0891b2;
  position: relative;
  overflow: hidden;
  padding: .85rem 2.2rem;
  font-size: 1rem;
  font-weight: 700;
  color: #e2e8f0;
  background: transparent;
  border: 2px solid var(--border-col);
  border-radius: 10px;
  cursor: pointer;
  outline: none;
  letter-spacing: .03em;
  transition: color .4s;
}

.ab-06__btn--cyan {
  --liquid: #0891b2;
  --border-col: #22d3ee;
  color: #67e8f9;
}

.ab-06__btn--violet {
  --liquid: #7c3aed;
  --border-col: #a78bfa;
  color: #c4b5fd;
}

.ab-06__btn--amber {
  --liquid: #d97706;
  --border-col: #fbbf24;
  color: #fde68a;
}

.ab-06__btn span {
  position: relative;
  z-index: 1;
}

.ab-06__btn::before {
  content: '';
  position: absolute;
  bottom: 0;
  left: -25%;
  width: 150%;
  height: 200%;
  background: var(--liquid);
  border-radius: 45% 55% 0 0 / 25% 25% 0 0;
  transform: translateY(100%);
  transition: transform .65s cubic-bezier(.4,0,.2,1);
  z-index: 0;
}

.ab-06__btn:hover::before {
  transform: translateY(5%);
  animation: ab-06-wave 2.5s ease-in-out infinite .65s;
}

.ab-06__btn:hover {
  color: #fff;
}

@keyframes ab-06-wave {
  0%,
    100% {
    border-radius: 45% 55% 0 0 / 25% 25% 0 0;
  }

  50% {
    border-radius: 55% 45% 0 0 / 20% 30% 0 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ab-06__btn::before {
    transition: none;
  }

  .ab-06__btn:hover::before {
    animation: none;
  }
}
```
