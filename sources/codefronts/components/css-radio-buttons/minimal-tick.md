---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/minimal-tick/"
title: "Minimal Checkmark Radio Button"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "Radical restraint: a typography-first option list where the only ornament is a checkmark that draws itself — two strokes of the tick sweep in sequentially…"
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimal Checkmark Radio Button
Source: https://codefronts.com/components/css-radio-buttons/minimal-tick/

Radical restraint: a typography-first option list where the only ornament is a checkmark that draws itself — two strokes of the tick sweep in sequentially when an option is chosen, and the selected line ink-darkens while the others recede. The minimalist radio for editorial sites, portfolios and quiet products.
## HTML
```html
<div class="crb-13-group">
<section class="crb-13a" aria-label="Minimal checkmark radio buttons">
  <fieldset class="crb-13a__group">
    <legend class="crb-13a__legend">Typeface</legend>
    <div class="crb-13a__list">
      <label class="crb-13a__row"><input class="crb-13a__input" type="radio" name="crb-13a" value="grotesk" checked><svg class="crb-13a__tick" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline class="crb-13a__stroke" points="4.5 12.5 9.5 17.5 19.5 6.5"/></svg><span class="crb-13a__text">Neue Grotesk</span></label>
      <label class="crb-13a__row"><input class="crb-13a__input" type="radio" name="crb-13a" value="serif"><svg class="crb-13a__tick" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline class="crb-13a__stroke" points="4.5 12.5 9.5 17.5 19.5 6.5"/></svg><span class="crb-13a__text">Editorial Serif</span></label>
      <label class="crb-13a__row"><input class="crb-13a__input" type="radio" name="crb-13a" value="mono"><svg class="crb-13a__tick" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline class="crb-13a__stroke" points="4.5 12.5 9.5 17.5 19.5 6.5"/></svg><span class="crb-13a__text">Studio Mono</span></label>
    </div>
  </fieldset>
</section>
</div>
```
## CSS
```css
.crb-13-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-13-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-13a,
.crb-13a *,
.crb-13a *::before,
.crb-13a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-13a {
  --ink: #191919;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #fcfcfa;
}

.crb-13a__group {
  border: none;
  width: min(320px,100%);
}

.crb-13a__legend {
  font-size: 13px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: #9a9a94;
}

.crb-13a__list {
  display: grid;
  margin-top: 14px;
}

.crb-13a__row {
  position: relative;
  display: flex;
  align-items: center;
  gap: 14px;
  min-height: 52px;
  border-bottom: 1px solid #ebebe6;
  cursor: pointer;
}

.crb-13a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-13a__tick {
  width: 20px;
  height: 20px;
  flex: none;
  color: var(--ink);
}

.crb-13a__stroke {
  stroke-dasharray: 28;
  stroke-dashoffset: 28;
  transition: stroke-dashoffset .35s cubic-bezier(.22,1,.36,1);
}

.crb-13a__text {
  font-size: 19px;
  font-weight: 450;
  color: rgba(25,25,25,.55);
  letter-spacing: -.01em;
  transition: color .3s,font-weight .3s;
}

.crb-13a__row:hover .crb-13a__text {
  color: rgba(25,25,25,.8);
}

.crb-13a__row:has(.crb-13a__input:checked) .crb-13a__stroke {
  stroke-dashoffset: 0;
}

.crb-13a__row:has(.crb-13a__input:checked) .crb-13a__text {
  color: var(--ink);
  font-weight: 650;
}

.crb-13a__row:has(.crb-13a__input:focus-visible) {
  outline: 3px solid var(--ink);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .crb-13a__stroke {
    transition: none;
  }

  .crb-13a__text {
    transition: color .2s;
  }
}
```

## JavaScript
```js
/* No JavaScript — the tick is an SVG polyline drawn on via stroke-dashoffset 28→0 when :has(input:checked) matches; selection is otherwise pure typography. */
```
