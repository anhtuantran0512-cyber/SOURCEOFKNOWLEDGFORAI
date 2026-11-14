---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/image-grid-to-lightbox-transition/"
title: "Image Grid to Lightbox Transition"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "A cropped square thumbnail expands into a full-bleed overlay."
has_js: "true"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Image Grid to Lightbox Transition
Source: https://codefronts.com/motion/css-view-transitions/image-grid-to-lightbox-transition/

A cropped square thumbnail expands into a full-bleed overlay. The interesting part is not the overlay, it is the aspect-ratio change: the browser morphs the element's box, not its contents, so a square-to-landscape jump distorts the captured image unless object-fit is set on both states. Demo 18 covers the full fix.
## HTML
```html
<section class="vtr-07" aria-labelledby="vtr-07-heading">
  <fieldset class="vtr-07__theme">
    <legend class="vtr-07__themelegend">Theme</legend>
    <input class="vtr-07__themeinput" type="radio" name="vtr-07-theme" id="vtr-07-theme-auto" checked>
    <label class="vtr-07__themeopt" for="vtr-07-theme-auto">Auto</label>
    <input class="vtr-07__themeinput" type="radio" name="vtr-07-theme" id="vtr-07-theme-light">
    <label class="vtr-07__themeopt" for="vtr-07-theme-light">Light</label>
    <input class="vtr-07__themeinput" type="radio" name="vtr-07-theme" id="vtr-07-theme-dark">
    <label class="vtr-07__themeopt" for="vtr-07-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-07__stage">
    <header class="vtr-07__head">
      <p class="vtr-07__kicker">Prism Archive · 06</p>
      <h2 class="vtr-07__heading" id="vtr-07-heading">Thumbnail to lightbox</h2>
      <p class="vtr-07__sub">The box is interpolated. The contents are a captured image, which is why the crop has to agree on both sides.</p>
    </header>

    <div class="vtr-07__pair">
      <ul class="vtr-07__grid" id="vtr-07-grid">
        <li><button class="vtr-07__tile" type="button" data-vtr07-open="1"><span class="vtr-07__art vtr-07__art--1"></span><span class="vtr-07__cap">Sable 01</span></button></li>
        <li><button class="vtr-07__tile" type="button" data-vtr07-open="2"><span class="vtr-07__art vtr-07__art--2"></span><span class="vtr-07__cap">Sable 02</span></button></li>
        <li><button class="vtr-07__tile" type="button" data-vtr07-open="3"><span class="vtr-07__art vtr-07__art--3"></span><span class="vtr-07__cap">Talon 07</span></button></li>
        <li><button class="vtr-07__tile" type="button" data-vtr07-open="4"><span class="vtr-07__art vtr-07__art--4"></span><span class="vtr-07__cap">Talon 09</span></button></li>
      </ul>

      <div class="vtr-07__overlay" id="vtr-07-overlay" hidden>
        <div class="vtr-07__frame">
          <span class="vtr-07__art vtr-07__art--1" id="vtr-07-shot"></span>
          <div class="vtr-07__bar">
            <p class="vtr-07__label" id="vtr-07-label">Sable 01</p>
            <button class="vtr-07__close" type="button" id="vtr-07-close">Close<span class="vtr-07__kbd">Esc</span></button>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.vtr-07 {
  --bg: #0d0d0d;
  --surface: #171717;
  --line: #2a2a2a;
  --ink: #f5f5f5;
  --muted: #9a9a9a;
  --accent: #ec4899;
  --scrim: rgba(8, 8, 8, 0.88);
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  color-scheme: dark light;
}

.vtr-07 *,
.vtr-07 *::before,
.vtr-07 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-07 {
    --bg: oklch(17% 0 0);
    --surface: oklch(22% 0 0);
    --line: oklch(30% 0 0);
    --ink: oklch(97% 0 0);
    --muted: oklch(68% 0 0);
    --accent: oklch(68% 0.21 350);
  }
}

@media (prefers-color-scheme: light) {
  .vtr-07 {
    --bg: #fafafa;
    --surface: #ffffff;
    --line: #e4e4e4;
    --ink: #111111;
    --muted: #6b6b6b;
    --accent: #db2777;
    --scrim: rgba(250, 250, 250, 0.94);
  }
}

.vtr-07[data-theme="light"] {
  --bg: #fafafa;
  --surface: #ffffff;
  --line: #e4e4e4;
  --ink: #111111;
  --muted: #6b6b6b;
  --accent: #db2777;
  --scrim: rgba(250, 250, 250, 0.94);
}

.vtr-07[data-theme="dark"] {
  --bg: #0d0d0d;
  --surface: #171717;
  --line: #2a2a2a;
  --ink: #f5f5f5;
  --muted: #9a9a9a;
  --accent: #ec4899;
  --scrim: rgba(8, 8, 8, 0.88);
}

.vtr-07__stage {
  max-width: 66rem;
  margin: 0 auto;
  padding: clamp(1.75rem, 5vw, 4rem) clamp(1rem, 4vw, 2.5rem);
  display: grid;
  gap: 2.25rem;
}

.vtr-07__kicker {
  margin: 0 0 0.7rem;
  font-size: 0.66rem;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-07__heading {
  margin: 0;
  font-size: clamp(1.5rem, 4.6vw, 2.2rem);
  font-weight: 500;
  letter-spacing: 0.02em;
  text-transform: uppercase;
}

.vtr-07__sub {
  margin: 0.7rem 0 0;
  font-size: 0.9rem;
  line-height: 1.6;
  color: var(--muted);
  max-width: 34rem;
}

.vtr-07__pair {
  position: relative;
  min-inline-size: 0;
}

.vtr-07__grid {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0.75rem;
  grid-template-columns: repeat(2, 1fr);
}

@media (min-width: 46rem) {
  .vtr-07__grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

.vtr-07__tile {
  display: grid;
  gap: 0.5rem;
  width: 100%;
  padding: 0;
  border: 0;
  background: none;
  cursor: pointer;
  color: inherit;
  min-inline-size: 0;
}

.vtr-07__tile:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 4px;
}

.vtr-07__art {
  display: block;
  width: 100%;
  aspect-ratio: 1;
  object-fit: cover;
  border-radius: 0.125rem;
}

.vtr-07__art--1 {
  background: conic-gradient(from 210deg at 60% 40%, #f472b6, #7c3aed, #0ea5e9, #f472b6);
}

.vtr-07__art--2 {
  background: conic-gradient(from 40deg at 30% 70%, #fbbf24, #ef4444, #1e293b, #fbbf24);
}

.vtr-07__art--3 {
  background: conic-gradient(from 120deg at 50% 50%, #10b981, #0f172a, #a3e635, #10b981);
}

.vtr-07__art--4 {
  background: conic-gradient(from 300deg at 70% 30%, #e2e8f0, #64748b, #0f172a, #e2e8f0);
}

.vtr-07__cap {
  font-size: 0.66rem;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: var(--muted);
  text-align: left;
}

.vtr-07__overlay {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  padding: clamp(0.5rem, 3vw, 2rem);
  background: var(--scrim);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
}

.vtr-07__overlay[hidden] {
  display: none;
}

.vtr-07__frame {
  width: 100%;
  max-width: 44rem;
  display: grid;
  gap: 0.6rem;
  min-inline-size: 0;
}

.vtr-07__frame .vtr-07__art {
  aspect-ratio: 16 / 9;
  border-radius: 0.25rem;
}

.vtr-07__bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.vtr-07__label {
  margin: 0;
  font-size: 0.68rem;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--muted);
  min-inline-size: 0;
}

.vtr-07__close {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  min-height: 44px;
  padding: 0 0.9rem;
  border: 1px solid var(--line);
  border-radius: 0.2rem;
  background: var(--surface);
  color: var(--ink);
  font-size: 0.72rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  cursor: pointer;
}

.vtr-07__close:hover {
  border-color: var(--accent);
  color: var(--accent);
}

.vtr-07__close:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.vtr-07__kbd {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.62rem;
  padding: 0.1rem 0.3rem;
  border: 1px solid var(--line);
  border-radius: 0.15rem;
  color: var(--muted);
}

::view-transition-group(vtr-07-shot) {
  animation-duration: 440ms;
  animation-timing-function: cubic-bezier(0.32, 0.72, 0, 1);
}

::view-transition-old(vtr-07-shot),
::view-transition-new(vtr-07-shot) {
  object-fit: cover;
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(vtr-07-shot) {
    animation-duration: 1ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-07 {
  position: relative;
}

.vtr-07__theme {
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

.vtr-07__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-07__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-07__themeopt {
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

.vtr-07__themeopt:hover {
  opacity: 0.85;
}

.vtr-07__themeinput:checked + .vtr-07__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-07__themeinput:focus-visible + .vtr-07__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-07:has(#vtr-07-theme-light:checked) {
  --bg: #fafafa;
  --surface: #ffffff;
  --line: #e4e4e4;
  --ink: #111111;
  --muted: #6b6b6b;
  --accent: #db2777;
  --scrim: rgba(250, 250, 250, 0.94);
}

.vtr-07:has(#vtr-07-theme-dark:checked) {
  --bg: #0d0d0d;
  --surface: #171717;
  --line: #2a2a2a;
  --ink: #f5f5f5;
  --muted: #9a9a9a;
  --accent: #ec4899;
  --scrim: rgba(8, 8, 8, 0.88);
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.vtr-07');
  if (!root || root.dataset.vtr07) return;
  root.dataset.vtr07 = 'on';
  const overlay = root.querySelector('#vtr-07-overlay'), shot = root.querySelector('#vtr-07-shot'), label = root.querySelector('#vtr-07-label');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let opener = null, busy = false;
  const name = (art, on) => [art, shot].forEach(el => { el.style.viewTransitionName = on ? 'vtr-07-shot' : ''; });
  const run = async (mutate, art) => {
    if (!document.startViewTransition || reduce.matches) { mutate(); return; }
    busy = true; name(art, true);
    try { await document.startViewTransition(mutate).finished; } finally { name(art, false); busy = false; }
  };
  root.addEventListener('click', async (e) => {
    const tile = e.target.closest('[data-vtr07-open]');
    if (busy || (!tile && !e.target.closest('#vtr-07-close') && e.target !== overlay)) return;
    if (tile) opener = tile;
    const art = opener.querySelector('.vtr-07__art');
    await run(() => {
      if (!tile) { overlay.hidden = true; return; }
      shot.className = art.className;
      label.textContent = tile.querySelector('.vtr-07__cap').textContent;
      overlay.hidden = false;
    }, art);
    (tile ? root.querySelector('#vtr-07-close') : opener).focus();
  });
  root.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !overlay.hidden) root.querySelector('#vtr-07-close').click(); });
})();
```
