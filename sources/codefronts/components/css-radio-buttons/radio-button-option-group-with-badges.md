---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/radio-button-option-group-with-badges/"
title: "Radio Button Option Group with Badges"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "A conversion-focused option list where marketing meta lives inside the choice: each radio row carries a price and a status badge — \"Most popular\" and \"Best…"
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Radio Button Option Group with Badges
Source: https://codefronts.com/components/css-radio-buttons/radio-button-option-group-with-badges/

A conversion-focused option list where marketing meta lives inside the choice: each radio row carries a price and a status badge — "Most popular" and "Best value" — the pattern behind every high-converting plan picker and add-on selector in modern checkout flows.
## HTML
```html
<div class="crb-06-group">
<section class="crb-06a" aria-label="Radio option group with badges">
  <fieldset class="crb-06a__group">
    <legend class="crb-06a__legend">Choose a plan</legend>
    <div class="crb-06a__list">
      <label class="crb-06a__row">
        <input class="crb-06a__input" type="radio" name="crb-06a" value="basic">
        <span class="crb-06a__radio" aria-hidden="true"></span>
        <span class="crb-06a__name">Basic</span>
        <span class="crb-06a__spacer"></span>
        <span class="crb-06a__price">$9<small>/mo</small></span>
      </label>
      <label class="crb-06a__row">
        <input class="crb-06a__input" type="radio" name="crb-06a" value="pro" checked>
        <span class="crb-06a__radio" aria-hidden="true"></span>
        <span class="crb-06a__name">Pro</span>
        <em class="crb-06a__badge crb-06a__badge--popular">Most popular</em>
        <span class="crb-06a__price">$24<small>/mo</small></span>
      </label>
      <label class="crb-06a__row">
        <input class="crb-06a__input" type="radio" name="crb-06a" value="team">
        <span class="crb-06a__radio" aria-hidden="true"></span>
        <span class="crb-06a__name">Team</span>
        <em class="crb-06a__badge crb-06a__badge--value">Best value</em>
        <span class="crb-06a__price">$59<small>/mo</small></span>
      </label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-06-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-06-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-06a,
.crb-06a *,
.crb-06a *::before,
.crb-06a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-06a {
  --accent: oklch(0.55 0.21 300);
  --ink: #1e2130;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #f6f5fa;
}

.crb-06a__group {
  border: none;
  width: min(430px,100%);
}

.crb-06a__legend {
  font-size: 24px;
  font-weight: 750;
  color: var(--ink);
  letter-spacing: -.02em;
}

.crb-06a__list {
  display: grid;
  gap: 10px;
  margin-top: 20px;
}

.crb-06a__row {
  position: relative;
  display: flex;
  align-items: center;
  gap: 12px;
  min-height: 58px;
  padding: 0 18px;
  background: #fff;
  border: 2px solid #e6e6ef;
  border-radius: 14px;
  cursor: pointer;
  transition: border-color .25s,background .25s,box-shadow .25s;
}

.crb-06a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-06a__radio {
  width: 21px;
  height: 21px;
  flex: none;
  border-radius: 50%;
  border: 2px solid #c3c8d9;
  display: grid;
  place-items: center;
  transition: border-color .25s,background .25s;
}

.crb-06a__radio::after {
  content: "";
  width: 9px;
  height: 9px;
  border-radius: 50%;
  background: #fff;
  transform: scale(0);
  transition: transform .3s cubic-bezier(.34,1.56,.64,1);
}

.crb-06a__name {
  font-size: 15.5px;
  font-weight: 700;
  color: var(--ink);
}

.crb-06a__spacer {
  flex: 1;
}

.crb-06a__badge {
  font-style: normal;
  font-size: 11px;
  font-weight: 750;
  letter-spacing: .02em;
  padding: 3px 9px;
  border-radius: 9999px;
  white-space: nowrap;
}

.crb-06a__badge--popular {
  background: color-mix(in oklab,var(--accent) 14%,white);
  color: var(--accent);
  flex: none;
  margin-right: auto;
}

.crb-06a__badge--value {
  background: oklch(0.93 0.07 155);
  color: oklch(0.42 0.12 155);
  flex: none;
  margin-right: auto;
}

.crb-06a__price {
  font-size: 16px;
  font-weight: 750;
  color: var(--ink);
}

.crb-06a__price small {
  font-size: 12px;
  font-weight: 600;
  color: #8a8fa3;
}

.crb-06a__row:hover {
  border-color: color-mix(in oklab,var(--accent) 38%,#e6e6ef);
}

.crb-06a__row:has(.crb-06a__input:checked) {
  border-color: var(--accent);
  background: color-mix(in oklab,var(--accent) 4%,white);
  box-shadow: 0 10px 24px -16px color-mix(in oklab,var(--accent) 55%,transparent);
}

.crb-06a__row:has(.crb-06a__input:checked) .crb-06a__radio {
  border-color: var(--accent);
  background: var(--accent);
}

.crb-06a__row:has(.crb-06a__input:checked) .crb-06a__radio::after {
  transform: scale(1);
}

.crb-06a__row:has(.crb-06a__input:focus-visible) {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .crb-06a__row,
    .crb-06a__radio,
    .crb-06a__radio::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — badge chips are plain <em> elements inside the label; a constant 2px border (transparent → accent) means the checked swap causes zero layout shift. */
```
