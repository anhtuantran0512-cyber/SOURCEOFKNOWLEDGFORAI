---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/css-style-queries-with-container-style/"
title: "CSS Style Queries with container style"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "&#64;container style(--cq-07-tone: featured) queries a custom property's value instead of a size, so one token on the parent restyles every descendant…"
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Style Queries with container style
Source: https://codefronts.com/layouts/css-container-queries/css-style-queries-with-container-style/

&#64;container style(--cq-07-tone: featured) queries a custom property's value instead of a size, so one token on the parent restyles every descendant &mdash; replacing a cascade of modifier classes. The card below is driven by a single --cq-07-tone value, shown next to the BEM version it replaces, with the honest caveat that only custom properties are queryable today.
## HTML
```html
<section class="cq-07" aria-labelledby="cq-07-h">
  <fieldset class="cq-07__theme">
    <legend class="cq-07__themelegend">Theme</legend>
    <input class="cq-07__themeinput" type="radio" name="cq-07-theme" id="cq-07-theme-auto" checked>
    <label class="cq-07__themeopt" for="cq-07-theme-auto">Auto</label>
    <input class="cq-07__themeinput" type="radio" name="cq-07-theme" id="cq-07-theme-light">
    <label class="cq-07__themeopt" for="cq-07-theme-light">Light</label>
    <input class="cq-07__themeinput" type="radio" name="cq-07-theme" id="cq-07-theme-dark">
    <label class="cq-07__themeopt" for="cq-07-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-07__stage">
    <header class="cq-07__head">
      <h2 class="cq-07__h" id="cq-07-h">One token, whole treatment</h2>
      <p class="cq-07__lede">Pick a tone. The card's markup never changes &mdash; only the value of <code>--cq-07-tone</code> on its parent.</p>
    </header>

    <fieldset class="cq-07__tones">
      <legend class="cq-07__vh">Card tone</legend>
      <div class="cq-07__seg">
        <input class="cq-07__sr" type="radio" name="cq-07-tone" id="cq-07-calm" checked>
        <label class="cq-07__opt" for="cq-07-calm">calm</label>
        <input class="cq-07__sr" type="radio" name="cq-07-tone" id="cq-07-featured">
        <label class="cq-07__opt" for="cq-07-featured">featured</label>
        <input class="cq-07__sr" type="radio" name="cq-07-tone" id="cq-07-retiring">
        <label class="cq-07__opt" for="cq-07-retiring">retiring</label>
      </div>
    </fieldset>

    <div class="cq-07__row">
      <section class="cq-07__side" aria-label="Style query version">
        <p class="cq-07__cap">Style query &middot; one declaration on the parent</p>
        <div class="cq-07__frame">
          <article class="cq-07__card">
            <p class="cq-07__badge">Featured plan</p>
            <h3 class="cq-07__title">Quill Studio</h3>
            <p class="cq-07__price">$38<span>/seat</span></p>
            <p class="cq-07__text">Shared libraries, review links and unlimited version history.</p>
            <p class="cq-07__foot">Tone comes from <code>--cq-07-tone</code></p>
          </article>
        </div>
      </section>

      <section class="cq-07__side" aria-label="Modifier class version">
        <p class="cq-07__cap">Modifier classes &middot; the version it replaces</p>
        <div class="cq-07__frame cq-07__frame--static">
          <article class="cq-07__card cq-07__card--featured">
            <p class="cq-07__badge cq-07__badge--featured">Featured plan</p>
            <h3 class="cq-07__title cq-07__title--featured">Quill Studio</h3>
            <p class="cq-07__price">$38<span>/seat</span></p>
            <p class="cq-07__text">Shared libraries, review links and unlimited version history.</p>
            <p class="cq-07__foot">Three classes, applied by whoever renders it</p>
          </article>
        </div>
      </section>
    </div>
  </div>
</section>
```
## CSS
```css
.cq-07,
.cq-07[data-theme="light"] {
  --bg: #ece4dc;
  --surf: #f7f1ea;
  --line: #d3c4b4;
  --ink: #2a201a;
  --mut: #6e5c4e;
  --acc: #b0347a;
  --hi: rgba(255, 255, 255, 0.85);
  --lo: rgba(94, 74, 60, 0.22);
  --calm-fill: #f7f1ea;
  --calm-line: #d3c4b4;
  --feat-fill: #fbe6f1;
  --feat-line: #b0347a;
  --ret-fill: #ece7e0;
  --ret-line: #b3a698;
}

.cq-07[data-theme="dark"] {
  --bg: #191310;
  --surf: #241b16;
  --line: #453529;
  --ink: #f4e9df;
  --mut: #b5a293;
  --acc: #f070ac;
  --hi: rgba(255, 255, 255, 0.06);
  --lo: rgba(0, 0, 0, 0.55);
  --calm-fill: #241b16;
  --calm-line: #453529;
  --feat-fill: #3a1c2c;
  --feat-line: #f070ac;
  --ret-fill: #201a17;
  --ret-line: #4a4038;
}

@media (prefers-color-scheme: dark) {
  .cq-07:not([data-theme="light"]) {
    --bg: #191310;
    --surf: #241b16;
    --line: #453529;
    --ink: #f4e9df;
    --mut: #b5a293;
    --acc: #f070ac;
    --hi: rgba(255, 255, 255, 0.06);
    --lo: rgba(0, 0, 0, 0.55);
    --calm-fill: #241b16;
    --calm-line: #453529;
    --feat-fill: #3a1c2c;
    --feat-line: #f070ac;
    --ret-fill: #201a17;
    --ret-line: #4a4038;
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .cq-07,
    .cq-07[data-theme="light"] {
    --acc: oklch(0.52 0.19 350);
  }

  .cq-07[data-theme="dark"] {
    --acc: oklch(0.75 0.17 350);
  }

  @media (prefers-color-scheme: dark) {
    .cq-07:not([data-theme="light"]) {
      --acc: oklch(0.75 0.17 350);
    }
  }
}

.cq-07 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: ui-rounded, "SF Pro Rounded", "Segoe UI Variable", Nunito, "Trebuchet MS", system-ui, sans-serif;
  line-height: 1.55;
}

.cq-07 *,
.cq-07 *::before,
.cq-07 *::after {
  box-sizing: border-box;
}

.cq-07__stage {
  max-width: 64rem;
  margin-inline: auto;
  padding: clamp(1rem, 3vw, 2.75rem);
  display: grid;
  gap: 1.5rem;
}

.cq-07__h {
  margin: 0;
  font-size: clamp(1.45rem, 1.1rem + 2vw, 2.15rem);
  font-weight: 700;
  letter-spacing: -0.01em;
}

.cq-07__lede {
  margin: 0.4rem 0 0;
  color: var(--mut);
  font-size: 0.9rem;
  max-width: 54ch;
}

.cq-07__lede code,
.cq-07__foot code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.82em;
}

.cq-07__vh,
.cq-07__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cq-07__tones {
  margin: 0;
  padding: 0;
  border: 0;
  min-inline-size: 0;
}

.cq-07__seg {
  padding: 0.4rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  border-radius: 999px;
  background: var(--surf);
  box-shadow: inset 2px 2px 5px var(--lo), inset -2px -2px 5px var(--hi);
  width: fit-content;
  max-inline-size: 100%;
}

.cq-07__opt {
  min-block-size: 2.75rem;
  min-inline-size: 5.5rem;
  padding: 0 1rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 999px;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--mut);
  cursor: pointer;
}

.cq-07__sr:checked + .cq-07__opt {
  color: var(--acc);
  background: var(--surf);
  box-shadow: 3px 3px 7px var(--lo), -3px -3px 7px var(--hi);
}

.cq-07__sr:focus-visible + .cq-07__opt {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cq-07__row {
  display: flex;
  flex-wrap: wrap;
  gap: 1.25rem;
}

.cq-07__side {
  flex: 1 1 18rem;
  min-inline-size: 0;
  display: grid;
  gap: 0.5rem;
  align-content: start;
}

.cq-07__cap {
  margin: 0;
  font-size: 0.74rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--mut);
}

.cq-07__frame {
  --cq-07-tone: calm;
}

.cq-07:has(#cq-07-featured:checked) .cq-07__frame {
  --cq-07-tone: featured;
}

.cq-07:has(#cq-07-retiring:checked) .cq-07__frame {
  --cq-07-tone: retiring;
}

.cq-07__frame--static {
  --cq-07-tone: static;
}

.cq-07__card {
  display: grid;
  gap: 0.4rem;
  padding: 1.5rem;
  border-radius: 20px;
  background: var(--calm-fill);
  border: 2px solid var(--calm-line);
  box-shadow: 6px 6px 14px var(--lo), -6px -6px 14px var(--hi);
}

.cq-07__badge {
  margin: 0;
  display: none;
  align-items: center;
  align-self: start;
  justify-self: start;
  padding: 0.2rem 0.6rem;
  border-radius: 999px;
  background: var(--acc);
  color: #fff;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.cq-07__title {
  margin: 0;
  font-size: 1.2rem;
  font-weight: 700;
}

.cq-07__price {
  margin: 0;
  font-size: 1.9rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.cq-07__price span {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--mut);
}

.cq-07__text {
  margin: 0;
  font-size: 0.85rem;
  color: var(--mut);
}

.cq-07__foot {
  margin: 0.5rem 0 0;
  font-size: 0.72rem;
  color: var(--mut);
}

.cq-07__card--featured {
  background: var(--feat-fill);
  border-color: var(--feat-line);
}

.cq-07__badge--featured {
  display: inline-flex;
}

.cq-07__title--featured {
  color: var(--acc);
  font-size: 1.35rem;
}

@container style(--cq-07-tone: featured) {
  .cq-07__card {
    background: var(--feat-fill);
    border-color: var(--feat-line);
  }

  .cq-07__badge {
    display: inline-flex;
  }

  .cq-07__title {
    color: var(--acc);
    font-size: 1.35rem;
  }

  .cq-07__price {
    letter-spacing: -0.02em;
  }
}

@container style(--cq-07-tone: retiring) {
  .cq-07__card {
    background: var(--ret-fill);
    border-color: var(--ret-line);
    border-style: dashed;
  }

  .cq-07__title {
    color: var(--mut);
  }

  .cq-07__price {
    opacity: 0.6;
  }
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. The
   pinned values are the demo's own [data-theme] declarations reused
   verbatim, so a toggled demo can never drift from how the same demo
   renders under the site theme. */

.cq-07 {
  position: relative;
}

.cq-07__theme {
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

.cq-07__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-07__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-07__themeopt {
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

.cq-07__themeopt:hover {
  opacity: 0.85;
}

.cq-07__themeinput:checked + .cq-07__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-07__themeinput:focus-visible + .cq-07__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-07:has(#cq-07-theme-light:checked) {
  --bg: #ece4dc;
  --surf: #f7f1ea;
  --line: #d3c4b4;
  --ink: #2a201a;
  --mut: #6e5c4e;
  --acc: #b0347a;
  --hi: rgba(255, 255, 255, 0.85);
  --lo: rgba(94, 74, 60, 0.22);
  --calm-fill: #f7f1ea;
  --calm-line: #d3c4b4;
  --feat-fill: #fbe6f1;
  --feat-line: #b0347a;
  --ret-fill: #ece7e0;
  --ret-line: #b3a698;
}

.cq-07:has(#cq-07-theme-dark:checked) {
  --bg: #191310;
  --surf: #241b16;
  --line: #453529;
  --ink: #f4e9df;
  --mut: #b5a293;
  --acc: #f070ac;
  --hi: rgba(255, 255, 255, 0.06);
  --lo: rgba(0, 0, 0, 0.55);
  --calm-fill: #241b16;
  --calm-line: #453529;
  --feat-fill: #3a1c2c;
  --feat-line: #f070ac;
  --ret-fill: #201a17;
  --ret-line: #4a4038;
}
```
