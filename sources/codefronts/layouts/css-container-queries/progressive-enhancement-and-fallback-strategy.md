---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/progressive-enhancement-and-fallback-strategy/"
title: "Progressive Enhancement and Fallback Strategy"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "How to ship container queries so an engine that lacks them still gets a good layout: a flex-wrap baseline declared first, then &#64;supports (container-type:…"
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Progressive Enhancement and Fallback Strategy
Source: https://codefronts.com/layouts/css-container-queries/progressive-enhancement-and-fallback-strategy/

How to ship container queries so an engine that lacks them still gets a good layout: a flex-wrap baseline declared first, then &#64;supports (container-type: inline-size) gating the enhanced path. Baseline since February 2023, so the realistic fallback target is old enterprise browsers &mdash; the baseline should be a design you would ship, not a broken one.
## HTML
```html
<section class="cq-16" aria-labelledby="cq-16-h">
  <fieldset class="cq-16__theme">
    <legend class="cq-16__themelegend">Theme</legend>
    <input class="cq-16__themeinput" type="radio" name="cq-16-theme" id="cq-16-theme-auto" checked>
    <label class="cq-16__themeopt" for="cq-16-theme-auto">Auto</label>
    <input class="cq-16__themeinput" type="radio" name="cq-16-theme" id="cq-16-theme-light">
    <label class="cq-16__themeopt" for="cq-16-theme-light">Light</label>
    <input class="cq-16__themeinput" type="radio" name="cq-16-theme" id="cq-16-theme-dark">
    <label class="cq-16__themeopt" for="cq-16-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-16__stage">
    <header class="cq-16__head">
      <h2 class="cq-16__h" id="cq-16-h">Baseline first, enhancement after</h2>
      <p class="cq-16__lede">Both panels ship the same markup and the same baseline rules. Only one of them establishes a container.</p>
    </header>

    <div class="cq-16__row">
      <section class="cq-16__panel" aria-label="Baseline path">
        <p class="cq-16__badge cq-16__badge--base">Baseline path &middot; no container</p>
        <div class="cq-16__host cq-16__host--nocq">
          <div class="cq-16__list">
            <article class="cq-16__lead">
              <h3>Fern grant round three</h3>
              <p>Applications close on the last Friday of the month; decisions within four weeks.</p>
            </article>
            <ul class="cq-16__facts">
              <li><b>42</b>awards made</li>
              <li><b>£1.8m</b>committed</li>
              <li><b>9</b>regions</li>
            </ul>
          </div>
        </div>
        <p class="cq-16__foot">Wraps at its own <code>flex-basis</code>. No per-placement decision, still a good layout.</p>
      </section>

      <section class="cq-16__panel" aria-label="Enhanced path">
        <p class="cq-16__badge cq-16__badge--enh">Enhanced path &middot; container established</p>
        <div class="cq-16__host">
          <div class="cq-16__list">
            <article class="cq-16__lead">
              <h3>Fern grant round three</h3>
              <p>Applications close on the last Friday of the month; decisions within four weeks.</p>
            </article>
            <ul class="cq-16__facts">
              <li><b>42</b>awards made</li>
              <li><b>£1.8m</b>committed</li>
              <li><b>9</b>regions</li>
            </ul>
          </div>
        </div>
        <p class="cq-16__foot">Inside <code>&#64;supports (container-type: inline-size)</code>, the query splits lead and facts by ratio.</p>
      </section>
    </div>

    <p class="cq-16__note">Container queries are Baseline since February 2023. The baseline path is for locked-down enterprise builds and old WebViews &mdash; one solid fallback, not a parallel design.</p>
  </div>
</section>
```
## CSS
```css
.cq-16,
.cq-16[data-theme="light"] {
  --bg: #ffffff;
  --surf: #f7f9fb;
  --line: #b9c6d4;
  --ink: #12202c;
  --mut: #5b6b7a;
  --acc: #21618c;
  --base: #7b6a5a;
}

.cq-16[data-theme="dark"] {
  --bg: #0b1218;
  --surf: #111c25;
  --line: #2a3d4d;
  --ink: #e7eff5;
  --mut: #93a5b4;
  --acc: #6fb2e0;
  --base: #c0aa93;
}

@media (prefers-color-scheme: dark) {
  .cq-16:not([data-theme="light"]) {
    --bg: #0b1218;
    --surf: #111c25;
    --line: #2a3d4d;
    --ink: #e7eff5;
    --mut: #93a5b4;
    --acc: #6fb2e0;
    --base: #c0aa93;
  }
}

.cq-16 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: "Helvetica Neue", Helvetica, Arial, system-ui, sans-serif;
  line-height: 1.45;
}

.cq-16 *,
.cq-16 *::before,
.cq-16 *::after {
  box-sizing: border-box;
}

.cq-16__stage {
  max-width: 72rem;
  margin-inline: auto;
  padding: clamp(1rem, 3vw, 2.5rem);
  display: grid;
  gap: 1.25rem;
}

.cq-16__h {
  margin: 0;
  font-size: clamp(1.2rem, 1rem + 1.4vw, 1.7rem);
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.cq-16__lede {
  margin: 0.4rem 0 0;
  font-size: 0.85rem;
  color: var(--mut);
  max-width: 58ch;
}

.cq-16__row {
  display: flex;
  flex-wrap: wrap;
  gap: 1.25rem;
}

.cq-16__panel {
  flex: 1 1 22rem;
  min-inline-size: 0;
  display: grid;
  gap: 0.6rem;
  align-content: start;
}

.cq-16__badge {
  margin: 0;
  padding: 0.3rem 0.55rem;
  border: 1px dashed var(--base);
  color: var(--base);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  width: fit-content;
  max-inline-size: 100%;
}

.cq-16__badge--enh {
  border-color: var(--acc);
  color: var(--acc);
  border-style: solid;
}

.cq-16__host {
  min-inline-size: 0;
  padding: 0.9rem;
  background: var(--surf);
  border: 1px dashed var(--line);
}

.cq-16__list {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
}

.cq-16__list > * {
  flex: 1 1 13rem;
  min-inline-size: 0;
}

.cq-16__lead h3 {
  margin: 0 0 0.3rem;
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: 0.01em;
}

.cq-16__lead p {
  margin: 0;
  font-size: 0.82rem;
  color: var(--mut);
}

.cq-16__facts {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.35rem;
}

.cq-16__facts li {
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
  font-size: 0.74rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--mut);
  border-block-end: 1px dashed var(--line);
  padding-block-end: 0.25rem;
}

.cq-16__facts b {
  font-size: 1.05rem;
  font-variant-numeric: tabular-nums;
  color: var(--ink);
  letter-spacing: 0;
}

.cq-16__foot {
  margin: 0;
  font-size: 0.74rem;
  color: var(--mut);
}

.cq-16__foot code,
.cq-16__note code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.9em;
}

.cq-16__note {
  margin: 0;
  padding-top: 0.85rem;
  border-top: 1px solid var(--line);
  font-size: 0.78rem;
  color: var(--mut);
  max-width: 76ch;
}

@supports (container-type: inline-size) {
  .cq-16__host {
    container: cq-16-host / inline-size;
  }

  .cq-16__host--nocq {
    container-type: normal;
  }

  @container cq-16-host (min-width: 24em) {
    .cq-16__list {
      display: grid;
      grid-template-columns: 2fr minmax(0, 1fr);
      gap: 1.5rem;
    }

    .cq-16__lead h3 {
      font-size: 1.25rem;
    }

    .cq-16__facts li {
      border-block-end-style: solid;
    }
  }
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. The
   pinned values are the demo's own [data-theme] declarations reused
   verbatim, so a toggled demo can never drift from how the same demo
   renders under the site theme. */

.cq-16 {
  position: relative;
}

.cq-16__theme {
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

.cq-16__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-16__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-16__themeopt {
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

.cq-16__themeopt:hover {
  opacity: 0.85;
}

.cq-16__themeinput:checked + .cq-16__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-16__themeinput:focus-visible + .cq-16__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-16:has(#cq-16-theme-light:checked) {
  --bg: #ffffff;
  --surf: #f7f9fb;
  --line: #b9c6d4;
  --ink: #12202c;
  --mut: #5b6b7a;
  --acc: #21618c;
  --base: #7b6a5a;
}

.cq-16:has(#cq-16-theme-dark:checked) {
  --bg: #0b1218;
  --surf: #111c25;
  --line: #2a3d4d;
  --ink: #e7eff5;
  --mut: #93a5b4;
  --acc: #6fb2e0;
  --base: #c0aa93;
}
```
