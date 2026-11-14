---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/accessible-tooltip-with-aria-roles/"
title: "Accessible Tooltip with ARIA Roles"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "A ledger of what the API gives you and what it does not."
has_js: "false"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible Tooltip with ARIA Roles
Source: https://codefronts.com/snippets/css-popovers/accessible-tooltip-with-aria-roles/

A ledger of what the API gives you and what it does not. It gives the top layer, light dismiss, Escape and focus returning to the trigger. It does not give a role, an accessible name or a described-by relationship — and role=tooltip on a click-triggered panel is actively wrong, because a tooltip is a hover and focus hint, not something you open.
## HTML
```html
<div class="pop-20">
  <div class="pop-20__stage">
    <div class="pop-20__paper">
      <p class="pop-20__kicker">Accessibility ledger</p>
      <h2 class="pop-20__h">What the API does, and does not, hand you</h2>
      <div class="pop-20__cols">
        <ul class="pop-20__gives">
          <li class="pop-20__li">Top layer</li>
          <li class="pop-20__li">Light dismiss</li>
          <li class="pop-20__li">Escape to close</li>
          <li class="pop-20__li">Focus back to the trigger</li>
        </ul>
        <ul class="pop-20__lacks">
          <li class="pop-20__li">A role</li>
          <li class="pop-20__li">An accessible name</li>
          <li class="pop-20__li">A described-by relationship</li>
          <li class="pop-20__li">Any keyboard model inside</li>
        </ul>
      </div>
      <div class="pop-20__demo">
        <p class="pop-20__row">
          Retention window
          <button class="pop-20__info" type="button" popovertarget="pop-20-hint" aria-describedby="pop-20-hint" aria-label="What the retention window means">
            <svg viewBox="0 0 20 20" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="10" cy="10" r="7.2"/><path d="M10 9v5M10 6.3v.8"/></svg>
          </button>
        </p>
        <button class="pop-20__menubtn" type="button" popovertarget="pop-20-menu">Row actions</button>
      </div>
      <p class="pop-20__foot">The hint is described-by. The menu is role=menu. Neither role came for free.</p>
    </div>
  </div>

  <div class="pop-20__hint" popover="auto" id="pop-20-hint">Deleted records stay recoverable for 30 days, then are purged nightly.</div>

  <div class="pop-20__menu" popover="auto" id="pop-20-menu" role="menu" aria-label="Row actions">
    <button class="pop-20__item" type="button" role="menuitem">Extend retention</button>
    <button class="pop-20__item" type="button" role="menuitem">Export audit trail</button>
    <button class="pop-20__item" type="button" role="menuitem">Purge now</button>
  </div>
</div>
```
## CSS
```css
.pop-20 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --sepia: #efe7d9;
  --paper: #fbf6ec;
  --ink: #302722;
  --muted: #786a5c;
  --rule: #ddd0bb;
  --yes: #4a6b3f;
  --no: #92462f;
  --font-ui: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--sepia);
  color: var(--ink);
  font-family: var(--font-ui);
  padding: 44px 20px;
}

.pop-20__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  min-height: calc(100vh - 88px);
}

.pop-20__paper {
  inline-size: 100%;
  max-inline-size: 32rem;
  min-inline-size: 0;
  background: var(--paper);
  border: 1px solid var(--rule);
  border-radius: 999px 999px 20px 20px;
  padding: 30px 26px 26px;
}

.pop-20__kicker {
  margin: 0 0 10px;
  font: 700 10px/1 var(--font-ui);
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--muted);
  text-align: center;
}

.pop-20__h {
  margin: 0 0 24px;
  font: 600 clamp(20px, 4.6vw, 26px)/1.25 var(--font-ui);
  letter-spacing: -0.02em;
  text-align: center;
  text-wrap: balance;
}

.pop-20__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 12rem), 1fr));
  gap: 16px;
  margin-bottom: 24px;
}

.pop-20__gives,
.pop-20__lacks {
  margin: 0;
  padding: 14px 16px;
  list-style: none;
  display: grid;
  gap: 8px;
  border-radius: 16px;
}

.pop-20__gives {
  background: color-mix(in oklab, var(--yes) 10%, var(--paper));
}

.pop-20__lacks {
  background: color-mix(in oklab, var(--no) 9%, var(--paper));
}

.pop-20__li {
  position: relative;
  padding-inline-start: 18px;
  font-size: 13px;
  line-height: 1.5;
  min-inline-size: 0;
}

.pop-20__gives .pop-20__li::before {
  content: "";
  position: absolute;
  inset-inline-start: 0;
  inset-block-start: 5px;
  inline-size: 9px;
  block-size: 5px;
  border-inline-start: 2px solid var(--yes);
  border-block-end: 2px solid var(--yes);
  transform: rotate(-45deg);
}

.pop-20__lacks .pop-20__li::before {
  content: "";
  position: absolute;
  inset-inline-start: 1px;
  inset-block-start: 9px;
  inline-size: 9px;
  block-size: 2px;
  background: var(--no);
}

.pop-20__demo {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  align-items: center;
  justify-content: space-between;
  padding-block-start: 18px;
  border-block-start: 1px solid var(--rule);
}

.pop-20__row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0;
  font-size: 14px;
  font-weight: 600;
  min-inline-size: 0;
}

.pop-20__info {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 44px;
  min-height: 44px;
  color: var(--muted);
  background: transparent;
  border: 1px solid var(--rule);
  border-radius: 999px;
  cursor: pointer;
  anchor-name: --pop-20-hintanchor;
}

.pop-20__info:hover {
  color: var(--ink);
  background: var(--sepia);
}

.pop-20__info:focus-visible {
  outline: 3px solid var(--yes);
  outline-offset: 2px;
}

.pop-20__menubtn {
  min-height: 44px;
  padding: 0 16px;
  font: 650 12.5px/1 var(--font-ui);
  color: var(--paper);
  background: var(--ink);
  border: 0;
  border-radius: 999px;
  cursor: pointer;
  anchor-name: --pop-20-menuanchor;
}

.pop-20__menubtn:focus-visible {
  outline: 3px solid var(--yes);
  outline-offset: 2px;
}

.pop-20__foot {
  margin: 18px 0 0;
  font-size: 12px;
  line-height: 1.6;
  color: var(--muted);
  text-align: center;
}

.pop-20__hint,
.pop-20__menu {
  position: fixed;
  margin: 0;
  max-inline-size: calc(100vw - 32px);
  color: var(--ink);
  background: var(--paper);
  border: 1px solid var(--rule);
  box-shadow: 0 18px 38px -24px rgba(48, 39, 34, 0.5);
}

.pop-20__hint {
  inline-size: min(16rem, calc(100vw - 32px));
  padding: 11px 16px;
  font-size: 12.5px;
  line-height: 1.55;
  border-radius: 999px;
  text-wrap: pretty;
}

.pop-20__menu {
  inline-size: min(14rem, calc(100vw - 32px));
  padding: 6px;
  border-radius: 22px;
  display: grid;
  gap: 2px;
}

@supports (anchor-name: --a) {
  .pop-20__hint {
    position-anchor: --pop-20-hintanchor;
    position-area: block-start center;
    justify-self: anchor-center;
    inset: auto;
    margin-block-end: 9px;
    position-try-fallbacks: flip-block;
  }

  .pop-20__menu {
    position-anchor: --pop-20-menuanchor;
    position-area: block-start span-inline-start;
    inset: auto;
    margin-block-end: 9px;
    position-try-fallbacks: flip-block, flip-inline;
  }
}

.pop-20__item {
  inline-size: 100%;
  min-height: 44px;
  padding: 0 14px;
  font: 500 13px/1.3 var(--font-ui);
  text-align: start;
  color: var(--ink);
  background: transparent;
  border: 0;
  border-radius: 999px;
  cursor: pointer;
  min-inline-size: 0;
}

.pop-20__item:hover {
  background: var(--sepia);
}

.pop-20__item:focus-visible {
  outline: 3px solid var(--yes);
  outline-offset: -3px;
}

@media (prefers-color-scheme: dark) {
  .pop-20 {
    --sepia: #191411;
    --paper: #231d18;
    --ink: #f2eae0;
    --muted: #a3927f;
    --rule: #382f26;
    --yes: #8fbb7f;
    --no: #e2907a;
  }

  .pop-20__menubtn {
    color: #191411;
  }
}

[data-theme="dark"] .pop-20 {
  --sepia: #191411;
  --paper: #231d18;
  --ink: #f2eae0;
  --muted: #a3927f;
  --rule: #382f26;
  --yes: #8fbb7f;
  --no: #e2907a;
}

[data-theme="dark"] .pop-20 .pop-20__menubtn {
  color: #191411;
}
```
