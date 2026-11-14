---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mega-menus/keyboard-accessible-mega-menu-with-escape/"
title: "Keyboard Accessible Mega Menu with Escape"
section: "navigation"
category: "css-mega-menus"
category_name: "CSS Mega Menus"
description: "Everything :focus-within cannot do, on a dark application shell where keyboard users live."
has_js: "true"
---

Here's a working CSS Mega Menu from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Keyboard Accessible Mega Menu with Escape
Source: https://codefronts.com/navigation/css-mega-menus/keyboard-accessible-mega-menu-with-escape/

Everything :focus-within cannot do, on a dark application shell where keyboard users live. Escape closes the panel and returns focus to its trigger, Tab moves through the panel and closes it when focus leaves the item entirely, and Enter or Space toggles. One state object drives both the class and aria-expanded, so the attribute never lies.
## HTML
```html
<section class="mm-07" aria-labelledby="mm-07-title">
  <h2 class="mm-07__sr" id="mm-07-title">Talon workspace</h2>

  <div class="mm-07__theme">
    <input class="mm-07__theme-input" type="checkbox" id="mm-07-theme">
    <label class="mm-07__theme-label" for="mm-07-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="mm-07__sr">Toggle dark theme</span>
    </label>
  </div>

  <header class="mm-07__header">
    <div class="mm-07__bar">
      <a class="mm-07__brand" href="#mm-07-title">TALON</a>
      <span class="mm-07__ws">
        <span class="mm-07__ws-dot" aria-hidden="true"></span>
        Northwind &middot; production
      </span>

      <nav class="mm-07__nav" aria-label="Primary">
        <ul class="mm-07__list">
          <li class="mm-07__item">
            <button class="mm-07__trigger" type="button" aria-expanded="false" aria-controls="mm-07-panel-workspace">Workspace</button>
            <div class="mm-07__panel" id="mm-07-panel-workspace" aria-label="Workspace">
              <div class="mm-07__panel-inner">
                <ul class="mm-07__grid">
                  <li><a href="#mm-07-title">
                    <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="3" y="4" width="18" height="16" rx="2" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M3 9h18" stroke="currentColor" stroke-width="1.7"/></svg>
                    <b>Projects</b><span>34 active</span></a></li>
                  <li><a href="#mm-07-title">
                    <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="9" cy="8" r="3.2" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M3.5 19c.8-3.2 3-4.8 5.5-4.8s4.7 1.6 5.5 4.8" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M17 7.5a2.8 2.8 0 0 1 0 5.4" fill="none" stroke="currentColor" stroke-width="1.7"/></svg>
                    <b>People</b><span>128 seats</span></a></li>
                  <li><a href="#mm-07-title">
                    <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 18V9m5 9V5m5 13v-6m5 6V8" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
                    <b>Insights</b><span>daily digest</span></a></li>
                  <li><a href="#mm-07-title">
                    <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 3.5 20 8v8l-8 4.5L4 16V8Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
                    <b>Automations</b><span>12 running</span></a></li>
                  <li><a href="#mm-07-title">
                    <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="3.2" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M12 3v3m0 12v3M3 12h3m12 0h3M5.6 5.6 7.7 7.7m8.6 8.6 2.1 2.1m0-13.4-2.1 2.1M7.7 16.3l-2.1 2.1" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
                    <b>Settings</b><span>workspace</span></a></li>
                  <li><a href="#mm-07-title">
                    <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M6 4h9l3 3v13H6Z" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M9 12h6M9 16h4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
                    <b>Audit log</b><span>90 days</span></a></li>
                </ul>
                <div class="mm-07__switch">
                  <p class="mm-07__switch-head">Switch workspace</p>
                  <ul class="mm-07__switch-list">
                    <li><a href="#mm-07-title"><span class="mm-07__mark" aria-hidden="true">NW</span>Northwind<span class="mm-07__meta">production</span></a></li>
                    <li><a href="#mm-07-title"><span class="mm-07__mark" aria-hidden="true">OR</span>Orbit Retail<span class="mm-07__meta">staging</span></a></li>
                    <li><a href="#mm-07-title"><span class="mm-07__mark" aria-hidden="true">FS</span>Fern Studio<span class="mm-07__meta">sandbox</span></a></li>
                  </ul>
                </div>
              </div>
            </div>
          </li>

          <li class="mm-07__item">
            <button class="mm-07__trigger" type="button" aria-expanded="false" aria-controls="mm-07-panel-develop">Develop</button>
            <div class="mm-07__panel" id="mm-07-panel-develop" aria-label="Develop">
              <div class="mm-07__panel-inner">
                <ul class="mm-07__grid">
                  <li><a href="#mm-07-title"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m9 8-5 4 5 4m6-8 5 4-5 4" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg><b>API reference</b><span>v4</span></a></li>
                  <li><a href="#mm-07-title"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 5h14v14H5Z" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M8 9h8M8 13h5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg><b>Migration guide</b><span>3 to 4</span></a></li>
                  <li><a href="#mm-07-title"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M12 8v4l3 2" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg><b>Status page</b><span>all systems go</span></a></li>
                  <li><a href="#mm-07-title"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 4v10m0 0-4-4m4 4 4-4M5 19h14" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg><b>CLI download</b><span>1.9 MB</span></a></li>
                </ul>
                <div class="mm-07__switch">
                  <p class="mm-07__switch-head">Recent</p>
                  <ul class="mm-07__switch-list">
                    <li><a href="#mm-07-title"><span class="mm-07__mark" aria-hidden="true">#</span>4471 queue latency<span class="mm-07__meta">open</span></a></li>
                    <li><a href="#mm-07-title"><span class="mm-07__mark" aria-hidden="true">#</span>4468 canary rollout<span class="mm-07__meta">merged</span></a></li>
                  </ul>
                </div>
              </div>
            </div>
          </li>

          <li class="mm-07__item"><a class="mm-07__plain" href="#mm-07-title">Billing</a></li>
        </ul>
      </nav>

      <div class="mm-07__utils">
        <span class="mm-07__kbd" aria-hidden="true"><kbd>&#8984;</kbd><kbd>K</kbd></span>
        <span class="mm-07__avatar" aria-hidden="true">PS</span>
      </div>
    </div>
  </header>

  <main class="mm-07__page">
    <div class="mm-07__canvas">
      <div class="mm-07__col-board">
        <p class="mm-07__board-head">In progress <span>4</span></p>
        <article class="mm-07__ticket"><b>Region failover drill</b><span>Priya Sharma &middot; due Fri</span></article>
        <article class="mm-07__ticket"><b>Trim CLI binary</b><span>Sam Rivera &middot; due Mon</span></article>
      </div>
      <div class="mm-07__col-board">
        <p class="mm-07__board-head">In review <span>2</span></p>
        <article class="mm-07__ticket"><b>Read replica docs</b><span>Alex Chen &middot; 2 approvals</span></article>
      </div>
      <div class="mm-07__col-board">
        <p class="mm-07__board-head">Shipped <span>9</span></p>
        <article class="mm-07__ticket mm-07__ticket--done"><b>Canary rollout v4.2</b><span>Jordan Lee &middot; today</span></article>
      </div>
    </div>
  </main>
</section>
```
## CSS
```css
.mm-07 {
  --mm-07-bg: #000000;
  --mm-07-surf: #0c0c10;
  --mm-07-panel: #101016;
  --mm-07-line: #23232b;
  --mm-07-ink: #f4f4f6;
  --mm-07-mut: #8c8c99;
  --mm-07-accent: #a78bfa;
  --mm-07-accent: oklch(76% 0.15 295);
  --mm-07-on-accent: #12100e;
  --mm-07-lift: 8px;
  --mm-07-font-display: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--mm-07-bg);
  color: var(--mm-07-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.mm-07 *,
.mm-07 *::before,
.mm-07 *::after {
  box-sizing: border-box;
}

.mm-07 :focus-visible {
  outline: 2px solid var(--mm-07-accent);
  outline-offset: 3px;
  border-radius: 6px;
}

.mm-07__sr {
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

.mm-07:has(.mm-07__theme-input:checked) {
  --mm-07-bg: #f5f5f7;
  --mm-07-surf: #ffffff;
  --mm-07-panel: #ffffff;
  --mm-07-line: #dededf;
  --mm-07-ink: #101014;
  --mm-07-mut: #62626b;
  --mm-07-accent: #6d28d9;
  --mm-07-accent: oklch(46% 0.22 296);
  --mm-07-on-accent: #ffffff;
}

@media (prefers-color-scheme: light) {
  .mm-07 {
    --mm-07-bg: #f5f5f7;
    --mm-07-surf: #ffffff;
    --mm-07-panel: #ffffff;
    --mm-07-line: #dededf;
    --mm-07-ink: #101014;
    --mm-07-mut: #62626b;
    --mm-07-accent: #6d28d9;
    --mm-07-accent: oklch(46% 0.22 296);
    --mm-07-on-accent: #ffffff;
  }

  .mm-07:has(.mm-07__theme-input:checked) {
    --mm-07-bg: #000000;
    --mm-07-surf: #0c0c10;
    --mm-07-panel: #101016;
    --mm-07-line: #23232b;
    --mm-07-ink: #f4f4f6;
    --mm-07-mut: #8c8c99;
    --mm-07-accent: #a78bfa;
    --mm-07-accent: oklch(76% 0.15 295);
    --mm-07-on-accent: #12100e;
  }
}

@media (prefers-color-scheme: dark) {
  .mm-07:has(.mm-07__theme-input:checked) {
    --mm-07-bg: #f5f5f7;
    --mm-07-surf: #ffffff;
    --mm-07-panel: #ffffff;
    --mm-07-line: #dededf;
    --mm-07-ink: #101014;
    --mm-07-mut: #62626b;
    --mm-07-accent: #6d28d9;
    --mm-07-accent: oklch(46% 0.22 296);
    --mm-07-on-accent: #ffffff;
  }
}

.mm-07__theme {
  position: absolute;
  inset-block-start: 11px;
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 60;
}

.mm-07__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.mm-07__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--mm-07-line);
  border-radius: 3px;
  background: var(--mm-07-surf);
  color: var(--mm-07-ink);
  cursor: pointer;
}

.mm-07__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.mm-07__theme-input:focus-visible + .mm-07__theme-label {
  outline: 2px solid var(--mm-07-accent);
  outline-offset: 3px;
}

.mm-07__header {
  position: relative;
  z-index: 10;
  inline-size: 100%;
  background: var(--mm-07-surf);
  border-block-end: 1px solid var(--mm-07-line);
}

.mm-07__bar {
  inline-size: min(84rem, calc(100% - 2rem));
  margin-inline: auto;
  display: flex;
  align-items: center;
  gap: clamp(0.5rem, 2vw, 1.25rem);
  flex-wrap: wrap;
  min-block-size: 64px;
  padding-inline-end: 60px;
}

.mm-07__brand {
  color: var(--mm-07-accent);
  text-decoration: none;
  font: 700 0.85rem/1 var(--mm-07-font-display);
  letter-spacing: 0.3em;
}

.mm-07__ws {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding-inline: 0.6rem;
  min-block-size: 28px;
  border: 1px solid var(--mm-07-line);
  border-radius: 4px;
  font: 500 0.74rem/1 var(--mm-07-font-display);
  color: var(--mm-07-mut);
}

.mm-07__ws-dot {
  inline-size: 7px;
  block-size: 7px;
  border-radius: 999px;
  background: var(--mm-07-accent);
}

.mm-07__nav {
  min-inline-size: 0;
}

.mm-07__list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.15rem;
  list-style: none;
  margin: 0;
  padding: 0;
  min-inline-size: 0;
}

.mm-07__item {
  position: static;
}

.mm-07__trigger,
.mm-07__plain {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 0.9rem;
  border: 0;
  background: transparent;
  color: var(--mm-07-ink);
  font: 600 0.86rem/1 var(--mm-07-font-display);
  letter-spacing: 0.02em;
  text-decoration: none;
  cursor: pointer;
}

.mm-07__item--open > .mm-07__trigger,
.mm-07__item:hover > .mm-07__trigger,
.mm-07__item:focus-within > .mm-07__trigger {
  background: var(--mm-07-accent);
  color: var(--mm-07-on-accent);
}

.mm-07__plain:hover,
.mm-07__trigger:hover {
  color: var(--mm-07-accent);
}

.mm-07__utils {
  margin-inline-start: auto;
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.mm-07__kbd {
  display: inline-flex;
  gap: 2px;
}

.mm-07 kbd {
  display: inline-grid;
  place-items: center;
  min-inline-size: 22px;
  block-size: 22px;
  border: 1px solid var(--mm-07-line);
  border-radius: 4px;
  font: 600 0.7rem/1 var(--mm-07-font-display);
  color: var(--mm-07-mut);
}

.mm-07__avatar {
  display: grid;
  place-items: center;
  inline-size: 30px;
  block-size: 30px;
  border-radius: 999px;
  background: color-mix(in oklab, var(--mm-07-accent) 26%, transparent);
  color: var(--mm-07-accent);
  font: 700 0.7rem/1 var(--mm-07-font-display);
}
/* Bridge the 10px gap between the trigger and the panel with transparent
   padding, so the pointer never crosses dead space on its way in. Without
   it, pointerleave fires on the item mid-travel and the panel closes before
   the cursor arrives — WCAG SC 1.4.13 requires hover content to be
   hoverable. background-clip keeps the padding transparent. */

.mm-07__panel {
  position: absolute;
  padding-block-start: 14px;
  margin-block-start: -14px;
  background-clip: content-box;
  inset-inline: 0;
  inset-block-start: 100%;
  z-index: 30;
  background: var(--mm-07-panel);
  border-block-end: 1px solid var(--mm-07-line);
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transform: translateY(calc(var(--mm-07-lift) * -1));
  transition: opacity 150ms ease, transform 150ms ease, visibility 0s linear 150ms;
}

.mm-07__item--open > .mm-07__panel {
  opacity: 1;
  visibility: visible;
  pointer-events: auto;
  transform: translateY(0);
  transition-delay: 0s;
}

.mm-07__panel-inner {
  inline-size: min(84rem, calc(100% - 2rem));
  margin-inline: auto;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: clamp(0.9rem, 2.5vw, 1.75rem);
  padding-block: clamp(1rem, 3vw, 1.6rem);
}

@media (min-width: 62rem) {
  .mm-07__panel-inner {
    grid-template-columns: minmax(0, 1fr) 17rem;
  }
}
/* Dividers are drawn as real borders on each card rather than by letting
   a 1px gap reveal the grid background. The bleed trick needs every track
   filled, and these panels hold 6 and 4 items, so no single column count
   fills both — auto-fit left empty cells that painted as solid grey blocks.
   With a transparent grid and per-card borders, an empty track paints
   nothing and any item count is safe. */

.mm-07__grid {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 14rem), 1fr));
  gap: 0;
  background: transparent;
  border: 1px solid var(--mm-07-line);
  border-block-end: 0;
  border-inline-end: 0;
  min-inline-size: 0;
}
/* Fill the whole cell: the anchor carries the card background, and any
   shortfall against the row height shows through as a grey band. */

.mm-07__grid a {
  block-size: 100%;
  border-inline-end: 1px solid var(--mm-07-line);
  border-block-end: 1px solid var(--mm-07-line);
  display: grid;
  grid-template-columns: 22px minmax(0, 1fr);
  grid-template-rows: auto auto;
  column-gap: 0.7rem;
  align-items: center;
  align-content: center;
  min-block-size: 60px;
  padding: 0.7rem 0.8rem;
  background: var(--mm-07-panel);
  color: var(--mm-07-ink);
  text-decoration: none;
}

.mm-07__grid svg {
  grid-row: span 2;
  inline-size: 22px;
  block-size: 22px;
  color: var(--mm-07-accent);
}

.mm-07__grid b {
  font: 600 0.9rem/1.3 system-ui, sans-serif;
  min-inline-size: 0;
}

.mm-07__grid span {
  font: 500 0.72rem/1.3 var(--mm-07-font-display);
  color: var(--mm-07-mut);
  min-inline-size: 0;
}

.mm-07__grid a:hover {
  background: color-mix(in oklab, var(--mm-07-accent) 14%, var(--mm-07-panel));
}

.mm-07__switch {
  min-inline-size: 0;
  display: grid;
  align-content: start;
  gap: 0.25rem;
  padding: 0.85rem 0.95rem;
  border: 1px solid var(--mm-07-line);
}

.mm-07__switch-head {
  margin: 0 0 0.25rem;
  font: 700 0.64rem/1 var(--mm-07-font-display);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--mm-07-mut);
}

.mm-07__switch-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1px;
}

.mm-07__switch-list a {
  display: grid;
  grid-template-columns: 26px minmax(0, 1fr) auto;
  align-items: center;
  gap: 0.6rem;
  min-block-size: 44px;
  padding-inline: 0.3rem;
  border-radius: 4px;
  color: var(--mm-07-ink);
  text-decoration: none;
  font-size: 0.87rem;
}

.mm-07__mark {
  display: grid;
  place-items: center;
  inline-size: 26px;
  block-size: 22px;
  border-radius: 3px;
  background: color-mix(in oklab, var(--mm-07-accent) 20%, transparent);
  color: var(--mm-07-accent);
  font: 700 0.64rem/1 var(--mm-07-font-display);
}

.mm-07__meta {
  font: 500 0.66rem/1 var(--mm-07-font-display);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--mm-07-mut);
}

.mm-07__switch-list a:hover {
  background: color-mix(in oklab, var(--mm-07-accent) 12%, transparent);
}

.mm-07__page {
  inline-size: min(84rem, calc(100% - 2rem));
  margin-inline: auto;
  padding-block: clamp(1.5rem, 5vw, 3rem);
}

.mm-07__canvas {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr));
  gap: 0.75rem;
}

.mm-07__col-board {
  min-inline-size: 0;
  display: grid;
  align-content: start;
  gap: 0.5rem;
  padding: 0.75rem;
  border: 1px solid var(--mm-07-line);
  background: var(--mm-07-surf);
}

.mm-07__board-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 0;
  font: 700 0.68rem/1 var(--mm-07-font-display);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--mm-07-mut);
}

.mm-07__board-head span {
  color: var(--mm-07-accent);
}

.mm-07__ticket {
  display: grid;
  gap: 2px;
  padding: 0.7rem 0.8rem;
  border: 1px solid var(--mm-07-line);
  background: var(--mm-07-panel);
}

.mm-07__ticket b {
  font: 600 0.88rem/1.3 system-ui, sans-serif;
}

.mm-07__ticket span {
  font: 500 0.72rem/1.3 var(--mm-07-font-display);
  color: var(--mm-07-mut);
}

.mm-07__ticket--done {
  border-inline-start: 2px solid var(--mm-07-accent);
}

@media (max-width: 52rem) {
  .mm-07__bar {
    flex-direction: column;
    align-items: stretch;
    padding-block: 0.6rem;
  }

  .mm-07__list {
    flex-direction: column;
  }

  .mm-07__utils {
    margin-inline-start: 0;
  }

  .mm-07__panel {
    position: static;
    opacity: 1;
    visibility: visible;
    transform: none;
    display: none;
  }

  .mm-07__item--open > .mm-07__panel {
    display: block;
  }

  .mm-07__panel-inner {
    inline-size: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .mm-07__panel {
    transition-duration: 1ms;
  }
}

@media (hover: hover) and (pointer: fine) {
  .mm-07__trigger {
    position: relative;
  }

  .mm-07__item:hover > .mm-07__trigger::after,
    .mm-07__item:focus-within > .mm-07__trigger::after {
    content: "";
    position: absolute;
    inset-inline: 0;
    inset-block-start: 100%;
    block-size: 16px;
  }
}
/* Entry signature — boards drop in from above on a short, crisp curve (keyboard-first, no bounce) */

.mm-07__col-board {
  opacity: 0;
  translate: 0 -12px;
  transition: opacity 160ms linear, translate 240ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.mm-07__item:hover > .mm-07__panel .mm-07__col-board,
.mm-07__item:focus-within > .mm-07__panel .mm-07__col-board,
.mm-07__item--open > .mm-07__panel .mm-07__col-board {
  opacity: 1;
  translate: 0 0;
}

.mm-07__col-board:nth-child(1) {
  transition-delay: 20ms;
}

.mm-07__col-board:nth-child(2) {
  transition-delay: 65ms;
}

.mm-07__col-board:nth-child(3) {
  transition-delay: 110ms;
}

.mm-07__col-board:nth-child(4) {
  transition-delay: 155ms;
}

.mm-07__col-board:nth-child(n+5) {
  transition-delay: 155ms;
}

@media (prefers-reduced-motion: reduce) {
  .mm-07__col-board {
    transition-duration: 1ms;
    transition-delay: 0s;
    animation: none;
  }

  .mm-07__col-board {
    opacity: 1;
    translate: none;
  }
}
```

## JavaScript
```js
const root = document.querySelector('.mm-07');
const nav = root.querySelector('.mm-07__nav');
const canHover = window.matchMedia('(hover: hover)');

const setOpen = (item, on) => {
  // Not every nav item owns a panel — the bar also carries plain links, and
  // pointerleave/focusout reach those through closest('.mm-07__item'). Bail
  // out rather than calling setAttribute on a missing trigger.
  const trigger = item.querySelector('.mm-07__trigger');
  if (!trigger) return;
  item.classList.toggle('mm-07__item--open', on);
  trigger.setAttribute('aria-expanded', String(on));
};
const closeAll = (except) => nav.querySelectorAll('.mm-07__item--open').forEach((i) => { if (i !== except) setOpen(i, false); });

const onClick = (e) => {
  const trigger = e.target.closest('.mm-07__trigger');
  if (!trigger) return;
  const item = trigger.closest('.mm-07__item');
  const open = item.classList.contains('mm-07__item--open');
  // On a hover device the panel is already open from pointerenter; a click on
  // the trigger must not toggle it shut. Only pointer-less devices toggle.
  if (open && canHover.matches) return;
  closeAll(item); setOpen(item, !open);
};
const onKeyDown = (e) => {
  const item = e.target.closest('.mm-07__item');
  if (!item) return;
  if (e.key === 'Escape' && item.classList.contains('mm-07__item--open')) {
    e.preventDefault();
    setOpen(item, false);
    item.querySelector('.mm-07__trigger').focus();
  }
};
const onFocusIn = (e) => {
  const item = e.target.closest('.mm-07__item');
  if (!item || !item.querySelector('.mm-07__panel')) return;
  closeAll(item); setOpen(item, true);
};
const onFocusOut = (e) => {
  const item = e.target.closest('.mm-07__item');
  if (!item) return;
  if (!e.relatedTarget || !item.contains(e.relatedTarget)) setOpen(item, false);
};
const onEnter = (e) => {
  if (!canHover.matches) return;
  const item = e.target.closest('.mm-07__item');
  if (item && item.querySelector('.mm-07__panel')) { closeAll(item); setOpen(item, true); }
};
const onLeave = (e) => {
  if (!canHover.matches) return;
  const item = e.target.closest('.mm-07__item');
  if (!item) return;
  if (item.contains(document.activeElement)) return;
  // The panel is far wider than its trigger, so moving into it fires
  // pointerleave on the item. Only close when the pointer has actually left
  // the nav — otherwise the panel shuts before the cursor reaches a link.
  if (e.relatedTarget && (item.contains(e.relatedTarget) || nav.contains(e.relatedTarget))) return;
  setOpen(item, false);
};

nav.addEventListener('click', onClick);
nav.addEventListener('keydown', onKeyDown);
nav.addEventListener('focusin', onFocusIn);
nav.addEventListener('focusout', onFocusOut);
nav.addEventListener('pointerenter', onEnter, true);
nav.addEventListener('pointerleave', onLeave, true);

root.__mmCleanup = () => {
  nav.removeEventListener('click', onClick);
  nav.removeEventListener('keydown', onKeyDown);
  nav.removeEventListener('focusin', onFocusIn);
  nav.removeEventListener('focusout', onFocusOut);
  nav.removeEventListener('pointerenter', onEnter, true);
  nav.removeEventListener('pointerleave', onLeave, true);
};
```
