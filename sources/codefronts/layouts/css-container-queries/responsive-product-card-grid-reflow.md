---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/responsive-product-card-grid-reflow/"
title: "Responsive Product Card Grid Reflow"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "Commerce cards where each cell is its own container, so a card in a two-up row and a card in a four-up row style themselves differently without the grid…"
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Product Card Grid Reflow
Source: https://codefronts.com/layouts/css-container-queries/responsive-product-card-grid-reflow/

Commerce cards where each cell is its own container, so a card in a two-up row and a card in a four-up row style themselves differently without the grid telling them to. The detail worth naming: the container must be the grid item, not the grid &mdash; querying the grid gives every card the same answer, which is exactly the bug this pattern is supposed to remove.
## HTML
```html
<section class="cq-11" aria-labelledby="cq-11-h">
  <fieldset class="cq-11__theme">
    <legend class="cq-11__themelegend">Theme</legend>
    <input class="cq-11__themeinput" type="radio" name="cq-11-theme" id="cq-11-theme-auto" checked>
    <label class="cq-11__themeopt" for="cq-11-theme-auto">Auto</label>
    <input class="cq-11__themeinput" type="radio" name="cq-11-theme" id="cq-11-theme-light">
    <label class="cq-11__themeopt" for="cq-11-theme-light">Light</label>
    <input class="cq-11__themeinput" type="radio" name="cq-11-theme" id="cq-11-theme-dark">
    <label class="cq-11__themeopt" for="cq-11-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-11__stage">
    <header class="cq-11__head">
      <p class="cq-11__kicker">Fern Supply Co.</p>
      <h2 class="cq-11__h" id="cq-11-h">Same card, different cells</h2>
    </header>

    <section class="cq-11__block" aria-label="Two column row">
      <p class="cq-11__rowlabel">Two up &middot; wide cells</p>
      <ul class="cq-11__row cq-11__row--two">
        <li class="cq-11__cell">
          <article class="cq-11__card">
            <div class="cq-11__shot cq-11__shot--a" role="img" aria-label="Enamel kettle in sage"></div>
            <div class="cq-11__info">
              <h3 class="cq-11__name">Enamel stovetop kettle</h3>
              <p class="cq-11__sub">1.4 litre &middot; sage</p>
              <ul class="cq-11__swatch"><li style="background:#8ba888"></li><li style="background:#e8d9b5"></li><li style="background:#c96a4b"></li></ul>
              <p class="cq-11__count">3 colours</p>
            </div>
            <div class="cq-11__buy">
              <p class="cq-11__price">$64</p>
              <button class="cq-11__btn" type="button">Add to bag</button>
            </div>
          </article>
        </li>
        <li class="cq-11__cell">
          <article class="cq-11__card">
            <div class="cq-11__shot cq-11__shot--b" role="img" aria-label="Stacked linen napkins"></div>
            <div class="cq-11__info">
              <h3 class="cq-11__name">Washed linen napkins</h3>
              <p class="cq-11__sub">Set of four &middot; clay</p>
              <ul class="cq-11__swatch"><li style="background:#c96a4b"></li><li style="background:#eae2d6"></li><li style="background:#6b7f9c"></li></ul>
              <p class="cq-11__count">3 colours</p>
            </div>
            <div class="cq-11__buy">
              <p class="cq-11__price">$38</p>
              <button class="cq-11__btn" type="button">Add to bag</button>
            </div>
          </article>
        </li>
      </ul>
    </section>

    <section class="cq-11__block" aria-label="Four column row">
      <p class="cq-11__rowlabel">Four up &middot; narrow cells</p>
      <ul class="cq-11__row cq-11__row--four">
        <li class="cq-11__cell">
          <article class="cq-11__card">
            <div class="cq-11__shot cq-11__shot--a" role="img" aria-label="Enamel kettle in sage"></div>
            <div class="cq-11__info">
              <h3 class="cq-11__name">Enamel stovetop kettle</h3>
              <p class="cq-11__sub">1.4 litre &middot; sage</p>
              <ul class="cq-11__swatch"><li style="background:#8ba888"></li><li style="background:#e8d9b5"></li><li style="background:#c96a4b"></li></ul>
              <p class="cq-11__count">3 colours</p>
            </div>
            <div class="cq-11__buy">
              <p class="cq-11__price">$64</p>
              <button class="cq-11__btn" type="button">Add to bag</button>
            </div>
          </article>
        </li>
        <li class="cq-11__cell">
          <article class="cq-11__card">
            <div class="cq-11__shot cq-11__shot--b" role="img" aria-label="Stacked linen napkins"></div>
            <div class="cq-11__info">
              <h3 class="cq-11__name">Washed linen napkins</h3>
              <p class="cq-11__sub">Set of four &middot; clay</p>
              <ul class="cq-11__swatch"><li style="background:#c96a4b"></li><li style="background:#eae2d6"></li><li style="background:#6b7f9c"></li></ul>
              <p class="cq-11__count">3 colours</p>
            </div>
            <div class="cq-11__buy">
              <p class="cq-11__price">$38</p>
              <button class="cq-11__btn" type="button">Add to bag</button>
            </div>
          </article>
        </li>
        <li class="cq-11__cell">
          <article class="cq-11__card">
            <div class="cq-11__shot cq-11__shot--c" role="img" aria-label="Ribbed drinking glasses"></div>
            <div class="cq-11__info">
              <h3 class="cq-11__name">Ribbed drinking glasses</h3>
              <p class="cq-11__sub">Set of six &middot; clear</p>
              <ul class="cq-11__swatch"><li style="background:#dfe7ea"></li><li style="background:#a7c3c9"></li><li style="background:#6b7f9c"></li></ul>
              <p class="cq-11__count">3 colours</p>
            </div>
            <div class="cq-11__buy">
              <p class="cq-11__price">$46</p>
              <button class="cq-11__btn" type="button">Add to bag</button>
            </div>
          </article>
        </li>
        <li class="cq-11__cell">
          <article class="cq-11__card">
            <div class="cq-11__shot cq-11__shot--d" role="img" aria-label="Beeswax taper candles"></div>
            <div class="cq-11__info">
              <h3 class="cq-11__name">Beeswax taper candles</h3>
              <p class="cq-11__sub">Pair &middot; honey</p>
              <ul class="cq-11__swatch"><li style="background:#e8c86a"></li><li style="background:#eae2d6"></li><li style="background:#8ba888"></li></ul>
              <p class="cq-11__count">3 colours</p>
            </div>
            <div class="cq-11__buy">
              <p class="cq-11__price">$18</p>
              <button class="cq-11__btn" type="button">Add to bag</button>
            </div>
          </article>
        </li>
      </ul>
    </section>
  </div>
</section>
```
## CSS
```css
.cq-11,
.cq-11[data-theme="light"] {
  --bg: #fdf4ee;
  --surf: #ffffff;
  --line: #f0d8c8;
  --ink: #2a1410;
  --mut: #7c5a4e;
  --acc: #e4472c;
  --bloom: rgba(228, 71, 44, 0.16);
}

.cq-11[data-theme="dark"] {
  --bg: #1b100d;
  --surf: #271713;
  --line: #46271f;
  --ink: #fdeee7;
  --mut: #c69a8a;
  --acc: #ff7a5c;
  --bloom: rgba(255, 122, 92, 0.2);
}

@media (prefers-color-scheme: dark) {
  .cq-11:not([data-theme="light"]) {
    --bg: #1b100d;
    --surf: #271713;
    --line: #46271f;
    --ink: #fdeee7;
    --mut: #c69a8a;
    --acc: #ff7a5c;
    --bloom: rgba(255, 122, 92, 0.2);
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .cq-11,
    .cq-11[data-theme="light"] {
    --acc: oklch(0.6 0.21 30);
  }

  .cq-11[data-theme="dark"] {
    --acc: oklch(0.75 0.16 32);
  }

  @media (prefers-color-scheme: dark) {
    .cq-11:not([data-theme="light"]) {
      --acc: oklch(0.75 0.16 32);
    }
  }
}

.cq-11 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: "Avenir Next", Futura, "Century Gothic", "Segoe UI", system-ui, sans-serif;
  line-height: 1.5;
}

.cq-11 *,
.cq-11 *::before,
.cq-11 *::after {
  box-sizing: border-box;
}

.cq-11__stage {
  max-width: 76rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 3vw, 2.75rem);
  display: grid;
  gap: 2rem;
}

.cq-11__kicker {
  margin: 0 0 0.4rem;
  font-size: 0.72rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--acc);
  font-weight: 700;
}

.cq-11__h {
  margin: 0;
  font-size: clamp(1.5rem, 1.2rem + 2vw, 2.3rem);
  font-weight: 600;
  letter-spacing: -0.02em;
}

.cq-11__block {
  display: grid;
  gap: 0.75rem;
}

.cq-11__rowlabel {
  margin: 0;
  font-size: 0.72rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--mut);
  font-weight: 700;
}

.cq-11__row {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1rem;
}

.cq-11__row--two {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.cq-11__row--four {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

.cq-11__cell {
  container: cq-11-cell / inline-size;
  min-inline-size: 0;
}

.cq-11__card {
  display: grid;
  gap: 0.75rem;
  padding: 1rem;
  background: var(--surf);
  border-radius: 18px;
  box-shadow: 0 10px 26px var(--bloom);
}

.cq-11__shot {
  aspect-ratio: 1;
  border-radius: 12px;
}

.cq-11__shot--a {
  background: linear-gradient(150deg, #8ba888, #cfdcc4 70%, #f1f4e8);
}

.cq-11__shot--b {
  background: linear-gradient(150deg, #c96a4b, #edc7b3 70%, #f8ece4);
}

.cq-11__shot--c {
  background: repeating-linear-gradient(90deg, #dfe7ea 0 8px, #c3d4d9 8px 16px);
}

.cq-11__shot--d {
  background: linear-gradient(160deg, #e8c86a, #f4e3ae 70%, #fdf6e4);
}

.cq-11__info {
  min-inline-size: 0;
  display: grid;
  gap: 0.2rem;
}

.cq-11__name {
  margin: 0;
  font-size: 0.95rem;
  font-weight: 650;
  line-height: 1.25;
}

.cq-11__sub {
  margin: 0;
  font-size: 0.78rem;
  color: var(--mut);
}

.cq-11__swatch {
  display: none;
  list-style: none;
  margin: 0.35rem 0 0;
  padding: 0;
  gap: 0.35rem;
}

.cq-11__swatch li {
  inline-size: 1.1rem;
  block-size: 1.1rem;
  border-radius: 50%;
  box-shadow: inset 0 0 0 1px var(--line);
}

.cq-11__count {
  margin: 0.3rem 0 0;
  font-size: 0.72rem;
  color: var(--mut);
}

.cq-11__buy {
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
  align-items: stretch;
}

.cq-11__price {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.cq-11__btn {
  min-block-size: 2.75rem;
  padding-inline: 1rem;
  border: 0;
  border-radius: 999px;
  background: var(--acc);
  color: #fff;
  font: inherit;
  font-size: 0.85rem;
  font-weight: 650;
  cursor: pointer;
}

.cq-11__btn:hover {
  background: color-mix(in srgb, var(--acc) 85%, black);
}

.cq-11__btn:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

@container cq-11-cell (min-width: 15em) {
  .cq-11__card {
    padding: 1.35rem;
    gap: 1rem;
  }

  .cq-11__shot {
    aspect-ratio: 4 / 3;
  }

  .cq-11__swatch {
    display: flex;
  }

  .cq-11__count {
    display: none;
  }

  .cq-11__name {
    font-size: 1.1rem;
  }

  .cq-11__buy {
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
  }

  .cq-11__price {
    font-size: 1.5rem;
  }
}

@media (max-width: 34em) {
  .cq-11__row--four {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .cq-11__row--two {
    grid-template-columns: minmax(0, 1fr);
  }
}

@container cq-11-cell (min-width: 24em) {
  .cq-11__card {
    grid-template-columns: 11rem minmax(0, 1fr);
    grid-template-areas: "shot info" "shot buy";
    align-content: start;
  }

  .cq-11__shot {
    grid-area: shot;
    aspect-ratio: auto;
    block-size: 100%;
    min-block-size: 8rem;
  }

  .cq-11__info {
    grid-area: info;
  }

  .cq-11__buy {
    grid-area: buy;
    align-self: end;
  }
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. The
   pinned values are the demo's own [data-theme] declarations reused
   verbatim, so a toggled demo can never drift from how the same demo
   renders under the site theme. */

.cq-11 {
  position: relative;
}

.cq-11__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 9;
  display: flex;
  align-items: center;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 8%, transparent);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  font-family: system-ui, sans-serif;
}

.cq-11__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-11__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-11__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.6875rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: inherit;
  opacity: 0.55;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}

.cq-11__themeopt:hover {
  opacity: 0.85;
}

.cq-11__themeinput:checked + .cq-11__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-11__themeinput:focus-visible + .cq-11__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-11:has(#cq-11-theme-light:checked) {
  --bg: #fdf4ee;
  --surf: #ffffff;
  --line: #f0d8c8;
  --ink: #2a1410;
  --mut: #7c5a4e;
  --acc: #e4472c;
  --bloom: rgba(228, 71, 44, 0.16);
}

.cq-11:has(#cq-11-theme-dark:checked) {
  --bg: #1b100d;
  --surf: #271713;
  --line: #46271f;
  --ink: #fdeee7;
  --mut: #c69a8a;
  --acc: #ff7a5c;
  --bloom: rgba(255, 122, 92, 0.2);
}
```
