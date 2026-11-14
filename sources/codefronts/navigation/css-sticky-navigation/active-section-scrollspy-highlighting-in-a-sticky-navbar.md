---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/active-section-scrollspy-highlighting-in-a-sticky-navbar/"
title: "Active-Section Scrollspy Highlighting in a Sticky Navbar"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "The one-page marketing site problem: as the visitor scrolls through hero, features, pricing and FAQ, the sticky nav has to say where they are."
has_js: "true"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Active-Section Scrollspy Highlighting in a Sticky Navbar
Source: https://codefronts.com/navigation/css-sticky-navigation/active-section-scrollspy-highlighting-in-a-sticky-navbar/

The one-page marketing site problem: as the visitor scrolls through hero, features, pricing and FAQ, the sticky nav has to say where they are. Built on a single observer with the offset maths that keeps the highlight in step with a sticky header — plus the scroll-end fallback that stops the last section being unreachable.
## HTML
```html
<section class="sn-23" aria-label="Scrollspy sticky navigation demo">
    <header class="sn-23__bar">
      <a class="sn-23__brand" href="#sn-23-s1"><span class="sn-23__logo" aria-hidden="true"></span>Northbound</a>
      <nav class="sn-23__nav" id="sn-23-nav" aria-label="Page sections">
        <span class="sn-23__ind" aria-hidden="true"></span>
        <a class="sn-23__link" href="#sn-23-s1" aria-current="location">Overview</a>
        <a class="sn-23__link" href="#sn-23-s2">Features</a>
        <a class="sn-23__link" href="#sn-23-s3">Pricing</a>
        <a class="sn-23__link" href="#sn-23-s4">FAQ</a>
      </nav>
      <p class="sn-23__count" id="sn-23-count" aria-hidden="true">01 / 04</p>
    </header>
    <main>
      <section class="sn-23__sec" id="sn-23-s1">
        <p class="sn-23__kicker">Overview</p>
        <h3 class="sn-23__h">One observer, four sections</h3>
        <p class="sn-23__p">The nav does not listen to scroll events. It reacts to intersection changes on the sections themselves, which is why the highlight stays exact during a fast flick.</p>
      </section>
      <section class="sn-23__sec" id="sn-23-s2">
        <p class="sn-23__kicker">Features</p>
        <h3 class="sn-23__h">rootMargin is the whole trick</h3>
        <p class="sn-23__p">A negative top margin equal to the header height, and a negative bottom margin that shrinks the band to the upper part of the port. Sections become current at reading position, not at first pixel.</p>
      </section>
      <section class="sn-23__sec" id="sn-23-s3">
        <p class="sn-23__kicker">Pricing</p>
        <h3 class="sn-23__h">Ties broken in document order</h3>
        <p class="sn-23__p">Two sections can occupy the band at once. Keeping a set of visible ids and picking the first one stops the flicker you get from taking whichever entry fired last.</p>
      </section>
      <section class="sn-23__sec sn-23__sec--short" id="sn-23-s4">
        <p class="sn-23__kicker">FAQ</p>
        <h3 class="sn-23__h">The short final section</h3>
        <p class="sn-23__p">This block is deliberately too short to fill the band — without the scroll-end fallback its nav entry could never light up. Scroll to the bottom and it does.</p>
      </section>
    </main>
  <footer class="sn-23__pagefoot">
    <p class="sn-23__pagefootin">Sticky navigation pattern 23 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-23 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-23-bg);
  --sn-23-bg: oklch(0.17 0.028 285);
  --sn-23-surface: oklch(0.215 0.032 285);
  --sn-23-ink: oklch(0.97 0.008 285);
  --sn-23-mut: oklch(0.7 0.024 285);
  --sn-23-acc: oklch(0.79 0.16 155);
  --sn-23-line: oklch(1 0 0/.11);
  --sn-23-h: 64px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-23-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-23 *,
.sn-23 *::before,
.sn-23 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-23__bar {
  position: sticky;
  top: 0;
  z-index: 20;
  display: flex;
  align-items: center;
  gap: clamp(10px,2vw,24px);
  min-height: var(--sn-23-h);
  padding: 0 clamp(14px,2.6vw,24px);
  background: color-mix(in oklch,var(--sn-23-surface) 88%,transparent);
  backdrop-filter: blur(16px) saturate(1.5);
  -webkit-backdrop-filter: blur(16px) saturate(1.5);
  border-bottom: 1px solid var(--sn-23-line);
}

.sn-23__brand {
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

.sn-23__logo {
  width: 18px;
  height: 18px;
  border-radius: 5px;
  background: linear-gradient(145deg,var(--sn-23-acc),oklch(0.68 0.15 210));
  box-shadow: 0 4px 14px -4px var(--sn-23-acc);
}

.sn-23__nav {
  position: relative;
  display: flex;
  align-items: center;
  gap: 2px;
  margin-inline: auto;
  --x: 0px;
  --w: 0px;
}

.sn-23__ind {
  position: absolute;
  inset-block-end: 0;
  inset-inline-start: 0;
  block-size: 2px;
  inline-size: var(--w);
  translate: var(--x) 0;
  border-radius: 99px;
  background: var(--sn-23-acc);
  box-shadow: 0 0 14px -2px var(--sn-23-acc);
  transition: translate .38s cubic-bezier(.32,.72,.3,1),inline-size .38s cubic-bezier(.32,.72,.3,1),opacity .2s ease;
}

.sn-23__link {
  position: relative;
  display: flex;
  align-items: center;
  min-height: 40px;
  padding: 0 13px;
  border-radius: 9px;
  font-size: 13.6px;
  font-weight: 600;
  color: var(--sn-23-mut);
  text-decoration: none;
  white-space: nowrap;
  transition: color .22s ease,background .22s ease;
}

.sn-23__link:hover {
  color: var(--sn-23-ink);
  background: oklch(1 0 0/.06);
}

.sn-23__link[aria-current="location"] {
  color: var(--sn-23-acc);
}

.sn-23__link:focus-visible,
.sn-23__brand:focus-visible {
  outline: 2px solid var(--sn-23-acc);
  outline-offset: 2px;
}

.sn-23__count {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .1em;
  color: var(--sn-23-mut);
  padding: 6px 10px;
  border: 1px solid var(--sn-23-line);
  border-radius: 99px;
}

.sn-23__sec {
  scroll-margin-top: var(--sn-23-h);
  display: grid;
  gap: 10px;
  align-content: center;
  min-height: 70svh;
  padding: clamp(26px,5vw,54px);
  border-bottom: 1px solid var(--sn-23-line);
  position: relative;
}

.sn-23__sec::before {
  content: '';
  position: absolute;
  inset-block-start: 0;
  inset-inline: 0;
  block-size: 1px;
  background: linear-gradient(90deg,transparent,color-mix(in oklch,var(--sn-23-acc) 40%,transparent),transparent);
}

.sn-23__sec--short {
  min-height: 190px;
  align-content: start;
}

.sn-23__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sn-23-acc);
}

.sn-23__h {
  font-size: clamp(20px,2.8vw,29px);
  line-height: 1.12;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-23__p {
  max-width: 54ch;
  font-size: 14.9px;
  line-height: 1.66;
  color: var(--sn-23-mut);
  text-wrap: pretty;
}

.sn-23__caption {
  font-size: 12.6px;
  color: oklch(0.72 0.02 285);
  text-align: center;
}

.sn-23__caption code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  color: var(--sn-23-acc);
  background: oklch(1 0 0/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

@media (max-width: 640px) {
  .sn-23 {
    --sn-23-h: 56px;
  }

  .sn-23__count {
    display: none;
  }

  .sn-23__link {
    padding: 0 9px;
    font-size: 12.6px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-23__ind {
    transition: none;
  }

  .sn-23 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-23) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-23-h) + 10px);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-23) {
    scroll-behavior: auto;
  }
}

.sn-23__bar,
.sn-23__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-23__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-23__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-23-line);
}

.sn-23__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-23-mut);
  text-align: center;
}

.sn-23__intro-title,
.sn-23__intro-sub {
  text-wrap: balance;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sn-23');
  if (!root || root.dataset.snWired) return;
  root.dataset.snWired = '1';
  const nav = root.querySelector('#sn-23-nav');
  const count = root.querySelector('#sn-23-count');
  const links = [...root.querySelectorAll('.sn-23__link')];
  const secs = links.map((l) => root.querySelector(l.getAttribute('href'))).filter(Boolean);
  let current = '';
  const move = (link) => {
    const navBox = nav.getBoundingClientRect();
    const box = link.getBoundingClientRect();
    nav.style.setProperty('--x', (box.left - navBox.left) + 'px');
    nav.style.setProperty('--w', box.width + 'px');
  };
  const mark = (id) => {
    if (id === current) return;
    current = id;
    links.forEach((l, i) => {
      const on = l.getAttribute('href') === '#' + id;
      if (on) { l.setAttribute('aria-current', 'location'); move(l); count.textContent = String(i + 1).padStart(2, '0') + ' / ' + String(links.length).padStart(2, '0'); }
      else l.removeAttribute('aria-current');
    });
  };
  const seen = new Set();
  const sync = () => {
    if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 4) { mark(secs[secs.length - 1].id); return; }
    const first = secs.find((s) => seen.has(s.id));
    if (first) mark(first.id);
  };
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => { e.isIntersecting ? seen.add(e.target.id) : seen.delete(e.target.id); });
    sync();
  }, { root: null, rootMargin: '-64px 0px -55% 0px', threshold: 0 });
  secs.forEach((s) => io.observe(s));
  window.addEventListener('scroll', sync, { passive: true });
  const active = () => links.find((l) => l.hasAttribute('aria-current')) || links[0];
  requestAnimationFrame(() => move(active()));
  new ResizeObserver(() => move(active())).observe(nav);
})();
```
