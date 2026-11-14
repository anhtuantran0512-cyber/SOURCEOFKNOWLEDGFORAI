---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/type-hierarchy-without-any-color-change/"
title: "Type Hierarchy Without Any Color Change"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "Two identical cards, one tinted and one reduced to a single ink colour, so you can check whether the hierarchy actually survives."
has_js: "false"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Type Hierarchy Without Any Color Change
Source: https://codefronts.com/design-styles/css-minimalist-ui/type-hierarchy-without-any-color-change/

Two identical cards, one tinted and one reduced to a single ink colour, so you can check whether the hierarchy actually survives. Separation comes from size, weight, letter-spacing and space &mdash; and if it collapses the moment colour is removed, colour was doing structural work it should never have been doing.
## HTML
```html
<section class="mu-02" aria-labelledby="mu-02-title">
  <h2 class="mu-02__sr" id="mu-02-title">Hierarchy with and without colour</h2>
  <div class="mu-02__theme">
    <input class="mu-02__theme-input" type="checkbox" id="mu-02-theme">
    <label class="mu-02__theme-label" for="mu-02-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-02__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-02__stage">

    <div class="mu-02__pair">
      <article class="mu-02__side mu-02__side--tinted" aria-labelledby="mu-02-side-a">
        <h3 class="mu-02__side-title" id="mu-02-side-a">With colour</h3>
        <div class="mu-02__card">
          <p class="mu-02__kicker">Invoice INV-2043</p>
          <h4 class="mu-02__card-title">Basalt Industries</h4>
          <p class="mu-02__amount">$18,420.00</p>
          <p class="mu-02__meta">Due 14 September &middot; Net 30 &middot; Sent by Priya Sharma</p>
          <ul class="mu-02__facts">
            <li><span>Retainer</span><b>$12,000.00</b></li>
            <li><span>Overage, 42 hrs</span><b>$6,420.00</b></li>
          </ul>
          <p class="mu-02__status">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
            Approved
          </p>
        </div>
      </article>

      <article class="mu-02__side mu-02__side--flat" aria-labelledby="mu-02-side-b">
        <h3 class="mu-02__side-title" id="mu-02-side-b">One ink colour</h3>
        <div class="mu-02__card">
          <p class="mu-02__kicker">Invoice INV-2043</p>
          <h4 class="mu-02__card-title">Basalt Industries</h4>
          <p class="mu-02__amount">$18,420.00</p>
          <p class="mu-02__meta">Due 14 September &middot; Net 30 &middot; Sent by Priya Sharma</p>
          <ul class="mu-02__facts">
            <li><span>Retainer</span><b>$12,000.00</b></li>
            <li><span>Overage, 42 hrs</span><b>$6,420.00</b></li>
          </ul>
          <p class="mu-02__status">
            <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 13l4 4L19 7" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
            Approved
          </p>
        </div>
      </article>
    </div>

    <dl class="mu-02__legend">
      <div><dt>Kicker</dt><dd>0.75rem &middot; 500 &middot; +0.10em &middot; uppercase</dd></div>
      <div><dt>Title</dt><dd>1.5rem &middot; 600 &middot; &minus;0.02em</dd></div>
      <div><dt>Amount</dt><dd>2.25rem &middot; 600 &middot; &minus;0.03em &middot; tabular</dd></div>
      <div><dt>Meta</dt><dd>0.875rem &middot; 400 &middot; normal</dd></div>
    </dl>
  </div>
</section>
```
## CSS
```css
.mu-02 {
  --mu-02-unit: 0.5rem;
  --mu-02-weight-hi: 600;
  --mu-02-track-label: 0.1em;
  --mu-02-font: ui-serif, Georgia, "Iowan Old Style", "Palatino Linotype", Palatino, serif;
  --mu-02-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --mu-02-bg: #ffffff;
  --mu-02-bg: oklch(100% 0 0);
  --mu-02-surface: #ffffff;
  --mu-02-surface: oklch(100% 0 0);
  --mu-02-ink: #1a1a1a;
  --mu-02-ink: oklch(22% 0 0);
  --mu-02-ink-2: #55595c;
  --mu-02-ink-2: oklch(46% 0.004 250);
  --mu-02-line: #d5d7d9;
  --mu-02-line: oklch(86% 0.003 250);
  --mu-02-tint: #0b5cd5;
  --mu-02-tint: oklch(48% 0.18 258);
  --mu-02-tint-2: #7a5b12;
  --mu-02-tint-2: oklch(46% 0.1 85);
  --mu-02-acc: #0b5cd5;
  --mu-02-acc: oklch(48% 0.18 258);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-02-bg);
  color: var(--mu-02-ink);
  font-family: var(--mu-02-ui);
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

.mu-02 *,
.mu-02 *::before,
.mu-02 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .mu-02 {
    --mu-02-bg: #101112;
    --mu-02-bg: oklch(17.5% 0.002 250);
    --mu-02-surface: #191b1d;
    --mu-02-surface: oklch(23% 0.003 250);
    --mu-02-ink: #f2f3f4;
    --mu-02-ink: oklch(96% 0.002 250);
    --mu-02-ink-2: #a9aeb2;
    --mu-02-ink-2: oklch(75% 0.005 250);
    --mu-02-line: #353839;
    --mu-02-line: oklch(34% 0.004 250);
    --mu-02-tint: #7fb0ff;
    --mu-02-tint: oklch(78% 0.12 258);
    --mu-02-tint-2: #dcbb63;
    --mu-02-tint-2: oklch(81% 0.1 85);
    --mu-02-acc: #7fb0ff;
    --mu-02-acc: oklch(78% 0.12 258);
  }
}

.mu-02[data-theme="dark"],
.mu-02:has(.mu-02__theme-input:checked) {
  --mu-02-bg: #101112;
  --mu-02-bg: oklch(17.5% 0.002 250);
  --mu-02-surface: #191b1d;
  --mu-02-surface: oklch(23% 0.003 250);
  --mu-02-ink: #f2f3f4;
  --mu-02-ink: oklch(96% 0.002 250);
  --mu-02-ink-2: #a9aeb2;
  --mu-02-ink-2: oklch(75% 0.005 250);
  --mu-02-line: #353839;
  --mu-02-line: oklch(34% 0.004 250);
  --mu-02-tint: #7fb0ff;
  --mu-02-tint: oklch(78% 0.12 258);
  --mu-02-tint-2: #dcbb63;
  --mu-02-tint-2: oklch(81% 0.1 85);
  --mu-02-acc: #7fb0ff;
  --mu-02-acc: oklch(78% 0.12 258);
}

@media (prefers-color-scheme: light) {
  .mu-02:has(.mu-02__theme-input:checked) {
    --mu-02-bg: #101112;
    --mu-02-bg: oklch(17.5% 0.002 250);
    --mu-02-surface: #191b1d;
    --mu-02-surface: oklch(23% 0.003 250);
    --mu-02-ink: #f2f3f4;
    --mu-02-ink: oklch(96% 0.002 250);
    --mu-02-ink-2: #a9aeb2;
    --mu-02-ink-2: oklch(75% 0.005 250);
    --mu-02-line: #353839;
    --mu-02-line: oklch(34% 0.004 250);
    --mu-02-tint: #7fb0ff;
    --mu-02-tint: oklch(78% 0.12 258);
    --mu-02-tint-2: #dcbb63;
    --mu-02-tint-2: oklch(81% 0.1 85);
    --mu-02-acc: #7fb0ff;
    --mu-02-acc: oklch(78% 0.12 258);
  }
}

@media (prefers-color-scheme: dark) {
  .mu-02:has(.mu-02__theme-input:checked) {
    --mu-02-bg: #ffffff;
    --mu-02-bg: oklch(100% 0 0);
    --mu-02-surface: #ffffff;
    --mu-02-surface: oklch(100% 0 0);
    --mu-02-ink: #1a1a1a;
    --mu-02-ink: oklch(22% 0 0);
    --mu-02-ink-2: #55595c;
    --mu-02-ink-2: oklch(46% 0.004 250);
    --mu-02-line: #d5d7d9;
    --mu-02-line: oklch(86% 0.003 250);
    --mu-02-tint: #0b5cd5;
    --mu-02-tint: oklch(48% 0.18 258);
    --mu-02-tint-2: #7a5b12;
    --mu-02-tint-2: oklch(46% 0.1 85);
    --mu-02-acc: #0b5cd5;
    --mu-02-acc: oklch(48% 0.18 258);
  }
}

.mu-02__sr {
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

.mu-02__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-02__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-02__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-02-line);
  border-radius: 4px;
  background: var(--mu-02-surface);
  color: var(--mu-02-ink-2);
  cursor: pointer;
}

.mu-02__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-02__theme-input:focus-visible + .mu-02__theme-label {
  outline: 2px solid var(--mu-02-acc);
  outline-offset: 2px;
}

.mu-02__stage {
  max-inline-size: 72rem;
  margin-inline: auto;
  padding: calc(var(--mu-02-unit) * 8) calc(var(--mu-02-unit) * 3) calc(var(--mu-02-unit) * 10);
  display: grid;
  gap: calc(var(--mu-02-unit) * 6);
  grid-template-columns: minmax(0, 1fr);
}

.mu-02__pair {
  display: grid;
  gap: calc(var(--mu-02-unit) * 3);
  grid-template-columns: minmax(0, 1fr);
}

.mu-02__side {
  min-inline-size: 0;
  display: grid;
  gap: var(--mu-02-unit);
  align-content: start;
  padding: calc(var(--mu-02-unit) * 3);
  border: 1px solid var(--mu-02-line);
  border-radius: 4px;
}

.mu-02__side-title {
  margin: 0;
  font-size: 0.8125rem;
  font-weight: 600;
  letter-spacing: var(--mu-02-track-label);
  text-transform: uppercase;
}

.mu-02__card {
  min-inline-size: 0;
  background: var(--mu-02-surface);
  border-block-start: 1px solid var(--mu-02-line);
  padding-block: calc(var(--mu-02-unit) * 3);
  display: grid;
  gap: calc(var(--mu-02-unit) * 1.5);
}

.mu-02__card p,
.mu-02__card h4 {
  margin: 0;
  min-inline-size: 0;
}

.mu-02__kicker {
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: var(--mu-02-track-label);
  text-transform: uppercase;
  color: var(--mu-02-ink-2);
}

.mu-02__card-title {
  font-family: var(--mu-02-font);
  font-size: 1.5rem;
  line-height: 1.15;
  letter-spacing: -0.02em;
  font-weight: var(--mu-02-weight-hi);
}

.mu-02__amount {
  font-size: clamp(1.875rem, 1.5rem + 1.5vw, 2.25rem);
  line-height: 1.05;
  letter-spacing: -0.03em;
  font-weight: var(--mu-02-weight-hi);
  font-variant-numeric: tabular-nums;
}

.mu-02__meta {
  font-size: 0.875rem;
  color: var(--mu-02-ink-2);
  text-wrap: pretty;
}

.mu-02__facts {
  margin: var(--mu-02-unit) 0 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: var(--mu-02-unit);
  font-size: 0.875rem;
  border-block-start: 1px solid var(--mu-02-line);
  padding-block-start: calc(var(--mu-02-unit) * 2);
}

.mu-02__facts li {
  display: flex;
  justify-content: space-between;
  gap: calc(var(--mu-02-unit) * 2);
  min-inline-size: 0;
}

.mu-02__facts span {
  color: var(--mu-02-ink-2);
  min-inline-size: 0;
}

.mu-02__facts b {
  font-weight: 500;
  font-variant-numeric: tabular-nums;
}

.mu-02__status {
  display: inline-flex;
  align-items: center;
  gap: var(--mu-02-unit);
  font-size: 0.8125rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.mu-02__status svg {
  inline-size: 16px;
  block-size: 16px;
  flex: none;
}

.mu-02__side--tinted .mu-02__kicker {
  color: var(--mu-02-tint);
}

.mu-02__side--tinted .mu-02__amount {
  color: var(--mu-02-tint);
}

.mu-02__side--tinted .mu-02__status {
  color: var(--mu-02-tint-2);
}

.mu-02__side--flat .mu-02__card * {
  color: var(--mu-02-ink);
}

.mu-02__legend {
  margin: 0;
  display: grid;
  gap: var(--mu-02-unit);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 14rem), 1fr));
  padding-block: calc(var(--mu-02-unit) * 3);
  border-block: 1px solid var(--mu-02-line);
  font-size: 0.8125rem;
}

.mu-02__legend > div {
  min-inline-size: 0;
  display: grid;
  gap: 2px;
}

.mu-02__legend dt {
  margin: 0;
  font-weight: 600;
}

.mu-02__legend dd {
  margin: 0;
  color: var(--mu-02-ink-2);
}

@media (min-width: 52rem) {
  .mu-02__pair {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .mu-02__stage {
    padding-inline: calc(var(--mu-02-unit) * 6);
  }
}
```
