---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/minimal-underline/"
title: "Minimal CSS Search Bar with Animated Underline"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "A borderless, editorial search field: no box, no shadow, just type on a hairline that draws itself outward from the centre on focus."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimal CSS Search Bar with Animated Underline
Source: https://codefronts.com/components/css-search-boxes/minimal-underline/

A borderless, editorial search field: no box, no shadow, just type on a hairline that draws itself outward from the centre on focus. Two stacked rules — a static hairline and an accent line scaled with transform: scaleX() — give a 60fps underline with zero layout cost.
## HTML
```html
<div class="sb-06">
  <button class="sb-06__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-06__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-06__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-06__stage">
    <div class="sb-06__wrap" role="search">
      <div class="sb-06__field">
        <svg class="sb-06__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.2" stroke="currentColor" stroke-width="1.5"/><path d="m15.8 15.8 4.4 4.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
        <label class="sb-06__vh" for="sb-06-input">Search the archive</label>
        <input class="sb-06__input" id="sb-06-input" type="search" placeholder="Search the archive" autocomplete="off">
        <kbd class="sb-06__enter">&crarr;</kbd>
      </div>
      <p class="sb-06__meta"><span>1,284 essays</span><span>&middot;</span><span>Updated weekly</span></p>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&display=swap');

.sb-06 {
  --bg: #fbfaf7;
  --ink: #14140f;
  --muted: #8a8778;
  --line: #14140f;
  --acc: #b8451f;
  --ring: #b8451f;
  --display: "Instrument Serif",ui-serif,Georgia,"Times New Roman",serif;
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

.sb-06 *,
.sb-06 *::before,
.sb-06 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% .1 40)) {
  .sb-06 {
    --bg: oklch(98% .008 85);
    --ink: oklch(18% .01 85);
    --muted: oklch(62% .015 85);
    --acc: oklch(52% .16 36);
  }
}

.sb-06__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,5vw,4rem);
}

.sb-06__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-06__wrap {
  inline-size: min(38rem,100%);
}

.sb-06__field {
  position: relative;
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: .9rem;
  padding-block: .65rem 1.05rem;
}

.sb-06__field::before,
.sb-06__field::after {
  content: '';
  position: absolute;
  inset-inline: 0;
  inset-block-end: 0;
}

.sb-06__field::before {
  block-size: 1px;
  background: var(--line);
  opacity: .22;
}

.sb-06__field::after {
  block-size: 2px;
  background: var(--acc);
  opacity: 0;
  -webkit-transform: scaleX(0);
  transform: scaleX(0);
  scale: 0 1;
  transform-origin: center;
  transition: scale .32s cubic-bezier(.2,.9,.25,1), transform .32s cubic-bezier(.2,.9,.25,1), opacity .18s;
}

.sb-06__field:focus-within::after {
  opacity: 1;
  -webkit-transform: scaleX(1);
  transform: scaleX(1);
  scale: 1 1;
}

.sb-06__ico {
  inline-size: 22px;
  block-size: 22px;
  color: var(--muted);
  transition: color .25s;
}

.sb-06__field:focus-within .sb-06__ico {
  color: var(--acc);
}

.sb-06__input {
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  padding: 0;
  font-family: var(--display);
  font-size: clamp(1.6rem,5vw,2.6rem);
  font-weight: 400;
  line-height: 1.1;
}

.sb-06__input::placeholder {
  color: var(--muted);
  font-style: italic;
  opacity: 1;
}

.sb-06__input:focus {
  outline: none;
}

.sb-06__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-06__enter {
  display: grid;
  place-items: center;
  inline-size: 2rem;
  block-size: 2rem;
  border: 1px solid rgba(20,20,15,.16);
  border-radius: 8px;
  color: var(--muted);
  font: 400 .85rem/1 ui-monospace,Menlo,monospace;
  opacity: 0;
  translate: 6px 0;
  transition: opacity .22s, translate .22s;
}

.sb-06__input:not(:placeholder-shown) ~ .sb-06__enter {
  opacity: 1;
  translate: 0 0;
}

.sb-06__meta {
  display: flex;
  gap: .55rem;
  margin: .85rem .1rem 0;
  color: var(--muted);
  font: 400 .8rem/1 inherit;
  letter-spacing: .02em;
}

.sb-06 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 4px;
}

.sb-06__input:focus-visible {
  outline: none;
}

.sb-06[data-theme="dark"] {
  --bg: #12110f;
  --ink: #f4f1ea;
  --muted: #8f8a7d;
  --line: #f4f1ea;
  --acc: #ff8a5b;
  --ring: #ff8a5b;
}

.sb-06[data-theme="dark"] .sb-06__enter {
  border-color: rgba(244,241,234,.2);
}

@media (prefers-color-scheme: dark) {
  .sb-06:not([data-theme="light"]) {
    --bg: #12110f;
    --ink: #f4f1ea;
    --muted: #8f8a7d;
    --line: #f4f1ea;
    --acc: #ff8a5b;
    --ring: #ff8a5b;
  }

  .sb-06:not([data-theme="light"]) .sb-06__enter {
    border-color: rgba(244,241,234,.2);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-06 *,
    .sb-06 *::before,
    .sb-06 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .sb-06__field::before {
    background: CanvasText;
  }

  .sb-06__field:focus-within::after {
    background: Highlight;
    opacity: 1;
  }
}

.sb-06__theme {
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

.sb-06[data-theme="dark"] .sb-06__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-06:not([data-theme="light"]) .sb-06__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-06__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-06[data-theme="dark"] .sb-06__theme:hover,
.sb-06:not([data-theme="light"]) .sb-06__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-06__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-06__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-06__sun {
  display: none;
}

.sb-06__theme[aria-pressed="true"] .sb-06__sun {
  display: block;
}

.sb-06__theme[aria-pressed="true"] .sb-06__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-06__theme {
    transition: none;
  }

  .sb-06__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-06');if(!r)return;const t=r.querySelector('.sb-06__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
