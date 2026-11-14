---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/compact-toolbar/"
title: "Compact Toolbar CSS Search Bar (Docs / Wiki)"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "A 200px search sized for a documentation sidebar: small type, tight 36px height, a quiet border that only asserts itself on focus, and a version chip below."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Compact Toolbar CSS Search Bar (Docs / Wiki)
Source: https://codefronts.com/components/css-search-boxes/compact-toolbar/

A 200px search sized for a documentation sidebar: small type, tight 36px height, a quiet border that only asserts itself on focus, and a version chip below. Built as part of a real nav so you can see the density it is designed for.
## HTML
```html
<div class="sb-22">
  <button class="sb-22__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-22__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-22__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-22__stage">
    <aside class="sb-22__side">
      <div class="sb-22__brandrow">
        <span class="sb-22__brand"><span class="sb-22__mark" aria-hidden="true"></span>Docs</span>
        <span class="sb-22__ver">v4.2</span>
      </div>

      <div class="sb-22__search" role="search">
        <svg class="sb-22__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.2" stroke="currentColor" stroke-width="1.8"/><path d="m15.8 15.8 4.4 4.4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <label class="sb-22__vh" for="sb-22-input">Search documentation</label>
        <input class="sb-22__input" id="sb-22-input" type="search" placeholder="Search docs" autocomplete="off">
      </div>

      <nav class="sb-22__nav" aria-label="Documentation">
        <p class="sb-22__label">Getting started</p>
        <a class="sb-22__link" href="#sb-22-input">Installation</a>
        <a class="sb-22__link" href="#sb-22-input" aria-current="page">Quick start</a>
        <a class="sb-22__link" href="#sb-22-input">Project structure</a>
        <p class="sb-22__label">Core concepts</p>
        <a class="sb-22__link" href="#sb-22-input">Routing</a>
        <a class="sb-22__link" href="#sb-22-input">Data fetching</a>
        <a class="sb-22__link" href="#sb-22-input">Caching</a>
        <p class="sb-22__label">API reference</p>
        <a class="sb-22__link" href="#sb-22-input">CLI</a>
        <a class="sb-22__link" href="#sb-22-input">Config</a>
      </nav>
    </aside>
  </div>
</div>
```
## CSS
```css
.sb-22 {
  --bg: #f8f9fa;
  --card: #ffffff;
  --ink: #1c2024;
  --muted: #697077;
  --line: #e6e8eb;
  --acc: #3b7ddd;
  --wash: rgba(59,125,221,.14);
  --ring: #3b7ddd;
  --shadow: rgba(28,32,36,.12);
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

.sb-22 *,
.sb-22 *::before,
.sb-22 *::after {
  box-sizing: border-box;
}

.sb-22__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-22__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-22__side {
  inline-size: min(15rem,100%);
  max-block-size: min(30rem,82svh);
  overflow: auto;
  padding: .9rem;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--card);
  box-shadow: 0 20px 44px -30px var(--shadow), 0 1px 2px rgba(28,32,36,.04);
  scrollbar-width: thin;
  scrollbar-color: #cfd4da transparent;
  scrollbar-gutter: stable;
}

.sb-22__side::-webkit-scrollbar {
  inline-size: 8px;
}

.sb-22__side::-webkit-scrollbar-thumb {
  background: #cfd4da;
  border-radius: 99px;
}

.sb-22__brandrow {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .5rem;
  margin-block-end: .75rem;
}

.sb-22__brand {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  font: 700 .88rem/1 inherit;
  letter-spacing: -.01em;
}

.sb-22__mark {
  inline-size: 16px;
  block-size: 16px;
  border-radius: 5px;
  background: linear-gradient(135deg, var(--acc), #7c3aed);
}

.sb-22__ver {
  padding: .16rem .35rem;
  border-radius: 5px;
  background: var(--wash);
  color: var(--acc);
  font: 600 .66rem/1 inherit;
  font-variant-numeric: tabular-nums;
}

.sb-22__search {
  display: flex;
  align-items: center;
  gap: .45rem;
  min-block-size: 36px;
  padding-inline: .55rem;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #fbfcfd;
  transition: border-color .18s, box-shadow .18s, background .18s;
}

.sb-22__search:hover {
  border-color: #d6dade;
}

.sb-22__search:focus-within {
  border-color: var(--acc);
  background: var(--card);
  box-shadow: 0 0 0 3px var(--wash);
}

.sb-22__ico {
  inline-size: 15px;
  block-size: 15px;
  flex: none;
  color: var(--muted);
}

.sb-22__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .82rem/1 inherit;
}

.sb-22__input::placeholder {
  color: var(--muted);
}

.sb-22__input:focus {
  outline: none;
}

.sb-22__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-22__nav {
  display: flex;
  flex-direction: column;
  gap: 1px;
  margin-block-start: 1rem;
}

.sb-22__label {
  margin: .85rem .35rem .3rem;
  color: var(--muted);
  font: 600 .66rem/1 inherit;
  letter-spacing: .1em;
  text-transform: uppercase;
}

.sb-22__label:first-child {
  margin-block-start: 0;
}

.sb-22__link {
  display: flex;
  align-items: center;
  min-block-size: 28px;
  padding-inline: .5rem;
  border-radius: 7px;
  color: var(--muted);
  text-decoration: none;
  font: 400 .82rem/1 inherit;
  transition: background .14s, color .14s;
}

.sb-22__link:hover {
  background: #f2f4f6;
  color: var(--ink);
}

.sb-22__link[aria-current="page"] {
  background: var(--wash);
  color: var(--acc);
  font-weight: 600;
}

.sb-22 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-22__input:focus-visible {
  outline: none;
}

.sb-22[data-theme="dark"] {
  --bg: #0c0e11;
  --card: #14171b;
  --ink: #e7eaee;
  --muted: #868e97;
  --line: #232830;
  --acc: #6ea8fe;
  --wash: rgba(110,168,254,.14);
  --ring: #6ea8fe;
  --shadow: rgba(0,0,0,.7);
}

.sb-22[data-theme="dark"] .sb-22__search {
  background: #101317;
}

.sb-22[data-theme="dark"] .sb-22__link:hover {
  background: #1b2027;
}

.sb-22[data-theme="dark"] .sb-22__side {
  scrollbar-color: #2c333c transparent;
}

@media (prefers-color-scheme: dark) {
  .sb-22:not([data-theme="light"]) {
    --bg: #0c0e11;
    --card: #14171b;
    --ink: #e7eaee;
    --muted: #868e97;
    --line: #232830;
    --acc: #6ea8fe;
    --wash: rgba(110,168,254,.14);
    --ring: #6ea8fe;
    --shadow: rgba(0,0,0,.7);
  }

  .sb-22:not([data-theme="light"]) .sb-22__search {
    background: #101317;
  }

  .sb-22:not([data-theme="light"]) .sb-22__link:hover {
    background: #1b2027;
  }

  .sb-22:not([data-theme="light"]) .sb-22__side {
    scrollbar-color: #2c333c transparent;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-22 *,
    .sb-22 *::before,
    .sb-22 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .sb-22__side,
    .sb-22__search {
    border: 1px solid CanvasText;
  }

  .sb-22__link[aria-current="page"] {
    outline: 1px solid Highlight;
  }
}

.sb-22__theme {
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

.sb-22[data-theme="dark"] .sb-22__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-22:not([data-theme="light"]) .sb-22__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-22__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-22[data-theme="dark"] .sb-22__theme:hover,
.sb-22:not([data-theme="light"]) .sb-22__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-22__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-22__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-22__sun {
  display: none;
}

.sb-22__theme[aria-pressed="true"] .sb-22__sun {
  display: block;
}

.sb-22__theme[aria-pressed="true"] .sb-22__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-22__theme {
    transition: none;
  }

  .sb-22__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-22');if(!r)return;const t=r.querySelector('.sb-22__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
