---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mega-menus/flash-sale-command-center/"
title: "Promotional Mega Menu with Offer Panel"
section: "navigation"
category: "css-mega-menus"
category_name: "CSS Mega Menus"
description: "Commerce navigation with a promotional block beside the links."
has_js: "false"
---

Here's a working CSS Mega Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Promotional Mega Menu with Offer Panel
Source: https://codefronts.com/navigation/css-mega-menus/flash-sale-command-center/

Commerce navigation with a promotional block beside the links. The design constraint is the interesting part: the promo has to stay subordinate to the navigation, because a panel that is mostly marketing stops doing the job the user opened it for. One offer, one third of the panel, and the categories keep their weight.
## HTML
```html
<section class="mm-20" aria-labelledby="mm-20-title">
  <h2 class="mm-20__sr" id="mm-20-title">Orbit Supply Co.</h2>

  <div class="mm-20__theme">
    <input class="mm-20__theme-input" type="checkbox" id="mm-20-theme">
    <label class="mm-20__theme-label" for="mm-20-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="mm-20__sr">Toggle dark theme</span>
    </label>
  </div>

  <header class="mm-20__header">
    <div class="mm-20__bar">
      <a class="mm-20__brand" href="#mm-20-title">ORBIT<span>supply co.</span></a>

      <nav class="mm-20__nav" aria-label="Primary">
        <ul class="mm-20__list">
          <li class="mm-20__item">
            <button class="mm-20__trigger" type="button" id="mm-20-trigger-shop" aria-expanded="false" aria-controls="mm-20-panel-shop">Shop</button>
            <div class="mm-20__panel" id="mm-20-panel-shop" aria-labelledby="mm-20-trigger-shop">
              <div class="mm-20__cols">
                <section class="mm-20__col" aria-labelledby="mm-20-h-desk">
                  <h3 class="mm-20__col-head" id="mm-20-h-desk">Desk</h3>
                  <ul class="mm-20__links"><li><a href="#mm-20-title">Notebooks</a></li><li><a href="#mm-20-title">Pens and refills</a></li><li><a href="#mm-20-title">Desk mats</a></li><li><a href="#mm-20-title">Organisers</a></li></ul>
                </section>
                <section class="mm-20__col" aria-labelledby="mm-20-h-carry">
                  <h3 class="mm-20__col-head" id="mm-20-h-carry">Carry</h3>
                  <ul class="mm-20__links"><li><a href="#mm-20-title">Backpacks</a></li><li><a href="#mm-20-title">Sleeves</a></li><li><a href="#mm-20-title">Pouches</a></li><li><a href="#mm-20-title">Travel sets</a></li></ul>
                </section>
                <section class="mm-20__col" aria-labelledby="mm-20-h-gift">
                  <h3 class="mm-20__col-head" id="mm-20-h-gift">Gifting</h3>
                  <ul class="mm-20__links"><li><a href="#mm-20-title">Under &pound;40</a></li><li><a href="#mm-20-title">Bundles</a></li><li><a href="#mm-20-title">Gift cards</a></li></ul>
                </section>
              </div>

              <aside class="mm-20__offer" aria-label="Autumn offer">
                <p class="mm-20__offer-tag">Autumn offer</p>
                <p class="mm-20__offer-head">Second notebook half price</p>
                <p class="mm-20__offer-body">On every A5 dot-grid in the Meridian range. Ends Sunday, no code needed.</p>
                <a class="mm-20__offer-cta" href="#mm-20-title">Shop the range</a>
              </aside>
            </div>
          </li>

          <li class="mm-20__item">
            <button class="mm-20__trigger" type="button" id="mm-20-trigger-new" aria-expanded="false" aria-controls="mm-20-panel-new">New in</button>
            <div class="mm-20__panel" id="mm-20-panel-new" aria-labelledby="mm-20-trigger-new">
              <div class="mm-20__cols">
                <section class="mm-20__col" aria-labelledby="mm-20-h-season">
                  <h3 class="mm-20__col-head" id="mm-20-h-season">This season</h3>
                  <ul class="mm-20__links"><li><a href="#mm-20-title">Winter linen range</a></li><li><a href="#mm-20-title">Brass edition pens</a></li><li><a href="#mm-20-title">Archive reprints</a></li></ul>
                </section>
                <section class="mm-20__col" aria-labelledby="mm-20-h-collab">
                  <h3 class="mm-20__col-head" id="mm-20-h-collab">Collaborations</h3>
                  <ul class="mm-20__links"><li><a href="#mm-20-title">Fern Studio</a></li><li><a href="#mm-20-title">Quill Press</a></li></ul>
                </section>
                <section class="mm-20__col" aria-labelledby="mm-20-h-back">
                  <h3 class="mm-20__col-head" id="mm-20-h-back">Back in stock</h3>
                  <ul class="mm-20__links"><li><a href="#mm-20-title">A5 dot grid</a></li><li><a href="#mm-20-title">Card wallet</a></li></ul>
                </section>
              </div>
              <aside class="mm-20__offer" aria-label="Members offer">
                <p class="mm-20__offer-tag">Members</p>
                <p class="mm-20__offer-head">Early access from Thursday</p>
                <p class="mm-20__offer-body">Sign in to shop the winter range 48 hours before general release.</p>
                <a class="mm-20__offer-cta" href="#mm-20-title">Sign in</a>
              </aside>
            </div>
          </li>

          <li class="mm-20__item"><a class="mm-20__plain" href="#mm-20-title">Journal</a></li>
          <li class="mm-20__item"><a class="mm-20__plain" href="#mm-20-title">Stores</a></li>
        </ul>
      </nav>

      <a class="mm-20__cart" href="#mm-20-title">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 7h12l-1.2 11H7.2Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M9.5 7a2.5 2.5 0 0 1 5 0" fill="none" stroke="currentColor" stroke-width="1.8"/></svg>
        Bag <span>2</span>
      </a>
    </div>
  </header>

  <main class="mm-20__page">
    <div class="mm-20__hero">
      <p class="mm-20__kicker">Made in Britain since 2009</p>
      <h1 class="mm-20__h1">Paper worth writing on.</h1>
      <p class="mm-20__sub">120gsm, fountain-pen friendly, bound to lie flat.</p>
      <a class="mm-20__hero-cta" href="#mm-20-title">Shop notebooks</a>
    </div>
  </main>
</section>
```
## CSS
```css
.mm-20 {
  --mm-20-bg: #eef2f8;
  --mm-20-surf: #ffffff;
  --mm-20-deep: #10213f;
  --mm-20-line: #10213f;
  --mm-20-soft: #d6dfec;
  --mm-20-ink: #10213f;
  --mm-20-mut: #56668a;
  --mm-20-acc: #f0a202;
  --mm-20-acc: oklch(78% 0.16 78);
  --mm-20-offset: 5px;
  --mm-20-font-display: "Futura", "Century Gothic", "Avenir Next", ui-sans-serif, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mm-20-bg);
  color: var(--mm-20-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.mm-20 *,
.mm-20 *::before,
.mm-20 *::after {
  box-sizing: border-box;
}

.mm-20 :focus-visible {
  outline: 2px solid var(--mm-20-deep);
  outline-offset: 3px;
}

.mm-20__sr {
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

.mm-20:has(.mm-20__theme-input:checked) {
  --mm-20-bg: #060b16;
  --mm-20-surf: #0d1626;
  --mm-20-deep: #f2f6fc;
  --mm-20-line: #22314c;
  --mm-20-soft: #1a2740;
  --mm-20-ink: #eaf0f9;
  --mm-20-mut: #93a5c2;
  --mm-20-acc: #fbbf24;
  --mm-20-acc: oklch(83% 0.15 80);
}

@media (prefers-color-scheme: dark) {
  .mm-20 {
    --mm-20-bg: #060b16;
    --mm-20-surf: #0d1626;
    --mm-20-deep: #f2f6fc;
    --mm-20-line: #22314c;
    --mm-20-soft: #1a2740;
    --mm-20-ink: #eaf0f9;
    --mm-20-mut: #93a5c2;
    --mm-20-acc: #fbbf24;
    --mm-20-acc: oklch(83% 0.15 80);
  }

  .mm-20:has(.mm-20__theme-input:checked) {
    --mm-20-bg: #eef2f8;
    --mm-20-surf: #ffffff;
    --mm-20-deep: #10213f;
    --mm-20-line: #10213f;
    --mm-20-soft: #d6dfec;
    --mm-20-ink: #10213f;
    --mm-20-mut: #56668a;
    --mm-20-acc: #f0a202;
    --mm-20-acc: oklch(78% 0.16 78);
  }
}

@media (prefers-color-scheme: light) {
  .mm-20:has(.mm-20__theme-input:checked) {
    --mm-20-bg: #060b16;
    --mm-20-surf: #0d1626;
    --mm-20-deep: #f2f6fc;
    --mm-20-line: #22314c;
    --mm-20-soft: #1a2740;
    --mm-20-ink: #eaf0f9;
    --mm-20-mut: #93a5c2;
    --mm-20-acc: #fbbf24;
    --mm-20-acc: oklch(83% 0.15 80);
  }
}

.mm-20__theme {
  position: absolute;
  inset-block-start: clamp(1.5rem, 4vw, 2.2rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 60;
}

.mm-20__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.mm-20__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 2px solid var(--mm-20-line);
  background: var(--mm-20-surf);
  color: var(--mm-20-ink);
  cursor: pointer;
  box-shadow: var(--mm-20-offset) var(--mm-20-offset) 0 var(--mm-20-line);
}

.mm-20__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-20__theme-input:focus-visible + .mm-20__theme-label {
  outline: 2px solid var(--mm-20-acc);
  outline-offset: 3px;
}

.mm-20__header {
  position: relative;
  z-index: 10;
  inline-size: min(70rem, calc(100% - 2rem));
  margin: clamp(1rem, 3vw, 1.75rem) auto 0;
}

.mm-20__bar {
  display: flex;
  align-items: center;
  gap: clamp(0.5rem, 2vw, 1.75rem);
  flex-wrap: wrap;
  min-block-size: 68px;
  padding-inline: clamp(0.85rem, 2vw, 1.25rem) 64px;
  border: 2px solid var(--mm-20-line);
  background: var(--mm-20-surf);
}

.mm-20__brand {
  color: var(--mm-20-ink);
  text-decoration: none;
  font: 700 1rem/1 var(--mm-20-font-display);
  letter-spacing: 0.14em;
}

.mm-20__brand span {
  display: block;
  font: 400 0.6rem/1.3 system-ui, sans-serif;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--mm-20-mut);
}

.mm-20__nav {
  min-inline-size: 0;
}

.mm-20__list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.2rem;
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
}

.mm-20__item {
  position: static;
}

.mm-20__trigger,
.mm-20__plain {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.9rem;
  border: 0;
  background: transparent;
  color: var(--mm-20-ink);
  font: 600 0.88rem/1 var(--mm-20-font-display);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  text-decoration: none;
  cursor: pointer;
}

.mm-20__item--open > .mm-20__trigger,
.mm-20__item:hover > .mm-20__trigger,
.mm-20__item:focus-within > .mm-20__trigger {
  background: var(--mm-20-acc);
  color: #10213f;
}

.mm-20__plain:hover,
.mm-20__trigger:hover {
  color: var(--mm-20-mut);
}

.mm-20__cart {
  margin-inline-start: auto;
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  min-block-size: 44px;
  padding-inline: 0.75rem;
  color: var(--mm-20-ink);
  text-decoration: none;
  font: 600 0.8rem/1 var(--mm-20-font-display);
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.mm-20__cart svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-20__cart span {
  display: grid;
  place-items: center;
  inline-size: 20px;
  block-size: 20px;
  border-radius: 999px;
  background: var(--mm-20-acc);
  color: #10213f;
  font-size: 0.7rem;
}

.mm-20__panel {
  position: absolute;
  inset-inline: -2px;
  inset-block-start: 100%;
  z-index: 30;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  border: 2px solid var(--mm-20-line);
  background: var(--mm-20-surf);
  box-shadow: var(--mm-20-offset) var(--mm-20-offset) 0 var(--mm-20-line);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 160ms ease, visibility 0s linear 160ms;
}

@media (min-width: 58rem) {
  .mm-20__panel {
    grid-template-columns: 2fr 1fr;
  }
}

.mm-20__item--open > .mm-20__panel,
.mm-20__item:focus-within > .mm-20__panel {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transition-delay: 0s;
}

@media (hover: hover) {
  .mm-20__item:hover > .mm-20__panel {
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    transition-delay: 0s;
  }
}

.mm-20__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 10rem), 1fr));
  gap: clamp(0.75rem, 2.4vw, 1.75rem);
  padding: clamp(1rem, 2.8vw, 1.6rem);
  min-inline-size: 0;
}

.mm-20__col {
  min-inline-size: 0;
}

.mm-20__col-head {
  margin: 0 0 0.4rem;
  padding-block-end: 0.35rem;
  border-block-end: 2px solid var(--mm-20-line);
  font: 700 0.85rem/1.2 var(--mm-20-font-display);
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.mm-20__links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1px;
}

.mm-20__links a {
  display: flex;
  align-items: center;
  min-block-size: 44px;
  color: var(--mm-20-ink);
  text-decoration: none;
  font-size: 0.9rem;
  min-inline-size: 0;
}

.mm-20__links a:hover {
  text-decoration: underline;
  text-underline-offset: 4px;
  text-decoration-thickness: 2px;
}

.mm-20__offer {
  min-inline-size: 0;
  display: grid;
  align-content: start;
  gap: 0.35rem;
  padding: clamp(1rem, 2.8vw, 1.6rem);
  background: var(--mm-20-acc);
  color: #10213f;
}

.mm-20__offer-tag {
  margin: 0;
  font: 700 0.66rem/1 var(--mm-20-font-display);
  letter-spacing: 0.2em;
  text-transform: uppercase;
}

.mm-20__offer-head {
  margin: 0;
  font: 700 clamp(1.1rem, 3vw, 1.35rem)/1.15 var(--mm-20-font-display);
  text-wrap: balance;
}

.mm-20__offer-body {
  margin: 0;
  font-size: 0.86rem;
  text-wrap: pretty;
}

.mm-20__offer-cta {
  justify-self: start;
  margin-block-start: 0.4rem;
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 1rem;
  background: #10213f;
  color: #ffffff;
  text-decoration: none;
  font: 700 0.78rem/1 var(--mm-20-font-display);
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.mm-20__offer-cta:hover {
  background: #000000;
}

.mm-20__page {
  inline-size: min(70rem, calc(100% - 2rem));
  margin-inline: auto;
  padding-block: clamp(3rem, 9vw, 5.5rem);
}

.mm-20__hero {
  max-inline-size: 34rem;
  display: grid;
  gap: 0.55rem;
}

.mm-20__kicker {
  margin: 0;
  font: 700 0.68rem/1 var(--mm-20-font-display);
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--mm-20-mut);
}

.mm-20__h1 {
  margin: 0;
  font: 700 clamp(2.2rem, 7vw, 3.8rem)/1.02 var(--mm-20-font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.mm-20__sub {
  margin: 0;
  color: var(--mm-20-mut);
  font-size: clamp(0.95rem, 2.3vw, 1.1rem);
}

.mm-20__hero-cta {
  justify-self: start;
  display: inline-flex;
  align-items: center;
  min-block-size: 48px;
  margin-block-start: 0.4rem;
  padding-inline: 1.4rem;
  border: 2px solid var(--mm-20-line);
  background: var(--mm-20-acc);
  color: #10213f;
  text-decoration: none;
  font: 700 0.82rem/1 var(--mm-20-font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  box-shadow: var(--mm-20-offset) var(--mm-20-offset) 0 var(--mm-20-line);
}

@media (max-width: 54rem) {
  .mm-20__bar {
    flex-direction: column;
    align-items: stretch;
    padding-block: 0.6rem;
  }

  .mm-20__list {
    flex-direction: column;
  }

  .mm-20__cart {
    margin-inline-start: 0;
  }

  .mm-20__panel {
    position: static;
    inset-inline: auto;
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    box-shadow: none;
    display: none;
    margin-block-start: 0.5rem;
  }

  .mm-20__item--open > .mm-20__panel,
    .mm-20__item:focus-within > .mm-20__panel {
    display: grid;
  }
}

@media (prefers-reduced-motion: reduce) {
  .mm-20__panel {
    transition-duration: 1ms;
  }
}

@media (hover: hover) and (pointer: fine) {
  .mm-20__trigger {
    position: relative;
  }

  .mm-20__item:hover > .mm-20__trigger::after,
    .mm-20__item:focus-within > .mm-20__trigger::after {
    content: "";
    position: absolute;
    inset-inline: 0;
    inset-block-start: 100%;
    block-size: 16px;
  }
}
/* Entry signature — fast overshoot pop, alternating columns offset for a ripple across the panel */

.mm-20__links li,
.mm-20__sub li {
  opacity: 0;
  scale: 0.86;
  transform-origin: 0 50%;
  transition: opacity 140ms ease, scale 400ms cubic-bezier(0.34, 1.6, 0.64, 1);
}

.mm-20__item:hover > .mm-20__panel .mm-20__links li,
.mm-20__item:focus-within > .mm-20__panel .mm-20__links li,
.mm-20__item--open > .mm-20__panel .mm-20__links li {
  opacity: 1;
  scale: 1;
}

.mm-20__item:hover > .mm-20__panel .mm-20__sub li,
.mm-20__item:focus-within > .mm-20__panel .mm-20__sub li,
.mm-20__item--open > .mm-20__panel .mm-20__sub li {
  opacity: 1;
  scale: 1;
}

.mm-20__links li:nth-child(1) {
  transition-delay: 20ms;
}

.mm-20__links li:nth-child(2) {
  transition-delay: 52ms;
}

.mm-20__links li:nth-child(3) {
  transition-delay: 84ms;
}

.mm-20__links li:nth-child(4) {
  transition-delay: 116ms;
}

.mm-20__links li:nth-child(5) {
  transition-delay: 148ms;
}

.mm-20__links li:nth-child(6) {
  transition-delay: 180ms;
}

.mm-20__links li:nth-child(n+7) {
  transition-delay: 180ms;
}

.mm-20__col:nth-child(even) .mm-20__links li {
  transition-delay: 80ms;
}

@media (prefers-reduced-motion: reduce) {
  .mm-20__links li,
    .mm-20__sub li {
    transition-duration: 1ms;
    transition-delay: 0s;
    animation: none;
  }

  .mm-20__links li,
    .mm-20__sub li {
    opacity: 1;
    scale: 1;
  }
}
```
