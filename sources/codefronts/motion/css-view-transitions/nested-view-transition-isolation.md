---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/nested-view-transition-isolation/"
title: "Nested View Transition Isolation"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "When a parent container morphs, its children are captured as pixels inside the parent's flat snapshot and warp along with it — text stretches, buttons skew."
has_js: "true"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Nested View Transition Isolation
Source: https://codefronts.com/motion/css-view-transitions/nested-view-transition-isolation/

When a parent container morphs, its children are captured as pixels inside the parent's flat snapshot and warp along with it — text stretches, buttons skew. The fix is to give the children their own view-transition-name so they animate as independent groups. Shown as a matched pair: one card with only the parent named, one with the children named too.
## HTML
```html
<section class="vtr-19" aria-labelledby="vtr-19-heading">
  <fieldset class="vtr-19__theme">
    <legend class="vtr-19__themelegend">Theme</legend>
    <input class="vtr-19__themeinput" type="radio" name="vtr-19-theme" id="vtr-19-theme-auto" checked>
    <label class="vtr-19__themeopt" for="vtr-19-theme-auto">Auto</label>
    <input class="vtr-19__themeinput" type="radio" name="vtr-19-theme" id="vtr-19-theme-light">
    <label class="vtr-19__themeopt" for="vtr-19-theme-light">Light</label>
    <input class="vtr-19__themeinput" type="radio" name="vtr-19-theme" id="vtr-19-theme-dark">
    <label class="vtr-19__themeopt" for="vtr-19-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-19__stage">
    <header class="vtr-19__head">
      <p class="vtr-19__kicker">Isolation</p>
      <h2 class="vtr-19__heading" id="vtr-19-heading">Warped children, then named children</h2>
      <p class="vtr-19__sub">Both cards grow by the same amount. Only the right-hand one names its title and its control.</p>
    </header>

    <div class="vtr-19__pair">
      <article class="vtr-19__panel">
        <p class="vtr-19__plabel">Parent named only</p>
        <div class="vtr-19__card" id="vtr-19-card-a" data-big="false">
          <p class="vtr-19__ctitle">Meridian throughput report</p>
          <p class="vtr-19__cbody">The title and the button are pixels inside the card's snapshot, so they scale with it.</p>
          <span class="vtr-19__cbtn">Open report</span>
        </div>
        <button class="vtr-19__btn" type="button" data-vtr19-toggle="a">Grow the card</button>
      </article>

      <article class="vtr-19__panel vtr-19__panel--fixed">
        <p class="vtr-19__plabel">Children named</p>
        <div class="vtr-19__card" id="vtr-19-card-b" data-big="false">
          <p class="vtr-19__ctitle vtr-19__ctitle--named">Meridian throughput report</p>
          <p class="vtr-19__cbody">The title and the button are their own groups, so they travel and resize as elements.</p>
          <span class="vtr-19__cbtn vtr-19__cbtn--named">Open report</span>
        </div>
        <button class="vtr-19__btn vtr-19__btn--go" type="button" data-vtr19-toggle="b">Grow the card</button>
      </article>
    </div>

    <p class="vtr-19__foot">Name the headline, the primary image and any control with a hard edge. Body copy that barely changes size usually does not need it.</p>
  </div>
</section>
```
## CSS
```css
.vtr-19 {
  --bg: #07211f;
  --surface: #0c2c29;
  --surface-2: #103a36;
  --line: #1c4f49;
  --ink: #eafaf6;
  --muted: #86b3ac;
  --accent: #fbbf24;
  --accent-soft: #2a2c14;
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

.vtr-19 *,
.vtr-19 *::before,
.vtr-19 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-19 {
    --bg: oklch(25% 0.045 180);
    --surface: oklch(30% 0.05 180);
    --surface-2: oklch(35% 0.055 180);
    --line: oklch(43% 0.06 180);
    --ink: oklch(96% 0.02 175);
    --muted: oklch(74% 0.04 178);
    --accent: oklch(84% 0.16 85);
    --accent-soft: oklch(32% 0.06 90);
  }
}

@media (prefers-color-scheme: light) {
  .vtr-19 {
    --bg: #f0f7f5;
    --surface: #ffffff;
    --surface-2: #e4f0ed;
    --line: #bdd8d3;
    --ink: #06231f;
    --muted: #47635e;
    --accent: #a16207;
    --accent-soft: #fdf3d7;
  }
}

.vtr-19[data-theme="light"] {
  --bg: #f0f7f5;
  --surface: #ffffff;
  --surface-2: #e4f0ed;
  --line: #bdd8d3;
  --ink: #06231f;
  --muted: #47635e;
  --accent: #a16207;
  --accent-soft: #fdf3d7;
}

.vtr-19[data-theme="dark"] {
  --bg: #07211f;
  --surface: #0c2c29;
  --surface-2: #103a36;
  --line: #1c4f49;
  --ink: #eafaf6;
  --muted: #86b3ac;
  --accent: #fbbf24;
  --accent-soft: #2a2c14;
}

.vtr-19__stage {
  max-width: 60rem;
  margin: 0 auto;
  padding: clamp(1.5rem, 4vw, 3rem) clamp(1rem, 4vw, 2.25rem);
  display: grid;
  gap: 1.35rem;
}

.vtr-19__kicker {
  margin: 0 0 0.35rem;
  font-family: var(--font-display);
  font-size: 0.72rem;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-19__heading {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.4rem, 4.6vw, 2.1rem);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.005em;
}

.vtr-19__sub {
  margin: 0.4rem 0 0;
  font-size: 0.88rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 38rem;
}

.vtr-19__pair {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr;
}

@media (min-width: 52rem) {
  .vtr-19__pair {
    grid-template-columns: 1fr 1fr;
  }
}

.vtr-19__panel {
  border: 2px solid var(--line);
  background: var(--surface);
  padding: 0.85rem;
  display: grid;
  gap: 0.7rem;
  align-content: start;
  min-inline-size: 0;
}

.vtr-19__panel--fixed {
  border-color: var(--accent);
}

.vtr-19__plabel {
  margin: 0;
  font-family: var(--font-display);
  font-size: 0.7rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-19__card {
  width: 60%;
  padding: 0.75rem;
  background: var(--surface-2);
  border: 1px solid var(--line);
  display: grid;
  gap: 0.45rem;
  min-inline-size: 0;
}

.vtr-19__card[data-big="true"] {
  width: 100%;
  padding: 1.35rem;
}

#vtr-19-card-a {
  view-transition-name: vtr-19-card-a;
}

#vtr-19-card-b {
  view-transition-name: vtr-19-card-b;
}

.vtr-19__ctitle {
  margin: 0;
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.02em;
}

.vtr-19__ctitle--named {
  view-transition-name: vtr-19-title-b;
}

.vtr-19__cbody {
  margin: 0;
  font-size: 0.78rem;
  line-height: 1.5;
  color: var(--muted);
}

.vtr-19__cbtn {
  justify-self: start;
  padding: 0.35rem 0.7rem;
  border: 1px solid var(--accent);
  color: var(--accent);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.vtr-19__cbtn--named {
  view-transition-name: vtr-19-btn-b;
}

.vtr-19__btn {
  justify-self: start;
  min-height: 44px;
  padding: 0 1rem;
  border: 1px solid var(--line);
  background: transparent;
  color: var(--ink);
  font-family: var(--font-display);
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  cursor: pointer;
}

.vtr-19__btn--go {
  border-color: var(--accent);
  background: var(--accent-soft);
  color: var(--accent);
}

.vtr-19__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.vtr-19__foot {
  margin: 0;
  font-size: 0.8rem;
  line-height: 1.55;
  color: var(--muted);
  max-width: 42rem;
}

::view-transition-group(vtr-19-card-a),
::view-transition-group(vtr-19-card-b) {
  animation-duration: 800ms;
  animation-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

::view-transition-group(vtr-19-title-b),
::view-transition-group(vtr-19-btn-b) {
  animation-duration: 800ms;
  animation-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(vtr-19-card-a),
    ::view-transition-group(vtr-19-card-b),
    ::view-transition-group(vtr-19-title-b),
    ::view-transition-group(vtr-19-btn-b) {
    animation-duration: 1ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-19 {
  position: relative;
}

.vtr-19__theme {
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

.vtr-19__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-19__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-19__themeopt {
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

.vtr-19__themeopt:hover {
  opacity: 0.85;
}

.vtr-19__themeinput:checked + .vtr-19__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-19__themeinput:focus-visible + .vtr-19__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-19:has(#vtr-19-theme-light:checked) {
  --bg: #f0f7f5;
  --surface: #ffffff;
  --surface-2: #e4f0ed;
  --line: #bdd8d3;
  --ink: #06231f;
  --muted: #47635e;
  --accent: #a16207;
  --accent-soft: #fdf3d7;
}

.vtr-19:has(#vtr-19-theme-dark:checked) {
  --bg: #07211f;
  --surface: #0c2c29;
  --surface-2: #103a36;
  --line: #1c4f49;
  --ink: #eafaf6;
  --muted: #86b3ac;
  --accent: #fbbf24;
  --accent-soft: #2a2c14;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.vtr-19');
  if (!root || root.dataset.vtr19) return;
  root.dataset.vtr19 = 'on';
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let busy = false;
  root.addEventListener('click', async (e) => {
    const btn = e.target.closest('[data-vtr19-toggle]');
    if (!btn || busy) return;
    const card = root.querySelector('#vtr-19-card-' + btn.dataset.vtr19Toggle);
    const flip = () => { card.dataset.big = card.dataset.big === 'true' ? 'false' : 'true'; };
    if (!document.startViewTransition || reduce.matches) { flip(); return; }
    busy = true;
    try { await document.startViewTransition(flip).finished; } finally { busy = false; }
  });
})();
```
