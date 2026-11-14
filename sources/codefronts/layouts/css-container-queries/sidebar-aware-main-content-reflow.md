---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/sidebar-aware-main-content-reflow/"
title: "Sidebar Aware Main Content Reflow"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "A content block that reacts to the space a collapsible sidebar leaves it: two columns when the rail is collapsed, one when it is expanded, decided entirely…"
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sidebar Aware Main Content Reflow
Source: https://codefronts.com/layouts/css-container-queries/sidebar-aware-main-content-reflow/

A content block that reacts to the space a collapsible sidebar leaves it: two columns when the rail is collapsed, one when it is expanded, decided entirely by the main region's own inline size. The subject is the content responding to space it did not choose &mdash; the sidebar is context, and the toggle is a real checkbox read with :has(), so no script is involved.
## HTML
```html
<section class="cq-05" aria-labelledby="cq-05-h">
  <fieldset class="cq-05__theme">
    <legend class="cq-05__themelegend">Theme</legend>
    <input class="cq-05__themeinput" type="radio" name="cq-05-theme" id="cq-05-theme-auto" checked>
    <label class="cq-05__themeopt" for="cq-05-theme-auto">Auto</label>
    <input class="cq-05__themeinput" type="radio" name="cq-05-theme" id="cq-05-theme-light">
    <label class="cq-05__themeopt" for="cq-05-theme-light">Light</label>
    <input class="cq-05__themeinput" type="radio" name="cq-05-theme" id="cq-05-theme-dark">
    <label class="cq-05__themeopt" for="cq-05-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-05__stage">
    <header class="cq-05__head">
      <h2 class="cq-05__h" id="cq-05-h">Content that reads its own space</h2>
      <p class="cq-05__lede">Collapse the rail. The viewport never changes &mdash; only the space left for the notes.</p>
    </header>

    <div class="cq-05__shell">
      <input class="cq-05__sr" type="checkbox" id="cq-05-collapse">
      <nav class="cq-05__rail" aria-label="Workspace">
        <label class="cq-05__toggle" for="cq-05-collapse">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 6h16M4 12h16M4 18h16" stroke="currentColor" stroke-width="2.75" stroke-linecap="round"/></svg>
          <span class="cq-05__vh">Collapse the workspace rail</span>
        </label>
        <ul class="cq-05__nav">
          <li><span class="cq-05__dot" aria-hidden="true"></span><span class="cq-05__nl">Field notes</span></li>
          <li><span class="cq-05__dot cq-05__dot--b" aria-hidden="true"></span><span class="cq-05__nl">Soil samples</span></li>
          <li><span class="cq-05__dot cq-05__dot--c" aria-hidden="true"></span><span class="cq-05__nl">Vale orchard</span></li>
          <li><span class="cq-05__dot cq-05__dot--d" aria-hidden="true"></span><span class="cq-05__nl">Archive</span></li>
        </ul>
      </nav>

      <main class="cq-05__main">
        <p class="cq-05__cap">main region &middot; container: cq-05-main / inline-size</p>
        <div class="cq-05__grid">
          <article class="cq-05__note">
            <h3>Row spacing trial, block C</h3>
            <p>Tighter rows held moisture four days longer than the control strip, with no measurable loss in yield.</p>
            <p class="cq-05__meta">Jordan Lee &middot; 12 Aug</p>
          </article>
          <article class="cq-05__note">
            <h3>Cover crop mix, second season</h3>
            <p>Clover and vetch established faster than last year; the rye is still slow on the north edge.</p>
            <p class="cq-05__meta">Sam Rivera &middot; 09 Aug</p>
          </article>
          <article class="cq-05__note">
            <h3>Irrigation window shifted</h3>
            <p>Moving the cycle to first light cut evaporation loss by roughly a fifth across the season.</p>
            <p class="cq-05__meta">Priya Sharma &middot; 04 Aug</p>
          </article>
          <article class="cq-05__note">
            <h3>Hedgerow survey</h3>
            <p>Twenty-two species counted along the west boundary, up from sixteen at the last count.</p>
            <p class="cq-05__meta">Alex Chen &middot; 28 Jul</p>
          </article>
        </div>
      </main>
    </div>
  </div>
</section>
```
## CSS
```css
.cq-05,
.cq-05[data-theme="light"] {
  --bg: #f4f1e8;
  --s1: #fbf9f3;
  --s2: #ebe7d9;
  --s3: #ddd8c5;
  --line: #cdc7b0;
  --ink: #1e241a;
  --mut: #5c6553;
  --acc: #4b6b3c;
}

.cq-05[data-theme="dark"] {
  --bg: #14170f;
  --s1: #1c2016;
  --s2: #23281c;
  --s3: #2c3223;
  --line: #3a4130;
  --ink: #edf0e6;
  --mut: #a3ad96;
  --acc: #9ec27f;
}

@media (prefers-color-scheme: dark) {
  .cq-05:not([data-theme="light"]) {
    --bg: #14170f;
    --s1: #1c2016;
    --s2: #23281c;
    --s3: #2c3223;
    --line: #3a4130;
    --ink: #edf0e6;
    --mut: #a3ad96;
    --acc: #9ec27f;
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .cq-05,
    .cq-05[data-theme="light"] {
    --acc: oklch(0.5 0.09 138);
  }

  .cq-05[data-theme="dark"] {
    --acc: oklch(0.8 0.11 135);
  }

  @media (prefers-color-scheme: dark) {
    .cq-05:not([data-theme="light"]) {
      --acc: oklch(0.8 0.11 135);
    }
  }
}

.cq-05 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: "Gill Sans", "Gill Sans MT", Optima, Avenir, "Segoe UI", system-ui, sans-serif;
  line-height: 1.5;
}

.cq-05 *,
.cq-05 *::before,
.cq-05 *::after {
  box-sizing: border-box;
}

.cq-05__stage {
  max-width: 72rem;
  margin-inline: auto;
  padding: clamp(1rem, 3vw, 2.5rem);
  display: grid;
  gap: 1.25rem;
}

.cq-05__h {
  margin: 0;
  font-size: clamp(1.35rem, 1.1rem + 1.6vw, 1.95rem);
  font-weight: 600;
  letter-spacing: 0.01em;
}

.cq-05__lede {
  margin: 0.35rem 0 0;
  color: var(--mut);
  font-size: 0.9rem;
  max-width: 52ch;
}

.cq-05__shell {
  display: grid;
  grid-template-columns: 15rem minmax(0, 1fr);
  gap: 0.75rem;
  padding: 0.75rem;
  background: var(--s2);
  border: 1px solid var(--line);
  border-radius: 10px;
  transition: grid-template-columns 0.28s ease;
}

.cq-05__shell:has(#cq-05-collapse:checked) {
  grid-template-columns: 4.25rem minmax(0, 1fr);
}

.cq-05__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cq-05__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cq-05__rail {
  min-inline-size: 0;
  padding: 0.6rem;
  background: var(--s3);
  border-radius: 8px;
  display: grid;
  gap: 0.75rem;
  align-content: start;
}

.cq-05__toggle {
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  border-radius: 8px;
  background: var(--s1);
  color: var(--acc);
  cursor: pointer;
}

.cq-05__toggle svg {
  inline-size: 1.35rem;
  block-size: 1.35rem;
}

.cq-05__sr:focus-visible + .cq-05__rail .cq-05__toggle {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cq-05__nav {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.5rem;
}

.cq-05__nav li {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  min-block-size: 2.25rem;
  padding-inline: 0.35rem;
  border-radius: 6px;
  font-size: 0.85rem;
  min-inline-size: 0;
}

.cq-05__dot {
  flex: none;
  inline-size: 0.7rem;
  block-size: 0.7rem;
  border-radius: 50%;
  background: var(--acc);
}

.cq-05__dot--b {
  background: color-mix(in srgb, var(--acc) 62%, var(--ink));
}

.cq-05__dot--c {
  background: color-mix(in srgb, var(--acc) 40%, var(--s1));
}

.cq-05__dot--d {
  background: var(--line);
}

.cq-05__nl {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  transition: opacity 0.2s ease;
}

.cq-05__shell:has(#cq-05-collapse:checked) .cq-05__nl {
  opacity: 0;
  visibility: hidden;
}

.cq-05__main {
  container: cq-05-main / inline-size;
  min-inline-size: 0;
  padding: 0.9rem;
  background: var(--s1);
  border-radius: 8px;
}

.cq-05__cap {
  margin: 0 0 0.75rem;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.68rem;
  color: var(--mut);
  letter-spacing: 0.01em;
}

.cq-05__grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0.75rem;
}

.cq-05__note {
  min-inline-size: 0;
  padding: 0.85rem;
  background: var(--s2);
  border-radius: 6px;
  border-inline-start: 3px solid var(--acc);
}

.cq-05__note h3 {
  margin: 0 0 0.3rem;
  font-size: 0.95rem;
  font-weight: 600;
}

.cq-05__note p {
  margin: 0;
  font-size: 0.83rem;
  color: var(--mut);
}

.cq-05__meta {
  margin-top: 0.4rem;
  font-size: 0.72rem;
  letter-spacing: 0.02em;
}

@container cq-05-main (min-width: 34em) {
  .cq-05__grid {
    grid-template-columns: 1fr 1fr;
  }

  .cq-05__note {
    padding: 1rem;
  }
}

@container cq-05-main (min-width: 52em) {
  .cq-05__grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (prefers-reduced-motion: reduce) {
  .cq-05__shell,
    .cq-05__nl {
    transition: none;
  }
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. The
   pinned values are the demo's own [data-theme] declarations reused
   verbatim, so a toggled demo can never drift from how the same demo
   renders under the site theme. */

.cq-05 {
  position: relative;
}

.cq-05__theme {
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

.cq-05__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-05__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-05__themeopt {
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

.cq-05__themeopt:hover {
  opacity: 0.85;
}

.cq-05__themeinput:checked + .cq-05__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-05__themeinput:focus-visible + .cq-05__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-05:has(#cq-05-theme-light:checked) {
  --bg: #f4f1e8;
  --s1: #fbf9f3;
  --s2: #ebe7d9;
  --s3: #ddd8c5;
  --line: #cdc7b0;
  --ink: #1e241a;
  --mut: #5c6553;
  --acc: #4b6b3c;
}

.cq-05:has(#cq-05-theme-dark:checked) {
  --bg: #14170f;
  --s1: #1c2016;
  --s2: #23281c;
  --s3: #2c3223;
  --line: #3a4130;
  --ink: #edf0e6;
  --mut: #a3ad96;
  --acc: #9ec27f;
}
```
