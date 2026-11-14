---
source: "codefronts"
url: "https://codefronts.com/navigation/css-sticky-navigation/sticky-header-with-theme-aware-token-swap-light-dark/"
title: "Sticky Header with Theme-Aware Token Swap (Light/Dark)"
section: "navigation"
category: "css-sticky-navigation"
category_name: "CSS Sticky Navigations"
description: "Theming a sticky header is harder than theming a page, because translucent chrome has to stay legible over whatever scrolls beneath it in both schemes."
has_js: "true"
---

Here's a working CSS Sticky Navigation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Header with Theme-Aware Token Swap (Light/Dark)
Source: https://codefronts.com/navigation/css-sticky-navigation/sticky-header-with-theme-aware-token-swap-light-dark/

Theming a sticky header is harder than theming a page, because translucent chrome has to stay legible over whatever scrolls beneath it in both schemes. This demo wires the modern token cascade — system preference as the default, an explicit override on top — using the light-dark() function, so a single token definition serves both themes instead of two duplicated blocks.
## HTML
```html
<section class="sn-12" id="sn-12-root" aria-label="Theme-aware sticky header demo">
    <header class="sn-12__bar">
      <a class="sn-12__brand" href="#sn-12-s1"><span class="sn-12__logo" aria-hidden="true"></span>Palette</a>
      <nav class="sn-12__nav" aria-label="Primary">
        <a class="sn-12__link" href="#sn-12-s1" aria-current="page">Tokens</a>
        <a class="sn-12__link" href="#sn-12-s2">Themes</a>
        <a class="sn-12__link" href="#sn-12-s3">Contrast</a>
      </nav>
      <button class="sn-12__toggle" type="button" id="sn-12-toggle" aria-pressed="false" aria-label="Switch to dark theme">
        <span class="sn-12__sun" aria-hidden="true"></span>
        <span class="sn-12__tlabel">Dark</span>
      </button>
    </header>
  <div class="sn-12__intro">
    <div class="sn-12__introin">
    <p class="sn-12__intro-eyebrow">light-dark() · color-scheme</p>
    <h2 class="sn-12__intro-title">One token, two themes</h2>
    </div>
  </div>
    <main>
      <section class="sn-12__sec" id="sn-12-s1">
        <p class="sn-12__kicker">Tokens</p>
        <h3 class="sn-12__h">Declared once, resolved twice</h3>
        <p class="sn-12__p">Each token carries both of its values in a single <code>light-dark()</code> call. No duplicated media-query block, no third override table.</p>
        <div class="sn-12__swatches">
          <span class="sn-12__sw sn-12__sw--surface">surface</span>
          <span class="sn-12__sw sn-12__sw--raised">raised</span>
          <span class="sn-12__sw sn-12__sw--acc">accent</span>
        </div>
      </section>
      <section class="sn-12__sec" id="sn-12-s2">
        <p class="sn-12__kicker">Themes</p>
        <h3 class="sn-12__h">The attribute changes everything</h3>
        <p class="sn-12__p">Flipping <code>color-scheme</code> also repaints scrollbars, focus rings and native controls — the parts a variables-only theme always forgets.</p>
      </section>
      <section class="sn-12__sec" id="sn-12-s3">
        <p class="sn-12__kicker">Contrast</p>
        <h3 class="sn-12__h">Dark is not inverted light</h3>
        <p class="sn-12__p">Borders gain contrast, shadows get lighter, and the accent shifts up in lightness so it still reads against a near-black surface.</p>
      </section>
    </main>
  <footer class="sn-12__pagefoot">
    <p class="sn-12__pagefootin">Sticky navigation pattern 12 of 25 · codefronts.com</p>
  </footer>
</section>
```
## CSS
```css
.sn-12 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  color-scheme: light dark;
  --sn-12-bg: light-dark(oklch(0.96 0.008 265),oklch(0.16 0.02 265));
  --sn-12-surface: light-dark(oklch(1 0 0),oklch(0.21 0.022 265));
  --sn-12-raised: light-dark(oklch(0.975 0.005 265),oklch(0.26 0.025 265));
  --sn-12-ink: light-dark(oklch(0.21 0.022 265),oklch(0.97 0.005 265));
  --sn-12-mut: light-dark(oklch(0.53 0.02 265),oklch(0.73 0.016 265));
  --sn-12-acc: light-dark(oklch(0.55 0.19 274),oklch(0.8 0.15 274));
  --sn-12-line: light-dark(oklch(0.21 0.022 265/.12),oklch(1 0 0/.13));
  --sn-12-h: 64px;
  background: var(--sn-12-bg);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--sn-12-ink);
  -webkit-font-smoothing: antialiased;
}

.sn-12[data-theme="light"] {
  color-scheme: light;
}

.sn-12[data-theme="dark"] {
  color-scheme: dark;
}

.sn-12 *,
.sn-12 *::before,
.sn-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.sn-12__eyebrow,
.sn-12__intro-eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .13em;
  text-transform: uppercase;
  color: var(--sn-12-acc);
}

.sn-12__title,
.sn-12__intro-title {
  font-size: clamp(23px,3.5vw,37px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.sn-12__bar {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  gap: clamp(10px,2vw,22px);
  min-height: var(--sn-12-h);
  padding: 0 clamp(14px,2.6vw,22px);
  background: color-mix(in oklch,var(--sn-12-surface) 84%,transparent);
  backdrop-filter: blur(16px) saturate(1.4);
  -webkit-backdrop-filter: blur(16px) saturate(1.4);
  border-bottom: 1px solid var(--sn-12-line);
  transition: background .3s ease,border-color .3s ease;
}

.sn-12__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.025em;
  color: inherit;
  text-decoration: none;
}

.sn-12__logo {
  width: 19px;
  height: 19px;
  border-radius: 6px;
  background: linear-gradient(140deg,var(--sn-12-acc),oklch(0.72 0.15 200));
}

.sn-12__nav {
  display: flex;
  align-items: center;
  gap: 2px;
  margin-inline-start: auto;
}

.sn-12__link {
  display: flex;
  align-items: center;
  min-height: 36px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 13.6px;
  font-weight: 600;
  color: var(--sn-12-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.sn-12__link:hover {
  color: var(--sn-12-ink);
  background: color-mix(in oklch,var(--sn-12-ink) 7%,transparent);
}

.sn-12__link[aria-current="page"] {
  color: var(--sn-12-acc);
  background: color-mix(in oklch,var(--sn-12-acc) 12%,transparent);
}

.sn-12__toggle {
  display: flex;
  align-items: center;
  gap: 8px;
  min-height: 38px;
  padding: 0 14px;
  border: 1px solid var(--sn-12-line);
  border-radius: 99px;
  background: var(--sn-12-raised);
  color: var(--sn-12-ink);
  font-family: inherit;
  font-size: 13px;
  font-weight: 640;
  cursor: pointer;
  transition: background .2s ease,border-color .2s ease;
}

.sn-12__toggle:hover {
  border-color: color-mix(in oklch,var(--sn-12-acc) 50%,var(--sn-12-line));
}

.sn-12__sun {
  position: relative;
  inline-size: 14px;
  block-size: 14px;
  border-radius: 50%;
  background: var(--sn-12-acc);
  box-shadow: 0 0 0 0 transparent;
  transition: box-shadow .3s ease,background .3s ease,clip-path .3s ease;
  clip-path: circle(60% at 50% 50%);
}

.sn-12__toggle[aria-pressed="true"] .sn-12__sun {
  clip-path: circle(56% at 72% 34%);
  background: var(--sn-12-acc);
}

.sn-12__link:focus-visible,
.sn-12__toggle:focus-visible,
.sn-12__brand:focus-visible {
  outline: 2px solid var(--sn-12-acc);
  outline-offset: 2px;
}

.sn-12__sec {
  scroll-margin-top: var(--sn-12-h);
  display: grid;
  gap: 11px;
  align-content: center;
  min-height: 66svh;
  padding: clamp(24px,4vw,46px);
  border-bottom: 1px solid var(--sn-12-line);
}

.sn-12__sec:nth-child(even) {
  background: var(--sn-12-raised);
}

.sn-12__kicker {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--sn-12-acc);
}

.sn-12__h {
  font-size: clamp(19px,2.6vw,26px);
  line-height: 1.16;
  letter-spacing: -.025em;
  font-weight: 690;
  text-wrap: balance;
}

.sn-12__p {
  max-width: 52ch;
  font-size: 14.8px;
  line-height: 1.64;
  color: var(--sn-12-mut);
  text-wrap: pretty;
}

.sn-12__p code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .85em;
  background: color-mix(in oklch,var(--sn-12-ink) 8%,transparent);
  padding: 2px 6px;
  border-radius: 5px;
}

.sn-12__swatches {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-block-start: 4px;
}

.sn-12__sw {
  display: flex;
  align-items: center;
  min-height: 34px;
  padding: 0 14px;
  border-radius: 99px;
  border: 1px solid var(--sn-12-line);
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11px;
  letter-spacing: .04em;
}

.sn-12__sw--surface {
  background: var(--sn-12-surface);
}

.sn-12__sw--raised {
  background: var(--sn-12-raised);
}

.sn-12__sw--acc {
  background: var(--sn-12-acc);
  color: light-dark(oklch(1 0 0),oklch(0.16 0.02 265));
  border-color: transparent;
}

@media (max-width: 600px) {
  .sn-12__tlabel {
    display: none;
  }

  .sn-12__toggle {
    padding-inline: 12px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sn-12 * {
    transition-duration: .01ms !important;
  }
}
/* ── full-page mode: the demo IS the document, so sticky pins against the real viewport ── */

:root:has(.sn-12) {
  scroll-behavior: smooth;
  scroll-padding-top: calc(var(--sn-12-h) + 8px);
}

@media (prefers-reduced-motion: reduce) {
  :root:has(.sn-12) {
    scroll-behavior: auto;
  }
}

.sn-12__bar,
.sn-12__barin {
  padding-inline: max(clamp(16px,3vw,26px),calc((100% - 1280px)/2));
}

.sn-12__sec {
  padding-inline: max(clamp(22px,5vw,44px),calc((100% - 1120px)/2));
}

.sn-12__intro {
  display: grid;
  place-items: center;
  min-height: min(90svh,900px);
  padding: clamp(56px,12vh,150px) clamp(20px,5vw,48px) clamp(40px,8vh,90px);
}

.sn-12__introin {
  display: grid;
  justify-items: center;
  gap: clamp(12px,1.8vw,18px);
  text-align: center;
  max-width: 26ch;
}

.sn-12__intro-eyebrow {
  font-size: clamp(11px,1.1vw,13px);
}

.sn-12__intro-title {
  font-size: clamp(38px,7.5vw,86px);
  line-height: .98;
  letter-spacing: -.04em;
  max-width: none;
}

.sn-12__intro-sub {
  font-size: clamp(15px,1.7vw,19px);
  line-height: 1.55;
  max-width: 46ch;
}

.sn-12__intro::after {
  content: "Scroll — the bar stays";
  justify-self: center;
  margin-block-start: clamp(20px,4vh,44px);
  padding: 9px 18px;
  border: 1px solid var(--sn-12-line);
  border-radius: 99px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--sn-12-mut);
  animation: sn-12-cue 2.6s ease-in-out infinite;
}

@keyframes sn-12-cue {
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
  .sn-12__intro::after {
    animation: none;
  }
}

.sn-12__pagefoot {
  display: grid;
  place-items: center;
  padding: clamp(44px,9vh,110px) 24px;
  border-top: 1px solid var(--sn-12-line);
}

.sn-12__pagefootin {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  letter-spacing: .06em;
  color: var(--sn-12-mut);
  text-align: center;
}

.sn-12__intro-title,
.sn-12__intro-sub {
  text-wrap: balance;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('#sn-12-root');
  if (!root || root.dataset.snWired) return;
  root.dataset.snWired = '1';
  const btn = root.querySelector('#sn-12-toggle');
  const label = btn.querySelector('.sn-12__tlabel');
  const dark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const apply = (isDark) => {
    root.dataset.theme = isDark ? 'dark' : 'light';
    btn.setAttribute('aria-pressed', String(isDark));
    btn.setAttribute('aria-label', isDark ? 'Switch to light theme' : 'Switch to dark theme');
    label.textContent = isDark ? 'Light' : 'Dark';
  };
  btn.addEventListener('click', () => apply(btn.getAttribute('aria-pressed') !== 'true'));
  apply(dark);
})();
```
