---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/pure-css-accessible-radio-button/"
title: "Pure CSS Accessible Radio Button"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "The reference implementation every custom radio should start from: style the native <input type=\"radio\"> itself with appearance:none — no hidden-input hacks,…"
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Accessible Radio Button
Source: https://codefronts.com/components/css-radio-buttons/pure-css-accessible-radio-button/

The reference implementation every custom radio should start from: style the native <input type="radio"> itself with appearance:none — no hidden-input hacks, no wrapper spans, no ARIA patching. You keep 100% of the browser's semantics, keyboard model and form behaviour, and lose only the default look.
## HTML
```html
<div class="crb-05-group">
<section class="crb-05a" aria-label="Accessible pure CSS radio buttons">
  <fieldset class="crb-05a__group">
    <legend class="crb-05a__legend">How did you hear about us?</legend>
    <div class="crb-05a__list">
      <label class="crb-05a__row"><input class="crb-05a__input" type="radio" name="crb-05a" value="search" checked><span class="crb-05a__text">Search engine</span></label>
      <label class="crb-05a__row"><input class="crb-05a__input" type="radio" name="crb-05a" value="social"><span class="crb-05a__text">Social media</span></label>
      <label class="crb-05a__row"><input class="crb-05a__input" type="radio" name="crb-05a" value="friend"><span class="crb-05a__text">Friend or colleague</span></label>
      <label class="crb-05a__row crb-05a__row--disabled"><input class="crb-05a__input" type="radio" name="crb-05a" value="event" disabled><span class="crb-05a__text">Event <em class="crb-05a__note">(unavailable)</em></span></label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-05-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-05-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-05a,
.crb-05a *,
.crb-05a *::before,
.crb-05a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-05a {
  --accent: oklch(0.52 0.18 250);
  --ink: #20242f;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #fafafc;
}

.crb-05a__group {
  border: none;
  width: min(380px,100%);
}

.crb-05a__legend {
  font-size: 24px;
  font-weight: 750;
  color: var(--ink);
  letter-spacing: -.02em;
}

.crb-05a__list {
  display: grid;
  margin-top: 16px;
}

.crb-05a__row {
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 48px;
  padding: 0 8px;
  border-radius: 10px;
  cursor: pointer;
  transition: background .2s;
}

.crb-05a__row:hover {
  background: #f0f1f6;
}

.crb-05a__input {
  appearance: none;
  -webkit-appearance: none;
  width: 22px;
  height: 22px;
  flex: none;
  border: 2px solid #b6bccd;
  border-radius: 50%;
  display: grid;
  place-items: center;
  cursor: pointer;
  background: #fff;
  transition: border-color .2s;
}

.crb-05a__input::before {
  content: "";
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: var(--accent);
  transform: scale(0);
  transition: transform .25s cubic-bezier(.34,1.56,.64,1);
}

.crb-05a__input:checked {
  border-color: var(--accent);
}

.crb-05a__input:checked::before {
  transform: scale(1);
}

.crb-05a__input:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.crb-05a__text {
  font-size: 15.5px;
  color: var(--ink);
}

.crb-05a__note {
  font-style: normal;
  font-size: 13px;
  color: #9aa0b2;
}

.crb-05a__input:disabled {
  border-color: #dcdfe8;
  background: #f2f3f7;
  cursor: not-allowed;
}

.crb-05a__row--disabled {
  cursor: not-allowed;
  color: #9aa0b2;
}

.crb-05a__row--disabled:hover {
  background: transparent;
}

.crb-05a__row--disabled .crb-05a__text {
  color: #9aa0b2;
}

@media (prefers-reduced-motion: reduce) {
  .crb-05a__input::before {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript, no hidden inputs, no ARIA patches — appearance:none styles the real radio element; every semantic comes free from the browser. */
```
