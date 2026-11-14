---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/vertical-stack/"
title: "Stacked Vertical Radio List"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "The connected vertical list: options stacked in a single bordered container with hairline dividers — one visual object, not floating cards — with a tinted…"
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stacked Vertical Radio List
Source: https://codefronts.com/components/css-radio-buttons/vertical-stack/

The connected vertical list: options stacked in a single bordered container with hairline dividers — one visual object, not floating cards — with a tinted rail that highlights the checked row. Ideal for payment methods, saved addresses, and dense forms where each row carries trailing meta.
## HTML
```html
<div class="crb-22-group">
<section class="crb-22a" aria-label="Stacked vertical radio list">
  <fieldset class="crb-22a__group">
    <legend class="crb-22a__legend">Payment method</legend>
    <div class="crb-22a__stack">
      <label class="crb-22a__row">
        <input class="crb-22a__input" type="radio" name="crb-22a" value="visa" checked>
        <span class="crb-22a__rail" aria-hidden="true"></span>
        <span class="crb-22a__radio" aria-hidden="true"></span>
        <span class="crb-22a__text"><span class="crb-22a__title">Visa ending 4242</span><span class="crb-22a__sub">Expires 09/28</span></span>
        <span class="crb-22a__meta">Default</span>
      </label>
      <label class="crb-22a__row">
        <input class="crb-22a__input" type="radio" name="crb-22a" value="amex">
        <span class="crb-22a__rail" aria-hidden="true"></span>
        <span class="crb-22a__radio" aria-hidden="true"></span>
        <span class="crb-22a__text"><span class="crb-22a__title">Amex ending 1005</span><span class="crb-22a__sub">Expires 02/27</span></span>
        <span class="crb-22a__meta"></span>
      </label>
      <label class="crb-22a__row">
        <input class="crb-22a__input" type="radio" name="crb-22a" value="bank">
        <span class="crb-22a__rail" aria-hidden="true"></span>
        <span class="crb-22a__radio" aria-hidden="true"></span>
        <span class="crb-22a__text"><span class="crb-22a__title">Bank transfer</span><span class="crb-22a__sub">2–3 business days</span></span>
        <span class="crb-22a__meta">No fee</span>
      </label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-22-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-22-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-22a,
.crb-22a *,
.crb-22a *::before,
.crb-22a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-22a {
  --accent: oklch(0.5 0.16 250);
  --ink: #1e222e;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #f5f6f9;
}

.crb-22a__group {
  border: none;
  width: min(440px,100%);
}

.crb-22a__legend {
  font-size: 24px;
  font-weight: 750;
  color: var(--ink);
  letter-spacing: -.02em;
}

.crb-22a__stack {
  margin-top: 18px;
  background: #fff;
  border: 1.5px solid #e2e5ee;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 1px 4px rgba(25,30,55,.05);
}

.crb-22a__row {
  position: relative;
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 64px;
  padding: 0 20px;
  cursor: pointer;
  transition: background .25s;
}

.crb-22a__row + .crb-22a__row {
  border-top: 1px solid #edeff5;
}

.crb-22a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-22a__rail {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 3px;
  background: var(--accent);
  transform: scaleY(0);
  transform-origin: center;
  transition: transform .3s cubic-bezier(.22,1,.36,1);
}

.crb-22a__radio {
  width: 21px;
  height: 21px;
  flex: none;
  border-radius: 50%;
  border: 2px solid #c4c9da;
  display: grid;
  place-items: center;
  transition: border-color .25s;
}

.crb-22a__radio::after {
  content: "";
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--accent);
  transform: scale(0);
  transition: transform .3s cubic-bezier(.34,1.56,.64,1);
}

.crb-22a__text {
  display: grid;
  gap: 1px;
  flex: 1;
}

.crb-22a__title {
  font-size: 15px;
  font-weight: 650;
  color: var(--ink);
}

.crb-22a__sub {
  font-size: 12.5px;
  color: #7c8296;
}

.crb-22a__meta {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .03em;
  color: #8a90a5;
}

.crb-22a__row:hover {
  background: #f8f9fc;
}

.crb-22a__row:has(.crb-22a__input:checked) {
  background: color-mix(in oklab,var(--accent) 5%,white);
}

.crb-22a__row:has(.crb-22a__input:checked) .crb-22a__rail {
  transform: scaleY(1);
}

.crb-22a__row:has(.crb-22a__input:checked) .crb-22a__radio {
  border-color: var(--accent);
}

.crb-22a__row:has(.crb-22a__input:checked) .crb-22a__radio::after {
  transform: scale(1);
}

.crb-22a__row:has(.crb-22a__input:checked) .crb-22a__meta {
  color: var(--accent);
}

.crb-22a__row:has(.crb-22a__input:focus-visible) {
  outline: 3px solid var(--accent);
  outline-offset: -3px;
}

@media (prefers-reduced-motion: reduce) {
  .crb-22a__row,
    .crb-22a__rail,
    .crb-22a__radio,
    .crb-22a__radio::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — one bordered container, hairline border-top dividers, and a left accent rail that scales in via :has(input:checked); overflow:hidden clips the wash at the corners. */
```
