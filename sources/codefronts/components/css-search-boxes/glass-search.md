---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/glass-search/"
title: "Glassmorphism CSS Search Bar (Backdrop Blur)"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "Frosted glass done properly: backdrop-filter: blur(20px) saturate(180%) over a slowly drifting colour field, a 1px inner highlight stroke that fakes the lit…"
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism CSS Search Bar (Backdrop Blur)
Source: https://codefronts.com/components/css-search-boxes/glass-search/

Frosted glass done properly: backdrop-filter: blur(20px) saturate(180%) over a slowly drifting colour field, a 1px inner highlight stroke that fakes the lit top edge of real glass, and a specular sheen that sweeps across on focus.
## HTML
```html
<div class="sb-08">
  <button class="sb-08__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-08__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-08__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <span class="sb-08__blob sb-08__blob--a" aria-hidden="true"></span>
  <span class="sb-08__blob sb-08__blob--b" aria-hidden="true"></span>
  <span class="sb-08__blob sb-08__blob--c" aria-hidden="true"></span>
  <div class="sb-08__stage">
    <div class="sb-08__bar" role="search">
      <svg class="sb-08__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      <label class="sb-08__vh" for="sb-08-input">Search your library</label>
      <input class="sb-08__input" id="sb-08-input" type="search" placeholder="Search your library" autocomplete="off">
      <kbd class="sb-08__kbd">&#8984;K</kbd>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-08 {
  --ink: #0b1020;
  --muted: rgba(11,16,32,.62);
  --tint: rgba(255,255,255,.16);
  --edge: rgba(255,255,255,.30);
  --hi: rgba(255,255,255,.6);
  --ring: #ffffff;
  --shadow: rgba(12,14,50,.42);
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  overflow: hidden;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: linear-gradient(140deg,#c8d8ff 0%, #f5d9ee 45%, #ffe8c9 100%);
  -webkit-font-smoothing: antialiased;
}

.sb-08 *,
.sb-08 *::before,
.sb-08 *::after {
  box-sizing: border-box;
}

.sb-08__blob {
  position: absolute;
  inline-size: 38vmax;
  block-size: 38vmax;
  border-radius: 50%;
  filter: blur(2px);
  will-change: transform;
}

.sb-08__blob--a {
  inset-block-start: -8vmax;
  inset-inline-start: -6vmax;
  background: radial-gradient(circle at 40% 40%, rgba(99,102,241,.85), transparent 62%);
  animation: sb-08-drift-a 24s ease-in-out infinite alternate;
}

.sb-08__blob--b {
  inset-block-end: -12vmax;
  inset-inline-end: -6vmax;
  background: radial-gradient(circle at 55% 45%, rgba(236,72,153,.75), transparent 62%);
  animation: sb-08-drift-b 28s ease-in-out infinite alternate;
}

.sb-08__blob--c {
  inset-block-start: 22%;
  inset-inline-end: 18%;
  inline-size: 26vmax;
  block-size: 26vmax;
  background: radial-gradient(circle at 50% 50%, rgba(45,212,191,.7), transparent 60%);
  animation: sb-08-drift-a 20s ease-in-out infinite alternate-reverse;
}

@keyframes sb-08-drift-a {
  to {
    -webkit-transform: translate(8vmax,6vmax);
    transform: translate(8vmax,6vmax);
    translate: 8vmax 6vmax;
  }
}

@keyframes sb-08-drift-b {
  to {
    -webkit-transform: translate(-9vmax,-5vmax);
    transform: translate(-9vmax,-5vmax);
    translate: -9vmax -5vmax;
  }
}

.sb-08__stage {
  position: relative;
  z-index: 1;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-08__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-08__bar {
  position: relative;
  display: flex;
  align-items: center;
  gap: .75rem;
  overflow: hidden;
  inline-size: min(32rem,100%);
  min-block-size: 58px;
  padding-inline: 1.15rem .55rem;
  border: 1px solid var(--edge);
  border-radius: 18px;
  background: rgba(255,255,255,.42);
  box-shadow: inset 0 1px 0 var(--hi), 0 24px 48px -22px var(--shadow);
  transition: box-shadow .25s, border-color .25s, translate .25s;
}

@supports ((-webkit-backdrop-filter: blur(1px)) or (backdrop-filter: blur(1px))) {
  .sb-08__bar {
    background: var(--tint);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    backdrop-filter: blur(20px) saturate(180%);
  }
}

.sb-08__bar::after {
  content: '';
  position: absolute;
  inset-block: 0;
  inline-size: 45%;
  inset-inline-start: -45%;
  background: linear-gradient(100deg, transparent, rgba(255,255,255,.5), transparent);
  transition: inset-inline-start .7s cubic-bezier(.2,.9,.25,1);
  pointer-events: none;
}

.sb-08__bar:focus-within {
  border-color: rgba(255,255,255,.6);
  box-shadow: inset 0 1px 0 var(--hi), 0 30px 60px -24px var(--shadow), 0 0 0 4px rgba(255,255,255,.28);
  translate: 0 -1px;
}

.sb-08__bar:focus-within::after {
  inset-inline-start: 110%;
}

.sb-08__ico {
  inline-size: 20px;
  block-size: 20px;
  flex: none;
  color: var(--muted);
}

.sb-08__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 500 1rem/1 inherit;
}

.sb-08__input::placeholder {
  color: var(--muted);
  font-weight: 400;
}

.sb-08__input:focus {
  outline: none;
}

.sb-08__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-08__kbd {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-inline-size: 2.2rem;
  block-size: 2rem;
  border: 1px solid var(--edge);
  border-radius: 9px;
  background: rgba(255,255,255,.32);
  color: var(--ink);
  font: 600 .74rem/1 ui-monospace,"SF Mono",Menlo,monospace;
}

.sb-08 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.sb-08__input:focus-visible {
  outline: none;
}

.sb-08[data-theme="dark"] {
  --ink: #f4f6ff;
  --muted: rgba(244,246,255,.72);
  --tint: rgba(16,18,44,.38);
  --edge: rgba(255,255,255,.16);
  --hi: rgba(255,255,255,.22);
  --shadow: rgba(0,0,0,.65);
  background: linear-gradient(140deg,#141a3a 0%, #2a1740 48%, #0f2b33 100%);
}

.sb-08[data-theme="dark"] .sb-08__bar {
  background: rgba(16,18,44,.6);
}

.sb-08[data-theme="dark"] .sb-08__kbd {
  background: rgba(255,255,255,.08);
}

@media (prefers-color-scheme: dark) {
  .sb-08:not([data-theme="light"]) {
    --ink: #f4f6ff;
    --muted: rgba(244,246,255,.72);
    --tint: rgba(16,18,44,.38);
    --edge: rgba(255,255,255,.16);
    --hi: rgba(255,255,255,.22);
    --shadow: rgba(0,0,0,.65);
    background: linear-gradient(140deg,#141a3a 0%, #2a1740 48%, #0f2b33 100%);
  }

  .sb-08:not([data-theme="light"]) .sb-08__bar {
    background: rgba(16,18,44,.6);
  }

  .sb-08:not([data-theme="light"]) .sb-08__kbd {
    background: rgba(255,255,255,.08);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-08 *,
    .sb-08 *::before,
    .sb-08 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .sb-08__bar {
    border: 1px solid CanvasText;
    background: Canvas;
  }

  .sb-08__blob {
    display: none;
  }
}

.sb-08__theme {
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

.sb-08[data-theme="dark"] .sb-08__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-08:not([data-theme="light"]) .sb-08__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-08__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-08[data-theme="dark"] .sb-08__theme:hover,
.sb-08:not([data-theme="light"]) .sb-08__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-08__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-08__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-08__sun {
  display: none;
}

.sb-08__theme[aria-pressed="true"] .sb-08__sun {
  display: block;
}

.sb-08__theme[aria-pressed="true"] .sb-08__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-08__theme {
    transition: none;
  }

  .sb-08__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-08');if(!r)return;const t=r.querySelector('.sb-08__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
