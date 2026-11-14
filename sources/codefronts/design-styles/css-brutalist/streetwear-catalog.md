---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/streetwear-catalog/"
title: "Brutalist Streetwear Catalog"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "A drop catalogue with lookbook energy and no polish: condensed uppercase type, black-framed product shots, prices in plain bold, and sizes as bordered square…"
has_js: "false"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Brutalist Streetwear Catalog
Source: https://codefronts.com/design-styles/css-brutalist/streetwear-catalog/

A drop catalogue with lookbook energy and no polish: condensed uppercase type, black-framed product shots, prices in plain bold, and sizes as bordered square chips that are real radio inputs — so selection works with no JavaScript and reads correctly to a screen reader. Sold-out sizes are disabled and hatched, not merely greyed.
## HTML
```html
<div class="brt-22">
  <input class="brt-22__sr" type="checkbox" id="brt-22-dark">
  <label class="brt-22__theme" for="brt-22-dark">
    <svg class="brt-22__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-22__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    <span class="brt-22__vh">Dark theme</span>
  </label>

  <div class="brt-22__stage">
    <section class="brt-22__wrap" aria-labelledby="brt-22-h">
      <header class="brt-22__head">
        <h1 class="brt-22__h" id="brt-22-h">DROP 07<span>／ WORKWEAR INDEX</span></h1>
        <p class="brt-22__meta">SHIPS 22 AUG · 340 UNITS TOTAL · NO RESTOCK · LEEDS, UK</p>
      </header>

      <ul class="brt-22__grid">
        <li class="brt-22__card">
          <figure class="brt-22__frame"><img class="brt-22__shot" src="https://images.unsplash.com/photo-1523381210434-271e8be1f52b?w=560&amp;h=700&amp;fit=crop&amp;auto=format" width="560" height="700" alt="Heavyweight cotton overshirt hanging against a plain wall" loading="lazy" decoding="async"></figure>
          <h2 class="brt-22__t">Shop Coat / 14oz Duck</h2>
          <p class="brt-22__spec">UNLINED · TRIPLE-STITCH · UNWASHED INDIGO</p>
          <fieldset class="brt-22__sizes">
            <legend class="brt-22__vh">Choose a size for Shop Coat</legend>
            <label class="brt-22__size"><input type="radio" name="brt-22-a"><span>S</span></label>
            <label class="brt-22__size"><input type="radio" name="brt-22-a" checked><span>M</span></label>
            <label class="brt-22__size"><input type="radio" name="brt-22-a"><span>L</span></label>
            <label class="brt-22__size"><input type="radio" name="brt-22-a" disabled><span>XL</span></label>
          </fieldset>
          <p class="brt-22__price">£184 <span class="brt-22__stock">XL SOLD OUT</span></p>
        </li>

        <li class="brt-22__card">
          <figure class="brt-22__frame"><img class="brt-22__shot" src="https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=560&amp;h=700&amp;fit=crop&amp;auto=format" width="560" height="700" alt="Plain heavyweight t-shirt folded on a concrete surface" loading="lazy" decoding="async"></figure>
          <h2 class="brt-22__t">Blank Tee / 280gsm</h2>
          <p class="brt-22__spec">BOXY · TUBULAR KNIT · RAW WHITE</p>
          <fieldset class="brt-22__sizes">
            <legend class="brt-22__vh">Choose a size for Blank Tee</legend>
            <label class="brt-22__size"><input type="radio" name="brt-22-b"><span>S</span></label>
            <label class="brt-22__size"><input type="radio" name="brt-22-b"><span>M</span></label>
            <label class="brt-22__size"><input type="radio" name="brt-22-b" checked><span>L</span></label>
            <label class="brt-22__size"><input type="radio" name="brt-22-b"><span>XL</span></label>
          </fieldset>
          <p class="brt-22__price">£46</p>
        </li>

        <li class="brt-22__card">
          <figure class="brt-22__frame"><img class="brt-22__shot" src="https://images.unsplash.com/photo-1542272604-787c3835535d?w=560&amp;h=700&amp;fit=crop&amp;auto=format" width="560" height="700" alt="Rigid denim trousers laid flat with visible selvedge" loading="lazy" decoding="async"></figure>
          <h2 class="brt-22__t">Yard Trouser / Rigid</h2>
          <p class="brt-22__spec">STRAIGHT · 13.5oz · SELVEDGE ID</p>
          <fieldset class="brt-22__sizes">
            <legend class="brt-22__vh">Choose a waist size for Yard Trouser</legend>
            <label class="brt-22__size"><input type="radio" name="brt-22-c" checked><span>30</span></label>
            <label class="brt-22__size"><input type="radio" name="brt-22-c"><span>32</span></label>
            <label class="brt-22__size"><input type="radio" name="brt-22-c"><span>34</span></label>
            <label class="brt-22__size"><input type="radio" name="brt-22-c" disabled><span>36</span></label>
          </fieldset>
          <p class="brt-22__price">£132 <span class="brt-22__stock">36 SOLD OUT</span></p>
        </li>

        <li class="brt-22__look">
          <figure class="brt-22__lookfig"><img class="brt-22__lookimg" src="https://images.unsplash.com/photo-1483985988355-763728e1935b?w=760&amp;h=560&amp;fit=crop&amp;auto=format" width="760" height="560" alt="Two models in workwear standing against a corrugated wall" loading="lazy" decoding="async"></figure>
          <div class="brt-22__lookcopy">
            <h2 class="brt-22__lookh">LOOKBOOK 07</h2>
            <p>Photographed on the yard at Hunslet, 06:40, before the trucks. Every garment shown is in this drop. Nothing is styled with anything we do not sell.</p>
            <p class="brt-22__lookmeta">18 FRAMES · SHOT ON 400 ISO · PRINT EDITION OF 200</p>
            <a class="brt-22__cta" href="#brt-22-h">VIEW ALL FRAMES</a>
          </div>
        </li>

        <li class="brt-22__card">
          <figure class="brt-22__frame"><img class="brt-22__shot" src="https://images.unsplash.com/photo-1556306535-0f09a537f0a3?w=560&amp;h=700&amp;fit=crop&amp;auto=format" width="560" height="700" alt="Canvas work cap resting on a wooden bench" loading="lazy" decoding="async"></figure>
          <h2 class="brt-22__t">Yard Cap / 6 Panel</h2>
          <p class="brt-22__spec">UNSTRUCTURED · BRASS BUCKLE</p>
          <fieldset class="brt-22__sizes">
            <legend class="brt-22__vh">Choose a size for Yard Cap</legend>
            <label class="brt-22__size"><input type="radio" name="brt-22-d" checked><span>ONE</span></label>
          </fieldset>
          <p class="brt-22__price">£38</p>
        </li>

        <li class="brt-22__card">
          <figure class="brt-22__frame"><img class="brt-22__shot" src="https://images.unsplash.com/photo-1549298916-b41d501d3772?w=560&amp;h=700&amp;fit=crop&amp;auto=format" width="560" height="700" alt="Pair of work boots on a concrete floor" loading="lazy" decoding="async"></figure>
          <h2 class="brt-22__t">Depot Boot / Resoleable</h2>
          <p class="brt-22__spec">GOODYEAR WELT · OILED SUEDE</p>
          <fieldset class="brt-22__sizes">
            <legend class="brt-22__vh">Choose a size for Depot Boot</legend>
            <label class="brt-22__size"><input type="radio" name="brt-22-e"><span>8</span></label>
            <label class="brt-22__size"><input type="radio" name="brt-22-e" checked><span>9</span></label>
            <label class="brt-22__size"><input type="radio" name="brt-22-e"><span>10</span></label>
            <label class="brt-22__size"><input type="radio" name="brt-22-e"><span>11</span></label>
          </fieldset>
          <p class="brt-22__price">£265</p>
        </li>
      </ul>

      <p class="brt-22__foot">SIZE GUIDE IN CENTIMETRES ON EVERY PRODUCT PAGE · RETURNS 30 DAYS, UNWORN · [email protected]</p>
    </section>
  </div>
</div>
```
## CSS
```css
.brt-22 {
  --page: #eeece7;
  --panel: #ffffff;
  --ink: #000000;
  --muted: #3a3a3a;
  --edge: #000000;
  --bw: 3px;
  --gap: 2px;
  --mono: ui-monospace,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace;
  --cond: 'Arial Narrow','Helvetica Neue Condensed',system-ui,-apple-system,Arial,sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui,-apple-system,'Segoe UI',Arial,sans-serif;
  font-size: 16px;
}

.brt-22 *,
.brt-22 *::before,
.brt-22 *::after {
  box-sizing: border-box;
  border-radius: 0;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-22 {
    --page: oklch(0.938 0.005 90);
    --panel: oklch(1 0 0);
    --ink: oklch(0 0 0);
    --muted: oklch(0.34 0 0);
  }
}

.brt-22__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.brt-22__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.brt-22__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  box-shadow: 4px 4px 0 var(--edge);
  cursor: pointer;
}

.brt-22__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-22__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-22__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--edge);
}

.brt-22__sr:focus-visible + .brt-22__theme {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-22__sun {
  display: none;
}

.brt-22__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: start center;
  padding: clamp(.75rem,2.6vw,2rem);
}

.brt-22__wrap {
  inline-size: min(78rem,100%);
}

.brt-22__head {
  padding-inline-end: 3.5rem;
  padding-block-end: .6rem;
  border-block-end: 5px solid var(--edge);
}

.brt-22__h {
  margin: 0;
  font-family: var(--cond);
  font-stretch: condensed;
  font-size: clamp(2.4rem,9vw,5.5rem);
  font-weight: 700;
  letter-spacing: -.02em;
  line-height: .9;
  text-transform: uppercase;
}

.brt-22__h span {
  display: block;
  font-size: .34em;
  letter-spacing: .04em;
}

.brt-22__meta {
  margin: .5rem 0 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .14em;
  color: var(--muted);
}

.brt-22__grid {
  list-style: none;
  margin: 1.5rem 0 0;
  padding: 0;
  display: grid;
  gap: var(--gap);
  grid-template-columns: repeat(auto-fill,minmax(min(14rem,100%),1fr));
}

.brt-22__card {
  display: flex;
  flex-direction: column;
  padding: .6rem .6rem 1rem;
  background: var(--panel);
  border: var(--bw) solid var(--edge);
}

.brt-22__card:has(:checked) .brt-22__t {
  text-decoration: 3px underline var(--edge);
  text-underline-offset: 3px;
}

.brt-22__frame {
  margin: 0 0 .7rem;
  border: var(--bw) solid var(--edge);
  background: var(--page);
}

.brt-22__shot {
  display: block;
  inline-size: 100%;
  aspect-ratio: 4/5;
  object-fit: cover;
  filter: grayscale(1) contrast(1.08);
}

.brt-22__card:hover .brt-22__shot {
  filter: none;
}

.brt-22__t {
  margin: 0;
  font-family: var(--cond);
  font-stretch: condensed;
  font-size: 1.35rem;
  font-weight: 700;
  line-height: 1.05;
  letter-spacing: -.01em;
  text-transform: uppercase;
}

.brt-22__spec {
  margin: .35rem 0 .75rem;
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .1em;
  line-height: 1.5;
  color: var(--muted);
}

.brt-22__sizes {
  display: flex;
  flex-wrap: wrap;
  gap: 0;
  margin: 0 0 .9rem;
  padding: 0;
  border: 0;
}

.brt-22__size {
  position: relative;
}

.brt-22__size input {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  margin: 0;
}

.brt-22__size span {
  display: grid;
  place-items: center;
  min-inline-size: 2.75rem;
  min-block-size: 2.75rem;
  padding: .35rem .5rem;
  font-family: var(--mono);
  font-size: .76rem;
  letter-spacing: .08em;
  cursor: pointer;
  border: var(--bw) solid var(--edge);
  margin-inline-end: -3px;
  background: var(--panel);
}

.brt-22__size input:checked + span {
  background: var(--ink);
  color: var(--panel);
  position: relative;
  z-index: 1;
}

.brt-22__size input:focus-visible + span {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
  position: relative;
  z-index: 2;
}

.brt-22__size input:disabled + span {
  cursor: not-allowed;
  color: var(--muted);
  background: repeating-linear-gradient(45deg, transparent 0 5px, var(--ink) 5px 7px);
}

.brt-22__price {
  margin: auto 0 0;
  display: flex;
  flex-wrap: wrap;
  gap: .4rem .6rem;
  align-items: baseline;
  font-size: 1.25rem;
  font-weight: 700;
  letter-spacing: -.01em;
}

.brt-22__stock {
  padding: .15rem .35rem;
  border: 2px solid var(--edge);
  font-family: var(--mono);
  font-size: .6rem;
  letter-spacing: .12em;
  font-weight: 400;
}

.brt-22__look {
  grid-column: 1 / -1;
  display: grid;
  gap: var(--gap);
  grid-template-columns: minmax(0,1fr);
  background: var(--ink);
  border: var(--bw) solid var(--edge);
}

@media (min-width: 52rem) {
  .brt-22__look {
    grid-template-columns: minmax(0,1.4fr) minmax(0,1fr);
  }
}

.brt-22__lookfig {
  margin: 0;
}

.brt-22__lookimg {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  aspect-ratio: 19/14;
  object-fit: cover;
  filter: grayscale(1) contrast(1.1);
}

.brt-22__lookcopy {
  padding: 1.1rem 1.15rem 1.25rem;
  color: var(--panel);
  display: flex;
  flex-direction: column;
  gap: .7rem;
}

.brt-22__lookh {
  margin: 0;
  font-family: var(--cond);
  font-stretch: condensed;
  font-size: clamp(1.8rem,5vw,2.8rem);
  font-weight: 700;
  line-height: .95;
  letter-spacing: -.02em;
}

.brt-22__lookcopy p {
  margin: 0;
  font-size: .95rem;
  line-height: 1.5;
}

.brt-22__lookmeta {
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .12em;
  opacity: .75;
}

.brt-22__cta {
  align-self: flex-start;
  margin-block-start: auto;
  display: inline-flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: .6rem 1rem;
  background: var(--panel);
  color: var(--ink);
  text-decoration: none;
  font-family: var(--mono);
  font-size: .76rem;
  font-weight: 700;
  letter-spacing: .14em;
  border: var(--bw) solid var(--panel);
  box-shadow: 4px 4px 0 var(--panel);
}

.brt-22__cta:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--panel);
}

.brt-22__cta:focus-visible {
  outline: 3px solid var(--panel);
  outline-offset: 3px;
}

.brt-22__foot {
  margin: 1.25rem 0 0;
  padding-block-start: .6rem;
  border-block-start: var(--bw) solid var(--edge);
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .12em;
  line-height: 1.6;
  color: var(--muted);
}

.brt-22:has(#brt-22-dark:checked) {
  --page: #000000;
  --panel: #0b0b0b;
  --ink: #ffffff;
  --muted: #bdbdbd;
  --edge: #ffffff;
}

.brt-22:has(#brt-22-dark:checked) .brt-22__moon {
  display: none;
}

.brt-22:has(#brt-22-dark:checked) .brt-22__sun {
  display: block;
}

.brt-22:has(#brt-22-dark:checked) .brt-22__look {
  background: var(--panel);
}

.brt-22:has(#brt-22-dark:checked) .brt-22__lookcopy {
  color: var(--ink);
}

@media (prefers-color-scheme: dark) {
  .brt-22:not(:has(#brt-22-dark:checked)) {
    --page: #000000;
    --panel: #0b0b0b;
    --ink: #ffffff;
    --muted: #bdbdbd;
    --edge: #ffffff;
  }

  .brt-22:not(:has(#brt-22-dark:checked)) .brt-22__moon {
    display: none;
  }

  .brt-22:not(:has(#brt-22-dark:checked)) .brt-22__sun {
    display: block;
  }

  .brt-22:not(:has(#brt-22-dark:checked)) .brt-22__look {
    background: var(--panel);
  }

  .brt-22:not(:has(#brt-22-dark:checked)) .brt-22__lookcopy {
    color: var(--ink);
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-22 *,
    .brt-22 *::before,
    .brt-22 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .brt-22__card,
    .brt-22__frame,
    .brt-22__size span,
    .brt-22__theme {
    border-color: CanvasText;
    box-shadow: none;
  }

  .brt-22__size input:checked + span {
    background: Highlight;
    color: HighlightText;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-22__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```
