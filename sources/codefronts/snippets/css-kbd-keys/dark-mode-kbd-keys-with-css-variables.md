---
source: "codefronts"
url: "https://codefronts.com/snippets/css-kbd-keys/dark-mode-kbd-keys-with-css-variables/"
title: "Dark Mode Kbd Keys with CSS Variables"
section: "snippets"
category: "css-kbd-keys"
category_name: "CSS Kbd Keys"
description: "Theme-aware key tokens plus a working light and dark switch with zero JavaScript."
has_js: "false"
---

Here's a working CSS Kbd Key from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Kbd Keys with CSS Variables
Source: https://codefronts.com/snippets/css-kbd-keys/dark-mode-kbd-keys-with-css-variables/

Theme-aware key tokens plus a working light and dark switch with zero JavaScript. State lives in a visually hidden checkbox and has() on the demo root rewrites the custom properties, so one checked state flips every colour at once. The OS-default block carries the opposite-base rule too, without which the switch silently does nothing for half your visitors.
## HTML
```html
<div class="kbd-20">
  <div class="kbd-20__stage">
    <section class="kbd-20__panel">
      <header class="kbd-20__head">
        <h2 class="kbd-20__title">Theme-aware keys</h2>
        <div class="kbd-20__toggle">
          <input class="kbd-20__switch" type="checkbox" id="kbd-20-switch">
          <label class="kbd-20__track" for="kbd-20-switch">
            <span class="kbd-20__thumb" aria-hidden="true"></span>
            <span class="kbd-20__switchlabel">Dark mode</span>
          </label>
        </div>
      </header>
      <ul class="kbd-20__list">
        <li class="kbd-20__row">
          <span class="kbd-20__label">Command palette</span>
          <kbd class="kbd-20__combo"><kbd class="kbd-20__key">Ctrl</kbd><span class="kbd-20__sep" aria-hidden="true">+</span><kbd class="kbd-20__key">K</kbd></kbd>
        </li>
        <li class="kbd-20__row">
          <span class="kbd-20__label">Toggle theme</span>
          <kbd class="kbd-20__combo"><kbd class="kbd-20__key">Ctrl</kbd><span class="kbd-20__sep" aria-hidden="true">+</span><kbd class="kbd-20__key">Shift</kbd><span class="kbd-20__sep" aria-hidden="true">+</span><kbd class="kbd-20__key">L</kbd></kbd>
        </li>
        <li class="kbd-20__row">
          <span class="kbd-20__label">Save all</span>
          <kbd class="kbd-20__combo"><kbd class="kbd-20__key">Ctrl</kbd><span class="kbd-20__sep" aria-hidden="true">+</span><kbd class="kbd-20__key">Alt</kbd><span class="kbd-20__sep" aria-hidden="true">+</span><kbd class="kbd-20__key">S</kbd></kbd>
        </li>
        <li class="kbd-20__row">
          <span class="kbd-20__label">Close panel</span>
          <kbd class="kbd-20__combo"><kbd class="kbd-20__key">Esc</kbd></kbd>
        </li>
      </ul>
      <dl class="kbd-20__tokens">
        <div class="kbd-20__trow"><dt class="kbd-20__tk">--cap</dt><dd class="kbd-20__tv">cap face</dd></div>
        <div class="kbd-20__trow"><dt class="kbd-20__tk">--cap-ink</dt><dd class="kbd-20__tv">label colour</dd></div>
        <div class="kbd-20__trow"><dt class="kbd-20__tk">--rule</dt><dd class="kbd-20__tv">borders and dividers</dd></div>
        <div class="kbd-20__trow"><dt class="kbd-20__tk">--accent</dt><dd class="kbd-20__tv">switch and focus ring</dd></div>
      </dl>
    </section>
  </div>
</div>
```
## CSS
```css
.kbd-20 {
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  --page: #eef0f3;
  --panel: #ffffff;
  --ink: #1b2129;
  --muted: #6b7581;
  --rule: #dce1e7;
  --cap: #f3f5f8;
  --cap-border: #c9d1da;
  --cap-ink: #313b47;
  --accent: #3b6ea5;
  --font-key: ui-sans-serif, system-ui, "Segoe UI", sans-serif;
  --font-token: ui-monospace, "SFMono-Regular", Menlo, monospace;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-key);
  padding: 40px 18px;
  transition: background 220ms ease, color 220ms ease;
}

.kbd-20:has(.kbd-20__switch:checked) {
  --page: #14181d;
  --panel: #1c222a;
  --ink: #e9eef4;
  --muted: #8d99a6;
  --rule: #2b333d;
  --cap: #242c36;
  --cap-border: #3b4653;
  --cap-ink: #dce6f1;
  --accent: #7fb0e8;
}

.kbd-20__stage {
  display: grid;
  place-items: center;
  min-height: calc(100vh - 80px);
}

.kbd-20__panel {
  inline-size: 100%;
  max-inline-size: 30rem;
  min-inline-size: 0;
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: 12px;
  padding: 22px 22px 18px;
  transition: background 220ms ease, border-color 220ms ease;
}

.kbd-20__head {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--rule);
  margin-bottom: 6px;
}

.kbd-20__title {
  margin: 0;
  font-size: 16px;
  font-weight: 700;
  letter-spacing: -0.01em;
  min-inline-size: 0;
}

.kbd-20__toggle {
  position: relative;
  min-inline-size: 0;
}

.kbd-20__switch {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.kbd-20__track {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  min-block-size: 44px;
  padding: 0 4px;
  cursor: pointer;
  user-select: none;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.kbd-20__thumb {
  position: relative;
  inline-size: 42px;
  block-size: 24px;
  flex: none;
  border-radius: 999px;
  background: var(--rule);
  border: 1px solid var(--cap-border);
}
/* The off-state fill and the edge are derived from the ink token, not from the
   divider tokens: a control boundary is measured against the panel it sits on,
   and the knob has to stay distinguishable from the fill behind it. */

@supports (background: color-mix(in oklab, currentColor 50%, transparent)) {
  .kbd-20__thumb {
    background: color-mix(in oklab, var(--ink) 52%, transparent);
    border-color: color-mix(in oklab, var(--ink) 60%, transparent);
  }
}

.kbd-20__thumb::after {
  content: "";
  position: absolute;
  inset-block-start: 2px;
  inset-inline-start: 2px;
  inline-size: 18px;
  block-size: 18px;
  border-radius: 50%;
  background: var(--panel);
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
  transition: transform 200ms cubic-bezier(0.3, 0.8, 0.3, 1);
}

.kbd-20:has(.kbd-20__switch:checked) .kbd-20__thumb {
  background: var(--accent);
}

.kbd-20:has(.kbd-20__switch:checked) .kbd-20__thumb::after {
  transform: translateX(18px);
}

.kbd-20__switch:focus-visible + .kbd-20__track {
  outline: 3px solid var(--accent);
  outline-offset: 2px;
  border-radius: 8px;
}

.kbd-20__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 1px;
}

.kbd-20__row {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding: 11px 0;
  border-bottom: 1px solid var(--rule);
}

.kbd-20__row:last-child {
  border-bottom: 0;
}

.kbd-20__label {
  font-size: 13.5px;
  min-inline-size: 0;
  flex: 1 1 9rem;
}

.kbd-20__combo {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  flex-wrap: nowrap;
  font-family: inherit;
  min-inline-size: 0;
}

.kbd-20__key {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-inline-size: 28px;
  min-block-size: 26px;
  padding: 0 8px;
  box-sizing: border-box;
  font-family: inherit;
  font-size: 12px;
  font-weight: 600;
  line-height: 1;
  color: var(--cap-ink);
  background: var(--cap);
  border: 1px solid var(--cap-border);
  border-radius: 6px;
  white-space: nowrap;
  transition: background 200ms ease, border-color 200ms ease, color 200ms ease;
}

.kbd-20__sep {
  font-size: 11px;
  color: var(--muted);
  user-select: none;
}

.kbd-20__tokens {
  margin: 16px 0 0;
  padding-top: 14px;
  border-top: 1px solid var(--rule);
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(12rem, 1fr));
  gap: 8px 20px;
}

.kbd-20__trow {
  display: flex;
  align-items: baseline;
  gap: 10px;
  min-inline-size: 0;
}

.kbd-20__tk {
  margin: 0;
  font-family: var(--font-token);
  font-size: 11px;
  color: var(--cap-ink);
  background: var(--cap);
  padding: 2px 5px;
  border-radius: 3px;
  flex: none;
}

.kbd-20__tv {
  margin: 0;
  font-size: 11.5px;
  color: var(--muted);
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .kbd-20,
    .kbd-20__panel,
    .kbd-20__key,
    .kbd-20__thumb,
    .kbd-20__thumb::after {
    transition: none;
  }
}

@media (prefers-color-scheme: dark) {
  .kbd-20:not(:has(.kbd-20__switch:checked)) {
    --page: #14181d;
    --panel: #1c222a;
    --ink: #e9eef4;
    --muted: #8d99a6;
    --rule: #2b333d;
    --cap: #242c36;
    --cap-border: #3b4653;
    --cap-ink: #dce6f1;
    --accent: #7fb0e8;
  }

  .kbd-20:has(.kbd-20__switch:checked) {
    --page: #eef0f3;
    --panel: #ffffff;
    --ink: #1b2129;
    --muted: #6b7581;
    --rule: #dce1e7;
    --cap: #f3f5f8;
    --cap-border: #c9d1da;
    --cap-ink: #313b47;
    --accent: #3b6ea5;
  }
}

.kbd-20[data-theme="dark"],
[data-theme="dark"] .kbd-20 {
  --page: #14181d;
  --panel: #1c222a;
  --ink: #e9eef4;
  --muted: #8d99a6;
  --rule: #2b333d;
  --cap: #242c36;
  --cap-border: #3b4653;
  --cap-ink: #dce6f1;
  --accent: #7fb0e8;
}
```
