---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/modular-type-scale-with-a-ratio-variable/"
title: "Modular Type Scale with a Ratio Variable"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "One custom property holds the ratio and every step is derived from it with calc(), so the whole type system moves when you change a single number."
has_js: "false"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Modular Type Scale with a Ratio Variable
Source: https://codefronts.com/design-styles/css-minimalist-ui/modular-type-scale-with-a-ratio-variable/

One custom property holds the ratio and every step is derived from it with calc(), so the whole type system moves when you change a single number. The same specimen renders at 1.200, 1.250 and 1.333 side by side with every computed size printed, so you can see what the ratio actually changes before you commit to one.
## HTML
```html
<section class="mu-01" aria-labelledby="mu-01-title">
  <h2 class="mu-01__sr" id="mu-01-title">Modular type scale specimen</h2>
  <div class="mu-01__theme">
    <input class="mu-01__theme-input" type="checkbox" id="mu-01-theme">
    <label class="mu-01__theme-label" for="mu-01-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-01__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-01__stage">

    <div class="mu-01__strips">
      <article class="mu-01__strip" style="--mu-01-ratio: 1.2" aria-labelledby="mu-01-r1">
        <header class="mu-01__strip-head">
          <h3 class="mu-01__strip-title" id="mu-01-r1">1.200</h3>
          <p class="mu-01__strip-sub">Minor third &middot; dense UI</p>
        </header>
        <div class="mu-01__spec">
          <p class="mu-01__s4">Ranger</p>
          <p class="mu-01__s3">Monthly recurring revenue</p>
          <p class="mu-01__s2">Draft saved</p>
          <p class="mu-01__s1">A ratio this tight keeps a dense console readable, because adjacent steps stay close enough to sit in the same table row.</p>
          <p class="mu-01__s0">Continue to payment</p>
        </div>
        <dl class="mu-01__vals">
          <div><dt>s4</dt><dd>33.18px</dd></div>
          <div><dt>s3</dt><dd>27.65px</dd></div>
          <div><dt>s2</dt><dd>23.04px</dd></div>
          <div><dt>s1</dt><dd>19.20px</dd></div>
          <div><dt>s0</dt><dd>16.00px</dd></div>
        </dl>
      </article>

      <article class="mu-01__strip mu-01__strip--mid" style="--mu-01-ratio: 1.25" aria-labelledby="mu-01-r2">
        <header class="mu-01__strip-head">
          <h3 class="mu-01__strip-title" id="mu-01-r2">1.250</h3>
          <p class="mu-01__strip-sub">Major third &middot; product UI</p>
        </header>
        <div class="mu-01__spec">
          <p class="mu-01__s4">Ranger</p>
          <p class="mu-01__s3">Monthly recurring revenue</p>
          <p class="mu-01__s2">Draft saved</p>
          <p class="mu-01__s1">The working default for most product interfaces: distinguishable steps that still leave room for four or five levels of hierarchy.</p>
          <p class="mu-01__s0">Continue to payment</p>
        </div>
        <dl class="mu-01__vals">
          <div><dt>s4</dt><dd>39.06px</dd></div>
          <div><dt>s3</dt><dd>31.25px</dd></div>
          <div><dt>s2</dt><dd>25.00px</dd></div>
          <div><dt>s1</dt><dd>20.00px</dd></div>
          <div><dt>s0</dt><dd>16.00px</dd></div>
        </dl>
      </article>

      <article class="mu-01__strip" style="--mu-01-ratio: 1.333" aria-labelledby="mu-01-r3">
        <header class="mu-01__strip-head">
          <h3 class="mu-01__strip-title" id="mu-01-r3">1.333</h3>
          <p class="mu-01__strip-sub">Perfect fourth &middot; editorial</p>
        </header>
        <div class="mu-01__spec">
          <p class="mu-01__s4">Ranger</p>
          <p class="mu-01__s3">Monthly recurring revenue</p>
          <p class="mu-01__s2">Draft saved</p>
          <p class="mu-01__s1">Decisive on a landing page and hostile in a data table &mdash; by the fourth step the jump is 13px, which no dense interface can absorb.</p>
          <p class="mu-01__s0">Continue to payment</p>
        </div>
        <dl class="mu-01__vals">
          <div><dt>s4</dt><dd>50.53px</dd></div>
          <div><dt>s3</dt><dd>37.91px</dd></div>
          <div><dt>s2</dt><dd>28.44px</dd></div>
          <div><dt>s1</dt><dd>21.33px</dd></div>
          <div><dt>s0</dt><dd>16.00px</dd></div>
        </dl>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.mu-01 {
  --mu-01-ratio: 1.25;
  --mu-01-base: clamp(0.9375rem, 0.9rem + 0.25vw, 1rem);
  --mu-01-s0: var(--mu-01-base);
  --mu-01-s1: calc(var(--mu-01-s0) * var(--mu-01-ratio));
  --mu-01-s2: calc(var(--mu-01-s1) * var(--mu-01-ratio));
  --mu-01-s3: calc(var(--mu-01-s2) * var(--mu-01-ratio));
  --mu-01-s4: calc(var(--mu-01-s3) * var(--mu-01-ratio));
  --mu-01-unit: 0.5rem;
  --mu-01-font: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --mu-01-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --mu-01-bg: #eef0f2;
  --mu-01-bg: oklch(94.6% 0.005 240);
  --mu-01-surface: #ffffff;
  --mu-01-surface: oklch(100% 0 0);
  --mu-01-ink: #14181c;
  --mu-01-ink: oklch(19% 0.012 250);
  --mu-01-ink-2: #4c565f;
  --mu-01-ink-2: oklch(43% 0.018 250);
  --mu-01-line: #c9cfd5;
  --mu-01-line: oklch(84% 0.008 250);
  --mu-01-acc: #1d5cff;
  --mu-01-acc: oklch(52% 0.21 264);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-01-bg);
  color: var(--mu-01-ink);
  font-family: var(--mu-01-font);
  font-size: var(--mu-01-s0);
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

.mu-01 *,
.mu-01 *::before,
.mu-01 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .mu-01 {
    --mu-01-bg: #0f1215;
    --mu-01-bg: oklch(17% 0.008 250);
    --mu-01-surface: #171b1f;
    --mu-01-surface: oklch(22% 0.009 250);
    --mu-01-ink: #eef1f4;
    --mu-01-ink: oklch(95% 0.004 250);
    --mu-01-ink-2: #a3adb6;
    --mu-01-ink-2: oklch(74% 0.012 250);
    --mu-01-line: #333c44;
    --mu-01-line: oklch(33% 0.012 250);
    --mu-01-acc: #7fa6ff;
    --mu-01-acc: oklch(76% 0.14 264);
  }
}

.mu-01[data-theme="dark"],
.mu-01:has(.mu-01__theme-input:checked) {
  --mu-01-bg: #0f1215;
  --mu-01-bg: oklch(17% 0.008 250);
  --mu-01-surface: #171b1f;
  --mu-01-surface: oklch(22% 0.009 250);
  --mu-01-ink: #eef1f4;
  --mu-01-ink: oklch(95% 0.004 250);
  --mu-01-ink-2: #a3adb6;
  --mu-01-ink-2: oklch(74% 0.012 250);
  --mu-01-line: #333c44;
  --mu-01-line: oklch(33% 0.012 250);
  --mu-01-acc: #7fa6ff;
  --mu-01-acc: oklch(76% 0.14 264);
}

@media (prefers-color-scheme: light) {
  .mu-01:has(.mu-01__theme-input:checked) {
    --mu-01-bg: #0f1215;
    --mu-01-bg: oklch(17% 0.008 250);
    --mu-01-surface: #171b1f;
    --mu-01-surface: oklch(22% 0.009 250);
    --mu-01-ink: #eef1f4;
    --mu-01-ink: oklch(95% 0.004 250);
    --mu-01-ink-2: #a3adb6;
    --mu-01-ink-2: oklch(74% 0.012 250);
    --mu-01-line: #333c44;
    --mu-01-line: oklch(33% 0.012 250);
    --mu-01-acc: #7fa6ff;
    --mu-01-acc: oklch(76% 0.14 264);
  }
}

@media (prefers-color-scheme: dark) {
  .mu-01:has(.mu-01__theme-input:checked) {
    --mu-01-bg: #eef0f2;
    --mu-01-bg: oklch(94.6% 0.005 240);
    --mu-01-surface: #ffffff;
    --mu-01-surface: oklch(100% 0 0);
    --mu-01-ink: #14181c;
    --mu-01-ink: oklch(19% 0.012 250);
    --mu-01-ink-2: #4c565f;
    --mu-01-ink-2: oklch(43% 0.018 250);
    --mu-01-line: #c9cfd5;
    --mu-01-line: oklch(84% 0.008 250);
    --mu-01-acc: #1d5cff;
    --mu-01-acc: oklch(52% 0.21 264);
  }
}

.mu-01__sr {
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

.mu-01__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-01__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-01__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-01-line);
  border-radius: 50%;
  background: var(--mu-01-surface);
  color: var(--mu-01-ink-2);
  cursor: pointer;
}

.mu-01__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-01__theme-input:focus-visible + .mu-01__theme-label {
  outline: 2px solid var(--mu-01-acc);
  outline-offset: 2px;
}

.mu-01__stage {
  max-inline-size: 78rem;
  margin-inline: auto;
  padding: calc(var(--mu-01-unit) * 7) calc(var(--mu-01-unit) * 3) calc(var(--mu-01-unit) * 9);
  display: grid;
  gap: calc(var(--mu-01-unit) * 6);
  grid-template-columns: minmax(0, 1fr);
}

.mu-01__strips {
  display: grid;
  gap: calc(var(--mu-01-unit) * 3);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
}

.mu-01__strip {
  min-inline-size: 0;
  background: var(--mu-01-surface);
  border: 1px solid var(--mu-01-line);
  border-radius: 4px;
  padding: calc(var(--mu-01-unit) * 3);
  display: grid;
  gap: calc(var(--mu-01-unit) * 3);
  align-content: start;
}

.mu-01__strip--mid {
  border-color: var(--mu-01-acc);
}

.mu-01__strip-head {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: calc(var(--mu-01-unit) * 1.5);
  padding-block-end: calc(var(--mu-01-unit) * 2);
  border-block-end: 1px solid var(--mu-01-line);
}

.mu-01__strip-title {
  margin: 0;
  font-family: var(--mu-01-mono);
  font-size: 1.375rem;
  font-weight: 500;
  letter-spacing: -0.01em;
  min-inline-size: 0;
}

.mu-01__strip-sub {
  margin: 0;
  font-size: 0.75rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--mu-01-ink-2);
  min-inline-size: 0;
}

.mu-01__spec {
  display: grid;
  gap: calc(var(--mu-01-unit) * 1.5);
  min-inline-size: 0;
}

.mu-01__spec p {
  margin: 0;
  min-inline-size: 0;
  overflow-wrap: break-word;
}

.mu-01__s4 {
  font-size: var(--mu-01-s4);
  line-height: 1.05;
  letter-spacing: -0.028em;
  font-weight: 600;
}

.mu-01__s3 {
  font-size: var(--mu-01-s3);
  line-height: 1.15;
  letter-spacing: -0.018em;
  font-weight: 600;
}

.mu-01__s2 {
  font-size: var(--mu-01-s2);
  line-height: 1.25;
  font-weight: 500;
}

.mu-01__s1 {
  font-size: var(--mu-01-s1);
  line-height: 1.5;
  color: var(--mu-01-ink-2);
  max-inline-size: 34ch;
  text-wrap: pretty;
}

.mu-01__s0 {
  font-size: var(--mu-01-s0);
  line-height: 1.5;
  font-weight: 500;
}

.mu-01__vals {
  margin: 0;
  display: grid;
  gap: 2px;
  padding-block-start: calc(var(--mu-01-unit) * 2);
  border-block-start: 1px solid var(--mu-01-line);
  font-family: var(--mu-01-mono);
  font-size: 0.75rem;
  font-variant-numeric: tabular-nums;
  color: var(--mu-01-ink-2);
}

.mu-01__vals > div {
  display: flex;
  justify-content: space-between;
  gap: var(--mu-01-unit);
}

.mu-01__vals dt {
  margin: 0;
}

.mu-01__vals dd {
  margin: 0;
  color: var(--mu-01-ink);
}

@media (min-width: 64rem) {
  .mu-01__stage {
    padding-inline: calc(var(--mu-01-unit) * 6);
  }
}
```
