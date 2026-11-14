---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/liquid-fill-checkbox/"
title: "Liquid Fill Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "A playful control where colour rises from the bottom like water filling a glass, complete with a subtle wave crest."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Fill Checkbox
Source: https://codefronts.com/components/css-checkboxes/liquid-fill-checkbox/

A playful control where colour rises from the bottom like water filling a glass, complete with a subtle wave crest. Great for gamified onboarding, habit trackers and progress-y task lists — pure CSS, no canvas.
## HTML
```html
<section class="cb-13" aria-label="Liquid fill checkboxes">
  <div class="cb-13__panel">
    <label class="cb-13__row"><input type="checkbox" class="cb-13__input" checked><span class="cb-13__box" aria-hidden="true"><span class="cb-13__liquid"></span></span><span class="cb-13__label">Drink water</span></label>
    <label class="cb-13__row"><input type="checkbox" class="cb-13__input"><span class="cb-13__box" aria-hidden="true"><span class="cb-13__liquid"></span></span><span class="cb-13__label">Morning workout</span></label>
    <label class="cb-13__row"><input type="checkbox" class="cb-13__input"><span class="cb-13__box" aria-hidden="true"><span class="cb-13__liquid"></span></span><span class="cb-13__label">Read 20 pages</span></label>
  </div>
</section>
```
## CSS
```css
.cb-13,
.cb-13 *,
.cb-13 *::before,
.cb-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-13 ::selection {
  background: oklch(0.62 0.14 230);
  color: #fff;
}

.cb-13 {
  --water: oklch(0.6 0.13 230);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #eef4f8;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-13__panel {
  width: min(400px,100%);
  background: #fff;
  border: 1px solid #dce6ee;
  border-radius: 14px;
  padding: 10px 14px;
}

.cb-13__row {
  display: flex;
  align-items: center;
  gap: 14px;
  cursor: pointer;
  padding: 13px 8px;
}

.cb-13__input {
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

.cb-13__box {
  position: relative;
  flex: none;
  width: 28px;
  height: 28px;
  border-radius: 8px;
  border: 2px solid #b9cad6;
  background: #fff;
  overflow: hidden;
  transition: border-color .3s;
}

.cb-13__liquid {
  position: absolute;
  left: -25%;
  bottom: 0;
  width: 150%;
  height: 130%;
  background: var(--water);
  border-radius: 42% 46% 0 0/14px;
  transform: translateY(105%);
  transition: transform .5s cubic-bezier(.5,.1,.3,1);
}

.cb-13__box::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 1;
  background: #fff;
  opacity: 0;
  transition: opacity .25s .18s;
  -webkit-mask: no-repeat center/15px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/15px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-13__input:checked ~ .cb-13__box {
  border-color: var(--water);
}

.cb-13__input:checked ~ .cb-13__box .cb-13__liquid {
  transform: translateY(0);
  animation: cb-13-wave 3s linear infinite;
}

.cb-13__input:checked ~ .cb-13__box::after {
  opacity: 1;
}

.cb-13__input:focus-visible ~ .cb-13__box {
  outline: 3px solid var(--water);
  outline-offset: 3px;
}

.cb-13__label {
  font-size: 14.5px;
  color: #2c3a44;
}

@keyframes cb-13-wave {
  0% {
    border-radius: 42% 46% 0 0/14px;
  }

  50% {
    border-radius: 46% 40% 0 0/12px;
  }

  100% {
    border-radius: 42% 46% 0 0/14px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-13__box,
    .cb-13__liquid,
    .cb-13__box::after {
    transition: none;
  }

  .cb-13__input:checked ~ .cb-13__box .cb-13__liquid {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the liquid rises via translateY on :checked; a keyframe waves the crest. */
```
