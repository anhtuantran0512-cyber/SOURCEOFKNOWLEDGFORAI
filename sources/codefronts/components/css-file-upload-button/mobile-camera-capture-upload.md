---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/mobile-camera-capture-upload/"
title: "Mobile Camera Capture Upload"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "On a phone, <input type=\"file\" accept=\"image/*\" capture=\"environment\"> opens the rear camera directly, skipping the picker entirely."
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Mobile Camera Capture Upload
Source: https://codefronts.com/components/css-file-upload-button/mobile-camera-capture-upload/

On a phone, <input type="file" accept="image/*" capture="environment"> opens the rear camera directly, skipping the picker entirely. This is the two-door pattern that gets it right: a primary camera trigger, a secondary library trigger, both real file inputs, both with 56px targets, and a layout that respects env(safe-area-inset-bottom) so the buttons clear the home indicator.
## HTML
```html
<div class="fu-18">
  <button class="fu-18__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-18__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-18__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <section class="fu-18__sheet" aria-labelledby="fu-18-h">
    <header class="fu-18__head">
      <span class="fu-18__step">Verification <span aria-hidden="true">·</span> 2 of 3</span>
      <h2 class="fu-18__h" id="fu-18-h">Photograph your ID</h2>
      <p class="fu-18__sub">All four corners visible, no glare.</p>
    </header>

    <div class="fu-18__frame">
      <img class="fu-18__shot" id="fu-18-shot" alt="" hidden>
      <span class="fu-18__guide" aria-hidden="true"><i></i><i></i><i></i><i></i></span>
      <span class="fu-18__idle" id="fu-18-idle">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 8.4h3.1l1.4-2h6l1.4 2h3.1v10.2h-15z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><circle cx="12" cy="13.1" r="3.2" stroke="currentColor" stroke-width="1.5"/></svg>
        <span>Camera preview appears here</span>
      </span>
    </div>

    <div class="fu-18__bar">
      <input class="fu-18__input" id="fu-18-cam" type="file" accept="image/*" capture="environment">
      <label class="fu-18__cam" for="fu-18-cam">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4.4" fill="currentColor"/></svg>
        Take photo
      </label>

      <input class="fu-18__input" id="fu-18-lib" type="file" accept="image/*">
      <label class="fu-18__lib" for="fu-18-lib">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="3.5" y="5.5" width="17" height="13" rx="2.2" stroke="currentColor" stroke-width="1.7"/><path d="m4.6 16.6 4.3-4.2 3.1 3 2.8-2.6 4.2 4" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
        Choose from library
      </label>

      <button class="fu-18__next" id="fu-18-next" type="button" disabled>Use this photo</button>
    </div>

    <p class="fu-18__status" id="fu-18-status" role="status" aria-live="polite"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Geist+Mono:wght@400;500&display=swap');

.fu-18 {
  --bg: #0c0d10;
  --surface: #15171c;
  --raise: #1d2026;
  --ink: #f3f4f7;
  --muted: #8b92a1;
  --line: #272b33;
  --acc: #c8ff4d;
  --acc-ink: #13180a;
  --sans: "Plus Jakarta Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1rem,4vw,3rem);
  background: radial-gradient(60% 40% at 50% 100%, color-mix(in oklab,var(--acc) 12%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.fu-18,
.fu-18 *,
.fu-18 *::before,
.fu-18 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .fu-18 {
    --acc: oklch(92% .19 118);
  }
}

.fu-18__sheet {
  inline-size: min(23rem,100%);
  display: grid;
  gap: 1rem;
  padding: 1.25rem 1.25rem max(1.25rem, env(safe-area-inset-bottom));
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.75rem;
  box-shadow: 0 40px 90px -60px #000;
}

.fu-18__head {
  display: grid;
  gap: .25rem;
}

.fu-18__step {
  font-family: var(--mono);
  font-size: .625rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--acc);
}

.fu-18__h {
  margin: .1rem 0 0;
  font-size: 1.4rem;
  font-weight: 800;
  letter-spacing: -.035em;
  line-height: 1.1;
}

.fu-18__sub {
  margin: 0;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

.fu-18__frame {
  position: relative;
  display: grid;
  place-items: center;
  aspect-ratio: 1.586;
  overflow: hidden;
  border-radius: 1.1rem;
  background: #000;
  border: 1px solid var(--line);
}

.fu-18__shot {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
}

.fu-18__shot[hidden] {
  display: none;
}

.fu-18__guide {
  position: absolute;
  inset: .75rem;
  pointer-events: none;
}

.fu-18__guide i {
  position: absolute;
  inline-size: 1.5rem;
  block-size: 1.5rem;
  border: 2px solid color-mix(in oklab,var(--acc) 75%,transparent);
}

.fu-18__guide i:nth-child(1) {
  inset-block-start: 0;
  inset-inline-start: 0;
  border-inline-end: 0;
  border-block-end: 0;
  border-start-start-radius: .5rem;
}

.fu-18__guide i:nth-child(2) {
  inset-block-start: 0;
  inset-inline-end: 0;
  border-inline-start: 0;
  border-block-end: 0;
  border-start-end-radius: .5rem;
}

.fu-18__guide i:nth-child(3) {
  inset-block-end: 0;
  inset-inline-start: 0;
  border-inline-end: 0;
  border-block-start: 0;
  border-end-start-radius: .5rem;
}

.fu-18__guide i:nth-child(4) {
  inset-block-end: 0;
  inset-inline-end: 0;
  border-inline-start: 0;
  border-block-start: 0;
  border-end-end-radius: .5rem;
}

.fu-18__idle {
  display: grid;
  justify-items: center;
  gap: .4rem;
  color: var(--muted);
  text-align: center;
  font-family: var(--mono);
  font-size: .625rem;
  padding: 1rem;
}

.fu-18__idle[hidden] {
  display: none;
}

.fu-18__idle svg {
  inline-size: 2rem;
  block-size: 2rem;
}

.fu-18__bar {
  display: grid;
  gap: .5rem;
}

.fu-18__input {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: 0;
  border: 0;
  overflow: hidden;
  opacity: 0;
  clip: rect(0 0 0 0);
  clip-path: inset(50%);
  white-space: nowrap;
}

.fu-18__cam,
.fu-18__lib,
.fu-18__next {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: .55rem;
  cursor: pointer;
  min-block-size: 3.5rem;
  padding: .85rem 1.2rem;
  border-radius: 1rem;
  font-family: var(--sans);
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: -.01em;
  transition: filter .2s ease, transform .2s cubic-bezier(.16,1,.3,1), background .2s ease, border-color .2s ease, opacity .2s ease;
}

.fu-18__cam {
  background: var(--acc);
  color: var(--acc-ink);
  border: 0;
}

.fu-18__cam svg {
  inline-size: 1.35rem;
  block-size: 1.35rem;
}

.fu-18__cam:hover {
  filter: brightness(1.05);
  transform: translateY(-1px);
}

.fu-18__cam:active {
  transform: scale(.985);
}

.fu-18__lib {
  background: var(--raise);
  color: var(--ink);
  border: 1px solid var(--line);
  font-size: .9375rem;
  font-weight: 600;
}

.fu-18__lib svg {
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-18__lib:hover {
  border-color: var(--muted);
}

.fu-18__next {
  background: transparent;
  color: var(--ink);
  border: 1px solid var(--acc);
  font-size: .9375rem;
}

.fu-18__next:disabled {
  opacity: .35;
  cursor: not-allowed;
}

.fu-18__next:hover:not(:disabled) {
  background: color-mix(in oklab,var(--acc) 14%,transparent);
}

.fu-18__input:focus-visible + label {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.fu-18__next:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.fu-18__status {
  margin: 0;
  min-block-size: 1rem;
  font-family: var(--mono);
  font-size: .625rem;
  color: var(--muted);
  text-align: center;
}

@media (pointer: coarse) {
  .fu-18__cam,
    .fu-18__lib,
    .fu-18__next {
    min-block-size: 3.75rem;
  }
}

@media (prefers-color-scheme: light) {
  .fu-18:not([data-theme="dark"]) {
    --bg: #f3f4f6;
    --surface: #ffffff;
    --raise: #f5f6f8;
    --ink: #0d0f13;
    --muted: #5c6373;
    --line: #e4e6ec;
    --acc: #4b7f00;
    --acc-ink: #ffffff;
  }
}

.fu-18[data-theme="light"] {
  --bg: #f3f4f6;
  --surface: #ffffff;
  --raise: #f5f6f8;
  --ink: #0d0f13;
  --muted: #5c6373;
  --line: #e4e6ec;
  --acc: #4b7f00;
  --acc-ink: #ffffff;
}

@media (prefers-reduced-motion: reduce) {
  .fu-18 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fu-18__sheet,
    .fu-18__frame,
    .fu-18__lib,
    .fu-18__next {
    border: 1px solid CanvasText;
  }

  .fu-18__cam {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }
}
/* ── in-demo theme toggle ── */

.fu-18 {
  position: relative;
}

.fu-18__theme {
  position: absolute;
  inset-block-start: clamp(.75rem,2.5vw,1.4rem);
  inset-inline-end: clamp(.75rem,2.5vw,1.4rem);
  z-index: 20;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab,currentColor 30%,transparent);
  background: color-mix(in oklab,currentColor 12%,transparent);
  color: inherit;
  transition: background .25s ease, transform .25s cubic-bezier(.16,1,.3,1), border-color .25s ease;
}

.fu-18__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-18__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-18__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-18__sun {
  display: none;
}

.fu-18__theme[aria-pressed="true"] .fu-18__sun {
  display: block;
}

.fu-18__theme[aria-pressed="true"] .fu-18__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-18__theme {
    transition: none;
  }

  .fu-18__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-18__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.fu-18');
  if (!root) return;
  const cam = root.querySelector('#fu-18-cam');
  const lib = root.querySelector('#fu-18-lib');
  const shot = root.querySelector('#fu-18-shot');
  const idle = root.querySelector('#fu-18-idle');
  const next = root.querySelector('#fu-18-next');
  const status = root.querySelector('#fu-18-status');
  let url = null;

  const show = (file, source) => {
    if (!file || !file.type.startsWith('image/')) { status.textContent = 'That file is not an image'; return; }
    if (url) URL.revokeObjectURL(url);
    url = URL.createObjectURL(file);
    shot.src = url; shot.alt = 'Photo of your ID document'; shot.hidden = false;
    idle.hidden = true; next.disabled = false;
    status.textContent = source + ' captured — check all four corners are visible';
  };

  cam.addEventListener('change', () => show(cam.files[0], 'Photo'));
  lib.addEventListener('change', () => show(lib.files[0], 'Library image'));

  next.addEventListener('click', () => {                 // simulated submit
    next.disabled = true;
    status.textContent = 'Checking image quality…';
    setTimeout(() => { status.textContent = 'Accepted — continue to step 3'; }, 1400);
  });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-18');
  const btn = root && root.querySelector('.fu-18__theme');
  if (!btn) return;
  const isDark = () => (root.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')) === 'dark';
  const sync = () => {
    btn.setAttribute('aria-pressed', String(isDark()));
    btn.setAttribute('aria-label', isDark() ? 'Switch to light theme' : 'Switch to dark theme');
  };
  btn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; sync(); });
  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (!root.dataset.theme) sync(); });
  sync();
})();
```
