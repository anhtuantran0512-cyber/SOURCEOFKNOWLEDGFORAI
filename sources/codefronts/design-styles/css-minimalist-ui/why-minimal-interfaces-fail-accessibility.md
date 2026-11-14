---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/why-minimal-interfaces-fail-accessibility/"
title: "Why Minimal Interfaces Fail Accessibility"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "Four failures side by side, each with the criterion it breaks printed on it and a switch that shows the corrected version in place: low-contrast secondary…"
has_js: "true"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Why Minimal Interfaces Fail Accessibility
Source: https://codefronts.com/design-styles/css-minimalist-ui/why-minimal-interfaces-fail-accessibility/

Four failures side by side, each with the criterion it breaks printed on it and a switch that shows the corrected version in place: low-contrast secondary text, an icon-only button with no accessible name, placeholders used as labels, and a 32px target chosen because 44px looked heavy. Every one of these ships weekly in the name of clean design.
## HTML
```html
<section class="mu-13" aria-labelledby="mu-13-title">
  <h2 class="mu-13__sr" id="mu-13-title">Accessibility failures and fixes</h2>
  <div class="mu-13__theme">
    <input class="mu-13__theme-input" type="checkbox" id="mu-13-theme">
    <label class="mu-13__theme-label" for="mu-13-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-13__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-13__stage" id="mu-13-board">

    <div class="mu-13__board">
      <article class="mu-13__panel" data-mu-13-panel aria-labelledby="mu-13-p1">
        <header class="mu-13__panel-head">
          <h3 class="mu-13__panel-title" id="mu-13-p1">Low-contrast secondary text</h3>
          <p class="mu-13__crit">SC 1.4.3 &middot; Contrast (Minimum)</p>
        </header>
        <div class="mu-13__sample">
          <p class="mu-13__sample-title">Monthly recurring revenue</p>
          <p class="mu-13__secondary">Updated 6 minutes ago by Alex Chen. Includes 42 hours of overage on the Basalt retainer.</p>
        </div>
        <p class="mu-13__measure"><b class="mu-13__measure-fail">2.9:1 &mdash; fails</b><b class="mu-13__measure-ok">7.0:1 &mdash; passes</b></p>
        <button class="mu-13__switch" type="button" aria-pressed="false" data-mu-13-switch>
          <span class="mu-13__switch-label">Show the fix</span>
        </button>
      </article>

      <article class="mu-13__panel" data-mu-13-panel aria-labelledby="mu-13-p2">
        <header class="mu-13__panel-head">
          <h3 class="mu-13__panel-title" id="mu-13-p2">Icon-only button, no name</h3>
          <p class="mu-13__crit">SC 4.1.2 &middot; Name, Role, Value</p>
        </header>
        <div class="mu-13__sample">
          <div class="mu-13__toolbar">
            <span class="mu-13__fail-only">
              <button class="mu-13__icon-btn" type="button">
                <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
              </button>
              <button class="mu-13__icon-btn" type="button">
                <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 7h16M9 7V5h6v2M6 7l1 13h10l1-13" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
              </button>
            </span>
            <span class="mu-13__fix-only">
              <button class="mu-13__icon-btn" type="button" aria-label="Add line item">
                <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
                <span class="mu-13__tip">Add line item</span>
              </button>
              <button class="mu-13__icon-btn" type="button" aria-label="Delete invoice">
                <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 7h16M9 7V5h6v2M6 7l1 13h10l1-13" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
                <span class="mu-13__tip">Delete invoice</span>
              </button>
            </span>
          </div>
        </div>
        <p class="mu-13__measure"><b class="mu-13__measure-fail">No accessible name</b><b class="mu-13__measure-ok">aria-label + visible tip</b></p>
        <button class="mu-13__switch" type="button" aria-pressed="false" data-mu-13-switch>
          <span class="mu-13__switch-label">Show the fix</span>
        </button>
      </article>

      <article class="mu-13__panel" data-mu-13-panel aria-labelledby="mu-13-p3">
        <header class="mu-13__panel-head">
          <h3 class="mu-13__panel-title" id="mu-13-p3">Placeholder used as a label</h3>
          <p class="mu-13__crit">SC 3.3.2 &middot; Labels or Instructions</p>
        </header>
        <div class="mu-13__sample">
          <div class="mu-13__fail-only">
            <input class="mu-13__input" type="text" placeholder="Card number" inputmode="numeric">
            <input class="mu-13__input" type="text" placeholder="MM / YY" inputmode="numeric">
          </div>
          <div class="mu-13__fix-only mu-13__fields">
            <div class="mu-13__field">
              <label class="mu-13__label" for="mu-13-card">Card number</label>
              <input class="mu-13__input" id="mu-13-card" type="text" placeholder="4242 4242 4242 4242" inputmode="numeric">
            </div>
            <div class="mu-13__field">
              <label class="mu-13__label" for="mu-13-exp">Expiry</label>
              <input class="mu-13__input" id="mu-13-exp" type="text" placeholder="MM / YY" inputmode="numeric">
            </div>
          </div>
        </div>
        <p class="mu-13__measure"><b class="mu-13__measure-fail">Label disappears on input</b><b class="mu-13__measure-ok">Label persists, hint remains</b></p>
        <button class="mu-13__switch" type="button" aria-pressed="false" data-mu-13-switch>
          <span class="mu-13__switch-label">Show the fix</span>
        </button>
      </article>

      <article class="mu-13__panel" data-mu-13-panel aria-labelledby="mu-13-p4">
        <header class="mu-13__panel-head">
          <h3 class="mu-13__panel-title" id="mu-13-p4">Target under 44px</h3>
          <p class="mu-13__crit">SC 2.5.8 &middot; Target Size (Minimum)</p>
        </header>
        <div class="mu-13__sample">
          <div class="mu-13__target-row">
            <button class="mu-13__target" type="button">Approve</button>
            <button class="mu-13__target" type="button">Reject</button>
          </div>
        </div>
        <p class="mu-13__measure"><b class="mu-13__measure-fail">32 &times; 28px</b><b class="mu-13__measure-ok">44 &times; 44px</b></p>
        <button class="mu-13__switch" type="button" aria-pressed="false" data-mu-13-switch>
          <span class="mu-13__switch-label">Show the fix</span>
        </button>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.mu-13 {
  --mu-13-target-fail: 28px;
  --mu-13-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --mu-13-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --mu-13-bg: #ffffff;
  --mu-13-bg: oklch(100% 0 0);
  --mu-13-surface: #f7f8f9;
  --mu-13-surface: oklch(97.5% 0.003 250);
  --mu-13-ink: #15181b;
  --mu-13-ink: oklch(19.5% 0.006 250);
  --mu-13-ink-2: #4f585f;
  --mu-13-ink-2: oklch(45% 0.012 250);
  --mu-13-fail-ink: #a9b0b5;
  --mu-13-fail-ink: oklch(75% 0.006 250);
  --mu-13-line: #d3d8db;
  --mu-13-line: oklch(86% 0.005 250);
  --mu-13-bad: #a11d1d;
  --mu-13-bad: oklch(44% 0.18 25);
  --mu-13-ok: #15613a;
  --mu-13-ok: oklch(43% 0.11 155);
  --mu-13-acc: #0f4faf;
  --mu-13-acc: oklch(44% 0.17 262);
  --mu-13-ring: #0f4faf;
  --mu-13-ring: oklch(44% 0.17 262);
  --mu-13-acc-ink: #ffffff;
  --mu-13-acc-ink: oklch(100% 0 0);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-13-bg);
  color: var(--mu-13-ink);
  font-family: var(--mu-13-ui);
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

.mu-13 *,
.mu-13 *::before,
.mu-13 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .mu-13 {
    --mu-13-bg: #101315;
    --mu-13-bg: oklch(17.5% 0.006 250);
    --mu-13-surface: #191d20;
    --mu-13-surface: oklch(23% 0.007 250);
    --mu-13-ink: #eef1f3;
    --mu-13-ink: oklch(95.5% 0.004 250);
    --mu-13-ink-2: #a5aeb5;
    --mu-13-ink-2: oklch(74% 0.01 250);
    --mu-13-fail-ink: #454d53;
    --mu-13-fail-ink: oklch(40% 0.01 250);
    --mu-13-line: #333b41;
    --mu-13-line: oklch(33% 0.011 250);
    --mu-13-bad: #f08a8a;
    --mu-13-bad: oklch(74% 0.14 25);
    --mu-13-ok: #62c78f;
    --mu-13-ok: oklch(78% 0.12 155);
    --mu-13-acc: #86b3ff;
    --mu-13-acc: oklch(80% 0.12 262);
    --mu-13-ring: #86b3ff;
    --mu-13-ring: oklch(80% 0.12 262);
    --mu-13-acc-ink: #0c1526;
    --mu-13-acc-ink: oklch(18% 0.03 258);
  }
}

.mu-13[data-theme="dark"],
.mu-13:has(.mu-13__theme-input:checked) {
  --mu-13-bg: #101315;
  --mu-13-bg: oklch(17.5% 0.006 250);
  --mu-13-surface: #191d20;
  --mu-13-surface: oklch(23% 0.007 250);
  --mu-13-ink: #eef1f3;
  --mu-13-ink: oklch(95.5% 0.004 250);
  --mu-13-ink-2: #a5aeb5;
  --mu-13-ink-2: oklch(74% 0.01 250);
  --mu-13-fail-ink: #454d53;
  --mu-13-fail-ink: oklch(40% 0.01 250);
  --mu-13-line: #333b41;
  --mu-13-line: oklch(33% 0.011 250);
  --mu-13-bad: #f08a8a;
  --mu-13-bad: oklch(74% 0.14 25);
  --mu-13-ok: #62c78f;
  --mu-13-ok: oklch(78% 0.12 155);
  --mu-13-acc: #86b3ff;
  --mu-13-acc: oklch(80% 0.12 262);
  --mu-13-ring: #86b3ff;
  --mu-13-ring: oklch(80% 0.12 262);
  --mu-13-acc-ink: #0c1526;
  --mu-13-acc-ink: oklch(18% 0.03 258);
}

@media (prefers-color-scheme: light) {
  .mu-13:has(.mu-13__theme-input:checked) {
    --mu-13-bg: #101315;
    --mu-13-bg: oklch(17.5% 0.006 250);
    --mu-13-surface: #191d20;
    --mu-13-surface: oklch(23% 0.007 250);
    --mu-13-ink: #eef1f3;
    --mu-13-ink: oklch(95.5% 0.004 250);
    --mu-13-ink-2: #a5aeb5;
    --mu-13-ink-2: oklch(74% 0.01 250);
    --mu-13-fail-ink: #454d53;
    --mu-13-fail-ink: oklch(40% 0.01 250);
    --mu-13-line: #333b41;
    --mu-13-line: oklch(33% 0.011 250);
    --mu-13-bad: #f08a8a;
    --mu-13-bad: oklch(74% 0.14 25);
    --mu-13-ok: #62c78f;
    --mu-13-ok: oklch(78% 0.12 155);
    --mu-13-acc: #86b3ff;
    --mu-13-acc: oklch(80% 0.12 262);
    --mu-13-ring: #86b3ff;
    --mu-13-ring: oklch(80% 0.12 262);
    --mu-13-acc-ink: #0c1526;
    --mu-13-acc-ink: oklch(18% 0.03 258);
  }
}

@media (prefers-color-scheme: dark) {
  .mu-13:has(.mu-13__theme-input:checked) {
    --mu-13-bg: #ffffff;
    --mu-13-bg: oklch(100% 0 0);
    --mu-13-surface: #f7f8f9;
    --mu-13-surface: oklch(97.5% 0.003 250);
    --mu-13-ink: #15181b;
    --mu-13-ink: oklch(19.5% 0.006 250);
    --mu-13-ink-2: #4f585f;
    --mu-13-ink-2: oklch(45% 0.012 250);
    --mu-13-fail-ink: #a9b0b5;
    --mu-13-fail-ink: oklch(75% 0.006 250);
    --mu-13-line: #d3d8db;
    --mu-13-line: oklch(86% 0.005 250);
    --mu-13-bad: #a11d1d;
    --mu-13-bad: oklch(44% 0.18 25);
    --mu-13-ok: #15613a;
    --mu-13-ok: oklch(43% 0.11 155);
    --mu-13-acc: #0f4faf;
    --mu-13-acc: oklch(44% 0.17 262);
    --mu-13-ring: #0f4faf;
    --mu-13-ring: oklch(44% 0.17 262);
    --mu-13-acc-ink: #ffffff;
    --mu-13-acc-ink: oklch(100% 0 0);
  }
}

.mu-13__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.mu-13__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-13__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-13__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-13-line);
  border-radius: 4px;
  background: var(--mu-13-surface);
  color: var(--mu-13-ink-2);
  cursor: pointer;
}

.mu-13__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-13__theme-input:focus-visible + .mu-13__theme-label {
  outline: 2px solid var(--mu-13-ring);
  outline-offset: 2px;
}

.mu-13__stage {
  max-inline-size: 78rem;
  margin-inline: auto;
  padding: 4rem 1.25rem 5rem;
  display: grid;
  gap: 2.5rem;
  grid-template-columns: minmax(0, 1fr);
}

.mu-13__board {
  display: grid;
  gap: 1.25rem;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
}

.mu-13__panel {
  min-inline-size: 0;
  display: grid;
  gap: 0.875rem;
  align-content: start;
  padding: 1.25rem;
  background: var(--mu-13-surface);
  border: 1px solid var(--mu-13-line);
  border-radius: 6px;
}

.mu-13__panel-head {
  display: grid;
  gap: 2px;
  min-inline-size: 0;
}

.mu-13__panel-title {
  margin: 0;
  font-size: 0.9375rem;
  font-weight: 600;
  letter-spacing: -0.01em;
}

.mu-13__crit {
  margin: 0;
  font-family: var(--mu-13-mono);
  font-size: 0.6875rem;
  letter-spacing: 0.04em;
  color: var(--mu-13-bad);
}

.mu-13__sample {
  min-inline-size: 0;
  display: grid;
  gap: 0.5rem;
  padding: 1rem;
  background: var(--mu-13-bg);
  border: 1px solid var(--mu-13-line);
  border-radius: 4px;
}

.mu-13__sample p {
  margin: 0;
  min-inline-size: 0;
}

.mu-13__sample-title {
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -0.012em;
}

.mu-13__secondary {
  font-size: 0.875rem;
  color: var(--mu-13-fail-ink);
  text-wrap: pretty;
}

.mu-13__panel.is-fixed .mu-13__secondary {
  color: var(--mu-13-ink-2);
}

.mu-13__fix-only {
  display: none;
}

.mu-13__panel.is-fixed .mu-13__fail-only {
  display: none;
}

.mu-13__panel.is-fixed .mu-13__fix-only {
  display: grid;
}

.mu-13__toolbar {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  min-inline-size: 0;
}

.mu-13__toolbar > span {
  display: flex;
  gap: 0.5rem;
}

.mu-13__panel.is-fixed .mu-13__toolbar > .mu-13__fix-only {
  display: flex;
}

.mu-13__icon-btn {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  min-inline-size: 44px;
  min-block-size: 44px;
  padding: 0;
  border: 1px solid var(--mu-13-line);
  border-radius: 4px;
  background: var(--mu-13-surface);
  color: var(--mu-13-ink);
  cursor: pointer;
}

.mu-13__icon-btn svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-13__icon-btn:focus-visible {
  outline: 2px solid var(--mu-13-ring);
  outline-offset: 2px;
}

.mu-13__tip {
  position: absolute;
  inset-block-start: calc(100% + 6px);
  inset-inline-start: 0;
  padding: 4px 8px;
  border-radius: 3px;
  white-space: nowrap;
  background: var(--mu-13-ink);
  color: var(--mu-13-bg);
  font-size: 0.6875rem;
  opacity: 0;
  pointer-events: none;
  transition: opacity 140ms ease;
}

.mu-13__icon-btn:hover .mu-13__tip,
.mu-13__icon-btn:focus-visible .mu-13__tip {
  opacity: 1;
}

.mu-13__fields {
  gap: 0.75rem;
}

.mu-13__field {
  display: grid;
  gap: 0.25rem;
  min-inline-size: 0;
}

.mu-13__label {
  font-size: 0.8125rem;
  font-weight: 500;
}

.mu-13__input {
  inline-size: 100%;
  min-inline-size: 0;
  min-block-size: 44px;
  padding-inline: 0.625rem;
  border: 1px solid var(--mu-13-line);
  border-radius: 4px;
  background: var(--mu-13-bg);
  color: var(--mu-13-ink);
  font: inherit;
  font-size: 0.875rem;
}

.mu-13__input::placeholder {
  color: var(--mu-13-ink-2);
  opacity: 1;
}

.mu-13__input:focus-visible {
  outline: 2px solid var(--mu-13-ring);
  outline-offset: 2px;
  border-color: var(--mu-13-acc);
}

.mu-13__fail-only > .mu-13__input + .mu-13__input {
  margin-block-start: 0.5rem;
}

.mu-13__target-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.mu-13__target {
  min-block-size: var(--mu-13-target-fail);
  block-size: var(--mu-13-target-fail);
  padding-inline: 0.625rem;
  border: 1px solid var(--mu-13-line);
  border-radius: 3px;
  background: var(--mu-13-surface);
  color: var(--mu-13-ink);
  font: inherit;
  font-size: 0.75rem;
  cursor: pointer;
}

.mu-13__target:focus-visible {
  outline: 2px solid var(--mu-13-ring);
  outline-offset: 2px;
}

.mu-13__panel.is-fixed .mu-13__target {
  min-block-size: 44px;
  block-size: 44px;
  min-inline-size: 44px;
  padding-inline: 1.125rem;
  border-color: transparent;
  background: var(--mu-13-acc);
  color: var(--mu-13-acc-ink);
  font-size: 0.875rem;
  font-weight: 600;
  border-radius: 4px;
}

.mu-13__panel.is-fixed .mu-13__target + .mu-13__target {
  background: transparent;
  color: var(--mu-13-ink);
  border-color: var(--mu-13-line);
}

.mu-13__measure {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.375rem;
  font-family: var(--mu-13-mono);
  font-size: 0.75rem;
  font-variant-numeric: tabular-nums;
}

.mu-13__measure-fail {
  color: var(--mu-13-bad);
  font-weight: 600;
}

.mu-13__measure-ok {
  display: none;
  color: var(--mu-13-ok);
  font-weight: 600;
}

.mu-13__panel.is-fixed .mu-13__measure-fail {
  display: none;
}

.mu-13__panel.is-fixed .mu-13__measure-ok {
  display: inline;
}

.mu-13__switch {
  justify-self: start;
  min-block-size: 44px;
  min-inline-size: 44px;
  display: inline-flex;
  align-items: center;
  padding-inline: 0.875rem;
  border: 1px solid var(--mu-13-line);
  border-radius: 4px;
  background: var(--mu-13-bg);
  color: var(--mu-13-ink);
  font: inherit;
  font-size: 0.8125rem;
  font-weight: 500;
  cursor: pointer;
}

.mu-13__switch:focus-visible {
  outline: 2px solid var(--mu-13-ring);
  outline-offset: 2px;
}

.mu-13__switch[aria-pressed="true"] {
  border-color: var(--mu-13-ok);
  color: var(--mu-13-ok);
}

@media (prefers-reduced-motion: reduce) {
  .mu-13__tip {
    transition: none;
  }
}

@media (min-width: 56rem) {
  .mu-13__stage {
    padding-inline: 3rem;
  }

  .mu-13__panel {
    padding: 1.5rem;
  }
}
```

## JavaScript
```js
(() => {
  const board = document.querySelector('#mu-13-board');
  if (!board) return;
  const switches = [...board.querySelectorAll('[data-mu-13-switch]')];
  const handlers = new Map();

  for (const btn of switches) {
    const panel = btn.closest('[data-mu-13-panel]');
    if (!panel) continue;
    const onClick = () => {
      const next = btn.getAttribute('aria-pressed') !== 'true';
      btn.setAttribute('aria-pressed', String(next));
      panel.classList.toggle('is-fixed', next);
      btn.querySelector('.mu-13__switch-label').textContent =
        next ? 'Show the failure' : 'Show the fix';
    };
    btn.addEventListener('click', onClick);
    handlers.set(btn, onClick);
  }

  board.__muCleanup = () => {
    for (const [btn, fn] of handlers) btn.removeEventListener('click', fn);
    handlers.clear();
  };
})();
```
