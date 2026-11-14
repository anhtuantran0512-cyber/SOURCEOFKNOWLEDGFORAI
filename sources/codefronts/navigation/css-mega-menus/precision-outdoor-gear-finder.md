---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mega-menus/precision-outdoor-gear-finder/"
title: "Product Finder Mega Menu with Filters"
section: "navigation"
category: "css-mega-menus"
category_name: "CSS Mega Menus"
description: "A panel containing controls rather than only links."
has_js: "true"
---

Here's a working CSS Mega Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Product Finder Mega Menu with Filters
Source: https://codefronts.com/navigation/css-mega-menus/precision-outdoor-gear-finder/

A panel containing controls rather than only links. The interaction trap is specific: a control inside a hover-opened panel must not close it, and real inputs need the panel to stay open on click, on drag and while a keyboard user moves between fields. Built with genuine <input> elements, no surrounding form, and a live result count.
## HTML
```html
<section class="mm-19" aria-labelledby="mm-19-title">
  <h2 class="mm-19__sr" id="mm-19-title">Ranger Outfitters</h2>

  <div class="mm-19__theme">
    <input class="mm-19__theme-input" type="checkbox" id="mm-19-theme">
    <label class="mm-19__theme-label" for="mm-19-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="mm-19__sr">Toggle dark theme</span>
    </label>
  </div>

  <header class="mm-19__header">
    <div class="mm-19__bar">
      <a class="mm-19__brand" href="#mm-19-title">RANGER<span>outfitters</span></a>

      <nav class="mm-19__nav" aria-label="Primary">
        <ul class="mm-19__list">
          <li class="mm-19__item">
            <button class="mm-19__trigger" type="button" id="mm-19-trigger-find" aria-expanded="false" aria-controls="mm-19-panel-find">Find your kit</button>
            <div class="mm-19__panel" id="mm-19-panel-find" aria-labelledby="mm-19-trigger-find">
              <div class="mm-19__facets">
                <fieldset class="mm-19__facet">
                  <legend class="mm-19__legend">Activity</legend>
                  <label class="mm-19__opt"><input type="checkbox" data-mm-19-filter checked> Trail running</label>
                  <label class="mm-19__opt"><input type="checkbox" data-mm-19-filter> Alpine</label>
                  <label class="mm-19__opt"><input type="checkbox" data-mm-19-filter> Bikepacking</label>
                  <label class="mm-19__opt"><input type="checkbox" data-mm-19-filter> Sea kayak</label>
                </fieldset>

                <fieldset class="mm-19__facet">
                  <legend class="mm-19__legend">Season</legend>
                  <label class="mm-19__opt"><input type="checkbox" data-mm-19-filter> Three season</label>
                  <label class="mm-19__opt"><input type="checkbox" data-mm-19-filter checked> Winter</label>
                  <label class="mm-19__opt"><input type="checkbox" data-mm-19-filter> Expedition</label>
                </fieldset>

                <fieldset class="mm-19__facet">
                  <legend class="mm-19__legend">Weight class</legend>
                  <label class="mm-19__opt"><input type="checkbox" data-mm-19-filter> Ultralight</label>
                  <label class="mm-19__opt"><input type="checkbox" data-mm-19-filter> Standard</label>
                  <label class="mm-19__opt"><input type="checkbox" data-mm-19-filter> Heavy duty</label>
                </fieldset>

                <fieldset class="mm-19__facet">
                  <legend class="mm-19__legend">Budget ceiling</legend>
                  <label class="mm-19__range" for="mm-19-price">up to <b data-mm-19-price>&pound;420</b></label>
                  <input class="mm-19__slider" type="range" id="mm-19-price" min="80" max="900" step="20" value="420" data-mm-19-filter>
                  <p class="mm-19__hint">Includes 2-year repair cover on every item.</p>
                </fieldset>
              </div>

              <div class="mm-19__result">
                <p class="mm-19__count" role="status" aria-live="polite"><b data-mm-19-count>168</b> products match</p>
                <button class="mm-19__go" type="button">See results</button>
                <ul class="mm-19__shortcuts">
                  <li><a href="#mm-19-title">Best sellers</a></li>
                  <li><a href="#mm-19-title">Field-tested picks</a></li>
                  <li><a href="#mm-19-title">Clearance</a></li>
                </ul>
              </div>
            </div>
          </li>

          <li class="mm-19__item"><a class="mm-19__plain" href="#mm-19-title">Repairs</a></li>
          <li class="mm-19__item"><a class="mm-19__plain" href="#mm-19-title">Guides</a></li>
          <li class="mm-19__item"><a class="mm-19__plain" href="#mm-19-title">Hire</a></li>
        </ul>
      </nav>

      <div class="mm-19__utils">
        <a class="mm-19__util" href="#mm-19-title">Stores</a>
        <a class="mm-19__bag" href="#mm-19-title">Bag &middot; 3</a>
      </div>
    </div>
  </header>

  <main class="mm-19__page">
    <div class="mm-19__hero">
      <p class="mm-19__kicker">Field tested in the Cairngorms since 1988</p>
      <h1 class="mm-19__h1">Kit that comes back.</h1>
      <p class="mm-19__sub">Every item repairable, every repair costed up front.</p>
    </div>
  </main>
</section>
```
## CSS
```css
.mm-19 {
  --mm-19-bg: #eceef0;
  --mm-19-surf: #ffffff;
  --mm-19-line: #c9ced4;
  --mm-19-ink: #16191c;
  --mm-19-mut: #5d656d;
  --mm-19-accent: #b34103;
  --mm-19-accent: oklch(50% 0.18 45);
  --mm-19-on-accent: #ffffff;
  --mm-19-panel-w: 58rem;
  --mm-19-font-display: "Roboto Slab", "Rockwell", ui-serif, Georgia, serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mm-19-bg);
  color: var(--mm-19-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
  accent-color: var(--mm-19-accent);
}

.mm-19 *,
.mm-19 *::before,
.mm-19 *::after {
  box-sizing: border-box;
}

.mm-19 :focus-visible {
  outline: 2px solid var(--mm-19-accent);
  outline-offset: 3px;
}

.mm-19__sr {
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

.mm-19:has(.mm-19__theme-input:checked) {
  --mm-19-bg: #0c0e10;
  --mm-19-surf: #15181b;
  --mm-19-line: #282d32;
  --mm-19-ink: #eef1f3;
  --mm-19-mut: #9aa3ab;
  --mm-19-accent: #ff8a4c;
  --mm-19-accent: oklch(76% 0.16 50);
  --mm-19-on-accent: #12100e;
}

@media (prefers-color-scheme: dark) {
  .mm-19 {
    --mm-19-bg: #0c0e10;
    --mm-19-surf: #15181b;
    --mm-19-line: #282d32;
    --mm-19-ink: #eef1f3;
    --mm-19-mut: #9aa3ab;
    --mm-19-accent: #ff8a4c;
    --mm-19-accent: oklch(76% 0.16 50);
    --mm-19-on-accent: #12100e;
  }

  .mm-19:has(.mm-19__theme-input:checked) {
    --mm-19-bg: #eceef0;
    --mm-19-surf: #ffffff;
    --mm-19-line: #c9ced4;
    --mm-19-ink: #16191c;
    --mm-19-mut: #5d656d;
    --mm-19-accent: #b34103;
    --mm-19-accent: oklch(50% 0.18 45);
    --mm-19-on-accent: #ffffff;
  }
}

@media (prefers-color-scheme: light) {
  .mm-19:has(.mm-19__theme-input:checked) {
    --mm-19-bg: #0c0e10;
    --mm-19-surf: #15181b;
    --mm-19-line: #282d32;
    --mm-19-ink: #eef1f3;
    --mm-19-mut: #9aa3ab;
    --mm-19-accent: #ff8a4c;
    --mm-19-accent: oklch(76% 0.16 50);
    --mm-19-on-accent: #12100e;
  }
}

.mm-19__theme {
  position: absolute;
  inset-block-start: 12px;
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 60;
}

.mm-19__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.mm-19__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mm-19-line);
  border-radius: 6px;
  background: var(--mm-19-surf);
  color: var(--mm-19-ink);
  cursor: pointer;
}

.mm-19__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-19__theme-input:focus-visible + .mm-19__theme-label {
  outline: 2px solid var(--mm-19-accent);
  outline-offset: 3px;
}

.mm-19__header {
  position: relative;
  z-index: 10;
  inline-size: 100%;
  background: var(--mm-19-surf);
  border-block-end: 1px solid var(--mm-19-line);
}

.mm-19__bar {
  inline-size: min(76rem, calc(100% - 2rem));
  margin-inline: auto;
  display: flex;
  align-items: center;
  gap: clamp(0.5rem, 2vw, 2rem);
  flex-wrap: wrap;
  min-block-size: 68px;
  padding-inline-end: 60px;
}

.mm-19__brand {
  color: var(--mm-19-ink);
  text-decoration: none;
  font: 700 1rem/1 var(--mm-19-font-display);
  letter-spacing: 0.06em;
}

.mm-19__brand span {
  display: block;
  font: 400 0.6rem/1.2 system-ui, sans-serif;
  letter-spacing: 0.26em;
  text-transform: uppercase;
  color: var(--mm-19-mut);
}

.mm-19__nav {
  min-inline-size: 0;
}

.mm-19__list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.2rem;
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
}

.mm-19__item {
  position: static;
}

.mm-19__trigger,
.mm-19__plain {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.9rem;
  border: 0;
  background: transparent;
  color: var(--mm-19-ink);
  font: 600 0.9rem/1 system-ui, sans-serif;
  text-decoration: none;
  cursor: pointer;
}

.mm-19__item--open > .mm-19__trigger,
.mm-19__item:hover > .mm-19__trigger,
.mm-19__item:focus-within > .mm-19__trigger {
  background: var(--mm-19-accent);
  color: var(--mm-19-on-accent);
}

.mm-19__plain:hover,
.mm-19__trigger:hover {
  color: var(--mm-19-accent);
}

.mm-19__utils {
  margin-inline-start: auto;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.mm-19__util {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.6rem;
  color: var(--mm-19-mut);
  text-decoration: none;
  font: 600 0.85rem/1 system-ui, sans-serif;
}

.mm-19__bag {
  display: inline-flex;
  align-items: center;
  min-block-size: 38px;
  padding-inline: 0.9rem;
  border: 1px solid var(--mm-19-line);
  color: var(--mm-19-ink);
  text-decoration: none;
  font: 600 0.82rem/1 system-ui, sans-serif;
}
/* Bridge the 12px gap between the trigger and the panel with transparent
   padding, so the pointer never crosses dead space on its way in. Without
   it, pointerleave fires on the item mid-travel and the panel closes before
   the cursor arrives — WCAG SC 1.4.13 requires hover content to be
   hoverable. background-clip keeps the padding transparent. */

.mm-19__panel {
  position: absolute;
  padding-block-start: 16px;
  margin-block-start: -16px;
  background-clip: content-box;
  inset-inline-start: 50%;
  inset-block-start: 100%;
  z-index: 30;
  inline-size: min(var(--mm-19-panel-w), calc(100vw - 2rem));
  transform: translateX(-50%);
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  border: 1px solid var(--mm-19-line);
  border-block-start: 0;
  background: var(--mm-19-surf);
  box-shadow: 0 24px 56px -30px rgba(22, 25, 28, 0.6);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 160ms ease, visibility 0s linear 160ms;
}

@media (min-width: 62rem) {
  .mm-19__panel {
    grid-template-columns: minmax(0, 1fr) 17rem;
  }
}

.mm-19__item--open > .mm-19__panel,
.mm-19__item:focus-within > .mm-19__panel {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transition-delay: 0s;
}

@media (hover: hover) {
  .mm-19__item:hover > .mm-19__panel {
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    transition-delay: 0s;
  }
}

.mm-19__facets {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 11rem), 1fr));
  gap: clamp(0.75rem, 2.4vw, 1.5rem);
  padding: clamp(0.9rem, 2.6vw, 1.4rem);
  min-inline-size: 0;
}

.mm-19__facet {
  min-inline-size: 0;
  margin: 0;
  padding: 0;
  border: 0;
  display: grid;
  gap: 2px;
  align-content: start;
}

.mm-19__legend {
  padding: 0 0 0.35rem;
  font: 700 0.68rem/1 var(--mm-19-font-display);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--mm-19-mut);
}

.mm-19__opt {
  display: flex;
  align-items: center;
  gap: 0.55rem;
  min-block-size: 44px;
  font-size: 0.88rem;
  cursor: pointer;
  min-inline-size: 0;
}

.mm-19__opt input {
  inline-size: 18px;
  block-size: 18px;
  flex: none;
}

.mm-19__range {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  min-block-size: 32px;
  font-size: 0.85rem;
  color: var(--mm-19-mut);
}

.mm-19__range b {
  color: var(--mm-19-accent);
  font-variant-numeric: tabular-nums;
  font-size: 0.95rem;
}

.mm-19__slider {
  inline-size: 100%;
  min-block-size: 44px;
}

.mm-19__hint {
  margin: 0;
  font-size: 0.74rem;
  color: var(--mm-19-mut);
  text-wrap: pretty;
}

.mm-19__result {
  display: grid;
  align-content: start;
  gap: 0.6rem;
  padding: clamp(0.9rem, 2.6vw, 1.4rem);
  background: color-mix(in oklab, var(--mm-19-accent) 8%, transparent);
  border-inline-start: 1px solid var(--mm-19-line);
  min-inline-size: 0;
}

.mm-19__count {
  margin: 0;
  font-size: 0.88rem;
  color: var(--mm-19-mut);
}

.mm-19__count b {
  display: block;
  font: 700 clamp(1.6rem, 5vw, 2.2rem)/1 var(--mm-19-font-display);
  color: var(--mm-19-ink);
  font-variant-numeric: tabular-nums;
}

.mm-19__go {
  min-block-size: 44px;
  padding-inline: 1.1rem;
  border: 0;
  background: var(--mm-19-accent);
  color: var(--mm-19-on-accent);
  font: 700 0.85rem/1 system-ui, sans-serif;
  cursor: pointer;
}

.mm-19__shortcuts {
  list-style: none;
  margin: 0.25rem 0 0;
  padding: 0.6rem 0 0;
  border-block-start: 1px solid var(--mm-19-line);
  display: grid;
  gap: 1px;
}

.mm-19__shortcuts a {
  display: flex;
  align-items: center;
  min-block-size: 44px;
  color: var(--mm-19-ink);
  text-decoration: none;
  font-size: 0.86rem;
}

.mm-19__shortcuts a:hover {
  color: color-mix(in oklab, var(--mm-19-accent) 72%, var(--mm-19-ink));
}

.mm-19__page {
  inline-size: min(76rem, calc(100% - 2rem));
  margin-inline: auto;
  padding-block: clamp(3rem, 9vw, 5.5rem);
}

.mm-19__hero {
  max-inline-size: 34rem;
  display: grid;
  gap: 0.5rem;
}

.mm-19__kicker {
  margin: 0;
  font: 600 0.7rem/1 var(--mm-19-font-display);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--mm-19-accent);
}

.mm-19__h1 {
  margin: 0;
  font: 700 clamp(2.2rem, 7vw, 4rem)/1 var(--mm-19-font-display);
  letter-spacing: -0.03em;
}

.mm-19__sub {
  margin: 0;
  color: var(--mm-19-mut);
  font-size: clamp(0.95rem, 2.3vw, 1.1rem);
  text-wrap: pretty;
}

@media (max-width: 54rem) {
  .mm-19__bar {
    flex-direction: column;
    align-items: stretch;
    padding-block: 0.6rem;
  }

  .mm-19__list {
    flex-direction: column;
  }

  .mm-19__utils {
    margin-inline-start: 0;
  }

  .mm-19__panel {
    position: static;
    inline-size: 100%;
    transform: none;
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    box-shadow: none;
    display: none;
    border-block-start: 1px solid var(--mm-19-line);
  }

  .mm-19__item--open > .mm-19__panel,
    .mm-19__item:focus-within > .mm-19__panel {
    display: grid;
  }

  .mm-19__result {
    border-inline-start: 0;
    border-block-start: 1px solid var(--mm-19-line);
  }
}

@media (prefers-reduced-motion: reduce) {
  .mm-19__panel {
    transition-duration: 1ms;
  }
}

@media (hover: hover) and (pointer: fine) {
  .mm-19__trigger {
    position: relative;
  }

  .mm-19__item:hover > .mm-19__trigger::after,
    .mm-19__item:focus-within > .mm-19__trigger::after {
    content: "";
    position: absolute;
    inset-inline: 0;
    inset-block-start: 100%;
    block-size: 16px;
  }
}
/* Entry signature — two-tier open: panel regions rise, then filter chips scale in from their leading edge */

.mm-19__panel > * {
  opacity: 0;
  translate: 0 10px;
  transition: opacity 200ms ease, translate 340ms cubic-bezier(0.22, 1, 0.36, 1);
}

.mm-19__item:hover > .mm-19__panel > *,
.mm-19__item:focus-within > .mm-19__panel > *,
.mm-19__item--open > .mm-19__panel > * {
  opacity: 1;
  translate: 0 0;
}

.mm-19__panel > *:nth-child(1) {
  transition-delay: 20ms;
}

.mm-19__panel > *:nth-child(2) {
  transition-delay: 90ms;
}

.mm-19__panel > *:nth-child(3) {
  transition-delay: 160ms;
}

.mm-19__panel > *:nth-child(n+4) {
  transition-delay: 160ms;
}

.mm-19__sub li {
  opacity: 0;
  scale: 0.95;
  transform-origin: 0 50%;
  transition: opacity 220ms ease, scale 320ms cubic-bezier(0.22, 1, 0.36, 1);
}

.mm-19__item:hover > .mm-19__panel .mm-19__sub li,
.mm-19__item:focus-within > .mm-19__panel .mm-19__sub li,
.mm-19__item--open > .mm-19__panel .mm-19__sub li {
  opacity: 1;
  scale: 1;
}

.mm-19__sub li:nth-child(1) {
  transition-delay: 140ms;
}

.mm-19__sub li:nth-child(2) {
  transition-delay: 180ms;
}

.mm-19__sub li:nth-child(3) {
  transition-delay: 220ms;
}

.mm-19__sub li:nth-child(4) {
  transition-delay: 260ms;
}

.mm-19__sub li:nth-child(5) {
  transition-delay: 300ms;
}

.mm-19__sub li:nth-child(6) {
  transition-delay: 340ms;
}

.mm-19__sub li:nth-child(n+7) {
  transition-delay: 340ms;
}

@media (prefers-reduced-motion: reduce) {
  .mm-19__panel > *,
    .mm-19__sub li {
    transition-duration: 1ms;
    transition-delay: 0s;
    animation: none;
  }

  .mm-19__panel > * {
    opacity: 1;
    translate: none;
  }

  .mm-19__sub li {
    opacity: 1;
    scale: 1;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.mm-19');
const item = root.querySelector('.mm-19__item');
const panel = root.querySelector('.mm-19__panel');
const trigger = root.querySelector('.mm-19__trigger');
const countEl = root.querySelector('[data-mm-19-count]');
const priceEl = root.querySelector('[data-mm-19-price]');
const slider = root.querySelector('.mm-19__slider');
const boxes = Array.from(root.querySelectorAll('input[type="checkbox"][data-mm-19-filter]'));

const recount = () => {
  const picked = boxes.filter((b) => b.checked).length;
  const ceiling = Number(slider.value);
  const total = Math.max(6, Math.round((420 - picked * 62) * (ceiling / 420)));
  if (countEl) countEl.textContent = String(total);
  if (priceEl) priceEl.textContent = '£' + ceiling;
};

const setOpen = (on) => { item.classList.toggle('mm-19__item--open', on); trigger.setAttribute('aria-expanded', String(on)); };

const onInput = (e) => { if (e.target.matches('[data-mm-19-filter]')) recount(); };
const onClick = (e) => { if (e.target.closest('.mm-19__trigger')) setOpen(!item.classList.contains('mm-19__item--open')); };
const onDocClick = (e) => { if (!item.contains(e.target)) setOpen(false); };
const onKey = (e) => { if (e.key === 'Escape') { setOpen(false); trigger.focus(); } };
const onFocusOut = (e) => { if (!e.relatedTarget || !item.contains(e.relatedTarget)) setOpen(false); };

panel.addEventListener('input', onInput);
root.addEventListener('click', onClick);
document.addEventListener('click', onDocClick);
item.addEventListener('keydown', onKey);
item.addEventListener('focusout', onFocusOut);
recount();

root.__mmCleanup = () => {
  panel.removeEventListener('input', onInput);
  root.removeEventListener('click', onClick);
  document.removeEventListener('click', onDocClick);
  item.removeEventListener('keydown', onKey);
  item.removeEventListener('focusout', onFocusOut);
};
```
