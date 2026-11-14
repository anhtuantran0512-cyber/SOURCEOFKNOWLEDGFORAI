---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/card-to-full-page-detail-morph/"
title: "Card to Full Page Detail Morph"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "A grid card expands into a full detail view with its image and headline flying to their new positions."
has_js: "true"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Card to Full Page Detail Morph
Source: https://codefronts.com/motion/css-view-transitions/card-to-full-page-detail-morph/

A grid card expands into a full detail view with its image and headline flying to their new positions. The subject is the pairing contract that makes it work: the same view-transition-name must exist on the outgoing element and the incoming one, and only one element per name may be present when the browser takes each snapshot.
## HTML
```html
<section class="vtr-06" aria-labelledby="vtr-06-heading">
  <fieldset class="vtr-06__theme">
    <legend class="vtr-06__themelegend">Theme</legend>
    <input class="vtr-06__themeinput" type="radio" name="vtr-06-theme" id="vtr-06-theme-auto" checked>
    <label class="vtr-06__themeopt" for="vtr-06-theme-auto">Auto</label>
    <input class="vtr-06__themeinput" type="radio" name="vtr-06-theme" id="vtr-06-theme-light">
    <label class="vtr-06__themeopt" for="vtr-06-theme-light">Light</label>
    <input class="vtr-06__themeinput" type="radio" name="vtr-06-theme" id="vtr-06-theme-dark">
    <label class="vtr-06__themeopt" for="vtr-06-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-06__stage">
    <header class="vtr-06__head">
      <p class="vtr-06__kicker">Fern Field Notes</p>
      <h2 class="vtr-06__heading" id="vtr-06-heading">Shared names, not shared nodes</h2>
      <p class="vtr-06__sub">Open a note. The card, its plate and its headline each carry a name, so each travels on its own.</p>
    </header>

    <div class="vtr-06__grid" id="vtr-06-grid">
      <article class="vtr-06__card" data-vtr06-id="soil">
        <div class="vtr-06__plate vtr-06__plate--soil"></div>
        <p class="vtr-06__badge">Soil</p>
        <h3 class="vtr-06__ctitle">What the second season taught us about mulch depth</h3>
        <p class="vtr-06__excerpt">Four beds, one variable, and a result that contradicted the first year.</p>
        <button class="vtr-06__open" type="button" data-vtr06-open="soil">Read note</button>
      </article>
      <article class="vtr-06__card" data-vtr06-id="water">
        <div class="vtr-06__plate vtr-06__plate--water"></div>
        <p class="vtr-06__badge">Water</p>
        <h3 class="vtr-06__ctitle">Drip lines are cheaper than the third rebuild</h3>
        <p class="vtr-06__excerpt">A costing note from the north slope, written after the second failure.</p>
        <button class="vtr-06__open" type="button" data-vtr06-open="water">Read note</button>
      </article>
      <article class="vtr-06__card" data-vtr06-id="canopy">
        <div class="vtr-06__plate vtr-06__plate--canopy"></div>
        <p class="vtr-06__badge">Canopy</p>
        <h3 class="vtr-06__ctitle">Thinning the alder row changed the whole understory</h3>
        <p class="vtr-06__excerpt">Light reaching the floor doubled. So did everything competing for it.</p>
        <button class="vtr-06__open" type="button" data-vtr06-open="canopy">Read note</button>
      </article>
    </div>

    <article class="vtr-06__detail" id="vtr-06-detail" hidden>
      <div class="vtr-06__plate vtr-06__plate--full" id="vtr-06-detail-plate"></div>
      <div class="vtr-06__dbody">
        <p class="vtr-06__badge" id="vtr-06-detail-badge">Soil</p>
        <h3 class="vtr-06__dtitle" id="vtr-06-detail-title" tabindex="-1">What the second season taught us about mulch depth</h3>
        <p class="vtr-06__dcopy" id="vtr-06-detail-copy">Four beds, one variable, and a result that contradicted the first year.</p>
        <p class="vtr-06__dmeta">Alex Chen · 6 min read</p>
        <button class="vtr-06__back" type="button" id="vtr-06-back">Back to notes</button>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
.vtr-06 {
  --bg: #f4f6f0;
  --surface: #ffffff;
  --line: #dbe2d3;
  --ink: #1a221a;
  --muted: #5a6657;
  --accent: #3f6b45;
  --accent-soft: #e6eee3;
  --font-display: "Iowan Old Style", Georgia, "Times New Roman", serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  color-scheme: light dark;
}

.vtr-06 *,
.vtr-06 *::before,
.vtr-06 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-06 {
    --bg: oklch(96.5% 0.012 130);
    --line: oklch(89% 0.022 130);
    --ink: oklch(22% 0.02 140);
    --muted: oklch(50% 0.022 140);
    --accent: oklch(48% 0.08 150);
    --accent-soft: oklch(94% 0.022 140);
  }
}

@media (prefers-color-scheme: dark) {
  .vtr-06 {
    --bg: #121611;
    --surface: #1a201a;
    --line: #2b332a;
    --ink: #eef2e9;
    --muted: #9fac9b;
    --accent: #8fc79a;
    --accent-soft: #1f2a20;
  }
}

.vtr-06[data-theme="light"] {
  --bg: #f4f6f0;
  --surface: #ffffff;
  --line: #dbe2d3;
  --ink: #1a221a;
  --muted: #5a6657;
  --accent: #3f6b45;
  --accent-soft: #e6eee3;
}

.vtr-06[data-theme="dark"] {
  --bg: #121611;
  --surface: #1a201a;
  --line: #2b332a;
  --ink: #eef2e9;
  --muted: #9fac9b;
  --accent: #8fc79a;
  --accent-soft: #1f2a20;
}

.vtr-06__stage {
  max-width: 68rem;
  margin: 0 auto;
  padding: clamp(1.75rem, 5vw, 4rem) clamp(1rem, 4vw, 2.5rem);
  display: grid;
  gap: 2.25rem;
}

.vtr-06__kicker {
  margin: 0 0 0.6rem;
  font-size: 0.7rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-06__heading {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.7rem, 5vw, 2.6rem);
  font-weight: 400;
  letter-spacing: -0.02em;
}

.vtr-06__sub {
  margin: 0.6rem 0 0;
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 36rem;
}

.vtr-06__grid {
  display: grid;
  gap: 1.75rem;
  grid-template-columns: 1fr;
}

@media (min-width: 46rem) {
  .vtr-06__grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

.vtr-06__grid[hidden] {
  display: none;
}

.vtr-06__card {
  display: grid;
  gap: 0.65rem;
  align-content: start;
  min-inline-size: 0;
}

.vtr-06__plate {
  border-radius: 0.25rem;
  height: 8.5rem;
}

.vtr-06__plate--soil {
  background: linear-gradient(150deg, #4b3b2a, #8a6b45 55%, #cbb08a);
}

.vtr-06__plate--water {
  background: linear-gradient(150deg, #1d3c4a, #2f7f96 55%, #a8dbe6);
}

.vtr-06__plate--canopy {
  background: linear-gradient(150deg, #23401f, #4e8c3f 55%, #b8dda0);
}

.vtr-06__plate--full {
  height: clamp(9rem, 26vw, 15rem);
}

.vtr-06__badge {
  margin: 0;
  font-size: 0.66rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-06__ctitle {
  margin: 0;
  font-family: var(--font-display);
  font-size: 1.1rem;
  font-weight: 400;
  line-height: 1.25;
  text-wrap: pretty;
}

.vtr-06__excerpt {
  margin: 0;
  font-size: 0.85rem;
  line-height: 1.55;
  color: var(--muted);
}

.vtr-06__open,
.vtr-06__back {
  justify-self: start;
  min-height: 44px;
  padding: 0 1rem;
  border: 1px solid var(--accent);
  border-radius: 999px;
  background: transparent;
  color: var(--accent);
  font-size: 0.8rem;
  cursor: pointer;
}

.vtr-06__open:hover,
.vtr-06__back:hover {
  background: var(--accent-soft);
}

.vtr-06__open:focus-visible,
.vtr-06__back:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.vtr-06__detail {
  display: grid;
  gap: 1.25rem;
  min-inline-size: 0;
}

.vtr-06__detail[hidden] {
  display: none;
}

.vtr-06__dbody {
  display: grid;
  gap: 0.8rem;
  max-width: 40rem;
}

.vtr-06__dtitle {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 4.6vw, 2.1rem);
  font-weight: 400;
  line-height: 1.15;
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.vtr-06__dtitle:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 4px;
}

.vtr-06__dcopy {
  margin: 0;
  font-size: 1rem;
  line-height: 1.7;
  color: var(--muted);
}

.vtr-06__dmeta {
  margin: 0;
  font-size: 0.78rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
}

::view-transition-group(vtr-06-card),
::view-transition-group(vtr-06-plate),
::view-transition-group(vtr-06-title) {
  animation-duration: 460ms;
  animation-timing-function: cubic-bezier(0.32, 0.72, 0, 1);
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(vtr-06-card),
    ::view-transition-group(vtr-06-plate),
    ::view-transition-group(vtr-06-title) {
    animation-duration: 1ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-06 {
  position: relative;
}

.vtr-06__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 9;
  display: flex;
  align-items: center;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 8%, transparent);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  font-family: system-ui, sans-serif;
}

.vtr-06__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-06__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-06__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.6875rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: inherit;
  opacity: 0.55;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}

.vtr-06__themeopt:hover {
  opacity: 0.85;
}

.vtr-06__themeinput:checked + .vtr-06__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-06__themeinput:focus-visible + .vtr-06__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-06:has(#vtr-06-theme-light:checked) {
  --bg: #f4f6f0;
  --surface: #ffffff;
  --line: #dbe2d3;
  --ink: #1a221a;
  --muted: #5a6657;
  --accent: #3f6b45;
  --accent-soft: #e6eee3;
}

.vtr-06:has(#vtr-06-theme-dark:checked) {
  --bg: #121611;
  --surface: #1a201a;
  --line: #2b332a;
  --ink: #eef2e9;
  --muted: #9fac9b;
  --accent: #8fc79a;
  --accent-soft: #1f2a20;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.vtr-06');
  if (!root || root.dataset.vtr06) return;
  root.dataset.vtr06 = 'on';
  const grid = root.querySelector('#vtr-06-grid'), detail = root.querySelector('#vtr-06-detail'), reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const keys = ['card', 'plate', 'title'];
  const nodes = (card) => [card, card.querySelector('.vtr-06__plate'), card.querySelector('.vtr-06__ctitle'),
    detail, root.querySelector('#vtr-06-detail-plate'), root.querySelector('#vtr-06-detail-title')];
  const mark = (card, on) => nodes(card).forEach((el, k) => { el.style.viewTransitionName = on ? 'vtr-06-' + keys[k % 3] : ''; });
  const run = async (mutate, card) => {
    if (!document.startViewTransition || reduce.matches) { mutate(); return; }
    mark(card, true);
    try { await document.startViewTransition(mutate).finished; } finally { mark(card, false); }
  };
  const fields = [['#vtr-06-detail-badge', '.vtr-06__badge'], ['#vtr-06-detail-title', '.vtr-06__ctitle'], ['#vtr-06-detail-copy', '.vtr-06__excerpt']];
  let opener = null;
  root.addEventListener('click', async (e) => {
    const open = e.target.closest('[data-vtr06-open]');
    if (!open && !e.target.closest('#vtr-06-back')) return;
    if (open) opener = open;
    const card = root.querySelector('[data-vtr06-id="' + opener.dataset.vtr06Open + '"]');
    await run(() => {
      if (!open) { detail.hidden = true; grid.hidden = false; return; }
      root.querySelector('#vtr-06-detail-plate').className = card.querySelector('.vtr-06__plate').className + ' vtr-06__plate--full';
      fields.forEach(([a, b]) => { root.querySelector(a).textContent = card.querySelector(b).textContent; });
      grid.hidden = true; detail.hidden = false;
    }, card);
    (open ? root.querySelector('#vtr-06-detail-title') : opener).focus();
  });
})();
```
