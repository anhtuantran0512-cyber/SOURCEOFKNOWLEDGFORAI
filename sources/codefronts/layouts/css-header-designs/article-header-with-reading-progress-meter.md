---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/article-header-with-reading-progress-meter/"
title: "Article Header with Reading Progress Meter"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "An editorial article header: section kicker, headline, byline with reading time, and a hairline progress meter that fills as the reader moves down the piece."
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Article Header with Reading Progress Meter
Source: https://codefronts.com/layouts/css-header-designs/article-header-with-reading-progress-meter/

An editorial article header: section kicker, headline, byline with reading time, and a hairline progress meter that fills as the reader moves down the piece. The meter is a single element scaled with transform: scaleX() on a scroll(root) timeline, so it costs one composited layer instead of a scroll handler recalculating percentages on every frame.
## HTML
```html
<div class="hd-06">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&display=swap">
  <a class="hd-06__skip" href="#hd-06-main">Skip to content</a>

  <header class="hd-06__bar">
    <div class="hd-06__bar-in">
      <a class="hd-06__brand" href="#hd-06-main">The Long Field</a>
      <nav class="hd-06__nav" aria-label="Main">
        <ul>
          <li><a href="#hd-06-main">Reporting</a></li>
          <li><a href="#hd-06-main">Essays</a></li>
          <li><a href="#hd-06-main">Interviews</a></li>
        </ul>
      </nav>
          <input class="hd-06__sr" type="checkbox" id="hd-06-dark">
      <label class="hd-06__theme" for="hd-06-dark">
        <svg class="hd-06__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <svg class="hd-06__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <span class="hd-06__vh">Switch light or dark theme</span>
      </label>
      <a class="hd-06__sub" href="#hd-06-main">Subscribe</a>
    </div>
    <div class="hd-06__meter" aria-hidden="true"><span class="hd-06__meter-fill"></span></div>
  </header>

  <main class="hd-06__main" id="hd-06-main">
    <article class="hd-06__article">
      <p class="hd-06__kicker">Infrastructure</p>
      <h1>The quiet return of the boring database</h1>
      <p class="hd-06__standfirst">Three years of exotic storage engines later, the teams shipping fastest are the ones who chose the least interesting option on the list.</p>

      <div class="hd-06__byline">
        <span class="hd-06__av" aria-hidden="true">JL</span>
        <span class="hd-06__by-t">
          <span class="hd-06__by-n">Jordan Lee</span>
          <span class="hd-06__by-m"><time datetime="2026-08-18">18 August 2026</time> &middot; 7 min read</span>
        </span>
      </div>

      <figure class="hd-06__figure">
        <img src="https://images.unsplash.com/photo-1544197150-b99a580bb7a8?auto=format&amp;fit=crop&amp;w=1200&amp;q=70" alt="Rows of server cabinets lit in low blue light" loading="lazy" width="1200" height="675">
        <figcaption>A regional facility outside Dublin, still running the same primary it was commissioned with.</figcaption>
      </figure>

      <p>The pitch was never wrong, exactly. Sharding across a mesh of specialised stores really can serve a workload no single node would survive. The problem is that almost nobody has that workload, and the ones who genuinely do tend to know it years in advance.</p>
      <p>What changed is not the technology. It is that the cost of operating exotic infrastructure finally landed on the same teams who chose it. When the on-call rotation and the migration budget belong to the same six people, the appetite for novelty drops sharply.</p>
      <h2>What the fast teams have in common</h2>
      <p>Every group we spoke to described the same sequence: a single managed primary, read replicas added only when a measured query budget demanded them, and a hard rule against a second storage technology until the first one has been genuinely exhausted.</p>
      <p>None of them described this as a philosophy. They described it as the thing that let them ship a feature in a week instead of a quarter.</p>
      <blockquote>We were spending about a day a week explaining our own architecture to ourselves. That is a tax you can just decline to pay.</blockquote>
      <p>The counter-argument is real and worth stating: the boring choice moves the ceiling closer. You will meet it, and when you do the migration is expensive precisely because everything depends on the thing you are replacing.</p>
      <h2>The part nobody writes down</h2>
      <p>Most of these teams do run something exotic &mdash; a vector index, a time-series store, a queue with unusual delivery semantics. The difference is that it sits beside the boring database rather than instead of it, and it holds data the team could lose on a bad afternoon without ending the company.</p>
      <p>That is the actual pattern. Not conservatism, but a clear-eyed split between the data that must survive and the data that merely has to be fast.</p>
      <p>Scroll back up: the hairline under the masthead has been tracking your position the whole way down, and it never once asked the main thread for help.</p>
    </article>
  </main>
</div>
```
## CSS
```css
.hd-06 {
  --paper: #fbf9f5;
  --ink: #16130f;
  --muted: #6d655a;
  --rule: rgba(22,19,15,.16);
  --accent: #b4232a;
  --accent-soft: rgba(180,35,42,.09);
  --meter-h: 3px;
  --av: 2.35rem;
  --font-display: "Newsreader",Georgia,"Iowan Old Style","Times New Roman",serif;
  --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.6;
}

@supports (color: oklch(50% .1 200)) {
  .hd-06 {
    --paper: oklch(98% .01 85);
    --ink: oklch(18% .012 60);
    --muted: oklch(50% .015 65);
    --accent: oklch(48% .17 25);
  }
}

.hd-06 * {
  box-sizing: border-box;
}

.hd-06 h1,
.hd-06 h2,
.hd-06 p,
.hd-06 ul,
.hd-06 figure,
.hd-06 blockquote {
  margin: 0;
  padding: 0;
}

.hd-06 ul {
  list-style: none;
}

.hd-06 [hidden] {
  display: none;
}

.hd-06 :focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.hd-06__skip {
  position: absolute;
  inset-inline-start: 1rem;
  top: -3rem;
  z-index: 60;
  padding: .5rem .9rem;
  background: var(--ink);
  color: var(--paper);
  font-size: .8rem;
  font-weight: 640;
  text-decoration: none;
  transition: top .18s ease;
}

.hd-06__skip:focus-visible {
  top: .75rem;
}
/* ── header: no chrome, hairline only ─────────────────────────────── */

.hd-06__bar {
  position: sticky;
  top: 0;
  z-index: 30;
  background: color-mix(in srgb, var(--paper) 94%, transparent);
  backdrop-filter: blur(8px);
}

.hd-06__bar-in {
  display: flex;
  align-items: center;
  gap: clamp(1rem,4vw,2.5rem);
  max-inline-size: 64rem;
  margin-inline: auto;
  padding: 1.1rem clamp(1.25rem,5vw,2.5rem);
  border-bottom: 1px solid var(--rule);
}

.hd-06__brand {
  font-family: var(--font-display);
  font-size: 1.28rem;
  font-weight: 600;
  letter-spacing: -.02em;
  color: var(--ink);
  text-decoration: none;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-06__nav {
  min-inline-size: 0;
}

.hd-06__nav ul {
  display: flex;
  gap: clamp(.9rem,3vw,1.75rem);
}

.hd-06__nav a {
  color: var(--muted);
  text-decoration: none;
  font-size: .72rem;
  font-weight: 660;
  letter-spacing: .14em;
  text-transform: uppercase;
  white-space: nowrap;
  padding-block: .4rem;
  transition: color .16s ease;
}

.hd-06__nav a:hover {
  color: var(--accent);
}

.hd-06__sub {
  margin-inline-start: auto;
  padding: .5rem .9rem;
  border: 1px solid var(--ink);
  color: var(--ink);
  text-decoration: none;
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  white-space: nowrap;
  transition: background-color .18s ease, color .18s ease;
}

.hd-06__sub:hover {
  background: var(--ink);
  color: var(--paper);
}

.hd-06__meter {
  block-size: var(--meter-h);
  background: var(--accent-soft);
  overflow: hidden;
}

.hd-06__meter-fill {
  display: block;
  block-size: 100%;
  inline-size: 100%;
  background: var(--accent);
  transform-origin: left center;
  scale: 1 1;
  /* fallback: full hairline rule */
}

@supports (animation-timeline: scroll()) {
  .hd-06__meter-fill {
    animation: hd-06-read linear both;
    animation-timeline: scroll(root);
    animation-range: normal;
  }

  @keyframes hd-06-read {
    from {
      scale: 0 1;
    }

    to {
      scale: 1 1;
    }
  }
}
/* ── article ──────────────────────────────────────────────────────── */

.hd-06__main {
  padding: clamp(2.5rem,7vw,4.5rem) clamp(1.25rem,5vw,2.5rem) 5rem;
}

.hd-06__article {
  max-inline-size: 40rem;
  margin-inline: auto;
}

.hd-06__kicker {
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--accent);
}

.hd-06__article h1 {
  font-family: var(--font-display);
  font-size: clamp(2.1rem,6.5vw,3.5rem);
  line-height: 1.08;
  letter-spacing: -.025em;
  font-weight: 600;
  margin-top: .9rem;
  text-wrap: balance;
}

.hd-06__standfirst {
  font-family: var(--font-display);
  font-size: clamp(1.1rem,3vw,1.4rem);
  line-height: 1.45;
  color: var(--muted);
  margin-top: 1rem;
  text-wrap: pretty;
}

.hd-06__byline {
  display: flex;
  align-items: center;
  gap: .7rem;
  margin-top: 1.75rem;
  padding-block: 1rem;
  border-block: 1px solid var(--rule);
}

.hd-06__av {
  display: grid;
  place-items: center;
  inline-size: var(--av);
  block-size: var(--av);
  flex: none;
  border-radius: 50%;
  background: var(--ink);
  color: var(--paper);
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .02em;
}

.hd-06__by-t {
  display: grid;
  min-inline-size: 0;
}

.hd-06__by-n {
  font-weight: 660;
  font-size: .92rem;
}

.hd-06__by-m {
  font-size: .8rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.hd-06__figure {
  margin: 2rem 0;
}

.hd-06__figure img {
  inline-size: 100%;
  block-size: auto;
  aspect-ratio: 16/9;
  object-fit: cover;
  display: block;
  background: linear-gradient(135deg,#d9d3c8,#b9b2a5);
}

.hd-06__figure figcaption {
  margin-top: .6rem;
  font-size: .8rem;
  color: var(--muted);
  text-wrap: pretty;
}

.hd-06__article h2 {
  font-family: var(--font-display);
  font-size: clamp(1.3rem,3.6vw,1.75rem);
  letter-spacing: -.02em;
  font-weight: 600;
  margin: 2.2rem 0 .6rem;
}

.hd-06__article p {
  font-size: 1.06rem;
  line-height: 1.72;
  max-inline-size: 65ch;
  text-wrap: pretty;
}

.hd-06__article p + p {
  margin-top: 1.1rem;
}

.hd-06__article blockquote {
  margin: 1.8rem 0;
  padding-inline-start: 1.25rem;
  border-inline-start: 3px solid var(--accent);
  font-family: var(--font-display);
  font-size: clamp(1.15rem,3vw,1.45rem);
  line-height: 1.4;
  text-wrap: pretty;
}

@media (max-width: 640px) {
  .hd-06__nav {
    display: none;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-06:has(#hd-06-dark:checked) {
  --paper: #141210;
  --ink: #f4efe6;
  --muted: #a49a8b;
  --rule: rgba(244,239,230,.16);
  --accent: #f4795f;
  --accent-soft: rgba(244,121,95,.14);
}

.hd-06:has(#hd-06-dark:checked) .hd-06__figure img {
  background: linear-gradient(135deg,#2a2620,#1b1815);
}
/* icon: shows the scheme the toggle will switch you to */

.hd-06__sun {
  display: none;
}

.hd-06:has(#hd-06-dark:checked) .hd-06__moon {
  display: none;
}

.hd-06:has(#hd-06-dark:checked) .hd-06__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .hd-06:not([data-theme="light"]):not(:has(#hd-06-dark:checked)) {
    --paper: #141210;
    --ink: #f4efe6;
    --muted: #a49a8b;
    --rule: rgba(244,239,230,.16);
    --accent: #f4795f;
    --accent-soft: rgba(244,121,95,.14);
  }

  .hd-06:not([data-theme="light"]):not(:has(#hd-06-dark:checked)) .hd-06__figure img {
    background: linear-gradient(135deg,#2a2620,#1b1815);
  }
  /* FLIP-BACK — dark OS + checked toggle returns to the other scheme */

  .hd-06:has(#hd-06-dark:checked) {
    --paper: #fbf9f5;
    --ink: #16130f;
    --muted: #6d655a;
    --rule: rgba(22,19,15,.16);
    --accent: #b4232a;
    --accent-soft: rgba(180,35,42,.09);
    --meter-h: 3px;
    --av: 2.35rem;
    --font-display: "Newsreader",Georgia,"Iowan Old Style","Times New Roman",serif;
    --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  }

  .hd-06:has(#hd-06-dark:checked) .hd-06__figure img {
    inline-size: 100%;
    block-size: auto;
    aspect-ratio: 16/9;
    object-fit: cover;
    display: block;
    background: linear-gradient(135deg,#d9d3c8,#b9b2a5);
  }
  /* the icon always offers the scheme you are not in */

  .hd-06:not([data-theme="light"]):not(:has(#hd-06-dark:checked)) .hd-06__moon {
    display: none;
  }

  .hd-06:not([data-theme="light"]):not(:has(#hd-06-dark:checked)) .hd-06__sun {
    display: block;
  }

  .hd-06:has(#hd-06-dark:checked) .hd-06__sun {
    display: none;
  }

  .hd-06:has(#hd-06-dark:checked) .hd-06__moon {
    display: block;
  }
}

.hd-06[data-theme="dark"] {
  --paper: #141210;
  --ink: #f4efe6;
  --muted: #a49a8b;
  --rule: rgba(244,239,230,.16);
  --accent: #f4795f;
  --accent-soft: rgba(244,121,95,.14);
}

@media (prefers-reduced-motion: reduce) {
  .hd-06__meter-fill {
    animation: none !important;
    scale: 1 1 !important;
  }

  .hd-06 * {
    transition-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-06__meter-fill {
    background: Highlight;
  }
}
/* ── theme toggle — visually hidden checkbox, zero JS ────────────── */

.hd-06__sr,
.hd-06__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-06__theme {
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

.hd-06__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-06__theme:hover {
  background: rgba(128,128,128,.16);
}

.hd-06:has(#hd-06-dark:focus-visible) .hd-06__theme {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```
