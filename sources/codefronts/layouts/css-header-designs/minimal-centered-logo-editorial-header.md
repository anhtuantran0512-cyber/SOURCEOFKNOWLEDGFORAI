---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/minimal-centered-logo-editorial-header/"
title: "Minimal Centered Logo Editorial Header"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "A masthead in the newspaper tradition: dateline and section on the left, a serif wordmark dead centre, subscribe and account on the right."
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimal Centered Logo Editorial Header
Source: https://codefronts.com/layouts/css-header-designs/minimal-centered-logo-editorial-header/

A masthead in the newspaper tradition: dateline and section on the left, a serif wordmark dead centre, subscribe and account on the right. The centring is structural rather than optical &mdash; a three-column grid with equal side tracks &mdash; so the wordmark stays exactly centred no matter how long the dateline or the buttons get.
## HTML
```html
<div class="hd-07">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700;900&display=swap">
  <a class="hd-07__skip" href="#hd-07-main">Skip to content</a>

  <header class="hd-07__bar">
    <p class="hd-07__meta">
      <span class="hd-07__date"><time datetime="2026-08-18">Tuesday, 18 August 2026</time></span>
      <span class="hd-07__sep" aria-hidden="true"></span>
      <span>Issue 214</span>
    </p>

    <a class="hd-07__word" href="#hd-07-main">The Ledger</a>

    <div class="hd-07__util">
      <input class="hd-07__sr" type="checkbox" id="hd-07-dark">
      <label class="hd-07__theme" for="hd-07-dark">
        <svg class="hd-07__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <svg class="hd-07__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <span class="hd-07__vh">Switch light or dark theme</span>
      </label>
      <a class="hd-07__sub" href="#hd-07-main">Subscribe</a>
      <a class="hd-07__acct" href="#hd-07-main">Account</a>
    </div>
  </header>

  <nav class="hd-07__sections" aria-label="Sections">
    <ul>
      <li><a href="#hd-07-main" aria-current="page">Markets</a></li>
      <li><a href="#hd-07-main">Policy</a></li>
      <li><a href="#hd-07-main">Technology</a></li>
      <li><a href="#hd-07-main">Culture</a></li>
      <li><a href="#hd-07-main">Letters</a></li>
      <li><a href="#hd-07-main">Archive</a></li>
    </ul>
  </nav>

  <main class="hd-07__main" id="hd-07-main">
    <article>
      <p class="hd-07__kicker">The week in freight</p>
      <h1>Rates cooled in July, and nobody wants to call it a trend</h1>
      <p class="hd-07__standfirst">Spot prices fell for a fourth consecutive week while contract rates held. Two brokers, three carriers and one very tired analyst explain why that combination is stranger than it sounds.</p>
      <p class="hd-07__byline">By Sam Rivera &middot; Photographs by Priya Sharma</p>

      <div class="hd-07__lede">
        <p>The number everyone quoted last Tuesday was a four per cent decline, which sounds like a story until you notice the comparison window ends on a public holiday. Strip the holiday and the decline is closer to one and a half.</p>
        <p>That has not stopped the reading being repeated in three separate industry newsletters, each citing the other. By Thursday it had become a fact with no author, which is the most durable kind.</p>
        <p>Carriers, for their part, describe a market that feels flat rather than falling. Capacity left the market slowly through the spring and has not come back, and the equipment that did return is older and more expensive to run.</p>
        <p>The honest summary is that July was uneventful, and an uneventful month is difficult to write about without inventing a direction for it.</p>
      </div>
    </article>
  </main>
</div>
```
## CSS
```css
.hd-07 {
  --paper: #f7f4ec;
  --paper2: #efe9dc;
  --ink: #141210;
  --muted: #5f574a;
  --rule: rgba(20,18,16,.28);
  --word: clamp(2rem,7vw,3.4rem);
  --font-display: "Playfair Display",Didot,"Times New Roman",serif;
  --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  background-color: var(--paper);
  background-image: radial-gradient(rgba(20,18,16,.055) 1px, transparent 1px);
  background-size: 14px 14px;
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.6;
}

@supports (color: oklch(50% .1 200)) {
  .hd-07 {
    --paper: oklch(96.5% .015 85);
    --paper2: oklch(93% .02 85);
    --ink: oklch(17% .012 60);
    --muted: oklch(47% .015 65);
  }
}

.hd-07 * {
  box-sizing: border-box;
}

.hd-07 h1,
.hd-07 p,
.hd-07 ul {
  margin: 0;
  padding: 0;
}

.hd-07 ul {
  list-style: none;
}

.hd-07 [hidden] {
  display: none;
}

.hd-07 :focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.hd-07__skip {
  position: absolute;
  inset-inline-start: 1rem;
  top: -3rem;
  z-index: 60;
  padding: .5rem .9rem;
  background: var(--ink);
  color: var(--paper);
  font-size: .8rem;
  font-weight: 650;
  text-decoration: none;
  transition: top .18s ease;
}

.hd-07__skip:focus-visible {
  top: .75rem;
}
/* ── masthead: true centre via 1fr auto 1fr ───────────────────────── */

.hd-07__bar {
  position: relative;
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 1rem;
  max-inline-size: 72rem;
  margin-inline: auto;
  padding: clamp(1.5rem,4vw,2.5rem) clamp(1.25rem,4vw,2.5rem) clamp(1rem,2.5vw,1.5rem);
  border-bottom: 2px solid var(--ink);
}

.hd-07__bar::after {
  content: "";
  position: absolute;
  inset-inline: clamp(1.25rem,4vw,2.5rem);
  bottom: -5px;
  block-size: 1px;
  background: var(--rule);
}

.hd-07__meta {
  justify-self: start;
  min-inline-size: 0;
  display: flex;
  align-items: center;
  gap: .6rem;
  flex-wrap: wrap;
  font-size: .74rem;
  font-variant-caps: all-small-caps;
  letter-spacing: .14em;
  color: var(--muted);
  font-weight: 600;
}

.hd-07__sep {
  inline-size: 1.5rem;
  block-size: 1px;
  background: var(--rule);
}

.hd-07__word {
  font-family: var(--font-display);
  font-size: var(--word);
  font-weight: 900;
  line-height: 1;
  letter-spacing: -.02em;
  color: var(--ink);
  text-decoration: none;
  white-space: nowrap;
  font-variation-settings: "opsz" 60;
}

.hd-07__util {
  justify-self: end;
  min-inline-size: 0;
  display: flex;
  align-items: center;
  gap: .5rem;
}

.hd-07__sub,
.hd-07__acct {
  padding: .55rem .95rem;
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  text-decoration: none;
  white-space: nowrap;
  transition: background-color .2s ease, color .2s ease;
}

.hd-07__sub {
  background: var(--ink);
  color: var(--paper);
}

.hd-07__sub:hover {
  background: var(--muted);
}

.hd-07__acct {
  color: var(--ink);
  border: 1px solid var(--rule);
}

.hd-07__acct:hover {
  background: var(--paper2);
}

.hd-07__sections {
  max-inline-size: 72rem;
  margin-inline: auto;
  padding: .9rem clamp(1.25rem,4vw,2.5rem) 0;
}

.hd-07__sections ul {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: clamp(.9rem,3vw,2rem);
}

.hd-07__sections a {
  color: var(--muted);
  text-decoration: none;
  font-size: .74rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  padding-block: .35rem;
  border-bottom: 2px solid transparent;
  transition: color .18s ease, border-color .18s ease;
}

.hd-07__sections a:hover {
  color: var(--ink);
  border-bottom-color: var(--ink);
}

.hd-07__sections a[aria-current="page"] {
  color: var(--ink);
  border-bottom-color: var(--ink);
}
/* ── page body ────────────────────────────────────────────────────── */

.hd-07__main {
  max-inline-size: 72rem;
  margin-inline: auto;
  padding: clamp(2.5rem,7vw,4.5rem) clamp(1.25rem,4vw,2.5rem) 5rem;
}

.hd-07__kicker {
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--muted);
  text-align: center;
}

.hd-07__main h1 {
  font-family: var(--font-display);
  font-size: clamp(2rem,6vw,3.6rem);
  line-height: 1.06;
  font-weight: 700;
  letter-spacing: -.02em;
  text-align: center;
  margin: .8rem auto 0;
  max-inline-size: 34ch;
  text-wrap: balance;
}

.hd-07__standfirst {
  margin: 1.1rem auto 0;
  max-inline-size: 52ch;
  text-align: center;
  color: var(--muted);
  font-size: 1.05rem;
  text-wrap: pretty;
}

.hd-07__byline {
  margin: 1.5rem auto;
  text-align: center;
  font-size: .72rem;
  font-variant-caps: all-small-caps;
  letter-spacing: .16em;
  color: var(--muted);
  font-weight: 650;
  padding-block: .9rem;
  border-block: 1px solid var(--rule);
  max-inline-size: 52ch;
}

.hd-07__lede {
  column-count: 3;
  column-gap: clamp(1.5rem,4vw,2.5rem);
  column-rule: 1px solid var(--rule);
  font-size: 1rem;
  line-height: 1.75;
}

.hd-07__lede p {
  margin-bottom: 1rem;
  text-wrap: pretty;
}

.hd-07__lede p:first-child::first-letter {
  font-family: var(--font-display);
  float: left;
  font-size: 3.4rem;
  line-height: .82;
  font-weight: 700;
  padding-inline-end: .35rem;
  padding-block-start: .15rem;
}

@media (max-width: 900px) {
  .hd-07__lede {
    column-count: 2;
  }
}

@media (max-width: 700px) {
  .hd-07__bar {
    grid-template-columns: minmax(0,1fr);
    justify-items: center;
    text-align: center;
    gap: .9rem;
  }

  .hd-07__meta {
    justify-self: center;
    justify-content: center;
  }

  .hd-07__util {
    justify-self: center;
  }

  .hd-07__lede {
    column-count: 1;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-07:has(#hd-07-dark:checked) {
  --paper: #12100e;
  --paper2: #1b1815;
  --ink: #f5f0e6;
  --muted: #a49a89;
  --rule: rgba(245,240,230,.26);
}

.hd-07:has(#hd-07-dark:checked) {
  background-image: radial-gradient(rgba(245,240,230,.06) 1px, transparent 1px);
}
/* icon: shows the scheme the toggle will switch you to */

.hd-07__sun {
  display: none;
}

.hd-07:has(#hd-07-dark:checked) .hd-07__moon {
  display: none;
}

.hd-07:has(#hd-07-dark:checked) .hd-07__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .hd-07:not([data-theme="light"]):not(:has(#hd-07-dark:checked)):not(:has(#hd-07-dark:checked)) {
    --paper: #12100e;
    --paper2: #1b1815;
    --ink: #f5f0e6;
    --muted: #a49a89;
    --rule: rgba(245,240,230,.26);
  }

  .hd-07:not([data-theme="light"]) {
    background-image: radial-gradient(rgba(245,240,230,.06) 1px, transparent 1px);
  }
  /* FLIP-BACK — dark OS + checked toggle returns to the other scheme */

  .hd-07:has(#hd-07-dark:checked) {
    --paper: #f7f4ec;
    --paper2: #efe9dc;
    --ink: #141210;
    --muted: #5f574a;
    --rule: rgba(20,18,16,.28);
    --word: clamp(2rem,7vw,3.4rem);
    --font-display: "Playfair Display",Didot,"Times New Roman",serif;
    --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  }
  /* the icon always offers the scheme you are not in */

  .hd-07:not([data-theme="light"]):not(:has(#hd-07-dark:checked)) .hd-07__moon {
    display: none;
  }

  .hd-07:not([data-theme="light"]):not(:has(#hd-07-dark:checked)) .hd-07__sun {
    display: block;
  }

  .hd-07:has(#hd-07-dark:checked) .hd-07__sun {
    display: none;
  }

  .hd-07:has(#hd-07-dark:checked) .hd-07__moon {
    display: block;
  }
}

.hd-07[data-theme="dark"] {
  --paper: #12100e;
  --paper2: #1b1815;
  --ink: #f5f0e6;
  --muted: #a49a89;
  --rule: rgba(245,240,230,.26);
  background-image: radial-gradient(rgba(245,240,230,.06) 1px, transparent 1px);
}

@media (prefers-reduced-motion: reduce) {
  .hd-07 * {
    transition-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-07__sub {
    border: 1px solid CanvasText;
  }
}
/* ── theme toggle — visually hidden checkbox, zero JS ────────────── */

.hd-07__sr,
.hd-07__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-07__theme {
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

.hd-07__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-07__theme:hover {
  background: rgba(128,128,128,.16);
}

.hd-07:has(#hd-07-dark:focus-visible) .hd-07__theme {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```
