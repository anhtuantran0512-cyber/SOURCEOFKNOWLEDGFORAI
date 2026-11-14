---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/avatar-upload-with-circular-preview/"
title: "Avatar Upload with Circular Preview"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "A profile photo control that behaves like the ones in real products: hover (or focus) reveals an edit scrim over a circular preview, a live zoom slider…"
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Avatar Upload with Circular Preview
Source: https://codefronts.com/components/css-file-upload-button/avatar-upload-with-circular-preview/

A profile photo control that behaves like the ones in real products: hover (or focus) reveals an edit scrim over a circular preview, a live zoom slider drives scale() on the image so users can frame their face, and a conic ring sweeps once when a new photo lands. The overlay is a <label>, so the entire circle is a legitimate click target and a keyboard-focusable control.
## HTML
```html
<div class="fu-11">
  <button class="fu-11__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-11__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-11__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <section class="fu-11__card" aria-labelledby="fu-11-h">
    <div class="fu-11__ring" id="fu-11-ring">
      <span class="fu-11__crop"><img class="fu-11__img" id="fu-11-img" src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=320&amp;h=320&amp;fit=crop&amp;crop=faces&amp;q=70&amp;auto=format" width="320" height="320" alt="Profile photo preview"></span>
      <input class="fu-11__input" id="fu-11-file" type="file" accept="image/*" aria-describedby="fu-11-hint">
      <label class="fu-11__scrim" for="fu-11-file">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 8.5h3l1.4-2h6.2l1.4 2h3v10h-15z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><circle cx="12" cy="13" r="3.1" stroke="currentColor" stroke-width="1.6"/></svg>
        <span class="fu-11__scrimText">Change</span>
      </label>
    </div>

    <div class="fu-11__body">
      <h2 class="fu-11__h" id="fu-11-h">Amara Osei</h2>
      <p class="fu-11__role">Principal designer <span aria-hidden="true">·</span> Bristol</p>
    </div>

    <div class="fu-11__zoom">
      <label class="fu-11__zoomLabel" for="fu-11-zoom">Zoom</label>
      <input class="fu-11__slider" id="fu-11-zoom" type="range" min="1" max="2" step=".01" value="1">
      <output class="fu-11__val" id="fu-11-val" for="fu-11-zoom">1.00×</output>
    </div>

    <p class="fu-11__hint" id="fu-11-hint">JPG, PNG or WEBP <span aria-hidden="true">·</span> square works best</p>
    <p class="fu-11__status" id="fu-11-status" role="status" aria-live="polite"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:opsz,[email protected],400;9..40,500;9..40,700&family=Geist+Mono:wght@400;500&display=swap');

@property --fu-11-sweep {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.fu-11 {
  --bg: #f6f4f1;
  --surface: #ffffff;
  --ink: #161513;
  --muted: #6b675f;
  --line: #e6e2db;
  --acc: #e0483a;
  --acc2: #1f6f5c;
  --ring-w: 4px;
  --zoom: 1;
  --sans: "DM Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(60% 45% at 50% 0%, color-mix(in oklab,var(--acc) 10%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

.fu-11,
.fu-11 *,
.fu-11 *::before,
.fu-11 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .fu-11 {
    --acc: oklch(60% .19 30);
    --acc2: oklch(45% .09 168);
  }
}

.fu-11__card {
  inline-size: min(21rem,100%);
  display: grid;
  justify-items: center;
  gap: .85rem;
  padding: clamp(1.5rem,5vw,2rem) 1.5rem 1.35rem;
  text-align: center;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.6rem;
  box-shadow: 0 30px 60px -45px rgba(22,21,19,.45);
}

.fu-11__ring {
  position: relative;
  inline-size: 8.5rem;
  block-size: 8.5rem;
  border-radius: 50%;
  isolation: isolate;
  padding: var(--ring-w);
  background: conic-gradient(from var(--fu-11-sweep), var(--acc), var(--acc2), var(--acc));
}

.fu-11__ring.is-new {
  animation: fu-11-sweep 1.1s cubic-bezier(.16,1,.3,1) 1;
}

@keyframes fu-11-sweep {
  from {
    --fu-11-sweep: 0deg;
  }

  to {
    --fu-11-sweep: 360deg;
  }
}
/* The zoom transform paints outside border-radius, and clip-path on the
   image itself would scale with it. The crop wrapper is the only element
   that can contain it: it fills the ring's padding box, never transforms,
   and clips with overflow — so the gradient ring stays visible. */

.fu-11__crop {
  display: block;
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
  overflow: hidden;
  isolation: isolate;
}

.fu-11__img {
  inline-size: 100%;
  block-size: 100%;
  border-radius: 50%;
  will-change: transform;
  object-fit: cover;
  display: block;
  background: var(--line);
  transform: scale(var(--zoom));
  transition: transform .12s linear;
  border: 3px solid var(--surface);
}

.fu-11__ring::after {
  content: "";
  position: absolute;
  inset: var(--ring-w);
  border-radius: 50%;
  overflow: hidden;
  pointer-events: none;
}

.fu-11__input {
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

.fu-11__scrim {
  position: absolute;
  inset: var(--ring-w);
  display: grid;
  place-content: center;
  justify-items: center;
  gap: .15rem;
  border-radius: 50%;
  cursor: pointer;
  opacity: 0;
  color: #fff;
  background: color-mix(in oklab,#000 62%,transparent);
  transition: opacity .28s ease;
}

.fu-11__scrim svg {
  inline-size: 1.5rem;
  block-size: 1.5rem;
}

.fu-11__scrimText {
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: .01em;
}

.fu-11__ring:hover .fu-11__scrim,
.fu-11__ring:focus-within .fu-11__scrim {
  opacity: 1;
}

.fu-11__input:focus-visible ~ .fu-11__scrim {
  outline: 2px solid var(--acc2);
  outline-offset: 3px;
}

.fu-11__body {
  display: grid;
  gap: .1rem;
}

.fu-11__h {
  margin: 0;
  font-size: 1.25rem;
  font-weight: 700;
  letter-spacing: -.025em;
}

.fu-11__role {
  margin: 0;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

.fu-11__zoom {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: .6rem;
  inline-size: 100%;
}

.fu-11__zoomLabel {
  font-family: var(--mono);
  font-size: .625rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.fu-11__slider {
  inline-size: 100%;
  block-size: 2.75rem;
  margin: 0;
  accent-color: var(--acc);
  cursor: pointer;
  background: transparent;
}

.fu-11__slider:focus-visible {
  outline: 2px solid var(--acc2);
  outline-offset: 2px;
  border-radius: .4rem;
}

.fu-11__val {
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.fu-11__hint {
  margin: 0;
  font-family: var(--mono);
  font-size: .625rem;
  color: var(--muted);
}

.fu-11__status {
  margin: 0;
  min-block-size: 1rem;
  font-family: var(--mono);
  font-size: .625rem;
  color: var(--acc2);
}

@media (prefers-color-scheme: dark) {
  .fu-11:not([data-theme="light"]) {
    --bg: #0d0c0b;
    --surface: #171614;
    --ink: #f4f2ee;
    --muted: #9b958a;
    --line: #282520;
    --acc: #ff6a58;
    --acc2: #4fd6ac;
  }
}

.fu-11[data-theme="dark"] {
  --bg: #0d0c0b;
  --surface: #171614;
  --ink: #f4f2ee;
  --muted: #9b958a;
  --line: #282520;
  --acc: #ff6a58;
  --acc2: #4fd6ac;
}

@media (prefers-reduced-motion: reduce) {
  .fu-11 * {
    animation: none !important;
    transition: none !important;
  }

  .fu-11__scrim {
    opacity: 1;
    background: color-mix(in oklab,#000 45%,transparent);
  }
}

@media (forced-colors: active) {
  .fu-11__card {
    border: 1px solid CanvasText;
  }

  .fu-11__scrim {
    background: Canvas;
    color: CanvasText;
    opacity: 1;
    border: 1px solid CanvasText;
  }
}
/* ── in-demo theme toggle ── */

.fu-11 {
  position: relative;
}

.fu-11__theme {
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

.fu-11__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-11__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-11__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-11__sun {
  display: none;
}

.fu-11__theme[aria-pressed="true"] .fu-11__sun {
  display: block;
}

.fu-11__theme[aria-pressed="true"] .fu-11__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-11__theme {
    transition: none;
  }

  .fu-11__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-11__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.fu-11');
  if (!root) return;
  const ring = root.querySelector('#fu-11-ring');
  const img = root.querySelector('#fu-11-img');
  const input = root.querySelector('#fu-11-file');
  const zoom = root.querySelector('#fu-11-zoom');
  const val = root.querySelector('#fu-11-val');
  const status = root.querySelector('#fu-11-status');
  let current = null;

  zoom.addEventListener('input', () => {
    root.style.setProperty('--zoom', zoom.value);
    val.textContent = Number(zoom.value).toFixed(2) + '×';
  });

  input.addEventListener('change', () => {
    const file = input.files && input.files[0];
    if (!file || !file.type.startsWith('image/')) return;
    if (current) URL.revokeObjectURL(current);
    current = URL.createObjectURL(file);
    img.src = current;
    img.alt = 'Profile photo preview';
    zoom.value = 1; root.style.setProperty('--zoom', 1); val.textContent = '1.00×';
    ring.classList.remove('is-new');
    void ring.offsetWidth;                    // force reflow so the sweep replays
    ring.classList.add('is-new');
    status.textContent = 'New profile photo selected — ' + file.name;
  });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-11');
  const btn = root && root.querySelector('.fu-11__theme');
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
