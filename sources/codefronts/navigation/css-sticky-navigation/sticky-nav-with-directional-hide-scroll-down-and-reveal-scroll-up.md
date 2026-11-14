---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/sticky-nav-with-directional-hide-scroll-down-and-reveal-scroll-up/"
title: "Sticky Nav with Directional Hide (Scroll Down) and Reveal (Scroll Up)"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "Reading-first navigation: the header slides out of the way while the reader moves down the page and snaps back the instant they scroll up, so the nav is…"
has_js: "true"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Nav with Directional Hide (Scroll Down) and Reveal (Scroll Up)
Source: https://codefronts.com/navigation/css-sticky-navigation/sticky-nav-with-directional-hide-scroll-down-and-reveal-scroll-up/

Reading-first navigation: the header slides out of the way while the reader moves down the page and snaps back the instant they scroll up, so the nav is always one small gesture away without permanently costing 64px of screen. The demo focuses on the two details that separate a polished implementation from a twitchy one — a movement dead zone and a rest state at the very top.
## HTML
```html
<section class="sn-07" aria-label="Directional hide and reveal sticky nav demo">
    <header class="sn-07__bar" id="sn-07-bar" data-hidden="false">
      <a class="sn-07__brand" href="#sn-07-s1"><span class="sn-07__logo" aria-hidden="true"></span>Dispatch</a>
      <nav class="sn-07__nav" aria-label="Primary">
        <a class="sn-07__link" href="#sn-07-s1" aria-current="page">World</a>
        <a class="sn-07__link" href="#sn-07-s2">Business</a>
        <a class="sn-07__link" href="#sn-07-s3">Culture</a>
      </nav>
      <span class="sn-07__state" id="sn-07-state" aria-live="off">visible</span>
    </header>
  <div class="sn-07__intro">
    <div class="sn-07__introin">
    <p class="sn-07__intro-eyebrow">scroll delta · dead zone · rAF</p>
    <h2 class="sn-07__intro-title">Down it goes, up it comes back</h2>
    <p class="sn-07__intro-sub">Scroll down past the intro, then reverse by a few pixels.</p>
    </div>
  </div>
    <main>
      <section class="sn-07__sec" id="sn-07-s1">
        <p class="sn-07__kicker">World</p>
        <h3 class="sn-07__h">Screen space back to the reader</h3>
        <p class="sn-07__p">A permanently pinned bar costs 64px on every screen of a long article. Directional hiding gives that space back and keeps the nav one gesture away.</p>
      </section>
      <section class="sn-07__sec" id="sn-07-s2">
        <p class="sn-07__kicker">Business</p>
        <h3 class="sn-07__h">The dead zone matters most</h3>
        <p class="sn-07__p">Without a movement threshold the bar flickers on trackpad jitter and elastic bounce. Six pixels is usually the sweet spot.</p>
      </section>
      <section class="sn-07__sec" id="sn-07-s3">
        <p class="sn-07__kicker">Culture</p>
        <h3 class="sn-07__h">Never hide near the top</h3>
        <p class="sn-07__p">Inside the first 120px, hiding reads as a bug. The rest zone keeps the header planted where users expect to find it.</p>
      </section>
      <section class="sn-07__sec">
        <p class="sn-07__kicker">Accessibility</p>
        <h3 class="sn-07__h">Focus pulls it back</h3>
        <p class="sn-07__p">A <code>:focus-within</code> rule overrides the hidden state, so tabbing into the nav can never leave a keyboard user chasing an off-screen link.</p>
      </section>
    </main>
  <footer class="sn-07__pagefoot">
    <p class="sn-07__pagefootin">Sticky navigation pattern 07 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-07 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-07-bg);
  --sn-07-bg: oklch(0.17 0.02 275);
  --sn-07-surface: oklch(0.215 0.024 275);
  --sn-07-ink: oklch(0.97 0.006 275);
  --sn-07-mut: oklch(0.72 0.018 275);
  --sn-07-acc: oklch(0.82 0.17 85);
  --sn-07-line: oklch(1 0 0/.1);
  --sn-07-h: 62px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-07-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-07 *,
.sn-07 *::before,
.sn-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-07__eyebrow,
.sn-07__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sn-07-acc);
}

.sn-07__title,
.sn-07__intro-title {
  font-size: clamp(23px,3.5vw,37px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-07__sub,
.sn-07__intro-sub {
  font-size: 14.4px;
  line-height: 1.6;
  color: var(--sn-07-mut);
  text-wrap: pretty;
}

.sn-07__bar {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  gap: clamp(10px,2vw,22px);
  min-height: var(--sn-07-h);
  padding: 0 clamp(14px,2.4vw,22px);
  background: color-mix(in oklch,var(--sn-07-surface) 84%,transparent);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--sn-07-line);
  will-change: translate;
  transition: translate .34s cubic-bezier(.32,.72,.3,1);
}

.sn-07__bar[data-hidden="true"] {
  translate: 0 -100%;
}

.sn-07__bar:focus-within {
  translate: 0 0;
}

.sn-07__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.025em;
  color: inherit;
  text-decoration: none;
}

.sn-07__logo {
  width: 20px;
  height: 20px;
  border-radius: 5px;
  background: var(--sn-07-acc);
  clip-path: polygon(0 0,100% 0,100% 62%,50% 100%,0 62%);
}

.sn-07__nav {
  display: flex;
  align-items: center;
  gap: 2px;
  margin-inline-start: auto;
}

.sn-07__link {
  display: flex;
  align-items: center;
  min-height: 36px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 13.6px;
  font-weight: 600;
  color: var(--sn-07-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.sn-07__link:hover {
  color: var(--sn-07-ink);
  background: oklch(1 0 0/.07);
}

.sn-07__link[aria-current="page"] {
  color: var(--sn-07-acc);
}

.sn-07__link:focus-visible,
.sn-07__brand:focus-visible {
  outline: 2px solid var(--sn-07-acc);
  outline-offset: 2px;
}

.sn-07__state {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sn-07-acc);
  padding: 5px 11px;
  border-radius: 99px;
  border: 1px solid color-mix(in oklch,var(--sn-07-acc) 32%,transparent);
  background: color-mix(in oklch,var(--sn-07-acc) 10%,transparent);
  white-space: nowrap;
}

.sn-07__sec {
  scroll-margin-top: var(--sn-07-h);
  display: grid;
  gap: 10px;
  align-content: center;
  min-height: 66svh;
  padding: clamp(24px,4vw,44px);
  border-bottom: 1px solid var(--sn-07-line);
}

.sn-07__sec:nth-child(even) {
  background: oklch(1 0 0/.025);
}

.sn-07__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sn-07-acc);
}

.sn-07__h {
  font-size: clamp(19px,2.6vw,26px);
  line-height: 1.16;
  letter-spacing: -.025em;
  font-weight: 690;
  text-wrap: balance;
}

.sn-07__p {
  max-width: 52ch;
  font-size: 14.8px;
  line-height: 1.64;
  color: var(--sn-07-mut);
  text-wrap: pretty;
}

.sn-07__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(1 0 0/.09);
  padding: 2px 6px;
  border-radius: 5px;
}

@media (max-width: 560px) {
  .sn-07__state {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-07__bar[data-hidden="true"] {
    translate: 0 0;
  }

  .sn-07 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-07) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-07-h) + 10px);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-07) {
    scroll-behavior: auto;
  }
}

.sn-07__bar,
.sn-07__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-07__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-07__intro {
  display: grid;
  place-items: center;
  min-height: min(90svh,900px);
  padding: clamp(56px,12vh,150px) clamp(20px,5vw,48px) clamp(40px,8vh,90px);
  background: radial-gradient(85% 55% at 50% 0%,oklch(0.3 0.06 85/.4),transparent);
}

.sn-07__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-width: 26ch;
}

.sn-07__intro-eyebrow {
  font-size: clamp(11px,1.1vw,13px);
}

.sn-07__intro-title {
  font-size: clamp(38px,7.5vw,86px);
  line-height: .98;
  letter-spacing: -.04em;
  max-width: none;
}

.sn-07__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  max-width: 46ch;
}

.sn-07__intro::after {
  content: "Scroll — the bar stays";
  justify-self: center;
  margin-block-start: clamp(20px,4vh,44px);
  padding: 9px 18px;
  border: 1px solid var(--sn-07-line);
  border-radius: 99px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sn-07-mut);
  animation: sn-07-cue 2.6s ease-in-out infinite;
}

@keyframes sn-07-cue {
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
  .sn-07__intro::after {
    animation: none;
  }
}

.sn-07__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-07-line);
}

.sn-07__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-07-mut);
  text-align: center;
}

.sn-07__intro-title,
.sn-07__intro-sub {
  text-wrap: balance;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sn-07');
  if (!root || root.dataset.snWired) return;
  root.dataset.snWired = '1';
  const bar = root.querySelector('#sn-07-bar');
  const label = root.querySelector('#sn-07-state');
  let last = 0, ticking = false;
  window.addEventListener('scroll', () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      const y = window.scrollY;
      if (Math.abs(y - last) > 6) {
        const hide = y > last && y > 120;
        bar.dataset.hidden = String(hide);
        label.textContent = hide ? 'hidden' : 'visible';
        last = y;
      }
      ticking = false;
    });
  }, { passive: true });
})();
```
