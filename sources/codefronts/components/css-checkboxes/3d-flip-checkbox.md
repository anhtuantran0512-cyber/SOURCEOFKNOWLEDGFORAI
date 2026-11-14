---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/3d-flip-checkbox/"
title: "3D Flip Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "A tactile coin-flip: on check the box rotates in 3D to reveal a different face bearing the checkmark."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: 3D Flip Checkbox
Source: https://codefronts.com/components/css-checkboxes/3d-flip-checkbox/

A tactile coin-flip: on check the box rotates in 3D to reveal a different face bearing the checkmark. Built with perspective and preserve-3d — a memorable micro-interaction for confirmations and 'done' states.
## HTML
```html
<section class="cb-17" aria-label="3D flip checkboxes">
  <div class="cb-17__panel">
    <label class="cb-17__row"><input type="checkbox" class="cb-17__input" checked><span class="cb-17__box" aria-hidden="true"><span class="cb-17__inner"><span class="cb-17__face cb-17__front"></span><span class="cb-17__face cb-17__back"></span></span></span><span class="cb-17__label">Task complete</span></label>
    <label class="cb-17__row"><input type="checkbox" class="cb-17__input"><span class="cb-17__box" aria-hidden="true"><span class="cb-17__inner"><span class="cb-17__face cb-17__front"></span><span class="cb-17__face cb-17__back"></span></span></span><span class="cb-17__label">Mark as read</span></label>
    <label class="cb-17__row"><input type="checkbox" class="cb-17__input"><span class="cb-17__box" aria-hidden="true"><span class="cb-17__inner"><span class="cb-17__face cb-17__front"></span><span class="cb-17__face cb-17__back"></span></span></span><span class="cb-17__label">Approve request</span></label>
  </div>
</section>
```
## CSS
```css
.cb-17,
.cb-17 *,
.cb-17 *::before,
.cb-17 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-17 ::selection {
  background: oklch(0.6 0.15 175);
  color: #fff;
}

.cb-17 {
  --accent: oklch(0.55 0.13 175);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #eef5f4;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-17__panel {
  width: min(400px,100%);
  background: #fff;
  border: 1px solid #dbe8e6;
  border-radius: 14px;
  padding: 10px 14px;
}

.cb-17__row {
  display: flex;
  align-items: center;
  gap: 16px;
  cursor: pointer;
  padding: 13px 8px;
}

.cb-17__input {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0 0 0 0);
  white-space: nowrap;
  border: 0;
}

.cb-17__box {
  display: block;
  flex: none;
  width: 28px;
  height: 28px;
  perspective: 600px;
}

.cb-17__inner {
  display: block;
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform .5s cubic-bezier(.4,.8,.3,1);
}

.cb-17__face {
  position: absolute;
  inset: 0;
  border-radius: 8px;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
}

.cb-17__front {
  border: 2px solid #b4cbc8;
  background: #fff;
}

.cb-17__back {
  background: var(--accent);
  transform: rotateY(180deg);
}

.cb-17__back::after {
  content: "";
  position: absolute;
  inset: 0;
  background: #fff;
  -webkit-mask: no-repeat center/16px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/16px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-17__input:checked ~ .cb-17__box .cb-17__inner {
  transform: rotateY(180deg);
}

.cb-17__input:focus-visible ~ .cb-17__box {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
  border-radius: 8px;
}

.cb-17__label {
  font-size: 14.5px;
  color: #2b3a38;
}

@media (prefers-reduced-motion: reduce) {
  .cb-17__inner {
    transition: opacity .2s;
  }

  .cb-17__input:checked ~ .cb-17__box .cb-17__inner {
    transform: none;
  }

  .cb-17__front {
    transition: opacity .2s;
  }

  .cb-17__input:checked ~ .cb-17__box .cb-17__front {
    opacity: 0;
  }

  .cb-17__back {
    transform: none;
    opacity: 0;
  }

  .cb-17__input:checked ~ .cb-17__box .cb-17__back {
    opacity: 1;
  }
}
```

## JavaScript
```js
/* No JavaScript — the inner element rotateY(180deg) flips faces on :checked. */
```
