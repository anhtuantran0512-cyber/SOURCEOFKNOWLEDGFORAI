---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/e-commerce-product-search-bar-with-category-scope-dropdown/"
title: "E-Commerce Product Search Bar with Category Scope Dropdown"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "The retailer pattern: a department <select> on the left, the query in the middle, a solid submit button on the right, all fused into one 48px bar inside a…"
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: E-Commerce Product Search Bar with Category Scope Dropdown
Source: https://codefronts.com/components/css-search-boxes/e-commerce-product-search-bar-with-category-scope-dropdown/

The retailer pattern: a department <select> on the left, the query in the middle, a solid submit button on the right, all fused into one 48px bar inside a mock storefront header. Trending suggestions open on :focus-within; the submit button spins for the round trip via a data-state flip.
## HTML
```html
<div class="sb-03">
  <button class="sb-03__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-03__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-03__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-03__stage">
    <header class="sb-03__header">
      <span class="sb-03__logo"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 7h16l-1.6 12.5H5.6z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M9 7a3 3 0 0 1 6 0" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>Northline</span>

      <div class="sb-03__searchcol">
        <div class="sb-03__bar" role="search">
          <span class="sb-03__scope">
            <label class="sb-03__vh" for="sb-03-cat">Search in department</label>
            <select class="sb-03__select" id="sb-03-cat">
              <option>All Departments</option>
              <option>Electronics</option>
              <option>Home &amp; Kitchen</option>
              <option>Audio &amp; Headphones</option>
              <option>Office</option>
            </select>
            <svg class="sb-03__chev" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m7 10 5 5 5-5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </span>

          <label class="sb-03__vh" for="sb-03-input">Search products</label>
          <input class="sb-03__input" id="sb-03-input" type="search" placeholder="Search wireless headphones, kettles, monitors&hellip;" autocomplete="off" aria-controls="sb-03-sug">

          <button class="sb-03__submit" id="sb-03-go" type="button" aria-label="Search">
            <svg class="sb-03__mag" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="2"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            <span class="sb-03__spin" aria-hidden="true"></span>
          </button>

          <div class="sb-03__sug" id="sb-03-sug">
            <p class="sb-03__sug-h">Trending in Audio</p>
            <ul class="sb-03__sug-list" role="listbox" aria-label="Trending searches">
              <li class="sb-03__sug-row" role="option" aria-selected="false"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 17.5 9.5 12l3.5 3.5L20 8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M15.5 8H20v4.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>wireless headphones<span class="sb-03__tag">412 items</span></li>
              <li class="sb-03__sug-row" role="option" aria-selected="false"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 17.5 9.5 12l3.5 3.5L20 8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M15.5 8H20v4.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>noise cancelling earbuds<span class="sb-03__tag">128 items</span></li>
              <li class="sb-03__sug-row" role="option" aria-selected="false"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 17.5 9.5 12l3.5 3.5L20 8" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M15.5 8H20v4.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>usb-c dock 4k<span class="sb-03__tag">64 items</span></li>
            </ul>
          </div>
        </div>
      </div>

      <div class="sb-03__actions">
        <button class="sb-03__iconbtn" type="button" aria-label="Your account">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="9" r="3.4" stroke="currentColor" stroke-width="1.7"/><path d="M5.5 19.5a6.5 6.5 0 0 1 13 0" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        </button>
        <button class="sb-03__iconbtn" type="button" aria-label="Basket, 3 items">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 7.5h15L18 19H6z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M9 7.5a3 3 0 0 1 6 0" stroke="currentColor" stroke-width="1.7"/></svg>
          <span class="sb-03__badge">3</span>
        </button>
      </div>
    </header>
  </div>
</div>
```
## CSS
```css
.sb-03 {
  --bg: #faf7f2;
  --card: #ffffff;
  --ink: #1c1917;
  --muted: #78716c;
  --line: #e3ddd3;
  --acc: #e2620f;
  --acc-ink: #ffffff;
  --wash: #fdf1e7;
  --ring: #1c1917;
  --shadow: rgba(28,25,23,.12);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: linear-gradient(180deg,#fffdf9 0%, var(--bg) 42%);
  -webkit-font-smoothing: antialiased;
}

.sb-03 *,
.sb-03 *::before,
.sb-03 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% .1 60)) {
  .sb-03 {
    --bg: oklch(97% .012 75);
    --ink: oklch(23% .015 60);
    --muted: oklch(55% .02 60);
    --line: oklch(90% .015 75);
    --acc: oklch(62% .17 47);
    --wash: color-mix(in oklab, oklch(62% .17 47) 10%, white);
  }
}

.sb-03__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-03__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-03__header {
  display: flex;
  align-items: center;
  gap: clamp(.8rem,2.5vw,1.75rem);
  inline-size: min(70rem,100%);
  padding: .9rem clamp(.9rem,2.5vw,1.4rem);
  border: 1px solid var(--line);
  border-radius: 18px;
  background: var(--card);
  box-shadow: 0 18px 40px -28px var(--shadow), 0 1px 2px rgba(28,25,23,.04);
}

@supports (container-type: inline-size) {
  .sb-03__header {
    container-type: inline-size;
  }

  @container (max-width: 34rem) {
    .sb-03__header {
      flex-wrap: wrap;
    }

    .sb-03__searchcol {
      order: 3;
      flex-basis: 100%;
    }
  }
}

.sb-03__logo {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  flex: none;
  font: 700 1.02rem/1 inherit;
  letter-spacing: -.02em;
}

.sb-03__logo svg {
  inline-size: 22px;
  block-size: 22px;
  color: var(--acc);
}

.sb-03__searchcol {
  flex: 1;
  min-inline-size: 0;
}
/* fused bar */

.sb-03__bar {
  position: relative;
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: stretch;
  min-block-size: 48px;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--card);
  transition: border-color .2s, box-shadow .2s;
}

.sb-03__bar:focus-within {
  border-color: var(--acc);
  box-shadow: 0 0 0 4px rgba(226,98,15,.18);
}

.sb-03__scope {
  position: relative;
  display: flex;
  align-items: center;
  border-inline-end: 1px solid var(--line);
}

.sb-03__select {
  appearance: none;
  -webkit-appearance: none;
  border: 0;
  background: none;
  color: var(--muted);
  cursor: pointer;
  max-inline-size: 11rem;
  padding: 0 2rem 0 .95rem;
  block-size: 100%;
  border-radius: 12px 0 0 12px;
  font: 500 .86rem/1 inherit;
  text-overflow: ellipsis;
}

.sb-03__select:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: -2px;
}

.sb-03__chev {
  position: absolute;
  inset-inline-end: .6rem;
  inline-size: 15px;
  block-size: 15px;
  color: var(--muted);
  pointer-events: none;
}

.sb-03__input {
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  padding: 0 .9rem;
  font: 400 .95rem/1 inherit;
}

.sb-03__input::placeholder {
  color: var(--muted);
  text-overflow: ellipsis;
}

.sb-03__input:focus {
  outline: none;
}

.sb-03__submit {
  display: grid;
  place-items: center;
  inline-size: 56px;
  margin: .28rem;
  border: 0;
  border-radius: 9px;
  cursor: pointer;
  background: var(--acc);
  color: var(--acc-ink);
  transition: filter .18s, scale .12s;
}

.sb-03__submit:hover {
  filter: brightness(1.06);
}

.sb-03__submit:active {
  scale: .97;
}

.sb-03__submit:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-03__mag {
  inline-size: 19px;
  block-size: 19px;
}

.sb-03__spin {
  display: none;
  inline-size: 18px;
  block-size: 18px;
  border: 2px solid rgba(255,255,255,.4);
  border-block-start-color: #fff;
  border-radius: 50%;
  animation: sb-03-spin .7s linear infinite;
}

.sb-03__bar[data-state="loading"] .sb-03__mag {
  display: none;
}

.sb-03__bar[data-state="loading"] .sb-03__spin {
  display: block;
}

@keyframes sb-03-spin {
  to {
    rotate: 360deg;
  }
}
/* suggestions */

.sb-03__sug {
  position: absolute;
  inset-inline: 0;
  inset-block-start: calc(100% + .5rem);
  z-index: 6;
  padding: .45rem;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--card);
  box-shadow: 0 24px 44px -20px var(--shadow);
  opacity: 0;
  translate: 0 -6px;
  visibility: hidden;
  transition: opacity .2s, translate .2s, visibility .2s;
}

.sb-03__bar:focus-within .sb-03__sug {
  opacity: 1;
  translate: 0 0;
  visibility: visible;
}

.sb-03__sug-h {
  margin: .4rem .6rem .3rem;
  color: var(--muted);
  font: 600 .68rem/1 inherit;
  letter-spacing: .09em;
  text-transform: uppercase;
}

.sb-03__sug-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.sb-03__sug-row {
  display: flex;
  align-items: center;
  gap: .6rem;
  min-block-size: 42px;
  padding: 0 .6rem;
  border-radius: 9px;
  cursor: pointer;
  font: 500 .88rem/1 inherit;
  transition: background .14s;
}

.sb-03__sug-row:hover {
  background: var(--wash);
}

.sb-03__sug-row svg {
  inline-size: 16px;
  block-size: 16px;
  color: var(--acc);
  flex: none;
}

.sb-03__tag {
  margin-inline-start: auto;
  color: var(--muted);
  font: 400 .76rem/1 inherit;
  font-variant-numeric: tabular-nums;
}

.sb-03__actions {
  display: flex;
  gap: .35rem;
  flex: none;
}

.sb-03__iconbtn {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid transparent;
  border-radius: 11px;
  background: none;
  color: var(--ink);
  cursor: pointer;
  transition: background .16s, border-color .16s;
}

.sb-03__iconbtn:hover {
  background: var(--wash);
  border-color: var(--line);
}

.sb-03__iconbtn:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-03__iconbtn svg {
  inline-size: 21px;
  block-size: 21px;
}

.sb-03__badge {
  position: absolute;
  inset-block-start: 5px;
  inset-inline-end: 4px;
  min-inline-size: 18px;
  block-size: 18px;
  display: grid;
  place-items: center;
  border-radius: 999px;
  background: var(--acc);
  color: #fff;
  font: 600 .68rem/1 inherit;
}
/* dark */

.sb-03[data-theme="dark"] {
  --bg: #14110e;
  --card: #1c1815;
  --ink: #f5f1ea;
  --muted: #a49c90;
  --line: #2c2622;
  --acc: #f97d24;
  --wash: rgba(249,125,36,.14);
  --ring: #f5f1ea;
  --shadow: rgba(0,0,0,.6);
  background: linear-gradient(180deg,#191510, var(--bg) 45%);
}

@media (prefers-color-scheme: dark) {
  .sb-03:not([data-theme="light"]) {
    --bg: #14110e;
    --card: #1c1815;
    --ink: #f5f1ea;
    --muted: #a49c90;
    --line: #2c2622;
    --acc: #f97d24;
    --wash: rgba(249,125,36,.14);
    --ring: #f5f1ea;
    --shadow: rgba(0,0,0,.6);
    background: linear-gradient(180deg,#191510, var(--bg) 45%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-03 *,
    .sb-03 *::before,
    .sb-03 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .sb-03__bar,
    .sb-03__sug,
    .sb-03__header {
    border: 1px solid CanvasText;
  }

  .sb-03__submit {
    border: 1px solid CanvasText;
  }
}

.sb-03__theme {
  position: absolute;
  inset-block-start: clamp(.75rem,2vw,1.25rem);
  inset-inline-end: clamp(.75rem,2vw,1.25rem);
  z-index: 50;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  padding: 0;
  border-radius: 999px;
  border: 1px solid rgba(0,0,0,.12);
  color: currentColor;
  background: rgba(255,255,255,.72);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1), border-color .25s ease;
}

.sb-03[data-theme="dark"] .sb-03__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-03:not([data-theme="light"]) .sb-03__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-03__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-03[data-theme="dark"] .sb-03__theme:hover,
.sb-03:not([data-theme="light"]) .sb-03__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-03__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-03__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-03__sun {
  display: none;
}

.sb-03__theme[aria-pressed="true"] .sb-03__sun {
  display: block;
}

.sb-03__theme[aria-pressed="true"] .sb-03__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-03__theme {
    transition: none;
  }

  .sb-03__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sb-03');
  if (!root) return;
  const bar = root.querySelector('.sb-03__bar');
  const input = root.querySelector('#sb-03-input');
  const go = root.querySelector('#sb-03-go');
  const cat = root.querySelector('#sb-03-cat');
  let timer;

  const submit = () => {
    const q = input.value.trim() || input.placeholder;
    bar.dataset.state = 'loading';
    bar.setAttribute('aria-busy', 'true');
    clearTimeout(timer);
    timer = setTimeout(() => { bar.dataset.state = 'idle'; bar.removeAttribute('aria-busy'); }, 900);
    return { scope: cat.value, q };                       /* hand this to your router / fetch */
  };

  go.addEventListener('click', submit);
  input.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); submit(); } });
  root.querySelectorAll('.sb-03__sug-row').forEach((row) => row.addEventListener('click', () => {
    input.value = row.textContent.replace(/\d+ items$/, '').trim();
    submit();
  }));
})();
(()=>{const r=document.querySelector('.sb-03');if(!r)return;const t=r.querySelector('.sb-03__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
