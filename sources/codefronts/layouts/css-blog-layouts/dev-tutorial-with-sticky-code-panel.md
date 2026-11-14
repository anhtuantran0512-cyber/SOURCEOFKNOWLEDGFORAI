---
source: "codefronts"
url: "https://codefronts.com/layouts/css-blog-layouts/dev-tutorial-with-sticky-code-panel/"
title: "Dev Tutorial with Sticky Code Panel"
section: "layouts"
category: "css-blog-layouts"
category_name: "CSS Blog Layouts"
description: "The layout every good tutorial converges on: steps scroll on the left, the code stays put on the right."
has_js: "true"
---

Here's a working CSS Blog Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dev Tutorial with Sticky Code Panel
Source: https://codefronts.com/layouts/css-blog-layouts/dev-tutorial-with-sticky-code-panel/

The layout every good tutorial converges on: steps scroll on the left, the code stays put on the right. Tabs between files are pure CSS (:checked + sibling selectors), line numbers are CSS counters, and the only JavaScript is a five-line clipboard copy. The sticky panel becomes a collapsible block on mobile instead of a squashed column.
## HTML
```html
<div class="bl-10">
  <header class="bl-10__head">
    <p class="bl-10__crumbs"><a href="#">Guides</a> <span aria-hidden="true">/</span> <a href="#">CSS</a> <span aria-hidden="true">/</span> Container queries</p>
    <h1>Build a card that responds to its container, not the viewport</h1>
    <p class="bl-10__sub">Four steps, one component, no media queries. Works today in every evergreen browser.</p>
    <ul class="bl-10__facts">
      <li><span>Level</span>Intermediate</li>
      <li><span>Time</span>12 min</li>
      <li><span>Updated</span><time datetime="2026-07-30">30 Jul 2026</time></li>
    </ul>
  </header>

  <div class="bl-10__main">
    <div class="bl-10__steps">
      <section class="bl-10__step">
        <h2>Make the parent a container</h2>
        <p>A container query needs something to query. Declaring <code>container-type: inline-size</code> tells the browser to track this element's inline dimension and makes it a query target for its descendants.</p>
        <p>Use <code>inline-size</code>, not <code>size</code>, unless you genuinely need block-direction queries — <code>size</code> requires the element to have a definite height, which almost never survives real content.</p>
        <p class="bl-10__callout"><strong>Why not a media query?</strong> Because the same card appears in a sidebar, a two-up grid and a full-width hero. The viewport is not the constraint; the slot is.</p>
      </section>

      <section class="bl-10__step">
        <h2>Name the container so queries stay explicit</h2>
        <p><code>container-name</code> is optional but worth the two seconds. Named containers let a descendant target a specific ancestor rather than the nearest one, which matters the moment you nest components.</p>
        <p>The shorthand is <code>container: card / inline-size</code> — name first, then type.</p>
      </section>

      <section class="bl-10__step">
        <h2>Query the container, not the screen</h2>
        <p>Now the component's layout rules live with the component. At 24rem the card switches from stacked to side-by-side, wherever it happens to be on the page.</p>
        <p>Inside a container query you can also use <code>cqw</code>, <code>cqi</code> and <code>cqb</code> units — <code>font-size: clamp(1rem, 4cqi, 1.5rem)</code> scales type to the card's width instead of the viewport's.</p>
      </section>

      <section class="bl-10__step">
        <h2>Verify the fallback</h2>
        <p>Style the stacked layout as the default and treat the side-by-side arrangement as the enhancement. A browser without container query support then renders the mobile layout everywhere, which is correct rather than broken.</p>
        <p>That's the whole technique. The card is now portable: drop it in any slot and it lays itself out.</p>
      </section>
    </div>

    <aside class="bl-10__code" aria-label="Code for this tutorial">
      <div class="bl-10__panel">
        <input class="bl-10__radio" type="radio" name="bl-10-file" id="bl-10-f1" checked>
        <input class="bl-10__radio" type="radio" name="bl-10-file" id="bl-10-f2">
        <input class="bl-10__radio" type="radio" name="bl-10-file" id="bl-10-f3">
        <div class="bl-10__tabs" role="presentation">
          <label class="bl-10__tab" for="bl-10-f1">card.css</label>
          <label class="bl-10__tab" for="bl-10-f2">card.html</label>
          <label class="bl-10__tab" for="bl-10-f3">tokens.css</label>
          <button class="bl-10__copy" type="button" data-copy>
            <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><rect x="7" y="7" width="9" height="9" rx="2" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M13 5.5A1.5 1.5 0 0 0 11.5 4H5.5A1.5 1.5 0 0 0 4 5.5v6A1.5 1.5 0 0 0 5.5 13" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
            <span data-copy-label>Copy</span>
          </button>
        </div>
        <div class="bl-10__panes">
          <pre class="bl-10__pane" data-lang="css"><code><span>.card-slot &#123;</span><span>  container: card / inline-size;</span><span>&#125;</span><span></span><span>.card &#123;</span><span>  display: grid;</span><span>  gap: 1rem;</span><span>  padding: 1.25rem;</span><span>  border-radius: 1rem;</span><span>  background: var(--surface);</span><span>&#125;</span><span></span><span>@container card (min-width: 24rem) &#123;</span><span>  .card &#123;</span><span>    grid-template-columns: 8rem 1fr;</span><span>    align-items: start;</span><span>  &#125;</span><span>  .card h3 &#123;</span><span>    font-size: clamp(1rem, 4cqi, 1.5rem);</span><span>  &#125;</span><span>&#125;</span></code></pre>
          <pre class="bl-10__pane" data-lang="html"><code><span>&lt;div class="card-slot"&gt;</span><span>  &lt;article class="card"&gt;</span><span>    &lt;img src="thumb.avif" alt=""</span><span>         width="320" height="240"&gt;</span><span>    &lt;div&gt;</span><span>      &lt;h3&gt;Portable by default&lt;/h3&gt;</span><span>      &lt;p&gt;Same component, any slot.&lt;/p&gt;</span><span>    &lt;/div&gt;</span><span>  &lt;/article&gt;</span><span>&lt;/div&gt;</span></code></pre>
          <pre class="bl-10__pane" data-lang="css"><code><span>:root &#123;</span><span>  --surface: oklch(100% 0 0);</span><span>  --text: oklch(20% .01 265);</span><span>  --muted: oklch(55% .02 265);</span><span>  --acc: oklch(58% .19 255);</span><span>&#125;</span><span></span><span>@media (prefers-color-scheme: dark) &#123;</span><span>  :root &#123;</span><span>    --surface: oklch(22% .01 265);</span><span>    --text: oklch(96% .01 265);</span><span>  &#125;</span><span>&#125;</span></code></pre>
        </div>
        <p class="bl-10__hint">Tabs are <code>:checked</code> radios — no JS. Line numbers are CSS counters, so they never end up in your clipboard.</p>
      </div>
    </aside>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');

.bl-10 {
  --bg: #f8f9fb;
  --surface: #ffffff;
  --code-bg: #0e1116;
  --code-fg: #dbe4f0;
  --code-line: #1c2330;
  --text: #0f1319;
  --muted: #5f6875;
  --line: #e2e6ec;
  --acc: #2563eb;
  --code-max: calc(100svh - 9rem);
  --sans: "Space Grotesk",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
}

@supports (color: oklch(50% 0 0)) {
  .bl-10 {
    --bg: oklch(98% .004 260);
    --surface: oklch(100% 0 0);
    --text: oklch(17% .012 265);
    --muted: oklch(50% .018 262);
    --line: oklch(91% .008 262);
    --acc: oklch(52% .2 262);
    --code-bg: oklch(17% .02 262);
    --code-fg: oklch(90% .015 262);
    --code-line: oklch(26% .02 262);
  }
}

@media (prefers-color-scheme: dark) {
  .bl-10:not([data-theme="light"]) {
    --bg: #0a0c10;
    --surface: #12151b;
    --text: #eef1f5;
    --muted: #98a2b0;
    --line: #222834;
    --acc: #7ea6ff;
    --code-bg: #080a0d;
    --code-line: #1a1f28;
  }
}

.bl-10[data-theme="dark"] {
  --bg: #0a0c10;
  --surface: #12151b;
  --text: #eef1f5;
  --muted: #98a2b0;
  --line: #222834;
  --acc: #7ea6ff;
  --code-bg: #080a0d;
  --code-line: #1a1f28;
}

.bl-10 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.bl-10,
.bl-10 *,
.bl-10 *::before,
.bl-10 *::after {
  box-sizing: border-box;
}

.bl-10 a {
  color: inherit;
}

.bl-10 :focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
  border-radius: 3px;
}

.bl-10__head {
  max-width: 82rem;
  margin-inline: auto;
  padding: clamp(2rem,5vw,3.5rem) clamp(1.25rem,4vw,3rem) clamp(1.5rem,3vw,2rem);
  display: grid;
  gap: .9rem;
}

.bl-10__crumbs {
  margin: 0;
  font-size: .8125rem;
  color: var(--muted);
}

.bl-10__crumbs a {
  color: var(--acc);
  text-decoration: none;
}

.bl-10__crumbs a:hover {
  text-decoration: underline;
  text-underline-offset: .2em;
}

.bl-10__head h1 {
  margin: 0;
  font-size: clamp(1.75rem,4vw,2.75rem);
  font-weight: 700;
  line-height: 1.06;
  letter-spacing: -.03em;
  max-width: 32ch;
  text-wrap: balance;
}

.bl-10__sub {
  margin: 0;
  font-size: 1.0625rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 60ch;
  text-wrap: pretty;
}

.bl-10__facts {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem 2rem;
  margin: .35rem 0 0;
  padding: 0;
  list-style: none;
}

.bl-10__facts li {
  display: grid;
  gap: .1rem;
  font-size: .875rem;
  font-weight: 500;
  font-variant-numeric: tabular-nums;
}

.bl-10__facts span {
  font-size: .625rem;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.bl-10__main {
  display: grid;
  gap: clamp(1.5rem,3vw,3rem);
  align-items: start;
  grid-template-columns: minmax(0,1fr) minmax(0,1.05fr);
  max-width: 82rem;
  margin-inline: auto;
  padding: 0 clamp(1.25rem,4vw,3rem) clamp(4rem,8vw,6rem);
}

.bl-10__steps {
  display: grid;
  gap: clamp(2rem,4vw,3rem);
  counter-reset: bl-10-step;
}

.bl-10__step {
  counter-increment: bl-10-step;
  display: grid;
  gap: .75rem;
}

.bl-10__step h2 {
  margin: 0;
  display: grid;
  grid-template-columns: auto minmax(0,1fr);
  gap: .75rem;
  align-items: baseline;
  font-size: clamp(1.1875rem,2.2vw,1.5rem);
  font-weight: 600;
  line-height: 1.2;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.bl-10__step h2::before {
  content: counter(bl-10-step);
  display: grid;
  place-items: center;
  width: 1.75rem;
  height: 1.75rem;
  border-radius: .5rem;
  background: var(--acc);
  color: #fff;
  font-family: var(--mono);
  font-size: .8125rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.bl-10__step p {
  margin: 0;
  font-size: 1rem;
  line-height: 1.7;
  color: var(--muted);
  max-width: 62ch;
  text-wrap: pretty;
}

.bl-10__step code {
  font-family: var(--mono);
  font-size: .85em;
  padding: .12em .35em;
  border-radius: .25rem;
  background: color-mix(in oklab,var(--acc) 12%,transparent);
  color: var(--text);
}

.bl-10__callout {
  padding: 1rem 1.15rem;
  border-radius: .75rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-inline-start: 3px solid var(--acc);
  color: var(--text) !important;
  font-size: .9375rem !important;
}

.bl-10__callout strong {
  font-weight: 600;
}

.bl-10__code {
  position: sticky;
  top: 1.5rem;
  align-self: start;
}

.bl-10__panel {
  display: grid;
  border: 1px solid var(--line);
  border-radius: 1rem;
  overflow: hidden;
  background: var(--code-bg);
  box-shadow: 0 1.5rem 3rem -1.5rem color-mix(in oklab,var(--text) 30%,transparent);
}

.bl-10__radio {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.bl-10__tabs {
  display: flex;
  align-items: center;
  gap: .25rem;
  padding: .5rem .5rem 0;
  background: var(--code-bg);
  border-bottom: 1px solid var(--code-line);
}

.bl-10__tab {
  display: inline-grid;
  place-items: center;
  min-height: 2.25rem;
  padding: 0 .85rem;
  border-radius: .5rem .5rem 0 0;
  font-family: var(--mono);
  font-size: .75rem;
  color: color-mix(in oklab,var(--code-fg) 55%,transparent);
  cursor: pointer;
  transition: background .18s ease, color .18s ease;
}

.bl-10__tab:hover {
  color: var(--code-fg);
}

.bl-10__radio:focus-visible + .bl-10__tab {
  outline: 2px solid var(--acc);
  outline-offset: -2px;
}

.bl-10__radio:nth-of-type(1):checked ~ .bl-10__tabs .bl-10__tab:nth-of-type(1),
.bl-10__radio:nth-of-type(2):checked ~ .bl-10__tabs .bl-10__tab:nth-of-type(2),
.bl-10__radio:nth-of-type(3):checked ~ .bl-10__tabs .bl-10__tab:nth-of-type(3) {
  background: color-mix(in oklab,var(--code-fg) 12%,transparent);
  color: var(--code-fg);
}

.bl-10__copy {
  margin-inline-start: auto;
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  min-height: 2.25rem;
  padding: 0 .7rem;
  border: 1px solid var(--code-line);
  border-radius: .5rem;
  background: transparent;
  color: color-mix(in oklab,var(--code-fg) 70%,transparent);
  font-family: var(--mono);
  font-size: .6875rem;
  cursor: pointer;
  transition: border-color .18s ease, color .18s ease;
}

.bl-10__copy svg {
  width: .95rem;
  height: .95rem;
}

.bl-10__copy:hover {
  color: var(--code-fg);
  border-color: color-mix(in oklab,var(--code-fg) 40%,transparent);
}

.bl-10__copy[data-done="true"] {
  color: #86efac;
  border-color: #86efac;
}

.bl-10__panes {
  display: grid;
  min-height: 22rem;
  max-height: var(--code-max);
  overflow: auto;
  scrollbar-width: thin;
}

.bl-10__pane {
  display: none;
  margin: 0;
  padding: 1rem 1rem 1.25rem;
  background: var(--code-bg);
}

.bl-10__radio:nth-of-type(1):checked ~ .bl-10__panes .bl-10__pane:nth-child(1),
.bl-10__radio:nth-of-type(2):checked ~ .bl-10__panes .bl-10__pane:nth-child(2),
.bl-10__radio:nth-of-type(3):checked ~ .bl-10__panes .bl-10__pane:nth-child(3) {
  display: block;
}

.bl-10__pane code {
  display: grid;
  counter-reset: bl-10-line;
  font-family: var(--mono);
  font-size: .8125rem;
  line-height: 1.75;
  color: var(--code-fg);
}

.bl-10__pane code span {
  counter-increment: bl-10-line;
  display: grid;
  grid-template-columns: 2.25rem minmax(0,1fr);
  white-space: pre-wrap;
}

.bl-10__pane code span::before {
  content: counter(bl-10-line);
  color: color-mix(in oklab,var(--code-fg) 32%,transparent);
  font-variant-numeric: tabular-nums;
  text-align: end;
  padding-inline-end: 1rem;
  user-select: none;
}

.bl-10__hint {
  margin: 0;
  padding: .7rem 1rem;
  border-top: 1px solid var(--code-line);
  background: var(--code-bg);
  font-size: .6875rem;
  line-height: 1.5;
  color: color-mix(in oklab,var(--code-fg) 55%,transparent);
}

.bl-10__hint code {
  font-family: var(--mono);
  color: var(--code-fg);
}

@media (max-width: 62rem) {
  .bl-10__main {
    grid-template-columns: minmax(0,1fr);
  }

  .bl-10__code {
    position: static;
    order: -1;
  }

  .bl-10__panes {
    max-height: 60svh;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bl-10 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .bl-10__step h2::before {
    forced-color-adjust: none;
    background: Highlight;
    color: HighlightText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.bl-10');
  if (!root) return;
  const btn = root.querySelector('[data-copy]');
  const label = root.querySelector('[data-copy-label]');
  btn.addEventListener('click', async () => {
    const pane = [...root.querySelectorAll('.bl-10__pane')].find((p) => getComputedStyle(p).display !== 'none');
    try {
      await navigator.clipboard.writeText(pane.innerText);
      btn.dataset.done = 'true'; label.textContent = 'Copied';
    } catch { label.textContent = 'Select & copy'; }
    setTimeout(() => { btn.removeAttribute('data-done'); label.textContent = 'Copy'; }, 1800);
  });
})();
```
