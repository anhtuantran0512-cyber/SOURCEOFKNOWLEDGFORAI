---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mega-menus/screen-reader-announcements-on-panel-open/"
title: "Screen Reader Announcements on Panel Open"
section: "navigation"
category: "css-mega-menus"
category_name: "CSS Mega Menus"
description: "Opening a large panel is a visual change that assistive technology also has to perceive."
has_js: "false"
---

Here's a working CSS Mega Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Screen Reader Announcements on Panel Open
Source: https://codefronts.com/navigation/css-mega-menus/screen-reader-announcements-on-panel-open/

Opening a large panel is a visual change that assistive technology also has to perceive. aria-expanded covers the state, but a panel with dozens of links needs an accessible name and a real heading structure so a user can navigate it by heading instead of tabbing through everything. This university header ships all three, plus a visually hidden count so people know what they are entering.
## HTML
```html
<section class="mm-11" aria-labelledby="mm-11-title">
  <h2 class="mm-11__sr" id="mm-11-title">Vale University</h2>

  <div class="mm-11__theme">
    <input class="mm-11__theme-input" type="checkbox" id="mm-11-theme">
    <label class="mm-11__theme-label" for="mm-11-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="mm-11__sr">Toggle dark theme</span>
    </label>
  </div>

  <header class="mm-11__header">
    <div class="mm-11__top">
      <span>Est. 1874</span>
      <a href="#mm-11-title">Staff and students</a>
      <a href="#mm-11-title">Library</a>
      <a href="#mm-11-title">Give</a>
    </div>

    <div class="mm-11__bar">
      <a class="mm-11__brand" href="#mm-11-title">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 4 2 9l10 5 10-5Z" fill="currentColor"/><path d="M6 12v4c0 1.7 2.7 3 6 3s6-1.3 6-3v-4" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>
        <span>Vale<b>University</b></span>
      </a>

      <nav class="mm-11__nav" aria-label="Primary">
        <ul class="mm-11__list">
          <li class="mm-11__item">
            <button class="mm-11__trigger" type="button" id="mm-11-trigger-study" aria-expanded="false" aria-controls="mm-11-panel-study">Study</button>
            <div class="mm-11__panel" id="mm-11-panel-study" aria-labelledby="mm-11-trigger-study">
              <p class="mm-11__sr">31 links in 4 groups.</p>
              <div class="mm-11__panel-inner">
                <section class="mm-11__col" aria-labelledby="mm-11-h-ug">
                  <h3 class="mm-11__col-head" id="mm-11-h-ug">Undergraduate</h3>
                  <ul class="mm-11__links"><li><a href="#mm-11-title">Courses A&ndash;Z</a></li><li><a href="#mm-11-title">Entry requirements</a></li><li><a href="#mm-11-title">Foundation year</a></li><li><a href="#mm-11-title">Open days</a></li><li><a href="#mm-11-title">Fees and funding</a></li></ul>
                </section>
                <section class="mm-11__col" aria-labelledby="mm-11-h-pg">
                  <h3 class="mm-11__col-head" id="mm-11-h-pg">Postgraduate</h3>
                  <ul class="mm-11__links"><li><a href="#mm-11-title">Taught masters</a></li><li><a href="#mm-11-title">Research degrees</a></li><li><a href="#mm-11-title">Doctoral college</a></li><li><a href="#mm-11-title">Scholarships</a></li></ul>
                </section>
                <section class="mm-11__col" aria-labelledby="mm-11-h-life">
                  <h3 class="mm-11__col-head" id="mm-11-h-life">Student life</h3>
                  <ul class="mm-11__links"><li><a href="#mm-11-title">Accommodation</a></li><li><a href="#mm-11-title">Campus map</a></li><li><a href="#mm-11-title">Wellbeing</a></li><li><a href="#mm-11-title">Clubs and societies</a></li></ul>
                </section>

                <aside class="mm-11__aside" aria-labelledby="mm-11-h-start">
                  <h3 class="mm-11__col-head" id="mm-11-h-start">Applying for 2027</h3>
                  <p class="mm-11__aside-body">Applications open on 1 October. Book a campus tour before you decide.</p>
                  <a class="mm-11__aside-cta" href="#mm-11-title">Book an open day</a>
                </aside>
              </div>
            </div>
          </li>

          <li class="mm-11__item">
            <button class="mm-11__trigger" type="button" id="mm-11-trigger-research" aria-expanded="false" aria-controls="mm-11-panel-research">Research</button>
            <div class="mm-11__panel" id="mm-11-panel-research" aria-labelledby="mm-11-trigger-research">
              <p class="mm-11__sr">12 links in 3 groups.</p>
              <div class="mm-11__panel-inner">
                <section class="mm-11__col" aria-labelledby="mm-11-h-inst">
                  <h3 class="mm-11__col-head" id="mm-11-h-inst">Institutes</h3>
                  <ul class="mm-11__links"><li><a href="#mm-11-title">Climate and coasts</a></li><li><a href="#mm-11-title">Population health</a></li><li><a href="#mm-11-title">Computation</a></li></ul>
                </section>
                <section class="mm-11__col" aria-labelledby="mm-11-h-work">
                  <h3 class="mm-11__col-head" id="mm-11-h-work">Work with us</h3>
                  <ul class="mm-11__links"><li><a href="#mm-11-title">Industry partnerships</a></li><li><a href="#mm-11-title">Consultancy</a></li><li><a href="#mm-11-title">Facilities hire</a></li></ul>
                </section>
                <section class="mm-11__col" aria-labelledby="mm-11-h-out">
                  <h3 class="mm-11__col-head" id="mm-11-h-out">Outputs</h3>
                  <ul class="mm-11__links"><li><a href="#mm-11-title">Publications</a></li><li><a href="#mm-11-title">Open data</a></li></ul>
                </section>
                <aside class="mm-11__aside" aria-labelledby="mm-11-h-fund">
                  <h3 class="mm-11__col-head" id="mm-11-h-fund">Funding calls</h3>
                  <p class="mm-11__aside-body">Six internal schemes close this term.</p>
                  <a class="mm-11__aside-cta" href="#mm-11-title">See all calls</a>
                </aside>
              </div>
            </div>
          </li>

          <li class="mm-11__item"><a class="mm-11__plain" href="#mm-11-title">About</a></li>
          <li class="mm-11__item"><a class="mm-11__plain" href="#mm-11-title">News</a></li>
        </ul>
      </nav>

      <a class="mm-11__cta" href="#mm-11-title">Apply</a>
    </div>
  </header>

  <main class="mm-11__page">
    <div class="mm-11__hero">
      <p class="mm-11__eyebrow">Clearing 2026</p>
      <h1 class="mm-11__h1">Places still available on 41 courses.</h1>
      <p class="mm-11__sub">Speak to an adviser today. Lines are open until 8pm.</p>
    </div>
  </main>
</section>
```
## CSS
```css
.mm-11 {
  --mm-11-bg: #eef0fa;
  --mm-11-surf: #ffffff;
  --mm-11-deep: #1e1b4b;
  --mm-11-line: #d4d7ee;
  --mm-11-ink: #171638;
  --mm-11-mut: #5d5f88;
  --mm-11-acc: #4338ca;
  --mm-11-acc: oklch(45% 0.21 277);
  --mm-11-on-acc: #ffffff;
  --mm-11-elev: 0.55;
  --mm-11-font-display: "Optima", "Gill Sans", "Segoe UI", ui-sans-serif, system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mm-11-bg);
  color: var(--mm-11-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.mm-11 *,
.mm-11 *::before,
.mm-11 *::after {
  box-sizing: border-box;
}

.mm-11 :focus-visible {
  outline: 2px solid var(--mm-11-acc);
  outline-offset: 3px;
  border-radius: 6px;
}

.mm-11__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.mm-11:has(.mm-11__theme-input:checked) {
  --mm-11-bg: #08081a;
  --mm-11-surf: #121233;
  --mm-11-deep: #0d0d26;
  --mm-11-line: #262657;
  --mm-11-ink: #eceafd;
  --mm-11-mut: #a2a3cd;
  --mm-11-acc: #a5b4fc;
  --mm-11-acc: oklch(78% 0.11 277);
  --mm-11-on-acc: #12100e;
}

@media (prefers-color-scheme: dark) {
  .mm-11 {
    --mm-11-bg: #08081a;
    --mm-11-surf: #121233;
    --mm-11-deep: #0d0d26;
    --mm-11-line: #262657;
    --mm-11-ink: #eceafd;
    --mm-11-mut: #a2a3cd;
    --mm-11-acc: #a5b4fc;
    --mm-11-acc: oklch(78% 0.11 277);
    --mm-11-on-acc: #12100e;
  }

  .mm-11:has(.mm-11__theme-input:checked) {
    --mm-11-bg: #eef0fa;
    --mm-11-surf: #ffffff;
    --mm-11-deep: #1e1b4b;
    --mm-11-line: #d4d7ee;
    --mm-11-ink: #171638;
    --mm-11-mut: #5d5f88;
    --mm-11-acc: #4338ca;
    --mm-11-acc: oklch(45% 0.21 277);
    --mm-11-on-acc: #ffffff;
  }
}

@media (prefers-color-scheme: light) {
  .mm-11:has(.mm-11__theme-input:checked) {
    --mm-11-bg: #08081a;
    --mm-11-surf: #121233;
    --mm-11-deep: #0d0d26;
    --mm-11-line: #262657;
    --mm-11-ink: #eceafd;
    --mm-11-mut: #a2a3cd;
    --mm-11-acc: #a5b4fc;
    --mm-11-acc: oklch(78% 0.11 277);
    --mm-11-on-acc: #12100e;
  }
}

.mm-11__theme {
  position: absolute;
  inset-block-start: 44px;
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 60;
}

.mm-11__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.mm-11__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mm-11-line);
  border-radius: 10px;
  background: var(--mm-11-surf);
  color: var(--mm-11-ink);
  cursor: pointer;
}

.mm-11__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-11__theme-input:focus-visible + .mm-11__theme-label {
  outline: 2px solid var(--mm-11-acc);
  outline-offset: 3px;
}

.mm-11__header {
  position: relative;
  z-index: 10;
  inline-size: 100%;
  background: var(--mm-11-surf);
  border-block-end: 1px solid var(--mm-11-line);
}

.mm-11__top {
  inline-size: min(78rem, calc(100% - 2rem));
  margin-inline: auto;
  display: flex;
  align-items: center;
  gap: 1.1rem;
  flex-wrap: wrap;
  min-block-size: 36px;
  border-block-end: 1px solid var(--mm-11-line);
  font: 500 0.74rem/1 system-ui, sans-serif;
  color: var(--mm-11-mut);
}

.mm-11__top a {
  color: var(--mm-11-mut);
  text-decoration: none;
}

.mm-11__top a:hover {
  color: var(--mm-11-acc);
}

.mm-11__top a:first-of-type {
  margin-inline-start: auto;
}

.mm-11__bar {
  inline-size: min(78rem, calc(100% - 2rem));
  margin-inline: auto;
  display: flex;
  align-items: center;
  gap: clamp(0.5rem, 2vw, 2rem);
  flex-wrap: wrap;
  min-block-size: 72px;
  padding-inline-end: 60px;
}

.mm-11__brand {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  color: var(--mm-11-ink);
  text-decoration: none;
}

.mm-11__brand svg {
  inline-size: 26px;
  block-size: 26px;
  color: var(--mm-11-acc);
}

.mm-11__brand span {
  display: grid;
  font: 400 1.15rem/1 var(--mm-11-font-display);
  letter-spacing: 0.02em;
}

.mm-11__brand b {
  font: 600 0.7rem/1.4 system-ui, sans-serif;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--mm-11-mut);
}

.mm-11__nav {
  min-inline-size: 0;
}

.mm-11__list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.2rem;
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
}

.mm-11__item {
  position: static;
}

.mm-11__trigger,
.mm-11__plain {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.9rem;
  border: 0;
  border-radius: 8px;
  background: transparent;
  color: var(--mm-11-ink);
  font: 600 0.98rem/1 var(--mm-11-font-display);
  letter-spacing: 0.01em;
  text-decoration: none;
  cursor: pointer;
}

.mm-11__item--open > .mm-11__trigger,
.mm-11__item:hover > .mm-11__trigger,
.mm-11__item:focus-within > .mm-11__trigger {
  background: color-mix(in oklab, var(--mm-11-acc) 14%, transparent);
  color: var(--mm-11-acc);
}

.mm-11__plain:hover,
.mm-11__trigger:hover {
  color: var(--mm-11-acc);
}

.mm-11__cta {
  margin-inline-start: auto;
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 1.3rem;
  border-radius: 8px;
  background: var(--mm-11-acc);
  color: var(--mm-11-on-acc);
  text-decoration: none;
  font: 600 0.9rem/1 var(--mm-11-font-display);
  letter-spacing: 0.04em;
}

.mm-11__panel {
  position: absolute;
  inset-inline: 0;
  inset-block-start: 100%;
  z-index: 30;
  background: var(--mm-11-surf);
  border-block-end: 1px solid var(--mm-11-line);
  box-shadow: 0 30px 60px -34px rgba(23, 22, 56, var(--mm-11-elev));
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 170ms ease, visibility 0s linear 170ms;
}

.mm-11__item--open > .mm-11__panel,
.mm-11__item:focus-within > .mm-11__panel {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transition-delay: 0s;
}

@media (hover: hover) {
  .mm-11__item:hover > .mm-11__panel {
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    transition-delay: 0s;
  }
}

.mm-11__panel-inner {
  inline-size: min(78rem, calc(100% - 2rem));
  margin-inline: auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 12rem), 1fr));
  gap: clamp(0.75rem, 2.4vw, 2rem);
  padding-block: clamp(1.1rem, 3vw, 1.9rem);
}

.mm-11__col {
  min-inline-size: 0;
}

.mm-11__col-head {
  margin: 0 0 0.45rem;
  padding-block-end: 0.4rem;
  border-block-end: 1px solid var(--mm-11-line);
  font: 600 0.98rem/1.2 var(--mm-11-font-display);
}

.mm-11__links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1px;
}

.mm-11__links a {
  display: flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.5rem;
  margin-inline: -0.5rem;
  border-radius: 6px;
  color: var(--mm-11-mut);
  text-decoration: none;
  font-size: 0.89rem;
  min-inline-size: 0;
}

.mm-11__links a:hover {
  color: var(--mm-11-acc);
  background: color-mix(in oklab, var(--mm-11-acc) 9%, transparent);
}

.mm-11__aside {
  min-inline-size: 0;
  padding: 0.9rem 1rem;
  border-radius: 12px;
  background: color-mix(in oklab, var(--mm-11-acc) 10%, transparent);
}

.mm-11__aside .mm-11__col-head {
  border-block-end: 0;
  padding-block-end: 0;
}

.mm-11__aside-body {
  margin: 0 0 0.4rem;
  font-size: 0.87rem;
  color: var(--mm-11-mut);
  text-wrap: pretty;
}

.mm-11__aside-cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  color: var(--mm-11-acc);
  font: 600 0.88rem/1 var(--mm-11-font-display);
  text-decoration: none;
}

.mm-11__aside-cta:hover {
  text-decoration: underline;
  text-underline-offset: 3px;
}

.mm-11__page {
  inline-size: min(78rem, calc(100% - 2rem));
  margin-inline: auto;
  padding-block: clamp(3rem, 9vw, 5.5rem);
}

.mm-11__hero {
  max-inline-size: 40rem;
  display: grid;
  gap: 0.6rem;
}

.mm-11__eyebrow {
  margin: 0;
  font: 700 0.68rem/1 system-ui, sans-serif;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--mm-11-acc);
}

.mm-11__h1 {
  margin: 0;
  font: 400 clamp(2rem, 6vw, 3.5rem)/1.06 var(--mm-11-font-display);
  letter-spacing: -0.01em;
  text-wrap: balance;
}

.mm-11__sub {
  margin: 0;
  color: var(--mm-11-mut);
  font-size: clamp(0.95rem, 2.3vw, 1.1rem);
  text-wrap: pretty;
}

@media (max-width: 54rem) {
  .mm-11__bar {
    flex-direction: column;
    align-items: stretch;
    padding-block: 0.6rem;
  }

  .mm-11__list {
    flex-direction: column;
  }

  .mm-11__cta {
    margin-inline-start: 0;
    justify-content: center;
  }

  .mm-11__panel {
    position: static;
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    box-shadow: none;
    display: none;
  }

  .mm-11__item--open > .mm-11__panel,
    .mm-11__item:focus-within > .mm-11__panel {
    display: block;
  }

  .mm-11__panel-inner {
    inline-size: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .mm-11__panel {
    transition-duration: 1ms;
  }
}

@media (hover: hover) and (pointer: fine) {
  .mm-11__trigger {
    position: relative;
  }

  .mm-11__item:hover > .mm-11__trigger::after,
    .mm-11__item:focus-within > .mm-11__trigger::after {
    content: "";
    position: absolute;
    inset-inline: 0;
    inset-block-start: 100%;
    block-size: 16px;
  }
}
/* Entry signature — the panel resolves out of a blur; nothing moves (calmest possible reveal) */

.mm-11__panel-inner {
  filter: blur(8px);
  opacity: 0;
  transition: filter 340ms ease, opacity 260ms ease;
}

.mm-11__item:hover > .mm-11__panel .mm-11__panel-inner,
.mm-11__item:focus-within > .mm-11__panel .mm-11__panel-inner,
.mm-11__item--open > .mm-11__panel .mm-11__panel-inner {
  filter: blur(0);
  opacity: 1;
}

.mm-11__col {
  opacity: 0;
  transition: opacity 320ms ease;
}

.mm-11__item:hover > .mm-11__panel .mm-11__col,
.mm-11__item:focus-within > .mm-11__panel .mm-11__col,
.mm-11__item--open > .mm-11__panel .mm-11__col {
  opacity: 1;
}

.mm-11__col:nth-child(1) {
  transition-delay: 60ms;
}

.mm-11__col:nth-child(2) {
  transition-delay: 120ms;
}

.mm-11__col:nth-child(3) {
  transition-delay: 180ms;
}

.mm-11__col:nth-child(4) {
  transition-delay: 240ms;
}

.mm-11__col:nth-child(n+5) {
  transition-delay: 240ms;
}

@media (prefers-reduced-motion: reduce) {
  .mm-11__panel-inner,
    .mm-11__col {
    transition-duration: 1ms;
    transition-delay: 0s;
    animation: none;
  }

  .mm-11__panel-inner {
    filter: none;
    opacity: 1;
  }

  .mm-11__col {
    opacity: 1;
  }
}
```
