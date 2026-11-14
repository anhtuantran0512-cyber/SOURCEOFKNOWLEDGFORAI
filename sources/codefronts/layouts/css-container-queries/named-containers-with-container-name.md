---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/named-containers-with-container-name/"
title: "Named Containers with container-name"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "An anonymous @container resolves against the nearest ancestor that establishes one, which in a nested component is usually not the one you meant."
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Named Containers with container-name
Source: https://codefronts.com/layouts/css-container-queries/named-containers-with-container-name/

An anonymous @container resolves against the nearest ancestor that establishes one, which in a nested component is usually not the one you meant. Naming the ancestor with container-name and querying &#64;container cq-03-page (min-width: 18em) targets it directly. Both panels nest identically, so the wrong answer and the right one sit side by side.
## HTML
```html
<section class="cq-03" aria-labelledby="cq-03-h">
  <fieldset class="cq-03__theme">
    <legend class="cq-03__themelegend">Theme</legend>
    <input class="cq-03__themeinput" type="radio" name="cq-03-theme" id="cq-03-theme-auto" checked>
    <label class="cq-03__themeopt" for="cq-03-theme-auto">Auto</label>
    <input class="cq-03__themeinput" type="radio" name="cq-03-theme" id="cq-03-theme-light">
    <label class="cq-03__themeopt" for="cq-03-theme-light">Light</label>
    <input class="cq-03__themeinput" type="radio" name="cq-03-theme" id="cq-03-theme-dark">
    <label class="cq-03__themeopt" for="cq-03-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-03__stage">
    <header class="cq-03__head">
      <h2 class="cq-03__h" id="cq-03-h">Which ancestor answers?</h2>
      <p class="cq-03__lede">Identical nesting in both panels. Only the query differs: one is anonymous, one names the outer container.</p>
    </header>

    <div class="cq-03__row">
      <section class="cq-03__panel" aria-label="Anonymous query">
        <p class="cq-03__cap"><b>Anonymous</b> <code>&#64;container (min-width: 18em)</code></p>
        <div class="cq-03__page">
          <p class="cq-03__w">outer container &middot; cq-03-page &middot; wide</p>
          <div class="cq-03__card">
            <p class="cq-03__w cq-03__w--in">inner container &middot; cq-03-card &middot; 16rem</p>
            <div class="cq-03__badge cq-03__badge--anon">
              <span class="cq-03__no">resolved against the inner container &mdash; no match</span>
              <span class="cq-03__yes">matched</span>
            </div>
          </div>
        </div>
      </section>

      <section class="cq-03__panel" aria-label="Named query">
        <p class="cq-03__cap"><b>Named</b> <code>&#64;container cq-03-page (min-width: 18em)</code></p>
        <div class="cq-03__page">
          <p class="cq-03__w">outer container &middot; cq-03-page &middot; wide</p>
          <div class="cq-03__card">
            <p class="cq-03__w cq-03__w--in">inner container &middot; cq-03-card &middot; 16rem</p>
            <div class="cq-03__badge cq-03__badge--named">
              <span class="cq-03__no">resolved against the inner container &mdash; no match</span>
              <span class="cq-03__yes">resolved against cq-03-page &mdash; matched</span>
            </div>
          </div>
        </div>
      </section>
    </div>

    <p class="cq-03__foot">Shorthand: <code>container: cq-03-page / inline-size</code>. A container may hold several names &mdash; <code>container-name: cq-03-page cq-03-shell</code> answers to either.</p>
  </div>
</section>
```
## CSS
```css
.cq-03,
.cq-03[data-theme="light"] {
  --bg: #f2e9dd;
  --surf: #fffaf2;
  --surf2: #eadfd0;
  --line: #cbb99f;
  --ink: #241a10;
  --mut: #6d5c48;
  --acc: #c0562b;
  --sh: #241a10;
  --ok: #3f6e3a;
}

.cq-03[data-theme="dark"] {
  --bg: #1a130d;
  --surf: #241a12;
  --surf2: #2f2318;
  --line: #4a3928;
  --ink: #f7ece0;
  --mut: #b8a48c;
  --acc: #f08a56;
  --sh: #000000;
  --ok: #8fc07f;
}

@media (prefers-color-scheme: dark) {
  .cq-03:not([data-theme="light"]) {
    --bg: #1a130d;
    --surf: #241a12;
    --surf2: #2f2318;
    --line: #4a3928;
    --ink: #f7ece0;
    --mut: #b8a48c;
    --acc: #f08a56;
    --sh: #000000;
    --ok: #8fc07f;
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .cq-03,
    .cq-03[data-theme="light"] {
    --acc: oklch(0.56 0.15 42);
    --ok: oklch(0.5 0.1 142);
  }

  .cq-03[data-theme="dark"] {
    --acc: oklch(0.75 0.14 45);
    --ok: oklch(0.78 0.1 142);
  }

  @media (prefers-color-scheme: dark) {
    .cq-03:not([data-theme="light"]) {
      --acc: oklch(0.75 0.14 45);
      --ok: oklch(0.78 0.1 142);
    }
  }
}

.cq-03 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: Rockwell, "Bookman Old Style", "Roboto Slab", Georgia, serif;
  line-height: 1.5;
}

.cq-03 *,
.cq-03 *::before,
.cq-03 *::after {
  box-sizing: border-box;
}

.cq-03__stage {
  max-width: 66rem;
  margin-inline: auto;
  padding: clamp(1rem, 3vw, 2.25rem);
  display: grid;
  gap: 1.25rem;
}

.cq-03__h {
  margin: 0;
  font-size: clamp(1.4rem, 1.1rem + 2vw, 2.1rem);
  font-weight: 400;
  letter-spacing: -0.01em;
}

.cq-03__lede {
  margin: 0.4rem 0 0;
  color: var(--mut);
  font-size: 0.9rem;
  max-width: 56ch;
  font-family: system-ui, sans-serif;
}

.cq-03__row {
  display: flex;
  flex-wrap: wrap;
  gap: 1.25rem;
}

.cq-03__panel {
  flex: 1 1 26rem;
  min-inline-size: 0;
  display: grid;
  gap: 0.5rem;
  align-content: start;
}

.cq-03__cap {
  margin: 0;
  font-family: system-ui, sans-serif;
  font-size: 0.76rem;
  color: var(--mut);
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  align-items: baseline;
}

.cq-03__cap b {
  color: var(--acc);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 0.7rem;
}

.cq-03__cap code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.72rem;
}

.cq-03__page {
  container: cq-03-page / inline-size;
  padding: 0.9rem;
  background: var(--surf2);
  border: 2px solid var(--ink);
  border-radius: 2px;
  box-shadow: 6px 6px 0 var(--sh);
}

.cq-03__card {
  container: cq-03-card / inline-size;
  max-inline-size: 16rem;
  margin-top: 0.5rem;
  padding: 0.75rem;
  background: var(--surf);
  border: 2px dashed var(--line);
}

.cq-03__w {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.66rem;
  letter-spacing: 0.02em;
  color: var(--mut);
  text-transform: lowercase;
}

.cq-03__w--in {
  color: var(--acc);
}

.cq-03__badge {
  margin-top: 0.6rem;
  padding: 0.65rem 0.7rem;
  min-block-size: 3.25rem;
  display: grid;
  align-content: center;
  background: var(--surf2);
  border-inline-start: 4px solid var(--line);
  font-family: system-ui, sans-serif;
  font-size: 0.78rem;
  color: var(--mut);
}

.cq-03__yes {
  display: none;
}

@container (min-width: 18em) {
  .cq-03__badge--anon {
    background: color-mix(in srgb, var(--ok) 18%, transparent);
    border-inline-start-color: var(--ok);
    color: var(--ink);
  }

  .cq-03__badge--anon .cq-03__no {
    display: none;
  }

  .cq-03__badge--anon .cq-03__yes {
    display: block;
    font-weight: 700;
  }
}

@container cq-03-page (min-width: 18em) {
  .cq-03__badge--named {
    background: color-mix(in srgb, var(--ok) 18%, transparent);
    border-inline-start-color: var(--ok);
    color: var(--ink);
    font-weight: 700;
  }

  .cq-03__badge--named .cq-03__no {
    display: none;
  }

  .cq-03__badge--named .cq-03__yes {
    display: block;
  }
}

.cq-03__foot {
  margin: 0;
  padding-top: 0.85rem;
  border-top: 2px solid var(--ink);
  font-family: system-ui, sans-serif;
  font-size: 0.78rem;
  color: var(--mut);
  max-width: 68ch;
}

.cq-03__foot code {
  font-family: ui-monospace, Menlo, monospace;
  color: var(--ink);
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. The
   pinned values are the demo's own [data-theme] declarations reused
   verbatim, so a toggled demo can never drift from how the same demo
   renders under the site theme. */

.cq-03 {
  position: relative;
}

.cq-03__theme {
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

.cq-03__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-03__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-03__themeopt {
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

.cq-03__themeopt:hover {
  opacity: 0.85;
}

.cq-03__themeinput:checked + .cq-03__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-03__themeinput:focus-visible + .cq-03__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-03:has(#cq-03-theme-light:checked) {
  --bg: #f2e9dd;
  --surf: #fffaf2;
  --surf2: #eadfd0;
  --line: #cbb99f;
  --ink: #241a10;
  --mut: #6d5c48;
  --acc: #c0562b;
  --sh: #241a10;
  --ok: #3f6e3a;
}

.cq-03:has(#cq-03-theme-dark:checked) {
  --bg: #1a130d;
  --surf: #241a12;
  --surf2: #2f2318;
  --line: #4a3928;
  --ink: #f7ece0;
  --mut: #b8a48c;
  --acc: #f08a56;
  --sh: #000000;
  --ok: #8fc07f;
}
```
