---
source: "codefronts"
url: "https://codefronts.com/layouts/css-header-designs/shrinking-header-on-scroll/"
title: "Shrinking Header on Scroll Animation Timeline"
section: "layouts"
category: "css-header-designs"
category_name: "CSS Headers"
description: "The header condenses as you read: 5&nbsp;rem tall at rest, 3.25&nbsp;rem once you pass 200&nbsp;px, with the wordmark scaling down and the shadow deepening…"
has_js: "false"
---

Here's a working CSS Header from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Shrinking Header on Scroll Animation Timeline
Source: https://codefronts.com/layouts/css-header-designs/shrinking-header-on-scroll/

The header condenses as you read: 5&nbsp;rem tall at rest, 3.25&nbsp;rem once you pass 200&nbsp;px, with the wordmark scaling down and the shadow deepening on the same timeline. Driven by animation-timeline: scroll(root), so there is no scroll handler and no requestAnimationFrame loop &mdash; and without scroll-timeline support the header simply stays at a fixed height.
## HTML
```html
<div class="hd-22">
  <a class="hd-22__skip" href="#hd-22-main">Skip to content</a>

  <header class="hd-22__bar">
    <a class="hd-22__brand" href="#hd-22-main">
      <span class="hd-22__mark" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 3 21 8.5v7L12 21 3 15.5v-7L12 3Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M12 8.5 16.5 11v3L12 16.5 7.5 14v-3L12 8.5Z" fill="currentColor"/></svg>
      </span>
      <span class="hd-22__word">Voltline</span>
    </a>

    <nav class="hd-22__nav" aria-label="Main">
      <ul>
        <li><a href="#hd-22-main" aria-current="page">Product</a></li>
        <li><a href="#hd-22-s2">Fleet</a></li>
        <li><a href="#hd-22-s3">Network</a></li>
        <li><a href="#hd-22-s4">Support</a></li>
      </ul>
    </nav>

    <div class="hd-22__right">
      <input class="hd-22__sr" type="checkbox" id="hd-22-dark">
      <label class="hd-22__theme" for="hd-22-dark">
        <svg class="hd-22__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 2.8v2.1M12 19.1v2.1M2.8 12h2.1M19.1 12h2.1M5.5 5.5 7 7M17 17l1.5 1.5M18.5 5.5 17 7M7 17l-1.5 1.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
        <svg class="hd-22__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>
        <span class="hd-22__vh">Switch light or dark theme</span>
      </label>
      <a class="hd-22__link" href="#hd-22-main">Sign in</a>
      <a class="hd-22__cta" href="#hd-22-main">Get a quote</a>
    </div>
  </header>

  <main class="hd-22__main" id="hd-22-main">
    <section class="hd-22__hero">
      <p class="hd-22__eyebrow">Fleet charging</p>
      <h1>Start scrolling. The bar condenses to 3.25&nbsp;rem and stays there.</h1>
      <p class="hd-22__lead">Height, padding, wordmark scale and shadow all move on one scroll-driven animation across the first 200 pixels. Where scroll timelines are unsupported, the header keeps its full height.</p>
    </section>

    <section class="hd-22__sec" id="hd-22-s2">
      <h2>Fleet</h2>
      <ul class="hd-22__grid">
        <li><p class="hd-22__g-v">248</p><p class="hd-22__g-k">Vehicles under management</p></li>
        <li><p class="hd-22__g-v">96%</p><p class="hd-22__g-k">Depot availability, rolling 90 days</p></li>
        <li><p class="hd-22__g-v">42 min</p><p class="hd-22__g-k">Median turnaround at a 150 kW post</p></li>
      </ul>
    </section>

    <section class="hd-22__sec" id="hd-22-s3">
      <h2>Network</h2>
      <p class="hd-22__p">Nineteen depots across the UK and Ireland, with priority access at 340 partner sites. Anchor links in the nav land below the collapsed bar because the root sets <code>scroll-padding-block-start</code>.</p>
    </section>

    <section class="hd-22__sec" id="hd-22-s4">
      <h2>Support</h2>
      <p class="hd-22__p">Engineers on call from 06:00 to 22:00, with a four-hour response commitment on depot hardware and a spare-parts guarantee for seven years.</p>
    </section>
    <div class="hd-22__filler" aria-hidden="true"></div>
  </main>
</div>
```
## CSS
```css
.hd-22 {
  --bg: #f5f7fb;
  --panel: #ffffff;
  --ink: #0b1a2e;
  --muted: #55637a;
  --line: rgba(11,26,46,.12);
  --accent: #0b5cff;
  --accent-soft: rgba(11,92,255,.1);
  --accent-ink: #ffffff;
  --font-display: system-ui,-apple-system,"Segoe UI",sans-serif;
  --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  scroll-padding-block-start: 3.75rem;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-body);
  line-height: 1.55;
}

@supports (color: oklch(50% .1 200)) {
  .hd-22 {
    --bg: oklch(97.5% .008 260);
    --ink: oklch(22% .05 255);
    --muted: oklch(50% .03 255);
    --accent: oklch(52% .24 262);
  }
}

.hd-22 * {
  box-sizing: border-box;
}

.hd-22 h1,
.hd-22 h2,
.hd-22 p,
.hd-22 ul {
  margin: 0;
  padding: 0;
}

.hd-22 ul {
  list-style: none;
}

.hd-22 [hidden] {
  display: none;
}

.hd-22 :focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: .4rem;
}

.hd-22__skip {
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

.hd-22__skip:focus-visible {
  top: 1rem;
}
/* ── header: tall resting state IS the fallback ───────────────────── */

.hd-22__bar {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  gap: clamp(.75rem,3vw,2rem);
  block-size: 5rem;
  padding: 1rem clamp(1rem,4vw,2.25rem);
  background: color-mix(in srgb, var(--panel) 92%, transparent);
  border-bottom: 1px solid var(--line);
  backdrop-filter: blur(10px);
}

.hd-22__brand {
  display: inline-flex;
  align-items: center;
  gap: .6rem;
  color: var(--ink);
  text-decoration: none;
  min-inline-size: 0;
  transform-origin: left center;
  scale: 1;
}

.hd-22__mark {
  display: grid;
  place-items: center;
  inline-size: 2.1rem;
  block-size: 2.1rem;
  border-radius: .6rem;
  background: var(--accent);
  color: #fff;
  flex: none;
}

.hd-22__mark svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.hd-22__word {
  font-family: var(--font-display);
  font-size: 1.15rem;
  font-weight: 700;
  letter-spacing: -.03em;
  min-inline-size: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.hd-22__nav {
  min-inline-size: 0;
}

.hd-22__nav ul {
  display: flex;
  align-items: center;
  gap: .15rem;
}

.hd-22__nav a {
  display: flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: .4rem .7rem;
  border-radius: .5rem;
  color: var(--muted);
  text-decoration: none;
  font-size: .88rem;
  font-weight: 560;
  white-space: nowrap;
  transition: color .15s ease, background-color .15s ease;
}

.hd-22__nav a:hover {
  color: var(--accent);
  background: var(--accent-soft);
}

.hd-22__nav a[aria-current="page"] {
  color: var(--accent);
  font-weight: 680;
}

.hd-22__right {
  display: flex;
  align-items: center;
  gap: .65rem;
  margin-inline-start: auto;
}

.hd-22__link {
  color: var(--muted);
  text-decoration: none;
  font-size: .88rem;
  font-weight: 580;
  white-space: nowrap;
}

.hd-22__link:hover {
  color: var(--ink);
}

.hd-22__cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.6rem;
  padding: .6rem 1.15rem;
  border-radius: .55rem;
  background: var(--accent);
  color: var(--accent-ink);
  text-decoration: none;
  font-size: .87rem;
  font-weight: 700;
  white-space: nowrap;
  box-shadow: 0 .5rem 1.2rem -.5rem rgba(11,92,255,.6);
  transition: translate .16s ease;
}

.hd-22__cta:hover {
  translate: 0 -1px;
}

@supports (animation-timeline: scroll()) {
  .hd-22__bar {
    animation: hd-22-shrink linear both;
    animation-timeline: scroll(root);
    animation-range: 0 200px;
  }

  .hd-22__brand {
    animation: hd-22-logo linear both;
    animation-timeline: scroll(root);
    animation-range: 0 200px;
  }

  @keyframes hd-22-shrink {
    from {
      block-size: 5rem;
      padding-block: 1rem;
      box-shadow: 0 0 0 rgba(8,20,40,0);
    }

    to {
      block-size: 3.25rem;
      padding-block: .4rem;
      box-shadow: 0 .5rem 1.5rem -.8rem rgba(8,20,40,.45);
    }
  }

  @keyframes hd-22-logo {
    from {
      scale: 1;
    }

    to {
      scale: .84;
    }
  }
}
/* ── page body ────────────────────────────────────────────────────── */

.hd-22__main {
  max-inline-size: 68rem;
  margin-inline: auto;
  padding: clamp(2.5rem,8vw,5rem) clamp(1.25rem,4vw,2.25rem) 5rem;
}

.hd-22__eyebrow {
  font-size: .74rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--accent);
}

.hd-22__hero h1 {
  font-family: var(--font-display);
  font-size: clamp(1.9rem,6vw,3.4rem);
  line-height: 1.06;
  font-weight: 700;
  letter-spacing: -.04em;
  margin-top: 1rem;
  max-inline-size: 28ch;
  text-wrap: balance;
}

.hd-22__lead {
  margin-top: 1.1rem;
  max-inline-size: 56ch;
  color: var(--muted);
  font-size: 1.05rem;
  text-wrap: pretty;
}

.hd-22__sec {
  margin-top: clamp(2.5rem,7vw,4rem);
  padding-top: 1.75rem;
  border-top: 1px solid var(--line);
}

.hd-22__sec h2 {
  font-family: var(--font-display);
  font-size: 1.2rem;
  font-weight: 680;
  letter-spacing: -.02em;
}

.hd-22__p {
  margin-top: .7rem;
  max-inline-size: 62ch;
  color: var(--muted);
  font-size: .98rem;
  text-wrap: pretty;
}

.hd-22__p code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  color: var(--accent);
}

.hd-22__grid {
  display: grid;
  gap: .85rem;
  grid-template-columns: repeat(auto-fit,minmax(min(100%,13rem),1fr));
  margin-top: 1.1rem;
}

.hd-22__grid li {
  padding: 1.1rem;
  border-radius: .8rem;
  background: var(--panel);
  border: 1px solid var(--line);
  min-inline-size: 0;
}

.hd-22__g-v {
  font-family: var(--font-display);
  font-size: 1.9rem;
  font-weight: 700;
  letter-spacing: -.04em;
  color: var(--accent);
  font-variant-numeric: tabular-nums;
}

.hd-22__g-k {
  margin-top: .3rem;
  font-size: .85rem;
  color: var(--muted);
  text-wrap: pretty;
}

.hd-22__filler {
  block-size: 85vh;
}

@media (max-width: 820px) {
  .hd-22__nav {
    display: none;
  }
}

@media (max-width: 480px) {
  .hd-22__link {
    display: none;
  }
}
/* ── manual theme toggle — beats the OS default ──────────────────── */

.hd-22:has(#hd-22-dark:checked) {
  --bg: #080e18;
  --panel: #111a29;
  --ink: #e9eef8;
  --muted: #93a1b8;
  --line: rgba(233,238,248,.12);
  --accent: #5b8cff;
  --accent-soft: rgba(91,140,255,.16);
  --accent-ink: #05101f;
}
/* icon: shows the scheme the toggle will switch you to */

.hd-22__sun {
  display: none;
}

.hd-22:has(#hd-22-dark:checked) .hd-22__moon {
  display: none;
}

.hd-22:has(#hd-22-dark:checked) .hd-22__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .hd-22:not([data-theme="light"]):not(:has(#hd-22-dark:checked)) {
    --bg: #080e18;
    --panel: #111a29;
    --ink: #e9eef8;
    --muted: #93a1b8;
    --line: rgba(233,238,248,.12);
    --accent: #5b8cff;
    --accent-soft: rgba(91,140,255,.16);
    --accent-ink: #05101f;
  }
  /* FLIP-BACK — dark OS + checked toggle returns to the other scheme */

  .hd-22:has(#hd-22-dark:checked) {
    --bg: #f5f7fb;
    --panel: #ffffff;
    --ink: #0b1a2e;
    --muted: #55637a;
    --line: rgba(11,26,46,.12);
    --accent: #0b5cff;
    --accent-soft: rgba(11,92,255,.1);
    --accent-ink: #ffffff;
    --font-display: system-ui,-apple-system,"Segoe UI",sans-serif;
    --font-body: system-ui,-apple-system,"Segoe UI",sans-serif;
  }
  /* the icon always offers the scheme you are not in */

  .hd-22:not([data-theme="light"]):not(:has(#hd-22-dark:checked)) .hd-22__moon {
    display: none;
  }

  .hd-22:not([data-theme="light"]):not(:has(#hd-22-dark:checked)) .hd-22__sun {
    display: block;
  }

  .hd-22:has(#hd-22-dark:checked) .hd-22__sun {
    display: none;
  }

  .hd-22:has(#hd-22-dark:checked) .hd-22__moon {
    display: block;
  }
}

.hd-22[data-theme="dark"] {
  --bg: #080e18;
  --panel: #111a29;
  --ink: #e9eef8;
  --muted: #93a1b8;
  --line: rgba(233,238,248,.12);
  --accent: #5b8cff;
  --accent-soft: rgba(91,140,255,.16);
  --accent-ink: #05101f;
}

@media (prefers-reduced-motion: reduce) {
  .hd-22__bar,
    .hd-22__brand {
    animation: none !important;
  }

  .hd-22 * {
    transition-duration: 1ms !important;
  }
}

@media (forced-colors: active) {
  .hd-22__bar {
    border-bottom: 1px solid CanvasText;
  }
}
/* ── theme toggle — visually hidden checkbox, zero JS ────────────── */

.hd-22__sr,
.hd-22__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.hd-22__theme {
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

.hd-22__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.hd-22__theme:hover {
  background: rgba(128,128,128,.16);
}

.hd-22:has(#hd-22-dark:focus-visible) .hd-22__theme {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
```
