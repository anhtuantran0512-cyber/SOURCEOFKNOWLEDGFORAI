---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/keyboard-hint/"
title: "CSS Search Bar with Keyboard Shortcut Hint (Cmd K / Ctrl K)"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "The documentation-site classic: a quiet search field with a <kbd> chip pinned inside the right edge, showing ⌘K on Mac and Ctrl K on Windows/Linux."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Search Bar with Keyboard Shortcut Hint (Cmd K / Ctrl K)
Source: https://codefronts.com/components/css-search-boxes/keyboard-hint/

The documentation-site classic: a quiet search field with a <kbd> chip pinned inside the right edge, showing ⌘K on Mac and Ctrl K on Windows/Linux. Focus the field with the shortcut and the chip flips to an esc hint.
## HTML
```html
<div class="sb-16">
  <button class="sb-16__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-16__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-16__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-16__stage">
    <div class="sb-16__bar" role="search">
      <svg class="sb-16__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.2" stroke="currentColor" stroke-width="1.7"/><path d="m15.8 15.8 4.4 4.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
      <label class="sb-16__vh" for="sb-16-input">Search documentation</label>
      <input class="sb-16__input" id="sb-16-input" type="search" placeholder="Search documentation" autocomplete="off" aria-describedby="sb-16-hint">
      <span class="sb-16__chips" id="sb-16-hint">
        <kbd class="sb-16__kbd sb-16__kbd--shortcut" id="sb-16-chip">&#8984;K</kbd>
        <kbd class="sb-16__kbd sb-16__kbd--esc">esc</kbd>
      </span>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-16 {
  --bg: #fbfbfc;
  --card: #ffffff;
  --ink: #1b1f27;
  --muted: #767d8a;
  --line: #e2e5ea;
  --acc: #2f6feb;
  --wash: #eef3ff;
  --ring: #2f6feb;
  --shadow: rgba(20,24,32,.1);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: linear-gradient(180deg,#ffffff, var(--bg)), repeating-linear-gradient(90deg, rgba(20,24,32,.028) 0 1px, transparent 1px 88px);
  -webkit-font-smoothing: antialiased;
}

.sb-16 *,
.sb-16 *::before,
.sb-16 *::after {
  box-sizing: border-box;
}

.sb-16__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-16__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-16__bar {
  display: flex;
  align-items: center;
  gap: .65rem;
  inline-size: min(27rem,100%);
  min-block-size: 46px;
  padding-inline: .85rem .375rem;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--card);
  box-shadow: 0 1px 2px rgba(20,24,32,.04);
  transition: border-color .18s, box-shadow .18s, background .18s;
}

.sb-16__bar:hover {
  border-color: #d3d8e0;
}

.sb-16__bar:focus-within {
  border-color: var(--acc);
  box-shadow: 0 0 0 4px rgba(47,111,235,.14);
}

.sb-16__ico {
  inline-size: 17px;
  block-size: 17px;
  flex: none;
  color: var(--muted);
}

.sb-16__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .91rem/1 inherit;
}

.sb-16__input::placeholder {
  color: var(--muted);
}

.sb-16__input:focus {
  outline: none;
}

.sb-16__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-16__chips {
  display: grid;
  flex: none;
}

.sb-16__kbd {
  grid-area: 1/1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 1px;
  min-inline-size: 2.35rem;
  block-size: 1.6rem;
  padding-inline: .4rem;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: #f8f9fb;
  color: var(--muted);
  font: 500 .72rem/1 ui-monospace,"SF Mono",Menlo,monospace;
  letter-spacing: .01em;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.9), 0 1px 0 var(--line);
  transition: opacity .18s, scale .18s;
}

.sb-16__kbd--esc {
  opacity: 0;
  scale: .9;
  text-transform: uppercase;
  font-size: .66rem;
}

.sb-16__bar:focus-within .sb-16__kbd--shortcut {
  opacity: 0;
  scale: .9;
}

.sb-16__bar:focus-within .sb-16__kbd--esc {
  opacity: 1;
  scale: 1;
}

.sb-16 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-16__input:focus-visible {
  outline: none;
}

.sb-16[data-theme="dark"] {
  --bg: #0c0e13;
  --card: #13161d;
  --ink: #e9ecf2;
  --muted: #858c99;
  --line: #232833;
  --acc: #5b8cff;
  --wash: rgba(91,140,255,.14);
  --ring: #5b8cff;
  --shadow: rgba(0,0,0,.7);
  background: linear-gradient(180deg,#101319, var(--bg)), repeating-linear-gradient(90deg, rgba(255,255,255,.02) 0 1px, transparent 1px 88px);
}

.sb-16[data-theme="dark"] .sb-16__kbd {
  background: #1a1f29;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.06), 0 1px 0 #0b0d12;
}

@media (prefers-color-scheme: dark) {
  .sb-16:not([data-theme="light"]) {
    --bg: #0c0e13;
    --card: #13161d;
    --ink: #e9ecf2;
    --muted: #858c99;
    --line: #232833;
    --acc: #5b8cff;
    --wash: rgba(91,140,255,.14);
    --ring: #5b8cff;
    --shadow: rgba(0,0,0,.7);
    background: linear-gradient(180deg,#101319, var(--bg)), repeating-linear-gradient(90deg, rgba(255,255,255,.02) 0 1px, transparent 1px 88px);
  }

  .sb-16:not([data-theme="light"]) .sb-16__kbd {
    background: #1a1f29;
    box-shadow: inset 0 1px 0 rgba(255,255,255,.06), 0 1px 0 #0b0d12;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-16 *,
    .sb-16 *::before,
    .sb-16 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .sb-16__bar,
    .sb-16__kbd {
    border: 1px solid CanvasText;
  }
}

.sb-16__theme {
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

.sb-16[data-theme="dark"] .sb-16__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-16:not([data-theme="light"]) .sb-16__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-16__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-16[data-theme="dark"] .sb-16__theme:hover,
.sb-16:not([data-theme="light"]) .sb-16__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-16__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-16__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-16__sun {
  display: none;
}

.sb-16__theme[aria-pressed="true"] .sb-16__sun {
  display: block;
}

.sb-16__theme[aria-pressed="true"] .sb-16__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-16__theme {
    transition: none;
  }

  .sb-16__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sb-16');
  if (!root) return;
  const input = root.querySelector('#sb-16-input');
  const chip = root.querySelector('#sb-16-chip');
  const mac = ((navigator.userAgentData && navigator.userAgentData.platform) || navigator.platform || '')
    .toLowerCase().includes('mac');
  chip.textContent = mac ? '\u2318K' : 'Ctrl K';

  document.addEventListener('keydown', (e) => {
    if ((mac ? e.metaKey : e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); input.focus(); input.select(); }
  });
  input.addEventListener('keydown', (e) => { if (e.key === 'Escape') input.blur(); });
})();
(()=>{const r=document.querySelector('.sb-16');if(!r)return;const t=r.querySelector('.sb-16__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
