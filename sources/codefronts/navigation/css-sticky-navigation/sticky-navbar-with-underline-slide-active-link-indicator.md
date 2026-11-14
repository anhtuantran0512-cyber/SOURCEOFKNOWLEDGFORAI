---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/sticky-navbar-with-underline-slide-active-link-indicator/"
title: "Sticky Navbar with Underline-Slide Active Link Indicator"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "The indicator that glides between links instead of fading in place — the detail that makes a header feel engineered rather than assembled."
has_js: "true"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Navbar with Underline-Slide Active Link Indicator
Source: https://codefronts.com/navigation/css-sticky-navigation/sticky-navbar-with-underline-slide-active-link-indicator/

The indicator that glides between links instead of fading in place — the detail that makes a header feel engineered rather than assembled. One shared underline element is translated and resized to whatever link is hovered, focused or current, so the motion always reads as a single object moving, not four separate underlines taking turns.
## HTML
```html
<section class="sn-11" aria-label="Underline slide active link indicator demo">
    <header class="sn-11__bar">
      <a class="sn-11__brand" href="#sn-11-s1"><span class="sn-11__logo" aria-hidden="true"></span>Vector</a>
      <nav class="sn-11__nav" id="sn-11-nav" aria-label="Primary">
        <a class="sn-11__link" href="#sn-11-s1" aria-current="page">Overview</a>
        <a class="sn-11__link" href="#sn-11-s2">Integrations</a>
        <a class="sn-11__link" href="#sn-11-s3">Pricing</a>
        <a class="sn-11__link" href="#sn-11-s4">Docs</a>
        <span class="sn-11__ind" id="sn-11-ind" aria-hidden="true"></span>
      </nav>
      <a class="sn-11__cta" href="#sn-11-s4">Sign up</a>
    </header>
  <div class="sn-11__intro">
    <div class="sn-11__introin">
    <p class="sn-11__intro-eyebrow">--x · --w · one indicator</p>
    <h2 class="sn-11__intro-title">The line follows you</h2>
    <p class="sn-11__intro-sub">Hover the links, then tab through them — the indicator tracks focus too.</p>
    </div>
  </div>
    <main>
      <section class="sn-11__sec" id="sn-11-s1">
        <p class="sn-11__kicker">Overview</p>
        <h3 class="sn-11__h">One object, moving</h3>
        <p class="sn-11__p">Four separate underlines fading in and out read as four things. A single element that travels reads as one thing — and that is the whole perceptual difference.</p>
      </section>
      <section class="sn-11__sec" id="sn-11-s2">
        <p class="sn-11__kicker">Integrations</p>
        <h3 class="sn-11__h">Two numbers on a bus</h3>
        <p class="sn-11__p">The script publishes <code>--x</code> and <code>--w</code>. Every visual decision — colour, thickness, easing, shape — stays in the stylesheet where it belongs.</p>
      </section>
      <section class="sn-11__sec" id="sn-11-s3">
        <p class="sn-11__kicker">Pricing</p>
        <h3 class="sn-11__h">Focus gets the same treatment</h3>
        <p class="sn-11__p">Keyboard users see the indicator move as they tab, because <code>focus</code> is bound next to <code>pointerenter</code> in the same handler.</p>
      </section>
      <section class="sn-11__sec" id="sn-11-s4">
        <p class="sn-11__kicker">Docs</p>
        <h3 class="sn-11__h">It settles back to the truth</h3>
        <p class="sn-11__p">Leaving the nav returns the line to the link marked <code>aria-current="page"</code>, so the header never lies about where you are.</p>
      </section>
    </main>
  <footer class="sn-11__pagefoot">
    <p class="sn-11__pagefootin">Sticky navigation pattern 11 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-11 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-11-bg);
  --sn-11-bg: oklch(0.16 0.018 265);
  --sn-11-surface: oklch(0.205 0.022 265);
  --sn-11-ink: oklch(0.98 0.005 265);
  --sn-11-mut: oklch(0.7 0.016 265);
  --sn-11-acc: oklch(0.75 0.17 145);
  --sn-11-line: oklch(1 0 0/.1);
  --sn-11-h: 66px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-11-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-11 *,
.sn-11 *::before,
.sn-11 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-11__eyebrow,
.sn-11__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sn-11-acc);
}

.sn-11__title,
.sn-11__intro-title {
  font-size: clamp(23px,3.5vw,37px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-11__sub,
.sn-11__intro-sub {
  font-size: 14.4px;
  line-height: 1.6;
  color: var(--sn-11-mut);
  text-wrap: pretty;
}

.sn-11__bar {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  gap: clamp(10px,2vw,24px);
  min-height: var(--sn-11-h);
  padding: 0 clamp(14px,2.6vw,24px);
  background: color-mix(in oklch,var(--sn-11-surface) 86%,transparent);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--sn-11-line);
}

.sn-11__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.025em;
  color: inherit;
  text-decoration: none;
}

.sn-11__logo {
  width: 18px;
  height: 18px;
  background: var(--sn-11-acc);
  clip-path: polygon(50% 0,100% 100%,0 100%);
}

.sn-11__nav {
  position: relative;
  display: flex;
  align-items: center;
  align-self: stretch;
  gap: 2px;
  margin-inline-start: auto;
}

.sn-11__link {
  display: flex;
  align-items: center;
  padding: 0 14px;
  align-self: stretch;
  font-size: 13.8px;
  font-weight: 600;
  color: var(--sn-11-mut);
  text-decoration: none;
  transition: color .2s ease;
}

.sn-11__link:hover {
  color: var(--sn-11-ink);
}

.sn-11__link[aria-current="page"] {
  color: var(--sn-11-ink);
}

.sn-11__link:focus-visible {
  outline: 2px solid var(--sn-11-acc);
  outline-offset: -4px;
  border-radius: 8px;
}

.sn-11__ind {
  position: absolute;
  inset-block-end: 0;
  inset-inline-start: 0;
  block-size: 2.5px;
  inline-size: var(--sn-11-w,0px);
  translate: var(--sn-11-x,0px) 0;
  border-radius: 99px 99px 0 0;
  background: var(--sn-11-acc);
  box-shadow: 0 0 16px -2px var(--sn-11-acc);
  transition: translate .32s cubic-bezier(.32,.72,.3,1),inline-size .32s cubic-bezier(.32,.72,.3,1),opacity .2s ease;
}

.sn-11__cta {
  display: flex;
  align-items: center;
  min-height: 38px;
  padding: 0 16px;
  border-radius: 9px;
  font-size: 13.4px;
  font-weight: 670;
  color: oklch(0.16 0.018 265);
  background: var(--sn-11-acc);
  text-decoration: none;
  white-space: nowrap;
  transition: transform .18s ease,filter .18s ease;
}

.sn-11__cta:hover {
  transform: translateY(-1px);
  filter: brightness(1.07);
}

.sn-11__cta:focus-visible,
.sn-11__brand:focus-visible {
  outline: 2px solid var(--sn-11-acc);
  outline-offset: 2px;
}

.sn-11__sec {
  scroll-margin-top: var(--sn-11-h);
  display: grid;
  gap: 10px;
  align-content: center;
  min-height: 66svh;
  padding: clamp(24px,4vw,46px);
  border-bottom: 1px solid var(--sn-11-line);
}

.sn-11__sec:nth-child(even) {
  background: oklch(1 0 0/.025);
}

.sn-11__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sn-11-acc);
}

.sn-11__h {
  font-size: clamp(19px,2.6vw,26px);
  line-height: 1.16;
  letter-spacing: -.025em;
  font-weight: 690;
  text-wrap: balance;
}

.sn-11__p {
  max-width: 52ch;
  font-size: 14.8px;
  line-height: 1.64;
  color: var(--sn-11-mut);
  text-wrap: pretty;
}

.sn-11__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(1 0 0/.09);
  padding: 2px 6px;
  border-radius: 5px;
}

@media (max-width: 680px) {
  .sn-11__cta {
    display: none;
  }

  .sn-11__link {
    padding: 0 10px;
    font-size: 12.8px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-11 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-11) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-11-h) + 8px);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-11) {
    scroll-behavior: auto;
  }
}

.sn-11__bar,
.sn-11__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-11__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-11__intro {
  display: grid;
  place-items: center;
  min-height: min(90svh,900px);
  padding: clamp(56px,12vh,150px) clamp(20px,5vw,48px) clamp(40px,8vh,90px);
  background: radial-gradient(80% 55% at 50% 0%,oklch(0.28 0.07 150/.5),transparent);
}

.sn-11__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-width: 26ch;
}

.sn-11__intro-eyebrow {
  font-size: clamp(11px,1.1vw,13px);
}

.sn-11__intro-title {
  font-size: clamp(38px,7.5vw,86px);
  line-height: .98;
  letter-spacing: -.04em;
  max-width: none;
}

.sn-11__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  max-width: 46ch;
}

.sn-11__intro::after {
  content: "Scroll — the bar stays";
  justify-self: center;
  margin-block-start: clamp(20px,4vh,44px);
  padding: 9px 18px;
  border: 1px solid var(--sn-11-line);
  border-radius: 99px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sn-11-mut);
  animation: sn-11-cue 2.6s ease-in-out infinite;
}

@keyframes sn-11-cue {
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
  .sn-11__intro::after {
    animation: none;
  }
}

.sn-11__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-11-line);
}

.sn-11__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-11-mut);
  text-align: center;
}

.sn-11__intro-title,
.sn-11__intro-sub {
  text-wrap: balance;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sn-11');
  if (!root || root.dataset.snWired) return;
  root.dataset.snWired = '1';
  const nav = root.querySelector('#sn-11-nav');
  const links = [...nav.querySelectorAll('.sn-11__link')];
  const move = (el) => {
    if (!el) return;
    nav.style.setProperty('--sn-11-x', el.offsetLeft + 'px');
    nav.style.setProperty('--sn-11-w', el.offsetWidth + 'px');
  };
  const home = () => move(nav.querySelector('[aria-current="page"]') || links[0]);
  links.forEach((a) => {
    a.addEventListener('pointerenter', () => move(a));
    a.addEventListener('focus', () => move(a));
    a.addEventListener('click', () => {
      links.forEach((l) => l.removeAttribute('aria-current'));
      a.setAttribute('aria-current', 'page');
    });
  });
  nav.addEventListener('pointerleave', home);
  nav.addEventListener('focusout', (e) => { if (!nav.contains(e.relatedTarget)) home(); });
  new ResizeObserver(home).observe(nav);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(home);
  home();
})();
```
