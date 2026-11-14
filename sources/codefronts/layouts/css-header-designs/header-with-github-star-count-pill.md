---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/header-with-github-star-count-pill/"
title: "Header with GitHub Star Count Pill"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "The header every open-source project ships: wordmark, a short docs nav, and a star-count pill that links to the repository."
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Header with GitHub Star Count Pill
Source: https://codefronts.com/layouts/css-header-designs/header-with-github-star-count-pill/

The header every open-source project ships: wordmark, a short docs nav, and a star-count pill that links to the repository. The pill is outlined at rest and fills with GitHub black on :hover and :focus-visible, the count is set in tabular figures so it never nudges the layout, and the whole design is monochrome with a hard offset shadow instead of a soft one.
## HTML
```html
<div class="hd-11">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;800&display=swap">
  <a class="hd-11__skip" href="#hd-11-main">Skip to content</a>

  <header class="hd-11__bar">
    <a class="hd-11__brand" href="#hd-11-main">
      <svg class="hd-11__mark" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false">
        <path d="M4 19V5l8 7 8-7v14" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <span class="hd-11__word">stackless<span>/ui</span></span>
    </a>

    <nav class="hd-11__nav" aria-label="Main">
      <ul>
        <li><a href="#hd-11-main" aria-current="page">Docs</a></li>
        <li><a href="#hd-11-main">Components</a></li>
        <li><a href="#hd-11-main">Themes</a></li>
        <li><a href="#hd-11-main">Blog</a></li>
      </ul>
    </nav>

    <div class="hd-11__right">
      <input class="hd-11__sr" type="checkbox" id="hd-11-dark">
      <label class="hd-11__theme" for="hd-11-dark">
        <svg class="hd-11__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <svg class="hd-11__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <span class="hd-11__vh">Switch light or dark theme</span>
      </label>
      <a class="hd-11__quiet" href="#hd-11-main">Changelog</a>
      <a class="hd-11__star" href="#hd-11-main" aria-label="Star stackless/ui on GitHub, 12.4 thousand stars">
        <svg class="hd-11__gh" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M12 2a10 10 0 0 0-3.16 19.49c.5.09.68-.22.68-.48v-1.7c-2.78.6-3.37-1.34-3.37-1.34-.45-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.89 1.53 2.34 1.09 2.91.83.09-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.94 0-1.09.39-1.98 1.03-2.68-.1-.25-.45-1.27.1-2.65 0 0 .83-.27 2.73 1.02a9.4 9.4 0 0 1 4.98 0c1.9-1.29 2.73-1.02 2.73-1.02.55 1.38.2 2.4.1 2.65.64.7 1.03 1.59 1.03 2.68 0 3.84-2.34 4.68-4.57 4.93.36.31.68.92.68 1.85v2.74c0 .27.18.58.69.48A10 10 0 0 0 12 2Z"/></svg>
        <svg class="hd-11__starico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="m12 3.6 2.6 5.5 6 .8-4.4 4.2 1.1 6-5.3-2.9-5.3 2.9 1.1-6L3.4 9.9l6-.8L12 3.6Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
        <span class="hd-11__count">12.4k</span>
      </a>
    </div>
  </header>

  <main class="hd-11__main" id="hd-11-main">
    <p class="hd-11__eyebrow">v4.2.0 &middot; MIT-free, copy the source</p>
    <h1>Primitives that render before your JavaScript does.</h1>
    <p class="hd-11__lead">Forty-one components, no runtime, no theme provider. Hover the star pill in the header &mdash; it fills with GitHub black and compresses its shadow on press.</p>

    <pre class="hd-11__pre"><code>$ npx stackless add header
&#8250; fetching header.css        1.9 kB
&#8250; fetching header.html       0.8 kB
&#8250; done in 240ms</code></pre>

    <ul class="hd-11__list">
      <li><span class="hd-11__num">01</span><span class="hd-11__li-t">Header</span><span class="hd-11__li-d">Composed bar with nav, utility slot and sticky behaviour</span></li>
      <li><span class="hd-11__num">02</span><span class="hd-11__li-t">Command menu</span><span class="hd-11__li-d">Dialog-based palette, no focus-trap dependency</span></li>
      <li><span class="hd-11__num">03</span><span class="hd-11__li-t">Data table</span><span class="hd-11__li-d">Sticky head, tabular figures, keyboard row selection</span></li>
      <li><span class="hd-11__num">04</span><span class="hd-11__li-t">Toast</span><span class="hd-11__li-d">Live region built in, four positions, zero deps</span></li>
    </ul>
    <div class="hd-11__filler" aria-hidden="true"></div>
  </main>
</div>
```
## CSS
```css
.hd-11 {
  --paper: #fbfbfa;
  --paper2: #f1f1ef;
  --ink: #111111;
  --muted: #5f5f5c;
  --line: #111111;
  --gh: #111111;
  --lift: 3px;
  --font-display: "JetBrains Mono",ui-monospace,"IBM Plex Mono",monospace;
  --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.55;
}

@supports (color: oklch(50% .1 200)) {
  .hd-11 {
    --paper: oklch(98.5% .002 90);
    --paper2: oklch(95% .003 90);
    --ink: oklch(15% 0 0);
    --muted: oklch(48% .003 90);
  }
}

.hd-11 * {
  box-sizing: border-box;
}

.hd-11 h1,
.hd-11 p,
.hd-11 ul,
.hd-11 pre {
  margin: 0;
  padding: 0;
}

.hd-11 ul {
  list-style: none;
}

.hd-11 [hidden] {
  display: none;
}

.hd-11 :focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 4px;
}

.hd-11__skip {
  position: absolute;
  inset-inline-start: 1rem;
  top: -3rem;
  z-index: 60;
  padding: .5rem .9rem;
  background: var(--ink);
  color: var(--paper);
  font-family: var(--font-display);
  font-size: .78rem;
  font-weight: 600;
  text-decoration: none;
  transition: top .18s ease;
}

.hd-11__skip:focus-visible {
  top: .75rem;
}
/* ── header: flat monochrome, hard offset accents ─────────────────── */

.hd-11__bar {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  gap: clamp(.75rem,3vw,2rem);
  padding: .9rem clamp(1rem,4vw,2rem);
  background: var(--paper);
  border-bottom: 1px solid var(--line);
}

.hd-11__brand {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  color: var(--ink);
  text-decoration: none;
  min-inline-size: 0;
}

.hd-11__mark {
  inline-size: 1.5rem;
  block-size: 1.5rem;
  flex: none;
}

.hd-11__word {
  font-family: var(--font-display);
  font-size: .95rem;
  font-weight: 800;
  letter-spacing: -.04em;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-11__word span {
  font-weight: 400;
  color: var(--muted);
}

.hd-11__nav {
  min-inline-size: 0;
}

.hd-11__nav ul {
  display: flex;
  align-items: center;
  gap: clamp(.5rem,2vw,1.35rem);
}

.hd-11__nav a {
  display: block;
  padding: .4rem 0;
  color: var(--muted);
  text-decoration: none;
  font-family: var(--font-display);
  font-size: .82rem;
  font-weight: 500;
  white-space: nowrap;
  border-bottom: 2px solid transparent;
  transition: color .15s ease, border-color .15s ease;
}

.hd-11__nav a:hover {
  color: var(--ink);
  border-bottom-color: var(--ink);
}

.hd-11__nav a[aria-current="page"] {
  color: var(--ink);
  border-bottom-color: var(--ink);
  font-weight: 600;
}

.hd-11__right {
  display: flex;
  align-items: center;
  gap: .75rem;
  margin-inline-start: auto;
}

.hd-11__quiet {
  color: var(--muted);
  text-decoration: none;
  font-family: var(--font-display);
  font-size: .82rem;
  white-space: nowrap;
  transition: color .15s ease;
}

.hd-11__quiet:hover {
  color: var(--ink);
  text-decoration: underline;
  text-underline-offset: .25em;
}

.hd-11__star {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  min-block-size: 2.75rem;
  min-inline-size: 7.5rem;
  padding: .6rem .9rem;
  border: 1.5px solid var(--line);
  border-radius: 0;
  background: var(--paper);
  color: var(--ink);
  text-decoration: none;
  font-family: var(--font-display);
  font-size: .85rem;
  font-weight: 600;
  white-space: nowrap;
  box-shadow: var(--lift) var(--lift) 0 0 var(--ink);
  transition: background-color .16s ease, color .16s ease, translate .16s ease, box-shadow .16s ease;
}

.hd-11__star svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  flex: none;
}

.hd-11__starico {
  color: #f0b429;
}

.hd-11__count {
  font-variant-numeric: tabular-nums;
  margin-inline-start: auto;
}

.hd-11__star:hover,
.hd-11__star:focus-visible {
  background: var(--gh);
  color: var(--paper);
  border-color: var(--gh);
  translate: calc(var(--lift) * -.6) calc(var(--lift) * -.6);
  box-shadow: calc(var(--lift) * 1.6) calc(var(--lift) * 1.6) 0 0 var(--ink);
}

.hd-11__star:active {
  translate: 0 0;
  box-shadow: 0 0 0 0 var(--ink);
}
/* ── page body ────────────────────────────────────────────────────── */

.hd-11__main {
  max-inline-size: 62rem;
  margin-inline: auto;
  padding: clamp(2.5rem,7vw,4.5rem) clamp(1rem,4vw,2rem) 5rem;
}

.hd-11__eyebrow {
  font-family: var(--font-display);
  font-size: .78rem;
  color: var(--muted);
}

.hd-11__main h1 {
  font-family: var(--font-display);
  font-size: clamp(1.9rem,6vw,3.2rem);
  line-height: 1.06;
  font-weight: 800;
  letter-spacing: -.055em;
  margin-top: 1rem;
  max-inline-size: 26ch;
  text-wrap: balance;
}

.hd-11__lead {
  margin-top: 1.1rem;
  max-inline-size: 56ch;
  color: var(--muted);
  font-size: 1.02rem;
  text-wrap: pretty;
}

.hd-11__pre {
  margin-top: 2rem;
  padding: 1.1rem 1.25rem;
  border: 1.5px solid var(--line);
  box-shadow: var(--lift) var(--lift) 0 0 var(--ink);
  background: var(--paper2);
  font-family: var(--font-display);
  font-size: .84rem;
  line-height: 1.8;
  overflow: auto;
}

.hd-11__list {
  margin-top: 2.25rem;
  border-top: 1px solid var(--line);
}

.hd-11__list li {
  display: grid;
  grid-template-columns: 2.5rem 10rem minmax(0,1fr);
  align-items: baseline;
  gap: 1rem;
  padding: .9rem .25rem;
  border-bottom: 1px solid var(--line);
}

.hd-11__list li:hover {
  background: var(--paper2);
}

.hd-11__num {
  font-family: var(--font-display);
  font-size: .78rem;
  color: var(--muted);
}

.hd-11__li-t {
  font-family: var(--font-display);
  font-size: .95rem;
  font-weight: 600;
}

.hd-11__li-d {
  font-size: .88rem;
  color: var(--muted);
  min-inline-size: 0;
  text-wrap: pretty;
}

.hd-11__filler {
  block-size: 45vh;
}

@media (max-width: 760px) {
  .hd-11__quiet {
    display: none;
  }

  .hd-11__list li {
    grid-template-columns: 2.5rem minmax(0,1fr);
  }

  .hd-11__li-d {
    grid-column: 2;
  }
}

@media (max-width: 640px) {
  .hd-11__nav {
    order: 3;
    flex-basis: 100%;
    overflow: auto;
    scroll-snap-type: x proximity;
    scrollbar-width: none;
  }

  .hd-11__nav::-webkit-scrollbar {
    display: none;
  }

  .hd-11__bar {
    flex-wrap: wrap;
    gap: .6rem;
  }

  .hd-11__nav a {
    scroll-snap-align: start;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-11:has(#hd-11-dark:checked) {
  --paper: #0d0d0d;
  --paper2: #171717;
  --ink: #f5f5f4;
  --muted: #9a9a97;
  --line: #f5f5f4;
  --gh: #f5f5f4;
}

.hd-11:has(#hd-11-dark:checked) .hd-11__star:hover,
.hd-11:has(#hd-11-dark:checked) .hd-11__star:focus-visible {
  color: #0d0d0d;
}
/* icon: shows the scheme the toggle will switch you to */

.hd-11__sun {
  display: none;
}

.hd-11:has(#hd-11-dark:checked) .hd-11__moon {
  display: none;
}

.hd-11:has(#hd-11-dark:checked) .hd-11__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .hd-11:not([data-theme="light"]):not(:has(#hd-11-dark:checked)) {
    --paper: #0d0d0d;
    --paper2: #171717;
    --ink: #f5f5f4;
    --muted: #9a9a97;
    --line: #f5f5f4;
    --gh: #f5f5f4;
  }

  .hd-11:not([data-theme="light"]):not(:has(#hd-11-dark:checked)) .hd-11__star:hover,
    .hd-11:not([data-theme="light"]):not(:has(#hd-11-dark:checked)) .hd-11__star:focus-visible {
    color: #0d0d0d;
  }
  /* FLIP-BACK — dark OS + checked toggle returns to the other scheme */

  .hd-11:has(#hd-11-dark:checked) {
    --paper: #fbfbfa;
    --paper2: #f1f1ef;
    --ink: #111111;
    --muted: #5f5f5c;
    --line: #111111;
    --gh: #111111;
    --lift: 3px;
    --font-display: "JetBrains Mono",ui-monospace,"IBM Plex Mono",monospace;
    --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  }

  .hd-11:has(#hd-11-dark:checked) .hd-11__star:hover,
    .hd-11:has(#hd-11-dark:checked) .hd-11__star:focus-visible {
    color: var(--paper);
  }
  /* the icon always offers the scheme you are not in */

  .hd-11:not([data-theme="light"]):not(:has(#hd-11-dark:checked)) .hd-11__moon {
    display: none;
  }

  .hd-11:not([data-theme="light"]):not(:has(#hd-11-dark:checked)) .hd-11__sun {
    display: block;
  }

  .hd-11:has(#hd-11-dark:checked) .hd-11__sun {
    display: none;
  }

  .hd-11:has(#hd-11-dark:checked) .hd-11__moon {
    display: block;
  }
}

.hd-11[data-theme="dark"] {
  --paper: #0d0d0d;
  --paper2: #171717;
  --ink: #f5f5f4;
  --muted: #9a9a97;
  --line: #f5f5f4;
  --gh: #f5f5f4;
}

@media (prefers-reduced-motion: reduce) {
  .hd-11 * {
    transition-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-11__star {
    border: 1px solid CanvasText;
  }
}
/* ── theme toggle — visually hidden checkbox, zero JS ────────────── */

.hd-11__sr,
.hd-11__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-11__theme {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 0;
  border-radius: 999px;
  background: transparent;
  color: inherit;
  cursor: pointer;
  transition: background-color .18s ease;
}

.hd-11__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-11__theme:hover {
  background: rgba(128,128,128,.16);
}

.hd-11:has(#hd-11-dark:focus-visible) .hd-11__theme {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```
