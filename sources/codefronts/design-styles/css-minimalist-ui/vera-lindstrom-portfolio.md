---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/vera-lindstrom-portfolio/"
title: "Minimalist Portfolio Project Listing"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "A project list as rows, where the hover state is the only decorative moment in the whole page."
has_js: "false"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Portfolio Project Listing
Source: https://codefronts.com/design-styles/css-minimalist-ui/vera-lindstrom-portfolio/

A project list as rows, where the hover state is the only decorative moment in the whole page. It also argues the case: when items are text-led, a list beats a card grid, because a grid spends most of its space on containers and thumbnails you did not need &mdash; and the whole row is one link, one tab stop, at a 44px minimum height.
## HTML
```html
<section class="mu-17" aria-labelledby="mu-17-title">
  <h2 class="mu-17__sr" id="mu-17-title">Selected work, 2022&ndash;2026</h2>
  <div class="mu-17__theme">
    <input class="mu-17__theme-input" type="checkbox" id="mu-17-theme">
    <label class="mu-17__theme-label" for="mu-17-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-17__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-17__stage">

    <nav class="mu-17__nav" aria-label="Project index">
      <ul class="mu-17__list">
        <li class="mu-17__row">
          <a class="mu-17__link" href="#mu-17-title">
            <span class="mu-17__name">Meridian platform rebuild</span>
            <span class="mu-17__meta">Product design &middot; 8 months</span>
            <span class="mu-17__year">2026</span>
            <svg class="mu-17__arrow" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h14m0 0-6-6m6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </a>
        </li>
        <li class="mu-17__row">
          <a class="mu-17__link" href="#mu-17-title">
            <span class="mu-17__name">Basalt identity and type system</span>
            <span class="mu-17__meta">Brand &middot; with Priya Sharma</span>
            <span class="mu-17__year">2025</span>
            <svg class="mu-17__arrow" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h14m0 0-6-6m6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </a>
        </li>
        <li class="mu-17__row">
          <a class="mu-17__link" href="#mu-17-title">
            <span class="mu-17__name">Orbit developer documentation</span>
            <span class="mu-17__meta">Information architecture</span>
            <span class="mu-17__year">2025</span>
            <svg class="mu-17__arrow" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h14m0 0-6-6m6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </a>
        </li>
        <li class="mu-17__row">
          <a class="mu-17__link" href="#mu-17-title">
            <span class="mu-17__name">Fern onboarding, mobile first</span>
            <span class="mu-17__meta">Product design &middot; iOS and Android</span>
            <span class="mu-17__year">2024</span>
            <svg class="mu-17__arrow" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h14m0 0-6-6m6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </a>
        </li>
        <li class="mu-17__row">
          <a class="mu-17__link" href="#mu-17-title">
            <span class="mu-17__name">Quill editorial commissioning tool</span>
            <span class="mu-17__meta">Interface design &middot; with Jordan Lee</span>
            <span class="mu-17__year">2023</span>
            <svg class="mu-17__arrow" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h14m0 0-6-6m6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </a>
        </li>
        <li class="mu-17__row">
          <a class="mu-17__link" href="#mu-17-title">
            <span class="mu-17__name">Vale annual report</span>
            <span class="mu-17__meta">Editorial &middot; print and web</span>
            <span class="mu-17__year">2022</span>
            <svg class="mu-17__arrow" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h14m0 0-6-6m6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </a>
        </li>
      </ul>
    </nav>
  </div>
</section>
```
## CSS
```css
.mu-17 {
  --mu-17-row-pad: 1.125rem;
  --mu-17-travel: 4px;
  --mu-17-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --mu-17-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --mu-17-bg: #eef0f1;
  --mu-17-bg: oklch(94.5% 0.003 220);
  --mu-17-ink: #15181a;
  --mu-17-ink: oklch(19.5% 0.005 240);
  --mu-17-ink-2: #4e565b;
  --mu-17-ink-2: oklch(45% 0.008 240);
  --mu-17-line: #c9ced1;
  --mu-17-line: oklch(84.5% 0.005 240);
  --mu-17-acc: #15181a;
  --mu-17-acc: oklch(19.5% 0.005 240);
  --mu-17-ring: #1f5fd0;
  --mu-17-ring: oklch(48% 0.17 262);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-17-bg);
  color: var(--mu-17-ink);
  font-family: var(--mu-17-ui);
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

.mu-17 *,
.mu-17 *::before,
.mu-17 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .mu-17 {
    --mu-17-bg: #121416;
    --mu-17-bg: oklch(18% 0.005 240);
    --mu-17-ink: #eef1f2;
    --mu-17-ink: oklch(95.5% 0.003 240);
    --mu-17-ink-2: #a2aab0;
    --mu-17-ink-2: oklch(74% 0.008 240);
    --mu-17-line: #333a3e;
    --mu-17-line: oklch(33% 0.009 240);
    --mu-17-acc: #eef1f2;
    --mu-17-acc: oklch(95.5% 0.003 240);
    --mu-17-ring: #8ab4ff;
    --mu-17-ring: oklch(80% 0.12 262);
  }
}

.mu-17[data-theme="dark"],
.mu-17:has(.mu-17__theme-input:checked) {
  --mu-17-bg: #121416;
  --mu-17-bg: oklch(18% 0.005 240);
  --mu-17-ink: #eef1f2;
  --mu-17-ink: oklch(95.5% 0.003 240);
  --mu-17-ink-2: #a2aab0;
  --mu-17-ink-2: oklch(74% 0.008 240);
  --mu-17-line: #333a3e;
  --mu-17-line: oklch(33% 0.009 240);
  --mu-17-acc: #eef1f2;
  --mu-17-acc: oklch(95.5% 0.003 240);
  --mu-17-ring: #8ab4ff;
  --mu-17-ring: oklch(80% 0.12 262);
}

@media (prefers-color-scheme: light) {
  .mu-17:has(.mu-17__theme-input:checked) {
    --mu-17-bg: #121416;
    --mu-17-bg: oklch(18% 0.005 240);
    --mu-17-ink: #eef1f2;
    --mu-17-ink: oklch(95.5% 0.003 240);
    --mu-17-ink-2: #a2aab0;
    --mu-17-ink-2: oklch(74% 0.008 240);
    --mu-17-line: #333a3e;
    --mu-17-line: oklch(33% 0.009 240);
    --mu-17-acc: #eef1f2;
    --mu-17-acc: oklch(95.5% 0.003 240);
    --mu-17-ring: #8ab4ff;
    --mu-17-ring: oklch(80% 0.12 262);
  }
}

@media (prefers-color-scheme: dark) {
  .mu-17:has(.mu-17__theme-input:checked) {
    --mu-17-bg: #eef0f1;
    --mu-17-bg: oklch(94.5% 0.003 220);
    --mu-17-ink: #15181a;
    --mu-17-ink: oklch(19.5% 0.005 240);
    --mu-17-ink-2: #4e565b;
    --mu-17-ink-2: oklch(45% 0.008 240);
    --mu-17-line: #c9ced1;
    --mu-17-line: oklch(84.5% 0.005 240);
    --mu-17-acc: #15181a;
    --mu-17-acc: oklch(19.5% 0.005 240);
    --mu-17-ring: #1f5fd0;
    --mu-17-ring: oklch(48% 0.17 262);
  }
}

.mu-17__sr {
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

.mu-17__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-17__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-17__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-17-line);
  border-radius: 2px;
  background: transparent;
  color: var(--mu-17-ink-2);
  cursor: pointer;
}

.mu-17__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-17__theme-input:focus-visible + .mu-17__theme-label {
  outline: 2px solid var(--mu-17-ring);
  outline-offset: 2px;
}

.mu-17__stage {
  max-inline-size: 62rem;
  margin-inline: auto;
  padding: 4.5rem 1.25rem 5rem;
  display: grid;
  gap: 2.5rem;
  grid-template-columns: minmax(0, 1fr);
}

.mu-17__nav {
  min-inline-size: 0;
}

.mu-17__list {
  margin: 0;
  padding: 0;
  list-style: none;
  border-block-start: 1px solid var(--mu-17-line);
}

.mu-17__row {
  min-inline-size: 0;
  border-block-end: 1px solid var(--mu-17-line);
}

.mu-17__link {
  min-inline-size: 0;
  min-block-size: 44px;
  display: grid;
  align-items: baseline;
  gap: 0.125rem 1rem;
  grid-template-columns: minmax(0, 1fr) auto 1.25rem;
  padding-block: var(--mu-17-row-pad);
  color: var(--mu-17-ink);
  text-decoration: none;
  transition: color 160ms ease;
}

.mu-17__name {
  grid-column: 1;
  min-inline-size: 0;
  font-size: clamp(1.0625rem, 1rem + 0.5vw, 1.375rem);
  line-height: 1.2;
  letter-spacing: -0.018em;
  font-weight: 500;
  text-wrap: pretty;
  transition: translate 180ms ease;
}

.mu-17__meta {
  grid-column: 1;
  grid-row: 2;
  min-inline-size: 0;
  font-size: 0.8125rem;
  color: var(--mu-17-ink-2);
}

.mu-17__year {
  grid-column: 2;
  grid-row: 1;
  font-family: var(--mu-17-mono);
  font-size: 0.8125rem;
  color: var(--mu-17-ink-2);
  font-variant-numeric: tabular-nums;
}

.mu-17__arrow {
  grid-column: 3;
  grid-row: 1;
  inline-size: 20px;
  block-size: 20px;
  color: var(--mu-17-ink-2);
  transition: translate 180ms ease, color 160ms ease;
}

.mu-17__row:hover {
  border-block-end-color: var(--mu-17-acc);
}

.mu-17__link:hover .mu-17__arrow,
.mu-17__link:focus-visible .mu-17__arrow {
  translate: var(--mu-17-travel) 0;
  color: var(--mu-17-acc);
}

.mu-17__link:hover .mu-17__name,
.mu-17__link:focus-visible .mu-17__name {
  translate: calc(var(--mu-17-travel) / 2) 0;
}

.mu-17__link:focus-visible {
  outline: 2px solid var(--mu-17-ring);
  outline-offset: 4px;
}

@media (prefers-reduced-motion: reduce) {
  .mu-17__link,
    .mu-17__name,
    .mu-17__arrow {
    transition: color 160ms ease;
  }

  .mu-17__link:hover .mu-17__arrow,
    .mu-17__link:focus-visible .mu-17__arrow,
    .mu-17__link:hover .mu-17__name,
    .mu-17__link:focus-visible .mu-17__name {
    translate: none;
  }
}

@media (min-width: 44rem) {
  .mu-17__link {
    grid-template-columns: minmax(0, 1fr) minmax(0, 14rem) 4rem 1.5rem;
    align-items: center;
  }

  .mu-17__meta {
    grid-column: 2;
    grid-row: 1;
  }

  .mu-17__year {
    grid-column: 3;
    justify-self: end;
  }

  .mu-17__arrow {
    grid-column: 4;
    justify-self: end;
  }
}

@media (min-width: 56rem) {
  .mu-17__stage {
    padding-inline: 3rem;
  }
}
```
