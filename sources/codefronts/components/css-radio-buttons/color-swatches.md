---
source: "codefronts"
url: "https://codefronts.com/components/css-radio-buttons/color-swatches/"
title: "Product Color Swatch Selector"
section: "components"
category: "css-radio-buttons"
category_name: "CSS Radio Buttons"
description: "The e-commerce essential: circular colour swatches that act as radio buttons, wired to a live product photo that recolours instantly when you pick a swatch —…"
has_js: "false"
---

Here's a working CSS Radio Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Product Color Swatch Selector
Source: https://codefronts.com/components/css-radio-buttons/color-swatches/

The e-commerce essential: circular colour swatches that act as radio buttons, wired to a live product photo that recolours instantly when you pick a swatch — no JavaScript, the product image's filter is switched by :has() from the swatch state. Checked swatch gets an offset ring; the label text updates too.
## HTML
```html
<div class="crb-14-group">
<section class="crb-14a" aria-label="Product color swatch selector">
  <div class="crb-14a__stage">
    <figure class="crb-14a__media">
      <img class="crb-14a__img" src="https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=640&q=80&auto=format&fit=crop" alt="Classic crew-neck t-shirt on a hanger" loading="lazy">
    </figure>
    <fieldset class="crb-14a__group">
      <legend class="crb-14a__legend">Classic Crew Tee</legend>
      <p class="crb-14a__label">Colour:
        <span class="crb-14a__cap" data-cap="natural">Natural white</span><span class="crb-14a__cap" data-cap="ocean">Ocean blue</span><span class="crb-14a__cap" data-cap="sage">Sage green</span><span class="crb-14a__cap" data-cap="clay">Baked clay</span>
      </p>
      <div class="crb-14a__swatches">
        <label class="crb-14a__sw" style="--sw:#ece7dd"><input class="crb-14a__input" type="radio" name="crb-14a" value="natural" checked><span class="crb-14a__sr">Natural white</span></label>
        <label class="crb-14a__sw" style="--sw:oklch(0.55 0.12 240)"><input class="crb-14a__input" type="radio" name="crb-14a" value="ocean"><span class="crb-14a__sr">Ocean blue</span></label>
        <label class="crb-14a__sw" style="--sw:oklch(0.62 0.09 150)"><input class="crb-14a__input" type="radio" name="crb-14a" value="sage"><span class="crb-14a__sr">Sage green</span></label>
        <label class="crb-14a__sw" style="--sw:oklch(0.58 0.11 45)"><input class="crb-14a__input" type="radio" name="crb-14a" value="clay"><span class="crb-14a__sr">Baked clay</span></label>
      </div>
    </fieldset>
  </div>
</section>
</div>
```
## CSS
```css
.crb-14-group {
  display: flex;
  flex-wrap: wrap;
  align-items: stretch;
  gap: 0;
}

.crb-14-group > section {
  flex: 1 1 340px;
  min-width: 300px;
}

.crb-14a,
.crb-14a *,
.crb-14a *::before,
.crb-14a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.crb-14a {
  --ink: #211f1c;
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: #f5f3ef;
}

.crb-14a__stage {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 36px;
  justify-content: center;
}

.crb-14a__media {
  width: min(300px,80vw);
  aspect-ratio: 4/5;
  border-radius: 20px;
  overflow: hidden;
  background: #e8e4dc;
}

.crb-14a__img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: filter .5s ease;
}

.crb-14a__group {
  border: none;
  width: 240px;
}

.crb-14a__legend {
  font-size: 24px;
  font-weight: 750;
  color: var(--ink);
  letter-spacing: -.02em;
}

.crb-14a__label {
  margin-top: 10px;
  font-size: 14px;
  color: #7c766c;
  display: flex;
  gap: 6px;
}

.crb-14a__cap {
  display: none;
  font-weight: 650;
  color: var(--ink);
}

.crb-14a__swatches {
  display: flex;
  gap: 14px;
  margin-top: 16px;
}

.crb-14a__sw {
  position: relative;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: var(--sw);
  cursor: pointer;
  box-shadow: inset 0 0 0 1px rgba(0,0,0,.12);
  transition: transform .25s cubic-bezier(.34,1.56,.64,1),box-shadow .25s;
}

.crb-14a__input {
  position: absolute;
  opacity: 0;
  width: 1px;
  height: 1px;
}

.crb-14a__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.crb-14a__sw:hover {
  transform: scale(1.1);
}

.crb-14a__sw:has(.crb-14a__input:checked) {
  transform: scale(1.08);
  box-shadow: inset 0 0 0 1px rgba(0,0,0,.12),0 0 0 3px #f5f3ef,0 0 0 5.5px var(--ink);
}

.crb-14a__sw:has(.crb-14a__input:focus-visible) {
  outline: 3px solid var(--ink);
  outline-offset: 4px;
}

.crb-14a__stage:has(.crb-14a__input[value="natural"]:checked) .crb-14a__cap[data-cap="natural"] {
  display: inline;
}

.crb-14a__stage:has(.crb-14a__input[value="ocean"]:checked) .crb-14a__cap[data-cap="ocean"] {
  display: inline;
}

.crb-14a__stage:has(.crb-14a__input[value="sage"]:checked) .crb-14a__cap[data-cap="sage"] {
  display: inline;
}

.crb-14a__stage:has(.crb-14a__input[value="clay"]:checked) .crb-14a__cap[data-cap="clay"] {
  display: inline;
}

.crb-14a__stage:has(.crb-14a__input[value="ocean"]:checked) .crb-14a__img {
  filter: sepia(.9) saturate(2.2) hue-rotate(170deg) brightness(.82);
}

.crb-14a__stage:has(.crb-14a__input[value="sage"]:checked) .crb-14a__img {
  filter: sepia(.8) saturate(1.6) hue-rotate(70deg) brightness(.9);
}

.crb-14a__stage:has(.crb-14a__input[value="clay"]:checked) .crb-14a__img {
  filter: sepia(.95) saturate(2) hue-rotate(-15deg) brightness(.85);
}

@media (prefers-reduced-motion: reduce) {
  .crb-14a__img {
    transition: none;
  }

  .crb-14a__sw {
    transition: box-shadow .2s;
  }

  .crb-14a__sw:hover,
    .crb-14a__sw:has(.crb-14a__input:checked) {
    transform: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — :has(input[value=…]:checked) on the stage switches the product photo's filter and the visible colour caption; the checked ring is a double box-shadow that works on any background. */
```
