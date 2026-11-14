---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/pure-css-sticky-navbar-no-javascript-position-sticky/"
title: "Pure CSS Sticky Navbar (No JavaScript, position:sticky)"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "The baseline sticky header every other pattern in this collection extends."
has_js: "false"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS Sticky Navbar (No JavaScript, position:sticky)
Source: https://codefronts.com/navigation/css-sticky-navigation/pure-css-sticky-navbar-no-javascript-position-sticky/

The baseline sticky header every other pattern in this collection extends. Two declarations pin a marketing or blog header to the top of its scroll container, and the rest of the demo is the part tutorials skip: why the header stops sticking when a parent has overflow:hidden, and how to stop in-page anchor links from landing underneath the bar.
## HTML
```html
<section class="sn-01" aria-label="Pure CSS sticky navbar demo">
    <header class="sn-01__bar">
      <a class="sn-01__brand" href="#sn-01-s1"><span class="sn-01__logo" aria-hidden="true"></span>Meridian</a>
      <nav class="sn-01__nav" aria-label="Primary">
        <a class="sn-01__link" href="#sn-01-s1" aria-current="page">Product</a>
        <a class="sn-01__link" href="#sn-01-s2">Pricing</a>
        <a class="sn-01__link" href="#sn-01-s3">Docs</a>
        <a class="sn-01__link" href="#sn-01-s4">Changelog</a>
      </nav>
      <a class="sn-01__cta" href="#sn-01-s4">Start free</a>
    </header>
  <div class="sn-01__intro">
    <div class="sn-01__introin">
    <p class="sn-01__intro-eyebrow">position: sticky · top: 0</p>
    <h2 class="sn-01__intro-title">The sticky header, done properly</h2>
    <p class="sn-01__intro-sub">Scroll inside the frame. The bar pins at the top, the anchor links land below it, not behind it.</p>
    </div>
  </div>
    <main class="sn-01__main">
      <section class="sn-01__sec" id="sn-01-s1">
        <p class="sn-01__kicker">Product</p>
        <h3 class="sn-01__h">Two declarations, one caveat</h3>
        <p class="sn-01__p">A sticky box keeps its space in normal flow, so nothing jumps when it pins — the layout shift you get for free with <code>position:fixed</code> never happens.</p>
      </section>
      <section class="sn-01__sec" id="sn-01-s2">
        <p class="sn-01__kicker">Pricing</p>
        <h3 class="sn-01__h">Anchors that clear the bar</h3>
        <p class="sn-01__p">Click any link above. <code>scroll-padding-top</code> on this scroll port offsets every anchor jump by the header height, for clicks, <code>:target</code> and keyboard focus alike.</p>
      </section>
      <section class="sn-01__sec" id="sn-01-s3">
        <p class="sn-01__kicker">Docs</p>
        <h3 class="sn-01__h">The overflow trap</h3>
        <p class="sn-01__p">The nearest scrolling ancestor becomes the sticky port. One stray <code>overflow:hidden</code> higher up and the bar quietly scrolls away with the page.</p>
      </section>
      <section class="sn-01__sec" id="sn-01-s4">
        <p class="sn-01__kicker">Changelog</p>
        <h3 class="sn-01__h">Bounded by its parent</h3>
        <p class="sn-01__p">Sticky elements never leave their containing block. Wrap the header with a single section and it releases at that section's end — chapter headers with zero script.</p>
        <p class="sn-01__chip">~900 bytes of CSS · 0 bytes of JS</p>
      </section>
    </main>
  <footer class="sn-01__pagefoot">
    <p class="sn-01__pagefootin">Sticky navigation pattern 01 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-01 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-01-bg);
  --sn-01-bg: oklch(0.967 0.008 265);
  --sn-01-surface: oklch(1 0 0);
  --sn-01-ink: oklch(0.22 0.022 272);
  --sn-01-mut: oklch(0.55 0.018 272);
  --sn-01-acc: oklch(0.55 0.19 274);
  --sn-01-line: oklch(0.22 0.022 272/.1);
  --sn-01-h: 64px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-01-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-01 *,
.sn-01 *::before,
.sn-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-01__eyebrow,
.sn-01__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sn-01-acc);
}

.sn-01__title,
.sn-01__intro-title {
  font-size: clamp(23px,3.5vw,37px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-01__sub,
.sn-01__intro-sub {
  font-size: 14.5px;
  line-height: 1.6;
  color: var(--sn-01-mut);
  text-wrap: pretty;
}

.sn-01__bar {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  gap: clamp(10px,2vw,26px);
  min-height: var(--sn-01-h);
  padding: 0 clamp(14px,2.4vw,22px);
  background: color-mix(in oklch,var(--sn-01-surface) 78%,transparent);
  backdrop-filter: blur(14px) saturate(1.5);
  -webkit-backdrop-filter: blur(14px) saturate(1.5);
  border-bottom: 1px solid var(--sn-01-line);
}

.sn-01__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
  white-space: nowrap;
}

.sn-01__logo {
  width: 19px;
  height: 19px;
  border-radius: 6px;
  background: linear-gradient(140deg,var(--sn-01-acc),oklch(0.7 0.16 320));
  box-shadow: 0 3px 10px -3px var(--sn-01-acc);
}

.sn-01__nav {
  display: flex;
  align-items: center;
  gap: 2px;
  margin-inline-start: auto;
}

.sn-01__link {
  display: flex;
  align-items: center;
  min-height: 36px;
  padding: 0 11px;
  border-radius: 9px;
  font-size: 13.6px;
  font-weight: 600;
  color: var(--sn-01-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.sn-01__link:hover {
  color: var(--sn-01-ink);
  background: oklch(0.22 0.022 272/.05);
}

.sn-01__link:focus-visible,
.sn-01__cta:focus-visible,
.sn-01__brand:focus-visible {
  outline: 2px solid var(--sn-01-acc);
  outline-offset: 2px;
}

.sn-01__link[aria-current="page"] {
  color: var(--sn-01-acc);
  background: color-mix(in oklch,var(--sn-01-acc) 10%,transparent);
}

.sn-01__cta {
  display: flex;
  align-items: center;
  min-height: 36px;
  padding: 0 15px;
  border-radius: 9px;
  font-size: 13.4px;
  font-weight: 650;
  color: oklch(1 0 0);
  background: var(--sn-01-ink);
  text-decoration: none;
  white-space: nowrap;
  transition: transform .18s ease,background .18s ease;
}

.sn-01__cta:hover {
  background: var(--sn-01-acc);
  transform: translateY(-1px);
}

.sn-01__main {
  display: grid;
}

.sn-01__sec {
  scroll-margin-top: var(--sn-01-h);
  display: grid;
  gap: 10px;
  align-content: center;
  min-height: 70svh;
  padding: clamp(24px,4vw,44px);
  border-bottom: 1px solid var(--sn-01-line);
}

.sn-01__sec:nth-child(even) {
  background: oklch(0.985 0.004 272);
}

.sn-01__sec:last-child {
  border-bottom: 0;
}

.sn-01__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sn-01-acc);
}

.sn-01__h {
  font-size: clamp(19px,2.6vw,26px);
  line-height: 1.16;
  letter-spacing: -.025em;
  font-weight: 690;
  text-wrap: balance;
}

.sn-01__p {
  max-width: 52ch;
  font-size: 14.8px;
  line-height: 1.64;
  color: var(--sn-01-mut);
  text-wrap: pretty;
}

.sn-01__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.22 0.022 272/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

.sn-01__chip {
  justify-self: start;
  margin-block-start: 4px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sn-01-acc);
  padding: 7px 13px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--sn-01-acc) 9%,transparent);
  border: 1px solid color-mix(in oklch,var(--sn-01-acc) 22%,transparent);
}

@media (max-width: 640px) {
  .sn-01 {
    --sn-01-h: 56px;
  }

  .sn-01__nav {
    gap: 0;
  }

  .sn-01__link {
    padding: 0 8px;
    font-size: 12.8px;
  }

  .sn-01__cta {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-01 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-01) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-01-h) + 12px);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-01) {
    scroll-behavior: auto;
  }
}

.sn-01__bar,
.sn-01__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-01__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-01__intro {
  display: grid;
  place-items: center;
  min-height: min(90svh,900px);
  padding: clamp(56px,12vh,150px) clamp(20px,5vw,48px) clamp(40px,8vh,90px);
  background: radial-gradient(92% 58% at 50% 0%,oklch(0.99 0.014 274),transparent);
}

.sn-01__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-width: 26ch;
}

.sn-01__intro-eyebrow {
  font-size: clamp(11px,1.1vw,13px);
}

.sn-01__intro-title {
  font-size: clamp(38px,7.5vw,86px);
  line-height: .98;
  letter-spacing: -.04em;
  max-width: none;
}

.sn-01__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  max-width: 46ch;
}

.sn-01__intro::after {
  content: "Scroll — the bar stays";
  justify-self: center;
  margin-block-start: clamp(20px,4vh,44px);
  padding: 9px 18px;
  border: 1px solid var(--sn-01-line);
  border-radius: 99px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sn-01-mut);
  animation: sn-01-cue 2.6s ease-in-out infinite;
}

@keyframes sn-01-cue {
  0%,
    100% {
    transform: translateY(0);
    opacity: .75;
  }

  50% {
    transform: translateY(5px);
    opacity: 1;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-01__intro::after {
    animation: none;
  }
}

.sn-01__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-01-line);
}

.sn-01__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-01-mut);
  text-align: center;
}

.sn-01__intro-title,
.sn-01__intro-sub {
  text-wrap: balance;
}
```
