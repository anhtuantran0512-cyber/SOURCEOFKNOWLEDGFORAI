---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/command-palette-trigger-header-with-k-shortcut/"
title: "Command Palette Trigger Header with ⌘K Shortcut"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "The header pattern every developer tool ships in 2027: a muted search pill in the middle of the bar with a ⌘K badge pinned to its right end."
has_js: "true"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Command Palette Trigger Header with ⌘K Shortcut
Source: https://codefronts.com/layouts/css-header-designs/command-palette-trigger-header-with-k-shortcut/

The header pattern every developer tool ships in 2027: a muted search pill in the middle of the bar with a ⌘K badge pinned to its right end. Clicking or tabbing to the pill opens a full command palette — recents, quick actions, help — that scales and fades in. The open/close is pure CSS state; the only script is a fourteen-line keyboard listener so the shortcut works from anywhere on the page.
## HTML
```html
<div class="hd-01">
  <a class="hd-01__skip" href="#hd-01-main">Skip to content</a>

  <header class="hd-01__bar">
    <a class="hd-01__brand" href="#hd-01-main" aria-label="Halcyon home">
      <svg class="hd-01__mark" viewBox="0 0 28 28" fill="none" aria-hidden="true" focusable="false">
        <path d="M14 2.6 24.4 8.6v11.8L14 26.4 3.6 20.4V8.6L14 2.6Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/>
        <path d="M9.2 17.6 14 9.4l4.8 8.2H9.2Z" fill="currentColor"/>
      </svg>
      <span class="hd-01__word">Halcyon</span>
    </a>

    <nav class="hd-01__nav" aria-label="Main">
      <ul class="hd-01__nav-list">
        <li><a href="#hd-01-main" aria-current="page">Product</a></li>
        <li><a href="#hd-01-main">Docs</a></li>
        <li><a href="#hd-01-main">Changelog</a></li>
        <li><a href="#hd-01-main">Pricing</a></li>
      </ul>
    </nav>

    <span class="hd-01__cmd">
      <input class="hd-01__probe" type="checkbox" id="hd-01-open" aria-label="Open command palette" aria-haspopup="dialog">
      <span class="hd-01__cmd-face" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.8 15.8 21 21" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <span class="hd-01__cmd-text">Search or jump to&hellip;</span>
        <kbd class="hd-01__kbd">&#8984;K</kbd>
      </span>
    </span>

    <div class="hd-01__utility">
      <input class="hd-01__sr" type="checkbox" id="hd-01-light">
      <label class="hd-01__theme" for="hd-01-light">
        <svg class="hd-01__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <svg class="hd-01__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <span class="hd-01__vh">Switch light or dark theme</span>
      </label>
      <a class="hd-01__ghost" href="#hd-01-main">Sign in</a>
      <a class="hd-01__cta" href="#hd-01-main">Get started</a>
    </div>
  </header>

  <div class="hd-01__overlay">
    <label class="hd-01__scrim" for="hd-01-open" aria-label="Close command palette"></label>
    <div class="hd-01__panel" role="dialog" aria-label="Command palette" aria-modal="true">
      <div class="hd-01__field">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.8 15.8 21 21" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
        <input class="hd-01__input" type="text" placeholder="Type a command or search projects" aria-label="Command or search">
        <label class="hd-01__esc" for="hd-01-open">esc</label>
      </div>

      <div class="hd-01__scroll">
        <p class="hd-01__group" id="hd-01-g1">Recent</p>
        <ul class="hd-01__list" role="menu" aria-labelledby="hd-01-g1">
          <li role="none" style="--i:1"><button class="hd-01__row" type="button" role="menuitem"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="4" y="4.5" width="16" height="15" rx="2.6" stroke="currentColor" stroke-width="1.7"/><path d="M8 9.5h8M8 13.5h5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg><span>Q3 pricing experiment</span><span class="hd-01__meta">Project</span></button></li>
          <li role="none" style="--i:2"><button class="hd-01__row" type="button" role="menuitem"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5 19.5 9v6L12 19.5 4.5 15V9L12 4.5Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg><span>Deploy pipeline &mdash; edge regions</span><span class="hd-01__meta">Doc</span></button></li>
          <li role="none" style="--i:3"><button class="hd-01__row" type="button" role="menuitem"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="8.6" r="3.6" stroke="currentColor" stroke-width="1.7"/><path d="M5.4 19.4a6.8 6.8 0 0 1 13.2 0" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg><span>Priya Sharma</span><span class="hd-01__meta">Teammate</span></button></li>
        </ul>

        <p class="hd-01__group" id="hd-01-g2">Actions</p>
        <ul class="hd-01__list" role="menu" aria-labelledby="hd-01-g2">
          <li role="none" style="--i:4"><button class="hd-01__row" type="button" role="menuitem"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg><span>New project</span><kbd class="hd-01__kbd hd-01__kbd--dim">N</kbd></button></li>
          <li role="none" style="--i:5"><button class="hd-01__row" type="button" role="menuitem"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 12h15M13 6.5l6 5.5-6 5.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Invite teammate</span><kbd class="hd-01__kbd hd-01__kbd--dim">I</kbd></button></li>
          <li role="none" style="--i:6"><button class="hd-01__row" type="button" role="menuitem"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="3.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.4v2.2M12 18.4v2.2M3.4 12h2.2M18.4 12h2.2M6 6l1.6 1.6M16.4 16.4 18 18M18 6l-1.6 1.6M7.6 16.4 6 18" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg><span>Toggle appearance</span><kbd class="hd-01__kbd hd-01__kbd--dim">T</kbd></button></li>
        </ul>

        <p class="hd-01__group" id="hd-01-g3">Help</p>
        <ul class="hd-01__list" role="menu" aria-labelledby="hd-01-g3">
          <li role="none" style="--i:7"><button class="hd-01__row" type="button" role="menuitem"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.2" stroke="currentColor" stroke-width="1.7"/><path d="M9.8 9.6a2.3 2.3 0 1 1 3.4 2.1c-.8.5-1.2 1-1.2 1.9M12 16.6h.01" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg><span>Keyboard shortcuts</span><span class="hd-01__meta">Help</span></button></li>
        </ul>
      </div>

      <p class="hd-01__foot"><kbd class="hd-01__kbd hd-01__kbd--dim">&#8593;</kbd><kbd class="hd-01__kbd hd-01__kbd--dim">&#8595;</kbd> to navigate <span class="hd-01__sep"></span> <kbd class="hd-01__kbd hd-01__kbd--dim">&#8629;</kbd> to select</p>
    </div>
  </div>

  <main class="hd-01__main" id="hd-01-main">
    <section class="hd-01__hero">
      <p class="hd-01__eyebrow">Changelog &middot; 18 Aug</p>
      <h1 class="hd-01__h1">Ship the whole surface, not the strip.</h1>
      <p class="hd-01__lead">Press <kbd class="hd-01__kbd hd-01__kbd--dim">&#8984;K</kbd> anywhere on this page &mdash; or tab to the pill in the header and hit space. Scroll and the bar tightens against the content.</p>
    </section>
    <ul class="hd-01__cards">
      <li><h2>Edge routing</h2><p>Region-aware requests with a 24&nbsp;ms median hop between London and Dublin.</p></li>
      <li><h2>Preview envs</h2><p>Every branch gets an isolated database seeded from the last good snapshot.</p></li>
      <li><h2>Audit trail</h2><p>Immutable event log, exportable to your own bucket on a nightly schedule.</p></li>
      <li><h2>Insights</h2><p>Cold-start, cache-hit and error budgets in one pane, refreshed each minute.</p></li>
    </ul>
    <div class="hd-01__filler" aria-hidden="true"></div>
  </main>
</div>
```
## CSS
```css
.hd-01 {
  --s0: #07070a;
  --s1: #0e0e14;
  --s2: #15151f;
  --s3: #1d1d29;
  --ink: #f4f4f8;
  --muted: #9a9aae;
  --line: rgba(255,255,255,.09);
  --line2: rgba(255,255,255,.16);
  --accent: #a78bfa;
  --accent-ink: #12081f;
  --accent-soft: rgba(167,139,250,.16);
  --font-display: system-ui,-apple-system,"Segoe UI",sans-serif;
  --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  --pop: 180ms;
  width: 100%;
  min-height: 100vh;
  display: block;
  background: radial-gradient(90rem 40rem at 78% -14%, rgba(167,139,250,.15), transparent 62%), radial-gradient(60rem 32rem at 8% 4%, rgba(56,189,248,.08), transparent 60%), var(--s0);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% .1 200)) {
  .hd-01 {
    --s0: oklch(13% .012 285);
    --s1: oklch(17% .015 285);
    --s2: oklch(21% .018 285);
    --s3: oklch(25% .02 285);
    --ink: oklch(97% .004 285);
    --muted: oklch(70% .02 285);
    --accent: oklch(76% .16 300);
  }
}

.hd-01 * {
  box-sizing: border-box;
}

.hd-01 h1,
.hd-01 h2,
.hd-01 p,
.hd-01 ul {
  margin: 0;
  padding: 0;
}

.hd-01 ul {
  list-style: none;
}

.hd-01 [hidden] {
  display: none;
}

.hd-01 :focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: .5rem;
}

.hd-01__skip {
  position: absolute;
  inset-inline-start: .75rem;
  top: -3rem;
  z-index: 60;
  padding: .6rem 1rem;
  border-radius: .6rem;
  background: var(--accent);
  color: var(--accent-ink);
  font-size: .82rem;
  font-weight: 650;
  text-decoration: none;
  transition: top .18s ease;
}

.hd-01__skip:focus-visible {
  top: .75rem;
}
/* ── header: compact, emissive, scroll-reactive ───────────────────── */

.hd-01__bar {
  position: sticky;
  top: 0;
  z-index: 40;
  display: flex;
  align-items: center;
  gap: .75rem;
  padding: .6rem clamp(.75rem,3vw,1.75rem);
  background: color-mix(in srgb, var(--s0) 86%, transparent);
  border-bottom: 1px solid transparent;
  backdrop-filter: blur(14px) saturate(140%);
}

.hd-01__brand {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  min-inline-size: 0;
  color: var(--ink);
  text-decoration: none;
  font-family: var(--font-display);
  font-weight: 680;
  letter-spacing: -.022em;
  font-size: 1.02rem;
}

.hd-01__mark {
  inline-size: 1.55rem;
  block-size: 1.55rem;
  color: var(--accent);
  flex: none;
  filter: drop-shadow(0 0 .55rem var(--accent-soft));
}

.hd-01__word {
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-01__nav {
  min-inline-size: 0;
}

.hd-01__nav-list {
  display: flex;
  align-items: center;
  gap: .15rem;
}

.hd-01__nav-list a {
  display: block;
  padding: .42rem .6rem;
  border-radius: .55rem;
  color: var(--muted);
  text-decoration: none;
  font-size: .855rem;
  font-weight: 520;
  white-space: nowrap;
  transition: color .16s ease, background-color .16s ease;
}

.hd-01__nav-list a:hover {
  color: var(--ink);
  background: var(--s2);
}

.hd-01__nav-list a[aria-current="page"] {
  color: var(--ink);
  background: var(--s2);
}

.hd-01__cmd {
  position: relative;
  display: block;
  flex: 1;
  min-inline-size: 0;
  max-inline-size: 23rem;
  margin-inline: auto;
}

.hd-01__probe {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  opacity: 0;
  cursor: pointer;
  z-index: 2;
}

.hd-01__cmd-face {
  display: flex;
  align-items: center;
  gap: .5rem;
  min-block-size: 2.4rem;
  padding: .4rem .5rem .4rem .7rem;
  border: 1px solid var(--line);
  border-radius: .7rem;
  background: var(--s1);
  color: var(--muted);
  font-size: .85rem;
  transition: border-color .16s ease, background-color .16s ease, box-shadow .16s ease;
}

.hd-01__cmd-face svg {
  inline-size: 1rem;
  block-size: 1rem;
  flex: none;
}

.hd-01__cmd-text {
  flex: 1;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-01__cmd:hover .hd-01__cmd-face {
  border-color: var(--line2);
  background: var(--s2);
}

.hd-01__cmd:has(.hd-01__probe:focus-visible) .hd-01__cmd-face {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px var(--accent-soft);
}

.hd-01__kbd {
  font-family: ui-monospace,"SFMono-Regular",Menlo,monospace;
  font-size: .7rem;
  line-height: 1;
  padding: .32rem .42rem;
  border: 1px solid var(--line2);
  border-radius: .4rem;
  background: var(--s3);
  color: var(--ink);
  flex: none;
}

.hd-01__kbd--dim {
  background: transparent;
  color: var(--muted);
}

.hd-01__utility {
  display: flex;
  align-items: center;
  gap: .4rem;
  margin-inline-start: auto;
}

.hd-01__ghost {
  padding: .5rem .7rem;
  border-radius: .55rem;
  color: var(--muted);
  text-decoration: none;
  font-size: .855rem;
  font-weight: 540;
  white-space: nowrap;
  transition: color .16s ease;
}

.hd-01__ghost:hover {
  color: var(--ink);
}

.hd-01__cta {
  padding: .52rem .95rem;
  border-radius: .6rem;
  background: var(--accent);
  color: var(--accent-ink);
  text-decoration: none;
  font-size: .855rem;
  font-weight: 660;
  white-space: nowrap;
  box-shadow: 0 .55rem 1.6rem -.6rem rgba(167,139,250,.7);
  transition: translate .16s ease, box-shadow .16s ease;
}

.hd-01__cta:hover {
  translate: 0 -1px;
  box-shadow: 0 .75rem 2rem -.6rem rgba(167,139,250,.85);
}
/* ── palette overlay ──────────────────────────────────────────────── */

.hd-01__overlay {
  position: fixed;
  inset: 0;
  z-index: 50;
  display: grid;
  place-items: start center;
  padding: clamp(1rem,9vh,6rem) 1rem 1rem;
  visibility: hidden;
  opacity: 0;
  transition: opacity var(--pop) ease, visibility var(--pop) allow-discrete;
}

.hd-01__scrim {
  position: absolute;
  inset: 0;
  background: rgba(3,3,6,.66);
  backdrop-filter: blur(3px);
  cursor: default;
}

.hd-01__panel {
  position: relative;
  inline-size: 100%;
  max-inline-size: 34rem;
  max-block-size: min(30rem,78vh);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  border: 1px solid var(--line2);
  border-radius: 1rem;
  background: var(--s1);
  box-shadow: 0 2.5rem 5rem -1rem rgba(0,0,0,.75), 0 0 0 1px rgba(167,139,250,.14), 0 1.5rem 4rem -2rem rgba(167,139,250,.5);
  scale: .965;
  translate: 0 -.5rem;
  transition: scale var(--pop) cubic-bezier(.2,.8,.2,1), translate var(--pop) cubic-bezier(.2,.8,.2,1);
}

.hd-01:has(#hd-01-open:checked) .hd-01__overlay {
  visibility: visible;
  opacity: 1;
}

.hd-01:has(#hd-01-open:checked) .hd-01__panel {
  scale: 1;
  translate: 0 0;
}

.hd-01__field {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .85rem 1rem;
  border-bottom: 1px solid var(--line);
}

.hd-01__field svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
  color: var(--muted);
  flex: none;
}

.hd-01__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: transparent;
  color: var(--ink);
  font: inherit;
  font-size: .98rem;
  padding: .2rem 0;
}

.hd-01__input::placeholder {
  color: var(--muted);
}

.hd-01__input:focus {
  outline: none;
}

.hd-01__esc {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .68rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  padding: .34rem .5rem;
  border: 1px solid var(--line2);
  border-radius: .4rem;
  color: var(--muted);
  cursor: pointer;
}

.hd-01__esc:hover {
  color: var(--ink);
  background: var(--s3);
}

.hd-01__scroll {
  overflow: auto;
  padding: .5rem;
  overscroll-behavior: contain;
}

.hd-01__group {
  padding: .55rem .6rem .3rem;
  font-size: .68rem;
  font-weight: 640;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.hd-01__row {
  inline-size: 100%;
  display: flex;
  align-items: center;
  gap: .7rem;
  min-block-size: 2.75rem;
  padding: .5rem .6rem;
  border: 0;
  border-radius: .6rem;
  background: transparent;
  color: var(--ink);
  font: inherit;
  font-size: .9rem;
  text-align: start;
  cursor: pointer;
  transition: background-color .13s ease;
}

.hd-01__row svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  color: var(--muted);
  flex: none;
}

.hd-01__row span:not(.hd-01__meta) {
  flex: 1;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-01__meta {
  font-size: .72rem;
  color: var(--muted);
  flex: none;
}

.hd-01__row:hover,
.hd-01__row:focus-visible {
  background: var(--accent-soft);
  outline-offset: -2px;
}

.hd-01__row:hover svg {
  color: var(--accent);
}

.hd-01:has(#hd-01-open:checked) .hd-01__list li {
  animation: hd-01-in 260ms cubic-bezier(.2,.8,.2,1) backwards;
  animation-delay: calc(var(--i,1) * 26ms + 40ms);
}

@keyframes hd-01-in {
  from {
    opacity: 0;
    translate: 0 .45rem;
  }
}

.hd-01__foot {
  display: flex;
  align-items: center;
  gap: .4rem;
  padding: .6rem 1rem;
  border-top: 1px solid var(--line);
  font-size: .74rem;
  color: var(--muted);
}

.hd-01__sep {
  inline-size: 1px;
  block-size: .85rem;
  background: var(--line2);
}
/* ── page body ────────────────────────────────────────────────────── */

.hd-01__main {
  padding: clamp(2rem,7vw,5rem) clamp(1rem,4vw,2.5rem) 4rem;
  max-inline-size: 70rem;
  margin-inline: auto;
}

.hd-01__eyebrow {
  font-size: .75rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--accent);
  font-weight: 620;
  margin-bottom: .9rem;
}

.hd-01__h1 {
  font-family: var(--font-display);
  font-size: clamp(1.9rem,6vw,3.4rem);
  line-height: 1.04;
  letter-spacing: -.035em;
  font-weight: 700;
  max-inline-size: 24ch;
  text-wrap: balance;
}

.hd-01__lead {
  margin-top: 1rem;
  max-inline-size: 52ch;
  color: var(--muted);
  font-size: 1.02rem;
  text-wrap: pretty;
}

.hd-01__cards {
  display: grid;
  gap: .8rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,15rem),1fr));
  margin-top: clamp(2rem,6vw,3.5rem);
}

.hd-01__cards li {
  padding: 1.1rem;
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--s1);
  min-inline-size: 0;
}

.hd-01__cards h2 {
  font-family: var(--font-display);
  font-size: .95rem;
  font-weight: 640;
  letter-spacing: -.01em;
}

.hd-01__cards p {
  margin-top: .4rem;
  font-size: .85rem;
  color: var(--muted);
}

.hd-01__filler {
  block-size: 60vh;
}
/* scroll-driven header tightening — resting state is the fallback */

@supports (animation-timeline: scroll()) {
  .hd-01__bar {
    animation: hd-01-tighten linear both;
    animation-timeline: scroll(root);
    animation-range: 0 160px;
  }

  @keyframes hd-01-tighten {
    from {
      background: transparent;
      border-bottom-color: transparent;
    }

    to {
      background: color-mix(in srgb, var(--s1) 88%, transparent);
      border-bottom-color: var(--line);
    }
  }
}

@media (max-width: 860px) {
  .hd-01__nav {
    display: none;
  }

  .hd-01__cmd {
    max-inline-size: none;
  }
}

@media (max-width: 560px) {
  .hd-01__ghost {
    display: none;
  }

  .hd-01__cmd-text {
    display: none;
  }

  .hd-01__cmd {
    flex: none;
    inline-size: auto;
    margin-inline-start: auto;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-01:has(#hd-01-light:checked) {
  --s0: #fbfbfd;
  --s1: #ffffff;
  --s2: #f2f2f7;
  --s3: #e8e8f0;
  --ink: #0d0d14;
  --muted: #5c5c70;
  --line: rgba(13,13,20,.1);
  --line2: rgba(13,13,20,.18);
  --accent: #6d28d9;
  --accent-ink: #ffffff;
  --accent-soft: rgba(109,40,217,.12);
}
/* icon: shows the scheme the toggle will switch you to */

.hd-01__moon {
  display: none;
}

.hd-01:has(#hd-01-light:checked) .hd-01__sun {
  display: none;
}

.hd-01:has(#hd-01-light:checked) .hd-01__moon {
  display: block;
}

@media (prefers-color-scheme: light) {
  .hd-01:not([data-theme="dark"]):not(:has(#hd-01-light:checked)) {
    --s0: #fbfbfd;
    --s1: #ffffff;
    --s2: #f2f2f7;
    --s3: #e8e8f0;
    --ink: #0d0d14;
    --muted: #5c5c70;
    --line: rgba(13,13,20,.1);
    --line2: rgba(13,13,20,.18);
    --accent: #6d28d9;
    --accent-ink: #ffffff;
    --accent-soft: rgba(109,40,217,.12);
  }
  /* FLIP-BACK — light OS + checked toggle returns to the other scheme */

  .hd-01:has(#hd-01-light:checked) {
    --s0: #07070a;
    --s1: #0e0e14;
    --s2: #15151f;
    --s3: #1d1d29;
    --ink: #f4f4f8;
    --muted: #9a9aae;
    --line: rgba(255,255,255,.09);
    --line2: rgba(255,255,255,.16);
    --accent: #a78bfa;
    --accent-ink: #12081f;
    --accent-soft: rgba(167,139,250,.16);
    --font-display: system-ui,-apple-system,"Segoe UI",sans-serif;
    --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
    --pop: 180ms;
  }
  /* the icon always offers the scheme you are not in */

  .hd-01:not([data-theme="dark"]):not(:has(#hd-01-light:checked)) .hd-01__sun {
    display: none;
  }

  .hd-01:not([data-theme="dark"]):not(:has(#hd-01-light:checked)) .hd-01__moon {
    display: block;
  }

  .hd-01:has(#hd-01-light:checked) .hd-01__moon {
    display: none;
  }

  .hd-01:has(#hd-01-light:checked) .hd-01__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hd-01 * {
    animation-duration: 1ms !important;
    transition-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-01__panel,
    .hd-01__cmd-face {
    border: 1px solid CanvasText;
  }
}
/* ── theme toggle — visually hidden checkbox, zero JS ────────────── */

.hd-01__sr,
.hd-01__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-01__theme {
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

.hd-01__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-01__theme:hover {
  background: rgba(128,128,128,.16);
}

.hd-01:has(#hd-01-light:focus-visible) .hd-01__theme {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```

## JavaScript
```js
{
  const root = document.querySelector('.hd-01');
  const box = root && root.querySelector('#hd-01-open');
  const input = root && root.querySelector('.hd-01__input');
  if (box) {
    document.addEventListener('keydown', (event) => {
      const key = event.key.toLowerCase();
      if ((event.metaKey || event.ctrlKey) && key === 'k') {
        event.preventDefault();                 // Firefox/Chrome own Cmd+K otherwise
        box.checked = !box.checked;
        if (box.checked && input) input.focus();
      } else if (key === 'escape' && box.checked) {
        box.checked = false;
        box.focus();                            // return focus to the trigger
      }
    });
    box.addEventListener('change', () => { if (box.checked && input) input.focus(); });
  }
}
```
