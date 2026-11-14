---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/container-query-units-cqi-cqw-cqmin/"
title: "Container Query Units cqi cqw cqmin"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "The whole unit family shown resolving against a container you can drag wider."
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Container Query Units cqi cqw cqmin
Source: https://codefronts.com/layouts/css-container-queries/container-query-units-cqi-cqw-cqmin/

The whole unit family shown resolving against a container you can drag wider. cqw and cqh are physical, cqi and cqb are logical and follow writing mode, cqmin and cqmax take the smaller or larger of the two. The second panel adds what most references skip: what cqb resolves against under inline-size.
## HTML
```html
<section class="cq-02" aria-labelledby="cq-02-h">
  <fieldset class="cq-02__theme">
    <legend class="cq-02__themelegend">Theme</legend>
    <input class="cq-02__themeinput" type="radio" name="cq-02-theme" id="cq-02-theme-auto" checked>
    <label class="cq-02__themeopt" for="cq-02-theme-auto">Auto</label>
    <input class="cq-02__themeinput" type="radio" name="cq-02-theme" id="cq-02-theme-light">
    <label class="cq-02__themeopt" for="cq-02-theme-light">Light</label>
    <input class="cq-02__themeinput" type="radio" name="cq-02-theme" id="cq-02-theme-dark">
    <label class="cq-02__themeopt" for="cq-02-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-02__stage">
    <header class="cq-02__head">
      <h2 class="cq-02__h" id="cq-02-h">Container units, resolving live</h2>
      <p class="cq-02__lede">Drag either panel's right edge. Every bar is sized in a cq unit and re-resolves against the panel, not the window.</p>
    </header>

    <section class="cq-02__panel" aria-label="Inline-size container">
      <p class="cq-02__cap"><span class="cq-02__chip">container-type: inline-size</span> inline axis is queryable</p>
      <div class="cq-02__box cq-02__box--inline">
        <ul class="cq-02__bars">
          <li><span class="cq-02__u">100cqi</span><span class="cq-02__bar" style="inline-size: 100%; inline-size: 100cqi"></span><span class="cq-02__v">full inline size</span></li>
          <li><span class="cq-02__u">50cqi</span><span class="cq-02__bar" style="inline-size: 50%; inline-size: 50cqi"></span><span class="cq-02__v">half, logical</span></li>
          <li><span class="cq-02__u">50cqw</span><span class="cq-02__bar" style="inline-size: 50%; inline-size: 50cqw"></span><span class="cq-02__v">half, physical</span></li>
          <li><span class="cq-02__u">25cqi</span><span class="cq-02__bar" style="inline-size: 25%; inline-size: 25cqi"></span><span class="cq-02__v">quarter</span></li>
          <li class="cq-02__warn"><span class="cq-02__u">40cqb</span><span class="cq-02__bar cq-02__bar--fb" style="inline-size: 40%; inline-size: 40cqb"></span><span class="cq-02__v">no block containment: falls back to the viewport</span></li>
        </ul>
      </div>
    </section>

    <section class="cq-02__panel" aria-label="Size container">
      <p class="cq-02__cap"><span class="cq-02__chip cq-02__chip--alt">container-type: size</span> both axes queryable, height set from outside</p>
      <div class="cq-02__box cq-02__box--size">
        <div class="cq-02__grid">
          <span class="cq-02__sq" style="inline-size: 22%; block-size: 22%; inline-size: 22cqmin; block-size: 22cqmin"><b>22cqmin</b></span>
          <span class="cq-02__sq cq-02__sq--b" style="inline-size: 18%; block-size: 18%; inline-size: 18cqmax; block-size: 18cqmax"><b>18cqmax</b></span>
          <span class="cq-02__sq cq-02__sq--c" style="block-size: 60%; block-size: 60cqb"><b>60cqb</b></span>
          <span class="cq-02__sq cq-02__sq--d" style="block-size: 40%; block-size: 40cqh"><b>40cqh</b></span>
        </div>
      </div>
    </section>

    <dl class="cq-02__legend">
      <div><dt>cqi / cqb</dt><dd>logical inline and block — follow writing mode, use these</dd></div>
      <div><dt>cqw / cqh</dt><dd>physical width and height — identical in Latin horizontal text, wrong in vertical</dd></div>
      <div><dt>cqmin / cqmax</dt><dd>the smaller and the larger of the two axes</dd></div>
    </dl>
  </div>
</section>
```
## CSS
```css
.cq-02,
.cq-02[data-theme="light"] {
  --bg: #f6f7f4;
  --surf: #ffffff;
  --line: #dcdfd6;
  --ink: #11130f;
  --mut: #5f6558;
  --acc: #4d7c0f;
  --acc2: #a3a80b;
  --warn: #b45309;
}

.cq-02[data-theme="dark"] {
  --bg: #07080a;
  --surf: #0e1013;
  --line: #23262b;
  --ink: #f2f4ef;
  --mut: #9aa093;
  --acc: #b7f13a;
  --acc2: #e4ff6b;
  --warn: #f5a524;
}

@media (prefers-color-scheme: dark) {
  .cq-02:not([data-theme="light"]) {
    --bg: #07080a;
    --surf: #0e1013;
    --line: #23262b;
    --ink: #f2f4ef;
    --mut: #9aa093;
    --acc: #b7f13a;
    --acc2: #e4ff6b;
    --warn: #f5a524;
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .cq-02,
    .cq-02[data-theme="light"] {
    --acc: oklch(0.55 0.16 128);
    --acc2: oklch(0.68 0.17 110);
  }

  .cq-02[data-theme="dark"] {
    --acc: oklch(0.88 0.21 122);
    --acc2: oklch(0.94 0.18 112);
  }

  @media (prefers-color-scheme: dark) {
    .cq-02:not([data-theme="light"]) {
      --acc: oklch(0.88 0.21 122);
      --acc2: oklch(0.94 0.18 112);
    }
  }
}

.cq-02 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.45;
}

.cq-02 *,
.cq-02 *::before,
.cq-02 *::after {
  box-sizing: border-box;
}

.cq-02__stage {
  max-width: 62rem;
  margin-inline: auto;
  padding: clamp(1rem, 3vw, 2.25rem);
  display: grid;
  gap: 1rem;
}

.cq-02__h {
  margin: 0;
  font-size: clamp(1.3rem, 1rem + 1.8vw, 1.9rem);
  font-weight: 800;
  letter-spacing: -0.02em;
  text-transform: uppercase;
}

.cq-02__lede {
  margin: 0.3rem 0 0;
  color: var(--mut);
  font-size: 0.85rem;
  max-width: 54ch;
}

.cq-02__panel {
  display: grid;
  gap: 0.4rem;
}

.cq-02__cap {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-items: center;
  font-size: 0.74rem;
  color: var(--mut);
  letter-spacing: 0.04em;
}

.cq-02__chip {
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.7rem;
  padding: 0.2rem 0.45rem;
  border-radius: 3px;
  background: var(--acc);
  color: #07080a;
  font-weight: 700;
}

.cq-02__chip--alt {
  background: var(--acc2);
}

.cq-02__box {
  container-type: inline-size;
  container-name: cq-02-box;
  min-inline-size: 12rem;
  max-inline-size: 100%;
  resize: horizontal;
  overflow: auto;
  padding: 0.75rem;
  background: var(--surf);
  border: 1px solid var(--line);
  border-radius: 4px;
}

.cq-02__box--size {
  container-type: size;
  block-size: 11rem;
  resize: horizontal;
}

.cq-02__bars {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.4rem;
}

.cq-02__bars li {
  display: grid;
  grid-template-columns: 4.5rem minmax(0, 1fr);
  gap: 0.15rem 0.6rem;
  align-items: center;
  min-inline-size: 0;
}

.cq-02__u {
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.72rem;
  font-variant-numeric: tabular-nums;
  color: var(--ink);
  font-weight: 700;
}

.cq-02__bar {
  display: block;
  block-size: 0.85rem;
  border-radius: 2px;
  background: linear-gradient(90deg, #4d7c0f, #a3a80b);
  background: linear-gradient(90deg, var(--acc), var(--acc2));
  max-inline-size: 100%;
}

.cq-02__bar--fb {
  background: repeating-linear-gradient(135deg, var(--warn) 0 6px, transparent 6px 12px), var(--line);
}

.cq-02__v {
  grid-column: 2;
  font-size: 0.7rem;
  color: var(--mut);
}

.cq-02__warn .cq-02__v {
  color: var(--warn);
}

.cq-02__grid {
  block-size: 100%;
  display: flex;
  align-items: flex-end;
  gap: 0.5rem;
}

.cq-02__sq {
  display: grid;
  place-items: center;
  min-inline-size: 3.2rem;
  padding: 0.2rem;
  border-radius: 3px;
  background: color-mix(in srgb, var(--acc) 22%, transparent);
  border: 1px solid var(--acc);
}

.cq-02__sq b {
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.62rem;
  font-variant-numeric: tabular-nums;
  color: var(--ink);
}

.cq-02__sq--b {
  background: color-mix(in srgb, var(--acc2) 22%, transparent);
  border-color: var(--acc2);
}

.cq-02__sq--c {
  inline-size: 4.5rem;
}

.cq-02__sq--d {
  inline-size: 4.5rem;
  border-style: dashed;
}

.cq-02__legend {
  margin: 0;
  display: grid;
  gap: 0.4rem;
  padding-top: 0.75rem;
  border-top: 1px solid var(--line);
  font-size: 0.76rem;
}

.cq-02__legend div {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  min-inline-size: 0;
}

.cq-02__legend dt {
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-weight: 700;
  flex: none;
}

.cq-02__legend dd {
  margin: 0;
  color: var(--mut);
}

@container cq-02-box (min-width: 26em) {
  .cq-02__bars li {
    grid-template-columns: 5rem minmax(0, 1fr) 13rem;
  }

  .cq-02__v {
    grid-column: 3;
  }
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. The
   pinned values are the demo's own [data-theme] declarations reused
   verbatim, so a toggled demo can never drift from how the same demo
   renders under the site theme. */

.cq-02 {
  position: relative;
}

.cq-02__theme {
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

.cq-02__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-02__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-02__themeopt {
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

.cq-02__themeopt:hover {
  opacity: 0.85;
}

.cq-02__themeinput:checked + .cq-02__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-02__themeinput:focus-visible + .cq-02__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-02:has(#cq-02-theme-light:checked) {
  --bg: #f6f7f4;
  --surf: #ffffff;
  --line: #dcdfd6;
  --ink: #11130f;
  --mut: #5f6558;
  --acc: #4d7c0f;
  --acc2: #a3a80b;
  --warn: #b45309;
}

.cq-02:has(#cq-02-theme-dark:checked) {
  --bg: #07080a;
  --surf: #0e1013;
  --line: #23262b;
  --ink: #f2f4ef;
  --mut: #9aa093;
  --acc: #b7f13a;
  --acc2: #e4ff6b;
  --warn: #f5a524;
}
```
