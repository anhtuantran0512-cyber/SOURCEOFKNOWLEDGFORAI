---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/fluid-typography-with-container-units/"
title: "Fluid Typography with Container Units"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "Type that scales with its container instead of the window: clamp(1.05rem, 4cqi, 2.1rem) beside clamp(1.05rem, 4vw, 2.1rem) in two identical narrow cards, so…"
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fluid Typography with Container Units
Source: https://codefronts.com/layouts/css-container-queries/fluid-typography-with-container-units/

Type that scales with its container instead of the window: clamp(1.05rem, 4cqi, 2.1rem) beside clamp(1.05rem, 4vw, 2.1rem) in two identical narrow cards, so the difference is visible rather than asserted. The vw version is sized by a window it knows nothing about; the cqi version is sized by the card it actually lives in.
## HTML
```html
<section class="cq-09" aria-labelledby="cq-09-h">
  <fieldset class="cq-09__theme">
    <legend class="cq-09__themelegend">Theme</legend>
    <input class="cq-09__themeinput" type="radio" name="cq-09-theme" id="cq-09-theme-auto" checked>
    <label class="cq-09__themeopt" for="cq-09-theme-auto">Auto</label>
    <input class="cq-09__themeinput" type="radio" name="cq-09-theme" id="cq-09-theme-light">
    <label class="cq-09__themeopt" for="cq-09-theme-light">Light</label>
    <input class="cq-09__themeinput" type="radio" name="cq-09-theme" id="cq-09-theme-dark">
    <label class="cq-09__themeopt" for="cq-09-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-09__stage">
    <header class="cq-09__head">
      <p class="cq-09__kicker">Type &amp; measure</p>
      <h2 class="cq-09__h" id="cq-09-h">Sized by the card, not the window</h2>
      <p class="cq-09__lede">Two identical cards, one declaration apart. Widen the browser and watch only one of them lose its proportions.</p>
    </header>

    <div class="cq-09__row">
      <figure class="cq-09__fig">
        <div class="cq-09__card">
          <p class="cq-09__eyebrow">Essay</p>
          <h3 class="cq-09__title cq-09__title--cq">The quiet return of the small page</h3>
          <p class="cq-09__body">Reading room design went wide for a decade. The interesting work went back to the column.</p>
        </div>
        <figcaption><code>clamp(1.05rem, 4cqi, 2.1rem)</code> &mdash; reads the card</figcaption>
      </figure>

      <figure class="cq-09__fig">
        <div class="cq-09__card">
          <p class="cq-09__eyebrow">Essay</p>
          <h3 class="cq-09__title cq-09__title--vw">The quiet return of the small page</h3>
          <p class="cq-09__body">Reading room design went wide for a decade. The interesting work went back to the column.</p>
        </div>
        <figcaption class="cq-09__bad"><code>clamp(1.05rem, 4vw, 2.1rem)</code> &mdash; reads the window</figcaption>
      </figure>
    </div>

    <figure class="cq-09__fig cq-09__fig--wide">
      <div class="cq-09__card cq-09__card--resize">
        <p class="cq-09__eyebrow">Drag the right edge</p>
        <h3 class="cq-09__title cq-09__title--cq">Every heading here is one declaration</h3>
        <p class="cq-09__body">The container changes width, the type follows, and the paragraph stays in rem so text settings still apply.</p>
      </div>
      <figcaption>Same rule, driven by hand with <code>resize: horizontal</code></figcaption>
    </figure>
  </div>
</section>
```
## CSS
```css
.cq-09,
.cq-09[data-theme="light"] {
  --bg: #fbfaf7;
  --ink: #14120e;
  --mut: #635c50;
  --line: #ddd6c8;
  --acc: #a86a10;
  --bad: #a3341f;
}

.cq-09[data-theme="dark"] {
  --bg: #100f0c;
  --ink: #f5f2ea;
  --mut: #a49b8a;
  --line: #34302a;
  --acc: #f0b95e;
  --bad: #f08a72;
}

@media (prefers-color-scheme: dark) {
  .cq-09:not([data-theme="light"]) {
    --bg: #100f0c;
    --ink: #f5f2ea;
    --mut: #a49b8a;
    --line: #34302a;
    --acc: #f0b95e;
    --bad: #f08a72;
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .cq-09,
    .cq-09[data-theme="light"] {
    --acc: oklch(0.58 0.12 68);
    --bad: oklch(0.5 0.16 30);
  }

  .cq-09[data-theme="dark"] {
    --acc: oklch(0.82 0.13 78);
    --bad: oklch(0.72 0.14 32);
  }

  @media (prefers-color-scheme: dark) {
    .cq-09:not([data-theme="light"]) {
      --acc: oklch(0.82 0.13 78);
      --bad: oklch(0.72 0.14 32);
    }
  }
}

.cq-09 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: Georgia, "Iowan Old Style", "Times New Roman", serif;
  line-height: 1.6;
}

.cq-09 *,
.cq-09 *::before,
.cq-09 *::after {
  box-sizing: border-box;
}

.cq-09__stage {
  max-width: 62rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem);
  display: grid;
  gap: 2rem;
}

.cq-09__kicker {
  margin: 0 0 0.5rem;
  font-family: system-ui, sans-serif;
  font-size: 0.7rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--acc);
}

.cq-09__h {
  margin: 0;
  font-size: clamp(1.6rem, 1.2rem + 2.4vw, 2.6rem);
  font-weight: 400;
  line-height: 1.15;
  letter-spacing: -0.015em;
  text-wrap: balance;
}

.cq-09__lede {
  margin: 0.6rem 0 0;
  color: var(--mut);
  font-size: 1rem;
  max-width: 46ch;
}

.cq-09__row {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
}

.cq-09__fig {
  margin: 0;
  flex: 0 1 17rem;
  min-inline-size: 0;
  display: grid;
  gap: 0.6rem;
}

.cq-09__fig--wide {
  flex: 1 1 100%;
}

.cq-09__fig figcaption {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.7rem;
  color: var(--mut);
  padding-top: 0.5rem;
  border-top: 1px solid var(--line);
  overflow-wrap: anywhere;
}

.cq-09__bad {
  color: var(--bad);
}

.cq-09__card {
  container: cq-09-card / inline-size;
  padding: 1.25rem;
  border-inline-start: 2px solid var(--line);
}

.cq-09__card--resize {
  resize: horizontal;
  overflow: auto;
  min-inline-size: 12rem;
  max-inline-size: 100%;
  border: 1px dashed var(--line);
  border-inline-start-width: 2px;
  border-inline-start-style: solid;
}

.cq-09__eyebrow {
  margin: 0 0 0.35rem;
  font-family: system-ui, sans-serif;
  font-size: 0.68rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--acc);
}

.cq-09__title {
  margin: 0 0 0.5rem;
  font-weight: 400;
  line-height: 1.12;
  letter-spacing: -0.01em;
  text-wrap: balance;
}

.cq-09__title--cq {
  font-size: 1.35rem;
  font-size: clamp(1.05rem, 4cqi, 2.1rem);
}

.cq-09__title--vw {
  font-size: 1.35rem;
  font-size: clamp(1.05rem, 4vw, 2.1rem);
}

.cq-09__body {
  margin: 0;
  font-size: 0.95rem;
  color: var(--mut);
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. The
   pinned values are the demo's own [data-theme] declarations reused
   verbatim, so a toggled demo can never drift from how the same demo
   renders under the site theme. */

.cq-09 {
  position: relative;
}

.cq-09__theme {
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

.cq-09__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-09__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-09__themeopt {
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

.cq-09__themeopt:hover {
  opacity: 0.85;
}

.cq-09__themeinput:checked + .cq-09__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-09__themeinput:focus-visible + .cq-09__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-09:has(#cq-09-theme-light:checked) {
  --bg: #fbfaf7;
  --ink: #14120e;
  --mut: #635c50;
  --line: #ddd6c8;
  --acc: #a86a10;
  --bad: #a3341f;
}

.cq-09:has(#cq-09-theme-dark:checked) {
  --bg: #100f0c;
  --ink: #f5f2ea;
  --mut: #a49b8a;
  --line: #34302a;
  --acc: #f0b95e;
  --bad: #f08a72;
}
```
