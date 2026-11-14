---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-retro-designs/retro-desktop-portfolio-website-template/"
title: "Retro Desktop Portfolio Template"
section: "design-styles"
category: "css-retro-designs"
category_name: "CSS Retro UI"
description: "A portfolio laid out as a desktop: menu bar, icon field and two windows you can move."
has_js: "true"
---

Here's a working CSS Retro UI from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Retro Desktop Portfolio Template
Source: https://codefronts.com/design-styles/css-retro-designs/retro-desktop-portfolio-website-template/

A portfolio laid out as a desktop: menu bar, icon field and two windows you can move. The drag is the point &mdash; a pointer-only implementation fails keyboard operability outright, so every title bar here is focusable, responds to the arrow keys, and reports its position, with the pointer path as an enhancement rather than the only way in.
## HTML
```html
<section class="rt-20" aria-labelledby="rt-20-title">
  <h2 class="rt-20__sr" id="rt-20-title">Retro desktop portfolio with movable windows</h2>

  <div class="rt-20__theme">
    <input class="rt-20__theme-input" type="checkbox" id="rt-20-theme">
    <label class="rt-20__theme-label" for="rt-20-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 4a8 8 0 0 0 0 16Z" fill="currentColor"/></svg>
      <span class="rt-20__sr">Toggle dark desktop</span>
    </label>
  </div>

  <div class="rt-20__bar">
    <span class="rt-20__mark" aria-hidden="true"></span>
    <nav class="rt-20__menu" aria-label="Desktop menu">
      <ul>
        <li><button type="button">File</button></li>
        <li><button type="button">View</button></li>
        <li><button type="button">Work</button></li>
        <li><button type="button">Contact</button></li>
      </ul>
    </nav>
    <span class="rt-20__clock">Sam Rivera &middot; 11:42</span>
  </div>

  <div class="rt-20__desk">
    <ul class="rt-20__icons">
      <li><button class="rt-20__icon" type="button"><span class="rt-20__gl rt-20__gl--folder" aria-hidden="true"></span>Selected Work</button></li>
      <li><button class="rt-20__icon" type="button"><span class="rt-20__gl rt-20__gl--doc" aria-hidden="true"></span>About.txt</button></li>
      <li><button class="rt-20__icon" type="button"><span class="rt-20__gl rt-20__gl--disk" aria-hidden="true"></span>Archive</button></li>
    </ul>

    <article class="rt-20__win" id="rt-20-win-1" style="--rt-20-x: 0px; --rt-20-y: 0px" aria-labelledby="rt-20-w1t">
      <div class="rt-20__cap" data-rt20-handle tabindex="0" role="button" aria-describedby="rt-20-hint">
        <span class="rt-20__dots" aria-hidden="true"><i></i><i></i><i></i></span>
        <span class="rt-20__cap-t" id="rt-20-w1t">Selected Work &mdash; 2024 to 2026</span>
      </div>
      <div class="rt-20__body">
        <ul class="rt-20__list">
          <li><span class="rt-20__li-n">Ledger</span><span class="rt-20__li-m">Design system &middot; 2026</span></li>
          <li><span class="rt-20__li-n">Northgate Radio</span><span class="rt-20__li-m">Product design &middot; 2025</span></li>
          <li><span class="rt-20__li-n">Field Notes</span><span class="rt-20__li-m">Editorial tooling &middot; 2025</span></li>
          <li><span class="rt-20__li-n">Sable</span><span class="rt-20__li-m">Identity &middot; 2024</span></li>
        </ul>
      </div>
    </article>

    <article class="rt-20__win rt-20__win--b" id="rt-20-win-2" style="--rt-20-x: 0px; --rt-20-y: 0px" aria-labelledby="rt-20-w2t">
      <div class="rt-20__cap" data-rt20-handle tabindex="0" role="button" aria-describedby="rt-20-hint">
        <span class="rt-20__dots" aria-hidden="true"><i></i><i></i><i></i></span>
        <span class="rt-20__cap-t" id="rt-20-w2t">About.txt</span>
      </div>
      <div class="rt-20__body">
        <p class="rt-20__p">Product designer working on tools for people who make things. Previously at two consultancies and one very small hardware company.</p>
        <p class="rt-20__p">This desktop is keyboard-operable: focus a title bar and use the arrow keys. Hold Shift for larger steps.</p>
        <p class="rt-20__meta">[email protected]</p>
      </div>
    </article>

    <p class="rt-20__sr" id="rt-20-hint">Move this window with the arrow keys, or drag the title bar. Hold Shift for larger steps.</p>

    <p class="rt-20__legend">Drag a title bar, or focus one with <kbd>Tab</kbd> and use the arrow keys.</p>
  </div>
</section>
```
## CSS
```css
.rt-20 {
  --rt-20-desk-a: #dcd9ec;
  --rt-20-desk-a: oklch(88% 0.025 290);
  --rt-20-desk-b: #c6c2de;
  --rt-20-desk-b: oklch(82% 0.035 290);
  --rt-20-surface: #ffffff;
  --rt-20-chrome: #edecf4;
  --rt-20-ink: #17161f;
  --rt-20-ink: oklch(20% 0.012 290);
  --rt-20-ink-2: #4c4a5c;
  --rt-20-ink-2: oklch(43% 0.018 290);
  --rt-20-line: #a9a5c0;
  --rt-20-line: oklch(72% 0.026 290);
  --rt-20-acc: #4b2ad0;
  --rt-20-acc: oklch(44% 0.21 285);
  --rt-20-sans: system-ui, -apple-system, "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  --rt-20-mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background-color: var(--rt-20-desk-a);
  background-image: linear-gradient(180deg, var(--rt-20-desk-a), var(--rt-20-desk-b)), repeating-linear-gradient(90deg, rgba(255,255,255,0.28) 0 1px, rgba(0,0,0,0) 1px 6px);
  color: var(--rt-20-ink);
  font-family: var(--rt-20-sans);
  overflow: hidden;
  -webkit-text-size-adjust: 100%;
}

.rt-20 *,
.rt-20 *::before,
.rt-20 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rt-20 {
    --rt-20-desk-a: #191727;
    --rt-20-desk-a: oklch(22% 0.03 290);
    --rt-20-desk-b: #100f1c;
    --rt-20-desk-b: oklch(17% 0.028 290);
    --rt-20-surface: #201e2e;
    --rt-20-chrome: #2a2839;
    --rt-20-ink: #efeef7;
    --rt-20-ink: oklch(95% 0.008 290);
    --rt-20-ink-2: #aeaac4;
    --rt-20-ink-2: oklch(75% 0.02 290);
    --rt-20-line: #413e56;
    --rt-20-line: oklch(38% 0.028 290);
    --rt-20-acc: #a894ff;
    --rt-20-acc: oklch(78% 0.15 285);
  }
}

.rt-20[data-theme="dark"],
.rt-20:has(.rt-20__theme-input:checked) {
  --rt-20-desk-a: #191727;
  --rt-20-desk-a: oklch(22% 0.03 290);
  --rt-20-desk-b: #100f1c;
  --rt-20-desk-b: oklch(17% 0.028 290);
  --rt-20-surface: #201e2e;
  --rt-20-chrome: #2a2839;
  --rt-20-ink: #efeef7;
  --rt-20-ink: oklch(95% 0.008 290);
  --rt-20-ink-2: #aeaac4;
  --rt-20-ink-2: oklch(75% 0.02 290);
  --rt-20-line: #413e56;
  --rt-20-line: oklch(38% 0.028 290);
  --rt-20-acc: #a894ff;
  --rt-20-acc: oklch(78% 0.15 285);
}

@media (prefers-color-scheme: light) {
  .rt-20:has(.rt-20__theme-input:checked) {
    --rt-20-desk-a: #191727;
    --rt-20-desk-a: oklch(22% 0.03 290);
    --rt-20-desk-b: #100f1c;
    --rt-20-desk-b: oklch(17% 0.028 290);
    --rt-20-surface: #201e2e;
    --rt-20-chrome: #2a2839;
    --rt-20-ink: #efeef7;
    --rt-20-ink: oklch(95% 0.008 290);
    --rt-20-ink-2: #aeaac4;
    --rt-20-ink-2: oklch(75% 0.02 290);
    --rt-20-line: #413e56;
    --rt-20-line: oklch(38% 0.028 290);
    --rt-20-acc: #a894ff;
    --rt-20-acc: oklch(78% 0.15 285);
  }
}

@media (prefers-color-scheme: dark) {
  .rt-20:has(.rt-20__theme-input:checked) {
    --rt-20-desk-a: #dcd9ec;
    --rt-20-desk-a: oklch(88% 0.025 290);
    --rt-20-desk-b: #c6c2de;
    --rt-20-desk-b: oklch(82% 0.035 290);
    --rt-20-surface: #ffffff;
    --rt-20-chrome: #edecf4;
    --rt-20-ink: #17161f;
    --rt-20-ink: oklch(20% 0.012 290);
    --rt-20-ink-2: #4c4a5c;
    --rt-20-ink-2: oklch(43% 0.018 290);
    --rt-20-line: #a9a5c0;
    --rt-20-line: oklch(72% 0.026 290);
    --rt-20-acc: #4b2ad0;
    --rt-20-acc: oklch(44% 0.21 285);
  }
}

.rt-20__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.rt-20__theme {
  position: absolute;
  inset-block-start: calc(44px + 0.75rem);
  inset-inline-end: 1rem;
  z-index: 40;
}

.rt-20__theme-input {
  position: absolute;
  inset: 0;
  inline-size: 44px;
  block-size: 44px;
  margin: 0;
  opacity: 0;
  cursor: pointer;
}

.rt-20__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--rt-20-line);
  border-radius: 8px;
  background: var(--rt-20-surface);
  color: var(--rt-20-ink-2);
  cursor: pointer;
}

.rt-20__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.rt-20__theme-input:focus-visible + .rt-20__theme-label {
  outline: 2px solid var(--rt-20-acc);
  outline-offset: 2px;
}

.rt-20__bar {
  position: relative;
  z-index: 30;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  min-block-size: 44px;
  padding-inline: 0.6rem;
  min-inline-size: 0;
  background: var(--rt-20-chrome);
  border-block-end: 1px solid var(--rt-20-line);
}

.rt-20__mark {
  inline-size: 16px;
  block-size: 16px;
  flex: none;
  background: var(--rt-20-acc);
  clip-path: polygon(50% 0, 100% 38%, 82% 100%, 18% 100%, 0 38%);
}

.rt-20__menu ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
}

.rt-20__menu button {
  min-block-size: 44px;
  min-inline-size: 44px;
  padding-inline: 0.7rem;
  border: 0;
  background: transparent;
  font: inherit;
  font-size: 0.85rem;
  color: var(--rt-20-ink);
  cursor: pointer;
  white-space: nowrap;
}

.rt-20__menu button:hover {
  background: var(--rt-20-acc);
  color: #ffffff;
}

.rt-20__menu button:focus-visible {
  outline: 2px solid var(--rt-20-acc);
  outline-offset: -3px;
}

.rt-20__clock {
  margin-inline-start: auto;
  font-family: var(--rt-20-mono);
  font-size: 0.75rem;
  color: var(--rt-20-ink-2);
  white-space: nowrap;
  padding-inline-start: 0.5rem;
}

.rt-20__desk {
  position: relative;
  min-block-size: calc(100vh - 44px);
  min-block-size: calc(100svh - 44px);
  padding: 1.1rem clamp(0.6rem, 0.4rem + 1.5vw, 2rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.1rem;
  align-content: start;
  max-inline-size: 76rem;
  margin-inline: auto;
}

.rt-20__icons {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.rt-20__icon {
  inline-size: 92px;
  min-block-size: 88px;
  padding: 0.5rem 0.25rem;
  border: 0;
  cursor: pointer;
  background: transparent;
  color: var(--rt-20-ink);
  font: inherit;
  font-size: 0.72rem;
  line-height: 1.3;
  display: grid;
  justify-items: center;
  gap: 0.4rem;
  border-radius: 6px;
}

.rt-20__icon:hover {
  background: rgba(255,255,255,0.4);
}

.rt-20__icon:focus-visible {
  outline: 2px solid var(--rt-20-acc);
  outline-offset: -2px;
}

.rt-20__gl {
  inline-size: 32px;
  block-size: 26px;
  background: var(--rt-20-acc);
}

.rt-20__gl--folder {
  clip-path: polygon(0 14%, 42% 14%, 50% 0, 100% 0, 100% 100%, 0 100%);
}

.rt-20__gl--doc {
  inline-size: 22px;
  clip-path: polygon(0 0, 70% 0, 100% 24%, 100% 100%, 0 100%);
}

.rt-20__gl--disk {
  clip-path: polygon(0 0, 100% 0, 100% 100%, 0 100%);
  background: linear-gradient(180deg, var(--rt-20-acc) 60%, var(--rt-20-ink-2) 60%);
}

.rt-20__win {
  min-inline-size: 0;
  background: var(--rt-20-surface);
  border: 1px solid var(--rt-20-line);
  border-radius: 10px;
  overflow: hidden;
  translate: var(--rt-20-x) var(--rt-20-y);
  box-shadow: 0 14px 30px -18px rgba(20, 16, 50, 0.6);
  max-inline-size: 34rem;
}

.rt-20__cap {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  min-block-size: 44px;
  padding-inline: 0.7rem;
  background: var(--rt-20-chrome);
  border-block-end: 1px solid var(--rt-20-line);
  cursor: grab;
  touch-action: none;
  min-inline-size: 0;
  user-select: none;
}

.rt-20__cap:active {
  cursor: grabbing;
}

.rt-20__cap:focus-visible {
  outline: 2px solid var(--rt-20-acc);
  outline-offset: -3px;
}

.rt-20__dots {
  display: flex;
  gap: 5px;
  flex: none;
}

.rt-20__dots i {
  inline-size: 10px;
  block-size: 10px;
  border-radius: 50%;
  background: var(--rt-20-line);
}

.rt-20__dots i:first-child {
  background: var(--rt-20-acc);
}

.rt-20__cap-t {
  min-inline-size: 0;
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--rt-20-ink);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.rt-20__body {
  padding: clamp(0.8rem, 0.6rem + 1vw, 1.2rem);
  display: grid;
  gap: 0.7rem;
  min-inline-size: 0;
}

.rt-20__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.4rem;
  min-inline-size: 0;
}

.rt-20__list li {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  justify-content: space-between;
  gap: 0.5rem;
  min-block-size: 44px;
  padding: 0.55rem 0.65rem;
  border-radius: 6px;
  background: var(--rt-20-chrome);
  min-inline-size: 0;
}

.rt-20__li-n {
  font-size: 0.92rem;
  font-weight: 600;
  min-inline-size: 0;
}

.rt-20__li-m {
  font-family: var(--rt-20-mono);
  font-size: 0.72rem;
  color: var(--rt-20-ink-2);
  min-inline-size: 0;
}

.rt-20__p {
  margin: 0;
  font-size: 0.92rem;
  line-height: 1.6;
  color: var(--rt-20-ink);
  min-inline-size: 0;
  text-wrap: pretty;
}

.rt-20__meta {
  margin: 0;
  font-family: var(--rt-20-mono);
  font-size: 0.78rem;
  color: var(--rt-20-acc);
  min-inline-size: 0;
  overflow-wrap: anywhere;
}

.rt-20__legend {
  margin: 0;
  font-size: 0.78rem;
  color: var(--rt-20-ink-2);
  min-inline-size: 0;
  text-wrap: pretty;
}

.rt-20__legend kbd {
  font-family: var(--rt-20-mono);
  font-size: 0.9em;
  padding: 0.1em 0.35em;
  border-radius: 4px;
  border: 1px solid var(--rt-20-line);
  background: var(--rt-20-surface);
}

@media (min-width: 62rem) {
  .rt-20__desk {
    grid-template-columns: 7rem minmax(0, 1fr) minmax(0, 1fr);
    align-items: start;
  }

  .rt-20__icons {
    flex-direction: column;
  }

  .rt-20__legend {
    grid-column: 2 / -1;
  }
}
```

## JavaScript
```js
const root = document.currentScript.closest('.rt-20') || document.querySelector('.rt-20');
const handles = [...root.querySelectorAll('[data-rt20-handle]')];
let zTop = 10;
const win = (h) => h.closest('.rt-20__win');
const num = (el, p) => parseFloat(getComputedStyle(el).getPropertyValue(p)) || 0;
const move = (el, dx, dy) => {
  el.style.setProperty('--rt-20-x', (num(el, '--rt-20-x') + dx) + 'px');
  el.style.setProperty('--rt-20-y', (num(el, '--rt-20-y') + dy) + 'px');
};
const raise = (e) => { zTop += 1; win(e.currentTarget).style.zIndex = String(zTop); };
const onDown = (e) => {
  const el = win(e.currentTarget);
  raise(e);
  let px = e.clientX;
  let py = e.clientY;
  e.currentTarget.setPointerCapture(e.pointerId);
  const onMove = (m) => { move(el, m.clientX - px, m.clientY - py); px = m.clientX; py = m.clientY; };
  const onUp = () => { e.currentTarget.removeEventListener('pointermove', onMove); };
  e.currentTarget.addEventListener('pointermove', onMove);
  e.currentTarget.addEventListener('pointerup', onUp, { once: true });
  e.currentTarget.addEventListener('pointercancel', onUp, { once: true });
};
const onKey = (e) => {
  const step = e.shiftKey ? 48 : 16;
  const map = { ArrowLeft: [-step, 0], ArrowRight: [step, 0], ArrowUp: [0, -step], ArrowDown: [0, step] };
  if (!map[e.key]) return;
  e.preventDefault();
  move(win(e.currentTarget), map[e.key][0], map[e.key][1]);
};
handles.forEach((h) => { h.addEventListener('pointerdown', onDown); h.addEventListener('keydown', onKey); h.addEventListener('focusin', raise); });
root.__rtCleanup = () => handles.forEach((h) => { h.removeEventListener('pointerdown', onDown); h.removeEventListener('keydown', onKey); h.removeEventListener('focusin', raise); });
```
