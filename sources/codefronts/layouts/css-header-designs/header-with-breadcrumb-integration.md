---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/header-with-breadcrumb-integration/"
title: "Header with Breadcrumb Integration"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "A two-tier header for deep pages: brand, section nav and utilities on the top row, then a breadcrumb trail on the row below with the page actions aligned to…"
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Header with Breadcrumb Integration
Source: https://codefronts.com/layouts/css-header-designs/header-with-breadcrumb-integration/

A two-tier header for deep pages: brand, section nav and utilities on the top row, then a breadcrumb trail on the row below with the page actions aligned to its right. The trail is a real <nav aria-label="Breadcrumb"> wrapping an ordered list, the last item carries aria-current="page", and separators are generated so they are never read aloud.
## HTML
```html
<div class="hd-09">
  <a class="hd-09__skip" href="#hd-09-main">Skip to content</a>

  <header class="hd-09__header">
    <div class="hd-09__row1">
      <a class="hd-09__brand" href="#hd-09-main">
        <span class="hd-09__mark" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M4 17.5 9.5 12l3.5 3.5L20 8" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </span>
        <span class="hd-09__word">Beacon<span>Cloud</span></span>
      </a>

      <nav class="hd-09__nav" aria-label="Main">
        <ul>
          <li><a href="#hd-09-main">Home</a></li>
          <li><a href="#hd-09-main" aria-current="page">Products</a></li>
          <li><a href="#hd-09-main">Reports</a></li>
          <li><a href="#hd-09-main">Admin</a></li>
        </ul>
      </nav>

      <div class="hd-09__util">
        <input class="hd-09__sr" type="checkbox" id="hd-09-dark">
        <label class="hd-09__theme" for="hd-09-dark">
          <svg class="hd-09__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          <svg class="hd-09__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
          <span class="hd-09__vh">Switch light or dark theme</span>
        </label>
        <button class="hd-09__icon" type="button" aria-label="Search">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.8 15.8 21 21" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        </button>
        <button class="hd-09__icon" type="button" aria-label="Help and documentation">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.4" stroke="currentColor" stroke-width="1.8"/><path d="M9.8 9.5a2.3 2.3 0 1 1 3.4 2.1c-.8.5-1.2 1-1.2 1.9M12 16.7h.01" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        </button>
        <div class="hd-09__menu">
          <button class="hd-09__who" type="button" aria-haspopup="menu">
            <span class="hd-09__av" aria-hidden="true">SR</span>
            <span class="hd-09__who-t">Sam Rivera</span>
            <svg class="hd-09__chev" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M8 10.5 12 14.5l4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </button>
          <div class="hd-09__pop" role="menu" aria-label="Account">
            <a role="menuitem" href="#hd-09-main">Account settings</a>
            <a role="menuitem" href="#hd-09-main">Organisation</a>
            <a role="menuitem" href="#hd-09-main">API tokens</a>
            <a role="menuitem" href="#hd-09-main">Sign out</a>
          </div>
        </div>
      </div>
    </div>

    <div class="hd-09__row2">
      <nav class="hd-09__crumbs" aria-label="Breadcrumb">
        <ol>
          <li><a href="#hd-09-main">Home</a></li>
          <li><a href="#hd-09-main">Products</a></li>
          <li><a href="#hd-09-main">Observability</a></li>
          <li><span aria-current="page">Analytics Dashboard</span></li>
        </ol>
      </nav>
      <div class="hd-09__actions">
        <button class="hd-09__btn" type="button">Export CSV</button>
        <button class="hd-09__btn hd-09__btn--primary" type="button">Edit dashboard</button>
      </div>
    </div>
  </header>

  <main class="hd-09__main" id="hd-09-main">
    <h1>Analytics Dashboard</h1>
    <p class="hd-09__lead">Request volume, error rate and saturation for the eu-west estate. The breadcrumb row above stays parked under the bar as you scroll, which is what deep-page navigation needs.</p>

    <ul class="hd-09__tiles">
      <li><p class="hd-09__k">Requests / min</p><p class="hd-09__v">48,210</p><span class="hd-09__spark" aria-hidden="true"></span></li>
      <li><p class="hd-09__k">Error rate</p><p class="hd-09__v">0.42<span>%</span></p><span class="hd-09__spark" aria-hidden="true"></span></li>
      <li><p class="hd-09__k">Saturation</p><p class="hd-09__v">61<span>%</span></p><span class="hd-09__spark" aria-hidden="true"></span></li>
    </ul>

    <section class="hd-09__table-wrap">
      <h2>Top routes</h2>
      <table class="hd-09__table">
        <thead><tr><th scope="col">Route</th><th scope="col">Calls</th><th scope="col">p95</th><th scope="col">Errors</th></tr></thead>
        <tbody>
          <tr><td>/api/v3/orders</td><td>18,402</td><td>212 ms</td><td>0.31%</td></tr>
          <tr><td>/api/v3/customers</td><td>11,940</td><td>168 ms</td><td>0.12%</td></tr>
          <tr><td>/api/v3/search</td><td>9,318</td><td>404 ms</td><td>1.04%</td></tr>
          <tr><td>/api/v3/webhooks</td><td>4,772</td><td>96 ms</td><td>0.02%</td></tr>
        </tbody>
      </table>
    </section>
    <div class="hd-09__filler" aria-hidden="true"></div>
  </main>
</div>
```
## CSS
```css
.hd-09 {
  --s1: #ffffff;
  --s2: #f4f7fb;
  --s3: #e8eef7;
  --ink: #0f1b2d;
  --muted: #5a6b83;
  --line: #dbe4f0;
  --accent: #0b6bcb;
  --accent-soft: #e8f1fd;
  --accent-ink: #ffffff;
  --row1: 3.5rem;
  --font-display: system-ui,-apple-system,"Segoe UI Variable","Segoe UI",sans-serif;
  --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  background: var(--s2);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.5;
}

@supports (color: oklch(50% .1 200)) {
  .hd-09 {
    --s2: oklch(97.5% .01 250);
    --s3: oklch(94% .015 250);
    --ink: oklch(22% .04 255);
    --muted: oklch(50% .03 255);
    --accent: oklch(52% .16 255);
  }
}

.hd-09 * {
  box-sizing: border-box;
}

.hd-09 h1,
.hd-09 h2,
.hd-09 p,
.hd-09 ul,
.hd-09 ol {
  margin: 0;
  padding: 0;
}

.hd-09 ul,
.hd-09 ol {
  list-style: none;
}

.hd-09 [hidden] {
  display: none;
}

.hd-09 :focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: .3rem;
}

.hd-09__skip {
  position: absolute;
  inset-inline-start: .75rem;
  top: -3rem;
  z-index: 60;
  padding: .5rem .9rem;
  border-radius: .3rem;
  background: var(--accent);
  color: var(--accent-ink);
  font-size: .8rem;
  font-weight: 640;
  text-decoration: none;
  transition: top .18s ease;
}

.hd-09__skip:focus-visible {
  top: .75rem;
}
/* ── two-tier header, layered surfaces, zero shadow ───────────────── */

.hd-09__header {
  position: relative;
  z-index: 30;
}

.hd-09__row1 {
  position: sticky;
  top: 0;
  z-index: 32;
  display: flex;
  align-items: center;
  gap: .75rem;
  min-block-size: var(--row1);
  padding: .4rem clamp(.75rem,3vw,1.5rem);
  background: var(--s1);
  border-bottom: 1px solid var(--line);
}

.hd-09__brand {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  color: var(--ink);
  text-decoration: none;
  min-inline-size: 0;
}

.hd-09__mark {
  display: grid;
  place-items: center;
  inline-size: 1.8rem;
  block-size: 1.8rem;
  border-radius: .4rem;
  background: var(--accent);
  color: #fff;
  flex: none;
}

.hd-09__mark svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.hd-09__word {
  font-family: var(--font-display);
  font-size: .95rem;
  font-weight: 700;
  letter-spacing: -.02em;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-09__word span {
  font-weight: 400;
  color: var(--muted);
}

.hd-09__nav {
  min-inline-size: 0;
  margin-inline-start: .75rem;
}

.hd-09__nav ul {
  display: flex;
  align-items: center;
  gap: .1rem;
}

.hd-09__nav a {
  display: block;
  padding: .45rem .7rem;
  color: var(--muted);
  text-decoration: none;
  font-size: .85rem;
  font-weight: 560;
  white-space: nowrap;
  border-bottom: 2px solid transparent;
  transition: color .15s ease, border-color .15s ease;
}

.hd-09__nav a:hover {
  color: var(--ink);
}

.hd-09__nav a[aria-current="page"] {
  color: var(--accent);
  border-bottom-color: var(--accent);
  font-weight: 640;
}

.hd-09__util {
  display: flex;
  align-items: center;
  gap: .25rem;
  margin-inline-start: auto;
}

.hd-09__icon {
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border: 0;
  border-radius: .4rem;
  background: transparent;
  color: var(--muted);
  cursor: pointer;
  transition: background-color .15s ease, color .15s ease;
}

.hd-09__icon svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-09__icon:hover {
  background: var(--s3);
  color: var(--ink);
}

.hd-09__menu {
  position: relative;
}

.hd-09__who {
  display: flex;
  align-items: center;
  gap: .45rem;
  max-inline-size: 12rem;
  min-inline-size: 0;
  min-block-size: 2.5rem;
  padding: .3rem .5rem;
  border: 1px solid var(--line);
  border-radius: .4rem;
  background: var(--s1);
  color: var(--ink);
  font: inherit;
  font-size: .84rem;
  cursor: pointer;
  transition: background-color .15s ease;
}

.hd-09__who:hover {
  background: var(--s2);
}

.hd-09__av {
  display: grid;
  place-items: center;
  inline-size: 1.6rem;
  block-size: 1.6rem;
  border-radius: .3rem;
  flex: none;
  background: var(--accent-soft);
  color: var(--accent);
  font-size: .66rem;
  font-weight: 700;
}

.hd-09__who-t {
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-09__chev {
  inline-size: .95rem;
  block-size: .95rem;
  color: var(--muted);
  flex: none;
  transition: rotate .18s ease;
}

.hd-09__menu:hover .hd-09__chev,
.hd-09__menu:focus-within .hd-09__chev {
  rotate: 180deg;
}

.hd-09__pop {
  position: absolute;
  inset-inline-end: 0;
  top: calc(100% + .35rem);
  z-index: 40;
  inline-size: 13rem;
  padding: .25rem;
  border: 1px solid var(--line);
  border-radius: .5rem;
  background: var(--s1);
  visibility: hidden;
  opacity: 0;
  translate: 0 -.25rem;
  transition: opacity .15s ease, translate .15s ease, visibility .15s allow-discrete;
}

.hd-09__menu:hover > .hd-09__pop,
.hd-09__menu:focus-within > .hd-09__pop {
  visibility: visible;
  opacity: 1;
  translate: 0 0;
}

.hd-09__pop a {
  display: flex;
  align-items: center;
  min-block-size: 2.4rem;
  padding: .4rem .55rem;
  border-radius: .35rem;
  color: var(--ink);
  text-decoration: none;
  font-size: .85rem;
}

.hd-09__pop a:hover {
  background: var(--s2);
}
/* breadcrumb row — sticks below row 1 */

.hd-09__row2 {
  position: sticky;
  top: var(--row1);
  z-index: 31;
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: .5rem clamp(.75rem,3vw,1.5rem);
  background: var(--s2);
  border-bottom: 1px solid var(--line);
}

.hd-09__crumbs {
  min-inline-size: 0;
  overflow-x: auto;
  scrollbar-width: none;
  direction: rtl;
}

.hd-09__crumbs::-webkit-scrollbar {
  display: none;
}

.hd-09__crumbs ol {
  direction: ltr;
  display: flex;
  align-items: center;
  font-size: .82rem;
  white-space: nowrap;
}

.hd-09__crumbs li {
  display: flex;
  align-items: center;
  min-inline-size: 0;
}

.hd-09__crumbs li + li::before {
  content: "\203A";
  color: var(--muted);
  padding-inline: .45rem;
  opacity: .7;
}

.hd-09__crumbs a {
  color: var(--muted);
  text-decoration: none;
  padding-block: .3rem;
  transition: color .15s ease;
}

.hd-09__crumbs a:hover {
  color: var(--accent);
  text-decoration: underline;
  text-underline-offset: .2em;
}

.hd-09__crumbs [aria-current="page"] {
  color: var(--ink);
  font-weight: 640;
}

.hd-09__actions {
  display: flex;
  align-items: center;
  gap: .4rem;
  margin-inline-start: auto;
}

.hd-09__btn {
  min-block-size: 2.35rem;
  padding: .5rem .85rem;
  border: 1px solid var(--line);
  border-radius: .4rem;
  background: var(--s1);
  color: var(--ink);
  font: inherit;
  font-size: .82rem;
  font-weight: 600;
  white-space: nowrap;
  cursor: pointer;
  transition: background-color .15s ease, border-color .15s ease;
}

.hd-09__btn:hover {
  background: var(--s3);
}

.hd-09__btn--primary {
  background: var(--accent);
  border-color: var(--accent);
  color: var(--accent-ink);
}

.hd-09__btn--primary:hover {
  background: color-mix(in srgb, var(--accent) 85%, #000);
}
/* ── page body ────────────────────────────────────────────────────── */

.hd-09__main {
  max-inline-size: 76rem;
  margin-inline: auto;
  padding: clamp(1.5rem,4vw,2.5rem) clamp(.75rem,3vw,1.5rem) 4rem;
}

.hd-09__main h1 {
  font-family: var(--font-display);
  font-size: clamp(1.5rem,4vw,2rem);
  font-weight: 700;
  letter-spacing: -.03em;
}

.hd-09__lead {
  margin-top: .5rem;
  max-inline-size: 60ch;
  color: var(--muted);
  font-size: .95rem;
  text-wrap: pretty;
}

.hd-09__tiles {
  display: grid;
  gap: .75rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,13rem),1fr));
  margin-top: 1.5rem;
}

.hd-09__tiles li {
  padding: 1rem;
  background: var(--s1);
  border: 1px solid var(--line);
  border-radius: .5rem;
  min-inline-size: 0;
}

.hd-09__k {
  font-size: .75rem;
  color: var(--muted);
  font-weight: 560;
}

.hd-09__v {
  font-family: var(--font-display);
  font-size: 1.75rem;
  font-weight: 700;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
  margin-top: .15rem;
}

.hd-09__v span {
  font-size: .95rem;
  color: var(--muted);
}

.hd-09__spark {
  display: block;
  block-size: .4rem;
  margin-top: .7rem;
  border-radius: 999px;
  background: linear-gradient(90deg, var(--accent) 0 62%, var(--s3) 62% 100%);
}

.hd-09__table-wrap {
  margin-top: 1.25rem;
  background: var(--s1);
  border: 1px solid var(--line);
  border-radius: .5rem;
  overflow: hidden;
}

.hd-09__table-wrap h2 {
  font-family: var(--font-display);
  font-size: .92rem;
  font-weight: 660;
  padding: .85rem 1rem;
  border-bottom: 1px solid var(--line);
}

.hd-09__table {
  inline-size: 100%;
  border-collapse: collapse;
  font-size: .85rem;
}

.hd-09__table th {
  text-align: start;
  padding: .6rem 1rem;
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--muted);
  background: var(--s2);
  border-bottom: 1px solid var(--line);
}

.hd-09__table td {
  padding: .65rem 1rem;
  border-bottom: 1px solid var(--line);
  font-variant-numeric: tabular-nums;
}

.hd-09__table tbody tr:last-child td {
  border-bottom: 0;
}

.hd-09__table tbody tr:hover {
  background: var(--s2);
}

.hd-09__filler {
  block-size: 50vh;
}

@media (max-width: 860px) {
  .hd-09__nav {
    display: none;
  }

  .hd-09__who-t {
    display: none;
  }
}

@media (max-width: 620px) {
  .hd-09__row2 {
    flex-wrap: wrap;
  }

  .hd-09__actions {
    margin-inline-start: 0;
    inline-size: 100%;
  }

  .hd-09__btn {
    flex: 1;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-09:has(#hd-09-dark:checked) {
  --s1: #111823;
  --s2: #0c111a;
  --s3: #1a2432;
  --ink: #e9eff8;
  --muted: #8fa0b8;
  --line: #22303f;
  --accent: #5aa9f5;
  --accent-soft: rgba(90,169,245,.16);
  --accent-ink: #08131f;
}
/* icon: shows the scheme the toggle will switch you to */

.hd-09__sun {
  display: none;
}

.hd-09:has(#hd-09-dark:checked) .hd-09__moon {
  display: none;
}

.hd-09:has(#hd-09-dark:checked) .hd-09__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .hd-09:not([data-theme="light"]):not(:has(#hd-09-dark:checked)) {
    --s1: #111823;
    --s2: #0c111a;
    --s3: #1a2432;
    --ink: #e9eff8;
    --muted: #8fa0b8;
    --line: #22303f;
    --accent: #5aa9f5;
    --accent-soft: rgba(90,169,245,.16);
    --accent-ink: #08131f;
  }
  /* FLIP-BACK — dark OS + checked toggle returns to the other scheme */

  .hd-09:has(#hd-09-dark:checked) {
    --s1: #ffffff;
    --s2: #f4f7fb;
    --s3: #e8eef7;
    --ink: #0f1b2d;
    --muted: #5a6b83;
    --line: #dbe4f0;
    --accent: #0b6bcb;
    --accent-soft: #e8f1fd;
    --accent-ink: #ffffff;
    --row1: 3.5rem;
    --font-display: system-ui,-apple-system,"Segoe UI Variable","Segoe UI",sans-serif;
    --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  }
  /* the icon always offers the scheme you are not in */

  .hd-09:not([data-theme="light"]):not(:has(#hd-09-dark:checked)) .hd-09__moon {
    display: none;
  }

  .hd-09:not([data-theme="light"]):not(:has(#hd-09-dark:checked)) .hd-09__sun {
    display: block;
  }

  .hd-09:has(#hd-09-dark:checked) .hd-09__sun {
    display: none;
  }

  .hd-09:has(#hd-09-dark:checked) .hd-09__moon {
    display: block;
  }
}

.hd-09[data-theme="dark"] {
  --s1: #111823;
  --s2: #0c111a;
  --s3: #1a2432;
  --ink: #e9eff8;
  --muted: #8fa0b8;
  --line: #22303f;
  --accent: #5aa9f5;
  --accent-soft: rgba(90,169,245,.16);
  --accent-ink: #08131f;
}

@media (prefers-reduced-motion: reduce) {
  .hd-09 * {
    transition-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-09__pop {
    border: 1px solid CanvasText;
  }
}
/* ── theme toggle — visually hidden checkbox, zero JS ────────────── */

.hd-09__sr,
.hd-09__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-09__theme {
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

.hd-09__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-09__theme:hover {
  background: rgba(128,128,128,.16);
}

.hd-09:has(#hd-09-dark:focus-visible) .hd-09__theme {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```
