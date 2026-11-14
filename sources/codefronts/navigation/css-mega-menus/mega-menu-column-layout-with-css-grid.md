---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mega-menus/mega-menu-column-layout-with-css-grid/"
title: "Mega Menu Column Layout with CSS Grid"
section: "navigation"
category: "css-mega-menus"
category_name: "CSS Mega Menus"
description: "The panel treated purely as a grid problem, on a publishing workspace that has genuinely uneven sections."
has_js: "false"
---

Here's a working CSS Mega Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mega Menu Column Layout with CSS Grid
Source: https://codefronts.com/navigation/css-mega-menus/mega-menu-column-layout-with-css-grid/

The panel treated purely as a grid problem, on a publishing workspace that has genuinely uneven sections. minmax(0, 1fr) stops one long link from blowing out a track, subgrid lines the column footers up across sections of different lengths, and repeat(auto-fit, …) makes the column count follow the content instead of a media query per breakpoint.
## HTML
```html
<section class="mm-04" aria-labelledby="mm-04-title">
  <h2 class="mm-04__sr" id="mm-04-title">Quill</h2>

  <div class="mm-04__theme">
    <input class="mm-04__theme-input" type="checkbox" id="mm-04-theme">
    <label class="mm-04__theme-label" for="mm-04-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="mm-04__sr">Toggle dark theme</span>
    </label>
  </div>

  <header class="mm-04__header">
    <div class="mm-04__bar">
      <a class="mm-04__brand" href="#mm-04-title">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 19c6-1 10-5 13-14-6 1-11 4-13 10Z" fill="currentColor" opacity=".85"/><path d="M5 19c2-4 5-6 8-7" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>
        Quill
      </a>

      <nav class="mm-04__nav" aria-label="Primary">
        <ul class="mm-04__list">
          <li class="mm-04__item">
            <button class="mm-04__trigger" type="button" aria-expanded="false" aria-controls="mm-04-panel-library">Library</button>
            <div class="mm-04__panel" id="mm-04-panel-library" aria-label="Library">
              <div class="mm-04__panel-inner">
                <section class="mm-04__col" aria-labelledby="mm-04-h-writing">
                  <h3 class="mm-04__col-head" id="mm-04-h-writing">Writing</h3>
                  <ul class="mm-04__links">
                    <li><a href="#mm-04-title">Drafts</a></li>
                    <li><a href="#mm-04-title">Style guide</a></li>
                    <li><a href="#mm-04-title">Collaborative review workflow</a></li>
                    <li><a href="#mm-04-title">Version history</a></li>
                    <li><a href="#mm-04-title">Templates</a></li>
                  </ul>
                  <p class="mm-04__count">18 documents</p>
                </section>
                <section class="mm-04__col" aria-labelledby="mm-04-h-publish">
                  <h3 class="mm-04__col-head" id="mm-04-h-publish">Publish</h3>
                  <ul class="mm-04__links">
                    <li><a href="#mm-04-title">Scheduling</a></li>
                    <li><a href="#mm-04-title">Distribution channels</a></li>
                    <li><a href="#mm-04-title">Newsletter</a></li>
                  </ul>
                  <p class="mm-04__count">2 channels live</p>
                </section>
                <section class="mm-04__col" aria-labelledby="mm-04-h-measure">
                  <h3 class="mm-04__col-head" id="mm-04-h-measure">Measure</h3>
                  <ul class="mm-04__links">
                    <li><a href="#mm-04-title">Readership</a></li>
                    <li><a href="#mm-04-title">Retention cohorts</a></li>
                    <li><a href="#mm-04-title">Referrals</a></li>
                    <li><a href="#mm-04-title">Export to warehouse</a></li>
                  </ul>
                  <p class="mm-04__count">updated hourly</p>
                </section>
                <section class="mm-04__col" aria-labelledby="mm-04-h-admin">
                  <h3 class="mm-04__col-head" id="mm-04-h-admin">Administration</h3>
                  <ul class="mm-04__links">
                    <li><a href="#mm-04-title">Enterprise single sign-on configuration</a></li>
                    <li><a href="#mm-04-title">Billing</a></li>
                  </ul>
                  <p class="mm-04__count">owner only</p>
                </section>
              </div>
              <div class="mm-04__panel-foot">
                <a href="#mm-04-title">Keyboard shortcuts</a>
                <a href="#mm-04-title">Import from Markdown</a>
                <a href="#mm-04-title">What's new</a>
              </div>
            </div>
          </li>

          <li class="mm-04__item">
            <button class="mm-04__trigger" type="button" aria-expanded="false" aria-controls="mm-04-panel-teams">Teams</button>
            <div class="mm-04__panel" id="mm-04-panel-teams" aria-label="Teams">
              <div class="mm-04__panel-inner">
                <section class="mm-04__col" aria-labelledby="mm-04-h-people">
                  <h3 class="mm-04__col-head" id="mm-04-h-people">People</h3>
                  <ul class="mm-04__links"><li><a href="#mm-04-title">Members</a></li><li><a href="#mm-04-title">Guest editors</a></li><li><a href="#mm-04-title">Roles</a></li></ul>
                  <p class="mm-04__count">34 seats</p>
                </section>
                <section class="mm-04__col" aria-labelledby="mm-04-h-spaces">
                  <h3 class="mm-04__col-head" id="mm-04-h-spaces">Spaces</h3>
                  <ul class="mm-04__links"><li><a href="#mm-04-title">Newsroom</a></li><li><a href="#mm-04-title">Longform</a></li></ul>
                  <p class="mm-04__count">2 spaces</p>
                </section>
                <section class="mm-04__col" aria-labelledby="mm-04-h-flow">
                  <h3 class="mm-04__col-head" id="mm-04-h-flow">Workflow</h3>
                  <ul class="mm-04__links"><li><a href="#mm-04-title">Approvals</a></li><li><a href="#mm-04-title">Fact checking</a></li><li><a href="#mm-04-title">Legal review</a></li><li><a href="#mm-04-title">Embargoes</a></li></ul>
                  <p class="mm-04__count">4 stages</p>
                </section>
              </div>
              <div class="mm-04__panel-foot"><a href="#mm-04-title">Invite a teammate</a></div>
            </div>
          </li>

          <li class="mm-04__item"><a class="mm-04__plain" href="#mm-04-title">Pricing</a></li>
          <li class="mm-04__item"><a class="mm-04__plain" href="#mm-04-title">Help</a></li>
        </ul>
      </nav>

      <div class="mm-04__utils">
        <a class="mm-04__signin" href="#mm-04-title">Log in</a>
        <a class="mm-04__cta" href="#mm-04-title">New document</a>
      </div>
    </div>
  </header>

  <main class="mm-04__page">
    <article class="mm-04__intro">
      <p class="mm-04__eyebrow">Quill for editorial teams</p>
      <h1 class="mm-04__title">Write, review and publish in one place.</h1>
      <p class="mm-04__lede">Drafts that never leave the workflow. Fact checks that stay attached to the sentence. A publish button that knows which channels are live.</p>
    </article>
  </main>
</section>
```
## CSS
```css
.mm-04 {
  --mm-04-bg: #faf6ef;
  --mm-04-surf: #fffdf9;
  --mm-04-line: #e7ddcd;
  --mm-04-ink: #241d14;
  --mm-04-mut: #766a58;
  --mm-04-acc: #9a3412;
  --mm-04-acc: oklch(48% 0.16 40);
  --mm-04-min: 11rem;
  --mm-04-gap: clamp(0.85rem, 2.4vw, 2rem);
  --mm-04-font-display: "Roboto Slab", ui-serif, Georgia, "Times New Roman", serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mm-04-bg);
  color: var(--mm-04-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.mm-04 *,
.mm-04 *::before,
.mm-04 *::after {
  box-sizing: border-box;
}

.mm-04 :focus-visible {
  outline: 2px solid var(--mm-04-acc);
  outline-offset: 3px;
  border-radius: 4px;
}

.mm-04__sr {
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

.mm-04:has(.mm-04__theme-input:checked) {
  --mm-04-bg: #14100b;
  --mm-04-surf: #1d1811;
  --mm-04-line: #342b1f;
  --mm-04-ink: #f6efe3;
  --mm-04-mut: #ab9c85;
  --mm-04-acc: #fb923c;
  --mm-04-acc: oklch(76% 0.16 55);
}

@media (prefers-color-scheme: dark) {
  .mm-04 {
    --mm-04-bg: #14100b;
    --mm-04-surf: #1d1811;
    --mm-04-line: #342b1f;
    --mm-04-ink: #f6efe3;
    --mm-04-mut: #ab9c85;
    --mm-04-acc: #fb923c;
    --mm-04-acc: oklch(76% 0.16 55);
  }

  .mm-04:has(.mm-04__theme-input:checked) {
    --mm-04-bg: #faf6ef;
    --mm-04-surf: #fffdf9;
    --mm-04-line: #e7ddcd;
    --mm-04-ink: #241d14;
    --mm-04-mut: #766a58;
    --mm-04-acc: #9a3412;
    --mm-04-acc: oklch(48% 0.16 40);
  }
}

@media (prefers-color-scheme: light) {
  .mm-04:has(.mm-04__theme-input:checked) {
    --mm-04-bg: #14100b;
    --mm-04-surf: #1d1811;
    --mm-04-line: #342b1f;
    --mm-04-ink: #f6efe3;
    --mm-04-mut: #ab9c85;
    --mm-04-acc: #fb923c;
    --mm-04-acc: oklch(76% 0.16 55);
  }
}

.mm-04__theme {
  position: absolute;
  inset-block-start: 12px;
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 60;
}

.mm-04__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.mm-04__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mm-04-line);
  border-radius: 999px;
  background: var(--mm-04-surf);
  color: var(--mm-04-ink);
  cursor: pointer;
}

.mm-04__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-04__theme-input:focus-visible + .mm-04__theme-label {
  outline: 2px solid var(--mm-04-acc);
  outline-offset: 3px;
}

.mm-04__header {
  position: relative;
  z-index: 10;
  inline-size: 100%;
  background: var(--mm-04-surf);
  border-block-end: 1px solid var(--mm-04-line);
}

.mm-04__bar {
  inline-size: min(78rem, calc(100% - 2rem));
  margin-inline: auto;
  display: flex;
  align-items: center;
  gap: clamp(0.5rem, 2vw, 2rem);
  flex-wrap: wrap;
  min-block-size: 66px;
  padding-inline-end: 60px;
}

.mm-04__brand {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  color: var(--mm-04-ink);
  text-decoration: none;
  font: 600 1.25rem/1 var(--mm-04-font-display);
}

.mm-04__brand svg {
  inline-size: 22px;
  block-size: 22px;
  color: var(--mm-04-acc);
}

.mm-04__nav {
  min-inline-size: 0;
}

.mm-04__list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.15rem;
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
}

.mm-04__item {
  position: static;
}

.mm-04__trigger,
.mm-04__plain {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.85rem;
  border: 0;
  background: transparent;
  color: var(--mm-04-ink);
  font: 600 0.92rem/1 system-ui, sans-serif;
  text-decoration: none;
  cursor: pointer;
}

.mm-04__item--open > .mm-04__trigger,
.mm-04__item:hover > .mm-04__trigger,
.mm-04__item:focus-within > .mm-04__trigger {
  color: var(--mm-04-acc);
  box-shadow: inset 0 -2px 0 var(--mm-04-acc);
}

.mm-04__plain:hover,
.mm-04__trigger:hover {
  color: var(--mm-04-acc);
}

.mm-04__utils {
  margin-inline-start: auto;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.mm-04__signin {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.6rem;
  color: var(--mm-04-mut);
  text-decoration: none;
  font: 600 0.88rem/1 system-ui, sans-serif;
}

.mm-04__cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 1rem;
  border: 1px solid var(--mm-04-ink);
  background: var(--mm-04-ink);
  color: var(--mm-04-surf);
  text-decoration: none;
  font: 600 0.88rem/1 system-ui, sans-serif;
}

.mm-04__panel {
  position: absolute;
  inset-inline: 0;
  inset-block-start: 100%;
  z-index: 30;
  background: var(--mm-04-surf);
  border-block-end: 1px solid var(--mm-04-line);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity 160ms ease, visibility 0s linear 160ms;
}

.mm-04__item--open > .mm-04__panel,
.mm-04__item:focus-within > .mm-04__panel {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transition-delay: 0s;
}

@media (hover: hover) {
  .mm-04__item:hover > .mm-04__panel {
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    transition-delay: 0s;
  }
}

.mm-04__panel-inner {
  inline-size: min(78rem, calc(100% - 2rem));
  margin-inline: auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(var(--mm-04-min), 1fr));
  grid-template-rows: auto minmax(0, 1fr) auto;
  column-gap: var(--mm-04-gap);
  row-gap: 0.3rem;
  padding-block: clamp(1.1rem, 3vw, 1.9rem) 0;
}

.mm-04__col {
  min-inline-size: 0;
  display: grid;
  grid-template-rows: auto minmax(0, 1fr) auto;
  grid-row: span 3;
  gap: 0.4rem;
}

@supports (grid-template-rows: subgrid) {
  .mm-04__col {
    grid-template-rows: subgrid;
  }
}

.mm-04__col-head {
  margin: 0;
  font: 600 1rem/1.2 var(--mm-04-font-display);
}

.mm-04__links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  align-content: start;
  gap: 1px;
}

.mm-04__links a {
  display: flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.4rem;
  margin-inline: -0.4rem;
  border-radius: 4px;
  color: var(--mm-04-mut);
  text-decoration: none;
  font-size: 0.89rem;
  min-inline-size: 0;
  text-wrap: pretty;
}

.mm-04__links a:hover {
  color: var(--mm-04-acc);
  background: color-mix(in oklab, var(--mm-04-acc) 8%, transparent);
}

.mm-04__count {
  margin: 0;
  padding-block: 0.5rem;
  border-block-start: 1px solid var(--mm-04-line);
  font: 500 0.7rem/1.4 var(--mm-04-font-display);
  letter-spacing: 0.05em;
  color: var(--mm-04-mut);
}

.mm-04__panel-foot {
  inline-size: min(78rem, calc(100% - 2rem));
  margin-inline: auto;
  display: flex;
  flex-wrap: wrap;
  gap: clamp(0.75rem, 3vw, 2rem);
  padding-block: 0.25rem 0.9rem;
}

.mm-04__panel-foot a {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  color: var(--mm-04-ink);
  text-decoration: none;
  font: 600 0.8rem/1 system-ui, sans-serif;
}

.mm-04__panel-foot a:hover {
  color: var(--mm-04-acc);
  text-decoration: underline;
  text-underline-offset: 3px;
}

.mm-04__page {
  inline-size: min(78rem, calc(100% - 2rem));
  margin-inline: auto;
  padding-block: clamp(3rem, 10vw, 6rem);
}

.mm-04__intro {
  max-inline-size: 42rem;
  display: grid;
  gap: 0.7rem;
}

.mm-04__eyebrow {
  margin: 0;
  font: 600 0.7rem/1 system-ui, sans-serif;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--mm-04-acc);
}

.mm-04__title {
  margin: 0;
  font: 600 clamp(2rem, 6vw, 3.4rem)/1.05 var(--mm-04-font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.mm-04__lede {
  margin: 0;
  color: var(--mm-04-mut);
  font-size: clamp(0.95rem, 2.4vw, 1.1rem);
  text-wrap: pretty;
}

@media (max-width: 52rem) {
  .mm-04__bar {
    flex-direction: column;
    align-items: stretch;
    padding-block: 0.5rem;
  }

  .mm-04__list {
    flex-direction: column;
  }

  .mm-04__utils {
    margin-inline-start: 0;
  }

  .mm-04__panel {
    position: static;
    opacity: 1;
    visibility: visible;
    pointer-events: auto;
    display: none;
  }

  .mm-04__item--open > .mm-04__panel,
    .mm-04__item:focus-within > .mm-04__panel {
    display: block;
  }

  .mm-04__panel-inner,
    .mm-04__panel-foot {
    inline-size: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .mm-04__panel {
    transition-duration: 1ms;
  }
}

@media (hover: hover) and (pointer: fine) {
  .mm-04__trigger {
    position: relative;
  }

  .mm-04__item:hover > .mm-04__trigger::after,
    .mm-04__item:focus-within > .mm-04__trigger::after {
    content: "";
    position: absolute;
    inset-inline: 0;
    inset-block-start: 100%;
    block-size: 16px;
  }
}
/* Entry signature — each grid column unrolls downward, one after the next */

.mm-04__col {
  clip-path: inset(0 0 100% 0);
  opacity: 0;
  transition: clip-path 400ms cubic-bezier(0.4, 0, 0.2, 1), opacity 200ms ease;
}

.mm-04__item:hover > .mm-04__panel .mm-04__col,
.mm-04__item:focus-within > .mm-04__panel .mm-04__col,
.mm-04__item--open > .mm-04__panel .mm-04__col {
  clip-path: inset(-8px);
  opacity: 1;
}

.mm-04__col:nth-child(1) {
  transition-delay: 30ms;
}

.mm-04__col:nth-child(2) {
  transition-delay: 105ms;
}

.mm-04__col:nth-child(3) {
  transition-delay: 180ms;
}

.mm-04__col:nth-child(4) {
  transition-delay: 255ms;
}

.mm-04__col:nth-child(5) {
  transition-delay: 330ms;
}

.mm-04__col:nth-child(n+6) {
  transition-delay: 330ms;
}

.mm-04__panel-foot {
  opacity: 0;
  transition: opacity 260ms ease 340ms;
}

.mm-04__item:hover > .mm-04__panel .mm-04__panel-foot,
.mm-04__item:focus-within > .mm-04__panel .mm-04__panel-foot,
.mm-04__item--open > .mm-04__panel .mm-04__panel-foot {
  opacity: 1;
}

@media (prefers-reduced-motion: reduce) {
  .mm-04__col,
    .mm-04__panel-foot {
    transition-duration: 1ms;
    transition-delay: 0s;
    animation: none;
  }

  .mm-04__col {
    clip-path: none;
    opacity: 1;
  }

  .mm-04__panel-foot {
    opacity: 1;
  }
}
```
