---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-label-inputs/css-floating-label-for-select-dropdowns/"
title: "CSS Floating Label for Select Dropdowns"
section: "components"
category: "css-floating-label-inputs"
category_name: "CSS Floating Label Inputs"
description: "The hardest field to float: <select> has no placeholder, so :placeholder-shown never fires."
has_js: "false"
---

Here's a working CSS Floating Label Input from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Floating Label for Select Dropdowns
Source: https://codefronts.com/components/css-floating-label-inputs/css-floating-label-for-select-dropdowns/

The hardest field to float: <select> has no placeholder, so :placeholder-shown never fires. This demo uses a hidden empty first option plus :has() and :valid to float the label only once a real choice is made — with a custom chevron, matching text-input styling, and full keyboard behaviour intact. Variation: the floated label becomes a solid accent PILL CHIP that lands on the top border — a badge, not a shrunken caption.
## HTML
```html
<section class="flb-08" aria-label="Floating label select demo">
  <form class="flb-08__form" novalidate>
    <h3 class="flb-08__title">Book a table</h3>
    <div class="flb-08__field">
      <select class="flb-08__select" id="flb-08-party" name="party" required>
        <option value="" selected></option>
        <option value="2">2 guests</option>
        <option value="4">4 guests</option>
        <option value="6">6 guests</option>
        <option value="8">8+ guests</option>
      </select>
      <label class="flb-08__label" for="flb-08-party">Party size</label>
      <span class="flb-08__chev" aria-hidden="true"></span>
    </div>
    <div class="flb-08__field">
      <select class="flb-08__select" id="flb-08-time" name="time" required>
        <option value="" selected></option>
        <option value="18">6:00 PM</option>
        <option value="19">7:00 PM</option>
        <option value="20">8:00 PM</option>
        <option value="21">9:00 PM</option>
      </select>
      <label class="flb-08__label" for="flb-08-time">Preferred time</label>
      <span class="flb-08__chev" aria-hidden="true"></span>
    </div>
    <button class="flb-08__btn" type="button">Find a table</button>
  </form>
</section>
```
## CSS
```css
.flb-08,
.flb-08 *,
.flb-08 *::before,
.flb-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.flb-08 {
  --accent: oklch(0.58 0.16 30);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f6f2ee;
  padding: 40px 20px;
}

.flb-08__form {
  width: min(380px,100%);
  background: #fff;
  border-radius: 20px;
  padding: 32px 30px;
  box-shadow: 0 22px 55px -30px rgba(60,30,10,.35);
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.flb-08__title {
  font-size: 23px;
  font-weight: 800;
  color: #26201b;
  letter-spacing: -.02em;
}

.flb-08__field {
  position: relative;
}

.flb-08__select {
  appearance: none;
  -webkit-appearance: none;
  width: 100%;
  height: 56px;
  padding: 0 44px 0 16px;
  font-size: 16px;
  font-family: inherit;
  color: #26201b;
  background: #fff;
  border: 1.5px solid #ddd4cb;
  border-radius: 12px;
  outline: none;
  cursor: pointer;
  transition: border-color .2s,box-shadow .2s;
}

.flb-08__select:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.58 0.16 30 / .14);
}

.flb-08__label {
  position: absolute;
  left: 16px;
  top: 50%;
  translate: 0 -50%;
  font-size: 16px;
  color: #8d8378;
  pointer-events: none;
  transform-origin: left center;
  padding: 3px 10px;
  margin-left: -10px;
  border-radius: 999px;
  transition: transform .22s,color .22s,background-color .22s;
}

.flb-08__select:focus ~ .flb-08__label,
.flb-08__select:valid ~ .flb-08__label {
  transform: translateY(-28px) scale(.74);
  background: var(--accent);
  color: #fff;
}

.flb-08__field:has(.flb-08__select:valid) .flb-08__label {
  transform: translateY(-28px) scale(.74);
  background: var(--accent);
  color: #fff;
}

.flb-08__select:focus ~ .flb-08__label {
  color: #fff;
}

.flb-08__chev {
  position: absolute;
  right: 18px;
  top: calc(50% - 7px);
  width: 10px;
  height: 10px;
  border-right: 2.5px solid #8d8378;
  border-bottom: 2.5px solid #8d8378;
  rotate: 45deg;
  pointer-events: none;
  transition: rotate .2s,border-color .2s;
}

.flb-08__field:has(.flb-08__select:focus) .flb-08__chev {
  rotate: 225deg;
  top: calc(50% - 2px);
  border-color: var(--accent);
}

.flb-08__btn {
  height: 50px;
  border: none;
  border-radius: 12px;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  transition: filter .15s;
}

.flb-08__btn:hover {
  filter: brightness(1.08);
}

.flb-08__btn:focus-visible,
.flb-08__select:focus-visible {
  outline: 3px solid oklch(0.58 0.16 30 / .5);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .flb-08__label,
    .flb-08__select,
    .flb-08__chev {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a required select with an empty first option is :invalid until a real choice is made; select:valid (plus :has() on the wrapper) floats the label. Native keyboard, type-ahead and mobile pickers stay intact. */
```
