---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/elara-fintech/"
title: "Minimalist Mobile App Screen in a Frame"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "A single app screen inside a phone frame, where minimalism is under real pressure: 390 points of width, a 44px touch floor, and a thumb that has to reach…"
has_js: "true"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Mobile App Screen in a Frame
Source: https://codefronts.com/design-styles/css-minimalist-ui/elara-fintech/

A single app screen inside a phone frame, where minimalism is under real pressure: 390 points of width, a 44px touch floor, and a thumb that has to reach everything. It shows what gets cut first when space runs out &mdash; imagery, repeated metadata, tertiary actions &mdash; and why the touch floor is never the thing you cut. The tab list is a real widget with arrow keys, in 24 lines of vanilla script.
## HTML
```html
<section class="mu-19" aria-labelledby="mu-19-title">
  <h2 class="mu-19__sr" id="mu-19-title">Vale account</h2>
  <div class="mu-19__theme">
    <input class="mu-19__theme-input" type="checkbox" id="mu-19-theme">
    <label class="mu-19__theme-label" for="mu-19-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-19__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-19__stage">

    <div class="mu-19__frame-wrap">
      <div class="mu-19__frame">
        <div class="mu-19__screen" id="mu-19-screen">
          <header class="mu-19__app-head">
            <p class="mu-19__app-label">Vale</p>
            <button class="mu-19__icon-btn" type="button" aria-label="Account settings">
              <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="8" r="3.4" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M5.5 20a6.5 6.5 0 0 1 13 0" fill="none" stroke="currentColor" stroke-width="1.7"/></svg>
            </button>
          </header>

          <div class="mu-19__balance">
            <p class="mu-19__balance-label">Available balance</p>
            <p class="mu-19__balance-value">&pound;4,182.60</p>
            <p class="mu-19__balance-note">&pound;620.00 pending &middot; settles Tuesday</p>
          </div>

          <div class="mu-19__tabs" role="tablist" aria-label="Account view">
            <button class="mu-19__tab" type="button" role="tab" id="mu-19-tab-1" aria-controls="mu-19-panel-1" aria-selected="true">Activity</button>
            <button class="mu-19__tab" type="button" role="tab" id="mu-19-tab-2" aria-controls="mu-19-panel-2" aria-selected="false" tabindex="-1">Scheduled</button>
            <button class="mu-19__tab" type="button" role="tab" id="mu-19-tab-3" aria-controls="mu-19-panel-3" aria-selected="false" tabindex="-1">Cards</button>
          </div>

          <div class="mu-19__panels">
            <div class="mu-19__panel" role="tabpanel" id="mu-19-panel-1" aria-labelledby="mu-19-tab-1" tabindex="0">
              <ul class="mu-19__rows">
                <li><span class="mu-19__row-name">Basalt Coffee Roasters</span><span class="mu-19__row-meta">Today</span><span class="mu-19__row-amt">&minus;&pound;4.80</span></li>
                <li><span class="mu-19__row-name">Meridian salary</span><span class="mu-19__row-meta">28 Aug</span><span class="mu-19__row-amt mu-19__row-amt--in">+&pound;3,410.00</span></li>
                <li><span class="mu-19__row-name">Orbit Broadband monthly</span><span class="mu-19__row-meta">27 Aug</span><span class="mu-19__row-amt">&minus;&pound;38.00</span></li>
                <li><span class="mu-19__row-name">Fern Grocery, Islington</span><span class="mu-19__row-meta">26 Aug</span><span class="mu-19__row-amt">&minus;&pound;61.24</span></li>
                <li><span class="mu-19__row-name">Transfer to savings</span><span class="mu-19__row-meta">25 Aug</span><span class="mu-19__row-amt">&minus;&pound;400.00</span></li>
              </ul>
            </div>
            <div class="mu-19__panel" role="tabpanel" id="mu-19-panel-2" aria-labelledby="mu-19-tab-2" tabindex="0" hidden>
              <ul class="mu-19__rows">
                <li><span class="mu-19__row-name">Rent, Talon Property</span><span class="mu-19__row-meta">1 Sep</span><span class="mu-19__row-amt">&minus;&pound;1,240.00</span></li>
                <li><span class="mu-19__row-name">Prism Energy</span><span class="mu-19__row-meta">4 Sep</span><span class="mu-19__row-amt">&minus;&pound;92.50</span></li>
                <li><span class="mu-19__row-name">Savings standing order</span><span class="mu-19__row-meta">6 Sep</span><span class="mu-19__row-amt">&minus;&pound;400.00</span></li>
              </ul>
            </div>
            <div class="mu-19__panel" role="tabpanel" id="mu-19-panel-3" aria-labelledby="mu-19-tab-3" tabindex="0" hidden>
              <ul class="mu-19__rows">
                <li><span class="mu-19__row-name">Physical &middot; 4412</span><span class="mu-19__row-meta">Active</span><span class="mu-19__row-amt">&pound;500 / day</span></li>
                <li><span class="mu-19__row-name">Virtual &middot; subscriptions</span><span class="mu-19__row-meta">Active</span><span class="mu-19__row-amt">&pound;120 / mo</span></li>
                <li><span class="mu-19__row-name">Virtual &middot; travel</span><span class="mu-19__row-meta">Frozen</span><span class="mu-19__row-amt">&mdash;</span></li>
              </ul>
            </div>
          </div>

          <footer class="mu-19__bar">
            <button class="mu-19__primary" type="button">Send money</button>
          </footer>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.mu-19 {
  --mu-19-frame-w: 390px;
  --mu-19-radius: 40px;
  --mu-19-tab-underline: 2px;
  --mu-19-round: ui-rounded, "SF Pro Rounded", "Hiragino Maru Gothic ProN", system-ui, -apple-system, "Segoe UI", sans-serif;
  --mu-19-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --mu-19-bg: #eaefe9;
  --mu-19-bg: oklch(94% 0.016 145);
  --mu-19-shell: #d7ddd5;
  --mu-19-shell: oklch(88% 0.014 145);
  --mu-19-surface: #ffffff;
  --mu-19-surface: oklch(100% 0 0);
  --mu-19-ink: #14180f;
  --mu-19-ink: oklch(19% 0.012 130);
  --mu-19-ink-2: #4d5548;
  --mu-19-ink-2: oklch(44% 0.014 135);
  --mu-19-line: #dfe3dc;
  --mu-19-line: oklch(90% 0.008 140);
  --mu-19-acc: #1d5c3a;
  --mu-19-acc: oklch(42% 0.1 158);
  --mu-19-acc-ink: #ffffff;
  --mu-19-acc-ink: oklch(100% 0 0);
  --mu-19-in: #14663f;
  --mu-19-in: oklch(43% 0.11 158);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-19-bg);
  color: var(--mu-19-ink);
  font-family: var(--mu-19-round);
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

.mu-19 *,
.mu-19 *::before,
.mu-19 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .mu-19 {
    --mu-19-bg: #0f1310;
    --mu-19-bg: oklch(17.5% 0.01 145);
    --mu-19-shell: #1c211c;
    --mu-19-shell: oklch(24% 0.012 145);
    --mu-19-surface: #171c17;
    --mu-19-surface: oklch(21.5% 0.011 145);
    --mu-19-ink: #edf1ea;
    --mu-19-ink: oklch(95.5% 0.01 140);
    --mu-19-ink-2: #a3ac9d;
    --mu-19-ink-2: oklch(73.5% 0.014 140);
    --mu-19-line: #2c332b;
    --mu-19-line: oklch(29% 0.012 145);
    --mu-19-acc: #74d3a1;
    --mu-19-acc: oklch(82% 0.12 158);
    --mu-19-acc-ink: #0d1a12;
    --mu-19-acc-ink: oklch(17% 0.02 158);
    --mu-19-in: #74d3a1;
    --mu-19-in: oklch(82% 0.12 158);
  }
}

.mu-19[data-theme="dark"],
.mu-19:has(.mu-19__theme-input:checked) {
  --mu-19-bg: #0f1310;
  --mu-19-bg: oklch(17.5% 0.01 145);
  --mu-19-shell: #1c211c;
  --mu-19-shell: oklch(24% 0.012 145);
  --mu-19-surface: #171c17;
  --mu-19-surface: oklch(21.5% 0.011 145);
  --mu-19-ink: #edf1ea;
  --mu-19-ink: oklch(95.5% 0.01 140);
  --mu-19-ink-2: #a3ac9d;
  --mu-19-ink-2: oklch(73.5% 0.014 140);
  --mu-19-line: #2c332b;
  --mu-19-line: oklch(29% 0.012 145);
  --mu-19-acc: #74d3a1;
  --mu-19-acc: oklch(82% 0.12 158);
  --mu-19-acc-ink: #0d1a12;
  --mu-19-acc-ink: oklch(17% 0.02 158);
  --mu-19-in: #74d3a1;
  --mu-19-in: oklch(82% 0.12 158);
}

@media (prefers-color-scheme: light) {
  .mu-19:has(.mu-19__theme-input:checked) {
    --mu-19-bg: #0f1310;
    --mu-19-bg: oklch(17.5% 0.01 145);
    --mu-19-shell: #1c211c;
    --mu-19-shell: oklch(24% 0.012 145);
    --mu-19-surface: #171c17;
    --mu-19-surface: oklch(21.5% 0.011 145);
    --mu-19-ink: #edf1ea;
    --mu-19-ink: oklch(95.5% 0.01 140);
    --mu-19-ink-2: #a3ac9d;
    --mu-19-ink-2: oklch(73.5% 0.014 140);
    --mu-19-line: #2c332b;
    --mu-19-line: oklch(29% 0.012 145);
    --mu-19-acc: #74d3a1;
    --mu-19-acc: oklch(82% 0.12 158);
    --mu-19-acc-ink: #0d1a12;
    --mu-19-acc-ink: oklch(17% 0.02 158);
    --mu-19-in: #74d3a1;
    --mu-19-in: oklch(82% 0.12 158);
  }
}

@media (prefers-color-scheme: dark) {
  .mu-19:has(.mu-19__theme-input:checked) {
    --mu-19-bg: #eaefe9;
    --mu-19-bg: oklch(94% 0.016 145);
    --mu-19-shell: #d7ddd5;
    --mu-19-shell: oklch(88% 0.014 145);
    --mu-19-surface: #ffffff;
    --mu-19-surface: oklch(100% 0 0);
    --mu-19-ink: #14180f;
    --mu-19-ink: oklch(19% 0.012 130);
    --mu-19-ink-2: #4d5548;
    --mu-19-ink-2: oklch(44% 0.014 135);
    --mu-19-line: #dfe3dc;
    --mu-19-line: oklch(90% 0.008 140);
    --mu-19-acc: #1d5c3a;
    --mu-19-acc: oklch(42% 0.1 158);
    --mu-19-acc-ink: #ffffff;
    --mu-19-acc-ink: oklch(100% 0 0);
    --mu-19-in: #14663f;
    --mu-19-in: oklch(43% 0.11 158);
  }
}

.mu-19__sr {
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

.mu-19__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-19__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-19__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-19-line);
  border-radius: 50%;
  background: var(--mu-19-surface);
  color: var(--mu-19-ink-2);
  cursor: pointer;
}

.mu-19__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-19__theme-input:focus-visible + .mu-19__theme-label {
  outline: 2px solid var(--mu-19-acc);
  outline-offset: 2px;
}

.mu-19__stage {
  max-inline-size: 68rem;
  margin-inline: auto;
  padding: 2.5rem 1.25rem 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
}

.mu-19__frame-wrap {
  display: grid;
  min-inline-size: 0;
}

.mu-19__frame {
  inline-size: 100%;
  max-inline-size: var(--mu-19-frame-w);
  margin-inline: auto;
  padding: 10px;
  border-radius: var(--mu-19-radius);
  background: var(--mu-19-shell);
  min-inline-size: 0;
}

.mu-19__screen {
  min-inline-size: 0;
  aspect-ratio: 390 / 844;
  display: grid;
  grid-template-rows: auto auto auto minmax(0, 1fr) auto;
  background: var(--mu-19-surface);
  border-radius: calc(var(--mu-19-radius) - 10px);
  overflow: hidden;
}

.mu-19__app-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  padding: 0.75rem 1.25rem 0.25rem;
}

.mu-19__app-label {
  margin: 0;
  font-size: 0.9375rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.mu-19__icon-btn {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  min-inline-size: 44px;
  min-block-size: 44px;
  padding: 0;
  border: 0;
  border-radius: 50%;
  background: transparent;
  color: var(--mu-19-ink);
  cursor: pointer;
}

.mu-19__icon-btn svg {
  inline-size: 22px;
  block-size: 22px;
}

.mu-19__icon-btn:focus-visible {
  outline: 2px solid var(--mu-19-acc);
  outline-offset: 2px;
}

.mu-19__balance {
  padding: 0.5rem 1.25rem 1.25rem;
  display: grid;
  gap: 0.25rem;
}

.mu-19__balance p {
  margin: 0;
  min-inline-size: 0;
}

.mu-19__balance-label {
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--mu-19-ink-2);
}

.mu-19__balance-value {
  font-size: clamp(1.875rem, 8cqi, 2.375rem);
  line-height: 1.05;
  letter-spacing: -0.03em;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.mu-19__balance-note {
  font-size: 0.75rem;
  color: var(--mu-19-ink-2);
}

.mu-19__tabs {
  display: flex;
  gap: 0.25rem;
  padding-inline: 1.25rem;
  border-block-end: 1px solid var(--mu-19-line);
}

.mu-19__tab {
  min-block-size: 44px;
  min-inline-size: 44px;
  padding-inline: 0.5rem;
  border: 0;
  border-block-end: var(--mu-19-tab-underline) solid transparent;
  background: transparent;
  color: var(--mu-19-ink-2);
  font: inherit;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
}

.mu-19__tab[aria-selected="true"] {
  color: var(--mu-19-ink);
  border-block-end-color: var(--mu-19-acc);
}

.mu-19__tab:focus-visible {
  outline: 2px solid var(--mu-19-acc);
  outline-offset: -2px;
}

.mu-19__panels {
  min-inline-size: 0;
  min-block-size: 0;
  overflow-y: auto;
}

.mu-19__panel {
  min-inline-size: 0;
}

.mu-19__panel:focus-visible {
  outline: 2px solid var(--mu-19-acc);
  outline-offset: -2px;
}

.mu-19__rows {
  margin: 0;
  padding: 0.5rem 1.25rem;
  list-style: none;
  display: grid;
  gap: 0;
}

.mu-19__rows li {
  min-inline-size: 0;
  min-block-size: 44px;
  display: grid;
  align-items: center;
  gap: 0 0.75rem;
  grid-template-columns: minmax(0, 1fr) auto;
  padding-block: 0.625rem;
  border-block-end: 1px solid var(--mu-19-line);
}

.mu-19__rows li:last-child {
  border-block-end: 0;
}

.mu-19__row-name {
  grid-column: 1;
  min-inline-size: 0;
  font-size: 0.875rem;
  font-weight: 500;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.mu-19__row-meta {
  grid-column: 1;
  grid-row: 2;
  font-size: 0.75rem;
  color: var(--mu-19-ink-2);
}

.mu-19__row-amt {
  grid-column: 2;
  grid-row: 1 / span 2;
  font-size: 0.875rem;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}

.mu-19__row-amt--in {
  color: var(--mu-19-in);
}

.mu-19__bar {
  padding: 0.75rem 1.25rem calc(0.75rem + env(safe-area-inset-bottom, 0px));
  border-block-start: 1px solid var(--mu-19-line);
}

.mu-19__primary {
  inline-size: 100%;
  min-block-size: 48px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: 0;
  border-radius: 12px;
  background: var(--mu-19-acc);
  color: var(--mu-19-acc-ink);
  font: inherit;
  font-size: 0.9375rem;
  font-weight: 700;
  cursor: pointer;
}

.mu-19__primary:focus-visible {
  outline: 2px solid var(--mu-19-ink);
  outline-offset: 2px;
}

@supports (container-type: inline-size) {
  .mu-19__screen {
    container-type: inline-size;
  }
}

@media (min-width: 56rem) {
  .mu-19__stage {
    grid-template-columns: minmax(0, 1fr) minmax(0, 26rem);
    padding-inline: 3rem;
    gap: 3rem;
  }

  .mu-19__frame-wrap {
    grid-row: span 2;
  }
}
```

## JavaScript
```js
(() => {
  const screen = document.querySelector('#mu-19-screen');
  if (!screen) return;
  const tabs = [...screen.querySelectorAll('[role="tab"]')];
  if (!tabs.length) return;

  const select = (tab) => {
    for (const t of tabs) {
      const on = t === tab;
      t.setAttribute('aria-selected', String(on));
      t.tabIndex = on ? 0 : -1;
      const panel = screen.querySelector('#' + t.getAttribute('aria-controls'));
      if (panel) panel.hidden = !on;
    }
    tab.focus();
  };
  const onClick = (e) => select(e.currentTarget);
  const onKey = (e) => {
    const i = tabs.indexOf(e.currentTarget);
    if (e.key === 'ArrowRight') select(tabs[(i + 1) % tabs.length]);
    else if (e.key === 'ArrowLeft') select(tabs[(i - 1 + tabs.length) % tabs.length]);
    else return;
    e.preventDefault();
  };

  for (const t of tabs) {
    t.addEventListener('click', onClick);
    t.addEventListener('keydown', onKey);
  }

  screen.__muCleanup = () => {
    for (const t of tabs) {
      t.removeEventListener('click', onClick);
      t.removeEventListener('keydown', onKey);
    }
  };
})();
```
