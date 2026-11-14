---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/caret-highlight/"
title: "CSS Search Bar with Animated Caret Highlight"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "An editor-grade field: the native caret is hidden and replaced with a glowing block cursor that tracks the real text width, blinking on a 1.06s square wave…"
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Search Bar with Animated Caret Highlight
Source: https://codefronts.com/components/css-search-boxes/caret-highlight/

An editor-grade field: the native caret is hidden and replaced with a glowing block cursor that tracks the real text width, blinking on a 1.06s square wave and dragging a soft highlight wash behind it. Measured with a mirrored span — no canvas, no font metrics guesswork.
## HTML
```html
<div class="sb-10">
  <button class="sb-10__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-10__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-10__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-10__stage">
    <div class="sb-10__bar" role="search">
      <span class="sb-10__prompt" aria-hidden="true">&gt;</span>
      <label class="sb-10__vh" for="sb-10-input">Search files by name or content</label>
      <span class="sb-10__box">
        <input class="sb-10__input" id="sb-10-input" type="search" value="annual report" placeholder="find in project" autocomplete="off" spellcheck="false">
        <span class="sb-10__mirror" aria-hidden="true"></span>
        <span class="sb-10__wash" aria-hidden="true"></span>
        <span class="sb-10__caret" aria-hidden="true"></span>
      </span>
      <span class="sb-10__count" aria-hidden="true">12/48</span>
    </div>
  </div>
</div>
```
## CSS
```css
@property --sb-10-x {
  syntax: '<length>';
  inherits: true;
  initial-value: 0px;
}

.sb-10 {
  --bg: #0d1117;
  --panel: #151b23;
  --ink: #e6edf3;
  --muted: #7d8590;
  --line: #242c37;
  --acc: #7ee787;
  --acc-2: #58a6ff;
  --ring: #58a6ff;
  --mono: "JetBrains Mono",ui-monospace,"SF Mono",Menlo,Consolas,monospace;
  --sb-10-x: 0px;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: var(--mono);
  color: var(--ink);
  background: radial-gradient(40rem 26rem at 50% 30%, rgba(88,166,255,.08), transparent 70%), var(--bg);
  -webkit-font-smoothing: antialiased;
}

.sb-10 *,
.sb-10 *::before,
.sb-10 *::after {
  box-sizing: border-box;
}

.sb-10__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-10__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-10__bar {
  display: flex;
  align-items: center;
  gap: .7rem;
  inline-size: min(34rem,100%);
  min-block-size: 54px;
  padding-inline: 1rem;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--panel);
  box-shadow: 0 20px 40px -28px #000;
  transition: border-color .2s, box-shadow .2s;
}

.sb-10__bar:focus-within {
  border-color: var(--acc-2);
  box-shadow: 0 0 0 3px rgba(88,166,255,.2), 0 20px 40px -28px #000;
}

.sb-10__prompt {
  flex: none;
  color: var(--acc);
  font: 700 1rem/1 inherit;
}

.sb-10__box {
  position: relative;
  flex: 1;
  min-inline-size: 0;
  display: flex;
  align-items: center;
  block-size: 100%;
}

.sb-10__input {
  position: relative;
  z-index: 2;
  inline-size: 100%;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .98rem/1 inherit;
  letter-spacing: 0;
  caret-color: transparent;
  padding: 0;
}

.sb-10__input::placeholder {
  color: var(--muted);
}

.sb-10__input:focus {
  outline: none;
}

.sb-10__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-10__mirror {
  position: absolute;
  inset-block-start: -999px;
  inset-inline-start: 0;
  visibility: hidden;
  white-space: pre;
  font: 400 .98rem/1 var(--mono);
  letter-spacing: 0;
}

.sb-10__caret {
  position: absolute;
  z-index: 3;
  inset-block: .75rem;
  inset-inline-start: 0;
  inline-size: 2px;
  background: var(--acc);
  border-radius: 1px;
  box-shadow: 0 0 10px 1px var(--acc);
  translate: var(--sb-10-x) 0;
  opacity: 0;
  transition: translate .09s cubic-bezier(.2,.9,.25,1);
}

.sb-10__bar:focus-within .sb-10__caret {
  opacity: 1;
  animation: sb-10-blink 1.06s infinite;
}

@keyframes sb-10-blink {
  0%,
    49% {
    opacity: 1;
  }

  50%,
    100% {
    opacity: 0;
  }
}

.sb-10__wash {
  position: absolute;
  z-index: 1;
  inset-block: .55rem;
  inset-inline-start: 0;
  inline-size: 7rem;
  background: linear-gradient(90deg, transparent, color-mix(in srgb, var(--acc) 16%, transparent) 65%, color-mix(in srgb, var(--acc) 26%, transparent));
  border-radius: 6px;
  opacity: 0;
  translate: calc(var(--sb-10-x) - 7rem) 0;
  transition: translate .12s cubic-bezier(.2,.9,.25,1), opacity .2s;
}

.sb-10__bar:focus-within .sb-10__wash {
  opacity: 1;
}

.sb-10__count {
  flex: none;
  color: var(--muted);
  font: 500 .78rem/1 inherit;
  font-variant-numeric: tabular-nums;
}

.sb-10 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.sb-10__input:focus-visible {
  outline: none;
}

.sb-10[data-theme="light"] {
  --bg: #f6f8fa;
  --panel: #fff;
  --ink: #1f2328;
  --muted: #656d76;
  --line: #d0d7de;
  --acc: #1a7f37;
  --acc-2: #0969da;
  --ring: #0969da;
  background: radial-gradient(40rem 26rem at 50% 30%, rgba(9,105,218,.07), transparent 70%), var(--bg);
}

.sb-10[data-theme="light"] .sb-10__caret {
  box-shadow: none;
}

@media (prefers-color-scheme: light) {
  .sb-10:not([data-theme="dark"]) {
    --bg: #f6f8fa;
    --panel: #fff;
    --ink: #1f2328;
    --muted: #656d76;
    --line: #d0d7de;
    --acc: #1a7f37;
    --acc-2: #0969da;
    --ring: #0969da;
    background: radial-gradient(40rem 26rem at 50% 30%, rgba(9,105,218,.07), transparent 70%), var(--bg);
  }

  .sb-10:not([data-theme="dark"]) .sb-10__caret {
    box-shadow: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-10 *,
    .sb-10 *::before,
    .sb-10 *::after {
    animation: none !important;
    transition: none !important;
  }

  .sb-10__bar:focus-within .sb-10__caret {
    opacity: 1;
  }
}

@media (forced-colors: active) {
  .sb-10__bar {
    border: 1px solid CanvasText;
  }

  .sb-10__caret {
    background: Highlight;
    box-shadow: none;
  }

  .sb-10__wash {
    display: none;
  }
}

.sb-10__theme {
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

.sb-10[data-theme="dark"] .sb-10__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-10:not([data-theme="light"]) .sb-10__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-10__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-10[data-theme="dark"] .sb-10__theme:hover,
.sb-10:not([data-theme="light"]) .sb-10__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-10__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-10__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-10__sun {
  display: none;
}

.sb-10__theme[aria-pressed="true"] .sb-10__sun {
  display: block;
}

.sb-10__theme[aria-pressed="true"] .sb-10__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-10__theme {
    transition: none;
  }

  .sb-10__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sb-10');
  if (!root) return;
  const input = root.querySelector('#sb-10-input');
  const mirror = root.querySelector('.sb-10__mirror');
  const caret = root.querySelector('.sb-10__caret');

  const place = () => {
    mirror.textContent = input.value.slice(0, input.selectionStart ?? input.value.length);
    root.style.setProperty('--sb-10-x', mirror.offsetWidth + 'px');
    caret.style.animation = 'none';                 /* solid while typing, like a native caret */
    void caret.offsetWidth;
    caret.style.animation = '';
  };
  ['input', 'click', 'keyup', 'focus', 'select'].forEach((evt) => input.addEventListener(evt, place));
  place();
})();
(()=>{const r=document.querySelector('.sb-10');if(!r)return;const t=r.querySelector('.sb-10__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
