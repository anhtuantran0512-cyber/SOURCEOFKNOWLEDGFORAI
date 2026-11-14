---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/flexbox-3-column-navbar-header/"
title: "Flexbox Three Column Navbar Header"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "The reference implementation: logo left, nav optically centred, actions right &mdash; and it stays centred even when the logo and the button are wildly…"
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Flexbox Three Column Navbar Header
Source: https://codefronts.com/layouts/css-header-designs/flexbox-3-column-navbar-header/

The reference implementation: logo left, nav optically centred, actions right &mdash; and it stays centred even when the logo and the button are wildly different widths. The trick is giving the outer columns equal flex-basis and letting the nav claim the middle, rather than trusting space-between. Monochrome Swiss treatment, hairline rules, zero decoration.
## HTML
```html
<div class="hd-14">
  <a class="hd-14__skip" href="#hd-14-main">Skip to content</a>

  <header class="hd-14__bar">
    <div class="hd-14__side hd-14__side--start">
      <a class="hd-14__brand" href="#hd-14-main">
        <svg class="hd-14__mark" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false">
          <rect x="3.5" y="3.5" width="7" height="7" fill="currentColor"/>
          <rect x="13.5" y="3.5" width="7" height="7" stroke="currentColor" stroke-width="1.6"/>
          <rect x="3.5" y="13.5" width="7" height="7" stroke="currentColor" stroke-width="1.6"/>
          <rect x="13.5" y="13.5" width="7" height="7" fill="currentColor"/>
        </svg>
        <span class="hd-14__word">Grid &amp; Rule</span>
      </a>
    </div>

    <nav class="hd-14__nav" aria-label="Main">
      <ul>
        <li><a href="#hd-14-main" aria-current="page">Work</a></li>
        <li><a href="#hd-14-main">Studio</a></li>
        <li><a href="#hd-14-main">Writing</a></li>
        <li><a href="#hd-14-main">Contact</a></li>
      </ul>
    </nav>

    <div class="hd-14__side hd-14__side--end">
      <input class="hd-14__sr" type="checkbox" id="hd-14-dark">
      <label class="hd-14__theme" for="hd-14-dark">
        <svg class="hd-14__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <svg class="hd-14__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <span class="hd-14__vh">Switch light or dark theme</span>
      </label>
      <input class="hd-14__sr" type="checkbox" id="hd-14-guides">
      <label class="hd-14__guide-btn" for="hd-14-guides">Show tracks</label>
      <a class="hd-14__cta" href="#hd-14-main">Start a project</a>
    </div>
  </header>

  <main class="hd-14__main" id="hd-14-main">
    <p class="hd-14__eyebrow">Layout reference &middot; 01</p>
    <h1>Three columns, one centred nav, no drift.</h1>
    <p class="hd-14__lead">Toggle <strong>Show tracks</strong> in the header to outline the flex columns. The side columns share slack equally, so the navigation stays optically centred no matter how long the wordmark or the button gets.</p>

    <div class="hd-14__code">
      <p class="hd-14__code-h">The whole layout</p>
      <pre><code>.bar   { display:flex; align-items:center; }
.side  { flex:1 1 0; min-inline-size:0; }
.side--start { justify-content:flex-start; }
.side--end   { justify-content:flex-end;   }
.nav   { flex:0 1 auto; }</code></pre>
    </div>

    <dl class="hd-14__notes">
      <div><dt>flex-basis: 0</dt><dd>Both sides start from zero, so growth is symmetrical and the middle track is the true centre.</dd></div>
      <div><dt>min-inline-size: 0</dt><dd>Lets a long wordmark truncate instead of setting a floor for the whole row.</dd></div>
      <div><dt>flex: 0 1 auto</dt><dd>The nav keeps its natural width and only shrinks when there is genuinely no room.</dd></div>
    </dl>
    <div class="hd-14__filler" aria-hidden="true"></div>
  </main>
</div>
```
## CSS
```css
.hd-14 {
  --paper: #ffffff;
  --paper2: #f5f5f5;
  --ink: #0a0a0a;
  --muted: #6b6b6b;
  --line: #0a0a0a;
  --hair: rgba(10,10,10,.14);
  --guide: #0a0a0a;
  --track: .14em;
  --bar-h: 4.25rem;
  --font-display: system-ui,-apple-system,"Helvetica Neue",Helvetica,sans-serif;
  --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  background-color: var(--paper);
  background-image: repeating-linear-gradient(to bottom, var(--hair) 0 1px, transparent 1px 8px);
  background-size: 100% 8px;
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.55;
}

@supports (color: oklch(50% .1 200)) {
  .hd-14 {
    --paper: oklch(100% 0 0);
    --paper2: oklch(96% 0 0);
    --ink: oklch(12% 0 0);
    --muted: oklch(50% 0 0);
  }
}

.hd-14 * {
  box-sizing: border-box;
}

.hd-14 h1,
.hd-14 p,
.hd-14 ul,
.hd-14 dl,
.hd-14 dt,
.hd-14 dd,
.hd-14 pre {
  margin: 0;
  padding: 0;
}

.hd-14 ul {
  list-style: none;
}

.hd-14 [hidden] {
  display: none;
}

.hd-14 :focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.hd-14__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.hd-14__skip {
  position: absolute;
  inset-inline-start: 1rem;
  top: -3rem;
  z-index: 60;
  padding: .5rem .9rem;
  background: var(--ink);
  color: var(--paper);
  font-size: .76rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  text-decoration: none;
  transition: top .18s ease;
}

.hd-14__skip:focus-visible {
  top: .75rem;
}
/* ── the three-column flex header ─────────────────────────────────── */

.hd-14__bar {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  gap: 1rem;
  min-block-size: var(--bar-h);
  padding-inline: clamp(1rem,4vw,2.5rem);
  background: var(--paper);
  border-bottom: 1px solid var(--line);
}

.hd-14__side {
  display: flex;
  align-items: center;
  gap: .75rem;
  flex: 1 1 0;
  min-inline-size: 0;
}

.hd-14__side--start {
  justify-content: flex-start;
}

.hd-14__side--end {
  justify-content: flex-end;
}

.hd-14__nav {
  flex: 0 1 auto;
  min-inline-size: 0;
}

.hd-14__brand {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  color: var(--ink);
  text-decoration: none;
  min-inline-size: 0;
}

.hd-14__mark {
  inline-size: 1.4rem;
  block-size: 1.4rem;
  flex: none;
}

.hd-14__word {
  font-family: var(--font-display);
  font-size: .8rem;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-14__nav ul {
  display: flex;
  align-items: center;
  gap: clamp(1rem,3vw,2rem);
}

.hd-14__nav a {
  display: block;
  padding: .5rem 0;
  color: var(--muted);
  text-decoration: none;
  font-size: .76rem;
  font-weight: 640;
  letter-spacing: var(--track);
  text-transform: uppercase;
  white-space: nowrap;
  border-bottom: 1px solid transparent;
  transition: color .16s ease, border-color .16s ease;
}

.hd-14__nav a:hover {
  color: var(--ink);
  border-bottom-color: var(--ink);
}

.hd-14__nav a[aria-current="page"] {
  color: var(--ink);
  border-bottom-color: var(--ink);
}

.hd-14__guide-btn {
  padding: .5rem .75rem;
  border: 1px solid var(--hair);
  color: var(--muted);
  font-size: .68rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  cursor: pointer;
  white-space: nowrap;
  transition: color .16s ease, border-color .16s ease;
}

.hd-14__guide-btn:hover {
  color: var(--ink);
  border-color: var(--ink);
}

.hd-14:has(#hd-14-guides:checked) .hd-14__guide-btn {
  background: var(--ink);
  color: var(--paper);
  border-color: var(--ink);
}

.hd-14:has(#hd-14-guides:focus-visible) .hd-14__guide-btn {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.hd-14:has(#hd-14-guides:checked) .hd-14__side,
.hd-14:has(#hd-14-guides:checked) .hd-14__nav {
  outline: 1px dashed var(--guide);
  outline-offset: -1px;
  position: relative;
}

.hd-14:has(#hd-14-guides:checked) .hd-14__side::after,
.hd-14:has(#hd-14-guides:checked) .hd-14__nav::after {
  content: attr(data-track);
  position: absolute;
  top: .1rem;
  inset-inline-start: .15rem;
  font-size: .55rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.hd-14__cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.5rem;
  padding: .6rem 1.1rem;
  background: var(--ink);
  color: var(--paper);
  text-decoration: none;
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  white-space: nowrap;
  transition: opacity .16s ease;
}

.hd-14__cta:hover {
  opacity: .82;
}
/* ── page body ────────────────────────────────────────────────────── */

.hd-14__main {
  max-inline-size: 62rem;
  margin-inline: auto;
  padding: clamp(2.5rem,7vw,4.5rem) clamp(1rem,4vw,2.5rem) 5rem;
}

.hd-14__eyebrow {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--muted);
}

.hd-14__main h1 {
  font-family: var(--font-display);
  font-size: clamp(1.9rem,6vw,3.2rem);
  line-height: 1.05;
  font-weight: 700;
  letter-spacing: -.04em;
  margin-top: 1rem;
  max-inline-size: 24ch;
  text-wrap: balance;
}

.hd-14__lead {
  margin-top: 1.1rem;
  max-inline-size: 56ch;
  color: var(--muted);
  font-size: 1.02rem;
  text-wrap: pretty;
}

.hd-14__code {
  margin-top: 2.25rem;
  border: 1px solid var(--line);
  background: var(--paper);
}

.hd-14__code-h {
  padding: .6rem .9rem;
  border-bottom: 1px solid var(--line);
  font-size: .68rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.hd-14__code pre {
  padding: 1rem .9rem;
  overflow: auto;
  font-family: ui-monospace,Menlo,"Courier New",monospace;
  font-size: .84rem;
  line-height: 1.75;
}

.hd-14__notes {
  display: grid;
  gap: 0;
  margin-top: 2rem;
  border-top: 1px solid var(--line);
}

.hd-14__notes > div {
  display: grid;
  grid-template-columns: 14rem minmax(0,1fr);
  gap: 1.5rem;
  padding: .9rem .1rem;
  border-bottom: 1px solid var(--hair);
}

.hd-14__notes dt {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .82rem;
  font-weight: 600;
}

.hd-14__notes dd {
  font-size: .9rem;
  color: var(--muted);
  text-wrap: pretty;
}

.hd-14__filler {
  block-size: 45vh;
}

@media (max-width: 720px) {
  .hd-14__bar {
    flex-wrap: wrap;
    padding-block: .75rem;
    gap: .6rem;
  }

  .hd-14__side {
    flex: 1 1 auto;
  }

  .hd-14__nav {
    order: 3;
    flex-basis: 100%;
    justify-content: center;
    display: flex;
  }

  .hd-14__nav ul {
    justify-content: center;
    flex-wrap: wrap;
  }

  .hd-14__guide-btn {
    display: none;
  }

  .hd-14__notes > div {
    grid-template-columns: minmax(0,1fr);
    gap: .25rem;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-14:has(#hd-14-dark:checked) {
  --paper: #0a0a0a;
  --paper2: #151515;
  --ink: #f5f5f5;
  --muted: #9b9b9b;
  --line: #f5f5f5;
  --hair: rgba(245,245,245,.14);
  --guide: #f5f5f5;
}

.hd-14:has(#hd-14-dark:checked) {
  background-image: repeating-linear-gradient(to bottom, rgba(245,245,245,.1) 0 1px, transparent 1px 8px);
}
/* icon: shows the scheme the toggle will switch you to */

.hd-14__sun {
  display: none;
}

.hd-14:has(#hd-14-dark:checked) .hd-14__moon {
  display: none;
}

.hd-14:has(#hd-14-dark:checked) .hd-14__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .hd-14:not([data-theme="light"]):not(:has(#hd-14-dark:checked)):not(:has(#hd-14-dark:checked)) {
    --paper: #0a0a0a;
    --paper2: #151515;
    --ink: #f5f5f5;
    --muted: #9b9b9b;
    --line: #f5f5f5;
    --hair: rgba(245,245,245,.14);
    --guide: #f5f5f5;
  }

  .hd-14:not([data-theme="light"]) {
    background-image: repeating-linear-gradient(to bottom, rgba(245,245,245,.1) 0 1px, transparent 1px 8px);
  }
  /* FLIP-BACK — dark OS + checked toggle returns to the other scheme */

  .hd-14:has(#hd-14-dark:checked) {
    --paper: #ffffff;
    --paper2: #f5f5f5;
    --ink: #0a0a0a;
    --muted: #6b6b6b;
    --line: #0a0a0a;
    --hair: rgba(10,10,10,.14);
    --guide: #0a0a0a;
    --track: .14em;
    --bar-h: 4.25rem;
    --font-display: system-ui,-apple-system,"Helvetica Neue",Helvetica,sans-serif;
    --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  }
  /* the icon always offers the scheme you are not in */

  .hd-14:not([data-theme="light"]):not(:has(#hd-14-dark:checked)) .hd-14__moon {
    display: none;
  }

  .hd-14:not([data-theme="light"]):not(:has(#hd-14-dark:checked)) .hd-14__sun {
    display: block;
  }

  .hd-14:has(#hd-14-dark:checked) .hd-14__sun {
    display: none;
  }

  .hd-14:has(#hd-14-dark:checked) .hd-14__moon {
    display: block;
  }
}

.hd-14[data-theme="dark"] {
  --paper: #0a0a0a;
  --paper2: #151515;
  --ink: #f5f5f5;
  --muted: #9b9b9b;
  --line: #f5f5f5;
  --hair: rgba(245,245,245,.14);
  --guide: #f5f5f5;
}

@media (prefers-reduced-motion: reduce) {
  .hd-14 * {
    transition-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-14__cta {
    border: 1px solid CanvasText;
  }
}
/* ── theme toggle — visually hidden checkbox, zero JS ────────────── */

.hd-14__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-14__theme {
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

.hd-14__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-14__theme:hover {
  background: rgba(128,128,128,.16);
}

.hd-14:has(#hd-14-dark:focus-visible) .hd-14__theme {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```
