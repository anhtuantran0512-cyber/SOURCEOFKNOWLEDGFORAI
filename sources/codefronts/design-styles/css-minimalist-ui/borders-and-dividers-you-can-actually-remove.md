---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/borders-and-dividers-you-can-actually-remove/"
title: "Borders and Dividers You Can Actually Remove"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "An audit, not a style: delete each border and see whether space or alignment already did its job."
has_js: "false"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Borders and Dividers You Can Actually Remove
Source: https://codefronts.com/design-styles/css-minimalist-ui/borders-and-dividers-you-can-actually-remove/

An audit, not a style: delete each border and see whether space or alignment already did its job. A table and a card set are shown fully ruled, then stripped, with a note on every rule that survived. Most card borders lose the test, most table rules lose it too &mdash; but not all, because in dense data, scanning across a row genuinely needs a guide, and a rule that stays has to be visible at 3:1 rather than a fashionable 8% hairline.
## HTML
```html
<section class="mu-11" aria-labelledby="mu-11-title">
  <h2 class="mu-11__sr" id="mu-11-title">Border audit reference</h2>
  <div class="mu-11__theme">
    <input class="mu-11__theme-input" type="checkbox" id="mu-11-theme">
    <label class="mu-11__theme-label" for="mu-11-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-11__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-11__stage">

    <section class="mu-11__block" aria-labelledby="mu-11-t1">
      <div class="mu-11__block-head">
        <h3 class="mu-11__sub" id="mu-11-t1">Before &mdash; fully ruled</h3>
        <p class="mu-11__count">9 rules &middot; outer box, header, every row, every column</p>
      </div>
      <div class="mu-11__scroller">
        <table class="mu-11__table mu-11__table--ruled">
          <caption class="mu-11__sr">Regional revenue, fully ruled version</caption>
          <thead>
            <tr><th scope="col">Region</th><th scope="col">Accounts</th><th scope="col">MRR</th><th scope="col">Change</th></tr>
          </thead>
          <tbody>
            <tr><th scope="row">Nordics</th><td>184</td><td>$92,400</td><td>+4.2%</td></tr>
            <tr><th scope="row">DACH</th><td>231</td><td>$118,900</td><td>+1.8%</td></tr>
            <tr><th scope="row">Benelux</th><td>96</td><td>$41,300</td><td>&minus;0.6%</td></tr>
            <tr><th scope="row">Iberia</th><td>74</td><td>$28,750</td><td>+6.1%</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section class="mu-11__block" aria-labelledby="mu-11-t2">
      <div class="mu-11__block-head">
        <h3 class="mu-11__sub" id="mu-11-t2">After &mdash; 8 removed, 1 kept</h3>
        <p class="mu-11__count">Header rule kept at 3:1 &middot; hover tint replaces row rules</p>
      </div>
      <div class="mu-11__scroller">
        <table class="mu-11__table mu-11__table--clean">
          <caption class="mu-11__sr">Regional revenue, audited version</caption>
          <thead>
            <tr><th scope="col">Region</th><th scope="col">Accounts</th><th scope="col">MRR</th><th scope="col">Change</th></tr>
          </thead>
          <tbody>
            <tr><th scope="row">Nordics</th><td>184</td><td>$92,400</td><td>+4.2%</td></tr>
            <tr><th scope="row">DACH</th><td>231</td><td>$118,900</td><td>+1.8%</td></tr>
            <tr><th scope="row">Benelux</th><td>96</td><td>$41,300</td><td>&minus;0.6%</td></tr>
            <tr><th scope="row">Iberia</th><td>74</td><td>$28,750</td><td>+6.1%</td></tr>
          </tbody>
        </table>
      </div>
    </section>

    <section class="mu-11__block" aria-labelledby="mu-11-t3">
      <div class="mu-11__block-head">
        <h3 class="mu-11__sub" id="mu-11-t3">Card set &mdash; borders removed</h3>
        <p class="mu-11__count">Tone and padding replace the outline entirely</p>
      </div>
      <ul class="mu-11__cards">
        <li class="mu-11__card">
          <p class="mu-11__card-kicker">Fern</p>
          <h4 class="mu-11__card-title">Support inbox</h4>
          <p class="mu-11__card-text">14 open, 3 waiting on a customer reply. Median first response 42 minutes.</p>
          <a class="mu-11__card-link" href="#mu-11-title">Open queue</a>
        </li>
        <li class="mu-11__card">
          <p class="mu-11__card-kicker">Talon</p>
          <h4 class="mu-11__card-title">Renewals this month</h4>
          <p class="mu-11__card-text">9 contracts, $214,000 combined. Two need a signature before the 14th.</p>
          <a class="mu-11__card-link" href="#mu-11-title">Review renewals</a>
        </li>
        <li class="mu-11__card">
          <p class="mu-11__card-kicker">Quill</p>
          <h4 class="mu-11__card-title">Draft releases</h4>
          <p class="mu-11__card-text">Draft saved 6 minutes ago by Alex Chen. No blocking review comments.</p>
          <a class="mu-11__card-link" href="#mu-11-title">Continue editing</a>
        </li>
      </ul>
    </section>
  </div>
</section>
```
## CSS
```css
.mu-11 {
  --mu-11-pad: 1.25rem;
  --mu-11-rule: transparent;
  --mu-11-rule-strong: 1px solid var(--mu-11-line-strong);
  --mu-11-card-border: 0;
  --mu-11-font: "Helvetica Neue", Helvetica, Arial, system-ui, sans-serif;
  --mu-11-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --mu-11-bg: #f2ece7;
  --mu-11-bg: oklch(93.5% 0.012 55);
  --mu-11-surface: #fbf7f4;
  --mu-11-surface: oklch(98% 0.007 60);
  --mu-11-surface-2: #e8e0d9;
  --mu-11-surface-2: oklch(90% 0.014 58);
  --mu-11-ink: #1e1a17;
  --mu-11-ink: oklch(21.5% 0.01 50);
  --mu-11-ink-2: #57504a;
  --mu-11-ink-2: oklch(45% 0.012 52);
  --mu-11-line: #d6cbc1;
  --mu-11-line: oklch(85% 0.016 58);
  --mu-11-line-strong: #7d726a;
  --mu-11-line-strong: oklch(54% 0.018 55);
  --mu-11-acc: #8c3b1c;
  --mu-11-acc: oklch(45% 0.13 40);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-11-bg);
  color: var(--mu-11-ink);
  font-family: var(--mu-11-font);
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

.mu-11 *,
.mu-11 *::before,
.mu-11 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .mu-11 {
    --mu-11-bg: #16130f;
    --mu-11-bg: oklch(18.5% 0.008 50);
    --mu-11-surface: #1f1b16;
    --mu-11-surface: oklch(23% 0.01 52);
    --mu-11-surface-2: #2a241d;
    --mu-11-surface-2: oklch(27.5% 0.013 55);
    --mu-11-ink: #f4efe9;
    --mu-11-ink: oklch(96% 0.008 60);
    --mu-11-ink-2: #b2a89d;
    --mu-11-ink-2: oklch(75% 0.014 58);
    --mu-11-line: #3c342b;
    --mu-11-line: oklch(33% 0.014 55);
    --mu-11-line-strong: #97897c;
    --mu-11-line-strong: oklch(64% 0.018 58);
    --mu-11-acc: #e8956a;
    --mu-11-acc: oklch(76% 0.12 45);
  }
}

.mu-11[data-theme="dark"],
.mu-11:has(.mu-11__theme-input:checked) {
  --mu-11-bg: #16130f;
  --mu-11-bg: oklch(18.5% 0.008 50);
  --mu-11-surface: #1f1b16;
  --mu-11-surface: oklch(23% 0.01 52);
  --mu-11-surface-2: #2a241d;
  --mu-11-surface-2: oklch(27.5% 0.013 55);
  --mu-11-ink: #f4efe9;
  --mu-11-ink: oklch(96% 0.008 60);
  --mu-11-ink-2: #b2a89d;
  --mu-11-ink-2: oklch(75% 0.014 58);
  --mu-11-line: #3c342b;
  --mu-11-line: oklch(33% 0.014 55);
  --mu-11-line-strong: #97897c;
  --mu-11-line-strong: oklch(64% 0.018 58);
  --mu-11-acc: #e8956a;
  --mu-11-acc: oklch(76% 0.12 45);
}

@media (prefers-color-scheme: light) {
  .mu-11:has(.mu-11__theme-input:checked) {
    --mu-11-bg: #16130f;
    --mu-11-bg: oklch(18.5% 0.008 50);
    --mu-11-surface: #1f1b16;
    --mu-11-surface: oklch(23% 0.01 52);
    --mu-11-surface-2: #2a241d;
    --mu-11-surface-2: oklch(27.5% 0.013 55);
    --mu-11-ink: #f4efe9;
    --mu-11-ink: oklch(96% 0.008 60);
    --mu-11-ink-2: #b2a89d;
    --mu-11-ink-2: oklch(75% 0.014 58);
    --mu-11-line: #3c342b;
    --mu-11-line: oklch(33% 0.014 55);
    --mu-11-line-strong: #97897c;
    --mu-11-line-strong: oklch(64% 0.018 58);
    --mu-11-acc: #e8956a;
    --mu-11-acc: oklch(76% 0.12 45);
  }
}

@media (prefers-color-scheme: dark) {
  .mu-11:has(.mu-11__theme-input:checked) {
    --mu-11-bg: #f2ece7;
    --mu-11-bg: oklch(93.5% 0.012 55);
    --mu-11-surface: #fbf7f4;
    --mu-11-surface: oklch(98% 0.007 60);
    --mu-11-surface-2: #e8e0d9;
    --mu-11-surface-2: oklch(90% 0.014 58);
    --mu-11-ink: #1e1a17;
    --mu-11-ink: oklch(21.5% 0.01 50);
    --mu-11-ink-2: #57504a;
    --mu-11-ink-2: oklch(45% 0.012 52);
    --mu-11-line: #d6cbc1;
    --mu-11-line: oklch(85% 0.016 58);
    --mu-11-line-strong: #7d726a;
    --mu-11-line-strong: oklch(54% 0.018 55);
    --mu-11-acc: #8c3b1c;
    --mu-11-acc: oklch(45% 0.13 40);
  }
}

.mu-11__sr {
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

.mu-11__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-11__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-11__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-11-line-strong);
  border-radius: 50%;
  background: var(--mu-11-surface);
  color: var(--mu-11-ink-2);
  cursor: pointer;
}

.mu-11__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-11__theme-input:focus-visible + .mu-11__theme-label {
  outline: 2px solid var(--mu-11-acc);
  outline-offset: 2px;
}

.mu-11__stage {
  max-inline-size: 70rem;
  margin-inline: auto;
  padding: 4rem 1.25rem 5rem;
  display: grid;
  gap: 2.75rem;
  grid-template-columns: minmax(0, 1fr);
}

.mu-11__block {
  display: grid;
  gap: 1rem;
  min-inline-size: 0;
}

.mu-11__block-head {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  justify-content: space-between;
  gap: 0.5rem 1rem;
}

.mu-11__sub {
  margin: 0;
  font-size: 0.8125rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.mu-11__count {
  margin: 0;
  font-family: var(--mu-11-mono);
  font-size: 0.75rem;
  color: var(--mu-11-ink-2);
}

.mu-11__scroller {
  min-inline-size: 0;
  overflow-x: auto;
}

.mu-11__table {
  inline-size: 100%;
  min-inline-size: 22rem;
  border-collapse: collapse;
  font-size: 0.875rem;
  background: var(--mu-11-surface);
}

.mu-11__table th,
.mu-11__table td {
  padding: 0.75rem 0.875rem;
  text-align: start;
  min-inline-size: 0;
}

.mu-11__table thead th {
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--mu-11-ink-2);
  white-space: nowrap;
}

.mu-11__table td:nth-child(n+2),
.mu-11__table thead th:nth-child(n+2) {
  text-align: end;
  font-variant-numeric: tabular-nums;
}

.mu-11__table tbody th {
  font-weight: 500;
}

.mu-11__table--ruled {
  border: 1px solid var(--mu-11-line-strong);
}

.mu-11__table--ruled th,
.mu-11__table--ruled td {
  border: 1px solid var(--mu-11-line-strong);
}

.mu-11__table--clean thead th {
  border-block-end: var(--mu-11-rule-strong);
}

.mu-11__table--clean tbody tr {
  transition: background-color 120ms ease;
}

.mu-11__table--clean tbody tr:hover {
  background: var(--mu-11-surface-2);
}

.mu-11__table--clean th,
.mu-11__table--clean td {
  border: 0;
  border-block-end: 1px solid var(--mu-11-rule);
}

.mu-11__cards {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr));
}

.mu-11__card {
  min-inline-size: 0;
  padding: var(--mu-11-pad);
  border-radius: 6px;
  border: var(--mu-11-card-border);
  background: var(--mu-11-surface);
  display: grid;
  gap: 0.5rem;
  align-content: start;
}

.mu-11__card p,
.mu-11__card h4 {
  margin: 0;
  min-inline-size: 0;
}

.mu-11__card-kicker {
  font-family: var(--mu-11-mono);
  font-size: 0.6875rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--mu-11-ink-2);
}

.mu-11__card-title {
  font-size: 1.0625rem;
  line-height: 1.25;
  letter-spacing: -0.014em;
  font-weight: 700;
}

.mu-11__card-text {
  font-size: 0.875rem;
  color: var(--mu-11-ink-2);
  text-wrap: pretty;
}

.mu-11__card-link {
  justify-self: start;
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--mu-11-acc);
  text-decoration: none;
  border-block-end: 1px solid transparent;
}

.mu-11__card-link:hover {
  border-block-end-color: currentColor;
}

.mu-11__card-link:focus-visible {
  outline: 2px solid var(--mu-11-acc);
  outline-offset: 3px;
  border-radius: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .mu-11__table--clean tbody tr {
    transition: none;
  }
}

@media (min-width: 56rem) {
  .mu-11__stage {
    padding-inline: 3rem;
  }

  .mu-11__card {
    padding: 1.75rem;
  }
}
```
