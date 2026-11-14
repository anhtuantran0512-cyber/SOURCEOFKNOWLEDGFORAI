---
source: "codefronts"
url: "https://codefronts.com/layouts/css-blog-layouts/documentation-article-chapter-nav/"
title: "Documentation Article Chapter Nav"
section: "layouts"
category: "css-blog-layouts"
category_name: "CSS Blog Layouts"
description: "A three-column docs page done right: collapsible section nav on the left (native <details>, no JS), the article in the middle at a 72ch measure, an “on this…"
has_js: "false"
---

Here's a working CSS Blog Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Documentation Article Chapter Nav
Source: https://codefronts.com/layouts/css-blog-layouts/documentation-article-chapter-nav/

A three-column docs page done right: collapsible section nav on the left (native <details>, no JS), the article in the middle at a 72ch measure, an “on this page” rail on the right, and prev/next chapter cards at the foot that show where you are going, not just an arrow. Includes the details every docs site forgets — a version badge, a copy-anchor affordance on headings, and a note/warning callout system.
## HTML
```html
<div class="bl-16">
  <header class="bl-16__top">
    <a class="bl-16__brand" href="#">Ember<span>docs</span></a>
    <p class="bl-16__version" data-v="stable">v4.2 · stable</p>
    <label class="bl-16__search"><span class="bl-16__srOnly">Search documentation</span><svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="9" cy="9" r="5.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="m13.2 13.2 3 3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><input type="search" placeholder="Search docs  ⌘K"></label>
  </header>

  <div class="bl-16__shell">
    <nav class="bl-16__side" aria-label="Documentation">
      <details open>
        <summary>Getting started</summary>
        <ul>
          <li><a href="#">Installation</a></li>
          <li><a href="#">Project structure</a></li>
          <li><a href="#">Your first component</a></li>
        </ul>
      </details>
      <details open>
        <summary>Core concepts</summary>
        <ul>
          <li><a href="#">Rendering model</a></li>
          <li><a href="#">State and effects</a></li>
          <li><a href="#" aria-current="page">Data loading</a></li>
          <li><a href="#">Error boundaries</a></li>
        </ul>
      </details>
      <details>
        <summary>Routing</summary>
        <ul>
          <li><a href="#">File conventions</a></li>
          <li><a href="#">Nested layouts</a></li>
          <li><a href="#">Redirects</a></li>
        </ul>
      </details>
      <details>
        <summary>Deployment</summary>
        <ul>
          <li><a href="#">Build output</a></li>
          <li><a href="#">Edge runtime</a></li>
          <li><a href="#">Caching</a></li>
        </ul>
      </details>
    </nav>

    <article class="bl-16__body">
      <p class="bl-16__crumbs"><a href="#">Docs</a> <span aria-hidden="true">›</span> <a href="#">Core concepts</a> <span aria-hidden="true">›</span> Data loading</p>
      <h1>Data loading</h1>
      <p class="bl-16__lede">Ember loads data on the server by default and streams the result. This page covers the three loading strategies, when each one applies, and how to opt out.</p>

      <div class="bl-16__callout" data-kind="note">
        <p><strong>Note</strong> — This page describes the v4 data layer. If you are on v3, <a href="#">the legacy loader guide</a> still applies until April 2027.</p>
      </div>

      <h2 id="bl-16-h1">Server loaders <a href="#bl-16-h1" aria-label="Link to this section">#</a></h2>
      <p>A loader is an exported async function that runs on the server before the component renders. It receives the request and returns serialisable data; the framework handles caching, revalidation and streaming.</p>
      <pre class="bl-16__code"><code><span>export async function load(&#123; params &#125;) &#123;</span><span>  const post = await db.post.find(params.slug);</span><span>  if (!post) throw new NotFound();</span><span>  return &#123; post, revalidate: 60 &#125;;</span><span>&#125;</span></code></pre>
      <p>Returning <code>revalidate</code> opts the route into time-based revalidation. Omit it and the response is cached until the next deploy.</p>

      <h2 id="bl-16-h2">Client fetches <a href="#bl-16-h2" aria-label="Link to this section">#</a></h2>
      <p>Use a client fetch only for data that is user-specific and not cacheable — a notification count, a draft autosave. Everything else belongs in a loader, where it costs one round trip instead of two.</p>
      <div class="bl-16__callout" data-kind="warn">
        <p><strong>Careful</strong> — Client fetches inside a component that also has a loader will run on every hydration. Move them into an event handler or an effect with a dependency array.</p>
      </div>

      <h2 id="bl-16-h3">Streaming and suspense boundaries <a href="#bl-16-h3" aria-label="Link to this section">#</a></h2>
      <p>Wrap slow segments in a boundary and the rest of the page ships immediately. The boundary's fallback should reserve the final layout's space — a skeleton with the same <code>aspect-ratio</code>, not a spinner — or you trade a blank screen for a layout shift.</p>
      <table class="bl-16__table">
        <caption>Choosing a strategy</caption>
        <thead><tr><th scope="col">Data</th><th scope="col">Strategy</th><th scope="col">Cache</th></tr></thead>
        <tbody>
          <tr><th scope="row">Public, shared</th><td>Server loader</td><td>Until deploy</td></tr>
          <tr><th scope="row">Public, changing</th><td>Loader + revalidate</td><td>n seconds</td></tr>
          <tr><th scope="row">Per-user</th><td>Client fetch</td><td>None</td></tr>
        </tbody>
      </table>
      <div class="bl-16__callout" data-kind="tip">
        <p><strong>Tip</strong> — Run <code>ember analyse --loaders</code> to list every route's loader latency at p95. Anything above 400ms is a boundary candidate.</p>
      </div>

      <nav class="bl-16__chapters" aria-label="Chapter navigation">
        <a class="bl-16__chapter" href="#" rel="prev">
          <span>← Previous</span><strong>State and effects</strong><i>Core concepts · 4 of 9</i>
        </a>
        <a class="bl-16__chapter" href="#" rel="next">
          <span>Next →</span><strong>Error boundaries</strong><i>Core concepts · 6 of 9</i>
        </a>
      </nav>

      <footer class="bl-16__editRow">
        <p>Last updated <time datetime="2026-07-27">27 July 2026</time></p>
        <a href="#">Edit this page on GitHub</a>
      </footer>
    </article>

    <nav class="bl-16__toc" aria-label="On this page">
      <p class="bl-16__tocHead">On this page</p>
      <ol>
        <li><a href="#bl-16-h1" aria-current="location">Server loaders</a></li>
        <li><a href="#bl-16-h2">Client fetches</a></li>
        <li><a href="#bl-16-h3">Streaming and suspense boundaries</a></li>
      </ol>
      <div class="bl-16__help">
        <p>Was this page helpful?</p>
        <div><button type="button" aria-pressed="false">Yes</button><button type="button" aria-pressed="false">No</button></div>
      </div>
    </nav>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

.bl-16 {
  --bg: #ffffff;
  --surface: #f7f8fa;
  --code-bg: #101418;
  --code-fg: #dce3ea;
  --text: #111418;
  --muted: #5d646c;
  --line: #e4e7eb;
  --acc: #5b21b6;
  --note: #2563eb;
  --warn: #b45309;
  --tip: #15803d;
  --sans: "IBM Plex Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
}

@supports (color: oklch(50% 0 0)) {
  .bl-16 {
    --bg: oklch(100% 0 0);
    --surface: oklch(97.5% .004 250);
    --text: oklch(17% .01 250);
    --muted: oklch(49% .012 250);
    --line: oklch(91% .006 250);
    --acc: oklch(42% .2 295);
    --note: oklch(52% .19 260);
    --warn: oklch(55% .14 65);
    --tip: oklch(50% .14 148);
  }
}

@media (prefers-color-scheme: dark) {
  .bl-16:not([data-theme="light"]) {
    --bg: #0b0d10;
    --surface: #13171c;
    --text: #eceff2;
    --muted: #98a1aa;
    --line: #222831;
    --acc: #c4a6ff;
    --code-bg: #080a0c;
    --note: #7ea6ff;
    --warn: #fbbf24;
    --tip: #5cd68f;
  }
}

.bl-16[data-theme="dark"] {
  --bg: #0b0d10;
  --surface: #13171c;
  --text: #eceff2;
  --muted: #98a1aa;
  --line: #222831;
  --acc: #c4a6ff;
  --code-bg: #080a0c;
  --note: #7ea6ff;
  --warn: #fbbf24;
  --tip: #5cd68f;
}

.bl-16 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.bl-16,
.bl-16 *,
.bl-16 *::before,
.bl-16 *::after {
  box-sizing: border-box;
}

.bl-16 a {
  color: inherit;
  text-decoration: none;
}

.bl-16 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
  border-radius: 3px;
}

.bl-16__srOnly {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.bl-16__top {
  position: sticky;
  top: 0;
  z-index: 8;
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: .75rem clamp(1rem,3vw,2rem);
  border-bottom: 1px solid var(--line);
  background: color-mix(in oklab,var(--bg) 90%,transparent);
}

@supports (backdrop-filter: blur(6px)) {
  .bl-16__top {
    backdrop-filter: blur(12px);
  }
}

.bl-16__brand {
  font-size: 1.0625rem;
  font-weight: 700;
  letter-spacing: -.03em;
}

.bl-16__brand span {
  color: var(--acc);
}

.bl-16__version {
  margin: 0;
  padding: .25rem .5rem;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: var(--surface);
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.bl-16__version[data-v="stable"] {
  color: var(--tip);
  border-color: color-mix(in oklab,var(--tip) 40%,transparent);
}

.bl-16__search {
  margin-inline-start: auto;
  display: flex;
  align-items: center;
  gap: .5rem;
  min-height: 2.5rem;
  padding: 0 .75rem;
  border: 1px solid var(--line);
  border-radius: .5rem;
  background: var(--surface);
  color: var(--muted);
  max-width: min(22rem,42vw);
  width: 100%;
}

.bl-16__search svg {
  width: 1rem;
  height: 1rem;
  flex: 0 0 auto;
}

.bl-16__search input {
  border: 0;
  background: transparent;
  color: var(--text);
  font: inherit;
  font-size: .875rem;
  width: 100%;
  min-width: 0;
  outline: 0;
}

.bl-16__shell {
  display: grid;
  grid-template-columns: 16rem minmax(0,1fr) 14rem;
  gap: clamp(1.5rem,3vw,3rem);
  max-width: 92rem;
  margin-inline: auto;
  padding: clamp(1.5rem,3vw,2.5rem) clamp(1rem,3vw,2rem) clamp(4rem,7vw,6rem);
  align-items: start;
}

.bl-16__side {
  position: sticky;
  top: 4.5rem;
  align-self: start;
  max-height: calc(100svh - 6rem);
  overflow: auto;
  scrollbar-width: thin;
  display: grid;
  gap: .35rem;
  padding-inline-end: .5rem;
}

.bl-16__side details {
  border-radius: .5rem;
}

.bl-16__side summary {
  display: flex;
  align-items: center;
  gap: .5rem;
  min-height: 2.5rem;
  padding: 0 .6rem;
  cursor: pointer;
  list-style: none;
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.bl-16__side summary::-webkit-details-marker {
  display: none;
}

.bl-16__side summary::before {
  content: "›";
  display: inline-block;
  font-size: 1rem;
  transition: rotate .2s ease;
  color: var(--acc);
}

.bl-16__side details[open] summary::before {
  rotate: 90deg;
}

.bl-16__side summary:hover {
  color: var(--text);
}

.bl-16__side ul {
  margin: .15rem 0 .5rem;
  padding: 0 0 0 1.1rem;
  list-style: none;
  display: grid;
  border-inline-start: 1px solid var(--line);
}

.bl-16__side li a {
  display: flex;
  align-items: center;
  min-height: 2.25rem;
  padding: 0 .6rem;
  border-radius: .375rem;
  font-size: .875rem;
  color: var(--muted);
}

.bl-16__side li a:hover {
  color: var(--text);
  background: var(--surface);
}

.bl-16__side li a[aria-current="page"] {
  color: var(--acc);
  background: color-mix(in oklab,var(--acc) 10%,transparent);
  font-weight: 600;
}

.bl-16__body {
  min-width: 0;
  display: grid;
  gap: 1.1rem;
  max-width: 72ch;
}

.bl-16__crumbs {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
}

.bl-16__crumbs a {
  color: var(--acc);
}

.bl-16__crumbs a:hover {
  text-decoration: underline;
  text-underline-offset: .2em;
}

.bl-16__body h1 {
  margin: 0;
  font-size: clamp(1.875rem,4vw,2.75rem);
  font-weight: 700;
  line-height: 1.08;
  letter-spacing: -.035em;
  text-wrap: balance;
}

.bl-16__lede {
  margin: 0;
  font-size: 1.125rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.bl-16__body h2 {
  margin: 1.25rem 0 0;
  font-size: 1.375rem;
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -.025em;
  scroll-margin-block-start: 5.5rem;
  display: flex;
  align-items: baseline;
  gap: .5rem;
}

.bl-16__body h2 a {
  color: var(--acc);
  font-weight: 400;
  opacity: 0;
  transition: opacity .18s ease;
}

.bl-16__body h2:hover a,
.bl-16__body h2 a:focus-visible {
  opacity: 1;
}

.bl-16__body p {
  margin: 0;
  font-size: 1rem;
  line-height: 1.72;
  text-wrap: pretty;
}

.bl-16__body code {
  font-family: var(--mono);
  font-size: .85em;
  padding: .12em .35em;
  border-radius: .25rem;
  background: color-mix(in oklab,var(--acc) 12%,transparent);
}

.bl-16__code {
  margin: 0;
  padding: 1rem 1.1rem;
  border-radius: .75rem;
  background: var(--code-bg);
  color: var(--code-fg);
  overflow-x: auto;
  border: 1px solid var(--line);
}

.bl-16__code code {
  display: grid;
  counter-reset: bl-16-l;
  background: none;
  padding: 0;
  font-family: var(--mono);
  font-size: .8125rem;
  line-height: 1.75;
  color: inherit;
}

.bl-16__code code span {
  counter-increment: bl-16-l;
  display: grid;
  grid-template-columns: 1.75rem minmax(0,1fr);
  white-space: pre;
}

.bl-16__code code span::before {
  content: counter(bl-16-l);
  color: color-mix(in oklab,var(--code-fg) 30%,transparent);
  text-align: end;
  padding-inline-end: .9rem;
  user-select: none;
  font-variant-numeric: tabular-nums;
}

.bl-16__callout {
  padding: .9rem 1.1rem;
  border-radius: .625rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-inline-start: 3px solid var(--note);
}

.bl-16__callout p {
  margin: 0;
  font-size: .9375rem;
  line-height: 1.65;
}

.bl-16__callout strong {
  color: var(--note);
  font-weight: 700;
}

.bl-16__callout a {
  color: var(--acc);
  text-decoration: underline;
  text-underline-offset: .2em;
}

.bl-16__callout[data-kind="warn"] {
  border-inline-start-color: var(--warn);
}

.bl-16__callout[data-kind="warn"] strong {
  color: var(--warn);
}

.bl-16__callout[data-kind="tip"] {
  border-inline-start-color: var(--tip);
}

.bl-16__callout[data-kind="tip"] strong {
  color: var(--tip);
}

.bl-16__table {
  width: 100%;
  border-collapse: collapse;
  font-size: .9375rem;
}

.bl-16__table caption {
  text-align: start;
  padding-bottom: .6rem;
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.bl-16__table th,
.bl-16__table td {
  padding: .65rem .5rem;
  text-align: start;
  border-bottom: 1px solid var(--line);
}

.bl-16__table thead th {
  font-size: .6875rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.bl-16__table tbody th {
  font-weight: 600;
}

.bl-16__chapters {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,13rem),1fr));
  gap: .75rem;
  margin-top: 1.5rem;
}

.bl-16__chapter {
  display: grid;
  gap: .25rem;
  padding: 1rem 1.1rem;
  border: 1px solid var(--line);
  border-radius: .75rem;
  transition: border-color .2s ease, background .2s ease, translate .2s cubic-bezier(.16,1,.3,1);
}

.bl-16__chapter:hover {
  border-color: var(--acc);
  background: var(--surface);
  translate: 0 -2px;
}

.bl-16__chapter span {
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--acc);
}

.bl-16__chapter strong {
  font-size: 1.0625rem;
  font-weight: 600;
  letter-spacing: -.02em;
  line-height: 1.25;
  text-wrap: pretty;
}

.bl-16__chapter i {
  font-style: normal;
  font-size: .75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.bl-16__chapter[rel="next"] {
  text-align: end;
}

.bl-16__editRow {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem 1.5rem;
  justify-content: space-between;
  margin-top: 1rem;
  padding-top: 1.25rem;
  border-top: 1px solid var(--line);
  font-size: .8125rem;
  color: var(--muted);
}

.bl-16__editRow p {
  margin: 0;
  font-variant-numeric: tabular-nums;
}

.bl-16__editRow a {
  color: var(--acc);
  text-decoration: underline;
  text-underline-offset: .2em;
}

.bl-16__toc {
  position: sticky;
  top: 4.5rem;
  align-self: start;
  max-height: calc(100svh - 6rem);
  overflow: auto;
  scrollbar-width: thin;
  display: grid;
  gap: 1rem;
}

.bl-16__tocHead {
  margin: 0;
  font-size: .6875rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.bl-16__toc ol {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  border-inline-start: 1px solid var(--line);
}

.bl-16__toc a {
  display: block;
  padding: .45rem .75rem;
  font-size: .8125rem;
  line-height: 1.4;
  color: var(--muted);
  border-inline-start: 2px solid transparent;
  margin-inline-start: -1px;
}

.bl-16__toc a:hover {
  color: var(--text);
}

.bl-16__toc a[aria-current] {
  color: var(--acc);
  border-inline-start-color: var(--acc);
  font-weight: 600;
}

.bl-16__help {
  display: grid;
  gap: .5rem;
  padding-top: 1rem;
  border-top: 1px solid var(--line);
}

.bl-16__help p {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
}

.bl-16__help div {
  display: flex;
  gap: .4rem;
}

.bl-16__help button {
  flex: 1 1 0;
  min-height: 2.5rem;
  border: 1px solid var(--line);
  border-radius: .375rem;
  background: var(--bg);
  color: var(--text);
  font: inherit;
  font-size: .8125rem;
  font-weight: 600;
  cursor: pointer;
  transition: border-color .18s ease, color .18s ease;
}

.bl-16__help button:hover {
  border-color: var(--acc);
  color: var(--acc);
}

@media (max-width: 74rem) {
  .bl-16__shell {
    grid-template-columns: 15rem minmax(0,1fr);
  }

  .bl-16__toc {
    display: none;
  }
}

@media (max-width: 56rem) {
  .bl-16__shell {
    grid-template-columns: minmax(0,1fr);
  }

  .bl-16__side {
    position: static;
    max-height: none;
    overflow: visible;
    padding: 1rem;
    border: 1px solid var(--line);
    border-radius: .75rem;
    background: var(--surface);
  }
}

@media (prefers-reduced-motion: reduce) {
  .bl-16 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .bl-16__side li a[aria-current="page"] {
    forced-color-adjust: none;
    background: Highlight;
    color: HighlightText;
  }
}
```
