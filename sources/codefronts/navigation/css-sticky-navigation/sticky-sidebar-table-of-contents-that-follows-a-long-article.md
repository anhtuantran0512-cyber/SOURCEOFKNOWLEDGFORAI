---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/sticky-sidebar-table-of-contents-that-follows-a-long-article/"
title: "Sticky Sidebar Table of Contents That Follows a Long Article"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "The On this page rail that documentation sites and long-form editorial layouts are built around: a contents list that pins beside the article, scrolls…"
has_js: "true"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Sidebar Table of Contents That Follows a Long Article
Source: https://codefronts.com/navigation/css-sticky-navigation/sticky-sidebar-table-of-contents-that-follows-a-long-article/

The On this page rail that documentation sites and long-form editorial layouts are built around: a contents list that pins beside the article, scrolls internally when the outline outgrows the viewport, and keeps the reader's current section marked while they move through the piece.
## HTML
```html
<section class="sn-21" aria-label="Sticky sidebar table of contents demo">
    <header class="sn-21__bar">
      <a class="sn-21__brand" href="#sn-21-s1"><span class="sn-21__logo" aria-hidden="true"></span>Lumen Handbook</a>
      <nav class="sn-21__nav" aria-label="Primary">
        <a class="sn-21__link" href="#sn-21-s1" aria-current="page">Guides</a>
        <a class="sn-21__link" href="#sn-21-s4">Patterns</a>
        <a class="sn-21__link" href="#sn-21-s6">Reference</a>
      </nav>
    </header>
  <div class="sn-21__intro">
    <div class="sn-21__introin">
    <p class="sn-21__intro-eyebrow">position: sticky · align-self: start</p>
    <h2 class="sn-21__intro-title">The rail that follows the reader</h2>
    <p class="sn-21__intro-sub">Scroll the article. The contents pin beside it and the current section stays marked.</p>
    </div>
  </div>
    <div class="sn-21__layout">
      <article class="sn-21__article">
        <figure class="sn-21__figure">
          <img class="sn-21__img" src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=1200&auto=format&fit=crop" alt="A laptop screen filled with source code in a dim workspace" width="1200" height="700" loading="lazy" decoding="async">
        </figure>
        <p class="sn-21__kicker">Layout · 9 min read</p>
        <h3 class="sn-21__lede">Building documentation shells that survive real content</h3>
        <section class="sn-21__sec" id="sn-21-s1">
          <h4 class="sn-21__h">Anatomy of the shell</h4>
          <p class="sn-21__p">Three regions: a sticky masthead, a measure-limited column of prose, and a contents rail that never leaves the reader. Everything below is about keeping the third one honest when the article runs to nine screens.</p>
        </section>
        <section class="sn-21__sec" id="sn-21-s2">
          <h4 class="sn-21__h">Why the rail stops sticking</h4>
          <p class="sn-21__p">Grid children stretch by default, so the aside is already as tall as the article and has no room to travel. <code>align-self:start</code> collapses it to its content height and the sticky inset starts working immediately.</p>
        </section>
        <section class="sn-21__sec" id="sn-21-s3">
          <h4 class="sn-21__h">Outlines longer than the viewport</h4>
          <p class="sn-21__p">Cap the rail with <code>max-block-size</code> and give it <code>overflow-y:auto</code>. Add <code>overscroll-behavior:contain</code> so reaching the end of the outline does not start dragging the article underneath it.</p>
        </section>
        <section class="sn-21__sec" id="sn-21-s4">
          <h4 class="sn-21__h">Marking the current section</h4>
          <p class="sn-21__p">An observer scoped to the scroll port flags whichever section occupies the upper band. The matching entry takes <code>aria-current="location"</code> — the token for a position inside the current page.</p>
        </section>
        <section class="sn-21__sec" id="sn-21-s5">
          <h4 class="sn-21__h">Focus is not for spying</h4>
          <p class="sn-21__p">Moving focus as sections pass feels clever and reads as a bug: the caret jumps, screen readers restart, and keyboard users lose their place. Update state, never focus.</p>
        </section>
        <section class="sn-21__sec" id="sn-21-s6">
          <h4 class="sn-21__h">Landing below the masthead</h4>
          <p class="sn-21__p">Every section carries <code>scroll-margin-top</code>, so entries clicked in the rail land under the bar with their heading visible — for pointer clicks, keyboard activation and deep links alike.</p>
          <p class="sn-21__note">One grid, one sticky child, one observer.</p>
        </section>
      </article>
      <aside class="sn-21__aside">
        <nav class="sn-21__toc" aria-labelledby="sn-21-toch">
          <p class="sn-21__toch" id="sn-21-toch">On this page</p>
          <ol class="sn-21__toclist">
            <li><a class="sn-21__toclink" href="#sn-21-s1" aria-current="location">Anatomy of the shell</a></li>
            <li><a class="sn-21__toclink" href="#sn-21-s2">Why the rail stops sticking</a></li>
            <li><a class="sn-21__toclink" href="#sn-21-s3">Outlines longer than the viewport</a></li>
            <li><a class="sn-21__toclink" href="#sn-21-s4">Marking the current section</a></li>
            <li><a class="sn-21__toclink" href="#sn-21-s5">Focus is not for spying</a></li>
            <li><a class="sn-21__toclink" href="#sn-21-s6">Landing below the masthead</a></li>
          </ol>
        </nav>
      </aside>
    </div>
  <footer class="sn-21__pagefoot">
    <p class="sn-21__pagefootin">Sticky navigation pattern 21 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-21 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-21-bg);
  --sn-21-bg: oklch(0.965 0.012 82);
  --sn-21-surface: oklch(0.995 0.004 82);
  --sn-21-ink: oklch(0.24 0.021 62);
  --sn-21-mut: oklch(0.53 0.021 62);
  --sn-21-acc: oklch(0.53 0.15 35);
  --sn-21-line: oklch(0.24 0.021 62/.13);
  --sn-21-h: 56px;
  --sn-21-port: min(76svh,620px);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-21-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-21 *,
.sn-21 *::before,
.sn-21 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-21__eyebrow,
.sn-21__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sn-21-acc);
}

.sn-21__title,
.sn-21__intro-title {
  font-size: clamp(23px,3.5vw,36px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-21__sub,
.sn-21__intro-sub {
  font-size: 14.4px;
  line-height: 1.6;
  color: var(--sn-21-mut);
  text-wrap: pretty;
}

.sn-21__bar {
  position: sticky;
  top: 0;
  z-index: 20;
  display: flex;
  align-items: center;
  gap: clamp(10px,2vw,20px);
  min-height: var(--sn-21-h);
  padding: 0 clamp(14px,2.6vw,22px);
  background: color-mix(in oklch,var(--sn-21-surface) 84%,transparent);
  backdrop-filter: blur(14px) saturate(1.4);
  -webkit-backdrop-filter: blur(14px) saturate(1.4);
  border-bottom: 1px solid var(--sn-21-line);
}

.sn-21__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 14.6px;
  font-weight: 700;
  letter-spacing: -.025em;
  color: inherit;
  text-decoration: none;
  white-space: nowrap;
}

.sn-21__logo {
  width: 18px;
  height: 18px;
  border-radius: 5px;
  background: linear-gradient(150deg,var(--sn-21-acc),oklch(0.72 0.14 78));
}

.sn-21__nav {
  display: flex;
  align-items: center;
  gap: 2px;
  margin-inline-start: auto;
}

.sn-21__link {
  display: flex;
  align-items: center;
  min-height: 36px;
  padding: 0 11px;
  border-radius: 8px;
  font-size: 13.2px;
  font-weight: 600;
  color: var(--sn-21-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.sn-21__link:hover {
  color: var(--sn-21-ink);
  background: oklch(0.24 0.021 62/.05);
}

.sn-21__link[aria-current="page"] {
  color: var(--sn-21-acc);
}

.sn-21__link:focus-visible,
.sn-21__brand:focus-visible,
.sn-21__toclink:focus-visible {
  outline: 2px solid var(--sn-21-acc);
  outline-offset: 2px;
}

.sn-21__layout {
  display: grid;
  grid-template-columns: minmax(0,1fr) 226px;
  gap: clamp(18px,3vw,34px);
  padding: clamp(16px,3vw,28px);
}

.sn-21__article {
  min-width: 0;
  display: grid;
  gap: 14px;
  max-width: 64ch;
}

.sn-21__figure {
  margin: 0;
  border-radius: 12px;
  overflow: hidden;
  background: linear-gradient(140deg,oklch(0.8 0.09 60),oklch(0.62 0.13 30));
  aspect-ratio: 16/7;
}

.sn-21__img {
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  display: block;
}

.sn-21__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sn-21-acc);
}

.sn-21__lede {
  font-size: clamp(20px,2.8vw,27px);
  line-height: 1.14;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-21__sec {
  scroll-margin-top: calc(var(--sn-21-h) + 12px);
  display: grid;
  gap: 8px;
  padding-block: clamp(22px,4vw,38px);
  border-top: 1px solid var(--sn-21-line);
}

.sn-21__h {
  font-size: 17px;
  line-height: 1.2;
  letter-spacing: -.02em;
  font-weight: 670;
}

.sn-21__p {
  font-size: 14.6px;
  line-height: 1.66;
  color: var(--sn-21-mut);
  text-wrap: pretty;
}

.sn-21__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.24 0.021 62/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

.sn-21__note {
  justify-self: start;
  margin-block-start: 6px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sn-21-acc);
  padding: 7px 13px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--sn-21-acc) 9%,transparent);
  border: 1px solid color-mix(in oklch,var(--sn-21-acc) 20%,transparent);
}

.sn-21__aside {
  align-self: start;
  position: sticky;
  top: calc(var(--sn-21-h) + 16px);
  max-block-size: calc(var(--sn-21-port) - var(--sn-21-h) - 40px);
  overflow-y: auto;
  overscroll-behavior: contain;
  scrollbar-width: thin;
}

.sn-21__toc {
  display: grid;
  gap: 9px;
}

.sn-21__toch {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sn-21-mut);
}

.sn-21__toclist {
  list-style: none;
  display: grid;
  gap: 1px;
  border-inline-start: 2px solid var(--sn-21-line);
}

.sn-21__toclink {
  display: block;
  padding: 8px 10px;
  margin-inline-start: -2px;
  border-inline-start: 2px solid transparent;
  font-size: 12.9px;
  line-height: 1.35;
  font-weight: 560;
  color: var(--sn-21-mut);
  text-decoration: none;
  transition: color .2s ease,border-color .2s ease,background .2s ease;
}

.sn-21__toclink:hover {
  color: var(--sn-21-ink);
  background: oklch(0.24 0.021 62/.04);
}

.sn-21__toclink[aria-current="location"] {
  color: var(--sn-21-acc);
  font-weight: 680;
  border-inline-start-color: var(--sn-21-acc);
  background: color-mix(in oklch,var(--sn-21-acc) 7%,transparent);
}

@media (max-width: 760px) {
  .sn-21__layout {
    grid-template-columns: minmax(0,1fr);
    gap: 14px;
  }

  .sn-21__aside {
    order: -1;
    position: sticky;
    top: var(--sn-21-h);
    max-block-size: none;
    overflow: visible;
    padding-block: 8px;
    background: color-mix(in oklch,var(--sn-21-surface) 92%,transparent);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    z-index: 10;
  }

  .sn-21__toch {
    display: none;
  }

  .sn-21__toclist {
    display: flex;
    gap: 6px;
    border: 0;
    overflow-x: auto;
    scroll-snap-type: inline mandatory;
    scrollbar-width: none;
    mask-image: linear-gradient(90deg,#000 0,#000 calc(100% - 28px),transparent);
  }

  .sn-21__toclist::-webkit-scrollbar {
    display: none;
  }

  .sn-21__toclink {
    flex: none;
    scroll-snap-align: start;
    white-space: nowrap;
    margin: 0;
    border: 1px solid var(--sn-21-line);
    border-radius: 99px;
    padding: 8px 13px;
    min-height: 38px;
  }

  .sn-21__toclink[aria-current="location"] {
    border-color: transparent;
    background: color-mix(in oklch,var(--sn-21-acc) 12%,transparent);
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-21 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-21) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-21-h) + 14px);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-21) {
    scroll-behavior: auto;
  }
}

.sn-21__bar,
.sn-21__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-21__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-21__intro {
  display: grid;
  place-items: center;
  min-height: min(90svh,900px);
  padding: clamp(56px,12vh,150px) clamp(20px,5vw,48px) clamp(40px,8vh,90px);
  background: radial-gradient(90% 55% at 50% 0%,oklch(0.99 0.02 70),transparent);
}

.sn-21__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-width: 26ch;
}

.sn-21__intro-eyebrow {
  font-size: clamp(11px,1.1vw,13px);
}

.sn-21__intro-title {
  font-size: clamp(38px,7.5vw,86px);
  line-height: .98;
  letter-spacing: -.04em;
  max-width: none;
}

.sn-21__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  max-width: 46ch;
}

.sn-21__intro::after {
  content: "Scroll — the bar stays";
  justify-self: center;
  margin-block-start: clamp(20px,4vh,44px);
  padding: 9px 18px;
  border: 1px solid var(--sn-21-line);
  border-radius: 99px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sn-21-mut);
  animation: sn-21-cue 2.6s ease-in-out infinite;
}

@keyframes sn-21-cue {
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
  .sn-21__intro::after {
    animation: none;
  }
}

.sn-21__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-21-line);
}

.sn-21__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-21-mut);
  text-align: center;
}

.sn-21__intro-title,
.sn-21__intro-sub {
  text-wrap: balance;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sn-21');
  if (!root || root.dataset.snWired) return;
  root.dataset.snWired = '1';
  const links = [...root.querySelectorAll('.sn-21__toclink')];
  const secs = links.map((l) => root.querySelector(l.getAttribute('href'))).filter(Boolean);
  const mark = (id) => links.forEach((l) => {
    if (l.getAttribute('href') === '#' + id) l.setAttribute('aria-current', 'location');
    else l.removeAttribute('aria-current');
  });
  const seen = new Set();
  const sync = () => {
    if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 4) { mark(secs[secs.length - 1].id); return; }
    const first = secs.find((s) => seen.has(s.id));
    if (first) mark(first.id);
  };
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => { e.isIntersecting ? seen.add(e.target.id) : seen.delete(e.target.id); });
    sync();
  }, { root: null, rootMargin: '-70px 0px -58% 0px', threshold: 0 });
  secs.forEach((s) => io.observe(s));
  window.addEventListener('scroll', sync, { passive: true });
})();
```
