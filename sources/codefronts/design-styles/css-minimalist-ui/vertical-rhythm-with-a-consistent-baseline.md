---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/vertical-rhythm-with-a-consistent-baseline/"
title: "Vertical Rhythm with a Consistent Baseline"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "Line heights and block margins are multiples of one rhythm unit, so text blocks line up down the page."
has_js: "true"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Rhythm with a Consistent Baseline
Source: https://codefronts.com/design-styles/css-minimalist-ui/vertical-rhythm-with-a-consistent-baseline/

Line heights and block margins are multiples of one rhythm unit, so text blocks line up down the page. A toggleable overlay draws the grid over live prose so you can see where the rhythm holds and where an image or an input breaks it &mdash; which it will, and the demo says what to do about that.
## HTML
```html
<section class="mu-07" aria-labelledby="mu-07-title">
  <h2 class="mu-07__sr" id="mu-07-title">Vertical rhythm article</h2>
  <div class="mu-07__theme">
    <input class="mu-07__theme-input" type="checkbox" id="mu-07-theme">
    <label class="mu-07__theme-label" for="mu-07-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-07__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-07__stage">
    <header class="mu-07__head">
      <div class="mu-07__controls">
        <button class="mu-07__toggle" id="mu-07-grid-btn" type="button" aria-pressed="false">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M3 6h18M3 12h18M3 18h18" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>
          Baseline overlay
        </button>
        <p class="mu-07__unit">Unit <b>1.5rem</b> &middot; 24px at a 16px root</p>
      </div>
    </header>

    <article class="mu-07__article" id="mu-07-article">
      <h3 class="mu-07__h3">Rhythm survives real content, grids do not</h3>
      <p class="mu-07__lead">Set the rhythm once and the column composes itself. Body copy takes one unit per line, a heading takes two, and the gap between blocks takes one &mdash; so the eye reads order it cannot name.</p>
      <p>Turn the overlay on and the mechanism becomes obvious: every line of prose sits on a rule, and every block boundary lands on one too. Nothing here is hand-nudged. The whole column is derived from a single custom property, which means the rhythm can be retuned for a different reading size in one edit.</p>
      <h4 class="mu-07__h4">Where it stops being free</h4>
      <p>The image below is 3:2, which is not a multiple of anything. Its caption is smaller than the body, so its own line height is not a whole unit either. A strict per-line grid would need padding calculated from the image height &mdash; a value that changes with the viewport, so the correction cannot be static.</p>
      <figure class="mu-07__figure">
        <div class="mu-07__frame" role="img" aria-label="Tonal placeholder standing in for an article image, 3 by 2">
          <span class="mu-07__frame-note">3:2 image area</span>
        </div>
        <figcaption class="mu-07__caption">A block on the grid, with an interior that is not. This is the compromise that keeps the system usable.</figcaption>
      </figure>
      <p>The practical answer is rhythm at the block level. Each block <em>starts</em> on the grid; its interior may not. That is nine-tenths of the perceived order at a tenth of the fragility, and it holds when an editor adds a pull quote, a table, or an embed you did not plan for.</p>
      <blockquote class="mu-07__quote">
        <p>If the correction has to be recalculated every time the content changes, it is not a system.</p>
      </blockquote>
      <p>Where a print designer can force every element onto the baseline because the page is fixed, a web page is not. Accepting that is what separates a rhythm that ships from a grid that gets quietly deleted in the third sprint.</p>
    </article>
  </div>
</section>
```
## CSS
```css
.mu-07 {
  --mu-07-rhythm: 1.5rem;
  --mu-07-h-lead: 2;
  --mu-07-measure: 66ch;
  --mu-07-fig-fix: 0px;
  --mu-07-serif: ui-serif, Georgia, "Iowan Old Style", "Palatino Linotype", Palatino, serif;
  --mu-07-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --mu-07-bg: #faf6ee;
  --mu-07-bg: oklch(97.5% 0.012 88);
  --mu-07-surface: #fffdf8;
  --mu-07-surface: oklch(99.2% 0.006 88);
  --mu-07-ink: #1a1712;
  --mu-07-ink: oklch(20% 0.01 70);
  --mu-07-ink-2: #57503f;
  --mu-07-ink-2: oklch(45% 0.018 78);
  --mu-07-line: #ddd4c1;
  --mu-07-line: oklch(87% 0.02 85);
  --mu-07-grid: rgba(139, 74, 20, 0.22);
  --mu-07-acc: #8b4a14;
  --mu-07-acc: oklch(45% 0.12 55);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-07-bg);
  color: var(--mu-07-ink);
  font-family: var(--mu-07-ui);
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

.mu-07 *,
.mu-07 *::before,
.mu-07 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .mu-07 {
    --mu-07-bg: #14120e;
    --mu-07-bg: oklch(18% 0.009 70);
    --mu-07-surface: #1c1914;
    --mu-07-surface: oklch(22.5% 0.01 72);
    --mu-07-ink: #f4efe4;
    --mu-07-ink: oklch(96% 0.012 88);
    --mu-07-ink-2: #b3a993;
    --mu-07-ink-2: oklch(76% 0.02 85);
    --mu-07-line: #3b342a;
    --mu-07-line: oklch(33% 0.015 78);
    --mu-07-grid: rgba(232, 168, 106, 0.24);
    --mu-07-acc: #e8a86a;
    --mu-07-acc: oklch(79% 0.11 60);
  }
}

.mu-07[data-theme="dark"],
.mu-07:has(.mu-07__theme-input:checked) {
  --mu-07-bg: #14120e;
  --mu-07-bg: oklch(18% 0.009 70);
  --mu-07-surface: #1c1914;
  --mu-07-surface: oklch(22.5% 0.01 72);
  --mu-07-ink: #f4efe4;
  --mu-07-ink: oklch(96% 0.012 88);
  --mu-07-ink-2: #b3a993;
  --mu-07-ink-2: oklch(76% 0.02 85);
  --mu-07-line: #3b342a;
  --mu-07-line: oklch(33% 0.015 78);
  --mu-07-grid: rgba(232, 168, 106, 0.24);
  --mu-07-acc: #e8a86a;
  --mu-07-acc: oklch(79% 0.11 60);
}

@media (prefers-color-scheme: light) {
  .mu-07:has(.mu-07__theme-input:checked) {
    --mu-07-bg: #14120e;
    --mu-07-bg: oklch(18% 0.009 70);
    --mu-07-surface: #1c1914;
    --mu-07-surface: oklch(22.5% 0.01 72);
    --mu-07-ink: #f4efe4;
    --mu-07-ink: oklch(96% 0.012 88);
    --mu-07-ink-2: #b3a993;
    --mu-07-ink-2: oklch(76% 0.02 85);
    --mu-07-line: #3b342a;
    --mu-07-line: oklch(33% 0.015 78);
    --mu-07-grid: rgba(232, 168, 106, 0.24);
    --mu-07-acc: #e8a86a;
    --mu-07-acc: oklch(79% 0.11 60);
  }
}

@media (prefers-color-scheme: dark) {
  .mu-07:has(.mu-07__theme-input:checked) {
    --mu-07-bg: #faf6ee;
    --mu-07-bg: oklch(97.5% 0.012 88);
    --mu-07-surface: #fffdf8;
    --mu-07-surface: oklch(99.2% 0.006 88);
    --mu-07-ink: #1a1712;
    --mu-07-ink: oklch(20% 0.01 70);
    --mu-07-ink-2: #57503f;
    --mu-07-ink-2: oklch(45% 0.018 78);
    --mu-07-line: #ddd4c1;
    --mu-07-line: oklch(87% 0.02 85);
    --mu-07-grid: rgba(139, 74, 20, 0.22);
    --mu-07-acc: #8b4a14;
    --mu-07-acc: oklch(45% 0.12 55);
  }
}

.mu-07__sr {
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

.mu-07__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-07__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-07__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-07-line);
  border-radius: 50%;
  background: var(--mu-07-surface);
  color: var(--mu-07-ink-2);
  cursor: pointer;
}

.mu-07__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-07__theme-input:focus-visible + .mu-07__theme-label {
  outline: 2px solid var(--mu-07-acc);
  outline-offset: 2px;
}

.mu-07__stage {
  max-inline-size: 60rem;
  margin-inline: auto;
  padding: calc(var(--mu-07-rhythm) * 3) 1.5rem calc(var(--mu-07-rhythm) * 4);
  display: grid;
  gap: calc(var(--mu-07-rhythm) * 2);
  grid-template-columns: minmax(0, 1fr);
}

.mu-07__head {
  display: grid;
  gap: var(--mu-07-rhythm);
  max-inline-size: var(--mu-07-measure);
}

.mu-07__controls {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.75rem 1rem;
  padding-block-start: 0.5rem;
}

.mu-07__toggle {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  min-block-size: 44px;
  min-inline-size: 44px;
  padding-inline: 1rem;
  border: 1px solid var(--mu-07-line);
  border-radius: 4px;
  background: var(--mu-07-surface);
  color: var(--mu-07-ink);
  font: inherit;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  transition: border-color 150ms ease, color 150ms ease;
}

.mu-07__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  flex: none;
}

.mu-07__toggle:hover {
  border-color: var(--mu-07-acc);
}

.mu-07__toggle:focus-visible {
  outline: 2px solid var(--mu-07-acc);
  outline-offset: 2px;
}

.mu-07__toggle[aria-pressed="true"] {
  border-color: var(--mu-07-acc);
  color: var(--mu-07-acc);
}

.mu-07__unit {
  margin: 0;
  font-size: 0.8125rem;
  color: var(--mu-07-ink-2);
  font-variant-numeric: tabular-nums;
}

.mu-07__article {
  position: relative;
  min-inline-size: 0;
  max-inline-size: var(--mu-07-measure);
  font-family: var(--mu-07-serif);
  font-size: 1.0625rem;
  line-height: var(--mu-07-rhythm);
}

.mu-07__article.is-grid {
  background-image: repeating-linear-gradient(
      to bottom,
      var(--mu-07-grid) 0,
      var(--mu-07-grid) 1px,
      transparent 1px,
      transparent var(--mu-07-rhythm)
    );
  background-position: 0 0;
}

.mu-07__article > * {
  margin: 0 0 var(--mu-07-rhythm);
  min-inline-size: 0;
}

.mu-07__article > :last-child {
  margin-block-end: 0;
}

.mu-07__h3 {
  font-size: 1.5rem;
  line-height: calc(var(--mu-07-rhythm) * var(--mu-07-h-lead));
  letter-spacing: -0.018em;
  font-weight: 600;
  margin-block: 0 var(--mu-07-rhythm);
  text-wrap: balance;
}

.mu-07__h4 {
  font-family: var(--mu-07-ui);
  font-size: 0.8125rem;
  line-height: var(--mu-07-rhythm);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  font-weight: 700;
  color: var(--mu-07-ink-2);
  margin-block: calc(var(--mu-07-rhythm) * 2) var(--mu-07-rhythm);
}

.mu-07__lead {
  font-size: 1.1875rem;
  line-height: calc(var(--mu-07-rhythm) * 1.5);
  text-wrap: pretty;
}

.mu-07__article p {
  text-wrap: pretty;
}

.mu-07__figure {
  margin-block: calc(var(--mu-07-rhythm) * 2) var(--mu-07-rhythm);
}

.mu-07__frame {
  aspect-ratio: 3 / 2;
  inline-size: 100%;
  display: grid;
  place-items: center;
  background: var(--mu-07-surface);
  border: 1px solid var(--mu-07-line);
  border-radius: 4px;
  margin-block-end: calc(var(--mu-07-rhythm) - var(--mu-07-fig-fix));
}

.mu-07__frame-note {
  font-family: var(--mu-07-ui);
  font-size: 0.75rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--mu-07-ink-2);
}

.mu-07__caption {
  font-family: var(--mu-07-ui);
  font-size: 0.8125rem;
  line-height: var(--mu-07-rhythm);
  color: var(--mu-07-ink-2);
  text-wrap: pretty;
}

.mu-07__quote {
  margin-block: calc(var(--mu-07-rhythm) * 2);
  margin-inline: 0;
  padding-inline-start: 1.25rem;
  border-inline-start: 2px solid var(--mu-07-acc);
}

.mu-07__quote p {
  margin: 0;
  font-size: 1.3125rem;
  line-height: calc(var(--mu-07-rhythm) * 1.5);
  letter-spacing: -0.014em;
  text-wrap: pretty;
}

@media (prefers-reduced-motion: reduce) {
  .mu-07__toggle {
    transition: none;
  }
}

@media (min-width: 56rem) {
  .mu-07__stage {
    padding-inline: 3rem;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.mu-07');
  if (!root) return;
  const btn = root.querySelector('#mu-07-grid-btn');
  const article = root.querySelector('#mu-07-article');
  if (!btn || !article) return;

  const setGrid = (on) => {
    btn.setAttribute('aria-pressed', String(on));
    article.classList.toggle('is-grid', on);
  };
  const onClick = () => setGrid(btn.getAttribute('aria-pressed') !== 'true');
  const onKey = (e) => {
    if (e.key === 'g' && !e.metaKey && !e.ctrlKey && !e.altKey) onClick();
  };

  btn.addEventListener('click', onClick);
  root.addEventListener('keydown', onKey);

  root.__muCleanup = () => {
    btn.removeEventListener('click', onClick);
    root.removeEventListener('keydown', onKey);
    setGrid(false);
  };
})();
```
