---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/inset-pressed/"
title: "CSS Search Bar with Inset Pressed 3D Effect"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "A field that looks carved into the surface: two inset shadows (dark from the top, light from the bottom) plus a 1px highlight on the lower lip."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Search Bar with Inset Pressed 3D Effect
Source: https://codefronts.com/components/css-search-boxes/inset-pressed/

A field that looks carved into the surface: two inset shadows (dark from the top, light from the bottom) plus a 1px highlight on the lower lip. The 2027 take on neumorphism — depth without the contrast failures, because the text and icons stay on solid, accessible colours.
## HTML
```html
<div class="sb-33">
  <button class="sb-33__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-33__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-33__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-33__stage">
    <div class="sb-33__panel">
      <p class="sb-33__label" id="sb-33-label">Library search</p>
      <div class="sb-33__row" role="search">
        <div class="sb-33__field">
          <svg class="sb-33__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.9"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
          <label class="sb-33__vh" for="sb-33-input">Search the library</label>
          <input class="sb-33__input" id="sb-33-input" type="search" placeholder="Search 4,281 records" autocomplete="off">
        </div>
        <button class="sb-33__go" type="button" aria-label="Search">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13m-5.5-5.5L18 12l-5.5 5.5" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-33 {
  --surface: #e8eaef;
  --ink: #1e2230;
  --muted: #6d7385;
  --acc: #4a5bd8;
  --dark: rgba(163,168,183,.85);
  --light: rgba(255,255,255,.95);
  --lip: rgba(255,255,255,.7);
  --ring: #4a5bd8;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: var(--surface);
  -webkit-font-smoothing: antialiased;
}

.sb-33 *,
.sb-33 *::before,
.sb-33 *::after {
  box-sizing: border-box;
}

.sb-33__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-33__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-33__panel {
  inline-size: min(30rem,100%);
  padding: clamp(1.1rem,3vw,1.6rem);
  border-radius: 22px;
  background: var(--surface);
  box-shadow: -8px -8px 18px var(--light), 10px 10px 22px var(--dark);
}

.sb-33__label {
  margin: 0 0 .8rem .25rem;
  color: var(--muted);
  font: 700 .74rem/1 inherit;
  letter-spacing: .12em;
  text-transform: uppercase;
  text-shadow: 0 1px 0 rgba(255,255,255,.85);
}

.sb-33__row {
  display: flex;
  align-items: center;
  gap: .75rem;
}

.sb-33__field {
  display: flex;
  align-items: center;
  gap: .7rem;
  flex: 1;
  min-inline-size: 0;
  min-block-size: 54px;
  padding-inline: 1rem;
  border-radius: 14px;
  background: var(--surface);
  box-shadow: inset 3px 3px 7px var(--dark), inset -3px -3px 7px var(--light), 0 1px 0 var(--lip);
  transition: box-shadow .22s;
}

.sb-33__field:focus-within {
  box-shadow: inset 4px 4px 9px var(--dark), inset -4px -4px 9px var(--light), 0 0 0 3px rgba(74,91,216,.28);
}

.sb-33__ico {
  inline-size: 19px;
  block-size: 19px;
  flex: none;
  color: var(--muted);
  transition: color .2s;
}

.sb-33__field:focus-within .sb-33__ico {
  color: var(--acc);
}

.sb-33__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 500 .96rem/1 inherit;
}

.sb-33__input::placeholder {
  color: var(--muted);
  font-weight: 400;
}

.sb-33__input:focus {
  outline: none;
}

.sb-33__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-33__go {
  display: grid;
  place-items: center;
  inline-size: 54px;
  block-size: 54px;
  flex: none;
  border: 0;
  border-radius: 14px;
  background: var(--surface);
  color: var(--acc);
  cursor: pointer;
  box-shadow: -4px -4px 9px var(--light), 5px 5px 11px var(--dark);
  transition: box-shadow .16s, color .16s;
}

.sb-33__go:hover {
  color: #3949c4;
}

.sb-33__go:active {
  box-shadow: inset 3px 3px 7px var(--dark), inset -3px -3px 7px var(--light);
}

.sb-33__go svg {
  inline-size: 19px;
  block-size: 19px;
}

.sb-33 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.sb-33__input:focus-visible {
  outline: none;
}

.sb-33[data-theme="dark"] {
  --surface: #22252e;
  --ink: #e9ebf2;
  --muted: #8f95a7;
  --acc: #8f9dff;
  --dark: rgba(9,10,14,.85);
  --light: rgba(255,255,255,.055);
  --lip: rgba(255,255,255,.05);
  --ring: #8f9dff;
}

.sb-33[data-theme="dark"] .sb-33__label {
  text-shadow: 0 -1px 0 rgba(0,0,0,.6);
}

@media (prefers-color-scheme: dark) {
  .sb-33:not([data-theme="light"]) {
    --surface: #22252e;
    --ink: #e9ebf2;
    --muted: #8f95a7;
    --acc: #8f9dff;
    --dark: rgba(9,10,14,.85);
    --light: rgba(255,255,255,.055);
    --lip: rgba(255,255,255,.05);
    --ring: #8f9dff;
  }

  .sb-33:not([data-theme="light"]) .sb-33__label {
    text-shadow: 0 -1px 0 rgba(0,0,0,.6);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-33 *,
    .sb-33 *::before,
    .sb-33 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .sb-33__panel,
    .sb-33__field,
    .sb-33__go {
    border: 1px solid CanvasText;
    box-shadow: none;
  }
}

.sb-33__theme {
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

.sb-33[data-theme="dark"] .sb-33__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-33:not([data-theme="light"]) .sb-33__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-33__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-33[data-theme="dark"] .sb-33__theme:hover,
.sb-33:not([data-theme="light"]) .sb-33__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-33__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-33__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-33__sun {
  display: none;
}

.sb-33__theme[aria-pressed="true"] .sb-33__sun {
  display: block;
}

.sb-33__theme[aria-pressed="true"] .sb-33__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-33__theme {
    transition: none;
  }

  .sb-33__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-33');if(!r)return;const t=r.querySelector('.sb-33__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
