---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/search-filter/"
title: "CSS Search + Filter Sidebar Combo Bar"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "A faceted-search sidebar: search at the top, then category checkboxes with result counts, a price range and an in-stock toggle."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Search + Filter Sidebar Combo Bar
Source: https://codefronts.com/components/css-search-boxes/search-filter/

A faceted-search sidebar: search at the top, then category checkboxes with result counts, a price range and an in-stock toggle. Every control is a native input styled with appearance:none, so keyboard, screen-reader and mobile behaviour are the browser's — not yours.
## HTML
```html
<div class="sb-26">
  <button class="sb-26__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-26__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-26__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-26__stage">
    <aside class="sb-26__panel">
      <div class="sb-26__search" role="search">
        <svg class="sb-26__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.3" stroke="currentColor" stroke-width="1.8"/><path d="m15.9 15.9 4.3 4.3" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <label class="sb-26__vh" for="sb-26-input">Search products</label>
        <input class="sb-26__input" id="sb-26-input" type="search" placeholder="Search products" autocomplete="off">
      </div>

      <fieldset class="sb-26__group">
        <legend class="sb-26__legend">Category</legend>
        <label class="sb-26__row"><input class="sb-26__check" type="checkbox" checked><span class="sb-26__txt">Headphones</span><span class="sb-26__num">412</span></label>
        <label class="sb-26__row"><input class="sb-26__check" type="checkbox"><span class="sb-26__txt">Keyboards</span><span class="sb-26__num">238</span></label>
        <label class="sb-26__row"><input class="sb-26__check" type="checkbox" checked><span class="sb-26__txt">Monitors</span><span class="sb-26__num">96</span></label>
        <label class="sb-26__row"><input class="sb-26__check" type="checkbox"><span class="sb-26__txt">Desk accessories</span><span class="sb-26__num">54</span></label>
      </fieldset>

      <fieldset class="sb-26__group">
        <legend class="sb-26__legend">Max price</legend>
        <label class="sb-26__vh" for="sb-26-price">Maximum price in dollars</label>
        <input class="sb-26__range" id="sb-26-price" type="range" min="0" max="500" value="280" step="10">
        <p class="sb-26__scale"><span>$0</span><span>$500</span></p>
      </fieldset>

      <label class="sb-26__row sb-26__row--switch">
        <span class="sb-26__txt">In stock only</span>
        <input class="sb-26__switch" type="checkbox" checked role="switch">
      </label>
    </aside>
  </div>
</div>
```
## CSS
```css
.sb-26 {
  --bg: #f4f5f8;
  --card: #ffffff;
  --ink: #151821;
  --muted: #6b7280;
  --line: #e3e6ec;
  --acc: #4f46e5;
  --wash: rgba(79,70,229,.10);
  --ring: #4f46e5;
  --shadow: rgba(21,24,33,.14);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: var(--bg);
  accent-color: #4f46e5;
  -webkit-font-smoothing: antialiased;
}

.sb-26 *,
.sb-26 *::before,
.sb-26 *::after {
  box-sizing: border-box;
}

.sb-26__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-26__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-26__panel {
  inline-size: min(19rem,100%);
  padding: 1rem;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: var(--card);
  box-shadow: 0 22px 46px -30px var(--shadow), 0 1px 2px rgba(21,24,33,.04);
  display: flex;
  flex-direction: column;
  gap: 1.1rem;
}

.sb-26__search {
  display: flex;
  align-items: center;
  gap: .55rem;
  min-block-size: 42px;
  padding-inline: .75rem;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: #fafbfd;
  transition: border-color .18s, box-shadow .18s, background .18s;
}

.sb-26__search:focus-within {
  border-color: var(--acc);
  background: var(--card);
  box-shadow: 0 0 0 3px var(--wash);
}

.sb-26__ico {
  inline-size: 16px;
  block-size: 16px;
  flex: none;
  color: var(--muted);
}

.sb-26__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .88rem/1 inherit;
}

.sb-26__input::placeholder {
  color: var(--muted);
}

.sb-26__input:focus {
  outline: none;
}

.sb-26__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-26__group {
  margin: 0;
  padding: 0;
  border: 0;
  display: flex;
  flex-direction: column;
  gap: .1rem;
}

.sb-26__legend {
  padding: 0 0 .35rem;
  color: var(--muted);
  font: 600 .68rem/1 inherit;
  letter-spacing: .09em;
  text-transform: uppercase;
}

.sb-26__row {
  display: flex;
  align-items: center;
  gap: .65rem;
  min-block-size: 44px;
  padding-inline: .55rem;
  border-radius: 9px;
  cursor: pointer;
  color: var(--ink);
  font: 500 .88rem/1 inherit;
  transition: background .14s;
}

.sb-26__row:hover {
  background: #f5f6fa;
}

.sb-26__row:has(:checked) {
  background: var(--wash);
}

.sb-26__txt {
  flex: 1;
  min-inline-size: 0;
}

.sb-26__num {
  color: var(--muted);
  font: 400 .78rem/1 inherit;
  font-variant-numeric: tabular-nums;
}

.sb-26__check {
  appearance: none;
  -webkit-appearance: none;
  position: relative;
  flex: none;
  margin: 0;
  inline-size: 18px;
  block-size: 18px;
  border: 1.5px solid #cfd4de;
  border-radius: 5px;
  background: var(--card);
  cursor: pointer;
  transition: background .16s, border-color .16s;
}

.sb-26__check:checked {
  background: var(--acc);
  border-color: var(--acc);
}

.sb-26__check:checked::after {
  content: '';
  position: absolute;
  inset-block-start: 2px;
  inset-inline-start: 5.5px;
  inline-size: 4px;
  block-size: 8px;
  border: 2px solid #fff;
  border-block-start: 0;
  border-inline-start: 0;
  -webkit-transform: rotate(45deg);
  transform: rotate(45deg);
  rotate: 45deg;
}

.sb-26__check:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-26__range {
  appearance: none;
  -webkit-appearance: none;
  inline-size: 100%;
  block-size: 22px;
  background: none;
  cursor: pointer;
  margin: 0;
}

.sb-26__range::-webkit-slider-runnable-track {
  block-size: 5px;
  border-radius: 99px;
  background: linear-gradient(90deg, var(--acc) 56%, #e6e8ef 56%);
}

.sb-26__range::-moz-range-track {
  block-size: 5px;
  border-radius: 99px;
  background: #e6e8ef;
}

.sb-26__range::-moz-range-progress {
  block-size: 5px;
  border-radius: 99px;
  background: var(--acc);
}

.sb-26__range::-webkit-slider-thumb {
  -webkit-appearance: none;
  inline-size: 18px;
  block-size: 18px;
  margin-block-start: -6.5px;
  border: 2px solid var(--acc);
  border-radius: 50%;
  background: var(--card);
  box-shadow: 0 1px 3px rgba(21,24,33,.25);
}

.sb-26__range::-moz-range-thumb {
  inline-size: 14px;
  block-size: 14px;
  border: 2px solid var(--acc);
  border-radius: 50%;
  background: var(--card);
  box-shadow: 0 1px 3px rgba(21,24,33,.25);
}

.sb-26__range:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 4px;
}

.sb-26__scale {
  display: flex;
  justify-content: space-between;
  margin: .15rem .1rem 0;
  color: var(--muted);
  font: 400 .74rem/1 inherit;
  font-variant-numeric: tabular-nums;
}

.sb-26__row--switch {
  margin-block-start: -.2rem;
}

.sb-26__switch {
  appearance: none;
  -webkit-appearance: none;
  position: relative;
  flex: none;
  margin: 0;
  inline-size: 38px;
  block-size: 22px;
  border-radius: 99px;
  background: #d3d7e0;
  cursor: pointer;
  transition: background .2s;
}

.sb-26__switch::before {
  content: '';
  position: absolute;
  inset-block-start: 2px;
  inset-inline-start: 2px;
  inline-size: 18px;
  block-size: 18px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 1px 2px rgba(21,24,33,.3);
  transition: translate .2s cubic-bezier(.2,.9,.25,1);
}

.sb-26__switch:checked {
  background: var(--acc);
}

.sb-26__switch:checked::before {
  translate: 16px 0;
}

.sb-26__switch:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-26[data-theme="dark"] {
  --bg: #0a0d13;
  --card: #141821;
  --ink: #e9ecf4;
  --muted: #878e9c;
  --line: #232a37;
  --acc: #8b83ff;
  --wash: rgba(139,131,255,.14);
  --ring: #8b83ff;
  --shadow: rgba(0,0,0,.7);
  accent-color: #8b83ff;
}

.sb-26[data-theme="dark"] .sb-26__search {
  background: #101520;
}

.sb-26[data-theme="dark"] .sb-26__row:hover {
  background: #1a2029;
}

.sb-26[data-theme="dark"] .sb-26__check {
  border-color: #39404f;
  background: #101520;
}

.sb-26[data-theme="dark"] .sb-26__range::-webkit-slider-runnable-track {
  background: linear-gradient(90deg, var(--acc) 56%, #2a3140 56%);
}

.sb-26[data-theme="dark"] .sb-26__range::-moz-range-track {
  background: #2a3140;
}

.sb-26[data-theme="dark"] .sb-26__switch {
  background: #39404f;
}

@media (prefers-color-scheme: dark) {
  .sb-26:not([data-theme="light"]) {
    --bg: #0a0d13;
    --card: #141821;
    --ink: #e9ecf4;
    --muted: #878e9c;
    --line: #232a37;
    --acc: #8b83ff;
    --wash: rgba(139,131,255,.14);
    --ring: #8b83ff;
    --shadow: rgba(0,0,0,.7);
    accent-color: #8b83ff;
  }

  .sb-26:not([data-theme="light"]) .sb-26__search {
    background: #101520;
  }

  .sb-26:not([data-theme="light"]) .sb-26__row:hover {
    background: #1a2029;
  }

  .sb-26:not([data-theme="light"]) .sb-26__check {
    border-color: #39404f;
    background: #101520;
  }

  .sb-26:not([data-theme="light"]) .sb-26__range::-webkit-slider-runnable-track {
    background: linear-gradient(90deg, var(--acc) 56%, #2a3140 56%);
  }

  .sb-26:not([data-theme="light"]) .sb-26__range::-moz-range-track {
    background: #2a3140;
  }

  .sb-26:not([data-theme="light"]) .sb-26__switch {
    background: #39404f;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-26 *,
    .sb-26 *::before,
    .sb-26 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .sb-26__panel,
    .sb-26__search,
    .sb-26__check,
    .sb-26__switch {
    border: 1px solid CanvasText;
  }

  .sb-26__check:checked {
    background: Highlight;
  }
}

.sb-26__theme {
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

.sb-26[data-theme="dark"] .sb-26__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-26:not([data-theme="light"]) .sb-26__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-26__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-26[data-theme="dark"] .sb-26__theme:hover,
.sb-26:not([data-theme="light"]) .sb-26__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-26__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-26__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-26__sun {
  display: none;
}

.sb-26__theme[aria-pressed="true"] .sb-26__sun {
  display: block;
}

.sb-26__theme[aria-pressed="true"] .sb-26__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-26__theme {
    transition: none;
  }

  .sb-26__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-26');if(!r)return;const t=r.querySelector('.sb-26__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
