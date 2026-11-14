---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/focus-ring-bloom/"
title: "CSS Search Bar with Focus Ring Bloom Animation"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "A focus indicator with a moment of delight and no accessibility cost: on focus a soft ring blooms outward once and settles into a persistent 4px halo."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Search Bar with Focus Ring Bloom Animation
Source: https://codefronts.com/components/css-search-boxes/focus-ring-bloom/

A focus indicator with a moment of delight and no accessibility cost: on focus a soft ring blooms outward once and settles into a persistent 4px halo. The persistent ring is what satisfies WCAG; the bloom is the 320ms that makes the interface feel alive.
## HTML
```html
<div class="sb-31">
  <button class="sb-31__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-31__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-31__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-31__stage">
    <div class="sb-31__bar" role="search">
      <svg class="sb-31__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      <label class="sb-31__vh" for="sb-31-input">Search projects and tasks</label>
      <input class="sb-31__input" id="sb-31-input" type="search" placeholder="Search projects and tasks" autocomplete="off">
      <kbd class="sb-31__kbd">&#8984;K</kbd>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-31 {
  --bg: #f4f6f8;
  --card: #ffffff;
  --ink: #111827;
  --muted: #6b7280;
  --line: #e3e7ec;
  --acc: #6d28d9;
  --wash: rgba(109,40,217,.16);
  --ring: #6d28d9;
  --shadow: rgba(17,24,39,.14);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: radial-gradient(38rem 22rem at 50% 10%, #fff, var(--bg) 76%);
  -webkit-font-smoothing: antialiased;
}

.sb-31 *,
.sb-31 *::before,
.sb-31 *::after {
  box-sizing: border-box;
}

.sb-31__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-31__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-31__bar {
  position: relative;
  display: flex;
  align-items: center;
  gap: .7rem;
  inline-size: min(30rem,100%);
  min-block-size: 56px;
  padding-inline: 1.05rem .5rem;
  border: 2px solid var(--line);
  border-radius: 14px;
  background: var(--card);
  transition: border-color .18s, box-shadow .18s;
}

.sb-31__bar:focus-within {
  border-color: var(--acc);
  box-shadow: 0 0 0 4px var(--wash);
}

.sb-31__bar::after {
  content: '';
  position: absolute;
  inset: -2px;
  border: 2px solid var(--acc);
  border-radius: inherit;
  opacity: 0;
  pointer-events: none;
}

.sb-31__bar:focus-within::after {
  animation: sb-31-bloom .42s cubic-bezier(.2,.9,.25,1) forwards;
}

@keyframes sb-31-bloom {
  0% {
    opacity: .75;
    -webkit-transform: scale(1);
    transform: scale(1);
    scale: 1;
  }

  100% {
    opacity: 0;
    -webkit-transform: scale(1.06);
    transform: scale(1.06);
    scale: 1.06;
  }
}

.sb-31__ico {
  inline-size: 19px;
  block-size: 19px;
  flex: none;
  color: var(--muted);
  transition: color .18s;
}

.sb-31__bar:focus-within .sb-31__ico {
  color: var(--acc);
}

.sb-31__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .97rem/1 inherit;
}

.sb-31__input::placeholder {
  color: var(--muted);
}

.sb-31__input:focus {
  outline: none;
}

.sb-31__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-31__kbd {
  display: inline-grid;
  place-items: center;
  min-inline-size: 2.2rem;
  block-size: 1.9rem;
  flex: none;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #f8f9fb;
  color: var(--muted);
  font: 500 .74rem/1 ui-monospace,Menlo,monospace;
}

.sb-31 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.sb-31__input:focus-visible {
  outline: none;
}

.sb-31[data-theme="dark"] {
  --bg: #0b0d13;
  --card: #151823;
  --ink: #eceff6;
  --muted: #8a91a1;
  --line: #242b39;
  --acc: #a78bfa;
  --wash: rgba(167,139,250,.20);
  --ring: #a78bfa;
  --shadow: rgba(0,0,0,.7);
  background: radial-gradient(38rem 22rem at 50% 10%, #181c28, var(--bg) 76%);
}

.sb-31[data-theme="dark"] .sb-31__kbd {
  background: #1b2130;
}

@media (prefers-color-scheme: dark) {
  .sb-31:not([data-theme="light"]) {
    --bg: #0b0d13;
    --card: #151823;
    --ink: #eceff6;
    --muted: #8a91a1;
    --line: #242b39;
    --acc: #a78bfa;
    --wash: rgba(167,139,250,.20);
    --ring: #a78bfa;
    --shadow: rgba(0,0,0,.7);
    background: radial-gradient(38rem 22rem at 50% 10%, #181c28, var(--bg) 76%);
  }

  .sb-31:not([data-theme="light"]) .sb-31__kbd {
    background: #1b2130;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-31 *,
    .sb-31 *::before,
    .sb-31 *::after {
    animation: none !important;
    transition: none !important;
  }

  .sb-31__bar:focus-within::after {
    opacity: 0;
  }
}

@media (forced-colors: active) {
  .sb-31__bar:focus-within {
    outline: 2px solid Highlight;
    outline-offset: 2px;
  }

  .sb-31__bar::after {
    display: none;
  }
}

.sb-31__theme {
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

.sb-31[data-theme="dark"] .sb-31__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-31:not([data-theme="light"]) .sb-31__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-31__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-31[data-theme="dark"] .sb-31__theme:hover,
.sb-31:not([data-theme="light"]) .sb-31__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-31__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-31__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-31__sun {
  display: none;
}

.sb-31__theme[aria-pressed="true"] .sb-31__sun {
  display: block;
}

.sb-31__theme[aria-pressed="true"] .sb-31__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-31__theme {
    transition: none;
  }

  .sb-31__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-31');if(!r)return;const t=r.querySelector('.sb-31__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
