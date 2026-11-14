---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/sticky-header-with-multi-column-mega-menu-dropdown/"
title: "Sticky Header with Multi-Column Mega Menu Dropdown"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "Category navigation for a catalogue that does not fit in a list: a full-width panel with grouped columns and a promoted product, opening from a sticky header…"
has_js: "true"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Header with Multi-Column Mega Menu Dropdown
Source: https://codefronts.com/navigation/css-sticky-navigation/sticky-header-with-multi-column-mega-menu-dropdown/

Category navigation for a catalogue that does not fit in a list: a full-width panel with grouped columns and a promoted product, opening from a sticky header so it stays reachable at any scroll depth. Built as a disclosure rather than a menu, which is what lets it work identically for pointer, keyboard and touch.
## HTML
```html
<section class="sn-16" aria-label="Multi-column mega menu demo">
    <header class="sn-16__bar" id="sn-16-bar">
      <a class="sn-16__brand" href="#sn-16-s1"><span class="sn-16__logo" aria-hidden="true"></span>Forge&amp;Field</a>
      <nav class="sn-16__nav" aria-label="Primary">
        <button class="sn-16__trigger" type="button" id="sn-16-trigger" aria-expanded="false" aria-controls="sn-16-mega">
          Shop
          <svg class="sn-16__caret" viewBox="0 0 12 12" aria-hidden="true" focusable="false"><path d="M2.5 4.5 6 8l3.5-3.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </button>
        <a class="sn-16__link" href="#sn-16-s2">Workshop</a>
        <a class="sn-16__link" href="#sn-16-s3">Stories</a>
      </nav>
      <a class="sn-16__cta" href="#sn-16-s3">Bag</a>
      <div class="sn-16__mega" id="sn-16-mega" hidden>
        <div class="sn-16__col">
          <h3 class="sn-16__ch">Hand tools</h3>
          <a class="sn-16__mlink" href="#sn-16-s1">Chisels &amp; gouges</a>
          <a class="sn-16__mlink" href="#sn-16-s1">Planes</a>
          <a class="sn-16__mlink" href="#sn-16-s1">Marking &amp; measuring</a>
          <a class="sn-16__mlink" href="#sn-16-s1">Sharpening</a>
        </div>
        <div class="sn-16__col">
          <h3 class="sn-16__ch">Workshop</h3>
          <a class="sn-16__mlink" href="#sn-16-s2">Benches</a>
          <a class="sn-16__mlink" href="#sn-16-s2">Vices &amp; clamps</a>
          <a class="sn-16__mlink" href="#sn-16-s2">Dust extraction</a>
          <a class="sn-16__mlink" href="#sn-16-s2">Storage</a>
        </div>
        <div class="sn-16__col">
          <h3 class="sn-16__ch">Materials</h3>
          <a class="sn-16__mlink" href="#sn-16-s3">Hardwoods</a>
          <a class="sn-16__mlink" href="#sn-16-s3">Finishes &amp; oils</a>
          <a class="sn-16__mlink" href="#sn-16-s3">Adhesives</a>
          <a class="sn-16__mlink" href="#sn-16-s3">Abrasives</a>
        </div>
        <a class="sn-16__promo" href="#sn-16-s1">
          <img class="sn-16__promoimg" src="https://images.unsplash.com/photo-1504148455328-c376907d081c?q=80&w=800&auto=format&fit=crop" alt="Woodworking hand tools arranged on a workbench" width="800" height="600" loading="lazy" decoding="async">
          <span class="sn-16__promotag">New season</span>
          <span class="sn-16__promoh">The bench collection</span>
        </a>
      </div>
    </header>
    <main>
      <section class="sn-16__sec" id="sn-16-s1">
        <p class="sn-16__kicker">Disclosure, not menu</p>
        <h3 class="sn-16__h">Links should behave like links</h3>
        <p class="sn-16__p">An ARIA menu changes the keyboard contract to arrow-keys-only and announces items as application commands. A disclosure keeps Tab, keeps link semantics and works on touch.</p>
      </section>
      <section class="sn-16__sec" id="sn-16-s2">
        <p class="sn-16__kicker">Grace period</p>
        <h3 class="sn-16__h">Diagonal mouse paths</h3>
        <p class="sn-16__p">Closing the instant the pointer leaves the trigger breaks the natural diagonal travel toward the panel. A short delay makes it feel forgiving without feeling stuck.</p>
      </section>
      <section class="sn-16__sec" id="sn-16-s3">
        <p class="sn-16__kicker">Sticky context</p>
        <h3 class="sn-16__h">The panel travels with the bar</h3>
        <p class="sn-16__p">Absolutely positioned inside the sticky header, the panel needs no coordinate maths — it is pinned wherever the header is.</p>
      </section>
    </main>
  <footer class="sn-16__pagefoot">
    <p class="sn-16__pagefootin">Sticky navigation pattern 16 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-16 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-16-bg);
  --sn-16-bg: oklch(0.95 0.012 75);
  --sn-16-surface: oklch(0.995 0.004 75);
  --sn-16-ink: oklch(0.23 0.024 55);
  --sn-16-mut: oklch(0.53 0.022 55);
  --sn-16-acc: oklch(0.5 0.13 42);
  --sn-16-line: oklch(0.23 0.024 55/.13);
  --sn-16-h: 66px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-16-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-16 *,
.sn-16 *::before,
.sn-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-16__bar {
  position: sticky;
  top: 0;
  z-index: 20;
  display: flex;
  align-items: center;
  gap: clamp(10px,2vw,24px);
  min-height: var(--sn-16-h);
  padding: 0 clamp(14px,2.6vw,24px);
  background: color-mix(in oklch,var(--sn-16-surface) 90%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--sn-16-line);
}

.sn-16__brand {
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

.sn-16__logo {
  width: 20px;
  height: 20px;
  border-radius: 5px;
  background: var(--sn-16-acc);
  clip-path: polygon(0 20%,100% 0,80% 100%,20% 80%);
}

.sn-16__nav {
  display: flex;
  align-items: center;
  gap: 2px;
  margin-inline-start: auto;
}

.sn-16__trigger {
  display: flex;
  align-items: center;
  gap: 6px;
  min-height: 38px;
  padding: 0 12px;
  border: 0;
  border-radius: 9px;
  background: transparent;
  font-family: inherit;
  font-size: 13.6px;
  font-weight: 640;
  color: var(--sn-16-mut);
  cursor: pointer;
  transition: color .18s ease,background .18s ease;
}

.sn-16__trigger:hover,
.sn-16__trigger[aria-expanded="true"] {
  color: var(--sn-16-ink);
  background: oklch(0.23 0.024 55/.06);
}

.sn-16__caret {
  inline-size: 12px;
  block-size: 12px;
  transition: rotate .26s ease;
}

.sn-16__trigger[aria-expanded="true"] .sn-16__caret {
  rotate: 180deg;
}

.sn-16__link {
  display: flex;
  align-items: center;
  min-height: 38px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 13.6px;
  font-weight: 600;
  color: var(--sn-16-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.sn-16__link:hover {
  color: var(--sn-16-ink);
  background: oklch(0.23 0.024 55/.05);
}

.sn-16__cta {
  display: flex;
  align-items: center;
  min-height: 38px;
  padding: 0 16px;
  border-radius: 99px;
  font-size: 13.2px;
  font-weight: 660;
  color: oklch(1 0 0);
  background: var(--sn-16-acc);
  text-decoration: none;
  white-space: nowrap;
  transition: transform .18s ease;
}

.sn-16__cta:hover {
  transform: translateY(-1px);
}

.sn-16__trigger:focus-visible,
.sn-16__link:focus-visible,
.sn-16__cta:focus-visible,
.sn-16__brand:focus-visible,
.sn-16__mlink:focus-visible,
.sn-16__promo:focus-visible {
  outline: 2px solid var(--sn-16-acc);
  outline-offset: 2px;
}

.sn-16__mega {
  position: absolute;
  inset-inline: 0;
  top: 100%;
  display: grid;
  grid-template-columns: repeat(3,minmax(0,1fr)) 250px;
  gap: clamp(16px,2.6vw,32px);
  padding: clamp(20px,3vw,30px);
  background: var(--sn-16-surface);
  border-bottom: 1px solid var(--sn-16-line);
  box-shadow: 0 30px 44px -30px oklch(0.23 0.024 55/.5);
  max-block-size: min(62svh,420px);
  overflow: auto;
  opacity: 1;
  translate: 0 0;
  transition: opacity .22s ease,translate .26s cubic-bezier(.32,.72,.3,1);
}

@starting-style {
  .sn-16__mega {
    opacity: 0;
    translate: 0 -10px;
  }
}

.sn-16__mega[hidden] {
  display: none;
}

.sn-16__col {
  display: grid;
  align-content: start;
  gap: 3px;
  min-width: 0;
}

.sn-16__ch {
  margin-block-end: 7px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10.5px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sn-16-acc);
}

.sn-16__mlink {
  display: flex;
  align-items: center;
  min-height: 38px;
  padding: 0 10px;
  margin-inline: -10px;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 560;
  color: var(--sn-16-mut);
  text-decoration: none;
  transition: color .16s ease,background .16s ease;
}

.sn-16__mlink:hover {
  color: var(--sn-16-ink);
  background: oklch(0.23 0.024 55/.05);
}

.sn-16__promo {
  position: relative;
  display: grid;
  align-content: end;
  gap: 4px;
  min-block-size: 160px;
  padding: 16px;
  border-radius: 12px;
  overflow: hidden;
  color: oklch(1 0 0);
  text-decoration: none;
  background: linear-gradient(160deg,oklch(0.5 0.1 45),oklch(0.35 0.06 60));
}

.sn-16__promoimg {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  opacity: .62;
  transition: scale .5s cubic-bezier(.32,.72,.3,1);
}

.sn-16__promo:hover .sn-16__promoimg {
  scale: 1.06;
}

.sn-16__promotag,
.sn-16__promoh {
  position: relative;
}

.sn-16__promotag {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 10px;
  letter-spacing: .14em;
  text-transform: uppercase;
  opacity: .92;
}

.sn-16__promoh {
  font-size: 17px;
  font-weight: 680;
  letter-spacing: -.02em;
  text-shadow: 0 1px 12px oklch(0 0 0/.5);
}

.sn-16__sec {
  scroll-margin-top: var(--sn-16-h);
  display: grid;
  gap: 10px;
  align-content: center;
  min-height: 66svh;
  padding: clamp(24px,4vw,48px);
  border-bottom: 1px solid var(--sn-16-line);
}

.sn-16__sec:nth-child(even) {
  background: oklch(0.975 0.008 70);
}

.sn-16__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sn-16-acc);
}

.sn-16__h {
  font-size: clamp(19px,2.6vw,26px);
  line-height: 1.16;
  letter-spacing: -.025em;
  font-weight: 690;
  text-wrap: balance;
}

.sn-16__p {
  max-width: 54ch;
  font-size: 14.8px;
  line-height: 1.64;
  color: var(--sn-16-mut);
  text-wrap: pretty;
}

@media (max-width: 780px) {
  .sn-16__mega {
    grid-template-columns: repeat(2,minmax(0,1fr));
  }

  .sn-16__promo {
    grid-column: 1/-1;
    min-block-size: 120px;
  }
}

@media (max-width: 520px) {
  .sn-16__mega {
    grid-template-columns: 1fr;
  }

  .sn-16__link {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-16 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-16) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-16-h) + 8px);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-16) {
    scroll-behavior: auto;
  }
}

.sn-16__bar,
.sn-16__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-16__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-16__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-16-line);
}

.sn-16__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-16-mut);
  text-align: center;
}

.sn-16__intro-title,
.sn-16__intro-sub {
  text-wrap: balance;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sn-16');
  if (!root || root.dataset.snWired) return;
  root.dataset.snWired = '1';
  const bar = root.querySelector('#sn-16-bar');
  const trigger = root.querySelector('#sn-16-trigger');
  const mega = root.querySelector('#sn-16-mega');
  let timer;
  const set = (open) => {
    clearTimeout(timer);
    trigger.setAttribute('aria-expanded', String(open));
    mega.hidden = !open;
  };
  trigger.addEventListener('click', () => set(trigger.getAttribute('aria-expanded') !== 'true'));
  trigger.addEventListener('pointerenter', () => set(true));
  bar.addEventListener('focusin', (e) => { if (e.target === trigger) set(true); });
  bar.addEventListener('pointerleave', () => { timer = setTimeout(() => set(false), 160); });
  bar.addEventListener('pointerenter', () => clearTimeout(timer));
  bar.addEventListener('focusout', (e) => { if (!bar.contains(e.relatedTarget)) set(false); });
  root.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && trigger.getAttribute('aria-expanded') === 'true') { set(false); trigger.focus(); }
  });
  mega.addEventListener('click', (e) => { if (e.target.closest('a')) set(false); });
})();
```
