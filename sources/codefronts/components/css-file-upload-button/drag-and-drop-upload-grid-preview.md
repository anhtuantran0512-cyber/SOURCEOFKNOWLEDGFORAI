---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/drag-and-drop-upload-grid-preview/"
title: "Drag and Drop Upload Grid Preview"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "Drop a folder of photos and watch them land in a responsive gallery."
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Drag and Drop Upload Grid Preview
Source: https://codefronts.com/components/css-file-upload-button/drag-and-drop-upload-grid-preview/

Drop a folder of photos and watch them land in a responsive gallery. Thumbnails come from URL.createObjectURL(file) — no FileReader, no base64, no memory bloat — and every URL is revoked on removal so long sessions do not leak. The grid is one repeat(auto-fill, minmax()) line, so it reflows from a phone to an ultrawide with no media queries and no breakpoints to maintain.
## HTML
```html
<div class="fu-07">
  <button class="fu-07__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-07__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-07__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <section class="fu-07__panel" aria-labelledby="fu-07-h">
    <header class="fu-07__head">
      <div>
        <h2 class="fu-07__h" id="fu-07-h">Gallery upload</h2>
        <p class="fu-07__sub"><span id="fu-07-count">3</span> images <span aria-hidden="true">·</span> JPG, PNG, WEBP</p>
      </div>
      <label class="fu-07__add" for="fu-07-file">
        <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 5.5v13M5.5 12h13" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
        Add
      </label>
      <input class="fu-07__input" id="fu-07-file" type="file" multiple accept="image/*">
    </header>

    <div class="fu-07__zone" id="fu-07-zone" role="button" tabindex="0"
         aria-label="Drop images here, or press Enter to browse your device">
      <ul class="fu-07__grid" id="fu-07-grid">
        <li class="fu-07__tile" style="--i:0">
          <img src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=320&amp;h=320&amp;fit=crop&amp;q=70&amp;auto=format" width="320" height="320" alt="Sunlit birch forest" loading="lazy" decoding="async">
          <span class="fu-07__cap">birch-canopy-4k.jpg</span>
        </li>
        <li class="fu-07__tile" style="--i:1">
          <img src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=320&amp;h=320&amp;fit=crop&amp;q=70&amp;auto=format" width="320" height="320" alt="Fog rolling over a mountain ridge" loading="lazy" decoding="async">
          <span class="fu-07__cap">ridge-fog-01.jpg</span>
        </li>
        <li class="fu-07__tile" style="--i:2">
          <img src="https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?w=320&amp;h=320&amp;fit=crop&amp;q=70&amp;auto=format" width="320" height="320" alt="Coastal cliffs at dusk" loading="lazy" decoding="async">
          <span class="fu-07__cap">coast-dusk-final.jpg</span>
        </li>
      </ul>

      <p class="fu-07__empty">Drop images here</p>
      <span class="fu-07__veil" aria-hidden="true"><span>Release to add</span></span>
    </div>

    <p class="fu-07__status" id="fu-07-status" role="status" aria-live="polite"></p>
  </section>

  <template id="fu-07-tpl">
    <li class="fu-07__tile">
      <img alt="" decoding="async">
      <span class="fu-07__cap"></span>
      <button class="fu-07__rm" type="button"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6.5 6.5l11 11m0-11-11 11" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg><span class="fu-07__vh"></span></button>
    </li>
  </template>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],400;12..96,600;12..96,700&family=Geist+Mono:wght@400;500&display=swap');

.fu-07 {
  --bg: #08090d;
  --surface: #101219;
  --raise: #171a23;
  --ink: #f1f3f8;
  --muted: #868fa2;
  --line: #242936;
  --acc: #ff6a3d;
  --acc2: #ffd166;
  --sans: "Bricolage Grotesque",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(70% 50% at 100% 0%, color-mix(in oklab,var(--acc) 18%,transparent), transparent 60%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.fu-07,
.fu-07 *,
.fu-07 *::before,
.fu-07 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .fu-07 {
    --acc: oklch(68% .2 43);
    --acc2: oklch(86% .14 88);
  }
}

.fu-07__panel {
  inline-size: min(44rem,100%);
  display: grid;
  gap: 1rem;
  padding: clamp(1.1rem,3.5vw,1.6rem);
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 1.5rem;
  box-shadow: 0 40px 90px -60px #000;
}

.fu-07__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.fu-07__h {
  margin: 0;
  font-size: 1.3rem;
  font-weight: 700;
  letter-spacing: -.03em;
}

.fu-07__sub {
  margin: .2rem 0 0;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.fu-07__input {
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

.fu-07__add {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  cursor: pointer;
  user-select: none;
  min-block-size: 2.75rem;
  padding: .55rem 1.05rem;
  border-radius: 999px;
  background: var(--acc);
  color: #120703;
  font-size: .875rem;
  font-weight: 600;
  transition: filter .2s ease, transform .2s cubic-bezier(.16,1,.3,1);
}

.fu-07__add svg {
  inline-size: 1rem;
  block-size: 1rem;
}

.fu-07__add:hover {
  filter: brightness(1.08);
  transform: translateY(-1px);
}

.fu-07__input:focus-visible ~ .fu-07__add,
.fu-07__input:focus-visible + .fu-07__add {
  outline: 2px solid var(--acc2);
  outline-offset: 3px;
}

.fu-07__zone {
  position: relative;
  cursor: pointer;
  border-radius: 1.2rem;
  padding: .7rem;
  border: 2px dashed var(--line);
  background: color-mix(in oklab,var(--ink) 3%,transparent);
  transition: border-color .3s ease, background .3s ease;
}

.fu-07__zone:hover {
  border-color: color-mix(in oklab,var(--acc) 45%,var(--line));
}

.fu-07__zone:focus-visible {
  outline: 2px solid var(--acc2);
  outline-offset: 3px;
}

.fu-07__zone.is-over {
  border-color: var(--acc);
  border-style: solid;
  background: color-mix(in oklab,var(--acc) 10%,transparent);
}

.fu-07__grid {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .6rem;
  grid-template-columns: repeat(auto-fill, minmax(7.5rem, 1fr));
}

.fu-07__grid:empty {
  display: none;
}

.fu-07__empty {
  margin: 0;
  padding: 2.5rem 1rem;
  text-align: center;
  font-family: var(--mono);
  font-size: .8125rem;
  color: var(--muted);
}

.fu-07__zone:has(.fu-07__tile) .fu-07__empty {
  display: none;
}

.fu-07__tile {
  position: relative;
  border-radius: .9rem;
  overflow: hidden;
  background: var(--raise);
  border: 1px solid var(--line);
  isolation: isolate;
  aspect-ratio: 1;
  animation: fu-07-in .5s cubic-bezier(.16,1,.3,1) both;
  animation-delay: calc(var(--i,0) * 55ms);
}

@keyframes fu-07-in {
  from {
    opacity: 0;
    transform: translateY(10px) scale(.96);
  }
}

.fu-07__tile img {
  position: absolute;
  inset: 0;
  display: block;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  background: var(--raise);
  transition: transform .5s cubic-bezier(.16,1,.3,1), filter .3s ease;
}

.fu-07__tile:hover img {
  transform: scale(1.06);
}

.fu-07__cap {
  position: absolute;
  inset-inline: 0;
  inset-block-end: 0;
  padding: 1.6rem .55rem .45rem;
  font-family: var(--mono);
  font-size: .5625rem;
  letter-spacing: .01em;
  color: #fff;
  background: linear-gradient(180deg, transparent, rgba(0,0,0,.82));
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.fu-07__rm {
  position: absolute;
  inset-block-start: .35rem;
  inset-inline-end: .35rem;
  inline-size: 2rem;
  block-size: 2rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border: 0;
  border-radius: 999px;
  background: rgba(8,9,13,.7);
  color: #fff;
  opacity: 0;
  transition: opacity .25s ease, background .2s ease;
  backdrop-filter: blur(6px);
}

.fu-07__rm svg {
  inline-size: .9rem;
  block-size: .9rem;
}

.fu-07__tile:hover .fu-07__rm,
.fu-07__rm:focus-visible {
  opacity: 1;
}

.fu-07__rm:hover {
  background: var(--acc);
}

.fu-07__rm:focus-visible {
  outline: 2px solid var(--acc2);
  outline-offset: 2px;
}

.fu-07__veil {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  border-radius: 1rem;
  background: color-mix(in oklab,var(--acc) 22%,transparent);
  opacity: 0;
  pointer-events: none;
  transition: opacity .25s ease;
  backdrop-filter: blur(2px);
}

.fu-07__veil span {
  font-family: var(--mono);
  font-size: .75rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  padding: .5rem .9rem;
  border-radius: 999px;
  background: #08090d;
  color: var(--ink);
}

.fu-07__zone.is-over .fu-07__veil {
  opacity: 1;
}

.fu-07__status {
  margin: 0;
  min-block-size: 1rem;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--muted);
}

.fu-07__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-color-scheme: light) {
  .fu-07:not([data-theme="dark"]) {
    --bg: #f4f2ef;
    --surface: #ffffff;
    --raise: #f3f4f7;
    --ink: #0b0c11;
    --muted: #5c6478;
    --line: #e2e4ea;
    --acc: #e8501f;
    --acc2: #a8620a;
  }

  .fu-07:not([data-theme="dark"]) .fu-07__add {
    color: #fff;
  }

  .fu-07:not([data-theme="dark"]) .fu-07__veil span {
    background: #fff;
    color: #0b0c11;
  }
}

.fu-07[data-theme="light"] {
  --bg: #f4f2ef;
  --surface: #ffffff;
  --raise: #f3f4f7;
  --ink: #0b0c11;
  --muted: #5c6478;
  --line: #e2e4ea;
  --acc: #e8501f;
  --acc2: #a8620a;
}

.fu-07[data-theme="light"] .fu-07__add {
  color: #fff;
}

.fu-07[data-theme="light"] .fu-07__veil span {
  background: #fff;
  color: #0b0c11;
}

@media (prefers-reduced-motion: reduce) {
  .fu-07 * {
    animation: none !important;
    transition: none !important;
  }

  .fu-07__rm {
    opacity: 1;
  }
}

@media (forced-colors: active) {
  .fu-07__zone,
    .fu-07__tile {
    border: 1px solid CanvasText;
  }

  .fu-07__add {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .fu-07__rm {
    opacity: 1;
    background: Canvas;
    color: CanvasText;
    border: 1px solid CanvasText;
  }
}
/* ── in-demo theme toggle ── */

.fu-07 {
  position: relative;
}

.fu-07__theme {
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

.fu-07__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-07__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-07__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-07__sun {
  display: none;
}

.fu-07__theme[aria-pressed="true"] .fu-07__sun {
  display: block;
}

.fu-07__theme[aria-pressed="true"] .fu-07__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-07__theme {
    transition: none;
  }

  .fu-07__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-07__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.fu-07');
  if (!root) return;
  const zone = root.querySelector('#fu-07-zone');
  const grid = root.querySelector('#fu-07-grid');
  const input = root.querySelector('#fu-07-file');
  const tpl = root.querySelector('#fu-07-tpl');
  const count = root.querySelector('#fu-07-count');
  const status = root.querySelector('#fu-07-status');
  let depth = 0;

  const recount = () => { count.textContent = grid.children.length; };

  const add = (files) => {
    const imgs = [...files].filter(f => f.type.startsWith('image/'));
    if (!imgs.length) { status.textContent = 'No images in that drop — images only'; return; }
    imgs.forEach((file, n) => {
      const li = tpl.content.firstElementChild.cloneNode(true);
      const img = li.querySelector('img');
      const url = URL.createObjectURL(file);
      img.src = url; img.alt = file.name;
      img.onload = () => URL.revokeObjectURL(url);       // free the blob once decoded
      li.style.setProperty('--i', n);
      li.querySelector('.fu-07__cap').textContent = file.name;
      li.querySelector('.fu-07__vh').textContent = 'Remove ' + file.name;
      grid.append(li);
    });
    recount();
    status.textContent = imgs.length + ' image' + (imgs.length === 1 ? '' : 's') + ' added, ' + grid.children.length + ' total';
  };

  ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(t =>
    zone.addEventListener(t, e => { e.preventDefault(); e.stopPropagation(); })
  );
  zone.addEventListener('dragenter', () => { depth++; zone.classList.add('is-over'); });
  zone.addEventListener('dragover', e => { e.dataTransfer.dropEffect = 'copy'; });
  zone.addEventListener('dragleave', () => { if (--depth <= 0) { depth = 0; zone.classList.remove('is-over'); } });
  zone.addEventListener('drop', e => { depth = 0; zone.classList.remove('is-over'); add(e.dataTransfer.files); });

  zone.addEventListener('click', e => { if (!e.target.closest('button')) input.click(); });
  zone.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); input.click(); } });
  input.addEventListener('change', () => { add(input.files); input.value = ''; });

  grid.addEventListener('click', e => {
    const btn = e.target.closest('.fu-07__rm');
    if (!btn) return;
    const tile = btn.closest('.fu-07__tile');
    const name = tile.querySelector('.fu-07__cap').textContent;
    tile.remove(); recount();
    status.textContent = name + ' removed';
  });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-07');
  const btn = root && root.querySelector('.fu-07__theme');
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
