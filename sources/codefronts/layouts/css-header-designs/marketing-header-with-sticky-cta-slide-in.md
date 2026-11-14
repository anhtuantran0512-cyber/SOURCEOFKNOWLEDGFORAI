---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/marketing-header-with-sticky-cta-slide-in/"
title: "Marketing Header with Sticky CTA Slide-In"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "A landing-page header that stays quiet until it has earned the ask: logo, nav and a text link at rest, then a solid Start free trial button slides in from…"
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Marketing Header with Sticky CTA Slide-In
Source: https://codefronts.com/layouts/css-header-designs/marketing-header-with-sticky-cta-slide-in/

A landing-page header that stays quiet until it has earned the ask: logo, nav and a text link at rest, then a solid Start free trial button slides in from the right once the reader passes 240&nbsp;px. It is driven entirely by animation-timeline: scroll(root) — no scroll listener, nothing to throttle — and where scroll-driven animation is unsupported the button is simply visible from the start.
## HTML
```html
<div class="hd-05">
  <a class="hd-05__skip" href="#hd-05-main">Skip to content</a>

  <header class="hd-05__bar">
    <a class="hd-05__brand" href="#hd-05-main">
      <svg class="hd-05__mark" viewBox="0 0 26 26" fill="none" aria-hidden="true" focusable="false">
        <circle cx="13" cy="13" r="10.4" stroke="currentColor" stroke-width="1.7"/>
        <path d="M8 13.6 11.6 17 18 9.6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <span class="hd-05__word">Cadence</span>
    </a>

    <nav class="hd-05__nav" aria-label="Main">
      <ul>
        <li><a href="#hd-05-main">Platform</a></li>
        <li><a href="#hd-05-main">Customers</a></li>
        <li><a href="#hd-05-main">Pricing</a></li>
        <li><a href="#hd-05-main">Resources</a></li>
      </ul>
    </nav>

    <div class="hd-05__right">
      <input class="hd-05__sr" type="checkbox" id="hd-05-light">
      <label class="hd-05__theme" for="hd-05-light">
        <svg class="hd-05__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <svg class="hd-05__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <span class="hd-05__vh">Switch light or dark theme</span>
      </label>
      <a class="hd-05__link" href="#hd-05-main">Sign in</a>
      <a class="hd-05__cta" href="#hd-05-main">Start free trial
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M5 12h13M12.5 6l6 6-6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </a>
    </div>
  </header>

  <main class="hd-05__main" id="hd-05-main">
    <section class="hd-05__hero">
      <p class="hd-05__eyebrow">Revenue operations</p>
      <h1>Forecasts your board can actually read.</h1>
      <p class="hd-05__lead">Scroll down &mdash; the header keeps its calm at the top of the page and the trial button slides in once you pass the fold. Zero scroll listeners: the reveal is one keyframe on a scroll timeline.</p>
      <div class="hd-05__proof">
        <p>Used by revenue teams at</p>
        <ul><li>Northwind</li><li>Atlas Freight</li><li>Halcyon</li><li>Foundry</li></ul>
      </div>
    </section>

    <section class="hd-05__band">
      <ul class="hd-05__facts">
        <li><p class="hd-05__n">4.2&#215;</p><p>faster close on committed pipeline after the first quarter.</p></li>
        <li><p class="hd-05__n">98%</p><p>of forecast lines reconcile without a manual override.</p></li>
        <li><p class="hd-05__n">11 min</p><p>median time from raw CRM export to a board-ready view.</p></li>
      </ul>
    </section>

    <section class="hd-05__quote">
      <blockquote>We stopped arguing about whose spreadsheet was right and started arguing about the actual number. That was the whole win.</blockquote>
      <p class="hd-05__cite">Priya Sharma &middot; VP Revenue Operations, Atlas Freight</p>
    </section>
    <div class="hd-05__filler" aria-hidden="true"></div>
  </main>
</div>
```
## CSS
```css
.hd-05 {
  --bg: #0b1524;
  --bg2: #0f1d31;
  --ink: #eef4ff;
  --muted: #93a6c4;
  --line: rgba(238,244,255,.12);
  --line2: rgba(238,244,255,.22);
  --accent: #bef264;
  --accent-ink: #16240a;
  --font-display: system-ui,-apple-system,"Segoe UI",sans-serif;
  --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  --pad: 1.15rem;
  width: 100%;
  min-height: 100vh;
  display: block;
  background: radial-gradient(70rem 34rem at 88% -8%, rgba(190,242,100,.13), transparent 60%), linear-gradient(180deg, var(--bg) 0%, var(--bg2) 60%, var(--bg) 100%);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.55;
}

@supports (color: oklch(50% .1 200)) {
  .hd-05 {
    --bg: oklch(20% .04 250);
    --bg2: oklch(24% .05 252);
    --ink: oklch(96% .015 250);
    --muted: oklch(72% .04 250);
    --accent: oklch(90% .17 120);
  }
}

.hd-05 * {
  box-sizing: border-box;
}

.hd-05 h1,
.hd-05 p,
.hd-05 ul,
.hd-05 blockquote {
  margin: 0;
  padding: 0;
}

.hd-05 ul {
  list-style: none;
}

.hd-05 [hidden] {
  display: none;
}

.hd-05 :focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.hd-05__skip {
  position: absolute;
  inset-inline-start: 1rem;
  top: -3rem;
  z-index: 60;
  padding: .55rem 1rem;
  background: var(--accent);
  color: var(--accent-ink);
  font-size: .82rem;
  font-weight: 700;
  text-decoration: none;
  transition: top .18s ease;
}

.hd-05__skip:focus-visible {
  top: 1rem;
}
/* ── header: flat, roomy, borderless at rest ──────────────────────── */

.hd-05__bar {
  position: sticky;
  top: 0;
  z-index: 30;
  overflow: hidden;
  display: flex;
  align-items: center;
  gap: clamp(1rem,4vw,2.5rem);
  padding: var(--pad) clamp(1rem,5vw,3rem);
  background: color-mix(in srgb, var(--bg) 82%, transparent);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid transparent;
}

.hd-05__brand {
  display: inline-flex;
  align-items: center;
  gap: .6rem;
  color: var(--ink);
  text-decoration: none;
  min-inline-size: 0;
}

.hd-05__mark {
  inline-size: 1.6rem;
  block-size: 1.6rem;
  color: var(--accent);
  flex: none;
}

.hd-05__word {
  font-family: var(--font-display);
  font-size: .95rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .24em;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-05__nav {
  min-inline-size: 0;
}

.hd-05__nav ul {
  display: flex;
  align-items: center;
  gap: clamp(.8rem,2.4vw,1.9rem);
}

.hd-05__nav a {
  position: relative;
  display: block;
  padding: .5rem 0;
  color: var(--muted);
  text-decoration: none;
  font-size: .78rem;
  font-weight: 640;
  letter-spacing: .14em;
  text-transform: uppercase;
  white-space: nowrap;
  transition: color .18s ease;
}

.hd-05__nav a::after {
  content: "";
  position: absolute;
  inset-inline: 0;
  bottom: .15rem;
  block-size: 1px;
  background: var(--accent);
  scale: 0 1;
  transform-origin: left;
  transition: scale .22s cubic-bezier(.2,.8,.2,1);
}

.hd-05__nav a:hover {
  color: var(--ink);
}

.hd-05__nav a:hover::after {
  scale: 1 1;
}

.hd-05__right {
  display: flex;
  align-items: center;
  gap: clamp(.6rem,2vw,1.25rem);
  margin-inline-start: auto;
}

.hd-05__link {
  color: var(--muted);
  text-decoration: none;
  font-size: .78rem;
  font-weight: 640;
  letter-spacing: .14em;
  text-transform: uppercase;
  white-space: nowrap;
  transition: color .18s ease;
}

.hd-05__link:hover {
  color: var(--ink);
}

.hd-05__cta {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  min-block-size: 2.75rem;
  padding: .7rem 1.15rem;
  background: var(--accent);
  color: var(--accent-ink);
  text-decoration: none;
  font-size: .78rem;
  font-weight: 750;
  letter-spacing: .12em;
  text-transform: uppercase;
  white-space: nowrap;
  opacity: 1;
  translate: 0 0;
  /* resting state = the fallback */
}

.hd-05__cta svg {
  inline-size: 1rem;
  block-size: 1rem;
}

.hd-05__cta:hover {
  background: #fff;
}
/* ── scroll-driven reveal ─────────────────────────────────────────── */

@supports (animation-timeline: scroll()) {
  .hd-05__cta {
    animation: hd-05-cta linear both;
    animation-timeline: scroll(root);
    animation-range: 140px 300px;
  }

  .hd-05__bar {
    animation: hd-05-edge linear both;
    animation-timeline: scroll(root);
    animation-range: 0 200px;
  }

  @keyframes hd-05-cta {
    from {
      opacity: 0;
      translate: 130% 0;
    }

    to {
      opacity: 1;
      translate: 0 0;
    }
  }

  @keyframes hd-05-edge {
    from {
      border-bottom-color: transparent;
    }

    to {
      border-bottom-color: var(--line);
    }
  }
}
/* ── page body ────────────────────────────────────────────────────── */

.hd-05__main {
  max-inline-size: 72rem;
  margin-inline: auto;
  padding: clamp(3rem,10vw,7rem) clamp(1.25rem,5vw,3rem) 5rem;
}

.hd-05__eyebrow {
  font-size: .74rem;
  font-weight: 700;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--accent);
}

.hd-05__hero h1 {
  font-family: var(--font-display);
  font-size: clamp(2.3rem,7.5vw,4.6rem);
  line-height: 1.02;
  letter-spacing: -.04em;
  font-weight: 700;
  margin-top: 1.2rem;
  max-inline-size: 26ch;
  text-wrap: balance;
}

.hd-05__lead {
  margin-top: 1.4rem;
  max-inline-size: 54ch;
  color: var(--muted);
  font-size: 1.08rem;
  text-wrap: pretty;
}

.hd-05__proof {
  margin-top: clamp(2.5rem,7vw,4rem);
}

.hd-05__proof p {
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 640;
}

.hd-05__proof ul {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(1rem,4vw,2.5rem);
  margin-top: 1rem;
}

.hd-05__proof li {
  font-family: var(--font-display);
  font-size: 1.15rem;
  font-weight: 700;
  letter-spacing: -.02em;
  color: var(--ink);
  opacity: .75;
}

.hd-05__band {
  margin-top: clamp(3rem,9vw,6rem);
  border-block: 1px solid var(--line);
  padding-block: clamp(2rem,5vw,3rem);
}

.hd-05__facts {
  display: grid;
  gap: clamp(1.5rem,4vw,3rem);
  grid-template-columns: repeat(auto-fit,minmax(min(100%,15rem),1fr));
}

.hd-05__facts li {
  min-inline-size: 0;
}

.hd-05__facts p:last-child {
  color: var(--muted);
  font-size: .95rem;
  max-inline-size: 32ch;
  margin-top: .4rem;
  text-wrap: pretty;
}

.hd-05__n {
  font-family: var(--font-display);
  font-size: clamp(2rem,5vw,2.9rem);
  font-weight: 700;
  letter-spacing: -.04em;
  color: var(--accent);
  font-variant-numeric: tabular-nums;
}

.hd-05__quote {
  margin-top: clamp(3rem,9vw,6rem);
  max-inline-size: 44ch;
}

.hd-05__quote blockquote {
  font-family: var(--font-display);
  font-size: clamp(1.2rem,3.4vw,1.7rem);
  line-height: 1.35;
  letter-spacing: -.02em;
  text-wrap: pretty;
}

.hd-05__cite {
  margin-top: 1rem;
  font-size: .8rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 600;
}

.hd-05__filler {
  block-size: 70vh;
}

@media (max-width: 900px) {
  .hd-05__nav {
    display: none;
  }
}

@media (max-width: 520px) {
  .hd-05__link {
    display: none;
  }

  .hd-05__cta {
    padding: .65rem .85rem;
    font-size: .72rem;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-05:has(#hd-05-light:checked) {
  --bg: #f4f6fb;
  --bg2: #ffffff;
  --ink: #0b1524;
  --muted: #4c5b74;
  --line: rgba(11,21,36,.12);
  --line2: rgba(11,21,36,.2);
  --accent: #3f6212;
  --accent-ink: #f7fee7;
}
/* icon: shows the scheme the toggle will switch you to */

.hd-05__moon {
  display: none;
}

.hd-05:has(#hd-05-light:checked) .hd-05__sun {
  display: none;
}

.hd-05:has(#hd-05-light:checked) .hd-05__moon {
  display: block;
}

@media (prefers-color-scheme: light) {
  .hd-05:not([data-theme="dark"]):not(:has(#hd-05-light:checked)) {
    --bg: #f4f6fb;
    --bg2: #ffffff;
    --ink: #0b1524;
    --muted: #4c5b74;
    --line: rgba(11,21,36,.12);
    --line2: rgba(11,21,36,.2);
    --accent: #3f6212;
    --accent-ink: #f7fee7;
  }
  /* FLIP-BACK — light OS + checked toggle returns to the other scheme */

  .hd-05:has(#hd-05-light:checked) {
    --bg: #0b1524;
    --bg2: #0f1d31;
    --ink: #eef4ff;
    --muted: #93a6c4;
    --line: rgba(238,244,255,.12);
    --line2: rgba(238,244,255,.22);
    --accent: #bef264;
    --accent-ink: #16240a;
    --font-display: system-ui,-apple-system,"Segoe UI",sans-serif;
    --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
    --pad: 1.15rem;
  }
  /* the icon always offers the scheme you are not in */

  .hd-05:not([data-theme="dark"]):not(:has(#hd-05-light:checked)) .hd-05__sun {
    display: none;
  }

  .hd-05:not([data-theme="dark"]):not(:has(#hd-05-light:checked)) .hd-05__moon {
    display: block;
  }

  .hd-05:has(#hd-05-light:checked) .hd-05__moon {
    display: none;
  }

  .hd-05:has(#hd-05-light:checked) .hd-05__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hd-05__cta {
    animation: none !important;
    opacity: 1 !important;
    translate: 0 0 !important;
  }

  .hd-05 * {
    transition-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-05__cta {
    border: 1px solid CanvasText;
  }
}
/* ── theme toggle — visually hidden checkbox, zero JS ────────────── */

.hd-05__sr,
.hd-05__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-05__theme {
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

.hd-05__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-05__theme:hover {
  background: rgba(128,128,128,.16);
}

.hd-05:has(#hd-05-light:focus-visible) .hd-05__theme {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```
