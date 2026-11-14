---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/recent-searches/"
title: "CSS Search Bar with Recent Searches Dropdown"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "Focus the field and your recent searches drop down — each with a clock glyph, a real <time> stamp and its own remove button, plus a \"Clear all\" action in the…"
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Search Bar with Recent Searches Dropdown
Source: https://codefronts.com/components/css-search-boxes/recent-searches/

Focus the field and your recent searches drop down — each with a clock glyph, a real <time> stamp and its own remove button, plus a "Clear all" action in the header. History persists in localStorage in ten lines.
## HTML
```html
<div class="sb-18">
  <button class="sb-18__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-18__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-18__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-18__stage">
    <div class="sb-18__wrap" role="search">
      <div class="sb-18__field">
        <svg class="sb-18__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <label class="sb-18__vh" for="sb-18-input">Search</label>
        <input class="sb-18__input" id="sb-18-input" type="search" placeholder="Search anything&hellip;" autocomplete="off" aria-controls="sb-18-panel">
      </div>

      <div class="sb-18__panel" id="sb-18-panel">
        <div class="sb-18__head">
          <p class="sb-18__group-h">Recent searches</p>
          <button class="sb-18__clear" id="sb-18-clear" type="button">Clear all</button>
        </div>
        <ul class="sb-18__list" id="sb-18-list" role="listbox" aria-label="Recent searches">
          <li class="sb-18__row" role="option" aria-selected="false">
            <span class="sb-18__glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="12" cy="12" r="7.6" stroke="currentColor" stroke-width="1.6"/><path d="M12 8.2V12l2.7 1.7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></span>
            <span class="sb-18__q">wireless headphones</span>
            <time class="sb-18__time" datetime="2027-02-11T09:14">9:14 AM</time>
            <button class="sb-18__x" type="button" aria-label="Remove wireless headphones from recent searches"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m7 7 10 10M17 7 7 17" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></button>
          </li>
          <li class="sb-18__row" role="option" aria-selected="false">
            <span class="sb-18__glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="12" cy="12" r="7.6" stroke="currentColor" stroke-width="1.6"/><path d="M12 8.2V12l2.7 1.7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></span>
            <span class="sb-18__q">invoice template</span>
            <time class="sb-18__time" datetime="2027-02-10T18:02">Yesterday</time>
            <button class="sb-18__x" type="button" aria-label="Remove invoice template from recent searches"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m7 7 10 10M17 7 7 17" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></button>
          </li>
          <li class="sb-18__row" role="option" aria-selected="false">
            <span class="sb-18__glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="12" cy="12" r="7.6" stroke="currentColor" stroke-width="1.6"/><path d="M12 8.2V12l2.7 1.7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></span>
            <span class="sb-18__q">Q3 revenue</span>
            <time class="sb-18__time" datetime="2027-02-09T11:41">Mon</time>
            <button class="sb-18__x" type="button" aria-label="Remove Q3 revenue from recent searches"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m7 7 10 10M17 7 7 17" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></button>
          </li>
          <li class="sb-18__row" role="option" aria-selected="false">
            <span class="sb-18__glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="12" cy="12" r="7.6" stroke="currentColor" stroke-width="1.6"/><path d="M12 8.2V12l2.7 1.7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></span>
            <span class="sb-18__q">onboarding checklist</span>
            <time class="sb-18__time" datetime="2027-02-06T15:20">Fri</time>
            <button class="sb-18__x" type="button" aria-label="Remove onboarding checklist from recent searches"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m7 7 10 10M17 7 7 17" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg></button>
          </li>
        </ul>
        <p class="sb-18__empty">No recent searches</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-18 {
  --bg: #f4f5f7;
  --card: #ffffff;
  --ink: #15181f;
  --muted: #6b7280;
  --line: #e4e6eb;
  --acc: #0f766e;
  --wash: #e9f6f3;
  --ring: #0f766e;
  --shadow: rgba(21,24,31,.14);
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

.sb-18 *,
.sb-18 *::before,
.sb-18 *::after {
  box-sizing: border-box;
}

.sb-18__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: start center;
  padding: clamp(2rem,12vh,7rem) clamp(1rem,4vw,3rem);
}

.sb-18__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-18__wrap {
  position: relative;
  inline-size: min(30rem,100%);
}

.sb-18__field {
  display: flex;
  align-items: center;
  gap: .7rem;
  min-block-size: 52px;
  padding-inline: 1rem;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--card);
  box-shadow: 0 1px 2px rgba(21,24,31,.05);
  transition: border-color .2s, box-shadow .2s;
}

.sb-18__wrap:focus-within .sb-18__field {
  border-color: var(--acc);
  box-shadow: 0 0 0 4px rgba(15,118,110,.14);
}

.sb-18__ico {
  inline-size: 19px;
  block-size: 19px;
  flex: none;
  color: var(--muted);
}

.sb-18__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .96rem/1 inherit;
}

.sb-18__input::placeholder {
  color: var(--muted);
}

.sb-18__input:focus {
  outline: none;
}

.sb-18__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-18__panel {
  position: absolute;
  inset-inline: 0;
  inset-block-start: calc(100% + .5rem);
  z-index: 5;
  padding: .4rem;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--card);
  box-shadow: 0 24px 46px -22px var(--shadow);
  opacity: 0;
  translate: 0 -6px;
  visibility: hidden;
  transition: opacity .2s cubic-bezier(.2,.9,.25,1), translate .2s cubic-bezier(.2,.9,.25,1), visibility .2s;
}

.sb-18__wrap:focus-within .sb-18__panel {
  opacity: 1;
  translate: 0 0;
  visibility: visible;
}

.sb-18__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: .45rem .6rem .3rem;
}

.sb-18__group-h {
  margin: 0;
  color: var(--muted);
  font: 600 .68rem/1 inherit;
  letter-spacing: .09em;
  text-transform: uppercase;
}

.sb-18__clear {
  border: 0;
  border-radius: 6px;
  padding: .25rem .4rem;
  background: none;
  color: var(--acc);
  cursor: pointer;
  font: 600 .74rem/1 inherit;
}

.sb-18__clear:hover {
  background: var(--wash);
}

.sb-18__clear:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 1px;
}

.sb-18__list {
  list-style: none;
  margin: 0;
  padding: 0;
  max-block-size: min(20rem,48vh);
  overflow: auto;
}

.sb-18__row {
  display: flex;
  align-items: center;
  gap: .65rem;
  min-block-size: 44px;
  padding: 0 .35rem 0 .6rem;
  border-radius: 9px;
  cursor: pointer;
  font: 500 .9rem/1 inherit;
  transition: background .14s;
}

.sb-18__row:hover,
.sb-18__row[aria-selected="true"] {
  background: var(--wash);
}

.sb-18__glyph {
  display: grid;
  place-items: center;
  inline-size: 26px;
  block-size: 26px;
  flex: none;
  color: var(--muted);
}

.sb-18__glyph svg {
  inline-size: 16px;
  block-size: 16px;
}

.sb-18__q {
  flex: 1;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.sb-18__time {
  flex: none;
  color: var(--muted);
  font: 400 .74rem/1 inherit;
  font-variant-numeric: tabular-nums;
}

.sb-18__x {
  display: grid;
  place-items: center;
  inline-size: 26px;
  block-size: 26px;
  flex: none;
  border: 0;
  border-radius: 7px;
  background: none;
  color: var(--muted);
  cursor: pointer;
  opacity: 0;
  transition: opacity .16s, background .16s;
}

.sb-18__row:hover .sb-18__x,
.sb-18__x:focus-visible {
  opacity: 1;
}

.sb-18__x:hover {
  background: rgba(0,0,0,.07);
  color: var(--ink);
}

.sb-18__x:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 1px;
}

.sb-18__x svg {
  inline-size: 12px;
  block-size: 12px;
}

.sb-18__empty {
  display: none;
  margin: 0;
  padding: 1.6rem 0;
  text-align: center;
  color: var(--muted);
  font: 400 .86rem/1 inherit;
}

@supports selector(:has(*)) {
  .sb-18__panel:not(:has(.sb-18__row)) .sb-18__empty {
    display: block;
  }

  .sb-18__panel:not(:has(.sb-18__row)) .sb-18__head {
    display: none;
  }
}

.sb-18 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-18__input:focus-visible {
  outline: none;
}

.sb-18[data-theme="dark"] {
  --bg: #0b0e12;
  --card: #141920;
  --ink: #e9eef3;
  --muted: #87909c;
  --line: #222a33;
  --acc: #2dd4bf;
  --wash: rgba(45,212,191,.12);
  --ring: #2dd4bf;
  --shadow: rgba(0,0,0,.7);
}

.sb-18[data-theme="dark"] .sb-18__x:hover {
  background: rgba(255,255,255,.1);
}

@media (prefers-color-scheme: dark) {
  .sb-18:not([data-theme="light"]) {
    --bg: #0b0e12;
    --card: #141920;
    --ink: #e9eef3;
    --muted: #87909c;
    --line: #222a33;
    --acc: #2dd4bf;
    --wash: rgba(45,212,191,.12);
    --ring: #2dd4bf;
    --shadow: rgba(0,0,0,.7);
  }

  .sb-18:not([data-theme="light"]) .sb-18__x:hover {
    background: rgba(255,255,255,.1);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-18 *,
    .sb-18 *::before,
    .sb-18 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .sb-18__field,
    .sb-18__panel {
    border: 1px solid CanvasText;
  }
}

.sb-18__theme {
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

.sb-18[data-theme="dark"] .sb-18__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-18:not([data-theme="light"]) .sb-18__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-18__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-18[data-theme="dark"] .sb-18__theme:hover,
.sb-18:not([data-theme="light"]) .sb-18__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-18__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-18__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-18__sun {
  display: none;
}

.sb-18__theme[aria-pressed="true"] .sb-18__sun {
  display: block;
}

.sb-18__theme[aria-pressed="true"] .sb-18__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-18__theme {
    transition: none;
  }

  .sb-18__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sb-18');
  if (!root) return;
  const input = root.querySelector('#sb-18-input');
  const list = root.querySelector('#sb-18-list');
  const KEY = 'sb-18-recent';

  const save = () => {
    try {
      const qs = [...list.querySelectorAll('.sb-18__q')].map((n) => n.textContent);
      localStorage.setItem(KEY, JSON.stringify(qs));
    } catch (_) { /* private mode / sandboxed iframe */ }
  };
  const drop = (row) => {
    const next = row.nextElementSibling || row.previousElementSibling;
    (next ? next.querySelector('.sb-18__x') : input).focus();
    row.remove(); save();
  };

  list.addEventListener('click', (e) => {
    const x = e.target.closest('.sb-18__x');
    const row = e.target.closest('.sb-18__row');
    if (x) { e.stopPropagation(); drop(row); return; }
    if (row) { input.value = row.querySelector('.sb-18__q').textContent; input.focus(); }
  });
  root.querySelector('#sb-18-clear').addEventListener('click', () => { list.replaceChildren(); save(); input.focus(); });
  input.addEventListener('mousedown', (e) => { if (document.activeElement === input) e.stopPropagation(); });
})();
(()=>{const r=document.querySelector('.sb-18');if(!r)return;const t=r.querySelector('.sb-18__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
