---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/preventing-flicker-and-z-index-stacking/"
title: "Preventing Flicker and Z Index Stacking"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "The debugging page."
has_js: "true"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Preventing Flicker and Z Index Stacking
Source: https://codefronts.com/motion/css-view-transitions/preventing-flicker-and-z-index-stacking/

The debugging page. Four failure modes in the order they actually bite: a duplicate view-transition-name aborting the whole transition with no error, pseudo-element paint order that ignores page z-index, a flash of the old state when the callback does async work without returning a promise, and transitions stacking during rapid interaction.
## HTML
```html
<section class="vtr-20" aria-labelledby="vtr-20-heading">
  <fieldset class="vtr-20__theme">
    <legend class="vtr-20__themelegend">Theme</legend>
    <input class="vtr-20__themeinput" type="radio" name="vtr-20-theme" id="vtr-20-theme-auto" checked>
    <label class="vtr-20__themeopt" for="vtr-20-theme-auto">Auto</label>
    <input class="vtr-20__themeinput" type="radio" name="vtr-20-theme" id="vtr-20-theme-light">
    <label class="vtr-20__themeopt" for="vtr-20-theme-light">Light</label>
    <input class="vtr-20__themeinput" type="radio" name="vtr-20-theme" id="vtr-20-theme-dark">
    <label class="vtr-20__themeopt" for="vtr-20-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-20__stage">
    <header class="vtr-20__head">
      <p class="vtr-20__kicker">debug · view transitions</p>
      <h2 class="vtr-20__heading" id="vtr-20-heading">Four ways it silently fails</h2>
      <p class="vtr-20__sub">In the order they bite. Each row runs on its own.</p>
    </header>

    <ol class="vtr-20__checks">
      <li class="vtr-20__check">
        <div class="vtr-20__ctext">
          <p class="vtr-20__cname">01 · Duplicate name</p>
          <p class="vtr-20__cdesc">Two elements share a name at capture time. The whole transition is abandoned. No error is logged.</p>
          <code class="vtr-20__cfix">clear names in a finally block</code>
        </div>
        <button class="vtr-20__run" type="button" data-vtr20-run="dupe">Run</button>
      </li>
      <li class="vtr-20__check">
        <div class="vtr-20__ctext">
          <p class="vtr-20__cname">02 · Wrong paint order</p>
          <p class="vtr-20__cdesc">Groups paint in creation order in the top layer. Page z-index has no effect on them.</p>
          <code class="vtr-20__cfix">::view-transition-new(name) { z-index: 2 }</code>
        </div>
        <button class="vtr-20__run" type="button" data-vtr20-run="layer">Run</button>
      </li>
      <li class="vtr-20__check">
        <div class="vtr-20__ctext">
          <p class="vtr-20__cname">03 · Async callback flash</p>
          <p class="vtr-20__cdesc">The callback awaits without returning the promise, so the second snapshot is taken too early.</p>
          <code class="vtr-20__cfix">return the promise from the callback</code>
        </div>
        <button class="vtr-20__run" type="button" data-vtr20-run="async">Run</button>
      </li>
      <li class="vtr-20__check">
        <div class="vtr-20__ctext">
          <p class="vtr-20__cname">04 · Stacked transitions</p>
          <p class="vtr-20__cdesc">A second call starts mid-animation and layers snapshots from three states.</p>
          <code class="vtr-20__cfix">await t.finished, or t.skipTransition()</code>
        </div>
        <button class="vtr-20__run" type="button" data-vtr20-run="stack">Run</button>
      </li>
    </ol>

    <div class="vtr-20__panel">
      <p class="vtr-20__plabel">Subject</p>
      <div class="vtr-20__subject" id="vtr-20-subject">
        <span class="vtr-20__badge" id="vtr-20-badge">v2.1.0</span>
        <span class="vtr-20__text" id="vtr-20-text">orbit-api · 4 replicas healthy</span>
      </div>
      <p class="vtr-20__log" id="vtr-20-log" role="status" aria-live="polite">No run yet.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.vtr-20 {
  --bg: #17171a;
  --surface: #1e1e22;
  --surface-2: #26262b;
  --line: #34343b;
  --ink: #f0f0f3;
  --muted: #9b9ba6;
  --accent: #ef4444;
  --accent-soft: #33191a;
  --ok: #4ade80;
  --font-display: ui-monospace, "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-display);
  color-scheme: dark light;
}

.vtr-20 *,
.vtr-20 *::before,
.vtr-20 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-20 {
    --bg: oklch(21% 0.004 300);
    --surface: oklch(25% 0.005 300);
    --surface-2: oklch(29% 0.006 300);
    --line: oklch(35% 0.008 300);
    --ink: oklch(96% 0.003 300);
    --muted: oklch(70% 0.012 300);
    --accent: oklch(63% 0.2 25);
    --accent-soft: oklch(28% 0.06 25);
    --ok: oklch(80% 0.16 150);
  }
}

@media (prefers-color-scheme: light) {
  .vtr-20 {
    --bg: #f6f6f7;
    --surface: #ffffff;
    --surface-2: #eeeef1;
    --line: #dcdce1;
    --ink: #16161a;
    --muted: #5c5c66;
    --accent: #dc2626;
    --accent-soft: #fde8e8;
    --ok: #15803d;
  }
}

.vtr-20[data-theme="light"] {
  --bg: #f6f6f7;
  --surface: #ffffff;
  --surface-2: #eeeef1;
  --line: #dcdce1;
  --ink: #16161a;
  --muted: #5c5c66;
  --accent: #dc2626;
  --accent-soft: #fde8e8;
  --ok: #15803d;
}

.vtr-20[data-theme="dark"] {
  --bg: #17171a;
  --surface: #1e1e22;
  --surface-2: #26262b;
  --line: #34343b;
  --ink: #f0f0f3;
  --muted: #9b9ba6;
  --accent: #ef4444;
  --accent-soft: #33191a;
  --ok: #4ade80;
}

.vtr-20__stage {
  max-width: 56rem;
  margin: 0 auto;
  padding: clamp(1rem, 3.5vw, 2rem) clamp(0.75rem, 3.5vw, 1.75rem);
  display: grid;
  gap: 0.75rem;
}

.vtr-20__kicker {
  margin: 0 0 0.2rem;
  font-size: 0.66rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-20__heading {
  margin: 0;
  font-size: clamp(1.1rem, 3.6vw, 1.5rem);
  font-weight: 600;
  letter-spacing: -0.01em;
}

.vtr-20__sub {
  margin: 0.25rem 0 0;
  font-size: 0.74rem;
  color: var(--muted);
}

.vtr-20__checks {
  margin: 0;
  padding: 0;
  list-style: none;
  border: 1px solid var(--line);
  border-radius: 0.2rem;
  background: var(--surface);
}

.vtr-20__check {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 0.75rem;
  align-items: center;
  padding: 0.6rem 0.7rem;
  border-bottom: 1px solid var(--line);
}

.vtr-20__check:last-child {
  border-bottom: 0;
}

.vtr-20__ctext {
  min-inline-size: 0;
  display: grid;
  gap: 0.15rem;
}

.vtr-20__cname {
  margin: 0;
  font-size: 0.76rem;
  font-weight: 600;
}

.vtr-20__cdesc {
  margin: 0;
  font-size: 0.7rem;
  line-height: 1.5;
  color: var(--muted);
}

.vtr-20__cfix {
  font-size: 0.66rem;
  color: var(--ok);
  word-break: break-word;
}

.vtr-20__run {
  min-height: 44px;
  padding: 0 0.8rem;
  border: 1px solid var(--line);
  border-radius: 0.15rem;
  background: var(--surface-2);
  color: var(--ink);
  font-family: inherit;
  font-size: 0.72rem;
  cursor: pointer;
}

.vtr-20__run:hover {
  border-color: var(--accent);
  color: var(--accent);
}

.vtr-20__run:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.vtr-20__panel {
  border: 1px solid var(--line);
  border-radius: 0.2rem;
  padding: 0.7rem 0.75rem;
  background: var(--surface);
  display: grid;
  gap: 0.5rem;
}

.vtr-20__plabel {
  margin: 0;
  font-size: 0.62rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--muted);
}

.vtr-20__subject {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  flex-wrap: wrap;
  padding: 0.6rem 0.7rem;
  border-radius: 0.15rem;
  background: var(--surface-2);
  view-transition-name: vtr-20-subject;
}

.vtr-20__badge {
  padding: 0.2rem 0.45rem;
  border-radius: 0.15rem;
  background: var(--accent-soft);
  color: var(--accent);
  font-size: 0.7rem;
  view-transition-name: vtr-20-badge;
}

.vtr-20__text {
  font-size: 0.76rem;
  min-inline-size: 0;
}

.vtr-20__log {
  margin: 0;
  padding: 0.5rem 0.6rem;
  border-left: 2px solid var(--accent);
  background: var(--surface-2);
  font-size: 0.7rem;
  line-height: 1.5;
  color: var(--muted);
}

::view-transition-group(vtr-20-subject),
::view-transition-group(vtr-20-badge) {
  animation-duration: 420ms;
}

::view-transition-new(vtr-20-badge) {
  z-index: 2;
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(vtr-20-subject),
    ::view-transition-group(vtr-20-badge) {
    animation-duration: 1ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-20 {
  position: relative;
}

.vtr-20__theme {
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

.vtr-20__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-20__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-20__themeopt {
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

.vtr-20__themeopt:hover {
  opacity: 0.85;
}

.vtr-20__themeinput:checked + .vtr-20__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-20__themeinput:focus-visible + .vtr-20__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-20:has(#vtr-20-theme-light:checked) {
  --bg: #f6f6f7;
  --surface: #ffffff;
  --surface-2: #eeeef1;
  --line: #dcdce1;
  --ink: #16161a;
  --muted: #5c5c66;
  --accent: #dc2626;
  --accent-soft: #fde8e8;
  --ok: #15803d;
}

.vtr-20:has(#vtr-20-theme-dark:checked) {
  --bg: #17171a;
  --surface: #1e1e22;
  --surface-2: #26262b;
  --line: #34343b;
  --ink: #f0f0f3;
  --muted: #9b9ba6;
  --accent: #ef4444;
  --accent-soft: #33191a;
  --ok: #4ade80;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.vtr-20');
  if (!root || root.dataset.vtr20) return;
  root.dataset.vtr20 = 'on';
  const badge = root.querySelector('#vtr-20-badge');
  const text = root.querySelector('#vtr-20-text');
  const log = root.querySelector('#vtr-20-log');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const rev = [['v2.1.0', 'orbit-api · 4 replicas healthy'], ['v2.2.0', 'orbit-api · rolling 2 of 4'], ['v2.3.1', 'orbit-api · 6 replicas healthy']];
  let n = 0, busy = false;
  const bump = () => { n = (n + 1) % 3; badge.textContent = rev[n][0]; text.textContent = rev[n][1]; };
  const notes = {
    dupe: 'Duplicate name: a second element took vtr-20-badge, so the browser abandoned the transition. Nothing animated and nothing was logged.',
    layer: 'Paint order: the badge is raised with z-index on ::view-transition-new(), not with page z-index, which the pseudo tree ignores.',
    async: 'Async callback: the promise is returned from the callback, so the old snapshot is held until the update resolves instead of flashing.',
    stack: 'Stacked calls: three updates fired at once. The in-flight flag kept the first and dropped the rest.'
  };
  root.addEventListener('click', async (e) => {
    const btn = e.target.closest('[data-vtr20-run]');
    if (!btn) return;
    const mode = btn.dataset.vtr20Run; log.textContent = notes[mode];
    if (!document.startViewTransition || reduce.matches) { bump(); return; }
    if (busy) return; busy = true;
    const clone = mode === 'dupe' ? badge.cloneNode(true) : null;
    if (clone) { clone.style.position = 'absolute'; clone.style.opacity = '0'; root.append(clone); }
    const work = mode === 'async' ? () => new Promise(r => setTimeout(() => { bump(); r(); }, 220)) : bump;
    try { await document.startViewTransition(work).finished.catch(() => {}); }
    finally { if (clone) clone.remove(); busy = false; }
  });
})();
```
