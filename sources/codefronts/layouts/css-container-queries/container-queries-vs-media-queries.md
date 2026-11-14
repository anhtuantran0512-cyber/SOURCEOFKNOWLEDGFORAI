---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/container-queries-vs-media-queries/"
title: "Container Queries vs Media Queries"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "The same component wired both ways, in a layout that breaks the media-query version: at one viewport width the card looks right in the main column and wrong…"
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Container Queries vs Media Queries
Source: https://codefronts.com/layouts/css-container-queries/container-queries-vs-media-queries/

The same component wired both ways, in a layout that breaks the media-query version: at one viewport width the card looks right in the main column and wrong in the sidebar, because the viewport says nothing about the space the component actually occupies. The demo then states the honest division of labour &mdash; media queries still own page-level, print and prefers-* decisions.
## HTML
```html
<section class="cq-06" aria-labelledby="cq-06-h">
  <fieldset class="cq-06__theme">
    <legend class="cq-06__themelegend">Theme</legend>
    <input class="cq-06__themeinput" type="radio" name="cq-06-theme" id="cq-06-theme-auto" checked>
    <label class="cq-06__themeopt" for="cq-06-theme-auto">Auto</label>
    <input class="cq-06__themeinput" type="radio" name="cq-06-theme" id="cq-06-theme-light">
    <label class="cq-06__themeopt" for="cq-06-theme-light">Light</label>
    <input class="cq-06__themeinput" type="radio" name="cq-06-theme" id="cq-06-theme-dark">
    <label class="cq-06__themeopt" for="cq-06-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-06__stage">
    <header class="cq-06__head">
      <h2 class="cq-06__h" id="cq-06-h">Same viewport, different answers</h2>
      <p class="cq-06__lede">Both lanes are identical markup at the same window width. Only the query mechanism differs.</p>
    </header>

    <section class="cq-06__lane cq-06__lane--bad" aria-label="Media query version">
      <p class="cq-06__tag"><span class="cq-06__x" aria-hidden="true">&times;</span> Media query &middot; <code>&#64;media (min-width: 30em)</code></p>
      <div class="cq-06__pair">
        <div class="cq-06__main">
          <article class="cq-06__card cq-06__card--mq">
            <div class="cq-06__art" aria-hidden="true"></div>
            <div class="cq-06__body">
              <h3>Nova Freight rate card</h3>
              <p>Lane pricing refreshed weekly from carrier tenders.</p>
            </div>
          </article>
        </div>
        <div class="cq-06__rail">
          <article class="cq-06__card cq-06__card--mq">
            <div class="cq-06__art" aria-hidden="true"></div>
            <div class="cq-06__body">
              <h3>Nova Freight rate card</h3>
              <p>Lane pricing refreshed weekly from carrier tenders.</p>
            </div>
          </article>
          <p class="cq-06__note">Viewport is wide, so the rail gets the wide layout it cannot fit.</p>
        </div>
      </div>
    </section>

    <section class="cq-06__lane cq-06__lane--good" aria-label="Container query version">
      <p class="cq-06__tag"><span class="cq-06__ok" aria-hidden="true">&check;</span> Container query &middot; <code>&#64;container cq-06-slot (min-width: 26em)</code></p>
      <div class="cq-06__pair">
        <div class="cq-06__main">
          <div class="cq-06__slot">
            <article class="cq-06__card cq-06__card--cq">
              <div class="cq-06__art" aria-hidden="true"></div>
              <div class="cq-06__body">
                <h3>Nova Freight rate card</h3>
                <p>Lane pricing refreshed weekly from carrier tenders.</p>
              </div>
            </article>
          </div>
        </div>
        <div class="cq-06__rail">
          <div class="cq-06__slot">
            <article class="cq-06__card cq-06__card--cq">
              <div class="cq-06__art" aria-hidden="true"></div>
              <div class="cq-06__body">
                <h3>Nova Freight rate card</h3>
                <p>Lane pricing refreshed weekly from carrier tenders.</p>
              </div>
            </article>
          </div>
          <p class="cq-06__note">The rail is under 26em, so this copy of the card stacks.</p>
        </div>
      </div>
    </section>

    <ul class="cq-06__split">
      <li><b>Media queries keep</b> page-level layout, print, <code>prefers-reduced-motion</code>, <code>prefers-color-scheme</code>, pointer coarseness</li>
      <li><b>Container queries take</b> every decision a component makes about its own internal layout</li>
    </ul>
  </div>
</section>
```
## CSS
```css
.cq-06,
.cq-06[data-theme="light"] {
  --bg: #eef2f8;
  --surf: #ffffff;
  --surf2: #e0e7f2;
  --line: #c3cfe0;
  --ink: #0b1830;
  --mut: #55658033;
  --muttxt: #4d5f7d;
  --acc: #0e7490;
  --bad: #b4263b;
  --glow: rgba(14, 116, 144, 0.18);
}

.cq-06[data-theme="dark"] {
  --bg: #060c1a;
  --surf: #0d1730;
  --surf2: #101d3c;
  --line: #1e2f55;
  --ink: #e4ecff;
  --mut: #7f92b833;
  --muttxt: #8fa2c8;
  --acc: #35d6f2;
  --bad: #ff6b81;
  --glow: rgba(53, 214, 242, 0.28);
}

@media (prefers-color-scheme: dark) {
  .cq-06:not([data-theme="light"]) {
    --bg: #060c1a;
    --surf: #0d1730;
    --surf2: #101d3c;
    --line: #1e2f55;
    --ink: #e4ecff;
    --mut: #7f92b833;
    --muttxt: #8fa2c8;
    --acc: #35d6f2;
    --bad: #ff6b81;
    --glow: rgba(53, 214, 242, 0.28);
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .cq-06,
    .cq-06[data-theme="light"] {
    --acc: oklch(0.55 0.11 210);
    --bad: oklch(0.52 0.19 20);
  }

  .cq-06[data-theme="dark"] {
    --acc: oklch(0.85 0.14 205);
    --bad: oklch(0.72 0.17 18);
  }

  @media (prefers-color-scheme: dark) {
    .cq-06:not([data-theme="light"]) {
      --acc: oklch(0.85 0.14 205);
      --bad: oklch(0.72 0.17 18);
    }
  }
}

.cq-06 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: "Archivo Narrow", "Roboto Condensed", "Liberation Sans Narrow", "Segoe UI", system-ui, sans-serif;
  line-height: 1.45;
}

.cq-06 *,
.cq-06 *::before,
.cq-06 *::after {
  box-sizing: border-box;
}

.cq-06__stage {
  max-width: 74rem;
  margin-inline: auto;
  padding: clamp(1rem, 3vw, 2.5rem);
  display: grid;
  gap: 1.1rem;
}

.cq-06__h {
  margin: 0;
  font-size: clamp(1.4rem, 1.1rem + 2vw, 2.2rem);
  font-weight: 700;
  letter-spacing: 0.01em;
  text-transform: uppercase;
}

.cq-06__lede {
  margin: 0.3rem 0 0;
  color: var(--muttxt);
  font-size: 0.88rem;
  max-width: 56ch;
}

.cq-06__lane {
  padding: 0.9rem;
  border-radius: 10px;
  background: var(--surf2);
  border: 1px solid var(--line);
}

.cq-06__lane--good {
  box-shadow: 0 0 0 1px var(--acc), 0 0 32px var(--glow);
}

.cq-06__tag {
  margin: 0 0 0.7rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
  align-items: center;
  font-size: 0.78rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muttxt);
}

.cq-06__tag code {
  font-family: ui-monospace, Menlo, monospace;
  text-transform: none;
  letter-spacing: 0;
  font-size: 0.74rem;
}

.cq-06__x,
.cq-06__ok {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  display: grid;
  place-items: center;
  border-radius: 50%;
  font-size: 0.75rem;
  font-weight: 700;
  color: #fff;
  background: var(--bad);
}

.cq-06__ok {
  background: var(--acc);
  color: #04121a;
}

.cq-06__pair {
  display: flex;
  flex-wrap: wrap;
  gap: 0.9rem;
  align-items: start;
}

.cq-06__main {
  flex: 1 1 26rem;
  min-inline-size: 0;
}

.cq-06__rail {
  flex: 0 1 15rem;
  min-inline-size: 0;
  display: grid;
  gap: 0.5rem;
}

.cq-06__slot {
  container: cq-06-slot / inline-size;
}

.cq-06__card {
  display: grid;
  gap: 0.6rem;
  padding: 0.8rem;
  background: var(--surf);
  border: 1px solid var(--line);
  border-radius: 8px;
}

.cq-06__art {
  aspect-ratio: 16 / 9;
  max-block-size: 9rem;
  border-radius: 5px;
  background: conic-gradient(from 210deg at 30% 40%, #0e7490, #7dd3fc, #0e7490);
  background: conic-gradient(from 210deg at 30% 40%, var(--acc), color-mix(in srgb, var(--acc) 35%, white), var(--acc));
}

.cq-06__body {
  min-inline-size: 0;
}

.cq-06__card h3 {
  margin: 0 0 0.2rem;
  font-size: 1rem;
  font-weight: 700;
}

.cq-06__card p {
  margin: 0;
  font-size: 0.82rem;
  color: var(--muttxt);
}

.cq-06__note {
  margin: 0;
  font-size: 0.74rem;
  color: var(--muttxt);
  font-style: italic;
}

.cq-06__lane--bad .cq-06__note {
  color: var(--bad);
  font-style: normal;
}

@media (min-width: 30em) {
  .cq-06__card--mq {
    grid-template-columns: 8rem 1fr;
    align-items: center;
  }

  .cq-06__card--mq .cq-06__art {
    aspect-ratio: 1;
  }

  .cq-06__card--mq h3 {
    font-size: 1.15rem;
  }
}

@container cq-06-slot (min-width: 26em) {
  .cq-06__card--cq {
    grid-template-columns: 8rem 1fr;
    align-items: center;
  }

  .cq-06__card--cq .cq-06__art {
    aspect-ratio: 1;
  }

  .cq-06__card--cq h3 {
    font-size: 1.15rem;
  }
}

.cq-06__split {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.5rem;
}

.cq-06__split li {
  padding: 0.65rem 0.75rem;
  border-inline-start: 3px solid var(--acc);
  background: var(--surf);
  border-radius: 0 6px 6px 0;
  font-size: 0.82rem;
  color: var(--muttxt);
}

.cq-06__split b {
  color: var(--ink);
}

.cq-06__split code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.76rem;
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. The
   pinned values are the demo's own [data-theme] declarations reused
   verbatim, so a toggled demo can never drift from how the same demo
   renders under the site theme. */

.cq-06 {
  position: relative;
}

.cq-06__theme {
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

.cq-06__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-06__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-06__themeopt {
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

.cq-06__themeopt:hover {
  opacity: 0.85;
}

.cq-06__themeinput:checked + .cq-06__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-06__themeinput:focus-visible + .cq-06__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-06:has(#cq-06-theme-light:checked) {
  --bg: #eef2f8;
  --surf: #ffffff;
  --surf2: #e0e7f2;
  --line: #c3cfe0;
  --ink: #0b1830;
  --mut: #55658033;
  --muttxt: #4d5f7d;
  --acc: #0e7490;
  --bad: #b4263b;
  --glow: rgba(14, 116, 144, 0.18);
}

.cq-06:has(#cq-06-theme-dark:checked) {
  --bg: #060c1a;
  --surf: #0d1730;
  --surf2: #101d3c;
  --line: #1e2f55;
  --ink: #e4ecff;
  --mut: #7f92b833;
  --muttxt: #8fa2c8;
  --acc: #35d6f2;
  --bad: #ff6b81;
  --glow: rgba(53, 214, 242, 0.28);
}
```
