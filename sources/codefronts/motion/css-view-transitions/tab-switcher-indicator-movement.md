---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/tab-switcher-indicator-movement/"
title: "Tab Switcher Indicator Movement"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "The sliding underline that follows the active tab, built by giving the indicator element one view-transition-name and moving it in the DOM."
has_js: "true"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tab Switcher Indicator Movement
Source: https://codefronts.com/motion/css-view-transitions/tab-switcher-indicator-movement/

The sliding underline that follows the active tab, built by giving the indicator element one view-transition-name and moving it in the DOM. No getBoundingClientRect, no custom properties tracking offsets, no resize listener re-measuring on layout change. The contrast with the manual approach is the whole point.
## HTML
```html
<section class="vtr-09" aria-labelledby="vtr-09-heading">
  <fieldset class="vtr-09__theme">
    <legend class="vtr-09__themelegend">Theme</legend>
    <input class="vtr-09__themeinput" type="radio" name="vtr-09-theme" id="vtr-09-theme-auto" checked>
    <label class="vtr-09__themeopt" for="vtr-09-theme-auto">Auto</label>
    <input class="vtr-09__themeinput" type="radio" name="vtr-09-theme" id="vtr-09-theme-light">
    <label class="vtr-09__themeopt" for="vtr-09-theme-light">Light</label>
    <input class="vtr-09__themeinput" type="radio" name="vtr-09-theme" id="vtr-09-theme-dark">
    <label class="vtr-09__themeopt" for="vtr-09-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-09__stage">
    <header class="vtr-09__head">
      <p class="vtr-09__kicker">Ranger Console</p>
      <h2 class="vtr-09__heading" id="vtr-09-heading">Move the indicator, not a measurement</h2>
      <p class="vtr-09__sub">One name on one element. No rect reads, no offset variables, no resize listener.</p>
    </header>

    <div class="vtr-09__bar">
      <div class="vtr-09__tabs" role="tablist" aria-label="Fleet views" id="vtr-09-tabs">
        <button class="vtr-09__tab" type="button" role="tab" aria-selected="true" data-vtr09-tab="live">
          <span class="vtr-09__label">Live</span>
          <span class="vtr-09__rail" id="vtr-09-rail"></span>
        </button>
        <button class="vtr-09__tab" type="button" role="tab" aria-selected="false" data-vtr09-tab="queued">
          <span class="vtr-09__label">Queued</span>
        </button>
        <button class="vtr-09__tab" type="button" role="tab" aria-selected="false" data-vtr09-tab="archive">
          <span class="vtr-09__label">Archive</span>
        </button>
        <button class="vtr-09__tab" type="button" role="tab" aria-selected="false" data-vtr09-tab="alerts">
          <span class="vtr-09__label">Alerts</span>
        </button>
      </div>
    </div>

    <div class="vtr-09__pane" id="vtr-09-pane" role="tabpanel" aria-label="Fleet detail">
      <p class="vtr-09__pcount" id="vtr-09-count">18</p>
      <p class="vtr-09__pnote" id="vtr-09-note">units reporting in the last 60 seconds</p>
    </div>

    <div class="vtr-09__compare">
      <div class="vtr-09__col">
        <p class="vtr-09__ctitle">Manual</p>
        <p class="vtr-09__cbody">Read the rect, write two custom properties, re-measure on resize and font load.</p>
      </div>
      <div class="vtr-09__col vtr-09__col--win">
        <p class="vtr-09__ctitle">With the API</p>
        <p class="vtr-09__cbody">Give the rail a name. Move it in the DOM inside the callback. Nothing to measure.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.vtr-09 {
  --bg: #201c18;
  --surface: #2b251f;
  --line: #3d352c;
  --ink: #f6eee2;
  --muted: #b4a48f;
  --accent: #f59e0b;
  --accent-soft: #3a2b13;
  --font-display: "Roboto Condensed", "Arial Narrow", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  color-scheme: dark light;
}

.vtr-09 *,
.vtr-09 *::before,
.vtr-09 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-09 {
    --bg: oklch(22% 0.014 60);
    --surface: oklch(27% 0.016 60);
    --line: oklch(35% 0.02 60);
    --ink: oklch(95% 0.02 80);
    --muted: oklch(74% 0.03 75);
    --accent: oklch(76% 0.16 70);
    --accent-soft: oklch(31% 0.06 70);
  }
}

@media (prefers-color-scheme: light) {
  .vtr-09 {
    --bg: #f7f3ec;
    --surface: #ffffff;
    --line: #e0d7c8;
    --ink: #241d15;
    --muted: #6d6152;
    --accent: #b45309;
    --accent-soft: #fbeed7;
  }
}

.vtr-09[data-theme="light"] {
  --bg: #f7f3ec;
  --surface: #ffffff;
  --line: #e0d7c8;
  --ink: #241d15;
  --muted: #6d6152;
  --accent: #b45309;
  --accent-soft: #fbeed7;
}

.vtr-09[data-theme="dark"] {
  --bg: #201c18;
  --surface: #2b251f;
  --line: #3d352c;
  --ink: #f6eee2;
  --muted: #b4a48f;
  --accent: #f59e0b;
  --accent-soft: #3a2b13;
}

.vtr-09__stage {
  max-width: 54rem;
  margin: 0 auto;
  padding: clamp(1.25rem, 4vw, 2.5rem) clamp(0.85rem, 4vw, 2rem);
  display: grid;
  gap: 0.9rem;
}

.vtr-09__kicker {
  margin: 0 0 0.3rem;
  font-family: var(--font-display);
  font-size: 0.72rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-09__heading {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.35rem, 4.4vw, 2rem);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.01em;
}

.vtr-09__sub {
  margin: 0.3rem 0 0;
  font-size: 0.85rem;
  color: var(--muted);
  max-width: 32rem;
}

.vtr-09__bar {
  background: var(--surface);
  border: 1px solid var(--line);
  box-shadow: 4px 4px 0 0 var(--line);
  overflow-x: auto;
  min-inline-size: 0;
}

.vtr-09__tabs {
  display: flex;
}

.vtr-09__tab {
  position: relative;
  flex: 1 0 auto;
  min-inline-size: 0;
  min-height: 44px;
  padding: 0.6rem 0.9rem 0.7rem;
  border: 0;
  background: none;
  color: var(--muted);
  font-family: var(--font-display);
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  cursor: pointer;
}

.vtr-09__tab[aria-selected="true"] {
  color: var(--accent);
}

.vtr-09__tab:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.vtr-09__rail {
  position: absolute;
  left: 0.5rem;
  right: 0.5rem;
  bottom: 0.2rem;
  height: 3px;
  background: var(--accent);
  view-transition-name: vtr-09-rail;
}

.vtr-09__pane {
  padding: 1rem 1.1rem;
  background: var(--surface);
  border: 1px solid var(--line);
  display: grid;
  gap: 0.15rem;
}

.vtr-09__pcount {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(2rem, 8vw, 3rem);
  font-weight: 700;
  line-height: 1;
  font-variant-numeric: tabular-nums;
}

.vtr-09__pnote {
  margin: 0;
  font-size: 0.78rem;
  color: var(--muted);
}

.vtr-09__compare {
  display: grid;
  gap: 0.6rem;
  grid-template-columns: 1fr;
}

@media (min-width: 40rem) {
  .vtr-09__compare {
    grid-template-columns: 1fr 1fr;
  }
}

.vtr-09__col {
  padding: 0.7rem 0.8rem;
  border: 1px dashed var(--line);
  min-inline-size: 0;
}

.vtr-09__col--win {
  border-style: solid;
  border-color: var(--accent);
  background: var(--accent-soft);
}

.vtr-09__ctitle {
  margin: 0 0 0.25rem;
  font-family: var(--font-display);
  font-size: 0.72rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-09__cbody {
  margin: 0;
  font-size: 0.78rem;
  line-height: 1.5;
  color: var(--muted);
}

::view-transition-group(vtr-09-rail) {
  animation-duration: 300ms;
  animation-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(vtr-09-rail) {
    animation-duration: 1ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-09 {
  position: relative;
}

.vtr-09__theme {
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

.vtr-09__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-09__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-09__themeopt {
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

.vtr-09__themeopt:hover {
  opacity: 0.85;
}

.vtr-09__themeinput:checked + .vtr-09__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-09__themeinput:focus-visible + .vtr-09__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-09:has(#vtr-09-theme-light:checked) {
  --bg: #f7f3ec;
  --surface: #ffffff;
  --line: #e0d7c8;
  --ink: #241d15;
  --muted: #6d6152;
  --accent: #b45309;
  --accent-soft: #fbeed7;
}

.vtr-09:has(#vtr-09-theme-dark:checked) {
  --bg: #201c18;
  --surface: #2b251f;
  --line: #3d352c;
  --ink: #f6eee2;
  --muted: #b4a48f;
  --accent: #f59e0b;
  --accent-soft: #3a2b13;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.vtr-09');
  if (!root || root.dataset.vtr09) return;
  root.dataset.vtr09 = 'on';
  const tabs = [...root.querySelectorAll('[data-vtr09-tab]')];
  const rail = root.querySelector('#vtr-09-rail');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const copy = { live: ['18', 'units reporting in the last 60 seconds'], queued: ['7', 'jobs waiting on a free worker'], archive: ['412', 'runs retained for 90 days'], alerts: ['2', 'thresholds breached since midnight'] };
  let busy = false;
  const select = (tab) => {
    tabs.forEach(t => t.setAttribute('aria-selected', String(t === tab)));
    tab.append(rail);
    ['#vtr-09-count', '#vtr-09-note'].forEach((sel, k) => { root.querySelector(sel).textContent = copy[tab.dataset.vtr09Tab][k]; });
  };
  const go = async (tab) => {
    if (busy || tab.getAttribute('aria-selected') === 'true') return;
    if (!document.startViewTransition || reduce.matches) { select(tab); tab.focus(); return; }
    busy = true;
    try { await document.startViewTransition(() => select(tab)).finished; } finally { busy = false; tab.focus(); }
  };
  tabs.forEach((tab, i) => {
    tab.addEventListener('click', () => go(tab));
    tab.addEventListener('keydown', (e) => {
      const d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (!d) return;
      e.preventDefault();
      go(tabs[(i + d + tabs.length) % tabs.length]);
    });
  });
})();
```
