---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-minimalist-ui/elevation-without-shadows-or-gradients/"
title: "Elevation Without Shadows or Gradients"
section: "design-styles"
category: "css-minimalist-ui"
category_name: "CSS Minimalist UI"
description: "Three elevation levels rendered with surface tone, spacing and a single hairline &mdash; no shadow stack, no gradients."
has_js: "false"
---

Here's a working CSS Minimalist UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Elevation Without Shadows or Gradients
Source: https://codefronts.com/design-styles/css-minimalist-ui/elevation-without-shadows-or-gradients/

Three elevation levels rendered with surface tone, spacing and a single hairline &mdash; no shadow stack, no gradients. It also states the limit honestly: without shadows a floating element loses its depth cue, so the overlay here still ships a scrim, and the demo explains why that is not a contradiction.
## HTML
```html
<section class="mu-12" aria-labelledby="mu-12-title">
  <h2 class="mu-12__sr" id="mu-12-title">Tonal elevation levels</h2>
  <div class="mu-12__theme">
    <input class="mu-12__theme-input" type="checkbox" id="mu-12-theme">
    <label class="mu-12__theme-label" for="mu-12-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="mu-12__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="mu-12__stage">

    <div class="mu-12__ladder">
      <article class="mu-12__level mu-12__level--0" aria-labelledby="mu-12-l0">
        <header class="mu-12__level-head">
          <h3 class="mu-12__level-title" id="mu-12-l0">Level 0 &mdash; page</h3>
          <p class="mu-12__level-spec">base tone &middot; no edge &middot; pad 24px</p>
        </header>

        <article class="mu-12__level mu-12__level--1" aria-labelledby="mu-12-l1">
          <header class="mu-12__level-head">
            <h4 class="mu-12__level-title" id="mu-12-l1">Level 1 &mdash; panel</h4>
            <p class="mu-12__level-spec">+4% lightness &middot; top hairline &middot; pad 28px</p>
          </header>

          <article class="mu-12__level mu-12__level--2" aria-labelledby="mu-12-l2">
            <header class="mu-12__level-head">
              <h5 class="mu-12__level-title" id="mu-12-l2">Level 2 &mdash; raised</h5>
              <p class="mu-12__level-spec">+8% lightness &middot; top hairline &middot; pad 32px</p>
            </header>
            <div class="mu-12__actions">
              <button class="mu-12__btn mu-12__btn--primary" type="button">Save workspace</button>
              <button class="mu-12__btn" type="button">Discard</button>
            </div>
          </article>
        </article>
      </article>
    </div>

    <section class="mu-12__overlay-demo" aria-labelledby="mu-12-l3">
      <div class="mu-12__scrim">
        <div class="mu-12__dialog">
          <h3 class="mu-12__level-title" id="mu-12-l3">Level 3 &mdash; overlay</h3>
          <p class="mu-12__level-spec">+12% lightness &middot; top hairline &middot; scrim required</p>
          <div class="mu-12__actions">
            <button class="mu-12__btn mu-12__btn--primary" type="button">Confirm transfer</button>
            <button class="mu-12__btn" type="button">Cancel</button>
          </div>
        </div>
      </div>
    </section>
  </div>
</section>
```
## CSS
```css
.mu-12 {
  --mu-12-pad-step: 0.25rem;
  --mu-12-round: ui-rounded, "SF Pro Rounded", "Hiragino Maru Gothic ProN", system-ui, -apple-system, "Segoe UI", sans-serif;
  --mu-12-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace;
  --mu-12-e0: #1b1917;
  --mu-12-e0: oklch(22% 0.006 60);
  --mu-12-e1: #232120;
  --mu-12-e1: oklch(26% 0.006 60);
  --mu-12-e2: #2c2a28;
  --mu-12-e2: oklch(30% 0.006 60);
  --mu-12-e3: #363331;
  --mu-12-e3: oklch(34% 0.007 60);
  --mu-12-edge: #4a4643;
  --mu-12-edge: oklch(42% 0.008 60);
  --mu-12-ink: #f5f2ef;
  --mu-12-ink: oklch(96% 0.005 70);
  --mu-12-ink-2: #b3aca6;
  --mu-12-ink-2: oklch(75% 0.009 65);
  --mu-12-scrim: rgba(8, 7, 6, 0.62);
  --mu-12-acc: #8fd4c4;
  --mu-12-acc: oklch(84% 0.09 175);
  --mu-12-acc-ink: #12201d;
  --mu-12-acc-ink: oklch(19% 0.02 175);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mu-12-e0);
  color: var(--mu-12-ink);
  font-family: var(--mu-12-round);
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
}

.mu-12 *,
.mu-12 *::before,
.mu-12 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: light) {
  .mu-12 {
    --mu-12-e0: #eeecea;
    --mu-12-e0: oklch(94% 0.004 70);
    --mu-12-e1: #f5f3f1;
    --mu-12-e1: oklch(96.5% 0.004 70);
    --mu-12-e2: #fbfaf9;
    --mu-12-e2: oklch(98.5% 0.003 70);
    --mu-12-e3: #ffffff;
    --mu-12-e3: oklch(100% 0 0);
    --mu-12-edge: #cfcac5;
    --mu-12-edge: oklch(84% 0.007 70);
    --mu-12-ink: #1b1917;
    --mu-12-ink: oklch(22% 0.006 60);
    --mu-12-ink-2: #57514b;
    --mu-12-ink-2: oklch(45% 0.01 62);
    --mu-12-scrim: rgba(24, 22, 20, 0.48);
    --mu-12-acc: #0d6355;
    --mu-12-acc: oklch(43% 0.09 175);
    --mu-12-acc-ink: #ffffff;
    --mu-12-acc-ink: oklch(100% 0 0);
  }
}

.mu-12[data-theme="light"],
.mu-12:has(.mu-12__theme-input:checked) {
  --mu-12-e0: #eeecea;
  --mu-12-e0: oklch(94% 0.004 70);
  --mu-12-e1: #f5f3f1;
  --mu-12-e1: oklch(96.5% 0.004 70);
  --mu-12-e2: #fbfaf9;
  --mu-12-e2: oklch(98.5% 0.003 70);
  --mu-12-e3: #ffffff;
  --mu-12-e3: oklch(100% 0 0);
  --mu-12-edge: #cfcac5;
  --mu-12-edge: oklch(84% 0.007 70);
  --mu-12-ink: #1b1917;
  --mu-12-ink: oklch(22% 0.006 60);
  --mu-12-ink-2: #57514b;
  --mu-12-ink-2: oklch(45% 0.01 62);
  --mu-12-scrim: rgba(24, 22, 20, 0.48);
  --mu-12-acc: #0d6355;
  --mu-12-acc: oklch(43% 0.09 175);
  --mu-12-acc-ink: #ffffff;
  --mu-12-acc-ink: oklch(100% 0 0);
}

@media (prefers-color-scheme: dark) {
  .mu-12:has(.mu-12__theme-input:checked) {
    --mu-12-e0: #eeecea;
    --mu-12-e0: oklch(94% 0.004 70);
    --mu-12-e1: #f5f3f1;
    --mu-12-e1: oklch(96.5% 0.004 70);
    --mu-12-e2: #fbfaf9;
    --mu-12-e2: oklch(98.5% 0.003 70);
    --mu-12-e3: #ffffff;
    --mu-12-e3: oklch(100% 0 0);
    --mu-12-edge: #cfcac5;
    --mu-12-edge: oklch(84% 0.007 70);
    --mu-12-ink: #1b1917;
    --mu-12-ink: oklch(22% 0.006 60);
    --mu-12-ink-2: #57514b;
    --mu-12-ink-2: oklch(45% 0.01 62);
    --mu-12-scrim: rgba(24, 22, 20, 0.48);
    --mu-12-acc: #0d6355;
    --mu-12-acc: oklch(43% 0.09 175);
    --mu-12-acc-ink: #ffffff;
    --mu-12-acc-ink: oklch(100% 0 0);
  }
}

@media (prefers-color-scheme: light) {
  .mu-12:has(.mu-12__theme-input:checked) {
    --mu-12-e0: #1b1917;
    --mu-12-e0: oklch(22% 0.006 60);
    --mu-12-e1: #232120;
    --mu-12-e1: oklch(26% 0.006 60);
    --mu-12-e2: #2c2a28;
    --mu-12-e2: oklch(30% 0.006 60);
    --mu-12-e3: #363331;
    --mu-12-e3: oklch(34% 0.007 60);
    --mu-12-edge: #4a4643;
    --mu-12-edge: oklch(42% 0.008 60);
    --mu-12-ink: #f5f2ef;
    --mu-12-ink: oklch(96% 0.005 70);
    --mu-12-ink-2: #b3aca6;
    --mu-12-ink-2: oklch(75% 0.009 65);
    --mu-12-scrim: rgba(8, 7, 6, 0.62);
    --mu-12-acc: #8fd4c4;
    --mu-12-acc: oklch(84% 0.09 175);
    --mu-12-acc-ink: #12201d;
    --mu-12-acc-ink: oklch(19% 0.02 175);
  }
}

.mu-12__sr {
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

.mu-12__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
}

.mu-12__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.mu-12__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mu-12-edge);
  border-radius: 50%;
  background: var(--mu-12-e2);
  color: var(--mu-12-ink-2);
  cursor: pointer;
}

.mu-12__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mu-12__theme-input:focus-visible + .mu-12__theme-label {
  outline: 2px solid var(--mu-12-acc);
  outline-offset: 2px;
}

.mu-12__stage {
  max-inline-size: 62rem;
  margin-inline: auto;
  padding: 4rem 1.25rem 5rem;
  display: grid;
  gap: 2.5rem;
  grid-template-columns: minmax(0, 1fr);
}

.mu-12__ladder {
  min-inline-size: 0;
}

.mu-12__level {
  min-inline-size: 0;
  display: grid;
  gap: 0.75rem;
  border-radius: 10px;
  border-block-start: 1px solid var(--mu-12-edge);
}

@supports (color: color-mix(in oklab, red, blue)) {
  .mu-12__level {
    border-block-start-color: color-mix(in oklab, var(--mu-12-edge) 85%, var(--mu-12-ink));
  }
}

.mu-12__level--0 {
  background: var(--mu-12-e0);
  padding: 1.5rem;
  border-block-start-color: transparent;
}

.mu-12__level--1 {
  background: var(--mu-12-e1);
  padding: calc(1.5rem + var(--mu-12-pad-step));
}

.mu-12__level--2 {
  background: var(--mu-12-e2);
  padding: calc(1.5rem + var(--mu-12-pad-step) * 2);
}

.mu-12__level-head {
  display: grid;
  gap: 2px;
  min-inline-size: 0;
}

.mu-12__level-title {
  margin: 0;
  font-size: 0.9375rem;
  font-weight: 600;
  letter-spacing: -0.008em;
}

.mu-12__level-spec {
  margin: 0;
  font-family: var(--mu-12-mono);
  font-size: 0.75rem;
  color: var(--mu-12-ink-2);
  font-variant-numeric: tabular-nums;
}

.mu-12__actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  padding-block-start: 0.25rem;
}

.mu-12__btn {
  min-block-size: 44px;
  min-inline-size: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding-inline: 1rem;
  border-radius: 8px;
  border: 1px solid var(--mu-12-edge);
  background: transparent;
  color: var(--mu-12-ink);
  font: inherit;
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
}

.mu-12__btn:focus-visible {
  outline: 2px solid var(--mu-12-acc);
  outline-offset: 2px;
}

.mu-12__btn--primary {
  background: var(--mu-12-acc);
  border-color: var(--mu-12-acc);
  color: var(--mu-12-acc-ink);
  font-weight: 600;
}

.mu-12__overlay-demo {
  display: grid;
  gap: 0.875rem;
  min-inline-size: 0;
}

.mu-12__scrim {
  min-inline-size: 0;
  padding: 2rem 1rem;
  border-radius: 10px;
  background: var(--mu-12-scrim);
  display: grid;
  place-items: center;
}

.mu-12__dialog {
  min-inline-size: 0;
  inline-size: 100%;
  max-inline-size: 26rem;
  display: grid;
  gap: 0.625rem;
  padding: calc(1.5rem + var(--mu-12-pad-step) * 3);
  background: var(--mu-12-e3);
  border-radius: 12px;
  border-block-start: 1px solid var(--mu-12-edge);
}

@media (min-width: 48rem) {
  .mu-12__stage {
    padding-inline: 3rem;
  }

  .mu-12__level--0 {
    padding: 2rem;
  }

  .mu-12__level--1 {
    padding: calc(2rem + var(--mu-12-pad-step));
  }

  .mu-12__level--2 {
    padding: calc(2rem + var(--mu-12-pad-step) * 2);
  }

  .mu-12__scrim {
    padding: 3rem;
  }
}
```
