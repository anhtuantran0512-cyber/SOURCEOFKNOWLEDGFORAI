---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/side-indicator/"
title: "CSS Search Bar with Side Category Indicator"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "A colour-coded search: pick Files, People, Messages or Code and a vertical bar on the input's leading edge changes colour and label to match."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Search Bar with Side Category Indicator
Source: https://codefronts.com/components/css-search-boxes/side-indicator/

A colour-coded search: pick Files, People, Messages or Code and a vertical bar on the input's leading edge changes colour and label to match. The state machine is a radio group read by :has() — no JavaScript, and the whole thing stays keyboard-operable because the controls are real radios.
## HTML
```html
<div class="sb-24">
  <button class="sb-24__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-24__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-24__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-24__stage">
    <div class="sb-24__wrap">
      <input class="sb-24__vh" type="radio" name="sb-24-cat" id="sb-24-files" checked>
      <input class="sb-24__vh" type="radio" name="sb-24-cat" id="sb-24-people">
      <input class="sb-24__vh" type="radio" name="sb-24-cat" id="sb-24-msgs">
      <input class="sb-24__vh" type="radio" name="sb-24-cat" id="sb-24-code">

      <div class="sb-24__seg" role="group" aria-label="Search category">
        <label class="sb-24__segbtn" for="sb-24-files">Files</label>
        <label class="sb-24__segbtn" for="sb-24-people">People</label>
        <label class="sb-24__segbtn" for="sb-24-msgs">Messages</label>
        <label class="sb-24__segbtn" for="sb-24-code">Code</label>
      </div>

      <div class="sb-24__bar" role="search">
        <span class="sb-24__scope">
          <svg class="sb-24__glyph sb-24__glyph--files" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 6.5h5.6l1.6 2H20v9.5H4z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
          <svg class="sb-24__glyph sb-24__glyph--people" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="9" r="3.3" stroke="currentColor" stroke-width="1.7"/><path d="M5.8 19.2a6.2 6.2 0 0 1 12.4 0" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          <svg class="sb-24__glyph sb-24__glyph--msgs" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 5.5h14v10H9.5L5 19z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
          <svg class="sb-24__glyph sb-24__glyph--code" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m9 8-4 4 4 4m6-8 4 4-4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <span class="sb-24__scopetxt"></span>
        </span>
        <label class="sb-24__vh" for="sb-24-input">Search within the selected category</label>
        <input class="sb-24__input" id="sb-24-input" type="search" placeholder="Search&hellip;" autocomplete="off">
        <kbd class="sb-24__kbd">&crarr;</kbd>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-24 {
  --bg: #f5f6f8;
  --card: #ffffff;
  --ink: #14171d;
  --muted: #6b7280;
  --line: #e4e6ec;
  --cat: #2563eb;
  --cat-wash: rgba(37,99,235,.12);
  --ring: #14171d;
  --shadow: rgba(20,23,29,.14);
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

.sb-24 *,
.sb-24 *::before,
.sb-24 *::after {
  box-sizing: border-box;
}

.sb-24__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-24__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-24__wrap {
  inline-size: min(32rem,100%);
  display: flex;
  flex-direction: column;
  gap: .85rem;
}

.sb-24__seg {
  display: flex;
  gap: .25rem;
  padding: .25rem;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--card);
  align-self: start;
}

.sb-24__segbtn {
  display: inline-flex;
  align-items: center;
  min-block-size: 34px;
  padding-inline: .7rem;
  border-radius: 9px;
  color: var(--muted);
  cursor: pointer;
  font: 600 .8rem/1 inherit;
  transition: background .16s, color .16s;
}

.sb-24__segbtn:hover {
  background: #f2f3f6;
  color: var(--ink);
}

.sb-24__bar {
  position: relative;
  display: flex;
  align-items: center;
  gap: .6rem;
  min-block-size: 56px;
  padding-inline: 1.05rem .5rem;
  overflow: hidden;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--card);
  box-shadow: 0 1px 2px rgba(20,23,29,.05);
  transition: border-color .2s, box-shadow .2s;
}

.sb-24__bar::before {
  content: '';
  position: absolute;
  inset-block: .5rem;
  inset-inline-start: 0;
  inline-size: 4px;
  border-start-end-radius: 4px;
  border-end-end-radius: 4px;
  background: var(--cat);
  transition: background .22s cubic-bezier(.2,.9,.25,1), inset-block .22s;
}

.sb-24__bar:focus-within {
  border-color: var(--cat);
  box-shadow: 0 0 0 4px var(--cat-wash);
}

.sb-24__bar:focus-within::before {
  inset-block: 0;
}

.sb-24__scope {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  flex: none;
  padding: .3rem .55rem;
  border-radius: 8px;
  background: var(--cat-wash);
  color: var(--cat);
  font: 600 .78rem/1 inherit;
}

.sb-24__glyph {
  display: none;
  inline-size: 15px;
  block-size: 15px;
}

.sb-24__scopetxt::after {
  content: 'Files';
}

.sb-24__glyph--files {
  display: block;
}

.sb-24__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .96rem/1 inherit;
}

.sb-24__input::placeholder {
  color: var(--muted);
}

.sb-24__input:focus {
  outline: none;
}

.sb-24__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-24__kbd {
  display: inline-grid;
  place-items: center;
  inline-size: 1.9rem;
  block-size: 1.9rem;
  flex: none;
  border: 1px solid var(--line);
  border-radius: 7px;
  background: #fafbfc;
  color: var(--muted);
  font: 500 .8rem/1 ui-monospace,Menlo,monospace;
}

.sb-24 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-24__input:focus-visible {
  outline: none;
}

@supports selector(:has(*)) {
  .sb-24:has(#sb-24-files:checked) .sb-24__segbtn[for="sb-24-files"],
    .sb-24:has(#sb-24-people:checked) .sb-24__segbtn[for="sb-24-people"],
    .sb-24:has(#sb-24-msgs:checked) .sb-24__segbtn[for="sb-24-msgs"],
    .sb-24:has(#sb-24-code:checked) .sb-24__segbtn[for="sb-24-code"] {
    background: var(--cat-wash);
    color: var(--cat);
  }

  .sb-24:has(#sb-24-people:checked) {
    --cat: #16a34a;
    --cat-wash: rgba(22,163,74,.13);
  }

  .sb-24:has(#sb-24-msgs:checked) {
    --cat: #ea580c;
    --cat-wash: rgba(234,88,12,.13);
  }

  .sb-24:has(#sb-24-code:checked) {
    --cat: #7c3aed;
    --cat-wash: rgba(124,58,237,.13);
  }

  .sb-24:has(#sb-24-people:checked) .sb-24__glyph--files,
    .sb-24:has(#sb-24-msgs:checked) .sb-24__glyph--files,
    .sb-24:has(#sb-24-code:checked) .sb-24__glyph--files {
    display: none;
  }

  .sb-24:has(#sb-24-people:checked) .sb-24__glyph--people {
    display: block;
  }

  .sb-24:has(#sb-24-msgs:checked) .sb-24__glyph--msgs {
    display: block;
  }

  .sb-24:has(#sb-24-code:checked) .sb-24__glyph--code {
    display: block;
  }

  .sb-24:has(#sb-24-people:checked) .sb-24__scopetxt::after {
    content: 'People';
  }

  .sb-24:has(#sb-24-msgs:checked) .sb-24__scopetxt::after {
    content: 'Messages';
  }

  .sb-24:has(#sb-24-code:checked) .sb-24__scopetxt::after {
    content: 'Code';
  }

  .sb-24:has(#sb-24-files:focus-visible) .sb-24__segbtn[for="sb-24-files"],
    .sb-24:has(#sb-24-people:focus-visible) .sb-24__segbtn[for="sb-24-people"],
    .sb-24:has(#sb-24-msgs:focus-visible) .sb-24__segbtn[for="sb-24-msgs"],
    .sb-24:has(#sb-24-code:focus-visible) .sb-24__segbtn[for="sb-24-code"] {
    outline: 2px solid var(--ring);
    outline-offset: 2px;
  }
}

.sb-24[data-theme="dark"] {
  --bg: #0b0e13;
  --card: #141821;
  --ink: #e9edf4;
  --muted: #878f9d;
  --line: #232a36;
  --ring: #e9edf4;
  --shadow: rgba(0,0,0,.7);
  --cat: #60a5fa;
  --cat-wash: rgba(96,165,250,.16);
}

.sb-24[data-theme="dark"] .sb-24__segbtn:hover {
  background: #1b2230;
}

.sb-24[data-theme="dark"] .sb-24__kbd {
  background: #1a2029;
}

@media (prefers-color-scheme: dark) {
  .sb-24:not([data-theme="light"]) {
    --bg: #0b0e13;
    --card: #141821;
    --ink: #e9edf4;
    --muted: #878f9d;
    --line: #232a36;
    --ring: #e9edf4;
    --shadow: rgba(0,0,0,.7);
    --cat: #60a5fa;
    --cat-wash: rgba(96,165,250,.16);
  }

  .sb-24:not([data-theme="light"]) .sb-24__segbtn:hover {
    background: #1b2230;
  }

  .sb-24:not([data-theme="light"]) .sb-24__kbd {
    background: #1a2029;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-24 *,
    .sb-24 *::before,
    .sb-24 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .sb-24__bar,
    .sb-24__seg {
    border: 1px solid CanvasText;
  }

  .sb-24__bar::before {
    background: Highlight;
  }
}

.sb-24__theme {
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

.sb-24[data-theme="dark"] .sb-24__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-24:not([data-theme="light"]) .sb-24__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-24__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-24[data-theme="dark"] .sb-24__theme:hover,
.sb-24:not([data-theme="light"]) .sb-24__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-24__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-24__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-24__sun {
  display: none;
}

.sb-24__theme[aria-pressed="true"] .sb-24__sun {
  display: block;
}

.sb-24__theme[aria-pressed="true"] .sb-24__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-24__theme {
    transition: none;
  }

  .sb-24__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-24');if(!r)return;const t=r.querySelector('.sb-24__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
