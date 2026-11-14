---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/ripple-wave-checkbox/"
title: "Ripple Wave Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "Material Design mechanics: clicking sends a translucent circular ripple expanding from the box, neatly contained within its bounds, as the check settles."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ripple Wave Checkbox
Source: https://codefronts.com/components/css-checkboxes/ripple-wave-checkbox/

Material Design mechanics: clicking sends a translucent circular ripple expanding from the box, neatly contained within its bounds, as the check settles. Familiar, satisfying, and achievable with pure CSS.
## HTML
```html
<section class="cb-18" aria-label="Ripple wave checkboxes">
  <div class="cb-18__panel">
    <label class="cb-18__row"><input type="checkbox" class="cb-18__input" checked><span class="cb-18__box" aria-hidden="true"><span class="cb-18__ripple"></span></span><span class="cb-18__label">Sync across devices</span></label>
    <label class="cb-18__row"><input type="checkbox" class="cb-18__input"><span class="cb-18__box" aria-hidden="true"><span class="cb-18__ripple"></span></span><span class="cb-18__label">Offline downloads</span></label>
    <label class="cb-18__row"><input type="checkbox" class="cb-18__input"><span class="cb-18__box" aria-hidden="true"><span class="cb-18__ripple"></span></span><span class="cb-18__label">Background refresh</span></label>
  </div>
</section>
```
## CSS
```css
.cb-18,
.cb-18 *,
.cb-18 *::before,
.cb-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-18 ::selection {
  background: oklch(0.62 0.16 265);
  color: #fff;
}

.cb-18 {
  --accent: oklch(0.58 0.17 265);
  font-family: 'Segoe UI','Roboto',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #f4f5fa;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-18__panel {
  width: min(400px,100%);
  background: #fff;
  border: 1px solid #e5e7f0;
  border-radius: 14px;
  padding: 10px 14px;
}

.cb-18__row {
  display: flex;
  align-items: center;
  gap: 14px;
  cursor: pointer;
  padding: 13px 8px;
}

.cb-18__input {
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

.cb-18__box {
  position: relative;
  flex: none;
  width: 26px;
  height: 26px;
  border-radius: 6px;
  border: 2px solid #b9bfd4;
  background: #fff;
  overflow: hidden;
  transition: background .2s,border-color .2s;
}

.cb-18__ripple {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 200%;
  height: 200%;
  border-radius: 50%;
  background: var(--accent);
  transform: translate(-50%,-50%) scale(0);
  opacity: .45;
  pointer-events: none;
}

.cb-18__box::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 1;
  background: #fff;
  opacity: 0;
  transform: scale(.5);
  transition: opacity .2s,transform .2s cubic-bezier(.2,.9,.3,1.2);
  -webkit-mask: no-repeat center/15px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/15px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-18__input:checked ~ .cb-18__box {
  background: var(--accent);
  border-color: var(--accent);
}

.cb-18__input:checked ~ .cb-18__box .cb-18__ripple {
  animation: cb-18-ripple .55s ease-out;
}

.cb-18__input:checked ~ .cb-18__box::after {
  opacity: 1;
  transform: scale(1);
}

.cb-18__input:focus-visible ~ .cb-18__box {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.cb-18__label {
  font-size: 14.5px;
  color: #2c3040;
}

@keyframes cb-18-ripple {
  0% {
    transform: translate(-50%,-50%) scale(0);
    opacity: .5;
  }

  100% {
    transform: translate(-50%,-50%) scale(1);
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-18__box,
    .cb-18__box::after {
    transition: none;
  }

  .cb-18__ripple {
    display: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a centre-origin ripple scales out via a one-shot keyframe on :checked. */
```
