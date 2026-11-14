---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/axiom-dashboard/"
title: "Minimalist Dashboard Card and Metric"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "One metric card &mdash; value, label, delta and sparkline &mdash; where the hierarchy between the number and its label comes from scale and weight, not colour."
has_js: "false"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Dashboard Card and Metric
Source: https://codefronts.com/design-styles/css-minimalist-ui/axiom-dashboard/

One metric card &mdash; value, label, delta and sparkline &mdash; where the hierarchy between the number and its label comes from scale and weight, not colour. A component study rather than a dashboard layout, so it drops into whatever grid you already have &mdash; and the delta carries a glyph and a word alongside its hue, so the direction survives for a reader who cannot resolve the colour.
## HTML
```html
<section class="mu-15" aria-labelledby="mu-15-title">
  <h2 class="mu-15__sr" id="mu-15-title">Account metrics</h2>
  <div class="mu-15__theme">
    <input class="mu-15__theme-input" type="checkbox" id="mu-15-theme">
    <label class="mu-15__theme-label" for="mu-15-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-15__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-15__stage">

    <div class="mu-15__grid">
      <article class="mu-15__card" aria-labelledby="mu-15-m1">
        <header class="mu-15__card-head">
          <h3 class="mu-15__label" id="mu-15-m1">Monthly recurring revenue</h3>
          <p class="mu-15__scope">Meridian &middot; all regions</p>
        </header>
        <p class="mu-15__value">$281,440</p>
        <p class="mu-15__delta mu-15__delta--up">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 19V5m0 0-6 6m6-6 6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
          <b>4.2%</b> <span>vs last month</span>
        </p>
        <div class="mu-15__spark">
          <svg viewBox="0 0 240 64" preserveAspectRatio="none" role="img" aria-label="Twelve-month trend, rising from 214,000 to 281,440">
            <path d="M0 52 20 49 40 51 60 44 80 46 100 38 120 34 140 36 160 27 180 22 200 24 220 14 240 10" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" vector-effect="non-scaling-stroke"/>
          </svg>
        </div>
        <footer class="mu-15__card-foot">
          <p class="mu-15__foot-note">Updated 6 min ago</p>
          <a class="mu-15__link" href="#mu-15-title">Full report</a>
        </footer>
      </article>

      <article class="mu-15__card" aria-labelledby="mu-15-m2">
        <header class="mu-15__card-head">
          <h3 class="mu-15__label" id="mu-15-m2">Net revenue retention</h3>
          <p class="mu-15__scope">Rolling 12 months</p>
        </header>
        <p class="mu-15__value">104.8%</p>
        <p class="mu-15__delta mu-15__delta--down">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 5v14m0 0 6-6m-6 6-6-6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
          <b>0.6pt</b> <span>vs last quarter</span>
        </p>
        <div class="mu-15__spark">
          <svg viewBox="0 0 240 64" preserveAspectRatio="none" role="img" aria-label="Rolling retention, flat then easing from 106.1 to 104.8 percent">
            <path d="M0 22 20 20 40 24 60 21 80 26 100 24 120 29 140 27 160 33 180 31 200 36 220 34 240 39" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round" vector-effect="non-scaling-stroke"/>
          </svg>
        </div>
        <footer class="mu-15__card-foot">
          <p class="mu-15__foot-note">Cohort model v4</p>
          <a class="mu-15__link" href="#mu-15-title">Full report</a>
        </footer>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.mu-15 {
  --mu-15-value-size: clamp(2.25rem, 1.7rem + 2.4vw, 3rem);
  --mu-15-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --mu-15-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --mu-15-bg: #08090b;
  --mu-15-bg: oklch(13% 0.004 250);
  --mu-15-surface: #12151a;
  --mu-15-surface: oklch(19% 0.006 250);
  --mu-15-edge: #262c33;
  --mu-15-edge: oklch(27% 0.008 250);
  --mu-15-ink: #f3f5f7;
  --mu-15-ink: oklch(96.5% 0.003 250);
  --mu-15-ink-2: #a2abb3;
  --mu-15-ink-2: oklch(74% 0.008 250);
  --mu-15-line: #232a30;
  --mu-15-line: oklch(25.5% 0.008 250);
  --mu-15-up: #63d19b;
  --mu-15-up: oklch(80% 0.13 158);
  --mu-15-down: #f0a58a;
  --mu-15-down: oklch(79% 0.11 40);
  --mu-15-acc: #7fb4ff;
  --mu-15-acc: oklch(79% 0.13 260);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-15-bg);
  color: var(--mu-15-ink);
  font-family: var(--mu-15-ui);
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

.mu-15 *,
.mu-15 *::before,
.mu-15 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: light) {
  .mu-15 {
    --mu-15-bg: #f4f5f7;
    --mu-15-bg: oklch(96.5% 0.003 250);
    --mu-15-surface: #ffffff;
    --mu-15-surface: oklch(100% 0 0);
    --mu-15-edge: #dfe3e7;
    --mu-15-edge: oklch(89% 0.005 250);
    --mu-15-ink: #12151a;
    --mu-15-ink: oklch(19% 0.006 250);
    --mu-15-ink-2: #4e575f;
    --mu-15-ink-2: oklch(45% 0.012 250);
    --mu-15-line: #e5e8eb;
    --mu-15-line: oklch(92% 0.004 250);
    --mu-15-up: #14663f;
    --mu-15-up: oklch(43% 0.11 158);
    --mu-15-down: #9c3f1c;
    --mu-15-down: oklch(45% 0.13 40);
    --mu-15-acc: #144aa8;
    --mu-15-acc: oklch(42% 0.16 262);
  }
}

.mu-15[data-theme="light"],
.mu-15:has(.mu-15__theme-input:checked) {
  --mu-15-bg: #f4f5f7;
  --mu-15-bg: oklch(96.5% 0.003 250);
  --mu-15-surface: #ffffff;
  --mu-15-surface: oklch(100% 0 0);
  --mu-15-edge: #dfe3e7;
  --mu-15-edge: oklch(89% 0.005 250);
  --mu-15-ink: #12151a;
  --mu-15-ink: oklch(19% 0.006 250);
  --mu-15-ink-2: #4e575f;
  --mu-15-ink-2: oklch(45% 0.012 250);
  --mu-15-line: #e5e8eb;
  --mu-15-line: oklch(92% 0.004 250);
  --mu-15-up: #14663f;
  --mu-15-up: oklch(43% 0.11 158);
  --mu-15-down: #9c3f1c;
  --mu-15-down: oklch(45% 0.13 40);
  --mu-15-acc: #144aa8;
  --mu-15-acc: oklch(42% 0.16 262);
}

@media (prefers-color-scheme: dark) {
  .mu-15:has(.mu-15__theme-input:checked) {
    --mu-15-bg: #f4f5f7;
    --mu-15-bg: oklch(96.5% 0.003 250);
    --mu-15-surface: #ffffff;
    --mu-15-surface: oklch(100% 0 0);
    --mu-15-edge: #dfe3e7;
    --mu-15-edge: oklch(89% 0.005 250);
    --mu-15-ink: #12151a;
    --mu-15-ink: oklch(19% 0.006 250);
    --mu-15-ink-2: #4e575f;
    --mu-15-ink-2: oklch(45% 0.012 250);
    --mu-15-line: #e5e8eb;
    --mu-15-line: oklch(92% 0.004 250);
    --mu-15-up: #14663f;
    --mu-15-up: oklch(43% 0.11 158);
    --mu-15-down: #9c3f1c;
    --mu-15-down: oklch(45% 0.13 40);
    --mu-15-acc: #144aa8;
    --mu-15-acc: oklch(42% 0.16 262);
  }
}

@media (prefers-color-scheme: light) {
  .mu-15:has(.mu-15__theme-input:checked) {
    --mu-15-bg: #08090b;
    --mu-15-bg: oklch(13% 0.004 250);
    --mu-15-surface: #12151a;
    --mu-15-surface: oklch(19% 0.006 250);
    --mu-15-edge: #262c33;
    --mu-15-edge: oklch(27% 0.008 250);
    --mu-15-ink: #f3f5f7;
    --mu-15-ink: oklch(96.5% 0.003 250);
    --mu-15-ink-2: #a2abb3;
    --mu-15-ink-2: oklch(74% 0.008 250);
    --mu-15-line: #232a30;
    --mu-15-line: oklch(25.5% 0.008 250);
    --mu-15-up: #63d19b;
    --mu-15-up: oklch(80% 0.13 158);
    --mu-15-down: #f0a58a;
    --mu-15-down: oklch(79% 0.11 40);
    --mu-15-acc: #7fb4ff;
    --mu-15-acc: oklch(79% 0.13 260);
  }
}

.mu-15__sr {
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

.mu-15__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-15__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-15__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-15-edge);
  border-radius: 50%;
  background: var(--mu-15-surface);
  color: var(--mu-15-ink-2);
  cursor: pointer;
}

.mu-15__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-15__theme-input:focus-visible + .mu-15__theme-label {
  outline: 2px solid var(--mu-15-acc);
  outline-offset: 2px;
}

.mu-15__stage {
  max-inline-size: 60rem;
  margin-inline: auto;
  padding: 4rem 1.25rem 5rem;
  display: grid;
  gap: 2.5rem;
  grid-template-columns: minmax(0, 1fr);
}

.mu-15__grid {
  display: grid;
  gap: 1.25rem;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
}

.mu-15__card {
  min-inline-size: 0;
  display: grid;
  gap: 0.75rem;
  align-content: start;
  padding: 1.5rem;
  border-radius: 10px;
  background: var(--mu-15-surface);
  border-block-start: 1px solid var(--mu-15-edge);
}

.mu-15__card p,
.mu-15__card h3 {
  margin: 0;
  min-inline-size: 0;
}

.mu-15__card-head {
  display: grid;
  gap: 2px;
  min-inline-size: 0;
}

.mu-15__label {
  font-size: 0.8125rem;
  font-weight: 500;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--mu-15-ink-2);
}

.mu-15__scope {
  font-size: 0.75rem;
  color: var(--mu-15-ink-2);
}

.mu-15__value {
  font-family: var(--mu-15-mono);
  font-size: var(--mu-15-value-size);
  line-height: 1.02;
  letter-spacing: -0.03em;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

.mu-15__delta {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  font-size: 0.8125rem;
  font-variant-numeric: tabular-nums;
}

.mu-15__delta svg {
  inline-size: 15px;
  block-size: 15px;
  flex: none;
}

.mu-15__delta b {
  font-weight: 600;
}

.mu-15__delta span {
  color: var(--mu-15-ink-2);
}

.mu-15__delta--up {
  color: var(--mu-15-up);
}

.mu-15__delta--down {
  color: var(--mu-15-down);
}

.mu-15__spark {
  min-inline-size: 0;
  aspect-ratio: 240 / 64;
  color: var(--mu-15-ink-2);
  margin-block-start: 0.25rem;
}

.mu-15__spark svg {
  display: block;
  inline-size: 100%;
  block-size: 100%;
}

.mu-15__card-foot {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem 1rem;
  padding-block-start: 0.75rem;
  border-block-start: 1px solid var(--mu-15-line);
}

.mu-15__foot-note {
  font-size: 0.75rem;
  color: var(--mu-15-ink-2);
}

.mu-15__link {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--mu-15-acc);
  text-decoration: none;
  border-block-end: 1px solid transparent;
}

.mu-15__link:hover {
  border-block-end-color: currentColor;
}

.mu-15__link:focus-visible {
  outline: 2px solid var(--mu-15-acc);
  outline-offset: 3px;
  border-radius: 2px;
}

@media (min-width: 48rem) {
  .mu-15__stage {
    padding-inline: 3rem;
  }

  .mu-15__card {
    padding: 1.75rem;
  }
}
```
