---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/sticky-header-with-svg-logo-wordmark-mark-only-morph-on-scroll/"
title: "Sticky Header with SVG Logo Wordmark → Mark-Only Morph on Scroll"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "The identity move used by large product sites: a full wordmark while the reader is at the top, cross-fading to the compact mark once the header pins,…"
has_js: "true"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Header with SVG Logo Wordmark → Mark-Only Morph on Scroll
Source: https://codefronts.com/navigation/css-sticky-navigation/sticky-header-with-svg-logo-wordmark-mark-only-morph-on-scroll/

The identity move used by large product sites: a full wordmark while the reader is at the top, cross-fading to the compact mark once the header pins, reclaiming horizontal space for navigation on narrow screens. Both lockups are inline SVG in one grid cell, so the swap costs no layout shift and no second network request.
## HTML
```html
<section class="sn-10" aria-label="Logo wordmark to mark morph on scroll demo">
    <div class="sn-10__sentinel" id="sn-10-sentinel" aria-hidden="true"></div>
    <header class="sn-10__bar" id="sn-10-bar" data-stuck="false">
      <a class="sn-10__logo" href="#sn-10-s1" aria-label="Ardor, home">
        <svg class="sn-10__word" viewBox="0 0 132 26" aria-hidden="true" focusable="false"><path d="M6 20 12 6l6 14h-3.2l-1-2.6H10.2L9.2 20H6zm5.1-5h2.9l-1.45-3.8L11.1 15z" fill="currentColor"/><path d="M24 20V6h5.6c3 0 4.9 1.6 4.9 4.3 0 1.9-1 3.3-2.7 3.9L35 20h-3.4l-2.8-5.3H27V20h-3zm3-7.8h2.3c1.4 0 2.2-.7 2.2-1.8s-.8-1.8-2.2-1.8H27v3.6z" fill="currentColor"/><path d="M40 13c0-4.1 3-7.3 7.2-7.3S54.4 8.9 54.4 13s-3 7.3-7.2 7.3S40 17.1 40 13zm11.3 0c0-2.5-1.7-4.4-4.1-4.4S43.1 10.5 43.1 13s1.7 4.4 4.1 4.4 4.1-1.9 4.1-4.4z" fill="currentColor"/><path d="M60 20V6h5c4.3 0 7.2 2.8 7.2 7s-2.9 7-7.2 7h-5zm3-2.7h1.9c2.5 0 4.2-1.7 4.2-4.3s-1.7-4.3-4.2-4.3H63v8.6z" fill="currentColor"/><path d="M78 20V6h5.6c3 0 4.9 1.6 4.9 4.3 0 1.9-1 3.3-2.7 3.9L89 20h-3.4l-2.8-5.3H81V20h-3zm3-7.8h2.3c1.4 0 2.2-.7 2.2-1.8s-.8-1.8-2.2-1.8H81v3.6z" fill="currentColor"/><circle cx="97" cy="13" r="3" fill="currentColor" opacity=".55"/></svg>
        <svg class="sn-10__mark" viewBox="0 0 32 32" aria-hidden="true" focusable="false"><path d="M16 2 30 30H2L16 2zm0 8.4L8.6 25.2h14.8L16 10.4z" fill="currentColor"/></svg>
      </a>
      <nav class="sn-10__nav" aria-label="Primary">
        <a class="sn-10__link" href="#sn-10-s1" aria-current="page">Collections</a>
        <a class="sn-10__link" href="#sn-10-s2">Materials</a>
        <a class="sn-10__link" href="#sn-10-s3">Stockists</a>
        <a class="sn-10__link" href="#sn-10-s3">Contact</a>
      </nav>
      <a class="sn-10__cta" href="#sn-10-s2">Bag (2)</a>
    </header>
  <div class="sn-10__intro">
    <div class="sn-10__introin">
    <p class="sn-10__intro-eyebrow">clip-path: inset() · grid-area: 1/1</p>
    <h2 class="sn-10__intro-title">Wordmark at rest, mark in motion</h2>
    <p class="sn-10__intro-sub">Scroll a little — the wordmark wipes away and the mark takes its place, with no width change.</p>
    </div>
  </div>
    <main>
      <section class="sn-10__sec" id="sn-10-s1">
        <p class="sn-10__kicker">Collections</p>
        <h3 class="sn-10__h">One cell, two lockups</h3>
        <p class="sn-10__p">Both SVGs sit in <code>grid-area: 1/1</code>, so the header measures the widest of them once and the navigation beside it never shifts.</p>
      </section>
      <section class="sn-10__sec" id="sn-10-s2">
        <p class="sn-10__kicker">Materials</p>
        <h3 class="sn-10__h">A wipe, not a dissolve</h3>
        <p class="sn-10__p">Animating <code>clip-path: inset()</code> makes the mark feel revealed from inside the wordmark rather than layered on top of it.</p>
      </section>
      <section class="sn-10__sec" id="sn-10-s3">
        <p class="sn-10__kicker">Stockists</p>
        <h3 class="sn-10__h">Announced once</h3>
        <p class="sn-10__p">The link owns the accessible name and both graphics are hidden, so the brand is never read out twice.</p>
      </section>
    </main>
  <footer class="sn-10__pagefoot">
    <p class="sn-10__pagefootin">Sticky navigation pattern 10 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-10 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-10-bg);
  --sn-10-bg: oklch(0.94 0.008 300);
  --sn-10-surface: oklch(0.99 0.003 300);
  --sn-10-ink: oklch(0.19 0.02 300);
  --sn-10-mut: oklch(0.51 0.02 300);
  --sn-10-acc: oklch(0.5 0.16 300);
  --sn-10-line: oklch(0.19 0.02 300/.13);
  --sn-10-h: 70px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-10-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-10 *,
.sn-10 *::before,
.sn-10 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-10__eyebrow,
.sn-10__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sn-10-acc);
}

.sn-10__title,
.sn-10__intro-title {
  font-size: clamp(23px,3.5vw,37px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-10__sub,
.sn-10__intro-sub {
  font-size: 14.4px;
  line-height: 1.6;
  color: var(--sn-10-mut);
  text-wrap: pretty;
}

.sn-10__sentinel {
  height: 1px;
  margin-block-end: -1px;
}

.sn-10__bar {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  gap: clamp(12px,2.4vw,26px);
  min-height: var(--sn-10-h);
  padding: 0 clamp(16px,3vw,26px);
  background: color-mix(in oklch,var(--sn-10-surface) 88%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid transparent;
  transition: min-height .3s cubic-bezier(.32,.72,.3,1),border-color .3s ease;
}

.sn-10__bar[data-stuck="true"] {
  min-height: 56px;
  border-bottom-color: var(--sn-10-line);
}

.sn-10__logo {
  display: grid;
  place-items: center start;
  inline-size: 112px;
  block-size: 26px;
  color: inherit;
  text-decoration: none;
}

.sn-10__logo>* {
  grid-area: 1/1;
}

.sn-10__word {
  inline-size: 112px;
  block-size: 22px;
  clip-path: inset(0 0 0 0);
  opacity: 1;
  transition: clip-path .4s cubic-bezier(.32,.72,.3,1),opacity .3s ease;
}

.sn-10__mark {
  inline-size: 26px;
  block-size: 26px;
  opacity: 0;
  scale: .6;
  transform-origin: left center;
  transition: opacity .3s ease .06s,scale .4s cubic-bezier(.32,.72,.3,1) .06s;
}

.sn-10__bar[data-stuck="true"] .sn-10__word {
  clip-path: inset(0 100% 0 0);
  opacity: 0;
  transition-delay: 0s;
}

.sn-10__bar[data-stuck="true"] .sn-10__mark {
  opacity: 1;
  scale: 1;
}

.sn-10__logo:focus-visible {
  outline: 2px solid var(--sn-10-acc);
  outline-offset: 4px;
  border-radius: 4px;
}

.sn-10__nav {
  display: flex;
  align-items: center;
  gap: 2px;
  margin-inline-start: auto;
}

.sn-10__link {
  display: flex;
  align-items: center;
  min-height: 38px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 13.4px;
  font-weight: 600;
  letter-spacing: .01em;
  color: var(--sn-10-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.sn-10__link:hover {
  color: var(--sn-10-ink);
  background: oklch(0.19 0.02 300/.05);
}

.sn-10__link[aria-current="page"] {
  color: var(--sn-10-acc);
}

.sn-10__cta {
  display: flex;
  align-items: center;
  min-height: 38px;
  padding: 0 15px;
  border-radius: 99px;
  font-size: 13px;
  font-weight: 660;
  color: var(--sn-10-ink);
  border: 1px solid var(--sn-10-line);
  text-decoration: none;
  white-space: nowrap;
  transition: background .2s ease,color .2s ease;
}

.sn-10__cta:hover {
  background: var(--sn-10-ink);
  color: var(--sn-10-surface);
}

.sn-10__link:focus-visible,
.sn-10__cta:focus-visible {
  outline: 2px solid var(--sn-10-acc);
  outline-offset: 2px;
}

.sn-10__sec {
  scroll-margin-top: var(--sn-10-h);
  display: grid;
  gap: 10px;
  align-content: center;
  min-height: 66svh;
  padding: clamp(24px,4vw,46px);
  border-bottom: 1px solid var(--sn-10-line);
}

.sn-10__sec:nth-child(even) {
  background: oklch(0.965 0.006 300);
}

.sn-10__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sn-10-acc);
}

.sn-10__h {
  font-size: clamp(19px,2.6vw,26px);
  line-height: 1.16;
  letter-spacing: -.025em;
  font-weight: 690;
  text-wrap: balance;
}

.sn-10__p {
  max-width: 52ch;
  font-size: 14.8px;
  line-height: 1.64;
  color: var(--sn-10-mut);
  text-wrap: pretty;
}

.sn-10__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.19 0.02 300/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

@media (max-width: 620px) {
  .sn-10 {
    --sn-10-h: 62px;
  }

  .sn-10__link {
    padding: 0 8px;
    font-size: 12.6px;
  }

  .sn-10__cta {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-10 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-10) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-10-h) + 8px);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-10) {
    scroll-behavior: auto;
  }
}

.sn-10__bar,
.sn-10__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-10__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-10__intro {
  display: grid;
  place-items: center;
  min-height: min(90svh,900px);
  padding: clamp(56px,12vh,150px) clamp(20px,5vw,48px) clamp(40px,8vh,90px);
  background: radial-gradient(85% 55% at 50% 0%,oklch(0.97 0.02 300),transparent);
}

.sn-10__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-width: 26ch;
}

.sn-10__intro-eyebrow {
  font-size: clamp(11px,1.1vw,13px);
}

.sn-10__intro-title {
  font-size: clamp(38px,7.5vw,86px);
  line-height: .98;
  letter-spacing: -.04em;
  max-width: none;
}

.sn-10__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  max-width: 46ch;
}

.sn-10__intro::after {
  content: "Scroll — the bar stays";
  justify-self: center;
  margin-block-start: clamp(20px,4vh,44px);
  padding: 9px 18px;
  border: 1px solid var(--sn-10-line);
  border-radius: 99px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sn-10-mut);
  animation: sn-10-cue 2.6s ease-in-out infinite;
}

@keyframes sn-10-cue {
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
  .sn-10__intro::after {
    animation: none;
  }
}

.sn-10__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-10-line);
}

.sn-10__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-10-mut);
  text-align: center;
}

.sn-10__intro-title,
.sn-10__intro-sub {
  text-wrap: balance;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sn-10');
  if (!root || root.dataset.snWired) return;
  root.dataset.snWired = '1';
  const bar = root.querySelector('#sn-10-bar');
  const io = new IntersectionObserver(
    ([e]) => bar.dataset.stuck = String(!e.isIntersecting),
    { root: null, threshold: 0 }
  );
  io.observe(root.querySelector('#sn-10-sentinel'));
})();
```
