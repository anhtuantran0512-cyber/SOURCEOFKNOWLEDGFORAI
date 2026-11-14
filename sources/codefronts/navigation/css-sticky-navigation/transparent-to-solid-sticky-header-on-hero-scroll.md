---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/transparent-to-solid-sticky-header-on-hero-scroll/"
title: "Transparent-to-Solid Sticky Header on Hero Scroll"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "The hero pattern used on almost every launch page: the header sits transparently over full-bleed imagery, then takes on a solid, legible background the…"
has_js: "true"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Transparent-to-Solid Sticky Header on Hero Scroll
Source: https://codefronts.com/navigation/css-sticky-navigation/transparent-to-solid-sticky-header-on-hero-scroll/

The hero pattern used on almost every launch page: the header sits transparently over full-bleed imagery, then takes on a solid, legible background the moment it starts overlapping real content. Implemented with the scroll-state container query — CSS can now style a stuck element without a single scroll listener — plus a sentinel-based fallback for engines that have not shipped it.
## HTML
```html
<section class="sn-08" aria-label="Transparent to solid sticky header demo">
    <div class="sn-08__sentinel" id="sn-08-sentinel" aria-hidden="true"></div>
    <header class="sn-08__bar" id="sn-08-bar" data-stuck="false">
      <div class="sn-08__inner">
        <a class="sn-08__brand" href="#sn-08-s1"><span class="sn-08__logo" aria-hidden="true"></span>Cirrus</a>
        <nav class="sn-08__nav" aria-label="Primary">
          <a class="sn-08__link" href="#sn-08-s1" aria-current="page">Expeditions</a>
          <a class="sn-08__link" href="#sn-08-s2">Journal</a>
          <a class="sn-08__link" href="#sn-08-s3">Gear</a>
        </nav>
        <a class="sn-08__cta" href="#sn-08-s3">Join</a>
      </div>
    </header>
    <div class="sn-08__hero">
      <img class="sn-08__img" src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=1500&auto=format&fit=crop" alt="Mist rolling across green highland peaks at dawn" width="1500" height="1000" loading="lazy" decoding="async">
      <div class="sn-08__herotext">
        <p class="sn-08__kicker">scroll-state(stuck: top)</p>
        <h2 class="sn-08__title">Transparent over the hero,<br>solid over the words</h2>
      </div>
    </div>
    <main>
      <section class="sn-08__sec" id="sn-08-s1">
        <h3 class="sn-08__h">CSS finally knows it is stuck</h3>
        <p class="sn-08__p">A sticky element can declare itself a scroll-state container, and descendants query <code>stuck: top</code> directly. No listener, no observer, no class toggling.</p>
      </section>
      <section class="sn-08__sec" id="sn-08-s2">
        <h3 class="sn-08__h">Contrast flips with the background</h3>
        <p class="sn-08__p">White labels over the photograph, dark labels over the page. Both token sets change together, so neither state is the accessible-by-accident one.</p>
      </section>
      <section class="sn-08__sec" id="sn-08-s3">
        <h3 class="sn-08__h">A sentinel covers the rest</h3>
        <p class="sn-08__p">Where the query is unavailable, a zero-height sentinel above the header is watched by an <code>IntersectionObserver</code> — it fires on boundary crossings only, never per frame.</p>
      </section>
    </main>
  <footer class="sn-08__pagefoot">
    <p class="sn-08__pagefootin">Sticky navigation pattern 08 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-08 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-08-bg);
  --sn-08-bg: oklch(0.95 0.012 160);
  --sn-08-surface: oklch(1 0 0);
  --sn-08-ink: oklch(0.22 0.03 170);
  --sn-08-mut: oklch(0.52 0.025 170);
  --sn-08-acc: oklch(0.55 0.14 165);
  --sn-08-line: oklch(0.22 0.03 170/.12);
  --sn-08-h: 64px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-08-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-08 *,
.sn-08 *::before,
.sn-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-08__sentinel {
  height: 1px;
  margin-block-end: -1px;
}

.sn-08__bar {
  position: sticky;
  top: 0;
  z-index: 20;
  container-type: scroll-state;
  container-name: sn-08-bar;
}

.sn-08__inner {
  display: flex;
  align-items: center;
  gap: clamp(10px,2vw,22px);
  min-height: var(--sn-08-h);
  padding: 0 clamp(14px,2.4vw,24px);
  color: oklch(1 0 0);
  background: transparent;
  border-block-end: 1px solid transparent;
  transition: background .28s ease,color .28s ease,border-color .28s ease,backdrop-filter .28s ease;
}

@container sn-08-bar scroll-state(stuck: top) {
  .sn-08__inner {
    color: var(--sn-08-ink);
    background: color-mix(in oklch,var(--sn-08-surface) 86%,transparent);
    backdrop-filter: blur(14px) saturate(1.4);
    -webkit-backdrop-filter: blur(14px) saturate(1.4);
    border-block-end-color: var(--sn-08-line);
    box-shadow: 0 10px 30px -22px oklch(0.22 0.03 170/.6);
  }
}

.sn-08__bar[data-stuck="true"] .sn-08__inner {
  color: var(--sn-08-ink);
  background: color-mix(in oklch,var(--sn-08-surface) 86%,transparent);
  backdrop-filter: blur(14px) saturate(1.4);
  -webkit-backdrop-filter: blur(14px) saturate(1.4);
  border-block-end-color: var(--sn-08-line);
  box-shadow: 0 10px 30px -22px oklch(0.22 0.03 170/.6);
}

.sn-08__brand {
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

.sn-08__logo {
  width: 18px;
  height: 18px;
  border-radius: 50%;
  border: 3px solid currentColor;
}

.sn-08__nav {
  display: flex;
  align-items: center;
  gap: 2px;
  margin-inline-start: auto;
}

.sn-08__link {
  display: flex;
  align-items: center;
  min-height: 38px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 13.6px;
  font-weight: 600;
  color: inherit;
  opacity: .86;
  text-decoration: none;
  transition: opacity .18s ease,background .18s ease;
}

.sn-08__link:hover {
  opacity: 1;
  background: color-mix(in oklch,currentColor 12%,transparent);
}

.sn-08__link[aria-current="page"] {
  opacity: 1;
  font-weight: 680;
}

.sn-08__cta {
  display: flex;
  align-items: center;
  min-height: 38px;
  padding: 0 16px;
  border-radius: 99px;
  font-size: 13.4px;
  font-weight: 670;
  color: inherit;
  text-decoration: none;
  border: 1px solid color-mix(in oklch,currentColor 45%,transparent);
  white-space: nowrap;
  transition: background .2s ease,color .2s ease;
}

.sn-08__cta:hover {
  background: currentColor;
  color: var(--sn-08-surface);
}

.sn-08__link:focus-visible,
.sn-08__cta:focus-visible,
.sn-08__brand:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.sn-08__hero {
  position: relative;
  margin-block-start: calc(var(--sn-08-h)*-1);
  height: min(56svh,460px);
  display: grid;
}

.sn-08__img {
  grid-area: 1/1;
  width: 100%;
  height: 100%;
  object-fit: cover;
  background: linear-gradient(160deg,oklch(0.42 0.1 175),oklch(0.3 0.07 210));
}

.sn-08__herotext {
  grid-area: 1/1;
  align-self: end;
  display: grid;
  gap: 10px;
  padding: clamp(22px,4vw,44px);
  color: oklch(1 0 0);
  background: linear-gradient(to top,oklch(0.16 0.03 175/.88),transparent 72%);
}

.sn-08__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .13em;
  text-transform: uppercase;
  opacity: .9;
}

.sn-08__title {
  font-size: clamp(25px,4.6vw,42px);
  line-height: 1.04;
  letter-spacing: -.035em;
  font-weight: 720;
  text-wrap: balance;
}

.sn-08__sec {
  scroll-margin-top: var(--sn-08-h);
  display: grid;
  gap: 10px;
  align-content: center;
  min-height: 66svh;
  padding: clamp(24px,4vw,46px);
  border-block-end: 1px solid var(--sn-08-line);
}

.sn-08__sec:nth-child(even) {
  background: oklch(0.98 0.008 165);
}

.sn-08__h {
  font-size: clamp(19px,2.6vw,26px);
  line-height: 1.16;
  letter-spacing: -.025em;
  font-weight: 690;
  text-wrap: balance;
}

.sn-08__p {
  max-width: 52ch;
  font-size: 14.8px;
  line-height: 1.64;
  color: var(--sn-08-mut);
  text-wrap: pretty;
}

.sn-08__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.22 0.03 170/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

@media (max-width: 560px) {
  .sn-08 {
    --sn-08-h: 56px;
  }

  .sn-08__cta {
    display: none;
  }

  .sn-08__link {
    padding: 0 9px;
    font-size: 12.8px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-08 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-08) {
  scroll-behavior: smooth;
  scroll-padding-top: var(--sn-08-h);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-08) {
    scroll-behavior: auto;
  }
}

.sn-08__inner {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-08__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-08__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-08-line);
}

.sn-08__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-08-mut);
  text-align: center;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sn-08');
  if (!root || root.dataset.snWired) return;
  root.dataset.snWired = '1';
  if (CSS.supports('container-type: scroll-state')) return; // native query handles it
  const bar = root.querySelector('#sn-08-bar');
  const io = new IntersectionObserver(
    ([e]) => bar.dataset.stuck = String(!e.isIntersecting),
    { root: null, threshold: 0 }
  );
  io.observe(root.querySelector('#sn-08-sentinel'));
})();
```
