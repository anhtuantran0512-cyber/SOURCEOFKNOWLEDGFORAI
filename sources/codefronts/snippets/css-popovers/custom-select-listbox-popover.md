---
source: "codefronts"
url: "https://codefronts.com/snippets/css-popovers/custom-select-listbox-popover/"
title: "Custom Select Listbox Popover"
section: "snippets"
category: "css-popovers"
category_name: "CSS Popovers"
description: "Popover hands you the top layer, light dismiss and Escape."
has_js: "true"
---

Here's a working CSS Popover from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Custom Select Listbox Popover
Source: https://codefronts.com/snippets/css-popovers/custom-select-listbox-popover/

Popover hands you the top layer, light dismiss and Escape. It hands you nothing about keyboard semantics, so a listbox built on it still needs roles, a selection state and arrow keys you write yourself. Under thirty lines of vanilla JS covers Up, Down, Home, End and Enter over a real role=listbox, with the panel sized and placed by anchor positioning.
## HTML
```html
<div class="pop-11">
  <div class="pop-11__stage">
    <div class="pop-11__panelui">
      <p class="pop-11__kicker">Report settings</p>
      <label class="pop-11__label" id="pop-11-label" for="pop-11-trigger">Group results by</label>
      <button class="pop-11__combo" type="button" id="pop-11-trigger" popovertarget="pop-11-list" aria-expanded="false" aria-labelledby="pop-11-label pop-11-trigger">
        <span class="pop-11__val" id="pop-11-value">Account owner</span>
        <svg viewBox="0 0 16 16" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true"><path d="M4 6.5 8 10.5 12 6.5"/></svg>
      </button>
      <p class="pop-11__hint">Arrow keys move, Home and End jump, Enter commits, Escape closes.</p>
    </div>
  </div>

  <div class="pop-11__list" popover="auto" id="pop-11-list" role="listbox" aria-labelledby="pop-11-label" tabindex="-1">
    <div class="pop-11__opt" role="option" tabindex="0" aria-selected="true">Account owner</div>
    <div class="pop-11__opt" role="option" tabindex="-1" aria-selected="false">Region</div>
    <div class="pop-11__opt" role="option" tabindex="-1" aria-selected="false">Plan tier</div>
    <div class="pop-11__opt" role="option" tabindex="-1" aria-selected="false">Signup month</div>
    <div class="pop-11__opt" role="option" tabindex="-1" aria-selected="false">Churn risk band</div>
  </div>
</div>
```
## CSS
```css
.pop-11 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  --bg: #f6f6f7;
  --surface: #ffffff;
  --ink: #17161a;
  --muted: #6c6a73;
  --rule: #dedde1;
  --sel: #5b3df5;
  --font-ui: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-ui);
  padding: 40px 18px;
}

.pop-11__stage {
  display: grid;
  place-items: center;
  max-inline-size: 100%;
  min-height: calc(100vh - 80px);
}

.pop-11__panelui {
  inline-size: 100%;
  max-inline-size: 24rem;
  min-inline-size: 0;
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 10px;
  padding: 20px 18px 18px;
  box-shadow: 0 12px 26px -20px rgba(23, 22, 26, 0.4);
}

.pop-11__kicker {
  margin: 0 0 16px;
  font: 700 10px/1 var(--font-ui);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--sel);
}

.pop-11__label {
  display: block;
  margin-bottom: 6px;
  font-size: 12px;
  font-weight: 600;
  color: var(--muted);
}

.pop-11__combo {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  inline-size: 100%;
  min-height: 44px;
  padding: 0 12px;
  font: 500 13.5px/1 var(--font-ui);
  text-align: start;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 8px;
  cursor: pointer;
  anchor-name: --pop-11-anchor;
}

.pop-11__combo:hover {
  border-color: var(--sel);
}

.pop-11__combo:focus-visible {
  outline: 3px solid var(--sel);
  outline-offset: 2px;
}

.pop-11__val {
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.pop-11__hint {
  margin: 10px 0 0;
  font-size: 12px;
  line-height: 1.6;
  color: var(--muted);
}

.pop-11__list {
  position: fixed;
  margin: 0;
  inline-size: min(22rem, calc(100vw - 32px));
  max-inline-size: calc(100vw - 32px);
  padding: 5px;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--rule);
  border-radius: 8px;
  box-shadow: 0 20px 40px -22px rgba(23, 22, 26, 0.5);
}

@supports (anchor-name: --a) {
  .pop-11__list {
    position-anchor: --pop-11-anchor;
    position-area: block-end span-inline-end;
    inset: auto;
    inline-size: anchor-size(width);
    max-inline-size: calc(100vw - 32px);
    margin-block-start: 6px;
    position-try-fallbacks: flip-block;
  }
}

.pop-11__opt {
  display: flex;
  align-items: center;
  min-height: 44px;
  padding: 0 11px;
  font-size: 13.5px;
  border-radius: 6px;
  cursor: pointer;
  min-inline-size: 0;
}

.pop-11__opt:hover {
  background: color-mix(in oklab, var(--sel) 8%, var(--surface));
}

.pop-11__opt:focus-visible {
  outline: 3px solid var(--sel);
  outline-offset: -3px;
}

.pop-11__opt[aria-selected="true"] {
  font-weight: 650;
  color: var(--sel);
  background: color-mix(in oklab, var(--sel) 10%, var(--surface));
}

.pop-11__opt[aria-selected="true"]::after {
  content: "";
  margin-inline-start: auto;
  inline-size: 14px;
  block-size: 8px;
  border-inline-start: 2px solid currentColor;
  border-block-end: 2px solid currentColor;
  transform: rotate(-45deg) translateY(-2px);
}

@media (prefers-color-scheme: dark) {
  .pop-11 {
    --bg: #121114;
    --surface: #1c1b20;
    --ink: #eeedf2;
    --muted: #9a98a3;
    --rule: #2c2b32;
    --sel: #a493ff;
  }
}

[data-theme="dark"] .pop-11 {
  --bg: #121114;
  --surface: #1c1b20;
  --ink: #eeedf2;
  --muted: #9a98a3;
  --rule: #2c2b32;
  --sel: #a493ff;
}
```

## JavaScript
```js
const list = document.getElementById('pop-11-list');
const trigger = document.getElementById('pop-11-trigger');
const value = document.getElementById('pop-11-value');
const opts = [...list.querySelectorAll('[role="option"]')];
const move = (to) => {
  const i = Math.max(0, Math.min(opts.length - 1, to));
  opts.forEach((o, n) => o.setAttribute('tabindex', n === i ? '0' : '-1'));
  opts[i].focus();
};
const commit = (o) => {
  opts.forEach((x) => x.setAttribute('aria-selected', String(x === o)));
  value.textContent = o.textContent.trim();
  list.hidePopover();
};
list.addEventListener('keydown', (e) => {
  const i = opts.indexOf(document.activeElement);
  const keys = { ArrowDown: i + 1, ArrowUp: i - 1, Home: 0, End: opts.length - 1 };
  if (e.key in keys) { e.preventDefault(); move(keys[e.key]); }
  if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); commit(opts[i]); }
});
opts.forEach((o) => o.addEventListener('click', () => commit(o)));
list.addEventListener('toggle', (e) => {
  trigger.setAttribute('aria-expanded', String(e.newState === 'open'));
  if (e.newState === 'open') move(opts.findIndex((o) => o.getAttribute('aria-selected') === 'true'));
});
```
