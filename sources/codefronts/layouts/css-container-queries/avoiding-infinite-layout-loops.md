---
source: "codefronts"
url: "https://codefronts.com/layouts/css-container-queries/avoiding-infinite-layout-loops/"
title: "Avoiding Infinite Layout Loops"
section: "layouts"
category: "css-container-queries"
category_name: "CSS Container Queries"
description: "The trap with no media-query equivalent: if a container's size depends on its contents and a query changes those contents' size, the dependency is circular."
has_js: "false"
---

Here's a working CSS Container Querie from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Avoiding Infinite Layout Loops
Source: https://codefronts.com/layouts/css-container-queries/avoiding-infinite-layout-loops/

The trap with no media-query equivalent: if a container's size depends on its contents and a query changes those contents' size, the dependency is circular. That is precisely why container-type: size requires both dimensions to be determined from outside, and why inline-size is the safe default. The demo shows the collapse that results, and the rule that avoids it.
## HTML
```html
<section class="cq-18" aria-labelledby="cq-18-h">
  <fieldset class="cq-18__theme">
    <legend class="cq-18__themelegend">Theme</legend>
    <input class="cq-18__themeinput" type="radio" name="cq-18-theme" id="cq-18-theme-auto" checked>
    <label class="cq-18__themeopt" for="cq-18-theme-auto">Auto</label>
    <input class="cq-18__themeinput" type="radio" name="cq-18-theme" id="cq-18-theme-light">
    <label class="cq-18__themeopt" for="cq-18-theme-light">Light</label>
    <input class="cq-18__themeinput" type="radio" name="cq-18-theme" id="cq-18-theme-dark">
    <label class="cq-18__themeopt" for="cq-18-theme-dark">Dark</label>
  </fieldset>
  <div class="cq-18__stage">
    <header class="cq-18__head">
      <p class="cq-18__kicker">container-type &middot; the loop</p>
      <h2 class="cq-18__h" id="cq-18-h">Why inline-size is the default</h2>
    </header>

    <ol class="cq-18__cycle">
      <li><span class="cq-18__step">1</span>Container measures itself</li>
      <li><span class="cq-18__step">2</span>Query matches on that size</li>
      <li><span class="cq-18__step">3</span>Children change size</li>
      <li><span class="cq-18__step">4</span>Container measures itself again &mdash; loop</li>
    </ol>

    <div class="cq-18__row">
      <section class="cq-18__panel cq-18__panel--bad" aria-label="Size container without a height">
        <p class="cq-18__cap"><span class="cq-18__flag cq-18__flag--bad">collapses</span><code>container-type: size</code> &middot; no height set</p>
        <div class="cq-18__bad">
          <p class="cq-18__fill">Block size resolves as if this container were empty, so it goes to zero and this text spills out of its box.</p>
        </div>
        <p class="cq-18__out">Symptom: a zero-height box. Cause: the block axis had nothing outside the container to size it.</p>
      </section>

      <section class="cq-18__panel cq-18__panel--ok" aria-label="Inline size container">
        <p class="cq-18__cap"><span class="cq-18__flag cq-18__flag--ok">safe</span><code>container-type: inline-size</code></p>
        <div class="cq-18__good">
          <p class="cq-18__fill">The inline axis comes from the parent, the block axis stays intrinsic, and this text sizes the box exactly as it always did.</p>
        </div>
        <p class="cq-18__out">Rule: query the inline axis, let the block axis be intrinsic.</p>
      </section>

      <section class="cq-18__panel cq-18__panel--ok" aria-label="Size container with a height">
        <p class="cq-18__cap"><span class="cq-18__flag cq-18__flag--ok">valid</span><code>container-type: size</code> &middot; height set from outside</p>
        <div class="cq-18__sized">
          <p class="cq-18__fill">With <b>block-size: 7rem</b> declared here, both axes are externally determined and block-axis queries become legitimate.</p>
        </div>
        <p class="cq-18__out">Use <code>size</code> only when you have set the height &mdash; fixed panel, definite grid track, aspect-ratio box.</p>
      </section>
    </div>
  </div>
</section>
```
## CSS
```css
.cq-18,
.cq-18[data-theme="dark"] {
  --bg: #05070a;
  --surf: #0a0f14;
  --line: #16303a;
  --ink: #c8f7e0;
  --mut: #6f9c8b;
  --acc: #35f5a0;
  --bad: #ff5f56;
  --scan: rgba(53, 245, 160, 0.045);
}

.cq-18[data-theme="light"] {
  --bg: #f3f6f4;
  --surf: #ffffff;
  --line: #c3d6cd;
  --ink: #0a1a14;
  --mut: #4c6a5e;
  --acc: #0d7f52;
  --bad: #b3261e;
  --scan: rgba(13, 127, 82, 0.05);
}

@media (prefers-color-scheme: light) {
  .cq-18:not([data-theme="dark"]) {
    --bg: #f3f6f4;
    --surf: #ffffff;
    --line: #c3d6cd;
    --ink: #0a1a14;
    --mut: #4c6a5e;
    --acc: #0d7f52;
    --bad: #b3261e;
    --scan: rgba(13, 127, 82, 0.05);
  }
}

@supports (color: oklch(0.5 0.1 250)) {
  .cq-18,
    .cq-18[data-theme="dark"] {
    --acc: oklch(0.88 0.19 158);
    --bad: oklch(0.68 0.2 25);
  }

  .cq-18[data-theme="light"] {
    --acc: oklch(0.5 0.13 158);
    --bad: oklch(0.5 0.18 28);
  }

  @media (prefers-color-scheme: light) {
    .cq-18:not([data-theme="dark"]) {
      --acc: oklch(0.5 0.13 158);
      --bad: oklch(0.5 0.18 28);
    }
  }
}

.cq-18 {
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  position: relative;
  background: var(--bg);
  color: var(--ink);
  font-family: ui-monospace, "SF Mono", "JetBrains Mono", Menlo, Consolas, monospace;
  line-height: 1.45;
}

.cq-18 *,
.cq-18 *::before,
.cq-18 *::after {
  box-sizing: border-box;
}

.cq-18::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(to bottom, var(--scan) 0 1px, transparent 1px 3px);
}

.cq-18__stage {
  position: relative;
  z-index: 1;
  max-width: 74rem;
  margin-inline: auto;
  padding: clamp(0.9rem, 3vw, 2.25rem);
  display: grid;
  gap: 1rem;
}

.cq-18__kicker {
  margin: 0 0 0.3rem;
  font-size: 0.68rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--mut);
}

.cq-18__h {
  margin: 0;
  font-size: clamp(1.2rem, 1rem + 1.5vw, 1.75rem);
  font-weight: 700;
  letter-spacing: -0.01em;
  color: var(--acc);
}

.cq-18__cycle {
  list-style: none;
  margin: 0;
  padding: 0.65rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1.25rem;
  background: var(--surf);
  border: 1px solid var(--line);
  border-radius: 4px;
  font-size: 0.74rem;
  color: var(--mut);
}

.cq-18__cycle li {
  display: flex;
  align-items: center;
  gap: 0.45rem;
  min-inline-size: 0;
}

.cq-18__cycle li + li::before {
  content: "\2192";
  color: var(--acc);
  margin-inline-end: 0.5rem;
}

.cq-18__step {
  inline-size: 1.25rem;
  block-size: 1.25rem;
  display: grid;
  place-items: center;
  border: 1px solid var(--acc);
  color: var(--acc);
  font-size: 0.66rem;
  font-weight: 700;
}

.cq-18__row {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  align-items: start;
}

.cq-18__panel {
  flex: 1 1 17rem;
  min-inline-size: 0;
  display: grid;
  gap: 0.5rem;
  align-content: start;
}

.cq-18__cap {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  align-items: center;
  font-size: 0.72rem;
  color: var(--mut);
}

.cq-18__cap code {
  color: var(--ink);
}

.cq-18__flag {
  padding: 0.1rem 0.35rem;
  border: 1px solid currentColor;
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.cq-18__flag--bad {
  color: var(--bad);
}

.cq-18__flag--ok {
  color: var(--acc);
}

.cq-18__bad,
.cq-18__good,
.cq-18__sized {
  padding: 0.6rem;
  background: var(--surf);
  border: 1px dashed var(--line);
}

.cq-18__bad {
  container-type: size;
}

.cq-18__good {
  container-type: inline-size;
}

.cq-18__sized {
  container-type: size;
  block-size: 7rem;
  overflow: auto;
}

.cq-18__panel--bad .cq-18__bad {
  border-color: var(--bad);
}

.cq-18__fill {
  margin: 0;
  font-size: 0.76rem;
  color: var(--ink);
}

.cq-18__fill b {
  color: var(--acc);
  font-weight: 700;
}

.cq-18__out {
  margin: 0.9rem 0 0;
  font-size: 0.7rem;
  color: var(--mut);
}

.cq-18__panel--bad .cq-18__out {
  color: var(--bad);
  margin-block-start: 3.75rem;
}

.cq-18__out code {
  color: var(--ink);
}

@container (min-width: 12em) {
  .cq-18__fill {
    letter-spacing: 0.01em;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cq-18::after {
    background: none;
  }
}
/* Theme switch (added 2026-08-25). Pure CSS: three radios + :has(), zero
   JavaScript. Auto inherits both the OS preference and the site's
   [data-theme] stamp; Light and Dark pin the palette and beat both. */

.cq-18 {
  position: relative;
}

.cq-18__theme {
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

.cq-18__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-18__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.cq-18__themeopt {
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

.cq-18__themeopt:hover {
  opacity: 0.85;
}

.cq-18__themeinput:checked + .cq-18__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.cq-18__themeinput:focus-visible + .cq-18__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.cq-18:has(#cq-18-theme-light:checked) {
  --bg: #f3f6f4;
  --surf: #ffffff;
  --line: #c3d6cd;
  --ink: #0a1a14;
  --mut: #4c6a5e;
  --acc: #0d7f52;
  --bad: #b3261e;
  --scan: rgba(13, 127, 82, 0.05);
}

.cq-18:has(#cq-18-theme-dark:checked) {
  --bg: #05070a;
  --surf: #0a0f14;
  --line: #16303a;
  --ink: #c8f7e0;
  --mut: #6f9c8b;
  --acc: #35f5a0;
  --bad: #ff5f56;
  --scan: rgba(53, 245, 160, 0.045);
}
```
