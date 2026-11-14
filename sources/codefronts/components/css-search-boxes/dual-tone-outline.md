---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/dual-tone-outline/"
title: "CSS Search Bar with Dual-Tone Border Outline"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "A cyan&rarr;magenta gradient border that stays crisp at any radius — built with the double-background background-clip technique (border-box gradient under a…"
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Search Bar with Dual-Tone Border Outline
Source: https://codefronts.com/components/css-search-boxes/dual-tone-outline/

A cyan&rarr;magenta gradient border that stays crisp at any radius — built with the double-background background-clip technique (border-box gradient under a padding-box fill), then set spinning on focus by animating a registered <angle>.
## HTML
```html
<div class="sb-28">
  <button class="sb-28__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-28__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-28__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-28__stage">
    <div class="sb-28__bar" role="search">
      <svg class="sb-28__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      <label class="sb-28__vh" for="sb-28-input">Search datasets</label>
      <input class="sb-28__input" id="sb-28-input" type="search" placeholder="Search datasets and models" autocomplete="off">
      <button class="sb-28__go" type="button" aria-label="Run search">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13m-5.5-5.5L18 12l-5.5 5.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
    </div>
  </div>
</div>
```
## CSS
```css
@property --sb-28-angle {
  syntax: '<angle>';
  inherits: true;
  initial-value: 120deg;
}

.sb-28 {
  --bg: #0b0d14;
  --card: #12151f;
  --ink: #eef1f8;
  --muted: #8b93a6;
  --line: #232838;
  --c1: #22d3ee;
  --c2: #a855f7;
  --c3: #f472b6;
  --ring: #22d3ee;
  --sb-28-angle: 120deg;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: radial-gradient(40rem 24rem at 20% 0%, rgba(34,211,238,.10), transparent 68%), radial-gradient(36rem 22rem at 90% 100%, rgba(244,114,182,.10), transparent 68%), var(--bg);
  -webkit-font-smoothing: antialiased;
}

.sb-28 *,
.sb-28 *::before,
.sb-28 *::after {
  box-sizing: border-box;
}

.sb-28__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-28__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-28__bar {
  display: flex;
  align-items: center;
  gap: .75rem;
  inline-size: min(32rem,100%);
  min-block-size: 58px;
  padding-inline: 1.05rem .5rem;
  border: 2px solid var(--c1);
  border-radius: 16px;
  background: var(--card);
  transition: box-shadow .25s;
}

@supports (background-clip: padding-box) {
  .sb-28__bar {
    border-color: transparent;
    background: linear-gradient(var(--card), var(--card)) padding-box, conic-gradient(from var(--sb-28-angle), var(--c1), var(--c2) 35%, var(--c3) 65%, var(--c1)) border-box;
  }
}

.sb-28__bar:focus-within {
  box-shadow: 0 0 0 5px rgba(34,211,238,.14), 0 22px 44px -26px rgba(0,0,0,.9);
}

@supports (background-clip: padding-box) and (color: oklch(50% .1 200)) {
  .sb-28__bar:focus-within {
    animation: sb-28-spin 4s linear infinite;
  }

  @keyframes sb-28-spin {
    to {
      --sb-28-angle: 480deg;
    }
  }
}

.sb-28__ico {
  inline-size: 19px;
  block-size: 19px;
  flex: none;
  color: var(--c1);
}

.sb-28__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .98rem/1 inherit;
}

.sb-28__input::placeholder {
  color: var(--muted);
}

.sb-28__input:focus {
  outline: none;
}

.sb-28__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-28__go {
  display: grid;
  place-items: center;
  inline-size: 46px;
  block-size: 46px;
  flex: none;
  border: 0;
  border-radius: 12px;
  background: linear-gradient(135deg, var(--c1), var(--c2));
  color: #08131a;
  cursor: pointer;
  transition: filter .18s, scale .12s;
}

.sb-28__go:hover {
  filter: brightness(1.1);
}

.sb-28__go:active {
  scale: .95;
}

.sb-28__go svg {
  inline-size: 18px;
  block-size: 18px;
}

.sb-28 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.sb-28__input:focus-visible {
  outline: none;
}

.sb-28[data-theme="light"] {
  --bg: #f6f7fb;
  --card: #ffffff;
  --ink: #101423;
  --muted: #6a7183;
  --line: #e4e7f0;
  --c1: #0891b2;
  --c2: #7c3aed;
  --c3: #db2777;
  --ring: #0891b2;
  background: radial-gradient(40rem 24rem at 20% 0%, rgba(8,145,178,.08), transparent 68%), radial-gradient(36rem 22rem at 90% 100%, rgba(219,39,119,.07), transparent 68%), var(--bg);
}

.sb-28[data-theme="light"] .sb-28__go {
  color: #fff;
}

@media (prefers-color-scheme: light) {
  .sb-28:not([data-theme="dark"]) {
    --bg: #f6f7fb;
    --card: #ffffff;
    --ink: #101423;
    --muted: #6a7183;
    --line: #e4e7f0;
    --c1: #0891b2;
    --c2: #7c3aed;
    --c3: #db2777;
    --ring: #0891b2;
    background: radial-gradient(40rem 24rem at 20% 0%, rgba(8,145,178,.08), transparent 68%), radial-gradient(36rem 22rem at 90% 100%, rgba(219,39,119,.07), transparent 68%), var(--bg);
  }

  .sb-28:not([data-theme="dark"]) .sb-28__go {
    color: #fff;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-28 *,
    .sb-28 *::before,
    .sb-28 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .sb-28__bar {
    border: 2px solid CanvasText;
    background: Canvas;
  }

  .sb-28__go {
    border: 1px solid CanvasText;
  }
}

.sb-28__theme {
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

.sb-28[data-theme="dark"] .sb-28__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-28:not([data-theme="light"]) .sb-28__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-28__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-28[data-theme="dark"] .sb-28__theme:hover,
.sb-28:not([data-theme="light"]) .sb-28__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-28__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-28__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-28__sun {
  display: none;
}

.sb-28__theme[aria-pressed="true"] .sb-28__sun {
  display: block;
}

.sb-28__theme[aria-pressed="true"] .sb-28__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-28__theme {
    transition: none;
  }

  .sb-28__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-28');if(!r)return;const t=r.querySelector('.sb-28__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
