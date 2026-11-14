---
source: "codefronts"
url: "https://codefronts.com/components/css-product-cards/sneaker-colour-size-picker-card/"
title: "Sneaker Colour + Size Picker Card"
section: "components"
category: "css-product-cards"
category_name: "CSS Product Cards"
description: "A Nike/Adidas-style sneaker card with interactive colourway swatches that recolour the product on click and a row of size chips — all with pure CSS via…"
has_js: "false"
---

Here's a working CSS Product Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sneaker Colour + Size Picker Card
Source: https://codefronts.com/components/css-product-cards/sneaker-colour-size-picker-card/

A Nike/Adidas-style sneaker card with interactive colourway swatches that recolour the product on click and a row of size chips — all with pure CSS via hidden radio inputs and :checked, no JavaScript. The exact sneaker-picker layout devs search for.
## HTML
```html
<article class="cpc-14">
  <div class="cpc-14__card">
    <div class="cpc-14__media" role="img" aria-label="Product photo: Aurora Runner sneaker"><span>product shot</span></div>
    <div class="cpc-14__body">
      <p class="cpc-14__brand">Aerolite</p>
      <h3 class="cpc-14__name">Aurora Runner</h3>
      <fieldset class="cpc-14__colors"><legend>Colour</legend>
        <label class="cpc-14__sw" style="--sw:oklch(0.6 0.16 25)"><input type="radio" name="cpc-14-color" checked><span aria-label="Ember red"></span></label>
        <label class="cpc-14__sw" style="--sw:oklch(0.6 0.14 250)"><input type="radio" name="cpc-14-color"><span aria-label="Cobalt blue"></span></label>
        <label class="cpc-14__sw" style="--sw:oklch(0.62 0.15 150)"><input type="radio" name="cpc-14-color"><span aria-label="Pine green"></span></label>
        <label class="cpc-14__sw" style="--sw:oklch(0.3 0.02 260)"><input type="radio" name="cpc-14-color"><span aria-label="Graphite"></span></label>
      </fieldset>
      <fieldset class="cpc-14__sizes"><legend>Size (UK)</legend>
        <label class="cpc-14__size"><input type="radio" name="cpc-14-size"><span>7</span></label>
        <label class="cpc-14__size"><input type="radio" name="cpc-14-size" checked><span>8</span></label>
        <label class="cpc-14__size"><input type="radio" name="cpc-14-size"><span>9</span></label>
        <label class="cpc-14__size"><input type="radio" name="cpc-14-size"><span>10</span></label>
        <label class="cpc-14__size"><input type="radio" name="cpc-14-size"><span>11</span></label>
      </fieldset>
      <div class="cpc-14__foot"><p class="cpc-14__price">$140</p><button class="cpc-14__cta" type="button">Add to Cart</button></div>
    </div>
  </div>
</article>
```
## CSS
```css
.cpc-14,
.cpc-14 *,
.cpc-14 *::before,
.cpc-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpc-14 ::selection {
  background: oklch(0.6 0.16 25);
  color: #fff;
}

.cpc-14 {
  --accent: oklch(0.28 0.03 260);
  --tint: oklch(0.6 0.16 25);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 48px 20px;
  background: #f0f1f4;
}

.cpc-14__card {
  width: 320px;
  border-radius: 20px;
  overflow: hidden;
  background: #fff;
  box-shadow: 0 18px 44px -24px rgba(16,24,40,.45);
}

.cpc-14__media {
  aspect-ratio: 16/11;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg,color-mix(in oklch,var(--tint) 22%,#eef0f4),color-mix(in oklch,var(--tint) 40%,#dfe2ea)), repeating-linear-gradient(45deg,rgba(255,255,255,.35) 0 14px,transparent 14px 28px);
  transition: background .4s;
}

.cpc-14__media {
  background-image: linear-gradient(135deg,color-mix(in oklch,var(--tint) 42%,transparent),color-mix(in oklch,var(--tint) 16%,transparent)),url("https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?q=80&w=600&h=600&auto=format&fit=crop");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  transition: background .4s;
}

.cpc-14__media span {
  display: none;
}

.cpc-14__body {
  padding: 18px 20px 20px;
}

.cpc-14__brand {
  font: 11px ui-monospace,Menlo,monospace;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: #98a2b8;
}

.cpc-14__name {
  margin-top: 4px;
  font-size: 20px;
  font-weight: 700;
  color: #101828;
}

.cpc-14__colors,
.cpc-14__sizes {
  border: none;
  margin-top: 16px;
}

.cpc-14__colors legend,
.cpc-14__sizes legend {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: #667085;
  margin-bottom: 8px;
}

.cpc-14__colors {
  display: flex;
  gap: 10px;
}

.cpc-14__sw {
  cursor: pointer;
}

.cpc-14__sw input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.cpc-14__sw span {
  display: block;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: var(--sw);
  box-shadow: 0 0 0 2px #fff,0 0 0 3px #d0d5dd;
  transition: box-shadow .2s,transform .2s;
}

.cpc-14__sw:hover span {
  transform: scale(1.08);
}

.cpc-14__sw input:checked+span {
  box-shadow: 0 0 0 2px #fff,0 0 0 3px var(--sw),0 0 0 5px color-mix(in oklch,var(--sw) 30%,#fff);
}

.cpc-14__sw input:focus-visible+span {
  box-shadow: 0 0 0 2px #fff,0 0 0 4px #101828;
}

.cpc-14__sizes {
  display: block;
}

.cpc-14__sizes .cpc-14__size {
  display: inline-block;
  margin-right: 8px;
  cursor: pointer;
}

.cpc-14__size input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.cpc-14__size span {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border-radius: 10px;
  border: 1px solid #d0d5dd;
  background: #fff;
  color: #344054;
  font-size: 14px;
  font-weight: 600;
  transition: .2s;
}

.cpc-14__size:hover span {
  border-color: #98a2b8;
}

.cpc-14__size input:checked+span {
  background: #101828;
  color: #fff;
  border-color: #101828;
}

.cpc-14__size input:focus-visible+span {
  outline: 2px solid #101828;
  outline-offset: 2px;
}

.cpc-14__foot {
  margin-top: 18px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.cpc-14__price {
  font-size: 22px;
  font-weight: 800;
  color: #101828;
}

.cpc-14__cta {
  height: 46px;
  padding: 0 22px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  background: var(--tint);
  color: #fff;
  font-size: 14px;
  font-weight: 700;
  transition: background .3s;
}

.cpc-14__cta:hover {
  filter: brightness(1.05);
}

.cpc-14__cta:focus-visible {
  outline: 3px solid #101828;
  outline-offset: 2px;
}
/* checked colour drives the whole card tint */

.cpc-14:has(.cpc-14__sw:nth-child(1) input:checked) {
  --tint: oklch(0.6 0.16 25);
}

.cpc-14:has(.cpc-14__sw:nth-child(2) input:checked) {
  --tint: oklch(0.6 0.14 250);
}

.cpc-14:has(.cpc-14__sw:nth-child(3) input:checked) {
  --tint: oklch(0.62 0.15 150);
}

.cpc-14:has(.cpc-14__sw:nth-child(4) input:checked) {
  --tint: oklch(0.42 0.03 260);
}

@media (prefers-reduced-motion: reduce) {
  .cpc-14__media,
    .cpc-14__sw span,
    .cpc-14__size span,
    .cpc-14__cta {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — hidden radios + :checked (with :has() for the tint) drive colour and size selection. */
```
