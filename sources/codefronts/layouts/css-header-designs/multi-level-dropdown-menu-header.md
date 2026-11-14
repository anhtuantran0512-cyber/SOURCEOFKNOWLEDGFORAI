---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/multi-level-dropdown-menu-header/"
title: "Multi Level Dropdown Menu Header"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "Three levels of nested navigation, opened by hover and by :focus-within, with each level flying out to the side of its parent row."
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi Level Dropdown Menu Header
Source: https://codefronts.com/layouts/css-header-designs/multi-level-dropdown-menu-header/

Three levels of nested navigation, opened by hover and by :focus-within, with each level flying out to the side of its parent row. Sub-panels flip to the opposite side near the viewport edge, every level is a real role="menu" with aria-haspopup triggers, and the whole thing is keyboard-walkable with Tab alone. Ink-and-sand minimal luxury, no shadows.
## HTML
```html
<div class="hd-21">
  <a class="hd-21__skip" href="#hd-21-main">Skip to content</a>

  <header class="hd-21__bar">
    <a class="hd-21__brand" href="#hd-21-main">Aurelio<span>&middot; est. 1974</span></a>

    <nav class="hd-21__nav" aria-label="Main">
      <ul class="hd-21__l1">
        <li>
          <a href="#hd-21-main" aria-haspopup="menu">Collections
            <svg class="hd-21__chev" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M8 10.5 12 14.5l4-4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <ul class="hd-21__p2" role="menu" aria-label="Collections">
            <li>
              <a role="menuitem" href="#hd-21-main" aria-haspopup="menu">Fragrance
                <svg class="hd-21__chev hd-21__chev--side" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M10 7.5l4.5 4.5L10 16.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </a>
              <ul class="hd-21__p3" role="menu" aria-label="Fragrance">
                <li><a role="menuitem" href="#hd-21-main">Eau de parfum</a></li>
                <li><a role="menuitem" href="#hd-21-main">Room sprays</a></li>
                <li><a role="menuitem" href="#hd-21-main">Incense</a></li>
                <li><a role="menuitem" href="#hd-21-main">Discovery set</a></li>
              </ul>
            </li>
            <li>
              <a role="menuitem" href="#hd-21-main" aria-haspopup="menu">Skin
                <svg class="hd-21__chev hd-21__chev--side" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M10 7.5l4.5 4.5L10 16.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </a>
              <ul class="hd-21__p3" role="menu" aria-label="Skin">
                <li><a role="menuitem" href="#hd-21-main">Cleansers</a></li>
                <li><a role="menuitem" href="#hd-21-main">Serums</a></li>
                <li><a role="menuitem" href="#hd-21-main">Balms</a></li>
              </ul>
            </li>
            <li>
              <a role="menuitem" href="#hd-21-main" aria-haspopup="menu">Home
                <svg class="hd-21__chev hd-21__chev--side" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M10 7.5l4.5 4.5L10 16.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </a>
              <ul class="hd-21__p3 hd-21__p3--flip" role="menu" aria-label="Home">
                <li><a role="menuitem" href="#hd-21-main">Candles</a></li>
                <li><a role="menuitem" href="#hd-21-main">Linen care</a></li>
                <li><a role="menuitem" href="#hd-21-main">Glassware</a></li>
              </ul>
            </li>
            <li><a role="menuitem" href="#hd-21-main">Gifting</a></li>
          </ul>
        </li>
        <li>
          <a href="#hd-21-main" aria-haspopup="menu">Stores
            <svg class="hd-21__chev" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M8 10.5 12 14.5l4-4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <ul class="hd-21__p2" role="menu" aria-label="Stores">
            <li><a role="menuitem" href="#hd-21-main">London &middot; Marylebone</a></li>
            <li><a role="menuitem" href="#hd-21-main">Edinburgh &middot; Stockbridge</a></li>
            <li><a role="menuitem" href="#hd-21-main">Dublin &middot; Drury Street</a></li>
            <li><a role="menuitem" href="#hd-21-main">Find a stockist</a></li>
          </ul>
        </li>
        <li><a href="#hd-21-main">Journal</a></li>
        <li><a href="#hd-21-main">About</a></li>
      </ul>
    </nav>

    <div class="hd-21__right">
      <input class="hd-21__sr" type="checkbox" id="hd-21-dark">
      <label class="hd-21__theme" for="hd-21-dark">
        <svg class="hd-21__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <svg class="hd-21__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <span class="hd-21__vh">Switch light or dark theme</span>
      </label>
      <a class="hd-21__quiet" href="#hd-21-main">Search</a>
      <a class="hd-21__quiet" href="#hd-21-main">Account</a>
      <a class="hd-21__bag" href="#hd-21-main">Bag <span>(2)</span></a>
    </div>
  </header>

  <main class="hd-21__main" id="hd-21-main">
    <p class="hd-21__eyebrow">Autumn formulations</p>
    <h1>Three levels deep, and every one reachable with Tab.</h1>
    <p class="hd-21__lead">Open <em>Collections</em>, then <em>Fragrance</em>. The second level flies out to the side; the third does the same, and the branch nearest the edge flips to the other side so nothing renders off-screen.</p>
    <ul class="hd-21__cols">
      <li><p class="hd-21__c-h">Composition</p><p>Bergamot, cedar, a little smoke. Bottled in Kent in batches of four hundred.</p></li>
      <li><p class="hd-21__c-h">Refills</p><p>Every vessel is refillable. Bring it back to a store or post it free.</p></li>
      <li><p class="hd-21__c-h">Care</p><p>Formulated without synthetic fragrance. Patch test, then use sparingly.</p></li>
    </ul>
    <div class="hd-21__filler" aria-hidden="true"></div>
  </main>
</div>
```
## CSS
```css
.hd-21 {
  --paper: #f6f3ec;
  --sand: #e8e1d3;
  --ink: #1d1c18;
  --muted: #6a6559;
  --line: rgba(29,28,24,.18);
  --menu-w: 14rem;
  --font-display: Georgia,"Iowan Old Style","Times New Roman",serif;
  --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.6;
}

@supports (color: oklch(50% .1 200)) {
  .hd-21 {
    --paper: oklch(96% .015 80);
    --sand: oklch(90% .022 80);
    --ink: oklch(20% .012 70);
    --muted: oklch(50% .015 70);
  }
}

.hd-21 * {
  box-sizing: border-box;
}

.hd-21 h1,
.hd-21 p,
.hd-21 ul {
  margin: 0;
  padding: 0;
}

.hd-21 ul {
  list-style: none;
}

.hd-21 [hidden] {
  display: none;
}

.hd-21 :focus-visible {
  outline: 1.5px solid var(--ink);
  outline-offset: 3px;
}

.hd-21__skip {
  position: absolute;
  inset-inline-start: 1rem;
  top: -3rem;
  z-index: 60;
  padding: .5rem .9rem;
  background: var(--ink);
  color: var(--paper);
  font-size: .78rem;
  font-weight: 640;
  text-decoration: none;
  transition: top .18s ease;
}

.hd-21__skip:focus-visible {
  top: 1rem;
}
/* ── header: roomy, no shadow, hairlines only ─────────────────────── */

.hd-21__bar {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  gap: clamp(1rem,4vw,3rem);
  padding: clamp(1rem,3vw,1.6rem) clamp(1.25rem,5vw,3rem);
  background: var(--paper);
  border-bottom: 1px solid var(--line);
}

.hd-21__brand {
  font-family: var(--font-display);
  font-size: 1.35rem;
  font-weight: 400;
  letter-spacing: .02em;
  color: var(--ink);
  text-decoration: none;
  min-inline-size: 0;
  white-space: nowrap;
}

.hd-21__brand span {
  font-family: var(--font-body);
  font-size: .66rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
  margin-inline-start: .4rem;
}

.hd-21__nav {
  min-inline-size: 0;
}

.hd-21__l1 {
  display: flex;
  align-items: center;
  gap: clamp(.75rem,2.5vw,2rem);
}

.hd-21__l1 > li {
  position: relative;
}

.hd-21__l1 > li > a {
  display: inline-flex;
  align-items: center;
  gap: .3rem;
  padding: .5rem 0;
  color: var(--ink);
  text-decoration: none;
  font-size: .74rem;
  font-weight: 640;
  letter-spacing: .16em;
  text-transform: uppercase;
  white-space: nowrap;
  border-bottom: 1px solid transparent;
  transition: border-color .2s ease;
}

.hd-21__l1 > li > a:hover {
  border-bottom-color: var(--ink);
}

.hd-21__chev {
  inline-size: .85rem;
  block-size: .85rem;
  color: var(--muted);
  transition: rotate .2s ease;
}

.hd-21__l1 > li:hover > a .hd-21__chev,
.hd-21__l1 > li:focus-within > a .hd-21__chev {
  rotate: 180deg;
}

.hd-21__chev--side {
  rotate: 0deg !important;
  margin-inline-start: auto;
}

.hd-21__p2,
.hd-21__p3 {
  position: absolute;
  z-index: 40;
  inline-size: var(--menu-w);
  padding: .4rem;
  background: var(--paper);
  border: 1px solid var(--line);
  visibility: hidden;
  opacity: 0;
  translate: 0 -.3rem;
  transition: opacity .18s ease, translate .18s ease, visibility .18s allow-discrete;
}

.hd-21__p2 {
  inset-inline-start: -.4rem;
  top: calc(100% + .8rem);
}

.hd-21__p2 > li {
  position: relative;
}

.hd-21__p3 {
  inset-inline-start: calc(100% - 2px);
  top: -.4rem;
  translate: -.3rem 0;
  background: var(--sand);
}

.hd-21__p3--flip {
  inset-inline-start: auto;
  inset-inline-end: calc(100% - 2px);
  translate: .3rem 0;
}

.hd-21__l1 > li:hover > .hd-21__p2,
.hd-21__l1 > li:focus-within > .hd-21__p2 {
  visibility: visible;
  opacity: 1;
  translate: 0 0;
}

.hd-21__p2 > li:hover > .hd-21__p3,
.hd-21__p2 > li:focus-within > .hd-21__p3 {
  visibility: visible;
  opacity: 1;
  translate: 0 0;
}

.hd-21__p2 a,
.hd-21__p3 a {
  display: flex;
  align-items: center;
  gap: .4rem;
  min-block-size: 2.5rem;
  padding: .45rem .6rem;
  color: var(--ink);
  text-decoration: none;
  font-size: .86rem;
  transition: background-color .15s ease;
}

.hd-21__p2 a:hover {
  background: var(--sand);
}

.hd-21__p3 a:hover {
  background: var(--paper);
}

.hd-21__right {
  display: flex;
  align-items: center;
  gap: clamp(.75rem,2.5vw,1.5rem);
  margin-inline-start: auto;
}

.hd-21__quiet,
.hd-21__bag {
  color: var(--ink);
  text-decoration: none;
  font-size: .72rem;
  font-weight: 640;
  letter-spacing: .14em;
  text-transform: uppercase;
  white-space: nowrap;
  padding-block: .4rem;
  border-bottom: 1px solid transparent;
  transition: border-color .2s ease;
}

.hd-21__quiet:hover,
.hd-21__bag:hover {
  border-bottom-color: var(--ink);
}

.hd-21__bag span {
  font-variant-numeric: tabular-nums;
  color: var(--muted);
}
/* ── page body ────────────────────────────────────────────────────── */

.hd-21__main {
  max-inline-size: 66rem;
  margin-inline: auto;
  padding: clamp(3rem,8vw,5.5rem) clamp(1.25rem,5vw,3rem) 5rem;
}

.hd-21__eyebrow {
  font-size: .7rem;
  font-weight: 640;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--muted);
}

.hd-21__main h1 {
  font-family: var(--font-display);
  font-size: clamp(1.9rem,5.5vw,3.2rem);
  line-height: 1.14;
  font-weight: 400;
  letter-spacing: -.015em;
  margin-top: 1.2rem;
  max-inline-size: 30ch;
  text-wrap: balance;
}

.hd-21__lead {
  margin-top: 1.2rem;
  max-inline-size: 56ch;
  color: var(--muted);
  font-size: 1.04rem;
  text-wrap: pretty;
}

.hd-21__lead em {
  font-family: var(--font-display);
  font-style: italic;
  color: var(--ink);
}

.hd-21__cols {
  display: grid;
  gap: clamp(1.5rem,4vw,3rem);
  grid-template-columns: repeat(auto-fit,minmax(min(100%,15rem),1fr));
  margin-top: clamp(2.5rem,7vw,4rem);
  padding-top: 2rem;
  border-top: 1px solid var(--line);
}

.hd-21__cols li {
  min-inline-size: 0;
}

.hd-21__c-h {
  font-family: var(--font-display);
  font-size: 1.05rem;
  margin-bottom: .5rem;
}

.hd-21__cols p:last-child {
  font-size: .92rem;
  color: var(--muted);
  text-wrap: pretty;
}

.hd-21__filler {
  block-size: 50vh;
}

@media (max-width: 900px) {
  .hd-21__bar {
    flex-wrap: wrap;
    gap: .75rem;
  }

  .hd-21__nav {
    order: 3;
    flex-basis: 100%;
  }

  .hd-21__l1 {
    flex-wrap: wrap;
    gap: .5rem 1.25rem;
  }

  .hd-21__p2,
    .hd-21__p3 {
    position: static;
    inline-size: 100%;
    translate: 0 0;
    border: 0;
    padding: 0 0 0 1rem;
    border-inline-start: 1px solid var(--line);
    background: transparent;
    display: none;
    visibility: visible;
    opacity: 1;
  }

  .hd-21__l1 > li:focus-within > .hd-21__p2,
    .hd-21__p2 > li:focus-within > .hd-21__p3 {
    display: block;
  }

  .hd-21__l1 > li {
    flex-basis: 100%;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-21:has(#hd-21-dark:checked) {
  --paper: #16150f;
  --sand: #221f17;
  --ink: #f2eee1;
  --muted: #a39b88;
  --line: rgba(242,238,225,.2);
}
/* icon: shows the scheme the toggle will switch you to */

.hd-21__sun {
  display: none;
}

.hd-21:has(#hd-21-dark:checked) .hd-21__moon {
  display: none;
}

.hd-21:has(#hd-21-dark:checked) .hd-21__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .hd-21:not([data-theme="light"]):not(:has(#hd-21-dark:checked)) {
    --paper: #16150f;
    --sand: #221f17;
    --ink: #f2eee1;
    --muted: #a39b88;
    --line: rgba(242,238,225,.2);
  }
  /* FLIP-BACK — dark OS + checked toggle returns to the other scheme */

  .hd-21:has(#hd-21-dark:checked) {
    --paper: #f6f3ec;
    --sand: #e8e1d3;
    --ink: #1d1c18;
    --muted: #6a6559;
    --line: rgba(29,28,24,.18);
    --menu-w: 14rem;
    --font-display: Georgia,"Iowan Old Style","Times New Roman",serif;
    --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  }
  /* the icon always offers the scheme you are not in */

  .hd-21:not([data-theme="light"]):not(:has(#hd-21-dark:checked)) .hd-21__moon {
    display: none;
  }

  .hd-21:not([data-theme="light"]):not(:has(#hd-21-dark:checked)) .hd-21__sun {
    display: block;
  }

  .hd-21:has(#hd-21-dark:checked) .hd-21__sun {
    display: none;
  }

  .hd-21:has(#hd-21-dark:checked) .hd-21__moon {
    display: block;
  }
}

.hd-21[data-theme="dark"] {
  --paper: #16150f;
  --sand: #221f17;
  --ink: #f2eee1;
  --muted: #a39b88;
  --line: rgba(242,238,225,.2);
}

@media (prefers-reduced-motion: reduce) {
  .hd-21 * {
    transition-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-21__p2,
    .hd-21__p3 {
    border: 1px solid CanvasText;
    background: Canvas;
  }
}
/* ── theme toggle — visually hidden checkbox, zero JS ────────────── */

.hd-21__sr,
.hd-21__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-21__theme {
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

.hd-21__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-21__theme:hover {
  background: rgba(128,128,128,.16);
}

.hd-21:has(#hd-21-dark:focus-visible) .hd-21__theme {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```
