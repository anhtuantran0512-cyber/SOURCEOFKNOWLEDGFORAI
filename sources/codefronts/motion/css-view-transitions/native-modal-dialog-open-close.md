---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/native-modal-dialog-open-close/"
title: "Native Modal Dialog Open Close"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "Animating a real <dialog> opened with showModal(), backdrop included."
has_js: "true"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Native Modal Dialog Open Close
Source: https://codefronts.com/motion/css-view-transitions/native-modal-dialog-open-close/

Animating a real <dialog> opened with showModal(), backdrop included. The wrinkle is that both the dialog and the view-transition pseudo-elements live in the top layer, so the interaction is subtler than it looks — this shows what actually works, and compares it against the @starting-style plus transition-behavior: allow-discrete route.
## HTML
```html
<section class="vtr-14" aria-labelledby="vtr-14-heading">
  <fieldset class="vtr-14__theme">
    <legend class="vtr-14__themelegend">Theme</legend>
    <input class="vtr-14__themeinput" type="radio" name="vtr-14-theme" id="vtr-14-theme-auto" checked>
    <label class="vtr-14__themeopt" for="vtr-14-theme-auto">Auto</label>
    <input class="vtr-14__themeinput" type="radio" name="vtr-14-theme" id="vtr-14-theme-light">
    <label class="vtr-14__themeopt" for="vtr-14-theme-light">Light</label>
    <input class="vtr-14__themeinput" type="radio" name="vtr-14-theme" id="vtr-14-theme-dark">
    <label class="vtr-14__themeopt" for="vtr-14-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-14__stage">
    <div class="vtr-14__card">
      <p class="vtr-14__kicker">Vale Billing</p>
      <h2 class="vtr-14__heading" id="vtr-14-heading">A native dialog, in the top layer</h2>
      <p class="vtr-14__sub">Both the dialog and the transition pseudo-elements render in the top layer. One mechanism per state change.</p>
      <dl class="vtr-14__meta">
        <div><dt>Invoice</dt><dd>VL-2049</dd></div>
        <div><dt>Amount</dt><dd>1,840.00</dd></div>
        <div><dt>Due</dt><dd>Sep 1</dd></div>
      </dl>
      <button class="vtr-14__trigger" type="button" id="vtr-14-open">Cancel this invoice</button>
    </div>

    <dialog class="vtr-14__dialog" id="vtr-14-dialog" aria-labelledby="vtr-14-dtitle" hidden>
      <h3 class="vtr-14__dtitle" id="vtr-14-dtitle">Cancel invoice VL-2049</h3>
      <p class="vtr-14__dbody">The customer keeps access until the end of the current period. A credit note is issued automatically and emailed to Priya Sharma.</p>
      <div class="vtr-14__actions">
        <button class="vtr-14__btn" type="button" id="vtr-14-keep">Keep invoice</button>
        <button class="vtr-14__btn vtr-14__btn--go" type="button" id="vtr-14-confirm">Cancel invoice</button>
      </div>
    </dialog>
  </div>
</section>
```
## CSS
```css
.vtr-14 {
  --bg: #f8f5f0;
  --surface: rgba(255, 255, 255, 0.82);
  --line: #e3dbd0;
  --ink: #1d1712;
  --muted: #6c6055;
  --accent: #be123c;
  --accent-soft: #fce7ec;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  color-scheme: light dark;
}

.vtr-14 *,
.vtr-14 *::before,
.vtr-14 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-14 {
    --bg: oklch(97% 0.012 80);
    --line: oklch(88% 0.02 78);
    --ink: oklch(21% 0.015 60);
    --muted: oklch(50% 0.02 62);
    --accent: oklch(53% 0.2 15);
    --accent-soft: oklch(94% 0.035 15);
  }
}

@media (prefers-color-scheme: dark) {
  .vtr-14 {
    --bg: #14110e;
    --surface: rgba(30, 25, 21, 0.86);
    --line: #322a23;
    --ink: #f4ede4;
    --muted: #a89887;
    --accent: #fb7185;
    --accent-soft: #3a1c22;
  }
}

.vtr-14[data-theme="light"] {
  --bg: #f8f5f0;
  --surface: rgba(255, 255, 255, 0.82);
  --line: #e3dbd0;
  --ink: #1d1712;
  --muted: #6c6055;
  --accent: #be123c;
  --accent-soft: #fce7ec;
}

.vtr-14[data-theme="dark"] {
  --bg: #14110e;
  --surface: rgba(30, 25, 21, 0.86);
  --line: #322a23;
  --ink: #f4ede4;
  --muted: #a89887;
  --accent: #fb7185;
  --accent-soft: #3a1c22;
}

.vtr-14__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem, 4vw, 3rem);
}

.vtr-14__card {
  width: 100%;
  max-width: 30rem;
  padding: clamp(1.25rem, 4vw, 2rem);
  border: 1px solid var(--line);
  border-radius: 0.75rem;
  background: var(--surface);
  -webkit-backdrop-filter: blur(14px);
  backdrop-filter: blur(14px);
  display: grid;
  gap: 0.9rem;
  min-inline-size: 0;
}

.vtr-14__kicker {
  margin: 0;
  font-size: 0.68rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-14__heading {
  margin: 0;
  font-size: clamp(1.25rem, 4vw, 1.6rem);
  font-weight: 650;
  letter-spacing: -0.02em;
}

.vtr-14__sub {
  margin: 0;
  font-size: 0.86rem;
  line-height: 1.6;
  color: var(--muted);
}

.vtr-14__meta {
  margin: 0;
  display: grid;
  gap: 0.45rem;
}

.vtr-14__meta div {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  padding-bottom: 0.4rem;
  border-bottom: 1px solid var(--line);
  font-size: 0.82rem;
  min-inline-size: 0;
}

.vtr-14__meta dt {
  color: var(--muted);
}

.vtr-14__meta dd {
  margin: 0;
  font-variant-numeric: tabular-nums;
}

.vtr-14__trigger {
  justify-self: start;
  min-height: 44px;
  padding: 0 1.1rem;
  border: 1px solid var(--accent);
  border-radius: 0.5rem;
  background: var(--accent-soft);
  color: var(--accent);
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  view-transition-name: vtr-14-trigger;
}

.vtr-14__trigger:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.vtr-14__dialog {
  width: min(26rem, calc(100vw - 2rem));
  padding: 1.25rem;
  border: 1px solid var(--line);
  border-radius: 0.75rem;
  background: var(--bg);
  color: var(--ink);
  view-transition-name: vtr-14-dialog;
}

.vtr-14__dialog[hidden] {
  display: none;
}

.vtr-14__dialog::backdrop {
  background: rgba(12, 10, 8, 0.55);
}

.vtr-14__dtitle {
  margin: 0 0 0.5rem;
  font-size: 1.1rem;
  font-weight: 650;
  letter-spacing: -0.015em;
}

.vtr-14__dbody {
  margin: 0 0 1.1rem;
  font-size: 0.85rem;
  line-height: 1.6;
  color: var(--muted);
}

.vtr-14__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  justify-content: flex-end;
}

.vtr-14__btn {
  min-height: 44px;
  padding: 0 1rem;
  border: 1px solid var(--line);
  border-radius: 0.5rem;
  background: transparent;
  color: var(--ink);
  font-size: 0.83rem;
  font-weight: 600;
  cursor: pointer;
}

.vtr-14__btn--go {
  border-color: var(--accent);
  background: var(--accent);
  color: #ffffff;
}

.vtr-14__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@keyframes vtr-14-in {
  from {
    opacity: 0;
    transform: scale(0.94);
  }
}

@keyframes vtr-14-out {
  to {
    opacity: 0;
    transform: scale(0.96);
  }
}

::view-transition-new(vtr-14-dialog) {
  animation: vtr-14-in 280ms cubic-bezier(0.32, 0.72, 0, 1) both;
}

::view-transition-old(vtr-14-dialog) {
  animation: vtr-14-out 200ms ease-in both;
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-new(vtr-14-dialog),
    ::view-transition-old(vtr-14-dialog) {
    animation-duration: 1ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-14 {
  position: relative;
}

.vtr-14__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 9;
  display: flex;
  align-items: center;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 8%, transparent);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  font-family: system-ui, sans-serif;
}

.vtr-14__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-14__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-14__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.6875rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: inherit;
  opacity: 0.55;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}

.vtr-14__themeopt:hover {
  opacity: 0.85;
}

.vtr-14__themeinput:checked + .vtr-14__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-14__themeinput:focus-visible + .vtr-14__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-14:has(#vtr-14-theme-light:checked) {
  --bg: #f8f5f0;
  --surface: rgba(255, 255, 255, 0.82);
  --line: #e3dbd0;
  --ink: #1d1712;
  --muted: #6c6055;
  --accent: #be123c;
  --accent-soft: #fce7ec;
}

.vtr-14:has(#vtr-14-theme-dark:checked) {
  --bg: #14110e;
  --surface: rgba(30, 25, 21, 0.86);
  --line: #322a23;
  --ink: #f4ede4;
  --muted: #a89887;
  --accent: #fb7185;
  --accent-soft: #3a1c22;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.vtr-14');
  if (!root || root.dataset.vtr14) return;
  root.dataset.vtr14 = 'on';
  const dlg = root.querySelector('#vtr-14-dialog');
  const opener = root.querySelector('#vtr-14-open');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let busy = false;
  const run = async (mutate) => {
    if (busy) return;
    if (!document.startViewTransition || reduce.matches) { mutate(); return; }
    busy = true;
    try { await document.startViewTransition(mutate).finished; } finally { busy = false; }
  };
  opener.addEventListener('click', () => run(() => { dlg.hidden = false; dlg.showModal(); }));
  const shut = () => run(() => { dlg.close(); dlg.hidden = true; }).then(() => opener.focus());
  root.querySelector('#vtr-14-keep').addEventListener('click', shut);
  root.querySelector('#vtr-14-confirm').addEventListener('click', shut);
  dlg.addEventListener('cancel', (e) => { e.preventDefault(); shut(); });
})();
```
