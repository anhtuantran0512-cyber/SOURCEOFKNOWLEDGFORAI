---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/transparent-over-hero-landing-page-header/"
title: "Transparent Over Hero Landing Page Header"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "The landing-page classic done without a scroll listener: the header floats transparent over a full-bleed hero photograph, then solidifies into an opaque bar…"
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Transparent Over Hero Landing Page Header
Source: https://codefronts.com/layouts/css-header-designs/transparent-over-hero-landing-page-header/

The landing-page classic done without a scroll listener: the header floats transparent over a full-bleed hero photograph, then solidifies into an opaque bar with dark ink as the reader passes 60&nbsp;px. Nav text over the photo carries a drop shadow and a gradient scrim for contrast, and a checkbox-driven theme pill flips the whole surface with zero theme JavaScript.
## HTML
```html
<div class="hd-08">
  <a class="hd-08__skip" href="#hd-08-main">Skip to content</a>

  <header class="hd-08__bar">
    <a class="hd-08__brand" href="#hd-08-main">
      <svg class="hd-08__mark" viewBox="0 0 26 26" fill="none" aria-hidden="true" focusable="false">
        <path d="M13 2.5 3.5 13 13 23.5 22.5 13 13 2.5Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/>
        <path d="M13 8.5 8.5 13l4.5 4.5L17.5 13 13 8.5Z" fill="currentColor"/>
      </svg>
      <span class="hd-08__word">Wayfare</span>
    </a>

    <nav class="hd-08__nav" aria-label="Main">
      <ul>
        <li><a href="#hd-08-main">Stays</a></li>
        <li><a href="#hd-08-main">Routes</a></li>
        <li><a href="#hd-08-main">Guides</a></li>
        <li><a href="#hd-08-main">Hosts</a></li>
      </ul>
    </nav>

    <div class="hd-08__right">
      <input class="hd-08__sr" type="checkbox" id="hd-08-dark">
      <label class="hd-08__theme" for="hd-08-dark">
        <svg class="hd-08__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <svg class="hd-08__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <span class="hd-08__vh">Switch light or dark theme</span>
      </label>
      <a class="hd-08__cta" href="#hd-08-main">Plan a trip</a>
    </div>
  </header>

  <main id="hd-08-main">
    <section class="hd-08__hero">
      <img class="hd-08__shot" src="https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&amp;fit=crop&amp;w=1600&amp;q=70" alt="Mountain valley at dusk with a single road running through it" width="1600" height="900">
      <div class="hd-08__scrim" aria-hidden="true"></div>
      <div class="hd-08__hero-in">
        <p class="hd-08__eyebrow">Late season &middot; Dolomites</p>
        <h1>Six days of altitude and very good bread.</h1>
        <p class="hd-08__lead">Start scrolling: the header lifts off the photograph and settles into a solid bar, driven by the page's own scroll progress rather than a listener.</p>
        <div class="hd-08__hero-cta">
          <a class="hd-08__cta hd-08__cta--big" href="#hd-08-main">See the route</a>
          <a class="hd-08__ghost" href="#hd-08-main">12 stays from &euro;96</a>
        </div>
      </div>
    </section>

    <section class="hd-08__body">
      <ul class="hd-08__cards">
        <li><p class="hd-08__c-k">Stage 01</p><h2>Bolzano to Ortisei</h2><p>34&nbsp;km on the valley floor, then the first real climb after lunch.</p></li>
        <li><p class="hd-08__c-k">Stage 02</p><h2>Alpe di Siusi</h2><p>A high plateau day. Thin air, no traffic, one refuge with a working oven.</p></li>
        <li><p class="hd-08__c-k">Stage 03</p><h2>Passo Gardena</h2><p>The pass everyone photographs, ridden early enough to have it alone.</p></li>
        <li><p class="hd-08__c-k">Stage 04</p><h2>Corvara rest</h2><p>Half a day off. The other half is spent eating and lying about gradients.</p></li>
      </ul>
      <div class="hd-08__filler" aria-hidden="true"></div>
    </section>
  </main>
</div>
```
## CSS
```css
.hd-08 {
  --surface: #0e1013;
  --surface2: #171a1f;
  --ink: #f2f4f7;
  --muted: #a7b0bd;
  --line: rgba(242,244,247,.14);
  --accent: #f5b942;
  --accent-ink: #241802;
  --scrim: .55;
  --font-display: system-ui,-apple-system,"Segoe UI",sans-serif;
  --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  background: var(--surface);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.55;
}

@supports (color: oklch(50% .1 200)) {
  .hd-08 {
    --surface: oklch(17% .008 250);
    --surface2: oklch(22% .01 250);
    --ink: oklch(96% .005 250);
    --muted: oklch(74% .02 250);
    --accent: oklch(82% .14 78);
  }
}

.hd-08 * {
  box-sizing: border-box;
}

.hd-08 h1,
.hd-08 h2,
.hd-08 p,
.hd-08 ul {
  margin: 0;
  padding: 0;
}

.hd-08 ul {
  list-style: none;
}

.hd-08 [hidden] {
  display: none;
}

.hd-08 :focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
  border-radius: .4rem;
}

.hd-08__vh,
.hd-08__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-08__skip {
  position: absolute;
  inset-inline-start: 1rem;
  top: -3rem;
  z-index: 60;
  padding: .55rem 1rem;
  border-radius: .5rem;
  background: var(--accent);
  color: var(--accent-ink);
  font-size: .82rem;
  font-weight: 700;
  text-decoration: none;
  transition: top .18s ease;
}

.hd-08__skip:focus-visible {
  top: 1rem;
}
/* ── header: solid + legible is the resting state (the fallback) ──── */

.hd-08__bar {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  gap: clamp(.75rem,3vw,2rem);
  padding: .9rem clamp(1rem,4vw,2.25rem);
  background: color-mix(in srgb, var(--surface) 92%, transparent);
  border-bottom: 1px solid var(--line);
  color: var(--ink);
  backdrop-filter: blur(14px);
}

.hd-08__brand {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  color: inherit;
  text-decoration: none;
  min-inline-size: 0;
}

.hd-08__mark {
  inline-size: 1.6rem;
  block-size: 1.6rem;
  color: var(--accent);
  flex: none;
}

.hd-08__word {
  font-family: var(--font-display);
  font-size: .9rem;
  font-weight: 700;
  letter-spacing: .22em;
  text-transform: uppercase;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-08__nav {
  min-inline-size: 0;
}

.hd-08__nav ul {
  display: flex;
  align-items: center;
  gap: clamp(.7rem,2.5vw,1.6rem);
}

.hd-08__nav a {
  color: inherit;
  text-decoration: none;
  font-size: .78rem;
  font-weight: 640;
  letter-spacing: .13em;
  text-transform: uppercase;
  white-space: nowrap;
  padding-block: .45rem;
  opacity: .85;
  border-bottom: 1px solid transparent;
  transition: opacity .18s ease, border-color .18s ease;
}

.hd-08__nav a:hover {
  opacity: 1;
  border-bottom-color: var(--accent);
}

.hd-08__right {
  display: flex;
  align-items: center;
  gap: .5rem;
  margin-inline-start: auto;
}

.hd-08__theme {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 999px;
  color: inherit;
  cursor: pointer;
  transition: background-color .18s ease;
}

.hd-08__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-08__theme:hover {
  background: rgba(255,255,255,.12);
}

.hd-08:has(#hd-08-dark:focus-visible) .hd-08__theme {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.hd-08__cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: .65rem 1.15rem;
  border-radius: 999px;
  background: var(--accent);
  color: var(--accent-ink);
  text-decoration: none;
  font-size: .78rem;
  font-weight: 750;
  letter-spacing: .1em;
  text-transform: uppercase;
  white-space: nowrap;
  transition: translate .18s ease;
}

.hd-08__cta:hover {
  translate: 0 -1px;
}

@supports (animation-timeline: scroll()) {
  .hd-08__bar {
    animation: hd-08-solid linear both;
    animation-timeline: scroll(root);
    animation-range: 60px 170px;
  }

  @keyframes hd-08-solid {
    from {
      background: transparent;
      border-bottom-color: transparent;
      color: #ffffff;
      text-shadow: 0 1px 14px rgba(0,0,0,.6);
      backdrop-filter: blur(0px);
    }

    to {
      background: color-mix(in srgb, var(--surface) 92%, transparent);
      border-bottom-color: var(--line);
      color: var(--ink);
      text-shadow: none;
      backdrop-filter: blur(14px);
    }
  }
}
/* ── hero ─────────────────────────────────────────────────────────── */

.hd-08__hero {
  position: relative;
  isolation: isolate;
  min-block-size: min(82vh,44rem);
  display: grid;
  align-items: end;
}

.hd-08__shot {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  z-index: -2;
  background: linear-gradient(160deg,#2b3a4a,#111820);
}

.hd-08__scrim {
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(180deg, rgba(6,8,11,var(--scrim)) 0%, rgba(6,8,11,.25) 38%, rgba(6,8,11,.82) 100%);
}

.hd-08__hero-in {
  max-inline-size: 70rem;
  margin-inline: auto;
  inline-size: 100%;
  padding: clamp(2.5rem,8vw,5rem) clamp(1.25rem,4vw,2.25rem);
}

.hd-08__eyebrow {
  font-size: .74rem;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--accent);
}

.hd-08__hero h1 {
  font-family: var(--font-display);
  font-size: clamp(2.2rem,7vw,4.2rem);
  line-height: 1.03;
  font-weight: 700;
  letter-spacing: -.035em;
  margin-top: 1rem;
  max-inline-size: 24ch;
  color: #fff;
  text-shadow: 0 2px 30px rgba(0,0,0,.5);
  text-wrap: balance;
}

.hd-08__lead {
  margin-top: 1.1rem;
  max-inline-size: 48ch;
  color: rgba(255,255,255,.86);
  font-size: 1.05rem;
  text-shadow: 0 1px 16px rgba(0,0,0,.5);
  text-wrap: pretty;
}

.hd-08__hero-cta {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .75rem;
  margin-top: 1.75rem;
}

.hd-08__cta--big {
  padding: .85rem 1.5rem;
  font-size: .82rem;
}

.hd-08__ghost {
  color: #fff;
  text-decoration: none;
  font-size: .82rem;
  font-weight: 600;
  padding: .85rem .5rem;
  border-bottom: 1px solid rgba(255,255,255,.5);
  transition: border-color .18s ease;
}

.hd-08__ghost:hover {
  border-bottom-color: var(--accent);
}

.hd-08__body {
  max-inline-size: 70rem;
  margin-inline: auto;
  padding: clamp(2.5rem,7vw,4.5rem) clamp(1.25rem,4vw,2.25rem) 5rem;
}

.hd-08__cards {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,15rem),1fr));
}

.hd-08__cards li {
  padding: 1.25rem;
  border-radius: 1rem;
  background: var(--surface2);
  border: 1px solid var(--line);
  min-inline-size: 0;
}

.hd-08__c-k {
  font-size: .7rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.hd-08__cards h2 {
  font-family: var(--font-display);
  font-size: 1.05rem;
  font-weight: 660;
  letter-spacing: -.015em;
  margin-top: .5rem;
}

.hd-08__cards p:last-child {
  margin-top: .4rem;
  font-size: .88rem;
  color: var(--muted);
  text-wrap: pretty;
}

.hd-08__filler {
  block-size: 55vh;
}

@media (max-width: 820px) {
  .hd-08__nav {
    display: none;
  }
}

@media (max-width: 480px) {
  .hd-08__cta {
    padding: .6rem .9rem;
    font-size: .72rem;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-08:has(#hd-08-dark:checked) {
  --surface: #0e1013;
  --surface2: #171a1f;
  --ink: #f2f4f7;
  --muted: #a7b0bd;
  --line: rgba(242,244,247,.14);
  --accent: #f5b942;
  --accent-ink: #241802;
}
/* icon: shows the scheme the toggle will switch you to */

.hd-08__moon {
  display: none;
}

.hd-08:has(#hd-08-dark:checked) .hd-08__sun {
  display: none;
}

.hd-08:has(#hd-08-dark:checked) .hd-08__moon {
  display: block;
}

@media (prefers-color-scheme: light) {
  /* light is the OS default here — dark-first demo, so flip the tokens */

  .hd-08:not([data-theme="dark"]):not(:has(#hd-08-dark:checked)) {
    --surface: #ffffff;
    --surface2: #f4f6f8;
    --ink: #111418;
    --muted: #5b6572;
    --line: rgba(17,20,24,.12);
    --accent: #a8620a;
    --accent-ink: #fffaf0;
    --scrim: .45;
  }
  /* FLIP-BACK — light OS + checked toggle restores the full dark set */

  .hd-08:has(#hd-08-dark:checked) {
    --surface: #0e1013;
    --surface2: #171a1f;
    --ink: #f2f4f7;
    --muted: #a7b0bd;
    --line: rgba(242,244,247,.14);
    --accent: #f5b942;
    --accent-ink: #241802;
    --scrim: .55;
  }
  /* the icon always offers the scheme you are not in */

  .hd-08:not([data-theme="dark"]):not(:has(#hd-08-dark:checked)) .hd-08__sun {
    display: none;
  }

  .hd-08:not([data-theme="dark"]):not(:has(#hd-08-dark:checked)) .hd-08__moon {
    display: block;
  }

  .hd-08:has(#hd-08-dark:checked) .hd-08__moon {
    display: none;
  }

  .hd-08:has(#hd-08-dark:checked) .hd-08__sun {
    display: block;
  }
}

.hd-08[data-theme="dark"] {
  --surface: #0e1013;
  --surface2: #171a1f;
  --ink: #f2f4f7;
  --muted: #a7b0bd;
  --line: rgba(242,244,247,.14);
  --accent: #f5b942;
  --accent-ink: #241802;
}

@media (prefers-reduced-motion: reduce) {
  .hd-08__bar {
    animation: none !important;
  }

  .hd-08 * {
    transition-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-08__bar {
    border-bottom: 1px solid CanvasText;
  }
}
```
