---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/bouncy-pop-checkbox/"
title: "Bouncy Pop Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "A satisfying, tactile toggle: on check the mark overshoots its size with a spring cubic-bezier before settling, and the box gives a tiny squash."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bouncy Pop Checkbox
Source: https://codefronts.com/components/css-checkboxes/bouncy-pop-checkbox/

A satisfying, tactile toggle: on check the mark overshoots its size with a spring cubic-bezier before settling, and the box gives a tiny squash. That physical bounce is what makes a checkbox feel alive — done entirely with transform.
## HTML
```html
<section class="cb-10" aria-label="Bouncy pop checkboxes">
  <div class="cb-10__panel">
    <label class="cb-10__row"><input type="checkbox" class="cb-10__input" checked><span class="cb-10__box" aria-hidden="true"></span><span class="cb-10__label">Add to favourites</span></label>
    <label class="cb-10__row"><input type="checkbox" class="cb-10__input"><span class="cb-10__box" aria-hidden="true"></span><span class="cb-10__label">Remind me later</span></label>
    <label class="cb-10__row"><input type="checkbox" class="cb-10__input"><span class="cb-10__box" aria-hidden="true"></span><span class="cb-10__label">Follow this thread</span></label>
  </div>
</section>
```
## CSS
```css
.cb-10,
.cb-10 *,
.cb-10 *::before,
.cb-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-10 ::selection {
  background: oklch(0.62 0.19 25);
  color: #fff;
}

.cb-10 {
  --accent: oklch(0.6 0.19 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #fbf4f2;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-10__panel {
  width: min(400px,100%);
  background: #fff;
  border: 1px solid #f0dfda;
  border-radius: 14px;
  padding: 10px 14px;
}

.cb-10__row {
  display: flex;
  align-items: center;
  gap: 14px;
  cursor: pointer;
  padding: 13px 8px;
}

.cb-10__input {
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

.cb-10__box {
  position: relative;
  flex: none;
  width: 26px;
  height: 26px;
  border-radius: 8px;
  border: 2px solid #e3b7ad;
  background: #fff;
  transition: background .2s,border-color .2s;
}

.cb-10__box::after {
  content: "";
  position: absolute;
  inset: 0;
  background: #fff;
  opacity: 0;
  transform: scale(0);
  transition: opacity .16s,transform .28s cubic-bezier(.34,1.7,.5,1);
  -webkit-mask: no-repeat center/15px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/15px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-10__input:checked ~ .cb-10__box {
  background: var(--accent);
  border-color: var(--accent);
  animation: cb-10-pop .32s ease;
}

.cb-10__input:checked ~ .cb-10__box::after {
  opacity: 1;
  transform: scale(1);
}

.cb-10__input:focus-visible ~ .cb-10__box {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.cb-10__label {
  font-size: 14.5px;
  color: #3a2a27;
}

@keyframes cb-10-pop {
  0% {
    transform: scale(1);
  }

  35% {
    transform: scale(.82,.82);
  }

  70% {
    transform: scale(1.12,1.12);
  }

  100% {
    transform: scale(1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-10__box,
    .cb-10__box::after {
    transition: opacity .15s;
    animation: none;
  }

  .cb-10__box::after {
    transform: scale(1);
  }
}
```

## JavaScript
```js
/* No JavaScript — an overshoot cubic-bezier + squash keyframe give the bounce. */
```
