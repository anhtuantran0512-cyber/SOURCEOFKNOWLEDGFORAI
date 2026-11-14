---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/image-upload-with-preview-thumbnail/"
title: "Image Upload with Preview Thumbnail"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "One image, one card, and everything you actually want to know before uploading: the thumbnail, the pixel dimensions read from naturalWidth/naturalHeight, the…"
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Image Upload with Preview Thumbnail
Source: https://codefronts.com/components/css-file-upload-button/image-upload-with-preview-thumbnail/

One image, one card, and everything you actually want to know before uploading: the thumbnail, the pixel dimensions read from naturalWidth/naturalHeight, the file weight, and a transparency-revealing checkerboard behind it so a PNG with an alpha channel is obvious at a glance. Replace and remove are separate affordances, because "choose a different one" and "clear this field" are different intents.
## HTML
```html
<div class="fu-10">
  <button class="fu-10__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-10__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-10__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <section class="fu-10__card" aria-labelledby="fu-10-h">
    <div class="fu-10__stage">
      <img class="fu-10__img" id="fu-10-img" alt="" hidden>
      <div class="fu-10__ph">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="3.2" y="4.8" width="17.6" height="14.4" rx="2.4" stroke="currentColor" stroke-width="1.6"/><circle cx="8.6" cy="10" r="1.5" fill="currentColor"/><path d="m4.4 17.4 4.6-4.5 3.3 3.2 3-2.8 4.3 4.1" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/></svg>
        <p>No image selected</p>
      </div>
    </div>

    <div class="fu-10__info">
      <h2 class="fu-10__h" id="fu-10-h">Cover image</h2>
      <p class="fu-10__name" id="fu-10-name">Recommended 1600 × 900, under 8 MB</p>
      <p class="fu-10__dims" id="fu-10-dims"></p>
    </div>

    <div class="fu-10__actions">
      <input class="fu-10__input" id="fu-10-file" type="file" accept="image/png,image/jpeg,image/webp,image/avif">
      <label class="fu-10__pick" for="fu-10-file" id="fu-10-picklabel">Choose image</label>
      <button class="fu-10__rm" id="fu-10-rm" type="button" hidden>Remove</button>
    </div>

    <p class="fu-10__status" id="fu-10-status" role="status" aria-live="polite"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fu-10 {
  --bg: #101216;
  --surface: #181b21;
  --ink: #f2f4f7;
  --muted: #8b93a1;
  --line: #282d36;
  --acc: #ffd84d;
  --acc-ink: #1a1500;
  --check: #22262e;
  --check-size: 16px;
  --sans: "Instrument Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(60% 40% at 80% 10%, color-mix(in oklab,var(--acc) 10%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.fu-10,
.fu-10 *,
.fu-10 *::before,
.fu-10 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .fu-10 {
    --acc: oklch(88% .16 96);
  }
}

.fu-10__card {
  inline-size: min(24rem,100%);
  display: grid;
  gap: .9rem;
  padding: 1rem;
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.4rem;
  box-shadow: 0 40px 80px -55px #000;
}

.fu-10__stage {
  position: relative;
  display: grid;
  place-items: center;
  aspect-ratio: 4/3;
  overflow: hidden;
  border-radius: 1rem;
  border: 1px solid var(--line);
  background-color: color-mix(in oklab,var(--ink) 4%,transparent);
  background-image: conic-gradient(rgba(0,0,0,0) 90deg, var(--check) 0 180deg, rgba(0,0,0,0) 0 270deg, var(--check) 0);
  background-size: var(--check-size) var(--check-size);
}

.fu-10__img {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  object-fit: contain;
  transition: opacity .35s ease;
}

.fu-10__img[hidden] {
  display: none;
}

@starting-style {
  .fu-10__img {
    opacity: 0;
  }
}

.fu-10__ph {
  display: grid;
  justify-items: center;
  gap: .5rem;
  color: var(--muted);
  text-align: center;
}

.fu-10__ph svg {
  inline-size: 2.25rem;
  block-size: 2.25rem;
  opacity: .7;
}

.fu-10__ph p {
  margin: 0;
  font-family: var(--mono);
  font-size: .75rem;
}

.fu-10__card:has(.fu-10__img:not([hidden])) .fu-10__ph {
  display: none;
}

.fu-10__info {
  display: grid;
  gap: .2rem;
}

.fu-10__h {
  margin: 0;
  font-size: 1.0625rem;
  font-weight: 700;
  letter-spacing: -.02em;
}

.fu-10__name {
  margin: 0;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.fu-10__dims {
  margin: 0;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--acc);
  font-variant-numeric: tabular-nums;
  min-block-size: 1rem;
}

.fu-10__actions {
  display: flex;
  gap: .5rem;
  align-items: center;
}

.fu-10__input {
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

.fu-10__pick {
  flex: 1;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  min-block-size: 2.85rem;
  padding: .6rem 1rem;
  border-radius: .8rem;
  background: var(--acc);
  color: var(--acc-ink);
  font-size: .9375rem;
  font-weight: 700;
  letter-spacing: -.01em;
  transition: filter .2s ease, transform .2s cubic-bezier(.16,1,.3,1);
}

.fu-10__pick:hover {
  filter: brightness(1.07);
  transform: translateY(-1px);
}

.fu-10__input:focus-visible + .fu-10__pick {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.fu-10__rm {
  min-block-size: 2.85rem;
  padding: .6rem 1rem;
  cursor: pointer;
  border-radius: .8rem;
  border: 1px solid var(--line);
  background: transparent;
  color: var(--muted);
  font-family: var(--sans);
  font-size: .875rem;
  font-weight: 600;
  transition: color .2s ease, border-color .2s ease, background .2s ease;
}

.fu-10__rm[hidden] {
  display: none;
}

.fu-10__rm:hover {
  color: var(--ink);
  border-color: var(--muted);
  background: color-mix(in oklab,var(--ink) 6%,transparent);
}

.fu-10__rm:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.fu-10__status {
  margin: 0;
  min-block-size: 1rem;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

@media (prefers-color-scheme: light) {
  .fu-10:not([data-theme="dark"]) {
    --bg: #f1f2f5;
    --surface: #ffffff;
    --ink: #0e1116;
    --muted: #5c6474;
    --line: #e3e6ec;
    --acc: #8a5cf6;
    --acc-ink: #ffffff;
    --check: #eceef3;
  }
}

.fu-10[data-theme="light"] {
  --bg: #f1f2f5;
  --surface: #ffffff;
  --ink: #0e1116;
  --muted: #5c6474;
  --line: #e3e6ec;
  --acc: #8a5cf6;
  --acc-ink: #ffffff;
  --check: #eceef3;
}

@media (prefers-reduced-motion: reduce) {
  .fu-10 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fu-10__card,
    .fu-10__stage,
    .fu-10__rm {
    border: 1px solid CanvasText;
  }

  .fu-10__pick {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }
}
/* ── in-demo theme toggle ── */

.fu-10 {
  position: relative;
}

.fu-10__theme {
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

.fu-10__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-10__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-10__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-10__sun {
  display: none;
}

.fu-10__theme[aria-pressed="true"] .fu-10__sun {
  display: block;
}

.fu-10__theme[aria-pressed="true"] .fu-10__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-10__theme {
    transition: none;
  }

  .fu-10__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-10__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.fu-10');
  if (!root) return;
  const input = root.querySelector('#fu-10-file');
  const img = root.querySelector('#fu-10-img');
  const nameEl = root.querySelector('#fu-10-name');
  const dims = root.querySelector('#fu-10-dims');
  const rm = root.querySelector('#fu-10-rm');
  const pick = root.querySelector('#fu-10-picklabel');
  const status = root.querySelector('#fu-10-status');

  const fmt = (n) => {
    const u = ['B','KB','MB']; let i = 0;
    while (n >= 1024 && i < u.length - 1) { n /= 1024; i++; }
    return new Intl.NumberFormat(undefined, { maximumFractionDigits: n < 10 && i ? 1 : 0 }).format(n) + ' ' + u[i];
  };

  input.addEventListener('change', () => {
    const file = input.files && input.files[0];
    if (!file) return;
    if (!file.type.startsWith('image/')) { status.textContent = 'That is not an image file'; input.value = ''; return; }
    const url = URL.createObjectURL(file);
    img.onload = () => {
      dims.textContent = img.naturalWidth + ' × ' + img.naturalHeight + ' px · ' + fmt(file.size);
      URL.revokeObjectURL(url);                 // safe: the bitmap is already decoded
    };
    img.src = url;
    img.alt = 'Preview of ' + file.name;
    img.hidden = false;
    nameEl.textContent = file.name;
    rm.hidden = false;
    pick.textContent = 'Replace image';
    status.textContent = file.name + ' ready to upload';
  });

  rm.addEventListener('click', () => {
    input.value = '';
    img.hidden = true; img.removeAttribute('src'); img.alt = '';
    nameEl.textContent = 'Recommended 1600 × 900, under 8 MB';
    dims.textContent = '';
    rm.hidden = true;
    pick.textContent = 'Choose image';
    status.textContent = 'Image removed';
    input.focus();
  });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-10');
  const btn = root && root.querySelector('.fu-10__theme');
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
