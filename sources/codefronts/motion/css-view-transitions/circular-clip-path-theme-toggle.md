---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/circular-clip-path-theme-toggle/"
title: "Circular Clip Path Theme Toggle"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "The dark-mode reveal that spreads from the toggle button as a growing circle."
has_js: "true"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Circular Clip Path Theme Toggle
Source: https://codefronts.com/motion/css-view-transitions/circular-clip-path-theme-toggle/

The dark-mode reveal that spreads from the toggle button as a growing circle. Read the click coordinates, compute the radius to the furthest viewport corner, and animate clip-path: circle() on the new snapshot. Two details make it correct: the new state has to paint above the old one, and the whole effect must be skipped under reduced motion.
## HTML
```html
<section class="vtr-10" aria-labelledby="vtr-10-heading">
  <fieldset class="vtr-10__theme">
    <legend class="vtr-10__themelegend">Theme</legend>
    <input class="vtr-10__themeinput" type="radio" name="vtr-10-theme" id="vtr-10-theme-auto" checked>
    <label class="vtr-10__themeopt" for="vtr-10-theme-auto">Auto</label>
    <input class="vtr-10__themeinput" type="radio" name="vtr-10-theme" id="vtr-10-theme-light">
    <label class="vtr-10__themeopt" for="vtr-10-theme-light">Light</label>
    <input class="vtr-10__themeinput" type="radio" name="vtr-10-theme" id="vtr-10-theme-dark">
    <label class="vtr-10__themeopt" for="vtr-10-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-10__stage" id="vtr-10-stage">
    <div class="vtr-10__panel">
      <header class="vtr-10__head">
        <p class="vtr-10__kicker">Aperture Settings</p>
        <h2 class="vtr-10__heading" id="vtr-10-heading">Reveal from the pointer</h2>
        <p class="vtr-10__sub">The incoming theme is clipped from a circle at the click, sized to the furthest corner.</p>
      </header>

      <div class="vtr-10__row">
        <div class="vtr-10__rowtext">
          <p class="vtr-10__rowtitle">Appearance</p>
          <p class="vtr-10__rownote" id="vtr-10-state">Light</p>
        </div>
        <button class="vtr-10__toggle" type="button" id="vtr-10-toggle" aria-pressed="false">
          <span class="vtr-10__ico" aria-hidden="true">
            <svg viewBox="0 0 20 20" width="16" height="16"><circle cx="10" cy="10" r="4" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M10 1.8v2M10 16.2v2M1.8 10h2M16.2 10h2M4.3 4.3l1.4 1.4M14.3 14.3l1.4 1.4M15.7 4.3l-1.4 1.4M5.7 14.3l-1.4 1.4" stroke="currentColor" stroke-width="1.4"/></svg>
          </span>
          <span>Switch theme</span>
        </button>
      </div>

      <dl class="vtr-10__facts">
        <div><dt>Origin</dt><dd id="vtr-10-origin">click x, y</dd></div>
        <div><dt>Radius</dt><dd>hypot to furthest corner</dd></div>
        <div><dt>Reduced motion</dt><dd>flip instantly, no reveal</dd></div>
      </dl>
    </div>
  </div>
</section>
```
## CSS
```css
.vtr-10 {
  --bg1: #eef1f8;
  --bg2: #dfe4f2;
  --panel: rgba(255, 255, 255, 0.72);
  --line: rgba(23, 30, 56, 0.12);
  --ink: #141a2e;
  --muted: #59617e;
  --accent: #4f46e5;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: linear-gradient(140deg, var(--bg1), var(--bg2));
  color: var(--ink);
  font-family: system-ui, "Segoe UI", sans-serif;
  color-scheme: light dark;
}

.vtr-10 *,
.vtr-10 *::before,
.vtr-10 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-10 {
    --bg1: oklch(95.5% 0.015 270);
    --bg2: oklch(91% 0.03 270);
    --ink: oklch(21% 0.03 270);
    --muted: oklch(52% 0.035 270);
    --accent: oklch(55% 0.2 280);
  }
}

@media (prefers-color-scheme: dark) {
  .vtr-10 {
    --bg1: #0b0f1d;
    --bg2: #151c33;
    --panel: rgba(20, 26, 46, 0.72);
    --line: rgba(210, 220, 255, 0.14);
    --ink: #eaeefb;
    --muted: #97a2c6;
    --accent: #a5b4fc;
  }
}

.vtr-10[data-theme="light"] {
  --bg1: #eef1f8;
  --bg2: #dfe4f2;
  --panel: rgba(255, 255, 255, 0.72);
  --line: rgba(23, 30, 56, 0.12);
  --ink: #141a2e;
  --muted: #59617e;
  --accent: #4f46e5;
}

.vtr-10[data-theme="dark"] {
  --bg1: #0b0f1d;
  --bg2: #151c33;
  --panel: rgba(20, 26, 46, 0.72);
  --line: rgba(210, 220, 255, 0.14);
  --ink: #eaeefb;
  --muted: #97a2c6;
  --accent: #a5b4fc;
}

.vtr-10__stage {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem, 5vw, 4rem) clamp(1rem, 4vw, 2.5rem);
}

.vtr-10__panel {
  width: 100%;
  max-width: 34rem;
  padding: clamp(1.5rem, 4vw, 2.25rem);
  border: 1px solid var(--line);
  border-radius: 1.25rem;
  background: var(--panel);
  -webkit-backdrop-filter: blur(18px) saturate(140%);
  backdrop-filter: blur(18px) saturate(140%);
  box-shadow: 0 24px 60px -32px rgba(10, 15, 40, 0.55);
  display: grid;
  gap: 1.5rem;
  min-inline-size: 0;
}

.vtr-10__kicker {
  margin: 0 0 0.5rem;
  font-size: 0.7rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-10__heading {
  margin: 0;
  font-size: clamp(1.4rem, 4.4vw, 1.9rem);
  font-weight: 600;
  letter-spacing: -0.02em;
}

.vtr-10__sub {
  margin: 0.5rem 0 0;
  font-size: 0.9rem;
  line-height: 1.6;
  color: var(--muted);
}

.vtr-10__row {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 0;
  border-top: 1px solid var(--line);
  border-bottom: 1px solid var(--line);
}

.vtr-10__rowtext {
  min-inline-size: 0;
}

.vtr-10__rowtitle {
  margin: 0 0 0.15rem;
  font-size: 0.95rem;
  font-weight: 600;
}

.vtr-10__rownote {
  margin: 0;
  font-size: 0.8rem;
  color: var(--muted);
}

.vtr-10__toggle {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  min-height: 44px;
  padding: 0 1.1rem;
  border: 1px solid var(--accent);
  border-radius: 999px;
  background: transparent;
  color: var(--accent);
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
}

.vtr-10__toggle:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.vtr-10__ico {
  display: inline-flex;
}

.vtr-10__facts {
  margin: 0;
  display: grid;
  gap: 0.6rem;
}

.vtr-10__facts div {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  font-size: 0.8rem;
  min-inline-size: 0;
}

.vtr-10__facts dt {
  color: var(--muted);
}

.vtr-10__facts dd {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.75rem;
}

.vtr-10__stage {
  view-transition-name: vtr-10-root;
}

@keyframes vtr-10-reveal {
  from {
    clip-path: circle(0 at var(--vtr-10-x, 50%) var(--vtr-10-y, 50%));
  }

  to {
    clip-path: circle(var(--vtr-10-r, 120vmax) at var(--vtr-10-x, 50%) var(--vtr-10-y, 50%));
  }
}

::view-transition-old(vtr-10-root) {
  animation: none;
}

::view-transition-new(vtr-10-root) {
  animation: vtr-10-reveal 620ms cubic-bezier(0.32, 0.72, 0, 1) both;
  z-index: 2;
}

::view-transition-old(vtr-10-root) {
  z-index: 1;
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-new(vtr-10-root) {
    animation-duration: 1ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-10 {
  position: relative;
}

.vtr-10__theme {
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

.vtr-10__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-10__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-10__themeopt {
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

.vtr-10__themeopt:hover {
  opacity: 0.85;
}

.vtr-10__themeinput:checked + .vtr-10__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-10__themeinput:focus-visible + .vtr-10__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-10:has(#vtr-10-theme-light:checked) {
  --bg1: #eef1f8;
  --bg2: #dfe4f2;
  --panel: rgba(255, 255, 255, 0.72);
  --line: rgba(23, 30, 56, 0.12);
  --ink: #141a2e;
  --muted: #59617e;
  --accent: #4f46e5;
}

.vtr-10:has(#vtr-10-theme-dark:checked) {
  --bg1: #0b0f1d;
  --bg2: #151c33;
  --panel: rgba(20, 26, 46, 0.72);
  --line: rgba(210, 220, 255, 0.14);
  --ink: #eaeefb;
  --muted: #97a2c6;
  --accent: #a5b4fc;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.vtr-10');
  if (!root || root.dataset.vtr10) return;
  root.dataset.vtr10 = 'on';
  const btn = root.querySelector('#vtr-10-toggle');
  const stage = root.querySelector('#vtr-10-stage');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let busy = false;
  const flip = () => {
    const dark = root.dataset.theme === 'dark';
    root.dataset.theme = dark ? 'light' : 'dark';
    btn.setAttribute('aria-pressed', String(!dark));
    root.querySelector('#vtr-10-state').textContent = dark ? 'Light' : 'Dark';
  };
  btn.addEventListener('click', async (e) => {
    if (busy) return;
    if (!document.startViewTransition || reduce.matches) { flip(); return; }
    const x = e.clientX || btn.getBoundingClientRect().left;
    const y = e.clientY || btn.getBoundingClientRect().top;
    const r = Math.hypot(Math.max(x, innerWidth - x), Math.max(y, innerHeight - y));
    const rootEl = document.documentElement.style;
    rootEl.setProperty('--vtr-10-x', x + 'px');
    rootEl.setProperty('--vtr-10-y', y + 'px');
    rootEl.setProperty('--vtr-10-r', r + 'px');
    root.querySelector('#vtr-10-origin').textContent = Math.round(x) + ', ' + Math.round(y);
    busy = true;
    try { await document.startViewTransition(flip).finished; } finally { busy = false; }
  });
})();
```
