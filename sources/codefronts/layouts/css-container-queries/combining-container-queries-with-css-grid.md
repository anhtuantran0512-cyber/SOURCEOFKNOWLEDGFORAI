---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/combining-container-queries-with-css-grid/"
title: "Combining Container Queries with CSS Grid"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "auto-fit with minmax() decides how many columns fit; a container query on each item decides what each item looks like at the width it got."
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Combining Container Queries with CSS Grid
Source: https://codefronts.com/layouts/css-container-queries/combining-container-queries-with-css-grid/

auto-fit with minmax() decides how many columns fit; a container query on each item decides what each item looks like at the width it got. They answer different questions and compose cleanly. Not a Grid tutorial &mdash; the subject is the interaction, and the trap named at the end is putting container-type on the grid instead of the items.
## HTML
```html
<section class="cq-19" aria-labelledby="cq-19-h">
  <fieldset class="cq-19__theme">
    <legend class="cq-19__themelegend">Theme</legend>
    <input class="cq-19__themeinput" type="radio" name="cq-19-theme" id="cq-19-theme-auto" checked>
    <label class="cq-19__themeopt" for="cq-19-theme-auto">Auto</label>
    <input class="cq-19__themeinput" type="radio" name="cq-19-theme" id="cq-19-theme-light">
    <label class="cq-19__themeopt" for="cq-19-theme-light">Light</label>
    <input class="cq-19__themeinput" type="radio" name="cq-19-theme" id="cq-19-theme-dark">
    <label class="cq-19__themeopt" for="cq-19-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-19__stage">
    <header class="cq-19__head">
      <h2 class="cq-19__h" id="cq-19-h">auto-fit counts columns, the query styles items</h2>
      <p class="cq-19__lede">One set of rules, two boards. The grid decides how many; each item decides how it looks.</p>
    </header>

    <section class="cq-19__block" aria-label="Wide board">
      <p class="cq-19__blabel">Board A &middot; wide &middot; <code>repeat(auto-fit, minmax(14rem, 1fr))</code></p>
      <ul class="cq-19__board">
        <li class="cq-19__cell">
          <article class="cq-19__item">
            <span class="cq-19__mark cq-19__mark--a" aria-hidden="true"></span>
            <div class="cq-19__body"><h3>Deploy queue</h3><p>4 waiting &middot; 1 running</p></div>
          </article>
        </li>
        <li class="cq-19__cell">
          <article class="cq-19__item">
            <span class="cq-19__mark cq-19__mark--b" aria-hidden="true"></span>
            <div class="cq-19__body"><h3>Error budget</h3><p>62% remaining this month</p></div>
          </article>
        </li>
        <li class="cq-19__cell">
          <article class="cq-19__item">
            <span class="cq-19__mark cq-19__mark--c" aria-hidden="true"></span>
            <div class="cq-19__body"><h3>Open incidents</h3><p>None since 14 August</p></div>
          </article>
        </li>
      </ul>
    </section>

    <section class="cq-19__block" aria-label="Narrow board">
      <p class="cq-19__blabel">Board B &middot; narrow &middot; same rules, fewer columns</p>
      <ul class="cq-19__board cq-19__board--narrow">
        <li class="cq-19__cell">
          <article class="cq-19__item">
            <span class="cq-19__mark cq-19__mark--a" aria-hidden="true"></span>
            <div class="cq-19__body"><h3>Deploy queue</h3><p>4 waiting &middot; 1 running</p></div>
          </article>
        </li>
        <li class="cq-19__cell">
          <article class="cq-19__item">
            <span class="cq-19__mark cq-19__mark--b" aria-hidden="true"></span>
            <div class="cq-19__body"><h3>Error budget</h3><p>62% remaining this month</p></div>
          </article>
        </li>
      </ul>
    </section>

    <section class="cq-19__block cq-19__block--trap" aria-label="The trap">
      <p class="cq-19__blabel cq-19__blabel--trap">Trap &middot; <code>container-type</code> on the board, not the items</p>
      <ul class="cq-19__board cq-19__board--trap">
        <li class="cq-19__cell cq-19__cell--flat">
          <article class="cq-19__item"><span class="cq-19__mark cq-19__mark--d" aria-hidden="true"></span><div class="cq-19__body"><h3>Deploy queue</h3><p>Both items measure the board</p></div></article>
        </li>
        <li class="cq-19__cell cq-19__cell--flat">
          <article class="cq-19__item"><span class="cq-19__mark cq-19__mark--d" aria-hidden="true"></span><div class="cq-19__body"><h3>Error budget</h3><p>so both get the same answer</p></div></article>
        </li>
      </ul>
    </section>
  </div>
</section>
```
## CSS
```css
.cq-19,
.cq-19[data-theme="light"] {
  --bg: #f6f5f1;
  --surf: #ffffff;
  --line: #d5d2c8;
  --ink: #191814;
  --mut: #5d5a51;
  --a1: #1f6f8b;
  --a2: #8b5cf6;
  --a3: #d97706;
  --bad: #b3261e;
}

.cq-19[data-theme="dark"] {
  --bg: #14140f;
  --surf: #1d1d17;
  --line: #333229;
  --ink: #f2f1e9;
  --mut: #a09d92;
  --a1: #5cc6e8;
  --a2: #c4a9ff;
  --a3: #f5b342;
  --bad: #ff7a70;
}

@media (prefers-color-scheme: dark) {
  .cq-19:not([data-theme="light"]) {
    --bg: #14140f;
    --surf: #1d1d17;
    --line: #333229;
    --ink: #f2f1e9;
    --mut: #a09d92;
    --a1: #5cc6e8;
    --a2: #c4a9ff;
    --a3: #f5b342;
    --bad: #ff7a70;
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .cq-19,
    .cq-19[data-theme="light"] {
    --a1: oklch(0.52 0.1 220);
    --a2: oklch(0.6 0.2 295);
    --a3: oklch(0.62 0.16 60);
  }

  .cq-19[data-theme="dark"] {
    --a1: oklch(0.8 0.11 220);
    --a2: oklch(0.8 0.13 295);
    --a3: oklch(0.82 0.14 70);
  }

  @media (prefers-color-scheme: dark) {
    .cq-19:not([data-theme="light"]) {
      --a1: oklch(0.8 0.11 220);
      --a2: oklch(0.8 0.13 295);
      --a3: oklch(0.82 0.14 70);
    }
  }
}

.cq-19 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", Helvetica, sans-serif;
  line-height: 1.45;
}

.cq-19 *,
.cq-19 *::before,
.cq-19 *::after {
  box-sizing: border-box;
}

.cq-19__stage {
  max-width: 74rem;
  margin-inline: auto;
  padding: clamp(1rem, 3vw, 2.5rem);
  display: grid;
  gap: 1.5rem;
}

.cq-19__h {
  margin: 0;
  font-size: clamp(1.25rem, 1.05rem + 1.5vw, 1.85rem);
  font-weight: 650;
  letter-spacing: -0.02em;
}

.cq-19__lede {
  margin: 0.35rem 0 0;
  font-size: 0.86rem;
  color: var(--mut);
  max-width: 56ch;
}

.cq-19__block {
  display: grid;
  gap: 0.6rem;
}

.cq-19__blabel {
  margin: 0;
  padding-block-end: 0.4rem;
  border-block-end: 1px solid var(--line);
  font-size: 0.72rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--mut);
}

.cq-19__blabel code {
  font-family: ui-monospace, Menlo, monospace;
  text-transform: none;
  letter-spacing: 0;
}

.cq-19__blabel--trap {
  color: var(--bad);
  border-block-end-color: var(--bad);
}

.cq-19__board {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(14rem, 100%), 1fr));
  gap: 1rem;
}

.cq-19__board--narrow {
  max-inline-size: 28rem;
}

.cq-19__board--trap {
  container: cq-19-board / inline-size;
  max-inline-size: 40rem;
}

.cq-19__cell {
  container: cq-19-item / inline-size;
  min-inline-size: 0;
}

.cq-19__cell--flat {
  container-type: normal;
}

.cq-19__item {
  display: grid;
  gap: 0.5rem;
  padding: 0.85rem;
  background: var(--surf);
  border: 1px solid var(--line);
}

.cq-19__mark {
  inline-size: 100%;
  block-size: 0.35rem;
  border-radius: 2px;
  background: var(--a1);
}

.cq-19__mark--b {
  background: var(--a2);
}

.cq-19__mark--c {
  background: var(--a3);
}

.cq-19__mark--d {
  background: var(--bad);
}

.cq-19__body {
  min-inline-size: 0;
}

.cq-19__item h3 {
  margin: 0 0 0.15rem;
  font-size: 0.95rem;
  font-weight: 650;
}

.cq-19__item p {
  margin: 0;
  font-size: 0.8rem;
  color: var(--mut);
}

@container cq-19-item (min-width: 18em) {
  .cq-19__item {
    grid-template-columns: 0.35rem minmax(0, 1fr);
    align-items: stretch;
    gap: 0.85rem;
    padding: 1.1rem;
  }

  .cq-19__mark {
    inline-size: 0.35rem;
    block-size: 100%;
  }

  .cq-19__item h3 {
    font-size: 1.1rem;
  }
}

@container cq-19-board (min-width: 30em) {
  .cq-19__board--trap .cq-19__item {
    border-color: var(--bad);
  }
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. The
   pinned values are the demo's own [data-theme] declarations reused
   verbatim, so a toggled demo can never drift from how the same demo
   renders under the site theme. */

.cq-19 {
  position: relative;
}

.cq-19__theme {
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

.cq-19__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-19__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-19__themeopt {
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

.cq-19__themeopt:hover {
  opacity: 0.85;
}

.cq-19__themeinput:checked + .cq-19__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-19__themeinput:focus-visible + .cq-19__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-19:has(#cq-19-theme-light:checked) {
  --bg: #f6f5f1;
  --surf: #ffffff;
  --line: #d5d2c8;
  --ink: #191814;
  --mut: #5d5a51;
  --a1: #1f6f8b;
  --a2: #8b5cf6;
  --a3: #d97706;
  --bad: #b3261e;
}

.cq-19:has(#cq-19-theme-dark:checked) {
  --bg: #14140f;
  --surf: #1d1d17;
  --line: #333229;
  --ink: #f2f1e9;
  --mut: #a09d92;
  --a1: #5cc6e8;
  --a2: #c4a9ff;
  --a3: #f5b342;
  --bad: #ff7a70;
}
```
