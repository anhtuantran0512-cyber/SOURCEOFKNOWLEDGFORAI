---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/multi-image-upload-grid/"
title: "Multi-Image Upload Grid"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "The listing-photo uploader: a grid where the add tile lives inside the grid, remove badges are always visible (not hover-only, because hover does not exist…"
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Image Upload Grid
Source: https://codefronts.com/components/css-file-upload-button/multi-image-upload-grid/

The listing-photo uploader: a grid where the add tile lives inside the grid, remove badges are always visible (not hover-only, because hover does not exist on touch), and the first tile is automatically the cover — labelled, not implied. Removing a tile re-flows the grid and re-announces the new cover, which is the detail that makes a photo uploader feel considered.
## HTML
```html
<div class="fu-12">
  <button class="fu-12__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-12__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-12__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <section class="fu-12__panel" aria-labelledby="fu-12-h">
    <header class="fu-12__head">
      <h2 class="fu-12__h" id="fu-12-h">Listing photos</h2>
      <p class="fu-12__sub"><span id="fu-12-count">4</span> of 12 <span aria-hidden="true">·</span> first photo is the cover</p>
    </header>

    <ul class="fu-12__grid" id="fu-12-grid">
      <li class="fu-12__tile">
        <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=480&amp;h=480&amp;fit=crop&amp;q=70&amp;auto=format" width="480" height="480" alt="Open-plan living room with large windows" loading="lazy" decoding="async">
        <button class="fu-12__badge" type="button"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg><span class="fu-12__vh">Remove living room photo</span></button>
      </li>
      <li class="fu-12__tile">
        <img src="https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=320&amp;h=320&amp;fit=crop&amp;q=70&amp;auto=format" width="320" height="320" alt="Kitchen with marble island" loading="lazy" decoding="async">
        <button class="fu-12__badge" type="button"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg><span class="fu-12__vh">Remove kitchen photo</span></button>
      </li>
      <li class="fu-12__tile">
        <img src="https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=320&amp;h=320&amp;fit=crop&amp;q=70&amp;auto=format" width="320" height="320" alt="Bedroom with linen bedding" loading="lazy" decoding="async">
        <button class="fu-12__badge" type="button"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg><span class="fu-12__vh">Remove bedroom photo</span></button>
      </li>
      <li class="fu-12__tile">
        <img src="https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=320&amp;h=320&amp;fit=crop&amp;q=70&amp;auto=format" width="320" height="320" alt="Tiled bathroom with walk-in shower" loading="lazy" decoding="async">
        <button class="fu-12__badge" type="button"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M7 7l10 10M17 7 7 17" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg><span class="fu-12__vh">Remove bathroom photo</span></button>
      </li>
      <li class="fu-12__tile fu-12__tile--add">
        <input class="fu-12__input" id="fu-12-file" type="file" multiple accept="image/*">
        <label class="fu-12__addLabel" for="fu-12-file">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 5.5v13M5.5 12h13" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
          <span>Add photos</span>
        </label>
      </li>
    </ul>

    <p class="fu-12__status" id="fu-12-status" role="status" aria-live="polite"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fu-12 {
  --bg: #fafaf9;
  --surface: #ffffff;
  --ink: #111318;
  --muted: #5f6675;
  --line: #e6e7eb;
  --acc: #0b62f6;
  --danger: #e02b45;
  --tile: 8rem;
  --sans: "Plus Jakarta Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
}

.fu-12,
.fu-12 *,
.fu-12 *::before,
.fu-12 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .fu-12 {
    --acc: oklch(55% .21 258);
    --danger: oklch(56% .2 18);
  }
}

.fu-12__panel {
  inline-size: min(38rem,100%);
  display: grid;
  gap: 1rem;
  padding: clamp(1.15rem,3.5vw,1.6rem);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.4rem;
  box-shadow: 0 24px 60px -50px rgba(17,19,24,.6);
}

.fu-12__head {
  display: grid;
  gap: .2rem;
}

.fu-12__h {
  margin: 0;
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: -.025em;
}

.fu-12__sub {
  margin: 0;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.fu-12__grid {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .6rem;
  grid-template-columns: repeat(auto-fill, minmax(var(--tile), 1fr));
  grid-auto-rows: var(--tile);
}

.fu-12__tile {
  position: relative;
  border-radius: 1rem;
  overflow: hidden;
  background: var(--line);
  border: 1px solid var(--line);
  transition: opacity .3s ease, transform .3s cubic-bezier(.16,1,.3,1);
}

@starting-style {
  .fu-12__tile {
    opacity: 0;
    transform: scale(.92);
  }
}

.fu-12__tile.is-going {
  opacity: 0;
  transform: scale(.9);
}

.fu-12__tile img {
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  display: block;
}

.fu-12__tile:first-child {
  grid-column: span 2;
  grid-row: span 2;
}

.fu-12__tile:first-child::after {
  content: "Cover";
  position: absolute;
  inset-block-start: .55rem;
  inset-inline-start: .55rem;
  padding: .25rem .5rem;
  border-radius: .4rem;
  background: rgba(10,12,16,.78);
  color: #fff;
  font-family: var(--mono);
  font-size: .5625rem;
  letter-spacing: .08em;
  text-transform: uppercase;
}

.fu-12__badge {
  position: absolute;
  inset-block-start: .4rem;
  inset-inline-end: .4rem;
  inline-size: 2rem;
  block-size: 2rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border: 0;
  border-radius: 999px;
  background: rgba(10,12,16,.72);
  color: #fff;
  transition: background .2s ease, transform .2s cubic-bezier(.16,1,.3,1);
}

.fu-12__badge::before {
  content: "";
  position: absolute;
  inset: -6px;
}

.fu-12__badge svg {
  inline-size: .85rem;
  block-size: .85rem;
}

.fu-12__badge:hover {
  background: var(--danger);
  transform: scale(1.08);
}

.fu-12__badge:focus-visible {
  outline: 2px solid #fff;
  outline-offset: -4px;
  box-shadow: 0 0 0 4px var(--acc);
}

.fu-12__tile--add {
  background: transparent;
  border: 2px dashed color-mix(in oklab,var(--acc) 30%,var(--line));
}

.fu-12__input {
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

.fu-12__addLabel {
  display: grid;
  place-content: center;
  justify-items: center;
  gap: .35rem;
  block-size: 100%;
  cursor: pointer;
  color: color-mix(in oklab,var(--acc) 85%,var(--ink));
  font-size: .75rem;
  font-weight: 600;
  text-align: center;
  transition: background .2s ease, color .2s ease;
}

.fu-12__addLabel svg {
  inline-size: 1.35rem;
  block-size: 1.35rem;
}

.fu-12__addLabel:hover {
  background: color-mix(in oklab,var(--acc) 7%,transparent);
}

.fu-12__input:focus-visible + .fu-12__addLabel {
  outline: 2px solid var(--acc);
  outline-offset: -3px;
}

.fu-12__status {
  margin: 0;
  min-block-size: 1rem;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

.fu-12__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-color-scheme: dark) {
  .fu-12:not([data-theme="light"]) {
    --bg: #0b0c10;
    --surface: #131620;
    --ink: #eff1f6;
    --muted: #8b93a5;
    --line: #232838;
    --acc: #6f9bff;
    --danger: #ff6b81;
  }
}

.fu-12[data-theme="dark"] {
  --bg: #0b0c10;
  --surface: #131620;
  --ink: #eff1f6;
  --muted: #8b93a5;
  --line: #232838;
  --acc: #6f9bff;
  --danger: #ff6b81;
}

@media (max-width: 26rem) {
  .fu-12 {
    --tile: 6.25rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fu-12 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fu-12__tile,
    .fu-12__panel {
    border: 1px solid CanvasText;
  }

  .fu-12__badge {
    background: Canvas;
    color: CanvasText;
    border: 1px solid CanvasText;
  }
}
/* ── in-demo theme toggle ── */

.fu-12 {
  position: relative;
}

.fu-12__theme {
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

.fu-12__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-12__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-12__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-12__sun {
  display: none;
}

.fu-12__theme[aria-pressed="true"] .fu-12__sun {
  display: block;
}

.fu-12__theme[aria-pressed="true"] .fu-12__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-12__theme {
    transition: none;
  }

  .fu-12__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-12__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.fu-12');
  if (!root) return;
  const grid = root.querySelector('#fu-12-grid');
  const input = root.querySelector('#fu-12-file');
  const addTile = root.querySelector('.fu-12__tile--add');
  const count = root.querySelector('#fu-12-count');
  const status = root.querySelector('#fu-12-status');
  const MAX = 12;
  const urls = new WeakMap();

  const photos = () => [...grid.querySelectorAll('.fu-12__tile:not(.fu-12__tile--add)')];
  const recount = () => {
    count.textContent = photos().length;
    addTile.hidden = photos().length >= MAX;
  };

  input.addEventListener('change', () => {
    const files = [...input.files].filter(f => f.type.startsWith('image/')).slice(0, MAX - photos().length);
    files.forEach(file => {
      const li = document.createElement('li');
      li.className = 'fu-12__tile';
      const img = document.createElement('img');
      const url = URL.createObjectURL(file);
      urls.set(li, url);
      img.src = url; img.alt = file.name; img.decoding = 'async';
      const btn = document.createElement('button');
      btn.type = 'button'; btn.className = 'fu-12__badge';
      btn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M7 7l10 10M17 7 7 17" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg><span class="fu-12__vh">Remove ' + file.name + '</span>';
      li.append(img, btn);
      grid.insertBefore(li, addTile);
    });
    recount();
    input.value = '';
    status.textContent = files.length + ' photo' + (files.length === 1 ? '' : 's') + ' added, ' + photos().length + ' total';
  });

  grid.addEventListener('click', (e) => {
    const btn = e.target.closest('.fu-12__badge');
    if (!btn) return;
    const tile = btn.closest('.fu-12__tile');
    const wasCover = tile === photos()[0];
    const url = urls.get(tile);
    if (url) URL.revokeObjectURL(url);
    tile.classList.add('is-going');
    setTimeout(() => {
      tile.remove(); recount();
      const next = grid.querySelector('.fu-12__badge') || root.querySelector('.fu-12__addLabel');
      next.focus();
      status.textContent = wasCover ? 'Photo removed — the next photo is now the cover' : 'Photo removed, ' + photos().length + ' remaining';
    }, 220);
  });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-12');
  const btn = root && root.querySelector('.fu-12__theme');
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
