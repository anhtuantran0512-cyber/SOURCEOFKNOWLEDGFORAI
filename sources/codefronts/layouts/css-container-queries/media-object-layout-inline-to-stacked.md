---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/media-object-layout-inline-to-stacked/"
title: "Media Object Layout Inline to Stacked"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "The oldest layout pattern on the web &mdash; image beside text, stacking when there is no room &mdash; finally solved at component level."
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Media Object Layout Inline to Stacked
Source: https://codefronts.com/layouts/css-container-queries/media-object-layout-inline-to-stacked/

The oldest layout pattern on the web &mdash; image beside text, stacking when there is no room &mdash; finally solved at component level. Historically this needed a modifier class per context (media--stacked, media--compact); now it is one rule that answers to whatever column the object lands in. Kept deliberately plain, because the mechanism is the whole content.
## HTML
```html
<section class="cq-12" aria-labelledby="cq-12-h">
  <fieldset class="cq-12__theme">
    <legend class="cq-12__themelegend">Theme</legend>
    <input class="cq-12__themeinput" type="radio" name="cq-12-theme" id="cq-12-theme-auto" checked>
    <label class="cq-12__themeopt" for="cq-12-theme-auto">Auto</label>
    <input class="cq-12__themeinput" type="radio" name="cq-12-theme" id="cq-12-theme-light">
    <label class="cq-12__themeopt" for="cq-12-theme-light">Light</label>
    <input class="cq-12__themeinput" type="radio" name="cq-12-theme" id="cq-12-theme-dark">
    <label class="cq-12__themeopt" for="cq-12-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-12__stage">
    <header class="cq-12__head">
      <p class="cq-12__kicker">The Basalt Review</p>
      <h2 class="cq-12__h" id="cq-12-h">One media object, any column</h2>
      <p class="cq-12__lede">Identical markup in a wide column, a half column and a rail. The object reads the column, not the page.</p>
    </header>

    <div class="cq-12__row">
      <div class="cq-12__col cq-12__col--wide">
        <p class="cq-12__w">wide column</p>
        <article class="cq-12__media">
          <div class="cq-12__fig" role="img" aria-label="Illustration: layered ridges at dusk"></div>
          <div class="cq-12__text">
            <h3 class="cq-12__title">The long walk back to the printed page</h3>
            <p class="cq-12__body">Three magazines that stopped chasing scroll depth and started charging for paper again, and what happened to their readers.</p>
            <p class="cq-12__by">Sam Rivera &middot; 18 August</p>
          </div>
        </article>
      </div>

      <div class="cq-12__col cq-12__col--rail">
        <p class="cq-12__w">rail</p>
        <article class="cq-12__media">
          <div class="cq-12__fig" role="img" aria-label="Illustration: layered ridges at dusk"></div>
          <div class="cq-12__text">
            <h3 class="cq-12__title">The long walk back to the printed page</h3>
            <p class="cq-12__body">Three magazines that stopped chasing scroll depth and started charging for paper again.</p>
            <p class="cq-12__by">Sam Rivera &middot; 18 August</p>
          </div>
        </article>
      </div>
    </div>

    <div class="cq-12__col cq-12__col--resize">
      <p class="cq-12__w">drag this column's edge</p>
      <article class="cq-12__media">
        <div class="cq-12__fig" role="img" aria-label="Illustration: layered ridges at dusk"></div>
        <div class="cq-12__text">
          <h3 class="cq-12__title">The long walk back to the printed page</h3>
          <p class="cq-12__body">Three magazines that stopped chasing scroll depth and started charging for paper again, and what happened to their readers.</p>
          <p class="cq-12__by">Sam Rivera &middot; 18 August</p>
        </div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.cq-12,
.cq-12[data-theme="light"] {
  --bg: #fcfbf8;
  --ink: #16150f;
  --mut: #5f5c50;
  --line: #d9d5c7;
  --acc: #2f4f43;
}

.cq-12[data-theme="dark"] {
  --bg: #0f0f0d;
  --ink: #f4f2ea;
  --mut: #a09c8e;
  --line: #302e28;
  --acc: #9dc4b3;
}

@media (prefers-color-scheme: dark) {
  .cq-12:not([data-theme="light"]) {
    --bg: #0f0f0d;
    --ink: #f4f2ea;
    --mut: #a09c8e;
    --line: #302e28;
    --acc: #9dc4b3;
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .cq-12,
    .cq-12[data-theme="light"] {
    --acc: oklch(0.4 0.05 165);
  }

  .cq-12[data-theme="dark"] {
    --acc: oklch(0.82 0.06 165);
  }

  @media (prefers-color-scheme: dark) {
    .cq-12:not([data-theme="light"]) {
      --acc: oklch(0.82 0.06 165);
    }
  }
}

.cq-12 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: "Iowan Old Style", Georgia, "Times New Roman", serif;
  line-height: 1.6;
}

.cq-12 *,
.cq-12 *::before,
.cq-12 *::after {
  box-sizing: border-box;
}

.cq-12__stage {
  max-width: 68rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem);
  display: grid;
  gap: 2.25rem;
}

.cq-12__kicker {
  margin: 0 0 0.6rem;
  font-family: system-ui, sans-serif;
  font-size: 0.68rem;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--acc);
}

.cq-12__h {
  margin: 0;
  font-size: clamp(1.6rem, 1.2rem + 2.4vw, 2.7rem);
  font-weight: 400;
  line-height: 1.1;
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.cq-12__lede {
  margin: 0.7rem 0 0;
  font-size: 1rem;
  color: var(--mut);
  max-width: 48ch;
}

.cq-12__row {
  display: flex;
  flex-wrap: wrap;
  gap: 2.25rem;
  align-items: start;
}

.cq-12__col {
  container: cq-12-col / inline-size;
  min-inline-size: 0;
}

.cq-12__col--wide {
  flex: 1 1 30rem;
}

.cq-12__col--rail {
  flex: 0 1 15rem;
}

.cq-12__col--resize {
  resize: horizontal;
  overflow: auto;
  min-inline-size: 13rem;
  max-inline-size: 100%;
  padding-inline-end: 0.5rem;
}

.cq-12__w {
  margin: 0 0 0.75rem;
  padding-bottom: 0.4rem;
  border-bottom: 1px solid var(--line);
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.66rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--mut);
}

.cq-12__media {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.cq-12__fig {
  flex: none;
  aspect-ratio: 16 / 10;
  background: linear-gradient(175deg, #2f4f43 0%, #6f8f7f 42%, #d9cdb4 42%, #efe6d2 100%);
  background: linear-gradient(175deg, var(--acc) 0%, color-mix(in srgb, var(--acc) 55%, white) 42%, color-mix(in srgb, var(--acc) 14%, #efe6d2) 42%, var(--bg) 100%);
}

.cq-12__text {
  min-inline-size: 0;
}

.cq-12__title {
  margin: 0 0 0.4rem;
  font-size: 1.25rem;
  font-weight: 400;
  line-height: 1.2;
  letter-spacing: -0.01em;
  text-wrap: pretty;
}

.cq-12__body {
  margin: 0;
  font-size: 0.92rem;
  color: var(--mut);
}

.cq-12__by {
  margin: 0.6rem 0 0;
  font-family: system-ui, sans-serif;
  font-size: 0.7rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--acc);
}

@container cq-12-col (min-width: 24em) {
  .cq-12__media {
    flex-direction: row;
    align-items: flex-start;
    gap: 1.5rem;
  }

  .cq-12__fig {
    flex: 0 0 40%;
    aspect-ratio: 4 / 5;
  }

  .cq-12__title {
    font-size: 1.6rem;
  }

  .cq-12__body {
    font-size: 1rem;
  }
}

@container cq-12-col (min-width: 44em) {
  .cq-12__fig {
    flex-basis: 46%;
    aspect-ratio: 3 / 2;
  }

  .cq-12__title {
    font-size: 2rem;
  }
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. The
   pinned values are the demo's own [data-theme] declarations reused
   verbatim, so a toggled demo can never drift from how the same demo
   renders under the site theme. */

.cq-12 {
  position: relative;
}

.cq-12__theme {
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

.cq-12__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-12__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-12__themeopt {
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

.cq-12__themeopt:hover {
  opacity: 0.85;
}

.cq-12__themeinput:checked + .cq-12__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-12__themeinput:focus-visible + .cq-12__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-12:has(#cq-12-theme-light:checked) {
  --bg: #fcfbf8;
  --ink: #16150f;
  --mut: #5f5c50;
  --line: #d9d5c7;
  --acc: #2f4f43;
}

.cq-12:has(#cq-12-theme-dark:checked) {
  --bg: #0f0f0d;
  --ink: #f4f2ea;
  --mut: #a09c8e;
  --line: #302e28;
  --acc: #9dc4b3;
}
```
