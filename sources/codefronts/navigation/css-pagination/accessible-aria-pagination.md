---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/accessible-aria-pagination/"
title: "Accessible ARIA Pagination"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "The reference implementation to copy when accessibility is the requirement, not an afterthought: a labelled <nav> landmark, an ordered list, aria-labels that…"
has_js: "false"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accessible ARIA Pagination
Source: https://codefronts.com/navigation/css-pagination/accessible-aria-pagination/

The reference implementation to copy when accessibility is the requirement, not an afterthought: a labelled <nav> landmark, an ordered list, aria-labels that read as sentences ("Page 5, current page"), a 2 px :focus-visible ring with offset, a redundant non-color cue on the active page, and a forced-colors block so the state survives Windows high contrast mode.
## HTML
```html
<section class="pgn-09" aria-label="Accessible ARIA Pagination with Focus Rings and aria-current demo">
  <div class="pgn-09__stage">
    <header class="pgn-09__head">
      <p class="pgn-09__eyebrow">WCAG 2.2 AA</p>
      <h2 class="pgn-09__title">Tab into the row — every stop is visible</h2>
      <p class="pgn-09__sub">Semantic nav and ordered list, a real accessible name on every control, aria-current on the active page, and a 2px focus ring with an offset so it never sits on top of the border it needs to contrast against.</p>
    </header>

    <nav class="pgn-09__nav" aria-label="Search results pagination">
      <a class="pgn-09__link pgn-09__link--edge" href="#pgn-09-results" aria-label="Previous page, page 4">
        <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <span>Previous</span>
      </a>
      <ol class="pgn-09__list">
        <li><a class="pgn-09__link" href="#pgn-09-results" aria-label="Page 3">3</a></li>
        <li><a class="pgn-09__link" href="#pgn-09-results" aria-label="Page 4">4</a></li>
        <li><a class="pgn-09__link" href="#pgn-09-results" aria-current="page" aria-label="Page 5, current page">5</a></li>
        <li><a class="pgn-09__link" href="#pgn-09-results" aria-label="Page 6">6</a></li>
        <li><a class="pgn-09__link" href="#pgn-09-results" aria-label="Page 7">7</a></li>
      </ol>
      <a class="pgn-09__link pgn-09__link--edge" href="#pgn-09-results" aria-label="Next page, page 6">
        <span>Next</span>
        <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
    </nav>

    <ul class="pgn-09__checks">
      <li><b>nav[aria-label]</b> distinguishes this landmark from other navs on the page.</li>
      <li><b>ol</b> gives the pages a counted, ordered relationship — not a pile of divs.</li>
      <li><b>aria-current="page"</b> is the state; the fill is only its visual echo.</li>
      <li><b>:focus-visible</b> ring is 2px at 3:1 contrast, with 2px offset.</li>
    </ul>

    <div class="pgn-09__results" id="pgn-09-results" tabindex="-1">Results region — focus lands here after a page change.</div>
  </div>
</section>
```
## CSS
```css
.pgn-09 {
  --bg: #fafafa;
  --surface: #ffffff;
  --surface-2: #f4f4f5;
  --text: #09090b;
  --muted: #71717a;
  --line: #e4e4e7;
  --acc: #1d4ed8;
  --acc-fg: #ffffff;
  --ring: #2563eb;
}

@supports (color: oklch(50% 0 0)) {
  .pgn-09 {
    --bg: oklch(98.4% .002 286);
    --surface: oklch(100% 0 0);
    --surface-2: oklch(96.5% .003 286);
    --text: oklch(17% .006 286);
    --muted: oklch(52% .015 286);
    --line: oklch(92% .004 286);
    --acc: oklch(45% .19 264);
    --acc-fg: oklch(99% 0 0);
    --ring: oklch(52% .21 264);
  }
}

@media (prefers-color-scheme: dark) {
  .pgn-09:not([data-theme="light"]) {
    --bg: #09090b;
    --surface: #131316;
    --surface-2: #1c1c20;
    --text: #fafafa;
    --muted: #a1a1aa;
    --line: #27272a;
    --acc: #60a5fa;
    --acc-fg: #0b1020;
    --ring: #93c5fd;
  }
}

.pgn-09[data-theme="dark"] {
  --bg: #09090b;
  --surface: #131316;
  --surface-2: #1c1c20;
  --text: #fafafa;
  --muted: #a1a1aa;
  --line: #27272a;
  --acc: #60a5fa;
  --acc-fg: #0b1020;
  --ring: #93c5fd;
}

.pgn-09 {
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

.pgn-09,
.pgn-09 *,
.pgn-09 *::before,
.pgn-09 *::after {
  box-sizing: border-box;
}

.pgn-09__stage {
  width: 100%;
  max-width: 46rem;
  display: grid;
  gap: 1.75rem;
}

.pgn-09__eyebrow {
  margin: 0 0 .4rem;
  font-size: .6875rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.pgn-09__title {
  margin: 0 0 .55rem;
  font-size: clamp(1.4rem,3.2vw,1.9rem);
  font-weight: 600;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.pgn-09__sub {
  margin: 0;
  max-width: 38rem;
  font-size: .875rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.pgn-09__nav {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .5rem;
}

.pgn-09__list {
  display: flex;
  gap: .375rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.pgn-09__link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: .4rem;
  min-width: 2.75rem;
  height: 2.75rem;
  padding: 0 .75rem;
  border: 1px solid var(--line);
  border-radius: .625rem;
  background: var(--surface);
  color: var(--text);
  text-decoration: none;
  font-size: .9375rem;
  font-weight: 500;
  font-variant-numeric: tabular-nums;
  transition: background .16s ease, border-color .16s ease;
}

.pgn-09__link:hover {
  background: var(--surface-2);
  border-color: color-mix(in oklab,var(--text) 26%,var(--line));
}

.pgn-09__link:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.pgn-09__link[aria-current="page"] {
  background: var(--acc);
  border-color: transparent;
  color: var(--acc-fg);
  font-weight: 600;
}

.pgn-09__link[aria-current="page"]::after {
  content: "";
  position: absolute;
  inset: auto auto -.45rem 50%;
  translate: -50% 0;
  width: .3rem;
  height: .3rem;
  border-radius: 50%;
  background: var(--acc);
}

.pgn-09__list li {
  position: relative;
}

.pgn-09__link--edge svg {
  width: 1.05rem;
  height: 1.05rem;
  color: var(--muted);
}

.pgn-09__checks {
  display: grid;
  gap: .55rem;
  margin: 0;
  padding: 0;
  list-style: none;
}

.pgn-09__checks li {
  position: relative;
  padding-left: 1.5rem;
  font-size: .8125rem;
  line-height: 1.6;
  color: var(--muted);
}

.pgn-09__checks li::before {
  content: "";
  position: absolute;
  left: 0;
  top: .42em;
  width: .55rem;
  height: .3rem;
  border-left: 2px solid var(--acc);
  border-bottom: 2px solid var(--acc);
  rotate: -45deg;
}

.pgn-09__checks b {
  color: var(--text);
  font-weight: 600;
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size: .75rem;
}

.pgn-09__results {
  padding: 1rem 1.15rem;
  border: 1px dashed var(--line);
  border-radius: .75rem;
  font-size: .8125rem;
  color: var(--muted);
  scroll-margin-block: 2rem;
}

.pgn-09__results:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .pgn-09__link[aria-current="page"] {
    forced-color-adjust: none;
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pgn-09 * {
    animation: none !important;
    transition: none !important;
  }
}
```
