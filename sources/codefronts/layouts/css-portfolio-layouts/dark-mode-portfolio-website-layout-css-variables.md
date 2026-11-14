---
source: "codefronts"
url: "https://codefronts.com/layouts/css-portfolio-layouts/dark-mode-portfolio-website-layout-css-variables/"
title: "Dark Mode Portfolio Website Layout CSS Variables"
section: "layouts"
category: "css-portfolio-layouts"
category_name: "CSS Portfolio Layouts"
description: "One layout, two skins, five lines of real logic: every color in the page routes through custom properties declared once for light and re-declared once under…"
has_js: "true"
---

Here's a working CSS Portfolio Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dark Mode Portfolio Website Layout CSS Variables
Source: https://codefronts.com/layouts/css-portfolio-layouts/dark-mode-portfolio-website-layout-css-variables/

One layout, two skins, five lines of real logic: every color in the page routes through custom properties declared once for light and re-declared once under [data-theme='dark'], so the toggle only flips an attribute. It respects prefers-color-scheme on first paint, the sun morphs into a moon with a pure-CSS mask trick, and color-scheme keeps native scrollbars and form controls in sync with the theme.
## HTML
```html
<section class="cpl-08" aria-label="Dark mode portfolio layout demo">
  <div class="cpl-08__page" id="cpl08-page">
    <header class="cpl-08__bar">
      <span class="cpl-08__brand"><i aria-hidden="true"></i>ren.dev</span>
      <nav class="cpl-08__nav" aria-label="Site">
        <a href="#work" aria-current="true">Work</a><a href="#notes">Notes</a><a href="#about">About</a>
      </nav>
      <button class="cpl-08__toggle" type="button" aria-pressed="false" aria-label="Switch to dark theme">
        <span class="cpl-08__orb" aria-hidden="true"></span>
      </button>
    </header>
    <main class="cpl-08__body">
      <div class="cpl-08__hero">
        <h2>Ren Okafor — front-end engineer who sweats the last 4%.</h2>
        <p>Design systems, performance budgets and interfaces that work at 2am. Previously at two startups you've heard of.</p>
      </div>
      <div class="cpl-08__cards">
        <a class="cpl-08__card" href="#tokens"><h3>Tokens at scale</h3><p>A theming architecture serving 6 products from one palette.</p><span>Case study →</span></a>
        <a class="cpl-08__card" href="#perf"><h3>The 90KB storefront</h3><p>Shipping a full e-commerce front end under a hard weight budget.</p><span>Case study →</span></a>
        <a class="cpl-08__card" href="#a11y"><h3>Keyboard-first checkout</h3><p>Rebuilding a payment flow to WCAG 2.2 AA without redesigning it.</p><span>Case study →</span></a>
      </div>
    </main>
  </div>
</section>
```
## CSS
```css
.cpl-08,
.cpl-08 *,
.cpl-08 *::before,
.cpl-08 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cpl-08 {
  font-family: 'Segoe UI',system-ui,sans-serif;
  container-type: inline-size;
}

.cpl-08__page {
  color-scheme: light;
  --bg: oklch(0.97 0.005 250);
  --card: oklch(1 0 0);
  --ink: oklch(0.23 0.02 260);
  --mut: oklch(0.53 0.015 260);
  --line: oklch(0.89 0.008 260);
  --acc: oklch(0.55 0.19 265);
  width: 100%;
  container: cpl08/inline-size;
  color: var(--ink);
  background: var(--bg);
  overflow: hidden;
  transition: background-color .4s,border-color .4s;
  min-height: 100vh;
  min-height: 100svh;
  display: flex;
  flex-direction: column;
}

.cpl-08__page[data-theme="dark"] {
  color-scheme: dark;
  --bg: oklch(0.19 0.02 265);
  --card: oklch(0.24 0.02 265);
  --ink: oklch(0.94 0.008 250);
  --mut: oklch(0.66 0.015 260);
  --line: oklch(0.31 0.02 265);
  --acc: oklch(0.75 0.14 85);
}

.cpl-08__bar {
  display: flex;
  align-items: center;
  gap: 22px;
  padding: 16px 24px;
  border-bottom: 1px solid var(--line);
  transition: border-color .4s;
}

.cpl-08__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-weight: 800;
  font-size: 15px;
  letter-spacing: -.01em;
}

.cpl-08__brand i {
  width: 10px;
  height: 10px;
  border-radius: 3px;
  background: var(--acc);
  transition: background .4s;
  rotate: 45deg;
}

.cpl-08__nav {
  display: flex;
  gap: 4px;
  margin-left: auto;
}

.cpl-08__nav a {
  display: grid;
  place-items: center;
  min-height: 36px;
  padding: 0 13px;
  border-radius: 9px;
  font-size: 13px;
  font-weight: 600;
  text-decoration: none;
  color: var(--mut);
  transition: color .2s,background .2s;
}

.cpl-08__nav a[aria-current],
.cpl-08__nav a:hover,
.cpl-08__nav a:focus-visible {
  color: var(--ink);
  background: color-mix(in oklch,var(--ink) 8%,transparent);
}

.cpl-08__nav a:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cpl-08__toggle {
  position: relative;
  width: 46px;
  height: 46px;
  border: 1px solid var(--line);
  border-radius: 50%;
  background: var(--card);
  cursor: pointer;
  display: grid;
  place-items: center;
  transition: background-color .4s,border-color .4s,scale .2s;
}

.cpl-08__toggle:hover {
  scale: 1.07;
}

.cpl-08__toggle:active {
  scale: .93;
}

.cpl-08__toggle:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cpl-08__orb {
  position: relative;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: var(--acc);
  transition: background .4s;
  mask: radial-gradient(circle 14px at 26px 4px,transparent 98%,#000);
  -webkit-mask: radial-gradient(circle 14px at 26px 4px,transparent 98%,#000);
  transition: background .4s,-webkit-mask-position .45s cubic-bezier(.4,0,.2,1),mask-position .45s cubic-bezier(.4,0,.2,1);
}

.cpl-08__page[data-theme="dark"] .cpl-08__orb {
  mask-position: -14px 8px;
  -webkit-mask-position: -14px 8px;
}

.cpl-08__body {
  flex: 1;
  align-content: center;
  padding: clamp(20px,4cqi,34px);
  display: grid;
  gap: 26px;
}

.cpl-08__hero h2 {
  font-size: clamp(21px,3.4cqi,29px);
  line-height: 1.18;
  letter-spacing: -.025em;
  max-width: 22em;
  text-wrap: balance;
}

.cpl-08__hero p {
  margin-top: 10px;
  font-size: 14px;
  line-height: 1.6;
  color: var(--mut);
  max-width: 52ch;
  transition: color .4s;
}

.cpl-08__cards {
  display: grid;
  gap: 14px;
  grid-template-columns: repeat(auto-fill,minmax(min(220px,100%),1fr));
}

.cpl-08__card {
  display: grid;
  gap: 8px;
  align-content: start;
  padding: 20px;
  border-radius: 16px;
  background: var(--card);
  border: 1px solid var(--line);
  text-decoration: none;
  color: inherit;
  transition: background-color .4s,border-color .3s,translate .25s cubic-bezier(.2,.7,.2,1);
}

.cpl-08__card:hover,
.cpl-08__card:focus-visible {
  translate: 0 -3px;
  border-color: color-mix(in oklch,var(--acc) 45%,var(--line));
}

.cpl-08__card:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.cpl-08__card h3 {
  font-size: 15.5px;
  letter-spacing: -.01em;
}

.cpl-08__card p {
  font-size: 13px;
  line-height: 1.55;
  color: var(--mut);
  transition: color .4s;
}

.cpl-08__card span {
  margin-top: 6px;
  font-size: 12.5px;
  font-weight: 700;
  color: var(--acc);
  transition: color .4s;
}

@media (prefers-reduced-motion: reduce) {
  .cpl-08 * {
    transition-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(function () {
  document.querySelectorAll('.cpl-08__page').forEach(function (page) {
    if (page.dataset.bound) return; page.dataset.bound = '1';
    var btn = page.querySelector('.cpl-08__toggle');
    function apply(dark) {
      page.toggleAttribute('data-theme', false);
      if (dark) page.setAttribute('data-theme', 'dark'); else page.removeAttribute('data-theme');
      btn.setAttribute('aria-pressed', String(dark));
      btn.setAttribute('aria-label', dark ? 'Switch to light theme' : 'Switch to dark theme');
    }
    apply(window.matchMedia('(prefers-color-scheme: dark)').matches);
    btn.addEventListener('click', function () { apply(!page.hasAttribute('data-theme')); });
  });
})();
```
