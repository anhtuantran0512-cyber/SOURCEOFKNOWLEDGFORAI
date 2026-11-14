---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/chunky-toggle-and-checkbox-set/"
title: "Chunky Toggle and Checkbox Set"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "A settings panel built entirely from native inputs: three switches with thick black tracks and a hard-shadowed knob that slides, three checkboxes with heavy…"
has_js: "false"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Chunky Toggle and Checkbox Set
Source: https://codefronts.com/design-styles/css-brutalist/chunky-toggle-and-checkbox-set/

A settings panel built entirely from native inputs: three switches with thick black tracks and a hard-shadowed knob that slides, three checkboxes with heavy ticks, and two radios — every state from :checked, zero JavaScript. Each row keeps its label and a muted description, which is what makes a control set feel like a real product rather than a component demo.
## HTML
```html
<div class="brt-10">
  <input class="brt-10__sr" type="checkbox" id="brt-10-dark">
  <label class="brt-10__theme" for="brt-10-dark">
    <svg class="brt-10__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-10__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    <span class="brt-10__vh">Dark theme</span>
  </label>

  <div class="brt-10__stage">
    <section class="brt-10__panel" aria-labelledby="brt-10-h">
      <header class="brt-10__head">
        <h2 class="brt-10__h" id="brt-10-h">Workspace settings</h2>
        <p class="brt-10__sub">Changes save as you make them.</p>
      </header>

      <fieldset class="brt-10__group">
        <legend class="brt-10__legend">Notifications</legend>
        <div class="brt-10__row">
          <label class="brt-10__label" for="brt-10-deploy">Deploy alerts<span class="brt-10__desc">Push a message when a build fails on main.</span></label>
          <input class="brt-10__switch" type="checkbox" role="switch" id="brt-10-deploy" checked>
        </div>
        <div class="brt-10__row">
          <label class="brt-10__label" for="brt-10-digest">Weekly digest<span class="brt-10__desc">Monday morning summary of usage and spend.</span></label>
          <input class="brt-10__switch" type="checkbox" role="switch" id="brt-10-digest">
        </div>
        <div class="brt-10__row">
          <label class="brt-10__label" for="brt-10-beta">Beta features<span class="brt-10__desc">Requires the Studio plan.</span></label>
          <input class="brt-10__switch" type="checkbox" role="switch" id="brt-10-beta" disabled>
        </div>
      </fieldset>

      <fieldset class="brt-10__group">
        <legend class="brt-10__legend">Access</legend>
        <div class="brt-10__row">
          <label class="brt-10__label" for="brt-10-sso">Require SSO<span class="brt-10__desc">Members sign in through your identity provider.</span></label>
          <input class="brt-10__box" type="checkbox" id="brt-10-sso" checked>
        </div>
        <div class="brt-10__row">
          <label class="brt-10__label" for="brt-10-guests">Allow guest links<span class="brt-10__desc">Anyone with the link can view a single project.</span></label>
          <input class="brt-10__box" type="checkbox" id="brt-10-guests">
        </div>
        <div class="brt-10__row">
          <label class="brt-10__label" for="brt-10-audit">Export audit log<span class="brt-10__desc">Nightly CSV to your storage bucket.</span></label>
          <input class="brt-10__box" type="checkbox" id="brt-10-audit" checked>
        </div>
      </fieldset>

      <fieldset class="brt-10__group">
        <legend class="brt-10__legend">Default visibility</legend>
        <div class="brt-10__row">
          <label class="brt-10__label" for="brt-10-priv">Private<span class="brt-10__desc">Only invited members see new projects.</span></label>
          <input class="brt-10__radio" type="radio" name="brt-10-vis" id="brt-10-priv" checked>
        </div>
        <div class="brt-10__row">
          <label class="brt-10__label" for="brt-10-team">Whole team<span class="brt-10__desc">Everyone in the workspace can open new projects.</span></label>
          <input class="brt-10__radio" type="radio" name="brt-10-vis" id="brt-10-team">
        </div>
      </fieldset>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap');

.brt-10 {
  --page: #f8f5ed;
  --panel: #ffffff;
  --ink: #0b0b0f;
  --on: #0b0b0f;
  --muted: #4a4a52;
  --line: #e2ddd1;
  --lilac: #c4b5fd;
  --mint: #86efac;
  --coral: #fda4af;
  --butter: #fde68a;
  --sky: #93c5fd;
  --on-fill: #86efac;
  --edge: #000000;
  --sh: #000000;
  --bw: 3px;
  --r: 12px;
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

.brt-10 *,
.brt-10 *::before,
.brt-10 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-10 {
    --page: oklch(0.97 0.016 90);
    --panel: oklch(1 0 0);
    --ink: oklch(0.16 0.01 285);
    --line: oklch(0.9 0.014 85);
    --lilac: oklch(0.82 0.11 296);
    --mint: oklch(0.89 0.13 155);
    --coral: oklch(0.83 0.10 15);
    --butter: oklch(0.92 0.11 95);
    --sky: oklch(0.83 0.09 250);
    --on-fill: oklch(0.89 0.13 155);
  }
}

.brt-10__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.brt-10__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.brt-10__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  border-radius: 10px;
  box-shadow: 4px 4px 0 var(--sh);
  cursor: pointer;
  transition: translate .14s ease, box-shadow .14s ease;
}

.brt-10__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-10__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-10__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-10__sr:focus-visible + .brt-10__theme {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-10__sun {
  display: none;
}

.brt-10__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3rem);
}

.brt-10__panel {
  inline-size: min(40rem,100%);
  padding: clamp(1.35rem,3.4vw,2.1rem);
  background: var(--panel);
  border: var(--bw) solid var(--edge);
  border-radius: 16px;
  box-shadow: 8px 8px 0 var(--sh);
}

.brt-10__head {
  margin-block-end: 1.4rem;
  padding-inline-end: 3rem;
}

.brt-10__h {
  margin: 0;
  font-size: clamp(1.6rem,4vw,2.2rem);
  font-weight: 700;
  letter-spacing: -.03em;
}

.brt-10__sub {
  margin: .35rem 0 0;
  font-size: .92rem;
  color: var(--muted);
}

.brt-10__group {
  margin: 0 0 1.35rem;
  padding: 0;
  border: 0;
}

.brt-10__legend {
  padding: 0 0 .6rem;
  font-size: .74rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--muted);
}

.brt-10__row {
  display: flex;
  align-items: center;
  gap: 1rem;
  justify-content: space-between;
  padding: .8rem .9rem;
  margin-block-end: .55rem;
  background: var(--page);
  border: 2px solid transparent;
  border-radius: var(--r);
  transition: background .14s ease, box-shadow .14s ease, border-color .14s ease;
}

.brt-10__row:has(:checked) {
  background: var(--panel);
  border-color: var(--edge);
  box-shadow: 4px 4px 0 var(--sh);
}

.brt-10__row:has(:disabled) {
  background: repeating-linear-gradient(45deg, var(--page) 0 7px, var(--line) 7px 14px);
}

.brt-10__label {
  display: grid;
  gap: .2rem;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
  min-block-size: 2.75rem;
  align-content: center;
}

.brt-10__row:has(:disabled) .brt-10__label {
  cursor: not-allowed;
  color: var(--muted);
}

.brt-10__desc {
  font-size: .85rem;
  font-weight: 500;
  color: var(--muted);
  text-wrap: pretty;
}

.brt-10__switch {
  appearance: none;
  -webkit-appearance: none;
  position: relative;
  margin: 0;
  flex: none;
  cursor: pointer;
  inline-size: 3.6rem;
  block-size: 2.1rem;
  background: var(--panel);
  border: var(--bw) solid var(--edge);
  border-radius: 999px;
  transition: background .16s ease;
}

.brt-10__switch::after {
  content: '';
  position: absolute;
  inset-block: 2px;
  inset-inline-start: 2px;
  inline-size: 1.35rem;
  block-size: 1.35rem;
  background: var(--panel);
  border: 2px solid var(--edge);
  border-radius: 50%;
  box-shadow: 2px 2px 0 var(--sh);
  transition: translate .16s cubic-bezier(.3,.9,.3,1);
}

.brt-10__switch:checked {
  background: var(--on-fill);
}

.brt-10__switch:checked::after {
  translate: 1.5rem 0;
}

.brt-10__switch:active::after {
  box-shadow: 1px 1px 0 var(--sh);
}

.brt-10__switch:disabled {
  cursor: not-allowed;
  background: transparent;
}

.brt-10__switch:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-10__box {
  appearance: none;
  -webkit-appearance: none;
  margin: 0;
  flex: none;
  cursor: pointer;
  inline-size: 1.85rem;
  block-size: 1.85rem;
  display: grid;
  place-items: center;
  background: var(--panel);
  border: var(--bw) solid var(--edge);
  border-radius: 7px;
  box-shadow: 3px 3px 0 var(--sh);
  transition: background .14s ease, translate .12s ease, box-shadow .12s ease;
}

.brt-10__box::after {
  content: '';
  inline-size: .55rem;
  block-size: 1rem;
  border: solid var(--on);
  border-width: 0 4px 4px 0;
  rotate: 45deg;
  translate: 0 -2px;
  opacity: 0;
  transition: opacity .12s ease;
}

.brt-10__box:checked {
  background: var(--on-fill);
}

.brt-10__box:checked::after {
  opacity: 1;
}

.brt-10__box:active {
  translate: 2px 2px;
  box-shadow: 1px 1px 0 var(--sh);
}

.brt-10__box:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-10__radio {
  appearance: none;
  -webkit-appearance: none;
  margin: 0;
  flex: none;
  cursor: pointer;
  inline-size: 1.85rem;
  block-size: 1.85rem;
  display: grid;
  place-items: center;
  background: var(--panel);
  border: var(--bw) solid var(--edge);
  border-radius: 50%;
  box-shadow: 3px 3px 0 var(--sh);
  transition: background .14s ease, translate .12s ease, box-shadow .12s ease;
}

.brt-10__radio::after {
  content: '';
  inline-size: .85rem;
  block-size: .85rem;
  background: var(--ink);
  border-radius: 2px;
  scale: 0;
  transition: scale .14s cubic-bezier(.3,.9,.3,1);
}

.brt-10__radio:checked {
  background: var(--butter);
}

.brt-10__radio:checked::after {
  scale: 1;
}

.brt-10__radio:active {
  translate: 2px 2px;
  box-shadow: 1px 1px 0 var(--sh);
}

.brt-10__radio:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-10:has(#brt-10-dark:checked) {
  --page: #191722;
  --panel: #221f2b;
  --ink: #f7f5ef;
  --muted: #b5b1c2;
  --line: #3a3646;
  --edge: #f7f5ef;
  --sh: #f7f5ef;
}

.brt-10:has(#brt-10-dark:checked) .brt-10__moon {
  display: none;
}

.brt-10:has(#brt-10-dark:checked) .brt-10__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-10:not(:has(#brt-10-dark:checked)) {
    --page: #191722;
    --panel: #221f2b;
    --ink: #f7f5ef;
    --muted: #b5b1c2;
    --line: #3a3646;
    --edge: #f7f5ef;
    --sh: #f7f5ef;
  }

  .brt-10:not(:has(#brt-10-dark:checked)) .brt-10__moon {
    display: none;
  }

  .brt-10:not(:has(#brt-10-dark:checked)) .brt-10__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-10 *,
    .brt-10 *::before,
    .brt-10 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .brt-10__panel,
    .brt-10__switch,
    .brt-10__box,
    .brt-10__radio,
    .brt-10__theme {
    border-color: CanvasText;
    box-shadow: none;
  }

  .brt-10__switch:checked {
    background: Highlight;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-10__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```
