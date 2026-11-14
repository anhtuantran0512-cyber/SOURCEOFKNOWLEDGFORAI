---
source: "codefronts"
url: "https://codefronts.com/snippets/css-empty-states/empty-notification-center-flyout/"
title: "Empty Notification Center Flyout"
section: "snippets"
category: "css-empty-states"
category_name: "CSS Empty States"
description: "A navbar bell that opens a real notification flyout with zero JavaScript: a single checkbox drives the open state and :has() lifts it to the panel, the bell,…"
has_js: "false"
---

Here's a working CSS Empty State from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Empty Notification Center Flyout
Source: https://codefronts.com/snippets/css-empty-states/empty-notification-center-flyout/

A navbar bell that opens a real notification flyout with zero JavaScript: a single checkbox drives the open state and :has() lifts it to the panel, the bell, and the page behind it, which blurs and dims as the flyout takes focus. Three radio-driven tabs each carry their own empty state.
## HTML
```html
<div class="est-10">
  <header class="est-10__bar">
    <span class="est-10__brand">Ledgerline</span>
    <nav class="est-10__nav">
      <a href="#est-10">Accounts</a>
      <a href="#est-10">Transfers</a>
      <a href="#est-10">Reports</a>
    </nav>
    <div class="est-10__right">
      <input class="est-10__sr" type="checkbox" id="est-10-open" checked>
      <label class="est-10__bell" for="est-10-open" title="Notifications">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6.5 16.5V11a5.5 5.5 0 0 1 11 0v5.5l1.5 2H5z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M10 19.5a2 2 0 0 0 4 0" stroke="currentColor" stroke-width="1.6"/></svg>
        <span class="est-10__vh">Notifications</span>
      </label>
      <span class="est-10__ava" aria-hidden="true">JS</span>

      <div class="est-10__flyout" role="dialog" aria-label="Notifications">
        <div class="est-10__fhead">
          <span class="est-10__ftitle">Notifications</span>
          <label class="est-10__fclose" for="est-10-open" aria-label="Close">
            <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M7 7l10 10M17 7 7 17" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
          </label>
        </div>

        <div class="est-10__ftabs">
          <input class="est-10__sr" type="radio" name="est-10-tab" id="est-10-a" checked>
          <input class="est-10__sr" type="radio" name="est-10-tab" id="est-10-b">
          <input class="est-10__sr" type="radio" name="est-10-tab" id="est-10-c">
          <div class="est-10__ftabrow">
            <label class="est-10__ftab" for="est-10-a">All</label>
            <label class="est-10__ftab" for="est-10-b">Approvals</label>
            <label class="est-10__ftab" for="est-10-c">Mentions</label>
          </div>

          <div class="est-10__fpanel" data-p="a">
            <span class="est-10__glyph" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M5 12.5 9.5 17 19 7.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
            <p class="est-10__eh">You are up to date</p>
            <p class="est-10__ep">Everything since Monday has been read. New activity lands here as it happens.</p>
          </div>
          <div class="est-10__fpanel" data-p="b">
            <span class="est-10__glyph" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 4.5 19 8v5c0 3.6-2.9 5.9-7 6.9-4.1-1-7-3.3-7-6.9V8z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
            </span>
            <p class="est-10__eh">No approvals waiting</p>
            <p class="est-10__ep">Transfers above your limit appear here for a second signature.</p>
          </div>
          <div class="est-10__fpanel" data-p="c">
            <span class="est-10__glyph" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M15 8.5a3.5 3.5 0 1 0-3 5.3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/><circle cx="12" cy="12" r="8" stroke="currentColor" stroke-width="1.6"/></svg>
            </span>
            <p class="est-10__eh">Nobody has tagged you</p>
            <p class="est-10__ep">Mentions in comments and reconciliation notes show up here.</p>
          </div>
        </div>

        <div class="est-10__ffoot">
          <a href="#est-10">Notification settings</a>
        </div>
      </div>
    </div>
  </header>

  <main class="est-10__page" aria-hidden="true">
    <div class="est-10__pcol">
      <div class="est-10__block" data-b="head"></div>
      <div class="est-10__row"><span></span><span></span><span></span></div>
      <div class="est-10__row"><span></span><span></span><span></span></div>
      <div class="est-10__row"><span></span><span></span><span></span></div>
      <div class="est-10__row"><span></span><span></span><span></span></div>
    </div>
    <div class="est-10__pcol">
      <div class="est-10__block" data-b="chart"></div>
      <div class="est-10__block" data-b="note"></div>
    </div>
  </main>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600&display=swap');

.est-10 {
  --bg: #f5f6f8;
  --surface: #ffffff;
  --sunk: #edeff2;
  --line: #e3e6ea;
  --line-2: #d2d6dc;
  --ink: #14161a;
  --muted: #5b606a;
  --faint: #8a8f99;
  --accent: #37507a;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: auto minmax(0,1fr);
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  color-scheme: light;
  font-synthesis: none;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,sans-serif;
  -webkit-font-smoothing: antialiased;
}

.est-10 *,
.est-10 *::before,
.est-10 *::after {
  box-sizing: border-box;
}

.est-10 [hidden] {
  display: none !important;
}

.est-10__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.est-10__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  margin: 0;
  pointer-events: none;
}

@supports (color: oklch(0.7 0.1 300)) {
  .est-10 {
    --bg: oklch(0.972 0.004 255);
    --surface: oklch(1 0 0);
    --sunk: oklch(0.952 0.005 255);
    --line: oklch(0.918 0.006 255);
    --line-2: oklch(0.865 0.008 255);
    --ink: oklch(0.175 0.009 260);
    --muted: oklch(0.465 0.012 260);
    --faint: oklch(0.625 0.013 260);
    --accent: oklch(0.4 0.075 262);
  }
}

.est-10__bar {
  position: relative;
  z-index: 5;
  display: flex;
  align-items: center;
  gap: 1.5rem;
  padding: .85rem clamp(1rem,3vw,2.25rem);
  border-block-end: 1px solid var(--line);
  background: var(--surface);
}

.est-10__brand {
  font-size: .95rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.est-10__nav {
  display: flex;
  gap: 1.15rem;
}

.est-10__nav a {
  font-size: .86rem;
  color: var(--muted);
  text-decoration: none;
  transition: color .16s;
}

.est-10__nav a:hover {
  color: var(--ink);
}

.est-10__right {
  position: relative;
  margin-inline-start: auto;
  display: flex;
  align-items: center;
  gap: .6rem;
}

.est-10__bell {
  position: relative;
  inline-size: 2.4rem;
  block-size: 2.4rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  color: var(--ink);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 10px;
  transition: background .16s, border-color .16s;
}

.est-10__bell svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.est-10__bell:hover {
  background: var(--sunk);
}

.est-10__right:has(#est-10-open:checked) .est-10__bell {
  background: var(--sunk);
  border-color: var(--line-2);
}

#est-10-open:focus-visible + .est-10__bell {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.est-10__ava {
  inline-size: 2rem;
  block-size: 2rem;
  display: grid;
  place-items: center;
  border-radius: 50%;
  font-size: .7rem;
  font-weight: 600;
  color: #fff;
  background: var(--accent);
}

.est-10__flyout {
  position: absolute;
  inset-block-start: calc(100% + .65rem);
  inset-inline-end: 0;
  inline-size: min(22.5rem,calc(100vw - 2rem));
  display: grid;
  opacity: 0;
  translate: 0 -.4rem;
  scale: .985;
  pointer-events: none;
  transform-origin: 100% 0;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 16px;
  box-shadow: 0 1px 2px rgba(18,20,24,.05), 0 30px 60px -34px rgba(18,20,24,.35);
  transition: opacity .2s ease, translate .22s cubic-bezier(.2,.7,.3,1), scale .22s cubic-bezier(.2,.7,.3,1);
}

.est-10__flyout::before {
  content: '';
  position: absolute;
  inset-block-start: -.36rem;
  inset-inline-end: 1.1rem;
  inline-size: .7rem;
  block-size: .7rem;
  rotate: 45deg;
  background: var(--surface);
  border-inline-start: 1px solid var(--line);
  border-block-start: 1px solid var(--line);
  border-start-start-radius: 3px;
}

.est-10__right:has(#est-10-open:checked) .est-10__flyout {
  opacity: 1;
  translate: 0 0;
  scale: 1;
  pointer-events: auto;
}

.est-10__fhead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: .85rem 1rem;
  border-block-end: 1px solid var(--line);
}

.est-10__ftitle {
  font-size: .9rem;
  font-weight: 600;
  letter-spacing: -.015em;
}

.est-10__fclose {
  inline-size: 1.75rem;
  block-size: 1.75rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  color: var(--faint);
  border-radius: 7px;
  transition: color .16s, background .16s;
}

.est-10__fclose svg {
  inline-size: .85rem;
  block-size: .85rem;
}

.est-10__fclose:hover {
  color: var(--ink);
  background: var(--sunk);
}

.est-10__ftabs {
  display: grid;
}

.est-10__ftabrow {
  display: flex;
  gap: .15rem;
  padding: .6rem .7rem 0;
}

.est-10__ftab {
  flex: 1 1 auto;
  padding: .4rem .5rem;
  text-align: center;
  cursor: pointer;
  font-size: .79rem;
  font-weight: 500;
  color: var(--muted);
  border-radius: 8px;
  transition: color .16s, background .16s;
}

.est-10__ftab:hover {
  color: var(--ink);
  background: var(--sunk);
}

#est-10-a:focus-visible ~ .est-10__ftabrow .est-10__ftab[for="est-10-a"],
#est-10-b:focus-visible ~ .est-10__ftabrow .est-10__ftab[for="est-10-b"],
#est-10-c:focus-visible ~ .est-10__ftabrow .est-10__ftab[for="est-10-c"] {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.est-10__ftabs:has(#est-10-a:checked) .est-10__ftab[for="est-10-a"],
.est-10__ftabs:has(#est-10-b:checked) .est-10__ftab[for="est-10-b"],
.est-10__ftabs:has(#est-10-c:checked) .est-10__ftab[for="est-10-c"] {
  color: var(--ink);
  background: var(--sunk);
  box-shadow: inset 0 0 0 1px var(--line);
}

.est-10__fpanel {
  display: none;
  justify-items: center;
  text-align: center;
  gap: .35rem;
  padding: 2rem 1.35rem 1.75rem;
}

.est-10__ftabs:has(#est-10-a:checked) [data-p="a"],
.est-10__ftabs:has(#est-10-b:checked) [data-p="b"],
.est-10__ftabs:has(#est-10-c:checked) [data-p="c"] {
  display: grid;
  animation: est-10-in .35s cubic-bezier(.2,.7,.3,1) both;
}

@keyframes est-10-in {
  from {
    opacity: 0;
    translate: 0 5px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.est-10__glyph {
  position: relative;
  inline-size: 3rem;
  block-size: 3rem;
  display: grid;
  place-items: center;
  margin-block-end: .5rem;
  color: var(--accent);
  background: color-mix(in oklab, var(--accent) 8%, var(--surface));
  border-radius: 50%;
  box-shadow: 0 0 0 1px color-mix(in oklab, var(--accent) 18%, transparent);
}

.est-10__glyph::after {
  content: '';
  position: absolute;
  inset: -.45rem;
  border-radius: 50%;
  border: 1px solid color-mix(in oklab, var(--accent) 15%, transparent);
  animation: est-10-breathe 5s ease-in-out infinite;
}

@keyframes est-10-breathe {
  0%,
    100% {
    opacity: .9;
    scale: 1;
  }

  50% {
    opacity: .35;
    scale: 1.05;
  }
}

.est-10__glyph svg {
  inline-size: 1.3rem;
  block-size: 1.3rem;
}

.est-10__eh {
  margin: 0;
  font-size: .95rem;
  font-weight: 600;
  letter-spacing: -.018em;
}

.est-10__ep {
  margin: 0;
  max-inline-size: 30ch;
  font-size: .82rem;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.est-10__ffoot {
  padding: .75rem 1rem;
  border-block-start: 1px solid var(--line);
  background: var(--sunk);
  border-end-start-radius: 16px;
  border-end-end-radius: 16px;
}

.est-10__ffoot a {
  font-size: .8rem;
  color: var(--accent);
  text-decoration: none;
}

.est-10__ffoot a:hover {
  text-decoration: underline;
  text-underline-offset: 3px;
}

.est-10__page {
  min-inline-size: 0;
  padding: clamp(1.25rem,3.5vw,2.5rem) clamp(1rem,3vw,2.25rem);
  display: grid;
  gap: 1.25rem;
  grid-template-columns: repeat(auto-fit,minmax(min(18rem,100%),1fr));
  align-content: start;
  filter: blur(0);
  transition: filter .3s ease, opacity .3s ease;
}

.est-10:has(#est-10-open:checked) .est-10__page {
  filter: blur(1.5px);
  opacity: .65;
}

.est-10__pcol {
  display: grid;
  gap: .75rem;
  align-content: start;
}

.est-10__block {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 14px;
}

.est-10__block[data-b="head"] {
  block-size: 3.25rem;
}

.est-10__block[data-b="chart"] {
  block-size: 12rem;
  background: linear-gradient(180deg, transparent 55%, color-mix(in oklab, var(--accent) 7%, transparent)), repeating-linear-gradient(180deg, var(--line) 0 1px, transparent 1px 3rem), var(--surface);
}

.est-10__block[data-b="note"] {
  block-size: 6rem;
}

.est-10__row {
  display: grid;
  grid-template-columns: minmax(0,2fr) minmax(0,1fr) minmax(0,1fr);
  gap: .75rem;
  padding: .9rem 1rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 12px;
}

.est-10__row span {
  block-size: .6rem;
  border-radius: 3px;
  background: var(--sunk);
}

.est-10__row span:first-child {
  background: color-mix(in oklab, var(--line-2) 75%, transparent);
}

@media (prefers-reduced-motion: reduce) {
  .est-10 *,
    .est-10 *::before,
    .est-10 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .est-10__flyout,
    .est-10__bell,
    .est-10__glyph {
    border-color: CanvasText;
  }
}
```
