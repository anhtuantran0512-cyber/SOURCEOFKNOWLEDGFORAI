---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/glitch-search/"
title: "CSS Glitch Search Bar with RGB Split Effect"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "Chromatic aberration on a search field: the label splits into red and cyan ghosts that drift a pixel or two at rest and tear into clipped slices on focus."
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Glitch Search Bar with RGB Split Effect
Source: https://codefronts.com/components/css-search-boxes/glitch-search/

Chromatic aberration on a search field: the label splits into red and cyan ghosts that drift a pixel or two at rest and tear into clipped slices on focus. Built from two ::before/::after copies driven by attr() content and clip-path keyframes.
## HTML
```html
<div class="sb-29">
  <button class="sb-29__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-29__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-29__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-29__stage">
    <div class="sb-29__wrap" role="search">
      <span class="sb-29__label" data-text="SEARCH_NODE">SEARCH_NODE</span>
      <div class="sb-29__bar">
        <span class="sb-29__prompt" aria-hidden="true">&gt;_</span>
        <label class="sb-29__vh" for="sb-29-input">Search the network</label>
        <input class="sb-29__input" id="sb-29-input" type="search" placeholder="query the network&hellip;" autocomplete="off" spellcheck="false">
        <span class="sb-29__status" aria-hidden="true">
          <i></i>LIVE
        </span>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-29 {
  --bg: #07070c;
  --card: #0e0e16;
  --ink: #f2f3ff;
  --muted: #8d8fb4;
  --line: #23233a;
  --r: #ff2d55;
  --c: #00e5ff;
  --ring: #00e5ff;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: ui-monospace,"SF Mono",Menlo,Consolas,monospace;
  color: var(--ink);
  background: radial-gradient(36rem 22rem at 50% 40%, rgba(0,229,255,.07), transparent 70%), var(--bg);
  -webkit-font-smoothing: antialiased;
}

.sb-29 *,
.sb-29 *::before,
.sb-29 *::after {
  box-sizing: border-box;
}

.sb-29__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-29__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-29__wrap {
  inline-size: min(32rem,100%);
  display: flex;
  flex-direction: column;
  gap: .85rem;
}

.sb-29__label {
  position: relative;
  align-self: start;
  color: var(--ink);
  font: 700 clamp(1.4rem,1rem + 2vw,2.1rem)/1 inherit;
  letter-spacing: .14em;
}

.sb-29__label::before,
.sb-29__label::after {
  content: attr(data-text);
  position: absolute;
  inset-block-start: 0;
  inset-inline-start: 0;
  opacity: .55;
  mix-blend-mode: screen;
  pointer-events: none;
}

.sb-29__label::before {
  color: var(--r);
  -webkit-transform: translateX(-.6px);
  transform: translateX(-.6px);
  translate: -.6px 0;
  animation: sb-29-idle-a 3.6s steps(2,end) infinite;
}

.sb-29__label::after {
  color: var(--c);
  -webkit-transform: translateX(.6px);
  transform: translateX(.6px);
  translate: .6px 0;
  animation: sb-29-idle-b 4.2s steps(2,end) infinite;
}

@keyframes sb-29-idle-a {
  0%,
    92% {
    translate: -.6px 0;
  }

  94% {
    translate: -2.4px 1px;
  }

  96% {
    translate: 1px -1px;
  }

  100% {
    translate: -.6px 0;
  }
}

@keyframes sb-29-idle-b {
  0%,
    90% {
    translate: .6px 0;
  }

  93% {
    translate: 2.6px -1px;
  }

  97% {
    translate: -1px 1px;
  }

  100% {
    translate: .6px 0;
  }
}

.sb-29__bar {
  display: flex;
  align-items: center;
  gap: .7rem;
  min-block-size: 56px;
  padding-inline: 1rem;
  border: 1px solid var(--line);
  border-radius: 4px;
  background: var(--card);
  box-shadow: inset 0 0 0 1px rgba(0,229,255,.06);
  transition: border-color .2s, box-shadow .2s;
}

.sb-29__bar:focus-within {
  border-color: var(--c);
  box-shadow: 0 0 0 3px rgba(0,229,255,.16), inset 0 0 24px -14px var(--c);
}

.sb-29__wrap:focus-within .sb-29__label::before {
  animation: sb-29-tear-a .7s steps(3,end) 2;
}

.sb-29__wrap:focus-within .sb-29__label::after {
  animation: sb-29-tear-b .7s steps(3,end) 2;
}

@keyframes sb-29-tear-a {
  0%,
    100% {
    clip-path: inset(0 0 0 0);
    translate: -.6px 0;
  }

  18% {
    clip-path: inset(16% 0 60% 0);
    translate: -5px 0;
  }

  38% {
    clip-path: inset(54% 0 26% 0);
    translate: 4px 0;
  }

  62% {
    clip-path: inset(8% 0 82% 0);
    translate: -3px 0;
  }

  82% {
    clip-path: inset(72% 0 8% 0);
    translate: 2px 0;
  }
}

@keyframes sb-29-tear-b {
  0%,
    100% {
    clip-path: inset(0 0 0 0);
    translate: .6px 0;
  }

  22% {
    clip-path: inset(62% 0 18% 0);
    translate: 5px 0;
  }

  44% {
    clip-path: inset(24% 0 58% 0);
    translate: -4px 0;
  }

  70% {
    clip-path: inset(80% 0 6% 0);
    translate: 3px 0;
  }
}

.sb-29__prompt {
  flex: none;
  color: var(--c);
  font: 700 1rem/1 inherit;
  letter-spacing: .05em;
}

.sb-29__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  caret-color: var(--r);
  font: 500 .96rem/1 inherit;
  letter-spacing: .02em;
}

.sb-29__input::placeholder {
  color: var(--muted);
}

.sb-29__input:focus {
  outline: none;
}

.sb-29__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-29__status {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  flex: none;
  color: var(--muted);
  font: 600 .68rem/1 inherit;
  letter-spacing: .16em;
}

.sb-29__status i {
  inline-size: 6px;
  block-size: 6px;
  border-radius: 50%;
  background: var(--r);
  box-shadow: 0 0 8px var(--r);
  animation: sb-29-pulse 1.6s ease-in-out infinite;
}

@keyframes sb-29-pulse {
  50% {
    opacity: .35;
  }
}

.sb-29 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.sb-29__input:focus-visible {
  outline: none;
}

.sb-29[data-theme="light"] {
  --bg: #f2f3f7;
  --card: #ffffff;
  --ink: #0b0b14;
  --muted: #6a6d85;
  --line: #dcdfe8;
  --r: #e01040;
  --c: #0090b0;
  --ring: #0090b0;
  background: radial-gradient(36rem 22rem at 50% 40%, rgba(0,144,176,.07), transparent 70%), var(--bg);
}

.sb-29[data-theme="light"] .sb-29__label::before,
.sb-29[data-theme="light"] .sb-29__label::after {
  mix-blend-mode: multiply;
  opacity: .4;
}

@media (prefers-color-scheme: light) {
  .sb-29:not([data-theme="dark"]) {
    --bg: #f2f3f7;
    --card: #ffffff;
    --ink: #0b0b14;
    --muted: #6a6d85;
    --line: #dcdfe8;
    --r: #e01040;
    --c: #0090b0;
    --ring: #0090b0;
    background: radial-gradient(36rem 22rem at 50% 40%, rgba(0,144,176,.07), transparent 70%), var(--bg);
  }

  .sb-29:not([data-theme="dark"]) .sb-29__label::before,
    .sb-29:not([data-theme="dark"]) .sb-29__label::after {
    mix-blend-mode: multiply;
    opacity: .4;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-29 *,
    .sb-29 *::before,
    .sb-29 *::after {
    animation: none !important;
    transition: none !important;
  }

  .sb-29__label::before,
    .sb-29__label::after {
    opacity: .3;
  }
}

@media (forced-colors: active) {
  .sb-29__bar {
    border: 1px solid CanvasText;
  }

  .sb-29__label::before,
    .sb-29__label::after {
    display: none;
  }
}

.sb-29__theme {
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

.sb-29[data-theme="dark"] .sb-29__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-29:not([data-theme="light"]) .sb-29__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-29__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-29[data-theme="dark"] .sb-29__theme:hover,
.sb-29:not([data-theme="light"]) .sb-29__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-29__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-29__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-29__sun {
  display: none;
}

.sb-29__theme[aria-pressed="true"] .sb-29__sun {
  display: block;
}

.sb-29__theme[aria-pressed="true"] .sb-29__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-29__theme {
    transition: none;
  }

  .sb-29__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(()=>{const r=document.querySelector('.sb-29');if(!r)return;const t=r.querySelector('.sb-29__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
