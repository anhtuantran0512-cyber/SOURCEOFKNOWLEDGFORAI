---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/debugging-container-query-sizing-issues/"
title: "Debugging Container Query Sizing Issues"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "Five ways a container query silently does nothing, as broken-then-fixed pairs: container-type missing on the parent, container-type on the element being…"
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Debugging Container Query Sizing Issues
Source: https://codefronts.com/layouts/css-container-queries/debugging-container-query-sizing-issues/

Five ways a container query silently does nothing, as broken-then-fixed pairs: container-type missing on the parent, container-type on the element being styled, a container with no definite inline size, an unnamed query resolving too near, and size used where inline-size was meant. Each pair is live, so the fix is visible rather than described.
## HTML
```html
<section class="cq-20" aria-labelledby="cq-20-h">
  <fieldset class="cq-20__theme">
    <legend class="cq-20__themelegend">Theme</legend>
    <input class="cq-20__themeinput" type="radio" name="cq-20-theme" id="cq-20-theme-auto" checked>
    <label class="cq-20__themeopt" for="cq-20-theme-auto">Auto</label>
    <input class="cq-20__themeinput" type="radio" name="cq-20-theme" id="cq-20-theme-light">
    <label class="cq-20__themeopt" for="cq-20-theme-light">Light</label>
    <input class="cq-20__themeinput" type="radio" name="cq-20-theme" id="cq-20-theme-dark">
    <label class="cq-20__themeopt" for="cq-20-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-20__stage">
    <header class="cq-20__head">
      <p class="cq-20__kicker">Checklist &middot; in order of how often it bites</p>
      <h2 class="cq-20__h" id="cq-20-h">Why isn't my container query working?</h2>
    </header>

    <ol class="cq-20__list">
      <li class="cq-20__case">
        <h3 class="cq-20__ct"><span class="cq-20__no">01</span>container-type is missing on the parent</h3>
        <p class="cq-20__cd">The query was written for the element to style, and nothing above it opted in.</p>
        <div class="cq-20__pair">
          <div class="cq-20__mini"><p class="cq-20__mt cq-20__mt--bad">broken</p><div class="cq-20__w1b"><p class="cq-20__probe cq-20__p1"><span class="cq-20__f">no match</span><span class="cq-20__p">matched</span></p></div></div>
          <div class="cq-20__mini"><p class="cq-20__mt cq-20__mt--ok">fixed</p><div class="cq-20__w1f"><p class="cq-20__probe cq-20__p1"><span class="cq-20__f">no match</span><span class="cq-20__p">matched</span></p></div></div>
        </div>
      </li>

      <li class="cq-20__case">
        <h3 class="cq-20__ct"><span class="cq-20__no">02</span>container-type is on the element being styled</h3>
        <p class="cq-20__cd">A query never styles its own container. Move the container up one level.</p>
        <div class="cq-20__pair">
          <div class="cq-20__mini"><p class="cq-20__mt cq-20__mt--bad">broken</p><div class="cq-20__w2b"><p class="cq-20__probe cq-20__p2b"><span class="cq-20__f">no match</span><span class="cq-20__p">matched</span></p></div></div>
          <div class="cq-20__mini"><p class="cq-20__mt cq-20__mt--ok">fixed</p><div class="cq-20__w2f"><p class="cq-20__probe cq-20__p2f"><span class="cq-20__f">no match</span><span class="cq-20__p">matched</span></p></div></div>
        </div>
      </li>

      <li class="cq-20__case">
        <h3 class="cq-20__ct"><span class="cq-20__no">03</span>the container has no definite inline size</h3>
        <p class="cq-20__cd">A display: contents wrapper generates no box, so containment cannot apply and the declaration is ignored.</p>
        <div class="cq-20__pair">
          <div class="cq-20__mini"><p class="cq-20__mt cq-20__mt--bad">broken &middot; display: contents</p><div class="cq-20__w3b"><p class="cq-20__probe cq-20__p3"><span class="cq-20__f">no match</span><span class="cq-20__p">matched</span></p></div></div>
          <div class="cq-20__mini"><p class="cq-20__mt cq-20__mt--ok">fixed &middot; display: block</p><div class="cq-20__w3f"><p class="cq-20__probe cq-20__p3"><span class="cq-20__f">no match</span><span class="cq-20__p">matched</span></p></div></div>
        </div>
      </li>

      <li class="cq-20__case">
        <h3 class="cq-20__ct"><span class="cq-20__no">04</span>an unnamed query found a nearer container</h3>
        <p class="cq-20__cd">Resolution stops at the nearest ancestor container. Name the one you meant.</p>
        <div class="cq-20__pair">
          <div class="cq-20__mini"><p class="cq-20__mt cq-20__mt--bad">broken &middot; unnamed</p><div class="cq-20__w4"><div class="cq-20__inner"><p class="cq-20__probe cq-20__p4b"><span class="cq-20__f">no match</span><span class="cq-20__p">matched</span></p></div></div></div>
          <div class="cq-20__mini"><p class="cq-20__mt cq-20__mt--ok">fixed &middot; named</p><div class="cq-20__w4"><div class="cq-20__inner"><p class="cq-20__probe cq-20__p4f"><span class="cq-20__f">no match</span><span class="cq-20__p">matched</span></p></div></div></div>
        </div>
      </li>

      <li class="cq-20__case">
        <h3 class="cq-20__ct"><span class="cq-20__no">05</span>size was used where inline-size was meant</h3>
        <p class="cq-20__cd">The block axis collapses, so the bug looks like a layout error, not a query error.</p>
        <div class="cq-20__pair">
          <div class="cq-20__mini"><p class="cq-20__mt cq-20__mt--bad">broken &middot; container-type: size</p><div class="cq-20__w5b"><p class="cq-20__probe cq-20__p5">block axis collapsed to zero</p></div></div>
          <div class="cq-20__mini"><p class="cq-20__mt cq-20__mt--ok">fixed &middot; inline-size</p><div class="cq-20__w5f"><p class="cq-20__probe cq-20__p5">height from content, query fires</p></div></div>
        </div>
      </li>
    </ol>
  </div>
</section>
```
## CSS
```css
.cq-20,
.cq-20[data-theme="dark"] {
  --bg: #0b0d10;
  --surf: #14171c;
  --surf2: #1b1f26;
  --line: #262c35;
  --ink: #e7ebf0;
  --mut: #8a93a1;
  --ok: #3ecf8e;
  --bad: #ff6a5e;
}

.cq-20[data-theme="light"] {
  --bg: #f5f6f8;
  --surf: #ffffff;
  --surf2: #eef0f3;
  --line: #d7dbe1;
  --ink: #12161c;
  --mut: #5a6472;
  --ok: #12805c;
  --bad: #b3261e;
}

@media (prefers-color-scheme: light) {
  .cq-20:not([data-theme="dark"]) {
    --bg: #f5f6f8;
    --surf: #ffffff;
    --surf2: #eef0f3;
    --line: #d7dbe1;
    --ink: #12161c;
    --mut: #5a6472;
    --ok: #12805c;
    --bad: #b3261e;
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .cq-20,
    .cq-20[data-theme="dark"] {
    --ok: oklch(0.8 0.15 160);
    --bad: oklch(0.72 0.18 25);
  }

  .cq-20[data-theme="light"] {
    --ok: oklch(0.5 0.12 160);
    --bad: oklch(0.5 0.18 28);
  }

  @media (prefers-color-scheme: light) {
    .cq-20:not([data-theme="dark"]) {
      --ok: oklch(0.5 0.12 160);
      --bad: oklch(0.5 0.18 28);
    }
  }
}

.cq-20 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: ui-monospace, "SF Mono", "JetBrains Mono", Menlo, Consolas, monospace;
  line-height: 1.4;
}

.cq-20 *,
.cq-20 *::before,
.cq-20 *::after {
  box-sizing: border-box;
}

.cq-20__stage {
  max-width: 72rem;
  margin-inline: auto;
  padding: clamp(0.85rem, 3vw, 2.25rem);
  display: grid;
  gap: 1rem;
}

.cq-20__kicker {
  margin: 0 0 0.3rem;
  font-size: 0.66rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--mut);
}

.cq-20__h {
  margin: 0;
  font-size: clamp(1.15rem, 0.95rem + 1.5vw, 1.7rem);
  font-weight: 700;
  letter-spacing: -0.01em;
}

.cq-20__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.75rem;
}

.cq-20__case {
  padding: 0.85rem;
  background: var(--surf);
  border: 1px solid var(--line);
  border-radius: 6px;
  display: grid;
  gap: 0.55rem;
}

.cq-20__ct {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-items: baseline;
  font-size: 0.85rem;
  font-weight: 600;
}

.cq-20__no {
  color: var(--bad);
  font-size: 0.72rem;
  font-weight: 700;
}

.cq-20__cd {
  margin: 0;
  font-size: 0.74rem;
  color: var(--mut);
  max-width: 76ch;
}

.cq-20__pair {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
}

.cq-20__mini {
  flex: 1 1 14rem;
  min-inline-size: 0;
  display: grid;
  gap: 0.3rem;
  align-content: start;
}

.cq-20__mt {
  margin: 0;
  font-size: 0.64rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.cq-20__mt--bad {
  color: var(--bad);
}

.cq-20__mt--ok {
  color: var(--ok);
}

.cq-20__probe {
  margin: 0;
  padding: 0.5rem 0.6rem;
  background: var(--surf2);
  border: 1px dashed var(--bad);
  border-radius: 4px;
  font-size: 0.72rem;
  color: var(--bad);
}

.cq-20__p {
  display: none;
}

.cq-20__w1f {
  container: cq-20-a / inline-size;
}

.cq-20__w2b {
  padding: 0;
}

.cq-20__p2b {
  container: cq-20-b / inline-size;
}

.cq-20__w2f {
  container: cq-20-b2 / inline-size;
}

.cq-20__w3b {
  display: contents;
  container: cq-20-c / inline-size;
}

.cq-20__w3f {
  display: block;
  container: cq-20-c2 / inline-size;
}

.cq-20__w4 {
  container: cq-20-d / inline-size;
}

.cq-20__inner {
  container-type: inline-size;
  max-inline-size: 9rem;
}

.cq-20__w5b {
  container-type: size;
  border: 1px solid var(--bad);
}

.cq-20__w5f {
  container-type: inline-size;
  border: 1px solid var(--ok);
}

.cq-20__w5b .cq-20__probe,
.cq-20__w5f .cq-20__probe {
  border-style: solid;
}

.cq-20__w5f .cq-20__probe {
  border-color: var(--ok);
  color: var(--ok);
}

@container cq-20-a (min-width: 8em) {
  .cq-20__p1 {
    border-style: solid;
    border-color: var(--ok);
    color: var(--ok);
  }

  .cq-20__p1 .cq-20__f {
    display: none;
  }

  .cq-20__p1 .cq-20__p {
    display: inline;
  }
}

@container cq-20-b (min-width: 8em) {
  .cq-20__p2b {
    border-style: solid;
    border-color: var(--ok);
    color: var(--ok);
  }
}

@container cq-20-b2 (min-width: 8em) {
  .cq-20__p2f {
    border-style: solid;
    border-color: var(--ok);
    color: var(--ok);
  }

  .cq-20__p2f .cq-20__f {
    display: none;
  }

  .cq-20__p2f .cq-20__p {
    display: inline;
  }
}

@container cq-20-c (min-width: 8em) {
  .cq-20__p3 {
    border-style: solid;
    border-color: var(--ok);
    color: var(--ok);
  }

  .cq-20__p3 .cq-20__f {
    display: none;
  }

  .cq-20__p3 .cq-20__p {
    display: inline;
  }
}

@container cq-20-c2 (min-width: 8em) {
  .cq-20__p3 {
    border-style: solid;
    border-color: var(--ok);
    color: var(--ok);
  }

  .cq-20__p3 .cq-20__f {
    display: none;
  }

  .cq-20__p3 .cq-20__p {
    display: inline;
  }
}

@container (min-width: 14em) {
  .cq-20__p4b {
    border-style: solid;
    border-color: var(--ok);
    color: var(--ok);
  }

  .cq-20__p4b .cq-20__f {
    display: none;
  }

  .cq-20__p4b .cq-20__p {
    display: inline;
  }
}

@container cq-20-d (min-width: 14em) {
  .cq-20__p4f {
    border-style: solid;
    border-color: var(--ok);
    color: var(--ok);
  }

  .cq-20__p4f .cq-20__f {
    display: none;
  }

  .cq-20__p4f .cq-20__p {
    display: inline;
  }
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. The
   pinned values are the demo's own [data-theme] declarations reused
   verbatim, so a toggled demo can never drift from how the same demo
   renders under the site theme. */

.cq-20 {
  position: relative;
}

.cq-20__theme {
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

.cq-20__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-20__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-20__themeopt {
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

.cq-20__themeopt:hover {
  opacity: 0.85;
}

.cq-20__themeinput:checked + .cq-20__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-20__themeinput:focus-visible + .cq-20__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-20:has(#cq-20-theme-light:checked) {
  --bg: #f5f6f8;
  --surf: #ffffff;
  --surf2: #eef0f3;
  --line: #d7dbe1;
  --ink: #12161c;
  --mut: #5a6472;
  --ok: #12805c;
  --bad: #b3261e;
}

.cq-20:has(#cq-20-theme-dark:checked) {
  --bg: #0b0d10;
  --surf: #14171c;
  --surf2: #1b1f26;
  --line: #262c35;
  --ink: #e7ebf0;
  --mut: #8a93a1;
  --ok: #3ecf8e;
  --bad: #ff6a5e;
}
```
