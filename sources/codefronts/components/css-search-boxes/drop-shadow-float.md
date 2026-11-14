---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/drop-shadow-float/"
title: "Floating CSS Search Bar with Drop Shadow (Elevated)"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "Elevation done like a designer, not a default: a four-layer shadow stack (contact, ambient, mid, far) that mimics real light falloff, plus a lift on hover…"
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Floating CSS Search Bar with Drop Shadow (Elevated)
Source: https://codefronts.com/components/css-search-boxes/drop-shadow-float/

Elevation done like a designer, not a default: a four-layer shadow stack (contact, ambient, mid, far) that mimics real light falloff, plus a lift on hover and a deeper drop on focus. The same tokens give you a documented elevation scale you can reuse across a product.
## HTML
```html
<div class="sb-25">
  <button class="sb-25__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-25__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-25__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-25__stage">
    <div class="sb-25__bar" role="search">
      <svg class="sb-25__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      <label class="sb-25__vh" for="sb-25-input">Search files and folders</label>
      <input class="sb-25__input" id="sb-25-input" type="search" placeholder="Search files and folders" autocomplete="off">
      <span class="sb-25__divider" aria-hidden="true"></span>
      <button class="sb-25__filter" type="button" aria-label="Filters">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 6.5h16M7 12h10M10 17.5h4" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
      </button>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-25 {
  --bg: #eef0f5;
  --card: #ffffff;
  --ink: #171923;
  --muted: #6b7280;
  --line: #e6e8ef;
  --acc: #3355ff;
  --wash: rgba(51,85,255,.12);
  --ring: #3355ff;
  --e1: 0 1px 2px rgba(23,25,35,.06), 0 3px 6px -2px rgba(23,25,35,.06);
  --e2: 0 1px 2px rgba(23,25,35,.06), 0 4px 8px -2px rgba(23,25,35,.07), 0 12px 24px -6px rgba(23,25,35,.09), 0 28px 48px -12px rgba(23,25,35,.11);
  --e3: 0 1px 2px rgba(23,25,35,.07), 0 6px 12px -3px rgba(23,25,35,.09), 0 18px 34px -8px rgba(23,25,35,.12), 0 40px 68px -16px rgba(23,25,35,.16);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: radial-gradient(40rem 24rem at 50% 22%, #ffffff, transparent 70%), linear-gradient(180deg,#f3f5f9, var(--bg));
  -webkit-font-smoothing: antialiased;
}

.sb-25 *,
.sb-25 *::before,
.sb-25 *::after {
  box-sizing: border-box;
}

.sb-25__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-25__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-25__bar {
  display: flex;
  align-items: center;
  gap: .75rem;
  inline-size: min(31rem,100%);
  min-block-size: 60px;
  padding-inline: 1.15rem .5rem;
  border: 1px solid var(--line);
  border-radius: 17px;
  background: var(--card);
  box-shadow: var(--e2);
  transition: box-shadow .26s cubic-bezier(.2,.9,.25,1), translate .26s cubic-bezier(.2,.9,.25,1), transform .26s cubic-bezier(.2,.9,.25,1), border-color .2s;
}

.sb-25__bar:hover {
  -webkit-transform: translateY(-2px);
  transform: translateY(-2px);
  translate: 0 -2px;
  box-shadow: var(--e3);
}

.sb-25__bar:focus-within {
  -webkit-transform: translateY(-2px);
  transform: translateY(-2px);
  translate: 0 -2px;
  border-color: var(--acc);
  box-shadow: var(--e3), 0 0 0 4px var(--wash);
}

.sb-25__ico {
  inline-size: 20px;
  block-size: 20px;
  flex: none;
  color: var(--muted);
  transition: color .2s;
}

.sb-25__bar:focus-within .sb-25__ico {
  color: var(--acc);
}

.sb-25__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 1rem/1 inherit;
}

.sb-25__input::placeholder {
  color: var(--muted);
}

.sb-25__input:focus {
  outline: none;
}

.sb-25__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-25__divider {
  inline-size: 1px;
  block-size: 24px;
  background: var(--line);
  flex: none;
}

.sb-25__filter {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  flex: none;
  border: 0;
  border-radius: 12px;
  background: none;
  color: var(--muted);
  cursor: pointer;
  transition: background .16s, color .16s;
}

.sb-25__filter:hover {
  background: #f2f4f8;
  color: var(--ink);
}

.sb-25__filter svg {
  inline-size: 19px;
  block-size: 19px;
}

.sb-25 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-25__input:focus-visible {
  outline: none;
}

.sb-25[data-theme="dark"] {
  --bg: #0a0c11;
  --card: #151923;
  --ink: #e9ecf3;
  --muted: #88909e;
  --line: #242c39;
  --acc: #7c9bff;
  --wash: rgba(124,155,255,.16);
  --ring: #7c9bff;
  --e1: 0 1px 2px rgba(0,0,0,.6);
  --e2: 0 1px 2px rgba(0,0,0,.6), 0 10px 24px -10px rgba(0,0,0,.8);
  --e3: 0 1px 2px rgba(0,0,0,.7), 0 18px 40px -14px rgba(0,0,0,.9), 0 0 0 1px rgba(124,155,255,.14);
  background: radial-gradient(40rem 24rem at 50% 22%, #171d29, transparent 70%), linear-gradient(180deg,#0e1219, var(--bg));
}

.sb-25[data-theme="dark"] .sb-25__filter:hover {
  background: #1d2430;
}

@media (prefers-color-scheme: dark) {
  .sb-25:not([data-theme="light"]) {
    --bg: #0a0c11;
    --card: #151923;
    --ink: #e9ecf3;
    --muted: #88909e;
    --line: #242c39;
    --acc: #7c9bff;
    --wash: rgba(124,155,255,.16);
    --ring: #7c9bff;
    --e1: 0 1px 2px rgba(0,0,0,.6);
    --e2: 0 1px 2px rgba(0,0,0,.6), 0 10px 24px -10px rgba(0,0,0,.8);
    --e3: 0 1px 2px rgba(0,0,0,.7), 0 18px 40px -14px rgba(0,0,0,.9), 0 0 0 1px rgba(124,155,255,.14);
    background: radial-gradient(40rem 24rem at 50% 22%, #171d29, transparent 70%), linear-gradient(180deg,#0e1219, var(--bg));
  }

  .sb-25:not([data-theme="light"]) .sb-25__filter:hover {
    background: #1d2430;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-25 *,
    .sb-25 *::before,
    .sb-25 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .sb-25__bar {
    border: 1px solid CanvasText;
    box-shadow: none;
  }
}

.sb-25__theme {
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

.sb-25[data-theme="dark"] .sb-25__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-25:not([data-theme="light"]) .sb-25__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-25__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-25[data-theme="dark"] .sb-25__theme:hover,
.sb-25:not([data-theme="light"]) .sb-25__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-25__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-25__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-25__sun {
  display: none;
}

.sb-25__theme[aria-pressed="true"] .sb-25__sun {
  display: block;
}

.sb-25__theme[aria-pressed="true"] .sb-25__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-25__theme {
    transition: none;
  }

  .sb-25__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-25');if(!r)return;const t=r.querySelector('.sb-25__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
