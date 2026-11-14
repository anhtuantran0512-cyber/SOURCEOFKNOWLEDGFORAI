---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/container-queries-getting-started/"
title: "Container Queries Getting Started"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "The reference implementation the rest of this collection borrows from: container-type: inline-size on the parent, an @container (min-width: 21em) block in…"
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Container Queries Getting Started
Source: https://codefronts.com/layouts/css-container-queries/container-queries-getting-started/

The reference implementation the rest of this collection borrows from: container-type: inline-size on the parent, an @container (min-width: 21em) block in the stylesheet, and the child rules inside it. The same card markup sits in a wide slot and a narrow slot side by side, so one query produces two layouts, and an annotated panel labels each of the three moving parts.
## HTML
```html
<section class="cq-01" aria-labelledby="cq-01-h">
  <fieldset class="cq-01__theme">
    <legend class="cq-01__themelegend">Theme</legend>
    <input class="cq-01__themeinput" type="radio" name="cq-01-theme" id="cq-01-theme-auto" checked>
    <label class="cq-01__themeopt" for="cq-01-theme-auto">Auto</label>
    <input class="cq-01__themeinput" type="radio" name="cq-01-theme" id="cq-01-theme-light">
    <label class="cq-01__themeopt" for="cq-01-theme-light">Light</label>
    <input class="cq-01__themeinput" type="radio" name="cq-01-theme" id="cq-01-theme-dark">
    <label class="cq-01__themeopt" for="cq-01-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-01__stage">
    <header class="cq-01__head">
      <p class="cq-01__kicker">Container queries / 01</p>
      <h2 class="cq-01__h" id="cq-01-h">One query, two layouts</h2>
      <p class="cq-01__lede">The card below is the same markup in both slots. Only the slot width differs.</p>
    </header>

    <ol class="cq-01__anno">
      <li><span class="cq-01__n">1</span><div><b>Opt the parent in</b><code>.slot { container-type: inline-size }</code></div></li>
      <li><span class="cq-01__n">2</span><div><b>Ask the question</b><code>&#64;container (min-width: 21em)</code></div></li>
      <li><span class="cq-01__n">3</span><div><b>Style the children</b><code>.card { grid-template-columns: 8rem 1fr }</code></div></li>
    </ol>

    <div class="cq-01__row">
      <div class="cq-01__col">
        <p class="cq-01__label">Main column <span>wide slot</span></p>
        <div class="cq-01__slot cq-01__slot--wide">
          <article class="cq-01__card">
            <div class="cq-01__thumb" role="img" aria-label="Abstract gradient artwork"></div>
            <div class="cq-01__body">
              <p class="cq-01__tag">Field notes</p>
              <h3 class="cq-01__title">Meridian ships regional failover</h3>
              <p class="cq-01__text">Read replicas now promote in under nine seconds without operator input.</p>
              <p class="cq-01__meta">Priya Sharma &middot; 6 min read</p>
            </div>
          </article>
        </div>
      </div>

      <div class="cq-01__col cq-01__col--narrow">
        <p class="cq-01__label">Sidebar rail <span>narrow slot</span></p>
        <div class="cq-01__slot cq-01__slot--narrow">
          <article class="cq-01__card">
            <div class="cq-01__thumb" role="img" aria-label="Abstract gradient artwork"></div>
            <div class="cq-01__body">
              <p class="cq-01__tag">Field notes</p>
              <h3 class="cq-01__title">Meridian ships regional failover</h3>
              <p class="cq-01__text">Read replicas now promote in under nine seconds without operator input.</p>
              <p class="cq-01__meta">Priya Sharma &middot; 6 min read</p>
            </div>
          </article>
        </div>
      </div>
    </div>

    <p class="cq-01__foot">The wide slot is past 21em, so the query matches and the card goes horizontal. The narrow slot is not, so it keeps the stacked default.</p>
  </div>
</section>
```
## CSS
```css
.cq-01,
.cq-01[data-theme="light"] {
  --bg: #f4f5f7;
  --surf: #ffffff;
  --surf2: #eaecf1;
  --line: #d6d9e0;
  --ink: #15171c;
  --mut: #5d6473;
  --acc: #1f57cf;
  --accs: #e7eefc;
}

.cq-01[data-theme="dark"] {
  --bg: #0f1116;
  --surf: #171a21;
  --surf2: #1e222b;
  --line: #2b303b;
  --ink: #eceef3;
  --mut: #99a1b3;
  --acc: #7fa6ff;
  --accs: #1a2340;
}

@media (prefers-color-scheme: dark) {
  .cq-01:not([data-theme="light"]) {
    --bg: #0f1116;
    --surf: #171a21;
    --surf2: #1e222b;
    --line: #2b303b;
    --ink: #eceef3;
    --mut: #99a1b3;
    --acc: #7fa6ff;
    --accs: #1a2340;
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .cq-01,
    .cq-01[data-theme="light"] {
    --acc: oklch(0.5 0.19 264);
    --accs: oklch(0.95 0.035 264);
  }

  .cq-01[data-theme="dark"] {
    --acc: oklch(0.78 0.13 264);
    --accs: oklch(0.28 0.07 264);
  }

  @media (prefers-color-scheme: dark) {
    .cq-01:not([data-theme="light"]) {
      --acc: oklch(0.78 0.13 264);
      --accs: oklch(0.28 0.07 264);
    }
  }
}

.cq-01 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: ui-monospace, "SF Mono", "JetBrains Mono", Menlo, Consolas, monospace;
  font-size: 100%;
  line-height: 1.5;
}

.cq-01 *,
.cq-01 *::before,
.cq-01 *::after {
  box-sizing: border-box;
}

.cq-01__stage {
  max-width: 68rem;
  margin-inline: auto;
  padding: clamp(1rem, 3vw, 2.25rem);
  display: grid;
  gap: 1.25rem;
}

.cq-01__kicker {
  margin: 0 0 0.35rem;
  font-size: 0.7rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--acc);
}

.cq-01__h {
  margin: 0;
  font-size: clamp(1.35rem, 1rem + 2cqi, 2rem);
  font-weight: 600;
  letter-spacing: -0.01em;
  text-wrap: balance;
}

.cq-01__lede {
  margin: 0.35rem 0 0;
  color: var(--mut);
  font-size: 0.82rem;
  max-width: 46ch;
}

.cq-01__anno {
  margin: 0;
  padding: 0.75rem;
  list-style: none;
  display: grid;
  gap: 0.5rem;
  background: var(--surf);
  border: 1px solid var(--line);
  border-radius: 6px;
}

.cq-01__anno li {
  display: flex;
  gap: 0.6rem;
  align-items: flex-start;
  min-inline-size: 0;
}

.cq-01__anno li + li {
  border-top: 1px dashed var(--line);
  padding-top: 0.5rem;
}

.cq-01__n {
  flex: none;
  width: 1.35rem;
  height: 1.35rem;
  display: grid;
  place-items: center;
  border-radius: 50%;
  background: var(--accs);
  color: var(--acc);
  font-size: 0.7rem;
  font-weight: 700;
}

.cq-01__anno b {
  display: block;
  font-size: 0.74rem;
  letter-spacing: 0.02em;
}

.cq-01__anno code {
  display: block;
  margin-top: 0.15rem;
  font-size: 0.72rem;
  color: var(--mut);
  overflow-wrap: anywhere;
}

.cq-01__row {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  align-items: start;
}

.cq-01__col {
  flex: 1 1 22rem;
  min-inline-size: 0;
  display: grid;
  gap: 0.45rem;
}

.cq-01__col--narrow {
  flex: 0 1 17rem;
}

.cq-01__label {
  margin: 0;
  font-size: 0.72rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--mut);
  display: flex;
  gap: 0.4rem;
  align-items: baseline;
}

.cq-01__label span {
  color: var(--acc);
  text-transform: none;
  letter-spacing: 0;
}

.cq-01__slot {
  container-type: inline-size;
  container-name: cq-01-slot;
  padding: 0.6rem;
  background: var(--surf2);
  border: 1px dashed var(--line);
  border-radius: 8px;
}

.cq-01__card {
  display: grid;
  gap: 0.7rem;
  padding: 0.7rem;
  background: var(--surf);
  border: 1px solid var(--line);
  border-radius: 6px;
}

.cq-01__thumb {
  aspect-ratio: 16 / 9;
  border-radius: 4px;
  background: linear-gradient(135deg, #1f57cf 0%, #6f8cf5 45%, #b9c9ff 100%);
}

.cq-01__body {
  min-inline-size: 0;
  display: grid;
  gap: 0.3rem;
  align-content: start;
}

.cq-01__tag {
  margin: 0;
  font-size: 0.66rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--acc);
}

.cq-01__title {
  margin: 0;
  font-size: 0.95rem;
  font-weight: 600;
  line-height: 1.25;
}

.cq-01__text {
  margin: 0;
  font-size: 0.78rem;
  color: var(--mut);
}

.cq-01__meta {
  margin: 0.15rem 0 0;
  font-size: 0.7rem;
  color: var(--mut);
}

@container cq-01-slot (min-width: 21em) {
  .cq-01__card {
    grid-template-columns: 9rem 1fr;
    align-items: start;
    padding: 0.85rem;
  }

  .cq-01__thumb {
    aspect-ratio: auto;
    block-size: 100%;
    min-block-size: 5.5rem;
  }

  .cq-01__title {
    font-size: 1.1rem;
  }
}

.cq-01__foot {
  margin: 0;
  font-size: 0.74rem;
  color: var(--mut);
  border-top: 1px solid var(--line);
  padding-top: 0.75rem;
  max-width: 62ch;
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. The
   pinned values are the demo's own [data-theme] declarations reused
   verbatim, so a toggled demo can never drift from how the same demo
   renders under the site theme. */

.cq-01 {
  position: relative;
}

.cq-01__theme {
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

.cq-01__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-01__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-01__themeopt {
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

.cq-01__themeopt:hover {
  opacity: 0.85;
}

.cq-01__themeinput:checked + .cq-01__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-01__themeinput:focus-visible + .cq-01__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-01:has(#cq-01-theme-light:checked) {
  --bg: #f4f5f7;
  --surf: #ffffff;
  --surf2: #eaecf1;
  --line: #d6d9e0;
  --ink: #15171c;
  --mut: #5d6473;
  --acc: #1f57cf;
  --accs: #e7eefc;
}

.cq-01:has(#cq-01-theme-dark:checked) {
  --bg: #0f1116;
  --surf: #171a21;
  --surf2: #1e222b;
  --line: #2b303b;
  --ink: #eceef3;
  --mut: #99a1b3;
  --acc: #7fa6ff;
  --accs: #1a2340;
}
```
