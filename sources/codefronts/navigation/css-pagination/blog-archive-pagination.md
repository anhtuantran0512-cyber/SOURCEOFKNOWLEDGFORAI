---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/blog-archive-pagination/"
title: "Blog Archive Pagination"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "Archive pagination is read, not clicked, so the directional links carry the destination article's title under a Newer / Older label — the reader knows what…"
has_js: "false"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Blog Archive Pagination
Source: https://codefronts.com/navigation/css-pagination/blog-archive-pagination/

Archive pagination is read, not clicked, so the directional links carry the destination article's title under a Newer / Older label — the reader knows what is on the other side before committing. A three-column grid pins the page numbers dead centre no matter how long those titles run, and the post links use an animated background-size underline that never shifts the baseline.
## HTML
```html
<section class="pgn-12" aria-label="Blog / Article Archive Pagination demo">
  <div class="pgn-12__stage">
    <header class="pgn-12__head">
      <p class="pgn-12__eyebrow">Archive · Page 3 of 12</p>
      <h2 class="pgn-12__title">Writing</h2>
    </header>

    <ol class="pgn-12__posts">
      <li class="pgn-12__post">
        <p class="pgn-12__meta"><time datetime="2026-05-14">14 May</time> · Container queries</p>
        <h3><a class="pgn-12__plink" href="#pgn-12-archive">Getting Started with Container Queries</a></h3>
        <p class="pgn-12__dek">Why component-level breakpoints replace the global ones you have been maintaining, and how to migrate a card grid in an afternoon.</p>
      </li>
      <li class="pgn-12__post">
        <p class="pgn-12__meta"><time datetime="2026-05-02">2 May</time> · Performance</p>
        <h3><a class="pgn-12__plink" href="#pgn-12-archive">The Cost of a Layout Library</a></h3>
        <p class="pgn-12__dek">We measured four grid abstractions against plain CSS grid on a mid-range Android device. The gap was larger than expected.</p>
      </li>
      <li class="pgn-12__post">
        <p class="pgn-12__meta"><time datetime="2026-04-27">27 Apr</time> · Accessibility</p>
        <h3><a class="pgn-12__plink" href="#pgn-12-archive">Focus Order Is a Design Decision</a></h3>
        <p class="pgn-12__dek">Tab order is not a developer detail — it is reading order, and it belongs in the wireframe next to the visual hierarchy.</p>
      </li>
    </ol>

    <nav class="pgn-12__nav" id="pgn-12-archive" aria-label="Archive pagination">
      <a class="pgn-12__dir" href="#pgn-12-archive">
        <span class="pgn-12__dirlabel">Newer posts</span>
        <span class="pgn-12__dirtitle">Focus Order Is a Design Decision</span>
      </a>
      <ol class="pgn-12__pages">
        <li><a class="pgn-12__num" href="#pgn-12-archive" aria-label="Page 2">2</a></li>
        <li><a class="pgn-12__num" href="#pgn-12-archive" aria-current="page" aria-label="Page 3, current page">3</a></li>
        <li><a class="pgn-12__num" href="#pgn-12-archive" aria-label="Page 4">4</a></li>
      </ol>
      <a class="pgn-12__dir pgn-12__dir--next" href="#pgn-12-archive">
        <span class="pgn-12__dirlabel">Older posts</span>
        <span class="pgn-12__dirtitle">A Budget for Third-Party Scripts</span>
      </a>
    </nav>
  </div>
</section>
```
## CSS
```css
.pgn-12 {
  --bg: #fbfaf8;
  --surface: #ffffff;
  --surface-2: #f3f2ef;
  --text: #12110f;
  --muted: #6f6b64;
  --line: #e5e2dc;
  --acc: #12110f;
  --acc-fg: #fbfaf8;
  --ring: #8b5cf6;
}

@supports (color: oklch(50% 0 0)) {
  .pgn-12 {
    --bg: oklch(98.4% .004 85);
    --surface: oklch(100% 0 0);
    --surface-2: oklch(96.4% .006 85);
    --text: oklch(18% .008 60);
    --muted: oklch(52% .012 70);
    --line: oklch(91% .008 80);
    --acc: oklch(18% .008 60);
    --acc-fg: oklch(98.4% .004 85);
    --ring: oklch(62% .19 300);
  }
}

@media (prefers-color-scheme: dark) {
  .pgn-12:not([data-theme="light"]) {
    --bg: #0d0c0b;
    --surface: #151412;
    --surface-2: #1e1c1a;
    --text: #f6f4f0;
    --muted: #a8a29a;
    --line: #2a2724;
    --acc: #f6f4f0;
    --acc-fg: #0d0c0b;
    --ring: #c4b5fd;
  }
}

.pgn-12[data-theme="dark"] {
  --bg: #0d0c0b;
  --surface: #151412;
  --surface-2: #1e1c1a;
  --text: #f6f4f0;
  --muted: #a8a29a;
  --line: #2a2724;
  --acc: #f6f4f0;
  --acc-fg: #0d0c0b;
  --ring: #c4b5fd;
}

.pgn-12 {
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

.pgn-12,
.pgn-12 *,
.pgn-12 *::before,
.pgn-12 *::after {
  box-sizing: border-box;
}

.pgn-12__stage {
  width: 100%;
  max-width: 44rem;
  display: grid;
  gap: 2.25rem;
}

.pgn-12__eyebrow {
  margin: 0 0 .4rem;
  font-size: .6875rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pgn-12__title {
  margin: 0;
  font-size: clamp(1.6rem,3.6vw,2.15rem);
  font-weight: 600;
  letter-spacing: -.03em;
}

.pgn-12__posts {
  display: grid;
  gap: 1.75rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.pgn-12__post {
  display: grid;
  gap: .4rem;
  padding-bottom: 1.75rem;
  border-bottom: 1px solid var(--line);
}

.pgn-12__post:last-child {
  border-bottom: 0;
  padding-bottom: 0;
}

.pgn-12__meta {
  margin: 0;
  font-size: .75rem;
  letter-spacing: .02em;
  color: var(--muted);
}

.pgn-12__post h3 {
  margin: 0;
  font-size: 1.125rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.pgn-12__plink {
  color: inherit;
  text-decoration: none;
  background-image: linear-gradient(currentColor,currentColor);
  background-size: 0 1px;
  background-position: 0 100%;
  background-repeat: no-repeat;
  transition: background-size .28s cubic-bezier(.16,1,.3,1);
}

.pgn-12__plink:hover {
  background-size: 100% 1px;
}

.pgn-12__plink:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
  border-radius: .15rem;
}

.pgn-12__dek {
  margin: 0;
  font-size: .9375rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.pgn-12__nav {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 1rem;
  padding-top: 1.75rem;
  border-top: 1px solid var(--line);
  scroll-margin-block: 2rem;
}

.pgn-12__dir {
  display: grid;
  gap: .2rem;
  padding: .7rem .9rem;
  border-radius: .75rem;
  color: inherit;
  text-decoration: none;
  transition: background .18s ease;
}

.pgn-12__dir:hover {
  background: var(--surface-2);
}

.pgn-12__dir:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.pgn-12__dir--next {
  text-align: right;
  justify-items: end;
}

.pgn-12__dirlabel {
  font-size: .75rem;
  letter-spacing: .02em;
  color: var(--muted);
}

.pgn-12__dirtitle {
  font-size: .875rem;
  font-weight: 550;
  letter-spacing: -.01em;
  max-width: 15rem;
  text-wrap: pretty;
}

.pgn-12__pages {
  display: flex;
  gap: .25rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.pgn-12__num {
  display: grid;
  place-items: center;
  min-width: 2.75rem;
  height: 2.75rem;
  border-radius: .5rem;
  color: var(--muted);
  text-decoration: none;
  font-size: .875rem;
  font-variant-numeric: tabular-nums;
  transition: background .16s ease, color .16s ease;
}

.pgn-12__num:hover {
  background: var(--surface-2);
  color: var(--text);
}

.pgn-12__num:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.pgn-12__num[aria-current="page"] {
  background: var(--acc);
  color: var(--acc-fg);
  font-weight: 600;
}

@media (max-width: 40rem) {
  .pgn-12__nav {
    grid-template-columns: 1fr 1fr;
  }

  .pgn-12__pages {
    grid-column: 1/-1;
    justify-content: center;
    order: -1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pgn-12 * {
    animation: none !important;
    transition: none !important;
  }
}
```
