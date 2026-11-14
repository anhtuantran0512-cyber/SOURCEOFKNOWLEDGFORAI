---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/basic-spa-view-transition/"
title: "Basic SPA View Transition"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "The reference build every other demo in this collection borrows from."
has_js: "true"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Basic SPA View Transition
Source: https://codefronts.com/motion/css-view-transitions/basic-spa-view-transition/

The reference build every other demo in this collection borrows from. One call to document.startViewTransition() wraps a panel swap, and an annotation column names the three phases the browser runs: screenshot the old state, run your callback, screenshot the new state and animate between them. Reach for it the first time you replace a hand-rolled fade with the API.
## HTML
```html
<section class="vtr-01" aria-labelledby="vtr-01-heading">
  <fieldset class="vtr-01__theme">
    <legend class="vtr-01__themelegend">Theme</legend>
    <input class="vtr-01__themeinput" type="radio" name="vtr-01-theme" id="vtr-01-theme-auto" checked>
    <label class="vtr-01__themeopt" for="vtr-01-theme-auto">Auto</label>
    <input class="vtr-01__themeinput" type="radio" name="vtr-01-theme" id="vtr-01-theme-light">
    <label class="vtr-01__themeopt" for="vtr-01-theme-light">Light</label>
    <input class="vtr-01__themeinput" type="radio" name="vtr-01-theme" id="vtr-01-theme-dark">
    <label class="vtr-01__themeopt" for="vtr-01-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-01__stage">
    <header class="vtr-01__head">
      <p class="vtr-01__kicker">document.startViewTransition()</p>
      <h2 class="vtr-01__heading" id="vtr-01-heading">One call, three phases</h2>
      <p class="vtr-01__sub">The callback does the DOM work. The browser does the animation.</p>
    </header>

    <div class="vtr-01__grid">
      <ol class="vtr-01__phases">
        <li class="vtr-01__phase">
          <span class="vtr-01__badge">1</span>
          <div class="vtr-01__ptext">
            <h3 class="vtr-01__ptitle">Capture old</h3>
            <p class="vtr-01__pnote">Rendering pauses. Every named element and the root are snapshotted as images.</p>
          </div>
        </li>
        <li class="vtr-01__phase">
          <span class="vtr-01__badge">2</span>
          <div class="vtr-01__ptext">
            <h3 class="vtr-01__ptitle">Run callback</h3>
            <p class="vtr-01__pnote">Your function mutates the DOM synchronously. This is the only place the update may happen.</p>
          </div>
        </li>
        <li class="vtr-01__phase">
          <span class="vtr-01__badge">3</span>
          <div class="vtr-01__ptext">
            <h3 class="vtr-01__ptitle">Capture new and animate</h3>
            <p class="vtr-01__pnote">A second snapshot is taken and matching names are interpolated. Unmatched pairs cross-fade.</p>
          </div>
        </li>
      </ol>

      <div class="vtr-01__panel">
        <nav class="vtr-01__nav" aria-label="Account sections">
          <button class="vtr-01__tab" type="button" data-vtr01-go="overview" aria-current="true">Overview</button>
          <button class="vtr-01__tab" type="button" data-vtr01-go="billing">Billing</button>
        </nav>
        <div class="vtr-01__view" id="vtr-01-view" data-state="overview">
          <p class="vtr-01__eyebrow">Meridian Workspace</p>
          <h3 class="vtr-01__vtitle" id="vtr-01-title">Overview</h3>
          <dl class="vtr-01__stats">
            <div><dt>Active seats</dt><dd>34</dd></div>
            <div><dt>Deploys this week</dt><dd>112</dd></div>
            <div><dt>Region</dt><dd>eu-west-1</dd></div>
          </dl>
        </div>
      </div>
    </div>

    <pre class="vtr-01__code"><code>document.startViewTransition(() =&gt; {
  panel.dataset.state = next;   <span class="vtr-01__cm">// mutate here, synchronously</span>
});</code></pre>
  </div>
</section>
```
## CSS
```css
.vtr-01 {
  --bg: #f7f4ef;
  --surface: #ffffff;
  --line: #e2dcd1;
  --ink: #241f1a;
  --muted: #6d655b;
  --accent: #b45309;
  --accent-soft: #fdf0dc;
  --dur: 420ms;
  --font-display: ui-monospace, "JetBrains Mono", "SFMono-Regular", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  color-scheme: light dark;
}

.vtr-01 *,
.vtr-01 *::before,
.vtr-01 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-01 {
    --bg: oklch(96.5% 0.012 78);
    --surface: oklch(100% 0 0);
    --line: oklch(89% 0.016 76);
    --ink: oklch(24% 0.018 55);
    --muted: oklch(52% 0.018 60);
    --accent: oklch(56% 0.14 62);
    --accent-soft: oklch(95% 0.04 74);
  }
}

@media (prefers-color-scheme: dark) {
  .vtr-01 {
    --bg: #17130f;
    --surface: #211b16;
    --line: #342c24;
    --ink: #f4ece2;
    --muted: #a89a8b;
    --accent: #f0a13c;
    --accent-soft: #322418;
  }
}

.vtr-01[data-theme="light"] {
  --bg: #f7f4ef;
  --surface: #ffffff;
  --line: #e2dcd1;
  --ink: #241f1a;
  --muted: #6d655b;
  --accent: #b45309;
  --accent-soft: #fdf0dc;
}

.vtr-01[data-theme="dark"] {
  --bg: #17130f;
  --surface: #211b16;
  --line: #342c24;
  --ink: #f4ece2;
  --muted: #a89a8b;
  --accent: #f0a13c;
  --accent-soft: #322418;
}

.vtr-01__stage {
  max-width: 62rem;
  margin: 0 auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.5rem);
  display: grid;
  gap: 1.5rem;
}

.vtr-01__kicker {
  margin: 0 0 0.5rem;
  font-family: var(--font-display);
  font-size: 0.7rem;
  letter-spacing: 0.04em;
  color: var(--accent);
}

.vtr-01__heading {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.35rem, 4vw, 1.9rem);
  font-weight: 600;
  letter-spacing: -0.01em;
}

.vtr-01__sub {
  margin: 0.4rem 0 0;
  color: var(--muted);
  font-size: 0.9rem;
  max-width: 34rem;
}

.vtr-01__grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr;
}

@media (min-width: 60rem) {
  .vtr-01__grid {
    grid-template-columns: 20rem 1fr;
  }
}

.vtr-01__phases {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0.75rem;
  align-content: start;
  border-top: 1px solid var(--line);
}

.vtr-01__phase {
  display: grid;
  grid-template-columns: 1.6rem 1fr;
  gap: 0.7rem;
  padding: 0.75rem 0;
  border-bottom: 1px solid var(--line);
}

.vtr-01__badge {
  display: grid;
  place-items: center;
  width: 1.6rem;
  height: 1.6rem;
  border-radius: 999px;
  background: var(--accent-soft);
  color: var(--accent);
  font-family: var(--font-display);
  font-size: 0.75rem;
}

.vtr-01__ptext {
  min-inline-size: 0;
}

.vtr-01__ptitle {
  margin: 0.15rem 0 0.2rem;
  font-family: var(--font-display);
  font-size: 0.8rem;
  font-weight: 600;
}

.vtr-01__pnote {
  margin: 0;
  font-size: 0.78rem;
  line-height: 1.5;
  color: var(--muted);
}

.vtr-01__panel {
  border: 1px solid var(--line);
  background: var(--surface);
  border-radius: 0.5rem;
  overflow: hidden;
  min-inline-size: 0;
}

.vtr-01__nav {
  display: flex;
  gap: 0.25rem;
  padding: 0.5rem;
  border-bottom: 1px solid var(--line);
  flex-wrap: wrap;
}

.vtr-01__tab {
  min-height: 44px;
  padding: 0 0.9rem;
  border: 1px solid transparent;
  border-radius: 0.35rem;
  background: none;
  color: var(--muted);
  font-family: var(--font-display);
  font-size: 0.78rem;
  cursor: pointer;
}

.vtr-01__tab[aria-current="true"] {
  background: var(--accent-soft);
  color: var(--accent);
  border-color: var(--line);
}

.vtr-01__tab:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.vtr-01__view {
  padding: 1.1rem;
  view-transition-name: vtr-01-view;
  contain: paint;
}

.vtr-01__eyebrow {
  margin: 0 0 0.35rem;
  font-family: var(--font-display);
  font-size: 0.68rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
}

.vtr-01__vtitle {
  margin: 0 0 0.9rem;
  font-family: var(--font-display);
  font-size: 1.25rem;
  font-weight: 600;
  view-transition-name: vtr-01-title;
}

.vtr-01__stats {
  margin: 0;
  display: grid;
  gap: 0.5rem;
}

.vtr-01__stats div {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  padding-bottom: 0.5rem;
  border-bottom: 1px dashed var(--line);
  min-inline-size: 0;
}

.vtr-01__stats dt {
  font-size: 0.82rem;
  color: var(--muted);
}

.vtr-01__stats dd {
  margin: 0;
  font-family: var(--font-display);
  font-size: 0.82rem;
}

.vtr-01__code {
  margin: 0;
  padding: 0.9rem 1rem;
  overflow-x: auto;
  border: 1px solid var(--line);
  border-radius: 0.5rem;
  background: var(--surface);
  font-family: var(--font-display);
  font-size: 0.74rem;
  line-height: 1.7;
}

.vtr-01__cm {
  color: var(--muted);
}

::view-transition-old(vtr-01-view),
::view-transition-new(vtr-01-view) {
  animation-duration: 420ms;
}

::view-transition-group(vtr-01-title) {
  animation-duration: 420ms;
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(vtr-01-view),
    ::view-transition-group(vtr-01-title) {
    animation-duration: 1ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-01 {
  position: relative;
}

.vtr-01__theme {
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

.vtr-01__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-01__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-01__themeopt {
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

.vtr-01__themeopt:hover {
  opacity: 0.85;
}

.vtr-01__themeinput:checked + .vtr-01__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-01__themeinput:focus-visible + .vtr-01__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-01:has(#vtr-01-theme-light:checked) {
  --bg: #f7f4ef;
  --surface: #ffffff;
  --line: #e2dcd1;
  --ink: #241f1a;
  --muted: #6d655b;
  --accent: #b45309;
  --accent-soft: #fdf0dc;
}

.vtr-01:has(#vtr-01-theme-dark:checked) {
  --bg: #17130f;
  --surface: #211b16;
  --line: #342c24;
  --ink: #f4ece2;
  --muted: #a89a8b;
  --accent: #f0a13c;
  --accent-soft: #322418;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.vtr-01');
  if (!root || root.dataset.vtr01) return;
  root.dataset.vtr01 = 'on';
  const view = root.querySelector('#vtr-01-view');
  const title = root.querySelector('#vtr-01-title');
  const tabs = [...root.querySelectorAll('[data-vtr01-go]')];
  const copy = {
    overview: ['Meridian Workspace', 'Overview', [['Active seats', '34'], ['Deploys this week', '112'], ['Region', 'eu-west-1']]],
    billing: ['Meridian Workspace', 'Billing', [['Plan', 'Scale'], ['Next invoice', 'Sep 1'], ['Seats billed', '34']]]
  };
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let busy = false;
  const apply = (key) => {
    const [eyebrow, heading, rows] = copy[key];
    view.dataset.state = key;
    view.querySelector('.vtr-01__eyebrow').textContent = eyebrow;
    title.textContent = heading;
    view.querySelector('.vtr-01__stats').innerHTML = rows.map(r => '<div><dt>' + r[0] + '</dt><dd>' + r[1] + '</dd></div>').join('');
    tabs.forEach(t => t.setAttribute('aria-current', String(t.dataset.vtr01Go === key)));
  };
  tabs.forEach(tab => tab.addEventListener('click', async () => {
    const key = tab.dataset.vtr01Go;
    if (key === view.dataset.state || busy) return;
    if (!document.startViewTransition || reduce.matches) { apply(key); return; }
    busy = true;
    try { await document.startViewTransition(() => apply(key)).finished; } finally { busy = false; }
  }));
})();
```
