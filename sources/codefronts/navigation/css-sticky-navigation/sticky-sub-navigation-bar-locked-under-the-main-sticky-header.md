---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/sticky-sub-navigation-bar-locked-under-the-main-sticky-header/"
title: "Sticky Sub-Navigation Bar Locked Under the Main Sticky Header"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "The second navigation layer that product catalogues and documentation sites need: a filter or category bar that pins directly beneath the main header and…"
has_js: "true"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Sub-Navigation Bar Locked Under the Main Sticky Header
Source: https://codefronts.com/navigation/css-sticky-navigation/sticky-sub-navigation-bar-locked-under-the-main-sticky-header/

The second navigation layer that product catalogues and documentation sites need: a filter or category bar that pins directly beneath the main header and stays there while the listing scrolls. Shows the offset arithmetic, the layering, and the visual treatment that keeps two stacked bars from reading as one heavy block.
## HTML
```html
<section class="sn-19" aria-label="Sticky sub-navigation under main header demo">
    <header class="sn-19__bar">
      <a class="sn-19__brand" href="#sn-19-s1"><span class="sn-19__logo" aria-hidden="true"></span>Atlas Docs</a>
      <nav class="sn-19__nav" aria-label="Primary">
        <a class="sn-19__link" href="#sn-19-s1" aria-current="page">Guides</a>
        <a class="sn-19__link" href="#sn-19-s2">API</a>
        <a class="sn-19__link" href="#sn-19-s3">Changelog</a>
      </nav>
      <a class="sn-19__cta" href="#sn-19-s2">Console</a>
    </header>
    <div class="sn-19__sub">
      <div class="sn-19__rail" role="group" aria-label="Filter guides by topic">
        <button class="sn-19__chip" type="button" aria-pressed="true">All</button>
        <button class="sn-19__chip" type="button" aria-pressed="false">Getting started</button>
        <button class="sn-19__chip" type="button" aria-pressed="false">Authentication</button>
        <button class="sn-19__chip" type="button" aria-pressed="false">Webhooks</button>
        <button class="sn-19__chip" type="button" aria-pressed="false">Rate limits</button>
        <button class="sn-19__chip" type="button" aria-pressed="false">Migrations</button>
      </div>
    </div>
    <main class="sn-19__main">
      <article class="sn-19__row" id="sn-19-s1"><h3 class="sn-19__rh">Install the SDK</h3><p class="sn-19__rp">Two stacked sticky layers: the header owns the brand and the accent, the sub-nav stays deliberately lighter.</p></article>
      <article class="sn-19__row"><h3 class="sn-19__rh">Authenticate a request</h3><p class="sn-19__rp">The sub-nav's inset is the header's height. Publish it as a token and both layers stay in agreement.</p></article>
      <article class="sn-19__row" id="sn-19-s2"><h3 class="sn-19__rh">Handle webhook retries</h3><p class="sn-19__rp">Chips are buttons with <code>aria-pressed</code> because filtering toggles state — links would promise navigation that never happens.</p></article>
      <article class="sn-19__row"><h3 class="sn-19__rh">Paginate large collections</h3><p class="sn-19__rp">The rail snaps on the inline axis, so a partially visible chip never comes to rest cut in half.</p></article>
      <article class="sn-19__row" id="sn-19-s3"><h3 class="sn-19__rh">Version your integration</h3><p class="sn-19__rp">Scroll padding covers both bars, so deep links land below the sub-nav rather than behind it.</p></article>
      <article class="sn-19__row"><h3 class="sn-19__rh">Migrate from v2</h3><p class="sn-19__rp">Give the secondary layer smaller type and a translucent surface, or the two bars read as one heavy slab.</p></article>
      <article class="sn-19__row"><h3 class="sn-19__rh">Error reference</h3><p class="sn-19__rp">Everything here is two declarations of <code>position:sticky</code> and one piece of arithmetic.</p></article>
    </main>
  <footer class="sn-19__pagefoot">
    <p class="sn-19__pagefootin">Sticky navigation pattern 19 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-19 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-19-bg);
  --sn-19-bg: oklch(0.16 0.02 255);
  --sn-19-surface: oklch(0.205 0.024 255);
  --sn-19-ink: oklch(0.97 0.006 255);
  --sn-19-mut: oklch(0.71 0.018 255);
  --sn-19-acc: oklch(0.78 0.16 200);
  --sn-19-line: oklch(1 0 0/.1);
  --sn-19-h: 60px;
  --sn-19-sub: 52px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-19-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-19 *,
.sn-19 *::before,
.sn-19 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-19__bar {
  position: sticky;
  top: 0;
  z-index: 30;
  display: flex;
  align-items: center;
  gap: clamp(10px,2vw,22px);
  block-size: var(--sn-19-h);
  padding: 0 clamp(14px,2.6vw,22px);
  background: color-mix(in oklch,var(--sn-19-surface) 92%,transparent);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--sn-19-line);
}

.sn-19__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.025em;
  color: inherit;
  text-decoration: none;
  white-space: nowrap;
}

.sn-19__logo {
  width: 19px;
  height: 19px;
  border-radius: 50%;
  background: conic-gradient(from 140deg,var(--sn-19-acc),oklch(0.6 0.16 280),var(--sn-19-acc));
}

.sn-19__nav {
  display: flex;
  align-items: center;
  gap: 2px;
  margin-inline-start: auto;
}

.sn-19__link {
  display: flex;
  align-items: center;
  min-height: 36px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--sn-19-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.sn-19__link:hover {
  color: var(--sn-19-ink);
  background: oklch(1 0 0/.06);
}

.sn-19__link[aria-current="page"] {
  color: var(--sn-19-acc);
}

.sn-19__cta {
  display: flex;
  align-items: center;
  min-height: 36px;
  padding: 0 15px;
  border-radius: 9px;
  font-size: 13px;
  font-weight: 660;
  color: oklch(0.16 0.02 255);
  background: var(--sn-19-acc);
  text-decoration: none;
  white-space: nowrap;
}

.sn-19__link:focus-visible,
.sn-19__cta:focus-visible,
.sn-19__brand:focus-visible,
.sn-19__chip:focus-visible {
  outline: 2px solid var(--sn-19-acc);
  outline-offset: 2px;
}

.sn-19__sub {
  position: sticky;
  top: var(--sn-19-h);
  z-index: 20;
  block-size: var(--sn-19-sub);
  background: color-mix(in oklch,var(--sn-19-surface) 88%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--sn-19-line);
  container-type: scroll-state;
  container-name: sn-19-sub;
  transition: box-shadow .3s ease;
}

@container sn-19-sub scroll-state(stuck: top) {
  .sn-19__rail {
    box-shadow: 0 14px 26px -24px oklch(0 0 0/.9);
  }
}

.sn-19__rail {
  display: flex;
  align-items: center;
  gap: 7px;
  block-size: 100%;
  padding-inline: clamp(14px,2.6vw,22px);
  overflow-x: auto;
  overscroll-behavior-inline: contain;
  scroll-snap-type: inline mandatory;
  scrollbar-width: none;
  mask-image: linear-gradient(90deg,#000 0,#000 calc(100% - 34px),transparent 100%);
}

.sn-19__rail::-webkit-scrollbar {
  display: none;
}

.sn-19__chip {
  flex: none;
  scroll-snap-align: start;
  display: flex;
  align-items: center;
  min-height: 34px;
  padding: 0 14px;
  border: 1px solid var(--sn-19-line);
  border-radius: 99px;
  background: transparent;
  font-family: inherit;
  font-size: 12.8px;
  font-weight: 600;
  color: var(--sn-19-mut);
  white-space: nowrap;
  cursor: pointer;
  transition: color .18s ease,background .18s ease,border-color .18s ease;
}

.sn-19__chip:hover {
  color: var(--sn-19-ink);
  background: oklch(1 0 0/.06);
}

.sn-19__chip[aria-pressed="true"] {
  color: oklch(0.16 0.02 255);
  background: var(--sn-19-acc);
  border-color: transparent;
}

.sn-19__main {
  display: grid;
}

.sn-19__row {
  scroll-margin-top: calc(var(--sn-19-h) + var(--sn-19-sub));
  display: grid;
  gap: 7px;
  padding: clamp(18px,3vw,26px) clamp(16px,3vw,26px);
  border-bottom: 1px solid var(--sn-19-line);
}

.sn-19__row:nth-child(even) {
  background: oklch(1 0 0/.022);
}

.sn-19__rh {
  font-size: 16.5px;
  line-height: 1.22;
  letter-spacing: -.02em;
  font-weight: 660;
}

.sn-19__rp {
  max-width: 60ch;
  font-size: 14.2px;
  line-height: 1.62;
  color: var(--sn-19-mut);
  text-wrap: pretty;
}

.sn-19__rp code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(1 0 0/.09);
  padding: 2px 6px;
  border-radius: 5px;
}

@media (max-width: 600px) {
  .sn-19__cta {
    display: none;
  }

  .sn-19__link {
    padding: 0 9px;
    font-size: 12.8px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-19 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-19) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-19-h) + var(--sn-19-sub) + 8px);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-19) {
    scroll-behavior: auto;
  }
}

.sn-19__bar,
.sn-19__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-19__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-19__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-19-line);
}

.sn-19__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-19-mut);
  text-align: center;
}

.sn-19__intro-title,
.sn-19__intro-sub {
  text-wrap: balance;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sn-19');
  if (!root || root.dataset.snWired) return;
  root.dataset.snWired = '1';
  const chips = [...root.querySelectorAll('.sn-19__chip')];
  chips.forEach((chip) => chip.addEventListener('click', () => {
    chips.forEach((c) => c.setAttribute('aria-pressed', String(c === chip)));
  }));
})();
```
