---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/neubrutalist-navbar-with-offset-shadow/"
title: "Neubrutalist Navbar with Offset Shadow"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "A sticky header block with a hard bottom shadow: wordmark left, links centre, black CTA right."
has_js: "true"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neubrutalist Navbar with Offset Shadow
Source: https://codefronts.com/design-styles/css-brutalist/neubrutalist-navbar-with-offset-shadow/

A sticky header block with a hard bottom shadow: wordmark left, links centre, black CTA right. The active link sits on a rotated pastel highlight block drawn with ::before, and at narrow widths a 20-line aria-expanded toggle opens a bordered panel — with @starting-style and transition-behavior: allow-discrete so the panel animates in and out of display:none.
## HTML
```html
<div class="brt-05">
  <button class="brt-05__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="brt-05__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-05__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
  </button>

  <div class="brt-05__stage">
    <header class="brt-05__bar">
      <a class="brt-05__brand" href="#brt-05-main"><span class="brt-05__mark" aria-hidden="true">P</span>Pagecraft</a>

      <nav class="brt-05__nav" aria-label="Primary">
        <ul class="brt-05__links">
          <li><a class="brt-05__link" href="#brt-05-main" aria-current="page">Product</a></li>
          <li><a class="brt-05__link" href="#brt-05-main">Templates</a></li>
          <li><a class="brt-05__link" href="#brt-05-main">Pricing</a></li>
          <li><a class="brt-05__link" href="#brt-05-main">Changelog</a></li>
        </ul>
      </nav>

      <div class="brt-05__end">
        <a class="brt-05__ghost" href="#brt-05-main">Sign in</a>
        <a class="brt-05__cta" href="#brt-05-main">Start building</a>
        <button class="brt-05__burger" id="brt-05-burger" type="button" aria-expanded="false" aria-controls="brt-05-panel" aria-label="Open menu">
          <span class="brt-05__bars" aria-hidden="true"></span>
        </button>
      </div>
    </header>

    <div class="brt-05__panel" id="brt-05-panel" hidden>
      <ul class="brt-05__panellinks">
        <li><a href="#brt-05-main" aria-current="page">Product</a></li>
        <li><a href="#brt-05-main">Templates</a></li>
        <li><a href="#brt-05-main">Pricing</a></li>
        <li><a href="#brt-05-main">Changelog</a></li>
        <li><a href="#brt-05-main">Sign in</a></li>
      </ul>
    </div>

    <main class="brt-05__main" id="brt-05-main">
      <h1 class="brt-05__h">Landing pages, built in the browser</h1>
      <p class="brt-05__p">Resize the frame to see the bar collapse into a bordered panel. The bar stays stuck to the top while this column scrolls.</p>
      <ul class="brt-05__filler">
        <li>Drag-and-drop sections with real CSS output</li>
        <li>Publish to your own domain in one step</li>
        <li>Version history for every page</li>
      </ul>
    </main>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap');

.brt-05 {
  --page: #f7f4ec;
  --panel: #ffffff;
  --ink: #0b0b0f;
  --on: #0b0b0f;
  --muted: #4a4a52;
  --lilac: #c4b5fd;
  --mint: #86efac;
  --coral: #fda4af;
  --butter: #fde68a;
  --sky: #93c5fd;
  --hl: #fde68a;
  --edge: #000000;
  --sh: #000000;
  --bw: 3px;
  --r: 12px;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: 'Space Grotesk','Sora',ui-sans-serif,system-ui,sans-serif;
}

.brt-05 *,
.brt-05 *::before,
.brt-05 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-05 {
    --page: oklch(0.968 0.016 88);
    --panel: oklch(1 0 0);
    --ink: oklch(0.16 0.01 285);
    --lilac: oklch(0.82 0.11 296);
    --mint: oklch(0.89 0.13 155);
    --coral: oklch(0.83 0.10 15);
    --butter: oklch(0.92 0.11 95);
    --sky: oklch(0.83 0.09 250);
    --hl: oklch(0.92 0.11 95);
  }
}

.brt-05__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 20;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  padding: 0;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  border-radius: 10px;
  box-shadow: 4px 4px 0 var(--sh);
  cursor: pointer;
  transition: translate .14s ease, box-shadow .14s ease;
}

.brt-05__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-05__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-05__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-05__theme:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-05__sun {
  display: none;
}

.brt-05__stage {
  min-height: 100vh;
  min-height: 100svh;
  padding: clamp(1rem,3vw,2rem);
  padding-block-start: 1rem;
}

.brt-05__bar {
  position: sticky;
  inset-block-start: 1rem;
  z-index: 10;
  inline-size: min(72rem,100%);
  margin-inline: auto;
  display: flex;
  align-items: center;
  gap: clamp(.5rem,2vw,1.5rem);
  padding: .7rem .8rem;
  padding-inline-end: 3.6rem;
  background: var(--panel);
  border: var(--bw) solid var(--edge);
  border-radius: var(--r);
  box-shadow: 0 6px 0 var(--sh);
}

.brt-05__brand {
  display: flex;
  align-items: center;
  gap: .5rem;
  color: var(--ink);
  text-decoration: none;
  font-weight: 700;
  font-size: 1.05rem;
  letter-spacing: -.02em;
  white-space: nowrap;
}

.brt-05__brand:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
  border-radius: 6px;
}

.brt-05__mark {
  display: grid;
  place-items: center;
  inline-size: 1.9rem;
  block-size: 1.9rem;
  background: var(--lilac);
  color: var(--on);
  border: var(--bw) solid var(--edge);
  border-radius: 8px;
  font-size: .9rem;
}

.brt-05__nav {
  margin-inline: auto;
}

.brt-05__links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  align-items: center;
  gap: .35rem;
}

.brt-05__link {
  position: relative;
  isolation: isolate;
  display: inline-flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: .5rem .7rem;
  border-radius: 8px;
  color: var(--ink);
  text-decoration: none;
  font-weight: 600;
  font-size: .95rem;
  transition: translate .14s ease, box-shadow .14s ease;
}

.brt-05__link:hover {
  border: 2px solid var(--edge);
  padding: calc(.5rem - 2px) calc(.7rem - 2px);
  box-shadow: 3px 3px 0 var(--sh);
}

.brt-05__link:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 2px;
}

.brt-05__link[aria-current="page"]::before {
  content: '';
  position: absolute;
  inset: .35rem -.15rem;
  z-index: -1;
  background: var(--hl);
  border: 2px solid var(--edge);
  border-radius: 7px;
  rotate: -1.5deg;
}

.brt-05__end {
  display: flex;
  align-items: center;
  gap: .5rem;
}

.brt-05__ghost {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: .5rem .7rem;
  color: var(--ink);
  text-decoration: none;
  font-weight: 600;
  font-size: .95rem;
  border-radius: 8px;
}

.brt-05__ghost:hover {
  text-decoration: 3px underline var(--sky);
  text-underline-offset: 4px;
}

.brt-05__ghost:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 2px;
}

.brt-05__cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: .6rem 1rem;
  background: var(--ink);
  color: var(--page);
  text-decoration: none;
  font-weight: 700;
  font-size: .95rem;
  border: var(--bw) solid var(--edge);
  border-radius: 10px;
  box-shadow: 4px 4px 0 var(--sh);
  transition: translate .14s ease, box-shadow .14s ease;
  white-space: nowrap;
}

.brt-05__cta:hover {
  translate: -1px -1px;
  box-shadow: 5px 5px 0 var(--sh);
}

.brt-05__cta:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-05__cta:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-05__burger {
  display: none;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  padding: 0;
  background: var(--butter);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  border-radius: 10px;
  box-shadow: 4px 4px 0 var(--sh);
  cursor: pointer;
  transition: translate .14s ease, box-shadow .14s ease;
}

.brt-05__burger:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-05__burger:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-05__bars {
  position: relative;
  display: block;
  inline-size: 1.15rem;
  block-size: 3px;
  background: currentColor;
}

.brt-05__bars::before,
.brt-05__bars::after {
  content: '';
  position: absolute;
  inset-inline: 0;
  block-size: 3px;
  background: currentColor;
  transition: translate .16s ease, rotate .16s ease;
}

.brt-05__bars::before {
  translate: 0 -6px;
}

.brt-05__bars::after {
  translate: 0 6px;
}

.brt-05__burger[aria-expanded="true"] .brt-05__bars {
  background: transparent;
}

.brt-05__burger[aria-expanded="true"] .brt-05__bars::before {
  translate: 0 0;
  rotate: 45deg;
}

.brt-05__burger[aria-expanded="true"] .brt-05__bars::after {
  translate: 0 0;
  rotate: -45deg;
}

.brt-05__panel {
  inline-size: min(72rem,100%);
  margin: .75rem auto 0;
  padding: .6rem;
  background: var(--panel);
  border: var(--bw) solid var(--edge);
  border-radius: var(--r);
  box-shadow: 0 6px 0 var(--sh);
  position: relative;
  z-index: 9;
  opacity: 1;
  translate: 0 0;
  transition: opacity .16s ease, translate .16s ease, display .16s allow-discrete;
}

@starting-style {
  .brt-05__panel {
    opacity: 0;
    translate: 0 -8px;
  }
}

.brt-05__panel[hidden] {
  display: none;
  opacity: 0;
  translate: 0 -8px;
}

.brt-05__panellinks {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .3rem;
}

.brt-05__panellinks a {
  display: flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: .6rem .8rem;
  color: var(--ink);
  text-decoration: none;
  font-weight: 700;
  border: 2px solid transparent;
  border-radius: 9px;
}

.brt-05__panellinks a:hover {
  background: var(--mint);
  color: var(--on);
  border-color: var(--edge);
  box-shadow: 3px 3px 0 var(--sh);
}

.brt-05__panellinks a[aria-current="page"] {
  background: var(--ink);
  color: var(--page);
  border-color: var(--edge);
}

.brt-05__panellinks a:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 2px;
}

.brt-05__main {
  inline-size: min(72rem,100%);
  margin-inline: auto;
  padding-block: clamp(2rem,6vw,4rem) 2rem;
}

.brt-05__h {
  margin: 0;
  font-size: clamp(1.9rem,5.5vw,3.4rem);
  font-weight: 700;
  letter-spacing: -.03em;
  line-height: 1.03;
  max-inline-size: 22ch;
  text-wrap: balance;
}

.brt-05__p {
  margin: 1rem 0 0;
  max-inline-size: 48ch;
  font-size: 1.02rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.brt-05__filler {
  list-style: none;
  margin: 1.75rem 0 0;
  padding: 0;
  display: grid;
  gap: .6rem;
  max-inline-size: 36rem;
}

.brt-05__filler li {
  padding: .8rem .95rem;
  background: var(--panel);
  border: 2px solid var(--edge);
  border-radius: 10px;
  box-shadow: 4px 4px 0 var(--sh);
  font-weight: 600;
  font-size: .95rem;
}

@media (max-width: 56rem) {
  .brt-05__nav,
    .brt-05__ghost {
    display: none;
  }

  .brt-05__burger {
    display: grid;
  }

  .brt-05__nav + .brt-05__end {
    margin-inline-start: auto;
  }

  .brt-05__end {
    margin-inline-start: auto;
  }
}

@media (max-width: 30rem) {
  .brt-05__cta {
    display: none;
  }
}

.brt-05[data-theme="dark"] {
  --page: #131218;
  --panel: #201e28;
  --ink: #f7f5ef;
  --muted: #b5b1c2;
  --edge: #f7f5ef;
  --sh: #f7f5ef;
}

.brt-05[data-theme="dark"] .brt-05__moon {
  display: none;
}

.brt-05[data-theme="dark"] .brt-05__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-05:not([data-theme="light"]) {
    --page: #131218;
    --panel: #201e28;
    --ink: #f7f5ef;
    --muted: #b5b1c2;
    --edge: #f7f5ef;
    --sh: #f7f5ef;
  }

  .brt-05:not([data-theme="light"]) .brt-05__moon {
    display: none;
  }

  .brt-05:not([data-theme="light"]) .brt-05__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-05 *,
    .brt-05 *::before,
    .brt-05 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .brt-05__bar,
    .brt-05__panel,
    .brt-05__cta,
    .brt-05__burger,
    .brt-05__theme {
    border-color: CanvasText;
    box-shadow: none;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-05__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.brt-05');
  if (!root) return;
  const btn = root.querySelector('#brt-05-burger');
  const panel = root.querySelector('#brt-05-panel');
  const set = (open) => {
    btn.setAttribute('aria-expanded', String(open));
    btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    panel.toggleAttribute('hidden', !open);
    if (open) panel.querySelector('a').focus();
  };
  btn.addEventListener('click', () => set(btn.getAttribute('aria-expanded') !== 'true'));
  root.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && btn.getAttribute('aria-expanded') === 'true') { set(false); btn.focus(); }
  });
  panel.addEventListener('click', (e) => { if (e.target.closest('a')) set(false); });
  matchMedia('(min-width: 56rem)').addEventListener('change', (e) => { if (e.matches) set(false); });
})();

(() => {                                     /* theme toggle */
  const root = document.querySelector('.brt-05');
  const btn = root && root.querySelector('.brt-05__theme');
  if (!btn) return;
  const dark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => {
    btn.setAttribute('aria-pressed', String(dark()));
    btn.setAttribute('aria-label', dark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  btn.addEventListener('click', () => { root.dataset.theme = dark() ? 'light' : 'dark'; sync(); });
  sync();
})();
```
