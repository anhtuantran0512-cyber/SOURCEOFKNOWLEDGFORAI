---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/header-with-announcement-bar/"
title: "Header with Announcement Bar Dismissible"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "A promo bar above the header that collapses to nothing when dismissed &mdash; no script, no display:none jump."
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Header with Announcement Bar Dismissible
Source: https://codefronts.com/layouts/css-header-designs/header-with-announcement-bar/

A promo bar above the header that collapses to nothing when dismissed &mdash; no script, no display:none jump. The close button is a label for a hidden checkbox, and the bar animates from grid-template-rows: 1fr to 0fr, which is the modern way to transition to intrinsic zero height. Warm sepia surface with soft neumorphic relief.
## HTML
```html
<div class="hd-17">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@400;600;800&display=swap">
  <a class="hd-17__skip" href="#hd-17-main">Skip to content</a>
  <input class="hd-17__sr" type="checkbox" id="hd-17-close" aria-label="Dismiss announcement">

  <div class="hd-17__ann" role="region" aria-label="Announcement">
    <div class="hd-17__ann-in">
      <p class="hd-17__ann-t">
        <span class="hd-17__pill">New</span>
        Autumn roasts land Thursday &mdash; subscribers get first pick and free delivery on orders over <span class="hd-17__num">&pound;30</span>.
        <a class="hd-17__ann-link" href="#hd-17-main">See the lineup</a>
      </p>
      <label class="hd-17__x" for="hd-17-close">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6.5 6.5l11 11M17.5 6.5l-11 11" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
        <span class="hd-17__vh">Dismiss announcement</span>
      </label>
    </div>
  </div>

  <header class="hd-17__bar">
    <a class="hd-17__brand" href="#hd-17-main">
      <svg class="hd-17__mark" viewBox="0 0 26 26" fill="none" aria-hidden="true" focusable="false">
        <path d="M6.5 9h11a4.5 4.5 0 0 1 0 9h-.6a5.4 5.4 0 0 1-10.4-2V9Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/>
        <path d="M9 4.2c0 1.4 1.2 1.8 1.2 3.2M13 4.2c0 1.4 1.2 1.8 1.2 3.2" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
      </svg>
      <span class="hd-17__word">Kiln &amp; Co</span>
    </a>

    <nav class="hd-17__nav" aria-label="Main">
      <ul>
        <li><a href="#hd-17-main" aria-current="page">Coffee</a></li>
        <li><a href="#hd-17-main">Subscriptions</a></li>
        <li><a href="#hd-17-main">Equipment</a></li>
        <li><a href="#hd-17-main">Roastery</a></li>
      </ul>
    </nav>

    <div class="hd-17__right">
      <input class="hd-17__sr" type="checkbox" id="hd-17-dark">
      <label class="hd-17__theme" for="hd-17-dark">
        <svg class="hd-17__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <svg class="hd-17__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <span class="hd-17__vh">Switch light or dark theme</span>
      </label>
      <a class="hd-17__quiet" href="#hd-17-main">Account</a>
      <a class="hd-17__cta" href="#hd-17-main">Basket &middot; <span class="hd-17__num">2</span></a>
    </div>
  </header>

  <main class="hd-17__main" id="hd-17-main">
    <p class="hd-17__eyebrow">Single origin &middot; Huila, Colombia</p>
    <h1>Dismiss the bar &mdash; it collapses to nothing, not to a gap.</h1>
    <p class="hd-17__lead">The close control is a label for a hidden checkbox. The bar's grid row animates from <code>1fr</code> to <code>0fr</code>, so the header slides up over the real content height with no magic numbers.</p>
    <ul class="hd-17__grid">
      <li><p class="hd-17__g-t">Comuna 13</p><p class="hd-17__g-d">Plum, cocoa, a long finish. Ground for filter.</p><p class="hd-17__g-p">&pound;14.50</p></li>
      <li><p class="hd-17__g-t">Nightwork</p><p class="hd-17__g-d">Darker roast for milk. Holds up to a flat white.</p><p class="hd-17__g-p">&pound;12.00</p></li>
      <li><p class="hd-17__g-t">Rest Day</p><p class="hd-17__g-d">Decaf, washed, sweet enough to drink black.</p><p class="hd-17__g-p">&pound;13.25</p></li>
    </ul>
    <div class="hd-17__filler" aria-hidden="true"></div>
  </main>
</div>
```
## CSS
```css
.hd-17 {
  --bg: #f4ece2;
  --panel: #faf4ec;
  --panel2: #eadfd1;
  --ink: #2b1f16;
  --muted: #7a6553;
  --line: rgba(43,31,22,.14);
  --accent: #c2521a;
  --accent-soft: rgba(194,82,26,.12);
  --accent-ink: #fff8f2;
  --relief: 1;
  --collapse: 320ms;
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
  .hd-17 {
    --bg: oklch(94% .022 70);
    --panel: oklch(96.5% .018 70);
    --panel2: oklch(89% .03 70);
    --ink: oklch(25% .04 50);
    --muted: oklch(52% .04 50);
    --accent: oklch(55% .15 45);
  }
}

@supports (interpolate-size: allow-keywords) {
  .hd-17 {
    interpolate-size: allow-keywords;
  }
}

.hd-17 * {
  box-sizing: border-box;
}

.hd-17 h1,
.hd-17 p,
.hd-17 ul {
  margin: 0;
  padding: 0;
}

.hd-17 ul {
  list-style: none;
}

.hd-17 [hidden] {
  display: none;
}

.hd-17 :focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: .4rem;
}

.hd-17__sr,
.hd-17__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-17__skip {
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

.hd-17__skip:focus-visible {
  top: .75rem;
}
/* ── the collapsing announcement bar ──────────────────────────────── */

.hd-17__ann {
  display: grid;
  grid-template-rows: 1fr;
  overflow: hidden;
  background: linear-gradient(180deg, var(--panel2), var(--bg));
  border-bottom: 1px solid var(--line);
  box-shadow: inset 0 -1px 0 rgba(255,255,255,.6);
  transition: grid-template-rows var(--collapse) cubic-bezier(.3,.8,.3,1), opacity var(--collapse) ease;
}

.hd-17__ann-in {
  min-block-size: 0;
  overflow: hidden;
  display: flex;
  align-items: center;
  gap: .75rem;
  padding: .6rem clamp(.85rem,3vw,1.5rem);
}

.hd-17:has(#hd-17-close:checked) .hd-17__ann {
  grid-template-rows: 0fr;
  opacity: 0;
  border-bottom-color: transparent;
}

.hd-17__ann-t {
  flex: 1;
  min-inline-size: 0;
  font-size: .85rem;
  color: var(--ink);
  text-wrap: pretty;
  display: flex;
  align-items: center;
  gap: .5rem;
  flex-wrap: wrap;
}

.hd-17__pill {
  font-family: var(--font-display);
  font-size: .62rem;
  font-weight: 800;
  letter-spacing: .12em;
  text-transform: uppercase;
  padding: .2rem .45rem;
  border-radius: .3rem;
  background: var(--accent);
  color: var(--accent-ink);
}

.hd-17__ann-link {
  color: var(--accent);
  font-weight: 660;
  text-decoration: underline;
  text-underline-offset: .2em;
}

.hd-17__num {
  font-variant-numeric: tabular-nums;
  font-weight: 660;
}

.hd-17__x {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  flex: none;
  border-radius: 999px;
  color: var(--muted);
  cursor: pointer;
  transition: background-color .16s ease, color .16s ease;
}

.hd-17__x svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.hd-17__x:hover {
  background: var(--accent-soft);
  color: var(--accent);
}

.hd-17:has(#hd-17-close:focus-visible) .hd-17__x {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}
/* ── header: soft neumorphic relief ───────────────────────────────── */

.hd-17__bar {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  gap: clamp(.75rem,3vw,1.5rem);
  padding: .65rem clamp(.85rem,3vw,1.5rem);
  background: var(--panel);
  box-shadow: 0 calc(.5rem * var(--relief)) calc(1.2rem * var(--relief)) calc(-.6rem * var(--relief)) rgba(43,31,22,.28), inset 0 1px 0 rgba(255,255,255,.85), inset 0 -1px 0 rgba(43,31,22,.06);
}

.hd-17__brand {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  color: var(--ink);
  text-decoration: none;
  min-inline-size: 0;
}

.hd-17__mark {
  inline-size: 1.7rem;
  block-size: 1.7rem;
  color: var(--accent);
  flex: none;
}

.hd-17__word {
  font-family: var(--font-display);
  font-size: 1.02rem;
  font-weight: 800;
  letter-spacing: -.01em;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-17__nav {
  min-inline-size: 0;
}

.hd-17__nav ul {
  display: flex;
  align-items: center;
  gap: .1rem;
}

.hd-17__nav a {
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

.hd-17__nav a:hover {
  color: var(--accent);
  background: var(--accent-soft);
}

.hd-17__nav a[aria-current="page"] {
  color: var(--accent);
  font-weight: 660;
}

.hd-17__right {
  display: flex;
  align-items: center;
  gap: .5rem;
  margin-inline-start: auto;
}

.hd-17__quiet {
  color: var(--muted);
  text-decoration: none;
  font-size: .85rem;
  font-weight: 560;
  white-space: nowrap;
}

.hd-17__quiet:hover {
  color: var(--ink);
}

.hd-17__cta {
  display: inline-flex;
  align-items: center;
  gap: .25rem;
  min-block-size: 2.4rem;
  padding: .55rem 1rem;
  border-radius: .6rem;
  background: var(--accent);
  color: var(--accent-ink);
  text-decoration: none;
  font-family: var(--font-display);
  font-size: .84rem;
  font-weight: 700;
  white-space: nowrap;
  box-shadow: 0 .35rem .9rem -.35rem rgba(194,82,26,.7), inset 0 1px 0 rgba(255,255,255,.3);
  transition: translate .15s ease;
}

.hd-17__cta:hover {
  translate: 0 -1px;
}
/* ── page body ────────────────────────────────────────────────────── */

.hd-17__main {
  max-inline-size: 66rem;
  margin-inline: auto;
  padding: clamp(2.25rem,6vw,3.5rem) clamp(1rem,3vw,1.5rem) 4rem;
}

.hd-17__eyebrow {
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.hd-17__main h1 {
  font-family: var(--font-display);
  font-size: clamp(1.8rem,5.5vw,2.9rem);
  line-height: 1.1;
  font-weight: 800;
  letter-spacing: -.025em;
  margin-top: .9rem;
  max-inline-size: 28ch;
  text-wrap: balance;
}

.hd-17__lead {
  margin-top: 1rem;
  max-inline-size: 58ch;
  color: var(--muted);
  font-size: 1rem;
  text-wrap: pretty;
}

.hd-17__lead code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  background: var(--panel2);
  padding: .1rem .3rem;
  border-radius: .25rem;
}

.hd-17__grid {
  display: grid;
  gap: .9rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,14rem),1fr));
  margin-top: 2rem;
}

.hd-17__grid li {
  padding: 1.1rem;
  border-radius: .9rem;
  background: var(--panel);
  min-inline-size: 0;
  box-shadow: 0 .5rem 1.2rem -.7rem rgba(43,31,22,.25), inset 0 1px 0 rgba(255,255,255,.8);
}

.hd-17__g-t {
  font-family: var(--font-display);
  font-size: 1.05rem;
  font-weight: 800;
}

.hd-17__g-d {
  margin-top: .3rem;
  font-size: .86rem;
  color: var(--muted);
  text-wrap: pretty;
}

.hd-17__g-p {
  margin-top: .6rem;
  font-family: var(--font-display);
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  color: var(--accent);
}

.hd-17__filler {
  block-size: 50vh;
}

@media (max-width: 780px) {
  .hd-17__nav {
    display: none;
  }
}

@media (max-width: 520px) {
  .hd-17__quiet {
    display: none;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-17:has(#hd-17-dark:checked) {
  --bg: #1a1410;
  --panel: #221a15;
  --panel2: #2c221b;
  --ink: #f6ece1;
  --muted: #b09a86;
  --line: rgba(246,236,225,.14);
  --accent: #f08b4a;
  --accent-soft: rgba(240,139,74,.16);
  --accent-ink: #2a1206;
  --relief: 1.4;
}

.hd-17:has(#hd-17-dark:checked) .hd-17__bar,
.hd-17:has(#hd-17-dark:checked) .hd-17__grid li {
  box-shadow: 0 .5rem 1.4rem -.7rem rgba(0,0,0,.75), inset 0 1px 0 rgba(255,255,255,.06);
}

.hd-17:has(#hd-17-dark:checked) .hd-17__ann {
  box-shadow: inset 0 -1px 0 rgba(255,255,255,.05);
}
/* icon: shows the scheme the toggle will switch you to */

.hd-17__sun {
  display: none;
}

.hd-17:has(#hd-17-dark:checked) .hd-17__moon {
  display: none;
}

.hd-17:has(#hd-17-dark:checked) .hd-17__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .hd-17:not([data-theme="light"]):not(:has(#hd-17-dark:checked)) {
    --bg: #1a1410;
    --panel: #221a15;
    --panel2: #2c221b;
    --ink: #f6ece1;
    --muted: #b09a86;
    --line: rgba(246,236,225,.14);
    --accent: #f08b4a;
    --accent-soft: rgba(240,139,74,.16);
    --accent-ink: #2a1206;
    --relief: 1.4;
  }

  .hd-17:not([data-theme="light"]):not(:has(#hd-17-dark:checked)) .hd-17__bar,
    .hd-17:not([data-theme="light"]):not(:has(#hd-17-dark:checked)) .hd-17__grid li {
    box-shadow: 0 .5rem 1.4rem -.7rem rgba(0,0,0,.75), inset 0 1px 0 rgba(255,255,255,.06);
  }

  .hd-17:not([data-theme="light"]):not(:has(#hd-17-dark:checked)) .hd-17__ann {
    box-shadow: inset 0 -1px 0 rgba(255,255,255,.05);
  }
  /* FLIP-BACK — dark OS + checked toggle returns to the other scheme */

  .hd-17:has(#hd-17-dark:checked) {
    --bg: #f4ece2;
    --panel: #faf4ec;
    --panel2: #eadfd1;
    --ink: #2b1f16;
    --muted: #7a6553;
    --line: rgba(43,31,22,.14);
    --accent: #c2521a;
    --accent-soft: rgba(194,82,26,.12);
    --accent-ink: #fff8f2;
    --relief: 1;
    --collapse: 320ms;
    --font-display: "Roboto Slab","Rockwell",Georgia,serif;
    --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  }

  .hd-17:has(#hd-17-dark:checked) .hd-17__bar {
    position: sticky;
    top: 0;
    z-index: 30;
    display: flex;
    align-items: center;
    gap: clamp(.75rem,3vw,1.5rem);
    padding: .65rem clamp(.85rem,3vw,1.5rem);
    background: var(--panel);
    box-shadow: 0 calc(.5rem * var(--relief)) calc(1.2rem * var(--relief)) calc(-.6rem * var(--relief)) rgba(43,31,22,.28), inset 0 1px 0 rgba(255,255,255,.85), inset 0 -1px 0 rgba(43,31,22,.06);
  }

  .hd-17:has(#hd-17-dark:checked) .hd-17__grid li {
    padding: 1.1rem;
    border-radius: .9rem;
    background: var(--panel);
    min-inline-size: 0;
    box-shadow: 0 .5rem 1.2rem -.7rem rgba(43,31,22,.25), inset 0 1px 0 rgba(255,255,255,.8);
  }

  .hd-17:has(#hd-17-dark:checked) .hd-17__ann {
    display: grid;
    grid-template-rows: 1fr;
    overflow: hidden;
    background: linear-gradient(180deg, var(--panel2), var(--bg));
    border-bottom: 1px solid var(--line);
    box-shadow: inset 0 -1px 0 rgba(255,255,255,.6);
    transition: grid-template-rows var(--collapse) cubic-bezier(.3,.8,.3,1), opacity var(--collapse) ease;
  }
  /* the icon always offers the scheme you are not in */

  .hd-17:not([data-theme="light"]):not(:has(#hd-17-dark:checked)) .hd-17__moon {
    display: none;
  }

  .hd-17:not([data-theme="light"]):not(:has(#hd-17-dark:checked)) .hd-17__sun {
    display: block;
  }

  .hd-17:has(#hd-17-dark:checked) .hd-17__sun {
    display: none;
  }

  .hd-17:has(#hd-17-dark:checked) .hd-17__moon {
    display: block;
  }
}

.hd-17[data-theme="dark"] {
  --bg: #1a1410;
  --panel: #221a15;
  --panel2: #2c221b;
  --ink: #f6ece1;
  --muted: #b09a86;
  --line: rgba(246,236,225,.14);
  --accent: #f08b4a;
  --accent-soft: rgba(240,139,74,.16);
  --accent-ink: #2a1206;
}

@media (prefers-reduced-motion: reduce) {
  .hd-17 * {
    transition-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-17__ann {
    border-bottom: 1px solid CanvasText;
  }
}
/* ── theme toggle — visually hidden checkbox, zero JS ────────────── */

.hd-17__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-17__theme {
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

.hd-17__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-17__theme:hover {
  background: rgba(128,128,128,.16);
}

.hd-17:has(#hd-17-dark:focus-visible) .hd-17__theme {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```
