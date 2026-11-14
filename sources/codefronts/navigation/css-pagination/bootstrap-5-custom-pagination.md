---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/bootstrap-5-custom-pagination/"
title: "Bootstrap 5 Custom Pagination"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "Bootstrap 5.3 exposes pagination through --bs-pagination-* custom properties, so restyling it no longer means a specificity war or a Sass rebuild. This keeps…"
has_js: "false"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Bootstrap 5 Custom Pagination
Source: https://codefronts.com/navigation/css-pagination/bootstrap-5-custom-pagination/

Bootstrap 5.3 exposes pagination through --bs-pagination-* custom properties, so restyling it no longer means a specificity war or a Sass rebuild. This keeps the canonical .pagination / .page-item / .page-link structure and its .active and .disabled states, and rewrites only the variables — neutral surface, softer radius, a near-black active fill instead of the default blue.
## HTML
```html
<section class="pgn-08" aria-label="Bootstrap 5 Custom Pagination demo">
  <div class="pgn-08__stage">
    <header class="pgn-08__head">
      <p class="pgn-08__eyebrow">Bootstrap 5 markup · restyled</p>
      <h2 class="pgn-08__title">.pagination without the Bootstrap blue</h2>
      <p class="pgn-08__sub">Standard Bootstrap class names and structure, overridden through the component's own CSS variables. Nothing is loaded from a CDN — the base rules ship in this stylesheet.</p>
    </header>

    <nav aria-label="Pagination">
      <ul class="pagination pagination-lg">
        <li class="page-item disabled"><span class="page-link" aria-disabled="true">Previous</span></li>
        <li class="page-item"><button class="page-link" type="button">1</button></li>
        <li class="page-item active" aria-current="page"><button class="page-link" type="button">2</button></li>
        <li class="page-item"><button class="page-link" type="button">3</button></li>
        <li class="page-item"><button class="page-link" type="button">4</button></li>
        <li class="page-item"><button class="page-link" type="button">Next</button></li>
      </ul>
    </nav>

    <p class="pgn-08__note">Override surface: <code>--bs-pagination-color</code>, <code>--bs-pagination-active-bg</code>, <code>--bs-pagination-border-radius</code>, <code>--bs-pagination-focus-box-shadow</code>.</p>
  </div>
</section>
```
## CSS
```css
.pgn-08 {
  --bg: #fafafa;
  --surface: #ffffff;
  --surface-2: #f4f4f5;
  --text: #09090b;
  --muted: #71717a;
  --line: #e4e4e7;
  --acc: #111827;
  --acc-fg: #ffffff;
  --ring: #6366f1;
  /* Bootstrap component variables, overridden */
  --bs-pagination-padding-x: 1rem;
  --bs-pagination-padding-y: .6rem;
  --bs-pagination-font-size: 1rem;
  --bs-pagination-color: var(--text);
  --bs-pagination-bg: var(--surface);
  --bs-pagination-border-width: 1px;
  --bs-pagination-border-color: var(--line);
  --bs-pagination-border-radius: .625rem;
  --bs-pagination-hover-bg: var(--surface-2);
  --bs-pagination-hover-color: var(--text);
  --bs-pagination-focus-box-shadow: 0 0 0 3px color-mix(in oklab,var(--ring) 40%,transparent);
  --bs-pagination-active-bg: var(--acc);
  --bs-pagination-active-color: var(--acc-fg);
  --bs-pagination-disabled-color: var(--muted);
  --bs-pagination-disabled-bg: transparent;
}

@supports (color: oklch(50% 0 0)) {
  .pgn-08 {
    --bg: oklch(98.4% .002 286);
    --surface: oklch(100% 0 0);
    --surface-2: oklch(96.5% .003 286);
    --text: oklch(17% .006 286);
    --muted: oklch(55% .015 286);
    --line: oklch(92% .004 286);
    --acc: oklch(22% .008 286);
    --acc-fg: oklch(99% 0 0);
    --ring: oklch(62% .19 277);
  }
}

@media (prefers-color-scheme: dark) {
  .pgn-08:not([data-theme="light"]) {
    --bg: #09090b;
    --surface: #131316;
    --surface-2: #1c1c20;
    --text: #fafafa;
    --muted: #a1a1aa;
    --line: #27272a;
    --acc: #fafafa;
    --acc-fg: #09090b;
    --ring: #818cf8;
  }
}

.pgn-08[data-theme="dark"] {
  --bg: #09090b;
  --surface: #131316;
  --surface-2: #1c1c20;
  --text: #fafafa;
  --muted: #a1a1aa;
  --line: #27272a;
  --acc: #fafafa;
  --acc-fg: #09090b;
  --ring: #818cf8;
}

.pgn-08 {
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

.pgn-08,
.pgn-08 *,
.pgn-08 *::before,
.pgn-08 *::after {
  box-sizing: border-box;
}

.pgn-08__stage {
  width: 100%;
  max-width: 46rem;
  display: grid;
  gap: 1.75rem;
  justify-items: start;
}

.pgn-08__eyebrow {
  margin: 0 0 .4rem;
  font-size: .6875rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.pgn-08__title {
  margin: 0 0 .55rem;
  font-size: clamp(1.4rem,3.2vw,1.9rem);
  font-weight: 600;
  letter-spacing: -.025em;
}

.pgn-08__sub {
  margin: 0;
  max-width: 36rem;
  font-size: .875rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.pgn-08__note {
  margin: 0;
  font-size: .75rem;
  line-height: 1.9;
  color: var(--muted);
}

.pgn-08 code {
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size: .6875rem;
  background: var(--surface-2);
  padding: .15rem .35rem;
  border-radius: .25rem;
}
/* Bootstrap 5 base, reproduced locally so no CDN is required */

.pgn-08 .pagination {
  display: flex;
  flex-wrap: wrap;
  gap: .375rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.pgn-08 .page-item {
  display: block;
}

.pgn-08 .page-link {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 2.75rem;
  min-height: 2.75rem;
  padding: var(--bs-pagination-padding-y) var(--bs-pagination-padding-x);
  font-family: inherit;
  font-size: var(--bs-pagination-font-size);
  font-weight: 500;
  font-variant-numeric: tabular-nums;
  line-height: 1;
  color: var(--bs-pagination-color);
  background: var(--bs-pagination-bg);
  border: var(--bs-pagination-border-width) solid var(--bs-pagination-border-color);
  border-radius: var(--bs-pagination-border-radius);
  text-decoration: none;
  cursor: pointer;
  transition: color .15s ease-in-out, background-color .15s ease-in-out, border-color .15s ease-in-out, box-shadow .15s ease-in-out;
}

.pgn-08 .pagination-lg .page-link {
  --bs-pagination-font-size: 1.125rem;
  --bs-pagination-padding-x: 1.15rem;
}

.pgn-08 .page-link:hover {
  color: var(--bs-pagination-hover-color);
  background: var(--bs-pagination-hover-bg);
  border-color: color-mix(in oklab,var(--text) 24%,var(--line));
}

.pgn-08 .page-link:focus-visible {
  outline: 0;
  box-shadow: var(--bs-pagination-focus-box-shadow);
  z-index: 1;
}

.pgn-08 .page-item.active .page-link {
  color: var(--bs-pagination-active-color);
  background: var(--bs-pagination-active-bg);
  border-color: transparent;
}

.pgn-08 .page-item.disabled .page-link {
  color: var(--bs-pagination-disabled-color);
  background: var(--bs-pagination-disabled-bg);
  pointer-events: none;
  opacity: .65;
}

@media (prefers-reduced-motion: reduce) {
  .pgn-08 * {
    animation: none !important;
    transition: none !important;
  }
}
```
