---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/pill-with-submit/"
title: "CSS Rounded Pill Search Bar with Submit Button"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "A fully-rounded pill with the magnifier inside on the left and a filled submit button hugging the right edge — the iOS/Safari address-bar shape."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Rounded Pill Search Bar with Submit Button
Source: https://codefronts.com/components/css-search-boxes/pill-with-submit/

A fully-rounded pill with the magnifier inside on the left and a filled submit button hugging the right edge — the iOS/Safari address-bar shape. The button reveals its "Search" label only when the pill has focus, so the resting state stays compact.
## HTML
```html
<div class="sb-07">
  <button class="sb-07__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-07__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-07__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-07__stage">
    <div class="sb-07__bar" role="search">
      <svg class="sb-07__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      <label class="sb-07__vh" for="sb-07-input">Search articles and guides</label>
      <input class="sb-07__input" id="sb-07-input" type="search" placeholder="Search articles, guides, changelog" autocomplete="off">
      <button class="sb-07__submit" type="button">
        <span class="sb-07__label"><span>Search</span></span>
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13m-5.5-5.5L18 12l-5.5 5.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-07 {
  --bg: #f2f4f7;
  --card: #ffffff;
  --ink: #0f1729;
  --muted: #697586;
  --line: #e3e8ef;
  --acc: #111827;
  --acc-ink: #ffffff;
  --ring: #2563eb;
  --h: 52px;
  --shadow: rgba(15,23,41,.16);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: radial-gradient(40rem 22rem at 50% 0%, #ffffff, var(--bg) 70%);
  -webkit-font-smoothing: antialiased;
}

.sb-07 *,
.sb-07 *::before,
.sb-07 *::after {
  box-sizing: border-box;
}

.sb-07__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-07__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-07__bar {
  display: flex;
  align-items: center;
  gap: .6rem;
  inline-size: min(30rem,100%);
  min-block-size: max(48px,var(--h));
  padding-inline: 1.1rem .28rem;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--card);
  box-shadow: 0 1px 2px rgba(15,23,41,.05);
  transition: box-shadow .22s, border-color .22s, translate .22s;
}

.sb-07__bar:hover {
  box-shadow: 0 6px 18px -10px var(--shadow);
}

.sb-07__bar:focus-within {
  border-color: var(--acc);
  box-shadow: 0 10px 26px -14px var(--shadow), 0 0 0 4px rgba(37,99,235,.16);
  translate: 0 -1px;
}

.sb-07__ico {
  inline-size: 19px;
  block-size: 19px;
  flex: none;
  color: var(--muted);
}

.sb-07__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .96rem/1 inherit;
}

.sb-07__input::placeholder {
  color: var(--muted);
}

.sb-07__input:focus {
  outline: none;
}

.sb-07__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-07__submit {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  flex: none;
  min-block-size: calc(max(48px,var(--h)) - 10px);
  padding-inline: .85rem;
  border: 0;
  border-radius: 999px;
  background: var(--acc);
  color: var(--acc-ink);
  cursor: pointer;
  font: 600 .87rem/1 inherit;
  transition: filter .18s, scale .12s;
}

.sb-07__submit:hover {
  filter: brightness(1.25);
}

.sb-07__submit:active {
  scale: .96;
}

.sb-07__submit:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.sb-07__submit svg {
  inline-size: 17px;
  block-size: 17px;
}

.sb-07__label {
  display: grid;
  grid-template-columns: 0fr;
  transition: grid-template-columns .28s cubic-bezier(.2,.9,.25,1);
}

.sb-07__label > span {
  min-inline-size: 0;
  overflow: hidden;
  white-space: nowrap;
}

.sb-07__bar:focus-within .sb-07__label,
.sb-07__bar:hover .sb-07__label {
  grid-template-columns: 1fr;
}

.sb-07[data-theme="dark"] {
  --bg: #0b0f17;
  --card: #121826;
  --ink: #eef2f8;
  --muted: #8b95a7;
  --line: #212a3a;
  --acc: #f1f5f9;
  --acc-ink: #0b0f17;
  --ring: #7aa2ff;
  --shadow: rgba(0,0,0,.7);
  background: radial-gradient(40rem 22rem at 50% 0%, #141b2a, var(--bg) 70%);
}

@media (prefers-color-scheme: dark) {
  .sb-07:not([data-theme="light"]) {
    --bg: #0b0f17;
    --card: #121826;
    --ink: #eef2f8;
    --muted: #8b95a7;
    --line: #212a3a;
    --acc: #f1f5f9;
    --acc-ink: #0b0f17;
    --ring: #7aa2ff;
    --shadow: rgba(0,0,0,.7);
    background: radial-gradient(40rem 22rem at 50% 0%, #141b2a, var(--bg) 70%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-07 *,
    .sb-07 *::before,
    .sb-07 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .sb-07__bar,
    .sb-07__submit {
    border: 1px solid CanvasText;
  }
}

.sb-07__theme {
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

.sb-07[data-theme="dark"] .sb-07__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-07:not([data-theme="light"]) .sb-07__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-07__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-07[data-theme="dark"] .sb-07__theme:hover,
.sb-07:not([data-theme="light"]) .sb-07__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-07__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-07__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-07__sun {
  display: none;
}

.sb-07__theme[aria-pressed="true"] .sb-07__sun {
  display: block;
}

.sb-07__theme[aria-pressed="true"] .sb-07__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-07__theme {
    transition: none;
  }

  .sb-07__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-07');if(!r)return;const t=r.querySelector('.sb-07__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
