---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/combo-with-scope/"
title: "CSS Search Bar Combo with Scope Selector"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "The developer-tool combo: a scope button on the left (\"All files &#9662;\") opening a menu of search scopes, with the query field beside it."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Search Bar Combo with Scope Selector
Source: https://codefronts.com/components/css-search-boxes/combo-with-scope/

The developer-tool combo: a scope button on the left ("All files &#9662;") opening a menu of search scopes, with the query field beside it. The menu uses the Popover API — top-layer, light-dismiss and Escape handling with no JavaScript — plus CSS anchor positioning where available.
## HTML
```html
<div class="sb-32">
  <button class="sb-32__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-32__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-32__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-32__stage">
    <div class="sb-32__bar" role="search">
      <div class="sb-32__scopewrap">
        <button class="sb-32__scope" id="sb-32-btn" type="button" popovertarget="sb-32-menu" aria-expanded="false">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 6.5h5.5l1.6 2H20v9.5H4z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
          <span id="sb-32-label">All files</span>
          <svg class="sb-32__chev" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m7 10 5 5 5-5" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>

        <div class="sb-32__menu" id="sb-32-menu" popover role="menu" aria-label="Search scope">
          <button class="sb-32__item" type="button" role="menuitemradio" aria-checked="true">All files<span class="sb-32__hint">1,204</span></button>
          <button class="sb-32__item" type="button" role="menuitemradio" aria-checked="false">Open editors<span class="sb-32__hint">7</span></button>
          <button class="sb-32__item" type="button" role="menuitemradio" aria-checked="false">Modified files<span class="sb-32__hint">12</span></button>
          <button class="sb-32__item" type="button" role="menuitemradio" aria-checked="false">This folder<span class="sb-32__hint">86</span></button>
        </div>
      </div>

      <label class="sb-32__vh" for="sb-32-input">Search in the selected scope</label>
      <input class="sb-32__input" id="sb-32-input" type="search" placeholder="Search&hellip;" autocomplete="off" spellcheck="false">
      <span class="sb-32__count" aria-hidden="true">18 of 42</span>
      <div class="sb-32__nav">
        <button class="sb-32__navbtn" type="button" aria-label="Previous match"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m7 14 5-5 5 5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
        <button class="sb-32__navbtn" type="button" aria-label="Next match"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m7 10 5 5 5-5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-32 {
  --bg: #f6f7f9;
  --card: #ffffff;
  --field: #f2f3f6;
  --ink: #14161c;
  --muted: #6a707c;
  --line: #e2e5ea;
  --acc: #1f6feb;
  --wash: rgba(31,111,235,.12);
  --ring: #1f6feb;
  --shadow: rgba(20,22,28,.16);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: var(--bg);
  -webkit-font-smoothing: antialiased;
}

.sb-32 *,
.sb-32 *::before,
.sb-32 *::after {
  box-sizing: border-box;
}

.sb-32__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-32__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-32__bar {
  display: flex;
  align-items: center;
  gap: .4rem;
  inline-size: min(38rem,100%);
  min-block-size: 52px;
  padding: .3rem .35rem .3rem .3rem;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--card);
  box-shadow: 0 1px 2px rgba(20,22,28,.05);
  transition: border-color .2s, box-shadow .2s;
}

.sb-32__bar:focus-within {
  border-color: var(--acc);
  box-shadow: 0 0 0 4px var(--wash);
}

.sb-32__scopewrap {
  position: relative;
  flex: none;
}

.sb-32__scope {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-block-size: 44px;
  padding-inline: .7rem .5rem;
  border: 0;
  border-radius: 9px;
  background: var(--field);
  color: var(--ink);
  cursor: pointer;
  font: 600 .86rem/1 inherit;
  white-space: nowrap;
  transition: background .16s;
  anchor-name: --sb-32-scope;
}

.sb-32__scope:hover {
  background: #e9ebef;
}

.sb-32__scope svg {
  inline-size: 16px;
  block-size: 16px;
  color: var(--muted);
}

.sb-32__chev {
  transition: rotate .2s;
}

.sb-32__scope[aria-expanded="true"] .sb-32__chev {
  rotate: 180deg;
}

.sb-32__menu {
  position: absolute;
  margin: 0;
  padding: .3rem;
  inline-size: 15rem;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--card);
  color: var(--ink);
  box-shadow: 0 24px 46px -20px var(--shadow);
  overflow: visible;
}

.sb-32__menu:not(:popover-open) {
  display: none;
}

.sb-32__menu::backdrop {
  background: transparent;
}

@supports not (anchor-name: --a) {
  .sb-32__menu {
    inset: auto;
    inset-block-start: calc(100% + .4rem);
    inset-inline-start: 0;
  }
}

@supports (anchor-name: --a) {
  .sb-32__menu {
    position-anchor: --sb-32-scope;
    inset: auto;
    inset-block-start: anchor(bottom);
    inset-inline-start: anchor(start);
    margin-block-start: .4rem;
  }
}

@supports (transition-behavior: allow-discrete) {
  .sb-32__menu {
    opacity: 0;
    translate: 0 -6px;
    transition: opacity .18s, translate .18s, overlay .18s allow-discrete, display .18s allow-discrete;
  }

  .sb-32__menu:popover-open {
    opacity: 1;
    translate: 0 0;
  }

  @starting-style {
    .sb-32__menu:popover-open {
      opacity: 0;
      translate: 0 -6px;
    }
  }
}

.sb-32__item {
  display: flex;
  align-items: center;
  gap: .5rem;
  inline-size: 100%;
  min-block-size: 40px;
  padding-inline: .6rem;
  border: 0;
  border-radius: 8px;
  background: none;
  color: var(--ink);
  cursor: pointer;
  text-align: start;
  font: 500 .88rem/1 inherit;
  transition: background .14s;
}

.sb-32__item:hover {
  background: var(--field);
}

.sb-32__item[aria-checked="true"] {
  background: var(--wash);
  color: var(--acc);
  font-weight: 600;
}

.sb-32__item[aria-checked="true"]::before {
  content: '\2713';
  font-size: .8rem;
}

.sb-32__item[aria-checked="false"]::before {
  content: '';
  inline-size: .55rem;
}

.sb-32__hint {
  margin-inline-start: auto;
  color: var(--muted);
  font: 400 .76rem/1 inherit;
  font-variant-numeric: tabular-nums;
}

.sb-32__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .93rem/1 inherit;
  padding-inline: .4rem;
}

.sb-32__input::placeholder {
  color: var(--muted);
}

.sb-32__input:focus {
  outline: none;
}

.sb-32__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-32__count {
  flex: none;
  color: var(--muted);
  font: 500 .78rem/1 inherit;
  font-variant-numeric: tabular-nums;
}

.sb-32__nav {
  display: flex;
  gap: .15rem;
  flex: none;
}

.sb-32__navbtn {
  display: grid;
  place-items: center;
  inline-size: 32px;
  block-size: 32px;
  border: 0;
  border-radius: 7px;
  background: none;
  color: var(--muted);
  cursor: pointer;
  transition: background .14s, color .14s;
}

.sb-32__navbtn:hover {
  background: var(--field);
  color: var(--ink);
}

.sb-32__navbtn svg {
  inline-size: 16px;
  block-size: 16px;
}

.sb-32 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-32__input:focus-visible {
  outline: none;
}

.sb-32[data-theme="dark"] {
  --bg: #0b0d11;
  --card: #14171d;
  --field: #1c2029;
  --ink: #e8ebf1;
  --muted: #868d99;
  --line: #232830;
  --acc: #589bff;
  --wash: rgba(88,155,255,.14);
  --ring: #589bff;
  --shadow: rgba(0,0,0,.75);
}

.sb-32[data-theme="dark"] .sb-32__scope:hover {
  background: #232936;
}

@media (prefers-color-scheme: dark) {
  .sb-32:not([data-theme="light"]) {
    --bg: #0b0d11;
    --card: #14171d;
    --field: #1c2029;
    --ink: #e8ebf1;
    --muted: #868d99;
    --line: #232830;
    --acc: #589bff;
    --wash: rgba(88,155,255,.14);
    --ring: #589bff;
    --shadow: rgba(0,0,0,.75);
  }

  .sb-32:not([data-theme="light"]) .sb-32__scope:hover {
    background: #232936;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-32 *,
    .sb-32 *::before,
    .sb-32 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .sb-32__bar,
    .sb-32__menu,
    .sb-32__scope {
    border: 1px solid CanvasText;
  }
}

.sb-32__theme {
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

.sb-32[data-theme="dark"] .sb-32__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-32:not([data-theme="light"]) .sb-32__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-32__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-32[data-theme="dark"] .sb-32__theme:hover,
.sb-32:not([data-theme="light"]) .sb-32__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-32__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-32__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-32__sun {
  display: none;
}

.sb-32__theme[aria-pressed="true"] .sb-32__sun {
  display: block;
}

.sb-32__theme[aria-pressed="true"] .sb-32__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-32__theme {
    transition: none;
  }

  .sb-32__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sb-32');
  if (!root) return;
  const btn = root.querySelector('#sb-32-btn');
  const menu = root.querySelector('#sb-32-menu');
  const label = root.querySelector('#sb-32-label');
  const items = [...menu.querySelectorAll('.sb-32__item')];

  menu.addEventListener('toggle', (e) => btn.setAttribute('aria-expanded', String(e.newState === 'open')));
  items.forEach((item, i) => {
    item.addEventListener('click', () => {
      items.forEach((n) => n.setAttribute('aria-checked', String(n === item)));
      label.textContent = item.firstChild.textContent.trim();
      menu.hidePopover(); btn.focus();
    });
    item.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowDown') { e.preventDefault(); items[(i + 1) % items.length].focus(); }
      if (e.key === 'ArrowUp') { e.preventDefault(); items[(i - 1 + items.length) % items.length].focus(); }
    });
  });
})();
(()=>{const r=document.querySelector('.sb-32');if(!r)return;const t=r.querySelector('.sb-32__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
