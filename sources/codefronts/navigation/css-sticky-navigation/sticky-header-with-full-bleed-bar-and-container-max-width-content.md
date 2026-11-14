---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/sticky-header-with-full-bleed-bar-and-container-max-width-content/"
title: "Sticky Header with Full-Bleed Bar and Container Max-Width Content"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "The layout contract behind almost every corporate site: the sticky bar's background, border and shadow run edge to edge, while the logo and links sit on…"
has_js: "false"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Header with Full-Bleed Bar and Container Max-Width Content
Source: https://codefronts.com/navigation/css-sticky-navigation/sticky-header-with-full-bleed-bar-and-container-max-width-content/

The layout contract behind almost every corporate site: the sticky bar's background, border and shadow run edge to edge, while the logo and links sit on exactly the same left margin as the article below. Uses a named-line grid so the page and the header share one measurement, rather than repeating a magic 1200px in six stylesheets.
## HTML
```html
<section class="sn-04" aria-label="Full-bleed sticky bar with contained content demo">
    <div class="sn-04__page">
      <header class="sn-04__bar">
        <div class="sn-04__barin">
          <a class="sn-04__brand" href="#sn-04-s1"><span class="sn-04__logo" aria-hidden="true"></span>Ardent Review</a>
          <nav class="sn-04__nav" aria-label="Primary">
            <a class="sn-04__link" href="#sn-04-s1" aria-current="page">Latest</a>
            <a class="sn-04__link" href="#sn-04-s2">Essays</a>
            <a class="sn-04__link" href="#sn-04-s3">Archive</a>
          </nav>
          <span class="sn-04__meta">Issue 42</span>
        </div>
      </header>
  <div class="sn-04__intro">
    <div class="sn-04__introin">
    <p class="sn-04__intro-eyebrow">[full-start] · min(100%, 1140px) · [full-end]</p>
    <h2 class="sn-04__intro-title">Bar edge to edge, content on the grid</h2>
    </div>
  </div>
      <div class="sn-04__hero">
        <div class="sn-04__heroin">
          <p class="sn-04__kicker">Layout</p>
          <h3 class="sn-04__hero-h">One grid, two behaviours</h3>
        </div>
      </div>
      <article class="sn-04__art" id="sn-04-s1">
        <h4 class="sn-04__h">The same line, not the same number</h4>
        <p class="sn-04__p">The logo's left edge and this paragraph's left edge are the identical grid line. Nothing is measured twice, so nothing can drift apart.</p>
        <p class="sn-04__rule" aria-hidden="true"></p>
        <h4 class="sn-04__h" id="sn-04-s2">Opting out is one declaration</h4>
        <p class="sn-04__p">Children default to the content track. A full-bleed band — header, hero, callout, footer — sets <code>grid-column: full</code> and nothing else.</p>
        <div class="sn-04__note">
          <p class="sn-04__p"><strong>Why not 100vw?</strong> Viewport units include the scrollbar, so the classic full-bleed hack overflows horizontally on Windows. Grid tracks never do.</p>
        </div>
        <h4 class="sn-04__h" id="sn-04-s3">Stable gutters</h4>
        <p class="sn-04__p"><code>scrollbar-gutter: stable</code> reserves the scrollbar's width before it appears, so the centred column never jumps sideways when a page grows past one screen.</p>
        <p class="sn-04__p">Every measurement in this layout comes from two custom properties: the gutter and the max measure.</p>
      </article>
      <footer class="sn-04__foot"><div class="sn-04__footin">Ardent Review — full-bleed band, contained text</div></footer>
    </div>
</section>
```
## CSS
```css
.sn-04 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-04-bg);
  --sn-04-bg: oklch(0.955 0.012 96);
  --sn-04-surface: oklch(0.995 0.005 96);
  --sn-04-ink: oklch(0.24 0.02 60);
  --sn-04-mut: oklch(0.53 0.02 60);
  --sn-04-acc: oklch(0.48 0.13 20);
  --sn-04-line: oklch(0.24 0.02 60/.14);
  --sn-04-gut: clamp(16px,4vw,40px);
  --sn-04-max: 640px;
  --sn-04-h: 60px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-04-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-04 *,
.sn-04 *::before,
.sn-04 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-04__eyebrow,
.sn-04__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--sn-04-acc);
}

.sn-04__title,
.sn-04__intro-title {
  font-size: clamp(23px,3.5vw,37px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-04__page {
  display: grid;
  grid-template-columns: [full-start] minmax(var(--sn-04-gut),1fr) [content-start] min(100% - var(--sn-04-gut)*2,var(--sn-04-max)) [content-end] minmax(var(--sn-04-gut),1fr) [full-end];
  align-content: start;
}

.sn-04__page>* {
  grid-column: content;
}

.sn-04__bar,
.sn-04__hero,
.sn-04__foot {
  grid-column: full;
  display: grid;
  grid-template-columns: subgrid;
}

.sn-04__barin,
.sn-04__heroin,
.sn-04__footin {
  grid-column: content;
}

.sn-04__bar {
  position: sticky;
  top: 0;
  z-index: 10;
  background: color-mix(in oklch,var(--sn-04-surface) 84%,transparent);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--sn-04-line);
}

.sn-04__barin {
  display: flex;
  align-items: center;
  gap: 16px;
  min-height: var(--sn-04-h);
}

.sn-04__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.02em;
  color: inherit;
  text-decoration: none;
  white-space: nowrap;
}

.sn-04__logo {
  width: 8px;
  height: 20px;
  background: var(--sn-04-acc);
}

.sn-04__nav {
  display: flex;
  gap: 2px;
  margin-inline-start: auto;
}

.sn-04__link {
  display: flex;
  align-items: center;
  min-height: 36px;
  padding: 0 11px;
  border-radius: 8px;
  font-size: 13.4px;
  font-weight: 600;
  color: var(--sn-04-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.sn-04__link:hover {
  color: var(--sn-04-ink);
  background: oklch(0.24 0.02 60/.05);
}

.sn-04__link[aria-current="page"] {
  color: var(--sn-04-acc);
}

.sn-04__link:focus-visible,
.sn-04__brand:focus-visible {
  outline: 2px solid var(--sn-04-acc);
  outline-offset: 2px;
}

.sn-04__meta {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  color: var(--sn-04-mut);
  padding-inline-start: 14px;
  border-inline-start: 1px solid var(--sn-04-line);
  white-space: nowrap;
}

.sn-04__hero {
  background: linear-gradient(120deg,oklch(0.93 0.05 40),oklch(0.95 0.03 96));
  border-bottom: 1px solid var(--sn-04-line);
}

.sn-04__heroin {
  display: grid;
  gap: 8px;
  padding-block: clamp(26px,5vw,52px);
}

.sn-04__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sn-04-acc);
}

.sn-04__hero-h {
  font-size: clamp(24px,4vw,34px);
  line-height: 1.08;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-04__art {
  display: grid;
  gap: 14px;
  padding-block: clamp(26px,4vw,44px);
}

.sn-04__h {
  scroll-margin-top: calc(var(--sn-04-h) + 12px);
  font-size: 19px;
  line-height: 1.2;
  letter-spacing: -.02em;
  font-weight: 690;
  text-wrap: balance;
}

.sn-04__p {
  font-size: 15px;
  line-height: 1.7;
  color: var(--sn-04-mut);
  text-wrap: pretty;
}

.sn-04__p strong {
  color: var(--sn-04-ink);
}

.sn-04__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: oklch(0.24 0.02 60/.07);
  padding: 2px 6px;
  border-radius: 5px;
}

.sn-04__rule {
  height: 1px;
  background: var(--sn-04-line);
}

.sn-04__note {
  padding: 16px 18px;
  border-inline-start: 3px solid var(--sn-04-acc);
  background: oklch(0.24 0.02 60/.04);
  border-radius: 0 10px 10px 0;
}

.sn-04__foot {
  background: oklch(0.24 0.02 60);
  color: oklch(0.95 0.01 60);
  border-top: 1px solid var(--sn-04-line);
}

.sn-04__footin {
  padding-block: 26px;
  font-size: 13px;
  letter-spacing: .01em;
}

@media (max-width: 560px) {
  .sn-04 {
    --sn-04-h: 54px;
  }

  .sn-04__meta {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-04 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-04) {
  scroll-behavior: smooth;
  scroll-padding-top: var(--sn-04-h);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-04) {
    scroll-behavior: auto;
  }
}

.sn-04__bar,
.sn-04__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-04__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-04__intro {
  display: grid;
  place-items: center;
  min-height: min(90svh,900px);
  padding: clamp(56px,12vh,150px) clamp(20px,5vw,48px) clamp(40px,8vh,90px);
}

.sn-04__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-width: 26ch;
}

.sn-04__intro-eyebrow {
  font-size: clamp(11px,1.1vw,13px);
}

.sn-04__intro-title {
  font-size: clamp(38px,7.5vw,86px);
  line-height: .98;
  letter-spacing: -.04em;
  max-width: none;
}

.sn-04__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  max-width: 46ch;
}

.sn-04__intro::after {
  content: "Scroll — the bar stays";
  justify-self: center;
  margin-block-start: clamp(20px,4vh,44px);
  padding: 9px 18px;
  border: 1px solid var(--sn-04-line);
  border-radius: 99px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sn-04-mut);
  animation: sn-04-cue 2.6s ease-in-out infinite;
}

@keyframes sn-04-cue {
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
  .sn-04__intro::after {
    animation: none;
  }
}

.sn-04__intro-title,
.sn-04__intro-sub {
  text-wrap: balance;
}
```
