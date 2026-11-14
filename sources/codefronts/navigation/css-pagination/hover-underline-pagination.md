---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/hover-underline-pagination/"
title: "Hover Underline Pagination"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "A dark, typographic pagination row where the interaction is the design: a rule wipes in from the left, the digit lifts and grows a fraction, and both effects…"
has_js: "false"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Hover Underline Pagination
Source: https://codefronts.com/navigation/css-pagination/hover-underline-pagination/

A dark, typographic pagination row where the interaction is the design: a rule wipes in from the left, the digit lifts and grows a fraction, and both effects run on :hover and :focus-visible so a keyboard user gets identical feedback. Nothing animated touches layout.
## HTML
```html
<section class="pgn-15" aria-label="Hover Underline / Scale Animation Pagination demo">
  <div class="pgn-15__stage">
    <header class="pgn-15__head">
      <p class="pgn-15__eyebrow">Micro-interaction</p>
      <h2 class="pgn-15__title">Hover the numbers</h2>
      <p class="pgn-15__sub">A rule wipes in from the left and out to the right, the digit lifts a fraction, and the whole thing is two transitions on transform-adjacent properties — nothing that touches layout.</p>
    </header>

    <nav class="pgn-15__nav" aria-label="Pagination">
      <button class="pgn-15__ghost" type="button" aria-label="Previous page">Prev</button>
      <ol class="pgn-15__list">
        <li><button class="pgn-15__num" type="button"><span>1</span></button></li>
        <li><button class="pgn-15__num" type="button"><span>2</span></button></li>
        <li><button class="pgn-15__num" type="button"><span>3</span></button></li>
        <li><button class="pgn-15__num" type="button" aria-current="page"><span>4</span></button></li>
        <li><button class="pgn-15__num" type="button"><span>5</span></button></li>
        <li><button class="pgn-15__num" type="button"><span>6</span></button></li>
      </ol>
      <button class="pgn-15__ghost" type="button" aria-label="Next page">Next</button>
    </nav>
  </div>
</section>
```
## CSS
```css
.pgn-15 {
  --bg: #0b0b0d;
  --surface: #141417;
  --text: #f4f4f5;
  --muted: #8b8b93;
  --line: #26262b;
  --acc: #f4f4f5;
  --ring: #a5b4fc;
}

@supports (color: oklch(50% 0 0)) {
  .pgn-15 {
    --bg: oklch(13% .004 286);
    --surface: oklch(17% .005 286);
    --text: oklch(96% .002 286);
    --muted: oklch(63% .012 286);
    --line: oklch(27% .008 286);
    --acc: oklch(96% .002 286);
    --ring: oklch(78% .12 277);
  }
}

@media (prefers-color-scheme: light) {
  .pgn-15:not([data-theme="dark"]) {
    --bg: #fafafa;
    --surface: #ffffff;
    --text: #09090b;
    --muted: #71717a;
    --line: #e4e4e7;
    --acc: #09090b;
    --ring: #4f46e5;
  }
}

.pgn-15[data-theme="light"] {
  --bg: #fafafa;
  --surface: #ffffff;
  --text: #09090b;
  --muted: #71717a;
  --line: #e4e4e7;
  --acc: #09090b;
  --ring: #4f46e5;
}

.pgn-15 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,5vw,4rem);
  background: var(--bg);
  color: var(--text);
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  -webkit-font-smoothing: antialiased;
}

.pgn-15,
.pgn-15 *,
.pgn-15 *::before,
.pgn-15 *::after {
  box-sizing: border-box;
}

.pgn-15__stage {
  width: 100%;
  max-width: 44rem;
  display: grid;
  gap: 2.5rem;
  justify-items: center;
  text-align: center;
}

.pgn-15__eyebrow {
  margin: 0 0 .4rem;
  font-size: .6875rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.pgn-15__title {
  margin: 0 0 .55rem;
  font-size: clamp(1.4rem,3.2vw,1.9rem);
  font-weight: 600;
  letter-spacing: -.025em;
}

.pgn-15__sub {
  margin: 0;
  max-width: 32rem;
  font-size: .875rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.pgn-15__nav {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  justify-content: center;
  gap: .75rem;
}

.pgn-15__list {
  display: flex;
  gap: .35rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.pgn-15__num {
  position: relative;
  display: grid;
  place-items: center;
  min-width: 2.75rem;
  height: 2.75rem;
  padding: 0 .35rem;
  border: 0;
  background: transparent;
  color: var(--muted);
  font: inherit;
  font-size: 1.0625rem;
  font-variant-numeric: tabular-nums;
  cursor: pointer;
  transition: color .22s ease;
}

.pgn-15__num span {
  display: block;
  transition: translate .28s cubic-bezier(.16,1,.3,1), scale .28s cubic-bezier(.16,1,.3,1);
}

.pgn-15__num::after {
  content: "";
  position: absolute;
  left: .35rem;
  right: .35rem;
  bottom: .45rem;
  height: 1.5px;
  background: currentColor;
  scale: 0 1;
  transform-origin: left center;
  transition: scale .28s cubic-bezier(.16,1,.3,1);
}

.pgn-15__num:hover,
.pgn-15__num:focus-visible {
  color: var(--acc);
}

.pgn-15__num:hover span,
.pgn-15__num:focus-visible span {
  translate: 0 -2px;
  scale: 1.12;
}

.pgn-15__num:hover::after,
.pgn-15__num:focus-visible::after {
  scale: 1 1;
}

.pgn-15__num:not(:hover)::after {
  transform-origin: right center;
}

.pgn-15__num:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
  border-radius: .4rem;
}

.pgn-15__num[aria-current="page"] {
  color: var(--acc);
  font-weight: 600;
}

.pgn-15__num[aria-current="page"]::after {
  scale: 1 1;
  transform-origin: left center;
}

.pgn-15__ghost {
  height: 2.75rem;
  padding: 0 1rem;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: transparent;
  color: var(--muted);
  font: inherit;
  font-size: .875rem;
  cursor: pointer;
  transition: color .2s ease, border-color .2s ease, background .2s ease;
}

.pgn-15__ghost:hover {
  color: var(--text);
  border-color: color-mix(in oklab,var(--text) 40%,var(--line));
  background: var(--surface);
}

.pgn-15__ghost:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .pgn-15 * {
    animation: none !important;
    transition: none !important;
  }

  .pgn-15__num:hover::after {
    scale: 1 1;
  }
}
```
