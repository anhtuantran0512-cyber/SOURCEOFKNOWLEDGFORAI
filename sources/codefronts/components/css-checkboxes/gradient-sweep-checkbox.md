---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/gradient-sweep-checkbox/"
title: "Gradient Sweep Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "A high-end agency / web3 treatment: on check the box fills with a multi-stop gradient that sweeps continuously via an animated background-position."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Sweep Checkbox
Source: https://codefronts.com/components/css-checkboxes/gradient-sweep-checkbox/

A high-end agency / web3 treatment: on check the box fills with a multi-stop gradient that sweeps continuously via an animated background-position. Rich, colourful and alive without a single image.
## HTML
```html
<section class="cb-16" aria-label="Gradient sweep checkboxes">
  <div class="cb-16__panel">
    <label class="cb-16__row"><input type="checkbox" class="cb-16__input" checked><span class="cb-16__box" aria-hidden="true"></span><span class="cb-16__label">Mint on completion</span></label>
    <label class="cb-16__row"><input type="checkbox" class="cb-16__input"><span class="cb-16__box" aria-hidden="true"></span><span class="cb-16__label">Enable gasless mode</span></label>
    <label class="cb-16__row"><input type="checkbox" class="cb-16__input" checked><span class="cb-16__box" aria-hidden="true"></span><span class="cb-16__label">Show floor price</span></label>
  </div>
</section>
```
## CSS
```css
.cb-16,
.cb-16 *,
.cb-16 *::before,
.cb-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-16 ::selection {
  background: oklch(0.65 0.2 320);
  color: #fff;
}

.cb-16 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #0f1020;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-16__panel {
  width: min(400px,100%);
  background: #181a30;
  border: 1px solid #2a2d4a;
  border-radius: 16px;
  padding: 12px 16px;
}

.cb-16__row {
  display: flex;
  align-items: center;
  gap: 14px;
  cursor: pointer;
  padding: 13px 6px;
}

.cb-16__input {
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

.cb-16__box {
  position: relative;
  flex: none;
  width: 26px;
  height: 26px;
  border-radius: 8px;
  border: 2px solid #3a3e66;
  background: #12142a;
  overflow: hidden;
  transition: border-color .25s;
}

.cb-16__box::before {
  content: "";
  position: absolute;
  inset: 0;
  opacity: 0;
  transition: opacity .3s;
  background: linear-gradient(115deg,#ff2e97,#ff9a3d,#ffe74c,#2effc8,#5b8bff,#c04cff,#ff2e97);
  background-size: 300% 300%;
}

.cb-16__box::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 1;
  background: #fff;
  opacity: 0;
  transform: scale(.5);
  transition: opacity .22s,transform .22s cubic-bezier(.2,.9,.3,1.3);
  -webkit-mask: no-repeat center/15px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/15px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-16__input:checked ~ .cb-16__box {
  border-color: transparent;
}

.cb-16__input:checked ~ .cb-16__box::before {
  opacity: 1;
  animation: cb-16-sweep 4s linear infinite;
}

.cb-16__input:checked ~ .cb-16__box::after {
  opacity: 1;
  transform: scale(1);
}

.cb-16__input:focus-visible ~ .cb-16__box {
  outline: 3px solid #c04cff;
  outline-offset: 3px;
}

.cb-16__label {
  font-size: 14.5px;
  color: #c7cbe6;
}

@keyframes cb-16-sweep {
  0% {
    background-position: 0% 50%;
  }

  100% {
    background-position: 300% 50%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-16__box,
    .cb-16__box::before,
    .cb-16__box::after {
    transition: none;
  }

  .cb-16__input:checked ~ .cb-16__box::before {
    animation: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — background-position sweeps across a multi-stop gradient on :checked. */
```
