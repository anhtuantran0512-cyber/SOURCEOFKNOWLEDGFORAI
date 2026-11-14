---
source: "codefronts"
url: "https://codefronts.com/motion/css-text-hover-effects/duotone-split-color-split-text/"
title: "Duotone / Split Color Split Text"
section: "motion"
category: "css-text-hover-effects"
category_name: "CSS Text Hover Effects"
description: "Risograph typography in the browser: the headline renders as two full-height clones of itself — red one clipped to the top half, blue one to the bottom —…"
has_js: "false"
---

Here's a working CSS Text Hover Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Duotone / Split Color Split Text
Source: https://codefronts.com/motion/css-text-hover-effects/duotone-split-color-split-text/

Risograph typography in the browser: the headline renders as two full-height clones of itself — red one clipped to the top half, blue one to the bottom — stacked in perfect register via pseudo-elements reading data-text (one string in the DOM, one string for screen readers). Hover knocks the print out of register: the split line slides off 50/50, the halves shear apart horizontally by a few hundredths of an em, and because clip-path inset() interpolates natively, the whole misprint is one smooth transition. The nav links run the same split vertically, left/right.
## HTML
```html
<section class="cth-27" aria-label="Duotone split color text demo">
  <div class="cth-27__stage">
    <div class="cth-27__scene">
      <header class="cth-27__head">
        <p class="cth-27__eyebrow">Riso Press &mdash; open studio night</p>
        <span class="cth-27__chip">two plates &middot; one string &middot; attr(data-text)</span>
      </header>
      <h1 class="cth-27__riso" data-text="BASEMENT TAPES">BASEMENT TAPES</h1>
      <p class="cth-27__vol">VOL. IX &mdash; printed loud, aligned rarely</p>
      <nav class="cth-27__nav" aria-label="Editions">
        <a class="cth-27__split" href="#cth27-top" id="cth27-top" data-text="Prints">Prints</a>
        <a class="cth-27__split" href="#cth27-top" data-text="Zines">Zines</a>
        <a class="cth-27__split" href="#cth27-top" data-text="Posters">Posters</a>
      </nav>
      <p class="cth-27__hint">Hover the headline: the 50/50 split slides to 44/56 and the plates shear apart &mdash; <code>clip-path:inset()</code> interpolating between matching shapes. Links split left/right instead.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.cth-27,
.cth-27 *,
.cth-27 *::before,
.cth-27 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cth-27 {
  --bg: oklch(0.955 0.012 85);
  --ink: oklch(0.24 0.01 60);
  --mut: oklch(0.5 0.02 60);
  --ink-a: oklch(0.58 0.22 28);
  --ink-b: oklch(0.5 0.17 260);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cth-27__stage {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  background: var(--bg);
  padding: clamp(20px,4vw,56px);
  container: cth27/inline-size;
}

.cth-27__scene {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: clamp(16px,3cqi,26px);
  width: min(100%,860px);
}

.cth-27__head {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 14px;
  flex-wrap: wrap;
  padding-bottom: 14px;
  border-bottom: 1.5px solid var(--ink);
}

.cth-27__eyebrow {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--mut);
}

.cth-27__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--mut);
  border: 1px solid oklch(0.85 0.015 70);
  border-radius: 99px;
  padding: 5px 11px;
}

.cth-27__riso {
  position: relative;
  display: inline-block;
  color: var(--ink);
  font-size: clamp(40px,9cqi,96px);
  font-weight: 900;
  letter-spacing: -.02em;
  line-height: 1.05;
  white-space: nowrap;
}

@supports ((background-clip: text) or (-webkit-background-clip: text)) {
  .cth-27__riso {
    color: transparent;
  }
}

.cth-27__riso::selection {
  background: oklch(0.58 0.22 28/.3);
  color: var(--ink);
}

.cth-27__riso::before,
.cth-27__riso::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  pointer-events: none;
  translate: 0 0;
  transition: clip-path .5s cubic-bezier(.25,.8,.25,1),translate .5s cubic-bezier(.25,.8,.25,1);
}

.cth-27__riso::before {
  color: var(--ink-a);
  clip-path: inset(0 0 50% 0);
}

.cth-27__riso::after {
  color: var(--ink-b);
  clip-path: inset(50% 0 0 0);
}

.cth-27__riso:hover::before {
  clip-path: inset(0 0 44% 0);
  translate: -.045em 0;
}

.cth-27__riso:hover::after {
  clip-path: inset(56% 0 0 0);
  translate: .045em 0;
}

.cth-27__vol {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12.5px;
  letter-spacing: .22em;
  color: var(--mut);
}

.cth-27__nav {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: clamp(10px,2.4cqi,20px);
  margin-top: 6px;
}

.cth-27__split {
  position: relative;
  display: grid;
  place-items: center;
  min-height: 50px;
  padding: 0 26px;
  border: 2px solid var(--ink);
  border-radius: 4px;
  text-decoration: none;
  color: transparent;
  font-size: 17px;
  font-weight: 850;
  letter-spacing: .02em;
  background: oklch(0.99 0.004 85);
}

.cth-27__split::before,
.cth-27__split::after {
  content: attr(data-text);
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  transition: clip-path .4s cubic-bezier(.25,.8,.25,1),translate .4s cubic-bezier(.25,.8,.25,1);
}

.cth-27__split::before {
  color: var(--ink-a);
  clip-path: inset(0 50% 0 0);
}

.cth-27__split::after {
  color: var(--ink-b);
  clip-path: inset(0 0 0 50%);
}

.cth-27__split:hover::before,
.cth-27__split:focus-visible::before {
  clip-path: inset(0 44% 0 0);
  translate: 0 -.06em;
}

.cth-27__split:hover::after,
.cth-27__split:focus-visible::after {
  clip-path: inset(0 0 0 56%);
  translate: 0 .06em;
}

.cth-27__split:focus-visible {
  outline: 2.5px solid var(--ink-a);
  outline-offset: 3px;
}

.cth-27__hint {
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
  max-width: 60ch;
}

.cth-27__hint code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.9 0.01 80);
  padding: 1px 6px;
  border-radius: 4px;
}

@container cth27 (width < 560px) {
  .cth-27__riso {
    white-space: normal;
  }

  .cth-27__chip {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cth-27 *,
    .cth-27 *::before,
    .cth-27 *::after {
    transition-duration: .01ms !important;
  }
}
```
