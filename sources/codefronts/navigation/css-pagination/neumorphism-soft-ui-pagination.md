---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/neumorphism-soft-ui-pagination/"
title: "Neumorphism Soft UI Pagination"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "Soft UI done with the contrast problem actually solved: extruded keys from a dual shadow pair, an inset press state for the active page, and a real accent…"
has_js: "false"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphism Soft UI Pagination
Source: https://codefronts.com/navigation/css-pagination/neumorphism-soft-ui-pagination/

Soft UI done with the contrast problem actually solved: extruded keys from a dual shadow pair, an inset press state for the active page, and a real accent colour plus weight change on the current item — because a shadow-only affordance sits near 1.5:1 and fails WCAG on its own. Includes a forced-colors block that restores visible borders.
## HTML
```html
<section class="pgn-20" aria-label="Neumorphism Pagination with Soft-UI Dual Shadows demo">
  <div class="pgn-20__stage">
    <header class="pgn-20__head">
      <p class="pgn-20__eyebrow">Soft UI</p>
      <h2 class="pgn-20__title">Extruded, then pressed</h2>
      <p class="pgn-20__sub">One light source, top-left. Raised keys cast a dark shadow down-right and a light one up-left; the active key inverts both to sit inside the surface.</p>
    </header>

    <nav class="pgn-20__nav" aria-label="Pagination">
      <button class="pgn-20__key" type="button" aria-label="Previous page">
        <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <ol class="pgn-20__list">
        <li><button class="pgn-20__key" type="button">1</button></li>
        <li><button class="pgn-20__key" type="button">2</button></li>
        <li><button class="pgn-20__key pgn-20__key--on" type="button" aria-current="page">3</button></li>
        <li><button class="pgn-20__key" type="button">4</button></li>
        <li><button class="pgn-20__key" type="button">5</button></li>
      </ol>
      <button class="pgn-20__key" type="button" aria-label="Next page">
        <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
    </nav>

    <p class="pgn-20__caption">Page 3 of 5 · 74 items</p>
  </div>
</section>
```
## CSS
```css
.pgn-20 {
  --bg: #e8ecf2;
  --text: #2c3444;
  --muted: #7a8497;
  --acc: #3b5bdb;
  --light: #ffffff;
  --dark: #c3cbd8;
  --ring: #3b5bdb;
  --d: .55rem;
  --blur: 1.1rem;
}

@supports (color: oklch(50% 0 0)) {
  .pgn-20 {
    --bg: oklch(93.5% .012 250);
    --text: oklch(35% .03 260);
    --muted: oklch(60% .025 258);
    --acc: oklch(52% .17 265);
    --light: oklch(100% 0 0);
    --dark: oklch(84% .018 250);
    --ring: oklch(52% .17 265);
  }
}

@media (prefers-color-scheme: dark) {
  .pgn-20:not([data-theme="light"]) {
    --bg: #252a33;
    --text: #dfe4ec;
    --muted: #98a2b3;
    --acc: #8ea2ff;
    --light: #2f3540;
    --dark: #1b1f26;
    --ring: #8ea2ff;
  }
}

.pgn-20[data-theme="dark"] {
  --bg: #252a33;
  --text: #dfe4ec;
  --muted: #98a2b3;
  --acc: #8ea2ff;
  --light: #2f3540;
  --dark: #1b1f26;
  --ring: #8ea2ff;
}

.pgn-20 {
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

.pgn-20,
.pgn-20 *,
.pgn-20 *::before,
.pgn-20 *::after {
  box-sizing: border-box;
}

.pgn-20__stage {
  width: 100%;
  max-width: 42rem;
  display: grid;
  gap: 2.25rem;
  justify-items: center;
  text-align: center;
}

.pgn-20__eyebrow {
  margin: 0 0 .45rem;
  font-size: .6875rem;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--muted);
}

.pgn-20__title {
  margin: 0 0 .6rem;
  font-size: clamp(1.4rem,3.4vw,2rem);
  font-weight: 600;
  letter-spacing: -.025em;
  color: var(--text);
}

.pgn-20__sub {
  margin: 0;
  max-width: 32rem;
  font-size: .875rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.pgn-20__nav {
  display: flex;
  align-items: center;
  gap: .75rem;
  padding: .9rem 1rem;
  border-radius: 1.5rem;
  background: var(--bg);
  box-shadow: var(--d) var(--d) calc(var(--blur) * 1.6) var(--dark), calc(var(--d) * -1) calc(var(--d) * -1) calc(var(--blur) * 1.6) var(--light);
}

.pgn-20__list {
  display: flex;
  gap: .6rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.pgn-20__key {
  display: grid;
  place-items: center;
  min-width: 3rem;
  height: 3rem;
  padding: 0 .5rem;
  border: 0;
  border-radius: .9rem;
  background: var(--bg);
  color: var(--text);
  font: inherit;
  font-size: .9375rem;
  font-weight: 500;
  font-variant-numeric: tabular-nums;
  cursor: pointer;
  box-shadow: calc(var(--d) * .55) calc(var(--d) * .55) var(--blur) var(--dark), calc(var(--d) * -.55) calc(var(--d) * -.55) var(--blur) var(--light);
  transition: box-shadow .22s ease, color .22s ease, translate .22s ease;
}

.pgn-20__key svg {
  width: 1.1rem;
  height: 1.1rem;
}

.pgn-20__key:hover {
  color: var(--acc);
  translate: 0 -1px;
}

.pgn-20__key:active,
.pgn-20__key--on {
  color: var(--acc);
  translate: 0 0;
  box-shadow: inset calc(var(--d) * .5) calc(var(--d) * .5) calc(var(--blur) * .8) var(--dark), inset calc(var(--d) * -.5) calc(var(--d) * -.5) calc(var(--blur) * .8) var(--light);
}

.pgn-20__key--on {
  font-weight: 700;
}

.pgn-20__key:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.pgn-20__caption {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

@media (forced-colors: active) {
  .pgn-20__key {
    border: 1px solid CanvasText;
  }

  .pgn-20__key--on {
    forced-color-adjust: none;
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pgn-20 * {
    animation: none !important;
    transition: none !important;
  }
}
```
