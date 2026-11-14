---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/the-one-accent-color-restraint-budget/"
title: "The One Accent Color Restraint Budget"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "A stated budget: one accent, spent on the single most important action in the view."
has_js: "false"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: The One Accent Color Restraint Budget
Source: https://codefronts.com/design-styles/css-minimalist-ui/the-one-accent-color-restraint-budget/

A stated budget: one accent, spent on the single most important action in the view. The same panel is shown with one accent and then with three, so you can watch the primary action stop being primary &mdash; and the demo draws the line between an accent and a semantic status colour, which is not part of the budget.
## HTML
```html
<section class="mu-09" aria-labelledby="mu-09-title">
  <h2 class="mu-09__sr" id="mu-09-title">Accent colour comparison</h2>
  <div class="mu-09__theme">
    <input class="mu-09__theme-input" type="checkbox" id="mu-09-theme">
    <label class="mu-09__theme-label" for="mu-09-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-09__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-09__stage">

    <div class="mu-09__pair">
      <article class="mu-09__panel" aria-labelledby="mu-09-a">
        <header class="mu-09__panel-head">
          <h3 class="mu-09__panel-title" id="mu-09-a">Budget: 1 accent</h3>
        </header>
        <div class="mu-09__body">
          <p class="mu-09__kicker">Invoice INV-2043 &middot; Basalt Industries</p>
          <p class="mu-09__amount">$18,420.00</p>
          <ul class="mu-09__rows">
            <li><span>Retainer</span><b>$12,000.00</b></li>
            <li><span>Overage, 42 hrs</span><b>$6,420.00</b></li>
            <li><span>Due</span><b>14 September</b></li>
          </ul>
          <p class="mu-09__status mu-09__status--ok">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
            Approved by Priya Sharma
          </p>
          <div class="mu-09__actions">
            <button class="mu-09__btn mu-09__btn--primary" type="button">Send for payment</button>
            <button class="mu-09__btn" type="button">Edit lines</button>
            <button class="mu-09__btn mu-09__btn--quiet" type="button">Duplicate</button>
          </div>
        </div>
      </article>

      <article class="mu-09__panel mu-09__panel--loud" aria-labelledby="mu-09-b">
        <header class="mu-09__panel-head">
          <h3 class="mu-09__panel-title" id="mu-09-b">Budget: 3 accents</h3>
        </header>
        <div class="mu-09__body">
          <p class="mu-09__kicker mu-09__kicker--tint">Invoice INV-2043 &middot; Basalt Industries</p>
          <p class="mu-09__amount mu-09__amount--tint">$18,420.00</p>
          <ul class="mu-09__rows">
            <li><span>Retainer</span><b>$12,000.00</b></li>
            <li><span>Overage, 42 hrs</span><b>$6,420.00</b></li>
            <li><span>Due</span><b>14 September</b></li>
          </ul>
          <p class="mu-09__status mu-09__status--ok">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
            Approved by Priya Sharma
          </p>
          <div class="mu-09__actions">
            <button class="mu-09__btn mu-09__btn--primary" type="button">Send for payment</button>
            <button class="mu-09__btn mu-09__btn--alt2" type="button">Edit lines</button>
            <button class="mu-09__btn mu-09__btn--alt3" type="button">Duplicate</button>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.mu-09 {
  --mu-09-radius: 4px;
  --mu-09-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --mu-09-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --mu-09-bg: #101a2c;
  --mu-09-bg: oklch(21% 0.04 258);
  --mu-09-surface: #17233a;
  --mu-09-surface: oklch(25.5% 0.042 258);
  --mu-09-surface-2: #1e2c46;
  --mu-09-surface-2: oklch(29% 0.044 258);
  --mu-09-ink: #f2f5fa;
  --mu-09-ink: oklch(96.5% 0.005 258);
  --mu-09-ink-2: #a9b6cc;
  --mu-09-ink-2: oklch(76% 0.026 258);
  --mu-09-line: #2d3c58;
  --mu-09-line: oklch(35% 0.038 258);
  --mu-09-acc: #7fb4ff;
  --mu-09-acc: oklch(79% 0.13 260);
  --mu-09-acc-ink: #0b1526;
  --mu-09-acc-ink: oklch(18% 0.03 258);
  --mu-09-alt2: #f0a35c;
  --mu-09-alt2: oklch(78% 0.13 62);
  --mu-09-alt3: #b79bf5;
  --mu-09-alt3: oklch(76% 0.13 300);
  --mu-09-status-ok: #6ed49a;
  --mu-09-status-ok: oklch(82% 0.13 155);
  --mu-09-status-warn: #f2c661;
  --mu-09-status-warn: oklch(85% 0.12 90);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-09-bg);
  color: var(--mu-09-ink);
  font-family: var(--mu-09-ui);
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

.mu-09 *,
.mu-09 *::before,
.mu-09 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: light) {
  .mu-09 {
    --mu-09-bg: #eef1f6;
    --mu-09-bg: oklch(94.5% 0.008 258);
    --mu-09-surface: #ffffff;
    --mu-09-surface: oklch(100% 0 0);
    --mu-09-surface-2: #f6f8fb;
    --mu-09-surface-2: oklch(97.8% 0.005 258);
    --mu-09-ink: #101a2c;
    --mu-09-ink: oklch(21% 0.04 258);
    --mu-09-ink-2: #4b5872;
    --mu-09-ink-2: oklch(45% 0.035 258);
    --mu-09-line: #ccd5e2;
    --mu-09-line: oklch(86% 0.014 258);
    --mu-09-acc: #14459e;
    --mu-09-acc: oklch(40% 0.16 262);
    --mu-09-acc-ink: #ffffff;
    --mu-09-acc-ink: oklch(100% 0 0);
    --mu-09-alt2: #8a4a06;
    --mu-09-alt2: oklch(45% 0.12 58);
    --mu-09-alt3: #5b2fb0;
    --mu-09-alt3: oklch(42% 0.18 298);
    --mu-09-status-ok: #16663d;
    --mu-09-status-ok: oklch(44% 0.11 155);
    --mu-09-status-warn: #7a5b12;
    --mu-09-status-warn: oklch(46% 0.1 85);
  }
}

.mu-09[data-theme="light"],
.mu-09:has(.mu-09__theme-input:checked) {
  --mu-09-bg: #eef1f6;
  --mu-09-bg: oklch(94.5% 0.008 258);
  --mu-09-surface: #ffffff;
  --mu-09-surface: oklch(100% 0 0);
  --mu-09-surface-2: #f6f8fb;
  --mu-09-surface-2: oklch(97.8% 0.005 258);
  --mu-09-ink: #101a2c;
  --mu-09-ink: oklch(21% 0.04 258);
  --mu-09-ink-2: #4b5872;
  --mu-09-ink-2: oklch(45% 0.035 258);
  --mu-09-line: #ccd5e2;
  --mu-09-line: oklch(86% 0.014 258);
  --mu-09-acc: #14459e;
  --mu-09-acc: oklch(40% 0.16 262);
  --mu-09-acc-ink: #ffffff;
  --mu-09-acc-ink: oklch(100% 0 0);
  --mu-09-alt2: #8a4a06;
  --mu-09-alt2: oklch(45% 0.12 58);
  --mu-09-alt3: #5b2fb0;
  --mu-09-alt3: oklch(42% 0.18 298);
  --mu-09-status-ok: #16663d;
  --mu-09-status-ok: oklch(44% 0.11 155);
  --mu-09-status-warn: #7a5b12;
  --mu-09-status-warn: oklch(46% 0.1 85);
}

@media (prefers-color-scheme: dark) {
  .mu-09:has(.mu-09__theme-input:checked) {
    --mu-09-bg: #eef1f6;
    --mu-09-bg: oklch(94.5% 0.008 258);
    --mu-09-surface: #ffffff;
    --mu-09-surface: oklch(100% 0 0);
    --mu-09-surface-2: #f6f8fb;
    --mu-09-surface-2: oklch(97.8% 0.005 258);
    --mu-09-ink: #101a2c;
    --mu-09-ink: oklch(21% 0.04 258);
    --mu-09-ink-2: #4b5872;
    --mu-09-ink-2: oklch(45% 0.035 258);
    --mu-09-line: #ccd5e2;
    --mu-09-line: oklch(86% 0.014 258);
    --mu-09-acc: #14459e;
    --mu-09-acc: oklch(40% 0.16 262);
    --mu-09-acc-ink: #ffffff;
    --mu-09-acc-ink: oklch(100% 0 0);
    --mu-09-alt2: #8a4a06;
    --mu-09-alt2: oklch(45% 0.12 58);
    --mu-09-alt3: #5b2fb0;
    --mu-09-alt3: oklch(42% 0.18 298);
    --mu-09-status-ok: #16663d;
    --mu-09-status-ok: oklch(44% 0.11 155);
    --mu-09-status-warn: #7a5b12;
    --mu-09-status-warn: oklch(46% 0.1 85);
  }
}

@media (prefers-color-scheme: light) {
  .mu-09:has(.mu-09__theme-input:checked) {
    --mu-09-bg: #101a2c;
    --mu-09-bg: oklch(21% 0.04 258);
    --mu-09-surface: #17233a;
    --mu-09-surface: oklch(25.5% 0.042 258);
    --mu-09-surface-2: #1e2c46;
    --mu-09-surface-2: oklch(29% 0.044 258);
    --mu-09-ink: #f2f5fa;
    --mu-09-ink: oklch(96.5% 0.005 258);
    --mu-09-ink-2: #a9b6cc;
    --mu-09-ink-2: oklch(76% 0.026 258);
    --mu-09-line: #2d3c58;
    --mu-09-line: oklch(35% 0.038 258);
    --mu-09-acc: #7fb4ff;
    --mu-09-acc: oklch(79% 0.13 260);
    --mu-09-acc-ink: #0b1526;
    --mu-09-acc-ink: oklch(18% 0.03 258);
    --mu-09-alt2: #f0a35c;
    --mu-09-alt2: oklch(78% 0.13 62);
    --mu-09-alt3: #b79bf5;
    --mu-09-alt3: oklch(76% 0.13 300);
    --mu-09-status-ok: #6ed49a;
    --mu-09-status-ok: oklch(82% 0.13 155);
    --mu-09-status-warn: #f2c661;
    --mu-09-status-warn: oklch(85% 0.12 90);
  }
}

.mu-09__sr {
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

.mu-09__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-09__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-09__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-09-line);
  border-radius: 50%;
  background: var(--mu-09-surface);
  color: var(--mu-09-ink-2);
  cursor: pointer;
}

.mu-09__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-09__theme-input:focus-visible + .mu-09__theme-label {
  outline: 2px solid var(--mu-09-acc);
  outline-offset: 2px;
}

.mu-09__stage {
  max-inline-size: 72rem;
  margin-inline: auto;
  padding: 4rem 1.5rem 5rem;
  display: grid;
  gap: 3rem;
  grid-template-columns: minmax(0, 1fr);
}

.mu-09__pair {
  display: grid;
  gap: 1.5rem;
  grid-template-columns: minmax(0, 1fr);
}

.mu-09__panel {
  min-inline-size: 0;
  display: grid;
  gap: 1.25rem;
  align-content: start;
  padding: 1.5rem;
  background: var(--mu-09-surface);
  border: 1px solid var(--mu-09-line);
  border-radius: 8px;
}

.mu-09__panel-head {
  display: grid;
  gap: 2px;
  min-inline-size: 0;
}

.mu-09__panel-title {
  margin: 0;
  font-size: 0.8125rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.mu-09__body {
  min-inline-size: 0;
  display: grid;
  gap: 1rem;
  padding: 1.25rem;
  background: var(--mu-09-surface-2);
  border-radius: 6px;
}

.mu-09__body p {
  margin: 0;
  min-inline-size: 0;
}

.mu-09__kicker {
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--mu-09-ink-2);
}

.mu-09__kicker--tint {
  color: var(--mu-09-alt3);
}

.mu-09__amount {
  font-size: clamp(1.875rem, 1.5rem + 1.6vw, 2.5rem);
  line-height: 1.05;
  letter-spacing: -0.03em;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

.mu-09__amount--tint {
  color: var(--mu-09-alt2);
}

.mu-09__rows {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0.5rem;
  font-size: 0.875rem;
  padding-block: 0.75rem;
  border-block: 1px solid var(--mu-09-line);
}

.mu-09__rows li {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  min-inline-size: 0;
}

.mu-09__rows span {
  color: var(--mu-09-ink-2);
  min-inline-size: 0;
}

.mu-09__rows b {
  font-weight: 500;
  font-variant-numeric: tabular-nums;
}

.mu-09__status {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.8125rem;
  font-weight: 600;
}

.mu-09__status svg {
  inline-size: 16px;
  block-size: 16px;
  flex: none;
}

.mu-09__status--ok {
  color: var(--mu-09-status-ok);
}

.mu-09__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.mu-09__btn {
  min-block-size: 44px;
  min-inline-size: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding-inline: 1rem;
  border-radius: var(--mu-09-radius);
  border: 1px solid var(--mu-09-line);
  background: transparent;
  color: var(--mu-09-ink);
  font: inherit;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: border-color 150ms ease, background-color 150ms ease;
}

.mu-09__btn:hover {
  border-color: var(--mu-09-ink-2);
}

.mu-09__btn:focus-visible {
  outline: 2px solid var(--mu-09-acc);
  outline-offset: 2px;
}

.mu-09__btn--quiet {
  border-color: transparent;
  color: var(--mu-09-ink-2);
}

.mu-09__btn--primary {
  background: var(--mu-09-acc);
  border-color: var(--mu-09-acc);
  color: var(--mu-09-acc-ink);
  font-weight: 600;
}

.mu-09__btn--primary:active {
  background: rgba(127, 180, 255, 0.82);
  background: color-mix(in oklab, var(--mu-09-acc) 82%, var(--mu-09-bg));
}

.mu-09__btn--alt2 {
  background: var(--mu-09-alt2);
  border-color: var(--mu-09-alt2);
  color: var(--mu-09-acc-ink);
  font-weight: 600;
}

.mu-09__btn--alt3 {
  background: var(--mu-09-alt3);
  border-color: var(--mu-09-alt3);
  color: var(--mu-09-acc-ink);
  font-weight: 600;
}

@media (prefers-reduced-motion: reduce) {
  .mu-09__btn {
    transition: none;
  }
}

@media (min-width: 52rem) {
  .mu-09__pair {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .mu-09__stage {
    padding-inline: 3rem;
  }

  .mu-09__panel {
    padding: 2rem;
  }
}
```
