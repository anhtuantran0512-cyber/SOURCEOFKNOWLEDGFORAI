---
source: "codefronts"
url: "https://codefronts.com/components/css-checkboxes/saas-dashboard-toggle-switch/"
title: "SaaS Dashboard Toggle Switch"
section: "components"
category: "css-checkboxes"
category_name: "CSS Checkboxes"
description: "The enterprise settings-page classic: a clean pill track with a thumb that glides horizontally on check."
has_js: "false"
---

Here's a working CSS Checkboxe from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SaaS Dashboard Toggle Switch
Source: https://codefronts.com/components/css-checkboxes/saas-dashboard-toggle-switch/

The enterprise settings-page classic: a clean pill track with a thumb that glides horizontally on check. Reads instantly as on/off, sits at home on any dashboard row, and ships with a sharp keyboard focus ring.
## HTML
```html
<section class="cb-01" aria-label="SaaS dashboard toggle switches">
  <div class="cb-01__panel">
    <label class="cb-01__row">
      <span class="cb-01__text"><span class="cb-01__title">Email notifications</span><span class="cb-01__sub">Product news &amp; weekly digest</span></span>
      <input type="checkbox" class="cb-01__input" checked>
      <span class="cb-01__track"><span class="cb-01__thumb"></span></span>
    </label>
    <label class="cb-01__row">
      <span class="cb-01__text"><span class="cb-01__title">Two-factor auth</span><span class="cb-01__sub">Require a code at sign-in</span></span>
      <input type="checkbox" class="cb-01__input">
      <span class="cb-01__track"><span class="cb-01__thumb"></span></span>
    </label>
    <label class="cb-01__row">
      <span class="cb-01__text"><span class="cb-01__title">Usage analytics</span><span class="cb-01__sub">Share anonymised metrics</span></span>
      <input type="checkbox" class="cb-01__input" checked>
      <span class="cb-01__track"><span class="cb-01__thumb"></span></span>
    </label>
  </div>
</section>
```
## CSS
```css
.cb-01,
.cb-01 *,
.cb-01 *::before,
.cb-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cb-01 ::selection {
  background: oklch(0.62 0.16 250);
  color: #fff;
}

.cb-01 {
  --on: oklch(0.62 0.16 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  padding: 40px 20px;
  background: #f4f5f7;
  display: flex;
  align-items: center;
  justify-content: center;
}

.cb-01__panel {
  width: min(420px,100%);
  background: #fff;
  border: 1px solid #e6e8ec;
  border-radius: 16px;
  box-shadow: 0 18px 40px -28px rgba(16,24,40,.5);
  overflow: hidden;
}

.cb-01__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  padding: 18px 22px;
  cursor: pointer;
  border-bottom: 1px solid #eef0f3;
}

.cb-01__row:last-child {
  border-bottom: 0;
}

.cb-01__title {
  display: block;
  font-size: 15px;
  font-weight: 600;
  color: #1f2430;
}

.cb-01__sub {
  display: block;
  font-size: 12.5px;
  color: #8a909c;
  margin-top: 2px;
}

.cb-01__input {
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

.cb-01__track {
  --w: 46px;
  --h: 26px;
  flex: none;
  position: relative;
  width: var(--w);
  height: var(--h);
  border-radius: 999px;
  background: #cfd4dc;
  transition: background .28s ease;
}

.cb-01__thumb {
  position: absolute;
  top: 3px;
  left: 3px;
  width: calc(var(--h) - 6px);
  height: calc(var(--h) - 6px);
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 2px 5px rgba(16,24,40,.35);
  transition: transform .28s cubic-bezier(.2,.8,.2,1);
}

.cb-01__input:checked ~ .cb-01__track {
  background: var(--on);
}

.cb-01__input:checked ~ .cb-01__track .cb-01__thumb {
  transform: translateX(calc(var(--w) - var(--h)));
}

.cb-01__input:focus-visible ~ .cb-01__track {
  outline: 3px solid var(--on);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .cb-01__track,
    .cb-01__thumb {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — :checked drives the track colour and the thumb's translateX. */
```
