---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/popover-vs-dialog-showcase/"
title: "Popover vs Dialog Showcase"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "One decision rule, shown twice: use dialog with showModal when the user must deal with it, and popover when they can ignore it and carry on."
has_js: "false"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Popover vs Dialog Showcase
Source: https://codefronts.com/snippets/css-popovers/popover-vs-dialog-showcase/

One decision rule, shown twice: use dialog with showModal when the user must deal with it, and popover when they can ignore it and carry on. Modal versus non-modal is the entire distinction — focus trapping, page inertness and a click-blocking backdrop all follow from it. The dialog side stays minimal on purpose.
## HTML
```html
<div class="pop-17">
  <div class="pop-17__stage">
    <div class="pop-17__sheet">
      <p class="pop-17__kicker">Decision</p>
      <h2 class="pop-17__h">Can the user ignore it?</h2>
      <div class="pop-17__cols">
        <div class="pop-17__col">
          <p class="pop-17__yes">Yes → popover</p>
          <p class="pop-17__copy">Page stays live. Focus can leave. An outside click puts it away.</p>
          <button class="pop-17__btn" type="button" popovertarget="pop-17-pop">Show share panel</button>
        </div>
        <div class="pop-17__col">
          <p class="pop-17__no">No → dialog</p>
          <p class="pop-17__copy">Focus contained. Page inert. Backdrop blocks the click.</p>
          <button class="pop-17__btn pop-17__btn--solid" type="button" command="show-modal" commandfor="pop-17-dialog">Delete workspace</button>
        </div>
      </div>
      <table class="pop-17__table">
        <tbody>
          <tr class="pop-17__tr"><th class="pop-17__th" scope="row">Focus</th><td class="pop-17__td">free</td><td class="pop-17__td">contained</td></tr>
          <tr class="pop-17__tr"><th class="pop-17__th" scope="row">Rest of page</th><td class="pop-17__td">interactive</td><td class="pop-17__td">inert</td></tr>
          <tr class="pop-17__tr"><th class="pop-17__th" scope="row">Backdrop</th><td class="pop-17__td">dismisses</td><td class="pop-17__td">blocks</td></tr>
          <tr class="pop-17__tr"><th class="pop-17__th" scope="row">Escape</th><td class="pop-17__td">closes top one</td><td class="pop-17__td">closes, cancelable</td></tr>
        </tbody>
      </table>
    </div>
  </div>

  <div class="pop-17__pop" popover="auto" id="pop-17-pop" role="group" aria-label="Share">
    <p class="pop-17__ptitle">Share this board</p>
    <p class="pop-17__pline">Anyone with the link can comment. Keep working — I am not in your way.</p>
    <p class="pop-17__ptag">popover · non-modal</p>
  </div>

  <dialog class="pop-17__dialog" id="pop-17-dialog" aria-labelledby="pop-17-dt">
    <p class="pop-17__ptitle" id="pop-17-dt">Delete workspace</p>
    <p class="pop-17__pline">This removes 1,284 records and cannot be undone. You must answer before continuing.</p>
    <div class="pop-17__dacts">
      <button class="pop-17__btn pop-17__btn--solid" type="button" command="close" commandfor="pop-17-dialog">Cancel</button>
      <button class="pop-17__btn" type="button" command="close" commandfor="pop-17-dialog">Delete</button>
    </div>
  </dialog>
</div>
```
## CSS
```css
.pop-17 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --paper: #f6f4ee;
  --surface: #ffffff;
  --ink: #14130f;
  --muted: #6d6a5f;
  --rule: #14130f;
  --hair: #ded9cd;
  --go: #1f5f4a;
  --stop: #93321f;
  --font-display: "Iowan Old Style", Georgia, serif;
  --font-ui: ui-sans-serif, system-ui, sans-serif;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--font-ui);
  padding: 40px 18px;
}

.pop-17__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.pop-17__sheet {
  inline-size: 100%;
  max-inline-size: 36rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--hair);
  padding: 26px 22px 22px;
}

.pop-17__kicker {
  margin: 0 0 8px;
  font: 700 10px/1 var(--font-ui);
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--muted);
}

.pop-17__h {
  margin: 0 0 22px;
  font: 400 clamp(24px, 5.6vw, 34px)/1.12 var(--font-display);
  letter-spacing: -0.02em;
}

.pop-17__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 13rem), 1fr));
  gap: 18px;
  margin-bottom: 24px;
}

.pop-17__col {
  min-inline-size: 0;
  display: grid;
  gap: 8px;
  align-content: start;
  padding-block-start: 12px;
  border-block-start: 2px solid var(--rule);
}

.pop-17__yes,
.pop-17__no {
  margin: 0;
  font: 700 12px/1 var(--font-ui);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.pop-17__yes {
  color: var(--go);
}

.pop-17__no {
  color: var(--stop);
}

.pop-17__copy {
  margin: 0 0 6px;
  font-size: 13px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.pop-17__btn {
  min-height: 44px;
  padding: 0 14px;
  font: 650 12.5px/1 var(--font-ui);
  color: var(--ink);
  background: transparent;
  border: 2px solid var(--rule);
  border-radius: 0;
  cursor: pointer;
  anchor-name: --pop-17-anchor;
}

.pop-17__btn--solid {
  color: var(--surface);
  background: var(--ink);
  anchor-name: none;
}

.pop-17__btn:focus-visible {
  outline: 3px solid var(--go);
  outline-offset: 2px;
}

.pop-17__table {
  inline-size: 100%;
  border-collapse: collapse;
}

.pop-17__tr {
  border-block-start: 1px solid var(--hair);
}

.pop-17__th {
  padding: 8px 0;
  text-align: start;
  font: 600 11.5px/1.3 var(--font-ui);
  color: var(--muted);
  min-inline-size: 0;
}

.pop-17__td {
  padding: 8px 0 8px 12px;
  font-size: 12.5px;
  min-inline-size: 0;
}

.pop-17__td:first-of-type {
  color: var(--go);
}

.pop-17__td:last-of-type {
  color: var(--stop);
  text-align: end;
}

.pop-17__pop {
  position: fixed;
  margin: 0;
  inline-size: min(19rem, calc(100vw - 28px));
  max-inline-size: calc(100vw - 28px);
  padding: 16px;
  color: var(--ink);
  background: var(--surface);
  border: 2px solid var(--go);
  border-radius: 0;
  box-shadow: 6px 6px 0 color-mix(in oklab, var(--go) 22%, transparent);
}

@supports (anchor-name: --a) {
  .pop-17__pop {
    position-anchor: --pop-17-anchor;
    position-area: block-end span-inline-end;
    inset: auto;
    margin-block-start: 9px;
    position-try-fallbacks: flip-block, flip-inline;
  }
}

.pop-17__dialog {
  inline-size: min(23rem, calc(100vw - 32px));
  max-inline-size: calc(100vw - 32px);
  padding: 18px;
  color: var(--ink);
  background: var(--surface);
  border: 2px solid var(--stop);
  border-radius: 0;
}

.pop-17__dialog::backdrop {
  background: rgba(20, 19, 15, 0.55);
}

.pop-17__ptitle {
  margin: 0 0 8px;
  font: 700 11px/1 var(--font-ui);
  letter-spacing: 0.14em;
  text-transform: uppercase;
}

.pop-17__pline {
  margin: 0 0 12px;
  font-size: 13px;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.pop-17__ptag {
  margin: 0;
  padding-block-start: 10px;
  border-block-start: 1px solid var(--hair);
  font: 600 11px/1 var(--font-ui);
  color: var(--go);
}

.pop-17__dacts {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.pop-17__dacts .pop-17__btn {
  flex: 1 1 auto;
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .pop-17__pop,
    .pop-17__dialog {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .pop-17 {
    --paper: #131210;
    --surface: #1c1a16;
    --ink: #f2efe6;
    --muted: #a09a8c;
    --rule: #f2efe6;
    --hair: #2f2c25;
    --go: #6fc9a8;
    --stop: #ef8f74;
  }

  .pop-17__btn--solid {
    color: #131210;
  }

  .pop-17__dialog::backdrop {
    background: rgba(0, 0, 0, 0.62);
  }
}

[data-theme="dark"] .pop-17 {
  --paper: #131210;
  --surface: #1c1a16;
  --ink: #f2efe6;
  --muted: #a09a8c;
  --rule: #f2efe6;
  --hair: #2f2c25;
  --go: #6fc9a8;
  --stop: #ef8f74;
}

[data-theme="dark"] .pop-17 .pop-17__btn--solid {
  color: #131210;
}
```
