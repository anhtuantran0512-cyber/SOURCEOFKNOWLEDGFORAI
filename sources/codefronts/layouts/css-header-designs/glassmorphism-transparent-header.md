---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/glassmorphism-transparent-header/"
title: "Glassmorphism Transparent Header Bar"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "A full header surface in glass: backdrop-filter: blur(20px) saturate(180%) over an ambient aurora background, with a thin inner-highlight stroke along the…"
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glassmorphism Transparent Header Bar
Source: https://codefronts.com/layouts/css-header-designs/glassmorphism-transparent-header/

A full header surface in glass: backdrop-filter: blur(20px) saturate(180%) over an ambient aurora background, with a thin inner-highlight stroke along the top edge that sells the material. The solid rgba() fallback is declared first, so browsers without backdrop-filter get an opaque bar that still meets contrast rather than unreadable text over a gradient.
## HTML
```html
<div class="hd-16">
  <a class="hd-16__skip" href="#hd-16-main">Skip to content</a>
  <div class="hd-16__ambient" aria-hidden="true">
    <span class="hd-16__blob hd-16__blob--a"></span>
    <span class="hd-16__blob hd-16__blob--b"></span>
    <span class="hd-16__blob hd-16__blob--c"></span>
  </div>

  <header class="hd-16__bar">
    <a class="hd-16__brand" href="#hd-16-main">
      <span class="hd-16__mark" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" focusable="false"><circle cx="12" cy="12" r="8.6" stroke="currentColor" stroke-width="1.8"/><path d="M12 3.4c3 3.6 3 13.6 0 17.2M3.4 12h17.2" stroke="currentColor" stroke-width="1.3" opacity=".6"/></svg>
      </span>
      <span class="hd-16__word">Aurora</span>
    </a>

    <nav class="hd-16__nav" aria-label="Main">
      <ul>
        <li><a href="#hd-16-main" aria-current="page">Discover</a></li>
        <li><a href="#hd-16-main">Spaces</a></li>
        <li><a href="#hd-16-main">Community</a></li>
        <li><a href="#hd-16-main">Pricing</a></li>
      </ul>
    </nav>

    <label class="hd-16__search" for="hd-16-q">
      <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="11" cy="11" r="6.4" stroke="currentColor" stroke-width="1.8"/><path d="M15.8 15.8 21 21" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>
      <input class="hd-16__q" id="hd-16-q" type="text" placeholder="Search spaces" aria-label="Search spaces">
    </label>

    <div class="hd-16__right">
      <input class="hd-16__sr" type="checkbox" id="hd-16-dark">
      <label class="hd-16__icon hd-16__theme" for="hd-16-dark">
        <svg class="hd-16__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <svg class="hd-16__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <span class="hd-16__vh">Switch light or dark theme</span>
      </label>
      <a class="hd-16__cta" href="#hd-16-main">Join free</a>
    </div>
  </header>

  <main class="hd-16__main" id="hd-16-main">
    <section class="hd-16__hero">
      <p class="hd-16__eyebrow">Shared workspaces</p>
      <h1>A header made of glass, over light that keeps moving.</h1>
      <p class="hd-16__lead">The bar samples the aurora behind it with a 20&nbsp;px blur and 180% saturation, then catches an inner highlight along its top edge. Where <code>backdrop-filter</code> is unsupported it falls back to an opaque surface.</p>
      <div class="hd-16__cards">
        <article class="hd-16__glass"><h2>Rooms</h2><p>Persistent audio spaces with a shared canvas and no meeting links.</p></article>
        <article class="hd-16__glass"><h2>Threads</h2><p>Long-form discussion that does not evaporate when the call ends.</p></article>
        <article class="hd-16__glass"><h2>Library</h2><p>Everything the team has written, searchable in one keystroke.</p></article>
      </div>
    </section>
    <div class="hd-16__filler" aria-hidden="true"></div>
  </main>
</div>
```
## CSS
```css
.hd-16 {
  --bg: #eef1fb;
  --glass: #ffffff;
  --ink: #12142b;
  --muted: #575d80;
  --rim: .55;
  --accent: #5b5bd6;
  --accent2: #e879f9;
  --accent-ink: #ffffff;
  --drift: 22s;
  --font-display: system-ui,-apple-system,"Segoe UI",sans-serif;
  --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  overflow: hidden;
  isolation: isolate;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.55;
}

@supports (color: oklch(50% .1 200)) {
  .hd-16 {
    --bg: oklch(95% .02 275);
    --ink: oklch(20% .05 285);
    --muted: oklch(48% .05 285);
    --accent: oklch(55% .2 285);
    --accent2: oklch(75% .2 330);
  }
}

.hd-16 * {
  box-sizing: border-box;
}

.hd-16 h1,
.hd-16 h2,
.hd-16 p,
.hd-16 ul {
  margin: 0;
  padding: 0;
}

.hd-16 ul {
  list-style: none;
}

.hd-16 [hidden] {
  display: none;
}

.hd-16 :focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
  border-radius: .5rem;
}

.hd-16__skip {
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

.hd-16__skip:focus-visible {
  top: 1rem;
}
/* ── ambient field behind the glass ───────────────────────────────── */

.hd-16__ambient {
  position: absolute;
  inset: 0;
  z-index: -1;
  overflow: hidden;
}

.hd-16__blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  opacity: .75;
}

.hd-16__blob--a {
  inline-size: 38rem;
  block-size: 38rem;
  top: -12rem;
  inset-inline-start: -8rem;
  background: radial-gradient(circle, #7c8cff, transparent 68%);
  animation: hd-16-drift var(--drift) ease-in-out infinite alternate;
}

.hd-16__blob--b {
  inline-size: 32rem;
  block-size: 32rem;
  top: 4rem;
  inset-inline-end: -6rem;
  background: radial-gradient(circle, #f0abfc, transparent 66%);
  animation: hd-16-drift calc(var(--drift) * 1.3) ease-in-out infinite alternate-reverse;
}

.hd-16__blob--c {
  inline-size: 30rem;
  block-size: 30rem;
  bottom: -10rem;
  inset-inline-start: 30%;
  background: radial-gradient(circle, #5eead4, transparent 66%);
  animation: hd-16-drift calc(var(--drift) * 1.6) ease-in-out infinite alternate;
}

@keyframes hd-16-drift {
  from {
    translate: 0 0;
  }

  to {
    translate: 3rem 2rem;
  }
}
/* ── the glass bar: opaque fallback FIRST ─────────────────────────── */

.hd-16__bar {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  gap: clamp(.75rem,2.5vw,1.5rem);
  padding: .85rem clamp(1rem,4vw,2rem);
  background: rgba(255,255,255,.94);
  border-block-end: 1px solid rgba(255,255,255,.35);
  box-shadow: inset 0 1px 0 rgba(255,255,255,var(--rim)), 0 1rem 2.5rem -1.2rem rgba(20,20,50,.35);
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .hd-16__bar {
    background: color-mix(in srgb, var(--glass) 52%, transparent);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    backdrop-filter: blur(20px) saturate(180%);
  }
}

.hd-16__brand {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  color: var(--ink);
  text-decoration: none;
  min-inline-size: 0;
}

.hd-16__mark {
  display: grid;
  place-items: center;
  inline-size: 2rem;
  block-size: 2rem;
  border-radius: .65rem;
  flex: none;
  background: linear-gradient(140deg, var(--accent), var(--accent2));
  color: #fff;
}

.hd-16__mark svg {
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.hd-16__word {
  font-family: var(--font-display);
  font-size: 1.02rem;
  font-weight: 700;
  letter-spacing: -.025em;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-16__nav {
  min-inline-size: 0;
}

.hd-16__nav ul {
  display: flex;
  align-items: center;
  gap: .15rem;
}

.hd-16__nav a {
  display: block;
  padding: .45rem .7rem;
  border-radius: 999px;
  color: var(--muted);
  text-decoration: none;
  font-size: .86rem;
  font-weight: 580;
  white-space: nowrap;
  transition: color .16s ease, background-color .16s ease;
}

.hd-16__nav a:hover {
  color: var(--ink);
  background: rgba(255,255,255,.5);
}

.hd-16__nav a[aria-current="page"] {
  color: var(--ink);
  background: rgba(255,255,255,.62);
}

.hd-16__search {
  display: flex;
  align-items: center;
  gap: .5rem;
  flex: 1;
  min-inline-size: 0;
  max-inline-size: 16rem;
  min-block-size: 2.5rem;
  padding: .4rem .85rem;
  border-radius: 999px;
  background: rgba(255,255,255,.55);
  border: 1px solid rgba(255,255,255,.7);
  cursor: text;
  transition: border-color .16s ease, box-shadow .16s ease;
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .hd-16__search {
    background: rgba(255,255,255,.32);
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
  }
}

.hd-16__search svg {
  inline-size: 1rem;
  block-size: 1rem;
  color: var(--muted);
  flex: none;
}

.hd-16__q {
  flex: 1;
  min-inline-size: 0;
  border: 0;
  background: transparent;
  font: inherit;
  font-size: .86rem;
  color: var(--ink);
}

.hd-16__q::placeholder {
  color: var(--muted);
}

.hd-16__q:focus {
  outline: none;
}

.hd-16__search:focus-within {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px rgba(91,91,214,.2);
}

.hd-16__right {
  display: flex;
  align-items: center;
  gap: .4rem;
  margin-inline-start: auto;
}

.hd-16__icon {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 0;
  border-radius: 999px;
  background: transparent;
  color: var(--muted);
  cursor: pointer;
  transition: background-color .16s ease, color .16s ease;
}

.hd-16__icon svg {
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.hd-16__icon:hover {
  background: rgba(255,255,255,.55);
  color: var(--ink);
}

.hd-16__cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.6rem;
  padding: .65rem 1.15rem;
  border-radius: 999px;
  background: linear-gradient(120deg, var(--accent), var(--accent2));
  color: var(--accent-ink);
  text-decoration: none;
  font-size: .86rem;
  font-weight: 700;
  white-space: nowrap;
  box-shadow: 0 .6rem 1.4rem -.5rem rgba(91,91,214,.65);
  transition: translate .16s ease;
}

.hd-16__cta:hover {
  translate: 0 -1px;
}
/* ── page body ────────────────────────────────────────────────────── */

.hd-16__main {
  position: relative;
  max-inline-size: 70rem;
  margin-inline: auto;
  padding: clamp(2.5rem,8vw,5rem) clamp(1.25rem,4vw,2rem) 5rem;
}

.hd-16__eyebrow {
  font-size: .74rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.hd-16__hero h1 {
  font-family: var(--font-display);
  font-size: clamp(2rem,6.5vw,3.6rem);
  line-height: 1.05;
  font-weight: 700;
  letter-spacing: -.035em;
  margin-top: 1rem;
  max-inline-size: 26ch;
  text-wrap: balance;
}

.hd-16__lead {
  margin-top: 1.1rem;
  max-inline-size: 56ch;
  color: var(--muted);
  font-size: 1.04rem;
  text-wrap: pretty;
}

.hd-16__lead code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
}

.hd-16__cards {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,15rem),1fr));
  margin-top: clamp(2rem,6vw,3rem);
}

.hd-16__glass {
  padding: 1.25rem;
  border-radius: 1.1rem;
  min-inline-size: 0;
  background: rgba(255,255,255,.62);
  border: 1px solid rgba(255,255,255,.75);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.7), 0 1.2rem 2.5rem -1.4rem rgba(20,20,50,.4);
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .hd-16__glass {
    background: rgba(255,255,255,.38);
    -webkit-backdrop-filter: blur(14px) saturate(160%);
    backdrop-filter: blur(14px) saturate(160%);
  }
}

.hd-16__glass h2 {
  font-family: var(--font-display);
  font-size: 1.05rem;
  font-weight: 680;
  letter-spacing: -.02em;
}

.hd-16__glass p {
  margin-top: .4rem;
  font-size: .88rem;
  color: var(--muted);
  text-wrap: pretty;
}

.hd-16__filler {
  block-size: 55vh;
}

@media (max-width: 900px) {
  .hd-16__search {
    display: none;
  }
}

@media (max-width: 760px) {
  .hd-16__nav {
    display: none;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-16:has(#hd-16-dark:checked) {
  --bg: #0a0b16;
  --glass: #2a2d52;
  --ink: #f0f1fb;
  --muted: #a7abd0;
  --rim: .22;
  --accent: #a5b4fc;
  --accent2: #f0abfc;
  --accent-ink: #151633;
}

.hd-16:has(#hd-16-dark:checked) .hd-16__bar {
  background: rgba(16,18,38,.94);
  border-block-end-color: rgba(255,255,255,.14);
}

.hd-16:has(#hd-16-dark:checked) .hd-16__nav a:hover,
.hd-16:has(#hd-16-dark:checked) .hd-16__nav a[aria-current="page"],
.hd-16:has(#hd-16-dark:checked) .hd-16__icon:hover {
  background: rgba(255,255,255,.12);
}

.hd-16:has(#hd-16-dark:checked) .hd-16__search {
  background: rgba(255,255,255,.1);
  border-color: rgba(255,255,255,.18);
}

.hd-16:has(#hd-16-dark:checked) .hd-16__glass {
  background: rgba(255,255,255,.08);
  border-color: rgba(255,255,255,.16);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.18), 0 1.2rem 2.5rem -1.4rem rgba(0,0,0,.8);
}
/* icon: shows the scheme the toggle will switch you to */

.hd-16__sun {
  display: none;
}

.hd-16:has(#hd-16-dark:checked) .hd-16__moon {
  display: none;
}

.hd-16:has(#hd-16-dark:checked) .hd-16__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .hd-16:not([data-theme="light"]):not(:has(#hd-16-dark:checked)) {
    --bg: #0a0b16;
    --glass: #2a2d52;
    --ink: #f0f1fb;
    --muted: #a7abd0;
    --rim: .22;
    --accent: #a5b4fc;
    --accent2: #f0abfc;
    --accent-ink: #151633;
  }

  .hd-16:not([data-theme="light"]):not(:has(#hd-16-dark:checked)) .hd-16__bar {
    background: rgba(16,18,38,.94);
    border-block-end-color: rgba(255,255,255,.14);
  }

  .hd-16:not([data-theme="light"]):not(:has(#hd-16-dark:checked)) .hd-16__nav a:hover,
    .hd-16:not([data-theme="light"]):not(:has(#hd-16-dark:checked)) .hd-16__nav a[aria-current="page"],
    .hd-16:not([data-theme="light"]):not(:has(#hd-16-dark:checked)) .hd-16__icon:hover {
    background: rgba(255,255,255,.12);
  }

  .hd-16:not([data-theme="light"]):not(:has(#hd-16-dark:checked)) .hd-16__search {
    background: rgba(255,255,255,.1);
    border-color: rgba(255,255,255,.18);
  }

  .hd-16:not([data-theme="light"]):not(:has(#hd-16-dark:checked)) .hd-16__glass {
    background: rgba(255,255,255,.08);
    border-color: rgba(255,255,255,.16);
    box-shadow: inset 0 1px 0 rgba(255,255,255,.18), 0 1.2rem 2.5rem -1.4rem rgba(0,0,0,.8);
  }

  @supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
    .hd-16:not([data-theme="light"]) .hd-16__bar {
      background: rgba(16,18,38,.5);
    }
  }
  /* FLIP-BACK — dark OS + checked toggle returns to the other scheme */

  .hd-16:has(#hd-16-dark:checked) {
    --bg: #eef1fb;
    --glass: #ffffff;
    --ink: #12142b;
    --muted: #575d80;
    --rim: .55;
    --accent: #5b5bd6;
    --accent2: #e879f9;
    --accent-ink: #ffffff;
    --drift: 22s;
    --font-display: system-ui,-apple-system,"Segoe UI",sans-serif;
    --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  }

  .hd-16:has(#hd-16-dark:checked) .hd-16__bar {
    position: sticky;
    top: 0;
    z-index: 30;
    display: flex;
    align-items: center;
    gap: clamp(.75rem,2.5vw,1.5rem);
    padding: .85rem clamp(1rem,4vw,2rem);
    background: rgba(255,255,255,.94);
    border-block-end: 1px solid rgba(255,255,255,.35);
    box-shadow: inset 0 1px 0 rgba(255,255,255,var(--rim)), 0 1rem 2.5rem -1.2rem rgba(20,20,50,.35);
  }

  .hd-16:has(#hd-16-dark:checked) .hd-16__nav a:hover {
    color: var(--ink);
    background: rgba(255,255,255,.5);
  }

  .hd-16:has(#hd-16-dark:checked) .hd-16__nav a[aria-current="page"] {
    color: var(--ink);
    background: rgba(255,255,255,.62);
  }

  .hd-16:has(#hd-16-dark:checked) .hd-16__icon:hover {
    background: rgba(255,255,255,.55);
    color: var(--ink);
  }

  .hd-16:has(#hd-16-dark:checked) .hd-16__search {
    display: flex;
    align-items: center;
    gap: .5rem;
    flex: 1;
    min-inline-size: 0;
    max-inline-size: 16rem;
    min-block-size: 2.5rem;
    padding: .4rem .85rem;
    border-radius: 999px;
    background: rgba(255,255,255,.55);
    border: 1px solid rgba(255,255,255,.7);
    cursor: text;
    transition: border-color .16s ease, box-shadow .16s ease;
  }

  .hd-16:has(#hd-16-dark:checked) .hd-16__glass {
    padding: 1.25rem;
    border-radius: 1.1rem;
    min-inline-size: 0;
    background: rgba(255,255,255,.62);
    border: 1px solid rgba(255,255,255,.75);
    box-shadow: inset 0 1px 0 rgba(255,255,255,.7), 0 1.2rem 2.5rem -1.4rem rgba(20,20,50,.4);
  }
  /* the icon always offers the scheme you are not in */

  .hd-16:not([data-theme="light"]):not(:has(#hd-16-dark:checked)) .hd-16__moon {
    display: none;
  }

  .hd-16:not([data-theme="light"]):not(:has(#hd-16-dark:checked)) .hd-16__sun {
    display: block;
  }

  .hd-16:has(#hd-16-dark:checked) .hd-16__sun {
    display: none;
  }

  .hd-16:has(#hd-16-dark:checked) .hd-16__moon {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hd-16__blob {
    animation: none !important;
  }

  .hd-16 * {
    transition-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-16__bar {
    background: Canvas;
    border-block-end: 1px solid CanvasText;
  }
}
/* ── theme toggle — visually hidden checkbox, zero JS ────────────── */

.hd-16__sr,
.hd-16__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-16__theme {
  cursor: pointer;
}

.hd-16:has(#hd-16-dark:focus-visible) .hd-16__theme {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```
