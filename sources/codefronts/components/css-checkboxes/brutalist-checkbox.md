---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/brutalist-checkbox/"
title: "Brutalist Checkbox"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "Raw, loud and unapologetic: thick black borders, zero radius, stark high-voltage colour, and a hard offset shadow that snaps down-and-right on click."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Checkbox
Source: https://codefronts.com/components/css-checkboxes/brutalist-checkbox/

Raw, loud and unapologetic: thick black borders, zero radius, stark high-voltage colour, and a hard offset shadow that snaps down-and-right on click. The look driving the neo-brutalist portfolio and indie-SaaS wave.
## HTML
```html
<section class="cb-15" aria-label="Brutalist checkboxes">
  <div class="cb-15__panel">
    <label class="cb-15__row"><input type="checkbox" class="cb-15__input" checked><span class="cb-15__box" aria-hidden="true"></span><span class="cb-15__label">SHIP IT</span></label>
    <label class="cb-15__row"><input type="checkbox" class="cb-15__input"><span class="cb-15__box" aria-hidden="true"></span><span class="cb-15__label">BREAK THINGS</span></label>
    <label class="cb-15__row"><input type="checkbox" class="cb-15__input"><span class="cb-15__box" aria-hidden="true"></span><span class="cb-15__label">NO REGRETS</span></label>
  </div>
</section>
```
## CSS
```css
.cb-15,
.cb-15 *,
.cb-15 *::before,
.cb-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-15 ::selection {
  background: #000;
  color: #f7ff37;
}

.cb-15 {
  --accent: #f7ff37;
  font-family: 'Arial Black',ui-monospace,system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #e8e6df;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-15__panel {
  width: min(400px,100%);
  background: #fff;
  border: 4px solid #000;
  padding: 8px;
  box-shadow: 8px 8px 0 #000;
}

.cb-15__row {
  display: flex;
  align-items: center;
  gap: 16px;
  cursor: pointer;
  padding: 14px 12px;
}

.cb-15__input {
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

.cb-15__box {
  position: relative;
  flex: none;
  width: 28px;
  height: 28px;
  background: #fff;
  border: 4px solid #000;
  box-shadow: 4px 4px 0 #000;
  transition: transform .08s linear,background .08s linear;
}

.cb-15__box::after {
  content: "";
  position: absolute;
  inset: 0;
  background: #000;
  opacity: 0;
  -webkit-mask: no-repeat center/18px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='4' stroke-linecap='square' stroke-linejoin='miter'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
  mask: no-repeat center/18px url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23000' stroke-width='4' stroke-linecap='square' stroke-linejoin='miter'%3E%3Cpath d='M20 6 9 17l-5-5'/%3E%3C/svg%3E");
}

.cb-15__input:checked ~ .cb-15__box {
  background: var(--accent);
  transform: translate(4px,4px);
  box-shadow: 0 0 0 #000;
}

.cb-15__input:checked ~ .cb-15__box::after {
  opacity: 1;
}

.cb-15__input:focus-visible ~ .cb-15__box {
  outline: 4px solid #000;
  outline-offset: 4px;
}

.cb-15__label {
  font-size: 16px;
  font-weight: 900;
  letter-spacing: .04em;
  color: #000;
}

@media (prefers-reduced-motion: reduce) {
  .cb-15__box {
    transition: background .08s linear;
  }

  .cb-15__input:checked ~ .cb-15__box {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a zero-blur hard shadow + transform shift snap on :checked. */
```
