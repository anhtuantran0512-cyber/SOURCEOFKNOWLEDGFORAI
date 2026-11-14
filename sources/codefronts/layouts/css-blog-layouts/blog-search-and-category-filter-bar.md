---
source: "codefronts"
url: "https://codefronts.com/layouts/css-blog-layouts/blog-search-and-category-filter-bar/"
title: "Blog Search and Category Filter Bar"
section: "layouts"
category: "css-blog-layouts"
category_name: "CSS Blog Layouts"
description: "A filter bar that survives real use: a search field with a clear button, a horizontally scrolling chip strip with scroll-snap and edge fade masks, live…"
has_js: "true"
---

Here's a working CSS Blog Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Blog Search and Category Filter Bar
Source: https://codefronts.com/layouts/css-blog-layouts/blog-search-and-category-filter-bar/

A filter bar that survives real use: a search field with a clear button, a horizontally scrolling chip strip with scroll-snap and edge fade masks, live result counts, and an empty state. Filtering is fifteen lines of vanilla JS over the DOM, announced politely to screen readers — the accessibility half every filter UI skips.
## HTML
```html
<div class="bl-18">
  <div class="bl-18__stage">
    <header class="bl-18__head">
      <h1>Browse the archive</h1>
      <p>142 posts on CSS, systems and the parts of the job nobody demos.</p>
    </header>

    <div class="bl-18__bar">
      <div class="bl-18__searchRow">
        <label class="bl-18__search">
          <span class="bl-18__srOnly">Search posts</span>
          <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="9" cy="9" r="5.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="m13.2 13.2 3.2 3.2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
          <input type="text" data-q placeholder="Search titles, tags, authors…" autocomplete="off">
          <button class="bl-18__clear" type="button" data-clear aria-label="Clear search">
            <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="m6.5 6.5 7 7m0-7-7 7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          </button>
        </label>
        <p class="bl-18__count" role="status" aria-live="polite" data-count>Showing 6 of 6 posts</p>
      </div>

      <div class="bl-18__chipsWrap">
        <div class="bl-18__chips" role="group" aria-label="Filter by category">
          <button class="bl-18__chip" type="button" data-tag="all" aria-pressed="true">All</button>
          <button class="bl-18__chip" type="button" data-tag="css" aria-pressed="false">CSS <i>38</i></button>
          <button class="bl-18__chip" type="button" data-tag="a11y" aria-pressed="false">Accessibility <i>21</i></button>
          <button class="bl-18__chip" type="button" data-tag="systems" aria-pressed="false">Design systems <i>17</i></button>
          <button class="bl-18__chip" type="button" data-tag="perf" aria-pressed="false">Performance <i>14</i></button>
          <button class="bl-18__chip" type="button" data-tag="process" aria-pressed="false">Process <i>26</i></button>
          <button class="bl-18__chip" type="button" data-tag="tooling" aria-pressed="false">Tooling <i>19</i></button>
          <button class="bl-18__chip" type="button" data-tag="typography" aria-pressed="false">Typography <i>7</i></button>
        </div>
      </div>
    </div>

    <ol class="bl-18__results" data-results>
      <li class="bl-18__post" data-tags="css typography" data-search="the case for fluid type scales clamp css typography rhea nandi">
        <p class="bl-18__cats"><span>CSS</span><span>Typography</span></p>
        <h2><a href="#">The case for fluid type scales that stop scaling</a></h2>
        <p class="bl-18__ex">Clamp is not a licence for infinite growth. Where to cap, and how to test it at 400% zoom.</p>
        <p class="bl-18__meta">Rhea Nandi · <time datetime="2026-08-04">4 Aug</time> · 7 min</p>
      </li>
      <li class="bl-18__post" data-tags="a11y process" data-search="accessibility audits that engineers actually fix marcus hale">
        <p class="bl-18__cats"><span>Accessibility</span><span>Process</span></p>
        <h2><a href="#">Accessibility audits that engineers actually fix</a></h2>
        <p class="bl-18__ex">Forty findings nobody reads versus six with reproduction steps. Guess which shipped.</p>
        <p class="bl-18__meta">Marcus Hale · <time datetime="2026-07-29">29 Jul</time> · 11 min</p>
      </li>
      <li class="bl-18__post" data-tags="systems tooling" data-search="deleting components a maintenance story design systems june park">
        <p class="bl-18__cats"><span>Design systems</span><span>Tooling</span></p>
        <h2><a href="#">Deleting components: a maintenance story</a></h2>
        <p class="bl-18__ex">We removed 41 components in a quarter. The hard part was proving nobody used them.</p>
        <p class="bl-18__meta">June Park · <time datetime="2026-07-21">21 Jul</time> · 9 min</p>
      </li>
      <li class="bl-18__post" data-tags="perf css" data-search="the layout shift you cannot see cls performance aspect ratio dev okoro">
        <p class="bl-18__cats"><span>Performance</span><span>CSS</span></p>
        <h2><a href="#">The layout shift you cannot see</a></h2>
        <p class="bl-18__ex">CLS below the fold still counts. Three sources of it that no lab tool reports.</p>
        <p class="bl-18__meta">Dev Okoro · <time datetime="2026-07-14">14 Jul</time> · 6 min</p>
      </li>
      <li class="bl-18__post" data-tags="css a11y" data-search="focus visible is not a nice to have keyboard css lena ostrowski">
        <p class="bl-18__cats"><span>CSS</span><span>Accessibility</span></p>
        <h2><a href="#">:focus-visible is not a nice-to-have</a></h2>
        <p class="bl-18__ex">A short, opinionated guide to focus styles that pass contrast and don't look bolted on.</p>
        <p class="bl-18__meta">Lena Ostrowski · <time datetime="2026-07-08">8 Jul</time> · 5 min</p>
      </li>
      <li class="bl-18__post" data-tags="process systems" data-search="the design review we stopped running process tomas ferreira">
        <p class="bl-18__cats"><span>Process</span><span>Design systems</span></p>
        <h2><a href="#">The design review we stopped running</a></h2>
        <p class="bl-18__ex">Weekly critique replaced by two async checkpoints, measured over a year.</p>
        <p class="bl-18__meta">Tomás Ferreira · <time datetime="2026-06-30">30 Jun</time> · 8 min</p>
      </li>
    </ol>

    <p class="bl-18__empty">No posts match that. <button type="button" data-reset>Clear all filters</button></p>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&family=Newsreader:opsz,[email protected],400&display=swap');

.bl-18 {
  --bg: #fbfbfc;
  --surface: #ffffff;
  --text: #101114;
  --muted: #61656e;
  --line: #e4e6ea;
  --acc: #0f766e;
  --acc-fg: #ffffff;
  --sans: "Instrument Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --serif: "Newsreader",ui-serif,Georgia,serif;
}

@supports (color: oklch(50% 0 0)) {
  .bl-18 {
    --bg: oklch(98.5% .003 270);
    --surface: oklch(100% 0 0);
    --text: oklch(16% .008 270);
    --muted: oklch(50% .014 268);
    --line: oklch(91% .006 268);
    --acc: oklch(48% .11 180);
  }
}

@media (prefers-color-scheme: dark) {
  .bl-18:not([data-theme="light"]) {
    --bg: #0a0b0d;
    --surface: #14161a;
    --text: #eff1f4;
    --muted: #99a0aa;
    --line: #23262c;
    --acc: #5eead4;
    --acc-fg: #07120f;
  }
}

.bl-18[data-theme="dark"] {
  --bg: #0a0b0d;
  --surface: #14161a;
  --text: #eff1f4;
  --muted: #99a0aa;
  --line: #23262c;
  --acc: #5eead4;
  --acc-fg: #07120f;
}

.bl-18 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.bl-18,
.bl-18 *,
.bl-18 *::before,
.bl-18 *::after {
  box-sizing: border-box;
}

.bl-18 a {
  color: inherit;
  text-decoration: none;
}

.bl-18 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
  border-radius: 4px;
}

.bl-18__srOnly {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.bl-18__stage {
  max-width: 58rem;
  margin-inline: auto;
  padding: clamp(2rem,6vw,4.5rem) clamp(1.25rem,4vw,2.5rem) clamp(3rem,7vw,5rem);
  display: grid;
  gap: 1.5rem;
}
/* Grid items default to min-width:auto ("at least my content width"), which
   lets the horizontally-scrolling chip strip force the whole column open.
   min-width:0 is what allows an overflow-x scroller to actually shrink. */

.bl-18__stage > * {
  min-width: 0;
}

.bl-18__chipsWrap {
  min-width: 0;
}

.bl-18__searchRow {
  min-width: 0;
}

.bl-18__head {
  display: grid;
  gap: .5rem;
}

.bl-18__head h1 {
  margin: 0;
  font-size: clamp(1.75rem,4.5vw,2.75rem);
  font-weight: 700;
  line-height: 1.05;
  letter-spacing: -.035em;
}

.bl-18__head p {
  margin: 0;
  font-family: var(--serif);
  font-size: 1.0625rem;
  color: var(--muted);
  text-wrap: pretty;
}

.bl-18__bar {
  position: sticky;
  top: 0;
  z-index: 4;
  display: grid;
  gap: .85rem;
  padding: .85rem 0 .75rem;
  background: color-mix(in oklab,var(--bg) 90%,transparent);
}

@supports (backdrop-filter: blur(6px)) {
  .bl-18__bar {
    backdrop-filter: blur(14px);
  }
}

.bl-18__searchRow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .75rem 1rem;
}

.bl-18__search {
  flex: 1 1 18rem;
  display: flex;
  align-items: center;
  gap: .6rem;
  min-height: 3rem;
  padding: 0 .35rem 0 .9rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 999px;
  color: var(--muted);
  transition: border-color .18s ease, box-shadow .18s ease;
}

.bl-18__search:focus-within {
  border-color: var(--acc);
  box-shadow: 0 0 0 3px color-mix(in oklab,var(--acc) 18%,transparent);
}

.bl-18__search svg {
  width: 1.05rem;
  height: 1.05rem;
  flex: 0 0 auto;
}

.bl-18__search input {
  flex: 1 1 auto;
  min-width: 0;
  border: 0;
  background: transparent;
  color: var(--text);
  font: inherit;
  font-size: .9375rem;
  outline: 0;
}

.bl-18__search input::placeholder {
  color: color-mix(in oklab,var(--muted) 80%,transparent);
}

.bl-18__clear {
  width: 2.25rem;
  height: 2.25rem;
  flex: 0 0 auto;
  display: grid;
  place-items: center;
  cursor: pointer;
  border: 0;
  border-radius: 50%;
  background: transparent;
  color: var(--muted);
  opacity: 0;
  pointer-events: none;
  transition: opacity .18s ease, background .18s ease;
}

.bl-18__clear svg {
  width: 1rem;
  height: 1rem;
}

.bl-18__search:has(input:not(:placeholder-shown)) .bl-18__clear {
  opacity: 1;
  pointer-events: auto;
}

.bl-18__clear:hover {
  background: color-mix(in oklab,var(--text) 8%,transparent);
  color: var(--text);
}

.bl-18__count {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.bl-18__chipsWrap {
  position: relative;
}

.bl-18__chips {
  display: flex;
  gap: .45rem;
  overflow-x: auto;
  padding-bottom: .25rem;
  scroll-snap-type: x proximity;
  scrollbar-width: none;
  -ms-overflow-style: none;
  mask-image: linear-gradient(90deg,transparent,#000 1rem,#000 calc(100% - 2.5rem),transparent);
}

.bl-18__chips::-webkit-scrollbar {
  display: none;
}

.bl-18__chip {
  flex: 0 0 auto;
  scroll-snap-align: start;
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 2.5rem;
  padding: 0 .9rem;
  cursor: pointer;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--surface);
  color: var(--muted);
  font: inherit;
  font-size: .8125rem;
  font-weight: 500;
  white-space: nowrap;
  transition: background .18s ease, border-color .18s ease, color .18s ease;
}

.bl-18__chip i {
  font-style: normal;
  font-size: .6875rem;
  opacity: .6;
  font-variant-numeric: tabular-nums;
}

.bl-18__chip:hover {
  border-color: var(--acc);
  color: var(--text);
}

.bl-18__chip[aria-pressed="true"] {
  background: var(--acc);
  border-color: var(--acc);
  color: var(--acc-fg);
  font-weight: 600;
}

.bl-18__chip[aria-pressed="true"] i {
  opacity: .8;
}

.bl-18__results {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .75rem;
}

.bl-18__post {
  display: grid;
  gap: .4rem;
  padding: clamp(1rem,2.5vw,1.35rem);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1rem;
  transition: border-color .2s ease, translate .25s cubic-bezier(.16,1,.3,1);
}

.bl-18__post:hover {
  border-color: color-mix(in oklab,var(--acc) 40%,var(--line));
  translate: 0 -2px;
}

.bl-18__cats {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .35rem;
}

.bl-18__cats span {
  font-size: .5625rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--acc);
  padding: .2rem .4rem;
  border-radius: .25rem;
  background: color-mix(in oklab,var(--acc) 10%,transparent);
}

.bl-18__post h2 {
  margin: 0;
  font-size: clamp(1.0625rem,2.2vw,1.3125rem);
  font-weight: 600;
  line-height: 1.2;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.bl-18__post h2 a {
  background: linear-gradient(currentColor,currentColor) 0 100%/0 1px no-repeat;
  transition: background-size .35s cubic-bezier(.16,1,.3,1);
}

.bl-18__post h2 a:hover {
  background-size: 100% 1px;
}

.bl-18__ex {
  margin: 0;
  font-family: var(--serif);
  font-size: .9375rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.bl-18__meta {
  margin: .1rem 0 0;
  font-size: .75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.bl-18__empty {
  display: none;
  margin: 0;
  padding: 2.5rem 1.25rem;
  text-align: center;
  border: 1px dashed var(--line);
  border-radius: 1rem;
  font-size: .9375rem;
  color: var(--muted);
}

.bl-18__empty button {
  margin-inline-start: .35rem;
  border: 0;
  background: none;
  padding: 0;
  cursor: pointer;
  color: var(--acc);
  font: inherit;
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: .2em;
}

.bl-18__stage:has([data-results] > li:not([hidden])) .bl-18__empty {
  display: none;
}

.bl-18__stage:not(:has([data-results] > li:not([hidden]))) .bl-18__empty {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .bl-18 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .bl-18__chip[aria-pressed="true"] {
    forced-color-adjust: none;
    background: Highlight;
    color: HighlightText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.bl-18');
  if (!root) return;
  const q = root.querySelector('[data-q]');
  const chips = [...root.querySelectorAll('.bl-18__chip')];
  const posts = [...root.querySelectorAll('[data-results] > li')];
  const count = root.querySelector('[data-count]');
  const active = () => chips.filter((c) => c.getAttribute('aria-pressed') === 'true' && c.dataset.tag !== 'all').map((c) => c.dataset.tag);
  const apply = () => {
    const text = q.value.trim().toLowerCase();
    const tags = active();
    let shown = 0;
    posts.forEach((p) => {
      const okText = !text || p.dataset.search.includes(text);
      const okTags = !tags.length || tags.some((t) => p.dataset.tags.split(' ').includes(t));
      p.hidden = !(okText && okTags);
      if (!p.hidden) shown++;
    });
    count.textContent = 'Showing ' + shown + ' of ' + posts.length + ' posts';
  };
  chips.forEach((chip) => chip.addEventListener('click', () => {
    if (chip.dataset.tag === 'all') chips.forEach((c) => c.setAttribute('aria-pressed', String(c === chip)));
    else {
      chip.setAttribute('aria-pressed', String(chip.getAttribute('aria-pressed') !== 'true'));
      chips[0].setAttribute('aria-pressed', String(!active().length));
    }
    apply();
  }));
  q.addEventListener('input', apply);
  root.querySelector('[data-clear]').addEventListener('click', () => { q.value = ''; q.focus(); apply(); });
  root.querySelector('[data-reset]').addEventListener('click', () => {
    q.value = ''; chips.forEach((c, i) => c.setAttribute('aria-pressed', String(i === 0))); apply(); q.focus();
  });
  apply();
})();
```
