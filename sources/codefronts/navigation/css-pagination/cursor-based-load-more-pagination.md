---
source: "codefronts"
url: "https://codefronts.com/navigation/css-pagination/cursor-based-load-more-pagination/"
title: "Cursor-Based Load More Pagination"
section: "navigation"
category: "css-pagination"
category_name: "CSS Pagination"
description: "Offset pagination breaks on live data: insert a row while someone is reading and page two silently repeats or skips records."
has_js: "true"
---

Here's a working CSS Pagination from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Cursor-Based Load More Pagination
Source: https://codefronts.com/navigation/css-pagination/cursor-based-load-more-pagination/

Offset pagination breaks on live data: insert a row while someone is reading and page two silently repeats or skips records. Cursor paging fixes it by pointing at the last row you saw, and the UI has to change too — no page count, no jump-to-40, just Load newer above the feed and Load older below, with each row exposing its own cursor id.
## HTML
```html
<section class="pgn-13" aria-label="Cursor-Based Load Newer / Older Pagination demo">
  <div class="pgn-13__stage">
    <header class="pgn-13__head">
      <p class="pgn-13__eyebrow">Event stream</p>
      <h2 class="pgn-13__title">Cursor paging, no offsets</h2>
      <p class="pgn-13__sub">Each request carries the id of the last row you saw. Rows inserted while you read never shift the window — the classic failure of LIMIT and OFFSET.</p>
    </header>

    <button class="pgn-13__load" type="button" data-newer>Load newer</button>

    <ol class="pgn-13__feed" data-feed>
      <li class="pgn-13__item"><span class="pgn-13__dot"></span><div><p class="pgn-13__ev">deploy.succeeded</p><p class="pgn-13__det">web · Alex Chen · 12:41</p></div><code class="pgn-13__cur">evt_8f2a</code></li>
      <li class="pgn-13__item"><span class="pgn-13__dot"></span><div><p class="pgn-13__ev">index.rebuilt</p><p class="pgn-13__det">search · system · 12:38</p></div><code class="pgn-13__cur">evt_8f29</code></li>
      <li class="pgn-13__item"><span class="pgn-13__dot"></span><div><p class="pgn-13__ev">key.rotated</p><p class="pgn-13__det">auth · Priya Sharma · 12:30</p></div><code class="pgn-13__cur">evt_8f28</code></li>
    </ol>

    <button class="pgn-13__load" type="button" data-older>Load older</button>

    <p class="pgn-13__cursorline" role="status" aria-live="polite" data-status>Cursor: after=evt_8f28 · limit=3</p>
  </div>
</section>
```
## CSS
```css
.pgn-13 {
  --bg: #fafafa;
  --surface: #ffffff;
  --surface-2: #f4f4f5;
  --text: #09090b;
  --muted: #71717a;
  --line: #e4e4e7;
  --acc: #18181b;
  --acc-fg: #ffffff;
  --ring: #6366f1;
  --live: #16a34a;
}

@supports (color: oklch(50% 0 0)) {
  .pgn-13 {
    --bg: oklch(98.4% .002 286);
    --surface: oklch(100% 0 0);
    --surface-2: oklch(96.5% .003 286);
    --text: oklch(17% .006 286);
    --muted: oklch(55% .015 286);
    --line: oklch(92% .004 286);
    --acc: oklch(22% .008 286);
    --acc-fg: oklch(99% 0 0);
    --ring: oklch(62% .19 277);
    --live: oklch(60% .16 150);
  }
}

@media (prefers-color-scheme: dark) {
  .pgn-13:not([data-theme="light"]) {
    --bg: #09090b;
    --surface: #131316;
    --surface-2: #1c1c20;
    --text: #fafafa;
    --muted: #a1a1aa;
    --line: #27272a;
    --acc: #fafafa;
    --acc-fg: #09090b;
    --ring: #818cf8;
    --live: #4ade80;
  }
}

.pgn-13[data-theme="dark"] {
  --bg: #09090b;
  --surface: #131316;
  --surface-2: #1c1c20;
  --text: #fafafa;
  --muted: #a1a1aa;
  --line: #27272a;
  --acc: #fafafa;
  --acc-fg: #09090b;
  --ring: #818cf8;
  --live: #4ade80;
}

.pgn-13 {
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

.pgn-13,
.pgn-13 *,
.pgn-13 *::before,
.pgn-13 *::after {
  box-sizing: border-box;
}

@supports (interpolate-size: allow-keywords) {
  .pgn-13 {
    interpolate-size: allow-keywords;
  }
}

.pgn-13__stage {
  width: 100%;
  max-width: 42rem;
  display: grid;
  gap: .85rem;
  justify-items: stretch;
}

.pgn-13__head {
  display: grid;
  gap: .45rem;
  margin-bottom: .75rem;
}

.pgn-13__eyebrow {
  margin: 0;
  font-size: .6875rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.pgn-13__title {
  margin: 0;
  font-size: clamp(1.4rem,3.2vw,1.9rem);
  font-weight: 600;
  letter-spacing: -.025em;
}

.pgn-13__sub {
  margin: 0;
  max-width: 34rem;
  font-size: .875rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.pgn-13__load {
  height: 2.75rem;
  border: 1px dashed var(--line);
  border-radius: .75rem;
  background: transparent;
  color: var(--muted);
  font: inherit;
  font-size: .8125rem;
  cursor: pointer;
  transition: background .16s ease, color .16s ease, border-color .16s ease;
}

.pgn-13__load:not(:disabled):hover {
  background: var(--surface-2);
  color: var(--text);
  border-color: color-mix(in oklab,var(--text) 25%,var(--line));
}

.pgn-13__load:focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}

.pgn-13__load:disabled {
  opacity: .4;
  cursor: not-allowed;
}

.pgn-13__feed {
  display: grid;
  gap: .5rem;
  list-style: none;
  margin: 0;
  padding: 0;
  block-size: auto;
  transition: block-size .3s cubic-bezier(.16,1,.3,1);
}

.pgn-13__item {
  display: flex;
  align-items: center;
  gap: .85rem;
  padding: .9rem 1rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: .75rem;
  animation: pgn-13-in .3s cubic-bezier(.16,1,.3,1);
}

.pgn-13__item > div {
  flex: 1 1 auto;
  min-width: 0;
}

@keyframes pgn-13-in {
  from {
    opacity: 0;
    translate: 0 .4rem;
  }
}

.pgn-13__dot {
  width: .5rem;
  height: .5rem;
  border-radius: 50%;
  background: var(--live);
  flex: none;
}

.pgn-13__ev {
  margin: 0;
  font-size: .875rem;
  font-weight: 550;
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  letter-spacing: -.01em;
}

.pgn-13__det {
  margin: .15rem 0 0;
  font-size: .75rem;
  color: var(--muted);
}

.pgn-13__cur {
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size: .6875rem;
  color: var(--muted);
  background: var(--surface-2);
  padding: .2rem .4rem;
  border-radius: .3rem;
  flex: none;
}

.pgn-13__cursorline {
  margin: .5rem 0 0;
  font-family: ui-monospace,SFMono-Regular,Menlo,monospace;
  font-size: .75rem;
  color: var(--muted);
  text-align: center;
}

@media (prefers-reduced-motion: reduce) {
  .pgn-13 * {
    animation: none !important;
    transition: none !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.pgn-13');
  if (!root) return;
  const feed = root.querySelector('[data-feed]');
  const status = root.querySelector('[data-status]');
  const newer = root.querySelector('[data-newer]');
  const older = root.querySelector('[data-older]');
  const pages = [
    [['deploy.succeeded', 'web · Alex Chen · 12:41', '8f2a'], ['index.rebuilt', 'search · system · 12:38', '8f29'], ['key.rotated', 'auth · Priya Sharma · 12:30', '8f28']],
    [['webhook.retried', 'billing · system · 12:12', '8f27'], ['plan.upgraded', 'billing · Jordan Lee · 11:58', '8f26'], ['seat.invited', 'team · Sam Rivera · 11:47', '8f25']],
    [['export.finished', 'reports · Priya Sharma · 11:20', '8f24'], ['rule.disabled', 'alerts · Alex Chen · 11:04', '8f23'], ['login.blocked', 'auth · system · 10:52', '8f22']]
  ];
  let i = 0;
  const paint = () => {
    feed.replaceChildren(...pages[i].map(([ev, det, id]) => {
      const li = document.createElement('li');
      li.className = 'pgn-13__item';
      li.innerHTML = '<span class="pgn-13__dot"></span><div><p class="pgn-13__ev"></p><p class="pgn-13__det"></p></div><code class="pgn-13__cur"></code>';
      li.querySelector('.pgn-13__ev').textContent = ev;
      li.querySelector('.pgn-13__det').textContent = det;
      li.querySelector('.pgn-13__cur').textContent = 'evt_' + id;
      return li;
    }));
    newer.disabled = i === 0; older.disabled = i === pages.length - 1;
    status.textContent = 'Cursor: after=evt_' + pages[i].at(-1)[2] + ' · limit=3';
  };
  newer.addEventListener('click', () => { if (i > 0) { i--; paint(); } });
  older.addEventListener('click', () => { if (i < pages.length - 1) { i++; paint(); } });
  paint();
})();
```
