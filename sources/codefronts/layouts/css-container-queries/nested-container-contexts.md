---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/nested-container-contexts/"
title: "Nested Container Contexts"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "A container inside a container, and the resolution rule that governs it: an unnamed &#64;container matches the nearest ancestor that establishes a context,…"
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Nested Container Contexts
Source: https://codefronts.com/layouts/css-container-queries/nested-container-contexts/

A container inside a container, and the resolution rule that governs it: an unnamed &#64;container matches the nearest ancestor that establishes a context, so a nested container shadows its parent for unnamed queries below it. The diagram shows the surprise first &mdash; a query meant for the outer container answering from the inner &mdash; then the fix.
## HTML
```html
<section class="cq-17" aria-labelledby="cq-17-h">
  <fieldset class="cq-17__theme">
    <legend class="cq-17__themelegend">Theme</legend>
    <input class="cq-17__themeinput" type="radio" name="cq-17-theme" id="cq-17-theme-auto" checked>
    <label class="cq-17__themeopt" for="cq-17-theme-auto">Auto</label>
    <input class="cq-17__themeinput" type="radio" name="cq-17-theme" id="cq-17-theme-light">
    <label class="cq-17__themeopt" for="cq-17-theme-light">Light</label>
    <input class="cq-17__themeinput" type="radio" name="cq-17-theme" id="cq-17-theme-dark">
    <label class="cq-17__themeopt" for="cq-17-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-17__stage">
    <header class="cq-17__head">
      <h2 class="cq-17__h" id="cq-17-h">Resolution stops at the nearest container</h2>
      <p class="cq-17__lede">Both panels have the same ancestor chain. The left query is unnamed, so it never sees the shell.</p>
    </header>

    <ol class="cq-17__chain">
      <li><span class="cq-17__lv">shell</span><code>container: cq-17-shell / inline-size</code><b>wide</b></li>
      <li><span class="cq-17__lv cq-17__lv--b">panel</span><code>container-type: inline-size</code><b>17em</b></li>
      <li><span class="cq-17__lv cq-17__lv--c">row</span><code>the element being styled</code><b>&mdash;</b></li>
    </ol>

    <div class="cq-17__row">
      <section class="cq-17__shell" aria-label="Unnamed query">
        <p class="cq-17__cap">unnamed &middot; <code>&#64;container (min-width: 22em)</code></p>
        <div class="cq-17__panel">
          <p class="cq-17__pw">panel &middot; 17em &mdash; the nearest container</p>
          <div class="cq-17__grid cq-17__grid--anon">
            <div class="cq-17__cellbox">Sensor 4A</div>
            <div class="cq-17__cellbox">Sensor 4B</div>
          </div>
          <p class="cq-17__verdict cq-17__verdict--bad">resolved against panel &mdash; 17em is under 22em, so no match</p>
        </div>
      </section>

      <section class="cq-17__shell" aria-label="Named query">
        <p class="cq-17__cap">named &middot; <code>&#64;container cq-17-shell (min-width: 22em)</code></p>
        <div class="cq-17__panel">
          <p class="cq-17__pw">panel &middot; 17em &mdash; skipped by name</p>
          <div class="cq-17__grid cq-17__grid--named">
            <div class="cq-17__cellbox">Sensor 4A</div>
            <div class="cq-17__cellbox">Sensor 4B</div>
          </div>
          <p class="cq-17__verdict cq-17__verdict--good">resolved against cq-17-shell &mdash; matched</p>
        </div>
      </section>
    </div>

    <p class="cq-17__note">Units nest the same way: <code>cqi</code> resolves against the nearest container, and units cannot be named.</p>
  </div>
</section>
```
## CSS
```css
.cq-17,
.cq-17[data-theme="light"] {
  --bg: #f4f4f8;
  --surf: #fbfbfe;
  --surf2: #eceaf4;
  --line: #c9c6d8;
  --ink: #17161f;
  --mut: #5d5a70;
  --acc: #0f8f95;
  --bad: #a83247;
}

.cq-17[data-theme="dark"] {
  --bg: #111018;
  --surf: #1a1924;
  --surf2: #22202e;
  --line: #34314a;
  --ink: #ecebf5;
  --mut: #9a97b0;
  --acc: #4fd6d6;
  --bad: #ff7b92;
}

@media (prefers-color-scheme: dark) {
  .cq-17:not([data-theme="light"]) {
    --bg: #111018;
    --surf: #1a1924;
    --surf2: #22202e;
    --line: #34314a;
    --ink: #ecebf5;
    --mut: #9a97b0;
    --acc: #4fd6d6;
    --bad: #ff7b92;
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .cq-17,
    .cq-17[data-theme="light"] {
    --acc: oklch(0.58 0.11 195);
    --bad: oklch(0.5 0.17 12);
  }

  .cq-17[data-theme="dark"] {
    --acc: oklch(0.83 0.12 190);
    --bad: oklch(0.72 0.16 12);
  }

  @media (prefers-color-scheme: dark) {
    .cq-17:not([data-theme="light"]) {
      --acc: oklch(0.83 0.12 190);
      --bad: oklch(0.72 0.16 12);
    }
  }
}

.cq-17 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.4;
}

.cq-17 *,
.cq-17 *::before,
.cq-17 *::after {
  box-sizing: border-box;
}

.cq-17__stage {
  max-width: 68rem;
  margin-inline: auto;
  padding: clamp(0.9rem, 3vw, 2.25rem);
  display: grid;
  gap: 0.9rem;
}

.cq-17__h {
  margin: 0;
  font-size: clamp(1.2rem, 1rem + 1.5vw, 1.75rem);
  font-weight: 650;
  letter-spacing: -0.01em;
}

.cq-17__lede {
  margin: 0.3rem 0 0;
  font-size: 0.84rem;
  color: var(--mut);
  max-width: 58ch;
}

.cq-17__chain {
  list-style: none;
  margin: 0;
  padding: 0.6rem;
  display: grid;
  gap: 0.35rem;
  background: var(--surf2);
  border: 1px solid var(--line);
  border-radius: 6px;
}

.cq-17__chain li {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-items: center;
  font-size: 0.74rem;
  color: var(--mut);
  min-inline-size: 0;
}

.cq-17__chain li + li {
  padding-inline-start: 1.1rem;
}

.cq-17__chain li + li::before {
  content: "\21B3";
  margin-inline-start: -1.1rem;
  color: var(--acc);
}

.cq-17__chain code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.72rem;
  color: var(--ink);
  overflow-wrap: anywhere;
}

.cq-17__chain b {
  margin-inline-start: auto;
  font-variant-numeric: tabular-nums;
  color: var(--acc);
}

.cq-17__lv {
  padding: 0.1rem 0.4rem;
  border-radius: 3px;
  background: color-mix(in srgb, var(--acc) 18%, transparent);
  color: var(--acc);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.cq-17__lv--b {
  background: color-mix(in srgb, var(--acc) 10%, transparent);
}

.cq-17__lv--c {
  background: var(--line);
  color: var(--mut);
}

.cq-17__row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.9rem;
}

.cq-17__shell {
  container: cq-17-shell / inline-size;
  flex: 1 1 20rem;
  min-inline-size: 0;
  padding: 0.7rem;
  background: var(--surf);
  border: 1px dashed var(--acc);
  border-radius: 6px;
}

.cq-17__cap {
  margin: 0 0 0.6rem;
  font-size: 0.72rem;
  color: var(--mut);
}

.cq-17__cap code {
  font-family: ui-monospace, Menlo, monospace;
  color: var(--ink);
  overflow-wrap: anywhere;
}

.cq-17__panel {
  container-type: inline-size;
  max-inline-size: 17rem;
  padding: 0.6rem;
  background: var(--surf2);
  border: 1px dashed var(--line);
  border-radius: 4px;
}

.cq-17__pw {
  margin: 0 0 0.5rem;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.64rem;
  color: var(--mut);
}

.cq-17__grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 0.4rem;
}

.cq-17__cellbox {
  padding: 0.5rem;
  background: var(--surf);
  border: 1px solid var(--line);
  border-radius: 3px;
  font-size: 0.78rem;
  font-variant-numeric: tabular-nums;
}

.cq-17__verdict {
  margin: 0.55rem 0 0;
  font-size: 0.7rem;
  font-weight: 600;
  padding: 0.3rem 0.4rem;
  border-radius: 3px;
}

.cq-17__verdict--bad {
  color: var(--bad);
  background: color-mix(in srgb, var(--bad) 12%, transparent);
}

.cq-17__verdict--good {
  color: var(--acc);
  background: color-mix(in srgb, var(--acc) 14%, transparent);
}

@container (min-width: 22em) {
  .cq-17__grid--anon {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@container cq-17-shell (min-width: 22em) {
  .cq-17__grid--named {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

.cq-17__note {
  margin: 0;
  padding-top: 0.75rem;
  border-top: 1px solid var(--line);
  font-size: 0.76rem;
  color: var(--mut);
}

.cq-17__note code {
  font-family: ui-monospace, Menlo, monospace;
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. */

.cq-17 {
  position: relative;
}

.cq-17__theme {
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

.cq-17__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-17__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-17__themeopt {
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

.cq-17__themeopt:hover {
  opacity: 0.85;
}

.cq-17__themeinput:checked + .cq-17__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-17__themeinput:focus-visible + .cq-17__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-17:has(#cq-17-theme-light:checked) {
  --bg: #f4f4f8;
  --surf: #fbfbfe;
  --surf2: #eceaf4;
  --line: #c9c6d8;
  --ink: #17161f;
  --mut: #5d5a70;
  --acc: #0f8f95;
  --bad: #a83247;
}

.cq-17:has(#cq-17-theme-dark:checked) {
  --bg: #111018;
  --surf: #1a1924;
  --surf2: #22202e;
  --line: #34314a;
  --ink: #ecebf5;
  --mut: #9a97b0;
  --acc: #4fd6d6;
  --bad: #ff7b92;
}
```
