---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/sticky-header-shrink-on-scroll-80px-50px-compact-state/"
title: "Sticky Header Shrink on Scroll (80px → 50px, Compact State)"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "The tall-at-rest header that compacts into a slim bar once the reader is past the first screen — buying back vertical space on long pages without ever losing…"
has_js: "true"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Header Shrink on Scroll (80px → 50px, Compact State)
Source: https://codefronts.com/navigation/css-sticky-navigation/sticky-header-shrink-on-scroll-80px-50px-compact-state/

The tall-at-rest header that compacts into a slim bar once the reader is past the first screen — buying back vertical space on long pages without ever losing the navigation. Driven by a scroll-progress timeline in CSS, so the shrink interpolates smoothly with the scroll position instead of snapping at a threshold, with a small script covering engines that have not shipped the timeline yet.
## HTML
```html
<section class="sn-06" aria-label="Sticky header shrink on scroll demo">
    <header class="sn-06__bar" id="sn-06-bar">
      <a class="sn-06__brand" href="#sn-06-s1"><span class="sn-06__logo" aria-hidden="true">N</span><span class="sn-06__word">Northbound</span></a>
      <nav class="sn-06__nav" aria-label="Primary">
        <a class="sn-06__link" href="#sn-06-s1" aria-current="page">Routes</a>
        <a class="sn-06__link" href="#sn-06-s2">Fleet</a>
        <a class="sn-06__link" href="#sn-06-s3">Fares</a>
      </nav>
      <a class="sn-06__cta" href="#sn-06-s3">Book</a>
    </header>
  <div class="sn-06__intro">
    <div class="sn-06__introin">
    <p class="sn-06__intro-eyebrow">animation-timeline: scroll() · @property</p>
    <h2 class="sn-06__intro-title">80px at rest, 50px in motion</h2>
    <p class="sn-06__intro-sub">Scroll slowly — the bar interpolates with position, it does not snap at a threshold.</p>
    </div>
  </div>
    <main>
      <section class="sn-06__sec" id="sn-06-s1">
        <p class="sn-06__kicker">Routes</p>
        <h3 class="sn-06__h">Off the main thread</h3>
        <p class="sn-06__p">A scroll-progress timeline is evaluated by the compositor. The bar keeps shrinking smoothly even while the main thread is busy parsing or hydrating.</p>
      </section>
      <section class="sn-06__sec" id="sn-06-s2">
        <p class="sn-06__kicker">Fleet</p>
        <h3 class="sn-06__h">Registered, therefore animatable</h3>
        <p class="sn-06__p">Height, padding and logo scale are all <code>@property</code> tokens. Without registration the browser treats them as strings and flips them at the halfway point.</p>
      </section>
      <section class="sn-06__sec" id="sn-06-s3">
        <p class="sn-06__kicker">Fares</p>
        <h3 class="sn-06__h">One value to tune</h3>
        <p class="sn-06__p">The entire feel of the effect lives in <code>animation-range</code>. No thresholds, no listener, no rAF loop to debounce.</p>
      </section>
      <section class="sn-06__sec sn-06__sec--end">
        <p class="sn-06__kicker">Fallback</p>
        <h3 class="sn-06__h">Identical without a timeline</h3>
        <p class="sn-06__p">Engines that lack scroll timelines get a nine-line listener toggling <code>data-compact</code>, transitioned by the same tokens.</p>
      </section>
    </main>
  <footer class="sn-06__pagefoot">
    <p class="sn-06__pagefootin">Sticky navigation pattern 06 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
@property --sn-06-h {
  syntax: '<length>';
  inherits: true;
  initial-value: 80px;
}

@property --sn-06-pad {
  syntax: '<length>';
  inherits: true;
  initial-value: 26px;
}

@property --sn-06-scale {
  syntax: '<number>';
  inherits: true;
  initial-value: 1;
}

@property --sn-06-shadow {
  syntax: '<number>';
  inherits: true;
  initial-value: 0;
}

.sn-06 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-06-bg);
  --sn-06-bg: oklch(0.96 0.01 230);
  --sn-06-surface: oklch(1 0 0);
  --sn-06-ink: oklch(0.22 0.03 245);
  --sn-06-mut: oklch(0.54 0.025 245);
  --sn-06-acc: oklch(0.55 0.16 250);
  --sn-06-line: oklch(0.22 0.03 245/.12);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-06-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-06 *,
.sn-06 *::before,
.sn-06 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-06__eyebrow,
.sn-06__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sn-06-acc);
}

.sn-06__title,
.sn-06__intro-title {
  font-size: clamp(23px,3.5vw,37px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-06__sub,
.sn-06__intro-sub {
  font-size: 14.4px;
  line-height: 1.6;
  color: var(--sn-06-mut);
  text-wrap: pretty;
}

.sn-06__bar {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  gap: clamp(10px,2vw,22px);
  block-size: var(--sn-06-h);
  padding-inline: var(--sn-06-pad);
  background: color-mix(in oklch,var(--sn-06-surface) 86%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--sn-06-line);
  box-shadow: 0 10px 30px -18px oklch(0.22 0.03 245/calc(var(--sn-06-shadow)*.9));
  animation: sn-06-shrink linear both;
  animation-timeline: scroll(nearest block);
  animation-range: 0 140px;
}

@keyframes sn-06-shrink {
  to {
    --sn-06-h: 50px;
    --sn-06-pad: 14px;
    --sn-06-scale: .8;
    --sn-06-shadow: 1;
  }
}

.sn-06__bar[data-compact="true"] {
  --sn-06-h: 50px;
  --sn-06-pad: 14px;
  --sn-06-scale: .8;
  --sn-06-shadow: 1;
}

.sn-06__bar[data-fallback="true"] {
  animation: none;
  transition: block-size .3s cubic-bezier(.32,.72,.3,1),padding-inline .3s cubic-bezier(.32,.72,.3,1),box-shadow .3s ease;
}

.sn-06__brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: calc(17px*var(--sn-06-scale));
  font-weight: 700;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
  white-space: nowrap;
  transition: font-size .12s linear;
}

.sn-06__logo {
  display: grid;
  place-items: center;
  inline-size: calc(34px*var(--sn-06-scale));
  block-size: calc(34px*var(--sn-06-scale));
  border-radius: calc(11px*var(--sn-06-scale));
  font-size: calc(15px*var(--sn-06-scale));
  color: oklch(1 0 0);
  background: linear-gradient(140deg,var(--sn-06-acc),oklch(0.62 0.17 290));
}

.sn-06__nav {
  display: flex;
  align-items: center;
  gap: 2px;
  margin-inline-start: auto;
}

.sn-06__link {
  display: flex;
  align-items: center;
  min-height: 36px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 13.6px;
  font-weight: 600;
  color: var(--sn-06-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.sn-06__link:hover {
  color: var(--sn-06-ink);
  background: oklch(0.22 0.03 245/.05);
}

.sn-06__link[aria-current="page"] {
  color: var(--sn-06-acc);
  background: color-mix(in oklch,var(--sn-06-acc) 10%,transparent);
}

.sn-06__cta {
  display: flex;
  align-items: center;
  min-height: 36px;
  padding: 0 16px;
  border-radius: 9px;
  font-size: 13.4px;
  font-weight: 660;
  color: oklch(1 0 0);
  background: var(--sn-06-acc);
  text-decoration: none;
  transition: transform .18s ease;
}

.sn-06__cta:hover {
  transform: translateY(-1px);
}

.sn-06__link:focus-visible,
.sn-06__cta:focus-visible,
.sn-06__brand:focus-visible {
  outline: 2px solid var(--sn-06-acc);
  outline-offset: 2px;
}

.sn-06__sec {
  scroll-margin-top: 88px;
  display: grid;
  gap: 10px;
  align-content: center;
  min-height: 66svh;
  padding: clamp(24px,4vw,44px);
  border-bottom: 1px solid var(--sn-06-line);
}

.sn-06__sec:nth-child(even) {
  background: oklch(0.985 0.006 245);
}

.sn-06__sec--end {
  border-bottom: 0;
}

.sn-06__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sn-06-acc);
}

.sn-06__h {
  font-size: clamp(19px,2.6vw,26px);
  line-height: 1.16;
  letter-spacing: -.025em;
  font-weight: 690;
  text-wrap: balance;
}

.sn-06__p {
  max-width: 52ch;
  font-size: 14.8px;
  line-height: 1.64;
  color: var(--sn-06-mut);
  text-wrap: pretty;
}

.sn-06__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.22 0.03 245/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

@media (max-width: 560px) {
  .sn-06__word {
    display: none;
  }

  .sn-06__cta {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-06__bar {
    animation: none;
  }

  .sn-06 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-06) {
  scroll-behavior: smooth;
  scroll-padding-top: 88px;
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-06) {
    scroll-behavior: auto;
  }
}

.sn-06__bar,
.sn-06__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-06__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-06__intro {
  display: grid;
  place-items: center;
  min-height: min(90svh,900px);
  padding: clamp(56px,12vh,150px) clamp(20px,5vw,48px) clamp(40px,8vh,90px);
  background: radial-gradient(90% 55% at 50% 0%,oklch(0.98 0.02 250),transparent);
}

.sn-06__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-width: 26ch;
}

.sn-06__intro-eyebrow {
  font-size: clamp(11px,1.1vw,13px);
}

.sn-06__intro-title {
  font-size: clamp(38px,7.5vw,86px);
  line-height: .98;
  letter-spacing: -.04em;
  max-width: none;
}

.sn-06__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  max-width: 46ch;
}

.sn-06__intro::after {
  content: "Scroll — the bar stays";
  justify-self: center;
  margin-block-start: clamp(20px,4vh,44px);
  padding: 9px 18px;
  border: 1px solid var(--sn-06-line);
  border-radius: 99px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sn-06-mut);
  animation: sn-06-cue 2.6s ease-in-out infinite;
}

@keyframes sn-06-cue {
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
  .sn-06__intro::after {
    animation: none;
  }
}

.sn-06__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-06-line);
}

.sn-06__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-06-mut);
  text-align: center;
}

.sn-06__intro-title,
.sn-06__intro-sub {
  text-wrap: balance;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sn-06');
  if (!root || root.dataset.snWired) return;
  root.dataset.snWired = '1';
  if (CSS.supports('animation-timeline: scroll()')) return; // modern engines: CSS already handles it
  const bar = root.querySelector('#sn-06-bar');
  bar.dataset.fallback = 'true';
  const sync = () => bar.dataset.compact = String(window.scrollY > 70);
  window.addEventListener('scroll', sync, { passive: true });
  sync();
})();
```
