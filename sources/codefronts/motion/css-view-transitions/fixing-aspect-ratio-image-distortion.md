---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/fixing-aspect-ratio-image-distortion/"
title: "Fixing Aspect Ratio Image Distortion"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "The single most-hit visual bug in the API."
has_js: "true"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fixing Aspect Ratio Image Distortion
Source: https://codefronts.com/motion/css-view-transitions/fixing-aspect-ratio-image-distortion/

The single most-hit visual bug in the API. When an element's aspect ratio changes during a morph, the default sizing of the captured old and new images stretches them, producing a visible squash-and-stretch. This shows the broken version and the fixed version side by side, with both available fixes: object-fit on the pseudo-elements, and a width and height override on the image pair.
## HTML
```html
<section class="vtr-18" aria-labelledby="vtr-18-heading">
  <fieldset class="vtr-18__theme">
    <legend class="vtr-18__themelegend">Theme</legend>
    <input class="vtr-18__themeinput" type="radio" name="vtr-18-theme" id="vtr-18-theme-auto" checked>
    <label class="vtr-18__themeopt" for="vtr-18-theme-auto">Auto</label>
    <input class="vtr-18__themeinput" type="radio" name="vtr-18-theme" id="vtr-18-theme-light">
    <label class="vtr-18__themeopt" for="vtr-18-theme-light">Light</label>
    <input class="vtr-18__themeinput" type="radio" name="vtr-18-theme" id="vtr-18-theme-dark">
    <label class="vtr-18__themeopt" for="vtr-18-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-18__stage">
    <header class="vtr-18__head">
      <p class="vtr-18__kicker">The most-hit visual bug</p>
      <h2 class="vtr-18__heading" id="vtr-18-heading">Square to 21:9, stretched and fixed</h2>
      <p class="vtr-18__sub">Same morph, same duration, same artwork. The right-hand panel sets <code>object-fit</code> on both captured snapshots.</p>
    </header>

    <div class="vtr-18__pair">
      <article class="vtr-18__panel">
        <div class="vtr-18__plabel"><span class="vtr-18__tag vtr-18__tag--bad">Default</span><span>no object-fit on the pseudos</span></div>
        <div class="vtr-18__holder">
          <span class="vtr-18__art vtr-18__art--bad" id="vtr-18-bad" data-wide="false"></span>
        </div>
        <button class="vtr-18__btn" type="button" data-vtr18-toggle="bad">Toggle ratio</button>
        <p class="vtr-18__pnote">The old snapshot keeps its square ratio while the box widens, so the artwork is pulled sideways mid-flight.</p>
      </article>

      <article class="vtr-18__panel vtr-18__panel--fixed">
        <div class="vtr-18__plabel"><span class="vtr-18__tag vtr-18__tag--good">Fixed</span><span>object-fit: cover on old and new</span></div>
        <div class="vtr-18__holder">
          <span class="vtr-18__art vtr-18__art--good" id="vtr-18-good" data-wide="false"></span>
        </div>
        <button class="vtr-18__btn vtr-18__btn--go" type="button" data-vtr18-toggle="good">Toggle ratio</button>
        <p class="vtr-18__pnote">Each snapshot fills the animating box and crops instead of stretching, so the change reads as a camera move.</p>
      </article>
    </div>

    <div class="vtr-18__fixes">
      <div class="vtr-18__fix">
        <p class="vtr-18__ftitle">Fix one · object-fit on the pseudos</p>
        <pre class="vtr-18__code"><code>::view-transition-old(shot),
::view-transition-new(shot) { object-fit: cover; }</code></pre>
      </div>
      <div class="vtr-18__fix">
        <p class="vtr-18__ftitle">Fix two · size the image pair</p>
        <pre class="vtr-18__code"><code>::view-transition-image-pair(shot) { width: 100%; height: 100%; }
::view-transition-old(shot),
::view-transition-new(shot) { width: 100%; height: 100%; }</code></pre>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.vtr-18 {
  --bg: #ffffff;
  --surface: #fafafa;
  --line: #111827;
  --soft: #e5e7eb;
  --ink: #0b1220;
  --muted: #4b5563;
  --accent: #1d4ed8;
  --bad: #b91c1c;
  --good: #15803d;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  color-scheme: light dark;
}

.vtr-18 *,
.vtr-18 *::before,
.vtr-18 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-18 {
    --surface: oklch(98% 0 0);
    --soft: oklch(91% 0.004 250);
    --ink: oklch(17% 0.02 255);
    --muted: oklch(45% 0.02 255);
    --accent: oklch(50% 0.2 265);
  }
}

@media (prefers-color-scheme: dark) {
  .vtr-18 {
    --bg: #0b0d10;
    --surface: #13161a;
    --line: #e5e7eb;
    --soft: #262b31;
    --ink: #f3f5f8;
    --muted: #a1abb8;
    --accent: #7ea2ff;
    --bad: #f87171;
    --good: #4ade80;
  }
}

.vtr-18[data-theme="light"] {
  --bg: #ffffff;
  --surface: #fafafa;
  --line: #111827;
  --soft: #e5e7eb;
  --ink: #0b1220;
  --muted: #4b5563;
  --accent: #1d4ed8;
  --bad: #b91c1c;
  --good: #15803d;
}

.vtr-18[data-theme="dark"] {
  --bg: #0b0d10;
  --surface: #13161a;
  --line: #e5e7eb;
  --soft: #262b31;
  --ink: #f3f5f8;
  --muted: #a1abb8;
  --accent: #7ea2ff;
  --bad: #f87171;
  --good: #4ade80;
}

.vtr-18__stage {
  max-width: 62rem;
  margin: 0 auto;
  padding: clamp(1.5rem, 4vw, 3rem) clamp(1rem, 4vw, 2.25rem);
  display: grid;
  gap: 1.5rem;
}

.vtr-18__kicker {
  margin: 0 0 0.4rem;
  font-size: 0.68rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-18__heading {
  margin: 0;
  font-size: clamp(1.4rem, 4.4vw, 2rem);
  font-weight: 700;
  letter-spacing: -0.025em;
  text-transform: uppercase;
}

.vtr-18__sub {
  margin: 0.5rem 0 0;
  font-size: 0.9rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 40rem;
}

.vtr-18__sub code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.82rem;
}

.vtr-18__pair {
  display: grid;
  gap: 1.25rem;
  grid-template-columns: 1fr;
}

@media (min-width: 54rem) {
  .vtr-18__pair {
    grid-template-columns: 1fr 1fr;
  }
}

.vtr-18__panel {
  border: 2px solid var(--line);
  background: var(--surface);
  box-shadow: 6px 6px 0 0 var(--soft);
  padding: 0.85rem;
  display: grid;
  gap: 0.7rem;
  align-content: start;
  min-inline-size: 0;
}

.vtr-18__plabel {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.68rem;
  color: var(--muted);
}

.vtr-18__tag {
  padding: 0.15rem 0.4rem;
  font-weight: 700;
  color: #ffffff;
  font-family: system-ui, sans-serif;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.vtr-18__tag--bad {
  background: var(--bad);
}

.vtr-18__tag--good {
  background: var(--good);
}

.vtr-18__holder {
  display: grid;
  place-items: center;
  min-height: 9rem;
}

.vtr-18__art {
  display: block;
  width: 8rem;
  aspect-ratio: 1;
  object-fit: cover;
  background: conic-gradient(from 200deg at 45% 55%, #f59e0b, #1d4ed8, #0f766e, #f59e0b);
}

.vtr-18__art[data-wide="true"] {
  width: 100%;
  aspect-ratio: 21 / 9;
}

.vtr-18__art--bad {
  view-transition-name: vtr-18-bad;
}

.vtr-18__art--good {
  view-transition-name: vtr-18-good;
}

.vtr-18__btn {
  justify-self: start;
  min-height: 44px;
  padding: 0 1rem;
  border: 2px solid var(--line);
  background: transparent;
  color: var(--ink);
  font-size: 0.8rem;
  font-weight: 700;
  cursor: pointer;
}

.vtr-18__btn--go {
  background: var(--line);
  color: var(--bg);
}

.vtr-18__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.vtr-18__pnote {
  margin: 0;
  font-size: 0.78rem;
  line-height: 1.55;
  color: var(--muted);
}

.vtr-18__fixes {
  display: grid;
  gap: 0.85rem;
  grid-template-columns: 1fr;
}

@media (min-width: 54rem) {
  .vtr-18__fixes {
    grid-template-columns: 1fr 1fr;
  }
}

.vtr-18__fix {
  display: grid;
  gap: 0.4rem;
  min-inline-size: 0;
}

.vtr-18__ftitle {
  margin: 0;
  font-size: 0.7rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-18__code {
  margin: 0;
  padding: 0.65rem 0.7rem;
  overflow-x: auto;
  border: 1px solid var(--soft);
  background: var(--surface);
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.68rem;
  line-height: 1.6;
}

::view-transition-group(vtr-18-bad),
::view-transition-group(vtr-18-good) {
  animation-duration: 700ms;
  animation-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
}

::view-transition-old(vtr-18-good),
::view-transition-new(vtr-18-good) {
  object-fit: cover;
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(vtr-18-bad),
    ::view-transition-group(vtr-18-good) {
    animation-duration: 1ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-18 {
  position: relative;
}

.vtr-18__theme {
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

.vtr-18__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-18__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-18__themeopt {
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

.vtr-18__themeopt:hover {
  opacity: 0.85;
}

.vtr-18__themeinput:checked + .vtr-18__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-18__themeinput:focus-visible + .vtr-18__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-18:has(#vtr-18-theme-light:checked) {
  --bg: #ffffff;
  --surface: #fafafa;
  --line: #111827;
  --soft: #e5e7eb;
  --ink: #0b1220;
  --muted: #4b5563;
  --accent: #1d4ed8;
  --bad: #b91c1c;
  --good: #15803d;
}

.vtr-18:has(#vtr-18-theme-dark:checked) {
  --bg: #0b0d10;
  --surface: #13161a;
  --line: #e5e7eb;
  --soft: #262b31;
  --ink: #f3f5f8;
  --muted: #a1abb8;
  --accent: #7ea2ff;
  --bad: #f87171;
  --good: #4ade80;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.vtr-18');
  if (!root || root.dataset.vtr18) return;
  root.dataset.vtr18 = 'on';
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let busy = false;
  root.addEventListener('click', async (e) => {
    const btn = e.target.closest('[data-vtr18-toggle]');
    if (!btn || busy) return;
    const art = root.querySelector('#vtr-18-' + btn.dataset.vtr18Toggle);
    const flip = () => { art.dataset.wide = art.dataset.wide === 'true' ? 'false' : 'true'; };
    if (!document.startViewTransition || reduce.matches) { flip(); return; }
    busy = true;
    try { await document.startViewTransition(flip).finished; } finally { busy = false; }
  });
})();
```
