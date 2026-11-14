---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/expanding-input/"
title: "Animated Expanding CSS Search Bar on Focus"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "A 44px circle that unfurls into a full search field when focused and folds back when you leave — the toolbar pattern from Gmail, Figma and every dense app…"
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Expanding CSS Search Bar on Focus
Source: https://codefronts.com/components/css-search-boxes/expanding-input/

A 44px circle that unfurls into a full search field when focused and folds back when you leave — the toolbar pattern from Gmail, Figma and every dense app header. Pure CSS: :focus-within drives an eased inline-size transition, and the input keeps its accessible name the whole time.
## HTML
```html
<div class="sb-14">
  <button class="sb-14__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-14__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-14__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-14__stage">
    <div class="sb-14__toolbar">
      <span class="sb-14__title">Projects</span>
      <div class="sb-14__spacer"></div>
      <div class="sb-14__box" role="search">
        <label class="sb-14__trigger" for="sb-14-input">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          <span class="sb-14__vh">Search projects</span>
        </label>
        <input class="sb-14__input" id="sb-14-input" type="search" placeholder="Search projects&hellip;" autocomplete="off">
      </div>
      <button class="sb-14__btn" type="button" aria-label="Filter">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 6.5h16M7 12h10M10 17.5h4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      </button>
      <button class="sb-14__btn sb-14__btn--solid" type="button">New project</button>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-14 {
  --bg: #f3f4f7;
  --card: #ffffff;
  --ink: #12141a;
  --muted: #6d7280;
  --line: #e5e7ec;
  --acc: #12141a;
  --wash: #f0f1f5;
  --ring: #3d5afe;
  --shadow: rgba(18,20,26,.14);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: radial-gradient(44rem 24rem at 50% 0%, #fff, var(--bg) 74%);
  -webkit-font-smoothing: antialiased;
}

.sb-14 *,
.sb-14 *::before,
.sb-14 *::after {
  box-sizing: border-box;
}

.sb-14__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-14__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-14__toolbar {
  display: flex;
  align-items: center;
  gap: .5rem;
  inline-size: min(46rem,100%);
  padding: .6rem .7rem;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: var(--card);
  box-shadow: 0 18px 40px -30px var(--shadow), 0 1px 2px rgba(18,20,26,.04);
}

.sb-14__title {
  padding-inline: .45rem;
  font: 700 1rem/1 inherit;
  letter-spacing: -.01em;
}

.sb-14__spacer {
  flex: 1;
}

.sb-14__box {
  display: flex;
  align-items: center;
  flex: none;
  overflow: hidden;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid transparent;
  border-radius: 12px;
  background: var(--wash);
  transition: inline-size .34s cubic-bezier(.2,.9,.25,1), background .2s, border-color .2s, box-shadow .2s;
}

.sb-14__box:hover {
  background: #e9ebf1;
}

.sb-14__box:focus-within {
  inline-size: min(22rem,60vw);
  background: var(--card);
  border-color: var(--acc);
  box-shadow: 0 0 0 3px rgba(18,20,26,.08);
}

.sb-14__box:has(.sb-14__input:not(:placeholder-shown)) {
  inline-size: min(22rem,60vw);
  background: var(--card);
  border-color: var(--line);
}

.sb-14__trigger {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  flex: none;
  cursor: pointer;
  color: var(--muted);
  transition: color .2s;
}

.sb-14__box:focus-within .sb-14__trigger {
  color: var(--acc);
}

.sb-14__trigger svg {
  inline-size: 19px;
  block-size: 19px;
}

.sb-14__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  padding-inline-end: .9rem;
  font: 400 .93rem/1 inherit;
  opacity: 0;
  translate: -6px 0;
  transition: opacity .18s, translate .22s;
}

.sb-14__box:focus-within .sb-14__input,
.sb-14__box:has(.sb-14__input:not(:placeholder-shown)) .sb-14__input {
  opacity: 1;
  translate: 0 0;
  transition-delay: .12s;
}

.sb-14__input::placeholder {
  color: var(--muted);
}

.sb-14__input:focus {
  outline: none;
}

.sb-14__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-14__btn {
  display: grid;
  place-items: center;
  min-inline-size: 44px;
  block-size: 44px;
  flex: none;
  padding-inline: .5rem;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--card);
  color: var(--ink);
  cursor: pointer;
  font: 600 .87rem/1 inherit;
  transition: background .18s, translate .18s;
}

.sb-14__btn:hover {
  background: var(--wash);
}

.sb-14__btn--solid {
  padding-inline: 1rem;
  border-color: transparent;
  background: var(--acc);
  color: var(--card);
}

.sb-14__btn--solid:hover {
  filter: brightness(1.3);
  background: var(--acc);
}

.sb-14__btn svg {
  inline-size: 18px;
  block-size: 18px;
}

.sb-14 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-14__input:focus-visible {
  outline: none;
}

@media (max-width: 34rem) {
  .sb-14__btn--solid {
    display: none;
  }
}

.sb-14[data-theme="dark"] {
  --bg: #0c0e14;
  --card: #141821;
  --ink: #eceff6;
  --muted: #8b92a2;
  --line: #222836;
  --acc: #eceff6;
  --wash: #1c222e;
  --ring: #7d95ff;
  --shadow: rgba(0,0,0,.7);
  background: radial-gradient(44rem 24rem at 50% 0%, #171c28, var(--bg) 74%);
}

.sb-14[data-theme="dark"] .sb-14__box:hover {
  background: #232a38;
}

@media (prefers-color-scheme: dark) {
  .sb-14:not([data-theme="light"]) {
    --bg: #0c0e14;
    --card: #141821;
    --ink: #eceff6;
    --muted: #8b92a2;
    --line: #222836;
    --acc: #eceff6;
    --wash: #1c222e;
    --ring: #7d95ff;
    --shadow: rgba(0,0,0,.7);
    background: radial-gradient(44rem 24rem at 50% 0%, #171c28, var(--bg) 74%);
  }

  .sb-14:not([data-theme="light"]) .sb-14__box:hover {
    background: #232a38;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-14 *,
    .sb-14 *::before,
    .sb-14 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .sb-14__toolbar,
    .sb-14__box,
    .sb-14__btn {
    border: 1px solid CanvasText;
  }
}

.sb-14__theme {
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

.sb-14[data-theme="dark"] .sb-14__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-14:not([data-theme="light"]) .sb-14__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-14__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-14[data-theme="dark"] .sb-14__theme:hover,
.sb-14:not([data-theme="light"]) .sb-14__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-14__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-14__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-14__sun {
  display: none;
}

.sb-14__theme[aria-pressed="true"] .sb-14__sun {
  display: block;
}

.sb-14__theme[aria-pressed="true"] .sb-14__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-14__theme {
    transition: none;
  }

  .sb-14__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-14');if(!r)return;const t=r.querySelector('.sb-14__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
