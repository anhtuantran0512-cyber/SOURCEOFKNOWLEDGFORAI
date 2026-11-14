---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/ink-drop/"
title: "Ink Splash Animation Radio"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "Material-style ink ripple, reimagined for radio rows: checking an option splashes a circle of ink from the indicator outward until it floods the whole row…"
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ink Splash Animation Radio
Source: https://codefronts.com/components/css-radio-buttons/ink-drop/

Material-style ink ripple, reimagined for radio rows: checking an option splashes a circle of ink from the indicator outward until it floods the whole row with a soft wash, while the dot itself stamps in like a wet ink press. Warm paper background, pure CSS.
## HTML
```html
<div class="crb-10-group">
<section class="crb-10a" aria-label="Ink splash radio buttons">
  <fieldset class="crb-10a__group">
    <legend class="crb-10a__legend">Paper stock</legend>
    <div class="crb-10a__list">
      <label class="crb-10a__row"><input class="crb-10a__input" type="radio" name="crb-10a" value="matte" checked><span class="crb-10a__radio" aria-hidden="true"></span><span class="crb-10a__text">Matte <span class="crb-10a__sub">soft, no glare</span></span></label>
      <label class="crb-10a__row"><input class="crb-10a__input" type="radio" name="crb-10a" value="satin"><span class="crb-10a__radio" aria-hidden="true"></span><span class="crb-10a__text">Satin <span class="crb-10a__sub">gentle sheen</span></span></label>
      <label class="crb-10a__row"><input class="crb-10a__input" type="radio" name="crb-10a" value="gloss"><span class="crb-10a__radio" aria-hidden="true"></span><span class="crb-10a__text">Gloss <span class="crb-10a__sub">vivid, reflective</span></span></label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-10-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-10-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-10a,
.crb-10a *,
.crb-10a *::before,
.crb-10a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-10a {
  --ink-c: oklch(0.45 0.16 265);
  --body: #2a2620;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #f6f1e7;
}

.crb-10a__group {
  border: none;
  width: min(400px,100%);
}

.crb-10a__legend {
  font-size: 24px;
  font-weight: 750;
  color: var(--body);
  letter-spacing: -.02em;
}

.crb-10a__list {
  display: grid;
  gap: 8px;
  margin-top: 18px;
}

.crb-10a__row {
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 56px;
  padding: 0 18px;
  background: #fffdf8;
  border: 1.5px solid #e7dfd0;
  border-radius: 14px;
  cursor: pointer;
  transition: border-color .3s;
}

.crb-10a__row::before {
  content: "";
  position: absolute;
  left: 28px;
  top: 50%;
  width: 30px;
  height: 30px;
  margin: -15px;
  border-radius: 50%;
  background: radial-gradient(circle,color-mix(in oklab,var(--ink-c) 12%,transparent) 0%,color-mix(in oklab,var(--ink-c) 9%,transparent) 55%,color-mix(in oklab,var(--ink-c) 7%,transparent) 80%,transparent 97%);
  transform: scale(0);
  opacity: 0;
  transition: transform .2s,opacity .3s;
  pointer-events: none;
}

.crb-10a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-10a__radio {
  position: relative;
  z-index: 1;
  width: 22px;
  height: 22px;
  flex: none;
  border-radius: 50%;
  border: 2px solid #bfb49d;
  display: grid;
  place-items: center;
  transition: border-color .3s;
}

.crb-10a__radio::after {
  content: "";
  width: 11px;
  height: 11px;
  border-radius: 50%;
  background: var(--ink-c);
  transform: scale(0);
  transition: transform .35s cubic-bezier(.34,1.7,.5,1);
}

.crb-10a__text {
  position: relative;
  z-index: 1;
  display: grid;
  font-size: 15.5px;
  font-weight: 650;
  color: var(--body);
}

.crb-10a__sub {
  font-size: 12.5px;
  font-weight: 450;
  color: #8d8471;
}

.crb-10a__row:hover {
  border-color: color-mix(in oklab,var(--ink-c) 35%,#e7dfd0);
}

.crb-10a__row:has(.crb-10a__input:checked) {
  border-color: color-mix(in oklab,var(--ink-c) 55%,#e7dfd0);
}

.crb-10a__row:has(.crb-10a__input:checked)::before {
  transform: scale(34);
  opacity: 1;
  transition: transform .8s cubic-bezier(.22,1,.36,1),opacity .2s;
}

.crb-10a__row:has(.crb-10a__input:checked) .crb-10a__radio {
  border-color: var(--ink-c);
}

.crb-10a__row:has(.crb-10a__input:checked) .crb-10a__radio::after {
  transform: scale(1);
}

.crb-10a__row:has(.crb-10a__input:focus-visible) {
  outline: 3px solid var(--ink-c);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .crb-10a__row::before {
    transition: opacity .2s;
  }

  .crb-10a__row:has(.crb-10a__input:checked)::before {
    transform: scale(34);
    transition: opacity .2s;
  }

  .crb-10a__radio::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a radial-gradient circle anchored at the indicator scales 0→34 inside the clipped row on :has(input:checked); the outgoing row's wash fades out faster, like drying ink. */
```
