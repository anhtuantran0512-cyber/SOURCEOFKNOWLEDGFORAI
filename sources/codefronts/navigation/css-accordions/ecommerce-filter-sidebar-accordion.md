---
source: "codefronts"
url: "https://codefronts.com/navigation/css-accordions/ecommerce-filter-sidebar-accordion/"
title: "E-commerce Filter Sidebar Accordion with Exclusive Open (Product Filters)"
section: "navigation"
category: "css-accordions"
category_name: "CSS Accordions — Vertical & Horizontal"
description: "The store-sidebar staple: Size, Color and Price filter groups as <details name=\"\"> accordions where opening one closes the rest — plus real checkboxes with…"
has_js: "false"
---

Here's a working CSS Accordions — Vertical & Horizontal from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-commerce Filter Sidebar Accordion with Exclusive Open (Product Filters)
Source: https://codefronts.com/navigation/css-accordions/ecommerce-filter-sidebar-accordion/

The store-sidebar staple: Size, Color and Price filter groups as <details name=""> accordions where opening one closes the rest — plus real checkboxes with custom styling, live result-count badges and color swatches. Solves the long-sidebar problem on category pages with zero JavaScript.
## HTML
```html
<section class="acc-03" aria-label="E-commerce filter sidebar accordion demo">
  <aside class="acc-03__side">
    <div class="acc-03__head"><h3 class="acc-03__title">Filters</h3><button type="button" class="acc-03__clear">Clear all</button></div>
    <details class="acc-03__group" name="acc-03-filters" open>
      <summary class="acc-03__sum">Size <span class="acc-03__badge">6</span></summary>
      <div class="acc-03__body acc-03__body--grid">
        <label class="acc-03__size"><input type="checkbox" name="size" value="xs"><span>XS</span></label>
        <label class="acc-03__size"><input type="checkbox" name="size" value="s" checked><span>S</span></label>
        <label class="acc-03__size"><input type="checkbox" name="size" value="m"><span>M</span></label>
        <label class="acc-03__size"><input type="checkbox" name="size" value="l"><span>L</span></label>
        <label class="acc-03__size"><input type="checkbox" name="size" value="xl"><span>XL</span></label>
        <label class="acc-03__size"><input type="checkbox" name="size" value="xxl"><span>2XL</span></label>
      </div>
    </details>
    <details class="acc-03__group" name="acc-03-filters">
      <summary class="acc-03__sum">Color <span class="acc-03__badge">5</span></summary>
      <div class="acc-03__body acc-03__body--row">
        <label class="acc-03__swatch" style="--sw:#1b1b1f"><input type="checkbox" name="color" value="black"><span></span><i>Black</i></label>
        <label class="acc-03__swatch" style="--sw:#8a4d2e"><input type="checkbox" name="color" value="tan"><span></span><i>Tan</i></label>
        <label class="acc-03__swatch" style="--sw:#3f5d43"><input type="checkbox" name="color" value="olive" checked><span></span><i>Olive</i></label>
        <label class="acc-03__swatch" style="--sw:#41598e"><input type="checkbox" name="color" value="navy"><span></span><i>Navy</i></label>
        <label class="acc-03__swatch" style="--sw:#d8d3c8"><input type="checkbox" name="color" value="bone"><span></span><i>Bone</i></label>
      </div>
    </details>
    <details class="acc-03__group" name="acc-03-filters">
      <summary class="acc-03__sum">Price <span class="acc-03__badge">4</span></summary>
      <div class="acc-03__body">
        <label class="acc-03__check"><input type="checkbox" name="price" value="0-50"><span class="acc-03__box"></span>Under $50 <em>128</em></label>
        <label class="acc-03__check"><input type="checkbox" name="price" value="50-100"><span class="acc-03__box"></span>$50 – $100 <em>94</em></label>
        <label class="acc-03__check"><input type="checkbox" name="price" value="100-200"><span class="acc-03__box"></span>$100 – $200 <em>52</em></label>
        <label class="acc-03__check"><input type="checkbox" name="price" value="200+"><span class="acc-03__box"></span>Over $200 <em>17</em></label>
      </div>
    </details>
    <button type="button" class="acc-03__apply">Show 291 results</button>
  </aside>
</section>
```
## CSS
```css
.acc-03,
.acc-03 *,
.acc-03 *::before,
.acc-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.acc-03 {
  --accent: oklch(0.45 0.12 40);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f5f2ee;
  padding: 40px 20px;
}

.acc-03__side {
  width: min(340px,100%);
  background: #fff;
  border-radius: 16px;
  padding: 24px 22px;
  box-shadow: 0 24px 60px -34px rgba(60,40,20,.35);
}

.acc-03__head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  margin-bottom: 8px;
}

.acc-03__title {
  font-size: 19px;
  font-weight: 800;
  color: #241d16;
  letter-spacing: -.01em;
}

.acc-03__clear {
  border: none;
  background: none;
  font-size: 13px;
  font-weight: 600;
  color: var(--accent);
  cursor: pointer;
  text-decoration: underline;
  text-underline-offset: 3px;
}

.acc-03__group {
  border-top: 1px solid #ece7e0;
  transition: background .2s;
  border-radius: 10px;
}

.acc-03__group[open] {
  background: #faf8f5;
}

.acc-03__sum {
  list-style: none;
  display: flex;
  align-items: center;
  gap: 8px;
  min-height: 50px;
  padding: 0 8px;
  font-size: 15px;
  font-weight: 700;
  color: #241d16;
  cursor: pointer;
  position: relative;
}

.acc-03__sum::-webkit-details-marker {
  display: none;
}

.acc-03__sum::marker {
  content: "";
}

.acc-03__badge {
  margin-left: auto;
  margin-right: 26px;
  font-size: 11.5px;
  font-weight: 700;
  background: #f0eae2;
  color: #6b5d4c;
  padding: 3px 8px;
  border-radius: 99px;
}

.acc-03__sum::after {
  content: "";
  position: absolute;
  right: 10px;
  width: 8px;
  height: 8px;
  border-right: 2px solid #6b5d4c;
  border-bottom: 2px solid #6b5d4c;
  transform: rotate(45deg) translateY(-2px);
  transition: transform .25s;
}

.acc-03__group[open] > .acc-03__sum::after {
  transform: rotate(225deg) translateY(-2px);
}

.acc-03__body {
  padding: 2px 8px 16px;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.acc-03__body--grid {
  flex-direction: row;
  flex-wrap: wrap;
  gap: 8px;
}

.acc-03__body--row {
  flex-direction: row;
  gap: 14px;
  flex-wrap: wrap;
}

.acc-03__size input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.acc-03__size span {
  display: grid;
  place-content: center;
  min-width: 46px;
  height: 40px;
  padding: 0 10px;
  border: 1.5px solid #ddd5c9;
  border-radius: 9px;
  font-size: 13.5px;
  font-weight: 650;
  color: #4d4237;
  cursor: pointer;
  transition: all .15s;
}

.acc-03__size input:checked + span {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
}

.acc-03__size input:focus-visible + span {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.acc-03__swatch {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5px;
  cursor: pointer;
}

.acc-03__swatch input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.acc-03__swatch span {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--sw);
  border: 2px solid #fff;
  box-shadow: 0 0 0 1.5px #ddd5c9;
  transition: box-shadow .15s;
}

.acc-03__swatch input:checked ~ span {
  box-shadow: 0 0 0 2.5px var(--accent);
}

.acc-03__swatch input:focus-visible ~ span {
  outline: 3px solid var(--accent);
  outline-offset: 3px;
}

.acc-03__swatch i {
  font-style: normal;
  font-size: 11.5px;
  color: #6b5d4c;
}

.acc-03__check {
  display: flex;
  align-items: center;
  gap: 10px;
  min-height: 40px;
  font-size: 14.5px;
  color: #3c332a;
  cursor: pointer;
}

.acc-03__check em {
  font-style: normal;
  margin-left: auto;
  font-size: 12px;
  color: #a0917d;
}

.acc-03__check input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.acc-03__box {
  width: 20px;
  height: 20px;
  border: 1.5px solid #cbbfae;
  border-radius: 6px;
  position: relative;
  transition: all .15s;
  flex: none;
}

.acc-03__check input:checked + .acc-03__box {
  background: var(--accent);
  border-color: var(--accent);
}

.acc-03__check input:checked + .acc-03__box::after {
  content: "";
  position: absolute;
  left: 6px;
  top: 2.5px;
  width: 5px;
  height: 10px;
  border-right: 2.5px solid #fff;
  border-bottom: 2.5px solid #fff;
  transform: rotate(45deg);
}

.acc-03__check input:focus-visible + .acc-03__box {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.acc-03__apply {
  width: 100%;
  margin-top: 16px;
  height: 50px;
  border: none;
  border-radius: 12px;
  background: #241d16;
  color: #fff;
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  transition: background .15s;
}

.acc-03__apply:hover {
  background: var(--accent);
}

.acc-03__sum:focus-visible,
.acc-03__apply:focus-visible,
.acc-03__clear:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
  border-radius: 6px;
}

@media (prefers-reduced-motion: reduce) {
  .acc-03__sum::after,
    .acc-03__group {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — details name="acc-03-filters" gives native exclusive opening (one group closes when another opens), and all filter controls are real checkboxes restyled with :checked sibling selectors. */
```
