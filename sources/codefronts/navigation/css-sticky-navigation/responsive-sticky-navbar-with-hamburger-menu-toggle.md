---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/responsive-sticky-navbar-with-hamburger-menu-toggle/"
title: "Responsive Sticky Navbar with Hamburger Menu Toggle"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "The mobile header that ships on most marketing sites, built the way an accessibility audit expects it: a real button that reports its state, a drawer that…"
has_js: "true"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Responsive Sticky Navbar with Hamburger Menu Toggle
Source: https://codefronts.com/navigation/css-sticky-navigation/responsive-sticky-navbar-with-hamburger-menu-toggle/

The mobile header that ships on most marketing sites, built the way an accessibility audit expects it: a real button that reports its state, a drawer that traps nothing but is properly hidden from assistive tech when closed, Escape and outside-click dismissal, and focus that returns to the toggle. The hamburger-to-close morph is pure CSS transforms.
## HTML
```html
<section class="sn-03" aria-label="Responsive sticky navbar with hamburger menu demo">
    <div class="sn-03__sticky">
      <header class="sn-03__bar">
        <a class="sn-03__brand" href="#sn-03-s1"><span class="sn-03__logo" aria-hidden="true"></span>Fernway</a>
        <button class="sn-03__burger" type="button" id="sn-03-burger" aria-expanded="false" aria-controls="sn-03-drawer" aria-label="Open main menu">
          <span class="sn-03__bars" aria-hidden="true"><i class="sn-03__b1"></i><i class="sn-03__b2"></i><i class="sn-03__b3"></i></span>
        </button>
      </header>
      <nav class="sn-03__drawer" id="sn-03-drawer" aria-label="Main" inert>
        <a class="sn-03__dlink" href="#sn-03-s1" aria-current="page">Trips</a>
        <a class="sn-03__dlink" href="#sn-03-s2">Stays</a>
        <a class="sn-03__dlink" href="#sn-03-s3">Guides</a>
        <a class="sn-03__dlink" href="#sn-03-s4">Account</a>
        <a class="sn-03__dcta" href="#sn-03-s4">Plan a trip</a>
      </nav>
    </div>
    <main>
      <div class="sn-03__intro">
        <div class="sn-03__introin">
          <p class="sn-03__intro-eyebrow">aria-expanded · :has() · inert</p>
          <h2 class="sn-03__intro-title">Hamburger menu that passes review</h2>
          <p class="sn-03__intro-sub">Tap the button, then press Escape or click the page behind it. The bar stays pinned the whole way down.</p>
        </div>
      </div>
      <section class="sn-03__sec" id="sn-03-s1">
        <p class="sn-03__kicker">Trips</p>
        <h3 class="sn-03__h">One source of truth</h3>
        <p class="sn-03__p">The open styles key off <code>aria-expanded="true"</code> itself, so the visual state and the announced state can never disagree.</p>
      </section>
      <section class="sn-03__sec" id="sn-03-s2">
        <p class="sn-03__kicker">Stays</p>
        <h3 class="sn-03__h">Closed means closed</h3>
        <p class="sn-03__p">The drawer carries <code>inert</code> while shut — out of the tab order and out of the accessibility tree, but still animatable.</p>
      </section>
      <section class="sn-03__sec" id="sn-03-s3">
        <p class="sn-03__kicker">Guides</p>
        <h3 class="sn-03__h">Escape, outside click, focus return</h3>
        <p class="sn-03__p">Fourteen lines of script cover the three dismissal behaviours users expect from every menu on the web.</p>
      </section>
      <section class="sn-03__sec" id="sn-03-s4">
        <p class="sn-03__kicker">Account</p>
        <h3 class="sn-03__h">Sticky, not fixed</h3>
        <p class="sn-03__p">Bar and drawer share one sticky wrapper, so the panel stays attached to the header instead of drifting up the page.</p>
      </section>
    </main>
  <footer class="sn-03__pagefoot">
    <p class="sn-03__pagefootin">Sticky navigation pattern 03 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-03 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-03-bg);
  --sn-03-bg: oklch(0.965 0.012 80);
  --sn-03-surface: oklch(1 0 0);
  --sn-03-ink: oklch(0.24 0.03 60);
  --sn-03-mut: oklch(0.56 0.03 60);
  --sn-03-acc: oklch(0.62 0.17 32);
  --sn-03-line: oklch(0.24 0.03 60/.12);
  --sn-03-h: 58px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-03-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-03 *,
.sn-03 *::before,
.sn-03 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-03__eyebrow,
.sn-03__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sn-03-acc);
}

.sn-03__title,
.sn-03__intro-title {
  font-size: clamp(23px,3.5vw,36px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-03__sub,
.sn-03__intro-sub {
  font-size: 14.4px;
  line-height: 1.6;
  color: var(--sn-03-mut);
  text-wrap: pretty;
}

.sn-03__sticky {
  position: sticky;
  top: 0;
  z-index: 20;
}

.sn-03__bar {
  position: relative;
  z-index: 2;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  min-height: var(--sn-03-h);
  padding: 0 12px 0 16px;
  background: color-mix(in oklch,var(--sn-03-surface) 88%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--sn-03-line);
}

.sn-03__brand {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
}

.sn-03__logo {
  width: 18px;
  height: 18px;
  border-radius: 6px;
  background: linear-gradient(140deg,var(--sn-03-acc),oklch(0.78 0.15 70));
}

.sn-03__burger {
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border: 0;
  border-radius: 12px;
  background: transparent;
  color: inherit;
  cursor: pointer;
  transition: background .18s ease;
}

.sn-03__burger:hover {
  background: oklch(0.24 0.03 60/.06);
}

.sn-03__burger:focus-visible {
  outline: 2px solid var(--sn-03-acc);
  outline-offset: 2px;
}

.sn-03__bars {
  position: relative;
  display: block;
  width: 19px;
  height: 13px;
}

.sn-03__bars i {
  position: absolute;
  left: 0;
  width: 19px;
  height: 2px;
  border-radius: 2px;
  background: currentColor;
  transition: translate .28s cubic-bezier(.32,.72,.3,1),rotate .28s cubic-bezier(.32,.72,.3,1),opacity .18s ease;
}

.sn-03__b1 {
  top: 0;
}

.sn-03__b2 {
  top: 5.5px;
}

.sn-03__b3 {
  top: 11px;
}

.sn-03__burger[aria-expanded="true"] .sn-03__b1 {
  translate: 0 5.5px;
  rotate: 45deg;
}

.sn-03__burger[aria-expanded="true"] .sn-03__b2 {
  opacity: 0;
  scale: .4 1;
}

.sn-03__burger[aria-expanded="true"] .sn-03__b3 {
  translate: 0 -5.5px;
  rotate: -45deg;
}

.sn-03__drawer {
  position: absolute;
  inset-inline: 0;
  top: 100%;
  z-index: 1;
  display: grid;
  gap: 2px;
  padding: 10px;
  background: var(--sn-03-surface);
  border-bottom: 1px solid var(--sn-03-line);
  box-shadow: 0 22px 34px -22px oklch(0.24 0.03 60/.4);
  translate: 0 -8px;
  opacity: 0;
  visibility: hidden;
  transition: translate .3s cubic-bezier(.32,.72,.3,1),opacity .24s ease,visibility 0s .3s;
}

.sn-03__sticky:has(.sn-03__burger[aria-expanded="true"]) .sn-03__drawer {
  translate: 0 0;
  opacity: 1;
  visibility: visible;
  transition-delay: 0s;
}

.sn-03__dlink {
  display: flex;
  align-items: center;
  min-height: 46px;
  padding: 0 14px;
  border-radius: 11px;
  font-size: 15px;
  font-weight: 620;
  color: var(--sn-03-mut);
  text-decoration: none;
  transition: color .16s ease,background .16s ease;
}

.sn-03__dlink:hover {
  color: var(--sn-03-ink);
  background: oklch(0.24 0.03 60/.05);
}

.sn-03__dlink[aria-current="page"] {
  color: var(--sn-03-acc);
  background: color-mix(in oklch,var(--sn-03-acc) 10%,transparent);
}

.sn-03__dcta {
  display: grid;
  place-items: center;
  min-height: 46px;
  margin-block-start: 6px;
  border-radius: 11px;
  font-size: 14.5px;
  font-weight: 670;
  color: oklch(1 0 0);
  background: var(--sn-03-acc);
  text-decoration: none;
}

.sn-03__dlink:focus-visible,
.sn-03__dcta:focus-visible,
.sn-03__brand:focus-visible {
  outline: 2px solid var(--sn-03-acc);
  outline-offset: 2px;
}

.sn-03__sec {
  scroll-margin-top: var(--sn-03-h);
  display: grid;
  gap: 9px;
  align-content: center;
  min-height: 70svh;
  padding: 26px 22px;
  border-bottom: 1px solid var(--sn-03-line);
}

.sn-03__sec:nth-child(even) {
  background: oklch(0.985 0.008 70);
}

.sn-03__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sn-03-acc);
}

.sn-03__h {
  font-size: 20px;
  line-height: 1.18;
  letter-spacing: -.025em;
  font-weight: 690;
  text-wrap: balance;
}

.sn-03__p {
  font-size: 14.2px;
  line-height: 1.6;
  color: var(--sn-03-mut);
  text-wrap: pretty;
}

.sn-03__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .84em;
  background: oklch(0.24 0.03 60/.07);
  padding: 2px 5px;
  border-radius: 5px;
}
/* full-page mode: the demo IS the document, so sticky pins against the real viewport */

:root:has(.sn-03) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-03-h) + 8px);
}

.sn-03__bar {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-03__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-03__intro {
  display: grid;
  place-items: center;
  align-content: center;
  min-height: min(88svh,860px);
  padding: clamp(48px,10vh,120px) clamp(20px,5vw,48px) clamp(40px,8vh,90px);
  background: radial-gradient(90% 55% at 50% 0%,oklch(0.98 0.03 60),transparent);
  border-bottom: 1px solid var(--sn-03-line);
}

.sn-03__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-width: min(100%,60ch);
}

.sn-03__intro-eyebrow {
  font-size: clamp(11px,1.1vw,13px);
}

.sn-03__intro-title {
  font-size: clamp(34px,6.4vw,74px);
  line-height: .99;
  letter-spacing: -.04em;
  max-width: 15ch;
}

.sn-03__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  max-width: 44ch;
}

.sn-03__intro::after {
  content: "Scroll — the bar stays";
  margin-block-start: clamp(20px,4vh,44px);
  padding: 9px 18px;
  border: 1px solid var(--sn-03-line);
  border-radius: 99px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sn-03-mut);
  animation: sn-03-cue 2.6s ease-in-out infinite;
}

@keyframes sn-03-cue {
  0%,
    100% {
    translate: 0 0;
    opacity: .75;
  }

  50% {
    translate: 0 5px;
    opacity: 1;
  }
}

.sn-03__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-03-line);
}

.sn-03__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-03-mut);
  text-align: center;
}

@media (min-width: 720px) {
  .sn-03__burger {
    display: none;
  }

  .sn-03__sticky {
    display: flex;
    align-items: center;
    gap: clamp(12px,2vw,24px);
    min-height: var(--sn-03-h);
    background: color-mix(in oklch,var(--sn-03-surface) 88%,transparent);
    backdrop-filter: blur(14px) saturate(1.4);
    -webkit-backdrop-filter: blur(14px) saturate(1.4);
    border-bottom: 1px solid var(--sn-03-line);
    padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
  }

  .sn-03__bar {
    flex: 1;
    min-width: 0;
    padding-inline: 0;
    border-bottom: 0;
    background: transparent;
    backdrop-filter: none;
    -webkit-backdrop-filter: none;
  }

  .sn-03__drawer {
    position: static;
    display: flex;
    align-items: center;
    gap: 2px;
    padding: 0;
    translate: none;
    opacity: 1;
    visibility: visible;
    box-shadow: none;
    border: 0;
    background: transparent;
    transition: none;
  }

  .sn-03__dlink {
    min-height: 38px;
    padding-inline: 12px;
    font-size: 13.6px;
    border-radius: 9px;
  }

  .sn-03__dcta {
    min-height: 38px;
    margin: 0 0 0 8px;
    padding-inline: 16px;
    font-size: 13.4px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-03 * {
    transition-duration: .01ms !important;
  }

  :root:has(.sn-03) {
    scroll-behavior: auto;
  }

  .sn-03__intro::after {
    animation: none;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sn-03');
  if (!root || root.dataset.snWired) return;
  root.dataset.snWired = '1';
  const btn = root.querySelector('#sn-03-burger');
  const drawer = root.querySelector('#sn-03-drawer');
  const desktop = window.matchMedia('(min-width:720px)');
  const set = (open) => {
    btn.setAttribute('aria-expanded', String(open));
    btn.setAttribute('aria-label', open ? 'Close main menu' : 'Open main menu');
    if (desktop.matches) drawer.removeAttribute('inert');
    else drawer.toggleAttribute('inert', !open);
  };
  btn.addEventListener('click', () => set(btn.getAttribute('aria-expanded') !== 'true'));
  drawer.addEventListener('click', (e) => { if (e.target.closest('a')) set(false); });
  root.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && btn.getAttribute('aria-expanded') === 'true') { set(false); btn.focus(); }
  });
  root.addEventListener('pointerdown', (e) => {
    if (!e.target.closest('.sn-03__sticky') && btn.getAttribute('aria-expanded') === 'true') set(false);
  });
  desktop.addEventListener('change', () => set(false));
  set(false);
})();
```
