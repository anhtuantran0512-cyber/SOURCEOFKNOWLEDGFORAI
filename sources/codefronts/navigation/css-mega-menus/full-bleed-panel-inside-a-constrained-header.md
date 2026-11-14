---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mega-menus/full-bleed-panel-inside-a-constrained-header/"
title: "Full Bleed Panel Inside a Constrained Header"
section: "navigation"
category: "css-mega-menus"
category_name: "CSS Mega Menus"
description: "The header content is capped at a max-width but the mega panel should span the whole viewport, and doing that from inside a constrained parent is the actual…"
has_js: "false"
---

Here's a working CSS Mega Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Full Bleed Panel Inside a Constrained Header
Source: https://codefronts.com/navigation/css-mega-menus/full-bleed-panel-inside-a-constrained-header/

The header content is capped at a max-width but the mega panel should span the whole viewport, and doing that from inside a constrained parent is the actual layout puzzle. This garden retail header solves it by moving the containing block rather than the panel &mdash; the outer element is positioned, the inner row keeps its cap, and no viewport units or negative margins are involved.
## HTML
```html
<section class="mm-06" aria-labelledby="mm-06-title">
  <h2 class="mm-06__sr" id="mm-06-title">Fern</h2>

  <div class="mm-06__theme">
    <input class="mm-06__theme-input" type="checkbox" id="mm-06-theme">
    <label class="mm-06__theme-label" for="mm-06-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="mm-06__sr">Toggle dark theme</span>
    </label>
  </div>

  <p class="mm-06__band">Free delivery on orders over &pound;40 &middot; Autumn bulbs now shipping</p>

  <header class="mm-06__header">
    <div class="mm-06__row">
      <a class="mm-06__brand" href="#mm-06-title">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 21c0-7 4-12 9-13-1 8-4 12-9 13Z" fill="currentColor" opacity=".85"/><path d="M12 21C9 15 5 12 3 11c1 6 4 9 9 10Z" fill="currentColor" opacity=".5"/></svg>
        Fern
      </a>

      <nav class="mm-06__nav" aria-label="Primary">
        <ul class="mm-06__list">
          <li class="mm-06__item">
            <button class="mm-06__trigger" type="button" aria-expanded="false" aria-controls="mm-06-panel-grow">Grow
              <svg class="mm-06__chev" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            </button>
            <div class="mm-06__panel" id="mm-06-panel-grow" aria-label="Grow">
              <div class="mm-06__panel-inner">
                <div class="mm-06__lead">
                  <p class="mm-06__eyebrow">Field notes</p>
                  <p class="mm-06__blurb">Seasonal planting guidance written by growers, not marketers.</p>
                  <a class="mm-06__lead-cta" href="#mm-06-title">Read the autumn guide</a>
                </div>
                <section class="mm-06__col" aria-labelledby="mm-06-h-soil">
                  <h3 class="mm-06__col-head" id="mm-06-h-soil">Soil</h3>
                  <ul class="mm-06__links"><li><a href="#mm-06-title">Composting</a></li><li><a href="#mm-06-title">pH testing</a></li><li><a href="#mm-06-title">Mulch types</a></li><li><a href="#mm-06-title">Raised beds</a></li></ul>
                </section>
                <section class="mm-06__col" aria-labelledby="mm-06-h-water">
                  <h3 class="mm-06__col-head" id="mm-06-h-water">Water</h3>
                  <ul class="mm-06__links"><li><a href="#mm-06-title">Drip systems</a></li><li><a href="#mm-06-title">Rain capture</a></li><li><a href="#mm-06-title">Drought planting</a></li></ul>
                </section>
                <section class="mm-06__col" aria-labelledby="mm-06-h-season">
                  <h3 class="mm-06__col-head" id="mm-06-h-season">Season</h3>
                  <ul class="mm-06__links"><li><a href="#mm-06-title">Frost dates</a></li><li><a href="#mm-06-title">Overwintering</a></li><li><a href="#mm-06-title">Cover crops</a></li><li><a href="#mm-06-title">Bulb planner</a></li></ul>
                </section>
              </div>
            </div>
          </li>

          <li class="mm-06__item">
            <button class="mm-06__trigger" type="button" aria-expanded="false" aria-controls="mm-06-panel-shop">Shop
              <svg class="mm-06__chev" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            </button>
            <div class="mm-06__panel" id="mm-06-panel-shop" aria-label="Shop">
              <div class="mm-06__panel-inner">
                <div class="mm-06__lead">
                  <p class="mm-06__eyebrow">In season</p>
                  <p class="mm-06__blurb">Bulbs and bare-root stock, lifted this week and shipped within two days.</p>
                  <a class="mm-06__lead-cta" href="#mm-06-title">Shop autumn planting</a>
                </div>
                <section class="mm-06__col" aria-labelledby="mm-06-h-plants">
                  <h3 class="mm-06__col-head" id="mm-06-h-plants">Plants</h3>
                  <ul class="mm-06__links"><li><a href="#mm-06-title">Bulbs</a></li><li><a href="#mm-06-title">Perennials</a></li><li><a href="#mm-06-title">Hedging</a></li></ul>
                </section>
                <section class="mm-06__col" aria-labelledby="mm-06-h-tools">
                  <h3 class="mm-06__col-head" id="mm-06-h-tools">Tools</h3>
                  <ul class="mm-06__links"><li><a href="#mm-06-title">Spades and forks</a></li><li><a href="#mm-06-title">Secateurs</a></li><li><a href="#mm-06-title">Watering</a></li></ul>
                </section>
                <section class="mm-06__col" aria-labelledby="mm-06-h-gifts">
                  <h3 class="mm-06__col-head" id="mm-06-h-gifts">Gifts</h3>
                  <ul class="mm-06__links"><li><a href="#mm-06-title">Gift cards</a></li><li><a href="#mm-06-title">Starter kits</a></li></ul>
                </section>
              </div>
            </div>
          </li>

          <li class="mm-06__item"><a class="mm-06__plain" href="#mm-06-title">Journal</a></li>
          <li class="mm-06__item"><a class="mm-06__plain" href="#mm-06-title">Visit us</a></li>
        </ul>
      </nav>

      <div class="mm-06__utils">
        <a class="mm-06__util" href="#mm-06-title">Account</a>
        <a class="mm-06__bag" href="#mm-06-title">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 7h12l-1.2 11H7.2Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M9.5 7a2.5 2.5 0 0 1 5 0" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>
          Basket <span>3</span>
        </a>
      </div>
    </div>
  </header>

  <main class="mm-06__page">
    <div class="mm-06__hero">
      <p class="mm-06__hero-kicker">Autumn 2026</p>
      <h1 class="mm-06__hero-title">Plant now. Thank yourself in March.</h1>
      <p class="mm-06__hero-sub">Twelve hundred bulb varieties, lifted to order from our Somerset beds.</p>
      <a class="mm-06__hero-cta" href="#mm-06-title">Shop autumn planting</a>
    </div>
  </main>
</section>
```
## CSS
```css
.mm-06 {
  --mm-06-bg: #f2f5f0;
  --mm-06-surf: #ffffff;
  --mm-06-panel: #eef2ea;
  --mm-06-line: #d3ddcc;
  --mm-06-ink: #1b2a1f;
  --mm-06-mut: #5f7061;
  --mm-06-acc: #2f6b3f;
  --mm-06-acc: oklch(46% 0.11 152);
  --mm-06-on-acc: #ffffff;
  --mm-06-max: 72rem;
  --mm-06-font-display: "Trebuchet MS", "Lucida Grande", ui-sans-serif, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mm-06-bg);
  color: var(--mm-06-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
  overflow-x: clip;
}

.mm-06 *,
.mm-06 *::before,
.mm-06 *::after {
  box-sizing: border-box;
}

.mm-06 :focus-visible {
  outline: 2px solid var(--mm-06-acc);
  outline-offset: 3px;
  border-radius: 4px;
}

.mm-06__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.mm-06:has(.mm-06__theme-input:checked) {
  --mm-06-bg: #0a110c;
  --mm-06-surf: #121b14;
  --mm-06-panel: #16211a;
  --mm-06-line: #26362a;
  --mm-06-ink: #e8f1e8;
  --mm-06-mut: #9bb09e;
  --mm-06-acc: #6ee7a0;
  --mm-06-acc: oklch(83% 0.14 156);
  --mm-06-on-acc: #12100e;
}

@media (prefers-color-scheme: dark) {
  .mm-06 {
    --mm-06-bg: #0a110c;
    --mm-06-surf: #121b14;
    --mm-06-panel: #16211a;
    --mm-06-line: #26362a;
    --mm-06-ink: #e8f1e8;
    --mm-06-mut: #9bb09e;
    --mm-06-acc: #6ee7a0;
    --mm-06-acc: oklch(83% 0.14 156);
    --mm-06-on-acc: #12100e;
  }

  .mm-06:has(.mm-06__theme-input:checked) {
    --mm-06-bg: #f2f5f0;
    --mm-06-surf: #ffffff;
    --mm-06-panel: #eef2ea;
    --mm-06-line: #d3ddcc;
    --mm-06-ink: #1b2a1f;
    --mm-06-mut: #5f7061;
    --mm-06-acc: #2f6b3f;
    --mm-06-acc: oklch(46% 0.11 152);
    --mm-06-on-acc: #ffffff;
  }
}

@media (prefers-color-scheme: light) {
  .mm-06:has(.mm-06__theme-input:checked) {
    --mm-06-bg: #0a110c;
    --mm-06-surf: #121b14;
    --mm-06-panel: #16211a;
    --mm-06-line: #26362a;
    --mm-06-ink: #e8f1e8;
    --mm-06-mut: #9bb09e;
    --mm-06-acc: #6ee7a0;
    --mm-06-acc: oklch(83% 0.14 156);
    --mm-06-on-acc: #12100e;
  }
}

.mm-06__theme {
  position: absolute;
  inset-block-start: 46px;
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 60;
}

.mm-06__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.mm-06__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mm-06-line);
  border-radius: 999px;
  background: var(--mm-06-surf);
  color: var(--mm-06-ink);
  cursor: pointer;
}

.mm-06__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-06__theme-input:focus-visible + .mm-06__theme-label {
  outline: 2px solid var(--mm-06-acc);
  outline-offset: 3px;
}

.mm-06__band {
  margin: 0;
  display: grid;
  place-items: center;
  min-block-size: 36px;
  padding-inline: 1rem;
  background: var(--mm-06-acc);
  color: var(--mm-06-on-acc);
  font: 600 0.76rem/1.3 system-ui, sans-serif;
  letter-spacing: 0.02em;
  text-align: center;
}

.mm-06__header {
  position: relative;
  z-index: 10;
  inline-size: 100%;
  background: var(--mm-06-surf);
  border-block-end: 1px solid var(--mm-06-line);
}

.mm-06__row {
  inline-size: min(var(--mm-06-max), calc(100% - 2rem));
  margin-inline: auto;
  display: flex;
  align-items: center;
  gap: clamp(0.5rem, 2vw, 2rem);
  flex-wrap: wrap;
  min-block-size: 70px;
  padding-inline-end: 60px;
}

.mm-06__brand {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  color: var(--mm-06-ink);
  text-decoration: none;
  font: 700 1.2rem/1 var(--mm-06-font-display);
  letter-spacing: -0.01em;
}

.mm-06__brand svg {
  inline-size: 22px;
  block-size: 22px;
  color: var(--mm-06-acc);
}

.mm-06__nav {
  min-inline-size: 0;
}

.mm-06__list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.2rem;
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
}

.mm-06__item {
  position: static;
}

.mm-06__trigger,
.mm-06__plain {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  min-block-size: 44px;
  padding-inline: 0.8rem;
  border: 0;
  border-radius: 6px;
  background: transparent;
  color: var(--mm-06-ink);
  font: 600 0.92rem/1 system-ui, sans-serif;
  text-decoration: none;
  cursor: pointer;
}

.mm-06__chev {
  inline-size: 15px;
  block-size: 15px;
}

.mm-06__item--open > .mm-06__trigger,
.mm-06__item:hover > .mm-06__trigger,
.mm-06__item:focus-within > .mm-06__trigger {
  color: var(--mm-06-acc);
}

.mm-06__plain:hover,
.mm-06__trigger:hover {
  color: var(--mm-06-acc);
}

.mm-06__utils {
  margin-inline-start: auto;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.mm-06__util {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.6rem;
  color: var(--mm-06-mut);
  text-decoration: none;
  font: 600 0.86rem/1 system-ui, sans-serif;
}

.mm-06__bag {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  min-block-size: 44px;
  padding-inline: 0.7rem;
  color: var(--mm-06-ink);
  text-decoration: none;
  font: 600 0.86rem/1 system-ui, sans-serif;
}

.mm-06__bag svg {
  inline-size: 19px;
  block-size: 19px;
}

.mm-06__bag span {
  display: grid;
  place-items: center;
  inline-size: 19px;
  block-size: 19px;
  border-radius: 999px;
  background: var(--mm-06-acc);
  color: var(--mm-06-on-acc);
  font-size: 0.68rem;
}

.mm-06__panel {
  position: absolute;
  inset-inline: 0;
  inset-block-start: 100%;
  z-index: 30;
  background: var(--mm-06-panel);
  border-block-end: 1px solid var(--mm-06-line);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 160ms ease, visibility 0s linear 160ms;
}

.mm-06__item--open > .mm-06__panel,
.mm-06__item:focus-within > .mm-06__panel {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transition-delay: 0s;
}

@media (hover: hover) {
  .mm-06__item:hover > .mm-06__panel {
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    transition-delay: 0s;
  }
}

.mm-06__panel-inner {
  inline-size: min(var(--mm-06-max), calc(100% - 2rem));
  margin-inline: auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 11rem), 1fr));
  gap: clamp(0.9rem, 2.5vw, 2.5rem);
  padding-block: clamp(1.1rem, 3vw, 2rem);
}

.mm-06__lead {
  min-inline-size: 0;
  display: grid;
  align-content: start;
  gap: 0.4rem;
  padding-inline-end: clamp(0.5rem, 2vw, 1.5rem);
  border-inline-end: 1px solid var(--mm-06-line);
}

.mm-06__eyebrow {
  margin: 0;
  font: 700 0.66rem/1 var(--mm-06-font-display);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--mm-06-acc);
}

.mm-06__blurb {
  margin: 0;
  font-size: 0.95rem;
  text-wrap: pretty;
}

.mm-06__lead-cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  color: var(--mm-06-acc);
  font: 600 0.86rem/1 system-ui, sans-serif;
  text-decoration: none;
}

.mm-06__lead-cta:hover {
  text-decoration: underline;
  text-underline-offset: 3px;
}

.mm-06__col {
  min-inline-size: 0;
}

.mm-06__col-head {
  margin: 0 0 0.3rem;
  font: 700 0.68rem/1 var(--mm-06-font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--mm-06-mut);
}

.mm-06__links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1px;
}

.mm-06__links a {
  display: flex;
  align-items: center;
  min-block-size: 44px;
  color: var(--mm-06-ink);
  text-decoration: none;
  font-size: 0.9rem;
  min-inline-size: 0;
}

.mm-06__links a:hover {
  color: var(--mm-06-acc);
  text-decoration: underline;
  text-underline-offset: 3px;
}

.mm-06__page {
  inline-size: min(var(--mm-06-max), calc(100% - 2rem));
  margin-inline: auto;
  padding-block: clamp(3rem, 10vw, 6rem);
}

.mm-06__hero {
  max-inline-size: 38rem;
  display: grid;
  gap: 0.7rem;
}

.mm-06__hero-kicker {
  margin: 0;
  font: 700 0.7rem/1 var(--mm-06-font-display);
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--mm-06-acc);
}

.mm-06__hero-title {
  margin: 0;
  font: 700 clamp(2rem, 6vw, 3.5rem)/1.05 var(--mm-06-font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.mm-06__hero-sub {
  margin: 0;
  color: var(--mm-06-mut);
  font-size: clamp(0.95rem, 2.3vw, 1.1rem);
  text-wrap: pretty;
}

.mm-06__hero-cta {
  justify-self: start;
  display: inline-flex;
  align-items: center;
  min-block-size: 48px;
  margin-block-start: 0.4rem;
  padding-inline: 1.3rem;
  border-radius: 999px;
  background: var(--mm-06-acc);
  color: var(--mm-06-on-acc);
  text-decoration: none;
  font: 600 0.95rem/1 system-ui, sans-serif;
}

@media (max-width: 54rem) {
  .mm-06__row {
    flex-direction: column;
    align-items: stretch;
    padding-block: 0.6rem;
  }

  .mm-06__list {
    flex-direction: column;
  }

  .mm-06__utils {
    margin-inline-start: 0;
  }

  .mm-06__panel {
    position: static;
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    display: none;
  }

  .mm-06__item--open > .mm-06__panel,
    .mm-06__item:focus-within > .mm-06__panel {
    display: block;
  }

  .mm-06__panel-inner {
    inline-size: 100%;
  }

  .mm-06__lead {
    border-inline-end: 0;
    padding-inline-end: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .mm-06__panel {
    transition-duration: 1ms;
  }
}

@media (hover: hover) and (pointer: fine) {
  .mm-06__trigger {
    position: relative;
  }

  .mm-06__item:hover > .mm-06__trigger::after,
    .mm-06__item:focus-within > .mm-06__trigger::after {
    content: "";
    position: absolute;
    inset-inline: 0;
    inset-block-start: 100%;
    block-size: 16px;
  }
}
/* Entry signature — full-bleed curtain opens from the centre outward */

.mm-06__panel-inner {
  clip-path: inset(0 46% 0 46%);
  opacity: 0.35;
  transition: clip-path 480ms cubic-bezier(0.22, 1, 0.36, 1), opacity 320ms ease;
}

.mm-06__item:hover > .mm-06__panel .mm-06__panel-inner,
.mm-06__item:focus-within > .mm-06__panel .mm-06__panel-inner,
.mm-06__item--open > .mm-06__panel .mm-06__panel-inner {
  clip-path: inset(-10px);
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  .mm-06__panel-inner {
    transition-duration: 1ms;
    transition-delay: 0s;
    animation: none;
  }

  .mm-06__panel-inner {
    clip-path: none;
    opacity: 1;
  }
}
```
