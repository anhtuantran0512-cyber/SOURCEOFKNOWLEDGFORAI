---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/sticky-header-with-article-reading-progress-bar-underneath/"
title: "Sticky Header with Article Reading Progress Bar Underneath"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "The publisher's progress indicator: a 3px fill welded to the bottom edge of the sticky header that tracks how far through the article the reader is."
has_js: "true"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Header with Article Reading Progress Bar Underneath
Source: https://codefronts.com/navigation/css-sticky-navigation/sticky-header-with-article-reading-progress-bar-underneath/

The publisher's progress indicator: a 3px fill welded to the bottom edge of the sticky header that tracks how far through the article the reader is. Runs entirely on a scroll-progress timeline, so the fill is driven by the compositor rather than by a scroll handler recalculating document height on every frame.
## HTML
```html
<section class="sn-09" aria-label="Sticky header with reading progress bar demo">
    <header class="sn-09__bar">
      <a class="sn-09__brand" href="#sn-09-top"><span class="sn-09__logo" aria-hidden="true"></span>The Long Read</a>
      <nav class="sn-09__nav" aria-label="Article">
        <a class="sn-09__link" href="#sn-09-top" aria-current="page">Essay</a>
        <a class="sn-09__link" href="#sn-09-s2">Notes</a>
      </nav>
      <span class="sn-09__time">9 min</span>
      <div class="sn-09__track" aria-hidden="true"><div class="sn-09__fill" id="sn-09-fill"></div></div>
    </header>
  <div class="sn-09__intro">
    <div class="sn-09__introin">
    <p class="sn-09__intro-eyebrow">scaleX · animation-timeline: scroll()</p>
    <h2 class="sn-09__intro-title">Progress welded to the header</h2>
    </div>
  </div>
    <article class="sn-09__art" id="sn-09-top">
      <p class="sn-09__kicker">Interface craft</p>
      <h3 class="sn-09__h1">The quiet mechanics of a progress bar</h3>
      <p class="sn-09__lead">Every publisher ships one. Almost none of them ship one that costs nothing to run.</p>
      <p class="sn-09__p">Scaling is free; resizing is not. A bar animated on its <code>width</code> asks the engine to lay out, paint and composite on every scroll frame. Scaling asks only the compositor, which is already awake.</p>
      <p class="sn-09__p">Binding that scale to a scroll timeline removes the last piece of JavaScript. There is no listener to throttle, no cached document height to invalidate on resize, and no work at all on a page that is not being scrolled.</p>
      <h4 class="sn-09__h2" id="sn-09-s2">Where it belongs</h4>
      <p class="sn-09__p">Attach the fill to the header rather than to the viewport. When the header hides, shrinks or gains an announcement bar above it, the indicator follows automatically instead of floating loose at the top of the screen.</p>
      <p class="sn-09__p">Keep it decorative. The browser already exposes scroll position to assistive technology through the scrollbar; a second announced value is noise, not access.</p>
      <p class="sn-09__p">The result is a component that measures three lines of CSS, holds a steady frame rate on a five-thousand-word article, and degrades to a passive listener where scroll timelines have not landed yet.</p>
      <p class="sn-09__end">— end of article —</p>
    </article>
  <footer class="sn-09__pagefoot">
    <p class="sn-09__pagefootin">Sticky navigation pattern 09 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-09 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-09-bg);
  --sn-09-bg: oklch(0.96 0.008 60);
  --sn-09-surface: oklch(0.995 0.004 80);
  --sn-09-ink: oklch(0.2 0.02 50);
  --sn-09-mut: oklch(0.5 0.02 50);
  --sn-09-acc: oklch(0.58 0.19 25);
  --sn-09-line: oklch(0.2 0.02 50/.13);
  --sn-09-h: 60px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-09-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-09 *,
.sn-09 *::before,
.sn-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-09__eyebrow,
.sn-09__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sn-09-acc);
}

.sn-09__title,
.sn-09__intro-title {
  font-size: clamp(23px,3.5vw,37px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-09__bar {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  gap: 16px;
  min-height: var(--sn-09-h);
  padding: 0 clamp(16px,3vw,26px);
  background: color-mix(in oklch,var(--sn-09-surface) 88%,transparent);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-bottom: 1px solid var(--sn-09-line);
}

.sn-09__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 14.6px;
  font-weight: 700;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
  white-space: nowrap;
}

.sn-09__logo {
  width: 7px;
  height: 18px;
  border-radius: 2px;
  background: var(--sn-09-acc);
}

.sn-09__nav {
  display: flex;
  gap: 2px;
  margin-inline-start: auto;
}

.sn-09__link {
  display: flex;
  align-items: center;
  min-height: 36px;
  padding: 0 11px;
  border-radius: 8px;
  font-size: 13.4px;
  font-weight: 600;
  color: var(--sn-09-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.sn-09__link:hover {
  color: var(--sn-09-ink);
  background: oklch(0.2 0.02 50/.05);
}

.sn-09__link[aria-current="page"] {
  color: var(--sn-09-acc);
}

.sn-09__link:focus-visible,
.sn-09__brand:focus-visible {
  outline: 2px solid var(--sn-09-acc);
  outline-offset: 2px;
}

.sn-09__time {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sn-09-mut);
  padding-inline-start: 14px;
  border-inline-start: 1px solid var(--sn-09-line);
  white-space: nowrap;
}

.sn-09__track {
  position: absolute;
  inset-inline: 0;
  inset-block-end: -1px;
  block-size: 3px;
  background: oklch(0.2 0.02 50/.07);
  overflow: hidden;
}

.sn-09__fill {
  block-size: 100%;
  transform-origin: left center;
  scale: var(--sn-09-p,0) 1;
  background: linear-gradient(90deg,var(--sn-09-acc),oklch(0.72 0.17 55));
  animation: sn-09-grow linear both;
  animation-timeline: scroll(root block);
}

@keyframes sn-09-grow {
  from {
    scale: 0 1;
  }

  to {
    scale: 1 1;
  }
}

.sn-09__art {
  display: grid;
  gap: 15px;
  max-width: 66ch;
  margin-inline: auto;
  padding: clamp(26px,4vw,48px) clamp(20px,4vw,40px) clamp(40px,8vw,90px);
}

.sn-09__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sn-09-acc);
}

.sn-09__h1 {
  font-size: clamp(25px,4vw,36px);
  line-height: 1.08;
  letter-spacing: -.032em;
  font-weight: 720;
  text-wrap: balance;
}

.sn-09__h2 {
  scroll-margin-top: calc(var(--sn-09-h) + 14px);
  margin-block-start: 12px;
  font-size: 19px;
  line-height: 1.2;
  letter-spacing: -.02em;
  font-weight: 690;
}

.sn-09__lead {
  font-size: 17.5px;
  line-height: 1.55;
  color: var(--sn-09-ink);
  text-wrap: pretty;
}

.sn-09__p {
  font-size: 15.4px;
  line-height: 1.75;
  color: var(--sn-09-mut);
  text-wrap: pretty;
}

.sn-09__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.2 0.02 50/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

.sn-09__end {
  margin-block-start: 18px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .1em;
  text-align: center;
  color: var(--sn-09-mut);
}

@media (max-width: 520px) {
  .sn-09__time {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-09) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-09-h) + 10px);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-09) {
    scroll-behavior: auto;
  }
}

.sn-09__bar,
.sn-09__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-09__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-09__intro {
  display: grid;
  place-items: center;
  min-height: min(90svh,900px);
  padding: clamp(56px,12vh,150px) clamp(20px,5vw,48px) clamp(40px,8vh,90px);
}

.sn-09__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-width: 26ch;
}

.sn-09__intro-eyebrow {
  font-size: clamp(11px,1.1vw,13px);
}

.sn-09__intro-title {
  font-size: clamp(38px,7.5vw,86px);
  line-height: .98;
  letter-spacing: -.04em;
  max-width: none;
}

.sn-09__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  max-width: 46ch;
}

.sn-09__intro::after {
  content: "Scroll — the bar stays";
  justify-self: center;
  margin-block-start: clamp(20px,4vh,44px);
  padding: 9px 18px;
  border: 1px solid var(--sn-09-line);
  border-radius: 99px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sn-09-mut);
  animation: sn-09-cue 2.6s ease-in-out infinite;
}

@keyframes sn-09-cue {
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
  .sn-09__intro::after {
    animation: none;
  }
}

.sn-09__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-09-line);
}

.sn-09__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-09-mut);
  text-align: center;
}

.sn-09__intro-title,
.sn-09__intro-sub {
  text-wrap: balance;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.sn-09');
  if (!root || root.dataset.snWired) return;
  root.dataset.snWired = '1';
  if (CSS.supports('animation-timeline: scroll()')) return;
  const fill = root.querySelector('#sn-09-fill');
  fill.style.animation = 'none';
  const sync = () => {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    fill.style.setProperty('--sn-09-p', max > 0 ? (window.scrollY / max).toFixed(4) : 0);
  };
  window.addEventListener('scroll', sync, { passive: true });
  sync();
})();
```
