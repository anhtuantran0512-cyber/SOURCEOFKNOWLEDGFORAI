---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/navigation-component-collapse-by-container/"
title: "Navigation Component Collapse by Container"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "A nav that shows its full link row while it has room and collapses to a disclosure when it does not &mdash; decided by its own width, so the same component…"
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Navigation Component Collapse by Container
Source: https://codefronts.com/layouts/css-container-queries/navigation-component-collapse-by-container/

A nav that shows its full link row while it has room and collapses to a disclosure when it does not &mdash; decided by its own width, so the same component works in a page header and inside a narrow card. The collapsed state is a native <details> element, so it is keyboard accessible and needs no script, and the links live in the markup once.
## HTML
```html
<section class="cq-14" aria-labelledby="cq-14-h">
  <fieldset class="cq-14__theme">
    <legend class="cq-14__themelegend">Theme</legend>
    <input class="cq-14__themeinput" type="radio" name="cq-14-theme" id="cq-14-theme-auto" checked>
    <label class="cq-14__themeopt" for="cq-14-theme-auto">Auto</label>
    <input class="cq-14__themeinput" type="radio" name="cq-14-theme" id="cq-14-theme-light">
    <label class="cq-14__themeopt" for="cq-14-theme-light">Light</label>
    <input class="cq-14__themeinput" type="radio" name="cq-14-theme" id="cq-14-theme-dark">
    <label class="cq-14__themeopt" for="cq-14-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-14__stage">
    <header class="cq-14__head">
      <h2 class="cq-14__h" id="cq-14-h">The nav decides for itself</h2>
      <p class="cq-14__lede">Two placements, one component. The wide header keeps its links; the card rail collapses.</p>
    </header>

    <div class="cq-14__slot cq-14__slot--wide">
      <p class="cq-14__w">page header &middot; wide container</p>
      <nav class="cq-14__bar" aria-label="Ranger Tools, page">
        <span class="cq-14__brand">Ranger</span>
        <ul class="cq-14__links">
          <li><a href="#cq-14-h" aria-current="page">Overview</a></li>
          <li><a href="#cq-14-h">Fleets</a></li>
          <li><a href="#cq-14-h">Maintenance</a></li>
          <li><a href="#cq-14-h">Reports</a></li>
        </ul>
        <details class="cq-14__menu">
          <summary class="cq-14__sum">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-width="2.75" stroke-linecap="round"/></svg>
            <span class="cq-14__sumtext">Menu</span>
          </summary>
          <ul class="cq-14__panel">
            <li><a href="#cq-14-h" aria-current="page">Overview</a></li>
            <li><a href="#cq-14-h">Fleets</a></li>
            <li><a href="#cq-14-h">Maintenance</a></li>
            <li><a href="#cq-14-h">Reports</a></li>
          </ul>
        </details>
      </nav>
    </div>

    <div class="cq-14__slot cq-14__slot--narrow">
      <p class="cq-14__w">card rail &middot; 16rem container</p>
      <nav class="cq-14__bar" aria-label="Ranger Tools, rail">
        <span class="cq-14__brand">Ranger</span>
        <ul class="cq-14__links">
          <li><a href="#cq-14-h" aria-current="page">Overview</a></li>
          <li><a href="#cq-14-h">Fleets</a></li>
          <li><a href="#cq-14-h">Maintenance</a></li>
          <li><a href="#cq-14-h">Reports</a></li>
        </ul>
        <details class="cq-14__menu">
          <summary class="cq-14__sum">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-width="2.75" stroke-linecap="round"/></svg>
            <span class="cq-14__sumtext">Menu</span>
          </summary>
          <ul class="cq-14__panel">
            <li><a href="#cq-14-h" aria-current="page">Overview</a></li>
            <li><a href="#cq-14-h">Fleets</a></li>
            <li><a href="#cq-14-h">Maintenance</a></li>
            <li><a href="#cq-14-h">Reports</a></li>
          </ul>
        </details>
      </nav>
    </div>
  </div>
</section>
```
## CSS
```css
.cq-14,
.cq-14[data-theme="light"] {
  --bg: #edeae6;
  --surf: #2a2723;
  --surf2: #38342f;
  --line: #4a453e;
  --ink: #f7f4ef;
  --mut: #b8b0a5;
  --acc: #f0a020;
  --sh: #cdc6bd;
}

.cq-14[data-theme="dark"] {
  --bg: #131210;
  --surf: #201e1b;
  --surf2: #2a2723;
  --line: #3b3731;
  --ink: #f5f2ec;
  --mut: #a49c91;
  --acc: #ffb84d;
  --sh: #000000;
}

@media (prefers-color-scheme: dark) {
  .cq-14:not([data-theme="light"]) {
    --bg: #131210;
    --surf: #201e1b;
    --surf2: #2a2723;
    --line: #3b3731;
    --ink: #f5f2ec;
    --mut: #a49c91;
    --acc: #ffb84d;
    --sh: #000000;
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .cq-14,
    .cq-14[data-theme="light"] {
    --acc: oklch(0.78 0.16 72);
  }

  .cq-14[data-theme="dark"] {
    --acc: oklch(0.84 0.14 76);
  }

  @media (prefers-color-scheme: dark) {
    .cq-14:not([data-theme="light"]) {
      --acc: oklch(0.84 0.14 76);
    }
  }
}

.cq-14 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: #201e1b;
  font-family: "Archivo Narrow", "Roboto Condensed", "Liberation Sans Narrow", "Segoe UI", system-ui, sans-serif;
  line-height: 1.4;
}

.cq-14[data-theme="dark"],
.cq-14[data-theme="dark"] .cq-14__w {
  color: var(--mut);
}

@media (prefers-color-scheme: dark) {
  .cq-14:not([data-theme="light"]) {
    color: var(--mut);
  }
}

.cq-14 *,
.cq-14 *::before,
.cq-14 *::after {
  box-sizing: border-box;
}

.cq-14 [hidden] {
  display: none;
}

.cq-14__stage {
  max-width: 66rem;
  margin-inline: auto;
  padding: clamp(1rem, 3vw, 2.25rem);
  display: grid;
  gap: 1.5rem;
}

.cq-14__h {
  margin: 0;
  font-size: clamp(1.3rem, 1.05rem + 1.8vw, 2rem);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.02em;
}

.cq-14__lede {
  margin: 0.3rem 0 0;
  font-size: 0.86rem;
  max-width: 54ch;
  opacity: 0.75;
}

.cq-14__slot {
  container: cq-14-nav / inline-size;
  display: grid;
  gap: 0.4rem;
}

.cq-14__slot--narrow {
  max-inline-size: 16rem;
}

.cq-14__w {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.66rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  opacity: 0.7;
}

.cq-14__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem 0.9rem;
  padding: 0.55rem 0.75rem;
  background: var(--surf);
  color: var(--ink);
  border-radius: 4px;
  box-shadow: 0 4px 0 var(--sh);
}

.cq-14__brand {
  font-size: 1.05rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--acc);
  margin-inline-end: auto;
}

.cq-14__links {
  display: none;
  list-style: none;
  margin: 0;
  padding: 0;
  gap: 1rem;
  flex-wrap: wrap;
}

.cq-14__links a,
.cq-14__panel a {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.75rem;
  color: var(--ink);
  text-decoration: none;
  font-size: 0.85rem;
  letter-spacing: 0.04em;
  border-block-end: 2px solid transparent;
}

.cq-14__links a:hover,
.cq-14__panel a:hover {
  color: var(--acc);
}

.cq-14__links a[aria-current="page"] {
  border-block-end-color: var(--acc);
  color: var(--acc);
}

.cq-14__links a:focus-visible,
.cq-14__panel a:focus-visible,
.cq-14__sum:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cq-14__menu {
  position: relative;
}

.cq-14__sum {
  list-style: none;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  min-block-size: 2.75rem;
  min-inline-size: 2.75rem;
  padding-inline: 0.6rem;
  border-radius: 4px;
  background: var(--surf2);
  color: var(--acc);
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  cursor: pointer;
}

.cq-14__sum::-webkit-details-marker {
  display: none;
}

.cq-14__sum svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  transition: rotate 0.18s ease;
}

.cq-14__menu[open] .cq-14__sum svg {
  rotate: 90deg;
}

.cq-14__panel {
  position: absolute;
  inset-inline: 0 auto;
  inset-block-start: calc(100% + 0.4rem);
  min-inline-size: 11rem;
  list-style: none;
  margin: 0;
  padding: 0.35rem 0.6rem;
  background: var(--surf2);
  border: 1px solid var(--line);
  border-radius: 4px;
  z-index: 2;
}

.cq-14__panel a {
  min-block-size: 2.5rem;
}

@container cq-14-nav (min-width: 32em) {
  .cq-14__links {
    display: flex;
  }

  .cq-14__menu {
    display: none;
  }

  .cq-14__bar {
    padding: 0.5rem 1rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cq-14__sum svg {
    transition: none;
  }
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. The
   pinned values are the demo's own [data-theme] declarations reused
   verbatim, so a toggled demo can never drift from how the same demo
   renders under the site theme. */

.cq-14 {
  position: relative;
}

.cq-14__theme {
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

.cq-14__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-14__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-14__themeopt {
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

.cq-14__themeopt:hover {
  opacity: 0.85;
}

.cq-14__themeinput:checked + .cq-14__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-14__themeinput:focus-visible + .cq-14__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-14:has(#cq-14-theme-light:checked) {
  --bg: #edeae6;
  --surf: #2a2723;
  --surf2: #38342f;
  --line: #4a453e;
  --ink: #f7f4ef;
  --mut: #b8b0a5;
  --acc: #f0a020;
  --sh: #cdc6bd;
}

.cq-14:has(#cq-14-theme-dark:checked) {
  --bg: #131210;
  --surf: #201e1b;
  --surf2: #2a2723;
  --line: #3b3731;
  --ink: #f5f2ec;
  --mut: #a49c91;
  --acc: #ffb84d;
  --sh: #000000;
}
```
