---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/view-transition-types/"
title: "View Transition Types"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "One transition, two behaviours: pass types: ['forward'] to document.startViewTransition() and branch on :active-view-transition-type(forward) in CSS. Forward…"
has_js: "true"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: View Transition Types
Source: https://codefronts.com/motion/css-view-transitions/view-transition-types/

One transition, two behaviours: pass types: ['forward'] to document.startViewTransition() and branch on :active-view-transition-type(forward) in CSS. Forward navigation slides left, back slides right, from a single call site. This is the piece that makes the API usable in a real router, and the type list is cleared automatically when the transition ends.
## HTML
```html
<section class="vtr-05" aria-labelledby="vtr-05-heading">
  <fieldset class="vtr-05__theme">
    <legend class="vtr-05__themelegend">Theme</legend>
    <input class="vtr-05__themeinput" type="radio" name="vtr-05-theme" id="vtr-05-theme-auto" checked>
    <label class="vtr-05__themeopt" for="vtr-05-theme-auto">Auto</label>
    <input class="vtr-05__themeinput" type="radio" name="vtr-05-theme" id="vtr-05-theme-light">
    <label class="vtr-05__themeopt" for="vtr-05-theme-light">Light</label>
    <input class="vtr-05__themeinput" type="radio" name="vtr-05-theme" id="vtr-05-theme-dark">
    <label class="vtr-05__themeopt" for="vtr-05-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-05__stage">
    <header class="vtr-05__head">
      <p class="vtr-05__kicker">types: ['forward'] · types: ['back']</p>
      <h2 class="vtr-05__heading" id="vtr-05-heading">One call site, two directions</h2>
      <p class="vtr-05__sub">The transition carries a tag. CSS reads it and picks the keyframes.</p>
    </header>

    <div class="vtr-05__router">
      <div class="vtr-05__crumbs" id="vtr-05-crumbs">
        <span class="vtr-05__crumb">Orbit</span>
        <span class="vtr-05__sep" aria-hidden="true">/</span>
        <span class="vtr-05__crumb vtr-05__crumb--live" id="vtr-05-crumb">Deployments</span>
      </div>
      <div class="vtr-05__panel" id="vtr-05-panel" data-step="0">
        <p class="vtr-05__route" id="vtr-05-route">/deployments</p>
        <h3 class="vtr-05__ptitle" id="vtr-05-ptitle">14 deployments today</h3>
        <p class="vtr-05__pbody" id="vtr-05-pbody">Every build from the main branch since 06:00. Select one to open its logs.</p>
      </div>
      <div class="vtr-05__nav">
        <button class="vtr-05__btn" type="button" data-vtr05-dir="back" disabled>Back</button>
        <button class="vtr-05__btn vtr-05__btn--primary" type="button" data-vtr05-dir="forward">Forward</button>
      </div>
    </div>

    <div class="vtr-05__branches">
      <div class="vtr-05__branch">
        <p class="vtr-05__blabel">:active-view-transition-type(forward)</p>
        <pre class="vtr-05__code"><code>::view-transition-old(vtr-05-panel) { animation: vtr-05-exit-l 340ms both; }
::view-transition-new(vtr-05-panel) { animation: vtr-05-enter-r 340ms both; }</code></pre>
        <p class="vtr-05__bnote">Old panel exits left, new panel enters from the right.</p>
      </div>
      <div class="vtr-05__branch">
        <p class="vtr-05__blabel">:active-view-transition-type(back)</p>
        <pre class="vtr-05__code"><code>::view-transition-old(vtr-05-panel) { animation: vtr-05-exit-r 340ms both; }
::view-transition-new(vtr-05-panel) { animation: vtr-05-enter-l 340ms both; }</code></pre>
        <p class="vtr-05__bnote">Mirrored, from the same JavaScript call.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.vtr-05 {
  --bg: #000000;
  --surface: #0b0b0f;
  --surface-2: #14141b;
  --line: #26262f;
  --ink: #f2f2f7;
  --muted: #8f8fa3;
  --accent: #a855f7;
  --accent-soft: #21133a;
  --dur: 340ms;
  --font-display: ui-monospace, "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  color-scheme: dark light;
}

.vtr-05 *,
.vtr-05 *::before,
.vtr-05 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-05 {
    --surface: oklch(15% 0.008 300);
    --surface-2: oklch(20% 0.012 300);
    --line: oklch(30% 0.014 300);
    --ink: oklch(96% 0.004 300);
    --muted: oklch(66% 0.02 300);
    --accent: oklch(70% 0.2 305);
    --accent-soft: oklch(26% 0.09 305);
  }
}

@media (prefers-color-scheme: light) {
  .vtr-05 {
    --bg: #f5f3fa;
    --surface: #ffffff;
    --surface-2: #f7f4fd;
    --line: #ddd6ec;
    --ink: #14101d;
    --muted: #5c5470;
    --accent: #7c3aed;
    --accent-soft: #efe7fe;
  }
}

.vtr-05[data-theme="light"] {
  --bg: #f5f3fa;
  --surface: #ffffff;
  --surface-2: #f7f4fd;
  --line: #ddd6ec;
  --ink: #14101d;
  --muted: #5c5470;
  --accent: #7c3aed;
  --accent-soft: #efe7fe;
}

.vtr-05[data-theme="dark"] {
  --bg: #000000;
  --surface: #0b0b0f;
  --surface-2: #14141b;
  --line: #26262f;
  --ink: #f2f2f7;
  --muted: #8f8fa3;
  --accent: #a855f7;
  --accent-soft: #21133a;
}

.vtr-05__stage {
  max-width: 60rem;
  margin: 0 auto;
  padding: clamp(1.25rem, 4vw, 2.75rem) clamp(0.9rem, 4vw, 2.25rem);
  display: grid;
  gap: 1.1rem;
}

.vtr-05__kicker {
  margin: 0 0 0.4rem;
  font-family: var(--font-display);
  font-size: 0.7rem;
  color: var(--accent);
}

.vtr-05__heading {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.3rem, 4.2vw, 1.85rem);
  font-weight: 600;
  letter-spacing: -0.02em;
}

.vtr-05__sub {
  margin: 0.35rem 0 0;
  font-size: 0.86rem;
  color: var(--muted);
}

.vtr-05__router {
  border: 1px solid var(--line);
  border-radius: 0.5rem;
  background: var(--surface);
  box-shadow: 0 0 0 1px rgba(168, 85, 247, 0.12), 0 0 32px -14px rgba(168, 85, 247, 0.5);
  overflow: hidden;
  min-inline-size: 0;
}

.vtr-05__crumbs {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.5rem 0.75rem;
  border-bottom: 1px solid var(--line);
  font-family: var(--font-display);
  font-size: 0.7rem;
  color: var(--muted);
  flex-wrap: wrap;
}

.vtr-05__crumb--live {
  color: var(--accent);
  view-transition-name: vtr-05-crumb;
}

.vtr-05__panel {
  padding: 1.1rem 0.9rem 1.25rem;
  background: var(--surface-2);
  view-transition-name: vtr-05-panel;
  min-inline-size: 0;
}

.vtr-05__route {
  margin: 0 0 0.5rem;
  font-family: var(--font-display);
  font-size: 0.68rem;
  color: var(--accent);
}

.vtr-05__ptitle {
  margin: 0 0 0.4rem;
  font-family: var(--font-display);
  font-size: clamp(1.05rem, 3.4vw, 1.3rem);
  font-weight: 600;
}

.vtr-05__pbody {
  margin: 0;
  font-size: 0.82rem;
  line-height: 1.55;
  color: var(--muted);
  max-width: 34rem;
}

.vtr-05__nav {
  display: flex;
  gap: 0.4rem;
  padding: 0.6rem 0.75rem;
  border-top: 1px solid var(--line);
  flex-wrap: wrap;
}

.vtr-05__btn {
  min-height: 44px;
  padding: 0 1rem;
  border: 1px solid var(--line);
  border-radius: 0.35rem;
  background: transparent;
  color: var(--ink);
  font-family: var(--font-display);
  font-size: 0.76rem;
  cursor: pointer;
}

.vtr-05__btn--primary {
  border-color: var(--accent);
  color: var(--accent);
  background: var(--accent-soft);
}

.vtr-05__btn:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}

.vtr-05__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.vtr-05__branches {
  display: grid;
  gap: 0.75rem;
  grid-template-columns: 1fr;
}

@media (min-width: 52rem) {
  .vtr-05__branches {
    grid-template-columns: 1fr 1fr;
  }
}

.vtr-05__branch {
  border: 1px solid var(--line);
  border-radius: 0.5rem;
  padding: 0.75rem 0.8rem;
  background: var(--surface);
  display: grid;
  gap: 0.5rem;
  min-inline-size: 0;
}

.vtr-05__blabel {
  margin: 0;
  font-family: var(--font-display);
  font-size: 0.7rem;
  color: var(--accent);
  word-break: break-word;
}

.vtr-05__code {
  margin: 0;
  padding: 0.6rem 0.65rem;
  overflow-x: auto;
  background: var(--surface-2);
  border-radius: 0.3rem;
  font-family: var(--font-display);
  font-size: 0.66rem;
  line-height: 1.6;
  color: var(--ink);
}

.vtr-05__bnote {
  margin: 0;
  font-size: 0.74rem;
  color: var(--muted);
}

@keyframes vtr-05-exit-l {
  to {
    transform: translateX(-14%);
    opacity: 0;
  }
}

@keyframes vtr-05-enter-r {
  from {
    transform: translateX(14%);
    opacity: 0;
  }
}

@keyframes vtr-05-exit-r {
  to {
    transform: translateX(14%);
    opacity: 0;
  }
}

@keyframes vtr-05-enter-l {
  from {
    transform: translateX(-14%);
    opacity: 0;
  }
}

:root:active-view-transition-type(vtr-05-forward) ::view-transition-old(vtr-05-panel) {
  animation: vtr-05-exit-l 340ms cubic-bezier(0.32, 0.72, 0, 1) both;
}

:root:active-view-transition-type(vtr-05-forward) ::view-transition-new(vtr-05-panel) {
  animation: vtr-05-enter-r 340ms cubic-bezier(0.32, 0.72, 0, 1) both;
}

:root:active-view-transition-type(vtr-05-back) ::view-transition-old(vtr-05-panel) {
  animation: vtr-05-exit-r 340ms cubic-bezier(0.32, 0.72, 0, 1) both;
}

:root:active-view-transition-type(vtr-05-back) ::view-transition-new(vtr-05-panel) {
  animation: vtr-05-enter-l 340ms cubic-bezier(0.32, 0.72, 0, 1) both;
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(vtr-05-panel),
    ::view-transition-group(vtr-05-crumb) {
    animation-duration: 1ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-05 {
  position: relative;
}

.vtr-05__theme {
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

.vtr-05__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-05__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-05__themeopt {
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

.vtr-05__themeopt:hover {
  opacity: 0.85;
}

.vtr-05__themeinput:checked + .vtr-05__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-05__themeinput:focus-visible + .vtr-05__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-05:has(#vtr-05-theme-light:checked) {
  --bg: #f5f3fa;
  --surface: #ffffff;
  --surface-2: #f7f4fd;
  --line: #ddd6ec;
  --ink: #14101d;
  --muted: #5c5470;
  --accent: #7c3aed;
  --accent-soft: #efe7fe;
}

.vtr-05:has(#vtr-05-theme-dark:checked) {
  --bg: #000000;
  --surface: #0b0b0f;
  --surface-2: #14141b;
  --line: #26262f;
  --ink: #f2f2f7;
  --muted: #8f8fa3;
  --accent: #a855f7;
  --accent-soft: #21133a;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.vtr-05');
  if (!root || root.dataset.vtr05) return;
  root.dataset.vtr05 = 'on';
  const panel = root.querySelector('#vtr-05-panel');
  const steps = [
    ['Deployments', '/deployments', '14 deployments today', 'Every build from the main branch since 06:00. Select one to open its logs.'],
    ['Build 4712', '/deployments/4712', 'Build 4712 · passed', 'Triggered by Priya Sharma. 2m 14s across four workers, no failed checks.'],
    ['Logs', '/deployments/4712/logs', 'Worker log · orbit-2', 'Tail of the final 200 lines. Filters apply to the visible range only.']
  ];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const back = root.querySelector('[data-vtr05-dir="back"]');
  const fwd = root.querySelector('[data-vtr05-dir="forward"]');
  let i = 0, busy = false;
  const slots = ['#vtr-05-crumb', '#vtr-05-route', '#vtr-05-ptitle', '#vtr-05-pbody'];
  const apply = (n) => {
    i = n; panel.dataset.step = String(n);
    slots.forEach((sel, k) => { root.querySelector(sel).textContent = steps[n][k]; });
    back.disabled = n === 0; fwd.disabled = n === steps.length - 1;
  };
  const go = async (dir) => {
    const n = i + (dir === 'forward' ? 1 : -1);
    if (n < 0 || n >= steps.length || busy) return;
    if (!document.startViewTransition || reduce.matches) { apply(n); return; }
    busy = true;
    try { await document.startViewTransition({ update: () => apply(n), types: ['vtr-05-' + dir] }).finished; }
    finally { busy = false; }
  };
  [back, fwd].forEach(b => b.addEventListener('click', () => go(b.dataset.vtr05Dir)));
})();
```
