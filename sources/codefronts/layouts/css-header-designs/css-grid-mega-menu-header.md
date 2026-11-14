---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/css-grid-mega-menu-header/"
title: "CSS Grid Mega Menu Header with Focus Within"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "A mega panel that is a genuine CSS Grid: a category column, a row of featured cards and a promo rail, laid out in three tracks and opened by :hover or…"
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Grid Mega Menu Header with Focus Within
Source: https://codefronts.com/layouts/css-header-designs/css-grid-mega-menu-header/

A mega panel that is a genuine CSS Grid: a category column, a row of featured cards and a promo rail, laid out in three tracks and opened by :hover or :focus-within on the parent item. transition-behavior: allow-discrete means the closed panel truly leaves the flow, so its twenty links are not sitting in the tab order waiting to swallow keyboard focus.
## HTML
```html
<div class="hd-13">
  <a class="hd-13__skip" href="#hd-13-main">Skip to content</a>

  <header class="hd-13__bar">
    <a class="hd-13__brand" href="#hd-13-main">
      <span class="hd-13__mark" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M5 18V6l7 6 7-6v12" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </span>
      <span class="hd-13__word">Mosaic</span>
    </a>

    <nav class="hd-13__nav" aria-label="Main">
      <ul class="hd-13__nav-list">
        <li class="hd-13__item">
          <a class="hd-13__trigger" href="#hd-13-main" aria-haspopup="menu">Platform
            <svg class="hd-13__chev" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M8 10.5 12 14.5l4-4" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <div class="hd-13__mega" role="menu" aria-label="Platform">
            <div class="hd-13__col hd-13__col--cats">
              <p class="hd-13__h">Capabilities</p>
              <a role="menuitem" href="#hd-13-main">Content model</a>
              <a role="menuitem" href="#hd-13-main">Workflows</a>
              <a role="menuitem" href="#hd-13-main">Localisation</a>
              <a role="menuitem" href="#hd-13-main">Asset pipeline</a>
              <a role="menuitem" href="#hd-13-main">Permissions</a>
              <a role="menuitem" href="#hd-13-main">Audit log</a>
            </div>
            <div class="hd-13__col hd-13__col--feat">
              <p class="hd-13__h">What teams build</p>
              <div class="hd-13__cards">
                <a class="hd-13__card" role="menuitem" href="#hd-13-main">
                  <span class="hd-13__thumb"><img src="https://images.unsplash.com/photo-1517180102446-f3ece451e9d8?auto=format&amp;fit=crop&amp;w=440&amp;q=70" alt="Two people reviewing layouts on a laptop screen" loading="lazy" width="440" height="248"></span>
                  <span class="hd-13__card-t">Editorial desks</span>
                  <span class="hd-13__card-d">Draft, review and schedule with real approvals.</span>
                </a>
                <a class="hd-13__card" role="menuitem" href="#hd-13-main">
                  <span class="hd-13__thumb"><img src="https://images.unsplash.com/photo-1551650975-87deedd944c3?auto=format&amp;fit=crop&amp;w=440&amp;q=70" alt="Designer sketching interface screens on paper" loading="lazy" width="440" height="248"></span>
                  <span class="hd-13__card-t">Design systems</span>
                  <span class="hd-13__card-d">One token source, every surface in sync.</span>
                </a>
                <a class="hd-13__card hd-13__card--flat" role="menuitem" href="#hd-13-main">
                  <span class="hd-13__chip">New</span>
                  <span class="hd-13__card-t">Commerce catalogues</span>
                  <span class="hd-13__card-d">40k SKUs with variant-aware previews.</span>
                </a>
                <a class="hd-13__card hd-13__card--flat" role="menuitem" href="#hd-13-main">
                  <span class="hd-13__chip hd-13__chip--alt">Guide</span>
                  <span class="hd-13__card-t">Migrating from files</span>
                  <span class="hd-13__card-d">A three-week plan that survived contact.</span>
                </a>
              </div>
            </div>
            <div class="hd-13__col hd-13__col--promo">
              <p class="hd-13__h">Live</p>
              <p class="hd-13__promo-t">Workflow builder, now visual</p>
              <p class="hd-13__promo-d">Draw the states, set the approvers, ship it the same afternoon.</p>
              <span class="hd-13__promo-cta" aria-hidden="true">Watch the 4 min tour &#8594;</span>
            </div>
          </div>
        </li>
        <li class="hd-13__item"><a class="hd-13__trigger" href="#hd-13-main">Solutions</a></li>
        <li class="hd-13__item"><a class="hd-13__trigger" href="#hd-13-main">Pricing</a></li>
        <li class="hd-13__item"><a class="hd-13__trigger" href="#hd-13-main">Docs</a></li>
      </ul>
    </nav>

    <div class="hd-13__right">
      <input class="hd-13__sr" type="checkbox" id="hd-13-dark">
      <label class="hd-13__theme" for="hd-13-dark">
        <svg class="hd-13__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <svg class="hd-13__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <span class="hd-13__vh">Switch light or dark theme</span>
      </label>
      <a class="hd-13__link" href="#hd-13-main">Sign in</a>
      <a class="hd-13__cta" href="#hd-13-main">Book a demo</a>
    </div>
  </header>

  <main class="hd-13__main" id="hd-13-main">
    <p class="hd-13__eyebrow">Content platform</p>
    <h1>Open <span>Platform</span> in the header &mdash; with a pointer or with Tab.</h1>
    <p class="hd-13__lead">The panel is one grid: categories, four cards, promo rail. When it closes it is <code>display:none</code>, so no invisible links sit in the tab order.</p>
    <ul class="hd-13__pills">
      <li>Keyboard operable</li>
      <li>No JavaScript</li>
      <li>Discrete transitions</li>
      <li>Static fallback under 820px</li>
    </ul>
    <div class="hd-13__filler" aria-hidden="true"></div>
  </main>
</div>
```
## CSS
```css
.hd-13 {
  --bg: #f6f4ff;
  --panel: #ffffff;
  --panel2: #f2eefe;
  --ink: #1b1436;
  --muted: #5f5580;
  --line: rgba(27,20,54,.1);
  --line2: rgba(27,20,54,.18);
  --accent: #7c3aed;
  --accent-soft: #ede4ff;
  --accent-ink: #ffffff;
  --lime: #c7f284;
  --in: 200ms;
  --font-display: ui-rounded,"SF Pro Rounded","Nunito",system-ui,sans-serif;
  --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  background: radial-gradient(48rem 24rem at 84% -12%, rgba(199,242,132,.5), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.55;
}

@supports (color: oklch(50% .1 200)) {
  .hd-13 {
    --bg: oklch(97% .02 300);
    --panel2: oklch(95% .03 300);
    --ink: oklch(22% .07 300);
    --muted: oklch(48% .05 300);
    --accent: oklch(52% .24 295);
  }
}

.hd-13 * {
  box-sizing: border-box;
}

.hd-13 h1,
.hd-13 p,
.hd-13 ul {
  margin: 0;
  padding: 0;
}

.hd-13 ul {
  list-style: none;
}

.hd-13 [hidden] {
  display: none;
}

.hd-13 :focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
  border-radius: .5rem;
}

.hd-13__skip {
  position: absolute;
  inset-inline-start: 1rem;
  top: -3rem;
  z-index: 60;
  padding: .55rem 1rem;
  border-radius: 999px;
  background: var(--accent);
  color: var(--accent-ink);
  font-size: .82rem;
  font-weight: 700;
  text-decoration: none;
  transition: top .18s ease;
}

.hd-13__skip:focus-visible {
  top: 1rem;
}
/* ── header: roomy, elevated panel idiom ──────────────────────────── */

.hd-13__bar {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  gap: clamp(1rem,3vw,2rem);
  padding: 1.05rem clamp(1rem,4vw,2.25rem);
  background: color-mix(in srgb, var(--bg) 88%, white);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--line);
}

.hd-13__brand {
  display: inline-flex;
  align-items: center;
  gap: .6rem;
  color: var(--ink);
  text-decoration: none;
  min-inline-size: 0;
}

.hd-13__mark {
  display: grid;
  place-items: center;
  inline-size: 2.1rem;
  block-size: 2.1rem;
  border-radius: .7rem;
  background: var(--accent);
  color: #fff;
  flex: none;
  box-shadow: 0 .5rem 1.2rem -.4rem rgba(124,58,237,.7);
}

.hd-13__mark svg {
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.hd-13__word {
  font-family: var(--font-display);
  font-size: 1.08rem;
  font-weight: 700;
  letter-spacing: -.02em;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-13__nav {
  min-inline-size: 0;
}

.hd-13__nav-list {
  display: flex;
  align-items: center;
  gap: .2rem;
}

.hd-13__item {
  position: relative;
}

.hd-13__trigger {
  display: inline-flex;
  align-items: center;
  gap: .3rem;
  min-block-size: 2.5rem;
  padding: .5rem .8rem;
  border-radius: 999px;
  color: var(--ink);
  text-decoration: none;
  font-family: var(--font-display);
  font-size: .9rem;
  font-weight: 620;
  white-space: nowrap;
  transition: background-color .16s ease, color .16s ease;
}

.hd-13__trigger:hover {
  background: var(--accent-soft);
  color: var(--accent);
}

.hd-13__chev {
  inline-size: .95rem;
  block-size: .95rem;
  transition: rotate .2s ease;
}

.hd-13__item:hover .hd-13__chev,
.hd-13__item:focus-within .hd-13__chev {
  rotate: 180deg;
}

.hd-13__mega {
  position: absolute;
  inset-inline-start: -1rem;
  top: calc(100% + .55rem);
  z-index: 35;
  inline-size: min(60rem,94vw);
  grid-template-columns: 12rem minmax(0,1fr) 14rem;
  gap: 1.5rem;
  padding: 1.5rem;
  border: 1px solid var(--line);
  border-radius: 1.4rem;
  background: var(--panel);
  box-shadow: 0 2.5rem 4.5rem -1.5rem rgba(27,20,54,.3);
  display: none;
  opacity: 0;
  translate: 0 -.5rem;
  transition: opacity var(--in) ease, translate var(--in) ease, display var(--in) allow-discrete;
}

@starting-style {
  .hd-13__item:hover > .hd-13__mega,
    .hd-13__item:focus-within > .hd-13__mega {
    opacity: 0;
    translate: 0 -.5rem;
  }
}

.hd-13__item:hover > .hd-13__mega,
.hd-13__item:focus-within > .hd-13__mega {
  display: grid;
  opacity: 1;
  translate: 0 0;
}

.hd-13__h {
  font-size: .68rem;
  font-weight: 800;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: .6rem;
}

.hd-13__col--cats {
  display: grid;
  gap: .1rem;
  align-content: start;
  border-inline-end: 1px solid var(--line);
  padding-inline-end: 1rem;
}

.hd-13__col--cats a {
  padding: .45rem .55rem;
  min-block-size: 2.3rem;
  display: flex;
  align-items: center;
  border-radius: .55rem;
  color: var(--ink);
  text-decoration: none;
  font-size: .87rem;
  transition: background-color .13s ease, color .13s ease;
}

.hd-13__col--cats a:hover {
  background: var(--accent-soft);
  color: var(--accent);
}

.hd-13__cards {
  display: grid;
  grid-template-columns: repeat(2,minmax(0,1fr));
  gap: .75rem;
}

.hd-13__card {
  display: grid;
  gap: .3rem;
  padding: .6rem;
  border-radius: .9rem;
  background: var(--panel2);
  color: var(--ink);
  text-decoration: none;
  min-inline-size: 0;
  transition: translate .18s ease, box-shadow .18s ease;
}

.hd-13__card:hover {
  translate: 0 -2px;
  box-shadow: 0 1rem 1.8rem -.9rem rgba(27,20,54,.28);
}

.hd-13__thumb {
  display: block;
  aspect-ratio: 16/9;
  overflow: hidden;
  border-radius: .6rem;
  background: linear-gradient(135deg,#ddd3ff,#c7f284);
}

.hd-13__thumb img {
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  display: block;
}

.hd-13__card-t {
  font-family: var(--font-display);
  font-size: .9rem;
  font-weight: 700;
}

.hd-13__card-d {
  font-size: .8rem;
  color: var(--muted);
  text-wrap: pretty;
}

.hd-13__card--flat {
  background: transparent;
  border: 1px dashed var(--line2);
}

.hd-13__chip {
  justify-self: start;
  font-size: .64rem;
  font-weight: 800;
  letter-spacing: .1em;
  text-transform: uppercase;
  padding: .2rem .45rem;
  border-radius: 999px;
  background: var(--accent);
  color: #fff;
}

.hd-13__chip--alt {
  background: var(--lime);
  color: #2c3d10;
}

.hd-13__col--promo {
  display: grid;
  align-content: start;
  gap: .35rem;
  padding: 1.1rem;
  border-radius: 1rem;
  background: linear-gradient(160deg, var(--accent) 0%, #a855f7 100%);
  color: #fff;
}

.hd-13__col--promo .hd-13__h {
  color: rgba(255,255,255,.75);
}

.hd-13__promo-t {
  font-family: var(--font-display);
  font-size: 1.15rem;
  font-weight: 700;
  line-height: 1.15;
  text-wrap: balance;
}

.hd-13__promo-d {
  font-size: .83rem;
  color: rgba(255,255,255,.85);
  text-wrap: pretty;
}

.hd-13__promo-cta {
  font-size: .82rem;
  font-weight: 700;
  margin-top: .3rem;
}

.hd-13__right {
  display: flex;
  align-items: center;
  gap: .75rem;
  margin-inline-start: auto;
}

.hd-13__link {
  color: var(--muted);
  text-decoration: none;
  font-size: .88rem;
  font-weight: 600;
  white-space: nowrap;
}

.hd-13__link:hover {
  color: var(--ink);
}

.hd-13__cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: .7rem 1.2rem;
  border-radius: 999px;
  background: var(--ink);
  color: #fff;
  text-decoration: none;
  font-family: var(--font-display);
  font-size: .88rem;
  font-weight: 700;
  white-space: nowrap;
  transition: translate .16s ease, background-color .16s ease;
}

.hd-13__cta:hover {
  translate: 0 -2px;
  background: var(--accent);
}
/* ── page body ────────────────────────────────────────────────────── */

.hd-13__main {
  max-inline-size: 64rem;
  margin-inline: auto;
  padding: clamp(2.5rem,8vw,5rem) clamp(1.25rem,4vw,2.25rem) 5rem;
}

.hd-13__eyebrow {
  font-size: .74rem;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.hd-13__main h1 {
  font-family: var(--font-display);
  font-size: clamp(1.9rem,6vw,3.3rem);
  line-height: 1.06;
  font-weight: 700;
  letter-spacing: -.03em;
  margin-top: 1rem;
  max-inline-size: 26ch;
  text-wrap: balance;
}

.hd-13__main h1 span {
  background: var(--lime);
  padding: 0 .3rem;
  border-radius: .4rem;
}

.hd-13__lead {
  margin-top: 1.1rem;
  max-inline-size: 54ch;
  color: var(--muted);
  font-size: 1.04rem;
  text-wrap: pretty;
}

.hd-13__lead code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  background: var(--panel2);
  padding: .1rem .3rem;
  border-radius: .3rem;
}

.hd-13__pills {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  margin-top: 1.75rem;
}

.hd-13__pills li {
  padding: .45rem .85rem;
  border-radius: 999px;
  background: var(--panel);
  border: 1px solid var(--line);
  font-size: .82rem;
  font-weight: 600;
}

.hd-13__filler {
  block-size: 50vh;
}

@media (max-width: 1080px) {
  .hd-13__mega {
    grid-template-columns: 11rem minmax(0,1fr);
    inline-size: min(46rem,94vw);
  }

  .hd-13__col--promo {
    display: none;
  }
}

@media (max-width: 820px) {
  .hd-13__nav-list {
    overflow: visible;
  }

  .hd-13__mega {
    position: static;
    inline-size: 100%;
    grid-template-columns: minmax(0,1fr);
    padding: 1rem;
    box-shadow: none;
    translate: 0 0;
    opacity: 1;
  }

  .hd-13__item:focus-within > .hd-13__mega {
    display: grid;
  }

  .hd-13__col--cats {
    border-inline-end: 0;
    padding-inline-end: 0;
  }

  .hd-13__cards {
    grid-template-columns: minmax(0,1fr);
  }

  .hd-13__bar {
    flex-wrap: wrap;
  }

  .hd-13__nav {
    flex-basis: 100%;
    order: 3;
  }

  .hd-13__nav-list {
    flex-wrap: wrap;
  }
}

@media (max-width: 480px) {
  .hd-13__link {
    display: none;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-13:has(#hd-13-dark:checked) {
  --bg: #120f1d;
  --panel: #1a1528;
  --panel2: #221a34;
  --ink: #f3eeff;
  --muted: #a99cc9;
  --line: rgba(243,238,255,.12);
  --line2: rgba(243,238,255,.2);
  --accent: #c4b5fd;
  --accent-soft: rgba(196,181,253,.16);
  --accent-ink: #1e1035;
  --lime: #b6e86a;
}

.hd-13:has(#hd-13-dark:checked) .hd-13__cta {
  background: var(--accent);
  color: var(--accent-ink);
}

.hd-13:has(#hd-13-dark:checked) .hd-13__main h1 span {
  color: #1e1035;
}
/* icon: shows the scheme the toggle will switch you to */

.hd-13__sun {
  display: none;
}

.hd-13:has(#hd-13-dark:checked) .hd-13__moon {
  display: none;
}

.hd-13:has(#hd-13-dark:checked) .hd-13__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .hd-13:not([data-theme="light"]):not(:has(#hd-13-dark:checked)) {
    --bg: #120f1d;
    --panel: #1a1528;
    --panel2: #221a34;
    --ink: #f3eeff;
    --muted: #a99cc9;
    --line: rgba(243,238,255,.12);
    --line2: rgba(243,238,255,.2);
    --accent: #c4b5fd;
    --accent-soft: rgba(196,181,253,.16);
    --accent-ink: #1e1035;
    --lime: #b6e86a;
  }

  .hd-13:not([data-theme="light"]):not(:has(#hd-13-dark:checked)) .hd-13__cta {
    background: var(--accent);
    color: var(--accent-ink);
  }

  .hd-13:not([data-theme="light"]):not(:has(#hd-13-dark:checked)) .hd-13__main h1 span {
    color: #1e1035;
  }
  /* FLIP-BACK — dark OS + checked toggle returns to the other scheme */

  .hd-13:has(#hd-13-dark:checked) {
    --bg: #f6f4ff;
    --panel: #ffffff;
    --panel2: #f2eefe;
    --ink: #1b1436;
    --muted: #5f5580;
    --line: rgba(27,20,54,.1);
    --line2: rgba(27,20,54,.18);
    --accent: #7c3aed;
    --accent-soft: #ede4ff;
    --accent-ink: #ffffff;
    --lime: #c7f284;
    --in: 200ms;
    --font-display: ui-rounded,"SF Pro Rounded","Nunito",system-ui,sans-serif;
    --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  }

  .hd-13:has(#hd-13-dark:checked) .hd-13__cta {
    display: inline-flex;
    align-items: center;
    min-block-size: 2.75rem;
    padding: .7rem 1.2rem;
    border-radius: 999px;
    background: var(--ink);
    color: #fff;
    text-decoration: none;
    font-family: var(--font-display);
    font-size: .88rem;
    font-weight: 700;
    white-space: nowrap;
    transition: translate .16s ease, background-color .16s ease;
  }

  .hd-13:has(#hd-13-dark:checked) .hd-13__main h1 span {
    background: var(--lime);
    padding: 0 .3rem;
    border-radius: .4rem;
  }
  /* the icon always offers the scheme you are not in */

  .hd-13:not([data-theme="light"]):not(:has(#hd-13-dark:checked)) .hd-13__moon {
    display: none;
  }

  .hd-13:not([data-theme="light"]):not(:has(#hd-13-dark:checked)) .hd-13__sun {
    display: block;
  }

  .hd-13:has(#hd-13-dark:checked) .hd-13__sun {
    display: none;
  }

  .hd-13:has(#hd-13-dark:checked) .hd-13__moon {
    display: block;
  }
}

.hd-13[data-theme="dark"] {
  --bg: #120f1d;
  --panel: #1a1528;
  --panel2: #221a34;
  --ink: #f3eeff;
  --muted: #a99cc9;
  --line: rgba(243,238,255,.12);
  --line2: rgba(243,238,255,.2);
  --accent: #c4b5fd;
  --accent-soft: rgba(196,181,253,.16);
  --accent-ink: #1e1035;
}

@media (prefers-reduced-motion: reduce) {
  .hd-13 * {
    transition-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-13__mega {
    border: 1px solid CanvasText;
  }
}
/* ── theme toggle — visually hidden checkbox, zero JS ────────────── */

.hd-13__sr,
.hd-13__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-13__theme {
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

.hd-13__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-13__theme:hover {
  background: rgba(128,128,128,.16);
}

.hd-13:has(#hd-13-dark:focus-visible) .hd-13__theme {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```
