---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/docs-site-header-with-version-and-search/"
title: "Docs Site Header with Version and Search"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "A documentation header that carries the three controls docs readers actually hunt for: the version switcher, the search field with its keyboard hint, and the…"
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Docs Site Header with Version and Search
Source: https://codefronts.com/layouts/css-header-designs/docs-site-header-with-version-and-search/

A documentation header that carries the three controls docs readers actually hunt for: the version switcher, the search field with its keyboard hint, and the Docs / API / Blog / GitHub row. The version dropdown opens on hover and on :focus-within, so it is fully keyboard operable without a line of script, and each release row shows its channel chip — Latest, LTS, Maintenance.
## HTML
```html
<div class="hd-02">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;600;700&display=swap">
  <a class="hd-02__skip" href="#hd-02-main">Skip to content</a>

  <header class="hd-02__bar">
    <div class="hd-02__left">
      <a class="hd-02__brand" href="#hd-02-main" aria-label="Meridian documentation home">
        <svg class="hd-02__mark" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false">
          <rect x="3" y="3" width="18" height="18" rx="5" stroke="currentColor" stroke-width="1.8"/>
          <path d="M7.5 15.5V9l4.5 4.2L16.5 9v6.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <span class="hd-02__word">meridian<span class="hd-02__word-dim">/docs</span></span>
      </a>

      <div class="hd-02__ver">
        <button class="hd-02__ver-btn" type="button" aria-haspopup="menu">
          <span class="hd-02__ver-num">v3.4.2</span>
          <span class="hd-02__chip hd-02__chip--ok">Latest</span>
          <svg class="hd-02__chev" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6.5 9.5 12 15l5.5-5.5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        <ul class="hd-02__ver-panel" role="menu" aria-label="Choose a documentation version">
          <li role="none"><a role="menuitem" href="#hd-02-main" aria-current="true"><span>v3.4.2</span><span class="hd-02__chip hd-02__chip--ok">Latest</span></a></li>
          <li role="none"><a role="menuitem" href="#hd-02-main"><span>v3.3.8</span><span class="hd-02__chip">Stable</span></a></li>
          <li role="none"><a role="menuitem" href="#hd-02-main"><span>v3.0.14</span><span class="hd-02__chip hd-02__chip--lts">LTS</span></a></li>
          <li role="none"><a role="menuitem" href="#hd-02-main"><span>v2.9.4</span><span class="hd-02__chip hd-02__chip--old">Maintenance</span></a></li>
          <li role="none" class="hd-02__ver-all"><a role="menuitem" href="#hd-02-main">All releases &#8594;</a></li>
        </ul>
      </div>
    </div>

    <label class="hd-02__search" for="hd-02-q">
      <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.8 15.8 21 21" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      <input class="hd-02__q" id="hd-02-q" type="text" placeholder="Search the docs" aria-label="Search the documentation">
      <kbd class="hd-02__kbd">/</kbd>
    </label>

    <div class="hd-02__right">
      <nav class="hd-02__nav" aria-label="Main">
        <ul>
          <li><a href="#hd-02-main" aria-current="page">Docs</a></li>
          <li><a href="#hd-02-main">API</a></li>
          <li><a href="#hd-02-main">Blog</a></li>
        </ul>
      </nav>
      <span class="hd-02__rule" aria-hidden="true"></span>
      <a class="hd-02__gh" href="#hd-02-main" aria-label="Meridian on GitHub">
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" focusable="false"><path d="M12 2a10 10 0 0 0-3.16 19.49c.5.09.68-.22.68-.48v-1.7c-2.78.6-3.37-1.34-3.37-1.34-.45-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.6.07-.6 1 .07 1.53 1.03 1.53 1.03.89 1.53 2.34 1.09 2.91.83.09-.65.35-1.09.63-1.34-2.22-.25-4.55-1.11-4.55-4.94 0-1.09.39-1.98 1.03-2.68-.1-.25-.45-1.27.1-2.65 0 0 .83-.27 2.73 1.02a9.4 9.4 0 0 1 4.98 0c1.9-1.29 2.73-1.02 2.73-1.02.55 1.38.2 2.4.1 2.65.64.7 1.03 1.59 1.03 2.68 0 3.84-2.34 4.68-4.57 4.93.36.31.68.92.68 1.85v2.74c0 .27.18.58.69.48A10 10 0 0 0 12 2Z"/></svg>
      </a>
      <input class="hd-02__sr" type="checkbox" id="hd-02-dark">
      <label class="hd-02__theme" for="hd-02-dark">
        <svg class="hd-02__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <svg class="hd-02__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <span class="hd-02__vh">Switch light or dark theme</span>
      </label>
    </div>
  </header>

  <div class="hd-02__shell">
    <nav class="hd-02__side" aria-label="Documentation sections">
      <p class="hd-02__side-h">Getting started</p>
      <ul>
        <li><a href="#hd-02-main">Installation</a></li>
        <li><a href="#hd-02-main" aria-current="page">Project structure</a></li>
        <li><a href="#hd-02-main">Configuration</a></li>
      </ul>
      <p class="hd-02__side-h">Core concepts</p>
      <ul>
        <li><a href="#hd-02-main">Routing</a></li>
        <li><a href="#hd-02-main">Data loading</a></li>
        <li><a href="#hd-02-main">Caching</a></li>
        <li><a href="#hd-02-main">Middleware</a></li>
      </ul>
    </nav>

    <main class="hd-02__main" id="hd-02-main">
      <p class="hd-02__crumb">Getting started <span aria-hidden="true">/</span> Project structure</p>
      <h1>Project structure</h1>
      <p class="hd-02__lead">Every Meridian app starts from four directories. The generator writes them for you; this page explains what belongs where and which files are safe to delete.</p>
      <div class="hd-02__note">
        <strong>Version note.</strong> Paths changed in v3.4 &mdash; use the version switcher in the header to read the v2.9 layout.
      </div>
      <h2>Directory layout</h2>
      <pre class="hd-02__pre"><code>app/
  routes/       route modules, one file per URL segment
  server/       loaders, actions and edge middleware
  ui/           components, tokens and the design layer
public/         static assets served verbatim</code></pre>
      <p>Route modules are discovered at build time, so adding a file is all it takes to add a URL. Nothing imports from <code>routes/</code> except the generated manifest.</p>
      <h2>What to commit</h2>
      <p>Commit everything except <code>.meridian/</code>. The cache directory is derived and rebuilds in about 400&nbsp;ms on a cold install.</p>
      <div class="hd-02__filler" aria-hidden="true"></div>
    </main>
  </div>
</div>
```
## CSS
```css
.hd-02 {
  --bg: #faf8f4;
  --panel: #ffffff;
  --panel2: #f3f0e9;
  --ink: #1a1a17;
  --muted: #6b6a63;
  --line: rgba(26,26,23,.12);
  --line2: rgba(26,26,23,.2);
  --accent: #0f766e;
  --accent-soft: rgba(15,118,110,.1);
  --accent-ink: #ffffff;
  --chip-ok: #0f766e;
  --chip-lts: #7c5c12;
  --chip-old: #8a5a4a;
  --font-display: "JetBrains Mono",ui-monospace,"IBM Plex Mono",monospace;
  --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  --search-w: 22rem;
  width: 100%;
  min-height: 100vh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.6;
}

@supports (color: oklch(50% .1 200)) {
  .hd-02 {
    --bg: oklch(97.5% .012 85);
    --panel: oklch(100% 0 0);
    --panel2: oklch(95% .015 85);
    --ink: oklch(20% .01 80);
    --muted: oklch(52% .012 80);
    --accent: oklch(52% .09 175);
  }
}

.hd-02 * {
  box-sizing: border-box;
}

.hd-02 h1,
.hd-02 h2,
.hd-02 p,
.hd-02 ul,
.hd-02 pre {
  margin: 0;
  padding: 0;
}

.hd-02 ul {
  list-style: none;
}

.hd-02 [hidden] {
  display: none;
}

.hd-02 :focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.hd-02__vh,
.hd-02__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-02__skip {
  position: absolute;
  inset-inline-start: .75rem;
  top: -3rem;
  z-index: 60;
  padding: .55rem 1rem;
  background: var(--accent);
  color: var(--accent-ink);
  border-radius: .4rem;
  font-size: .82rem;
  font-weight: 600;
  text-decoration: none;
  transition: top .18s ease;
}

.hd-02__skip:focus-visible {
  top: .75rem;
}
/* ── header: hairline dividers, no shadow ─────────────────────────── */

.hd-02__bar {
  position: sticky;
  top: 0;
  z-index: 30;
  display: grid;
  grid-template-columns: auto minmax(0,1fr) auto;
  align-items: center;
  gap: 1rem;
  padding: .7rem clamp(.75rem,3vw,1.5rem);
  background: color-mix(in srgb, var(--bg) 92%, transparent);
  border-bottom: 1px solid var(--line);
  backdrop-filter: blur(10px);
}

.hd-02__left {
  display: flex;
  align-items: center;
  gap: .85rem;
  min-inline-size: 0;
}

.hd-02__brand {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  text-decoration: none;
  color: var(--ink);
  min-inline-size: 0;
}

.hd-02__mark {
  inline-size: 1.5rem;
  block-size: 1.5rem;
  color: var(--accent);
  flex: none;
}

.hd-02__word {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: .98rem;
  letter-spacing: -.03em;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-02__word-dim {
  color: var(--muted);
  font-weight: 500;
}

.hd-02__ver {
  position: relative;
}

.hd-02__ver-btn {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-block-size: 2.2rem;
  padding: .3rem .5rem .3rem .6rem;
  border: 1px solid var(--line);
  border-radius: .45rem;
  background: var(--panel);
  color: var(--ink);
  font: inherit;
  font-size: .8rem;
  cursor: pointer;
  transition: border-color .15s ease, background-color .15s ease;
}

.hd-02__ver-btn:hover {
  border-color: var(--line2);
  background: var(--panel2);
}

.hd-02__ver-num {
  font-family: var(--font-display);
  font-weight: 600;
}

.hd-02__chev {
  inline-size: .85rem;
  block-size: .85rem;
  color: var(--muted);
  transition: rotate .18s ease;
}

.hd-02__ver:hover .hd-02__chev,
.hd-02__ver:focus-within .hd-02__chev {
  rotate: 180deg;
}

.hd-02__chip {
  font-size: .62rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  padding: .16rem .34rem;
  border-radius: .25rem;
  background: var(--panel2);
  color: var(--muted);
  flex: none;
}

.hd-02__chip--ok {
  background: var(--accent-soft);
  color: var(--chip-ok);
}

.hd-02__chip--lts {
  background: rgba(124,92,18,.12);
  color: var(--chip-lts);
}

.hd-02__chip--old {
  background: rgba(138,90,74,.12);
  color: var(--chip-old);
}

.hd-02__ver-panel {
  position: absolute;
  inset-inline-start: 0;
  top: calc(100% + .45rem);
  z-index: 40;
  inline-size: 15rem;
  padding: .3rem;
  border: 1px solid var(--line2);
  border-radius: .55rem;
  background: var(--panel);
  box-shadow: 0 1rem 2rem -1rem rgba(26,26,23,.28);
  visibility: hidden;
  opacity: 0;
  translate: 0 -.35rem;
  transition: opacity .16s ease, translate .16s ease, visibility .16s allow-discrete;
}

.hd-02__ver:hover .hd-02__ver-panel,
.hd-02__ver:focus-within .hd-02__ver-panel {
  visibility: visible;
  opacity: 1;
  translate: 0 0;
}

.hd-02__ver-panel a {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .5rem;
  min-block-size: 2.3rem;
  padding: .4rem .55rem;
  border-radius: .4rem;
  text-decoration: none;
  color: var(--ink);
  font-family: var(--font-display);
  font-size: .8rem;
  font-weight: 600;
}

.hd-02__ver-panel a:hover {
  background: var(--panel2);
}

.hd-02__ver-panel a[aria-current="true"] {
  background: var(--accent-soft);
  color: var(--accent);
}

.hd-02__ver-all {
  border-top: 1px solid var(--line);
  margin-top: .25rem;
  padding-top: .25rem;
}

.hd-02__ver-all a {
  font-family: var(--font-body);
  font-weight: 550;
  font-size: .78rem;
  color: var(--muted);
}

.hd-02__search {
  display: flex;
  align-items: center;
  gap: .5rem;
  inline-size: 100%;
  max-inline-size: var(--search-w);
  margin-inline: auto;
  min-block-size: 2.35rem;
  padding: .35rem .5rem .35rem .65rem;
  border: 1px solid var(--line);
  border-radius: .45rem;
  background: var(--panel);
  box-shadow: inset 0 1px 0 rgba(26,26,23,.04);
  cursor: text;
  transition: border-color .15s ease, box-shadow .15s ease;
}

.hd-02__search svg {
  inline-size: 1rem;
  block-size: 1rem;
  color: var(--muted);
  flex: none;
}

.hd-02__q {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: transparent;
  color: var(--ink);
  font: inherit;
  font-size: .86rem;
}

.hd-02__q::placeholder {
  color: var(--muted);
}

.hd-02__q:focus {
  outline: none;
}

.hd-02__search:focus-within {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px var(--accent-soft);
}

.hd-02__kbd {
  font-family: var(--font-display);
  font-size: .68rem;
  padding: .2rem .4rem;
  border: 1px solid var(--line);
  border-radius: .25rem;
  color: var(--muted);
  background: var(--panel2);
  flex: none;
}

.hd-02__right {
  display: flex;
  align-items: center;
  gap: .5rem;
}

.hd-02__nav ul {
  display: flex;
  align-items: center;
  gap: .1rem;
}

.hd-02__nav a {
  display: block;
  padding: .4rem .55rem;
  border-radius: .35rem;
  color: var(--muted);
  text-decoration: none;
  font-size: .85rem;
  font-weight: 540;
  white-space: nowrap;
  transition: color .15s ease;
}

.hd-02__nav a:hover {
  color: var(--ink);
}

.hd-02__nav a[aria-current="page"] {
  color: var(--accent);
  font-weight: 620;
}

.hd-02__rule {
  inline-size: 1px;
  block-size: 1.2rem;
  background: var(--line);
}

.hd-02__gh,
.hd-02__theme {
  display: grid;
  place-items: center;
  inline-size: 2.2rem;
  block-size: 2.2rem;
  border-radius: .4rem;
  color: var(--muted);
  cursor: pointer;
  transition: color .15s ease, background-color .15s ease;
}

.hd-02__gh svg,
.hd-02__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-02__gh:hover,
.hd-02__theme:hover {
  color: var(--ink);
  background: var(--panel2);
}

.hd-02:has(#hd-02-dark:focus-visible) .hd-02__theme {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
/* ── docs shell ───────────────────────────────────────────────────── */

.hd-02__shell {
  display: grid;
  grid-template-columns: 15rem minmax(0,1fr);
  gap: clamp(1rem,4vw,3rem);
  max-inline-size: 80rem;
  margin-inline: auto;
  padding: clamp(1.25rem,4vw,2.5rem) clamp(1rem,3vw,1.5rem) 4rem;
}

.hd-02__side {
  position: sticky;
  top: 5rem;
  align-self: start;
  border-inline-start: 1px solid var(--line);
  padding-inline-start: 1rem;
}

.hd-02__side-h {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
  margin: 1.1rem 0 .4rem;
}

.hd-02__side-h:first-child {
  margin-top: 0;
}

.hd-02__side a {
  display: block;
  padding: .28rem 0;
  color: var(--muted);
  text-decoration: none;
  font-size: .87rem;
}

.hd-02__side a:hover {
  color: var(--ink);
}

.hd-02__side a[aria-current="page"] {
  color: var(--accent);
  font-weight: 620;
}

.hd-02__main {
  min-inline-size: 0;
}

.hd-02__crumb {
  font-size: .78rem;
  color: var(--muted);
  font-family: var(--font-display);
}

.hd-02__main h1 {
  font-family: var(--font-display);
  font-size: clamp(1.7rem,4.5vw,2.5rem);
  letter-spacing: -.04em;
  font-weight: 700;
  margin: .5rem 0 0;
}

.hd-02__main h2 {
  font-family: var(--font-display);
  font-size: 1.1rem;
  letter-spacing: -.02em;
  margin: 2rem 0 .6rem;
}

.hd-02__lead {
  margin-top: .8rem;
  max-inline-size: 62ch;
  color: var(--muted);
  font-size: 1.02rem;
  text-wrap: pretty;
}

.hd-02__main p {
  max-inline-size: 66ch;
  text-wrap: pretty;
}

.hd-02__main p + p {
  margin-top: .8rem;
}

.hd-02__note {
  margin: 1.5rem 0 0;
  padding: .85rem 1rem;
  border: 1px solid var(--line);
  border-inline-start: 3px solid var(--accent);
  border-radius: .4rem;
  background: var(--accent-soft);
  font-size: .9rem;
  max-inline-size: 66ch;
}

.hd-02__pre {
  margin-top: .5rem;
  padding: 1rem;
  overflow: auto;
  border: 1px solid var(--line);
  border-radius: .5rem;
  background: var(--panel);
  font-family: var(--font-display);
  font-size: .82rem;
  line-height: 1.7;
}

.hd-02__main code {
  font-family: var(--font-display);
  font-size: .9em;
}

.hd-02__filler {
  block-size: 55vh;
}

@media (max-width: 1000px) {
  .hd-02__shell {
    grid-template-columns: minmax(0,1fr);
  }

  .hd-02__side {
    position: static;
    display: none;
  }

  .hd-02__nav {
    display: none;
  }
}

@media (max-width: 680px) {
  .hd-02__bar {
    grid-template-columns: minmax(0,1fr) auto;
  }

  .hd-02__search {
    grid-column: 1/-1;
    order: 3;
    max-inline-size: none;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-02:has(#hd-02-dark:checked) {
  --bg: #14140f;
  --panel: #1c1c16;
  --panel2: #26261e;
  --ink: #f2f0e8;
  --muted: #a3a094;
  --line: rgba(242,240,232,.12);
  --line2: rgba(242,240,232,.2);
  --accent: #5eead4;
  --accent-soft: rgba(94,234,212,.14);
  --accent-ink: #0b1f1c;
}
/* icon: shows the scheme the toggle will switch you to */

.hd-02__sun {
  display: none;
}

.hd-02:has(#hd-02-dark:checked) .hd-02__moon {
  display: none;
}

.hd-02:has(#hd-02-dark:checked) .hd-02__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .hd-02:not([data-theme="light"]):not(:has(#hd-02-dark:checked)) {
    --bg: #14140f;
    --panel: #1c1c16;
    --panel2: #26261e;
    --ink: #f2f0e8;
    --muted: #a3a094;
    --line: rgba(242,240,232,.12);
    --line2: rgba(242,240,232,.2);
    --accent: #5eead4;
    --accent-soft: rgba(94,234,212,.14);
    --accent-ink: #0b1f1c;
    --chip-ok: #5eead4;
    --chip-lts: #e4c169;
    --chip-old: #d6a08c;
  }
  /* FLIP-BACK — dark OS + checked toggle restores the light surface */

  .hd-02:has(#hd-02-dark:checked) {
    --bg: #faf8f4;
    --panel: #ffffff;
    --panel2: #f3f0e9;
    --ink: #1a1a17;
    --muted: #6b6a63;
    --line: rgba(26,26,23,.12);
    --line2: rgba(26,26,23,.2);
    --accent: #0f766e;
    --accent-soft: rgba(15,118,110,.1);
    --accent-ink: #ffffff;
    --chip-ok: #0f766e;
    --chip-lts: #7c5c12;
    --chip-old: #8a5a4a;
  }
  /* the icon always offers the scheme you are not in */

  .hd-02:not([data-theme="light"]):not(:has(#hd-02-dark:checked)) .hd-02__moon {
    display: none;
  }

  .hd-02:not([data-theme="light"]):not(:has(#hd-02-dark:checked)) .hd-02__sun {
    display: block;
  }

  .hd-02:has(#hd-02-dark:checked) .hd-02__sun {
    display: none;
  }

  .hd-02:has(#hd-02-dark:checked) .hd-02__moon {
    display: block;
  }
}

.hd-02[data-theme="dark"] {
  --bg: #14140f;
  --panel: #1c1c16;
  --panel2: #26261e;
  --ink: #f2f0e8;
  --muted: #a3a094;
  --line: rgba(242,240,232,.12);
  --line2: rgba(242,240,232,.2);
  --accent: #5eead4;
  --accent-soft: rgba(94,234,212,.14);
  --accent-ink: #0b1f1c;
}

@media (prefers-reduced-motion: reduce) {
  .hd-02 * {
    transition-duration: 1ms !important;
    animation-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-02__ver-panel,
    .hd-02__search {
    border: 1px solid CanvasText;
  }
}
```
