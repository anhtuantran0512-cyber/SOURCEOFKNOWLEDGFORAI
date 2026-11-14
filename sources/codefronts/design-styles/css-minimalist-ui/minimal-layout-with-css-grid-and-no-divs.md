---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/minimal-layout-with-css-grid-and-no-divs/"
title: "Minimal Layout with CSS Grid and No Divs"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "The same card rendered twice &mdash; once with five wrapper <div> elements doing the positioning, once with grid applied directly to <article>, <header> and…"
has_js: "false"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimal Layout with CSS Grid and No Divs
Source: https://codefronts.com/design-styles/css-minimalist-ui/minimal-layout-with-css-grid-and-no-divs/

The same card rendered twice &mdash; once with five wrapper <div> elements doing the positioning, once with grid applied directly to <article>, <header> and <ul>. Identical output, half the markup, and a DOM that describes the content instead of the layout.
## HTML
```html
<section class="mu-08" aria-labelledby="mu-08-title">
  <h2 class="mu-08__sr" id="mu-08-title">Semantic and div-based markup</h2>
  <div class="mu-08__theme">
    <input class="mu-08__theme-input" type="checkbox" id="mu-08-theme">
    <label class="mu-08__theme-label" for="mu-08-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-08__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-08__stage">

    <div class="mu-08__pair">
      <section class="mu-08__panel" aria-labelledby="mu-08-a">
        <header class="mu-08__panel-head">
          <h3 class="mu-08__panel-title" id="mu-08-a">Div-heavy</h3>
          <p class="mu-08__panel-count">14 elements &middot; 5 wrappers with no meaning</p>
        </header>
        <div class="mu-08__card">
          <div class="mu-08__row">
            <div class="mu-08__col">
              <div class="mu-08__eyebrow-sm">Release 4.2</div>
              <div class="mu-08__card-title">Prism Query Engine</div>
            </div>
            <div class="mu-08__col mu-08__col--end">
              <div class="mu-08__stat">+18%</div>
            </div>
          </div>
          <div class="mu-08__row">
            <div class="mu-08__text">Cold-start latency down across all regions after the planner rewrite.</div>
          </div>
          <div class="mu-08__row">
            <div class="mu-08__links">
              <div><a href="#mu-08-title">Changelog</a></div>
              <div><a href="#mu-08-title">Migration notes</a></div>
              <div><a href="#mu-08-title">Benchmarks</a></div>
            </div>
          </div>
        </div>
        <pre class="mu-08__code"><code>&lt;div class="card"&gt;
  &lt;div class="row"&gt;
    &lt;div class="col"&gt;&hellip;&lt;/div&gt;
    &lt;div class="col end"&gt;&hellip;&lt;/div&gt;
  &lt;/div&gt;
  &lt;div class="row"&gt;&hellip;&lt;/div&gt;
&lt;/div&gt;</code></pre>
      </section>

      <section class="mu-08__panel mu-08__panel--good" aria-labelledby="mu-08-b">
        <header class="mu-08__panel-head">
          <h3 class="mu-08__panel-title" id="mu-08-b">Semantic</h3>
          <p class="mu-08__panel-count">9 elements &middot; 0 layout wrappers</p>
        </header>
        <article class="mu-08__semantic">
          <header>
            <p class="mu-08__eyebrow-sm">Release 4.2</p>
            <h4 class="mu-08__card-title">Prism Query Engine</h4>
          </header>
          <p class="mu-08__stat">+18%</p>
          <p class="mu-08__text">Cold-start latency down across all regions after the planner rewrite.</p>
          <ul class="mu-08__links">
            <li><a href="#mu-08-title">Changelog</a></li>
            <li><a href="#mu-08-title">Migration notes</a></li>
            <li><a href="#mu-08-title">Benchmarks</a></li>
          </ul>
        </article>
        <pre class="mu-08__code"><code>&lt;article&gt;
  &lt;header&gt;&hellip;&lt;/header&gt;
  &lt;p class="stat"&gt;&hellip;&lt;/p&gt;
  &lt;p&gt;&hellip;&lt;/p&gt;
  &lt;ul&gt;&hellip;&lt;/ul&gt;
&lt;/article&gt;</code></pre>
      </section>
    </div>
  </div>
</section>
```
## CSS
```css
.mu-08 {
  --mu-08-pad: 1.25rem;
  --mu-08-gap: 0.75rem;
  --mu-08-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --mu-08-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --mu-08-bg: #eceef0;
  --mu-08-bg: oklch(94% 0.004 240);
  --mu-08-surface: #ffffff;
  --mu-08-surface: oklch(100% 0 0);
  --mu-08-code: #f4f6f7;
  --mu-08-code: oklch(97% 0.003 240);
  --mu-08-ink: #16191c;
  --mu-08-ink: oklch(20% 0.008 250);
  --mu-08-ink-2: #4d565e;
  --mu-08-ink-2: oklch(44% 0.014 250);
  --mu-08-line: #ccd2d7;
  --mu-08-line: oklch(85% 0.007 250);
  --mu-08-acc: #0f5f8f;
  --mu-08-acc: oklch(45% 0.11 240);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-08-bg);
  color: var(--mu-08-ink);
  font-family: var(--mu-08-ui);
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

.mu-08 *,
.mu-08 *::before,
.mu-08 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .mu-08 {
    --mu-08-bg: #101315;
    --mu-08-bg: oklch(17.5% 0.006 250);
    --mu-08-surface: #191d20;
    --mu-08-surface: oklch(23% 0.007 250);
    --mu-08-code: #12171a;
    --mu-08-code: oklch(19.5% 0.008 250);
    --mu-08-ink: #eef1f3;
    --mu-08-ink: oklch(95.5% 0.004 250);
    --mu-08-ink-2: #a4adb4;
    --mu-08-ink-2: oklch(74% 0.01 250);
    --mu-08-line: #333b41;
    --mu-08-line: oklch(33% 0.011 250);
    --mu-08-acc: #6fbde8;
    --mu-08-acc: oklch(78% 0.1 235);
  }
}

.mu-08[data-theme="dark"],
.mu-08:has(.mu-08__theme-input:checked) {
  --mu-08-bg: #101315;
  --mu-08-bg: oklch(17.5% 0.006 250);
  --mu-08-surface: #191d20;
  --mu-08-surface: oklch(23% 0.007 250);
  --mu-08-code: #12171a;
  --mu-08-code: oklch(19.5% 0.008 250);
  --mu-08-ink: #eef1f3;
  --mu-08-ink: oklch(95.5% 0.004 250);
  --mu-08-ink-2: #a4adb4;
  --mu-08-ink-2: oklch(74% 0.01 250);
  --mu-08-line: #333b41;
  --mu-08-line: oklch(33% 0.011 250);
  --mu-08-acc: #6fbde8;
  --mu-08-acc: oklch(78% 0.1 235);
}

@media (prefers-color-scheme: light) {
  .mu-08:has(.mu-08__theme-input:checked) {
    --mu-08-bg: #101315;
    --mu-08-bg: oklch(17.5% 0.006 250);
    --mu-08-surface: #191d20;
    --mu-08-surface: oklch(23% 0.007 250);
    --mu-08-code: #12171a;
    --mu-08-code: oklch(19.5% 0.008 250);
    --mu-08-ink: #eef1f3;
    --mu-08-ink: oklch(95.5% 0.004 250);
    --mu-08-ink-2: #a4adb4;
    --mu-08-ink-2: oklch(74% 0.01 250);
    --mu-08-line: #333b41;
    --mu-08-line: oklch(33% 0.011 250);
    --mu-08-acc: #6fbde8;
    --mu-08-acc: oklch(78% 0.1 235);
  }
}

@media (prefers-color-scheme: dark) {
  .mu-08:has(.mu-08__theme-input:checked) {
    --mu-08-bg: #eceef0;
    --mu-08-bg: oklch(94% 0.004 240);
    --mu-08-surface: #ffffff;
    --mu-08-surface: oklch(100% 0 0);
    --mu-08-code: #f4f6f7;
    --mu-08-code: oklch(97% 0.003 240);
    --mu-08-ink: #16191c;
    --mu-08-ink: oklch(20% 0.008 250);
    --mu-08-ink-2: #4d565e;
    --mu-08-ink-2: oklch(44% 0.014 250);
    --mu-08-line: #ccd2d7;
    --mu-08-line: oklch(85% 0.007 250);
    --mu-08-acc: #0f5f8f;
    --mu-08-acc: oklch(45% 0.11 240);
  }
}

.mu-08__sr {
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

.mu-08__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-08__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-08__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-08-line);
  border-radius: 4px;
  background: var(--mu-08-surface);
  color: var(--mu-08-ink-2);
  cursor: pointer;
}

.mu-08__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-08__theme-input:focus-visible + .mu-08__theme-label {
  outline: 2px solid var(--mu-08-acc);
  outline-offset: 2px;
}

.mu-08__stage {
  max-inline-size: 74rem;
  margin-inline: auto;
  padding: 4rem 1.5rem 5rem;
  display: grid;
  gap: 3rem;
  grid-template-columns: minmax(0, 1fr);
}

.mu-08__pair {
  display: grid;
  gap: 1.5rem;
  grid-template-columns: minmax(0, 1fr);
}

.mu-08__panel {
  min-inline-size: 0;
  display: grid;
  gap: 1rem;
  align-content: start;
  padding: 1.25rem;
  border: 1px solid var(--mu-08-line);
  border-radius: 6px;
  background: var(--mu-08-surface);
}

.mu-08__panel--good {
  border-color: var(--mu-08-acc);
}

.mu-08__panel-head {
  display: grid;
  gap: 2px;
  min-inline-size: 0;
}

.mu-08__panel-title {
  margin: 0;
  font-size: 0.8125rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.mu-08__panel-count {
  margin: 0;
  font-family: var(--mu-08-mono);
  font-size: 0.75rem;
  color: var(--mu-08-ink-2);
}

.mu-08__card,
.mu-08__semantic {
  min-inline-size: 0;
  padding: var(--mu-08-pad);
  border: 1px solid var(--mu-08-line);
  border-radius: 4px;
}

.mu-08__card {
  display: grid;
  gap: var(--mu-08-gap);
}

.mu-08__row {
  display: grid;
  gap: var(--mu-08-gap);
  grid-template-columns: minmax(0, 1fr) auto;
}

.mu-08__row:nth-child(n+2) {
  grid-template-columns: minmax(0, 1fr);
}

.mu-08__col {
  min-inline-size: 0;
  display: grid;
  gap: 2px;
  align-content: start;
}

.mu-08__col--end {
  justify-items: end;
}

.mu-08__semantic {
  display: grid;
  gap: var(--mu-08-gap);
  grid-template-columns: minmax(0, 1fr) auto;
  grid-template-areas: "head stat" "text text" "links links";
}

.mu-08__semantic > header {
  grid-area: head;
  min-inline-size: 0;
  display: grid;
  gap: 2px;
}

.mu-08__semantic > .mu-08__stat {
  grid-area: stat;
  justify-self: end;
}

.mu-08__semantic > .mu-08__text {
  grid-area: text;
}

.mu-08__semantic > .mu-08__links {
  grid-area: links;
}

.mu-08__eyebrow-sm {
  margin: 0;
  font-family: var(--mu-08-mono);
  font-size: 0.6875rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--mu-08-ink-2);
}

.mu-08__card-title {
  margin: 0;
  font-size: 1.125rem;
  line-height: 1.2;
  letter-spacing: -0.016em;
  font-weight: 600;
  min-inline-size: 0;
}

.mu-08__stat {
  margin: 0;
  font-family: var(--mu-08-mono);
  font-size: 1.125rem;
  font-weight: 500;
  font-variant-numeric: tabular-nums;
  color: var(--mu-08-acc);
}

.mu-08__text {
  margin: 0;
  font-size: 0.9375rem;
  color: var(--mu-08-ink-2);
  text-wrap: pretty;
}

.mu-08__links {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1rem;
  padding-block-start: 0.5rem;
  border-block-start: 1px solid var(--mu-08-line);
}

.mu-08__links > div,
.mu-08__links > li {
  min-inline-size: 0;
}

.mu-08__links a {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--mu-08-acc);
  text-decoration: none;
  border-block-end: 1px solid transparent;
}

.mu-08__links a:hover {
  border-block-end-color: currentColor;
}

.mu-08__links a:focus-visible {
  outline: 2px solid var(--mu-08-acc);
  outline-offset: 3px;
  border-radius: 2px;
}

.mu-08__code {
  margin: 0;
  padding: 0.875rem;
  overflow-x: auto;
  min-inline-size: 0;
  background: var(--mu-08-code);
  border: 1px solid var(--mu-08-line);
  border-radius: 4px;
  font-family: var(--mu-08-mono);
  font-size: 0.75rem;
  line-height: 1.6;
  color: var(--mu-08-ink-2);
}

.mu-08__code code {
  font: inherit;
  white-space: pre;
}

@media (min-width: 52rem) {
  .mu-08__pair {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .mu-08__stage {
    padding-inline: 3rem;
  }
}
```
