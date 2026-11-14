---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/clipboard-image-paste-upload/"
title: "Clipboard Image Paste Upload"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "Screenshots never touch the filesystem, so the fastest upload is Ctrl/Cmd + V."
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Clipboard Image Paste Upload
Source: https://codefronts.com/components/css-file-upload-button/clipboard-image-paste-upload/

Screenshots never touch the filesystem, so the fastest upload is Ctrl/Cmd + V. This area listens for paste and reads e.clipboardData.files — plus a click-to-read fallback using the async navigator.clipboard.read() API for users who prefer a button. The target is a real focusable region with a keyboard hint, so it is discoverable rather than a hidden trick.
## HTML
```html
<div class="fu-19">
  <button class="fu-19__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-19__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-19__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <section class="fu-19__card" aria-labelledby="fu-19-h">
    <div class="fu-19__area" id="fu-19-area" tabindex="0" role="button"
         aria-label="Paste an image with Control or Command V, or press Enter to browse files"
         aria-describedby="fu-19-hint">
      <span class="fu-19__kbd" aria-hidden="true"><kbd>⌘</kbd><kbd>V</kbd></span>
      <h2 class="fu-19__h" id="fu-19-h">Paste a screenshot</h2>
      <p class="fu-19__hint" id="fu-19-hint">Copy any image, then press <kbd>Ctrl</kbd>/<kbd>⌘</kbd> + <kbd>V</kbd> here</p>
      <div class="fu-19__row">
        <button class="fu-19__read" id="fu-19-read" type="button">Read clipboard</button>
        <input class="fu-19__input" id="fu-19-file" type="file" accept="image/*" multiple>
        <label class="fu-19__browse" for="fu-19-file">Browse files</label>
      </div>
    </div>

    <ul class="fu-19__shots" id="fu-19-shots"></ul>
    <p class="fu-19__status" id="fu-19-status" role="status" aria-live="polite"></p>
  </section>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

.fu-19 {
  --bg: #0d0b14;
  --surface: #161320;
  --raise: #1e1a2b;
  --ink: #f2effa;
  --muted: #9a92b3;
  --line: #2b2740;
  --acc: #b388ff;
  --acc2: #61f0d0;
  --sans: "Space Grotesk",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(75% 50% at 50% 0%, color-mix(in oklab,var(--acc) 18%,transparent), transparent 62%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.fu-19,
.fu-19 *,
.fu-19 *::before,
.fu-19 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .fu-19 {
    --acc: oklch(76% .15 300);
    --acc2: oklch(86% .14 175);
  }
}

.fu-19__card {
  inline-size: min(32rem,100%);
  display: grid;
  gap: .8rem;
}

.fu-19__area {
  position: relative;
  display: grid;
  justify-items: center;
  gap: .45rem;
  text-align: center;
  cursor: pointer;
  padding: clamp(1.75rem,6vw,2.75rem) 1.25rem;
  border-radius: 1.5rem;
  background: linear-gradient(180deg, color-mix(in oklab,var(--surface) 90%,transparent), var(--surface));
  border: 1.5px dashed var(--line);
  transition: border-color .3s ease, background .3s ease, transform .3s cubic-bezier(.16,1,.3,1);
}

.fu-19__area:hover {
  border-color: color-mix(in oklab,var(--acc) 50%,var(--line));
}

.fu-19__area:focus-visible {
  outline: 2px solid var(--acc2);
  outline-offset: 4px;
  border-color: var(--acc);
}

.fu-19__area.is-hot {
  border-color: var(--acc2);
  border-style: solid;
  transform: scale(1.008);
  background: color-mix(in oklab,var(--acc2) 8%,var(--surface));
}

.fu-19__kbd {
  display: inline-flex;
  gap: .3rem;
  margin-block-end: .3rem;
}

.fu-19__kbd kbd,
.fu-19__hint kbd {
  display: inline-grid;
  place-items: center;
  min-inline-size: 1.9rem;
  min-block-size: 1.9rem;
  padding: .15rem .45rem;
  border-radius: .5rem;
  border: 1px solid var(--line);
  border-block-end-width: 3px;
  background: var(--raise);
  color: var(--ink);
  font-family: var(--mono);
  font-size: .75rem;
}

.fu-19__hint kbd {
  min-inline-size: auto;
  min-block-size: auto;
  font-size: .625rem;
  border-block-end-width: 2px;
}

.fu-19__h {
  margin: 0;
  font-size: clamp(1.2rem,3vw,1.5rem);
  font-weight: 700;
  letter-spacing: -.03em;
}

.fu-19__hint {
  margin: 0;
  font-family: var(--mono);
  font-size: .75rem;
  color: var(--muted);
  display: flex;
  align-items: center;
  gap: .3rem;
  flex-wrap: wrap;
  justify-content: center;
}

.fu-19__row {
  display: flex;
  gap: .5rem;
  margin-block-start: .55rem;
  flex-wrap: wrap;
  justify-content: center;
}

.fu-19__input {
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

.fu-19__read,
.fu-19__browse {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  min-block-size: 2.75rem;
  padding: .6rem 1.1rem;
  border-radius: .8rem;
  font-family: var(--sans);
  font-size: .875rem;
  font-weight: 600;
  transition: filter .2s ease, transform .2s cubic-bezier(.16,1,.3,1), border-color .2s ease, background .2s ease;
}

.fu-19__read {
  border: 0;
  background: var(--acc);
  color: #170c2b;
}

.fu-19__read:hover {
  filter: brightness(1.08);
  transform: translateY(-1px);
}

.fu-19__read:focus-visible {
  outline: 2px solid var(--acc2);
  outline-offset: 3px;
}

.fu-19__browse {
  border: 1px solid var(--line);
  background: transparent;
  color: var(--ink);
}

.fu-19__browse:hover {
  border-color: var(--acc2);
}

.fu-19__input:focus-visible + .fu-19__browse {
  outline: 2px solid var(--acc2);
  outline-offset: 3px;
}

.fu-19__shots {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .5rem;
  grid-template-columns: repeat(auto-fill, minmax(8rem, 1fr));
}

.fu-19__shots:empty {
  display: none;
}

.fu-19__shots li {
  position: relative;
  border-radius: .9rem;
  overflow: hidden;
  border: 1px solid var(--line);
  background: var(--raise);
  animation: fu-19-in .45s cubic-bezier(.16,1,.3,1) both;
}

@keyframes fu-19-in {
  from {
    opacity: 0;
    transform: translateY(8px) scale(.97);
  }
}

.fu-19__shots img {
  display: block;
  inline-size: 100%;
  aspect-ratio: 16/10;
  object-fit: cover;
}

.fu-19__shots figcaption,
.fu-19__shots span {
  display: block;
  padding: .4rem .55rem;
  font-family: var(--mono);
  font-size: .5625rem;
  color: var(--muted);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.fu-19__status {
  margin: 0;
  min-block-size: 1rem;
  font-family: var(--mono);
  font-size: .6875rem;
  color: var(--acc2);
  text-align: center;
}

@media (prefers-color-scheme: light) {
  .fu-19:not([data-theme="dark"]) {
    --bg: #f4f2fa;
    --surface: #ffffff;
    --raise: #f6f4fc;
    --ink: #130f1e;
    --muted: #5f5878;
    --line: #e4e0f0;
    --acc: #7c4dff;
    --acc2: #0f9d8c;
  }

  .fu-19:not([data-theme="dark"]) .fu-19__read {
    color: #fff;
  }
}

.fu-19[data-theme="light"] {
  --bg: #f4f2fa;
  --surface: #ffffff;
  --raise: #f6f4fc;
  --ink: #130f1e;
  --muted: #5f5878;
  --line: #e4e0f0;
  --acc: #7c4dff;
  --acc2: #0f9d8c;
}

.fu-19[data-theme="light"] .fu-19__read {
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .fu-19 * {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fu-19__area,
    .fu-19__shots li {
    border: 1px solid CanvasText;
  }

  .fu-19__read {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }
}
/* ── in-demo theme toggle ── */

.fu-19 {
  position: relative;
}

.fu-19__theme {
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

.fu-19__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-19__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-19__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-19__sun {
  display: none;
}

.fu-19__theme[aria-pressed="true"] .fu-19__sun {
  display: block;
}

.fu-19__theme[aria-pressed="true"] .fu-19__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-19__theme {
    transition: none;
  }

  .fu-19__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-19__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.fu-19');
  if (!root) return;
  const area = root.querySelector('#fu-19-area');
  const shots = root.querySelector('#fu-19-shots');
  const input = root.querySelector('#fu-19-file');
  const status = root.querySelector('#fu-19-status');
  let n = 0;

  const intake = (files) => {
    const imgs = [...files].filter(f => f.type.startsWith('image/'));
    if (!imgs.length) { status.textContent = 'No image found in that clipboard content'; return; }
    imgs.forEach(file => {
      const li = document.createElement('li');
      const img = document.createElement('img');
      const url = URL.createObjectURL(file);
      img.src = url; img.alt = file.name || 'Pasted image';
      img.onload = () => URL.revokeObjectURL(url);
      const cap = document.createElement('span');
      cap.textContent = (file.name === 'image.png' ? 'screenshot-' + (++n) + '.png' : file.name) +
        ' · ' + Math.max(1, Math.round(file.size / 1024)) + ' KB';
      li.append(img, cap);
      shots.prepend(li);
    });
    status.textContent = imgs.length + ' image' + (imgs.length === 1 ? '' : 's') + ' added from the clipboard';
  };

  area.addEventListener('paste', (e) => {
    const files = [...(e.clipboardData?.files || [])].filter(f => f.type.startsWith('image/'));
    if (!files.length) return;                    // let text paste through untouched
    e.preventDefault();
    intake(files);
  });
  document.addEventListener('paste', (e) => {
    if (document.activeElement === area) return;  // already handled above
    const files = [...(e.clipboardData?.files || [])].filter(f => f.type.startsWith('image/'));
    if (files.length) { e.preventDefault(); intake(files); }
  });

  root.querySelector('#fu-19-read').addEventListener('click', async () => {
    try {
      const items = await navigator.clipboard.read();
      const out = [];
      for (const item of items) {
        const type = item.types.find(t => t.startsWith('image/'));
        if (type) out.push(new File([await item.getType(type)], 'clipboard.png', { type }));
      }
      out.length ? intake(out) : (status.textContent = 'Clipboard holds no image');
    } catch {
      status.textContent = 'Clipboard access was blocked — press Ctrl or ⌘ + V instead';
      area.focus();
    }
  });

  area.addEventListener('keydown', (e) => { if (e.key === 'Enter') { e.preventDefault(); input.click(); } });
  area.addEventListener('click', (e) => { if (!e.target.closest('button,label')) area.focus(); });
  area.addEventListener('focus', () => area.classList.add('is-hot'));
  area.addEventListener('blur', () => area.classList.remove('is-hot'));
  input.addEventListener('change', () => { intake(input.files); input.value = ''; });
})();

(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-19');
  const btn = root && root.querySelector('.fu-19__theme');
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
