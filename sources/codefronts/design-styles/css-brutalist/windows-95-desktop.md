---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/windows-95-desktop/"
title: "Windows 95 Desktop UI"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "Window chrome, done properly: a beveled grey frame, a title bar with minimise/maximise/close boxes, a menu bar with a working keyboard-accessible dropdown,…"
has_js: "true"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Windows 95 Desktop UI
Source: https://codefronts.com/design-styles/css-brutalist/windows-95-desktop/

Window chrome, done properly: a beveled grey frame, a title bar with minimise/maximise/close boxes, a menu bar with a working keyboard-accessible dropdown, an inset content well, and a taskbar with a Start button and a live clock. The bevels are pure box-shadow — four inset shadows per element, no images and no borders faked with gradients.
## HTML
```html
<div class="brt-20">
  <button class="brt-20__theme brt-20__raise" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="brt-20__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-20__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
  </button>

  <div class="brt-20__stage">
    <div class="brt-20__desktop">
      <section class="brt-20__window brt-20__raise" aria-labelledby="brt-20-title">
        <header class="brt-20__titlebar">
          <span class="brt-20__ico" aria-hidden="true">
            <svg viewBox="0 0 16 16" fill="none"><rect x="1.5" y="2.5" width="13" height="11" stroke="currentColor" stroke-width="1.6"/><path d="M1.5 6h13" stroke="currentColor" stroke-width="1.6"/></svg>
          </span>
          <h2 class="brt-20__title" id="brt-20-title">Ledger.txt — Notepad</h2>
          <span class="brt-20__wbtns">
            <button class="brt-20__wbtn brt-20__raise" type="button" aria-label="Minimise window"><span class="brt-20__min" aria-hidden="true"></span></button>
            <button class="brt-20__wbtn brt-20__raise" type="button" aria-label="Maximise window"><span class="brt-20__max" aria-hidden="true"></span></button>
            <button class="brt-20__wbtn brt-20__raise" type="button" aria-label="Close window"><svg class="brt-20__close" viewBox="0 0 10 10" fill="none" aria-hidden="true" focusable="false"><path d="M1 1l8 8M9 1L1 9" stroke="currentColor" stroke-width="1.6"/></svg></button>
          </span>
        </header>

        <div class="brt-20__menubar">
          <button class="brt-20__menu" id="brt-20-mfile" type="button" aria-expanded="false" aria-controls="brt-20-file"><u>F</u>ile</button>
          <button class="brt-20__menu" type="button"><u>E</u>dit</button>
          <button class="brt-20__menu" type="button"><u>S</u>earch</button>
          <button class="brt-20__menu" type="button"><u>H</u>elp</button>
          <ul class="brt-20__dropdown brt-20__raise" id="brt-20-file" hidden>
            <li><button type="button">New<span>Ctrl+N</span></button></li>
            <li><button type="button">Open…<span>Ctrl+O</span></button></li>
            <li><button type="button">Save<span>Ctrl+S</span></button></li>
            <li class="brt-20__sep"></li>
            <li><button type="button">Page Setup…</button></li>
            <li><button type="button">Exit</button></li>
          </ul>
        </div>

        <div class="brt-20__client brt-20__sink">
          <p>WAREHOUSE LEDGER — WEEK 33</p>
          <p>&nbsp;</p>
          <p>MON 10/08  crate 118 received      qty 24   ok</p>
          <p>TUE 11/08  crate 119 received      qty 12   short 2</p>
          <p>WED 12/08  outbound 441 dispatched qty 30   ok</p>
          <p>THU 13/08  stock count, aisle C</p>
          <p>&nbsp;</p>
          <p>NOTE: reorder pallet straps before Friday.</p>
          <p>NOTE: forklift service due 21/08.</p>
        </div>

        <footer class="brt-20__statusbar">
          <span class="brt-20__sink brt-20__cell">Ln 9, Col 1</span>
          <span class="brt-20__sink brt-20__cell">1,204 bytes</span>
          <span class="brt-20__sink brt-20__cell">Read-only</span>
        </footer>
      </section>

      <div class="brt-20__taskbar brt-20__raise">
        <button class="brt-20__start brt-20__raise" id="brt-20-start" type="button" aria-expanded="false" aria-controls="brt-20-startmenu">
          <span class="brt-20__flag" aria-hidden="true"></span>Start
        </button>
        <ul class="brt-20__startmenu brt-20__raise" id="brt-20-startmenu" hidden>
          <li><button type="button">Programs</button></li>
          <li><button type="button">Documents</button></li>
          <li><button type="button">Settings</button></li>
          <li><button type="button">Find</button></li>
          <li class="brt-20__sep"></li>
          <li><button type="button">Shut Down…</button></li>
        </ul>
        <span class="brt-20__task brt-20__raise">Ledger.txt — Notepad</span>
        <span class="brt-20__tray brt-20__sink"><time class="brt-20__clock" id="brt-20-clock" datetime="09:41">09:41</time></span>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.brt-20 {
  --desk: #0f7c76;
  --face: #c0c0c0;
  --face2: #dfdfdf;
  --light: #ffffff;
  --shade: #808080;
  --dark: #000000;
  --title: #000080;
  --titletext: #ffffff;
  --ink: #000000;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--desk);
  color: var(--ink);
  font-family: system-ui,'Segoe UI',Tahoma,Arial,sans-serif;
  font-size: 13px;
}

.brt-20 *,
.brt-20 *::before,
.brt-20 *::after {
  box-sizing: border-box;
  border-radius: 0;
}

.brt-20__raise {
  background: var(--face);
  box-shadow: inset -1px -1px 0 var(--dark), inset 1px 1px 0 var(--light), inset -2px -2px 0 var(--shade), inset 2px 2px 0 var(--face2);
}

.brt-20__sink {
  background: var(--light);
  box-shadow: inset 1px 1px 0 var(--shade), inset -1px -1px 0 var(--light), inset 2px 2px 0 var(--dark), inset -2px -2px 0 var(--face2);
}

.brt-20__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 20;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  padding: 0;
  color: var(--ink);
  border: 0;
  cursor: pointer;
}

.brt-20__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-20__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.brt-20__theme:active {
  box-shadow: inset 1px 1px 0 var(--shade), inset -1px -1px 0 var(--light), inset 2px 2px 0 var(--dark);
}

.brt-20__theme:focus-visible {
  outline: 2px dotted var(--dark);
  outline-offset: -5px;
}

.brt-20__sun {
  display: none;
}

.brt-20__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(.75rem,3vw,2.5rem) clamp(.75rem,3vw,2.5rem) 4rem;
}

.brt-20__desktop {
  inline-size: min(52rem,100%);
  position: relative;
}

.brt-20__window {
  padding: 3px;
  box-shadow: inset -1px -1px 0 var(--dark), inset 1px 1px 0 var(--light), inset -2px -2px 0 var(--shade), inset 2px 2px 0 var(--face2), 4px 4px 0 rgb(0 0 0 / .35);
}

.brt-20__titlebar {
  display: flex;
  align-items: center;
  gap: .4rem;
  padding: .2rem .2rem .2rem .3rem;
  background: var(--title);
  color: var(--titletext);
}

.brt-20__ico {
  display: grid;
  place-items: center;
  inline-size: 1rem;
  block-size: 1rem;
  color: var(--titletext);
}

.brt-20__ico svg {
  inline-size: 1rem;
  block-size: 1rem;
}

.brt-20__title {
  margin: 0;
  flex: 1;
  font-size: .82rem;
  font-weight: 700;
  letter-spacing: .01em;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.brt-20__wbtns {
  display: flex;
  gap: 2px;
}

.brt-20__wbtn {
  inline-size: 1.5rem;
  block-size: 1.35rem;
  display: grid;
  place-items: center;
  padding: 0;
  border: 0;
  color: var(--ink);
  cursor: pointer;
  position: relative;
  font-size: .7rem;
  line-height: 1;
}

.brt-20__wbtn::after {
  content: '';
  position: absolute;
  inset: -6px -3px;
}

.brt-20__wbtn:active {
  box-shadow: inset 1px 1px 0 var(--shade), inset -1px -1px 0 var(--light), inset 2px 2px 0 var(--dark);
}

.brt-20__wbtn:focus-visible {
  outline: 2px dotted var(--dark);
  outline-offset: -4px;
}

.brt-20__min {
  inline-size: .6rem;
  block-size: 2px;
  background: var(--ink);
  translate: 0 .3rem;
}

.brt-20__max {
  inline-size: .65rem;
  block-size: .55rem;
  border: 2px solid var(--ink);
  border-block-start-width: 3px;
}

.brt-20__close {
  inline-size: .6rem;
  block-size: .6rem;
  color: var(--ink);
}

.brt-20__menubar {
  position: relative;
  display: flex;
  gap: 0;
  padding: .15rem .1rem;
  border-block-end: 1px solid var(--shade);
}

.brt-20__menu {
  min-block-size: 1.6rem;
  padding: .2rem .55rem;
  background: transparent;
  border: 0;
  cursor: pointer;
  font: inherit;
  font-size: .82rem;
  color: var(--ink);
}

.brt-20__menu u {
  text-underline-offset: 2px;
}

.brt-20__menu:hover,
.brt-20__menu[aria-expanded="true"] {
  background: var(--title);
  color: var(--titletext);
}

.brt-20__menu:focus-visible {
  outline: 2px dotted var(--dark);
  outline-offset: -3px;
}

.brt-20__dropdown {
  position: absolute;
  inset-block-start: 100%;
  inset-inline-start: .1rem;
  z-index: 12;
  min-inline-size: 12rem;
  margin: 0;
  padding: 2px;
  list-style: none;
  box-shadow: inset -1px -1px 0 var(--dark), inset 1px 1px 0 var(--light), inset -2px -2px 0 var(--shade), inset 2px 2px 0 var(--face2), 3px 3px 0 rgb(0 0 0 / .3);
}

.brt-20__dropdown[hidden] {
  display: none;
}

.brt-20__dropdown button {
  inline-size: 100%;
  display: flex;
  justify-content: space-between;
  gap: 1.5rem;
  min-block-size: 1.7rem;
  padding: .25rem .6rem;
  background: transparent;
  border: 0;
  cursor: pointer;
  font: inherit;
  font-size: .82rem;
  color: var(--ink);
  text-align: start;
}

.brt-20__dropdown button span {
  color: var(--shade);
}

.brt-20__dropdown button:hover {
  background: var(--title);
  color: var(--titletext);
}

.brt-20__dropdown button:hover span {
  color: var(--titletext);
}

.brt-20__dropdown button:focus-visible {
  outline: 2px dotted var(--titletext);
  outline-offset: -3px;
  background: var(--title);
  color: var(--titletext);
}

.brt-20__sep {
  block-size: 2px;
  margin: .25rem .3rem;
  box-shadow: inset 0 1px 0 var(--shade), inset 0 -1px 0 var(--light);
}

.brt-20__client {
  margin: 3px 0;
  padding: .7rem .8rem;
  min-block-size: clamp(11rem,34vh,20rem);
  overflow: auto;
  font-family: ui-monospace,'Courier New',Courier,monospace;
  font-size: .82rem;
  line-height: 1.5;
}

.brt-20__client p {
  margin: 0;
  white-space: pre-wrap;
}

.brt-20__statusbar {
  display: flex;
  gap: 3px;
  padding: 2px 0 0;
}

.brt-20__cell {
  flex: 0 1 auto;
  padding: .2rem .45rem;
  background: var(--face);
  font-size: .75rem;
  color: var(--ink);
}

.brt-20__cell:first-child {
  flex: 1;
}

.brt-20__taskbar {
  position: absolute;
  inset-inline: 0;
  inset-block-end: -3.1rem;
  display: flex;
  align-items: center;
  gap: .35rem;
  padding: .25rem;
}

.brt-20__start {
  display: flex;
  align-items: center;
  gap: .35rem;
  min-block-size: 1.9rem;
  padding: .25rem .6rem;
  border: 0;
  cursor: pointer;
  font: inherit;
  font-size: .82rem;
  font-weight: 700;
  color: var(--ink);
}

.brt-20__start:active,
.brt-20__start[aria-expanded="true"] {
  box-shadow: inset 1px 1px 0 var(--shade), inset -1px -1px 0 var(--light), inset 2px 2px 0 var(--dark);
}

.brt-20__start:focus-visible {
  outline: 2px dotted var(--dark);
  outline-offset: -4px;
}

.brt-20__flag {
  inline-size: 1rem;
  block-size: 1rem;
  background: linear-gradient(135deg, var(--dark) 0 45%, transparent 45%) no-repeat, var(--face2);
  box-shadow: inset 0 0 0 1px var(--shade);
}

.brt-20__startmenu {
  position: absolute;
  inset-block-end: 100%;
  inset-inline-start: .25rem;
  z-index: 14;
  min-inline-size: 11rem;
  margin: 0 0 .3rem;
  padding: 2px;
  list-style: none;
  box-shadow: inset -1px -1px 0 var(--dark), inset 1px 1px 0 var(--light), inset -2px -2px 0 var(--shade), inset 2px 2px 0 var(--face2), 3px 3px 0 rgb(0 0 0 / .3);
}

.brt-20__startmenu[hidden] {
  display: none;
}

.brt-20__startmenu button {
  inline-size: 100%;
  min-block-size: 2rem;
  padding: .3rem .7rem;
  background: transparent;
  border: 0;
  cursor: pointer;
  font: inherit;
  font-size: .85rem;
  color: var(--ink);
  text-align: start;
}

.brt-20__startmenu button:hover,
.brt-20__startmenu button:focus-visible {
  background: var(--title);
  color: var(--titletext);
  outline: none;
}

.brt-20__task {
  flex: 0 1 14rem;
  padding: .3rem .55rem;
  font-size: .78rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  color: var(--ink);
}

.brt-20__tray {
  margin-inline-start: auto;
  padding: .3rem .6rem;
  background: var(--face);
  font-size: .78rem;
  font-variant-numeric: tabular-nums;
  color: var(--ink);
}

.brt-20[data-theme="dark"] {
  --desk: #04211f;
  --face: #2b2b2b;
  --face2: #4a4a4a;
  --light: #6f6f6f;
  --shade: #141414;
  --dark: #000000;
  --title: #000040;
  --titletext: #ffffff;
  --ink: #f0f0f0;
}

.brt-20[data-theme="dark"] .brt-20__sink {
  background: #111111;
}

.brt-20[data-theme="dark"] .brt-20__moon {
  display: none;
}

.brt-20[data-theme="dark"] .brt-20__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-20:not([data-theme="light"]) {
    --desk: #04211f;
    --face: #2b2b2b;
    --face2: #4a4a4a;
    --light: #6f6f6f;
    --shade: #141414;
    --dark: #000000;
    --title: #000040;
    --titletext: #ffffff;
    --ink: #f0f0f0;
  }

  .brt-20:not([data-theme="light"]) .brt-20__sink {
    background: #111111;
  }

  .brt-20:not([data-theme="light"]) .brt-20__moon {
    display: none;
  }

  .brt-20:not([data-theme="light"]) .brt-20__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-20 *,
    .brt-20 *::before,
    .brt-20 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .brt-20__raise,
    .brt-20__sink {
    box-shadow: none;
    border: 1px solid CanvasText;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-20__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.brt-20');
  if (!root) return;
  const pairs = [['#brt-20-mfile', '#brt-20-file'], ['#brt-20-start', '#brt-20-startmenu']];
  const closeAll = () => pairs.forEach(([b, p]) => {
    root.querySelector(b).setAttribute('aria-expanded', 'false');
    root.querySelector(p).hidden = true;
  });
  pairs.forEach(([b, p]) => {
    const btn = root.querySelector(b), panel = root.querySelector(p);
    btn.addEventListener('click', () => {
      const open = btn.getAttribute('aria-expanded') === 'true';
      closeAll();
      if (!open) { btn.setAttribute('aria-expanded', 'true'); panel.hidden = false; panel.querySelector('button').focus(); }
    });
  });
  root.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeAll(); });
  document.addEventListener('click', (e) => { if (!e.target.closest('.brt-20__menubar, .brt-20__taskbar')) closeAll(); });

  const clock = root.querySelector('#brt-20-clock');
  const tick = () => {
    const d = new Date();
    const hh = String(d.getHours()).padStart(2, '0'), mm = String(d.getMinutes()).padStart(2, '0');
    clock.textContent = hh + ':' + mm;
    clock.setAttribute('datetime', hh + ':' + mm);
  };
  tick(); setInterval(tick, 30000);
})();

(() => {                                     /* theme toggle */
  const root = document.querySelector('.brt-20');
  const btn = root && root.querySelector('.brt-20__theme');
  if (!btn) return;
  const dark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => {
    btn.setAttribute('aria-pressed', String(dark()));
    btn.setAttribute('aria-label', dark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  btn.addEventListener('click', () => { root.dataset.theme = dark() ? 'light' : 'dark'; sync(); });
  sync();
})();
```
