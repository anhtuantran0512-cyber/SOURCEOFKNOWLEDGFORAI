---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/inline-suggestions/"
title: "CSS Search Bar with Autocomplete Suggestions Dropdown"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "The plain, fast autocomplete: focus the field and five suggestions slide down under it, each with a category glyph and a keyboard-affordance chevron."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Search Bar with Autocomplete Suggestions Dropdown
Source: https://codefronts.com/components/css-search-boxes/inline-suggestions/

The plain, fast autocomplete: focus the field and five suggestions slide down under it, each with a category glyph and a keyboard-affordance chevron. No JavaScript — the panel is a :focus-within reveal, styled to sit flush with the input so the two read as one surface.
## HTML
```html
<div class="sb-15">
  <button class="sb-15__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-15__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-15__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-15__stage">
    <div class="sb-15__wrap" role="search">
      <div class="sb-15__field">
        <svg class="sb-15__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <label class="sb-15__vh" for="sb-15-input">Search workspace</label>
        <input class="sb-15__input" id="sb-15-input" type="search" placeholder="Search workspace&hellip;" autocomplete="off" aria-controls="sb-15-list">
      </div>
      <ul class="sb-15__panel" id="sb-15-list" role="listbox" aria-label="Suggestions">
        <li class="sb-15__row" role="option" aria-selected="false" style="--i:1">
          <span class="sb-15__glyph sb-15__glyph--doc" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M6 3.8h7.4L18 8.3v11.9H6z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M13 3.8v4.5h5" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></span>
          <span class="sb-15__txt">onboarding checklist</span>
          <svg class="sb-15__go" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M9 6.5 14.5 12 9 17.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </li>
        <li class="sb-15__row" role="option" aria-selected="false" style="--i:2">
          <span class="sb-15__glyph sb-15__glyph--file" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><rect x="3.6" y="6" width="16.8" height="13" rx="2.4" stroke="currentColor" stroke-width="1.6"/><path d="M3.6 9.6h16.8" stroke="currentColor" stroke-width="1.6"/></svg></span>
          <span class="sb-15__txt">Q3 revenue &mdash; final.xlsx</span>
          <svg class="sb-15__go" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M9 6.5 14.5 12 9 17.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </li>
        <li class="sb-15__row" role="option" aria-selected="false" style="--i:3">
          <span class="sb-15__glyph sb-15__glyph--person" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="12" cy="9" r="3.3" stroke="currentColor" stroke-width="1.6"/><path d="M5.8 19.2a6.2 6.2 0 0 1 12.4 0" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></span>
          <span class="sb-15__txt">Jordan Lee</span>
          <svg class="sb-15__go" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M9 6.5 14.5 12 9 17.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </li>
        <li class="sb-15__row" role="option" aria-selected="false" style="--i:4">
          <span class="sb-15__glyph sb-15__glyph--doc" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M6 3.8h7.4L18 8.3v11.9H6z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M13 3.8v4.5h5" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg></span>
          <span class="sb-15__txt">invoice template 2027</span>
          <svg class="sb-15__go" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M9 6.5 14.5 12 9 17.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </li>
        <li class="sb-15__row sb-15__row--all" role="option" aria-selected="false" style="--i:5">
          <span class="sb-15__glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.7"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg></span>
          <span class="sb-15__txt">See all results</span>
          <kbd class="sb-15__kbd">&crarr;</kbd>
        </li>
      </ul>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-15 {
  --bg: #f5f6f8;
  --card: #ffffff;
  --ink: #14161c;
  --muted: #6c7280;
  --line: #e4e6ec;
  --acc: #5b47f5;
  --wash: #f1efff;
  --doc: #5b47f5;
  --file: #0f9d76;
  --person: #e0642f;
  --ring: #5b47f5;
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

.sb-15 *,
.sb-15 *::before,
.sb-15 *::after {
  box-sizing: border-box;
}

.sb-15__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: start center;
  padding: clamp(2rem,14vh,8rem) clamp(1rem,4vw,3rem);
}

.sb-15__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-15__wrap {
  position: relative;
  inline-size: min(29rem,100%);
}

.sb-15__field {
  display: flex;
  align-items: center;
  gap: .7rem;
  min-block-size: 52px;
  padding-inline: 1rem;
  border: 1px solid var(--line);
  border-radius: 13px;
  background: var(--card);
  box-shadow: 0 1px 2px rgba(20,22,28,.05);
  transition: border-color .2s, box-shadow .2s, border-radius .2s;
}

.sb-15__wrap:focus-within .sb-15__field {
  border-color: var(--acc);
  box-shadow: 0 0 0 4px rgba(91,71,245,.14);
  border-end-start-radius: 0;
  border-end-end-radius: 0;
}

.sb-15__ico {
  inline-size: 19px;
  block-size: 19px;
  flex: none;
  color: var(--muted);
  transition: color .2s;
}

.sb-15__wrap:focus-within .sb-15__ico {
  color: var(--acc);
}

.sb-15__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .96rem/1 inherit;
}

.sb-15__input::placeholder {
  color: var(--muted);
}

.sb-15__input:focus {
  outline: none;
}

.sb-15__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-15__panel {
  position: absolute;
  inset-inline: 0;
  inset-block-start: calc(100% - 1px);
  z-index: 5;
  list-style: none;
  margin: 0;
  padding: .35rem;
  max-block-size: min(22rem,52vh);
  overflow: auto;
  border: 1px solid var(--acc);
  border-block-start: 0;
  border-radius: 0 0 13px 13px;
  background: var(--card);
  box-shadow: 0 22px 44px -20px var(--shadow);
  opacity: 0;
  translate: 0 -6px;
  visibility: hidden;
  transition: opacity .2s cubic-bezier(.2,.9,.25,1), translate .2s cubic-bezier(.2,.9,.25,1), visibility .2s;
}

.sb-15__wrap:focus-within .sb-15__panel {
  opacity: 1;
  translate: 0 0;
  visibility: visible;
}

.sb-15__row {
  display: flex;
  align-items: center;
  gap: .7rem;
  min-block-size: 46px;
  padding: 0 .6rem;
  border-radius: 9px;
  cursor: pointer;
  font: 500 .92rem/1.3 inherit;
  text-wrap: pretty;
  opacity: 0;
  translate: 0 5px;
  transition: opacity .24s, translate .24s, background .14s;
}

.sb-15__wrap:focus-within .sb-15__row {
  opacity: 1;
  translate: 0 0;
  transition-delay: calc(var(--i,0) * 24ms);
}

.sb-15__row:hover,
.sb-15__row[aria-selected="true"] {
  background: var(--wash);
}

.sb-15__row--all {
  color: var(--acc);
  font-weight: 600;
}

.sb-15__glyph {
  display: grid;
  place-items: center;
  inline-size: 28px;
  block-size: 28px;
  flex: none;
  border-radius: 8px;
  background: #f2f3f7;
  color: var(--muted);
}

.sb-15__glyph svg {
  inline-size: 16px;
  block-size: 16px;
}

.sb-15__glyph--doc {
  color: var(--doc);
  background: color-mix(in srgb, var(--doc) 10%, white);
}

.sb-15__glyph--file {
  color: var(--file);
  background: color-mix(in srgb, var(--file) 10%, white);
}

.sb-15__glyph--person {
  color: var(--person);
  background: color-mix(in srgb, var(--person) 10%, white);
}

.sb-15__txt {
  flex: 1;
  min-inline-size: 0;
}

.sb-15__go {
  inline-size: 15px;
  block-size: 15px;
  color: var(--muted);
  opacity: 0;
  transition: opacity .16s, translate .16s;
  translate: -3px 0;
}

.sb-15__row:hover .sb-15__go {
  opacity: 1;
  translate: 0 0;
}

.sb-15__kbd {
  display: inline-grid;
  place-items: center;
  min-inline-size: 1.5rem;
  block-size: 1.5rem;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: #fafbfc;
  color: var(--muted);
  font: 500 .74rem/1 ui-monospace,Menlo,monospace;
}

@supports selector(:has(*)) {
  .sb-15__wrap:has(.sb-15__input:placeholder-shown):focus-within .sb-15__panel {
    opacity: 0;
    translate: 0 -6px;
    visibility: hidden;
  }
}

.sb-15 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-15__input:focus-visible {
  outline: none;
}

.sb-15[data-theme="dark"] {
  --bg: #0b0d13;
  --card: #141720;
  --ink: #eceef4;
  --muted: #868d9c;
  --line: #222736;
  --wash: rgba(122,105,255,.14);
  --acc: #7a69ff;
  --doc: #9d8cff;
  --file: #34d3a6;
  --person: #ff8f5e;
  --ring: #7a69ff;
  --shadow: rgba(0,0,0,.7);
}

.sb-15[data-theme="dark"] .sb-15__glyph {
  background: #1b2130;
}

.sb-15[data-theme="dark"] .sb-15__glyph--doc,
.sb-15[data-theme="dark"] .sb-15__glyph--file,
.sb-15[data-theme="dark"] .sb-15__glyph--person {
  background: rgba(255,255,255,.05);
}

.sb-15[data-theme="dark"] .sb-15__kbd {
  background: #1b2130;
}

@media (prefers-color-scheme: dark) {
  .sb-15:not([data-theme="light"]) {
    --bg: #0b0d13;
    --card: #141720;
    --ink: #eceef4;
    --muted: #868d9c;
    --line: #222736;
    --wash: rgba(122,105,255,.14);
    --acc: #7a69ff;
    --doc: #9d8cff;
    --file: #34d3a6;
    --person: #ff8f5e;
    --ring: #7a69ff;
    --shadow: rgba(0,0,0,.7);
  }

  .sb-15:not([data-theme="light"]) .sb-15__glyph {
    background: #1b2130;
  }

  .sb-15:not([data-theme="light"]) .sb-15__glyph--doc,
    .sb-15:not([data-theme="light"]) .sb-15__glyph--file,
    .sb-15:not([data-theme="light"]) .sb-15__glyph--person {
    background: rgba(255,255,255,.05);
  }

  .sb-15:not([data-theme="light"]) .sb-15__kbd {
    background: #1b2130;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-15 *,
    .sb-15 *::before,
    .sb-15 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .sb-15__field,
    .sb-15__panel {
    border: 1px solid CanvasText;
  }
}

.sb-15__theme {
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

.sb-15[data-theme="dark"] .sb-15__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-15:not([data-theme="light"]) .sb-15__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-15__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-15[data-theme="dark"] .sb-15__theme:hover,
.sb-15:not([data-theme="light"]) .sb-15__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-15__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-15__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-15__sun {
  display: none;
}

.sb-15__theme[aria-pressed="true"] .sb-15__sun {
  display: block;
}

.sb-15__theme[aria-pressed="true"] .sb-15__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-15__theme {
    transition: none;
  }

  .sb-15__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-15');if(!r)return;const t=r.querySelector('.sb-15__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
