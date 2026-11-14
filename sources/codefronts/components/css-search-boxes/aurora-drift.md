---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/aurora-drift/"
title: "Aurora Gradient CSS Search Bar"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "The \"AI product\" field: a slow aurora of teal, violet and rose drifting around the border while a soft bloom of the same hues pools underneath."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Aurora Gradient CSS Search Bar
Source: https://codefronts.com/components/css-search-boxes/aurora-drift/

The "AI product" field: a slow aurora of teal, violet and rose drifting around the border while a soft bloom of the same hues pools underneath. Driven by an @property-registered <angle> so a conic gradient can actually animate — the technique that makes this look impossible in plain CSS.
## HTML
```html
<div class="sb-36">
  <button class="sb-36__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-36__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-36__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-36__stage">
    <div class="sb-36__wrap">
      <span class="sb-36__glow" aria-hidden="true"></span>
      <div class="sb-36__bar" role="search">
        <svg class="sb-36__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 3.6l1.6 4.4 4.4 1.6-4.4 1.6L12 15.6l-1.6-4.4L6 9.6l4.4-1.6z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M18.4 15.2l.8 2.2 2.2.8-2.2.8-.8 2.2-.8-2.2-2.2-.8 2.2-.8z" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/></svg>
        <label class="sb-36__vh" for="sb-36-input">Ask or search anything</label>
        <input class="sb-36__input" id="sb-36-input" type="search" placeholder="Ask anything, or search your workspace" autocomplete="off">
        <button class="sb-36__go" type="button" aria-label="Submit">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 19V5m-6 6 6-6 6 6" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
@property --sb-36-a {
  syntax: '<angle>';
  inherits: true;
  initial-value: 0deg;
}

.sb-36 {
  --bg: #08090f;
  --card: #101219;
  --ink: #f0f2f8;
  --muted: #8990a4;
  --line: #232838;
  --c1: #2dd4bf;
  --c2: #8b5cf6;
  --c3: #fb7185;
  --c4: #38bdf8;
  --ring: #8b5cf6;
  --sb-36-a: 0deg;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: radial-gradient(50rem 30rem at 50% 120%, rgba(139,92,246,.16), transparent 66%), var(--bg);
  -webkit-font-smoothing: antialiased;
}

.sb-36 *,
.sb-36 *::before,
.sb-36 *::after {
  box-sizing: border-box;
}

.sb-36__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-36__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-36__wrap {
  position: relative;
  inline-size: min(34rem,100%);
}

.sb-36__glow {
  position: absolute;
  inset: -6px 6px 0;
  z-index: 0;
  border-radius: 22px;
  opacity: .5;
  background: conic-gradient(from var(--sb-36-a), var(--c1), var(--c2) 30%, var(--c3) 58%, var(--c4) 80%, var(--c1));
  filter: blur(22px);
  pointer-events: none;
}

.sb-36__bar {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  gap: .8rem;
  min-block-size: 62px;
  padding-inline: 1.15rem .5rem;
  border: 2px solid transparent;
  border-radius: 18px;
  background: linear-gradient(var(--card), var(--card)) padding-box, conic-gradient(from var(--sb-36-a), var(--c1), var(--c2) 30%, var(--c3) 58%, var(--c4) 80%, var(--c1)) border-box;
  transition: box-shadow .25s;
}

@supports not (background-clip: padding-box) {
  .sb-36__bar {
    border-color: var(--c2);
    background: var(--card);
  }
}

.sb-36__wrap:hover .sb-36__bar,
.sb-36__wrap:focus-within .sb-36__bar {
  animation: sb-36-drift 9s linear infinite;
}

.sb-36__wrap:hover .sb-36__glow,
.sb-36__wrap:focus-within .sb-36__glow {
  animation: sb-36-drift 14s linear infinite reverse;
  opacity: .72;
}

@keyframes sb-36-drift {
  to {
    --sb-36-a: 360deg;
  }
}

.sb-36__wrap:focus-within .sb-36__bar {
  box-shadow: 0 0 0 4px rgba(139,92,246,.16);
}

.sb-36__ico {
  inline-size: 21px;
  block-size: 21px;
  flex: none;
  color: var(--c1);
}

.sb-36__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 1rem/1 inherit;
}

.sb-36__input::placeholder {
  color: var(--muted);
}

.sb-36__input:focus {
  outline: none;
}

.sb-36__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-36__go {
  display: grid;
  place-items: center;
  inline-size: 46px;
  block-size: 46px;
  flex: none;
  border: 0;
  border-radius: 13px;
  background: linear-gradient(140deg, var(--c2), var(--c1));
  color: #08090f;
  cursor: pointer;
  transition: filter .18s, scale .12s;
}

.sb-36__go:hover {
  filter: brightness(1.12);
}

.sb-36__go:active {
  scale: .95;
}

.sb-36__go svg {
  inline-size: 19px;
  block-size: 19px;
}

.sb-36 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.sb-36__input:focus-visible {
  outline: none;
}

.sb-36[data-theme="light"] {
  --bg: #f7f7fb;
  --card: #ffffff;
  --ink: #12141c;
  --muted: #6b7183;
  --line: #e5e7f0;
  --c1: #0d9488;
  --c2: #7c3aed;
  --c3: #e11d48;
  --c4: #0284c7;
  --ring: #7c3aed;
  background: radial-gradient(50rem 30rem at 50% 120%, rgba(124,58,237,.10), transparent 66%), var(--bg);
}

.sb-36[data-theme="light"] .sb-36__glow {
  opacity: .34;
}

.sb-36[data-theme="light"] .sb-36__go {
  color: #fff;
}

@media (prefers-color-scheme: light) {
  .sb-36:not([data-theme="dark"]) {
    --bg: #f7f7fb;
    --card: #ffffff;
    --ink: #12141c;
    --muted: #6b7183;
    --line: #e5e7f0;
    --c1: #0d9488;
    --c2: #7c3aed;
    --c3: #e11d48;
    --c4: #0284c7;
    --ring: #7c3aed;
    background: radial-gradient(50rem 30rem at 50% 120%, rgba(124,58,237,.10), transparent 66%), var(--bg);
  }

  .sb-36:not([data-theme="dark"]) .sb-36__glow {
    opacity: .34;
  }

  .sb-36:not([data-theme="dark"]) .sb-36__go {
    color: #fff;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-36 *,
    .sb-36 *::before,
    .sb-36 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .sb-36__bar {
    border: 2px solid CanvasText;
    background: Canvas;
  }

  .sb-36__glow {
    display: none;
  }
}

.sb-36__theme {
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

.sb-36[data-theme="dark"] .sb-36__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-36:not([data-theme="light"]) .sb-36__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-36__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-36[data-theme="dark"] .sb-36__theme:hover,
.sb-36:not([data-theme="light"]) .sb-36__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-36__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-36__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-36__sun {
  display: none;
}

.sb-36__theme[aria-pressed="true"] .sb-36__sun {
  display: block;
}

.sb-36__theme[aria-pressed="true"] .sb-36__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-36__theme {
    transition: none;
  }

  .sb-36__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-36');if(!r)return;const t=r.querySelector('.sb-36__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
