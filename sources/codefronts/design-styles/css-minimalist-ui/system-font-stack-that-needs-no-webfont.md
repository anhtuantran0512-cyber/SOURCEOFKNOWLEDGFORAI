---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/system-font-stack-that-needs-no-webfont/"
title: "System Font Stack That Needs No Webfont"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "The full modern system stack, row by row, with what each entry actually catches and why system-ui alone is not enough."
has_js: "false"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: System Font Stack That Needs No Webfont
Source: https://codefronts.com/design-styles/css-minimalist-ui/system-font-stack-that-needs-no-webfont/

The full modern system stack, row by row, with what each entry actually catches and why system-ui alone is not enough. Four specimens &mdash; sans, serif, monospace and rounded &mdash; render in the native UI face with a metric-compatible fallback chain, so a fallback swap changes the shape of the letters and not the shape of the layout.
## HTML
```html
<section class="mu-03" aria-labelledby="mu-03-title">
  <h2 class="mu-03__sr" id="mu-03-title">System font stack specimens</h2>
  <div class="mu-03__theme">
    <input class="mu-03__theme-input" type="checkbox" id="mu-03-theme">
    <label class="mu-03__theme-label" for="mu-03-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-03__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-03__stage">

    <div class="mu-03__rows">
      <article class="mu-03__row mu-03__row--sans" aria-labelledby="mu-03-h1">
        <div class="mu-03__row-head">
          <h3 class="mu-03__row-title" id="mu-03-h1">Interface sans</h3>
          <p class="mu-03__row-use">Buttons, labels, dense product UI</p>
        </div>
        <p class="mu-03__specimen">Continue to payment</p>
        <ol class="mu-03__ladder">
          <li><code>system-ui</code><span>Resolves the OS UI face</span></li>
          <li><code>-apple-system</code><span>Safari before 11</span></li>
          <li><code>&quot;Segoe UI&quot;</code><span>Windows, explicit</span></li>
          <li><code>Roboto</code><span>Android, Chrome OS</span></li>
          <li><code>&quot;Helvetica Neue&quot;, Arial</code><span>Metric-compatible pair</span></li>
          <li><code>sans-serif</code><span>Last resort</span></li>
        </ol>
      </article>

      <article class="mu-03__row mu-03__row--serif" aria-labelledby="mu-03-h2">
        <div class="mu-03__row-head">
          <h3 class="mu-03__row-title" id="mu-03-h2">Reading serif</h3>
          <p class="mu-03__row-use">Long-form prose, article columns</p>
        </div>
        <p class="mu-03__specimen">A calm measure, set in Georgia</p>
        <ol class="mu-03__ladder">
          <li><code>ui-serif</code><span>Apple platforms</span></li>
          <li><code>Georgia</code><span>Everywhere since 1996</span></li>
          <li><code>&quot;Iowan Old Style&quot;</code><span>iOS reading face</span></li>
          <li><code>&quot;Palatino Linotype&quot;, Palatino</code><span>Metric-compatible pair</span></li>
          <li><code>serif</code><span>Last resort</span></li>
        </ol>
      </article>

      <article class="mu-03__row mu-03__row--mono" aria-labelledby="mu-03-h3">
        <div class="mu-03__row-head">
          <h3 class="mu-03__row-title" id="mu-03-h3">Data monospace</h3>
          <p class="mu-03__row-use">Figures, code, log output</p>
        </div>
        <p class="mu-03__specimen">1,284.06 &middot; 99.982% &middot; 0x1F</p>
        <ol class="mu-03__ladder">
          <li><code>ui-monospace</code><span>Apple platforms</span></li>
          <li><code>SFMono-Regular</code><span>macOS, older Safari</span></li>
          <li><code>Menlo, Consolas</code><span>macOS / Windows pair</span></li>
          <li><code>&quot;Liberation Mono&quot;</code><span>Linux, Android</span></li>
          <li><code>monospace</code><span>Last resort</span></li>
        </ol>
      </article>

      <article class="mu-03__row mu-03__row--round" aria-labelledby="mu-03-h4">
        <div class="mu-03__row-head">
          <h3 class="mu-03__row-title" id="mu-03-h4">Rounded, with a caveat</h3>
          <p class="mu-03__row-use">Consumer apps &mdash; degrades to sans</p>
        </div>
        <p class="mu-03__specimen">Draft saved</p>
        <ol class="mu-03__ladder">
          <li><code>ui-rounded</code><span>Apple only &mdash; falls through elsewhere</span></li>
          <li><code>&quot;SF Pro Rounded&quot;</code><span>macOS, iOS</span></li>
          <li><code>&quot;Hiragino Maru Gothic ProN&quot;</code><span>Japanese rounded</span></li>
          <li><code>system-ui</code><span>The realistic result on Windows</span></li>
          <li><code>sans-serif</code><span>Last resort</span></li>
        </ol>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.mu-03 {
  --mu-03-unit: 0.5rem;
  --mu-03-step: 3%;
  --mu-03-sans: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --mu-03-serif: ui-serif, Georgia, "Iowan Old Style", "Palatino Linotype", Palatino, serif;
  --mu-03-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --mu-03-round: ui-rounded, "SF Pro Rounded", "Hiragino Maru Gothic ProN", system-ui, sans-serif;
  --mu-03-bg: #f7f4ee;
  --mu-03-bg: oklch(96.5% 0.008 85);
  --mu-03-surface: #fffdf9;
  --mu-03-surface: oklch(99% 0.005 85);
  --mu-03-surface-2: #f0ece3;
  --mu-03-surface-2: oklch(93.5% 0.011 85);
  --mu-03-ink: #1b1915;
  --mu-03-ink: oklch(20% 0.008 70);
  --mu-03-ink-2: #575249;
  --mu-03-ink-2: oklch(45% 0.012 75);
  --mu-03-line: #d8d2c6;
  --mu-03-line: oklch(86% 0.013 82);
  --mu-03-acc: #8a4b12;
  --mu-03-acc: oklch(46% 0.13 55);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-03-bg);
  color: var(--mu-03-ink);
  font-family: var(--mu-03-sans);
  font-synthesis: none;
  font-optical-sizing: auto;
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

.mu-03 *,
.mu-03 *::before,
.mu-03 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .mu-03 {
    --mu-03-bg: #14120f;
    --mu-03-bg: oklch(18% 0.008 70);
    --mu-03-surface: #1d1a16;
    --mu-03-surface: oklch(23% 0.009 70);
    --mu-03-surface-2: #262218;
    --mu-03-surface-2: oklch(27% 0.012 75);
    --mu-03-ink: #f3efe7;
    --mu-03-ink: oklch(95.5% 0.008 85);
    --mu-03-ink-2: #b0a998;
    --mu-03-ink-2: oklch(76% 0.016 82);
    --mu-03-line: #3b3529;
    --mu-03-line: oklch(33% 0.014 78);
    --mu-03-acc: #e8a86a;
    --mu-03-acc: oklch(79% 0.11 60);
  }
}

.mu-03[data-theme="dark"],
.mu-03:has(.mu-03__theme-input:checked) {
  --mu-03-bg: #14120f;
  --mu-03-bg: oklch(18% 0.008 70);
  --mu-03-surface: #1d1a16;
  --mu-03-surface: oklch(23% 0.009 70);
  --mu-03-surface-2: #262218;
  --mu-03-surface-2: oklch(27% 0.012 75);
  --mu-03-ink: #f3efe7;
  --mu-03-ink: oklch(95.5% 0.008 85);
  --mu-03-ink-2: #b0a998;
  --mu-03-ink-2: oklch(76% 0.016 82);
  --mu-03-line: #3b3529;
  --mu-03-line: oklch(33% 0.014 78);
  --mu-03-acc: #e8a86a;
  --mu-03-acc: oklch(79% 0.11 60);
}

@media (prefers-color-scheme: light) {
  .mu-03:has(.mu-03__theme-input:checked) {
    --mu-03-bg: #14120f;
    --mu-03-bg: oklch(18% 0.008 70);
    --mu-03-surface: #1d1a16;
    --mu-03-surface: oklch(23% 0.009 70);
    --mu-03-surface-2: #262218;
    --mu-03-surface-2: oklch(27% 0.012 75);
    --mu-03-ink: #f3efe7;
    --mu-03-ink: oklch(95.5% 0.008 85);
    --mu-03-ink-2: #b0a998;
    --mu-03-ink-2: oklch(76% 0.016 82);
    --mu-03-line: #3b3529;
    --mu-03-line: oklch(33% 0.014 78);
    --mu-03-acc: #e8a86a;
    --mu-03-acc: oklch(79% 0.11 60);
  }
}

@media (prefers-color-scheme: dark) {
  .mu-03:has(.mu-03__theme-input:checked) {
    --mu-03-bg: #f7f4ee;
    --mu-03-bg: oklch(96.5% 0.008 85);
    --mu-03-surface: #fffdf9;
    --mu-03-surface: oklch(99% 0.005 85);
    --mu-03-surface-2: #f0ece3;
    --mu-03-surface-2: oklch(93.5% 0.011 85);
    --mu-03-ink: #1b1915;
    --mu-03-ink: oklch(20% 0.008 70);
    --mu-03-ink-2: #575249;
    --mu-03-ink-2: oklch(45% 0.012 75);
    --mu-03-line: #d8d2c6;
    --mu-03-line: oklch(86% 0.013 82);
    --mu-03-acc: #8a4b12;
    --mu-03-acc: oklch(46% 0.13 55);
  }
}

.mu-03__sr {
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

.mu-03__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-03__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-03__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-03-line);
  border-radius: 50%;
  background: var(--mu-03-surface);
  color: var(--mu-03-ink-2);
  cursor: pointer;
}

.mu-03__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-03__theme-input:focus-visible + .mu-03__theme-label {
  outline: 2px solid var(--mu-03-acc);
  outline-offset: 2px;
}

.mu-03__stage {
  max-inline-size: 76rem;
  margin-inline: auto;
  padding: calc(var(--mu-03-unit) * 8) calc(var(--mu-03-unit) * 3) calc(var(--mu-03-unit) * 10);
  display: grid;
  gap: calc(var(--mu-03-unit) * 6);
  grid-template-columns: minmax(0, 1fr);
}

.mu-03__rows {
  display: grid;
  gap: calc(var(--mu-03-unit) * 3);
  grid-template-columns: minmax(0, 1fr);
}

.mu-03__row {
  min-inline-size: 0;
  display: grid;
  gap: calc(var(--mu-03-unit) * 2.5);
  grid-template-columns: minmax(0, 1fr);
  padding: calc(var(--mu-03-unit) * 3.5);
  border-radius: 6px;
  background: var(--mu-03-surface);
  border: 1px solid var(--mu-03-line);
}

.mu-03__row:nth-child(even) {
  background: var(--mu-03-surface-2);
}

.mu-03__row-head {
  min-inline-size: 0;
  display: grid;
  gap: 2px;
}

.mu-03__row-title {
  margin: 0;
  font-family: var(--mu-03-mono);
  font-size: 0.8125rem;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--mu-03-acc);
}

.mu-03__row-use {
  margin: 0;
  font-size: 0.8125rem;
  color: var(--mu-03-ink-2);
}

.mu-03__specimen {
  margin: 0;
  min-inline-size: 0;
  overflow-wrap: break-word;
  font-size: clamp(1.5rem, 1.1rem + 2.6vw, 2.75rem);
  line-height: 1.1;
  letter-spacing: -0.022em;
  font-weight: 500;
}

.mu-03__row--sans .mu-03__specimen {
  font-family: var(--mu-03-sans);
}

.mu-03__row--serif .mu-03__specimen {
  font-family: var(--mu-03-serif);
  letter-spacing: -0.012em;
}

.mu-03__row--mono .mu-03__specimen {
  font-family: var(--mu-03-mono);
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.01em;
}

.mu-03__row--round .mu-03__specimen {
  font-family: var(--mu-03-round);
}

.mu-03__ladder {
  margin: 0;
  padding: 0;
  list-style: none;
  counter-reset: mu-03-step;
  display: grid;
  gap: 0;
  min-inline-size: 0;
  border-block-start: 1px solid var(--mu-03-line);
}

.mu-03__ladder li {
  counter-increment: mu-03-step;
  min-inline-size: 0;
  display: grid;
  gap: 2px calc(var(--mu-03-unit) * 2);
  grid-template-columns: 1.5rem minmax(0, 1fr);
  padding-block: calc(var(--mu-03-unit) * 1.25);
  border-block-end: 1px solid var(--mu-03-line);
  font-size: 0.875rem;
}

.mu-03__ladder li::before {
  content: counter(mu-03-step);
  grid-row: span 2;
  font-family: var(--mu-03-mono);
  font-size: 0.75rem;
  color: var(--mu-03-ink-2);
  font-variant-numeric: tabular-nums;
  padding-block-start: 2px;
}

.mu-03__ladder code {
  font-family: var(--mu-03-mono);
  font-size: 0.8125rem;
  min-inline-size: 0;
  overflow-wrap: break-word;
}

.mu-03__ladder span {
  font-size: 0.8125rem;
  color: var(--mu-03-ink-2);
  min-inline-size: 0;
}

@media (min-width: 56rem) {
  .mu-03__rows {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .mu-03__row {
    grid-template-columns: minmax(0, 1fr);
    align-content: start;
  }

  .mu-03__stage {
    padding-inline: calc(var(--mu-03-unit) * 6);
  }
}
```
