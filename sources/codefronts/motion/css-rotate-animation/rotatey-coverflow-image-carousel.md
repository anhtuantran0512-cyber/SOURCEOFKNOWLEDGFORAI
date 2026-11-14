---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/rotatey-coverflow-image-carousel/"
title: "RotateY Coverflow Image Carousel"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "A cover-flow rail where the angle is the point: each item's rotateY, translateZ and scale are derived from how far it sits from the active index, so the…"
has_js: "true"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: RotateY Coverflow Image Carousel
Source: https://codefronts.com/motion/css-rotate-animation/rotatey-coverflow-image-carousel/

A cover-flow rail where the angle is the point: each item's rotateY, translateZ and scale are derived from how far it sits from the active index, so the falloff is one formula rather than a pile of per-slide rules. About twenty lines of JavaScript track the index and write a custom property — every transform is computed in CSS.
## HTML
```html
<section class="rot-07" aria-labelledby="rot-07-h">
  <fieldset class="rot-07__theme">
    <legend class="rot-07__themelegend">Theme</legend>
    <input class="rot-07__themeinput" type="radio" name="rot-07-theme" id="rot-07-theme-auto" checked>
    <label class="rot-07__themeopt" for="rot-07-theme-auto">Auto</label>
    <input class="rot-07__themeinput" type="radio" name="rot-07-theme" id="rot-07-theme-light">
    <label class="rot-07__themeopt" for="rot-07-theme-light">Light</label>
    <input class="rot-07__themeinput" type="radio" name="rot-07-theme" id="rot-07-theme-dark">
    <label class="rot-07__themeopt" for="rot-07-theme-dark">Dark</label>
  </fieldset>

  <div class="rot-07__stage">
    <header class="rot-07__head">
      <p class="rot-07__eyebrow">Basalt Recordings · Catalogue</p>
      <h2 class="rot-07__h" id="rot-07-h">The angle is the interface</h2>
      <p class="rot-07__sub">Every cover derives its rotation, depth and scale from one number: how far its index sits from the active one.</p>
    </header>

    <div class="rot-07__viewport">
      <div class="rot-07__rail" id="rot-07-rail" style="--rot-07-active: 2" role="listbox" aria-label="Catalogue covers" tabindex="0">
        <div class="rot-07__item" style="--i: 0" role="option" aria-selected="false">
          <div class="rot-07__cover rot-07__cover--a" aria-hidden="true"><span class="rot-07__grooves"></span></div>
          <p class="rot-07__title">Longwave</p>
          <p class="rot-07__by">Priya Sharma</p>
        </div>
        <div class="rot-07__item" style="--i: 1" role="option" aria-selected="false">
          <div class="rot-07__cover rot-07__cover--b" aria-hidden="true"><span class="rot-07__grooves"></span></div>
          <p class="rot-07__title">Dry Season</p>
          <p class="rot-07__by">Talon Quartet</p>
        </div>
        <div class="rot-07__item" style="--i: 2" role="option" aria-selected="true">
          <div class="rot-07__cover rot-07__cover--c" aria-hidden="true"><span class="rot-07__grooves"></span></div>
          <p class="rot-07__title">Meridian Line</p>
          <p class="rot-07__by">Jordan Lee</p>
        </div>
        <div class="rot-07__item" style="--i: 3" role="option" aria-selected="false">
          <div class="rot-07__cover rot-07__cover--d" aria-hidden="true"><span class="rot-07__grooves"></span></div>
          <p class="rot-07__title">Ferrous</p>
          <p class="rot-07__by">Sable Union</p>
        </div>
        <div class="rot-07__item" style="--i: 4" role="option" aria-selected="false">
          <div class="rot-07__cover rot-07__cover--e" aria-hidden="true"><span class="rot-07__grooves"></span></div>
          <p class="rot-07__title">Night Ferry</p>
          <p class="rot-07__by">Alex Chen</p>
        </div>
      </div>
    </div>

    <div class="rot-07__controls">
      <button class="rot-07__btn" type="button" data-rot07="prev" aria-label="Previous cover">
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M14.5 5 8 12l6.5 7" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"></path></svg>
      </button>
      <output class="rot-07__status" id="rot-07-status" aria-live="polite">Meridian Line · Jordan Lee</output>
      <button class="rot-07__btn" type="button" data-rot07="next" aria-label="Next cover">
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M9.5 5 16 12l-6.5 7" fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"></path></svg>
      </button>
    </div>

    <p class="rot-07__fine">Arrow keys move the selection when the rail has focus; Home and End jump to the ends. The rotation is decoration — <span class="rot-07__code">aria-selected</span> and the live region carry the state.</p>
  </div>
</section>
```
## CSS
```css
.rot-07 {
  --page: #1a1712;
  --surface: #241f18;
  --ink: #f5ece0;
  --muted: #a5947e;
  --rule: #3a3226;
  --accent: #e0a33c;
  --card: clamp(7rem, 24vw, 10rem);
  --turn: 42deg;
  --depth: 120px;
  --gap-x: 0.8;
  --persp: 1100px;
  --font-display: Rockwell, "Bookman Old Style", "Roboto Slab", Georgia, serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(0 0 0)) {
  .rot-07 {
    --accent: oklch(0.78 0.14 78);
  }
}

.rot-07 *,
.rot-07 *::before,
.rot-07 *::after {
  box-sizing: border-box;
}

.rot-07__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.25rem, 3.5vw, 2rem);
  padding: clamp(1.25rem, 4vw, 3rem);
  padding-block-start: 5.25rem;
}

.rot-07__head {
  max-inline-size: 36rem;
  min-inline-size: 0;
  text-align: center;
}

.rot-07__eyebrow {
  margin: 0 0 0.6rem;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.rot-07__h {
  margin: 0 0 0.6rem;
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 5vw, 2.375rem);
  font-weight: 400;
  line-height: 1.12;
}

.rot-07__sub {
  margin: 0;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-07__code {
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.85em;
  color: var(--accent);
}

.rot-07__viewport {
  inline-size: 100%;
  display: grid;
  place-items: center;
  padding-block: 0.5rem;
  perspective: var(--persp);
  perspective-origin: 50% 45%;
}

.rot-07__rail {
  position: relative;
  inline-size: min(100%, 44rem);
  block-size: calc(var(--card) * 1.85);
  transform-style: preserve-3d;
  outline: none;
}

.rot-07__rail:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 6px;
  border-radius: 0.5rem;
}

.rot-07__item {
  --off: calc(var(--i) - var(--rot-07-active));
  position: absolute;
  inset-block-start: 0;
  inset-inline-start: 50%;
  inline-size: var(--card);
  display: grid;
  gap: 0.4rem;
  justify-items: center;
  margin-inline-start: calc(var(--card) / -2);
  transform: translateX(calc(var(--off) * var(--gap-x) * var(--card))) translateZ(calc(max(var(--off), var(--off) * -1) * var(--depth) * -1)) rotateY(calc(clamp(-1, var(--off), 1) * var(--turn) * -1)) scale(calc(1 - max(var(--off), var(--off) * -1) * 0.06));
  transition: transform 420ms cubic-bezier(0.25, 0.8, 0.3, 1), opacity 420ms linear;
  opacity: calc(1 - max(var(--off), var(--off) * -1) * 0.18);
  z-index: calc(10 - max(var(--off), var(--off) * -1));
}

.rot-07__cover {
  position: relative;
  inline-size: 100%;
  aspect-ratio: 1;
  border: 1px solid var(--rule);
  border-radius: 0.25rem;
  box-shadow: 0 22px 40px -26px rgba(0, 0, 0, 0.9);
  overflow: hidden;
}

.rot-07__cover--a {
  background: linear-gradient(145deg, #2f5d63, #16333a);
}

.rot-07__cover--b {
  background: linear-gradient(145deg, #a3562c, #5c2b16);
}

.rot-07__cover--c {
  background: linear-gradient(145deg, #e0a33c, #8a5c12);
}

.rot-07__cover--d {
  background: linear-gradient(145deg, #55585f, #24262b);
}

.rot-07__cover--e {
  background: linear-gradient(145deg, #3d4a86, #1a1f45);
}

.rot-07__grooves {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(90deg, rgba(255, 255, 255, 0.09) 0 1px, transparent 1px 9px);
}

.rot-07__title {
  margin: 0.15rem 0 0;
  font-family: var(--font-display);
  font-size: 0.9375rem;
  text-align: center;
  min-inline-size: 0;
}

.rot-07__by {
  margin: 0;
  font-size: 0.75rem;
  color: var(--muted);
  text-align: center;
  min-inline-size: 0;
}

.rot-07__item[aria-selected="true"] .rot-07__title {
  color: var(--accent);
}

.rot-07__controls {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
  justify-content: center;
}

.rot-07__btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 1px solid var(--rule);
  border-radius: 50%;
  background: var(--surface);
  color: var(--ink);
  cursor: pointer;
}

.rot-07__btn:hover {
  border-color: var(--accent);
  color: var(--accent);
}

.rot-07__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.rot-07__status {
  min-inline-size: 12rem;
  text-align: center;
  font-family: var(--font-display);
  font-size: 0.875rem;
  color: var(--muted);
}

.rot-07__fine {
  inline-size: min(100%, 38rem);
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.65;
  text-align: center;
  color: var(--muted);
  text-wrap: pretty;
}

@media (max-width: 30rem) {
  .rot-07 {
    --card: clamp(3.75rem, 17vw, 7rem);
    --gap-x: 0.5;
    --depth: 80px;
    --turn: 34deg;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rot-07__item {
    transition: none;
  }
}

.rot-07__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 20;
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

.rot-07__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-07__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-07__themeopt {
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

.rot-07__themeopt:hover {
  opacity: 0.85;
}

.rot-07__themeinput:checked + .rot-07__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-07__themeinput:focus-visible + .rot-07__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .rot-07__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-07__themeinput:checked + .rot-07__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: light) {
  .rot-07:not(:has(#rot-07-theme-dark:checked)) {
    --page: #f7f3ec;
    --surface: #ffffff;
    --ink: #241d14;
    --muted: #776853;
    --rule: #e0d6c6;
    --accent: #a86a10;
  }

  .rot-07:not(:has(#rot-07-theme-dark:checked)) .rot-07__cover {
    box-shadow: 0 22px 40px -28px rgba(60, 45, 25, 0.55);
  }
}

@media (prefers-color-scheme: dark) {
  .rot-07:has(#rot-07-theme-light:checked) {
    --page: #f7f3ec;
    --surface: #ffffff;
    --ink: #241d14;
    --muted: #776853;
    --rule: #e0d6c6;
    --accent: #a86a10;
  }
}

[data-theme="light"] .rot-07:not(:has(#rot-07-theme-dark:checked)) {
  --page: #f7f3ec;
  --surface: #ffffff;
  --ink: #241d14;
  --muted: #776853;
  --rule: #e0d6c6;
  --accent: #a86a10;
}

.rot-07:has(#rot-07-theme-light:checked) {
  --page: #f7f3ec;
  --surface: #ffffff;
  --ink: #241d14;
  --muted: #776853;
  --rule: #e0d6c6;
  --accent: #a86a10;
}

.rot-07:has(#rot-07-theme-light:checked) .rot-07__cover {
  box-shadow: 0 22px 40px -28px rgba(60, 45, 25, 0.55);
}

.rot-07:has(#rot-07-theme-dark:checked) {
  --page: #1a1712;
  --surface: #241f18;
  --ink: #f5ece0;
  --muted: #a5947e;
  --rule: #3a3226;
  --accent: #e0a33c;
}

.rot-07:has(#rot-07-theme-dark:checked) .rot-07__cover {
  box-shadow: 0 22px 40px -26px rgba(0, 0, 0, 0.9);
}
/* Site-theme bridge: the per-demo page stamps [data-theme] on the iframe
   root. Without these rules a dark-by-default demo followed the OS instead
   of the site when the visitor was on OS-light + site-dark. Guarded by the
   light toggle so the in-demo switch still wins. */

[data-theme="dark"] .rot-07:not(:has(#rot-07-theme-light:checked)) {
  --page: #1a1712;
  --surface: #241f18;
  --ink: #f5ece0;
  --muted: #a5947e;
  --rule: #3a3226;
  --accent: #e0a33c;
}

[data-theme="dark"] .rot-07:not(:has(#rot-07-theme-light:checked)) .rot-07__cover {
  box-shadow: 0 22px 40px -26px rgba(0, 0, 0, 0.9);
}
```

## JavaScript
```js
(() => {
  const rail = document.querySelector('.rot-07__rail');
  if (!rail || rail.dataset.rot07) return;
  rail.dataset.rot07 = '1';
  const items = [...rail.querySelectorAll('.rot-07__item')];
  const status = document.querySelector('.rot-07__status');
  let active = Number(rail.style.getPropertyValue('--rot-07-active')) || 0;
  const show = (next) => {
    active = Math.min(items.length - 1, Math.max(0, next));
    rail.style.setProperty('--rot-07-active', String(active));
    items.forEach((el, i) => el.setAttribute('aria-selected', i === active ? 'true' : 'false'));
    const pick = items[active];
    status.textContent = pick.querySelector('.rot-07__title').textContent + ' · ' + pick.querySelector('.rot-07__by').textContent;
  };
  document.querySelectorAll('[data-rot07]').forEach((btn) => {
    btn.addEventListener('click', () => show(active + (btn.dataset.rot07 === 'next' ? 1 : -1)));
  });
  items.forEach((el, i) => el.addEventListener('click', () => show(i)));
  rail.addEventListener('keydown', (e) => {
    const map = { ArrowRight: active + 1, ArrowLeft: active - 1, Home: 0, End: items.length - 1 };
    if (!(e.key in map)) return;
    e.preventDefault();
    show(map[e.key]);
  });
  show(active);
})();
```
