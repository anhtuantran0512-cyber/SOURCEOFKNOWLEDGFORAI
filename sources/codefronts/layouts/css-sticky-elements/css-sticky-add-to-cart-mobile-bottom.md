---
source: "codefronts"
url: "https://codefronts.com/layouts/css-sticky-elements/css-sticky-add-to-cart-mobile-bottom/"
title: "CSS Sticky Add to Cart Mobile Bottom"
section: "layouts"
category: "css-sticky-elements"
category_name: "CSS Sticky Elements"
description: "The highest-converting pixels in mobile commerce: a bottom-pinned bar with the price and the buy button, always one thumb-tap away."
has_js: "false"
---

Here's a working CSS Sticky Element from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sticky Add to Cart Mobile Bottom
Source: https://codefronts.com/layouts/css-sticky-elements/css-sticky-add-to-cart-mobile-bottom/

The highest-converting pixels in mobile commerce: a bottom-pinned bar with the price and the buy button, always one thumb-tap away. The trick is that position: sticky; bottom: 0 works in reverse — place the bar near the END of the page and it rides pinned at the viewport bottom from the first paint, then settles into normal flow when you reach it. Add :has() and the CTA stays disabled until a size is picked — state management with zero JavaScript.
## HTML
```html
<section class="cst-11" aria-label="Sticky add to cart bottom bar demo">
  <div class="cst-11__stage" id="cst11-top">
    <header class="cst-11__mast">
      <a class="cst-11__brand" href="#cst11-top">COURTSIDE</a>
      <nav aria-label="Store"><a href="#cst11-new">New</a><a href="#cst11-men">Men</a><a href="#cst11-women">Women</a></nav>
      <a class="cst-11__bag" href="#cst11-bag">Bag (0)</a>
    </header>
    <form class="cst-11__main" onsubmit="return false">
      <div class="cst-11__gallery">
        <figure class="cst-11__heroimg" style="--img:url('https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=1400&auto=format&fit=crop')"><span>Reissue · 1988</span></figure>
        <div class="cst-11__thumbs" role="img" aria-label="Three alternate product views">
          <i style="--img:url('https://images.unsplash.com/photo-1549298916-b41d501d3772?q=80&w=600&auto=format&fit=crop')"></i>
          <i style="--img:url('https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?q=80&w=600&auto=format&fit=crop')"></i>
          <i style="--img:url('https://images.unsplash.com/photo-1600185365483-26d7a4cc7519?q=80&w=600&auto=format&fit=crop')"></i>
        </div>
      </div>
      <div class="cst-11__info">
        <p class="cst-11__kicker">Volley Court 88</p>
        <h1>The court shoe that never left</h1>
        <p class="cst-11__meta"><span class="cst-11__stars" aria-label="Rated 4.7 of 5">★★★★★</span> 4.7 · 862 reviews · Flame / Chalk</p>
        <p class="cst-11__price">$129 <em>free returns</em></p>
        <fieldset class="cst-11__sizes">
          <legend>Select size (US)</legend>
          <input type="radio" name="cst11size" id="cst11-s7"><label for="cst11-s7">7</label>
          <input type="radio" name="cst11size" id="cst11-s8"><label for="cst11-s8">8</label>
          <input type="radio" name="cst11size" id="cst11-s9"><label for="cst11-s9">9</label>
          <input type="radio" name="cst11size" id="cst11-s10"><label for="cst11-s10">10</label>
          <input type="radio" name="cst11size" id="cst11-s11"><label for="cst11-s11">11</label>
          <input type="radio" name="cst11size" id="cst11-s12"><label for="cst11-s12">12</label>
        </fieldset>
        <p class="cst-11__hint">Pick a size — the bar below unlocks itself with <code>:has(input:checked)</code>. No JavaScript on this page.</p>
        <details open><summary>Details</summary><p>Full-grain leather upper on the original 1988 last. Cupsole re-tooled for 40% more heel cushion; everything else left exactly alone.</p></details>
        <details><summary>Shipping &amp; returns</summary><p>Free over $75, carbon-neutral. 60-day returns in any condition — yes, worn outside.</p></details>
        <details><summary>Materials</summary><p>Leather (LWG Gold tanneries), 71% recycled rubber outsole, undyed cotton laces.</p></details>
        <section class="cst-11__revs" aria-label="Recent reviews">
          <article><p>“Bought the '88 originals in the '88. These are better and I'm furious about it.”</p><footer>Ray C. · Chicago</footer></article>
          <article><p>“Sized true. The sticky bar followed me all the way down this page and I respect the hustle.”</p><footer>Tess M. · Brisbane</footer></article>
        </section>
      </div>
      <div class="cst-11__bar">
        <i class="cst-11__barthumb" style="--img:url('https://images.unsplash.com/photo-1542291026-7eec264c27ff?q=80&w=300&auto=format&fit=crop')" aria-hidden="true"></i>
        <div class="cst-11__barinfo">
          <strong>Volley Court 88</strong>
          <span class="cst-11__picked">Size: </span>
        </div>
        <span class="cst-11__barprice">$129</span>
        <button class="cst-11__go" type="submit">
          <span class="cst-11__go-wait">Pick a size</span>
          <span class="cst-11__go-ready">Add to cart</span>
        </button>
      </div>
    </form>
    <footer class="cst-11__footer"><p><strong>Courtside</strong> — a demo from the CodeFronts sticky-elements collection. The bar above just docked into flow: that's its natural DOM position.</p><a href="#cst11-top">Back to top ↑</a></footer>
  </div>
</section>
```
## CSS
```css
.cst-11,
.cst-11 *,
.cst-11 *::before,
.cst-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cst-11 {
  --bg: oklch(0.98 0.004 60);
  --ink: oklch(0.22 0.015 45);
  --mut: oklch(0.51 0.015 45);
  --line: oklch(0.9 0.01 60);
  --acc: oklch(0.6 0.19 30);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.cst-11__stage {
  width: 100%;
  container: cst11/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.cst-11__mast {
  position: sticky;
  top: 0;
  z-index: 8;
  display: flex;
  align-items: center;
  gap: 20px;
  height: 54px;
  padding: 0 clamp(16px,4cqi,40px);
  background: color-mix(in oklch,var(--bg) 84%,transparent);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--line);
}

.cst-11__brand {
  font-size: 15px;
  font-weight: 800;
  letter-spacing: .14em;
  color: inherit;
  text-decoration: none;
}

.cst-11__brand:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-11__mast nav {
  display: flex;
  gap: 2px;
  margin-inline: auto;
}

.cst-11__mast nav a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 13px;
  font-weight: 600;
  color: var(--mut);
  text-decoration: none;
  transition: color .2s,background .2s;
}

.cst-11__mast nav a:hover,
.cst-11__mast nav a:focus-visible {
  color: var(--ink);
  background: oklch(0.93 0.012 60);
}

.cst-11__mast nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.cst-11__bag {
  display: grid;
  place-items: center;
  min-height: 38px;
  padding: 0 14px;
  border-radius: 99px;
  border: 1.5px solid var(--line);
  font-size: 12.5px;
  font-weight: 700;
  color: inherit;
  text-decoration: none;
  transition: border-color .2s;
}

.cst-11__bag:hover,
.cst-11__bag:focus-visible {
  border-color: var(--acc);
}

.cst-11__bag:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-11__main {
  display: grid;
  grid-template-columns: minmax(0,6fr) minmax(0,5fr);
  gap: clamp(20px,4cqi,48px);
  padding: clamp(16px,3.5cqi,36px) clamp(16px,4cqi,40px) 0;
  align-items: start;
}

.cst-11__gallery {
  position: sticky;
  top: 70px;
  align-self: start;
  display: grid;
  gap: 10px;
}

.cst-11__heroimg {
  aspect-ratio: 4/3.6;
  border-radius: 20px;
  background-image: var(--img,none),linear-gradient(150deg,oklch(0.75 0.1 35),oklch(0.5 0.14 25));
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: flex-end;
  padding: 14px;
}

.cst-11__heroimg span {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: oklch(0.99 0 0);
  background: oklch(0.2 0.02 45/.6);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  padding: 6px 10px;
  border-radius: 99px;
}

.cst-11__thumbs {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 10px;
}

.cst-11__thumbs i {
  aspect-ratio: 4/3;
  border-radius: 12px;
  background-image: var(--img,none),linear-gradient(150deg,oklch(0.85 0.04 60),oklch(0.68 0.08 45));
  background-size: cover;
  background-position: center;
}

.cst-11__kicker {
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
  margin-bottom: 8px;
}

.cst-11__info h1 {
  font-size: clamp(26px,4.4cqi,42px);
  line-height: 1.04;
  letter-spacing: -.03em;
  font-weight: 800;
  text-wrap: balance;
}

.cst-11__meta {
  margin-top: 10px;
  font-size: 13px;
  color: var(--mut);
}

.cst-11__stars {
  color: oklch(0.72 0.15 70);
  letter-spacing: 2px;
}

.cst-11__price {
  margin-top: 12px;
  font-size: 26px;
  font-weight: 800;
  letter-spacing: -.02em;
}

.cst-11__price em {
  font-style: normal;
  font-size: 12.5px;
  font-weight: 600;
  color: var(--mut);
  margin-left: 10px;
}

.cst-11__sizes {
  border: none;
  margin-top: 18px;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.cst-11__sizes legend {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 10px;
}

.cst-11__sizes input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
}

.cst-11__sizes label {
  display: grid;
  place-items: center;
  min-width: 52px;
  min-height: 46px;
  border-radius: 11px;
  border: 1.5px solid var(--line);
  background: oklch(1 0 0);
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  transition: border-color .15s,background .15s,color .15s,translate .15s;
}

.cst-11__sizes label:hover {
  border-color: oklch(0.7 0.06 40);
  translate: 0 -1px;
}

.cst-11__sizes input:focus-visible+label {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cst-11__sizes input:checked+label {
  border-color: var(--ink);
  background: var(--ink);
  color: oklch(0.98 0 0);
}

.cst-11__hint {
  margin-top: 14px;
  font-size: 12.5px;
  line-height: 1.55;
  color: var(--mut);
}

.cst-11__hint code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  background: oklch(0.92 0.012 60);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

.cst-11__info details {
  border-bottom: 1px solid var(--line);
}

.cst-11__info details:first-of-type {
  margin-top: 18px;
  border-top: 1px solid var(--line);
}

.cst-11__info summary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 50px;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  list-style: none;
}

.cst-11__info summary::-webkit-details-marker {
  display: none;
}

.cst-11__info summary::after {
  content: "+";
  font-size: 19px;
  font-weight: 400;
  color: var(--mut);
  transition: rotate .25s;
}

.cst-11__info details[open] summary::after {
  rotate: 45deg;
}

.cst-11__info summary:hover {
  color: var(--acc);
}

.cst-11__info summary:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
  border-radius: 6px;
}

.cst-11__info details p {
  padding-bottom: 16px;
  font-size: 13.5px;
  line-height: 1.65;
  color: var(--mut);
  max-width: 56ch;
}

.cst-11__revs {
  display: grid;
  gap: 10px;
  margin: 20px 0 26px;
}

.cst-11__revs article {
  padding: 16px 18px;
  border-radius: 14px;
  background: oklch(1 0 0);
  border: 1px solid var(--line);
}

.cst-11__revs p {
  font-size: 13.5px;
  line-height: 1.6;
}

.cst-11__revs footer {
  margin-top: 8px;
  font-size: 11.5px;
  color: var(--mut);
}

.cst-11__bar {
  grid-column: 1/-1;
  position: sticky;
  bottom: 0;
  z-index: 9;
  display: flex;
  align-items: center;
  gap: 14px;
  margin: 0 calc(-1 * clamp(16px,4cqi,40px));
  padding: 10px clamp(16px,4cqi,40px) max(10px,env(safe-area-inset-bottom));
  background: color-mix(in oklch,oklch(1 0 0) 88%,transparent);
  -webkit-backdrop-filter: blur(14px);
  backdrop-filter: blur(14px);
  border-top: 1px solid var(--line);
  box-shadow: 0 -12px 34px oklch(0.3 0.03 45/.1);
}

.cst-11__barthumb {
  flex: none;
  width: 46px;
  height: 46px;
  border-radius: 10px;
  background-image: var(--img,none),linear-gradient(150deg,oklch(0.75 0.1 35),oklch(0.5 0.14 25));
  background-size: cover;
  background-position: center;
}

.cst-11__barinfo {
  display: grid;
  gap: 1px;
  min-width: 0;
}

.cst-11__barinfo strong {
  font-size: 13.5px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.cst-11__picked {
  font-size: 11.5px;
  color: var(--mut);
}

.cst-11__picked::after {
  content: "none yet";
  font-weight: 700;
}

.cst-11__stage:has(#cst11-s7:checked) .cst-11__picked::after {
  content: "US 7";
}

.cst-11__stage:has(#cst11-s8:checked) .cst-11__picked::after {
  content: "US 8";
}

.cst-11__stage:has(#cst11-s9:checked) .cst-11__picked::after {
  content: "US 9";
}

.cst-11__stage:has(#cst11-s10:checked) .cst-11__picked::after {
  content: "US 10";
}

.cst-11__stage:has(#cst11-s11:checked) .cst-11__picked::after {
  content: "US 11";
}

.cst-11__stage:has(#cst11-s12:checked) .cst-11__picked::after {
  content: "US 12";
}

.cst-11__barprice {
  margin-left: auto;
  font-size: 17px;
  font-weight: 800;
  letter-spacing: -.01em;
}

.cst-11__go {
  position: relative;
  flex: none;
  min-height: 48px;
  padding: 0 clamp(16px,3cqi,30px);
  border: none;
  border-radius: 13px;
  font: inherit;
  font-size: 14px;
  font-weight: 800;
  color: oklch(0.99 0 0);
  background: var(--mut);
  cursor: not-allowed;
  pointer-events: none;
  transition: background .25s,translate .2s;
}

.cst-11__go-ready {
  display: none;
}

.cst-11__stage:has(.cst-11__sizes input:checked) .cst-11__go {
  background: var(--acc);
  cursor: pointer;
  pointer-events: auto;
}

.cst-11__stage:has(.cst-11__sizes input:checked) .cst-11__go-wait {
  display: none;
}

.cst-11__stage:has(.cst-11__sizes input:checked) .cst-11__go-ready {
  display: inline;
}

.cst-11__go:hover,
.cst-11__go:focus-visible {
  translate: 0 -1px;
  background: color-mix(in oklch,var(--acc) 85%,black);
}

.cst-11__go:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cst-11__footer {
  display: flex;
  flex-wrap: wrap;
  gap: 14px 26px;
  align-items: center;
  justify-content: space-between;
  padding: 26px clamp(16px,4cqi,40px) 38px;
  border-top: 1px solid var(--line);
  margin-top: 18px;
}

.cst-11__footer p {
  font-size: 12.5px;
  line-height: 1.55;
  color: var(--mut);
  max-width: 60ch;
}

.cst-11__footer a {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 14px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 700;
  color: var(--ink);
  text-decoration: none;
  border: 1.5px solid var(--line);
  transition: border-color .2s;
}

.cst-11__footer a:hover,
.cst-11__footer a:focus-visible {
  border-color: var(--acc);
}

.cst-11__footer a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

@container cst11 (width < 700px) {
  .cst-11__main {
    grid-template-columns: 1fr;
  }

  .cst-11__gallery {
    position: static;
  }

  .cst-11__mast nav {
    display: none;
  }

  .cst-11__barinfo {
    display: none;
  }

  .cst-11__barthumb {
    width: 40px;
    height: 40px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cst-11 * {
    transition-duration: .01ms !important;
  }
}
```
