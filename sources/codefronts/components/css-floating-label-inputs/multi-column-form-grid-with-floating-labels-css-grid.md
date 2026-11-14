---
source: "codefronts"
url: "https://codefronts.com/components/css-floating-label-inputs/multi-column-form-grid-with-floating-labels-css-grid/"
title: "Multi-Column Form Grid with Floating Labels (CSS Grid)"
section: "components"
category: "css-floating-label-inputs"
category_name: "CSS Floating Label Inputs"
description: "A full checkout-style address form laying floating label fields into a responsive CSS grid: paired columns on desktop, asymmetric spans for city/state/ZIP,…"
has_js: "false"
---

Here's a working CSS Floating Label Input from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Column Form Grid with Floating Labels (CSS Grid)
Source: https://codefronts.com/components/css-floating-label-inputs/multi-column-form-grid-with-floating-labels-css-grid/

A full checkout-style address form laying floating label fields into a responsive CSS grid: paired columns on desktop, asymmetric spans for city/state/ZIP, and a single column under 560px — proving the floating label pattern composes cleanly when fields share rows, gaps and baselines. Variation: floated labels snap to UPPERCASE MICRO-LEGENDS with wide tracking — reading as engraved field headings that unify the whole grid.
## HTML
```html
<section class="flb-16" aria-label="Multi-column form grid floating labels demo">
  <form class="flb-16__form" novalidate>
    <h3 class="flb-16__title">Shipping address</h3>
    <div class="flb-16__grid">
      <div class="flb-16__field" style="--span:3">
        <input class="flb-16__input" type="text" id="flb-16-first" name="given-name" placeholder=" " autocomplete="given-name">
        <label class="flb-16__label" for="flb-16-first">First name</label>
      </div>
      <div class="flb-16__field" style="--span:3">
        <input class="flb-16__input" type="text" id="flb-16-last" name="family-name" placeholder=" " autocomplete="family-name">
        <label class="flb-16__label" for="flb-16-last">Last name</label>
      </div>
      <div class="flb-16__field" style="--span:6">
        <input class="flb-16__input" type="text" id="flb-16-street" name="street-address" placeholder=" " autocomplete="street-address">
        <label class="flb-16__label" for="flb-16-street">Street address</label>
      </div>
      <div class="flb-16__field" style="--span:2">
        <input class="flb-16__input" type="text" id="flb-16-city" name="address-level2" placeholder=" " autocomplete="address-level2">
        <label class="flb-16__label" for="flb-16-city">City</label>
      </div>
      <div class="flb-16__field" style="--span:2">
        <input class="flb-16__input" type="text" id="flb-16-state" name="address-level1" placeholder=" " autocomplete="address-level1">
        <label class="flb-16__label" for="flb-16-state">State</label>
      </div>
      <div class="flb-16__field" style="--span:2">
        <input class="flb-16__input" type="text" id="flb-16-zip" name="postal-code" placeholder=" " inputmode="numeric" autocomplete="postal-code">
        <label class="flb-16__label" for="flb-16-zip">ZIP</label>
      </div>
    </div>
    <button class="flb-16__btn" type="button">Continue to payment</button>
  </form>
</section>
```
## CSS
```css
.flb-16,
.flb-16 *,
.flb-16 *::before,
.flb-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.flb-16 {
  --accent: oklch(0.52 0.16 264);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f0f1f5;
  padding: 40px 20px;
  container-type: inline-size;
}

.flb-16__form {
  width: min(560px,100%);
  background: #fff;
  border-radius: 20px;
  padding: 34px 32px;
  box-shadow: 0 24px 60px -32px rgba(24,28,60,.35);
  display: flex;
  flex-direction: column;
  gap: 22px;
  container-type: inline-size;
  container-name: flb16form;
}

.flb-16__title {
  font-size: 23px;
  font-weight: 800;
  color: #191c2b;
  letter-spacing: -.02em;
}

.flb-16__grid {
  display: grid;
  grid-template-columns: repeat(6,1fr);
  gap: 16px;
}

.flb-16__field {
  position: relative;
  grid-column: span var(--span,6);
}

.flb-16__input {
  width: 100%;
  height: 56px;
  padding: 22px 16px 6px;
  font-size: 16px;
  color: #191c2b;
  background: #fff;
  border: 1.5px solid #d6d9e4;
  border-radius: 12px;
  outline: none;
  transition: border-color .2s,box-shadow .2s;
}

.flb-16__input:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 4px oklch(0.52 0.16 264 / .13);
}

.flb-16__label {
  position: absolute;
  left: 16px;
  top: 50%;
  translate: 0 -50%;
  font-size: 15px;
  color: #7a7f93;
  pointer-events: none;
  transform-origin: left center;
  transition: transform .18s,color .18s;
  max-width: calc(100% - 28px);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.flb-16__input:focus ~ .flb-16__label,
.flb-16__input:not(:placeholder-shown) ~ .flb-16__label {
  transform: translateY(-14px) scale(.7);
  text-transform: uppercase;
  letter-spacing: .12em;
  font-weight: 700;
}

.flb-16__input:focus ~ .flb-16__label {
  color: var(--accent);
}

.flb-16__btn {
  height: 52px;
  border: none;
  border-radius: 12px;
  background: var(--accent);
  color: #fff;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  transition: filter .15s;
}

.flb-16__btn:hover {
  filter: brightness(1.12);
}

.flb-16__btn:focus-visible,
.flb-16__input:focus-visible {
  outline: 3px solid oklch(0.52 0.16 264 / .5);
  outline-offset: 2px;
}

@container flb16form (max-width: 559px) {
  .flb-16__field {
    grid-column: span 6;
  }
}

@media (prefers-reduced-motion: reduce) {
  .flb-16__label,
    .flb-16__input {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — a 6-track CSS grid with per-field --span variables handles all column layouts; a container query collapses to one column based on the form's own width, not the viewport's. */
```
