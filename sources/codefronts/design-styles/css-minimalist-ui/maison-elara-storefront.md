---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/maison-elara-storefront/"
title: "Minimalist Product Card for Ecommerce"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "One product card: image area, name, price, one action."
has_js: "false"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Product Card for Ecommerce
Source: https://codefronts.com/design-styles/css-minimalist-ui/maison-elara-storefront/

One product card: image area, name, price, one action. It covers the place where restraint conflicts with commerce head on &mdash; a price and an add-to-cart both want to be primary. The demo takes a position on which channel each one gets, reserves the image box before the photo loads, and lists exactly what was deleted to get here.
## HTML
```html
<section class="mu-16" aria-labelledby="mu-16-title">
  <h2 class="mu-16__sr" id="mu-16-title">Featured products</h2>
  <div class="mu-16__theme">
    <input class="mu-16__theme-input" type="checkbox" id="mu-16-theme">
    <label class="mu-16__theme-label" for="mu-16-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-16__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-16__stage">

    <ul class="mu-16__grid">
      <li class="mu-16__card">
        <article aria-labelledby="mu-16-p1">
          <div class="mu-16__media">
            <div class="mu-16__slot" role="img" aria-label="Product photograph area, 4 by 5 &mdash; stoneware carafe">
              <span class="mu-16__slot-note">4:5 image area</span>
            </div>
          </div>
          <div class="mu-16__body">
            <p class="mu-16__maker">Nova Studio</p>
            <h3 class="mu-16__name" id="mu-16-p1">Unglazed stoneware carafe</h3>
            <p class="mu-16__spec">1.2 L &middot; matte body, polished lip</p>
            <p class="mu-16__price">&pound;68</p>
            <button class="mu-16__action" type="button">
              Add to bag
              <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h13m0 0-5-5m5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            </button>
          </div>
        </article>
      </li>

      <li class="mu-16__card">
        <article aria-labelledby="mu-16-p2">
          <div class="mu-16__media">
            <div class="mu-16__slot" role="img" aria-label="Product photograph area, 4 by 5 &mdash; linen throw">
              <span class="mu-16__slot-note">4:5 image area</span>
            </div>
          </div>
          <div class="mu-16__body">
            <p class="mu-16__maker">Aperture Goods</p>
            <h3 class="mu-16__name" id="mu-16-p2">Heavyweight linen throw</h3>
            <p class="mu-16__spec">140 &times; 200 cm &middot; undyed European flax</p>
            <p class="mu-16__price">&pound;145</p>
            <button class="mu-16__action" type="button">
              Add to bag
              <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h13m0 0-5-5m5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            </button>
          </div>
        </article>
      </li>

      <li class="mu-16__card">
        <article aria-labelledby="mu-16-p3">
          <div class="mu-16__media">
            <div class="mu-16__slot" role="img" aria-label="Product photograph area, 4 by 5 &mdash; desk lamp">
              <span class="mu-16__slot-note">4:5 image area</span>
            </div>
          </div>
          <div class="mu-16__body">
            <p class="mu-16__maker">Sable Works</p>
            <h3 class="mu-16__name" id="mu-16-p3">Anodised desk lamp</h3>
            <p class="mu-16__spec">2700 K &middot; stepless dimming</p>
            <p class="mu-16__price">&pound;210</p>
            <button class="mu-16__action" type="button">
              Add to bag
              <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 12h13m0 0-5-5m5 5-5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
            </button>
          </div>
        </article>
      </li>
    </ul>
  </div>
</section>
```
## CSS
```css
.mu-16 {
  --mu-16-ratio: 4 / 5;
  --mu-16-lift: 3px;
  --mu-16-serif: ui-serif, Georgia, "Iowan Old Style", "Palatino Linotype", Palatino, serif;
  --mu-16-ui: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --mu-16-bg: #f7f5f1;
  --mu-16-bg: oklch(96.8% 0.006 80);
  --mu-16-surface: #fffefc;
  --mu-16-surface: oklch(99.5% 0.003 85);
  --mu-16-media: #eae5dd;
  --mu-16-media: oklch(92% 0.01 80);
  --mu-16-ink: #1a1815;
  --mu-16-ink: oklch(20.5% 0.007 70);
  --mu-16-ink-2: #56514a;
  --mu-16-ink-2: oklch(45% 0.01 72);
  --mu-16-line: #d9d3c9;
  --mu-16-line: oklch(86% 0.012 80);
  --mu-16-acc: #23433a;
  --mu-16-acc: oklch(33% 0.05 165);
  --mu-16-acc-ink: #fbfaf8;
  --mu-16-acc-ink: oklch(98.5% 0.003 85);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-16-bg);
  color: var(--mu-16-ink);
  font-family: var(--mu-16-ui);
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

.mu-16 *,
.mu-16 *::before,
.mu-16 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .mu-16 {
    --mu-16-bg: #14120f;
    --mu-16-bg: oklch(18% 0.006 70);
    --mu-16-surface: #1c1a16;
    --mu-16-surface: oklch(22.5% 0.007 72);
    --mu-16-media: #262219;
    --mu-16-media: oklch(27% 0.01 78);
    --mu-16-ink: #f4f1eb;
    --mu-16-ink: oklch(96% 0.006 85);
    --mu-16-ink-2: #b0a99e;
    --mu-16-ink-2: oklch(75% 0.011 80);
    --mu-16-line: #3a352c;
    --mu-16-line: oklch(33% 0.012 78);
    --mu-16-acc: #8ecfb8;
    --mu-16-acc: oklch(83% 0.08 168);
    --mu-16-acc-ink: #14211c;
    --mu-16-acc-ink: oklch(19% 0.02 168);
  }
}

.mu-16[data-theme="dark"],
.mu-16:has(.mu-16__theme-input:checked) {
  --mu-16-bg: #14120f;
  --mu-16-bg: oklch(18% 0.006 70);
  --mu-16-surface: #1c1a16;
  --mu-16-surface: oklch(22.5% 0.007 72);
  --mu-16-media: #262219;
  --mu-16-media: oklch(27% 0.01 78);
  --mu-16-ink: #f4f1eb;
  --mu-16-ink: oklch(96% 0.006 85);
  --mu-16-ink-2: #b0a99e;
  --mu-16-ink-2: oklch(75% 0.011 80);
  --mu-16-line: #3a352c;
  --mu-16-line: oklch(33% 0.012 78);
  --mu-16-acc: #8ecfb8;
  --mu-16-acc: oklch(83% 0.08 168);
  --mu-16-acc-ink: #14211c;
  --mu-16-acc-ink: oklch(19% 0.02 168);
}

@media (prefers-color-scheme: light) {
  .mu-16:has(.mu-16__theme-input:checked) {
    --mu-16-bg: #14120f;
    --mu-16-bg: oklch(18% 0.006 70);
    --mu-16-surface: #1c1a16;
    --mu-16-surface: oklch(22.5% 0.007 72);
    --mu-16-media: #262219;
    --mu-16-media: oklch(27% 0.01 78);
    --mu-16-ink: #f4f1eb;
    --mu-16-ink: oklch(96% 0.006 85);
    --mu-16-ink-2: #b0a99e;
    --mu-16-ink-2: oklch(75% 0.011 80);
    --mu-16-line: #3a352c;
    --mu-16-line: oklch(33% 0.012 78);
    --mu-16-acc: #8ecfb8;
    --mu-16-acc: oklch(83% 0.08 168);
    --mu-16-acc-ink: #14211c;
    --mu-16-acc-ink: oklch(19% 0.02 168);
  }
}

@media (prefers-color-scheme: dark) {
  .mu-16:has(.mu-16__theme-input:checked) {
    --mu-16-bg: #f7f5f1;
    --mu-16-bg: oklch(96.8% 0.006 80);
    --mu-16-surface: #fffefc;
    --mu-16-surface: oklch(99.5% 0.003 85);
    --mu-16-media: #eae5dd;
    --mu-16-media: oklch(92% 0.01 80);
    --mu-16-ink: #1a1815;
    --mu-16-ink: oklch(20.5% 0.007 70);
    --mu-16-ink-2: #56514a;
    --mu-16-ink-2: oklch(45% 0.01 72);
    --mu-16-line: #d9d3c9;
    --mu-16-line: oklch(86% 0.012 80);
    --mu-16-acc: #23433a;
    --mu-16-acc: oklch(33% 0.05 165);
    --mu-16-acc-ink: #fbfaf8;
    --mu-16-acc-ink: oklch(98.5% 0.003 85);
  }
}

.mu-16__sr {
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

.mu-16__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-16__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-16__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-16-line);
  border-radius: 50%;
  background: var(--mu-16-surface);
  color: var(--mu-16-ink-2);
  cursor: pointer;
}

.mu-16__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-16__theme-input:focus-visible + .mu-16__theme-label {
  outline: 2px solid var(--mu-16-acc);
  outline-offset: 2px;
}

.mu-16__stage {
  max-inline-size: 72rem;
  margin-inline: auto;
  padding: 4rem 1.25rem 5rem;
  display: grid;
  gap: 3rem;
  grid-template-columns: minmax(0, 1fr);
}

.mu-16__grid {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 2rem 1.5rem;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr));
}

.mu-16__card {
  min-inline-size: 0;
}

.mu-16__card > article {
  min-inline-size: 0;
  display: grid;
  gap: 1rem;
  background: var(--mu-16-surface);
  border-radius: 4px;
  overflow: hidden;
  transition: translate 200ms ease;
}

.mu-16__card > article:hover,
.mu-16__card > article:focus-within {
  translate: 0 calc(var(--mu-16-lift) * -1);
}

.mu-16__media {
  min-inline-size: 0;
  aspect-ratio: var(--mu-16-ratio);
  background: var(--mu-16-media);
  overflow: hidden;
}

.mu-16__slot {
  display: grid;
  place-items: center;
  inline-size: 100%;
  block-size: 100%;
  transition: scale 320ms ease;
}

.mu-16__slot-note {
  font-size: 0.6875rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--mu-16-ink-2);
}

.mu-16__card > article:hover .mu-16__slot,
.mu-16__card > article:focus-within .mu-16__slot {
  scale: 1.03;
}

.mu-16__body {
  min-inline-size: 0;
  display: grid;
  gap: 0.375rem;
  padding: 0 1.125rem 1.25rem;
}

.mu-16__body p,
.mu-16__body h3 {
  margin: 0;
  min-inline-size: 0;
}

.mu-16__maker {
  font-size: 0.6875rem;
  font-weight: 500;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--mu-16-ink-2);
}

.mu-16__name {
  font-family: var(--mu-16-serif);
  font-size: 1.125rem;
  line-height: 1.25;
  letter-spacing: -0.012em;
  font-weight: 500;
  text-wrap: pretty;
}

.mu-16__spec {
  font-size: 0.8125rem;
  color: var(--mu-16-ink-2);
}

.mu-16__price {
  font-family: var(--mu-16-serif);
  font-size: 1.3125rem;
  font-weight: 600;
  letter-spacing: -0.016em;
  font-variant-numeric: tabular-nums;
  margin-block-start: 0.25rem;
}

.mu-16__action {
  margin-block-start: 0.5rem;
  min-block-size: 44px;
  min-inline-size: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
  padding-inline: 1rem;
  border: 1px solid var(--mu-16-acc);
  border-radius: 3px;
  background: transparent;
  color: var(--mu-16-acc);
  font: inherit;
  font-size: 0.875rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 180ms ease, color 180ms ease;
}

.mu-16__action svg {
  inline-size: 17px;
  block-size: 17px;
  flex: none;
}

.mu-16__action:hover {
  background: var(--mu-16-acc);
  color: var(--mu-16-acc-ink);
}

.mu-16__action:focus-visible {
  outline: 2px solid var(--mu-16-acc);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .mu-16__card > article,
    .mu-16__slot,
    .mu-16__action {
    transition: none;
  }

  .mu-16__card > article:hover,
    .mu-16__card > article:focus-within {
    translate: none;
  }

  .mu-16__card > article:hover .mu-16__slot,
    .mu-16__card > article:focus-within .mu-16__slot {
    scale: 1;
  }
}

@media (min-width: 56rem) {
  .mu-16__stage {
    padding-inline: 3rem;
  }
}
```
