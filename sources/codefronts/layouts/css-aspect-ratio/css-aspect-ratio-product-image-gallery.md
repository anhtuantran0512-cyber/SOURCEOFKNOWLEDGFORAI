---
source: "codefronts"
url: "https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-product-image-gallery/"
title: "CSS Aspect Ratio Product Image Gallery"
section: "layouts"
category: "css-aspect-ratio"
category_name: "CSS Aspect Ratio Demos"
description: "A full product page whose gallery is 100% CSS: four hidden radio inputs drive the view, thumbnail labels switch it, and :checked does the state management —…"
has_js: "false"
---

Here's a working CSS Aspect Ratio Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aspect Ratio Product Image Gallery
Source: https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-product-image-gallery/

A full product page whose gallery is 100% CSS: four hidden radio inputs drive the view, thumbnail labels switch it, and :checked does the state management — no JavaScript, no gallery library. The main stage is locked to 4:5 (the portrait ratio apparel retailers standardize on) and the thumbnails to 1:1, so every upload — flat-lay, on-model, detail crop — presents identically. Crossfade between views, keyboard-operable via the radio group, and a details column with real size selectors.
## HTML
```html
<section class="car-06" aria-label="Product image gallery demo">
  <div class="car-06__stage-scroll" id="car06-top">
    <header class="car-06__bar">
      <a class="car-06__brand" href="#car06-top">ATELIER&nbsp;NORD</a>
      <nav class="car-06__crumb" aria-label="Breadcrumb"><a href="#car06-top">Women</a><span aria-hidden="true">/</span><a href="#car06-top">Outerwear</a><span aria-hidden="true">/</span><b aria-current="page">Halden Wool Coat</b></nav>
      <a class="car-06__bag" href="#car06-top">Bag · 2</a>
    </header>
    <main class="car-06__main">
      <div class="car-06__gallery" role="group" aria-label="Product photos, 4 views">
        <input class="car-06__radio" type="radio" name="car06-view" id="car06-v1" checked>
        <input class="car-06__radio" type="radio" name="car06-view" id="car06-v2">
        <input class="car-06__radio" type="radio" name="car06-view" id="car06-v3">
        <input class="car-06__radio" type="radio" name="car06-view" id="car06-v4">
        <figure class="car-06__view">
          <img class="car-06__img car-06__img--1" src="https://images.unsplash.com/photo-1539109136881-3be0616acf4b?q=80&w=900&h=1125&auto=format&fit=crop" width="900" height="1125" alt="Halden coat, front view on model">
          <img class="car-06__img car-06__img--2" src="https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?q=80&w=900&h=1125&auto=format&fit=crop" width="900" height="1125" loading="lazy" alt="Halden coat, styled full look">
          <img class="car-06__img car-06__img--3" src="https://images.unsplash.com/photo-1483985988355-763728e1935b?q=80&w=900&h=1125&auto=format&fit=crop" width="900" height="1125" loading="lazy" alt="Halden coat, movement shot">
          <img class="car-06__img car-06__img--4" src="https://images.unsplash.com/photo-1490481651871-ab68de25d43d?q=80&w=900&h=1125&auto=format&fit=crop" width="900" height="1125" loading="lazy" alt="Halden coat, fabric detail">
          <figcaption class="car-06__ratio-tag">stage <code>4:5</code> · thumbs <code>1:1</code></figcaption>
        </figure>
        <div class="car-06__thumbs">
          <label for="car06-v1"><img src="https://images.unsplash.com/photo-1539109136881-3be0616acf4b?q=80&w=200&h=200&auto=format&fit=crop" width="200" height="200" loading="lazy" alt="Select front view"></label>
          <label for="car06-v2"><img src="https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?q=80&w=200&h=200&auto=format&fit=crop" width="200" height="200" loading="lazy" alt="Select styled look"></label>
          <label for="car06-v3"><img src="https://images.unsplash.com/photo-1483985988355-763728e1935b?q=80&w=200&h=200&auto=format&fit=crop" width="200" height="200" loading="lazy" alt="Select movement shot"></label>
          <label for="car06-v4"><img src="https://images.unsplash.com/photo-1490481651871-ab68de25d43d?q=80&w=200&h=200&auto=format&fit=crop" width="200" height="200" loading="lazy" alt="Select fabric detail"></label>
        </div>
      </div>
      <div class="car-06__info">
        <p class="car-06__kicker">New season · Recycled wool</p>
        <h1>Halden Wool Coat</h1>
        <p class="car-06__price">$248 <s>$310</s> <em>−20%</em></p>
        <p class="car-06__blurb">Every view lands in the same 4:5 stage — flip the thumbnails and watch the box never move. The gallery is radio inputs and <code>:checked</code>; the page ships zero gallery JavaScript.</p>
        <fieldset class="car-06__opts"><legend>Color</legend>
          <label class="car-06__swatch"><input type="radio" name="car06-color" checked><i style="--c:oklch(0.35 0.03 60)"></i><span>Umber</span></label>
          <label class="car-06__swatch"><input type="radio" name="car06-color"><i style="--c:oklch(0.75 0.02 90)"></i><span>Oat</span></label>
          <label class="car-06__swatch"><input type="radio" name="car06-color"><i style="--c:oklch(0.25 0.01 260)"></i><span>Ink</span></label>
        </fieldset>
        <fieldset class="car-06__opts"><legend>Size</legend>
          <label class="car-06__size"><input type="radio" name="car06-size"><span>XS</span></label>
          <label class="car-06__size"><input type="radio" name="car06-size" checked><span>S</span></label>
          <label class="car-06__size"><input type="radio" name="car06-size"><span>M</span></label>
          <label class="car-06__size"><input type="radio" name="car06-size"><span>L</span></label>
          <label class="car-06__size"><input type="radio" name="car06-size"><span>XL</span></label>
        </fieldset>
        <a class="car-06__cta" href="#car06-top">Add to bag — $248</a>
        <p class="car-06__ship">Free carbon-neutral shipping · 60-day returns</p>
        <details class="car-06__more"><summary>Fabric &amp; care</summary><p>72% recycled wool, 20% polyamide, 8% cashmere. Dry clean. Woven in Biella; cut and finished in Porto.</p></details>
        <details class="car-06__more"><summary>Fit notes</summary><p>Relaxed through the shoulder, straight through the body. Model is 178cm in size S. Between sizes? Size down.</p></details>
      </div>
    </main>
    <footer class="car-06__foot">Portrait ratios (4:5, 3:4) keep racks of mixed photography uniform — the stage is the contract, <code>object-fit:cover</code> is the enforcement. A demo from the CodeFronts aspect-ratio collection.</footer>
  </div>
</section>
```
## CSS
```css
.car-06,
.car-06 *,
.car-06 *::before,
.car-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-06 {
  --bg: oklch(0.975 0.006 80);
  --ink: oklch(0.23 0.015 60);
  --mut: oklch(0.5 0.015 60);
  --line: oklch(0.89 0.01 80);
  --acc: oklch(0.45 0.09 50);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.car-06__stage-scroll {
  width: 100%;
  container: car06/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.car-06__bar {
  display: flex;
  align-items: center;
  gap: 18px;
  padding: 16px clamp(16px,4cqi,44px);
  border-bottom: 1px solid var(--line);
  flex-wrap: wrap;
}

.car-06__brand {
  font-size: 15px;
  font-weight: 800;
  letter-spacing: .3em;
  color: inherit;
  text-decoration: none;
}

.car-06__crumb {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12.5px;
  color: var(--mut);
  margin-inline: auto;
  flex-wrap: wrap;
}

.car-06__crumb a {
  color: inherit;
  text-decoration: none;
  padding: 10px 2px;
}

.car-06__crumb a:hover,
.car-06__crumb a:focus-visible {
  color: var(--ink);
  text-decoration: underline;
  text-underline-offset: 3px;
}

.car-06__crumb a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
  border-radius: 2px;
}

.car-06__crumb b {
  color: var(--ink);
  font-weight: 600;
}

.car-06__bag {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 16px;
  border-radius: 99px;
  border: 1px solid var(--line);
  font-size: 12.5px;
  font-weight: 700;
  color: inherit;
  text-decoration: none;
  transition: border-color .2s;
}

.car-06__bag:hover,
.car-06__bag:focus-visible {
  border-color: var(--acc);
}

.car-06__bag:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.car-06__main {
  display: grid;
  grid-template-columns: minmax(0,7fr) minmax(300px,5fr);
  gap: clamp(22px,4cqi,52px);
  align-items: start;
  max-width: 1160px;
  margin-inline: auto;
  padding: clamp(20px,4cqi,44px) clamp(16px,4cqi,44px);
}

.car-06__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.car-06__gallery {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.car-06__view {
  position: relative;
  aspect-ratio: 4/5;
  width: 100%;
  border-radius: 16px;
  overflow: hidden;
  background: linear-gradient(150deg,oklch(0.88 0.02 80),oklch(0.78 0.03 60));
}

.car-06__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0;
  scale: 1.035;
  transition: opacity .45s ease,scale .6s cubic-bezier(.2,.7,.2,1);
}

.car-06__ratio-tag {
  position: absolute;
  left: 12px;
  bottom: 12px;
  z-index: 2;
  font-size: 11px;
  font-weight: 600;
  color: oklch(0.98 0 0);
  background: oklch(0.2 0.02 60/.6);
  padding: 6px 10px;
  border-radius: 99px;
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
}

.car-06__ratio-tag code {
  font-family: ui-monospace,Menlo,monospace;
}

.car-06__thumbs {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 10px;
}

.car-06__thumbs label {
  aspect-ratio: 1;
  border-radius: 10px;
  overflow: hidden;
  border: 2px solid var(--line);
  cursor: pointer;
  transition: border-color .2s,translate .2s;
}

.car-06__thumbs label:hover {
  translate: 0 -2px;
}

.car-06__thumbs img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

#car06-v1:checked ~ .car-06__view .car-06__img--1,
#car06-v2:checked ~ .car-06__view .car-06__img--2,
#car06-v3:checked ~ .car-06__view .car-06__img--3,
#car06-v4:checked ~ .car-06__view .car-06__img--4 {
  opacity: 1;
  scale: 1;
}

#car06-v1:checked ~ .car-06__thumbs label[for="car06-v1"],
#car06-v2:checked ~ .car-06__thumbs label[for="car06-v2"],
#car06-v3:checked ~ .car-06__thumbs label[for="car06-v3"],
#car06-v4:checked ~ .car-06__thumbs label[for="car06-v4"] {
  border-color: var(--acc);
}

#car06-v1:focus-visible ~ .car-06__thumbs label[for="car06-v1"],
#car06-v2:focus-visible ~ .car-06__thumbs label[for="car06-v2"],
#car06-v3:focus-visible ~ .car-06__thumbs label[for="car06-v3"],
#car06-v4:focus-visible ~ .car-06__thumbs label[for="car06-v4"] {
  outline: 3px solid var(--acc);
  outline-offset: 2px;
}

.car-06__kicker {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
}

.car-06__info h1 {
  font-size: clamp(24px,3.4cqi,34px);
  letter-spacing: -.02em;
  font-weight: 800;
  margin-top: 8px;
}

.car-06__price {
  margin-top: 10px;
  font-size: 19px;
  font-weight: 800;
}

.car-06__price s {
  font-size: 14px;
  font-weight: 400;
  color: var(--mut);
  margin-left: 8px;
}

.car-06__price em {
  font-style: normal;
  font-size: 12px;
  font-weight: 700;
  color: oklch(0.5 0.15 25);
  margin-left: 6px;
}

.car-06__blurb {
  margin-top: 12px;
  font-size: 14px;
  line-height: 1.6;
  color: var(--mut);
}

.car-06__blurb code,
.car-06__foot code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .88em;
  background: oklch(0.92 0.01 80);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
}

.car-06__opts {
  border: 0;
  margin-top: 18px;
}

.car-06__opts legend {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 9px;
}

.car-06__swatch {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  margin-right: 12px;
  cursor: pointer;
  font-size: 13px;
  min-height: 44px;
}

.car-06__swatch input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.car-06__swatch i {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: var(--c);
  border: 2px solid var(--bg);
  outline: 1.5px solid var(--line);
  transition: outline-color .2s,scale .2s;
}

.car-06__swatch input:checked + i {
  outline: 2.5px solid var(--acc);
  scale: 1.08;
}

.car-06__swatch input:focus-visible + i {
  outline: 3px solid var(--acc);
  outline-offset: 2px;
}

.car-06__size {
  display: inline-grid;
  margin: 0 8px 8px 0;
  cursor: pointer;
}

.car-06__size input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.car-06__size span {
  display: grid;
  place-items: center;
  min-width: 52px;
  min-height: 44px;
  border-radius: 10px;
  border: 1.5px solid var(--line);
  font-size: 13.5px;
  font-weight: 600;
  transition: border-color .2s,background .2s,color .2s;
}

.car-06__size input:checked + span {
  border-color: var(--ink);
  background: var(--ink);
  color: var(--bg);
}

.car-06__size input:focus-visible + span {
  outline: 3px solid var(--acc);
  outline-offset: 2px;
}

.car-06__size span:hover {
  border-color: var(--acc);
}

.car-06__cta {
  display: grid;
  place-items: center;
  min-height: 52px;
  margin-top: 20px;
  border-radius: 13px;
  background: var(--acc);
  color: oklch(0.99 0 0);
  font-size: 15px;
  font-weight: 700;
  text-decoration: none;
  transition: background .2s,translate .2s;
}

.car-06__cta:hover,
.car-06__cta:focus-visible {
  background: color-mix(in oklch,var(--acc) 85%,black);
  translate: 0 -2px;
}

.car-06__cta:focus-visible {
  outline: 3px solid var(--acc);
  outline-offset: 3px;
}

.car-06__ship {
  margin-top: 10px;
  font-size: 12px;
  color: var(--mut);
  text-align: center;
}

.car-06__more {
  margin-top: 14px;
  border-top: 1px solid var(--line);
  padding-top: 14px;
}

.car-06__more summary {
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  list-style: none;
  display: flex;
  justify-content: space-between;
  align-items: center;
  min-height: 44px;
}

.car-06__more summary::after {
  content: "+";
  font-size: 18px;
  color: var(--mut);
  transition: rotate .25s;
}

.car-06__more[open] summary::after {
  rotate: 45deg;
}

.car-06__more summary:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
  border-radius: 4px;
}

.car-06__more p {
  font-size: 13.5px;
  line-height: 1.6;
  color: var(--mut);
  padding: 2px 0 10px;
}

.car-06__foot {
  max-width: 1160px;
  margin-inline: auto;
  padding: 18px clamp(16px,4cqi,44px) 34px;
  border-top: 1px solid var(--line);
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
}

@container car06 (width < 720px) {
  .car-06__main {
    grid-template-columns: 1fr;
  }

  .car-06__crumb {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-06 * {
    transition-duration: .01ms !important;
  }
}
```
