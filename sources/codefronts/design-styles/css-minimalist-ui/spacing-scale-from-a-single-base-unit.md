---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/spacing-scale-from-a-single-base-unit/"
title: "Spacing Scale from a Single Base Unit"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "One base unit, six derived steps, and a rule that no component invents an off-scale value."
has_js: "false"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Spacing Scale from a Single Base Unit
Source: https://codefronts.com/design-styles/css-minimalist-ui/spacing-scale-from-a-single-base-unit/

One base unit, six derived steps, and a rule that no component invents an off-scale value. A measured ruler prints every step, then the same card is built twice &mdash; once from the scale and once from hand-picked pixels &mdash; with the values labelled on both so the drift is visible rather than asserted.
## HTML
```html
<section class="mu-05" aria-labelledby="mu-05-title">
  <h2 class="mu-05__sr" id="mu-05-title">Spacing scale reference</h2>
  <div class="mu-05__theme">
    <input class="mu-05__theme-input" type="checkbox" id="mu-05-theme">
    <label class="mu-05__theme-label" for="mu-05-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-05__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-05__stage">

    <section class="mu-05__ruler-wrap" aria-labelledby="mu-05-ruler-h">
      <h3 class="mu-05__sub" id="mu-05-ruler-h">The scale</h3>
      <ul class="mu-05__ruler">
        <li class="mu-05__tick" style="--mu-05-n: 1"><span class="mu-05__bar"></span><b>s1</b><i>8px</i></li>
        <li class="mu-05__tick" style="--mu-05-n: 2"><span class="mu-05__bar"></span><b>s2</b><i>16px</i></li>
        <li class="mu-05__tick" style="--mu-05-n: 3"><span class="mu-05__bar"></span><b>s3</b><i>24px</i></li>
        <li class="mu-05__tick" style="--mu-05-n: 4"><span class="mu-05__bar"></span><b>s4</b><i>32px</i></li>
        <li class="mu-05__tick" style="--mu-05-n: 6"><span class="mu-05__bar"></span><b>s5</b><i>48px</i></li>
        <li class="mu-05__tick" style="--mu-05-n: 8"><span class="mu-05__bar"></span><b>s6</b><i>64px</i></li>
      </ul>
    </section>

    <div class="mu-05__pair">
      <article class="mu-05__col" aria-labelledby="mu-05-bad-h">
        <div class="mu-05__col-head">
          <h3 class="mu-05__sub" id="mu-05-bad-h">Arbitrary values</h3>
          <p class="mu-05__col-note">13 &middot; 17 &middot; 22 &middot; 9 &middot; 31</p>
        </div>
        <div class="mu-05__card mu-05__card--bad">
          <p class="mu-05__card-kicker">Deployment</p>
          <h4 class="mu-05__card-title">Orbit API, region eu-west</h4>
          <p class="mu-05__card-body">Rolled out to 34 of 34 instances. No error budget consumed in the last hour.</p>
          <ul class="mu-05__card-meta">
            <li>Build 4c19f0</li>
            <li>Jordan Lee</li>
            <li>11 min ago</li>
          </ul>
          <div class="mu-05__card-actions">
            <button class="mu-05__btn mu-05__btn--primary" type="button">Promote to production</button>
            <button class="mu-05__btn" type="button">Roll back</button>
          </div>
        </div>
      </article>

      <article class="mu-05__col" aria-labelledby="mu-05-good-h">
        <div class="mu-05__col-head">
          <h3 class="mu-05__sub" id="mu-05-good-h">8px scale</h3>
          <p class="mu-05__col-note">8 &middot; 16 &middot; 24 &middot; 32</p>
        </div>
        <div class="mu-05__card mu-05__card--good">
          <p class="mu-05__card-kicker">Deployment</p>
          <h4 class="mu-05__card-title">Orbit API, region eu-west</h4>
          <p class="mu-05__card-body">Rolled out to 34 of 34 instances. No error budget consumed in the last hour.</p>
          <ul class="mu-05__card-meta">
            <li>Build 4c19f0</li>
            <li>Jordan Lee</li>
            <li>11 min ago</li>
          </ul>
          <div class="mu-05__card-actions">
            <button class="mu-05__btn mu-05__btn--primary" type="button">Promote to production</button>
            <button class="mu-05__btn" type="button">Roll back</button>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.mu-05 {
  --mu-05-unit: 0.5rem;
  --mu-05-s1: calc(var(--mu-05-unit) * 1);
  --mu-05-s2: calc(var(--mu-05-unit) * 2);
  --mu-05-s3: calc(var(--mu-05-unit) * 3);
  --mu-05-s4: calc(var(--mu-05-unit) * 4);
  --mu-05-s5: calc(var(--mu-05-unit) * 6);
  --mu-05-s6: calc(var(--mu-05-unit) * 8);
  --mu-05-card-pad: var(--mu-05-s4);
  --mu-05-font: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --mu-05-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --mu-05-bg: #eef1ea;
  --mu-05-bg: oklch(94.5% 0.014 140);
  --mu-05-surface: #fbfcf9;
  --mu-05-surface: oklch(98.8% 0.006 140);
  --mu-05-ink: #161a15;
  --mu-05-ink: oklch(19.5% 0.012 140);
  --mu-05-ink-2: #4e564c;
  --mu-05-ink-2: oklch(44% 0.016 140);
  --mu-05-line: #ccd3c6;
  --mu-05-line: oklch(85% 0.018 140);
  --mu-05-acc: #1f6b3f;
  --mu-05-acc: oklch(46% 0.11 155);
  --mu-05-acc-ink: #ffffff;
  --mu-05-acc-ink: oklch(100% 0 0);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-05-bg);
  color: var(--mu-05-ink);
  font-family: var(--mu-05-ui);
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

.mu-05 *,
.mu-05 *::before,
.mu-05 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .mu-05 {
    --mu-05-bg: #101310;
    --mu-05-bg: oklch(17.5% 0.008 140);
    --mu-05-surface: #181d18;
    --mu-05-surface: oklch(22.5% 0.01 140);
    --mu-05-ink: #eef2ec;
    --mu-05-ink: oklch(95.5% 0.008 140);
    --mu-05-ink-2: #a5ad9f;
    --mu-05-ink-2: oklch(74% 0.014 140);
    --mu-05-line: #333a31;
    --mu-05-line: oklch(33% 0.014 140);
    --mu-05-acc: #6ed49a;
    --mu-05-acc: oklch(82% 0.13 155);
    --mu-05-acc-ink: #0b1a0f;
    --mu-05-acc-ink: oklch(16% 0.02 155);
  }
}

.mu-05[data-theme="dark"],
.mu-05:has(.mu-05__theme-input:checked) {
  --mu-05-bg: #101310;
  --mu-05-bg: oklch(17.5% 0.008 140);
  --mu-05-surface: #181d18;
  --mu-05-surface: oklch(22.5% 0.01 140);
  --mu-05-ink: #eef2ec;
  --mu-05-ink: oklch(95.5% 0.008 140);
  --mu-05-ink-2: #a5ad9f;
  --mu-05-ink-2: oklch(74% 0.014 140);
  --mu-05-line: #333a31;
  --mu-05-line: oklch(33% 0.014 140);
  --mu-05-acc: #6ed49a;
  --mu-05-acc: oklch(82% 0.13 155);
  --mu-05-acc-ink: #0b1a0f;
  --mu-05-acc-ink: oklch(16% 0.02 155);
}

@media (prefers-color-scheme: light) {
  .mu-05:has(.mu-05__theme-input:checked) {
    --mu-05-bg: #101310;
    --mu-05-bg: oklch(17.5% 0.008 140);
    --mu-05-surface: #181d18;
    --mu-05-surface: oklch(22.5% 0.01 140);
    --mu-05-ink: #eef2ec;
    --mu-05-ink: oklch(95.5% 0.008 140);
    --mu-05-ink-2: #a5ad9f;
    --mu-05-ink-2: oklch(74% 0.014 140);
    --mu-05-line: #333a31;
    --mu-05-line: oklch(33% 0.014 140);
    --mu-05-acc: #6ed49a;
    --mu-05-acc: oklch(82% 0.13 155);
    --mu-05-acc-ink: #0b1a0f;
    --mu-05-acc-ink: oklch(16% 0.02 155);
  }
}

@media (prefers-color-scheme: dark) {
  .mu-05:has(.mu-05__theme-input:checked) {
    --mu-05-bg: #eef1ea;
    --mu-05-bg: oklch(94.5% 0.014 140);
    --mu-05-surface: #fbfcf9;
    --mu-05-surface: oklch(98.8% 0.006 140);
    --mu-05-ink: #161a15;
    --mu-05-ink: oklch(19.5% 0.012 140);
    --mu-05-ink-2: #4e564c;
    --mu-05-ink-2: oklch(44% 0.016 140);
    --mu-05-line: #ccd3c6;
    --mu-05-line: oklch(85% 0.018 140);
    --mu-05-acc: #1f6b3f;
    --mu-05-acc: oklch(46% 0.11 155);
    --mu-05-acc-ink: #ffffff;
    --mu-05-acc-ink: oklch(100% 0 0);
  }
}

.mu-05__sr {
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

.mu-05__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-05__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-05__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-05-line);
  border-radius: 4px;
  background: var(--mu-05-surface);
  color: var(--mu-05-ink-2);
  cursor: pointer;
}

.mu-05__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-05__theme-input:focus-visible + .mu-05__theme-label {
  outline: 2px solid var(--mu-05-acc);
  outline-offset: 2px;
}

.mu-05__stage {
  max-inline-size: 74rem;
  margin-inline: auto;
  padding: var(--mu-05-s6) var(--mu-05-s3) var(--mu-05-s6);
  display: grid;
  gap: var(--mu-05-s5);
  grid-template-columns: minmax(0, 1fr);
}

.mu-05__sub {
  margin: 0;
  font-family: var(--mu-05-font);
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--mu-05-ink);
}

.mu-05__ruler-wrap {
  display: grid;
  gap: var(--mu-05-s3);
  min-inline-size: 0;
}

.mu-05__ruler {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: var(--mu-05-s1);
  min-inline-size: 0;
}

.mu-05__tick {
  display: grid;
  align-items: center;
  gap: var(--mu-05-s2);
  grid-template-columns: 2.25rem 3.5rem minmax(0, 1fr);
  font-family: var(--mu-05-font);
  font-size: 0.75rem;
  font-variant-numeric: tabular-nums;
  padding-block: 2px;
  min-inline-size: 0;
}

.mu-05__tick b {
  order: 1;
  font-weight: 500;
  color: var(--mu-05-ink);
}

.mu-05__tick i {
  order: 2;
  font-style: normal;
  color: var(--mu-05-ink-2);
}

.mu-05__bar {
  order: 3;
  display: block;
  block-size: 10px;
  inline-size: calc(var(--mu-05-unit) * var(--mu-05-n));
  background: var(--mu-05-acc);
  border-radius: 1px;
}

.mu-05__ruler-note code,
.mu-05__col-note code {
  font-family: var(--mu-05-font);
  font-size: 0.9em;
}

.mu-05__pair {
  display: grid;
  gap: var(--mu-05-s3);
  grid-template-columns: minmax(0, 1fr);
}

.mu-05__col {
  min-inline-size: 0;
  display: grid;
  gap: var(--mu-05-s2);
  align-content: start;
}

.mu-05__col-head {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  justify-content: space-between;
  gap: var(--mu-05-s1);
  padding-block-end: var(--mu-05-s1);
  border-block-end: 1px solid var(--mu-05-line);
}

.mu-05__col-note {
  margin: 0;
  font-family: var(--mu-05-font);
  font-size: 0.75rem;
  color: var(--mu-05-ink-2);
  font-variant-numeric: tabular-nums;
}

.mu-05__card {
  min-inline-size: 0;
  background: var(--mu-05-surface);
  border: 1px solid var(--mu-05-line);
  border-radius: 6px;
}

.mu-05__card p,
.mu-05__card h4 {
  margin: 0;
  min-inline-size: 0;
}

.mu-05__card-kicker {
  font-family: var(--mu-05-font);
  font-size: 0.6875rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--mu-05-ink-2);
}

.mu-05__card-title {
  font-size: 1.25rem;
  line-height: 1.2;
  letter-spacing: -0.018em;
  font-weight: 600;
}

.mu-05__card-body {
  font-size: 0.9375rem;
  color: var(--mu-05-ink-2);
  max-inline-size: 46ch;
  text-wrap: pretty;
}

.mu-05__card-meta {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  font-family: var(--mu-05-font);
  font-size: 0.75rem;
  color: var(--mu-05-ink-2);
}

.mu-05__card-actions {
  display: flex;
  flex-wrap: wrap;
}

.mu-05__btn {
  min-block-size: 44px;
  min-inline-size: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding-inline: var(--mu-05-s2);
  border-radius: 4px;
  border: 1px solid var(--mu-05-line);
  background: transparent;
  color: var(--mu-05-ink);
  font: inherit;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: border-color 150ms ease;
}

.mu-05__btn:hover {
  border-color: var(--mu-05-ink);
}

.mu-05__btn:focus-visible {
  outline: 2px solid var(--mu-05-acc);
  outline-offset: 2px;
}

.mu-05__btn--primary {
  background: var(--mu-05-acc);
  border-color: var(--mu-05-acc);
  color: var(--mu-05-acc-ink);
}

.mu-05__card--bad {
  padding: 17px 13px 22px;
}

.mu-05__card--bad .mu-05__card-kicker {
  margin-block-end: 9px;
}

.mu-05__card--bad .mu-05__card-title {
  margin-block-end: 11px;
}

.mu-05__card--bad .mu-05__card-body {
  margin-block-end: 22px;
}

.mu-05__card--bad .mu-05__card-meta {
  gap: 6px 13px;
  margin-block-end: 31px;
}

.mu-05__card--bad .mu-05__card-actions {
  gap: 9px;
}

.mu-05__card--good {
  padding: var(--mu-05-card-pad);
  display: grid;
  gap: var(--mu-05-s2);
  align-content: start;
}

.mu-05__card--good .mu-05__card-meta {
  gap: var(--mu-05-s1) var(--mu-05-s2);
}

.mu-05__card--good .mu-05__card-actions {
  gap: var(--mu-05-s1);
  margin-block-start: var(--mu-05-s1);
}

@media (prefers-reduced-motion: reduce) {
  .mu-05__btn {
    transition: none;
  }
}

@media (min-width: 52rem) {
  .mu-05__pair {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .mu-05__stage {
    padding-inline: var(--mu-05-s5);
  }
}
```
