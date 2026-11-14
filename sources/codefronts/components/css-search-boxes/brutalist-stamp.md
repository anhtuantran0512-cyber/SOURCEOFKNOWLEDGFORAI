---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/brutalist-stamp/"
title: "Neo-Brutalist CSS Search Bar with Offset Stamp"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "Chunky 3px borders, zero-blur offset shadows, unapologetic yellow, and a rotated SEARCH stamp that snaps flat when you focus."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neo-Brutalist CSS Search Bar with Offset Stamp
Source: https://codefronts.com/components/css-search-boxes/brutalist-stamp/

Chunky 3px borders, zero-blur offset shadows, unapologetic yellow, and a rotated SEARCH stamp that snaps flat when you focus. The press interaction is the one everyone gets wrong: the shadow shrinks by exactly the distance the element moves, so the object looks pressed rather than shifted.
## HTML
```html
<div class="sb-21">
  <button class="sb-21__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-21__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-21__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-21__stage">
    <div class="sb-21__panel">
      <span class="sb-21__stamp" aria-hidden="true">SEARCH</span>
      <div class="sb-21__bar" role="search">
        <label class="sb-21__vh" for="sb-21-input">Search the catalogue</label>
        <input class="sb-21__input" id="sb-21-input" type="search" placeholder="TYPE SOMETHING" autocomplete="off">
        <button class="sb-21__go" type="button">
          GO
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 12h14m-6-6 6 6-6 6" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
      </div>
      <div class="sb-21__tags">
        <button class="sb-21__tag" type="button">POSTERS</button>
        <button class="sb-21__tag" type="button">TYPE</button>
        <button class="sb-21__tag" type="button">ZINES</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-21 {
  --paper: #f5f0e4;
  --ink: #0f0f0f;
  --pop: #ffe600;
  --pop2: #ff5c38;
  --card: #ffffff;
  --bd: 3px;
  --ring: #0f0f0f;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: ui-monospace,"SF Mono",Menlo,Consolas,monospace;
  color: var(--ink);
  background: repeating-linear-gradient(45deg, rgba(15,15,15,.045) 0 2px, transparent 2px 11px), var(--paper);
  -webkit-font-smoothing: antialiased;
}

.sb-21 *,
.sb-21 *::before,
.sb-21 *::after {
  box-sizing: border-box;
}

.sb-21__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,5vw,3rem);
}

.sb-21__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-21__panel {
  position: relative;
  inline-size: min(32rem,100%);
  padding: clamp(1.1rem,3vw,1.6rem);
  border: var(--bd) solid var(--ink);
  border-radius: 2px;
  background: var(--card);
  box-shadow: 9px 9px 0 var(--ink);
}

.sb-21__stamp {
  position: absolute;
  inset-block-start: -.95rem;
  inset-inline-end: 1.2rem;
  padding: .3rem .7rem;
  border: var(--bd) solid var(--ink);
  background: var(--pop);
  font: 700 .78rem/1 inherit;
  letter-spacing: .22em;
  -webkit-transform: rotate(-6deg);
  transform: rotate(-6deg);
  rotate: -6deg;
  box-shadow: 4px 4px 0 var(--ink);
  transition: rotate .16s cubic-bezier(.2,.9,.25,1), transform .16s cubic-bezier(.2,.9,.25,1), background .16s;
}

.sb-21__panel:focus-within .sb-21__stamp {
  -webkit-transform: none;
  transform: none;
  rotate: 0deg;
  background: var(--pop2);
}

.sb-21__bar {
  display: flex;
  align-items: stretch;
  gap: .7rem;
  margin-block-start: .4rem;
}

.sb-21__input {
  flex: 1;
  min-inline-size: 0;
  min-block-size: 54px;
  padding-inline: .9rem;
  border: var(--bd) solid var(--ink);
  border-radius: 0;
  background: var(--card);
  color: var(--ink);
  font: 600 1rem/1 inherit;
  letter-spacing: .04em;
  box-shadow: 5px 5px 0 var(--ink);
  transition: translate .12s, box-shadow .12s;
}

.sb-21__input::placeholder {
  color: rgba(15,15,15,.45);
  letter-spacing: .12em;
}

.sb-21__input:focus {
  outline: none;
  translate: 2px 2px;
  box-shadow: 3px 3px 0 var(--ink);
  background: var(--pop);
}

.sb-21__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-21__go {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  flex: none;
  min-block-size: 54px;
  padding-inline: 1.05rem;
  border: var(--bd) solid var(--ink);
  border-radius: 0;
  background: var(--pop2);
  color: var(--ink);
  cursor: pointer;
  font: 700 .95rem/1 inherit;
  letter-spacing: .1em;
  box-shadow: 5px 5px 0 var(--ink);
  transition: translate .12s, box-shadow .12s, background .16s;
}

.sb-21__go:hover {
  background: var(--pop);
}

.sb-21__go:active {
  translate: 5px 5px;
  box-shadow: 0 0 0 var(--ink);
}

.sb-21__go svg {
  inline-size: 18px;
  block-size: 18px;
}

.sb-21__tags {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  margin-block-start: 1rem;
}

.sb-21__tag {
  min-block-size: 36px;
  padding-inline: .75rem;
  border: 2px solid var(--ink);
  border-radius: 0;
  background: var(--card);
  color: var(--ink);
  cursor: pointer;
  font: 700 .74rem/1 inherit;
  letter-spacing: .12em;
  box-shadow: 3px 3px 0 var(--ink);
  transition: translate .12s, box-shadow .12s, background .16s;
}

.sb-21__tag:hover {
  background: var(--pop);
}

.sb-21__tag:active {
  translate: 3px 3px;
  box-shadow: 0 0 0 var(--ink);
}

.sb-21 :focus-visible {
  outline: 3px solid var(--ring);
  outline-offset: 3px;
}

.sb-21[data-theme="dark"] {
  --paper: #141414;
  --ink: #f4f1e8;
  --card: #1d1d1d;
  --pop: #ffe600;
  --pop2: #41d6a1;
  --ring: #ffe600;
  background: repeating-linear-gradient(45deg, rgba(244,241,232,.05) 0 2px, transparent 2px 11px), var(--paper);
}

.sb-21[data-theme="dark"] .sb-21__input:focus,
.sb-21[data-theme="dark"] .sb-21__go,
.sb-21[data-theme="dark"] .sb-21__tag:hover,
.sb-21[data-theme="dark"] .sb-21__stamp {
  color: #141414;
}

.sb-21[data-theme="dark"] .sb-21__input::placeholder {
  color: rgba(244,241,232,.45);
}

@media (prefers-color-scheme: dark) {
  .sb-21:not([data-theme="light"]) {
    --paper: #141414;
    --ink: #f4f1e8;
    --card: #1d1d1d;
    --pop: #ffe600;
    --pop2: #41d6a1;
    --ring: #ffe600;
    background: repeating-linear-gradient(45deg, rgba(244,241,232,.05) 0 2px, transparent 2px 11px), var(--paper);
  }

  .sb-21:not([data-theme="light"]) .sb-21__input:focus,
    .sb-21:not([data-theme="light"]) .sb-21__go,
    .sb-21:not([data-theme="light"]) .sb-21__tag:hover,
    .sb-21:not([data-theme="light"]) .sb-21__stamp {
    color: #141414;
  }

  .sb-21:not([data-theme="light"]) .sb-21__input::placeholder {
    color: rgba(244,241,232,.45);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-21 *,
    .sb-21 *::before,
    .sb-21 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .sb-21__panel,
    .sb-21__input,
    .sb-21__go,
    .sb-21__tag,
    .sb-21__stamp {
    border: 2px solid CanvasText;
    box-shadow: none;
  }
}

.sb-21__theme {
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

.sb-21[data-theme="dark"] .sb-21__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-21:not([data-theme="light"]) .sb-21__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-21__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-21[data-theme="dark"] .sb-21__theme:hover,
.sb-21:not([data-theme="light"]) .sb-21__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-21__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-21__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-21__sun {
  display: none;
}

.sb-21__theme[aria-pressed="true"] .sb-21__sun {
  display: block;
}

.sb-21__theme[aria-pressed="true"] .sb-21__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-21__theme {
    transition: none;
  }

  .sb-21__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-21');if(!r)return;const t=r.querySelector('.sb-21__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
