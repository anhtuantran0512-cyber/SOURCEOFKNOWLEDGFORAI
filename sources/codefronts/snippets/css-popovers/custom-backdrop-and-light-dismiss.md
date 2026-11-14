---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/custom-backdrop-and-light-dismiss/"
title: "Custom Backdrop and Light Dismiss"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "Every popover gets a ::backdrop box behind it, and styling it gives you a dimmed page without an overlay div, a scroll lock, or a click listener."
has_js: "false"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Custom Backdrop and Light Dismiss
Source: https://codefronts.com/snippets/css-popovers/custom-backdrop-and-light-dismiss/

Every popover gets a ::backdrop box behind it, and styling it gives you a dimmed page without an overlay div, a scroll lock, or a click listener. Light dismiss stays intact: the backdrop is decoration, not a click shield, so clicking through it still closes an auto popover. Manual popovers get the same box and none of the dismissal.
## HTML
```html
<div class="pop-05">
  <div class="pop-05__stage">
    <div class="pop-05__sheet">
      <p class="pop-05__kicker">Settings · Workspace</p>
      <h2 class="pop-05__h">Transfer ownership</h2>
      <p class="pop-05__p">Ownership moves the billing contact and the audit trail with it. The workspace keeps its integrations. Sam Rivera will be notified by email.</p>
      <div class="pop-05__acts">
        <button class="pop-05__btn" type="button" popovertarget="pop-05-auto">Review transfer</button>
        <button class="pop-05__btn pop-05__btn--ghost" type="button" popovertarget="pop-05-manual" popovertargetaction="show">Open sticky version</button>
      </div>
      <p class="pop-05__hint">The first dims the page and still closes on an outside click. The second dims it and refuses.</p>
    </div>
  </div>

  <div class="pop-05__panel" popover="auto" id="pop-05-auto" role="group" aria-labelledby="pop-05-t1">
    <p class="pop-05__ptitle" id="pop-05-t1">Review transfer</p>
    <p class="pop-05__pbody">Alex Chen becomes owner. You keep admin. Two seats change price on the next invoice.</p>
    <p class="pop-05__ptag">popover="auto" · click the dimmed page to dismiss</p>
  </div>

  <div class="pop-05__panel pop-05__panel--manual" popover="manual" id="pop-05-manual" role="group" aria-labelledby="pop-05-t2">
    <p class="pop-05__ptitle" id="pop-05-t2">Sticky version</p>
    <p class="pop-05__pbody">Same backdrop, no dismissal. Manual popovers hand the whole job to you, so this needs a real button.</p>
    <button class="pop-05__close" type="button" popovertarget="pop-05-manual" popovertargetaction="hide">Close panel</button>
  </div>
</div>
```
## CSS
```css
.pop-05 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --paper: #ece3d4;
  --sheet: #f8f2e6;
  --ink: #2e2519;
  --muted: #7a6a53;
  --rule: #d6c8b0;
  --accent: #7c4a2d;
  --dim: rgba(46, 37, 25, 0.45);
  --font-ui: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--font-ui);
  padding: 40px 18px;
}

.pop-05__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.pop-05__sheet {
  inline-size: 100%;
  max-inline-size: 32rem;
  min-inline-size: 0;
  background: var(--sheet);
  border: 1px solid var(--rule);
  border-radius: 10px;
  padding: 26px 22px 22px;
}

.pop-05__kicker {
  margin: 0 0 10px;
  font: 700 10px/1 var(--font-ui);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.pop-05__h {
  margin: 0 0 12px;
  font: 600 clamp(21px, 4.6vw, 27px)/1.2 var(--font-ui);
  letter-spacing: -0.02em;
}

.pop-05__p {
  margin: 0 0 20px;
  font-size: 14.5px;
  line-height: 1.7;
  color: var(--muted);
  text-wrap: pretty;
}

.pop-05__acts {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.pop-05__btn {
  min-height: 44px;
  padding: 0 16px;
  font: 650 13px/1 var(--font-ui);
  color: var(--sheet);
  background: var(--accent);
  border: 1px solid var(--accent);
  border-radius: 7px;
  cursor: pointer;
}

.pop-05__btn--ghost {
  color: var(--accent);
  background: transparent;
}

.pop-05__btn:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

.pop-05__hint {
  margin: 16px 0 0;
  font-size: 12px;
  line-height: 1.6;
  color: var(--muted);
}

.pop-05__panel {
  position: fixed;
  margin: auto;
  inset: 0;
  block-size: fit-content;
  inline-size: min(23rem, calc(100vw - 32px));
  max-inline-size: calc(100vw - 32px);
  padding: 20px;
  color: var(--ink);
  background: var(--sheet);
  border: 1px solid var(--rule);
  border-radius: 10px;
  box-shadow: 0 30px 60px -28px rgba(46, 37, 25, 0.55);
  opacity: 0;
  transform: scale(0.97);
  transition: opacity 180ms ease, transform 220ms cubic-bezier(0.2, 0.9, 0.25, 1), display 220ms allow-discrete, overlay 220ms allow-discrete;
}

.pop-05__panel:popover-open {
  opacity: 1;
  transform: scale(1);
}

@starting-style {
  .pop-05__panel:popover-open {
    opacity: 0;
    transform: scale(0.97);
  }
}

.pop-05__panel::backdrop {
  background: var(--dim);
  opacity: 0;
  transition: opacity 180ms ease, display 180ms allow-discrete, overlay 180ms allow-discrete;
}

.pop-05__panel:popover-open::backdrop {
  opacity: 1;
}

@starting-style {
  .pop-05__panel:popover-open::backdrop {
    opacity: 0;
  }
}

@supports (background: color-mix(in oklab, black 50%, transparent)) {
  .pop-05__panel::backdrop {
    background: color-mix(in oklab, #2e2519 48%, transparent);
  }
}

.pop-05__panel--manual {
  border-color: var(--accent);
  border-width: 2px;
}

.pop-05__ptitle {
  margin: 0 0 10px;
  font: 700 11px/1 var(--font-ui);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.pop-05__pbody {
  margin: 0 0 14px;
  font-size: 13.5px;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.pop-05__ptag {
  margin: 0;
  padding-block-start: 12px;
  border-block-start: 1px solid var(--rule);
  font-size: 11.5px;
  color: var(--muted);
}

.pop-05__close {
  min-height: 44px;
  inline-size: 100%;
  padding: 0 14px;
  font: 650 13px/1 var(--font-ui);
  color: var(--sheet);
  background: var(--ink);
  border: 0;
  border-radius: 7px;
  cursor: pointer;
}

.pop-05__close:focus-visible {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .pop-05__panel,
    .pop-05__panel::backdrop {
    transition: none;
    opacity: 1;
    transform: none;
  }

  @starting-style {
    .pop-05__panel:popover-open {
      opacity: 1;
      transform: none;
    }
  }
}

@media (prefers-color-scheme: dark) {
  .pop-05 {
    --paper: #1a1611;
    --sheet: #241f18;
    --ink: #f2eadc;
    --muted: #a89679;
    --rule: #3a3226;
    --accent: #d99a6c;
    --dim: rgba(0, 0, 0, 0.6);
  }

  .pop-05__btn {
    color: #1a1611;
  }

  .pop-05__btn--ghost {
    color: var(--accent);
  }

  .pop-05__close {
    color: #1a1611;
  }

  .pop-05__panel::backdrop {
    background: rgba(0, 0, 0, 0.62);
  }
}

[data-theme="dark"] .pop-05 {
  --paper: #1a1611;
  --sheet: #241f18;
  --ink: #f2eadc;
  --muted: #a89679;
  --rule: #3a3226;
  --accent: #d99a6c;
  --dim: rgba(0, 0, 0, 0.62);
}

[data-theme="dark"] .pop-05 .pop-05__btn,
[data-theme="dark"] .pop-05 .pop-05__close {
  color: #1a1611;
}

[data-theme="dark"] .pop-05 .pop-05__btn--ghost {
  color: var(--accent);
}
```
