---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/neon-outline/"
title: "Neon Glow CSS Search Bar (Cyberpunk)"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "Cyan-and-magenta neon on near-black: the field's glow is a five-layer box-shadow — two tight inner rings for the tube, three wide outer washes for the bloom…"
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Glow CSS Search Bar (Cyberpunk)
Source: https://codefronts.com/components/css-search-boxes/neon-outline/

Cyan-and-magenta neon on near-black: the field's glow is a five-layer box-shadow — two tight inner rings for the tube, three wide outer washes for the bloom — and focus runs a slow hue-shifting pulse. Monospace type, scanline grid, zero JavaScript.
## HTML
```html
<div class="sb-09">
  <button class="sb-09__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-09__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-09__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-09__stage">
    <div class="sb-09__bar" role="search">
      <svg class="sb-09__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.7"/><path d="m16 16 4.4 4.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
      <label class="sb-09__vh" for="sb-09-input">Search the grid</label>
      <input class="sb-09__input" id="sb-09-input" type="search" placeholder="search://the-grid" autocomplete="off" spellcheck="false">
      <span class="sb-09__status" aria-hidden="true">ONLINE</span>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&display=swap');

@property --sb-09-neon {
  syntax: '<color>';
  inherits: true;
  initial-value: #22d3ee;
}

@property --sb-09-neon2 {
  syntax: '<color>';
  inherits: true;
  initial-value: #f472b6;
}

.sb-09 {
  --bg: #05060a;
  --ink: #e8fbff;
  --muted: #6fd8e8;
  --neon: #22d3ee;
  --neon2: #f472b6;
  --ring: #22d3ee;
  --sb-09-neon: #22d3ee;
  --sb-09-neon2: #f472b6;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  overflow: hidden;
  box-sizing: border-box;
  color: var(--ink);
  font-family: "JetBrains Mono",ui-monospace,"SF Mono",Menlo,Consolas,monospace;
  background: radial-gradient(38rem 24rem at 50% 46%, rgba(34,211,238,.10), transparent 70%), radial-gradient(30rem 20rem at 78% 82%, rgba(244,114,182,.10), transparent 70%), var(--bg);
  -webkit-font-smoothing: antialiased;
}

.sb-09 *,
.sb-09 *::before,
.sb-09 *::after {
  box-sizing: border-box;
}

.sb-09::before {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: .5;
  background: repeating-linear-gradient(0deg, rgba(255,255,255,.035) 0 1px, transparent 1px 3px);
}

.sb-09__stage {
  position: relative;
  z-index: 1;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-09__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-09__bar {
  display: flex;
  align-items: center;
  gap: .85rem;
  inline-size: min(32rem,100%);
  min-block-size: 56px;
  padding-inline: 1.1rem;
  border: 0;
  border-radius: 12px;
  background: rgba(8,12,20,.9);
  box-shadow: inset 0 0 0 1px var(--sb-09-neon), inset 0 0 14px -6px var(--sb-09-neon), 0 0 8px -2px var(--sb-09-neon), 0 0 26px -8px var(--sb-09-neon2), 0 0 56px -14px var(--sb-09-neon2);
  transition: box-shadow .3s ease, translate .3s ease;
}

.sb-09__bar:focus-within {
  translate: 0 -1px;
  animation: sb-09-pulse 3.2s ease-in-out infinite;
}

@keyframes sb-09-pulse {
  0%,
    100% {
    --sb-09-neon: #22d3ee;
    --sb-09-neon2: #f472b6;
    box-shadow: inset 0 0 0 1px var(--sb-09-neon), inset 0 0 16px -6px var(--sb-09-neon), 0 0 10px -2px var(--sb-09-neon), 0 0 34px -8px var(--sb-09-neon2), 0 0 72px -14px var(--sb-09-neon2);
  }

  50% {
    --sb-09-neon: #a78bfa;
    --sb-09-neon2: #22d3ee;
    box-shadow: inset 0 0 0 1px var(--sb-09-neon), inset 0 0 22px -6px var(--sb-09-neon), 0 0 14px -2px var(--sb-09-neon), 0 0 46px -8px var(--sb-09-neon2), 0 0 92px -14px var(--sb-09-neon2);
  }
}

.sb-09__ico {
  inline-size: 20px;
  block-size: 20px;
  flex: none;
  color: var(--neon);
  filter: drop-shadow(0 0 6px var(--neon));
}

.sb-09__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 500 .98rem/1 inherit;
  letter-spacing: .01em;
  caret-color: var(--neon2);
  text-shadow: 0 0 12px rgba(34,211,238,.45);
}

.sb-09__input::placeholder {
  color: var(--muted);
  opacity: .75;
  text-shadow: 0 0 10px rgba(34,211,238,.35);
}

.sb-09__input:focus {
  outline: none;
}

.sb-09__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-09__status {
  flex: none;
  padding: .28rem .5rem;
  border-radius: 6px;
  color: var(--neon2);
  font: 700 .64rem/1 inherit;
  letter-spacing: .16em;
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--neon2) 55%, transparent), 0 0 12px -4px var(--neon2);
}

.sb-09 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 4px;
}

.sb-09__input:focus-visible {
  outline: none;
}

.sb-09[data-theme="light"] {
  --bg: #f4f6fb;
  --ink: #0b1120;
  --muted: #5b6478;
  --neon: #0891b2;
  --neon2: #be185d;
  --ring: #0891b2;
  --sb-09-neon: #0891b2;
  --sb-09-neon2: #be185d;
  background: radial-gradient(38rem 24rem at 50% 46%, rgba(8,145,178,.10), transparent 70%), var(--bg);
}

.sb-09[data-theme="light"]::before {
  opacity: 0;
}

.sb-09[data-theme="light"] .sb-09__bar {
  background: #fff;
  box-shadow: inset 0 0 0 1px var(--sb-09-neon), 0 0 0 4px rgba(8,145,178,.12), 0 18px 36px -22px rgba(8,17,32,.5);
  animation: none;
}

.sb-09[data-theme="light"] .sb-09__input,
.sb-09[data-theme="light"] .sb-09__input::placeholder {
  text-shadow: none;
}

@media (prefers-color-scheme: light) {
  .sb-09:not([data-theme="dark"]) {
    --bg: #f4f6fb;
    --ink: #0b1120;
    --muted: #5b6478;
    --neon: #0891b2;
    --neon2: #be185d;
    --ring: #0891b2;
    --sb-09-neon: #0891b2;
    --sb-09-neon2: #be185d;
    background: radial-gradient(38rem 24rem at 50% 46%, rgba(8,145,178,.10), transparent 70%), var(--bg);
  }

  .sb-09:not([data-theme="dark"])::before {
    opacity: 0;
  }

  .sb-09:not([data-theme="dark"]) .sb-09__bar {
    background: #fff;
    box-shadow: inset 0 0 0 1px var(--sb-09-neon), 0 0 0 4px rgba(8,145,178,.12), 0 18px 36px -22px rgba(8,17,32,.5);
    animation: none;
  }

  .sb-09:not([data-theme="dark"]) .sb-09__input,
    .sb-09:not([data-theme="dark"]) .sb-09__input::placeholder {
    text-shadow: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-09 *,
    .sb-09 *::before,
    .sb-09 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .sb-09__bar {
    border: 1px solid CanvasText;
    box-shadow: none;
  }

  .sb-09::before {
    display: none;
  }
}

.sb-09__theme {
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

.sb-09[data-theme="dark"] .sb-09__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-09:not([data-theme="light"]) .sb-09__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-09__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-09[data-theme="dark"] .sb-09__theme:hover,
.sb-09:not([data-theme="light"]) .sb-09__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-09__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-09__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-09__sun {
  display: none;
}

.sb-09__theme[aria-pressed="true"] .sb-09__sun {
  display: block;
}

.sb-09__theme[aria-pressed="true"] .sb-09__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-09__theme {
    transition: none;
  }

  .sb-09__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-09');if(!r)return;const t=r.querySelector('.sb-09__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
