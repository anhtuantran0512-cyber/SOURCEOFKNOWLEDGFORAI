---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/off-canvas-sidebar-drawer/"
title: "Off Canvas Sidebar Drawer"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "A mobile navigation drawer where one transition handles the panel slide, the backdrop fade and the content shift together, instead of three separate CSS…"
has_js: "true"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Off Canvas Sidebar Drawer
Source: https://codefronts.com/motion/css-view-transitions/off-canvas-sidebar-drawer/

A mobile navigation drawer where one transition handles the panel slide, the backdrop fade and the content shift together, instead of three separate CSS transitions that can drift out of sync. Also covers the part the API does not do for you: moving focus into the drawer when it opens and returning it to the trigger on close.
## HTML
```html
<section class="vtr-13" aria-labelledby="vtr-13-heading">
  <fieldset class="vtr-13__theme">
    <legend class="vtr-13__themelegend">Theme</legend>
    <input class="vtr-13__themeinput" type="radio" name="vtr-13-theme" id="vtr-13-theme-auto" checked>
    <label class="vtr-13__themeopt" for="vtr-13-theme-auto">Auto</label>
    <input class="vtr-13__themeinput" type="radio" name="vtr-13-theme" id="vtr-13-theme-light">
    <label class="vtr-13__themeopt" for="vtr-13-theme-light">Light</label>
    <input class="vtr-13__themeinput" type="radio" name="vtr-13-theme" id="vtr-13-theme-dark">
    <label class="vtr-13__themeopt" for="vtr-13-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-13__stage">
    <div class="vtr-13__shell" id="vtr-13-shell" data-open="false">
      <header class="vtr-13__bar">
        <button class="vtr-13__burger" type="button" id="vtr-13-open" aria-expanded="false" aria-label="Open navigation">
          <svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path d="M3 5.5h14M3 10h14M3 14.5h14" stroke="currentColor" stroke-width="1.8"/></svg>
        </button>
        <p class="vtr-13__brand">Talon Fleet</p>
        <span class="vtr-13__pill">3 alerts</span>
      </header>

      <main class="vtr-13__content" id="vtr-13-content">
        <p class="vtr-13__kicker">Dispatch</p>
        <h2 class="vtr-13__heading" id="vtr-13-heading">One transition, three moving parts</h2>
        <p class="vtr-13__sub">The panel slides, the backdrop fades and the content shifts as a single composed change — not three CSS transitions hoping to stay in step.</p>
        <ul class="vtr-13__rows">
          <li><span>Route 14 · Vale depot</span><span class="vtr-13__ok">On time</span></li>
          <li><span>Route 22 · Basalt yard</span><span class="vtr-13__late">+18 min</span></li>
          <li><span>Route 31 · Orbit hub</span><span class="vtr-13__ok">On time</span></li>
        </ul>
      </main>

      <div class="vtr-13__scrim" id="vtr-13-scrim" hidden></div>
      <nav class="vtr-13__drawer" id="vtr-13-drawer" aria-label="Main navigation" hidden>
        <p class="vtr-13__dtitle">Navigation</p>
        <a class="vtr-13__link vtr-13__link--on" href="#vtr-13-heading" id="vtr-13-first">Dispatch</a>
        <a class="vtr-13__link" href="#vtr-13-heading">Vehicles</a>
        <a class="vtr-13__link" href="#vtr-13-heading">Drivers</a>
        <a class="vtr-13__link" href="#vtr-13-heading">Maintenance</a>
        <button class="vtr-13__close" type="button" id="vtr-13-close">Close</button>
      </nav>
    </div>
  </div>
</section>
```
## CSS
```css
.vtr-13 {
  --bg: #0f1319;
  --surface: #171c24;
  --surface-2: #1e242e;
  --line: #2b3340;
  --ink: #e9edf4;
  --muted: #93a0b4;
  --accent: #3b82f6;
  --accent-soft: #16243d;
  --drawer-w: 15rem;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  color-scheme: dark light;
}

.vtr-13 *,
.vtr-13 *::before,
.vtr-13 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-13 {
    --bg: oklch(19% 0.015 255);
    --surface: oklch(23% 0.017 255);
    --surface-2: oklch(27% 0.018 255);
    --line: oklch(34% 0.02 255);
    --ink: oklch(95% 0.01 255);
    --muted: oklch(72% 0.025 255);
    --accent: oklch(65% 0.17 255);
    --accent-soft: oklch(29% 0.07 255);
  }
}

@media (prefers-color-scheme: light) {
  .vtr-13 {
    --bg: #eef1f6;
    --surface: #ffffff;
    --surface-2: #f5f7fb;
    --line: #dbe1ea;
    --ink: #111722;
    --muted: #5a6577;
    --accent: #2563eb;
    --accent-soft: #e4edfd;
  }
}

.vtr-13[data-theme="light"] {
  --bg: #eef1f6;
  --surface: #ffffff;
  --surface-2: #f5f7fb;
  --line: #dbe1ea;
  --ink: #111722;
  --muted: #5a6577;
  --accent: #2563eb;
  --accent-soft: #e4edfd;
}

.vtr-13[data-theme="dark"] {
  --bg: #0f1319;
  --surface: #171c24;
  --surface-2: #1e242e;
  --line: #2b3340;
  --ink: #e9edf4;
  --muted: #93a0b4;
  --accent: #3b82f6;
  --accent-soft: #16243d;
}

.vtr-13__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1rem, 4vw, 2.5rem);
}

.vtr-13__shell {
  position: relative;
  overflow: hidden;
  width: 100%;
  max-width: 34rem;
  min-height: 26rem;
  border: 1px solid var(--line);
  border-radius: 0.9rem;
  background: var(--surface);
  min-inline-size: 0;
}

.vtr-13__bar {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.6rem 0.75rem;
  border-bottom: 1px solid var(--line);
  background: var(--surface-2);
}

.vtr-13__burger {
  display: grid;
  place-items: center;
  width: 44px;
  height: 44px;
  border: 1px solid var(--line);
  border-radius: 0.5rem;
  background: transparent;
  color: var(--ink);
  cursor: pointer;
}

.vtr-13__burger:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.vtr-13__brand {
  margin: 0;
  flex: 1;
  min-inline-size: 0;
  font-size: 0.9rem;
  font-weight: 600;
}

.vtr-13__pill {
  font-size: 0.7rem;
  padding: 0.25rem 0.5rem;
  border-radius: 999px;
  background: var(--accent-soft);
  color: var(--accent);
}

.vtr-13__content {
  padding: 1.1rem 1rem 1.35rem;
  display: grid;
  gap: 0.6rem;
}

.vtr-13__kicker {
  margin: 0;
  font-size: 0.68rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-13__heading {
  margin: 0;
  font-size: clamp(1.15rem, 3.8vw, 1.5rem);
  font-weight: 650;
  letter-spacing: -0.02em;
}

.vtr-13__sub {
  margin: 0;
  font-size: 0.84rem;
  line-height: 1.6;
  color: var(--muted);
}

.vtr-13__rows {
  margin: 0.3rem 0 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0.35rem;
}

.vtr-13__rows li {
  display: flex;
  justify-content: space-between;
  gap: 0.75rem;
  padding: 0.55rem 0.65rem;
  border-radius: 0.45rem;
  background: var(--surface-2);
  font-size: 0.8rem;
  min-inline-size: 0;
}

.vtr-13__ok {
  color: var(--accent);
}

.vtr-13__late {
  color: #f59e0b;
}

.vtr-13__scrim {
  position: absolute;
  inset: 0;
  background: rgba(6, 9, 14, 0.6);
  -webkit-backdrop-filter: blur(2px);
  backdrop-filter: blur(2px);
  view-transition-name: vtr-13-scrim;
}

.vtr-13__scrim[hidden] {
  display: none;
}

.vtr-13__drawer {
  position: absolute;
  inset: 0 auto 0 0;
  width: var(--drawer-w);
  padding: 0.85rem 0.8rem;
  display: grid;
  gap: 0.3rem;
  align-content: start;
  background: var(--surface-2);
  border-right: 1px solid var(--line);
  view-transition-name: vtr-13-drawer;
}

.vtr-13__drawer[hidden] {
  display: none;
}

.vtr-13__dtitle {
  margin: 0 0 0.4rem;
  font-size: 0.66rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--muted);
}

.vtr-13__link {
  display: flex;
  align-items: center;
  min-height: 44px;
  padding: 0 0.6rem;
  border-radius: 0.45rem;
  color: var(--ink);
  text-decoration: none;
  font-size: 0.85rem;
}

.vtr-13__link:hover {
  background: var(--surface);
}

.vtr-13__link--on {
  background: var(--accent-soft);
  color: var(--accent);
}

.vtr-13__link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.vtr-13__close {
  margin-top: 0.5rem;
  min-height: 44px;
  border: 1px solid var(--line);
  border-radius: 0.45rem;
  background: transparent;
  color: var(--muted);
  font-size: 0.8rem;
  cursor: pointer;
}

.vtr-13__close:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@keyframes vtr-13-in {
  from {
    transform: translateX(-100%);
  }
}

@keyframes vtr-13-out {
  to {
    transform: translateX(-100%);
  }
}

::view-transition-new(vtr-13-drawer) {
  animation: vtr-13-in 320ms cubic-bezier(0.32, 0.72, 0, 1) both;
}

::view-transition-old(vtr-13-drawer) {
  animation: vtr-13-out 260ms cubic-bezier(0.4, 0, 1, 1) both;
}

::view-transition-group(vtr-13-scrim) {
  animation-duration: 320ms;
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-new(vtr-13-drawer),
    ::view-transition-old(vtr-13-drawer),
    ::view-transition-group(vtr-13-scrim) {
    animation-duration: 1ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-13 {
  position: relative;
}

.vtr-13__theme {
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

.vtr-13__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-13__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-13__themeopt {
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

.vtr-13__themeopt:hover {
  opacity: 0.85;
}

.vtr-13__themeinput:checked + .vtr-13__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-13__themeinput:focus-visible + .vtr-13__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-13:has(#vtr-13-theme-light:checked) {
  --bg: #eef1f6;
  --surface: #ffffff;
  --surface-2: #f5f7fb;
  --line: #dbe1ea;
  --ink: #111722;
  --muted: #5a6577;
  --accent: #2563eb;
  --accent-soft: #e4edfd;
}

.vtr-13:has(#vtr-13-theme-dark:checked) {
  --bg: #0f1319;
  --surface: #171c24;
  --surface-2: #1e242e;
  --line: #2b3340;
  --ink: #e9edf4;
  --muted: #93a0b4;
  --accent: #3b82f6;
  --accent-soft: #16243d;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.vtr-13');
  if (!root || root.dataset.vtr13) return;
  root.dataset.vtr13 = 'on';
  const shell = root.querySelector('#vtr-13-shell');
  const drawer = root.querySelector('#vtr-13-drawer');
  const scrim = root.querySelector('#vtr-13-scrim');
  const content = root.querySelector('#vtr-13-content');
  const opener = root.querySelector('#vtr-13-open');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let busy = false;
  const set = (open) => {
    shell.dataset.open = String(open);
    drawer.hidden = !open; scrim.hidden = !open; content.inert = open;
    opener.setAttribute('aria-expanded', String(open));
  };
  const toggle = async (open) => {
    if (busy || drawer.hidden !== open) return;
    if (!document.startViewTransition || reduce.matches) set(open);
    else {
      busy = true;
      try { await document.startViewTransition(() => set(open)).finished; } finally { busy = false; }
    }
    (open ? root.querySelector('#vtr-13-first') : opener).focus();
  };
  opener.addEventListener('click', () => toggle(true));
  scrim.addEventListener('click', () => toggle(false));
  root.querySelector('#vtr-13-close').addEventListener('click', () => toggle(false));
  root.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !drawer.hidden) toggle(false); });
})();
```
