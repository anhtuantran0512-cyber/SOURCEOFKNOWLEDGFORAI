---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/pure-css-pagination-with-target/"
title: "Pure CSS Pagination with :target"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "The pagination every static-site and docs build actually wants: page state lives in the URL fragment, so a reload, a shared link or a back-button press all…"
has_js: "false"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Pagination with :target
Source: https://codefronts.com/navigation/css-pagination/pure-css-pagination-with-target/

The pagination every static-site and docs build actually wants: page state lives in the URL fragment, so a reload, a shared link or a back-button press all land on the right page with zero JavaScript. Four panels, four anchors, and a :target rule doing the switching — plus a :has() fallback that keeps page one visible when nothing is targeted at all.
## HTML
```html
<section class="pgn-01" aria-label="Pure CSS No-JS Pagination (:target selector) demo">
  <div class="pgn-01__stage">
    <header class="pgn-01__head">
      <p class="pgn-01__eyebrow">Changelog</p>
      <h2 class="pgn-01__title">Every release, four at a time</h2>
    </header>

    <div class="pgn-01__panels">
      <section class="pgn-01__panel" id="pgn-01-1" aria-label="Page 1 of 4">
        <article class="pgn-01__row"><h3>Container queries land in the grid system</h3><p>Alex Chen · 14 min read</p></article>
        <article class="pgn-01__row"><h3>Subgrid alignment for nested cards</h3><p>Priya Sharma · 6 min read</p></article>
        <article class="pgn-01__row"><h3>Dropping the last polyfill</h3><p>Jordan Lee · 4 min read</p></article>
      </section>
      <section class="pgn-01__panel" id="pgn-01-2" aria-label="Page 2 of 4">
        <article class="pgn-01__row"><h3>Scroll-driven animations, no observers</h3><p>Sam Rivera · 9 min read</p></article>
        <article class="pgn-01__row"><h3>Anchor positioning for tooltips</h3><p>Alex Chen · 7 min read</p></article>
        <article class="pgn-01__row"><h3>Rewriting focus management</h3><p>Priya Sharma · 11 min read</p></article>
      </section>
      <section class="pgn-01__panel" id="pgn-01-3" aria-label="Page 3 of 4">
        <article class="pgn-01__row"><h3>Why we moved to oklch</h3><p>Jordan Lee · 5 min read</p></article>
        <article class="pgn-01__row"><h3>Popover API in production</h3><p>Sam Rivera · 8 min read</p></article>
        <article class="pgn-01__row"><h3>Cutting 40kb of layout JavaScript</h3><p>Alex Chen · 12 min read</p></article>
      </section>
      <section class="pgn-01__panel" id="pgn-01-4" aria-label="Page 4 of 4">
        <article class="pgn-01__row"><h3>View transitions between routes</h3><p>Priya Sharma · 10 min read</p></article>
        <article class="pgn-01__row"><h3>A budget for third-party scripts</h3><p>Jordan Lee · 6 min read</p></article>
        <article class="pgn-01__row"><h3>Testing with prefers-reduced-motion</h3><p>Sam Rivera · 3 min read</p></article>
      </section>
    </div>

    <nav class="pgn-01__nav" aria-label="Pagination">
      <ol class="pgn-01__list">
        <li><a class="pgn-01__link" href="#pgn-01-1">1</a></li>
        <li><a class="pgn-01__link" href="#pgn-01-2">2</a></li>
        <li><a class="pgn-01__link" href="#pgn-01-3">3</a></li>
        <li><a class="pgn-01__link" href="#pgn-01-4">4</a></li>
      </ol>
      <p class="pgn-01__hint">State lives in the URL fragment — reload keeps your page.</p>
    </nav>
  </div>
</section>
```
## CSS
```css
.pgn-01 {
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
  .pgn-01 {
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
  .pgn-01:not([data-theme="light"]) {
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

.pgn-01[data-theme="dark"] {
  --bg: #09090b;
  --surface: #131316;
  --text: #fafafa;
  --muted: #a1a1aa;
  --line: #27272a;
  --acc: #fafafa;
  --acc-fg: #09090b;
  --ring: #818cf8;
}

.pgn-01 {
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

.pgn-01,
.pgn-01 *,
.pgn-01 *::before,
.pgn-01 *::after {
  box-sizing: border-box;
}

.pgn-01__stage {
  width: 100%;
  max-width: 44rem;
  display: grid;
  gap: 2rem;
}

.pgn-01__head {
  display: grid;
  gap: .4rem;
}

.pgn-01__eyebrow {
  margin: 0;
  font-size: .6875rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.pgn-01__title {
  margin: 0;
  font-size: clamp(1.5rem,3.4vw,2rem);
  font-weight: 600;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.pgn-01__panels {
  display: grid;
}

.pgn-01__panel {
  display: none;
  grid-area: 1/1;
  gap: 0;
  scroll-margin-block: 4rem;
}

.pgn-01__panel:target {
  display: grid;
  animation: pgn-01-in .28s cubic-bezier(.16,1,.3,1);
}

.pgn-01:not(:has(.pgn-01__panel:target)) #pgn-01-1 {
  display: grid;
}

@keyframes pgn-01-in {
  from {
    opacity: 0;
    translate: 0 .5rem;
  }
}

.pgn-01__row {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  justify-content: space-between;
  gap: .5rem 1rem;
  padding: 1.15rem 1.25rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: .75rem;
  margin-bottom: .5rem;
}

.pgn-01__row h3 {
  margin: 0;
  font-size: .9375rem;
  font-weight: 550;
  letter-spacing: -.01em;
}

.pgn-01__row p {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pgn-01__nav {
  display: grid;
  gap: .75rem;
  justify-items: center;
}

.pgn-01__list {
  display: flex;
  gap: .375rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.pgn-01__link {
  display: grid;
  place-items: center;
  min-width: 2.75rem;
  height: 2.75rem;
  padding: 0 .5rem;
  border: 1px solid var(--line);
  border-radius: .625rem;
  background: var(--surface);
  color: var(--text);
  text-decoration: none;
  font-size: .9375rem;
  font-variant-numeric: tabular-nums;
  transition: background .16s ease, border-color .16s ease, color .16s ease;
}

.pgn-01__link:hover {
  border-color: color-mix(in oklab,var(--text) 28%,var(--line));
}

.pgn-01__link:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.pgn-01:has(#pgn-01-1:target) [href="#pgn-01-1"],
.pgn-01:has(#pgn-01-2:target) [href="#pgn-01-2"],
.pgn-01:has(#pgn-01-3:target) [href="#pgn-01-3"],
.pgn-01:has(#pgn-01-4:target) [href="#pgn-01-4"],
.pgn-01:not(:has(.pgn-01__panel:target)) [href="#pgn-01-1"] {
  background: var(--acc);
  border-color: transparent;
  color: var(--acc-fg);
}

.pgn-01__hint {
  margin: 0;
  font-size: .75rem;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .pgn-01 * {
    animation: none !important;
    transition: none !important;
  }
}
```
