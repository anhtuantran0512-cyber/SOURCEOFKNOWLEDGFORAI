---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/playful-button-set/"
title: "Playful Button Set"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "The demo that teaches the mechanic the whole collection is built on: ten button variants — primary, pastel, outline, pill, icon-only, split, disabled,…"
has_js: "true"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Playful Button Set
Source: https://codefronts.com/design-styles/css-brutalist/playful-button-set/

The demo that teaches the mechanic the whole collection is built on: ten button variants — primary, pastel, outline, pill, icon-only, split, disabled, loading, toggle and destructive — all sharing one press recipe of translate: 2px 2px with the shadow halving. Every state is real (:active, :disabled, aria-busy, aria-pressed) so you can copy any row straight into a design system.
## HTML
```html
<div class="brt-06">
  <button class="brt-06__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="brt-06__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-06__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
  </button>

  <div class="brt-06__stage">
    <section class="brt-06__panel" aria-labelledby="brt-06-h">
      <header class="brt-06__head">
        <h2 class="brt-06__h" id="brt-06-h">Buttons</h2>
        <p class="brt-06__sub">Press any of them — the block moves toward its shadow and the shadow halves.</p>
      </header>

      <div class="brt-06__group" role="group" aria-label="Primary actions">
        <button class="brt-06__btn brt-06__btn--dark" type="button"><span class="brt-06__spin" aria-hidden="true"></span>Publish page</button>
        <button class="brt-06__btn brt-06__btn--mint" type="button">Save draft</button>
        <button class="brt-06__btn brt-06__btn--lilac" type="button">Duplicate</button>
        <button class="brt-06__btn brt-06__btn--ghost" type="button">Preview</button>
      </div>

      <div class="brt-06__group" role="group" aria-label="Shapes and sizes">
        <button class="brt-06__btn brt-06__btn--pill brt-06__btn--butter" type="button">Pill button</button>
        <button class="brt-06__btn brt-06__btn--sm brt-06__btn--sky" type="button">Small</button>
        <button class="brt-06__btn brt-06__btn--icon" type="button" aria-label="Add block">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="3" stroke-linecap="square"/></svg>
        </button>
        <div class="brt-06__split">
          <button class="brt-06__btn brt-06__btn--dark brt-06__btn--splitmain" type="button">Export</button>
          <button class="brt-06__btn brt-06__btn--dark brt-06__btn--splitend" type="button" aria-label="Export options">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 9.5l6 6 6-6" stroke="currentColor" stroke-width="3" stroke-linecap="square"/></svg>
          </button>
        </div>
      </div>

      <div class="brt-06__group" role="group" aria-label="States">
        <button class="brt-06__btn brt-06__btn--dark" id="brt-06-load" type="button"><span class="brt-06__spin" aria-hidden="true"></span><span class="brt-06__label">Run build</span></button>
        <button class="brt-06__btn brt-06__btn--toggle" id="brt-06-toggle" type="button" aria-pressed="false">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5l2.4 4.9 5.4.8-3.9 3.8.9 5.4-4.8-2.6-4.8 2.6.9-5.4L4.2 10.2l5.4-.8z" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
          Favourite
        </button>
        <button class="brt-06__btn brt-06__btn--coral" type="button">Delete page</button>
        <button class="brt-06__btn" type="button" disabled>Merge blocked</button>
      </div>

      <p class="brt-06__status" id="brt-06-status" role="status" aria-live="polite"></p>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap');

@property --brt-06-off {
  syntax: '<length>';
  inherits: true;
  initial-value: 4px;
}

.brt-06 {
  --page: #f9f6ef;
  --panel: #ffffff;
  --ink: #0b0b0f;
  --on: #0b0b0f;
  --muted: #4a4a52;
  --line: #e3ded2;
  --lilac: #c4b5fd;
  --mint: #86efac;
  --coral: #fda4af;
  --butter: #fde68a;
  --sky: #93c5fd;
  --edge: #000000;
  --sh: #000000;
  --bw: 3px;
  --r: 11px;
  --brt-06-off: 4px;
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

.brt-06 *,
.brt-06 *::before,
.brt-06 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-06 {
    --page: oklch(0.972 0.014 88);
    --panel: oklch(1 0 0);
    --ink: oklch(0.16 0.01 285);
    --line: oklch(0.9 0.014 85);
    --lilac: oklch(0.82 0.11 296);
    --mint: oklch(0.89 0.13 155);
    --coral: oklch(0.83 0.10 15);
    --butter: oklch(0.92 0.11 95);
    --sky: oklch(0.83 0.09 250);
  }
}

.brt-06__theme {
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
  transition: translate .13s ease, box-shadow .13s ease;
}

.brt-06__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-06__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-06__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-06__theme:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-06__sun {
  display: none;
}

.brt-06__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3rem);
}

.brt-06__panel {
  inline-size: min(56rem,100%);
  padding: clamp(1.35rem,3.4vw,2.25rem);
  background: var(--panel);
  border: var(--bw) solid var(--edge);
  border-radius: 16px;
  box-shadow: 8px 8px 0 var(--sh);
}

.brt-06__head {
  margin-block-end: 1.5rem;
  padding-inline-end: 3rem;
}

.brt-06__h {
  margin: 0;
  font-size: clamp(1.7rem,4.4vw,2.4rem);
  font-weight: 700;
  letter-spacing: -.03em;
}

.brt-06__sub {
  margin: .4rem 0 0;
  font-size: .95rem;
  color: var(--muted);
  text-wrap: pretty;
}

.brt-06__group {
  display: flex;
  flex-wrap: wrap;
  gap: .85rem;
  padding-block: 1.1rem;
  border-block-start: 2px dashed var(--line);
}

.brt-06__group:first-of-type {
  border-block-start: 0;
  padding-block-start: 0;
}

.brt-06__btn {
  --brt-06-off: 4px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: .5rem;
  min-block-size: 2.75rem;
  min-inline-size: 2.75rem;
  padding: .65rem 1.05rem;
  font: inherit;
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: .005em;
  cursor: pointer;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  border-radius: var(--r);
  box-shadow: var(--brt-06-off) var(--brt-06-off) 0 var(--sh);
  transition: translate .13s ease, box-shadow .13s ease, --brt-06-off .13s ease, background .13s ease;
}

.brt-06__btn:hover:not(:disabled) {
  --brt-06-off: 6px;
  translate: -1px -1px;
}

.brt-06__btn:active:not(:disabled) {
  --brt-06-off: 2px;
  translate: 2px 2px;
}

.brt-06__btn:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-06__btn svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  flex: none;
}

.brt-06__btn--dark {
  background: var(--ink);
  color: var(--page);
}

.brt-06__btn--mint {
  background: var(--mint);
  color: var(--on);
}

.brt-06__btn--lilac {
  background: var(--lilac);
  color: var(--on);
}

.brt-06__btn--butter {
  background: var(--butter);
  color: var(--on);
}

.brt-06__btn--sky {
  background: var(--sky);
  color: var(--on);
}

.brt-06__btn--coral {
  background: var(--coral);
  color: var(--on);
}

.brt-06__btn--ghost {
  background: transparent;
  box-shadow: none;
  border-style: dashed;
}

.brt-06__btn--ghost:hover:not(:disabled) {
  background: var(--page);
  border-style: solid;
  box-shadow: var(--brt-06-off) var(--brt-06-off) 0 var(--sh);
}

.brt-06__btn--pill {
  border-radius: 999px;
  padding-inline: 1.4rem;
}

.brt-06__btn--sm {
  min-block-size: 2.75rem;
  padding: .45rem .8rem;
  font-size: .88rem;
  border-width: 2px;
}

.brt-06__btn--icon {
  padding: 0;
  inline-size: 2.75rem;
  block-size: 2.75rem;
}

.brt-06__btn:disabled {
  cursor: not-allowed;
  color: var(--muted);
  --brt-06-off: 2px;
  translate: 2px 2px;
  background: repeating-linear-gradient(45deg, var(--page) 0 6px, var(--line) 6px 12px);
}

.brt-06__split {
  display: flex;
  gap: 0;
}

.brt-06__btn--splitmain {
  border-start-end-radius: 0;
  border-end-end-radius: 0;
  border-inline-end-width: 0;
}

.brt-06__btn--splitend {
  border-start-start-radius: 0;
  border-end-start-radius: 0;
  padding-inline: .7rem;
  border-inline-start: var(--bw) solid var(--page);
}

.brt-06__btn--toggle[aria-pressed="true"] {
  background: var(--ink);
  color: var(--page);
}

.brt-06__btn--toggle[aria-pressed="true"] svg {
  fill: var(--butter);
  stroke: var(--butter);
}

.brt-06__spin {
  inline-size: 0;
  block-size: 1rem;
  flex: none;
  transition: inline-size .13s ease;
}

.brt-06__btn[aria-busy="true"] {
  cursor: progress;
}

.brt-06__btn[aria-busy="true"] .brt-06__spin {
  inline-size: 1rem;
  border: 3px solid currentColor;
  border-block-start-color: transparent;
  border-radius: 50%;
  animation: brt-06-spin .7s linear infinite;
}

@keyframes brt-06-spin {
  to {
    rotate: 360deg;
  }
}

.brt-06__status {
  margin: 1.25rem 0 0;
  min-block-size: 1.25rem;
  font-size: .9rem;
  font-weight: 700;
}

.brt-06__status:not(:empty) {
  display: inline-block;
  padding: .4rem .65rem;
  background: var(--mint);
  color: var(--on);
  border: 2px solid var(--edge);
  border-radius: 8px;
}

.brt-06[data-theme="dark"] {
  --page: #131218;
  --panel: #201e28;
  --ink: #f7f5ef;
  --muted: #b5b1c2;
  --line: #3a3646;
  --edge: #f7f5ef;
  --sh: #f7f5ef;
}

.brt-06[data-theme="dark"] .brt-06__moon {
  display: none;
}

.brt-06[data-theme="dark"] .brt-06__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-06:not([data-theme="light"]) {
    --page: #131218;
    --panel: #201e28;
    --ink: #f7f5ef;
    --muted: #b5b1c2;
    --line: #3a3646;
    --edge: #f7f5ef;
    --sh: #f7f5ef;
  }

  .brt-06:not([data-theme="light"]) .brt-06__moon {
    display: none;
  }

  .brt-06:not([data-theme="light"]) .brt-06__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-06 *,
    .brt-06 *::before,
    .brt-06 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .brt-06__btn,
    .brt-06__panel,
    .brt-06__theme {
    border-color: CanvasText;
    box-shadow: none;
  }

  .brt-06__btn--toggle[aria-pressed="true"] {
    background: Highlight;
    color: HighlightText;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-06__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.brt-06');
  if (!root) return;
  const status = root.querySelector('#brt-06-status');
  const load = root.querySelector('#brt-06-load');
  const label = load.querySelector('.brt-06__label');
  const toggle = root.querySelector('#brt-06-toggle');

  load.addEventListener('click', () => {
    if (load.getAttribute('aria-busy') === 'true') return;
    load.setAttribute('aria-busy', 'true');
    label.textContent = 'Building';
    status.textContent = 'Build started…';
    setTimeout(() => {
      load.removeAttribute('aria-busy');
      label.textContent = 'Run build';
      status.textContent = 'Build finished in 41s.';
    }, 1600);
  });

  toggle.addEventListener('click', () => {
    const on = toggle.getAttribute('aria-pressed') !== 'true';
    toggle.setAttribute('aria-pressed', String(on));
    status.textContent = on ? 'Added to favourites.' : 'Removed from favourites.';
  });
})();

(() => {                                     /* theme toggle */
  const root = document.querySelector('.brt-06');
  const btn = root && root.querySelector('.brt-06__theme');
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
