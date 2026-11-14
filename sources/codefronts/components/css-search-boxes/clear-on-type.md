---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/clear-on-type/"
title: "CSS Search Bar with Clear Button (X on Type)"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "The clear &times; appears only once you have typed — and the appearing is done entirely in CSS with :not(:placeholder-shown), no input listener required."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Search Bar with Clear Button (X on Type)
Source: https://codefronts.com/components/css-search-boxes/clear-on-type/

The clear &times; appears only once you have typed — and the appearing is done entirely in CSS with :not(:placeholder-shown), no input listener required. Five lines of JavaScript clear the value and hand focus back to the field, which is the part CSS cannot do.
## HTML
```html
<div class="sb-13">
  <button class="sb-13__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-13__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-13__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-13__stage">
    <div class="sb-13__bar" role="search">
      <svg class="sb-13__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      <label class="sb-13__vh" for="sb-13-input">Search orders</label>
      <input class="sb-13__input" id="sb-13-input" type="search" value="invoice template" placeholder="Search orders, invoices, customers" autocomplete="off">
      <button class="sb-13__clear" id="sb-13-clear" type="button" aria-label="Clear search">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m7 7 10 10M17 7 7 17" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      </button>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-13 {
  --bg: #f6f7f9;
  --card: #ffffff;
  --ink: #111827;
  --muted: #6b7280;
  --line: #e4e7ec;
  --acc: #111827;
  --wash: #f1f3f7;
  --ring: #2563eb;
  --shadow: rgba(17,24,39,.12);
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

.sb-13 *,
.sb-13 *::before,
.sb-13 *::after {
  box-sizing: border-box;
}

.sb-13__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-13__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-13__bar {
  display: flex;
  align-items: center;
  gap: .7rem;
  inline-size: min(28rem,100%);
  min-block-size: 54px;
  padding-inline: 1rem .5rem;
  border: 1px solid var(--line);
  border-radius: 13px;
  background: var(--card);
  box-shadow: 0 1px 2px rgba(17,24,39,.04);
  transition: border-color .2s, box-shadow .2s;
}

.sb-13__bar:focus-within {
  border-color: var(--acc);
  box-shadow: 0 0 0 4px rgba(17,24,39,.08);
}

.sb-13__ico {
  inline-size: 19px;
  block-size: 19px;
  flex: none;
  color: var(--muted);
}

.sb-13__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .96rem/1 inherit;
}

.sb-13__input::placeholder {
  color: var(--muted);
}

.sb-13__input:focus {
  outline: none;
}

.sb-13__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-13__clear {
  display: grid;
  place-items: center;
  inline-size: 36px;
  block-size: 36px;
  flex: none;
  border: 0;
  border-radius: 10px;
  background: var(--wash);
  color: var(--muted);
  cursor: pointer;
  opacity: 0;
  pointer-events: none;
  -webkit-transform: scale(.6) rotate(-90deg);
  transform: scale(.6) rotate(-90deg);
  scale: .6;
  rotate: -90deg;
  transition: opacity .18s cubic-bezier(.2,.9,.25,1), scale .18s cubic-bezier(.2,.9,.25,1), rotate .18s cubic-bezier(.2,.9,.25,1), transform .18s cubic-bezier(.2,.9,.25,1), background .16s, color .16s;
}

.sb-13__input:not(:placeholder-shown) ~ .sb-13__clear {
  opacity: 1;
  pointer-events: auto;
  -webkit-transform: none;
  transform: none;
  scale: 1;
  rotate: 0deg;
}

.sb-13__clear:hover {
  background: #e7eaf0;
  color: var(--ink);
}

.sb-13__clear:active {
  scale: .92;
}

.sb-13__clear:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-13__clear svg {
  inline-size: 16px;
  block-size: 16px;
}

.sb-13[data-theme="dark"] {
  --bg: #0d1017;
  --card: #151a24;
  --ink: #eceff5;
  --muted: #8a919f;
  --line: #232a36;
  --acc: #eceff5;
  --wash: #1d2430;
  --ring: #7aa2ff;
  --shadow: rgba(0,0,0,.7);
}

.sb-13[data-theme="dark"] .sb-13__bar:focus-within {
  box-shadow: 0 0 0 4px rgba(236,239,245,.10);
}

.sb-13[data-theme="dark"] .sb-13__clear:hover {
  background: #27303e;
}

@media (prefers-color-scheme: dark) {
  .sb-13:not([data-theme="light"]) {
    --bg: #0d1017;
    --card: #151a24;
    --ink: #eceff5;
    --muted: #8a919f;
    --line: #232a36;
    --acc: #eceff5;
    --wash: #1d2430;
    --ring: #7aa2ff;
    --shadow: rgba(0,0,0,.7);
  }

  .sb-13:not([data-theme="light"]) .sb-13__bar:focus-within {
    box-shadow: 0 0 0 4px rgba(236,239,245,.10);
  }

  .sb-13:not([data-theme="light"]) .sb-13__clear:hover {
    background: #27303e;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-13 *,
    .sb-13 *::before,
    .sb-13 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .sb-13__bar,
    .sb-13__clear {
    border: 1px solid CanvasText;
  }
}

.sb-13__theme {
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

.sb-13[data-theme="dark"] .sb-13__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-13:not([data-theme="light"]) .sb-13__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-13__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-13[data-theme="dark"] .sb-13__theme:hover,
.sb-13:not([data-theme="light"]) .sb-13__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-13__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-13__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-13__sun {
  display: none;
}

.sb-13__theme[aria-pressed="true"] .sb-13__sun {
  display: block;
}

.sb-13__theme[aria-pressed="true"] .sb-13__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-13__theme {
    transition: none;
  }

  .sb-13__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sb-13');
  if (!root) return;
  const input = root.querySelector('#sb-13-input');
  root.querySelector('#sb-13-clear').addEventListener('click', () => {
    input.value = '';
    input.dispatchEvent(new Event('input', { bubbles: true }));   /* let debounced search know */
    input.focus();
  });
})();
(()=>{const r=document.querySelector('.sb-13');if(!r)return;const t=r.querySelector('.sb-13__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
