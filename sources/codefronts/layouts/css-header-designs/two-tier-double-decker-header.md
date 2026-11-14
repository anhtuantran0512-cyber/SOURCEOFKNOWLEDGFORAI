---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/two-tier-double-decker-header/"
title: "Two Tier Double Decker Enterprise Header"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "The double-decker enterprise header: a dense utility strip on top for support, docs, region, currency and language, then the primary bar underneath with…"
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Two Tier Double Decker Enterprise Header
Source: https://codefronts.com/layouts/css-header-designs/two-tier-double-decker-header/

The double-decker enterprise header: a dense utility strip on top for support, docs, region, currency and language, then the primary bar underneath with logo, main nav and the demo CTA. Ultra-compact spacing, zero border radius and sharp hairlines &mdash; the vocabulary banks, healthcare portals and B2B platforms actually use.
## HTML
```html
<div class="hd-18">
  <a class="hd-18__skip" href="#hd-18-main">Skip to content</a>

  <header class="hd-18__header">
    <div class="hd-18__utility">
      <nav class="hd-18__u-nav" aria-label="Utility">
        <ul>
          <li><a href="#hd-18-main">Support</a></li>
          <li><a href="#hd-18-main">Documentation</a></li>
          <li><a href="#hd-18-main">Status</a></li>
          <li><a href="#hd-18-main">Partner portal</a></li>
        </ul>
      </nav>

      <div class="hd-18__u-right">
        <input class="hd-18__sr" type="checkbox" id="hd-18-dark">
        <label class="hd-18__theme" for="hd-18-dark">
          <svg class="hd-18__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          <svg class="hd-18__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
          <span class="hd-18__vh">Switch light or dark theme</span>
        </label>
        <div class="hd-18__sel">
          <button class="hd-18__sel-btn" type="button" aria-haspopup="menu">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.4" stroke="currentColor" stroke-width="1.6"/><path d="M3.6 12h16.8M12 3.6c2.6 2.8 2.6 13.6 0 16.8" stroke="currentColor" stroke-width="1.4"/></svg>
            United Kingdom
          </button>
          <ul class="hd-18__pop" role="menu" aria-label="Choose a region">
            <li role="none"><a role="menuitem" href="#hd-18-main" aria-current="true">United Kingdom</a></li>
            <li role="none"><a role="menuitem" href="#hd-18-main">Ireland</a></li>
            <li role="none"><a role="menuitem" href="#hd-18-main">Germany</a></li>
            <li role="none"><a role="menuitem" href="#hd-18-main">United States</a></li>
            <li role="none"><a role="menuitem" href="#hd-18-main">Singapore</a></li>
          </ul>
        </div>
        <span class="hd-18__pipe" aria-hidden="true"></span>
        <div class="hd-18__sel">
          <button class="hd-18__sel-btn" type="button" aria-haspopup="menu">GBP &pound;</button>
          <ul class="hd-18__pop" role="menu" aria-label="Choose a currency">
            <li role="none"><a role="menuitem" href="#hd-18-main" aria-current="true">GBP &pound;</a></li>
            <li role="none"><a role="menuitem" href="#hd-18-main">EUR &euro;</a></li>
            <li role="none"><a role="menuitem" href="#hd-18-main">USD $</a></li>
            <li role="none"><a role="menuitem" href="#hd-18-main">SGD $</a></li>
          </ul>
        </div>
        <span class="hd-18__pipe" aria-hidden="true"></span>
        <div class="hd-18__sel">
          <button class="hd-18__sel-btn" type="button" aria-haspopup="menu">English</button>
          <ul class="hd-18__pop" role="menu" aria-label="Choose a language">
            <li role="none"><a role="menuitem" href="#hd-18-main" aria-current="true">English</a></li>
            <li role="none"><a role="menuitem" href="#hd-18-main">Deutsch</a></li>
            <li role="none"><a role="menuitem" href="#hd-18-main">Fran&ccedil;ais</a></li>
            <li role="none"><a role="menuitem" href="#hd-18-main">&#26085;&#26412;&#35486;</a></li>
          </ul>
        </div>
        <span class="hd-18__pipe" aria-hidden="true"></span>
        <a class="hd-18__u-link" href="#hd-18-main">Sign in</a>
      </div>
    </div>

    <div class="hd-18__primary">
      <a class="hd-18__brand" href="#hd-18-main">
        <span class="hd-18__mark" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M4 20V7l8-3 8 3v13" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M9 20v-6h6v6" stroke="currentColor" stroke-width="1.8"/></svg>
        </span>
        <span class="hd-18__word">Charter <span>Financial Systems</span></span>
      </a>

      <nav class="hd-18__nav" aria-label="Main">
        <ul>
          <li><a href="#hd-18-main" aria-current="page">Platform</a></li>
          <li><a href="#hd-18-main">Industries</a></li>
          <li><a href="#hd-18-main">Compliance</a></li>
          <li><a href="#hd-18-main">Resources</a></li>
          <li><a href="#hd-18-main">Company</a></li>
        </ul>
      </nav>

      <div class="hd-18__p-right">
        <label class="hd-18__search" for="hd-18-q">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.8 15.8 21 21" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          <input class="hd-18__q" id="hd-18-q" type="text" placeholder="Search" aria-label="Search the site">
        </label>
        <a class="hd-18__cta" href="#hd-18-main">Request a demo</a>
      </div>
    </div>
  </header>

  <main class="hd-18__main" id="hd-18-main">
    <p class="hd-18__eyebrow">Treasury operations</p>
    <h1>Settlement infrastructure for regulated institutions.</h1>
    <p class="hd-18__lead">Two rows, two jobs: the utility strip carries region, currency and language and scrolls away; the primary bar stays. Every dropdown opens on hover and on keyboard focus.</p>
    <ul class="hd-18__facts">
      <li><p class="hd-18__f-k">Settlement finality</p><p class="hd-18__f-v">T+0</p></li>
      <li><p class="hd-18__f-k">Uptime, 24 months</p><p class="hd-18__f-v">99.995%</p></li>
      <li><p class="hd-18__f-k">Regulated entities</p><p class="hd-18__f-v">412</p></li>
      <li><p class="hd-18__f-k">Jurisdictions</p><p class="hd-18__f-v">28</p></li>
    </ul>
    <div class="hd-18__filler" aria-hidden="true"></div>
  </main>
</div>
```
## CSS
```css
.hd-18 {
  --bg: #ffffff;
  --u-bg: #0d2440;
  --panel: #f4f6f9;
  --ink: #0d2440;
  --muted: #4a5b70;
  --line: #c9d3e0;
  --accent: #1a56b0;
  --accent-ink: #ffffff;
  --pad-u: .35rem;
  --pad-p: .55rem;
  --r: 0;
  --font-display: system-ui,-apple-system,"Segoe UI",Tahoma,sans-serif;
  --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.45;
}

@supports (color: oklch(50% .1 200)) {
  .hd-18 {
    --u-bg: oklch(28% .07 255);
    --ink: oklch(28% .07 255);
    --muted: oklch(45% .04 255);
    --accent: oklch(45% .16 258);
  }
}

.hd-18 * {
  box-sizing: border-box;
}

.hd-18 h1,
.hd-18 p,
.hd-18 ul {
  margin: 0;
  padding: 0;
}

.hd-18 ul {
  list-style: none;
}

.hd-18 [hidden] {
  display: none;
}

.hd-18 :focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 1px;
}

.hd-18__skip {
  position: absolute;
  inset-inline-start: .5rem;
  top: -3rem;
  z-index: 60;
  padding: .5rem .9rem;
  background: var(--accent);
  color: var(--accent-ink);
  font-size: .78rem;
  font-weight: 700;
  text-decoration: none;
  transition: top .18s ease;
}

.hd-18__skip:focus-visible {
  top: .5rem;
}
/* ── tier 1: utility strip (not sticky) ───────────────────────────── */

.hd-18__utility {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: var(--pad-u) clamp(.6rem,2.5vw,1.5rem);
  background: var(--u-bg);
  color: #e8eef7;
}

.hd-18__u-nav {
  min-inline-size: 0;
}

.hd-18__u-nav ul {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.hd-18__u-nav a,
.hd-18__u-link {
  color: #e8eef7;
  text-decoration: none;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .08em;
  text-transform: uppercase;
  white-space: nowrap;
  padding-block: .3rem;
  transition: color .15s ease;
}

.hd-18__u-nav a:hover,
.hd-18__u-link:hover {
  color: #ffffff;
  text-decoration: underline;
  text-underline-offset: .25em;
}

.hd-18__u-right {
  display: flex;
  align-items: center;
  gap: .6rem;
  margin-inline-start: auto;
}

.hd-18__pipe {
  inline-size: 1px;
  block-size: .9rem;
  background: rgba(232,238,247,.32);
}

.hd-18__sel {
  position: relative;
}

.hd-18__sel-btn {
  display: inline-flex;
  align-items: center;
  gap: .35rem;
  min-block-size: 1.9rem;
  padding: .25rem .35rem;
  border: 0;
  border-radius: var(--r);
  background: transparent;
  color: #e8eef7;
  font: inherit;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .08em;
  text-transform: uppercase;
  white-space: nowrap;
  cursor: pointer;
}

.hd-18__sel-btn svg {
  inline-size: .9rem;
  block-size: .9rem;
}

.hd-18__sel-btn:hover {
  color: #fff;
  text-decoration: underline;
  text-underline-offset: .25em;
}

.hd-18__pop {
  position: absolute;
  inset-inline-end: 0;
  top: calc(100% + .25rem);
  z-index: 40;
  inline-size: 12rem;
  border: 1px solid var(--line);
  border-radius: var(--r);
  background: #fff;
  padding: .2rem;
  box-shadow: 0 .8rem 1.6rem -.8rem rgba(13,36,64,.4);
  visibility: hidden;
  opacity: 0;
  translate: 0 -.2rem;
  transition: opacity .14s ease, translate .14s ease, visibility .14s allow-discrete;
}

.hd-18__sel:hover > .hd-18__pop,
.hd-18__sel:focus-within > .hd-18__pop {
  visibility: visible;
  opacity: 1;
  translate: 0 0;
}

.hd-18__pop a {
  display: flex;
  align-items: center;
  min-block-size: 2.2rem;
  padding: .35rem .5rem;
  color: var(--ink);
  text-decoration: none;
  font-size: .8rem;
  text-transform: none;
  letter-spacing: 0;
}

.hd-18__pop a:hover {
  background: var(--panel);
}

.hd-18__pop a[aria-current="true"] {
  font-weight: 700;
  color: var(--accent);
  background: var(--panel);
}
/* ── tier 2: primary bar (sticky) ─────────────────────────────────── */

.hd-18__primary {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  gap: clamp(.75rem,3vw,2rem);
  padding: var(--pad-p) clamp(.6rem,2.5vw,1.5rem);
  background: var(--bg);
  border-bottom: 2px solid var(--ink);
}

.hd-18__brand {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  color: var(--ink);
  text-decoration: none;
  min-inline-size: 0;
}

.hd-18__mark {
  display: grid;
  place-items: center;
  inline-size: 2.1rem;
  block-size: 2.1rem;
  background: var(--ink);
  color: #fff;
  flex: none;
}

.hd-18__mark svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.hd-18__word {
  font-family: var(--font-display);
  font-size: .95rem;
  font-weight: 700;
  letter-spacing: -.01em;
  line-height: 1.2;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-18__word span {
  display: block;
  font-size: .66rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.hd-18__nav {
  min-inline-size: 0;
}

.hd-18__nav ul {
  display: flex;
  align-items: center;
  gap: clamp(.6rem,2vw,1.4rem);
}

.hd-18__nav a {
  display: block;
  padding: .7rem 0;
  color: var(--ink);
  text-decoration: none;
  font-size: .78rem;
  font-weight: 660;
  letter-spacing: .06em;
  text-transform: uppercase;
  white-space: nowrap;
  border-bottom: 3px solid transparent;
  transition: border-color .15s ease, color .15s ease;
}

.hd-18__nav a:hover {
  color: var(--accent);
  border-bottom-color: var(--accent);
}

.hd-18__nav a[aria-current="page"] {
  border-bottom-color: var(--accent);
  color: var(--accent);
}

.hd-18__p-right {
  display: flex;
  align-items: center;
  gap: .5rem;
  margin-inline-start: auto;
}

.hd-18__search {
  display: flex;
  align-items: center;
  gap: .4rem;
  inline-size: 11rem;
  min-inline-size: 0;
  min-block-size: 2.3rem;
  padding: .3rem .55rem;
  border: 1px solid var(--line);
  border-radius: var(--r);
  background: var(--bg);
  cursor: text;
}

.hd-18__search svg {
  inline-size: .95rem;
  block-size: .95rem;
  color: var(--muted);
  flex: none;
}

.hd-18__q {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: transparent;
  font: inherit;
  font-size: .82rem;
  color: var(--ink);
}

.hd-18__q:focus {
  outline: none;
}

.hd-18__search:focus-within {
  border-color: var(--accent);
  box-shadow: 0 0 0 2px rgba(26,86,176,.18);
}

.hd-18__cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.5rem;
  padding: .6rem 1.05rem;
  border-radius: var(--r);
  background: var(--accent);
  color: var(--accent-ink);
  text-decoration: none;
  font-size: .78rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  white-space: nowrap;
  transition: background-color .15s ease;
}

.hd-18__cta:hover {
  background: var(--ink);
}
/* ── page body ────────────────────────────────────────────────────── */

.hd-18__main {
  max-inline-size: 74rem;
  margin-inline: auto;
  padding: clamp(2rem,5vw,3rem) clamp(.75rem,3vw,1.5rem) 4rem;
}

.hd-18__eyebrow {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.hd-18__main h1 {
  font-family: var(--font-display);
  font-size: clamp(1.7rem,5vw,2.8rem);
  line-height: 1.1;
  font-weight: 700;
  letter-spacing: -.03em;
  margin-top: .8rem;
  max-inline-size: 30ch;
  text-wrap: balance;
}

.hd-18__lead {
  margin-top: 1rem;
  max-inline-size: 62ch;
  color: var(--muted);
  font-size: 1rem;
  text-wrap: pretty;
}

.hd-18__facts {
  display: grid;
  gap: 1px;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,11rem),1fr));
  margin-top: 2rem;
  background: var(--line);
  border: 1px solid var(--line);
}

.hd-18__facts li {
  padding: 1rem;
  background: var(--bg);
  min-inline-size: 0;
}

.hd-18__f-k {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.hd-18__f-v {
  font-family: var(--font-display);
  font-size: 1.8rem;
  font-weight: 700;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
  margin-top: .3rem;
}

.hd-18__filler {
  block-size: 50vh;
}

@media (max-width: 1000px) {
  .hd-18__search {
    display: none;
  }
}

@media (max-width: 860px) {
  .hd-18__nav {
    display: none;
  }
}

@media (max-width: 720px) {
  .hd-18__utility {
    overflow-x: auto;
    scrollbar-width: none;
  }

  .hd-18__utility::-webkit-scrollbar {
    display: none;
  }

  .hd-18__u-nav ul {
    gap: .75rem;
  }

  .hd-18__pop {
    inset-inline-end: auto;
    inset-inline-start: 0;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-18:has(#hd-18-dark:checked) {
  --bg: #0b1220;
  --u-bg: #060c16;
  --panel: #141d2c;
  --ink: #e9eff8;
  --muted: #9aabc2;
  --line: #26334a;
  --accent: #6ba6ff;
  --accent-ink: #06101f;
}

.hd-18:has(#hd-18-dark:checked) .hd-18__mark {
  background: var(--accent);
  color: #06101f;
}

.hd-18:has(#hd-18-dark:checked) .hd-18__pop {
  background: var(--panel);
}

.hd-18:has(#hd-18-dark:checked) .hd-18__cta:hover {
  background: #fff;
  color: #06101f;
}
/* icon: shows the scheme the toggle will switch you to */

.hd-18__sun {
  display: none;
}

.hd-18:has(#hd-18-dark:checked) .hd-18__moon {
  display: none;
}

.hd-18:has(#hd-18-dark:checked) .hd-18__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .hd-18:not([data-theme="light"]):not(:has(#hd-18-dark:checked)) {
    --bg: #0b1220;
    --u-bg: #060c16;
    --panel: #141d2c;
    --ink: #e9eff8;
    --muted: #9aabc2;
    --line: #26334a;
    --accent: #6ba6ff;
    --accent-ink: #06101f;
  }

  .hd-18:not([data-theme="light"]):not(:has(#hd-18-dark:checked)) .hd-18__mark {
    background: var(--accent);
    color: #06101f;
  }

  .hd-18:not([data-theme="light"]):not(:has(#hd-18-dark:checked)) .hd-18__pop {
    background: var(--panel);
  }

  .hd-18:not([data-theme="light"]):not(:has(#hd-18-dark:checked)) .hd-18__cta:hover {
    background: #fff;
    color: #06101f;
  }
  /* FLIP-BACK — dark OS + checked toggle returns to the other scheme */

  .hd-18:has(#hd-18-dark:checked) {
    --bg: #ffffff;
    --u-bg: #0d2440;
    --panel: #f4f6f9;
    --ink: #0d2440;
    --muted: #4a5b70;
    --line: #c9d3e0;
    --accent: #1a56b0;
    --accent-ink: #ffffff;
    --pad-u: .35rem;
    --pad-p: .55rem;
    --r: 0;
    --font-display: system-ui,-apple-system,"Segoe UI",Tahoma,sans-serif;
    --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  }

  .hd-18:has(#hd-18-dark:checked) .hd-18__mark {
    display: grid;
    place-items: center;
    inline-size: 2.1rem;
    block-size: 2.1rem;
    background: var(--ink);
    color: #fff;
    flex: none;
  }

  .hd-18:has(#hd-18-dark:checked) .hd-18__pop {
    position: absolute;
    inset-inline-end: 0;
    top: calc(100% + .25rem);
    z-index: 40;
    inline-size: 12rem;
    border: 1px solid var(--line);
    border-radius: var(--r);
    background: #fff;
    padding: .2rem;
    box-shadow: 0 .8rem 1.6rem -.8rem rgba(13,36,64,.4);
    visibility: hidden;
    opacity: 0;
    translate: 0 -.2rem;
    transition: opacity .14s ease, translate .14s ease, visibility .14s allow-discrete;
  }

  .hd-18:has(#hd-18-dark:checked) .hd-18__cta:hover {
    background: var(--ink);
  }
  /* the icon always offers the scheme you are not in */

  .hd-18:not([data-theme="light"]):not(:has(#hd-18-dark:checked)) .hd-18__moon {
    display: none;
  }

  .hd-18:not([data-theme="light"]):not(:has(#hd-18-dark:checked)) .hd-18__sun {
    display: block;
  }

  .hd-18:has(#hd-18-dark:checked) .hd-18__sun {
    display: none;
  }

  .hd-18:has(#hd-18-dark:checked) .hd-18__moon {
    display: block;
  }
}

.hd-18[data-theme="dark"] {
  --bg: #0b1220;
  --u-bg: #060c16;
  --panel: #141d2c;
  --ink: #e9eff8;
  --muted: #9aabc2;
  --line: #26334a;
  --accent: #6ba6ff;
  --accent-ink: #06101f;
}

@media (prefers-reduced-motion: reduce) {
  .hd-18 * {
    transition-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-18__pop {
    border: 1px solid CanvasText;
  }
}
/* ── theme toggle — visually hidden checkbox, zero JS ────────────── */

.hd-18__sr,
.hd-18__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-18__theme {
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

.hd-18__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-18__theme:hover {
  background: rgba(128,128,128,.16);
}

.hd-18:has(#hd-18-dark:focus-visible) .hd-18__theme {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```
