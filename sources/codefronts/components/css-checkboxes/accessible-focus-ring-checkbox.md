---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/accessible-focus-ring-checkbox/"
title: "Accessible Focus-Ring Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "The production-safe baseline every design system needs: a minimalist square with a subtle check, but with obsessive attention to keyboard focus."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Focus-Ring Checkbox
Source: https://codefronts.com/components/css-checkboxes/accessible-focus-ring-checkbox/

The production-safe baseline every design system needs: a minimalist square with a subtle check, but with obsessive attention to keyboard focus. This is the demo Tier-1 devs audit first — the :focus-visible ring is the whole point.
## HTML
```html
<section class="cb-06" aria-label="Accessible checkbox group">
  <fieldset class="cb-06__group">
    <legend class="cb-06__legend">Notification preferences</legend>
    <label class="cb-06__row"><input type="checkbox" class="cb-06__input" checked><span class="cb-06__box" aria-hidden="true"></span><span class="cb-06__label">Enable desktop alerts</span></label>
    <label class="cb-06__row"><input type="checkbox" class="cb-06__input"><span class="cb-06__box" aria-hidden="true"></span><span class="cb-06__label">Play a sound on mention</span></label>
    <label class="cb-06__row"><input type="checkbox" class="cb-06__input" checked><span class="cb-06__box" aria-hidden="true"></span><span class="cb-06__label">Weekly summary email</span></label>
    <label class="cb-06__row cb-06__row--disabled"><input type="checkbox" class="cb-06__input" disabled><span class="cb-06__box" aria-hidden="true"></span><span class="cb-06__label">SMS alerts (upgrade required)</span></label>
  </fieldset>
</section>
```
## CSS
```css
.cb-06,
.cb-06 *,
.cb-06 *::before,
.cb-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-06 ::selection {
  background: oklch(0.55 0.02 250);
  color: #fff;
}

.cb-06 {
  --accent: oklch(0.32 0.02 260);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #fbfbfc;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-06__group {
  width: min(420px,100%);
  border: 1px solid #e6e7ea;
  border-radius: 14px;
  padding: 14px 18px 20px;
  background: #fff;
}

.cb-06__legend {
  font-size: 12px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: #9aa0aa;
  padding: 0 4px;
}

.cb-06__row {
  display: flex;
  align-items: center;
  gap: 13px;
  min-height: 44px;
  cursor: pointer;
}

.cb-06__row--disabled {
  cursor: not-allowed;
  opacity: .5;
}

.cb-06__input {
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

.cb-06__box {
  position: relative;
  flex: none;
  width: 22px;
  height: 22px;
  border-radius: 6px;
  border: 2px solid #b8bcc4;
  background: #fff;
  transition: background .18s,border-color .18s;
}

.cb-06__box::after {
  content: "";
  position: absolute;
  inset: 0;
  background: #fff;
  opacity: 0;
  transform: scale(.5);
  transition: opacity .18s,transform .18s cubic-bezier(.2,.9,.3,1.2);
  -webkit-mask: no-repeat center/14px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/14px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-06__input:checked ~ .cb-06__box {
  background: var(--accent);
  border-color: var(--accent);
}

.cb-06__input:checked ~ .cb-06__box::after {
  opacity: 1;
  transform: scale(1);
}

.cb-06__input:focus-visible ~ .cb-06__box {
  outline: 3px solid oklch(0.62 0.17 250);
  outline-offset: 3px;
}

.cb-06__input:focus:not(:focus-visible) ~ .cb-06__box {
  outline: none;
}

.cb-06__label {
  font-size: 14.5px;
  color: #2a2f3a;
}

@media (prefers-reduced-motion: reduce) {
  .cb-06__box,
    .cb-06__box::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the emphasis is a pure-CSS :focus-visible ring on the custom box. */
```
