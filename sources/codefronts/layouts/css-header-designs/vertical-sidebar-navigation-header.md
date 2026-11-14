---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/vertical-sidebar-navigation-header/"
title: "Vertical Sidebar App Shell Header"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "When the header is vertical: a sidebar carrying the logo, grouped navigation and a user footer, with the main region getting a slim top bar for breadcrumb…"
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vertical Sidebar App Shell Header
Source: https://codefronts.com/layouts/css-header-designs/vertical-sidebar-navigation-header/

When the header is vertical: a sidebar carrying the logo, grouped navigation and a user footer, with the main region getting a slim top bar for breadcrumb and page actions. The shell is one CSS Grid, the sidebar collapses to an icon rail on a pure-CSS toggle, and both regions scroll independently without breaking sticky positioning.
## HTML
```html
<div class="hd-20">
  <a class="hd-20__skip" href="#hd-20-main">Skip to content</a>
      <input class="hd-20__sr" type="checkbox" id="hd-20-rail" aria-label="Collapse the sidebar">

  <div class="hd-20__stage">
    <header class="hd-20__side">
      <a class="hd-20__brand" href="#hd-20-main">
        <span class="hd-20__mark" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M5 16.5 12 5l7 11.5H5Z" stroke="currentColor" stroke-width="1.9" stroke-linejoin="round"/></svg>
        </span>
        <span class="hd-20__word">Ridgeline</span>
      </a>

      <label class="hd-20__collapse" for="hd-20-rail">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M14.5 7 9.5 12l5 5" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <span class="hd-20__vh">Collapse or expand the sidebar</span>
      </label>

      <input class="hd-20__sr" type="checkbox" id="hd-20-dark">
      <label class="hd-20__theme" for="hd-20-dark">
        <svg class="hd-20__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <svg class="hd-20__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <span class="hd-20__vh">Switch light or dark theme</span>
      </label>
      <nav class="hd-20__nav" aria-label="Workspace">
        <p class="hd-20__group">Workspace</p>
        <ul>
          <li><a href="#hd-20-main" aria-current="page">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="4" y="4" width="7" height="7" rx="1.6" stroke="currentColor" stroke-width="1.7"/><rect x="13" y="4" width="7" height="7" rx="1.6" stroke="currentColor" stroke-width="1.7"/><rect x="4" y="13" width="7" height="7" rx="1.6" stroke="currentColor" stroke-width="1.7"/><rect x="13" y="13" width="7" height="7" rx="1.6" stroke="currentColor" stroke-width="1.7"/></svg>
            <span class="hd-20__label">Overview</span></a></li>
          <li><a href="#hd-20-main">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 7.5h16M4 12h16M4 16.5h10" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
            <span class="hd-20__label">Projects</span><span class="hd-20__pill">12</span></a></li>
          <li><a href="#hd-20-main">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 18V10M9.5 18V5M15 18v-6M20.5 18v-9" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
            <span class="hd-20__label">Insights</span></a></li>
          <li><a href="#hd-20-main">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="3" stroke="currentColor" stroke-width="1.7"/><path d="M12 4v2.5M12 17.5V20M4 12h2.5M17.5 12H20M6.4 6.4l1.8 1.8M15.8 15.8l1.8 1.8M17.6 6.4l-1.8 1.8M8.2 15.8l-1.8 1.8" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
            <span class="hd-20__label">Automations</span></a></li>
        </ul>

        <p class="hd-20__group">Library</p>
        <ul>
          <li><a href="#hd-20-main">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 5.5h6l1.5 2H19v11H5V5.5Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
            <span class="hd-20__label">Assets</span></a></li>
          <li><a href="#hd-20-main">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6 4.5h9l3.5 3.5V19.5H6V4.5Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M9 12h6M9 15.5h4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
            <span class="hd-20__label">Templates</span></a></li>
          <li><a href="#hd-20-main">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5 4.5 8.5 12 12.5 19.5 8.5 12 4.5Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M4.5 15.5 12 19.5l7.5-4" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
            <span class="hd-20__label">Archive</span></a></li>
        </ul>
      </nav>

      <div class="hd-20__foot">
        <span class="hd-20__av" aria-hidden="true">PS</span>
        <span class="hd-20__foot-t">
          <span class="hd-20__foot-n">Priya Sharma</span>
          <span class="hd-20__foot-r">Owner &middot; Ridgeline</span>
        </span>
      </div>
    </header>

    <div class="hd-20__col">
      <div class="hd-20__topbar">
        <nav class="hd-20__crumbs" aria-label="Breadcrumb">
          <ol>
            <li><a href="#hd-20-main">Workspace</a></li>
            <li><a href="#hd-20-main">Projects</a></li>
            <li><span aria-current="page">Trail resurfacing</span></li>
          </ol>
        </nav>
        <div class="hd-20__t-right">
          <button class="hd-20__icon" type="button" aria-label="Search this workspace">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.8 15.8 21 21" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          </button>
          <button class="hd-20__icon" type="button" aria-label="Notifications">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6.5 10.6a5.5 5.5 0 0 1 11 0c0 3 .7 4.4 1.4 5.2.4.5.1 1.3-.6 1.3H5.7c-.7 0-1-.8-.6-1.3.7-.8 1.4-2.2 1.4-5.2Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M10 19.5a2.2 2.2 0 0 0 4 0" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          </button>
          <a class="hd-20__cta" href="#hd-20-main">Share</a>
        </div>
      </div>

      <main class="hd-20__main" id="hd-20-main">
        <h1>Trail resurfacing</h1>
        <p class="hd-20__lead">Collapse the sidebar with the chevron &mdash; the shell is one grid and the rail width is one custom property. Labels stay in the DOM so icon-only rows keep their names.</p>

        <ul class="hd-20__cards">
          <li><p class="hd-20__c-k">Phase</p><p class="hd-20__c-v">2 of 4</p></li>
          <li><p class="hd-20__c-k">Spend to date</p><p class="hd-20__c-v">&pound;184k</p></li>
          <li><p class="hd-20__c-k">Open issues</p><p class="hd-20__c-v">7</p></li>
        </ul>

        <section class="hd-20__panel">
          <h2>Activity</h2>
          <ul>
            <li><span>Jordan Lee closed <strong>Drainage survey</strong></span><time>2h</time></li>
            <li><span>Alex Chen uploaded <strong>Section C photos</strong></span><time>5h</time></li>
            <li><span>Sam Rivera changed the phase to <strong>Resurfacing</strong></span><time>Yesterday</time></li>
            <li><span>Priya Sharma invited two contractors</span><time>Mon</time></li>
          </ul>
        </section>
        <div class="hd-20__filler" aria-hidden="true"></div>
      </main>
    </div>
  </div>
</div>
```
## CSS
```css
.hd-20 {
  --s1: #faf8f4;
  --s2: #f2eee6;
  --s3: #e7e1d5;
  --ink: #211d16;
  --muted: #6f6759;
  --line: rgba(33,29,22,.12);
  --accent: #b8860b;
  --accent-soft: rgba(184,134,11,.13);
  --accent-ink: #ffffff;
  --rail-open: 15.5rem;
  --rail: var(--rail-open);
  --font-display: ui-rounded,"SF Pro Rounded","Nunito",system-ui,sans-serif;
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
  .hd-20 {
    --s1: oklch(97.5% .012 85);
    --s2: oklch(95% .015 85);
    --s3: oklch(91% .02 85);
    --ink: oklch(22% .02 70);
    --muted: oklch(50% .02 70);
    --accent: oklch(62% .12 85);
  }
}

.hd-20 * {
  box-sizing: border-box;
}

.hd-20 h1,
.hd-20 h2,
.hd-20 p,
.hd-20 ul,
.hd-20 ol {
  margin: 0;
  padding: 0;
}

.hd-20 ul,
.hd-20 ol {
  list-style: none;
}

.hd-20 [hidden] {
  display: none;
}

.hd-20 :focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: .4rem;
}

.hd-20__sr,
.hd-20__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-20__skip {
  position: absolute;
  inset-inline-start: .75rem;
  top: -3rem;
  z-index: 60;
  padding: .5rem .9rem;
  border-radius: .5rem;
  background: var(--accent);
  color: var(--accent-ink);
  font-size: .8rem;
  font-weight: 700;
  text-decoration: none;
  transition: top .18s ease;
}

.hd-20__skip:focus-visible {
  top: .75rem;
}
/* ── the shell ────────────────────────────────────────────────────── */

.hd-20__stage {
  display: grid;
  grid-template-columns: var(--rail) minmax(0,1fr);
  min-block-size: 100vh;
  transition: grid-template-columns .28s cubic-bezier(.3,.8,.3,1);
}

.hd-20:has(#hd-20-rail:checked) {
  --rail: 4.25rem;
}
/* ── vertical header ─────────────────────────────────────────────── */

.hd-20__side {
  position: sticky;
  top: 0;
  align-self: start;
  block-size: 100vh;
  display: flex;
  flex-direction: column;
  gap: .25rem;
  min-inline-size: 0;
  padding: .85rem .6rem;
  background: var(--s1);
  border-inline-end: 1px solid var(--line);
}

.hd-20__brand {
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .3rem .35rem;
  color: var(--ink);
  text-decoration: none;
  min-inline-size: 0;
}

.hd-20__mark {
  display: grid;
  place-items: center;
  inline-size: 2.1rem;
  block-size: 2.1rem;
  border-radius: .6rem;
  background: var(--accent);
  color: #fff;
  flex: none;
}

.hd-20__mark svg {
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.hd-20__word {
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: -.02em;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  opacity: 1;
  transition: opacity .2s ease;
}

.hd-20__collapse {
  position: absolute;
  top: 1rem;
  inset-inline-end: -.85rem;
  z-index: 5;
  display: grid;
  place-items: center;
  inline-size: 1.7rem;
  block-size: 1.7rem;
  border-radius: 999px;
  background: var(--s1);
  border: 1px solid var(--line);
  color: var(--muted);
  cursor: pointer;
  transition: rotate .28s ease, color .16s ease;
}

.hd-20__side {
  position: relative;
}

.hd-20__collapse svg {
  inline-size: 1rem;
  block-size: 1rem;
}

.hd-20__collapse:hover {
  color: var(--ink);
}

.hd-20:has(#hd-20-rail:checked) .hd-20__collapse {
  rotate: 180deg;
}

.hd-20:has(#hd-20-rail:focus-visible) .hd-20__collapse {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.hd-20__nav {
  margin-top: .75rem;
  min-inline-size: 0;
}

.hd-20__group {
  padding: .5rem .55rem .3rem;
  font-size: .66rem;
  font-weight: 800;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
  white-space: nowrap;
  overflow: hidden;
}

.hd-20__nav a {
  display: flex;
  align-items: center;
  gap: .65rem;
  min-block-size: 2.5rem;
  padding: .45rem .55rem;
  border-radius: .6rem;
  color: var(--muted);
  text-decoration: none;
  font-size: .88rem;
  font-weight: 560;
  min-inline-size: 0;
  transition: background-color .15s ease, color .15s ease;
}

.hd-20__nav a svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
  flex: none;
}

.hd-20__nav a:hover {
  background: var(--s2);
  color: var(--ink);
}

.hd-20__nav a[aria-current="page"] {
  background: var(--accent-soft);
  color: var(--accent);
  font-weight: 700;
}

.hd-20__label {
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  transition: opacity .2s ease;
}

.hd-20__pill {
  margin-inline-start: auto;
  font-size: .7rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  padding: .1rem .4rem;
  border-radius: 999px;
  background: var(--s3);
  color: var(--muted);
}

.hd-20__foot {
  margin-block-start: auto;
  display: flex;
  align-items: center;
  gap: .6rem;
  padding: .6rem .55rem;
  border-top: 1px solid var(--line);
  min-inline-size: 0;
}

.hd-20__av {
  display: grid;
  place-items: center;
  inline-size: 2rem;
  block-size: 2rem;
  border-radius: 50%;
  flex: none;
  background: var(--s3);
  color: var(--ink);
  font-family: var(--font-display);
  font-size: .7rem;
  font-weight: 700;
  box-shadow: 0 0 0 2px var(--accent-soft);
}

.hd-20__foot-t {
  display: grid;
  min-inline-size: 0;
}

.hd-20__foot-n {
  font-size: .84rem;
  font-weight: 660;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-20__foot-r {
  font-size: .7rem;
  color: var(--muted);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-20:has(#hd-20-rail:checked) .hd-20__word,
.hd-20:has(#hd-20-rail:checked) .hd-20__label,
.hd-20:has(#hd-20-rail:checked) .hd-20__group,
.hd-20:has(#hd-20-rail:checked) .hd-20__pill,
.hd-20:has(#hd-20-rail:checked) .hd-20__foot-t {
  opacity: 0;
  inline-size: 0;
  overflow: hidden;
}
/* ── main column ─────────────────────────────────────────────────── */

.hd-20__col {
  display: flex;
  flex-direction: column;
  min-inline-size: 0;
}

.hd-20__topbar {
  position: sticky;
  top: 0;
  z-index: 20;
  display: flex;
  align-items: center;
  gap: 1rem;
  min-block-size: 3.25rem;
  padding: .4rem clamp(.75rem,3vw,1.5rem);
  background: color-mix(in srgb, var(--s2) 92%, transparent);
  border-bottom: 1px solid var(--line);
  backdrop-filter: blur(8px);
}

.hd-20__crumbs {
  min-inline-size: 0;
  overflow-x: auto;
  scrollbar-width: none;
  direction: rtl;
}

.hd-20__crumbs::-webkit-scrollbar {
  display: none;
}

.hd-20__crumbs ol {
  direction: ltr;
  display: flex;
  align-items: center;
  font-size: .82rem;
  white-space: nowrap;
}

.hd-20__crumbs li + li::before {
  content: "/";
  color: var(--muted);
  padding-inline: .4rem;
  opacity: .6;
}

.hd-20__crumbs a {
  color: var(--muted);
  text-decoration: none;
  padding-block: .3rem;
}

.hd-20__crumbs a:hover {
  color: var(--accent);
}

.hd-20__crumbs [aria-current="page"] {
  color: var(--ink);
  font-weight: 660;
}

.hd-20__t-right {
  display: flex;
  align-items: center;
  gap: .3rem;
  margin-inline-start: auto;
}

.hd-20__icon {
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border: 0;
  border-radius: .5rem;
  background: transparent;
  color: var(--muted);
  cursor: pointer;
  transition: background-color .15s ease, color .15s ease;
}

.hd-20__icon svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-20__icon:hover {
  background: var(--s3);
  color: var(--ink);
}

.hd-20__cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.4rem;
  padding: .55rem 1rem;
  border-radius: .55rem;
  background: var(--ink);
  color: var(--s1);
  text-decoration: none;
  font-family: var(--font-display);
  font-size: .85rem;
  font-weight: 700;
  white-space: nowrap;
  transition: background-color .15s ease;
}

.hd-20__cta:hover {
  background: var(--accent);
}

.hd-20__main {
  padding: clamp(1.5rem,4vw,2.5rem) clamp(.75rem,3vw,1.5rem) 4rem;
  min-inline-size: 0;
}

.hd-20__main h1 {
  font-family: var(--font-display);
  font-size: clamp(1.5rem,4vw,2.1rem);
  font-weight: 700;
  letter-spacing: -.03em;
}

.hd-20__lead {
  margin-top: .6rem;
  max-inline-size: 60ch;
  color: var(--muted);
  font-size: .95rem;
  text-wrap: pretty;
}

.hd-20__cards {
  display: grid;
  gap: .75rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,11rem),1fr));
  margin-top: 1.5rem;
}

.hd-20__cards li {
  padding: 1rem;
  border-radius: .8rem;
  background: var(--s1);
  border: 1px solid var(--line);
  min-inline-size: 0;
}

.hd-20__c-k {
  font-size: .74rem;
  color: var(--muted);
  font-weight: 560;
}

.hd-20__c-v {
  font-family: var(--font-display);
  font-size: 1.6rem;
  font-weight: 700;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
  margin-top: .15rem;
}

.hd-20__panel {
  margin-top: 1.25rem;
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--s1);
  overflow: hidden;
}

.hd-20__panel h2 {
  font-family: var(--font-display);
  font-size: .95rem;
  font-weight: 700;
  padding: .85rem 1rem;
  border-bottom: 1px solid var(--line);
}

.hd-20__panel li {
  display: flex;
  align-items: center;
  gap: .75rem;
  padding: .7rem 1rem;
  border-bottom: 1px solid var(--line);
  font-size: .87rem;
}

.hd-20__panel li:last-child {
  border-bottom: 0;
}

.hd-20__panel li span {
  flex: 1;
  min-inline-size: 0;
}

.hd-20__panel time {
  font-size: .75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.hd-20__filler {
  block-size: 45vh;
}

@media (max-width: 760px) {
  .hd-20 {
    --rail-open: 4.25rem;
  }

  .hd-20__word,
    .hd-20__label,
    .hd-20__group,
    .hd-20__pill,
    .hd-20__foot-t {
    opacity: 0;
    inline-size: 0;
    overflow: hidden;
  }

  .hd-20:has(#hd-20-rail:checked) {
    --rail: 15.5rem;
  }

  .hd-20:has(#hd-20-rail:checked) .hd-20__word,
    .hd-20:has(#hd-20-rail:checked) .hd-20__label,
    .hd-20:has(#hd-20-rail:checked) .hd-20__group,
    .hd-20:has(#hd-20-rail:checked) .hd-20__pill,
    .hd-20:has(#hd-20-rail:checked) .hd-20__foot-t {
    opacity: 1;
    inline-size: auto;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-20:has(#hd-20-dark:checked) {
  --s1: #1a1815;
  --s2: #131110;
  --s3: #262220;
  --ink: #f3efe7;
  --muted: #a49b8c;
  --line: rgba(243,239,231,.12);
  --accent: #e0b64a;
  --accent-soft: rgba(224,182,74,.16);
  --accent-ink: #241a04;
}

.hd-20:has(#hd-20-dark:checked) .hd-20__cta {
  background: var(--accent);
  color: var(--accent-ink);
}
/* icon: shows the scheme the toggle will switch you to */

.hd-20__sun {
  display: none;
}

.hd-20:has(#hd-20-dark:checked) .hd-20__moon {
  display: none;
}

.hd-20:has(#hd-20-dark:checked) .hd-20__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .hd-20:not([data-theme="light"]):not(:has(#hd-20-dark:checked)) {
    --s1: #1a1815;
    --s2: #131110;
    --s3: #262220;
    --ink: #f3efe7;
    --muted: #a49b8c;
    --line: rgba(243,239,231,.12);
    --accent: #e0b64a;
    --accent-soft: rgba(224,182,74,.16);
    --accent-ink: #241a04;
  }

  .hd-20:not([data-theme="light"]):not(:has(#hd-20-dark:checked)) .hd-20__cta {
    background: var(--accent);
    color: var(--accent-ink);
  }
  /* FLIP-BACK — dark OS + checked toggle returns to the other scheme */

  .hd-20:has(#hd-20-dark:checked) {
    --s1: #faf8f4;
    --s2: #f2eee6;
    --s3: #e7e1d5;
    --ink: #211d16;
    --muted: #6f6759;
    --line: rgba(33,29,22,.12);
    --accent: #b8860b;
    --accent-soft: rgba(184,134,11,.13);
    --accent-ink: #ffffff;
    --rail-open: 15.5rem;
    --rail: var(--rail-open);
    --font-display: ui-rounded,"SF Pro Rounded","Nunito",system-ui,sans-serif;
    --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  }

  .hd-20:has(#hd-20-dark:checked) .hd-20__cta {
    display: inline-flex;
    align-items: center;
    min-block-size: 2.4rem;
    padding: .55rem 1rem;
    border-radius: .55rem;
    background: var(--ink);
    color: var(--s1);
    text-decoration: none;
    font-family: var(--font-display);
    font-size: .85rem;
    font-weight: 700;
    white-space: nowrap;
    transition: background-color .15s ease;
  }
  /* the icon always offers the scheme you are not in */

  .hd-20:not([data-theme="light"]):not(:has(#hd-20-dark:checked)) .hd-20__moon {
    display: none;
  }

  .hd-20:not([data-theme="light"]):not(:has(#hd-20-dark:checked)) .hd-20__sun {
    display: block;
  }

  .hd-20:has(#hd-20-dark:checked) .hd-20__sun {
    display: none;
  }

  .hd-20:has(#hd-20-dark:checked) .hd-20__moon {
    display: block;
  }
}

.hd-20[data-theme="dark"] {
  --s1: #1a1815;
  --s2: #131110;
  --s3: #262220;
  --ink: #f3efe7;
  --muted: #a49b8c;
  --line: rgba(243,239,231,.12);
  --accent: #e0b64a;
  --accent-soft: rgba(224,182,74,.16);
  --accent-ink: #241a04;
}

@media (prefers-reduced-motion: reduce) {
  .hd-20 * {
    transition-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-20__side {
    border-inline-end: 1px solid CanvasText;
  }
}
/* ── theme toggle — visually hidden checkbox, zero JS ────────────── */

.hd-20__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-20__theme {
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

.hd-20__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-20__theme:hover {
  background: rgba(128,128,128,.16);
}

.hd-20:has(#hd-20-dark:focus-visible) .hd-20__theme {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```
