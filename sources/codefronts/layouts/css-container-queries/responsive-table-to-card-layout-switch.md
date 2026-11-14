---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/responsive-table-to-card-layout-switch/"
title: "Responsive Table to Card Layout Switch"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "Tabular data that becomes a stack of labelled cards when its container is narrow, with the label for each value coming from ::before and a data- attribute."
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Table to Card Layout Switch
Source: https://codefronts.com/layouts/css-container-queries/responsive-table-to-card-layout-switch/

Tabular data that becomes a stack of labelled cards when its container is narrow, with the label for each value coming from ::before and a data- attribute. The accessibility tradeoff is stated rather than skipped: changing display on table elements removes the implicit table semantics, so this demo keeps the real markup and accepts the loss deliberately.
## HTML
```html
<section class="cq-15" aria-labelledby="cq-15-h">
  <fieldset class="cq-15__theme">
    <legend class="cq-15__themelegend">Theme</legend>
    <input class="cq-15__themeinput" type="radio" name="cq-15-theme" id="cq-15-theme-auto" checked>
    <label class="cq-15__themeopt" for="cq-15-theme-auto">Auto</label>
    <input class="cq-15__themeinput" type="radio" name="cq-15-theme" id="cq-15-theme-light">
    <label class="cq-15__themeopt" for="cq-15-theme-light">Light</label>
    <input class="cq-15__themeinput" type="radio" name="cq-15-theme" id="cq-15-theme-dark">
    <label class="cq-15__themeopt" for="cq-15-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-15__stage">
    <header class="cq-15__head">
      <h2 class="cq-15__h" id="cq-15-h">Table, then cards</h2>
      <p class="cq-15__lede">Same table in a wide region and a narrow one. Below 34em the rows become labelled cards.</p>
    </header>

    <div class="cq-15__row">
      <div class="cq-15__wrap cq-15__wrap--wide">
        <p class="cq-15__w">wide container</p>
        <table class="cq-15__table">
          <caption class="cq-15__cap">Aperture Freight &middot; open shipments</caption>
          <thead>
            <tr><th scope="col">Reference</th><th scope="col">Route</th><th scope="col">Weight</th><th scope="col">Status</th></tr>
          </thead>
          <tbody>
            <tr>
              <td data-label="Reference"><span class="cq-15__ref">APF-40912</span></td>
              <td data-label="Route">Rotterdam &rarr; Leeds</td>
              <td data-label="Weight" class="cq-15__num">18,400 kg</td>
              <td data-label="Status"><span class="cq-15__pill cq-15__pill--ok">In transit</span></td>
            </tr>
            <tr>
              <td data-label="Reference"><span class="cq-15__ref">APF-40918</span></td>
              <td data-label="Route">Bilbao &rarr; Bristol</td>
              <td data-label="Weight" class="cq-15__num">6,120 kg</td>
              <td data-label="Status"><span class="cq-15__pill cq-15__pill--warn">Held at customs</span></td>
            </tr>
            <tr>
              <td data-label="Reference"><span class="cq-15__ref">APF-40930</span></td>
              <td data-label="Route">Gdansk &rarr; Hull</td>
              <td data-label="Weight" class="cq-15__num">24,860 kg</td>
              <td data-label="Status"><span class="cq-15__pill cq-15__pill--ok">In transit</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="cq-15__wrap cq-15__wrap--narrow">
        <p class="cq-15__w">narrow container</p>
        <table class="cq-15__table">
          <caption class="cq-15__cap">Aperture Freight &middot; open shipments</caption>
          <thead>
            <tr><th scope="col">Reference</th><th scope="col">Route</th><th scope="col">Weight</th><th scope="col">Status</th></tr>
          </thead>
          <tbody>
            <tr>
              <td data-label="Reference"><span class="cq-15__ref">APF-40912</span></td>
              <td data-label="Route">Rotterdam &rarr; Leeds</td>
              <td data-label="Weight" class="cq-15__num">18,400 kg</td>
              <td data-label="Status"><span class="cq-15__pill cq-15__pill--ok">In transit</span></td>
            </tr>
            <tr>
              <td data-label="Reference"><span class="cq-15__ref">APF-40918</span></td>
              <td data-label="Route">Bilbao &rarr; Bristol</td>
              <td data-label="Weight" class="cq-15__num">6,120 kg</td>
              <td data-label="Status"><span class="cq-15__pill cq-15__pill--warn">Held at customs</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <p class="cq-15__note">Card mode keeps the <code>&lt;table&gt;</code> markup and accepts that the display switch drops row and column association for screen readers &mdash; the <code>data-label</code> text carries the column name instead. Add explicit ARIA table roles if you need the structure preserved.</p>
  </div>
</section>
```
## CSS
```css
.cq-15,
.cq-15[data-theme="light"] {
  --bg: #f7f6f2;
  --surf: #ffffff;
  --line: #ddd9cf;
  --line2: #c7c2b5;
  --ink: #191713;
  --mut: #5e594f;
  --ok: #1f6f43;
  --warn: #9a5b0c;
}

.cq-15[data-theme="dark"] {
  --bg: #12110f;
  --surf: #1a1917;
  --line: #2e2c28;
  --line2: #423f39;
  --ink: #f3f1ec;
  --mut: #a29c91;
  --ok: #6cc48f;
  --warn: #e5a24d;
}

@media (prefers-color-scheme: dark) {
  .cq-15:not([data-theme="light"]) {
    --bg: #12110f;
    --surf: #1a1917;
    --line: #2e2c28;
    --line2: #423f39;
    --ink: #f3f1ec;
    --mut: #a29c91;
    --ok: #6cc48f;
    --warn: #e5a24d;
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .cq-15,
    .cq-15[data-theme="light"] {
    --ok: oklch(0.48 0.11 155);
    --warn: oklch(0.55 0.13 65);
  }

  .cq-15[data-theme="dark"] {
    --ok: oklch(0.78 0.12 155);
    --warn: oklch(0.78 0.12 70);
  }

  @media (prefers-color-scheme: dark) {
    .cq-15:not([data-theme="light"]) {
      --ok: oklch(0.78 0.12 155);
      --warn: oklch(0.78 0.12 70);
    }
  }
}

.cq-15 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: "Segoe UI", Tahoma, Verdana, system-ui, sans-serif;
  font-size: 100%;
  line-height: 1.35;
}

.cq-15 *,
.cq-15 *::before,
.cq-15 *::after {
  box-sizing: border-box;
}

.cq-15__stage {
  max-width: 74rem;
  margin-inline: auto;
  padding: clamp(0.9rem, 3vw, 2.25rem);
  display: grid;
  gap: 1rem;
}

.cq-15__h {
  margin: 0;
  font-size: clamp(1.25rem, 1.05rem + 1.4vw, 1.8rem);
  font-weight: 600;
  letter-spacing: -0.01em;
}

.cq-15__lede {
  margin: 0.3rem 0 0;
  font-size: 0.84rem;
  color: var(--mut);
  max-width: 56ch;
}

.cq-15__row {
  display: flex;
  flex-wrap: wrap;
  gap: 1.25rem;
  align-items: start;
}

.cq-15__wrap {
  container: cq-15-wrap / inline-size;
  min-inline-size: 0;
  display: grid;
  gap: 0.4rem;
}

.cq-15__wrap--wide {
  flex: 1 1 30rem;
}

.cq-15__wrap--narrow {
  flex: 0 1 17rem;
}

.cq-15__w {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.64rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--mut);
}

.cq-15__table {
  inline-size: 100%;
  border-collapse: collapse;
  background: var(--surf);
  border: 1px solid var(--line2);
  font-size: 0.8rem;
}

.cq-15__cap {
  caption-side: top;
  text-align: start;
  padding: 0.4rem 0.5rem;
  font-size: 0.7rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--mut);
}

.cq-15__table th,
.cq-15__table td {
  padding: 0.4rem 0.5rem;
  text-align: start;
  border-block-end: 1px solid var(--line);
  vertical-align: top;
}

.cq-15__table th {
  font-size: 0.68rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--mut);
  border-block-end: 1px solid var(--line2);
  white-space: nowrap;
}

.cq-15__table tbody tr:last-child td {
  border-block-end: 0;
}

.cq-15__ref {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.78rem;
}

.cq-15__num {
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}

.cq-15__pill {
  display: inline-flex;
  width: fit-content;
  align-items: center;
  padding: 0.1rem 0.4rem;
  border-radius: 3px;
  font-size: 0.7rem;
  font-weight: 600;
  border: 1px solid currentColor;
}

.cq-15__pill--ok {
  color: var(--ok);
}

.cq-15__pill--warn {
  color: var(--warn);
}

.cq-15__table td::before {
  content: none;
}

@container cq-15-wrap (max-width: 34em) {
  .cq-15__table {
    border: 0;
    background: transparent;
  }

  .cq-15__table thead {
    display: none;
  }

  .cq-15__table tbody {
    display: grid;
    gap: 0.5rem;
  }

  .cq-15__table tr {
    display: grid;
    gap: 0.15rem;
    padding: 0.5rem 0.6rem;
    background: var(--surf);
    border: 1px solid var(--line2);
  }

  .cq-15__table td {
    display: grid;
    grid-template-columns: 5.5rem minmax(0, 1fr);
    gap: 0.5rem;
    padding: 0.15rem 0;
    border: 0;
  }

  .cq-15__table td::before {
    content: attr(data-label);
    font-size: 0.66rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--mut);
  }

  .cq-15__table tbody tr:last-child td {
    border: 0;
  }
}

.cq-15__note {
  margin: 0;
  padding-top: 0.8rem;
  border-top: 1px solid var(--line2);
  font-size: 0.76rem;
  color: var(--mut);
  max-width: 74ch;
}

.cq-15__note code {
  font-family: ui-monospace, Menlo, monospace;
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. The
   pinned values are the demo's own [data-theme] declarations reused
   verbatim, so a toggled demo can never drift from how the same demo
   renders under the site theme. */

.cq-15 {
  position: relative;
}

.cq-15__theme {
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

.cq-15__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-15__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-15__themeopt {
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

.cq-15__themeopt:hover {
  opacity: 0.85;
}

.cq-15__themeinput:checked + .cq-15__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-15__themeinput:focus-visible + .cq-15__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-15:has(#cq-15-theme-light:checked) {
  --bg: #f7f6f2;
  --surf: #ffffff;
  --line: #ddd9cf;
  --line2: #c7c2b5;
  --ink: #191713;
  --mut: #5e594f;
  --ok: #1f6f43;
  --warn: #9a5b0c;
}

.cq-15:has(#cq-15-theme-dark:checked) {
  --bg: #12110f;
  --surf: #1a1917;
  --line: #2e2c28;
  --line2: #423f39;
  --ink: #f3f1ec;
  --mut: #a29c91;
  --ok: #6cc48f;
  --warn: #e5a24d;
}
```
