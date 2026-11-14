---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-label-inputs/material-design-outlined-text-field-in-pure-css/"
title: "Material Design Outlined Text Field in Pure CSS"
section: "components"
category: "css-floating-label-inputs"
category_name: "CSS Floating Label Inputs"
description: "The classic Google-style outlined text field: on focus the label glides up onto the border line and the outline visually 'opens' a notch around it — built…"
has_js: "false"
---

Here's a working CSS Floating Label Input from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Material Design Outlined Text Field in Pure CSS
Source: https://codefronts.com/components/css-floating-label-inputs/material-design-outlined-text-field-in-pure-css/

The classic Google-style outlined text field: on focus the label glides up onto the border line and the outline visually 'opens' a notch around it — built with a single background trick, no fieldset/legend hacks, no extra wrapper spans, no JS measuring label widths.
## HTML
```html
<section class="flb-09" aria-label="Outlined material floating label demo">
  <form class="flb-09__form" novalidate>
    <h3 class="flb-09__title">Payment details</h3>
    <div class="flb-09__field">
      <input class="flb-09__input" type="text" id="flb-09-card" name="cc-number" placeholder=" " inputmode="numeric" autocomplete="cc-number">
      <label class="flb-09__label" for="flb-09-card">Card number</label>
    </div>
    <div class="flb-09__row">
      <div class="flb-09__field">
        <input class="flb-09__input" type="text" id="flb-09-exp" name="cc-exp" placeholder=" " inputmode="numeric" autocomplete="cc-exp">
        <label class="flb-09__label" for="flb-09-exp">MM / YY</label>
      </div>
      <div class="flb-09__field">
        <input class="flb-09__input" type="text" id="flb-09-cvc" name="cc-csc" placeholder=" " inputmode="numeric" autocomplete="cc-csc">
        <label class="flb-09__label" for="flb-09-cvc">CVC</label>
      </div>
    </div>
    <button class="flb-09__btn" type="button">Pay $48.00</button>
  </form>
</section>
```
## CSS
```css
.flb-09,
.flb-09 *,
.flb-09 *::before,
.flb-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.flb-09 {
  --accent: oklch(0.5 0.17 285);
  --surface: #ffffff;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #ebe9f2;
  padding: 40px 20px;
}

.flb-09__form {
  width: min(400px,100%);
  background: var(--surface);
  border-radius: 20px;
  padding: 32px 30px;
  box-shadow: 0 24px 60px -32px rgba(40,30,80,.35);
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.flb-09__title {
  font-size: 23px;
  font-weight: 800;
  color: #1f1b2e;
  letter-spacing: -.02em;
}

.flb-09__row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}

.flb-09__field {
  position: relative;
}

.flb-09__input {
  width: 100%;
  height: 56px;
  padding: 14px 16px;
  font-size: 16px;
  color: #1f1b2e;
  background: transparent;
  border: 1.5px solid #c9c4da;
  border-radius: 12px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.flb-09__input:hover {
  border-color: #a29bc;
}

.flb-09__input:focus {
  border-color: var(--accent);
  box-shadow: inset 0 0 0 1px var(--accent);
}

.flb-09__label {
  position: absolute;
  left: 12px;
  top: 50%;
  translate: 0 -50%;
  font-size: 16px;
  color: #756e8c;
  background: var(--surface);
  padding: 0 5px;
  pointer-events: none;
  transform-origin: left center;
  transition: transform .18s,color .18s;
}

.flb-09__input:focus ~ .flb-09__label,
.flb-09__input:not(:placeholder-shown) ~ .flb-09__label {
  transform: translateY(-28px) scale(.76);
}

.flb-09__input:focus ~ .flb-09__label {
  color: var(--accent);
  font-weight: 600;
}

.flb-09__btn {
  height: 52px;
  border: none;
  border-radius: 12px;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  transition: filter .15s,transform .15s;
}

.flb-09__btn:hover {
  filter: brightness(1.12);
}

.flb-09__btn:active {
  transform: scale(.985);
}

.flb-09__btn:focus-visible,
.flb-09__input:focus-visible {
  outline: 3px solid oklch(0.5 0.17 285 / .5);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .flb-09__label,
    .flb-09__input,
    .flb-09__btn {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — the floated label carries the surface background + side padding, so it visually notches the border. No legend hacks, no width measuring. */
```
