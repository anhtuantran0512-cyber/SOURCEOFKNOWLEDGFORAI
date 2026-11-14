---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mega-menus/aria-for-disclosure-style-navigation-panels/"
title: "ARIA for Disclosure Style Navigation Panels"
section: "navigation"
category: "css-mega-menus"
category_name: "CSS Mega Menus"
description: "The boundary marker for the whole collection, shipped as a working retail header."
has_js: "false"
---

Here's a working CSS Mega Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: ARIA for Disclosure Style Navigation Panels
Source: https://codefronts.com/navigation/css-mega-menus/aria-for-disclosure-style-navigation-panels/

The boundary marker for the whole collection, shipped as a working retail header. role="menu" and role="menuitem" belong to application menus and bring keyboard conventions that are wrong for navigation links. This panel is a disclosure instead: a <button> with aria-expanded and aria-controls, a named region, real lists, real links and aria-current="page" on the active one.
## HTML
```html
<section class="mm-09" aria-labelledby="mm-09-title">
  <h2 class="mm-09__sr" id="mm-09-title">Aperture</h2>

  <div class="mm-09__theme">
    <input class="mm-09__theme-input" type="checkbox" id="mm-09-theme">
    <label class="mm-09__theme-label" for="mm-09-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="mm-09__sr">Toggle dark theme</span>
    </label>
  </div>

  <header class="mm-09__header">
    <div class="mm-09__bar">
      <a class="mm-09__brand" href="#mm-09-title">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.5 16 11h-8Zm8.2 5.6L16 16l4.2 1.1ZM3.8 9.1 8 16l-4.2 1.1Z" fill="currentColor"/></svg>
        APERTURE
      </a>

      <nav class="mm-09__nav" aria-label="Primary">
        <ul class="mm-09__list">
          <li class="mm-09__item">
            <button class="mm-09__trigger" type="button" id="mm-09-trigger-products" aria-expanded="false" aria-controls="mm-09-panel-products">Products</button>
            <div class="mm-09__panel" id="mm-09-panel-products" aria-labelledby="mm-09-trigger-products">
              <div class="mm-09__panel-inner">
                <section class="mm-09__col" aria-labelledby="mm-09-h-bodies">
                  <h3 class="mm-09__col-head" id="mm-09-h-bodies">Bodies</h3>
                  <ul class="mm-09__links">
                    <li><a href="#mm-09-title">Full frame</a></li>
                    <li><a href="#mm-09-title">APS-C</a></li>
                    <li><a href="#mm-09-title">Medium format</a></li>
                    <li><a href="#mm-09-title">Rangefinder</a></li>
                  </ul>
                </section>
                <section class="mm-09__col" aria-labelledby="mm-09-h-glass">
                  <h3 class="mm-09__col-head" id="mm-09-h-glass">Lenses</h3>
                  <ul class="mm-09__links">
                    <li><a href="#mm-09-title" aria-current="page">Primes</a></li>
                    <li><a href="#mm-09-title">Zooms</a></li>
                    <li><a href="#mm-09-title">Tilt-shift</a></li>
                    <li><a href="#mm-09-title">Adapters</a></li>
                  </ul>
                </section>
                <section class="mm-09__col" aria-labelledby="mm-09-h-light">
                  <h3 class="mm-09__col-head" id="mm-09-h-light">Lighting</h3>
                  <ul class="mm-09__links">
                    <li><a href="#mm-09-title">Strobes</a></li>
                    <li><a href="#mm-09-title">Continuous</a></li>
                    <li><a href="#mm-09-title">Modifiers</a></li>
                  </ul>
                </section>

                <dl class="mm-09__spec">
                  <div><dt>In stock today</dt><dd>412 items</dd></div>
                  <div><dt>Trade-in</dt><dd>Valuation in 24h</dd></div>
                  <div><dt>Rental</dt><dd>Next-day to 42 cities</dd></div>
                </dl>
              </div>
            </div>
          </li>

          <li class="mm-09__item">
            <button class="mm-09__trigger" type="button" id="mm-09-trigger-service" aria-expanded="false" aria-controls="mm-09-panel-service">Service</button>
            <div class="mm-09__panel" id="mm-09-panel-service" aria-labelledby="mm-09-trigger-service">
              <div class="mm-09__panel-inner">
                <section class="mm-09__col" aria-labelledby="mm-09-h-repair">
                  <h3 class="mm-09__col-head" id="mm-09-h-repair">Repair</h3>
                  <ul class="mm-09__links"><li><a href="#mm-09-title">Sensor clean</a></li><li><a href="#mm-09-title">Shutter replacement</a></li><li><a href="#mm-09-title">Lens calibration</a></li></ul>
                </section>
                <section class="mm-09__col" aria-labelledby="mm-09-h-trade">
                  <h3 class="mm-09__col-head" id="mm-09-h-trade">Trade</h3>
                  <ul class="mm-09__links"><li><a href="#mm-09-title">Sell your kit</a></li><li><a href="#mm-09-title">Part exchange</a></li></ul>
                </section>
                <section class="mm-09__col" aria-labelledby="mm-09-h-learn9">
                  <h3 class="mm-09__col-head" id="mm-09-h-learn9">Learn</h3>
                  <ul class="mm-09__links"><li><a href="#mm-09-title">Workshops</a></li><li><a href="#mm-09-title">Darkroom hire</a></li></ul>
                </section>
                <dl class="mm-09__spec">
                  <div><dt>Turnaround</dt><dd>5 working days</dd></div>
                  <div><dt>Warranty</dt><dd>12 months on repairs</dd></div>
                </dl>
              </div>
            </div>
          </li>

          <li class="mm-09__item"><a class="mm-09__plain" href="#mm-09-title">Used</a></li>
          <li class="mm-09__item"><a class="mm-09__plain mm-09__plain--flag" href="#mm-09-title">Clearance</a></li>
        </ul>
      </nav>

      <div class="mm-09__utils">
        <a class="mm-09__util" href="#mm-09-title">Stores</a>
        <a class="mm-09__util" href="#mm-09-title">Account</a>
        <a class="mm-09__bag" href="#mm-09-title">Bag (1)</a>
      </div>
    </div>
  </header>

  <main class="mm-09__page">
    <div class="mm-09__feature">
      <p class="mm-09__feature-k">Primes / 35mm</p>
      <h1 class="mm-09__feature-h">Aperture 35mm f/1.4 Mark III</h1>
      <p class="mm-09__feature-p">Eleven elements, weather sealed, 420g. Built for the frame you did not plan for.</p>
      <p class="mm-09__price">&pound;1,290 <span>or &pound;107/mo</span></p>
    </div>
  </main>
</section>
```
## CSS
```css
.mm-09 {
  --mm-09-bg: #ffffff;
  --mm-09-surf: #ffffff;
  --mm-09-line: #111111;
  --mm-09-soft: #ededed;
  --mm-09-ink: #111111;
  --mm-09-mut: #6b6b6b;
  --mm-09-red: #d90429;
  --mm-09-red: oklch(55% 0.23 25);
  --mm-09-rule: 1px;
  --mm-09-font-display: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mm-09-bg);
  color: var(--mm-09-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.mm-09 *,
.mm-09 *::before,
.mm-09 *::after {
  box-sizing: border-box;
}

.mm-09 :focus-visible {
  outline: 2px solid var(--mm-09-red);
  outline-offset: 2px;
}

.mm-09__sr {
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

.mm-09:has(.mm-09__theme-input:checked) {
  --mm-09-bg: #0b0b0b;
  --mm-09-surf: #131313;
  --mm-09-line: #f2f2f2;
  --mm-09-soft: #262626;
  --mm-09-ink: #f2f2f2;
  --mm-09-mut: #a0a0a0;
  --mm-09-red: #ff4d6d;
  --mm-09-red: oklch(71% 0.18 20);
}

@media (prefers-color-scheme: dark) {
  .mm-09 {
    --mm-09-bg: #0b0b0b;
    --mm-09-surf: #131313;
    --mm-09-line: #f2f2f2;
    --mm-09-soft: #262626;
    --mm-09-ink: #f2f2f2;
    --mm-09-mut: #a0a0a0;
    --mm-09-red: #ff4d6d;
    --mm-09-red: oklch(71% 0.18 20);
  }

  .mm-09:has(.mm-09__theme-input:checked) {
    --mm-09-bg: #ffffff;
    --mm-09-surf: #ffffff;
    --mm-09-line: #111111;
    --mm-09-soft: #ededed;
    --mm-09-ink: #111111;
    --mm-09-mut: #6b6b6b;
    --mm-09-red: #d90429;
    --mm-09-red: oklch(55% 0.23 25);
  }
}

@media (prefers-color-scheme: light) {
  .mm-09:has(.mm-09__theme-input:checked) {
    --mm-09-bg: #0b0b0b;
    --mm-09-surf: #131313;
    --mm-09-line: #f2f2f2;
    --mm-09-soft: #262626;
    --mm-09-ink: #f2f2f2;
    --mm-09-mut: #a0a0a0;
    --mm-09-red: #ff4d6d;
    --mm-09-red: oklch(71% 0.18 20);
  }
}

.mm-09__theme {
  position: absolute;
  inset-block-start: 12px;
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 60;
}

.mm-09__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.mm-09__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: var(--mm-09-rule) solid var(--mm-09-line);
  background: var(--mm-09-surf);
  color: var(--mm-09-ink);
  cursor: pointer;
}

.mm-09__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-09__theme-input:focus-visible + .mm-09__theme-label {
  outline: 2px solid var(--mm-09-red);
  outline-offset: 3px;
}

.mm-09__header {
  position: relative;
  z-index: 10;
  inline-size: 100%;
  border-block-end: 2px solid var(--mm-09-line);
  background: var(--mm-09-surf);
}

.mm-09__bar {
  inline-size: min(80rem, calc(100% - 2rem));
  margin-inline: auto;
  display: flex;
  align-items: center;
  gap: clamp(0.75rem, 3vw, 2.5rem);
  flex-wrap: wrap;
  min-block-size: 66px;
  padding-inline-end: 60px;
}

.mm-09__brand {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--mm-09-ink);
  text-decoration: none;
  font: 700 0.95rem/1 var(--mm-09-font-display);
  letter-spacing: 0.22em;
}

.mm-09__brand svg {
  inline-size: 22px;
  block-size: 22px;
}

.mm-09__nav {
  min-inline-size: 0;
}

.mm-09__list {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(0.15rem, 1.5vw, 0.5rem);
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
}

.mm-09__item {
  position: static;
}

.mm-09__trigger,
.mm-09__plain {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.6rem;
  border: 0;
  background: transparent;
  color: var(--mm-09-ink);
  font: 600 0.82rem/1 var(--mm-09-font-display);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  text-decoration: none;
  cursor: pointer;
}

.mm-09__item--open > .mm-09__trigger,
.mm-09__item:hover > .mm-09__trigger,
.mm-09__item:focus-within > .mm-09__trigger {
  background: var(--mm-09-ink);
  color: var(--mm-09-bg);
}

.mm-09__plain--flag {
  color: var(--mm-09-red);
}

.mm-09__utils {
  margin-inline-start: auto;
  display: flex;
  align-items: center;
  gap: 0.9rem;
}

.mm-09__util {
  color: var(--mm-09-mut);
  text-decoration: none;
  font: 500 0.78rem/1 var(--mm-09-font-display);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
}

.mm-09__bag {
  display: inline-flex;
  align-items: center;
  min-block-size: 34px;
  padding-inline: 0.7rem;
  border: var(--mm-09-rule) solid var(--mm-09-line);
  color: var(--mm-09-ink);
  text-decoration: none;
  font: 600 0.75rem/1 var(--mm-09-font-display);
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.mm-09__panel {
  position: absolute;
  inset-inline: 0;
  inset-block-start: 100%;
  z-index: 30;
  background: var(--mm-09-surf);
  border-block-end: 2px solid var(--mm-09-line);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 150ms ease, visibility 0s linear 150ms;
}

.mm-09__item--open > .mm-09__panel,
.mm-09__item:focus-within > .mm-09__panel {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transition-delay: 0s;
}

@media (hover: hover) {
  .mm-09__item:hover > .mm-09__panel {
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    transition-delay: 0s;
  }
}

.mm-09__panel-inner {
  inline-size: min(80rem, calc(100% - 2rem));
  margin-inline: auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 11rem), 1fr));
  gap: 0 clamp(1rem, 4vw, 3rem);
  padding-block: clamp(1.1rem, 3vw, 1.9rem);
}

.mm-09__col {
  min-inline-size: 0;
}

.mm-09__col-head {
  margin: 0 0 0.4rem;
  padding-block-end: 0.35rem;
  border-block-end: 2px solid var(--mm-09-line);
  font: 700 0.7rem/1 var(--mm-09-font-display);
  letter-spacing: 0.18em;
  text-transform: uppercase;
}

.mm-09__links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
}

.mm-09__links a {
  display: flex;
  align-items: center;
  min-block-size: 44px;
  color: var(--mm-09-ink);
  text-decoration: none;
  font-size: 0.9rem;
  border-block-end: var(--mm-09-rule) solid var(--mm-09-soft);
  min-inline-size: 0;
}

.mm-09__links a:hover {
  color: var(--mm-09-red);
}

.mm-09__links a[aria-current="page"] {
  font-weight: 700;
  box-shadow: inset 3px 0 0 var(--mm-09-red);
  padding-inline-start: 0.5rem;
}

.mm-09__spec {
  display: grid;
  align-content: start;
  gap: 0.6rem;
  margin: 0;
  padding: 0.9rem 1rem;
  background: var(--mm-09-soft);
  min-inline-size: 0;
}

.mm-09__spec dt {
  font: 700 0.62rem/1 var(--mm-09-font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--mm-09-mut);
}

.mm-09__spec dd {
  margin: 0.15rem 0 0;
  font-size: 0.86rem;
}

.mm-09__page {
  inline-size: min(80rem, calc(100% - 2rem));
  margin-inline: auto;
  padding-block: clamp(2.5rem, 8vw, 5rem);
}

.mm-09__feature {
  max-inline-size: 40rem;
  display: grid;
  gap: 0.5rem;
}

.mm-09__feature-k {
  margin: 0;
  font: 600 0.72rem/1 var(--mm-09-font-display);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--mm-09-red);
}

.mm-09__feature-h {
  margin: 0;
  font: 400 clamp(1.9rem, 6vw, 3.2rem)/1.05 var(--mm-09-font-display);
  letter-spacing: -0.04em;
  text-wrap: balance;
}

.mm-09__feature-p {
  margin: 0;
  color: var(--mm-09-mut);
  font-size: clamp(0.95rem, 2.3vw, 1.05rem);
  text-wrap: pretty;
}

.mm-09__price {
  margin: 0.4rem 0 0;
  font: 700 1.6rem/1 var(--mm-09-font-display);
  font-variant-numeric: tabular-nums;
}

.mm-09__price span {
  font: 400 0.85rem/1 var(--mm-09-font-display);
  color: var(--mm-09-mut);
}

@media (max-width: 52rem) {
  .mm-09__bar {
    flex-direction: column;
    align-items: stretch;
    padding-block: 0.6rem;
  }

  .mm-09__list {
    flex-direction: column;
  }

  .mm-09__utils {
    margin-inline-start: 0;
  }

  .mm-09__panel {
    position: static;
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    display: none;
  }

  .mm-09__item--open > .mm-09__panel,
    .mm-09__item:focus-within > .mm-09__panel {
    display: block;
  }

  .mm-09__panel-inner {
    inline-size: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .mm-09__panel {
    transition-duration: 1ms;
  }
}

@media (hover: hover) and (pointer: fine) {
  .mm-09__trigger {
    position: relative;
  }

  .mm-09__item:hover > .mm-09__trigger::after,
    .mm-09__item:focus-within > .mm-09__trigger::after {
    content: "";
    position: absolute;
    inset-inline: 0;
    inset-block-start: 100%;
    block-size: 16px;
  }
}
/* Entry signature — rows switch on staccato with no fade, then the feature block glides up */

.mm-09__links li {
  opacity: 0;
  transition: opacity 1ms steps(1, end);
}

.mm-09__item:hover > .mm-09__panel .mm-09__links li,
.mm-09__item:focus-within > .mm-09__panel .mm-09__links li,
.mm-09__item--open > .mm-09__panel .mm-09__links li {
  opacity: 1;
}

.mm-09__links li:nth-child(1) {
  transition-delay: 30ms;
}

.mm-09__links li:nth-child(2) {
  transition-delay: 80ms;
}

.mm-09__links li:nth-child(3) {
  transition-delay: 130ms;
}

.mm-09__links li:nth-child(4) {
  transition-delay: 180ms;
}

.mm-09__links li:nth-child(5) {
  transition-delay: 230ms;
}

.mm-09__links li:nth-child(6) {
  transition-delay: 280ms;
}

.mm-09__links li:nth-child(n+7) {
  transition-delay: 280ms;
}

.mm-09__feature {
  opacity: 0;
  translate: 0 10px;
  transition: opacity 260ms ease 240ms, translate 340ms cubic-bezier(0.22, 1, 0.36, 1) 240ms;
}

.mm-09__item:hover > .mm-09__panel .mm-09__feature,
.mm-09__item:focus-within > .mm-09__panel .mm-09__feature,
.mm-09__item--open > .mm-09__panel .mm-09__feature {
  opacity: 1;
  translate: 0 0;
}

@media (prefers-reduced-motion: reduce) {
  .mm-09__links li,
    .mm-09__feature {
    transition-duration: 1ms;
    transition-delay: 0s;
    animation: none;
  }

  .mm-09__links li {
    opacity: 1;
  }

  .mm-09__feature {
    opacity: 1;
    translate: none;
  }
}
```
