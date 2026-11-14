---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/responsive-compact-pagination/"
title: "Responsive Compact Pagination"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "One markup, two layouts, no viewport media query: a full number row on wide containers that collapses to Previous · Page 3 of 12 · Next when its own wrapper…"
has_js: "false"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Compact Pagination
Source: https://codefronts.com/navigation/css-pagination/responsive-compact-pagination/

One markup, two layouts, no viewport media query: a full number row on wide containers that collapses to Previous · Page 3 of 12 · Next when its own wrapper gets narrow. Because it queries the container and not the screen, the same component behaves correctly in a sidebar, a modal and a full-width page — drag the demo's resize handle to watch it switch.
## HTML
```html
<section class="pgn-03" aria-label="Responsive Pagination (Full Numbers → Compact Prev/Page X of N/Next) demo">
  <div class="pgn-03__stage">
    <header class="pgn-03__head">
      <p class="pgn-03__eyebrow">Container query · drag the handle</p>
      <h2 class="pgn-03__title">One markup, two layouts</h2>
      <p class="pgn-03__sub">Resize the frame from its bottom-right corner. Under 30rem the number list is replaced by a compact readout — no media query, no JavaScript.</p>
    </header>

    <div class="pgn-03__frame">
      <nav class="pgn-03__nav" aria-label="Pagination">
        <button class="pgn-03__edge" type="button" aria-label="Previous page">
          <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M12.5 4.5 7 10l5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <span class="pgn-03__edgetext">Previous</span>
        </button>

        <ol class="pgn-03__list">
          <li><button class="pgn-03__num" type="button">1</button></li>
          <li><button class="pgn-03__num" type="button">2</button></li>
          <li><button class="pgn-03__num" type="button" aria-current="page">3</button></li>
          <li><button class="pgn-03__num" type="button">4</button></li>
          <li><button class="pgn-03__num" type="button">5</button></li>
          <li><button class="pgn-03__num" type="button">6</button></li>
        </ol>

        <p class="pgn-03__compact" hidden>Page <b>3</b> of <b>12</b></p>

        <button class="pgn-03__edge" type="button" aria-label="Next page">
          <span class="pgn-03__edgetext">Next</span>
          <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M7.5 4.5 13 10l-5.5 5.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
      </nav>
    </div>
  </div>
</section>
```
## CSS
```css
.pgn-03 {
  --bg: #fafafa;
  --surface: #ffffff;
  --text: #09090b;
  --muted: #71717a;
  --line: #e4e4e7;
  --acc: #18181b;
  --acc-fg: #ffffff;
  --ring: #6366f1;
}

@supports (color: oklch(50% 0 0)) {
  .pgn-03 {
    --bg: oklch(98.4% .002 286);
    --surface: oklch(100% 0 0);
    --text: oklch(17% .006 286);
    --muted: oklch(55% .015 286);
    --line: oklch(92% .004 286);
    --acc: oklch(22% .008 286);
    --acc-fg: oklch(99% 0 0);
    --ring: oklch(62% .19 277);
  }
}

@media (prefers-color-scheme: dark) {
  .pgn-03:not([data-theme="light"]) {
    --bg: #09090b;
    --surface: #131316;
    --text: #fafafa;
    --muted: #a1a1aa;
    --line: #27272a;
    --acc: #fafafa;
    --acc-fg: #09090b;
    --ring: #818cf8;
  }
}

.pgn-03[data-theme="dark"] {
  --bg: #09090b;
  --surface: #131316;
  --text: #fafafa;
  --muted: #a1a1aa;
  --line: #27272a;
  --acc: #fafafa;
  --acc-fg: #09090b;
  --ring: #818cf8;
}

.pgn-03 {
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

.pgn-03,
.pgn-03 *,
.pgn-03 *::before,
.pgn-03 *::after {
  box-sizing: border-box;
}

.pgn-03__stage {
  width: 100%;
  max-width: 48rem;
  display: grid;
  gap: 1.75rem;
}

.pgn-03__eyebrow {
  margin: 0 0 .4rem;
  font-size: .6875rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.pgn-03__title {
  margin: 0 0 .55rem;
  font-size: clamp(1.4rem,3.2vw,1.9rem);
  font-weight: 600;
  letter-spacing: -.025em;
}

.pgn-03__sub {
  margin: 0;
  max-width: 34rem;
  font-size: .875rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.pgn-03__frame {
  container-type: inline-size;
  resize: horizontal;
  overflow: auto;
  width: 100%;
  min-width: 17rem;
  max-width: 100%;
  padding: 1.25rem;
  border: 1px dashed var(--line);
  border-radius: 1rem;
}

.pgn-03__nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .5rem;
}

.pgn-03__list {
  display: flex;
  gap: .25rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.pgn-03__compact {
  margin: 0;
  font-size: .9375rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pgn-03__compact b {
  color: var(--text);
  font-weight: 600;
}

.pgn-03 [hidden] {
  display: none !important;
}

.pgn-03__num,
.pgn-03__edge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: .4rem;
  min-width: 2.75rem;
  height: 2.75rem;
  padding: 0 .85rem;
  border: 1px solid var(--line);
  border-radius: .625rem;
  background: var(--surface);
  color: var(--text);
  font: inherit;
  font-size: .9375rem;
  font-variant-numeric: tabular-nums;
  cursor: pointer;
  transition: background .16s ease, border-color .16s ease;
}

.pgn-03__num {
  padding: 0 .5rem;
}

.pgn-03__num:hover,
.pgn-03__edge:hover {
  border-color: color-mix(in oklab,var(--text) 28%,var(--line));
}

.pgn-03__num:focus-visible,
.pgn-03__edge:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.pgn-03__num[aria-current="page"] {
  background: var(--acc);
  border-color: transparent;
  color: var(--acc-fg);
}

.pgn-03__edge svg {
  width: 1.125rem;
  height: 1.125rem;
  color: var(--muted);
}

@container (max-width: 30rem) {
  .pgn-03__list {
    display: none;
  }

  .pgn-03__compact[hidden] {
    display: block !important;
  }

  .pgn-03__edgetext {
    position: absolute;
    width: 1px;
    height: 1px;
    overflow: hidden;
    clip-path: inset(50%);
  }

  .pgn-03__edge {
    padding: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pgn-03 * {
    animation: none !important;
    transition: none !important;
  }
}
```
