---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/sticky-announcement-bar-stacked-above-sticky-nav-dual-stick/"
title: "Sticky Announcement Bar Stacked Above Sticky Nav (Dual-Stick)"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "Two independently sticky bars that have to cooperate: a promotional strip that scrolls away and a navigation bar that pins beneath it."
has_js: "true"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Announcement Bar Stacked Above Sticky Nav (Dual-Stick)
Source: https://codefronts.com/navigation/css-sticky-navigation/sticky-announcement-bar-stacked-above-sticky-nav-dual-stick/

Two independently sticky bars that have to cooperate: a promotional strip that scrolls away and a navigation bar that pins beneath it. The demo solves the offset arithmetic properly — each bar's inset is derived from the heights above it, so dismissing the promo re-seats the nav at the top with no leftover gap and no stale scroll padding.
## HTML
```html
<section class="sn-18" aria-label="Dual sticky announcement bar and nav demo">
    <div class="sn-18__wrap" id="sn-18-wrap" data-dismissed="false">
      <div class="sn-18__promo" id="sn-18-promo">
        <div class="sn-18__promoin">
          <p class="sn-18__promotext"><strong>Free delivery</strong> on orders over £50 — ends Sunday</p>
          <button class="sn-18__x" type="button" id="sn-18-dismiss" aria-label="Dismiss announcement">
            <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="m4 4 8 8M12 4l-8 8" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
          </button>
        </div>
      </div>
      <header class="sn-18__nav" id="sn-18-nav" tabindex="-1">
        <a class="sn-18__brand" href="#sn-18-s1"><span class="sn-18__logo" aria-hidden="true"></span>Tidewell</a>
        <nav class="sn-18__links" aria-label="Primary">
          <a class="sn-18__link" href="#sn-18-s1" aria-current="page">Shop</a>
          <a class="sn-18__link" href="#sn-18-s2">Delivery</a>
          <a class="sn-18__link" href="#sn-18-s3">Support</a>
        </nav>
        <a class="sn-18__cta" href="#sn-18-s3">Basket</a>
      </header>
  <div class="sn-18__intro">
    <div class="sn-18__introin">
    <p class="sn-18__intro-eyebrow">top: 0 · top: var(--promo)</p>
    <h2 class="sn-18__intro-title">Two bars, one offset chain</h2>
    </div>
  </div>
    </div>
    <main>
      <section class="sn-18__sec" id="sn-18-s1">
        <p class="sn-18__kicker">Offsets</p>
        <h3 class="sn-18__h">Each inset is a running total</h3>
        <p class="sn-18__p">The nav's <code>top</code> equals the promo's height. Dismiss the promo and that token becomes <code>0px</code>, re-seating the nav with no gap left behind.</p>
      </section>
      <section class="sn-18__sec" id="sn-18-s2">
        <p class="sn-18__kicker">Layering</p>
        <h3 class="sn-18__h">DOM order paints backwards</h3>
        <p class="sn-18__p">Without explicit z-index the promo, which comes first, would slide over the nav as they meet. Higher on screen means higher in the stack.</p>
      </section>
      <section class="sn-18__sec" id="sn-18-s3">
        <p class="sn-18__kicker">Anchors</p>
        <h3 class="sn-18__h">Scroll padding tracks the same token</h3>
        <p class="sn-18__p">Anchor targets clear both bars because the port's padding is <code>calc(promo + nav)</code>, recalculated automatically when either changes.</p>
      </section>
    </main>
  <footer class="sn-18__pagefoot">
    <p class="sn-18__pagefootin">Sticky navigation pattern 18 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-18 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-18-bg);
  --sn-18-bg: oklch(0.955 0.01 250);
  --sn-18-surface: oklch(0.997 0.002 250);
  --sn-18-ink: oklch(0.22 0.026 258);
  --sn-18-mut: oklch(0.53 0.022 258);
  --sn-18-acc: oklch(0.53 0.18 262);
  --sn-18-line: oklch(0.22 0.026 258/.12);
  --sn-18-promoh: 42px;
  --sn-18-navh: 60px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-18-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-18 *,
.sn-18 *::before,
.sn-18 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-18__eyebrow,
.sn-18__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sn-18-acc);
}

.sn-18__title,
.sn-18__intro-title {
  font-size: clamp(23px,3.5vw,36px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-18__wrap {
  display: contents;
}

.sn-18__promo {
  position: sticky;
  top: 0;
  z-index: 30;
  display: grid;
  grid-template-rows: 1fr;
  background: linear-gradient(100deg,var(--sn-18-acc),oklch(0.6 0.17 300));
  color: oklch(1 0 0);
  transition: grid-template-rows .32s cubic-bezier(.32,.72,.3,1);
}

.sn-18__promoin {
  overflow: hidden;
  min-height: 0;
  display: flex;
  align-items: center;
  gap: 12px;
  block-size: var(--sn-18-promoh);
  padding: 0 12px 0 clamp(14px,2.6vw,22px);
}

.sn-18__promotext {
  flex: 1;
  font-size: 12.8px;
  letter-spacing: .005em;
  text-wrap: pretty;
}

.sn-18__promotext strong {
  font-weight: 700;
}

.sn-18__x {
  display: grid;
  place-items: center;
  inline-size: 30px;
  block-size: 30px;
  border: 0;
  border-radius: 8px;
  background: oklch(1 0 0/.14);
  color: inherit;
  cursor: pointer;
  transition: background .18s ease;
}

.sn-18__x:hover {
  background: oklch(1 0 0/.26);
}

.sn-18__x svg {
  inline-size: 14px;
  block-size: 14px;
}

.sn-18__x:focus-visible {
  outline: 2px solid oklch(1 0 0);
  outline-offset: 2px;
}

.sn-18__wrap[data-dismissed="true"] {
  --sn-18-promoh: 0px;
}

.sn-18__wrap[data-dismissed="true"] .sn-18__promo {
  grid-template-rows: 0fr;
}

.sn-18__nav {
  position: sticky;
  top: var(--sn-18-promoh);
  z-index: 20;
  display: flex;
  align-items: center;
  gap: clamp(10px,2vw,22px);
  block-size: var(--sn-18-navh);
  padding: 0 clamp(14px,2.6vw,22px);
  background: color-mix(in oklch,var(--sn-18-surface) 88%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--sn-18-line);
  transition: top .32s cubic-bezier(.32,.72,.3,1);
}

.sn-18__nav:focus {
  outline: none;
}

.sn-18__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.025em;
  color: inherit;
  text-decoration: none;
}

.sn-18__logo {
  width: 19px;
  height: 19px;
  border-radius: 6px;
  background: var(--sn-18-acc);
}

.sn-18__links {
  display: flex;
  align-items: center;
  gap: 2px;
  margin-inline-start: auto;
}

.sn-18__link {
  display: flex;
  align-items: center;
  min-height: 36px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 13.5px;
  font-weight: 600;
  color: var(--sn-18-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.sn-18__link:hover {
  color: var(--sn-18-ink);
  background: oklch(0.22 0.026 258/.05);
}

.sn-18__link[aria-current="page"] {
  color: var(--sn-18-acc);
}

.sn-18__cta {
  display: flex;
  align-items: center;
  min-height: 36px;
  padding: 0 15px;
  border-radius: 9px;
  font-size: 13.2px;
  font-weight: 660;
  color: oklch(1 0 0);
  background: var(--sn-18-ink);
  text-decoration: none;
  transition: background .2s ease;
}

.sn-18__cta:hover {
  background: var(--sn-18-acc);
}

.sn-18__link:focus-visible,
.sn-18__cta:focus-visible,
.sn-18__brand:focus-visible {
  outline: 2px solid var(--sn-18-acc);
  outline-offset: 2px;
}

.sn-18__sec {
  scroll-margin-top: calc(var(--sn-18-promoh) + var(--sn-18-navh));
  display: grid;
  gap: 10px;
  align-content: center;
  min-height: 66svh;
  padding: clamp(24px,4vw,46px);
  border-bottom: 1px solid var(--sn-18-line);
}

.sn-18__sec:nth-child(even) {
  background: oklch(0.98 0.006 258);
}

.sn-18__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sn-18-acc);
}

.sn-18__h {
  font-size: clamp(19px,2.6vw,26px);
  line-height: 1.16;
  letter-spacing: -.025em;
  font-weight: 690;
  text-wrap: balance;
}

.sn-18__p {
  max-width: 52ch;
  font-size: 14.8px;
  line-height: 1.64;
  color: var(--sn-18-mut);
  text-wrap: pretty;
}

.sn-18__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.22 0.026 258/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

@media (max-width: 560px) {
  .sn-18 {
    --sn-18-promoh: 52px;
  }

  .sn-18__promotext {
    font-size: 12px;
  }

  .sn-18__cta {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-18 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-18) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-18-promoh) + var(--sn-18-navh) + 8px);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-18) {
    scroll-behavior: auto;
  }
}

.sn-18__bar,
.sn-18__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-18__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-18__intro {
  display: grid;
  place-items: center;
  min-height: min(90svh,900px);
  padding: clamp(56px,12vh,150px) clamp(20px,5vw,48px) clamp(40px,8vh,90px);
}

.sn-18__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-width: 26ch;
}

.sn-18__intro-eyebrow {
  font-size: clamp(11px,1.1vw,13px);
}

.sn-18__intro-title {
  font-size: clamp(38px,7.5vw,86px);
  line-height: .98;
  letter-spacing: -.04em;
  max-width: none;
}

.sn-18__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  max-width: 46ch;
}

.sn-18__intro::after {
  content: "Scroll — the bar stays";
  justify-self: center;
  margin-block-start: clamp(20px,4vh,44px);
  padding: 9px 18px;
  border: 1px solid var(--sn-18-line);
  border-radius: 99px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sn-18-mut);
  animation: sn-18-cue 2.6s ease-in-out infinite;
}

@keyframes sn-18-cue {
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
  .sn-18__intro::after {
    animation: none;
  }
}

.sn-18__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-18-line);
}

.sn-18__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-18-mut);
  text-align: center;
}

.sn-18__intro-title,
.sn-18__intro-sub {
  text-wrap: balance;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sn-18');
  if (!root || root.dataset.snWired) return;
  root.dataset.snWired = '1';
  const wrap = root.querySelector('#sn-18-wrap');
  const nav = root.querySelector('#sn-18-nav');
  root.querySelector('#sn-18-dismiss').addEventListener('click', () => {
    wrap.dataset.dismissed = 'true';
    nav.focus({ preventScroll: true });
  });
})();
```
