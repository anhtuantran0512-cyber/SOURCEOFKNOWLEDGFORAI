---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/card-component-adapting-to-container-width/"
title: "Card Component Adapting to Container Width"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "One card component in three placements &mdash; a wide feature slot, a mid-width grid cell and a narrow rail &mdash; with layout, image ratio and type scale…"
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Card Component Adapting to Container Width
Source: https://codefronts.com/layouts/css-container-queries/card-component-adapting-to-container-width/

One card component in three placements &mdash; a wide feature slot, a mid-width grid cell and a narrow rail &mdash; with layout, image ratio and type scale all changing from container width alone. The markup and class names are byte-for-byte identical in all three; nothing about the page layout is baked into the component, which is the point that makes the whole idea click.
## HTML
```html
<section class="cq-04" aria-labelledby="cq-04-h">
  <fieldset class="cq-04__theme">
    <legend class="cq-04__themelegend">Theme</legend>
    <input class="cq-04__themeinput" type="radio" name="cq-04-theme" id="cq-04-theme-auto" checked>
    <label class="cq-04__themeopt" for="cq-04-theme-auto">Auto</label>
    <input class="cq-04__themeinput" type="radio" name="cq-04-theme" id="cq-04-theme-light">
    <label class="cq-04__themeopt" for="cq-04-theme-light">Light</label>
    <input class="cq-04__themeinput" type="radio" name="cq-04-theme" id="cq-04-theme-dark">
    <label class="cq-04__themeopt" for="cq-04-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-04__stage">
    <header class="cq-04__head">
      <p class="cq-04__kicker">Basalt Analytics &middot; component library</p>
      <h2 class="cq-04__h" id="cq-04-h">One card, three placements</h2>
    </header>

    <div class="cq-04__row">
      <div class="cq-04__col cq-04__col--wide">
        <p class="cq-04__label">Feature slot</p>
        <div class="cq-04__slot">
          <article class="cq-04__card">
            <div class="cq-04__art" role="img" aria-label="Report cover artwork"></div>
            <p class="cq-04__tag">Quarterly report</p>
            <h3 class="cq-04__title">Where activation actually breaks</h3>
            <p class="cq-04__text">Nine hundred onboarding sessions, replayed and grouped by the first step where intent drops off.</p>
            <div class="cq-04__foot">
              <span class="cq-04__who"><span class="cq-04__av" aria-hidden="true">AC</span>Alex Chen</span>
              <span class="cq-04__read">14 min</span>
            </div>
          </article>
        </div>
      </div>

      <div class="cq-04__col cq-04__col--mid">
        <p class="cq-04__label">Grid cell</p>
        <div class="cq-04__slot">
          <article class="cq-04__card">
            <div class="cq-04__art" role="img" aria-label="Report cover artwork"></div>
            <p class="cq-04__tag">Quarterly report</p>
            <h3 class="cq-04__title">Where activation actually breaks</h3>
            <p class="cq-04__text">Nine hundred onboarding sessions, replayed and grouped by the first step where intent drops off.</p>
            <div class="cq-04__foot">
              <span class="cq-04__who"><span class="cq-04__av" aria-hidden="true">AC</span>Alex Chen</span>
              <span class="cq-04__read">14 min</span>
            </div>
          </article>
        </div>
      </div>

      <div class="cq-04__col cq-04__col--rail">
        <p class="cq-04__label">Narrow rail</p>
        <div class="cq-04__slot">
          <article class="cq-04__card">
            <div class="cq-04__art" role="img" aria-label="Report cover artwork"></div>
            <p class="cq-04__tag">Quarterly report</p>
            <h3 class="cq-04__title">Where activation actually breaks</h3>
            <p class="cq-04__text">Nine hundred onboarding sessions, replayed and grouped by the first step where intent drops off.</p>
            <div class="cq-04__foot">
              <span class="cq-04__who"><span class="cq-04__av" aria-hidden="true">AC</span>Alex Chen</span>
              <span class="cq-04__read">14 min</span>
            </div>
          </article>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.cq-04,
.cq-04[data-theme="light"] {
  --bg: #f7f9fc;
  --surf: #ffffff;
  --line: #dde4ee;
  --ink: #0d1b2e;
  --mut: #5a6a80;
  --acc: #1665d8;
  --acc2: #6aa5f5;
  --sh: 0 1px 2px rgba(13, 27, 46, 0.06), 0 8px 24px rgba(13, 27, 46, 0.07);
}

.cq-04[data-theme="dark"] {
  --bg: #0a1220;
  --surf: #111c2e;
  --line: #21304a;
  --ink: #e9eff8;
  --mut: #93a4bd;
  --acc: #62a0ff;
  --acc2: #9cc4ff;
  --sh: 0 1px 2px rgba(0, 0, 0, 0.5), 0 10px 28px rgba(0, 0, 0, 0.4);
}

@media (prefers-color-scheme: dark) {
  .cq-04:not([data-theme="light"]) {
    --bg: #0a1220;
    --surf: #111c2e;
    --line: #21304a;
    --ink: #e9eff8;
    --mut: #93a4bd;
    --acc: #62a0ff;
    --acc2: #9cc4ff;
    --sh: 0 1px 2px rgba(0, 0, 0, 0.5), 0 10px 28px rgba(0, 0, 0, 0.4);
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .cq-04,
    .cq-04[data-theme="light"] {
    --acc: oklch(0.53 0.17 255);
    --acc2: oklch(0.72 0.12 255);
  }

  .cq-04[data-theme="dark"] {
    --acc: oklch(0.72 0.14 255);
    --acc2: oklch(0.84 0.09 255);
  }

  @media (prefers-color-scheme: dark) {
    .cq-04:not([data-theme="light"]) {
      --acc: oklch(0.72 0.14 255);
      --acc2: oklch(0.84 0.09 255);
    }
  }
}

.cq-04 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, -apple-system, "Segoe UI", Helvetica, sans-serif;
  line-height: 1.55;
}

.cq-04 *,
.cq-04 *::before,
.cq-04 *::after {
  box-sizing: border-box;
}

.cq-04__stage {
  max-width: 78rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 3vw, 2.75rem);
  display: grid;
  gap: 1.75rem;
}

.cq-04__kicker {
  margin: 0 0 0.4rem;
  font-size: 0.75rem;
  letter-spacing: 0.06em;
  color: var(--acc);
  font-weight: 600;
}

.cq-04__h {
  margin: 0;
  font-size: clamp(1.4rem, 1.1rem + 1.6vw, 2rem);
  font-weight: 650;
  letter-spacing: -0.02em;
}

.cq-04__row {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  align-items: start;
}

.cq-04__col {
  min-inline-size: 0;
  display: grid;
  gap: 0.6rem;
}

.cq-04__col--wide {
  flex: 1 1 32rem;
}

.cq-04__col--mid {
  flex: 1 1 19rem;
}

.cq-04__col--rail {
  flex: 0 1 14.5rem;
}

.cq-04__label {
  margin: 0;
  font-size: 0.7rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--mut);
  font-weight: 600;
}

.cq-04__slot {
  container: cq-04-slot / inline-size;
}

.cq-04__card {
  display: grid;
  grid-template-areas: "art" "tag" "title" "text" "foot";
  gap: 0.55rem;
  padding: 1.25rem;
  background: var(--surf);
  border: 1px solid var(--line);
  border-radius: 14px;
  box-shadow: var(--sh);
}

.cq-04__art {
  grid-area: art;
  aspect-ratio: 4 / 3;
  border-radius: 10px;
  background: linear-gradient(140deg, #1665d8, #6aa5f5 60%, #cfe0fb);
  background: linear-gradient(140deg, var(--acc), var(--acc2) 60%, color-mix(in srgb, var(--acc2) 35%, white));
}

.cq-04__tag {
  grid-area: tag;
  margin: 0;
  font-size: 0.68rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--acc);
  font-weight: 700;
}

.cq-04__title {
  grid-area: title;
  margin: 0;
  font-size: 1.05rem;
  font-weight: 650;
  line-height: 1.25;
  letter-spacing: -0.01em;
  text-wrap: balance;
}

.cq-04__text {
  grid-area: text;
  margin: 0;
  font-size: 0.85rem;
  color: var(--mut);
}

.cq-04__foot {
  grid-area: foot;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 0.75rem;
  align-items: center;
  justify-content: space-between;
  padding-top: 0.6rem;
  border-top: 1px solid var(--line);
  font-size: 0.78rem;
  color: var(--mut);
}

.cq-04__who {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  min-inline-size: 0;
}

.cq-04__av {
  inline-size: 1.6rem;
  block-size: 1.6rem;
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: color-mix(in srgb, var(--acc) 18%, transparent);
  color: var(--acc);
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.02em;
}

.cq-04__read {
  font-variant-numeric: tabular-nums;
}

@container cq-04-slot (min-width: 17em) {
  .cq-04__card {
    grid-template-areas: "art tag" "art title" "art text" "art foot";
    grid-template-columns: 7.5rem 1fr;
    column-gap: 1rem;
    align-content: start;
  }

  .cq-04__art {
    aspect-ratio: auto;
    block-size: 100%;
    min-block-size: 6rem;
  }
}

@container cq-04-slot (min-width: 30em) {
  .cq-04__card {
    grid-template-areas: "art art" "tag tag" "title title" "text text" "foot foot";
    grid-template-columns: 1fr;
    padding: 1.75rem;
    gap: 0.7rem 1rem;
  }

  .cq-04__art {
    aspect-ratio: 21 / 9;
    block-size: auto;
  }

  .cq-04__title {
    font-size: 1.65rem;
  }

  .cq-04__text {
    font-size: 0.95rem;
    max-width: 52ch;
  }
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. The
   pinned values are the demo's own [data-theme] declarations reused
   verbatim, so a toggled demo can never drift from how the same demo
   renders under the site theme. */

.cq-04 {
  position: relative;
}

.cq-04__theme {
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

.cq-04__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-04__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-04__themeopt {
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

.cq-04__themeopt:hover {
  opacity: 0.85;
}

.cq-04__themeinput:checked + .cq-04__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-04__themeinput:focus-visible + .cq-04__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-04:has(#cq-04-theme-light:checked) {
  --bg: #f7f9fc;
  --surf: #ffffff;
  --line: #dde4ee;
  --ink: #0d1b2e;
  --mut: #5a6a80;
  --acc: #1665d8;
  --acc2: #6aa5f5;
  --sh: 0 1px 2px rgba(13, 27, 46, 0.06), 0 8px 24px rgba(13, 27, 46, 0.07);
}

.cq-04:has(#cq-04-theme-dark:checked) {
  --bg: #0a1220;
  --surf: #111c2e;
  --line: #21304a;
  --ink: #e9eff8;
  --mut: #93a4bd;
  --acc: #62a0ff;
  --acc2: #9cc4ff;
  --sh: 0 1px 2px rgba(0, 0, 0, 0.5), 0 10px 28px rgba(0, 0, 0, 0.4);
}
```
