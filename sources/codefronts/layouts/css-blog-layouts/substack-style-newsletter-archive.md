---
source: "codefronts"
url: "https://codefronts.com/layouts/css-blog-layouts/substack-style-newsletter-archive/"
title: "Substack Style Newsletter Archive"
section: "layouts"
category: "css-blog-layouts"
category_name: "CSS Blog Layouts"
description: "A newsletter archive that reads like a back catalogue: issue numbers in a mono gutter, an inline subscribe block that sits inside the list after the third…"
has_js: "true"
---

Here's a working CSS Blog Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Substack Style Newsletter Archive
Source: https://codefronts.com/layouts/css-blog-layouts/substack-style-newsletter-archive/

A newsletter archive that reads like a back catalogue: issue numbers in a mono gutter, an inline subscribe block that sits inside the list after the third issue (where conversion actually happens), free/paid badges driven by a data attribute, and a sort toggle that reverses the visual order with flex-direction instead of re-rendering the DOM.
## HTML
```html
<div class="bl-04">
  <header class="bl-04__head">
    <div class="bl-04__brandRow">
      <span class="bl-04__mark" aria-hidden="true">RD</span>
      <div>
        <h1>Rough Drafts</h1>
        <p>A weekly letter about writing software slowly. Thursdays, ~1,400 words.</p>
      </div>
    </div>
    <p class="bl-04__count"><strong>47</strong> issues · <strong>9,120</strong> readers · <strong>68%</strong> open rate</p>
  </header>

  <div class="bl-04__toolbar">
    <h2 class="bl-04__archiveTitle">Archive</h2>
    <button class="bl-04__sort" type="button" data-sort aria-pressed="false">
      <svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M6 3v14m0 0-3-3m3 3 3-3M14 17V3m0 0-3 3m3-3 3 3" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
      <span data-sort-label>Newest first</span>
    </button>
  </div>

  <main class="bl-04__main">
    <ol class="bl-04__list" data-list style="--total:47">
      <li class="bl-04__item" data-tier="free">
        <p class="bl-04__num" aria-hidden="true"></p>
        <div class="bl-04__body">
          <h3><a href="#">The pull request that took a year</a></h3>
          <p class="bl-04__excerpt">A refactor I abandoned four times, and what the fifth attempt finally got right about scope.</p>
          <p class="bl-04__meta"><time datetime="2026-08-06">6 Aug 2026</time> · 11 min · <span class="bl-04__tier">Free</span></p>
        </div>
      </li>
      <li class="bl-04__item" data-tier="paid">
        <p class="bl-04__num" aria-hidden="true"></p>
        <div class="bl-04__body">
          <h3><a href="#">Pricing a product you don't want to grow</a></h3>
          <p class="bl-04__excerpt">Deliberate ceilings, and the three numbers I check before raising a price.</p>
          <p class="bl-04__meta"><time datetime="2026-07-30">30 Jul 2026</time> · 14 min · <span class="bl-04__tier">Subscribers</span></p>
        </div>
      </li>
      <li class="bl-04__item" data-tier="free">
        <p class="bl-04__num" aria-hidden="true"></p>
        <div class="bl-04__body">
          <h3><a href="#">Notes on writing documentation nobody asked for</a></h3>
          <p class="bl-04__excerpt">Docs as a design tool: what writing the guide first changed about the API.</p>
          <p class="bl-04__meta"><time datetime="2026-07-23">23 Jul 2026</time> · 9 min · <span class="bl-04__tier">Free</span></p>
        </div>
      </li>

      <li class="bl-04__breakout">
        <div class="bl-04__sub">
          <h3>Get the next one in your inbox</h3>
          <p>One letter a week. No sponsors, no drip sequence, one-click unsubscribe.</p>
          <div class="bl-04__field">
            <label class="bl-04__srOnly" for="bl-04-email">Email address</label>
            <input id="bl-04-email" type="email" inputmode="email" autocomplete="email" placeholder="[email protected]" required>
            <button type="button">Subscribe</button>
          </div>
          <p class="bl-04__fine">Joining 9,120 readers · <a href="#">read a sample issue</a></p>
        </div>
      </li>

      <li class="bl-04__item" data-tier="paid">
        <p class="bl-04__num" aria-hidden="true"></p>
        <div class="bl-04__body">
          <h3><a href="#">Six months of shipping on Fridays</a></h3>
          <p class="bl-04__excerpt">The deploy policy everyone told me was a mistake, measured honestly.</p>
          <p class="bl-04__meta"><time datetime="2026-07-16">16 Jul 2026</time> · 16 min · <span class="bl-04__tier">Subscribers</span></p>
        </div>
      </li>
      <li class="bl-04__item" data-tier="free">
        <p class="bl-04__num" aria-hidden="true"></p>
        <div class="bl-04__body">
          <h3><a href="#">Against the roadmap</a></h3>
          <p class="bl-04__excerpt">What replaced quarterly planning here, and the one thing I miss about it.</p>
          <p class="bl-04__meta"><time datetime="2026-07-09">9 Jul 2026</time> · 8 min · <span class="bl-04__tier">Free</span></p>
        </div>
      </li>
      <li class="bl-04__item" data-tier="free">
        <p class="bl-04__num" aria-hidden="true"></p>
        <div class="bl-04__body">
          <h3><a href="#">A reading list for people who hate reading lists</a></h3>
          <p class="bl-04__excerpt">Four books, one paper, and why I stopped recommending the obvious one.</p>
          <p class="bl-04__meta"><time datetime="2026-07-02">2 Jul 2026</time> · 6 min · <span class="bl-04__tier">Free</span></p>
        </div>
      </li>
    </ol>
  </main>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Literata:opsz,[email protected],400;7..72,500;7..72,600&family=JetBrains+Mono:wght@400;600&display=swap');

.bl-04 {
  --bg: #fffdf9;
  --surface: #ffffff;
  --text: #191612;
  --muted: #726b61;
  --line: #e8e1d6;
  --acc: #c2410c;
  --paid: #7c2d12;
  --ring: #c2410c;
  --serif: "Literata",ui-serif,Georgia,serif;
  --mono: "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
}

@supports (color: oklch(50% 0 0)) {
  .bl-04 {
    --bg: oklch(99% .008 85);
    --surface: oklch(100% 0 0);
    --text: oklch(19% .012 60);
    --muted: oklch(53% .018 65);
    --line: oklch(91% .015 82);
    --acc: oklch(55% .17 45);
    --paid: oklch(42% .12 45);
  }
}

@media (prefers-color-scheme: dark) {
  .bl-04:not([data-theme="light"]) {
    --bg: #100f0d;
    --surface: #191714;
    --text: #f4f1ea;
    --muted: #a49c90;
    --line: #2b2823;
    --acc: #fb923c;
    --paid: #fdba74;
  }
}

.bl-04[data-theme="dark"] {
  --bg: #100f0d;
  --surface: #191714;
  --text: #f4f1ea;
  --muted: #a49c90;
  --line: #2b2823;
  --acc: #fb923c;
  --paid: #fdba74;
}

.bl-04 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  color: var(--text);
  font-family: var(--serif);
  -webkit-font-smoothing: antialiased;
}

.bl-04,
.bl-04 *,
.bl-04 *::before,
.bl-04 *::after {
  box-sizing: border-box;
}

.bl-04 a {
  color: inherit;
  text-decoration: none;
}

.bl-04 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
  border-radius: 3px;
}

.bl-04__srOnly {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.bl-04__head {
  max-width: 52rem;
  margin-inline: auto;
  padding: clamp(2.5rem,7vw,5rem) clamp(1.25rem,5vw,2rem) 1.5rem;
  display: grid;
  gap: 1.25rem;
}

.bl-04__brandRow {
  display: flex;
  gap: 1.25rem;
  align-items: start;
}

.bl-04__mark {
  display: grid;
  place-items: center;
  flex: 0 0 auto;
  width: 3.5rem;
  height: 3.5rem;
  border-radius: .75rem;
  background: var(--acc);
  color: #fff;
  font-family: var(--mono);
  font-weight: 600;
  font-size: 1.125rem;
  letter-spacing: -.02em;
}

.bl-04__head h1 {
  margin: 0 0 .35rem;
  font-size: clamp(1.75rem,4vw,2.5rem);
  font-weight: 600;
  letter-spacing: -.025em;
  line-height: 1.05;
}

.bl-04__brandRow p {
  margin: 0;
  font-size: 1rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 46ch;
  text-wrap: pretty;
}

.bl-04__count {
  margin: 0;
  padding-top: 1.25rem;
  border-top: 1px solid var(--line);
  font-family: var(--mono);
  font-size: .75rem;
  letter-spacing: .02em;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.bl-04__count strong {
  color: var(--text);
  font-weight: 600;
}

.bl-04__toolbar {
  position: sticky;
  top: 0;
  z-index: 3;
  max-width: 52rem;
  margin-inline: auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: .75rem clamp(1.25rem,5vw,2rem);
  background: color-mix(in oklab,var(--bg) 88%,transparent);
}

@supports (backdrop-filter: blur(6px)) {
  .bl-04__toolbar {
    backdrop-filter: blur(12px);
  }
}

.bl-04__archiveTitle {
  margin: 0;
  font-family: var(--mono);
  font-size: .75rem;
  font-weight: 600;
  letter-spacing: .18em;
  text-transform: uppercase;
}

.bl-04__sort {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  min-height: 2.75rem;
  padding: 0 .875rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 999px;
  font-family: var(--mono);
  font-size: .75rem;
  color: var(--text);
  cursor: pointer;
  transition: border-color .18s ease, background .18s ease;
}

.bl-04__sort svg {
  width: 1rem;
  height: 1rem;
}

.bl-04__sort:hover {
  border-color: var(--acc);
}

.bl-04__sort[aria-pressed="true"] {
  background: color-mix(in oklab,var(--acc) 12%,transparent);
  border-color: var(--acc);
  color: var(--acc);
}

.bl-04__main {
  max-width: 52rem;
  margin-inline: auto;
  padding: 0 clamp(1.25rem,5vw,2rem) clamp(3rem,8vw,6rem);
}

.bl-04__list {
  display: flex;
  flex-direction: column;
  margin: 0;
  padding: 0;
  list-style: none;
  counter-reset: bl-04-issue var(--total,47);
}

.bl-04__list[data-order="oldest"] {
  flex-direction: column-reverse;
}

.bl-04__item {
  counter-increment: bl-04-issue -1;
  display: grid;
  grid-template-columns: 4.5rem minmax(0,1fr);
  gap: 1.25rem;
  padding-block: clamp(1.25rem,2.5vw,1.75rem);
  border-top: 1px solid var(--line);
}

.bl-04__num {
  margin: 0;
  font-family: var(--mono);
  font-size: .8125rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  letter-spacing: -.02em;
}

.bl-04__num::before {
  content: "#" counter(bl-04-issue);
}

.bl-04__body {
  display: grid;
  gap: .5rem;
}

.bl-04__item h3 {
  margin: 0;
  font-size: clamp(1.1875rem,2.4vw,1.5rem);
  font-weight: 600;
  line-height: 1.2;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.bl-04__item h3 a {
  background: linear-gradient(var(--acc),var(--acc)) 0 100%/0 1.5px no-repeat;
  transition: background-size .35s cubic-bezier(.16,1,.3,1);
}

.bl-04__item h3 a:hover {
  background-size: 100% 1.5px;
}

.bl-04__excerpt {
  margin: 0;
  font-size: .9375rem;
  line-height: 1.65;
  color: var(--muted);
  max-width: 60ch;
  text-wrap: pretty;
}

.bl-04__meta {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .5rem;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.bl-04__tier {
  padding: .2rem .45rem;
  border: 1px solid var(--line);
  border-radius: .25rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  font-size: .5625rem;
}

.bl-04__item[data-tier="paid"] .bl-04__tier {
  border-color: color-mix(in oklab,var(--paid) 45%,transparent);
  background: color-mix(in oklab,var(--paid) 12%,transparent);
  color: var(--paid);
}

.bl-04__item:has([data-tier]) {
  position: relative;
}

.bl-04__item[data-tier="paid"] .bl-04__num::after {
  content: " ★";
  color: var(--paid);
}

.bl-04__breakout {
  padding-block: clamp(1.5rem,3vw,2rem);
  border-top: 1px solid var(--line);
}

.bl-04__sub {
  display: grid;
  gap: .85rem;
  padding: clamp(1.25rem,3vw,2rem);
  border: 1px solid color-mix(in oklab,var(--acc) 30%,var(--line));
  border-radius: 1rem;
  background: color-mix(in oklab,var(--acc) 6%,var(--surface));
}

.bl-04__sub h3 {
  margin: 0;
  font-size: clamp(1.25rem,2.6vw,1.625rem);
  font-weight: 600;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.bl-04__sub > p {
  margin: 0;
  font-size: .9375rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 50ch;
  text-wrap: pretty;
}

.bl-04__field {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  margin-top: .25rem;
}

.bl-04__field input {
  flex: 1 1 14rem;
  min-width: 0;
  min-height: 3rem;
  padding: 0 1rem;
  background: var(--surface);
  color: var(--text);
  border: 1px solid var(--line);
  border-radius: .5rem;
  font-family: var(--mono);
  font-size: .875rem;
}

.bl-04__field input::placeholder {
  color: color-mix(in oklab,var(--muted) 70%,transparent);
}

.bl-04__field input:user-invalid {
  border-color: #dc2626;
  box-shadow: 0 0 0 3px color-mix(in oklab,#dc2626 15%,transparent);
}

.bl-04__field button {
  min-height: 3rem;
  padding: 0 1.5rem;
  border: 0;
  border-radius: .5rem;
  background: var(--acc);
  color: #fff;
  font-family: var(--mono);
  font-size: .8125rem;
  font-weight: 600;
  letter-spacing: .02em;
  cursor: pointer;
  transition: filter .18s ease, translate .18s ease;
}

.bl-04__field button:hover {
  filter: brightness(1.08);
  translate: 0 -1px;
}

.bl-04__fine {
  margin: 0;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

.bl-04__fine a {
  text-decoration: underline;
  text-underline-offset: .2em;
  color: var(--acc);
}

@media (max-width: 32rem) {
  .bl-04__item {
    grid-template-columns: minmax(0,1fr);
    gap: .4rem;
  }

  .bl-04__brandRow {
    flex-direction: column;
    gap: .875rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .bl-04 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .bl-04__sub {
    border: 1px solid CanvasText;
  }

  .bl-04__field button {
    forced-color-adjust: none;
    background: Highlight;
    color: HighlightText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.bl-04');
  if (!root) return;
  const list = root.querySelector('[data-list]');
  const btn = root.querySelector('[data-sort]');
  const label = root.querySelector('[data-sort-label]');
  btn.addEventListener('click', () => {
    const oldest = btn.getAttribute('aria-pressed') !== 'true';
    btn.setAttribute('aria-pressed', String(oldest));
    list.dataset.order = oldest ? 'oldest' : 'newest';
    label.textContent = oldest ? 'Oldest first' : 'Newest first';
  });
})();
```
