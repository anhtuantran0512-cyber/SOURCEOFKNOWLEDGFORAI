---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/header-with-notification-bell-and-user-menu/"
title: "Header with Notification Bell and User Menu"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "The right-hand utility cluster, taken seriously: a notification bell with an unread pill that pulses once on arrival, a panel of recent notifications, and an…"
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Header with Notification Bell and User Menu
Source: https://codefronts.com/layouts/css-header-designs/header-with-notification-bell-and-user-menu/

The right-hand utility cluster, taken seriously: a notification bell with an unread pill that pulses once on arrival, a panel of recent notifications, and an avatar menu with profile, preferences and sign out. Both panels open on hover and on :focus-within, so the whole cluster is operable from the keyboard without a single line of script.
## HTML
```html
<div class="hd-10">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@500;700&display=swap">
  <a class="hd-10__skip" href="#hd-10-main">Skip to content</a>

  <header class="hd-10__bar">
    <a class="hd-10__brand" href="#hd-10-main">
      <svg class="hd-10__mark" viewBox="0 0 26 26" fill="none" aria-hidden="true" focusable="false">
        <rect x="3.5" y="3.5" width="19" height="19" rx="6" stroke="currentColor" stroke-width="1.8"/>
        <path d="M8.5 16.5v-7l4.5 4 4.5-4v7" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <span class="hd-10__word">Marlow</span>
    </a>

    <nav class="hd-10__nav" aria-label="Main">
      <ul>
        <li><a href="#hd-10-main" aria-current="page">Inbox</a></li>
        <li><a href="#hd-10-main">Threads</a></li>
        <li><a href="#hd-10-main">Directory</a></li>
        <li><a href="#hd-10-main">Reports</a></li>
      </ul>
    </nav>

    <div class="hd-10__cluster">
      <div class="hd-10__pod">
        <button class="hd-10__bell" type="button" aria-haspopup="menu" aria-label="Notifications, 3 unread">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6.4 10.6a5.6 5.6 0 0 1 11.2 0c0 3.1.7 4.5 1.5 5.4.4.5.1 1.3-.6 1.3H5.5c-.7 0-1-.8-.6-1.3.8-.9 1.5-2.3 1.5-5.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M9.9 19.6a2.3 2.3 0 0 0 4.2 0" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
          <span class="hd-10__badge" aria-hidden="true">3</span>
        </button>
        <div class="hd-10__panel hd-10__panel--notes" role="menu" aria-label="Notifications">
          <p class="hd-10__panel-h">Notifications <span>3 unread</span></p>
          <a class="hd-10__note hd-10__note--new" role="menuitem" href="#hd-10-main">
            <span class="hd-10__dot" aria-hidden="true"></span>
            <span class="hd-10__note-t"><strong>Priya Sharma</strong> requested review on <em>Billing rewrite</em><span class="hd-10__vh">Unread</span></span>
            <time>4m</time>
          </a>
          <a class="hd-10__note hd-10__note--new" role="menuitem" href="#hd-10-main">
            <span class="hd-10__dot" aria-hidden="true"></span>
            <span class="hd-10__note-t"><strong>Deploy 4821</strong> finished in 2m 14s on eu-west<span class="hd-10__vh">Unread</span></span>
            <time>26m</time>
          </a>
          <a class="hd-10__note hd-10__note--new" role="menuitem" href="#hd-10-main">
            <span class="hd-10__dot" aria-hidden="true"></span>
            <span class="hd-10__note-t"><strong>Jordan Lee</strong> mentioned you in <em>Q3 retro</em><span class="hd-10__vh">Unread</span></span>
            <time>1h</time>
          </a>
          <a class="hd-10__note" role="menuitem" href="#hd-10-main">
            <span class="hd-10__note-t"><strong>Sam Rivera</strong> added 2 members to Support</span>
            <time>Yesterday</time>
          </a>
          <a class="hd-10__note" role="menuitem" href="#hd-10-main">
            <span class="hd-10__note-t">Weekly digest for <em>Northwind</em> is ready</span>
            <time>Mon</time>
          </a>
          <a class="hd-10__panel-f" role="menuitem" href="#hd-10-main">Open notification centre</a>
        </div>
      </div>

      <input class="hd-10__sr" type="checkbox" id="hd-10-light">
      <label class="hd-10__theme" for="hd-10-light">
        <svg class="hd-10__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <svg class="hd-10__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <span class="hd-10__vh">Switch light or dark theme</span>
      </label>

      <div class="hd-10__pod">
        <button class="hd-10__user" type="button" aria-haspopup="menu">
          <span class="hd-10__av" aria-hidden="true">AC</span>
          <span class="hd-10__user-t">
            <span class="hd-10__user-n">Alex Chen</span>
            <span class="hd-10__user-r">Support lead</span>
          </span>
          <svg class="hd-10__chev" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M8 10.5 12 14.5l4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        <div class="hd-10__panel hd-10__panel--user" role="menu" aria-label="Account">
          <a class="hd-10__row" role="menuitem" href="#hd-10-main">Profile</a>
          <a class="hd-10__row" role="menuitem" href="#hd-10-main">Preferences <kbd>,</kbd></a>
          <a class="hd-10__row" role="menuitem" href="#hd-10-main">Notification rules</a>
          <a class="hd-10__row" role="menuitem" href="#hd-10-main">Keyboard shortcuts</a>
          <a class="hd-10__row hd-10__row--out" role="menuitem" href="#hd-10-main">Sign out</a>
        </div>
      </div>
    </div>
  </header>

  <main class="hd-10__main" id="hd-10-main">
    <h1>Inbox</h1>
    <p class="hd-10__lead">Open the bell or the avatar with a click, or tab into either and the panel opens on focus. The unread pill pulses twice on arrival and then leaves you alone.</p>

    <ul class="hd-10__threads">
      <li><span class="hd-10__t-av" aria-hidden="true">PS</span><span class="hd-10__t-t"><strong>Priya Sharma</strong> &mdash; Can we ship the billing copy before Thursday?</span><time>4m</time></li>
      <li><span class="hd-10__t-av" aria-hidden="true">JL</span><span class="hd-10__t-t"><strong>Jordan Lee</strong> &mdash; Retro notes are in, two action items for you</span><time>1h</time></li>
      <li><span class="hd-10__t-av" aria-hidden="true">SR</span><span class="hd-10__t-t"><strong>Sam Rivera</strong> &mdash; Support rota for September</span><time>3h</time></li>
      <li><span class="hd-10__t-av" aria-hidden="true">NW</span><span class="hd-10__t-t"><strong>Northwind alerts</strong> &mdash; Error budget at 96%, no action needed</span><time>Yesterday</time></li>
    </ul>
    <div class="hd-10__filler" aria-hidden="true"></div>
  </main>
</div>
```
## CSS
```css
.hd-10 {
  --bg: #181513;
  --panel: #221e1b;
  --panel2: #2c2724;
  --ink: #f6f1ec;
  --muted: #a99e95;
  --line: rgba(246,241,236,.12);
  --line2: rgba(246,241,236,.2);
  --accent: #ec4899;
  --accent-ink: #2a0716;
  --accent-soft: rgba(236,72,153,.16);
  --accent-glow: rgba(236,72,153,.55);
  --panel-w: 22rem;
  --panel-h: 20rem;
  --font-display: "Roboto Slab","Rockwell",Georgia,serif;
  --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.55;
}

@supports (color: oklch(50% .1 200)) {
  .hd-10 {
    --bg: oklch(20% .012 50);
    --panel: oklch(24% .014 50);
    --panel2: oklch(28% .016 50);
    --ink: oklch(96% .01 60);
    --muted: oklch(72% .015 60);
    --accent: oklch(65% .22 350);
  }
}

.hd-10 * {
  box-sizing: border-box;
}

.hd-10 h1,
.hd-10 p,
.hd-10 ul {
  margin: 0;
  padding: 0;
}

.hd-10 ul {
  list-style: none;
}

.hd-10 [hidden] {
  display: none;
}

.hd-10 :focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: .4rem;
}

.hd-10__vh,
.hd-10__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-10__skip {
  position: absolute;
  inset-inline-start: .75rem;
  top: -3rem;
  z-index: 60;
  padding: .55rem 1rem;
  border-radius: .4rem;
  background: var(--accent);
  color: var(--accent-ink);
  font-size: .82rem;
  font-weight: 700;
  text-decoration: none;
  transition: top .18s ease;
}

.hd-10__skip:focus-visible {
  top: .75rem;
}
/* ── header: hard bottom shadow elevation ─────────────────────────── */

.hd-10__bar {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: .75rem clamp(.85rem,3vw,1.5rem);
  background: var(--panel);
  border-bottom: 1px solid var(--line);
  box-shadow: 0 4px 0 0 rgba(0,0,0,.25);
}

.hd-10__brand {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  color: var(--ink);
  text-decoration: none;
  min-inline-size: 0;
}

.hd-10__mark {
  inline-size: 1.65rem;
  block-size: 1.65rem;
  color: var(--accent);
  flex: none;
}

.hd-10__word {
  font-family: var(--font-display);
  font-size: 1.05rem;
  font-weight: 700;
  letter-spacing: -.01em;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-10__nav {
  min-inline-size: 0;
}

.hd-10__nav ul {
  display: flex;
  align-items: center;
  gap: .15rem;
}

.hd-10__nav a {
  display: block;
  padding: .45rem .7rem;
  border-radius: .45rem;
  color: var(--muted);
  text-decoration: none;
  font-size: .87rem;
  font-weight: 560;
  white-space: nowrap;
  transition: color .15s ease, background-color .15s ease;
}

.hd-10__nav a:hover {
  color: var(--ink);
  background: var(--panel2);
}

.hd-10__nav a[aria-current="page"] {
  color: var(--ink);
  background: var(--panel2);
  font-weight: 640;
}

.hd-10__cluster {
  display: flex;
  align-items: center;
  gap: .4rem;
  margin-inline-start: auto;
}

.hd-10__pod {
  position: relative;
}

.hd-10__bell,
.hd-10__theme {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 0;
  border-radius: .6rem;
  background: transparent;
  color: var(--muted);
  cursor: pointer;
  overflow: visible;
  transition: background-color .15s ease, color .15s ease;
}

.hd-10__bell svg,
.hd-10__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.hd-10__bell:hover,
.hd-10__theme:hover {
  background: var(--panel2);
  color: var(--ink);
}

.hd-10__badge {
  position: absolute;
  top: .4rem;
  inset-inline-end: .42rem;
  min-inline-size: 1.1rem;
  block-size: 1.1rem;
  display: grid;
  place-items: center;
  padding: 0 .2rem;
  border-radius: 999px;
  background: var(--accent);
  color: var(--accent-ink);
  font-size: .66rem;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
  box-shadow: 0 0 0 2px var(--panel);
  animation: hd-10-pulse 1.6s ease-out 2;
}

@keyframes hd-10-pulse {
  0%,
    100% {
    scale: 1;
    box-shadow: 0 0 0 2px var(--panel), 0 0 0 0 var(--accent-glow);
  }

  50% {
    scale: 1.16;
    box-shadow: 0 0 0 2px var(--panel), 0 0 0 .4rem transparent;
  }
}

.hd-10:has(#hd-10-light:focus-visible) .hd-10__theme {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.hd-10__user {
  display: flex;
  align-items: center;
  gap: .5rem;
  max-inline-size: 13rem;
  min-inline-size: 0;
  min-block-size: 2.75rem;
  padding: .35rem .5rem;
  border: 1px solid var(--line);
  border-radius: .6rem;
  background: var(--panel2);
  color: var(--ink);
  font: inherit;
  cursor: pointer;
  text-align: start;
  transition: border-color .15s ease;
}

.hd-10__user:hover {
  border-color: var(--line2);
}

.hd-10__av {
  display: grid;
  place-items: center;
  inline-size: 1.85rem;
  block-size: 1.85rem;
  border-radius: .45rem;
  flex: none;
  background: linear-gradient(140deg, var(--accent), #7c3aed);
  color: #fff;
  font-family: var(--font-display);
  font-size: .68rem;
  font-weight: 700;
}

.hd-10__user-t {
  display: grid;
  min-inline-size: 0;
}

.hd-10__user-n {
  font-size: .85rem;
  font-weight: 640;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-10__user-r {
  font-size: .7rem;
  color: var(--muted);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-10__chev {
  inline-size: .95rem;
  block-size: .95rem;
  color: var(--muted);
  flex: none;
  transition: rotate .18s ease;
}

.hd-10__pod:hover .hd-10__chev,
.hd-10__pod:focus-within .hd-10__chev {
  rotate: 180deg;
}

.hd-10__panel {
  position: absolute;
  inset-inline-end: 0;
  top: calc(100% + .5rem);
  z-index: 40;
  border: 1px solid var(--line2);
  border-radius: .8rem;
  background: var(--panel);
  box-shadow: 0 6px 0 0 rgba(0,0,0,.28), 0 1.5rem 3rem -1.2rem rgba(0,0,0,.6);
  visibility: hidden;
  opacity: 0;
  translate: 0 -.4rem;
  transition: opacity .16s ease, translate .16s ease, visibility .16s allow-discrete;
}

.hd-10__pod:hover > .hd-10__panel,
.hd-10__pod:focus-within > .hd-10__panel {
  visibility: visible;
  opacity: 1;
  translate: 0 0;
}

.hd-10__panel--notes {
  inline-size: min(var(--panel-w),92vw);
  max-block-size: var(--panel-h);
  overflow: auto;
  overscroll-behavior: contain;
  padding: .35rem;
}

.hd-10__panel--user {
  inline-size: 14rem;
  padding: .3rem;
}

.hd-10__panel-h {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .5rem;
  padding: .55rem .6rem;
  font-family: var(--font-display);
  font-size: .85rem;
  font-weight: 700;
  border-bottom: 1px solid var(--line);
  position: sticky;
  top: -.35rem;
  background: var(--panel);
}

.hd-10__panel-h span {
  font-family: var(--font-body);
  font-size: .7rem;
  font-weight: 600;
  color: var(--accent);
}

.hd-10__note {
  display: flex;
  align-items: start;
  gap: .55rem;
  padding: .6rem;
  border-radius: .55rem;
  color: var(--ink);
  text-decoration: none;
  font-size: .84rem;
  transition: background-color .13s ease;
}

.hd-10__note:hover {
  background: var(--panel2);
}

.hd-10__note-t {
  flex: 1;
  min-inline-size: 0;
  text-wrap: pretty;
}

.hd-10__note strong {
  font-weight: 660;
}

.hd-10__note em {
  font-style: normal;
  color: var(--accent);
}

.hd-10__note time {
  font-size: .72rem;
  color: var(--muted);
  flex: none;
  font-variant-numeric: tabular-nums;
  padding-top: .1rem;
}

.hd-10__dot {
  inline-size: .45rem;
  block-size: .45rem;
  border-radius: 50%;
  background: var(--accent);
  flex: none;
  margin-top: .45rem;
}

.hd-10__note--new {
  background: var(--accent-soft);
}

.hd-10__panel-f {
  display: block;
  margin-top: .25rem;
  padding: .6rem;
  border-top: 1px solid var(--line);
  color: var(--accent);
  text-decoration: none;
  font-size: .82rem;
  font-weight: 640;
  text-align: center;
}

.hd-10__row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .5rem;
  min-block-size: 2.5rem;
  padding: .45rem .6rem;
  border-radius: .5rem;
  color: var(--ink);
  text-decoration: none;
  font-size: .86rem;
}

.hd-10__row:hover {
  background: var(--panel2);
}

.hd-10__row kbd {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .7rem;
  color: var(--muted);
  border: 1px solid var(--line2);
  border-radius: .25rem;
  padding: .1rem .3rem;
}

.hd-10__row--out {
  color: #fb7185;
  border-top: 1px solid var(--line);
  margin-top: .25rem;
  padding-top: .55rem;
  border-radius: 0 0 .5rem .5rem;
}
/* ── page body ────────────────────────────────────────────────────── */

.hd-10__main {
  max-inline-size: 64rem;
  margin-inline: auto;
  padding: clamp(2rem,5vw,3rem) clamp(1rem,3vw,1.5rem) 4rem;
}

.hd-10__main h1 {
  font-family: var(--font-display);
  font-size: clamp(1.6rem,4.5vw,2.2rem);
  font-weight: 700;
  letter-spacing: -.02em;
}

.hd-10__lead {
  margin-top: .6rem;
  max-inline-size: 58ch;
  color: var(--muted);
  font-size: .98rem;
  text-wrap: pretty;
}

.hd-10__threads {
  margin-top: 1.75rem;
  border: 1px solid var(--line);
  border-radius: .8rem;
  overflow: hidden;
  background: var(--panel);
}

.hd-10__threads li {
  display: flex;
  align-items: center;
  gap: .75rem;
  padding: .9rem 1rem;
  border-bottom: 1px solid var(--line);
  font-size: .9rem;
}

.hd-10__threads li:last-child {
  border-bottom: 0;
}

.hd-10__threads li:hover {
  background: var(--panel2);
}

.hd-10__t-av {
  display: grid;
  place-items: center;
  inline-size: 2rem;
  block-size: 2rem;
  border-radius: .5rem;
  flex: none;
  background: var(--panel2);
  border: 1px solid var(--line2);
  font-family: var(--font-display);
  font-size: .7rem;
  font-weight: 700;
  color: var(--muted);
}

.hd-10__t-t {
  flex: 1;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-10__threads time {
  font-size: .75rem;
  color: var(--muted);
  flex: none;
  font-variant-numeric: tabular-nums;
}

.hd-10__filler {
  block-size: 50vh;
}

@media (max-width: 820px) {
  .hd-10__nav {
    display: none;
  }
}

@media (max-width: 520px) {
  .hd-10__user-t {
    display: none;
  }

  .hd-10__user {
    max-inline-size: none;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-10:has(#hd-10-light:checked) {
  --bg: #faf7f4;
  --panel: #ffffff;
  --panel2: #f2ece7;
  --ink: #1c1714;
  --muted: #6d6259;
  --line: rgba(28,23,20,.12);
  --line2: rgba(28,23,20,.2);
  --accent: #be185d;
  --accent-ink: #ffffff;
  --accent-soft: rgba(190,24,93,.09);
}
/* icon: shows the scheme the toggle will switch you to */

.hd-10__moon {
  display: none;
}

.hd-10:has(#hd-10-light:checked) .hd-10__sun {
  display: none;
}

.hd-10:has(#hd-10-light:checked) .hd-10__moon {
  display: block;
}

@media (prefers-color-scheme: light) {
  .hd-10:not([data-theme="dark"]):not(:has(#hd-10-light:checked)) {
    --bg: #faf7f4;
    --panel: #ffffff;
    --panel2: #f2ece7;
    --ink: #1c1714;
    --muted: #6d6259;
    --line: rgba(28,23,20,.12);
    --line2: rgba(28,23,20,.2);
    --accent: #be185d;
    --accent-ink: #ffffff;
    --accent-soft: rgba(190,24,93,.09);
    --accent-glow: rgba(190,24,93,.4);
  }
  /* FLIP-BACK — light OS + checked toggle restores the full charcoal set */

  .hd-10:has(#hd-10-light:checked) {
    --bg: #181513;
    --panel: #221e1b;
    --panel2: #2c2724;
    --ink: #f6f1ec;
    --muted: #a99e95;
    --line: rgba(246,241,236,.12);
    --line2: rgba(246,241,236,.2);
    --accent: #ec4899;
    --accent-ink: #2a0716;
    --accent-soft: rgba(236,72,153,.16);
    --accent-glow: rgba(236,72,153,.55);
  }
  /* the icon always offers the scheme you are not in */

  .hd-10:not([data-theme="dark"]):not(:has(#hd-10-light:checked)) .hd-10__sun {
    display: none;
  }

  .hd-10:not([data-theme="dark"]):not(:has(#hd-10-light:checked)) .hd-10__moon {
    display: block;
  }

  .hd-10:has(#hd-10-light:checked) .hd-10__moon {
    display: none;
  }

  .hd-10:has(#hd-10-light:checked) .hd-10__sun {
    display: block;
  }
}

.hd-10[data-theme="light"] {
  --bg: #faf7f4;
  --panel: #ffffff;
  --panel2: #f2ece7;
  --ink: #1c1714;
  --muted: #6d6259;
  --line: rgba(28,23,20,.12);
  --line2: rgba(28,23,20,.2);
  --accent: #be185d;
  --accent-ink: #ffffff;
  --accent-soft: rgba(190,24,93,.09);
}

@media (prefers-reduced-motion: reduce) {
  .hd-10__badge {
    animation: none !important;
  }

  .hd-10 * {
    transition-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-10__panel {
    border: 1px solid CanvasText;
  }
}
```
