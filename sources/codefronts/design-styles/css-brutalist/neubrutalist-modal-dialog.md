---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/neubrutalist-modal-dialog/"
title: "Neubrutalist Modal Dialog"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "A native <dialog> opened with showModal() — so the focus trap, Escape handling and inert background come from the platform, not from 200 lines of JavaScript."
has_js: "true"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neubrutalist Modal Dialog
Source: https://codefronts.com/design-styles/css-brutalist/neubrutalist-modal-dialog/

A native <dialog> opened with showModal() — so the focus trap, Escape handling and inert background come from the platform, not from 200 lines of JavaScript. The block has a pastel header strip, a black close button in the corner and a flat semi-opaque ::backdrop with no blur, because blur is the one thing this aesthetic never does.
## HTML
```html
<div class="brt-07">
  <button class="brt-07__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="brt-07__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-07__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
  </button>

  <div class="brt-07__stage">
    <section class="brt-07__card" aria-labelledby="brt-07-h">
      <h2 class="brt-07__h" id="brt-07-h">Northwind Studio</h2>
      <p class="brt-07__meta">14 pages · last published 3 days ago</p>
      <p class="brt-07__p">Archiving hides the project from your workspace and pauses billing for its seats. You can restore it for 90 days.</p>
      <div class="brt-07__actions">
        <button class="brt-07__open" id="brt-07-open" type="button">Archive project</button>
        <a class="brt-07__link" href="#brt-07-h">View activity</a>
      </div>
      <p class="brt-07__status" id="brt-07-status" role="status" aria-live="polite"></p>
    </section>

    <dialog class="brt-07__dialog" id="brt-07-dialog" aria-labelledby="brt-07-dh" aria-describedby="brt-07-dp">
      <header class="brt-07__strip">
        <h3 class="brt-07__dh" id="brt-07-dh">Archive this project?</h3>
        <button class="brt-07__x" id="brt-07-x" type="button" aria-label="Close dialog">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="3" stroke-linecap="square"/></svg>
        </button>
      </header>
      <div class="brt-07__body">
        <p class="brt-07__dp" id="brt-07-dp">Northwind Studio and its 14 pages will be hidden from the workspace. Custom domains stay reserved.</p>
        <ul class="brt-07__facts">
          <li><b>3 seats</b> released back to your plan</li>
          <li><b>90 days</b> to restore before deletion</li>
          <li><b>2 domains</b> stay pointed at a holding page</li>
        </ul>
        <label class="brt-07__confirm">
          <input class="brt-07__box" type="checkbox" id="brt-07-ack">
          <span>Tell the three collaborators by email</span>
        </label>
      </div>
      <footer class="brt-07__foot">
        <button class="brt-07__btn brt-07__btn--ghost" type="button" id="brt-07-cancel">Keep it active</button>
        <button class="brt-07__btn brt-07__btn--dark" type="button" id="brt-07-confirm" autofocus>Archive project</button>
      </footer>
    </dialog>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap');

.brt-07 {
  --page: #f8f5ed;
  --panel: #ffffff;
  --ink: #0b0b0f;
  --on: #0b0b0f;
  --muted: #4a4a52;
  --lilac: #c4b5fd;
  --mint: #86efac;
  --coral: #fda4af;
  --butter: #fde68a;
  --sky: #93c5fd;
  --strip: #c4b5fd;
  --edge: #000000;
  --sh: #000000;
  --bw: 3px;
  --r: 16px;
  --w: 34rem;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: 'Space Grotesk','Sora',ui-sans-serif,system-ui,sans-serif;
}

.brt-07 *,
.brt-07 *::before,
.brt-07 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-07 {
    --page: oklch(0.97 0.016 90);
    --panel: oklch(1 0 0);
    --ink: oklch(0.16 0.01 285);
    --lilac: oklch(0.82 0.11 296);
    --mint: oklch(0.89 0.13 155);
    --coral: oklch(0.83 0.10 15);
    --butter: oklch(0.92 0.11 95);
    --sky: oklch(0.83 0.09 250);
    --strip: oklch(0.82 0.11 296);
  }
}

.brt-07__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  padding: 0;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  border-radius: 10px;
  box-shadow: 4px 4px 0 var(--sh);
  cursor: pointer;
  transition: translate .14s ease, box-shadow .14s ease;
}

.brt-07__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-07__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-07__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-07__theme:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-07__sun {
  display: none;
}

.brt-07__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,3rem);
}

.brt-07__card {
  inline-size: min(30rem,100%);
  padding: clamp(1.4rem,3.5vw,2rem);
  background: var(--panel);
  border: var(--bw) solid var(--edge);
  border-radius: var(--r);
  box-shadow: 8px 8px 0 var(--sh);
}

.brt-07__h {
  margin: 0;
  font-size: clamp(1.5rem,4vw,2rem);
  font-weight: 700;
  letter-spacing: -.025em;
}

.brt-07__meta {
  margin: .35rem 0 0;
  font-size: .8rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.brt-07__p {
  margin: 1rem 0 1.5rem;
  font-size: .98rem;
  line-height: 1.55;
  color: var(--ink);
  text-wrap: pretty;
}

.brt-07__actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 1rem;
}

.brt-07__open {
  min-block-size: 2.9rem;
  padding: .75rem 1.15rem;
  font: inherit;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  background: var(--coral);
  color: var(--on);
  border: var(--bw) solid var(--edge);
  border-radius: 11px;
  box-shadow: 5px 5px 0 var(--sh);
  transition: translate .14s ease, box-shadow .14s ease;
}

.brt-07__open:hover {
  translate: -1px -1px;
  box-shadow: 7px 7px 0 var(--sh);
}

.brt-07__open:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-07__open:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-07__link {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.75rem;
  color: var(--ink);
  font-weight: 700;
  font-size: .95rem;
  text-decoration: 3px underline var(--sky);
  text-underline-offset: 4px;
}

.brt-07__link:hover {
  background: var(--sky);
  color: var(--on);
}

.brt-07__link:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 2px;
}

.brt-07__status {
  margin: 1.1rem 0 0;
  min-block-size: 1.2rem;
  font-size: .88rem;
  font-weight: 700;
}

.brt-07__status:not(:empty) {
  display: inline-block;
  padding: .4rem .6rem;
  background: var(--mint);
  color: var(--on);
  border: 2px solid var(--edge);
  border-radius: 8px;
}

.brt-07__dialog {
  inline-size: min(var(--w),calc(100% - 2rem));
  max-block-size: min(90svh,42rem);
  padding: 0;
  margin: auto;
  background: var(--panel);
  color: var(--ink);
  overflow: hidden;
  border: var(--bw) solid var(--edge);
  border-radius: var(--r);
  box-shadow: 12px 12px 0 var(--sh);
}

@supports selector(dialog: modal) {
  .brt-07__dialog {
    opacity: 1;
    translate: 0 0;
    scale: 1;
    transition: opacity .17s ease, translate .17s ease, scale .17s ease, display .17s allow-discrete, overlay .17s allow-discrete;
  }

  @starting-style {
    .brt-07__dialog[open] {
      opacity: 0;
      translate: 0 -12px;
      scale: .97;
    }
  }

  .brt-07__dialog:not([open]) {
    opacity: 0;
    translate: 0 -12px;
    scale: .97;
  }
}

.brt-07__dialog::backdrop {
  background: rgb(0 0 0 / .55);
  transition: opacity .17s ease, display .17s allow-discrete;
}

@starting-style {
  .brt-07__dialog[open]::backdrop {
    opacity: 0;
  }
}

.brt-07__strip {
  display: flex;
  align-items: center;
  gap: 1rem;
  justify-content: space-between;
  padding: .9rem 1rem .9rem 1.25rem;
  background: var(--strip);
  color: var(--on);
  border-block-end: var(--bw) solid var(--edge);
}

.brt-07__dh {
  margin: 0;
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: -.015em;
}

.brt-07__x {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  padding: 0;
  flex: none;
  background: var(--ink);
  color: var(--panel);
  border: var(--bw) solid var(--edge);
  border-radius: 9px;
  box-shadow: 3px 3px 0 var(--sh);
  cursor: pointer;
  transition: translate .13s ease, box-shadow .13s ease;
}

.brt-07__x svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.brt-07__x:active {
  translate: 2px 2px;
  box-shadow: 1px 1px 0 var(--sh);
}

.brt-07__x:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-07__body {
  padding: 1.25rem;
  overflow: auto;
}

.brt-07__dp {
  margin: 0 0 1rem;
  font-size: .98rem;
  line-height: 1.55;
  text-wrap: pretty;
}

.brt-07__facts {
  list-style: none;
  margin: 0 0 1.1rem;
  padding: 0;
  display: grid;
  gap: .5rem;
}

.brt-07__facts li {
  padding: .55rem .7rem;
  background: var(--page);
  border: 2px solid var(--edge);
  border-radius: 9px;
  font-size: .9rem;
}

.brt-07__confirm {
  display: grid;
  grid-template-columns: 1.6rem 1fr;
  gap: .7rem;
  align-items: center;
  min-block-size: 2.75rem;
  font-size: .92rem;
  cursor: pointer;
}

.brt-07__box {
  appearance: none;
  -webkit-appearance: none;
  margin: 0;
  inline-size: 1.6rem;
  block-size: 1.6rem;
  display: grid;
  place-items: center;
  background: var(--panel);
  cursor: pointer;
  border: var(--bw) solid var(--edge);
  border-radius: 6px;
  box-shadow: 3px 3px 0 var(--sh);
}

.brt-07__box::after {
  content: '';
  inline-size: .5rem;
  block-size: .9rem;
  border: solid var(--on);
  border-width: 0 4px 4px 0;
  rotate: 45deg;
  translate: 0 -2px;
  opacity: 0;
}

.brt-07__box:checked {
  background: var(--mint);
}

.brt-07__box:checked::after {
  opacity: 1;
}

.brt-07__box:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-07__foot {
  display: flex;
  flex-wrap: wrap;
  gap: .75rem;
  justify-content: flex-end;
  padding: 1rem 1.25rem 1.25rem;
  border-block-start: 2px dashed var(--edge);
}

.brt-07__btn {
  min-block-size: 2.75rem;
  padding: .7rem 1.1rem;
  font: inherit;
  font-size: .98rem;
  font-weight: 700;
  cursor: pointer;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  border-radius: 10px;
  box-shadow: 4px 4px 0 var(--sh);
  transition: translate .13s ease, box-shadow .13s ease;
}

.brt-07__btn--dark {
  background: var(--ink);
  color: var(--page);
}

.brt-07__btn--ghost {
  background: var(--panel);
}

.brt-07__btn:hover {
  translate: -1px -1px;
  box-shadow: 6px 6px 0 var(--sh);
}

.brt-07__btn:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-07__btn:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-07[data-theme="dark"] {
  --page: #131218;
  --panel: #201e28;
  --ink: #f7f5ef;
  --muted: #b5b1c2;
  --edge: #f7f5ef;
  --sh: #f7f5ef;
}

.brt-07[data-theme="dark"] .brt-07__moon {
  display: none;
}

.brt-07[data-theme="dark"] .brt-07__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-07:not([data-theme="light"]) {
    --page: #131218;
    --panel: #201e28;
    --ink: #f7f5ef;
    --muted: #b5b1c2;
    --edge: #f7f5ef;
    --sh: #f7f5ef;
  }

  .brt-07:not([data-theme="light"]) .brt-07__moon {
    display: none;
  }

  .brt-07:not([data-theme="light"]) .brt-07__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-07 *,
    .brt-07 *::before,
    .brt-07 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .brt-07__dialog,
    .brt-07__card,
    .brt-07__btn,
    .brt-07__x,
    .brt-07__theme {
    border-color: CanvasText;
    box-shadow: none;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-07__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.brt-07');
  if (!root) return;
  const dlg = root.querySelector('#brt-07-dialog');
  const open = root.querySelector('#brt-07-open');
  const status = root.querySelector('#brt-07-status');

  open.addEventListener('click', () => (dlg.showModal ? dlg.showModal() : (dlg.open = true)));
  root.querySelector('#brt-07-x').addEventListener('click', () => dlg.close('dismiss'));
  root.querySelector('#brt-07-cancel').addEventListener('click', () => dlg.close('cancel'));
  root.querySelector('#brt-07-confirm').addEventListener('click', () => dlg.close('archive'));
  dlg.addEventListener('click', (e) => { if (e.target === dlg) dlg.close('dismiss'); });

  dlg.addEventListener('close', () => {
    open.focus();                                     /* focus must come back */
    const notify = root.querySelector('#brt-07-ack').checked;
    status.textContent = dlg.returnValue === 'archive'
      ? 'Northwind Studio archived' + (notify ? ' — collaborators emailed.' : '.')
      : 'Still active. Nothing changed.';
  });
})();

(() => {                                     /* theme toggle */
  const root = document.querySelector('.brt-07');
  const btn = root && root.querySelector('.brt-07__theme');
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
