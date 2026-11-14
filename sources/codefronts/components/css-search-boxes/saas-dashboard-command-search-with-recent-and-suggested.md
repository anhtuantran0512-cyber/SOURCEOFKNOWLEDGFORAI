---
source: "codefronts"
url: "https://codefronts.com/components/css-search-boxes/saas-dashboard-command-search-with-recent-and-suggested/"
title: "SaaS Dashboard Command Search with Recent and Suggested"
section: "components"
category: "css-search-boxes"
category_name: "CSS Search Bars"
description: "The persistent dashboard topbar search: focus it and a rich panel opens with Recent (clock icons), Suggested (sparkle icons) and Quick actions with real ⌘…"
has_js: "true"
---

Here's a working CSS Search Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SaaS Dashboard Command Search with Recent and Suggested
Source: https://codefronts.com/components/css-search-boxes/saas-dashboard-command-search-with-recent-and-suggested/

The persistent dashboard topbar search: focus it and a rich panel opens with Recent (clock icons), Suggested (sparkle icons) and Quick actions with real ⌘ shortcuts. Dark-first, arrow-key navigable, and mounted in a mock admin shell so you can see it in context.
## HTML
```html
<div class="sb-05">
  <button class="sb-05__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="sb-05__moon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2"/></svg>
    <svg class="sb-05__sun" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4"/><path d="M12 3.4v2M12 18.6v2M3.4 12h2M18.6 12h2M6 6l1.4 1.4M16.6 16.6 18 18M18 6l-1.4 1.4M7.4 16.6 6 18"/></svg>
  </button>
  <div class="sb-05__stage">
    <div class="sb-05__shell">
      <aside class="sb-05__rail" aria-hidden="true">
        <span class="sb-05__mark"></span>
        <span class="sb-05__railitem sb-05__railitem--on"></span>
        <span class="sb-05__railitem"></span>
        <span class="sb-05__railitem"></span>
        <span class="sb-05__railitem"></span>
      </aside>

      <div class="sb-05__main">
        <header class="sb-05__topbar">
          <div class="sb-05__combo" role="search">
            <div class="sb-05__field">
              <svg class="sb-05__ico" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.7"/><path d="m16 16 4.2 4.2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
              <label class="sb-05__vh" for="sb-05-input">Search customers, invoices and actions</label>
              <input class="sb-05__input" id="sb-05-input" type="search" role="combobox" placeholder="Search or run a command&hellip;" autocomplete="off" spellcheck="false" aria-controls="sb-05-list" aria-expanded="false" aria-activedescendant="sb-05-r1">
              <kbd class="sb-05__kbd">&#8984;K</kbd>
            </div>

            <div class="sb-05__panel">
              <ul class="sb-05__list" id="sb-05-list" role="listbox" aria-label="Search results and actions">
                <li class="sb-05__sect" role="presentation">
                  <p class="sb-05__sect-h" id="sb-05-h1">Recent</p>
                  <ul class="sb-05__sub" role="group" aria-labelledby="sb-05-h1">
                    <li class="sb-05__row" role="option" id="sb-05-r1" aria-selected="true">
                      <span class="sb-05__glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="12" cy="12" r="7.6" stroke="currentColor" stroke-width="1.6"/><path d="M12 8.4V12l2.6 1.6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></span>
                      <span class="sb-05__txt">Q3 revenue<small>Reports</small></span>
                      <time class="sb-05__meta" datetime="2027-02-11T09:20">9:20 AM</time>
                    </li>
                    <li class="sb-05__row" role="option" id="sb-05-r2" aria-selected="false">
                      <span class="sb-05__glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="12" cy="12" r="7.6" stroke="currentColor" stroke-width="1.6"/><path d="M12 8.4V12l2.6 1.6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></span>
                      <span class="sb-05__txt">invoice template<small>Documents</small></span>
                      <time class="sb-05__meta" datetime="2027-02-10T16:04">Yesterday</time>
                    </li>
                    <li class="sb-05__row" role="option" id="sb-05-r3" aria-selected="false">
                      <span class="sb-05__glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="12" cy="12" r="7.6" stroke="currentColor" stroke-width="1.6"/><path d="M12 8.4V12l2.6 1.6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></span>
                      <span class="sb-05__txt">Sam Rivera<small>Customer &middot; #40219</small></span>
                      <time class="sb-05__meta" datetime="2027-02-09T11:12">Mon</time>
                    </li>
                  </ul>
                </li>

                <li class="sb-05__sect" role="presentation">
                  <p class="sb-05__sect-h" id="sb-05-h2">Suggested</p>
                  <ul class="sb-05__sub" role="group" aria-labelledby="sb-05-h2">
                    <li class="sb-05__row" role="option" id="sb-05-r4" aria-selected="false">
                      <span class="sb-05__glyph sb-05__glyph--ai" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 3.5l1.7 4.6 4.6 1.7-4.6 1.7L12 16.1l-1.7-4.6L5.7 9.8l4.6-1.7z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><path d="M18 16.5l.8 2.1 2.1.8-2.1.8-.8 2.1-.8-2.1-2.1-.8 2.1-.8z" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round"/></svg></span>
                      <span class="sb-05__txt">Churn risk accounts this week<small>Generated view</small></span>
                      <span class="sb-05__pill">New</span>
                    </li>
                    <li class="sb-05__row" role="option" id="sb-05-r5" aria-selected="false">
                      <span class="sb-05__glyph sb-05__glyph--ai" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 3.5l1.7 4.6 4.6 1.7-4.6 1.7L12 16.1l-1.7-4.6L5.7 9.8l4.6-1.7z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg></span>
                      <span class="sb-05__txt">Failed payments &gt; $500<small>Saved filter</small></span>
                    </li>
                    <li class="sb-05__row" role="option" id="sb-05-r6" aria-selected="false">
                      <span class="sb-05__glyph sb-05__glyph--ai" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 3.5l1.7 4.6 4.6 1.7-4.6 1.7L12 16.1l-1.7-4.6L5.7 9.8l4.6-1.7z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg></span>
                      <span class="sb-05__txt">Compare MRR to last quarter<small>Insight</small></span>
                    </li>
                  </ul>
                </li>

                <li class="sb-05__sect" role="presentation">
                  <p class="sb-05__sect-h" id="sb-05-h3">Quick actions</p>
                  <ul class="sb-05__sub" role="group" aria-labelledby="sb-05-h3">
                    <li class="sb-05__row" role="option" id="sb-05-r7" aria-selected="false">
                      <span class="sb-05__glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></span>
                      <span class="sb-05__txt">New invoice</span>
                      <kbd class="sb-05__kbd">&#8984;&#8679;N</kbd>
                    </li>
                    <li class="sb-05__row" role="option" id="sb-05-r8" aria-selected="false">
                      <span class="sb-05__glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="12" cy="12" r="2.7" stroke="currentColor" stroke-width="1.6"/><path d="M12 4.2v2.4m0 10.8v2.4M4.2 12h2.4m10.8 0h2.4M6.7 6.7l1.7 1.7m7.2 7.2 1.7 1.7m0-10.6-1.7 1.7M8.4 15.6l-1.7 1.7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></span>
                      <span class="sb-05__txt">Settings</span>
                      <kbd class="sb-05__kbd">&#8984;,</kbd>
                    </li>
                    <li class="sb-05__row" role="option" id="sb-05-r9" aria-selected="false">
                      <span class="sb-05__glyph" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="12" cy="12" r="7.8" stroke="currentColor" stroke-width="1.6"/><path d="M9.9 9.6a2.2 2.2 0 1 1 3.2 2c-.7.4-1.1.9-1.1 1.7" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="12" cy="16.4" r=".9" fill="currentColor"/></svg></span>
                      <span class="sb-05__txt">Help &amp; docs</span>
                      <kbd class="sb-05__kbd">&#8984;/</kbd>
                    </li>
                  </ul>
                </li>
              </ul>
            </div>
          </div>

          <div class="sb-05__topright" aria-hidden="true">
            <span class="sb-05__chip"></span>
            <span class="sb-05__avatar">AC</span>
          </div>
        </header>

        <div class="sb-05__body" aria-hidden="true">
          <div class="sb-05__cards">
            <span class="sb-05__card"></span>
            <span class="sb-05__card"></span>
            <span class="sb-05__card"></span>
          </div>
          <span class="sb-05__chart"></span>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.sb-05 {
  --bg: #07080d;
  --shell: #0d0f16;
  --panel: #12141d;
  --panel-2: #181b26;
  --ink: #f2f3f8;
  --muted: #8b90a4;
  --line: #222634;
  --acc: #7c6cff;
  --acc-2: #2dd4bf;
  --wash: rgba(124,108,255,.14);
  --ring: #9c90ff;
  --shadow: rgba(0,0,0,.72);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  box-sizing: border-box;
  font-family: system-ui,-apple-system,"Segoe UI",sans-serif;
  color: var(--ink);
  background: radial-gradient(52rem 32rem at 88% -10%, rgba(124,108,255,.18), transparent 68%), radial-gradient(40rem 26rem at -6% 104%, rgba(45,212,191,.12), transparent 68%), var(--bg);
  -webkit-font-smoothing: antialiased;
}

.sb-05 *,
.sb-05 *::before,
.sb-05 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% .1 280)) {
  .sb-05 {
    --shell: oklch(16% .015 280);
    --panel: oklch(19% .018 280);
    --panel-2: oklch(24% .02 280);
    --ink: oklch(97% .005 280);
    --muted: oklch(68% .02 280);
    --line: oklch(28% .018 280);
    --acc: oklch(68% .18 292);
    --acc-2: oklch(78% .13 180);
    --wash: color-mix(in oklab, oklch(68% .18 292) 16%, transparent);
  }
}

.sb-05__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
}

.sb-05__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.sb-05__shell {
  display: flex;
  inline-size: min(62rem,100%);
  block-size: min(32rem,82svh);
  overflow: hidden;
  border: 1px solid var(--line);
  border-radius: 20px;
  background: var(--shell);
  box-shadow: 0 40px 80px -34px var(--shadow), 0 0 0 1px rgba(255,255,255,.03) inset;
}

.sb-05__rail {
  flex: none;
  inline-size: 60px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: .7rem;
  padding: 1rem .5rem;
  border-inline-end: 1px solid var(--line);
  background: rgba(255,255,255,.015);
}

.sb-05__mark {
  inline-size: 26px;
  block-size: 26px;
  border-radius: 8px;
  background: conic-gradient(from 210deg,#7c6cff,#c084fc 45%,#2dd4bf 80%,#7c6cff);
  margin-block-end: .6rem;
}

.sb-05__railitem {
  inline-size: 24px;
  block-size: 24px;
  border-radius: 7px;
  background: var(--panel-2);
}

.sb-05__railitem--on {
  background: var(--wash);
  box-shadow: inset 0 0 0 1px color-mix(in oklab, var(--acc) 40%, transparent);
}

.sb-05__main {
  flex: 1;
  min-inline-size: 0;
  display: flex;
  flex-direction: column;
}

.sb-05__topbar {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: .85rem 1rem;
  border-block-end: 1px solid var(--line);
  background: rgba(255,255,255,.012);
}

.sb-05__combo {
  position: relative;
  flex: 1;
  min-inline-size: 0;
  max-inline-size: 34rem;
}

.sb-05__field {
  display: flex;
  align-items: center;
  gap: .65rem;
  min-block-size: 44px;
  padding-inline: .85rem .5rem;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: var(--panel);
  transition: border-color .2s, box-shadow .2s, background .2s;
}

.sb-05__combo:focus-within .sb-05__field {
  border-color: color-mix(in oklab, var(--acc) 55%, var(--line));
  box-shadow: 0 0 0 4px var(--wash);
  background: var(--panel-2);
}

.sb-05__ico {
  inline-size: 18px;
  block-size: 18px;
  flex: none;
  color: var(--muted);
  transition: color .2s;
}

.sb-05__combo:focus-within .sb-05__ico {
  color: var(--acc);
}

.sb-05__input {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: none;
  color: var(--ink);
  font: 400 .93rem/1 inherit;
}

.sb-05__input::placeholder {
  color: var(--muted);
}

.sb-05__input:focus {
  outline: none;
}

.sb-05__input::-webkit-search-cancel-button {
  -webkit-appearance: none;
  appearance: none;
}

.sb-05__kbd {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-inline-size: 1.7rem;
  block-size: 1.5rem;
  padding-inline: .38rem;
  border: 1px solid var(--line);
  border-radius: 6px;
  background: var(--panel-2);
  color: var(--muted);
  font: 500 .7rem/1 ui-monospace,"SF Mono",Menlo,monospace;
  font-variant-numeric: tabular-nums;
}
/* panel */

.sb-05__panel {
  position: absolute;
  inset-inline: 0;
  inset-block-start: calc(100% + .45rem);
  z-index: 8;
  max-block-size: min(24rem,60svh);
  overflow: auto;
  overscroll-behavior: contain;
  padding: .4rem;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: var(--panel);
  box-shadow: 0 30px 60px -22px var(--shadow), 0 0 0 1px rgba(255,255,255,.04) inset;
  opacity: 0;
  translate: 0 -8px;
  scale: .99;
  visibility: hidden;
  transform-origin: top center;
  transition: opacity .2s cubic-bezier(.2,.9,.25,1), translate .2s cubic-bezier(.2,.9,.25,1), scale .2s, visibility .2s;
}

.sb-05__combo:focus-within .sb-05__panel {
  opacity: 1;
  translate: 0 0;
  scale: 1;
  visibility: visible;
}

.sb-05__list,
.sb-05__sub {
  list-style: none;
  margin: 0;
  padding: 0;
}

.sb-05__sect-h {
  position: sticky;
  inset-block-start: 0;
  z-index: 1;
  margin: 0;
  padding: .55rem .65rem .3rem;
  background: var(--panel);
  color: var(--muted);
  font: 600 .67rem/1 inherit;
  letter-spacing: .09em;
  text-transform: uppercase;
}

.sb-05__sect:not(:has(.sb-05__row:not([hidden]))) {
  display: none;
}

.sb-05__row {
  display: flex;
  align-items: center;
  gap: .7rem;
  min-block-size: 44px;
  padding: .4rem .65rem;
  border-radius: 10px;
  cursor: pointer;
  scroll-margin: 2rem;
  transition: background .14s;
}

.sb-05__row:hover {
  background: rgba(255,255,255,.04);
}

.sb-05__row[aria-selected="true"] {
  background: var(--wash);
  box-shadow: inset 0 0 0 1px color-mix(in oklab, var(--acc) 32%, transparent);
}

.sb-05__glyph {
  display: grid;
  place-items: center;
  inline-size: 28px;
  block-size: 28px;
  flex: none;
  border-radius: 8px;
  background: var(--panel-2);
  color: var(--muted);
}

.sb-05__glyph svg {
  inline-size: 16px;
  block-size: 16px;
}

.sb-05__glyph--ai {
  color: var(--acc-2);
  background: color-mix(in oklab, var(--acc-2) 14%, var(--panel-2));
}

.sb-05__txt {
  display: flex;
  flex-direction: column;
  gap: .1rem;
  flex: 1;
  min-inline-size: 0;
  font: 500 .89rem/1.25 inherit;
}

.sb-05__txt small {
  color: var(--muted);
  font: 400 .74rem/1.3 inherit;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.sb-05__meta {
  color: var(--muted);
  font: 400 .74rem/1 inherit;
  font-variant-numeric: tabular-nums;
  flex: none;
}

.sb-05__pill {
  flex: none;
  padding: .2rem .45rem;
  border-radius: 999px;
  background: color-mix(in oklab, var(--acc-2) 20%, transparent);
  color: var(--acc-2);
  font: 600 .66rem/1 inherit;
  letter-spacing: .04em;
  text-transform: uppercase;
}
/* shell chrome */

.sb-05__topright {
  display: flex;
  align-items: center;
  gap: .6rem;
  flex: none;
}

.sb-05__chip {
  inline-size: 64px;
  block-size: 26px;
  border-radius: 8px;
  background: var(--panel-2);
}

.sb-05__avatar {
  display: grid;
  place-items: center;
  inline-size: 32px;
  block-size: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg,#7c6cff,#4f46e5);
  color: #fff;
  font: 600 .72rem/1 inherit;
}

.sb-05__body {
  flex: 1;
  display: grid;
  gap: 1rem;
  grid-template-rows: auto 1fr;
  padding: 1rem;
  opacity: .55;
}

.sb-05__cards {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 1rem;
}

.sb-05__card {
  block-size: 5.5rem;
  border-radius: 12px;
  background: var(--panel);
  box-shadow: inset 0 0 0 1px var(--line);
}

.sb-05__chart {
  border-radius: 12px;
  background: linear-gradient(180deg, var(--wash), transparent 70%), var(--panel);
  box-shadow: inset 0 0 0 1px var(--line);
}

.sb-05 :focus-visible {
  outline: 2px solid var(--ring);
  outline-offset: 2px;
}
/* light fallback (this demo is dark-first) */

.sb-05[data-theme="light"] {
  --bg: #f5f6fa;
  --shell: #fff;
  --panel: #fff;
  --panel-2: #f3f4f9;
  --ink: #12141c;
  --muted: #6b7080;
  --line: #e5e7f0;
  --acc: #6455f0;
  --acc-2: #0d9488;
  --wash: rgba(100,85,240,.10);
  --ring: #6455f0;
  --shadow: rgba(20,22,40,.2);
  background: radial-gradient(52rem 32rem at 88% -10%, rgba(100,85,240,.10), transparent 68%), var(--bg);
}

.sb-05[data-theme="light"] .sb-05__row:hover {
  background: #f5f6fa;
}

@media (prefers-color-scheme: light) {
  .sb-05:not([data-theme="dark"]) {
    --bg: #f5f6fa;
    --shell: #fff;
    --panel: #fff;
    --panel-2: #f3f4f9;
    --ink: #12141c;
    --muted: #6b7080;
    --line: #e5e7f0;
    --acc: #6455f0;
    --acc-2: #0d9488;
    --wash: rgba(100,85,240,.10);
    --ring: #6455f0;
    --shadow: rgba(20,22,40,.2);
    background: radial-gradient(52rem 32rem at 88% -10%, rgba(100,85,240,.10), transparent 68%), var(--bg);
  }

  .sb-05:not([data-theme="dark"]) .sb-05__row:hover {
    background: #f5f6fa;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sb-05 *,
    .sb-05 *::before,
    .sb-05 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .sb-05__field,
    .sb-05__panel,
    .sb-05__shell {
    border: 1px solid CanvasText;
  }

  .sb-05__row[aria-selected="true"] {
    outline: 2px solid Highlight;
  }
}

.sb-05__theme {
  position: absolute;
  inset-block-start: clamp(.75rem,2vw,1.25rem);
  inset-inline-end: clamp(.75rem,2vw,1.25rem);
  z-index: 50;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  padding: 0;
  border-radius: 999px;
  border: 1px solid rgba(0,0,0,.12);
  color: currentColor;
  background: rgba(255,255,255,.72);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1), border-color .25s ease;
}

.sb-05[data-theme="dark"] .sb-05__theme {
  background: rgba(20,20,28,.72);
  border-color: rgba(255,255,255,.15);
  color: #fff;
}

@media (prefers-color-scheme: dark) {
  .sb-05:not([data-theme="light"]) .sb-05__theme {
    background: rgba(20,20,28,.72);
    border-color: rgba(255,255,255,.15);
    color: #fff;
  }
}

.sb-05__theme:hover {
  transform: translateY(-1px);
  border-color: rgba(0,0,0,.24);
}

.sb-05[data-theme="dark"] .sb-05__theme:hover,
.sb-05:not([data-theme="light"]) .sb-05__theme:hover {
  border-color: rgba(255,255,255,.3);
}

.sb-05__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.sb-05__theme svg {
  grid-area: 1/1;
  inline-size: 1.1rem;
  block-size: 1.1rem;
  fill: none;
  stroke: currentColor;
  stroke-width: 1.7;
  stroke-linecap: round;
  stroke-linejoin: round;
}

.sb-05__sun {
  display: none;
}

.sb-05__theme[aria-pressed="true"] .sb-05__sun {
  display: block;
}

.sb-05__theme[aria-pressed="true"] .sb-05__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .sb-05__theme {
    transition: none;
  }

  .sb-05__theme:hover {
    transform: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sb-05');
  if (!root) return;
  const combo = root.querySelector('.sb-05__combo');
  const input = root.querySelector('#sb-05-input');
  const rows = [...root.querySelectorAll('.sb-05__row')];

  const select = (el) => {
    if (!el) return;
    rows.forEach((r) => r.setAttribute('aria-selected', String(r === el)));
    input.setAttribute('aria-activedescendant', el.id);
    el.scrollIntoView({ block: 'nearest' });
  };
  const index = () => rows.findIndex((r) => r.getAttribute('aria-selected') === 'true');

  input.addEventListener('focus', () => input.setAttribute('aria-expanded', 'true'));
  input.addEventListener('blur', () => input.setAttribute('aria-expanded', 'false'));
  input.addEventListener('keydown', (e) => {
    const i = index();
    if (e.key === 'ArrowDown') { e.preventDefault(); select(rows[(i + 1) % rows.length]); }
    if (e.key === 'ArrowUp') { e.preventDefault(); select(rows[(i - 1 + rows.length) % rows.length]); }
    if (e.key === 'Enter') { e.preventDefault(); rows[i] && rows[i].animate([{ scale: '.985' }, { scale: '1' }], 150); }
    if (e.key === 'Escape') { input.blur(); }
  });
  rows.forEach((r) => {
    r.addEventListener('mousemove', () => select(r));
    r.addEventListener('mousedown', (e) => e.preventDefault());   /* keep focus in the field */
  });
  document.addEventListener('keydown', (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); input.focus(); input.select(); }
  });
})();
(()=>{const r=document.querySelector('.sb-05');if(!r)return;const t=r.querySelector('.sb-05__theme');if(!t)return;const dark=()=>(r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light'))==='dark';const sync=()=>{t.setAttribute('aria-pressed',String(dark()));t.setAttribute('aria-label',dark()?'Switch to light theme':'Switch to dark theme');};t.addEventListener('click',()=>{r.dataset.theme=dark()?'light':'dark';sync();});matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{if(!r.dataset.theme)sync();});sync();})();
```
