---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/border-trace/"
title: "CSS Search Bar with Animated Border Trace"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "On focus, a single accent stroke runs around the field like a light travelling a wire, then settles into a full outline."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Search Bar with Animated Border Trace
Source: https://codefronts.com/components/css-search-boxes/border-trace/

On focus, a single accent stroke runs around the field like a light travelling a wire, then settles into a full outline. Drawn with an inline SVG rounded rect and stroke-dashoffset — pixel-crisp at any size, and immune to the corner artefacts gradient-border tricks produce.
## HTML
```html
<div class="sb-34">
  <button class="sb-34__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-34__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-34__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-34__stage">
    <div class="sb-34__bar" role="search">
      <svg class="sb-34__outline" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true" focusable="false">
        <rect class="sb-34__base" x="1" y="1" width="98" height="98" rx="14" ry="14" pathLength="100" fill="none" stroke="currentColor" stroke-width="2" vector-effect="non-scaling-stroke"></rect>
        <rect class="sb-34__trace" x="1" y="1" width="98" height="98" rx="14" ry="14" pathLength="100" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" vector-effect="non-scaling-stroke"></rect>
      </svg>
      <svg class="sb-34__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      <label class="sb-34__vh" for="sb-34-input">Search components</label>
      <input class="sb-34__input" id="sb-34-input" type="search" placeholder="Search components and tokens" autocomplete="off">
      <kbd class="sb-34__kbd">&crarr;</kbd>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-34 {
  --bg: #0e1015;
  --card: #161a22;
  --ink: #eef1f7;
  --muted: #8b93a3;
  --line: #262d3a;
  --acc: #4ade80;
  --acc-2: #22d3ee;
  --ring: #4ade80;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: radial-gradient(38rem 22rem at 50% 34%, rgba(74,222,128,.08), transparent 70%), var(--bg);
  -webkit-font-smoothing: antialiased;
}

.sb-34 *,
.sb-34 *::before,
.sb-34 *::after {
  box-sizing: border-box;
}

.sb-34__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-34__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-34__bar {
  position: relative;
  display: flex;
  align-items: center;
  gap: .75rem;
  inline-size: min(31rem,100%);
  min-block-size: 58px;
  padding-inline: 1.1rem .5rem;
  border-radius: 14px;
  background: var(--card);
}

.sb-34__outline {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
  pointer-events: none;
}

.sb-34__base {
  color: var(--line);
}

.sb-34__trace {
  color: var(--acc);
  opacity: 0;
  stroke-dasharray: 18 82;
  stroke-dashoffset: 100;
  filter: drop-shadow(0 0 6px currentColor);
  transition: opacity .18s;
}

.sb-34__bar:focus-within .sb-34__base {
  color: transparent;
}

.sb-34__bar:focus-within .sb-34__trace {
  opacity: 1;
  animation: sb-34-run .75s cubic-bezier(.4,0,.2,1) forwards;
}

@keyframes sb-34-run {
  0% {
    stroke-dasharray: 18 82;
    stroke-dashoffset: 100;
  }

  70% {
    stroke-dasharray: 18 82;
    stroke-dashoffset: 0;
  }

  100% {
    stroke-dasharray: 100 0;
    stroke-dashoffset: 0;
  }
}

.sb-34__ico {
  position: relative;
  inline-size: 19px;
  block-size: 19px;
  flex: none;
  color: var(--muted);
  transition: color .2s;
}

.sb-34__bar:focus-within .sb-34__ico {
  color: var(--acc);
}

.sb-34__input {
  position: relative;
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .97rem/1 inherit;
}

.sb-34__input::placeholder {
  color: var(--muted);
}

.sb-34__input:focus {
  outline: none;
}

.sb-34__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-34__kbd {
  position: relative;
  display: inline-grid;
  place-items: center;
  inline-size: 2rem;
  block-size: 2rem;
  flex: none;
  border: 1px solid var(--line);
  border-radius: 8px;
  background: #11151c;
  color: var(--muted);
  font: 500 .8rem/1 ui-monospace,Menlo,monospace;
}

.sb-34 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.sb-34__input:focus-visible {
  outline: none;
}

.sb-34[data-theme="light"] {
  --bg: #f5f7f6;
  --card: #ffffff;
  --ink: #0f1720;
  --muted: #68707e;
  --line: #e0e5e2;
  --acc: #0f9d58;
  --acc-2: #0891b2;
  --ring: #0f9d58;
  background: radial-gradient(38rem 22rem at 50% 34%, rgba(15,157,88,.07), transparent 70%), var(--bg);
}

.sb-34[data-theme="light"] .sb-34__kbd {
  background: #f7f9f8;
}

.sb-34[data-theme="light"] .sb-34__trace {
  filter: none;
}

@media (prefers-color-scheme: light) {
  .sb-34:not([data-theme="dark"]) {
    --bg: #f5f7f6;
    --card: #ffffff;
    --ink: #0f1720;
    --muted: #68707e;
    --line: #e0e5e2;
    --acc: #0f9d58;
    --acc-2: #0891b2;
    --ring: #0f9d58;
    background: radial-gradient(38rem 22rem at 50% 34%, rgba(15,157,88,.07), transparent 70%), var(--bg);
  }

  .sb-34:not([data-theme="dark"]) .sb-34__kbd {
    background: #f7f9f8;
  }

  .sb-34:not([data-theme="dark"]) .sb-34__trace {
    filter: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-34 *,
    .sb-34 *::before,
    .sb-34 *::after {
    animation: none !important;
    transition: none !important;
  }

  .sb-34__bar:focus-within .sb-34__trace {
    opacity: 1;
    stroke-dasharray: 100 0;
    stroke-dashoffset: 0;
  }
}

@media (forced-colors: active) {
  .sb-34__bar {
    border: 1px solid CanvasText;
  }

  .sb-34__outline {
    display: none;
  }
}

.sb-34__theme {
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

.sb-34[data-theme="dark"] .sb-34__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-34:not([data-theme="light"]) .sb-34__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-34__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-34[data-theme="dark"] .sb-34__theme:hover,
.sb-34:not([data-theme="light"]) .sb-34__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-34__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-34__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-34__sun {
  display: none;
}

.sb-34__theme[aria-pressed="true"] .sb-34__sun {
  display: block;
}

.sb-34__theme[aria-pressed="true"] .sb-34__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-34__theme {
    transition: none;
  }

  .sb-34__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-34');if(!r)return;const t=r.querySelector('.sb-34__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
