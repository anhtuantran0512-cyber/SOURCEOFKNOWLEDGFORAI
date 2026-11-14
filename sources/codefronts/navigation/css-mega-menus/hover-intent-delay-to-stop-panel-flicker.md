---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mega-menus/hover-intent-delay-to-stop-panel-flicker/"
title: "Hover Intent Delay to Stop Panel Flicker"
section: "navigation"
category: "css-mega-menus"
category_name: "CSS Mega Menus"
description: "Opening on raw mouseenter means a pointer crossing the bar to reach something else fires three panels in sequence."
has_js: "true"
---

Here's a working CSS Mega Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hover Intent Delay to Stop Panel Flicker
Source: https://codefronts.com/navigation/css-mega-menus/hover-intent-delay-to-stop-panel-flicker/

Opening on raw mouseenter means a pointer crossing the bar to reach something else fires three panels in sequence. This airline header ships the fix: a 120ms open delay that cancels if the pointer leaves, and a 250ms close delay so a brief slip does not dismiss an open panel. Drag the pointer straight across the bar and only the item you stop on opens.
## HTML
```html
<section class="mm-02" aria-labelledby="mm-02-title">
  <h2 class="mm-02__sr" id="mm-02-title">Orbit Air</h2>

  <div class="mm-02__theme">
    <input class="mm-02__theme-input" type="checkbox" id="mm-02-theme">
    <label class="mm-02__theme-label" for="mm-02-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="mm-02__sr">Toggle dark theme</span>
    </label>
  </div>

  <header class="mm-02__header">
    <div class="mm-02__strip">
      <span>Orbit Club</span>
      <span>English &middot; GBP</span>
      <a href="#mm-02-title">Flight status</a>
    </div>

    <div class="mm-02__bar">
      <a class="mm-02__brand" href="#mm-02-title">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M2.5 13.5 21 5l-5 9.5 1.5 5.5-4-3.5-4 2 .5-4Z" fill="currentColor"/></svg>
        Orbit Air
      </a>

      <nav class="mm-02__nav" aria-label="Primary" data-mm02-open="120" data-mm02-close="250">
        <ul class="mm-02__list">
          <li class="mm-02__item">
            <button class="mm-02__trigger" type="button" aria-expanded="false" aria-controls="mm-02-panel-book">Book</button>
            <div class="mm-02__panel" id="mm-02-panel-book" aria-label="Book">
              <div class="mm-02__panel-inner">
                <ul class="mm-02__cards">
                  <li><a href="#mm-02-title"><span class="mm-02__card-k">Return</span><b>Flights</b><span class="mm-02__card-m">Economy to Business</span></a></li>
                  <li><a href="#mm-02-title"><span class="mm-02__card-k">Bundle</span><b>Flight and hotel</b><span class="mm-02__card-m">Save up to 18%</span></a></li>
                  <li><a href="#mm-02-title"><span class="mm-02__card-k">Group</span><b>10+ travellers</b><span class="mm-02__card-m">Held fares</span></a></li>
                </ul>
                <div class="mm-02__aside">
                  <p class="mm-02__aside-head">Quick actions</p>
                  <ul class="mm-02__aside-links">
                    <li><a href="#mm-02-title">Manage a booking</a></li>
                    <li><a href="#mm-02-title">Check in</a></li>
                    <li><a href="#mm-02-title">Add extra bags</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </li>

          <li class="mm-02__item">
            <button class="mm-02__trigger" type="button" aria-expanded="false" aria-controls="mm-02-panel-where">Destinations</button>
            <div class="mm-02__panel" id="mm-02-panel-where" aria-label="Destinations">
              <div class="mm-02__panel-inner">
                <div class="mm-02__routes">
                  <p class="mm-02__routes-head">From London &middot; direct</p>
                  <ul class="mm-02__fares">
                    <li><a href="#mm-02-title"><span class="mm-02__iata">LIS</span><b>Lisbon</b><span class="mm-02__time">2h 45m</span><span class="mm-02__price">&pound;68</span></a></li>
                    <li><a href="#mm-02-title"><span class="mm-02__iata">KEF</span><b>Reykjavik</b><span class="mm-02__time">3h 05m</span><span class="mm-02__price">&pound;94</span></a></li>
                    <li><a href="#mm-02-title"><span class="mm-02__iata">ATH</span><b>Athens</b><span class="mm-02__time">3h 50m</span><span class="mm-02__price">&pound;112</span></a></li>
                    <li><a href="#mm-02-title"><span class="mm-02__iata">TLL</span><b>Tallinn</b><span class="mm-02__time">2h 55m</span><span class="mm-02__price">&pound;79</span></a></li>
                    <li><a href="#mm-02-title"><span class="mm-02__iata">JFK</span><b>New York</b><span class="mm-02__time">7h 40m</span><span class="mm-02__price">&pound;322</span></a></li>
                    <li><a href="#mm-02-title"><span class="mm-02__iata">YYZ</span><b>Toronto</b><span class="mm-02__time">7h 55m</span><span class="mm-02__price">&pound;348</span></a></li>
                  </ul>
                </div>
                <div class="mm-02__aside">
                  <p class="mm-02__aside-head">Browse</p>
                  <ul class="mm-02__aside-links">
                    <li><a href="#mm-02-title">Route map</a></li>
                    <li><a href="#mm-02-title">Seasonal routes</a></li>
                    <li><a href="#mm-02-title">Where can I fly?</a></li>
                  </ul>
                  <a class="mm-02__aside-cta" href="#mm-02-title">Open the fare finder</a>
                </div>
              </div>
            </div>
          </li>

          <li class="mm-02__item">
            <button class="mm-02__trigger" type="button" aria-expanded="false" aria-controls="mm-02-panel-onboard">Onboard</button>
            <div class="mm-02__panel" id="mm-02-panel-onboard" aria-label="Onboard">
              <div class="mm-02__panel-inner">
                <ul class="mm-02__cards">
                  <li><a href="#mm-02-title"><span class="mm-02__card-k">Cabins</span><b>Seats and space</b><span class="mm-02__card-m">Pitch and recline</span></a></li>
                  <li><a href="#mm-02-title"><span class="mm-02__card-k">Service</span><b>Food and drink</b><span class="mm-02__card-m">Pre-order to save</span></a></li>
                  <li><a href="#mm-02-title"><span class="mm-02__card-k">Wi-Fi</span><b>Stay connected</b><span class="mm-02__card-m">Free for Club</span></a></li>
                </ul>
                <div class="mm-02__aside">
                  <p class="mm-02__aside-head">Before you fly</p>
                  <ul class="mm-02__aside-links">
                    <li><a href="#mm-02-title">Baggage rules</a></li>
                    <li><a href="#mm-02-title">Special assistance</a></li>
                    <li><a href="#mm-02-title">Travelling with pets</a></li>
                  </ul>
                </div>
              </div>
            </div>
          </li>

          <li class="mm-02__item"><a class="mm-02__plain" href="#mm-02-title">Help</a></li>
        </ul>
      </nav>

      <div class="mm-02__utils">
        <a class="mm-02__signin" href="#mm-02-title">Sign in</a>
        <a class="mm-02__cta" href="#mm-02-title">Check in</a>
      </div>
    </div>
  </header>

  <main class="mm-02__page">
    <div class="mm-02__hero">
      <p class="mm-02__eyebrow">Winter timetable now open</p>
      <h1 class="mm-02__title">Twelve new direct routes from London.</h1>
      <div class="mm-02__search" role="group" aria-label="Search flights">
        <div class="mm-02__field"><span>From</span><b>London LHR</b></div>
        <div class="mm-02__field"><span>To</span><b>Anywhere</b></div>
        <div class="mm-02__field"><span>Depart</span><b>12 Nov</b></div>
        <div class="mm-02__field"><span>Travellers</span><b>1 adult</b></div>
        <a class="mm-02__cta mm-02__cta--lg" href="#mm-02-title">Search fares</a>
      </div>
    </div>
  </main>
</section>
```
## CSS
```css
.mm-02 {
  --mm-02-chrome: #0f1a2e;
  --mm-02-panel: #0b1424;
  --mm-02-line: #23324c;
  --mm-02-ink: #e8eef7;
  --mm-02-mut: #93a3bd;
  --mm-02-acc: #7ea6ff;
  --mm-02-acc: oklch(76% 0.14 262);
  --mm-02-warm: #ffb454;
  --mm-02-warm: oklch(80% 0.14 70);
  --mm-02-bg: #e9edf4;
  --mm-02-page-ink: #0d1b33;
  --mm-02-page-mut: #5b6b85;
  --mm-02-card: #ffffff;
  --mm-02-lift: 8px;
  --mm-02-font-display: "Archivo Narrow", "Roboto Condensed", ui-sans-serif, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background-color: var(--mm-02-bg);
  background-image: radial-gradient(72rem 34rem at 12% -14%, rgba(126, 166, 255, 0.2), transparent 62%), radial-gradient(50rem 26rem at 96% 6%, rgba(255, 180, 84, 0.16), transparent 60%);
  color: var(--mm-02-page-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.mm-02 *,
.mm-02 *::before,
.mm-02 *::after {
  box-sizing: border-box;
}

.mm-02 :focus-visible {
  outline: 2px solid var(--mm-02-acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.mm-02__sr {
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

.mm-02:has(.mm-02__theme-input:checked) {
  --mm-02-bg: #070c15;
  --mm-02-page-ink: #e8eef7;
  --mm-02-page-mut: #93a3bd;
  --mm-02-chrome: #0c1424;
  --mm-02-panel: #090f1c;
  --mm-02-card: #101a2c;
}

@media (prefers-color-scheme: dark) {
  .mm-02 {
    --mm-02-bg: #070c15;
    --mm-02-page-ink: #e8eef7;
    --mm-02-page-mut: #93a3bd;
    --mm-02-chrome: #0c1424;
    --mm-02-panel: #090f1c;
    --mm-02-card: #101a2c;
  }

  .mm-02:has(.mm-02__theme-input:checked) {
    --mm-02-bg: #e9edf4;
    --mm-02-page-ink: #0d1b33;
    --mm-02-page-mut: #5b6b85;
    --mm-02-chrome: #0f1a2e;
    --mm-02-panel: #0b1424;
    --mm-02-card: #ffffff;
  }
}

@media (prefers-color-scheme: light) {
  .mm-02:has(.mm-02__theme-input:checked) {
    --mm-02-bg: #070c15;
    --mm-02-page-ink: #e8eef7;
    --mm-02-page-mut: #93a3bd;
    --mm-02-chrome: #0c1424;
    --mm-02-panel: #090f1c;
    --mm-02-card: #101a2c;
  }
}

.mm-02__theme {
  position: absolute;
  inset-block-start: 42px;
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 60;
}

.mm-02__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.mm-02__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mm-02-line);
  border-radius: 999px;
  background: var(--mm-02-chrome);
  color: var(--mm-02-ink);
  cursor: pointer;
}

.mm-02__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-02__theme-input:focus-visible + .mm-02__theme-label {
  outline: 2px solid var(--mm-02-acc);
  outline-offset: 3px;
}

.mm-02__header {
  position: relative;
  z-index: 10;
  inline-size: 100%;
  background: var(--mm-02-chrome);
  color: var(--mm-02-ink);
}

.mm-02__strip {
  inline-size: min(82rem, calc(100% - 2rem));
  margin-inline: auto;
  display: flex;
  align-items: center;
  gap: 1.25rem;
  flex-wrap: wrap;
  min-block-size: 34px;
  font: 500 0.72rem/1 system-ui, sans-serif;
  letter-spacing: 0.04em;
  color: var(--mm-02-mut);
  border-block-end: 1px solid var(--mm-02-line);
}

.mm-02__strip a {
  margin-inline-start: auto;
  color: var(--mm-02-warm);
  text-decoration: none;
}

.mm-02__bar {
  inline-size: min(82rem, calc(100% - 2rem));
  margin-inline: auto;
  display: flex;
  align-items: center;
  gap: clamp(0.5rem, 2vw, 2rem);
  flex-wrap: wrap;
  min-block-size: 68px;
  padding-inline-end: 60px;
}

.mm-02__brand {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--mm-02-ink);
  text-decoration: none;
  font: 700 1.1rem/1 var(--mm-02-font-display);
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.mm-02__brand svg {
  inline-size: 24px;
  block-size: 24px;
  color: var(--mm-02-warm);
}

.mm-02__nav {
  min-inline-size: 0;
}

.mm-02__list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.15rem;
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
}

.mm-02__item {
  position: static;
}

.mm-02__trigger,
.mm-02__plain {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.9rem;
  border: 0;
  background: transparent;
  color: var(--mm-02-ink);
  font: 600 0.9rem/1 var(--mm-02-font-display);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  text-decoration: none;
  cursor: pointer;
}

.mm-02__trigger[aria-expanded="true"],
.mm-02__item--open > .mm-02__trigger,
.mm-02__item:hover > .mm-02__trigger,
.mm-02__item:focus-within > .mm-02__trigger {
  color: var(--mm-02-warm);
  box-shadow: inset 0 -3px 0 var(--mm-02-warm);
}

.mm-02__plain:hover,
.mm-02__trigger:hover {
  color: var(--mm-02-warm);
}

.mm-02__utils {
  margin-inline-start: auto;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.mm-02__signin {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.7rem;
  color: var(--mm-02-mut);
  text-decoration: none;
  font: 600 0.85rem/1 system-ui, sans-serif;
}

.mm-02__cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 1.1rem;
  border-radius: 999px;
  background: var(--mm-02-warm);
  color: #241503;
  text-decoration: none;
  font: 700 0.85rem/1 system-ui, sans-serif;
}

.mm-02__panel {
  position: absolute;
  inset-inline: 0;
  inset-block-start: 100%;
  z-index: 30;
  background: var(--mm-02-panel);
  border-block-end: 3px solid var(--mm-02-warm);
  box-shadow: 0 30px 60px -36px rgba(0, 0, 0, 0.75);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: translateY(calc(var(--mm-02-lift) * -1));
  transition: opacity 150ms ease, transform 150ms ease, visibility 0s linear 150ms;
}

.mm-02__item--open > .mm-02__panel,
.mm-02__item:focus-within > .mm-02__panel {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transform: translateY(0);
  transition-delay: 0s;
}

.mm-02__panel-inner {
  inline-size: min(82rem, calc(100% - 2rem));
  margin-inline: auto;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: clamp(0.9rem, 2.6vw, 2rem);
  padding-block: clamp(1.1rem, 3vw, 1.75rem);
}

@media (min-width: 62rem) {
  .mm-02__panel-inner {
    grid-template-columns: minmax(0, 1fr) 15rem;
  }
}

.mm-02__routes {
  min-inline-size: 0;
}

.mm-02__routes-head {
  margin: 0 0 0.5rem;
  font: 600 0.68rem/1 var(--mm-02-font-display);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--mm-02-mut);
}

.mm-02__fares {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr));
  gap: 2px;
}

.mm-02__fares a {
  display: grid;
  grid-template-columns: 3.2rem minmax(0, 1fr) auto;
  align-items: center;
  column-gap: 0.75rem;
  min-block-size: 52px;
  padding: 0.35rem 0.6rem;
  border-radius: 8px;
  color: var(--mm-02-ink);
  text-decoration: none;
}

.mm-02__iata {
  grid-row: span 2;
  display: grid;
  place-items: center;
  inline-size: 3.2rem;
  block-size: 2.2rem;
  border-radius: 6px;
  background: color-mix(in oklab, var(--mm-02-acc) 18%, transparent);
  color: var(--mm-02-acc);
  font: 700 0.82rem/1 var(--mm-02-font-display);
  letter-spacing: 0.08em;
}

.mm-02__fares b {
  font: 600 0.95rem/1.2 system-ui, sans-serif;
  min-inline-size: 0;
}

.mm-02__time {
  grid-column: 2;
  font: 400 0.74rem/1.2 system-ui, sans-serif;
  color: var(--mm-02-mut);
}

.mm-02__price {
  grid-column: 3;
  grid-row: span 2;
  font: 700 1rem/1 var(--mm-02-font-display);
  color: var(--mm-02-warm);
  font-variant-numeric: tabular-nums;
}

.mm-02__fares a:hover {
  background: color-mix(in oklab, var(--mm-02-acc) 12%, transparent);
}

.mm-02__cards {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 13rem), 1fr));
  gap: 0.6rem;
  min-inline-size: 0;
}

.mm-02__cards a {
  display: grid;
  align-content: start;
  gap: 2px;
  min-block-size: 92px;
  padding: 0.8rem 0.9rem;
  border: 1px solid var(--mm-02-line);
  border-radius: 10px;
  color: var(--mm-02-ink);
  text-decoration: none;
}

.mm-02__card-k {
  font: 700 0.62rem/1 var(--mm-02-font-display);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--mm-02-warm);
}

.mm-02__cards b {
  font: 600 0.98rem/1.2 system-ui, sans-serif;
}

.mm-02__card-m {
  font-size: 0.78rem;
  color: var(--mm-02-mut);
}

.mm-02__cards a:hover {
  border-color: var(--mm-02-warm);
}

.mm-02__aside {
  min-inline-size: 0;
  display: grid;
  align-content: start;
  gap: 0.2rem;
  padding: clamp(0.85rem, 2.2vw, 1.1rem);
  border-radius: 10px;
  background: color-mix(in oklab, var(--mm-02-acc) 12%, transparent);
}

.mm-02__aside-head {
  margin: 0 0 0.2rem;
  font: 700 0.64rem/1 var(--mm-02-font-display);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--mm-02-acc);
}

.mm-02__aside-links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1px;
}

.mm-02__aside-links a {
  display: flex;
  align-items: center;
  min-block-size: 44px;
  color: var(--mm-02-ink);
  text-decoration: none;
  font-size: 0.87rem;
}

.mm-02__aside-links a:hover {
  color: var(--mm-02-warm);
}

.mm-02__aside-cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  margin-block-start: 0.2rem;
  color: var(--mm-02-warm);
  font: 600 0.84rem/1 system-ui, sans-serif;
  text-decoration: none;
}

.mm-02__page {
  inline-size: min(82rem, calc(100% - 2rem));
  margin-inline: auto;
  padding-block: clamp(3rem, 9vw, 5.5rem);
}

.mm-02__hero {
  display: grid;
  gap: 1rem;
}

.mm-02__eyebrow {
  margin: 0;
  font: 600 0.72rem/1 var(--mm-02-font-display);
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: color-mix(in oklab, var(--mm-02-acc) 55%, var(--mm-02-page-ink));
}

.mm-02__title {
  margin: 0;
  max-inline-size: 22ch;
  color: var(--mm-02-page-ink);
  font: 700 clamp(2.1rem, 6.5vw, 4rem)/1.02 var(--mm-02-font-display);
  letter-spacing: -0.01em;
  text-wrap: balance;
}
/* Per-cell borders rather than a 1px gap revealing the container
   background: five fields never fill an auto-fit track count, so the
   bleed trick painted the empty cells as solid blocks. */

.mm-02__search {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 11rem), 1fr));
  gap: 0;
  margin-block-start: 0.6rem;
  background: transparent;
  border-radius: 14px;
  overflow: hidden;
}

.mm-02__field {
  border-inline-end: 1px solid color-mix(in oklab, var(--mm-02-page-ink) 12%, transparent);
  border-block-end: 1px solid color-mix(in oklab, var(--mm-02-page-ink) 12%, transparent);
  display: grid;
  gap: 2px;
  padding: 0.8rem 1rem;
  background: var(--mm-02-card);
  min-inline-size: 0;
}

.mm-02__field span {
  font: 600 0.64rem/1 var(--mm-02-font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--mm-02-page-mut);
}

.mm-02__field b {
  font: 600 1rem/1.2 system-ui, sans-serif;
  color: var(--mm-02-page-ink);
}

.mm-02__cta--lg {
  border-radius: 0;
  justify-content: center;
  min-block-size: 100%;
  padding-inline: 1.4rem;
  font-size: 0.95rem;
}

@media (max-width: 56rem) {
  .mm-02__bar {
    flex-direction: column;
    align-items: stretch;
    padding-block: 0.6rem;
  }

  .mm-02__list {
    flex-direction: column;
  }

  .mm-02__utils {
    margin-inline-start: 0;
  }

  .mm-02__panel {
    position: static;
    opacity: 1;
    visibility: visible;
    transform: none;
    box-shadow: none;
    display: none;
  }

  .mm-02__item--open > .mm-02__panel {
    display: block;
  }
  /* Keyboard fallback only. On touch the tapped trigger keeps focus, so a bare
       :focus-within here would override the JS toggle and the panel could never
       be tapped shut. Hover-capable devices are the ones that need it. */

  @media (hover: hover) {
    .mm-02__item:focus-within > .mm-02__panel {
      display: block;
    }
  }

  .mm-02__panel-inner {
    inline-size: 100%;
  }

  .mm-02__cta--lg {
    min-block-size: 52px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .mm-02__panel {
    transition-duration: 1ms;
  }
}

@media (hover: hover) and (pointer: fine) {
  .mm-02__trigger {
    position: relative;
  }

  .mm-02__item:hover > .mm-02__trigger::after,
    .mm-02__item:focus-within > .mm-02__trigger::after {
    content: "";
    position: absolute;
    inset-inline: 0;
    inset-block-start: 100%;
    block-size: 16px;
  }
}
/* Entry signature — cards spring up from their own baseline, aside slides in from the end edge */

.mm-02__panel-inner > * {
  opacity: 0;
  scale: 0.97;
  transform-origin: 50% 100%;
  transition: opacity 200ms ease, scale 380ms cubic-bezier(0.34, 1.45, 0.64, 1);
}

.mm-02__item:hover > .mm-02__panel .mm-02__panel-inner > *,
.mm-02__item:focus-within > .mm-02__panel .mm-02__panel-inner > *,
.mm-02__item--open > .mm-02__panel .mm-02__panel-inner > * {
  opacity: 1;
  scale: 1;
}

.mm-02__panel-inner > *:nth-child(1) {
  transition-delay: 30ms;
}

.mm-02__panel-inner > *:nth-child(2) {
  transition-delay: 120ms;
}

.mm-02__panel-inner > *:nth-child(3) {
  transition-delay: 210ms;
}

.mm-02__panel-inner > *:nth-child(4) {
  transition-delay: 300ms;
}

.mm-02__panel-inner > *:nth-child(n+5) {
  transition-delay: 300ms;
}

.mm-02__aside-links li {
  opacity: 0;
  translate: 14px 0;
  transition: opacity 200ms ease, translate 320ms cubic-bezier(0.22, 1, 0.36, 1);
}

.mm-02__item:hover > .mm-02__panel .mm-02__aside-links li,
.mm-02__item:focus-within > .mm-02__panel .mm-02__aside-links li,
.mm-02__item--open > .mm-02__panel .mm-02__aside-links li {
  opacity: 1;
  translate: 0 0;
}

.mm-02__aside-links li:nth-child(1) {
  transition-delay: 180ms;
}

.mm-02__aside-links li:nth-child(2) {
  transition-delay: 225ms;
}

.mm-02__aside-links li:nth-child(3) {
  transition-delay: 270ms;
}

.mm-02__aside-links li:nth-child(4) {
  transition-delay: 315ms;
}

.mm-02__aside-links li:nth-child(5) {
  transition-delay: 360ms;
}

.mm-02__aside-links li:nth-child(n+6) {
  transition-delay: 360ms;
}

@media (prefers-reduced-motion: reduce) {
  .mm-02__panel-inner > *,
    .mm-02__aside-links li {
    transition-duration: 1ms;
    transition-delay: 0s;
    animation: none;
  }

  .mm-02__panel-inner > * {
    opacity: 1;
    scale: 1;
  }

  .mm-02__aside-links li {
    opacity: 1;
    translate: none;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.mm-02');
const nav = root.querySelector('.mm-02__nav');
const openMs = Number(nav.dataset.mm02Open || 120);
const closeMs = Number(nav.dataset.mm02Close || 250);
const canHover = window.matchMedia('(hover: hover)');
let openT = 0, closeT = 0;

const setOpen = (item, on) => {
  item.classList.toggle('mm-02__item--open', on);
  item.querySelector('.mm-02__trigger').setAttribute('aria-expanded', String(on));
};
const closeAll = () => nav.querySelectorAll('.mm-02__item--open').forEach((i) => setOpen(i, false));

const onEnter = (e) => {
  const item = e.target.closest('.mm-02__item');
  if (!item || !item.querySelector('.mm-02__panel') || !canHover.matches) return;
  clearTimeout(closeT); clearTimeout(openT);
  openT = setTimeout(() => { closeAll(); setOpen(item, true); }, openMs);
};
const onLeave = (e) => {
  if (!canHover.matches) return;
  if (!e.target.closest('.mm-02__item')) return;
  clearTimeout(openT); openT = 0;
  clearTimeout(closeT);
  closeT = setTimeout(() => { if (!nav.contains(document.activeElement)) closeAll(); }, closeMs);
};
const onClick = (e) => {
  const trigger = e.target.closest('.mm-02__trigger');
  if (!trigger) return;
  const item = trigger.closest('.mm-02__item');
  const open = item.classList.contains('mm-02__item--open');
  clearTimeout(openT); clearTimeout(closeT);
  // Hover already opened this panel; a click must not close it again.
  if (open && canHover.matches) return;
  closeAll(); setOpen(item, !open);
};
const onKey = (e) => {
  if (e.key !== 'Escape') return;
  const open = nav.querySelector('.mm-02__item--open');
  if (!open) return;
  clearTimeout(openT); clearTimeout(closeT);
  setOpen(open, false); open.querySelector('.mm-02__trigger').focus();
};

nav.addEventListener('pointerenter', onEnter, true);
nav.addEventListener('pointerleave', onLeave, true);
nav.addEventListener('click', onClick);
nav.addEventListener('keydown', onKey);

root.__mmCleanup = () => {
  nav.removeEventListener('pointerenter', onEnter, true);
  nav.removeEventListener('pointerleave', onLeave, true);
  nav.removeEventListener('click', onClick);
  nav.removeEventListener('keydown', onKey);
  clearTimeout(openT); clearTimeout(closeT);
};
```
