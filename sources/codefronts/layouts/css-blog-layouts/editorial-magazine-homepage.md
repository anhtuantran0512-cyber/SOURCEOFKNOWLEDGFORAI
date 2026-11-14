---
source: "codefronts"
url: "https://codefronts.com/layouts/css-blog-layouts/editorial-magazine-homepage/"
title: "Editorial Magazine Homepage"
section: "layouts"
category: "css-blog-layouts"
category_name: "CSS Blog Layouts"
description: "A full publication front page in one grid: an oversized lead story, a four-up secondary grid whose cards align to the pixel via subgrid, and an editor's…"
has_js: "false"
---

Here's a working CSS Blog Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Editorial Magazine Homepage
Source: https://codefronts.com/layouts/css-blog-layouts/editorial-magazine-homepage/

A full publication front page in one grid: an oversized lead story, a four-up secondary grid whose cards align to the pixel via subgrid, and an editor's picks rail that is a sticky column on the desktop and a scroll-snap strip on a phone. No JavaScript — the entire responsive behaviour is grid-template-areas plus one container query.
## HTML
```html
<div class="bl-01">
  <header class="bl-01__masthead">
    <a class="bl-01__wordmark" href="#bl-01-main">The Fold<span aria-hidden="true">.</span></a>
    <nav class="bl-01__sections" aria-label="Sections">
      <a href="#bl-01-main" aria-current="page">Culture</a>
      <a href="#bl-01-main">Design</a>
      <a href="#bl-01-main">Technology</a>
      <a href="#bl-01-main">Cities</a>
      <a href="#bl-01-main">Long Reads</a>
    </nav>
    <p class="bl-01__meta"><time datetime="2026-08-10">Mon 10 Aug 2026</time> · Issue 214</p>
  </header>

  <p class="bl-01__ticker">Now reading — <a href="#bl-01-main">The quiet return of the printed zine</a></p>

  <main class="bl-01__main" id="bl-01-main">
    <article class="bl-01__lead">
      <a class="bl-01__leadMedia" href="#bl-01-main" tabindex="-1" aria-hidden="true">
        <img src="https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=1400&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="1400" height="900" loading="eager" decoding="async">
      </a>
      <div class="bl-01__leadBody">
        <p class="bl-01__kicker">The Reported Essay</p>
        <h1 class="bl-01__leadTitle"><a href="#bl-01-main">The city that decided to stop building upwards</a></h1>
        <p class="bl-01__dek">Fourteen years after the tower moratorium, planners in Rotterdam are quietly proving that density and height were never the same argument.</p>
        <p class="bl-01__byline">By <a href="#bl-01-main">Marta Kollár</a> · <span>18 min read</span></p>
      </div>
    </article>

    <section class="bl-01__grid" aria-label="More stories">
      <article class="bl-01__card">
        <a class="bl-01__cardMedia" href="#bl-01-main" tabindex="-1" aria-hidden="true">
          <img src="https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=700&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="700" height="500" loading="lazy" decoding="async">
        </a>
        <h2><a href="#bl-01-main">Fifteen-minute neighbourhoods, audited</a></h2>
        <p class="bl-01__cardMeta">Cities · <time datetime="2026-08-09">9 Aug</time></p>
      </article>
      <article class="bl-01__card">
        <a class="bl-01__cardMedia" href="#bl-01-main" tabindex="-1" aria-hidden="true">
          <img src="https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=700&amp;q=70&amp;auto=format&amp;fit=crop" alt="" width="700" height="500" loading="lazy" decoding="async">
        </a>
        <h2><a href="#bl-01-main">The studio that runs on four-day weeks</a></h2>
        <p class="bl-01__cardMeta">Work · <time datetime="2026-08-08">8 Aug</time></p>
      </article>
      <article class="bl-01__card">
        <h2><a href="#bl-01-main">A short history of the pull quote, from Gutenberg to the feed</a></h2>
        <p class="bl-01__cardDek">Typography's loudest device was invented to sell newspapers, and it still is.</p>
        <p class="bl-01__cardMeta">Design · <time datetime="2026-08-07">7 Aug</time></p>
      </article>
      <article class="bl-01__card">
        <h2><a href="#bl-01-main">Why every archive is a design problem first</a></h2>
        <p class="bl-01__cardDek">Six librarians on the interfaces that decide what gets remembered.</p>
        <p class="bl-01__cardMeta">Culture · <time datetime="2026-08-06">6 Aug</time></p>
      </article>
    </section>

    <aside class="bl-01__picks" aria-labelledby="bl-01-picks-h">
      <div class="bl-01__picksInner">
        <h2 class="bl-01__picksTitle" id="bl-01-picks-h">Editor's picks</h2>
        <ol class="bl-01__picksList">
          <li><a href="#bl-01-main"><span class="bl-01__picksNum">01</span><span>The last independent bookshop on Gran Via</span></a></li>
          <li><a href="#bl-01-main"><span class="bl-01__picksNum">02</span><span>What we got wrong about remote culture</span></a></li>
          <li><a href="#bl-01-main"><span class="bl-01__picksNum">03</span><span>A field guide to municipal typography</span></a></li>
          <li><a href="#bl-01-main"><span class="bl-01__picksNum">04</span><span>The 40-year-old software still running the trams</span></a></li>
          <li><a href="#bl-01-main"><span class="bl-01__picksNum">05</span><span>Notes on writing in public for a decade</span></a></li>
        </ol>
        <p class="bl-01__picksNote">Updated weekly by the desk.</p>
      </div>
    </aside>
  </main>

  <footer class="bl-01__footer">
    <p>The Fold — independent since 2019.</p>
    <nav aria-label="Footer"><a href="#bl-01-main">Masthead</a><a href="#bl-01-main">Ethics</a><a href="#bl-01-main">Newsletter</a></nav>
  </footer>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Schibsted+Grotesk:wght@400;500;600;700&display=swap');

.bl-01 {
  --bg: #fdfcfa;
  --surface: #ffffff;
  --text: #14110f;
  --muted: #6b645c;
  --line: #e6e1d8;
  --acc: #9a3412;
  --lead-ratio: 16/10;
  --serif: "Instrument Serif",ui-serif,Georgia,"Times New Roman",serif;
  --sans: "Schibsted Grotesk",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
}

@supports (color: oklch(50% 0 0)) {
  .bl-01 {
    --bg: oklch(98.8% .005 85);
    --surface: oklch(100% 0 0);
    --text: oklch(18% .012 60);
    --muted: oklch(52% .015 65);
    --line: oklch(91% .012 82);
    --acc: oklch(48% .15 42);
  }
}

@media (prefers-color-scheme: dark) {
  .bl-01:not([data-theme="light"]) {
    --bg: #0f0e0d;
    --surface: #171513;
    --text: #f5f2ed;
    --muted: #a39c92;
    --line: #2c2825;
    --acc: #f97316;
  }
}

.bl-01[data-theme="dark"] {
  --bg: #0f0e0d;
  --surface: #171513;
  --text: #f5f2ed;
  --muted: #a39c92;
  --line: #2c2825;
  --acc: #f97316;
}

.bl-01 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}

.bl-01,
.bl-01 *,
.bl-01 *::before,
.bl-01 *::after {
  box-sizing: border-box;
}

.bl-01 img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: var(--line);
}

.bl-01 a {
  color: inherit;
  text-decoration: none;
}

.bl-01 a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
  border-radius: 2px;
}

.bl-01 ::selection {
  background: color-mix(in oklab,var(--acc) 22%,transparent);
}

.bl-01__masthead {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .75rem clamp(1rem,3vw,2.5rem);
  padding: clamp(1rem,2.5vw,1.5rem) clamp(1.25rem,4vw,4rem);
  border-bottom: 1px solid var(--line);
  background: color-mix(in oklab,var(--bg) 82%,transparent);
  position: sticky;
  top: 0;
  z-index: 5;
}

@supports (backdrop-filter: blur(6px)) {
  .bl-01__masthead {
    backdrop-filter: blur(14px) saturate(1.4);
  }
}

.bl-01__wordmark {
  font-family: var(--serif);
  font-size: clamp(1.5rem,3vw,2rem);
  line-height: 1;
  letter-spacing: -.02em;
}

.bl-01__wordmark span {
  color: var(--acc);
}

.bl-01__sections {
  display: flex;
  flex-wrap: wrap;
  gap: .25rem;
  margin-inline-end: auto;
}

.bl-01__sections a {
  display: grid;
  place-items: center;
  min-height: 2.75rem;
  padding: 0 .75rem;
  border-radius: 999px;
  font-size: .8125rem;
  font-weight: 500;
  letter-spacing: .01em;
  color: var(--muted);
  transition: background .18s ease, color .18s ease;
}

.bl-01__sections a:hover {
  background: color-mix(in oklab,var(--text) 6%,transparent);
  color: var(--text);
}

.bl-01__sections a[aria-current="page"] {
  color: var(--text);
  background: color-mix(in oklab,var(--acc) 12%,transparent);
}

.bl-01__meta {
  margin: 0;
  font-size: .75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.bl-01__ticker {
  margin: 0;
  padding: .625rem clamp(1.25rem,4vw,4rem);
  border-bottom: 1px solid var(--line);
  font-size: .8125rem;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: .1em;
}

.bl-01__ticker a {
  color: var(--text);
  text-decoration: underline;
  text-decoration-color: color-mix(in oklab,var(--acc) 60%,transparent);
  text-underline-offset: .25em;
}

.bl-01__main {
  display: grid;
  gap: clamp(1.75rem,3.5vw,3.5rem);
  grid-template-columns: minmax(0,2.2fr) minmax(0,1fr);
  grid-template-areas: "lead picks" "grid picks";
  align-items: start;
  padding: clamp(1.75rem,4vw,4rem) clamp(1.25rem,4vw,4rem);
  max-width: 96rem;
  margin-inline: auto;
}

.bl-01__lead {
  grid-area: lead;
  display: grid;
  gap: clamp(1rem,2vw,1.75rem);
}

.bl-01__leadMedia {
  display: block;
  aspect-ratio: var(--lead-ratio);
  overflow: hidden;
  border-radius: .5rem;
}

.bl-01__leadMedia img {
  transition: scale .7s cubic-bezier(.16,1,.3,1);
}

.bl-01__lead:hover .bl-01__leadMedia img {
  scale: 1.03;
}

.bl-01__leadBody {
  display: grid;
  gap: .75rem;
  max-width: 38ch;
}

.bl-01__kicker {
  margin: 0;
  font-size: .75rem;
  font-weight: 600;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
}

.bl-01__leadTitle {
  margin: 0;
  font-family: var(--serif);
  font-weight: 400;
  font-size: clamp(2.25rem,5.2vw,4rem);
  line-height: .98;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.bl-01__leadTitle a {
  background: linear-gradient(currentColor,currentColor) 0 100%/0 1px no-repeat;
  transition: background-size .4s cubic-bezier(.16,1,.3,1);
}

.bl-01__leadTitle a:hover {
  background-size: 100% 1px;
}

.bl-01__dek {
  margin: 0;
  font-size: clamp(1rem,1.5vw,1.125rem);
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
  max-width: 52ch;
}

.bl-01__byline {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
}

.bl-01__byline a {
  color: var(--text);
  font-weight: 500;
}

.bl-01__grid {
  grid-area: grid;
  display: grid;
  gap: clamp(1.25rem,2.5vw,2rem);
  grid-template-columns: repeat(auto-fill,minmax(15rem,1fr));
  grid-template-rows: repeat(3,auto);
  padding-top: clamp(1.5rem,3vw,2.5rem);
  border-top: 1px solid var(--line);
}

.bl-01__card {
  display: grid;
  gap: .5rem;
  align-content: start;
  grid-row: span 3;
}

@supports (grid-template-rows: subgrid) {
  .bl-01__card {
    grid-template-rows: subgrid;
  }
}

.bl-01__cardMedia {
  display: block;
  aspect-ratio: 7/5;
  overflow: hidden;
  border-radius: .375rem;
  margin-bottom: .25rem;
}

.bl-01__card h2 {
  margin: 0;
  font-family: var(--serif);
  font-weight: 400;
  font-size: 1.375rem;
  line-height: 1.12;
  letter-spacing: -.01em;
  text-wrap: balance;
  align-self: start;
}

.bl-01__card:not(:has(img)) h2 {
  font-size: 1.625rem;
}

.bl-01__card:not(:has(img)) {
  padding: 1.125rem 1.25rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: .625rem;
}

.bl-01__card h2 a {
  transition: color .18s ease;
}

.bl-01__card h2 a:hover {
  color: var(--acc);
}

.bl-01__cardDek {
  margin: 0;
  font-size: .875rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.bl-01__cardMeta {
  margin: 0;
  align-self: end;
  font-size: .6875rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.bl-01__picks {
  grid-area: picks;
}

.bl-01__picksInner {
  position: sticky;
  top: 6.5rem;
  padding: clamp(1.25rem,2vw,1.75rem);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: .75rem;
}

.bl-01__picksTitle {
  margin: 0 0 1rem;
  font-size: .75rem;
  font-weight: 600;
  letter-spacing: .16em;
  text-transform: uppercase;
}

.bl-01__picksList {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
}

.bl-01__picksList li + li {
  border-top: 1px solid var(--line);
}

.bl-01__picksList a {
  display: grid;
  grid-template-columns: 2rem 1fr;
  gap: .75rem;
  align-items: baseline;
  padding: .875rem 0;
  min-height: 2.75rem;
  font-family: var(--serif);
  font-size: 1.0625rem;
  line-height: 1.25;
  text-wrap: pretty;
  transition: padding-inline-start .25s cubic-bezier(.16,1,.3,1), color .18s ease;
}

.bl-01__picksList a:hover {
  padding-inline-start: .375rem;
  color: var(--acc);
}

.bl-01__picksNum {
  font-family: var(--sans);
  font-size: .6875rem;
  font-weight: 600;
  color: var(--acc);
  font-variant-numeric: tabular-nums;
}

.bl-01__picksNote {
  margin: 1rem 0 0;
  font-size: .75rem;
  color: var(--muted);
}

.bl-01__footer {
  display: flex;
  flex-wrap: wrap;
  gap: .75rem 1.5rem;
  align-items: center;
  justify-content: space-between;
  padding: clamp(1.5rem,3vw,2.5rem) clamp(1.25rem,4vw,4rem);
  border-top: 1px solid var(--line);
  font-size: .8125rem;
  color: var(--muted);
}

.bl-01__footer p {
  margin: 0;
}

.bl-01__footer nav {
  display: flex;
  gap: 1.25rem;
}

.bl-01__footer a:hover {
  color: var(--acc);
}

@media (max-width: 60rem) {
  .bl-01__main {
    grid-template-columns: minmax(0,1fr);
    grid-template-areas: "lead" "grid" "picks";
  }

  .bl-01__picksInner {
    position: static;
  }

  .bl-01__picksList {
    grid-auto-flow: column;
    grid-auto-columns: min(72vw,17rem);
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    gap: 0 1rem;
    padding-bottom: .5rem;
    scrollbar-width: thin;
  }

  .bl-01__picksList li {
    scroll-snap-align: start;
  }

  .bl-01__picksList li + li {
    border-top: 0;
    border-inline-start: 1px solid var(--line);
    padding-inline-start: 1rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bl-01 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .bl-01__sections a[aria-current="page"] {
    forced-color-adjust: none;
    background: Highlight;
    color: HighlightText;
  }
}
```
