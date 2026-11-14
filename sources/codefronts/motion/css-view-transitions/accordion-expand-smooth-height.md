---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/accordion-expand-smooth-height/"
title: "Accordion Expand Smooth Height"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "Animating to intrinsic height without max-height guesswork or JavaScript measurement: name the panel, toggle it open inside the callback, and the browser…"
has_js: "true"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Accordion Expand Smooth Height
Source: https://codefronts.com/motion/css-view-transitions/accordion-expand-smooth-height/

Animating to intrinsic height without max-height guesswork or JavaScript measurement: name the panel, toggle it open inside the callback, and the browser interpolates the box. Also weighs the two honest alternatives — grid-template-rows: 0fr to 1fr and interpolate-size: allow-keywords — because the API is not always right for a disclosure.
## HTML
```html
<section class="vtr-12" aria-labelledby="vtr-12-heading">
  <fieldset class="vtr-12__theme">
    <legend class="vtr-12__themelegend">Theme</legend>
    <input class="vtr-12__themeinput" type="radio" name="vtr-12-theme" id="vtr-12-theme-auto" checked>
    <label class="vtr-12__themeopt" for="vtr-12-theme-auto">Auto</label>
    <input class="vtr-12__themeinput" type="radio" name="vtr-12-theme" id="vtr-12-theme-light">
    <label class="vtr-12__themeopt" for="vtr-12-theme-light">Light</label>
    <input class="vtr-12__themeinput" type="radio" name="vtr-12-theme" id="vtr-12-theme-dark">
    <label class="vtr-12__themeopt" for="vtr-12-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-12__stage">
    <header class="vtr-12__head">
      <p class="vtr-12__kicker">Sable Support</p>
      <h2 class="vtr-12__heading" id="vtr-12-heading">Height, without a measurement</h2>
      <p class="vtr-12__sub">The panel is named. The open state is toggled. Nothing reads scrollHeight.</p>
    </header>

    <div class="vtr-12__acc" id="vtr-12-acc">
      <div class="vtr-12__item" data-open="true">
        <button class="vtr-12__trigger" type="button" aria-expanded="true" data-vtr12-toggle>
          <span>How do I move a workspace to another region</span>
          <span class="vtr-12__chev" aria-hidden="true"></span>
        </button>
        <div class="vtr-12__panel">
          <p>Open the workspace settings, choose the destination region and confirm. Sable copies object storage first, then cuts over the database in a single write-locked window of about ninety seconds.</p>
          <p>Existing API keys keep working. Region-pinned endpoints do not, so update any hardcoded hostnames before the cutover.</p>
        </div>
      </div>
      <div class="vtr-12__item">
        <button class="vtr-12__trigger" type="button" aria-expanded="false" data-vtr12-toggle>
          <span>What happens to scheduled jobs during a plan change</span>
          <span class="vtr-12__chev" aria-hidden="true"></span>
        </button>
        <div class="vtr-12__panel">
          <p>Jobs already running finish on the old plan's limits. Anything queued starts under the new limits, which can mean a shorter timeout — check the concurrency ceiling before downgrading.</p>
        </div>
      </div>
      <div class="vtr-12__item">
        <button class="vtr-12__trigger" type="button" aria-expanded="false" data-vtr12-toggle>
          <span>Can I export audit logs on the Team plan</span>
          <span class="vtr-12__chev" aria-hidden="true"></span>
        </button>
        <div class="vtr-12__panel">
          <p>Yes, as newline-delimited JSON for the last ninety days. Longer retention and streaming export to a bucket are Scale features.</p>
        </div>
      </div>
    </div>

    <div class="vtr-12__alts">
      <p class="vtr-12__altstitle">When not to use this</p>
      <ul class="vtr-12__altlist">
        <li><code>grid-template-rows: 0fr to 1fr</code><span>Pure CSS, no API, works everywhere. Better for a lone disclosure.</span></li>
        <li><code>interpolate-size: allow-keywords</code><span>Cleanest syntax, transitions height: auto directly. Chrome only today.</span></li>
        <li><code>view-transition-name</code><span>Worth it when the open state also moves siblings, badges or icons.</span></li>
      </ul>
    </div>
  </div>
</section>
```
## CSS
```css
.vtr-12 {
  --bg: #f5f1eb;
  --surface: #fbf8f4;
  --line: #ddd2c4;
  --ink: #2b2118;
  --muted: #6f6053;
  --accent: #8a6a4b;
  --accent-soft: #ece1d4;
  --font-display: "Bookman Old Style", Rockwell, Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  color-scheme: light dark;
}

.vtr-12 *,
.vtr-12 *::before,
.vtr-12 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-12 {
    --bg: oklch(95.5% 0.014 75);
    --surface: oklch(97.5% 0.01 75);
    --line: oklch(86% 0.024 72);
    --ink: oklch(25% 0.025 60);
    --muted: oklch(50% 0.028 62);
    --accent: oklch(55% 0.06 62);
    --accent-soft: oklch(90% 0.024 70);
  }
}

@media (prefers-color-scheme: dark) {
  .vtr-12 {
    --bg: #161210;
    --surface: #1e1815;
    --line: #322821;
    --ink: #f2e8de;
    --muted: #a89684;
    --accent: #c9a37a;
    --accent-soft: #2a211a;
  }
}

.vtr-12[data-theme="light"] {
  --bg: #f5f1eb;
  --surface: #fbf8f4;
  --line: #ddd2c4;
  --ink: #2b2118;
  --muted: #6f6053;
  --accent: #8a6a4b;
  --accent-soft: #ece1d4;
}

.vtr-12[data-theme="dark"] {
  --bg: #161210;
  --surface: #1e1815;
  --line: #322821;
  --ink: #f2e8de;
  --muted: #a89684;
  --accent: #c9a37a;
  --accent-soft: #2a211a;
}

.vtr-12__stage {
  max-width: 48rem;
  margin: 0 auto;
  padding: clamp(1.25rem, 4vw, 2.75rem) clamp(0.9rem, 4vw, 2rem);
  display: grid;
  gap: 1.1rem;
}

.vtr-12__kicker {
  margin: 0 0 0.3rem;
  font-size: 0.68rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-12__heading {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.3rem, 4.2vw, 1.8rem);
  font-weight: 700;
  letter-spacing: -0.01em;
}

.vtr-12__sub {
  margin: 0.3rem 0 0;
  font-size: 0.86rem;
  color: var(--muted);
}

.vtr-12__acc {
  border-top: 1px solid var(--line);
}

.vtr-12__item {
  border-bottom: 1px solid var(--line);
}

.vtr-12__trigger {
  width: 100%;
  min-height: 44px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  padding: 0.7rem 0.15rem;
  border: 0;
  background: none;
  color: var(--ink);
  font-family: var(--font-display);
  font-size: 0.92rem;
  font-weight: 700;
  text-align: left;
  cursor: pointer;
}

.vtr-12__trigger:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.vtr-12__trigger[aria-expanded="true"] {
  color: var(--accent);
}

.vtr-12__chev {
  flex: none;
  width: 0.6rem;
  height: 0.6rem;
  border-right: 2px solid currentColor;
  border-bottom: 2px solid currentColor;
  transform: rotate(45deg);
}

.vtr-12__trigger[aria-expanded="true"] .vtr-12__chev {
  transform: rotate(-135deg);
}

.vtr-12__panel {
  height: 0;
  overflow: hidden;
}

.vtr-12__item[data-open="true"] .vtr-12__panel {
  height: auto;
  padding-bottom: 0.8rem;
  view-transition-name: vtr-12-panel;
}

.vtr-12__panel p {
  margin: 0 0 0.6rem;
  padding-right: 1rem;
  font-size: 0.85rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 38rem;
}

.vtr-12__panel p:last-child {
  margin-bottom: 0;
}

.vtr-12__alts {
  padding: 0.85rem 0.9rem;
  background: var(--surface);
  border: 1px solid var(--line);
}

.vtr-12__altstitle {
  margin: 0 0 0.5rem;
  font-size: 0.68rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-12__altlist {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0.5rem;
}

.vtr-12__altlist li {
  display: grid;
  gap: 0.1rem;
  min-inline-size: 0;
}

.vtr-12__altlist code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.72rem;
  word-break: break-word;
}

.vtr-12__altlist span {
  font-size: 0.76rem;
  color: var(--muted);
}

::view-transition-group(vtr-12-panel) {
  animation-duration: 380ms;
  animation-timing-function: cubic-bezier(0.32, 0.72, 0, 1);
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(vtr-12-panel) {
    animation-duration: 1ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-12 {
  position: relative;
}

.vtr-12__theme {
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

.vtr-12__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-12__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-12__themeopt {
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

.vtr-12__themeopt:hover {
  opacity: 0.85;
}

.vtr-12__themeinput:checked + .vtr-12__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-12__themeinput:focus-visible + .vtr-12__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-12:has(#vtr-12-theme-light:checked) {
  --bg: #f5f1eb;
  --surface: #fbf8f4;
  --line: #ddd2c4;
  --ink: #2b2118;
  --muted: #6f6053;
  --accent: #8a6a4b;
  --accent-soft: #ece1d4;
}

.vtr-12:has(#vtr-12-theme-dark:checked) {
  --bg: #161210;
  --surface: #1e1815;
  --line: #322821;
  --ink: #f2e8de;
  --muted: #a89684;
  --accent: #c9a37a;
  --accent-soft: #2a211a;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.vtr-12');
  if (!root || root.dataset.vtr12) return;
  root.dataset.vtr12 = 'on';
  const items = [...root.querySelectorAll('.vtr-12__item')];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let busy = false;
  const set = (item) => {
    const opening = item.dataset.open !== 'true';
    items.forEach(i => {
      const on = i === item && opening;
      i.dataset.open = String(on);
      i.querySelector('.vtr-12__trigger').setAttribute('aria-expanded', String(on));
    });
  };
  items.forEach(item => item.querySelector('[data-vtr12-toggle]').addEventListener('click', async () => {
    if (busy) return;
    if (!document.startViewTransition || reduce.matches) { set(item); return; }
    busy = true;
    try { await document.startViewTransition(() => set(item)).finished; } finally { busy = false; }
  }));
})();
```
