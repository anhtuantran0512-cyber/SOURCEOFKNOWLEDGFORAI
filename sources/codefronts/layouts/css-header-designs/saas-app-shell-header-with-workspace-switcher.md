---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/saas-app-shell-header-with-workspace-switcher/"
title: "SaaS App Shell Header with Workspace Switcher"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "The chrome that wraps a multi-tenant product: a workspace picker on the left showing the active tenant's avatar and a truncated name, section nav in the…"
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SaaS App Shell Header with Workspace Switcher
Source: https://codefronts.com/layouts/css-header-designs/saas-app-shell-header-with-workspace-switcher/

The chrome that wraps a multi-tenant product: a workspace picker on the left showing the active tenant's avatar and a truncated name, section nav in the middle, and a right toolbar of search, notifications and account. Both menus open on hover and on :focus-within with no script, and the workspace list ends in a Create workspace row like every real switcher does.
## HTML
```html
<div class="hd-03">
  <a class="hd-03__skip" href="#hd-03-main">Skip to content</a>

  <header class="hd-03__bar">
    <div class="hd-03__menu">
      <button class="hd-03__ws" type="button" aria-haspopup="menu">
        <span class="hd-03__av" style="--a:#4f46e5;--b:#0ea5e9" aria-hidden="true">NW</span>
        <span class="hd-03__ws-text">
          <span class="hd-03__ws-name">Northwind Labs</span>
          <span class="hd-03__ws-sub">Pro &middot; 24 seats</span>
        </span>
        <svg class="hd-03__chev" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M8 10.5 12 14.5l4-4" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
      <div class="hd-03__pop hd-03__pop--ws" role="menu" aria-label="Switch workspace">
        <p class="hd-03__pop-h">Workspaces</p>
        <a class="hd-03__item" role="menuitem" href="#hd-03-main" aria-current="true">
          <span class="hd-03__av hd-03__av--sm" style="--a:#4f46e5;--b:#0ea5e9" aria-hidden="true">NW</span>
          <span class="hd-03__item-t">Northwind Labs</span>
          <svg class="hd-03__tick" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12.5 9.5 17 19 7" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </a>
        <a class="hd-03__item" role="menuitem" href="#hd-03-main">
          <span class="hd-03__av hd-03__av--sm" style="--a:#f97316;--b:#e11d48" aria-hidden="true">AT</span>
          <span class="hd-03__item-t">Atlas Freight</span>
        </a>
        <a class="hd-03__item" role="menuitem" href="#hd-03-main">
          <span class="hd-03__av hd-03__av--sm" style="--a:#059669;--b:#65a30d" aria-hidden="true">FD</span>
          <span class="hd-03__item-t">Foundry Design Co</span>
        </a>
        <a class="hd-03__item" role="menuitem" href="#hd-03-main">
          <span class="hd-03__av hd-03__av--sm" style="--a:#7c3aed;--b:#db2777" aria-hidden="true">HL</span>
          <span class="hd-03__item-t">Halcyon Internal</span>
        </a>
        <a class="hd-03__item hd-03__item--new" role="menuitem" href="#hd-03-main">
          <span class="hd-03__plus" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 5.5v13M5.5 12h13" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></span>
          <span class="hd-03__item-t">Create workspace</span>
        </a>
      </div>
    </div>

    <nav class="hd-03__nav" aria-label="Main">
      <ul>
        <li><a href="#hd-03-main" aria-current="page">Overview</a></li>
        <li><a href="#hd-03-main">Projects</a></li>
        <li><a href="#hd-03-main">Insights</a></li>
        <li><a href="#hd-03-main">Billing</a></li>
      </ul>
    </nav>

    <div class="hd-03__tools">
      <input class="hd-03__sr" type="checkbox" id="hd-03-dark">
      <label class="hd-03__theme" for="hd-03-dark">
        <svg class="hd-03__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <svg class="hd-03__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <span class="hd-03__vh">Switch light or dark theme</span>
      </label>
      <button class="hd-03__icon" type="button" aria-label="Search this workspace">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.8 15.8 21 21" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      </button>
      <button class="hd-03__icon" type="button" aria-label="Notifications, 3 unread">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6.5 10.5a5.5 5.5 0 0 1 11 0c0 3 .7 4.4 1.4 5.2.4.5.1 1.3-.6 1.3H5.7c-.7 0-1-.8-.6-1.3.7-.8 1.4-2.2 1.4-5.2Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><path d="M10 19.5a2.2 2.2 0 0 0 4 0" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <span class="hd-03__dot" aria-hidden="true"></span>
      </button>
      <div class="hd-03__menu">
        <button class="hd-03__acct" type="button" aria-haspopup="menu" aria-label="Account menu for Alex Chen">
          <span class="hd-03__av hd-03__av--sm" style="--a:#0ea5e9;--b:#6366f1" aria-hidden="true">AC</span>
        </button>
        <div class="hd-03__pop hd-03__pop--acct" role="menu" aria-label="Account">
          <p class="hd-03__who"><strong>Alex Chen</strong><span>[email protected]</span></p>
          <a class="hd-03__item" role="menuitem" href="#hd-03-main"><span class="hd-03__item-t">Profile</span></a>
          <a class="hd-03__item" role="menuitem" href="#hd-03-main"><span class="hd-03__item-t">Preferences</span><kbd>,</kbd></a>
          <a class="hd-03__item" role="menuitem" href="#hd-03-main"><span class="hd-03__item-t">Members and roles</span></a>
          <a class="hd-03__item hd-03__item--out" role="menuitem" href="#hd-03-main"><span class="hd-03__item-t">Sign out</span></a>
        </div>
      </div>
    </div>
  </header>

  <main class="hd-03__main" id="hd-03-main">
    <div class="hd-03__head">
      <div>
        <h1>Overview</h1>
        <p>Northwind Labs &middot; last 7 days</p>
      </div>
      <a class="hd-03__cta" href="#hd-03-main">New project</a>
    </div>

    <ul class="hd-03__stats">
      <li><p class="hd-03__k">Active projects</p><p class="hd-03__v">18</p><p class="hd-03__d hd-03__d--up">+3 this week</p></li>
      <li><p class="hd-03__k">Deploys</p><p class="hd-03__v">1,284</p><p class="hd-03__d hd-03__d--up">+11.4%</p></li>
      <li><p class="hd-03__k">p95 latency</p><p class="hd-03__v">184<span>ms</span></p><p class="hd-03__d hd-03__d--down">-22ms</p></li>
      <li><p class="hd-03__k">Error budget</p><p class="hd-03__v">96<span>%</span></p><p class="hd-03__d">on track</p></li>
    </ul>

    <section class="hd-03__panel">
      <h2>Recent activity</h2>
      <ul class="hd-03__rows">
        <li><span class="hd-03__av hd-03__av--sm" style="--a:#0ea5e9;--b:#6366f1" aria-hidden="true">AC</span><span class="hd-03__row-t">Alex Chen promoted <strong>checkout-v3</strong> to production</span><time>12m</time></li>
        <li><span class="hd-03__av hd-03__av--sm" style="--a:#f97316;--b:#e11d48" aria-hidden="true">PS</span><span class="hd-03__row-t">Priya Sharma opened <strong>Reduce cold starts in eu-west</strong></span><time>1h</time></li>
        <li><span class="hd-03__av hd-03__av--sm" style="--a:#059669;--b:#65a30d" aria-hidden="true">JL</span><span class="hd-03__row-t">Jordan Lee invited two members to <strong>Atlas Freight</strong></span><time>3h</time></li>
        <li><span class="hd-03__av hd-03__av--sm" style="--a:#7c3aed;--b:#db2777" aria-hidden="true">SR</span><span class="hd-03__row-t">Sam Rivera rotated the staging API key</span><time>Yesterday</time></li>
      </ul>
    </section>
    <div class="hd-03__filler" aria-hidden="true"></div>
  </main>
</div>
```
## CSS
```css
.hd-03 {
  --bg: #f7f8fa;
  --panel: #ffffff;
  --panel2: #eef0f4;
  --ink: #121620;
  --muted: #626b7d;
  --line: rgba(18,22,32,.1);
  --line2: rgba(18,22,32,.16);
  --accent: #4f46e5;
  --accent-soft: rgba(79,70,229,.1);
  --accent-ink: #ffffff;
  --up: #0f7a4d;
  --down: #0f6fb8;
  --font-display: ui-rounded,"SF Pro Rounded","Nunito",system-ui,sans-serif;
  --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  --pad: .55rem;
  --r: .65rem;
  width: 100%;
  min-height: 100vh;
  display: block;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.5;
}

@supports (color: oklch(50% .1 200)) {
  .hd-03 {
    --bg: oklch(97.5% .005 260);
    --panel: oklch(100% 0 0);
    --panel2: oklch(95% .007 260);
    --ink: oklch(19% .02 265);
    --muted: oklch(52% .02 265);
    --accent: oklch(52% .2 279);
  }
}

.hd-03 * {
  box-sizing: border-box;
}

.hd-03 h1,
.hd-03 h2,
.hd-03 p,
.hd-03 ul {
  margin: 0;
  padding: 0;
}

.hd-03 ul {
  list-style: none;
}

.hd-03 [hidden] {
  display: none;
}

.hd-03 :focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: .4rem;
}

.hd-03__skip {
  position: absolute;
  inset-inline-start: .75rem;
  top: -3rem;
  z-index: 60;
  padding: .55rem 1rem;
  border-radius: .5rem;
  background: var(--accent);
  color: var(--accent-ink);
  font-size: .82rem;
  font-weight: 640;
  text-decoration: none;
  transition: top .18s ease;
}

.hd-03__skip:focus-visible {
  top: .75rem;
}
/* ── header: compact app chrome, 1px border + soft shadow ─────────── */

.hd-03__bar {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  gap: .5rem;
  padding: var(--pad) clamp(.6rem,2.5vw,1rem);
  background: var(--panel);
  border-bottom: 1px solid var(--line);
  box-shadow: 0 1px 2px rgba(18,22,32,.04), 0 8px 24px -18px rgba(18,22,32,.5);
}

.hd-03__menu {
  position: relative;
  min-inline-size: 0;
}

.hd-03__ws {
  display: flex;
  align-items: center;
  gap: .55rem;
  max-inline-size: 15rem;
  min-inline-size: 0;
  padding: .35rem .45rem;
  border: 1px solid transparent;
  border-radius: var(--r);
  background: transparent;
  color: var(--ink);
  font: inherit;
  cursor: pointer;
  text-align: start;
  transition: background-color .15s ease, border-color .15s ease;
}

.hd-03__ws:hover {
  background: var(--panel2);
  border-color: var(--line);
}

.hd-03__av {
  display: grid;
  place-items: center;
  inline-size: 2rem;
  block-size: 2rem;
  border-radius: .55rem;
  flex: none;
  background: linear-gradient(135deg, var(--a), var(--b));
  color: #fff;
  font-family: var(--font-display);
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .02em;
  box-shadow: inset 0 0 0 1px rgba(255,255,255,.22);
}

.hd-03__av--sm {
  inline-size: 1.7rem;
  block-size: 1.7rem;
  border-radius: .5rem;
  font-size: .64rem;
}

.hd-03__ws-text {
  display: grid;
  min-inline-size: 0;
}

.hd-03__ws-name {
  font-family: var(--font-display);
  font-size: .86rem;
  font-weight: 660;
  letter-spacing: -.01em;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-03__ws-sub {
  font-size: .7rem;
  color: var(--muted);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-03__chev {
  inline-size: 1rem;
  block-size: 1rem;
  color: var(--muted);
  flex: none;
  transition: rotate .18s ease;
}

.hd-03__menu:hover .hd-03__chev,
.hd-03__menu:focus-within .hd-03__chev {
  rotate: 180deg;
}

.hd-03__pop {
  position: absolute;
  top: calc(100% + .4rem);
  z-index: 40;
  inline-size: 16rem;
  padding: .35rem;
  border: 1px solid var(--line2);
  border-radius: .8rem;
  background: var(--panel);
  box-shadow: 0 1.4rem 2.8rem -1rem rgba(18,22,32,.3);
  visibility: hidden;
  opacity: 0;
  translate: 0 -.35rem;
  transition: opacity .16s ease, translate .16s ease, visibility .16s allow-discrete;
}

.hd-03__pop--ws {
  inset-inline-start: 0;
}

.hd-03__pop--acct {
  inset-inline-end: 0;
  inline-size: 14rem;
}

.hd-03__menu:hover > .hd-03__pop,
.hd-03__menu:focus-within > .hd-03__pop {
  visibility: visible;
  opacity: 1;
  translate: 0 0;
}

.hd-03__pop-h,
.hd-03__who {
  padding: .45rem .55rem;
  font-size: .68rem;
  font-weight: 700;
  letter-spacing: .09em;
  text-transform: uppercase;
  color: var(--muted);
}

.hd-03__who {
  display: grid;
  gap: .1rem;
  letter-spacing: 0;
  text-transform: none;
  font-weight: 500;
  border-bottom: 1px solid var(--line);
  margin-bottom: .25rem;
}

.hd-03__who strong {
  font-family: var(--font-display);
  font-size: .85rem;
  color: var(--ink);
}

.hd-03__who span {
  font-size: .75rem;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-03__item {
  display: flex;
  align-items: center;
  gap: .55rem;
  min-block-size: 2.5rem;
  padding: .4rem .55rem;
  border-radius: .55rem;
  text-decoration: none;
  color: var(--ink);
  font-size: .86rem;
  transition: background-color .13s ease;
}

.hd-03__item:hover {
  background: var(--panel2);
}

.hd-03__item-t {
  flex: 1;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-03__item kbd {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .7rem;
  color: var(--muted);
  border: 1px solid var(--line);
  border-radius: .25rem;
  padding: .1rem .3rem;
}

.hd-03__item[aria-current="true"] {
  background: var(--accent-soft);
  color: var(--accent);
  font-weight: 600;
}

.hd-03__tick {
  inline-size: 1rem;
  block-size: 1rem;
  flex: none;
}

.hd-03__item--new {
  border-top: 1px solid var(--line);
  margin-top: .25rem;
  padding-top: .5rem;
  color: var(--accent);
  font-weight: 600;
}

.hd-03__plus {
  display: grid;
  place-items: center;
  inline-size: 1.7rem;
  block-size: 1.7rem;
  border: 1px dashed var(--line2);
  border-radius: .5rem;
}

.hd-03__plus svg {
  inline-size: .9rem;
  block-size: .9rem;
}

.hd-03__item--out {
  color: #b42318;
}

.hd-03__nav {
  min-inline-size: 0;
  margin-inline-start: .5rem;
}

.hd-03__nav ul {
  display: flex;
  align-items: center;
  gap: .1rem;
  overflow: auto;
  scrollbar-width: none;
}

.hd-03__nav ul::-webkit-scrollbar {
  display: none;
}

.hd-03__nav a {
  display: block;
  padding: .42rem .65rem;
  border-radius: .5rem;
  color: var(--muted);
  text-decoration: none;
  font-size: .85rem;
  font-weight: 560;
  white-space: nowrap;
  transition: color .15s ease, background-color .15s ease;
}

.hd-03__nav a:hover {
  color: var(--ink);
  background: var(--panel2);
}

.hd-03__nav a[aria-current="page"] {
  color: var(--accent);
  background: var(--accent-soft);
}

.hd-03__tools {
  display: flex;
  align-items: center;
  gap: .25rem;
  margin-inline-start: auto;
}

.hd-03__icon,
.hd-03__acct {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: 2.35rem;
  block-size: 2.35rem;
  border: 0;
  border-radius: var(--r);
  background: transparent;
  color: var(--muted);
  cursor: pointer;
  transition: background-color .15s ease, color .15s ease;
}

.hd-03__icon svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-03__icon:hover,
.hd-03__acct:hover {
  background: var(--panel2);
  color: var(--ink);
}

.hd-03__dot {
  position: absolute;
  top: .45rem;
  inset-inline-end: .5rem;
  inline-size: .45rem;
  block-size: .45rem;
  border-radius: 50%;
  background: #e11d48;
  box-shadow: 0 0 0 2px var(--panel);
}
/* ── dashboard body ───────────────────────────────────────────────── */

.hd-03__main {
  max-inline-size: 78rem;
  margin-inline: auto;
  padding: clamp(1.25rem,4vw,2.25rem) clamp(1rem,3vw,1.5rem) 4rem;
}

.hd-03__head {
  display: flex;
  align-items: end;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.hd-03__head h1 {
  font-family: var(--font-display);
  font-size: clamp(1.5rem,4vw,2rem);
  font-weight: 700;
  letter-spacing: -.03em;
}

.hd-03__head p {
  color: var(--muted);
  font-size: .87rem;
  margin-top: .2rem;
}

.hd-03__cta {
  padding: .6rem 1rem;
  border-radius: var(--r);
  background: var(--accent);
  color: var(--accent-ink);
  text-decoration: none;
  font-size: .86rem;
  font-weight: 650;
  white-space: nowrap;
  box-shadow: 0 .4rem 1rem -.4rem rgba(79,70,229,.6);
  transition: translate .15s ease;
}

.hd-03__cta:hover {
  translate: 0 -1px;
}

.hd-03__stats {
  display: grid;
  gap: .75rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,11rem),1fr));
  margin-top: 1.5rem;
}

.hd-03__stats li {
  padding: .9rem 1rem;
  border: 1px solid var(--line);
  border-radius: .8rem;
  background: var(--panel);
  min-inline-size: 0;
}

.hd-03__k {
  font-size: .74rem;
  color: var(--muted);
  font-weight: 560;
}

.hd-03__v {
  font-family: var(--font-display);
  font-size: 1.7rem;
  font-weight: 700;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
  margin-top: .2rem;
}

.hd-03__v span {
  font-size: .9rem;
  color: var(--muted);
  font-weight: 600;
}

.hd-03__d {
  font-size: .75rem;
  color: var(--muted);
  margin-top: .15rem;
}

.hd-03__d--up {
  color: var(--up);
}

.hd-03__d--down {
  color: var(--down);
}

.hd-03__panel {
  margin-top: 1.25rem;
  border: 1px solid var(--line);
  border-radius: .9rem;
  background: var(--panel);
  overflow: hidden;
}

.hd-03__panel h2 {
  font-family: var(--font-display);
  font-size: .95rem;
  font-weight: 660;
  padding: .9rem 1rem;
  border-bottom: 1px solid var(--line);
}

.hd-03__rows li {
  display: flex;
  align-items: center;
  gap: .7rem;
  padding: .75rem 1rem;
  border-bottom: 1px solid var(--line);
  font-size: .87rem;
}

.hd-03__rows li:last-child {
  border-bottom: 0;
}

.hd-03__row-t {
  flex: 1;
  min-inline-size: 0;
}

.hd-03__rows time {
  font-size: .75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
  flex: none;
}

.hd-03__filler {
  block-size: 45vh;
}

@media (max-width: 820px) {
  .hd-03__nav {
    display: none;
  }

  .hd-03__ws-sub {
    display: none;
  }
}

@media (max-width: 420px) {
  .hd-03__ws {
    max-inline-size: 9rem;
  }

  .hd-03__pop--ws {
    inline-size: 14rem;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-03:has(#hd-03-dark:checked) {
  --bg: #0d1017;
  --panel: #151a24;
  --panel2: #1d2430;
  --ink: #eef1f7;
  --muted: #96a0b3;
  --line: rgba(238,241,247,.1);
  --line2: rgba(238,241,247,.18);
  --accent: #a5b4fc;
  --accent-soft: rgba(165,180,252,.14);
  --accent-ink: #131533;
  --up: #4ade80;
  --down: #7dd3fc;
}
/* icon: shows the scheme the toggle will switch you to */

.hd-03__sun {
  display: none;
}

.hd-03:has(#hd-03-dark:checked) .hd-03__moon {
  display: none;
}

.hd-03:has(#hd-03-dark:checked) .hd-03__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .hd-03:not([data-theme="light"]):not(:has(#hd-03-dark:checked)) {
    --bg: #0d1017;
    --panel: #151a24;
    --panel2: #1d2430;
    --ink: #eef1f7;
    --muted: #96a0b3;
    --line: rgba(238,241,247,.1);
    --line2: rgba(238,241,247,.18);
    --accent: #a5b4fc;
    --accent-soft: rgba(165,180,252,.14);
    --accent-ink: #131533;
    --up: #4ade80;
    --down: #7dd3fc;
  }
  /* FLIP-BACK — dark OS + checked toggle returns to the other scheme */

  .hd-03:has(#hd-03-dark:checked) {
    --bg: #f7f8fa;
    --panel: #ffffff;
    --panel2: #eef0f4;
    --ink: #121620;
    --muted: #626b7d;
    --line: rgba(18,22,32,.1);
    --line2: rgba(18,22,32,.16);
    --accent: #4f46e5;
    --accent-soft: rgba(79,70,229,.1);
    --accent-ink: #ffffff;
    --up: #0f7a4d;
    --down: #0f6fb8;
    --font-display: ui-rounded,"SF Pro Rounded","Nunito",system-ui,sans-serif;
    --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
    --pad: .55rem;
    --r: .65rem;
  }
  /* the icon always offers the scheme you are not in */

  .hd-03:not([data-theme="light"]):not(:has(#hd-03-dark:checked)) .hd-03__moon {
    display: none;
  }

  .hd-03:not([data-theme="light"]):not(:has(#hd-03-dark:checked)) .hd-03__sun {
    display: block;
  }

  .hd-03:has(#hd-03-dark:checked) .hd-03__sun {
    display: none;
  }

  .hd-03:has(#hd-03-dark:checked) .hd-03__moon {
    display: block;
  }
}

.hd-03[data-theme="dark"] {
  --bg: #0d1017;
  --panel: #151a24;
  --panel2: #1d2430;
  --ink: #eef1f7;
  --muted: #96a0b3;
  --line: rgba(238,241,247,.1);
  --line2: rgba(238,241,247,.18);
  --accent: #a5b4fc;
  --accent-soft: rgba(165,180,252,.14);
  --accent-ink: #131533;
}

@media (prefers-reduced-motion: reduce) {
  .hd-03 * {
    transition-duration: 1ms !important;
    animation-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-03__pop {
    border: 1px solid CanvasText;
  }
}
/* ── theme toggle — visually hidden checkbox, zero JS ────────────── */

.hd-03__sr,
.hd-03__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-03__theme {
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

.hd-03__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-03__theme:hover {
  background: rgba(128,128,128,.16);
}

.hd-03:has(#hd-03-dark:focus-visible) .hd-03__theme {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```
