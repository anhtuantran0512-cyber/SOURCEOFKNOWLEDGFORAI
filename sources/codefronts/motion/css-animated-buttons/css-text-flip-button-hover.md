---
source: "codefronts"
url: "https://codefronts.com/motion/css-animated-buttons/css-text-flip-button-hover/"
title: "CSS Text Flip Button Hover"
section: "motion"
category: "css-animated-buttons"
category_name: "CSS Animated Buttons"
description: "Button labels flip vertically on hover to reveal a secondary message — built with CSS 3D perspective transforms on stacked spans, no JavaScript required."
has_js: "false"
---

Here's a working CSS Animated Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Text Flip Button Hover
Source: https://codefronts.com/motion/css-animated-buttons/css-text-flip-button-hover/

Button labels flip vertically on hover to reveal a secondary message — built with CSS 3D perspective transforms on stacked spans, no JavaScript required.
## HTML
```html
<div class="ab-10">
  <p class="ab-10__label">Hover to flip text</p>
  <div class="ab-10__row">
    <button class="ab-10__btn ab-10__btn--indigo">
      <span class="ab-10__inner">
        <span class="ab-10__front">View Pricing</span>
        <span class="ab-10__back">From $9/mo →</span>
      </span>
    </button>
    <button class="ab-10__btn ab-10__btn--teal">
      <span class="ab-10__inner">
        <span class="ab-10__front">Follow Us</span>
        <span class="ab-10__back">@codefronts</span>
      </span>
    </button>
    <button class="ab-10__btn ab-10__btn--rose">
      <span class="ab-10__inner">
        <span class="ab-10__front">Join Beta</span>
        <span class="ab-10__back">Spots Left: 3</span>
      </span>
    </button>
  </div>
</div>
```
## CSS
```css
.ab-10,
.ab-10 *,
.ab-10 *::before,
.ab-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ab-10 ::selection {
  background: #4f46e5;
  color: #fff;
}

.ab-10 {
  font-family: system-ui,sans-serif;
  background: #0f0c1f;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2rem;
  padding: 2rem;
}

.ab-10__label {
  font-size: .78rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #818cf8;
  opacity: .6;
}

.ab-10__row {
  display: flex;
  gap: 1.25rem;
  flex-wrap: wrap;
  justify-content: center;
}

.ab-10__btn {
  --c: #4f46e5;
  padding: 0;
  background: var(--c);
  border: none;
  border-radius: 10px;
  cursor: pointer;
  outline: none;
  perspective: 600px;
}

.ab-10__btn--indigo {
  --c: #4f46e5;
}

.ab-10__btn--teal {
  --c: #0d9488;
}

.ab-10__btn--rose {
  --c: #e11d48;
}

.ab-10__inner {
  position: relative;
  display: block;
  padding: .85rem 2rem;
  width: 9rem;
  height: 3.1rem;
  overflow: hidden;
  transform-style: preserve-3d;
}

.ab-10__front,
.ab-10__back {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: .95rem;
  font-weight: 700;
  color: #fff;
  letter-spacing: .04em;
  white-space: nowrap;
  backface-visibility: hidden;
  transition: transform .35s cubic-bezier(.4,0,.2,1);
}

.ab-10__front {
  transform: translateY(0) rotateX(0);
}

.ab-10__back {
  transform: translateY(100%) rotateX(-90deg);
}

.ab-10__btn:hover .ab-10__front {
  transform: translateY(-100%) rotateX(90deg);
}

.ab-10__btn:hover .ab-10__back {
  transform: translateY(0) rotateX(0);
}

@media (prefers-reduced-motion: reduce) {
  .ab-10__front,
    .ab-10__back {
    transition: none;
  }

  .ab-10__btn:hover .ab-10__front {
    transform: none;
    opacity: 0;
  }

  .ab-10__btn:hover .ab-10__back {
    transform: none;
    opacity: 1;
  }
}
```
