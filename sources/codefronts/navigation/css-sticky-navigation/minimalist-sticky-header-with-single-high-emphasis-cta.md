---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/minimalist-sticky-header-with-single-high-emphasis-cta/"
title: "Minimalist Sticky Header with Single High-Emphasis CTA"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "A landing-page header stripped to what actually converts: a wordmark, three links and one unmistakable action."
has_js: "false"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Minimalist Sticky Header with Single High-Emphasis CTA
Source: https://codefronts.com/navigation/css-sticky-navigation/minimalist-sticky-header-with-single-high-emphasis-cta/

A landing-page header stripped to what actually converts: a wordmark, three links and one unmistakable action. The engineering interest is in restraint — how a single accent colour, one weight step and a 4px shadow do the entire job of hierarchy, with nothing competing for the click.
## HTML
```html
<section class="sn-13" aria-label="Minimalist sticky header with single CTA demo">
    <a class="sn-13__skip" href="#sn-13-main">Skip to content</a>
    <header class="sn-13__bar">
      <a class="sn-13__brand" href="#sn-13-main">Quill</a>
      <nav class="sn-13__nav" aria-label="Primary">
        <a class="sn-13__link" href="#sn-13-main" aria-current="page">Why Quill</a>
        <a class="sn-13__link" href="#sn-13-s2">Pricing</a>
        <a class="sn-13__link" href="#sn-13-s3">Customers</a>
      </nav>
      <a class="sn-13__cta" href="#sn-13-s3">Start writing</a>
    </header>
    <main id="sn-13-main">
      <section class="sn-13__hero">
        <p class="sn-13__kicker">One action per screen</p>
        <h2 class="sn-13__title">Writing software that gets out of the way</h2>
        <p class="sn-13__lead">Three links, one button, and a header that never asks the reader to choose between two competing next steps.</p>
      </section>
      <section class="sn-13__sec" id="sn-13-s2">
        <h3 class="sn-13__h">One accent, spent once</h3>
        <p class="sn-13__p">Colour, weight and elevation are reserved entirely for the primary action. Nothing else in the header borrows any of the three.</p>
      </section>
      <section class="sn-13__sec" id="sn-13-s3">
        <h3 class="sn-13__h">Type set, not typed</h3>
        <p class="sn-13__p">Negative tracking on the wordmark, a touch of positive tracking on the small nav labels. Both corrections are invisible individually and obvious together.</p>
      </section>
      <section class="sn-13__sec">
        <h3 class="sn-13__h">Quiet chrome, loud action</h3>
        <p class="sn-13__p">The bar carries a hairline and a whisper of shadow — enough to separate chrome from page, not enough to compete with the button.</p>
      </section>
    </main>
  <footer class="sn-13__pagefoot">
    <p class="sn-13__pagefootin">Sticky navigation pattern 13 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-13 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--sn-13-bg);
  --sn-13-bg: oklch(0.972 0.006 85);
  --sn-13-surface: oklch(0.995 0.003 85);
  --sn-13-ink: oklch(0.21 0.014 60);
  --sn-13-mut: oklch(0.52 0.014 60);
  --sn-13-acc: oklch(0.52 0.15 268);
  --sn-13-line: oklch(0.21 0.014 60/.1);
  --sn-13-h: 66px;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-13-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-13 *,
.sn-13 *::before,
.sn-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-13__skip {
  position: absolute;
  inset-block-start: 8px;
  inset-inline-start: 8px;
  z-index: 30;
  padding: 10px 16px;
  border-radius: 10px;
  background: var(--sn-13-ink);
  color: oklch(1 0 0);
  font-size: 13px;
  font-weight: 640;
  text-decoration: none;
  translate: 0 -160%;
  transition: translate .2s ease;
}

.sn-13__skip:focus-visible {
  translate: 0 0;
  outline: 2px solid var(--sn-13-acc);
  outline-offset: 2px;
}

.sn-13__bar {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  gap: clamp(12px,3vw,30px);
  min-height: var(--sn-13-h);
  padding: 0 clamp(18px,3.4vw,32px);
  background: color-mix(in oklch,var(--sn-13-surface) 82%,transparent);
  backdrop-filter: blur(14px) saturate(1.3);
  -webkit-backdrop-filter: blur(14px) saturate(1.3);
  border-bottom: 1px solid var(--sn-13-line);
  box-shadow: 0 8px 24px -22px oklch(0.21 0.014 60/.7);
}

.sn-13__brand {
  font-size: 19px;
  font-weight: 700;
  letter-spacing: -.035em;
  color: inherit;
  text-decoration: none;
}

.sn-13__nav {
  display: flex;
  align-items: center;
  gap: clamp(4px,1.4vw,14px);
  margin-inline-start: auto;
}

.sn-13__link {
  display: flex;
  align-items: center;
  min-height: 38px;
  padding: 0 6px;
  font-size: 13.6px;
  font-weight: 520;
  letter-spacing: .012em;
  color: var(--sn-13-mut);
  text-decoration: none;
  transition: color .18s ease;
}

.sn-13__link:hover {
  color: var(--sn-13-ink);
}

.sn-13__link[aria-current="page"] {
  color: var(--sn-13-ink);
}

.sn-13__cta {
  display: flex;
  align-items: center;
  min-height: 42px;
  padding: 0 20px;
  border-radius: 11px;
  font-size: 13.8px;
  font-weight: 640;
  letter-spacing: -.005em;
  color: oklch(1 0 0);
  background: var(--sn-13-acc);
  text-decoration: none;
  white-space: nowrap;
  box-shadow: 0 1px 2px oklch(0 0 0/.14),0 10px 24px -12px var(--sn-13-acc);
  transition: transform .16s ease,box-shadow .2s ease,filter .2s ease;
}

.sn-13__cta:hover {
  transform: translateY(-1.5px);
  box-shadow: 0 1px 2px oklch(0 0 0/.16),0 16px 30px -14px var(--sn-13-acc);
  filter: brightness(1.05);
}

.sn-13__cta:active {
  transform: translateY(0);
  box-shadow: 0 1px 2px oklch(0 0 0/.2);
}

.sn-13__link:focus-visible,
.sn-13__cta:focus-visible,
.sn-13__brand:focus-visible {
  outline: 2px solid var(--sn-13-acc);
  outline-offset: 3px;
  border-radius: 8px;
}

.sn-13__hero {
  display: grid;
  gap: 14px;
  align-content: center;
  min-height: 66svh;
  padding: clamp(28px,5vw,58px);
  max-width: 40ch;
}

.sn-13__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--sn-13-acc);
}

.sn-13__title {
  font-size: clamp(28px,5vw,46px);
  line-height: 1.04;
  letter-spacing: -.038em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-13__lead {
  font-size: 16.5px;
  line-height: 1.6;
  color: var(--sn-13-mut);
  text-wrap: pretty;
}

.sn-13__sec {
  scroll-margin-top: var(--sn-13-h);
  display: grid;
  gap: 10px;
  align-content: center;
  min-height: 66svh;
  padding: clamp(26px,5vw,58px);
  border-top: 1px solid var(--sn-13-line);
}

.sn-13__h {
  font-size: clamp(19px,2.6vw,25px);
  line-height: 1.18;
  letter-spacing: -.028em;
  font-weight: 680;
  text-wrap: balance;
}

.sn-13__p {
  max-width: 50ch;
  font-size: 15.4px;
  line-height: 1.7;
  color: var(--sn-13-mut);
  text-wrap: pretty;
}

@media (max-width: 620px) {
  .sn-13__nav {
    display: none;
  }

  .sn-13__cta {
    margin-inline-start: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-13 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-13) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-13-h) + 10px);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-13) {
    scroll-behavior: auto;
  }
}

.sn-13__bar,
.sn-13__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-13__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-13__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-13-line);
}

.sn-13__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-13-mut);
  text-align: center;
}

.sn-13__intro-title,
.sn-13__intro-sub {
  text-wrap: balance;
}
```
