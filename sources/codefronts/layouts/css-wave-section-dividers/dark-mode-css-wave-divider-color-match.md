---
source: "codefronts"
url: "https://codefronts.com/layouts/css-wave-section-dividers/dark-mode-css-wave-divider-color-match/"
title: "Dark mode CSS wave divider color match"
section: "layouts"
category: "css-wave-section-dividers"
category_name: "CSS Wave Section Dividers"
description: "Three ways to make a wave follow your theme automatically — a working light/dark toggle with a currentColor wave, a prefers-color-scheme version with no…"
has_js: "true"
---

Here's a working CSS Wave Section Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark mode CSS wave divider color match
Source: https://codefronts.com/layouts/css-wave-section-dividers/dark-mode-css-wave-divider-color-match/

Three ways to make a wave follow your theme automatically — a working light/dark toggle with a currentColor wave, a prefers-color-scheme version with no JavaScript at all, and the modern light-dark() one-liner. Never hard-code a wave fill again.
## HTML
```html
<div class="wsd-11-group">
<section class="wsd-11a" id="wsd-11a" data-theme="dark">
  <div class="wsd-11a__hero">
    <button class="wsd-11a__toggle" id="wsd-11a-toggle" type="button" aria-pressed="true">
      <span class="wsd-11a__dot" aria-hidden="true"></span><span id="wsd-11a-toggle-label">Dark mode</span>
    </button>
    <h2 class="wsd-11a__title">The wave follows the theme</h2>
    <p class="wsd-11a__copy">fill: currentColor — nothing to recolour by hand.</p>
    <svg class="wsd-11a__wave" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,56 C260,116 540,4 820,50 C1060,88 1250,104 1440,72 L1440,120 L0,120 Z"></path>
    </svg>
  </div>
  <div class="wsd-11a__next"><p class="wsd-11a__copy">Both surfaces and the seam recolour from one token.</p></div>
</section>
<section class="wsd-11b">
  <div class="wsd-11b__hero">
    <h2 class="wsd-11b__title">Matches your OS right now</h2>
    <p class="wsd-11b__copy">Switch your system theme — this recolours with no script.</p>
    <svg class="wsd-11b__wave" viewBox="0 0 1440 110" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,50 C300,104 620,2 940,48 C1160,80 1300,92 1440,64 L1440,110 L0,110 Z"></path>
    </svg>
  </div>
  <div class="wsd-11b__next"><p class="wsd-11b__copy">One media query, both surfaces, one seam.</p></div>
</section>
<section class="wsd-11c">
  <div class="wsd-11c__hero">
    <h2 class="wsd-11c__title">light-dark(), one declaration</h2>
    <p class="wsd-11c__copy">--next: light-dark(#dbe4ee, #1b2430);</p>
    <svg class="wsd-11c__wave" viewBox="0 0 1440 100" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path d="M0,44 C240,96 520,0 800,42 C1040,78 1250,90 1440,58 L1440,100 L0,100 Z"></path>
    </svg>
  </div>
  <div class="wsd-11c__next"><p class="wsd-11c__copy">Keep a plain fallback above it for older browsers.</p></div>
</section>
</div>
```
## CSS
```css
.wsd-11-group {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.wsd-11-group > section {
  width: 100%;
}

.wsd-11a,
.wsd-11a *,
.wsd-11a *::before,
.wsd-11a *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-11a {
  --hero: oklch(0.96 0.01 250);
  --next: oklch(0.88 0.03 250);
  --text: oklch(0.24 0.02 250);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color-scheme: light;
}

.wsd-11a[data-theme="dark"] {
  --hero: oklch(0.17 0.02 260);
  --next: oklch(0.24 0.03 260);
  --text: oklch(0.95 0.01 260);
  color-scheme: dark;
}

.wsd-11a__hero {
  position: relative;
  background: var(--hero);
  color: var(--text);
  padding: 56px 24px 112px;
  text-align: center;
  transition: background .22s,color .22s;
}

.wsd-11a__toggle {
  display: inline-flex;
  align-items: center;
  gap: 9px;
  font-size: 13px;
  font-weight: 700;
  color: var(--text);
  background: color-mix(in oklab,var(--text) 10%,transparent);
  border: 1px solid color-mix(in oklab,var(--text) 24%,transparent);
  border-radius: 999px;
  padding: 8px 15px;
  margin-bottom: 22px;
  cursor: pointer;
  transition: background .2s;
}

.wsd-11a__toggle:hover {
  background: color-mix(in oklab,var(--text) 18%,transparent);
}

.wsd-11a__toggle:focus-visible {
  outline: 3px solid oklch(0.7 0.16 250);
  outline-offset: 3px;
}

.wsd-11a__dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: currentColor;
}

.wsd-11a__title {
  font-size: clamp(24px,3.8vw,38px);
  margin-bottom: 8px;
}

.wsd-11a__copy {
  font-size: 15px;
  opacity: .74;
  font-family: ui-monospace,monospace;
}

.wsd-11a__wave {
  position: absolute;
  left: 0;
  bottom: -1px;
  display: block;
  width: 100%;
  height: clamp(54px,8vw,110px);
  color: var(--next);
  pointer-events: none;
  transition: color .22s;
}

.wsd-11a__wave path {
  fill: currentColor;
}

.wsd-11a__next {
  background: var(--next);
  color: var(--text);
  padding: 22px 24px 56px;
  text-align: center;
  transition: background .22s,color .22s;
}

@media (prefers-reduced-motion: reduce) {
  .wsd-11a__hero,
    .wsd-11a__wave,
    .wsd-11a__next {
    transition: none;
  }
}

.wsd-11b,
.wsd-11b *,
.wsd-11b *::before,
.wsd-11b *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-11b {
  --hero: oklch(0.97 0.01 210);
  --next: oklch(0.87 0.04 210);
  --text: oklch(0.24 0.03 210);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

@media (prefers-color-scheme: dark) {
  .wsd-11b {
    --hero: oklch(0.16 0.02 215);
    --next: oklch(0.23 0.04 215);
    --text: oklch(0.95 0.01 215);
  }
}

.wsd-11b__hero {
  position: relative;
  background: var(--hero);
  color: var(--text);
  padding: 60px 24px 106px;
  text-align: center;
}

.wsd-11b__title {
  font-size: clamp(24px,3.8vw,36px);
  margin-bottom: 8px;
}

.wsd-11b__copy {
  font-size: 15px;
  opacity: .74;
}

.wsd-11b__wave {
  position: absolute;
  left: 0;
  bottom: -1px;
  display: block;
  width: 100%;
  height: clamp(50px,8vw,104px);
  color: var(--next);
  pointer-events: none;
}

.wsd-11b__wave path {
  fill: currentColor;
}

.wsd-11b__next {
  background: var(--next);
  color: var(--text);
  padding: 22px 24px 54px;
  text-align: center;
}

.wsd-11c,
.wsd-11c *,
.wsd-11c *::before,
.wsd-11c *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.wsd-11c {
  color-scheme: light dark;
  --hero: #f6f8fb;
  --hero: light-dark(#f6f8fb,#11161d);
  --next: #dbe4ee;
  --next: light-dark(#dbe4ee,#1b2430);
  --text: #22303c;
  --text: light-dark(#22303c,#eaf1f8);
  font-family: 'Segoe UI',system-ui,sans-serif;
}

.wsd-11c__hero {
  position: relative;
  background: var(--hero);
  color: var(--text);
  padding: 58px 24px 100px;
  text-align: center;
}

.wsd-11c__title {
  font-size: clamp(23px,3.6vw,34px);
  margin-bottom: 8px;
}

.wsd-11c__copy {
  font-size: 14px;
  font-family: ui-monospace,monospace;
  opacity: .72;
}

.wsd-11c__wave {
  position: absolute;
  left: 0;
  bottom: -1px;
  display: block;
  width: 100%;
  height: clamp(46px,7vw,96px);
  color: var(--next);
  pointer-events: none;
}

.wsd-11c__wave path {
  fill: currentColor;
}

.wsd-11c__next {
  background: var(--next);
  color: var(--text);
  padding: 22px 24px 52px;
  text-align: center;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('#wsd-11a');
  const btn = document.querySelector('#wsd-11a-toggle');
  const label = document.querySelector('#wsd-11a-toggle-label');
  if (!root || !btn || !label) return;
  // Respect the OS preference on first paint, then let the user override.
  const sysDark = matchMedia('(prefers-color-scheme: dark)').matches;
  const set = (dark) => {
    root.dataset.theme = dark ? 'dark' : 'light';
    btn.setAttribute('aria-pressed', String(dark));
    label.textContent = dark ? 'Dark mode' : 'Light mode';
  };
  set(sysDark);
  btn.addEventListener('click', () => set(root.dataset.theme !== 'dark'));
})();

/* No JavaScript — prefers-color-scheme flips the two surface tokens and the path inherits via currentColor. */

/* No JavaScript — light-dark() resolves per the page's color-scheme, so one token holds both theme values. */
```
