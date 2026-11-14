---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/loading-spinner/"
title: "CSS Search Bar with Loading Spinner Indicator"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "Type and the magnifier morphs into a spinner while results are fetched, then settles into a result count."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Search Bar with Loading Spinner Indicator
Source: https://codefronts.com/components/css-search-boxes/loading-spinner/

Type and the magnifier morphs into a spinner while results are fetched, then settles into a result count. The spinner is a single element — a conic gradient masked into a ring — and the whole state machine is one data-state attribute with aria-busy for assistive tech.
## HTML
```html
<div class="sb-12">
  <button class="sb-12__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-12__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-12__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-12__stage">
    <div class="sb-12__bar" role="search" data-state="idle">
      <span class="sb-12__lead" aria-hidden="true">
        <svg class="sb-12__mag" viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <span class="sb-12__spin"></span>
      </span>
      <label class="sb-12__vh" for="sb-12-input">Search the knowledge base</label>
      <input class="sb-12__input" id="sb-12-input" type="search" placeholder="Search the knowledge base&hellip;" autocomplete="off">
      <span class="sb-12__count" aria-hidden="true">24 results</span>
      <p class="sb-12__vh" id="sb-12-status" role="status" aria-live="polite"></p>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-12 {
  --bg: #f4f6f9;
  --card: #ffffff;
  --ink: #0f172a;
  --muted: #64748b;
  --line: #e2e8f0;
  --acc: #0ea5e9;
  --wash: rgba(14,165,233,.12);
  --ring: #0ea5e9;
  --shadow: rgba(15,23,42,.14);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: radial-gradient(38rem 22rem at 50% 6%, #ffffff, var(--bg) 72%);
  -webkit-font-smoothing: antialiased;
}

.sb-12 *,
.sb-12 *::before,
.sb-12 *::after {
  box-sizing: border-box;
}

.sb-12__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-12__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-12__bar {
  display: flex;
  align-items: center;
  gap: .75rem;
  inline-size: min(30rem,100%);
  min-block-size: 54px;
  padding-inline: 1.05rem;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--card);
  box-shadow: 0 1px 2px rgba(15,23,42,.05);
  transition: border-color .2s, box-shadow .2s;
}

.sb-12__bar:focus-within {
  border-color: var(--acc);
  box-shadow: 0 0 0 4px var(--wash);
}

.sb-12__lead {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 22px;
  block-size: 22px;
  flex: none;
  color: var(--muted);
}

.sb-12__mag {
  inline-size: 19px;
  block-size: 19px;
  transition: opacity .18s, scale .18s;
}

.sb-12__spin {
  position: absolute;
  inline-size: 20px;
  block-size: 20px;
  border-radius: 50%;
  background: conic-gradient(from 0deg, transparent 0 25%, var(--acc));
  -webkit-mask: radial-gradient(closest-side, transparent 68%, #000 70%);
  mask: radial-gradient(closest-side, transparent 68%, #000 70%);
  opacity: 0;
  scale: .7;
  transition: opacity .18s, scale .18s;
}

@supports not ((-webkit-mask: radial-gradient(#000,#000)) or (mask: radial-gradient(#000,#000))) {
  .sb-12__spin {
    background: none;
    border: 2px solid var(--wash);
    border-block-start-color: var(--acc);
  }
}

.sb-12__bar[data-state="loading"] .sb-12__mag {
  opacity: 0;
  scale: .7;
}

.sb-12__bar[data-state="loading"] .sb-12__spin {
  opacity: 1;
  scale: 1;
  animation: sb-12-spin .8s linear infinite;
}

@keyframes sb-12-spin {
  to {
    -webkit-transform: rotate(1turn);
    transform: rotate(1turn);
    rotate: 1turn;
  }
}

.sb-12__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .96rem/1 inherit;
}

.sb-12__input::placeholder {
  color: var(--muted);
}

.sb-12__input:focus {
  outline: none;
}

.sb-12__count {
  flex: none;
  padding: .28rem .55rem;
  border-radius: 999px;
  background: var(--wash);
  color: var(--acc);
  font: 600 .74rem/1 inherit;
  font-variant-numeric: tabular-nums;
  opacity: 0;
  scale: .9;
  transition: opacity .2s, scale .2s;
}

.sb-12__bar[data-state="done"] .sb-12__count {
  opacity: 1;
  scale: 1;
}

.sb-12 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.sb-12__input:focus-visible {
  outline: none;
}

.sb-12[data-theme="dark"] {
  --bg: #0b1120;
  --card: #131a2b;
  --ink: #e8eef8;
  --muted: #8695ad;
  --line: #222c42;
  --acc: #38bdf8;
  --wash: rgba(56,189,248,.16);
  --ring: #38bdf8;
  --shadow: rgba(0,0,0,.7);
  background: radial-gradient(38rem 22rem at 50% 6%, #16203a, var(--bg) 72%);
}

@media (prefers-color-scheme: dark) {
  .sb-12:not([data-theme="light"]) {
    --bg: #0b1120;
    --card: #131a2b;
    --ink: #e8eef8;
    --muted: #8695ad;
    --line: #222c42;
    --acc: #38bdf8;
    --wash: rgba(56,189,248,.16);
    --ring: #38bdf8;
    --shadow: rgba(0,0,0,.7);
    background: radial-gradient(38rem 22rem at 50% 6%, #16203a, var(--bg) 72%);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-12 *,
    .sb-12 *::before,
    .sb-12 *::after {
    transition: none !important;
  }

  .sb-12__bar[data-state="loading"] .sb-12__spin {
    animation-duration: 2.4s;
  }
}

@media (forced-colors: active) {
  .sb-12__bar {
    border: 1px solid CanvasText;
  }

  .sb-12__spin {
    background: Highlight;
  }
}

.sb-12__theme {
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

.sb-12[data-theme="dark"] .sb-12__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-12:not([data-theme="light"]) .sb-12__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-12__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-12[data-theme="dark"] .sb-12__theme:hover,
.sb-12:not([data-theme="light"]) .sb-12__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-12__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-12__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-12__sun {
  display: none;
}

.sb-12__theme[aria-pressed="true"] .sb-12__sun {
  display: block;
}

.sb-12__theme[aria-pressed="true"] .sb-12__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-12__theme {
    transition: none;
  }

  .sb-12__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sb-12');
  if (!root) return;
  const bar = root.querySelector('.sb-12__bar');
  const input = root.querySelector('#sb-12-input');
  const count = root.querySelector('.sb-12__count');
  const status = root.querySelector('#sb-12-status');
  let debounce, done;

  const set = (state, n) => {
    bar.dataset.state = state;
    bar.toggleAttribute('aria-busy', state === 'loading');
    if (state === 'loading') status.textContent = 'Searching';
    if (state === 'done') { count.textContent = n + ' results'; status.textContent = n + ' results found'; }
  };

  input.addEventListener('input', () => {
    clearTimeout(debounce); clearTimeout(done);
    if (!input.value.trim()) return set('idle');
    debounce = setTimeout(() => {
      set('loading');                                   /* replace with your fetch() */
      done = setTimeout(() => set('done', 3 + Math.floor(Math.random() * 40)), 700);
    }, 280);
  });
})();
(()=>{const r=document.querySelector('.sb-12');if(!r)return;const t=r.querySelector('.sb-12__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
