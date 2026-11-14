---
source: "codefronts"
url: "https://codefronts.com/layouts/css-footer-designs/sticky-footer-to-bottom-of-page-flexbox-and-css-grid/"
title: "Sticky Footer to Bottom of Page (Flexbox & CSS Grid)"
section: "layouts"
category: "css-footer-designs"
category_name: "CSS Footer Designs"
description: "The layout every other footer in this collection sits on: a footer that rests on the bottom edge of the viewport when the page is short, and gets pushed down…"
has_js: "true"
---

Here's a working CSS Footer Design from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticky Footer to Bottom of Page (Flexbox & CSS Grid)
Source: https://codefronts.com/layouts/css-footer-designs/sticky-footer-to-bottom-of-page-flexbox-and-css-grid/

The layout every other footer in this collection sits on: a footer that rests on the bottom edge of the viewport when the page is short, and gets pushed down naturally when the page is long — no position:fixed, no calc(100vh - 180px), no JavaScript measuring anything. Both the Grid and the Flexbox recipe are wired to a live switch so you can watch them behave identically.
## HTML
```html
<section class="ft-01" data-mode="grid" aria-label="Sticky footer to bottom of page demo">
  <main class="ft-01__main">
    <p class="ft-01__eyebrow">grid-template-rows: 1fr auto</p>
    <h1 class="ft-01__title">The footer that knows where the bottom is</h1>
    <p class="ft-01__sub">This page is deliberately short. The footer is still welded to the bottom edge — and the moment the content outgrows the screen it is pushed down instead of overlapping. Same result from Grid and from Flexbox.</p>
    <div class="ft-01__switch" role="group" aria-label="Layout technique">
      <button class="ft-01__seg" type="button" data-set="grid" aria-pressed="true">CSS Grid</button>
      <button class="ft-01__seg" type="button" data-set="flex" aria-pressed="false">Flexbox</button>
    </div>
    <div class="ft-01__tools">
      <button class="ft-01__ghost" type="button" id="ft-01-add">Add a paragraph</button>
      <button class="ft-01__ghost" type="button" id="ft-01-reset">Reset page</button>
    </div>
    <div class="ft-01__grow" id="ft-01-grow"></div>
    <p class="ft-01__live" id="ft-01-live" role="status" aria-live="polite">Layout: CSS Grid · page is shorter than the viewport</p>
  </main>
  <footer class="ft-01__foot">
    <div class="ft-01__brand"><span class="ft-01__mark" aria-hidden="true"></span>Meridian</div>
    <nav class="ft-01__nav" aria-label="Footer">
      <a class="ft-01__link" href="#ft-01-privacy">Privacy</a>
      <a class="ft-01__link" href="#ft-01-terms">Terms</a>
      <a class="ft-01__link" href="#ft-01-status">Status</a>
      <a class="ft-01__link" href="#ft-01-contact">Contact</a>
    </nav>
    <p class="ft-01__copy">© <time datetime="2026">2026</time> Meridian Labs</p>
  </footer>
</section>
```
## CSS
```css
.ft-01 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  grid-template-rows: 1fr auto;
  background: var(--ft-01-bg);
  --ft-01-bg: oklch(0.972 0.006 265);
  --ft-01-surface: oklch(1 0 0);
  --ft-01-ink: oklch(0.22 0.024 272);
  --ft-01-mut: oklch(0.55 0.018 272);
  --ft-01-acc: oklch(0.56 0.19 272);
  --ft-01-line: oklch(0.22 0.024 272/.11);
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--ft-01-ink);
  -webkit-font-smoothing: antialiased;
}

.ft-01 *,
.ft-01 *::before,
.ft-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ft-01[data-mode="flex"] {
  display: flex;
  flex-direction: column;
}

.ft-01[data-mode="flex"] .ft-01__main {
  flex: 1;
}

.ft-01__main {
  display: grid;
  align-content: center;
  justify-items: start;
  gap: 16px;
  padding-block: clamp(48px,10vh,110px);
  padding-inline: max(clamp(20px,5vw,44px),calc((100% - 1000px)/2));
  background: radial-gradient(88% 62% at 12% 0%,oklch(0.99 0.016 272),transparent);
}

.ft-01__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: clamp(11px,1.1vw,12.5px);
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--ft-01-acc);
}

.ft-01__title {
  font-size: clamp(32px,6vw,64px);
  line-height: 1.02;
  letter-spacing: -.04em;
  font-weight: 700;
  max-width: 16ch;
  text-wrap: balance;
}

.ft-01__sub {
  font-size: clamp(15px,1.6vw,18px);
  line-height: 1.6;
  color: var(--ft-01-mut);
  max-width: 56ch;
  text-wrap: pretty;
}

.ft-01__switch {
  display: inline-flex;
  gap: 4px;
  padding: 4px;
  margin-block-start: 8px;
  border-radius: 12px;
  background: var(--ft-01-surface);
  border: 1px solid var(--ft-01-line);
  box-shadow: 0 1px 2px oklch(0.22 0.024 272/.05);
}

.ft-01__seg {
  min-height: 40px;
  padding: 0 18px;
  border: 0;
  border-radius: 9px;
  background: transparent;
  font: inherit;
  font-size: 14px;
  font-weight: 600;
  color: var(--ft-01-mut);
  cursor: pointer;
  transition: background .2s ease,color .2s ease;
}

.ft-01__seg[aria-pressed="true"] {
  background: var(--ft-01-ink);
  color: oklch(1 0 0);
}

.ft-01__seg:hover:not([aria-pressed="true"]) {
  color: var(--ft-01-ink);
  background: oklch(0.22 0.024 272/.05);
}

.ft-01__tools {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.ft-01__ghost {
  min-height: 44px;
  padding: 0 18px;
  border: 1px solid var(--ft-01-line);
  border-radius: 11px;
  background: var(--ft-01-surface);
  font: inherit;
  font-size: 14px;
  font-weight: 600;
  color: var(--ft-01-ink);
  cursor: pointer;
  transition: transform .18s ease,border-color .18s ease,box-shadow .18s ease;
}

.ft-01__ghost:hover {
  transform: translateY(-1px);
  border-color: var(--ft-01-acc);
  box-shadow: 0 6px 18px -10px var(--ft-01-acc);
}

.ft-01__seg:focus-visible,
.ft-01__ghost:focus-visible,
.ft-01__link:focus-visible {
  outline: 2px solid var(--ft-01-acc);
  outline-offset: 2px;
}

.ft-01__grow {
  display: grid;
  gap: 14px;
  max-width: 62ch;
}

.ft-01__grow p {
  font-size: 15px;
  line-height: 1.65;
  color: var(--ft-01-mut);
  padding-inline-start: 16px;
  border-inline-start: 2px solid color-mix(in oklch,var(--ft-01-acc) 40%,transparent);
  animation: ft-01-in .4s ease both;
}

@keyframes ft-01-in {
  from {
    opacity: 0;
    transform: translateY(8px);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

.ft-01__live {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  color: var(--ft-01-mut);
}

.ft-01__foot {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 14px 26px;
  padding-block: 22px;
  padding-bottom: calc(22px + env(safe-area-inset-bottom,0px));
  padding-inline: max(clamp(20px,5vw,44px),calc((100% - 1000px)/2));
  background: var(--ft-01-surface);
  border-top: 1px solid var(--ft-01-line);
}

.ft-01__brand {
  display: flex;
  align-items: center;
  gap: 9px;
  font-size: 15px;
  font-weight: 700;
  letter-spacing: -.02em;
}

.ft-01__mark {
  width: 20px;
  height: 20px;
  border-radius: 7px;
  background: linear-gradient(140deg,var(--ft-01-acc),oklch(0.72 0.16 330));
  box-shadow: 0 4px 12px -4px var(--ft-01-acc);
}

.ft-01__nav {
  display: flex;
  flex-wrap: wrap;
  gap: 2px;
  margin-inline-start: auto;
}

.ft-01__link {
  display: flex;
  align-items: center;
  min-height: 40px;
  padding: 0 12px;
  border-radius: 9px;
  font-size: 14px;
  font-weight: 600;
  color: var(--ft-01-mut);
  text-decoration: none;
  transition: color .18s ease,background .18s ease;
}

.ft-01__link:hover {
  color: var(--ft-01-ink);
  background: oklch(0.22 0.024 272/.05);
}

.ft-01__copy {
  font-size: 13.5px;
  color: var(--ft-01-mut);
}

@media (max-width: 720px) {
  .ft-01__nav {
    margin-inline-start: 0;
    order: 3;
    width: 100%;
  }

  .ft-01__copy {
    margin-inline-start: auto;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ft-01 * {
    transition-duration: .01ms !important;
    animation-duration: .01ms !important;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.ft-01');
  if (!root || root.dataset.ready) return;
  root.dataset.ready = '1';
  const grow = root.querySelector('#ft-01-grow');
  const live = root.querySelector('#ft-01-live');
  const lines = [
    'Add enough content and the 1fr row outgrows the viewport — the footer is pushed below the fold exactly as it should be, with no overlap.',
    'Nothing here is fixed to the viewport, so there is no scroll listener, no resize observer and no layout thrash on a long page.',
    'The same markup drives both techniques: only the display value on the shell changes between Grid and Flexbox.',
    'Because the footer is in normal flow, a screen reader reaches it in document order and the contentinfo landmark is announced once.'
  ];
  let i = 0;
  const report = () => {
    const mode = root.dataset.mode === 'flex' ? 'Flexbox' : 'CSS Grid';
    const tall = root.scrollHeight > window.innerHeight + 4;
    live.textContent = 'Layout: ' + mode + ' · page is ' + (tall ? 'taller than the viewport — footer pushed down' : 'shorter than the viewport — footer pinned to the bottom');
  };
  root.querySelectorAll('.ft-01__seg').forEach((b) => b.addEventListener('click', () => {
    root.dataset.mode = b.dataset.set;
    root.querySelectorAll('.ft-01__seg').forEach((o) => o.setAttribute('aria-pressed', String(o === b)));
    report();
  }));
  root.querySelector('#ft-01-add').addEventListener('click', () => {
    const p = document.createElement('p');
    p.textContent = lines[i % lines.length]; i++;
    grow.appendChild(p);
    report();
  });
  root.querySelector('#ft-01-reset').addEventListener('click', () => { grow.replaceChildren(); i = 0; report(); });
  window.addEventListener('resize', report, { passive: true });
  report();
})();
```
