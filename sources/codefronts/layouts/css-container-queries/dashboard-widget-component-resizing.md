---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/dashboard-widget-component-resizing/"
title: "Dashboard Widget Component Resizing"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "One stat widget at three container widths: a sparkline plus delta at full width, a number and label at medium, and a bare number in the narrowest slot."
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dashboard Widget Component Resizing
Source: https://codefronts.com/layouts/css-container-queries/dashboard-widget-component-resizing/

One stat widget at three container widths: a sparkline plus delta at full width, a number and label at medium, and a bare number in the narrowest slot. The same component fills every dashboard slot, so the tile decides its own level of detail from the space it was given &mdash; no size prop, no variant class, no dashboard grid required.
## HTML
```html
<section class="cq-10" aria-labelledby="cq-10-h">
  <fieldset class="cq-10__theme">
    <legend class="cq-10__themelegend">Theme</legend>
    <input class="cq-10__themeinput" type="radio" name="cq-10-theme" id="cq-10-theme-auto" checked>
    <label class="cq-10__themeopt" for="cq-10-theme-auto">Auto</label>
    <input class="cq-10__themeinput" type="radio" name="cq-10-theme" id="cq-10-theme-light">
    <label class="cq-10__themeopt" for="cq-10-theme-light">Light</label>
    <input class="cq-10__themeinput" type="radio" name="cq-10-theme" id="cq-10-theme-dark">
    <label class="cq-10__themeopt" for="cq-10-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-10__stage">
    <header class="cq-10__head">
      <p class="cq-10__kicker">Meridian &middot; observability</p>
      <h2 class="cq-10__h" id="cq-10-h">One tile, three slot widths</h2>
    </header>

    <div class="cq-10__row">
      <div class="cq-10__cell cq-10__cell--lg">
        <p class="cq-10__slotlabel">26rem cell</p>
        <div class="cq-10__slot">
          <article class="cq-10__tile">
            <p class="cq-10__label">Median ingest latency</p>
            <p class="cq-10__figure">148<span class="cq-10__unit">ms</span></p>
            <p class="cq-10__delta"><span class="cq-10__arrow" aria-hidden="true">&darr;</span>12.4% vs last week</p>
            <svg class="cq-10__spark" viewBox="0 0 120 32" preserveAspectRatio="none" aria-hidden="true" focusable="false">
              <polyline points="0,26 12,22 24,25 36,17 48,19 60,13 72,15 84,9 96,11 108,6 120,8" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
            </svg>
            <p class="cq-10__foot">Rolling 7 days &middot; p50</p>
          </article>
        </div>
      </div>

      <div class="cq-10__cell cq-10__cell--md">
        <p class="cq-10__slotlabel">14rem cell</p>
        <div class="cq-10__slot">
          <article class="cq-10__tile">
            <p class="cq-10__label">Median ingest latency</p>
            <p class="cq-10__figure">148<span class="cq-10__unit">ms</span></p>
            <p class="cq-10__delta"><span class="cq-10__arrow" aria-hidden="true">&darr;</span>12.4% vs last week</p>
            <svg class="cq-10__spark" viewBox="0 0 120 32" preserveAspectRatio="none" aria-hidden="true" focusable="false">
              <polyline points="0,26 12,22 24,25 36,17 48,19 60,13 72,15 84,9 96,11 108,6 120,8" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
            </svg>
            <p class="cq-10__foot">Rolling 7 days &middot; p50</p>
          </article>
        </div>
      </div>

      <div class="cq-10__cell cq-10__cell--sm">
        <p class="cq-10__slotlabel">8rem cell</p>
        <div class="cq-10__slot">
          <article class="cq-10__tile">
            <p class="cq-10__label">Median ingest latency</p>
            <p class="cq-10__figure">148<span class="cq-10__unit">ms</span></p>
            <p class="cq-10__delta"><span class="cq-10__arrow" aria-hidden="true">&darr;</span>12.4% vs last week</p>
            <svg class="cq-10__spark" viewBox="0 0 120 32" preserveAspectRatio="none" aria-hidden="true" focusable="false">
              <polyline points="0,26 12,22 24,25 36,17 48,19 60,13 72,15 84,9 96,11 108,6 120,8" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>
            </svg>
            <p class="cq-10__foot">Rolling 7 days &middot; p50</p>
          </article>
        </div>
      </div>
    </div>

    <p class="cq-10__note">Identical markup in all three cells. The tile discloses the label at 11em and the sparkline at 20em.</p>
  </div>
</section>
```
## CSS
```css
.cq-10,
.cq-10[data-theme="dark"] {
  --bg: #0c0f11;
  --surf: #14181b;
  --surf2: #1a1f23;
  --line: #262d32;
  --ink: #e8eef0;
  --mut: #8b979d;
  --acc: #2fd6a5;
  --bloom: rgba(47, 214, 165, 0.14);
}

.cq-10[data-theme="light"] {
  --bg: #f2f5f5;
  --surf: #ffffff;
  --surf2: #eaefef;
  --line: #d5dddd;
  --ink: #0c1416;
  --mut: #55676c;
  --acc: #0f8f6c;
  --bloom: rgba(15, 143, 108, 0.1);
}

@media (prefers-color-scheme: light) {
  .cq-10:not([data-theme="dark"]) {
    --bg: #f2f5f5;
    --surf: #ffffff;
    --surf2: #eaefef;
    --line: #d5dddd;
    --ink: #0c1416;
    --mut: #55676c;
    --acc: #0f8f6c;
    --bloom: rgba(15, 143, 108, 0.1);
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .cq-10,
    .cq-10[data-theme="dark"] {
    --acc: oklch(0.8 0.14 168);
  }

  .cq-10[data-theme="light"] {
    --acc: oklch(0.56 0.12 168);
  }

  @media (prefers-color-scheme: light) {
    .cq-10:not([data-theme="dark"]) {
      --acc: oklch(0.56 0.12 168);
    }
  }
}

.cq-10 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: ui-monospace, "SF Mono", "JetBrains Mono", Menlo, Consolas, monospace;
  line-height: 1.4;
}

.cq-10 *,
.cq-10 *::before,
.cq-10 *::after {
  box-sizing: border-box;
}

.cq-10__stage {
  max-width: 72rem;
  margin-inline: auto;
  padding: clamp(0.85rem, 3vw, 2.25rem);
  display: grid;
  gap: 1rem;
}

.cq-10__kicker {
  margin: 0 0 0.3rem;
  font-size: 0.68rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--acc);
}

.cq-10__h {
  margin: 0;
  font-size: clamp(1.15rem, 0.95rem + 1.4vw, 1.6rem);
  font-weight: 600;
  letter-spacing: -0.01em;
}

.cq-10__row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  align-items: start;
}

.cq-10__cell {
  min-inline-size: 0;
  display: grid;
  gap: 0.35rem;
}

.cq-10__cell--lg {
  flex: 1 1 26rem;
}

.cq-10__cell--md {
  flex: 0 1 14rem;
}

.cq-10__cell--sm {
  flex: 0 1 8rem;
}

.cq-10__slotlabel {
  margin: 0;
  font-size: 0.64rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--mut);
}

.cq-10__slot {
  container: cq-10-tile / inline-size;
}

.cq-10__tile {
  display: grid;
  gap: 0.25rem;
  padding: 0.75rem;
  background: var(--surf);
  border: 1px solid var(--line);
  border-radius: 6px;
  box-shadow: 0 0 0 1px var(--bloom), 0 6px 24px var(--bloom);
  color: var(--ink);
}

.cq-10__label {
  display: none;
  margin: 0;
  font-size: 0.68rem;
  letter-spacing: 0.04em;
  color: var(--mut);
}

.cq-10__figure {
  margin: 0;
  font-size: 1.65rem;
  font-weight: 600;
  letter-spacing: -0.03em;
  font-variant-numeric: tabular-nums;
  line-height: 1.05;
}

.cq-10__unit {
  font-size: 0.7em;
  color: var(--mut);
  margin-inline-start: 0.1em;
}

.cq-10__delta {
  display: none;
  margin: 0;
  font-size: 0.7rem;
  color: var(--acc);
  font-variant-numeric: tabular-nums;
}

.cq-10__arrow {
  margin-inline-end: 0.2rem;
}

.cq-10__spark {
  display: none;
  inline-size: 100%;
  block-size: 2.75rem;
  color: var(--acc);
  margin-top: 0.35rem;
}

.cq-10__foot {
  display: none;
  margin: 0;
  font-size: 0.62rem;
  letter-spacing: 0.06em;
  color: var(--mut);
  border-top: 1px solid var(--line);
  padding-top: 0.4rem;
}

@container cq-10-tile (min-width: 11em) {
  .cq-10__label,
    .cq-10__delta {
    display: block;
  }

  .cq-10__tile {
    padding: 0.9rem;
    gap: 0.3rem;
  }

  .cq-10__figure {
    font-size: 2rem;
  }
}

@container cq-10-tile (min-width: 20em) {
  .cq-10__spark,
    .cq-10__foot {
    display: block;
  }

  .cq-10__tile {
    padding: 1.1rem;
    background: var(--surf2);
  }

  .cq-10__figure {
    font-size: 2.75rem;
  }

  .cq-10__label {
    font-size: 0.74rem;
  }
}

.cq-10__note {
  margin: 0;
  padding-top: 0.75rem;
  border-top: 1px solid var(--line);
  font-size: 0.7rem;
  color: var(--mut);
  max-width: 70ch;
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. The
   pinned values are the demo's own [data-theme] declarations reused
   verbatim, so a toggled demo can never drift from how the same demo
   renders under the site theme. */

.cq-10 {
  position: relative;
}

.cq-10__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 9;
  display: flex;
  align-items: center;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 8%, transparent);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  font-family: system-ui, sans-serif;
}

.cq-10__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-10__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-10__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.6875rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: inherit;
  opacity: 0.55;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}

.cq-10__themeopt:hover {
  opacity: 0.85;
}

.cq-10__themeinput:checked + .cq-10__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-10__themeinput:focus-visible + .cq-10__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-10:has(#cq-10-theme-light:checked) {
  --bg: #f2f5f5;
  --surf: #ffffff;
  --surf2: #eaefef;
  --line: #d5dddd;
  --ink: #0c1416;
  --mut: #55676c;
  --acc: #0f8f6c;
  --bloom: rgba(15, 143, 108, 0.1);
}

.cq-10:has(#cq-10-theme-dark:checked) {
  --bg: #0c0f11;
  --surf: #14181b;
  --surf2: #1a1f23;
  --line: #262d32;
  --ink: #e8eef0;
  --mut: #8b979d;
  --acc: #2fd6a5;
  --bloom: rgba(47, 214, 165, 0.14);
}
```
