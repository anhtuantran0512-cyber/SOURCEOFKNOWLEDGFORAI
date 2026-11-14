---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/tagged-filter/"
title: "CSS Search Bar with Filter Chip Tags"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "Filters live inside the field as removable chips sitting before the caret, GitHub/Linear style."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Search Bar with Filter Chip Tags
Source: https://codefronts.com/components/css-search-boxes/tagged-filter/

Filters live inside the field as removable chips sitting before the caret, GitHub/Linear style. The wrapper is a wrapping flex container, the input is a flex:1 child with a minimum width, and Backspace on an empty query pops the last chip — the interaction people expect and almost nobody implements.
## HTML
```html
<div class="sb-17">
  <button class="sb-17__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-17__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-17__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-17__stage">
    <div class="sb-17__field" id="sb-17-field" role="search">
      <svg class="sb-17__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>

      <span class="sb-17__chip sb-17__chip--type">
        <span class="sb-17__k">type</span>report
        <button class="sb-17__x" type="button" aria-label="Remove filter type: report">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m7 7 10 10M17 7 7 17" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
        </button>
      </span>
      <span class="sb-17__chip sb-17__chip--author">
        <span class="sb-17__k">author</span>Priya Sharma
        <button class="sb-17__x" type="button" aria-label="Remove filter author: Priya Sharma">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m7 7 10 10M17 7 7 17" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
        </button>
      </span>
      <span class="sb-17__chip sb-17__chip--date">
        <span class="sb-17__k">updated</span>&gt; 2027-01-01
        <button class="sb-17__x" type="button" aria-label="Remove filter updated after 1 January 2027">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m7 7 10 10M17 7 7 17" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
        </button>
      </span>

      <label class="sb-17__vh" for="sb-17-input">Search with active filters</label>
      <input class="sb-17__input" id="sb-17-input" type="search" placeholder="Add a keyword&hellip;" autocomplete="off">
      <p class="sb-17__vh" id="sb-17-status" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-17 {
  --bg: #f5f6f8;
  --card: #ffffff;
  --ink: #14171f;
  --muted: #6b7280;
  --line: #e3e6ec;
  --acc: #1d4ed8;
  --type: #0f766e;
  --author: #7c3aed;
  --date: #b45309;
  --ring: #1d4ed8;
  --shadow: rgba(20,23,31,.12);
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

.sb-17 *,
.sb-17 *::before,
.sb-17 *::after {
  box-sizing: border-box;
}

.sb-17__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-17__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-17__field {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .4rem;
  inline-size: min(34rem,100%);
  min-block-size: 54px;
  padding: .5rem .8rem;
  border: 1px solid var(--line);
  border-radius: 13px;
  background: var(--card);
  box-shadow: 0 1px 2px rgba(20,23,31,.05);
  transition: border-color .2s, box-shadow .2s;
}

.sb-17__field:focus-within {
  border-color: var(--acc);
  box-shadow: 0 0 0 4px rgba(29,78,216,.14);
}

.sb-17__ico {
  inline-size: 18px;
  block-size: 18px;
  flex: none;
  color: var(--muted);
  margin-inline-end: .15rem;
}

.sb-17__chip {
  display: inline-flex;
  align-items: center;
  gap: .3rem;
  block-size: 30px;
  padding-inline: .55rem .2rem;
  border-radius: 8px;
  background: #f1f3f7;
  color: var(--ink);
  font: 500 .82rem/1 inherit;
  white-space: nowrap;
  animation: sb-17-in .2s cubic-bezier(.2,.9,.25,1);
}

@keyframes sb-17-in {
  from {
    opacity: 0;
    scale: .9;
  }

  to {
    opacity: 1;
    scale: 1;
  }
}

.sb-17__k {
  padding-inline-end: .3rem;
  border-inline-end: 1px solid rgba(20,23,31,.12);
  margin-inline-end: .1rem;
  color: var(--muted);
  font: 600 .72rem/1 ui-monospace,Menlo,monospace;
  letter-spacing: .02em;
}

.sb-17__chip--type {
  background: color-mix(in srgb, var(--type) 10%, white);
  color: var(--type);
}

.sb-17__chip--author {
  background: color-mix(in srgb, var(--author) 10%, white);
  color: var(--author);
}

.sb-17__chip--date {
  background: color-mix(in srgb, var(--date) 12%, white);
  color: var(--date);
}

.sb-17__chip--type .sb-17__k,
.sb-17__chip--author .sb-17__k,
.sb-17__chip--date .sb-17__k {
  color: inherit;
  opacity: .72;
  border-color: currentColor;
}

.sb-17__x {
  display: grid;
  place-items: center;
  inline-size: 24px;
  block-size: 24px;
  flex: none;
  border: 0;
  border-radius: 6px;
  background: none;
  color: inherit;
  cursor: pointer;
  opacity: .6;
  transition: opacity .16s, background .16s;
}

.sb-17__x:hover {
  opacity: 1;
  background: rgba(0,0,0,.08);
}

.sb-17__x:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 1px;
  opacity: 1;
}

.sb-17__x svg {
  inline-size: 11px;
  block-size: 11px;
}

.sb-17__input {
  flex: 1 1 8ch;
  min-inline-size: 8ch;
  block-size: 30px;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .93rem/1 inherit;
}

@supports (field-sizing: content) {
  .sb-17__input {
    field-sizing: content;
  }
}

.sb-17__input::placeholder {
  color: var(--muted);
}

.sb-17__input:focus {
  outline: none;
}

.sb-17__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-17[data-theme="dark"] {
  --bg: #0b0e14;
  --card: #141922;
  --ink: #e9edf5;
  --muted: #89909f;
  --line: #222a37;
  --acc: #6a97ff;
  --type: #2dd4bf;
  --author: #c4b5fd;
  --date: #fbbf24;
  --ring: #6a97ff;
  --shadow: rgba(0,0,0,.7);
}

.sb-17[data-theme="dark"] .sb-17__chip {
  background: #1c2230;
}

.sb-17[data-theme="dark"] .sb-17__chip--type,
.sb-17[data-theme="dark"] .sb-17__chip--author,
.sb-17[data-theme="dark"] .sb-17__chip--date {
  background: rgba(255,255,255,.06);
}

.sb-17[data-theme="dark"] .sb-17__x:hover {
  background: rgba(255,255,255,.12);
}

@media (prefers-color-scheme: dark) {
  .sb-17:not([data-theme="light"]) {
    --bg: #0b0e14;
    --card: #141922;
    --ink: #e9edf5;
    --muted: #89909f;
    --line: #222a37;
    --acc: #6a97ff;
    --type: #2dd4bf;
    --author: #c4b5fd;
    --date: #fbbf24;
    --ring: #6a97ff;
    --shadow: rgba(0,0,0,.7);
  }

  .sb-17:not([data-theme="light"]) .sb-17__chip {
    background: #1c2230;
  }

  .sb-17:not([data-theme="light"]) .sb-17__chip--type,
    .sb-17:not([data-theme="light"]) .sb-17__chip--author,
    .sb-17:not([data-theme="light"]) .sb-17__chip--date {
    background: rgba(255,255,255,.06);
  }

  .sb-17:not([data-theme="light"]) .sb-17__x:hover {
    background: rgba(255,255,255,.12);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-17 *,
    .sb-17 *::before,
    .sb-17 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .sb-17__field,
    .sb-17__chip {
    border: 1px solid CanvasText;
  }
}

.sb-17__theme {
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

.sb-17[data-theme="dark"] .sb-17__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-17:not([data-theme="light"]) .sb-17__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-17__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-17[data-theme="dark"] .sb-17__theme:hover,
.sb-17:not([data-theme="light"]) .sb-17__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-17__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-17__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-17__sun {
  display: none;
}

.sb-17__theme[aria-pressed="true"] .sb-17__sun {
  display: block;
}

.sb-17__theme[aria-pressed="true"] .sb-17__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-17__theme {
    transition: none;
  }

  .sb-17__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sb-17');
  if (!root) return;
  const field = root.querySelector('#sb-17-field');
  const input = root.querySelector('#sb-17-input');
  const status = root.querySelector('#sb-17-status');
  const chips = () => [...field.querySelectorAll('.sb-17__chip')];

  const remove = (chip) => {
    if (!chip) return;
    const next = chip.nextElementSibling;
    status.textContent = chip.textContent.trim() + ' filter removed';
    chip.remove();
    (next && next.classList.contains('sb-17__chip') ? next.querySelector('.sb-17__x') : input).focus();
  };
  field.addEventListener('click', (e) => {
    const x = e.target.closest('.sb-17__x');
    if (x) remove(x.closest('.sb-17__chip'));
  });
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Backspace' && input.value === '') { e.preventDefault(); remove(chips().at(-1)); }
  });
})();
(()=>{const r=document.querySelector('.sb-17');if(!r)return;const t=r.querySelector('.sb-17__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
