---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/list-reorder-and-filtering/"
title: "List Reorder and Filtering"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "Filter or sort a list and every remaining row glides to its new position."
has_js: "true"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: List Reorder and Filtering
Source: https://codefronts.com/motion/css-view-transitions/list-reorder-and-filtering/

Filter or sort a list and every remaining row glides to its new position. This is the native replacement for FLIP libraries and layout animations from a motion framework — no measuring, no getBoundingClientRect, no wrapper components. Each row needs its own unique name, and there is a practical ceiling worth knowing before you scale it.
## HTML
```html
<section class="vtr-08" aria-labelledby="vtr-08-heading">
  <fieldset class="vtr-08__theme">
    <legend class="vtr-08__themelegend">Theme</legend>
    <input class="vtr-08__themeinput" type="radio" name="vtr-08-theme" id="vtr-08-theme-auto" checked>
    <label class="vtr-08__themeopt" for="vtr-08-theme-auto">Auto</label>
    <input class="vtr-08__themeinput" type="radio" name="vtr-08-theme" id="vtr-08-theme-light">
    <label class="vtr-08__themeopt" for="vtr-08-theme-light">Light</label>
    <input class="vtr-08__themeinput" type="radio" name="vtr-08-theme" id="vtr-08-theme-dark">
    <label class="vtr-08__themeopt" for="vtr-08-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-08__stage">
    <header class="vtr-08__head">
      <p class="vtr-08__kicker">Meridian · Ledger</p>
      <h2 class="vtr-08__heading" id="vtr-08-heading">Filtering, without a layout library</h2>
      <p class="vtr-08__sub">Each row carries its own name. The browser measures and moves them for you.</p>
    </header>

    <div class="vtr-08__chips" role="group" aria-label="Filter transactions">
      <button class="vtr-08__chip" type="button" data-vtr08-filter="all" aria-pressed="true">All</button>
      <button class="vtr-08__chip" type="button" data-vtr08-filter="cloud" aria-pressed="false">Cloud</button>
      <button class="vtr-08__chip" type="button" data-vtr08-filter="travel" aria-pressed="false">Travel</button>
      <button class="vtr-08__chip" type="button" data-vtr08-filter="tools" aria-pressed="false">Tools</button>
    </div>

    <ul class="vtr-08__list" id="vtr-08-list"></ul>
    <p class="vtr-08__status" id="vtr-08-status" role="status" aria-live="polite">6 transactions</p>
  </div>
</section>
```
## CSS
```css
.vtr-08 {
  --bg: #f2f7f5;
  --surface: #ffffff;
  --surface-2: #e9f2ef;
  --line: #d3e3dd;
  --ink: #16211d;
  --muted: #55665f;
  --accent: #0f9b8e;
  --accent-soft: #dcf5f1;
  --font-display: "Avenir Next", "Segoe UI", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  color-scheme: light dark;
}

.vtr-08 *,
.vtr-08 *::before,
.vtr-08 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-08 {
    --bg: oklch(96.5% 0.014 175);
    --surface-2: oklch(93.5% 0.02 175);
    --line: oklch(89% 0.025 175);
    --ink: oklch(22% 0.02 175);
    --muted: oklch(48% 0.02 175);
    --accent: oklch(60% 0.11 180);
    --accent-soft: oklch(94% 0.035 180);
  }
}

@media (prefers-color-scheme: dark) {
  .vtr-08 {
    --bg: #0c1412;
    --surface: #14201d;
    --surface-2: #182723;
    --line: #23352f;
    --ink: #e7f2ee;
    --muted: #93a8a1;
    --accent: #4dd8c6;
    --accent-soft: #12312c;
  }
}

.vtr-08[data-theme="light"] {
  --bg: #f2f7f5;
  --surface: #ffffff;
  --surface-2: #e9f2ef;
  --line: #d3e3dd;
  --ink: #16211d;
  --muted: #55665f;
  --accent: #0f9b8e;
  --accent-soft: #dcf5f1;
}

.vtr-08[data-theme="dark"] {
  --bg: #0c1412;
  --surface: #14201d;
  --surface-2: #182723;
  --line: #23352f;
  --ink: #e7f2ee;
  --muted: #93a8a1;
  --accent: #4dd8c6;
  --accent-soft: #12312c;
}

.vtr-08__stage {
  max-width: 52rem;
  margin: 0 auto;
  padding: clamp(1.5rem, 4vw, 3rem) clamp(1rem, 4vw, 2rem);
  display: grid;
  gap: 1.1rem;
}

.vtr-08__kicker {
  margin: 0 0 0.4rem;
  font-size: 0.7rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-08__heading {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.35rem, 4.2vw, 1.9rem);
  font-weight: 600;
  letter-spacing: -0.015em;
}

.vtr-08__sub {
  margin: 0.4rem 0 0;
  font-size: 0.9rem;
  color: var(--muted);
  max-width: 32rem;
}

.vtr-08__chips {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.vtr-08__chip {
  min-height: 44px;
  padding: 0 1rem;
  border: 0;
  border-radius: 999px;
  background: var(--surface-2);
  color: var(--muted);
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
}

.vtr-08__chip[aria-pressed="true"] {
  background: var(--accent);
  color: #ffffff;
}

.vtr-08__chip:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.vtr-08__list {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0.4rem;
}

.vtr-08__row {
  display: grid;
  grid-template-columns: 2.25rem 1fr auto;
  gap: 0.75rem;
  align-items: center;
  padding: 0.7rem 0.85rem;
  border-radius: 0.6rem;
  background: var(--surface);
  min-inline-size: 0;
}

.vtr-08__mark {
  display: grid;
  place-items: center;
  width: 2.25rem;
  height: 2.25rem;
  border-radius: 0.5rem;
  background: var(--surface-2);
  color: var(--accent);
  font-family: var(--font-display);
  font-size: 0.72rem;
  font-weight: 700;
}

.vtr-08__rowtext {
  display: grid;
  gap: 0.1rem;
  min-inline-size: 0;
}

.vtr-08__rowtext strong {
  font-size: 0.86rem;
  font-weight: 600;
}

.vtr-08__rowtext span {
  font-size: 0.72rem;
  color: var(--muted);
}

.vtr-08__amt {
  font-family: var(--font-display);
  font-size: 0.86rem;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

.vtr-08__status {
  margin: 0;
  padding-top: 0.5rem;
  border-top: 1px solid var(--line);
  font-size: 0.76rem;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .vtr-08 {
    --dur: 1ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-08 {
  position: relative;
}

.vtr-08__theme {
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

.vtr-08__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-08__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-08__themeopt {
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

.vtr-08__themeopt:hover {
  opacity: 0.85;
}

.vtr-08__themeinput:checked + .vtr-08__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-08__themeinput:focus-visible + .vtr-08__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-08:has(#vtr-08-theme-light:checked) {
  --bg: #f2f7f5;
  --surface: #ffffff;
  --surface-2: #e9f2ef;
  --line: #d3e3dd;
  --ink: #16211d;
  --muted: #55665f;
  --accent: #0f9b8e;
  --accent-soft: #dcf5f1;
}

.vtr-08:has(#vtr-08-theme-dark:checked) {
  --bg: #0c1412;
  --surface: #14201d;
  --surface-2: #182723;
  --line: #23352f;
  --ink: #e7f2ee;
  --muted: #93a8a1;
  --accent: #4dd8c6;
  --accent-soft: #12312c;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.vtr-08');
  if (!root || root.dataset.vtr08) return;
  root.dataset.vtr08 = 'on';
  const list = root.querySelector('#vtr-08-list');
  const status = root.querySelector('#vtr-08-status');
  const chips = [...root.querySelectorAll('[data-vtr08-filter]')];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const data = [
    ['a1', 'Orbit Cloud', 'Compute · eu-west-1', '1,248.00', 'cloud', 'OC'], ['a2', 'Vale Rail', 'Zurich to Milan · Jordan Lee', '184.40', 'travel', 'VR'],
    ['a3', 'Basalt Storage', 'Object store · 4.1 TB', '612.90', 'cloud', 'BS'], ['a4', 'Quill Design', 'Team seats · 12', '348.00', 'tools', 'QD'],
    ['a5', 'Talon Air', 'LHR to BER · Sam Rivera', '410.75', 'travel', 'TA'], ['a6', 'Nova Analytics', 'Annual plan', '2,100.00', 'tools', 'NA']
  ];
  let filter = 'all', busy = false;
  const render = () => {
    const rows = data.filter(r => filter === 'all' || r[4] === filter);
    list.innerHTML = rows.map(r => '<li class="vtr-08__row" style="view-transition-name:vtr-08-row-' + r[0] + '"><span class="vtr-08__mark">' + r[5] + '</span><span class="vtr-08__rowtext"><strong>' + r[1] + '</strong><span>' + r[2] + '</span></span><span class="vtr-08__amt">' + r[3] + '</span></li>').join('');
    status.textContent = rows.length + (rows.length === 1 ? ' transaction' : ' transactions');
  };
  render();
  chips.forEach(chip => chip.addEventListener('click', async () => {
    if (busy || chip.dataset.vtr08Filter === filter) return;
    filter = chip.dataset.vtr08Filter;
    chips.forEach(c => c.setAttribute('aria-pressed', String(c === chip)));
    if (!document.startViewTransition || reduce.matches) { render(); return; }
    busy = true;
    try { await document.startViewTransition(render).finished; } finally { busy = false; }
  }));
})();
```
