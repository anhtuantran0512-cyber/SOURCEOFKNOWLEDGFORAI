---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/inline-loading-bar/"
title: "CSS Search Bar with Inline Loading Progress Bar"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "A hairline progress bar rides the field's bottom edge: an indeterminate sweep while the request is in flight, then a determinate fill to 100% and a fade-out."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Search Bar with Inline Loading Progress Bar
Source: https://codefronts.com/components/css-search-boxes/inline-loading-bar/

A hairline progress bar rides the field's bottom edge: an indeterminate sweep while the request is in flight, then a determinate fill to 100% and a fade-out. Two keyframes, one data-state, and a real role="progressbar" for assistive tech.
## HTML
```html
<div class="sb-27">
  <button class="sb-27__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-27__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-27__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-27__stage">
    <div class="sb-27__bar" id="sb-27-bar" role="search" data-state="idle">
      <svg class="sb-27__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      <label class="sb-27__vh" for="sb-27-input">Search the catalogue</label>
      <input class="sb-27__input" id="sb-27-input" type="search" placeholder="Search 2.4M records&hellip;" autocomplete="off">
      <button class="sb-27__go" id="sb-27-go" type="button">Search</button>
      <span class="sb-27__track" id="sb-27-progress" role="progressbar" aria-label="Search progress">
        <span class="sb-27__fill"></span>
      </span>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-27 {
  --bg: #f5f6f9;
  --card: #ffffff;
  --ink: #131720;
  --muted: #69707e;
  --line: #e3e6ed;
  --acc: #e11d48;
  --acc-2: #f43f5e;
  --wash: rgba(225,29,72,.10);
  --ring: #e11d48;
  --shadow: rgba(19,23,32,.14);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: radial-gradient(40rem 22rem at 50% 8%, #fff, var(--bg) 74%);
  -webkit-font-smoothing: antialiased;
}

.sb-27 *,
.sb-27 *::before,
.sb-27 *::after {
  box-sizing: border-box;
}

.sb-27__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-27__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-27__bar {
  position: relative;
  display: flex;
  align-items: center;
  gap: .7rem;
  overflow: hidden;
  inline-size: min(32rem,100%);
  min-block-size: 56px;
  padding-inline: 1.05rem .45rem;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--card);
  box-shadow: 0 1px 2px rgba(19,23,32,.05);
  transition: border-color .2s, box-shadow .2s;
}

.sb-27__bar:focus-within {
  border-color: var(--acc);
  box-shadow: 0 0 0 4px var(--wash);
}

.sb-27__ico {
  inline-size: 19px;
  block-size: 19px;
  flex: none;
  color: var(--muted);
}

.sb-27__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .96rem/1 inherit;
}

.sb-27__input::placeholder {
  color: var(--muted);
}

.sb-27__input:focus {
  outline: none;
}

.sb-27__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-27__go {
  flex: none;
  min-block-size: 44px;
  padding-inline: 1.1rem;
  border: 0;
  border-radius: 10px;
  background: var(--acc);
  color: #fff;
  cursor: pointer;
  font: 600 .88rem/1 inherit;
  transition: filter .18s, scale .12s;
}

.sb-27__go:hover {
  filter: brightness(1.08);
}

.sb-27__go:active {
  scale: .97;
}

.sb-27__go:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.sb-27__track {
  position: absolute;
  inset-inline: 0;
  inset-block-end: 0;
  block-size: 2.5px;
  overflow: hidden;
  opacity: 0;
  transition: opacity .25s;
}

.sb-27__fill {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 99px;
  background: linear-gradient(90deg, var(--acc), var(--acc-2));
  -webkit-transform: scaleX(0);
  transform: scaleX(0);
  scale: 0 1;
  transform-origin: left center;
}

.sb-27__bar[data-state="loading"] .sb-27__track,
.sb-27__bar[data-state="done"] .sb-27__track {
  opacity: 1;
}

.sb-27__bar[data-state="loading"] .sb-27__fill {
  animation: sb-27-sweep 1.15s ease-in-out infinite;
}

@keyframes sb-27-sweep {
  0% {
    -webkit-transform: translateX(-100%) scaleX(.35);
    transform: translateX(-100%) scaleX(.35);
    translate: -100% 0;
    scale: .35 1;
  }

  50% {
    -webkit-transform: translateX(20%) scaleX(.6);
    transform: translateX(20%) scaleX(.6);
    translate: 20% 0;
    scale: .6 1;
  }

  100% {
    -webkit-transform: translateX(100%) scaleX(.35);
    transform: translateX(100%) scaleX(.35);
    translate: 100% 0;
    scale: .35 1;
  }
}

.sb-27__bar[data-state="done"] .sb-27__fill {
  animation: none;
  -webkit-transform: scaleX(1);
  transform: scaleX(1);
  translate: 0 0;
  scale: 1 1;
  transition: scale .3s cubic-bezier(.2,.9,.25,1), transform .3s cubic-bezier(.2,.9,.25,1);
}

.sb-27[data-theme="dark"] {
  --bg: #0b0e14;
  --card: #141922;
  --ink: #e9ecf4;
  --muted: #878f9e;
  --line: #232a37;
  --acc: #fb7185;
  --acc-2: #f472b6;
  --wash: rgba(251,113,133,.14);
  --ring: #fb7185;
  --shadow: rgba(0,0,0,.7);
  background: radial-gradient(40rem 22rem at 50% 8%, #171d29, var(--bg) 74%);
}

.sb-27[data-theme="dark"] .sb-27__go {
  color: #160b10;
}

@media (prefers-color-scheme: dark) {
  .sb-27:not([data-theme="light"]) {
    --bg: #0b0e14;
    --card: #141922;
    --ink: #e9ecf4;
    --muted: #878f9e;
    --line: #232a37;
    --acc: #fb7185;
    --acc-2: #f472b6;
    --wash: rgba(251,113,133,.14);
    --ring: #fb7185;
    --shadow: rgba(0,0,0,.7);
    background: radial-gradient(40rem 22rem at 50% 8%, #171d29, var(--bg) 74%);
  }

  .sb-27:not([data-theme="light"]) .sb-27__go {
    color: #160b10;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-27 *,
    .sb-27 *::before,
    .sb-27 *::after {
    transition: none !important;
  }

  .sb-27__bar[data-state="loading"] .sb-27__fill {
    animation: none;
    scale: .4 1;
  }
}

@media (forced-colors: active) {
  .sb-27__bar {
    border: 1px solid CanvasText;
  }

  .sb-27__fill {
    background: Highlight;
  }
}

.sb-27__theme {
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

.sb-27[data-theme="dark"] .sb-27__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-27:not([data-theme="light"]) .sb-27__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-27__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-27[data-theme="dark"] .sb-27__theme:hover,
.sb-27:not([data-theme="light"]) .sb-27__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-27__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-27__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-27__sun {
  display: none;
}

.sb-27__theme[aria-pressed="true"] .sb-27__sun {
  display: block;
}

.sb-27__theme[aria-pressed="true"] .sb-27__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-27__theme {
    transition: none;
  }

  .sb-27__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sb-27');
  if (!root) return;
  const bar = root.querySelector('#sb-27-bar');
  const input = root.querySelector('#sb-27-input');
  const pb = root.querySelector('#sb-27-progress');
  let t1, t2;

  const run = () => {
    clearTimeout(t1); clearTimeout(t2);
    bar.dataset.state = 'loading';
    bar.setAttribute('aria-busy', 'true');
    pb.removeAttribute('aria-valuenow');                 /* indeterminate: omit the value */
    t1 = setTimeout(() => {
      bar.dataset.state = 'done';                        /* fill to 100% */
      pb.setAttribute('aria-valuenow', '100');
      pb.setAttribute('aria-valuetext', 'Search complete');
      bar.removeAttribute('aria-busy');
      t2 = setTimeout(() => { bar.dataset.state = 'idle'; }, 700);
    }, 1400);
  };

  root.querySelector('#sb-27-go').addEventListener('click', run);
  input.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); run(); } });
})();
(()=>{const r=document.querySelector('.sb-27');if(!r)return;const t=r.querySelector('.sb-27__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
