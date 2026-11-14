---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/algolia-style-instant-search-with-highlighted-results-dropdown/"
title: "Algolia-Style Instant Search with Highlighted Results Dropdown"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "An instant-search dropdown in the DocSearch/Algolia idiom: focus the field and a panel opens with results grouped under Products, Categories and Help…"
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Algolia-Style Instant Search with Highlighted Results Dropdown
Source: https://codefronts.com/components/css-search-boxes/algolia-style-instant-search-with-highlighted-results-dropdown/

An instant-search dropdown in the DocSearch/Algolia idiom: focus the field and a panel opens with results grouped under Products, Categories and Help articles, each row a thumbnail or icon plus title, description and the matched substring wrapped in <mark>. The reveal is :focus-within — no JavaScript at all.
## HTML
```html
<div class="sb-02">
  <button class="sb-02__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-02__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-02__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-02__stage">
    <div class="sb-02__wrap" role="search">
      <div class="sb-02__field">
        <svg class="sb-02__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.7"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <label class="sb-02__vh" for="sb-02-input">Search products, categories and help articles</label>
        <input class="sb-02__input" id="sb-02-input" type="search" value="head" placeholder="Search everything&hellip;" autocomplete="off" spellcheck="false" aria-haspopup="listbox" aria-controls="sb-02-list">
        <kbd class="sb-02__kbd">&#8984;K</kbd>
      </div>

      <div class="sb-02__panel">
        <ul class="sb-02__list" id="sb-02-list" role="listbox" aria-label="Search results">
          <li class="sb-02__group" role="presentation">
            <p class="sb-02__group-h" id="sb-02-g1">Products</p>
            <ul class="sb-02__sub" role="group" aria-labelledby="sb-02-g1">
              <li class="sb-02__row" role="option" aria-selected="true" style="--i:1">
                <img class="sb-02__thumb" src="https://picsum.photos/seed/sb02-headphones/96/96" width="96" height="96" alt="Over-ear wireless headphones on a grey background" loading="lazy" decoding="async">
                <span class="sb-02__txt">Wireless <mark>head</mark>phones ANC 700<small>Audio &middot; 4.8 &starf; &middot; in stock</small></span>
                <span class="sb-02__price">$249</span>
              </li>
              <li class="sb-02__row" role="option" aria-selected="false" style="--i:2">
                <img class="sb-02__thumb" src="https://picsum.photos/seed/sb02-earbuds/96/96" width="96" height="96" alt="Wireless earbuds in an open charging case" loading="lazy" decoding="async">
                <span class="sb-02__txt"><mark>Head</mark>set Pro USB-C earbuds<small>Audio &middot; 4.6 &starf; &middot; 2 colours</small></span>
                <span class="sb-02__price">$89</span>
              </li>
              <li class="sb-02__row" role="option" aria-selected="false" style="--i:3">
                <img class="sb-02__thumb" src="https://picsum.photos/seed/sb02-stand/96/96" width="96" height="96" alt="Aluminium headphone stand on a desk" loading="lazy" decoding="async">
                <span class="sb-02__txt">Aluminium <mark>head</mark>phone stand<small>Desk &middot; 4.9 &starf;</small></span>
                <span class="sb-02__price">$39</span>
              </li>
            </ul>
          </li>

          <li class="sb-02__group" role="presentation">
            <p class="sb-02__group-h" id="sb-02-g2">Categories</p>
            <ul class="sb-02__sub" role="group" aria-labelledby="sb-02-g2">
              <li class="sb-02__row sb-02__row--slim" role="option" aria-selected="false" style="--i:4">
                <span class="sb-02__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><rect x="4" y="4" width="7" height="7" rx="1.8" stroke="currentColor" stroke-width="1.6"/><rect x="13" y="4" width="7" height="7" rx="1.8" stroke="currentColor" stroke-width="1.6"/><rect x="4" y="13" width="7" height="7" rx="1.8" stroke="currentColor" stroke-width="1.6"/><rect x="13" y="13" width="7" height="7" rx="1.8" stroke="currentColor" stroke-width="1.6"/></svg></span>
                <span class="sb-02__txt"><mark>Head</mark>phones &amp; audio<small>412 products</small></span>
                <svg class="sb-02__go" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13m-5.5-5.5L18 12l-5.5 5.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </li>
              <li class="sb-02__row sb-02__row--slim" role="option" aria-selected="false" style="--i:5">
                <span class="sb-02__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M5 8.5h14M5 12h14M5 15.5h9" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg></span>
                <span class="sb-02__txt"><mark>Head</mark>sets for conferencing<small>96 products</small></span>
                <svg class="sb-02__go" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13m-5.5-5.5L18 12l-5.5 5.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </li>
            </ul>
          </li>

          <li class="sb-02__group" role="presentation">
            <p class="sb-02__group-h" id="sb-02-g3">Help articles</p>
            <ul class="sb-02__sub" role="group" aria-labelledby="sb-02-g3">
              <li class="sb-02__row sb-02__row--slim" role="option" aria-selected="false" style="--i:6">
                <span class="sb-02__tile" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M6 3.8h7.4L18 8.3v11.9H6z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M13 3.8v4.5h5" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></span>
                <span class="sb-02__txt">Pairing your <mark>head</mark>phones with two devices<small>Updated 3 weeks ago</small></span>
                <svg class="sb-02__go" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13m-5.5-5.5L18 12l-5.5 5.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </li>
            </ul>
          </li>
        </ul>
        <footer class="sb-02__foot">
          <span class="sb-02__hint"><kbd class="sb-02__kbd">&crarr;</kbd> to select</span>
          <span class="sb-02__count">18 results</span>
        </footer>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-02 {
  --bg: #f7f8fb;
  --card: #ffffff;
  --ink: #101828;
  --muted: #667085;
  --line: #e6e8f0;
  --acc: #2563eb;
  --wash: #eff4ff;
  --ring: #2563eb;
  --shadow: rgba(16,24,40,.14);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: radial-gradient(46rem 26rem at 50% -8%, rgba(37,99,235,.09), transparent 70%), var(--bg);
  -webkit-font-smoothing: antialiased;
}

.sb-02 *,
.sb-02 *::before,
.sb-02 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% .1 270)) {
  .sb-02 {
    --bg: oklch(97.5% .006 265);
    --ink: oklch(22% .03 265);
    --muted: oklch(55% .03 265);
    --line: oklch(92% .01 265);
    --acc: oklch(55% .21 262);
    --wash: color-mix(in oklab, oklch(55% .21 262) 8%, white);
  }
}

.sb-02__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: start center;
  padding: clamp(1.5rem,10vh,7rem) clamp(1rem,4vw,3rem);
}

.sb-02__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-02__wrap {
  position: relative;
  inline-size: min(34rem,100%);
}
/* field */

.sb-02__field {
  display: flex;
  align-items: center;
  gap: .7rem;
  min-block-size: 52px;
  padding-inline: 1rem .55rem;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--card);
  box-shadow: 0 1px 2px rgba(16,24,40,.05);
  transition: border-color .2s, box-shadow .2s;
}

.sb-02__wrap:focus-within .sb-02__field {
  border-color: var(--acc);
  border-end-start-radius: 0;
  border-end-end-radius: 0;
  box-shadow: 0 0 0 4px color-mix(in oklab, var(--acc) 14%, transparent);
}

.sb-02__ico {
  inline-size: 19px;
  block-size: 19px;
  flex: none;
  color: var(--muted);
  transition: color .2s;
}

.sb-02__wrap:focus-within .sb-02__ico {
  color: var(--acc);
}

.sb-02__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 1rem/1.4 inherit;
}

.sb-02__input::placeholder {
  color: var(--muted);
}

.sb-02__input:focus {
  outline: none;
}

.sb-02__kbd {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-inline-size: 1.6rem;
  block-size: 1.6rem;
  padding-inline: .4rem;
  border: 1px solid var(--line);
  border-radius: 7px;
  background: #f7f8fb;
  color: var(--muted);
  font: 500 .7rem/1 ui-monospace,"SF Mono",Menlo,monospace;
}
/* panel */

.sb-02__panel {
  position: absolute;
  inset-inline: 0;
  inset-block-start: calc(100% - 1px);
  z-index: 5;
  border: 1px solid var(--acc);
  border-block-start: 0;
  border-radius: 0 0 14px 14px;
  background: var(--card);
  box-shadow: 0 24px 48px -18px var(--shadow);
  overflow: hidden;
  opacity: 0;
  translate: 0 -6px;
  visibility: hidden;
  transition: opacity .2s cubic-bezier(.2,.9,.25,1), translate .2s cubic-bezier(.2,.9,.25,1), visibility .2s;
}

.sb-02__wrap:focus-within .sb-02__panel {
  opacity: 1;
  translate: 0 0;
  visibility: visible;
}

.sb-02__list,
.sb-02__sub {
  list-style: none;
  margin: 0;
  padding: 0;
}

.sb-02__list {
  max-block-size: min(26rem,58vh);
  overflow: auto;
  overscroll-behavior: contain;
  padding: .4rem;
}

.sb-02__group-h {
  margin: .6rem .65rem .25rem;
  color: var(--muted);
  font: 600 .68rem/1 inherit;
  letter-spacing: .09em;
  text-transform: uppercase;
}

.sb-02__row {
  display: flex;
  align-items: center;
  gap: .8rem;
  min-block-size: 56px;
  padding: .5rem .65rem;
  border-radius: 10px;
  cursor: pointer;
  opacity: 0;
  translate: 0 6px;
  transition: opacity .26s cubic-bezier(.2,.9,.25,1), translate .26s cubic-bezier(.2,.9,.25,1), background .14s;
}

.sb-02__wrap:focus-within .sb-02__row {
  opacity: 1;
  translate: 0 0;
  transition-delay: calc(var(--i,0) * 22ms);
}

.sb-02__row--slim {
  min-block-size: 48px;
}

.sb-02__row:hover,
.sb-02__row[aria-selected="true"] {
  background: var(--wash);
}

.sb-02__thumb {
  inline-size: 40px;
  block-size: 40px;
  flex: none;
  border-radius: 9px;
  object-fit: cover;
  background: #eef0f6;
  box-shadow: inset 0 0 0 1px var(--line);
}

.sb-02__tile {
  display: grid;
  place-items: center;
  inline-size: 34px;
  block-size: 34px;
  flex: none;
  border-radius: 9px;
  background: var(--wash);
  color: var(--acc);
}

.sb-02__tile svg {
  inline-size: 17px;
  block-size: 17px;
}

.sb-02__txt {
  display: block;
  flex: 1;
  min-inline-size: 0;
  font: 500 .92rem/1.3 inherit;
  text-wrap: pretty;
}

.sb-02__txt small {
  display: block;
  margin-block-start: .15rem;
  color: var(--muted);
  font: 400 .76rem/1.3 inherit;
}

.sb-02__panel mark {
  background: none;
  color: var(--acc);
  font-weight: 650;
  padding-inline: .02em;
}

.sb-02__price {
  font: 600 .9rem/1 inherit;
  font-variant-numeric: tabular-nums;
}

.sb-02__go {
  inline-size: 16px;
  block-size: 16px;
  color: var(--muted);
  opacity: 0;
  translate: -4px 0;
  transition: opacity .16s, translate .16s;
}

.sb-02__row:hover .sb-02__go,
.sb-02__row[aria-selected="true"] .sb-02__go {
  opacity: 1;
  translate: 0 0;
  color: var(--acc);
}

.sb-02__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: .6rem .9rem;
  border-block-start: 1px solid var(--line);
  background: #fafbfd;
  color: var(--muted);
  font: 500 .74rem/1 inherit;
}

.sb-02__hint {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
}

.sb-02__foot .sb-02__kbd {
  min-inline-size: 1.35rem;
  block-size: 1.35rem;
  font-size: .68rem;
  background: var(--card);
}

.sb-02 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}
/* dark */

.sb-02[data-theme="dark"] {
  --bg: #0b0e14;
  --card: #12161f;
  --ink: #e9ecf5;
  --muted: #8a93a6;
  --line: #212734;
  --acc: #6ea8fe;
  --wash: rgba(110,168,254,.12);
  --ring: #6ea8fe;
  --shadow: rgba(0,0,0,.6);
  background: radial-gradient(46rem 26rem at 50% -8%, rgba(110,168,254,.12), transparent 70%), var(--bg);
}

.sb-02[data-theme="dark"] .sb-02__kbd,
.sb-02[data-theme="dark"] .sb-02__foot {
  background: #0f131b;
}

.sb-02[data-theme="dark"] .sb-02__thumb {
  background: #1a2130;
}

@media (prefers-color-scheme: dark) {
  .sb-02:not([data-theme="light"]) {
    --bg: #0b0e14;
    --card: #12161f;
    --ink: #e9ecf5;
    --muted: #8a93a6;
    --line: #212734;
    --acc: #6ea8fe;
    --wash: rgba(110,168,254,.12);
    --ring: #6ea8fe;
    --shadow: rgba(0,0,0,.6);
    background: radial-gradient(46rem 26rem at 50% -8%, rgba(110,168,254,.12), transparent 70%), var(--bg);
  }

  .sb-02:not([data-theme="light"]) .sb-02__kbd,
    .sb-02:not([data-theme="light"]) .sb-02__foot {
    background: #0f131b;
  }

  .sb-02:not([data-theme="light"]) .sb-02__thumb {
    background: #1a2130;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-02 *,
    .sb-02 *::before,
    .sb-02 *::after {
    animation: none !important;
    transition: none !important;
  }

  .sb-02__wrap:focus-within .sb-02__row {
    opacity: 1;
    translate: 0 0;
  }
}

@media (forced-colors: active) {
  .sb-02__field,
    .sb-02__panel {
    border: 1px solid CanvasText;
  }

  .sb-02__row[aria-selected="true"] {
    outline: 2px solid Highlight;
  }

  .sb-02__panel mark {
    background: Highlight;
    color: HighlightText;
  }
}

.sb-02__theme {
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

.sb-02[data-theme="dark"] .sb-02__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-02:not([data-theme="light"]) .sb-02__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-02__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-02[data-theme="dark"] .sb-02__theme:hover,
.sb-02:not([data-theme="light"]) .sb-02__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-02__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-02__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-02__sun {
  display: none;
}

.sb-02__theme[aria-pressed="true"] .sb-02__sun {
  display: block;
}

.sb-02__theme[aria-pressed="true"] .sb-02__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-02__theme {
    transition: none;
  }

  .sb-02__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-02');if(!r)return;const t=r.querySelector('.sb-02__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
