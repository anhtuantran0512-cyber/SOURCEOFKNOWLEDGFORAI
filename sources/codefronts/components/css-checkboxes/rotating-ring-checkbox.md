---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/rotating-ring-checkbox/"
title: "Rotating Ring Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "A crisp mechanical feel: on check a circular ring spins a rapid turn and snaps shut around the box as the check appears."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rotating Ring Checkbox
Source: https://codefronts.com/components/css-checkboxes/rotating-ring-checkbox/

A crisp mechanical feel: on check a circular ring spins a rapid turn and snaps shut around the box as the check appears. Reads like a lock engaging — ideal for security toggles and confirm steps.
## HTML
```html
<section class="cb-14" aria-label="Rotating ring checkboxes">
  <div class="cb-14__panel">
    <label class="cb-14__row"><input type="checkbox" class="cb-14__input" checked><span class="cb-14__box" aria-hidden="true"><span class="cb-14__ring"></span></span><span class="cb-14__label">Lock workspace</span></label>
    <label class="cb-14__row"><input type="checkbox" class="cb-14__input"><span class="cb-14__box" aria-hidden="true"><span class="cb-14__ring"></span></span><span class="cb-14__label">Require passphrase</span></label>
    <label class="cb-14__row"><input type="checkbox" class="cb-14__input"><span class="cb-14__box" aria-hidden="true"><span class="cb-14__ring"></span></span><span class="cb-14__label">Auto-lock on idle</span></label>
  </div>
</section>
```
## CSS
```css
.cb-14,
.cb-14 *,
.cb-14 *::before,
.cb-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-14 ::selection {
  background: oklch(0.6 0.16 300);
  color: #fff;
}

.cb-14 {
  --accent: oklch(0.55 0.18 300);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #f5f2f8;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-14__panel {
  width: min(400px,100%);
  background: #fff;
  border: 1px solid #e8e2ee;
  border-radius: 14px;
  padding: 10px 14px;
}

.cb-14__row {
  display: flex;
  align-items: center;
  gap: 16px;
  cursor: pointer;
  padding: 13px 8px;
}

.cb-14__input {
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

.cb-14__box {
  position: relative;
  flex: none;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: #f1edf6;
}

.cb-14__ring {
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 2.5px solid #cfc6dd;
  transform: rotate(0deg) scale(1);
  transition: border-color .3s,transform .5s cubic-bezier(.3,1.3,.4,1);
}

.cb-14__box::after {
  content: "";
  width: 16px;
  height: 16px;
  background: var(--accent);
  opacity: 0;
  transform: scale(0) rotate(-40deg);
  transition: opacity .25s .12s,transform .35s .12s cubic-bezier(.2,1.3,.4,1);
  -webkit-mask: no-repeat center/16px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/16px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-14__input:checked ~ .cb-14__box .cb-14__ring {
  border-color: var(--accent);
  transform: rotate(360deg) scale(1);
}

.cb-14__input:checked ~ .cb-14__box::after {
  opacity: 1;
  transform: scale(1) rotate(0deg);
}

.cb-14__input:focus-visible ~ .cb-14__box {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
  border-radius: 50%;
}

.cb-14__label {
  font-size: 14.5px;
  color: #332a3d;
}

@media (prefers-reduced-motion: reduce) {
  .cb-14__ring,
    .cb-14__box::after {
    transition: opacity .2s;
  }

  .cb-14__input:checked ~ .cb-14__box .cb-14__ring {
    transform: none;
  }

  .cb-14__input:checked ~ .cb-14__box::after {
    transform: scale(1) rotate(0);
  }
}
```

## JavaScript
```js
/* No JavaScript — the ring spins a full turn via rotate() on :checked. */
```
