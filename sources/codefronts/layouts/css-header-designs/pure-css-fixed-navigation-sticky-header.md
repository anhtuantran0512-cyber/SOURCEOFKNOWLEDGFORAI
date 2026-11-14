---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/pure-css-fixed-navigation-sticky-header/"
title: "Pure CSS Sticky Header with Scroll Timeline"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "The reference sticky header, rebuilt: it starts fully transparent over the page and gains its surface, blur and gradient rim as the reader passes the first…"
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Sticky Header with Scroll Timeline
Source: https://codefronts.com/layouts/css-header-designs/pure-css-fixed-navigation-sticky-header/

The reference sticky header, rebuilt: it starts fully transparent over the page and gains its surface, blur and gradient rim as the reader passes the first 80&nbsp;px. Everything is position: sticky plus animation-timeline: scroll(root) &mdash; no listeners, no position: fixed, no layout shift &mdash; and browsers without scroll timelines get the solid bar from the first pixel.
## HTML
```html
<div class="hd-12">
  <a class="hd-12__skip" href="#hd-12-main">Skip to content</a>

  <header class="hd-12__bar">
    <a class="hd-12__brand" href="#hd-12-main">
      <svg class="hd-12__mark" viewBox="0 0 26 26" fill="none" aria-hidden="true" focusable="false">
        <circle cx="13" cy="13" r="9.6" stroke="currentColor" stroke-width="1.7"/>
        <path d="M13 3.4v19.2M3.4 13h19.2" stroke="currentColor" stroke-width="1.3" opacity=".55"/>
      </svg>
      <span class="hd-12__word">Orbital</span>
    </a>

    <nav class="hd-12__nav" aria-label="Main">
      <ul>
        <li><a href="#hd-12-main" aria-current="page">Overview</a></li>
        <li><a href="#hd-12-s2">Regions</a></li>
        <li><a href="#hd-12-s3">Pricing</a></li>
        <li><a href="#hd-12-s4">Docs</a></li>
      </ul>
    </nav>

    <div class="hd-12__right">
      <input class="hd-12__sr" type="checkbox" id="hd-12-light">
      <label class="hd-12__theme" for="hd-12-light">
        <svg class="hd-12__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <svg class="hd-12__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <span class="hd-12__vh">Switch light or dark theme</span>
      </label>
      <a class="hd-12__link" href="#hd-12-main">Sign in</a>
      <a class="hd-12__cta" href="#hd-12-main">Deploy free</a>
    </div>
  </header>

  <main class="hd-12__main" id="hd-12-main">
    <section class="hd-12__hero">
      <p class="hd-12__eyebrow">Edge compute</p>
      <h1>Nothing sticks like a header that stays in flow.</h1>
      <p class="hd-12__lead">Scroll: the bar picks up its surface, its blur and a thin iridescent rim across the first 80 pixels, then holds. No scroll listener exists on this page.</p>
    </section>

    <section class="hd-12__sec" id="hd-12-s2">
      <h2>Regions</h2>
      <ul class="hd-12__grid">
        <li><p class="hd-12__g-k">eu-west</p><p class="hd-12__g-v">Dublin</p><p class="hd-12__g-d">24 ms median</p></li>
        <li><p class="hd-12__g-k">eu-central</p><p class="hd-12__g-v">Frankfurt</p><p class="hd-12__g-d">31 ms median</p></li>
        <li><p class="hd-12__g-k">us-east</p><p class="hd-12__g-v">Ashburn</p><p class="hd-12__g-d">18 ms median</p></li>
        <li><p class="hd-12__g-k">ap-south</p><p class="hd-12__g-v">Singapore</p><p class="hd-12__g-d">42 ms median</p></li>
      </ul>
    </section>

    <section class="hd-12__sec" id="hd-12-s3">
      <h2>Pricing</h2>
      <p class="hd-12__p">Metered per request with a flat regional egress rate. The first 5 million requests each month are free, which covers most side projects for their entire life.</p>
    </section>

    <section class="hd-12__sec" id="hd-12-s4">
      <h2>Docs</h2>
      <p class="hd-12__p">Anchor links in the nav jump to these sections. Because the root sets <code>scroll-padding-block-start</code>, the heading lands below the sticky bar instead of underneath it.</p>
    </section>
    <div class="hd-12__filler" aria-hidden="true"></div>
  </main>
</div>
```
## CSS
```css
.hd-12 {
  --surface: #0f1115;
  --surface2: #171a21;
  --ink: #eef0f5;
  --muted: #98a0b0;
  --line: rgba(238,240,245,.12);
  --accent: #22d3ee;
  --accent2: #a78bfa;
  --accent-ink: #04222a;
  --font-display: system-ui,-apple-system,"Segoe UI",sans-serif;
  --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  scroll-padding-block-start: 5rem;
  background: radial-gradient(60rem 30rem at 12% -10%, rgba(34,211,238,.12), transparent 60%), radial-gradient(50rem 26rem at 88% 8%, rgba(167,139,250,.12), transparent 62%), var(--surface);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.55;
}

@supports (color: oklch(50% .1 200)) {
  .hd-12 {
    --surface: oklch(17% .012 265);
    --surface2: oklch(21% .014 265);
    --ink: oklch(96% .006 265);
    --muted: oklch(72% .02 265);
    --accent: oklch(80% .13 200);
    --accent2: oklch(76% .16 300);
  }
}

.hd-12 * {
  box-sizing: border-box;
}

.hd-12 h1,
.hd-12 h2,
.hd-12 p,
.hd-12 ul {
  margin: 0;
  padding: 0;
}

.hd-12 ul {
  list-style: none;
}

.hd-12 [hidden] {
  display: none;
}

.hd-12 :focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
  border-radius: .4rem;
}

.hd-12__skip {
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

.hd-12__skip:focus-visible {
  top: 1rem;
}
/* ── header: finished glass state IS the fallback ─────────────────── */

.hd-12__bar {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  gap: clamp(.75rem,3vw,2rem);
  padding: .85rem clamp(1rem,4vw,2.25rem);
  background: color-mix(in srgb, var(--surface) 82%, transparent);
  backdrop-filter: blur(16px) saturate(160%);
  border-bottom: 1px solid var(--line);
}

.hd-12__brand {
  display: inline-flex;
  align-items: center;
  gap: .55rem;
  color: var(--ink);
  text-decoration: none;
  min-inline-size: 0;
}

.hd-12__mark {
  inline-size: 1.55rem;
  block-size: 1.55rem;
  color: var(--accent);
  flex: none;
}

.hd-12__word {
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 680;
  letter-spacing: -.025em;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-12__nav {
  min-inline-size: 0;
}

.hd-12__nav ul {
  display: flex;
  align-items: center;
  gap: .15rem;
}

.hd-12__nav a {
  display: block;
  padding: .45rem .7rem;
  border-radius: .5rem;
  color: var(--muted);
  text-decoration: none;
  font-size: .86rem;
  font-weight: 540;
  white-space: nowrap;
  transition: color .15s ease, background-color .15s ease;
}

.hd-12__nav a:hover {
  color: var(--ink);
  background: rgba(255,255,255,.07);
}

.hd-12__nav a[aria-current="page"] {
  color: var(--ink);
}

.hd-12__right {
  display: flex;
  align-items: center;
  gap: .6rem;
  margin-inline-start: auto;
}

.hd-12__link {
  color: var(--muted);
  text-decoration: none;
  font-size: .86rem;
  font-weight: 560;
  white-space: nowrap;
}

.hd-12__link:hover {
  color: var(--ink);
}

.hd-12__cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.6rem;
  padding: .6rem 1.05rem;
  border-radius: .55rem;
  background: linear-gradient(120deg, var(--accent), var(--accent2));
  color: var(--accent-ink);
  text-decoration: none;
  font-size: .85rem;
  font-weight: 700;
  white-space: nowrap;
  transition: translate .16s ease, filter .16s ease;
}

.hd-12__cta:hover {
  translate: 0 -1px;
  filter: brightness(1.08);
}

@supports (animation-timeline: scroll()) {
  .hd-12__bar {
    animation: hd-12-glass linear both;
    animation-timeline: scroll(root);
    animation-range: 0 80px;
    border-block-end: 1px solid transparent;
    border-image: linear-gradient(90deg, transparent, var(--accent), var(--accent2), transparent) 1;
  }

  @keyframes hd-12-glass {
    from {
      background: transparent;
      backdrop-filter: blur(0px) saturate(100%);
      border-image: linear-gradient(90deg, transparent, transparent) 1;
    }

    to {
      background: color-mix(in srgb, var(--surface) 82%, transparent);
      backdrop-filter: blur(16px) saturate(160%);
      border-image: linear-gradient(90deg, transparent, var(--accent), var(--accent2), transparent) 1;
    }
  }
}
/* ── page body ────────────────────────────────────────────────────── */

.hd-12__main {
  max-inline-size: 68rem;
  margin-inline: auto;
  padding: clamp(2.5rem,8vw,5rem) clamp(1.25rem,4vw,2.25rem) 5rem;
}

.hd-12__eyebrow {
  font-size: .74rem;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--accent);
}

.hd-12__hero h1 {
  font-family: var(--font-display);
  font-size: clamp(2rem,6.5vw,3.6rem);
  line-height: 1.04;
  font-weight: 700;
  letter-spacing: -.04em;
  margin-top: 1rem;
  max-inline-size: 26ch;
  text-wrap: balance;
}

.hd-12__lead {
  margin-top: 1.1rem;
  max-inline-size: 52ch;
  color: var(--muted);
  font-size: 1.05rem;
  text-wrap: pretty;
}

.hd-12__sec {
  margin-top: clamp(2.5rem,7vw,4rem);
  padding-top: 1.75rem;
  border-top: 1px solid var(--line);
}

.hd-12__sec h2 {
  font-family: var(--font-display);
  font-size: 1.15rem;
  font-weight: 660;
  letter-spacing: -.02em;
}

.hd-12__p {
  margin-top: .7rem;
  max-inline-size: 62ch;
  color: var(--muted);
  font-size: .98rem;
  text-wrap: pretty;
}

.hd-12__p code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  color: var(--accent);
}

.hd-12__grid {
  display: grid;
  gap: .75rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,12rem),1fr));
  margin-top: 1.1rem;
}

.hd-12__grid li {
  padding: 1rem;
  border: 1px solid var(--line);
  border-radius: .8rem;
  background: var(--surface2);
  min-inline-size: 0;
}

.hd-12__g-k {
  font-size: .72rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--accent);
  font-weight: 660;
}

.hd-12__g-v {
  font-family: var(--font-display);
  font-size: 1.15rem;
  font-weight: 660;
  margin-top: .25rem;
}

.hd-12__g-d {
  font-size: .82rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.hd-12__filler {
  block-size: 80vh;
}

@media (max-width: 800px) {
  .hd-12__nav {
    display: none;
  }
}

@media (max-width: 480px) {
  .hd-12__link {
    display: none;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-12:has(#hd-12-light:checked) {
  --surface: #f7f9fc;
  --surface2: #ffffff;
  --ink: #101319;
  --muted: #576076;
  --line: rgba(16,19,25,.12);
  --accent: #0e7490;
  --accent2: #6d28d9;
  --accent-ink: #ffffff;
}
/* icon: shows the scheme the toggle will switch you to */

.hd-12__moon {
  display: none;
}

.hd-12:has(#hd-12-light:checked) .hd-12__sun {
  display: none;
}

.hd-12:has(#hd-12-light:checked) .hd-12__moon {
  display: block;
}

@media (prefers-color-scheme: light) {
  .hd-12:not([data-theme="dark"]):not(:has(#hd-12-light:checked)) {
    --surface: #f7f9fc;
    --surface2: #ffffff;
    --ink: #101319;
    --muted: #576076;
    --line: rgba(16,19,25,.12);
    --accent: #0e7490;
    --accent2: #6d28d9;
    --accent-ink: #ffffff;
  }
  /* FLIP-BACK — light OS + checked toggle returns to the other scheme */

  .hd-12:has(#hd-12-light:checked) {
    --surface: #0f1115;
    --surface2: #171a21;
    --ink: #eef0f5;
    --muted: #98a0b0;
    --line: rgba(238,240,245,.12);
    --accent: #22d3ee;
    --accent2: #a78bfa;
    --accent-ink: #04222a;
    --font-display: system-ui,-apple-system,"Segoe UI",sans-serif;
    --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  }
  /* the icon always offers the scheme you are not in */

  .hd-12:not([data-theme="dark"]):not(:has(#hd-12-light:checked)) .hd-12__sun {
    display: none;
  }

  .hd-12:not([data-theme="dark"]):not(:has(#hd-12-light:checked)) .hd-12__moon {
    display: block;
  }

  .hd-12:has(#hd-12-light:checked) .hd-12__moon {
    display: none;
  }

  .hd-12:has(#hd-12-light:checked) .hd-12__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hd-12__bar {
    animation: none !important;
  }

  .hd-12 * {
    transition-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-12__bar {
    border-bottom: 1px solid CanvasText;
  }
}
/* ── theme toggle — visually hidden checkbox, zero JS ────────────── */

.hd-12__sr,
.hd-12__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-12__theme {
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

.hd-12__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-12__theme:hover {
  background: rgba(128,128,128,.16);
}

.hd-12:has(#hd-12-light:focus-visible) .hd-12__theme {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```
