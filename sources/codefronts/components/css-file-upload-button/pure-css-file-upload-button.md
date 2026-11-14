---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/pure-css-file-upload-button/"
title: "Pure CSS File Upload Button"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "Most \"pure CSS\" upload buttons stop at styling the label — they cannot tell you whether a file was actually picked."
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Pure CSS File Upload Button
Source: https://codefronts.com/components/css-file-upload-button/pure-css-file-upload-button/

Most "pure CSS" upload buttons stop at styling the label — they cannot tell you whether a file was actually picked. This one can. A required file input is :invalid while empty and flips to :valid the moment the user chooses something, so :has(input:required:valid) swaps the entire card into its attached state — checkmark, colour, copy and a @starting-style pop — with zero JavaScript.
## HTML
```html
<div class="fu-02" id="fu-02">
  <button class="fu-02__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-02__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-02__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <div class="fu-02__card">
    <div class="fu-02__top">
      <span class="fu-02__tag">Step 2 of 3</span>
      <span class="fu-02__dots" aria-hidden="true"><i></i><i></i><i></i></span>
    </div>

    <input class="fu-02__input" id="fu-02-file" type="file" accept="image/png,image/jpeg,application/pdf" required aria-describedby="fu-02-hint">
    <label class="fu-02__label" for="fu-02-file">
      <span class="fu-02__box" aria-hidden="true">
        <svg class="fu-02__plus" viewBox="0 0 24 24" fill="none" focusable="false"><path d="M12 5.5v13M5.5 12h13" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"/></svg>
        <svg class="fu-02__tick" viewBox="0 0 24 24" fill="none" focusable="false"><path d="m5.5 12.5 4.2 4.2 8.8-9.4" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </span>
      <span class="fu-02__labelText">Choose a file</span>
    </label>

    <div class="fu-02__msg">
      <p class="fu-02__idle" id="fu-02-hint">PNG, JPG or PDF <span aria-hidden="true">—</span> nothing attached yet</p>
      <p class="fu-02__done">File attached <span aria-hidden="true">—</span> <a href="#fu-02">pick a different one</a></p>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

.fu-02 {
  --bg: #eeeade;
  --surface: #fffdf7;
  --ink: #141210;
  --muted: #6d6559;
  --line: #141210;
  --acc: #ff5a1f;
  --ok: #0f9d58;
  --state: var(--ink);
  --offset: 5px;
  --sans: "Space Grotesk",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "JetBrains Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background-color: var(--bg);
  background-image: linear-gradient(color-mix(in oklab,var(--ink) 6%,transparent) 1px, transparent 1px), linear-gradient(90deg, color-mix(in oklab,var(--ink) 6%,transparent) 1px, transparent 1px);
  background-size: 28px 28px, 28px 28px;
  color: var(--ink);
  font-family: var(--sans);
}

.fu-02,
.fu-02 *,
.fu-02 *::before,
.fu-02 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .fu-02 {
    --acc: oklch(66% .21 42);
    --ok: oklch(58% .16 152);
  }
}

.fu-02__card {
  inline-size: min(26rem,100%);
  display: grid;
  gap: 1.1rem;
  padding: 1.5rem;
  background: var(--surface);
  border: 2px solid var(--line);
  border-radius: 1.25rem;
  box-shadow: var(--offset) var(--offset) 0 var(--state);
  transition: box-shadow .35s cubic-bezier(.16,1,.3,1), border-color .35s ease;
}

.fu-02__top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.fu-02__tag {
  font-family: var(--mono);
  font-size: .6875rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  padding: .3rem .55rem;
  border-radius: .4rem;
  border: 1.5px solid var(--line);
  background: color-mix(in oklab,var(--state) 12%,transparent);
}

.fu-02__dots {
  display: inline-flex;
  gap: .3rem;
}

.fu-02__dots i {
  inline-size: .5rem;
  block-size: .5rem;
  border-radius: 999px;
  border: 1.5px solid var(--line);
}

.fu-02__dots i:nth-child(-n+2) {
  background: var(--line);
}

.fu-02__input {
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

.fu-02__label {
  display: flex;
  align-items: center;
  gap: .9rem;
  cursor: pointer;
  user-select: none;
  min-block-size: 3.5rem;
  padding: .7rem 1.1rem;
  border-radius: .9rem;
  border: 2px solid var(--line);
  background: color-mix(in oklab,var(--state) 8%,var(--surface));
  font-size: 1.0625rem;
  font-weight: 600;
  letter-spacing: -.01em;
  transition: background .3s ease, transform .2s cubic-bezier(.16,1,.3,1), box-shadow .2s ease;
}

.fu-02__label:hover {
  background: color-mix(in oklab,var(--state) 16%,var(--surface));
  transform: translate(-2px,-2px);
  box-shadow: 2px 2px 0 var(--state);
}

.fu-02__label:active {
  transform: translate(0,0);
  box-shadow: none;
}

.fu-02__input:focus-visible + .fu-02__label {
  outline: 2px solid var(--acc);
  outline-offset: 3px;
}

.fu-02__box {
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  flex: none;
  border-radius: .65rem;
  border: 2px solid var(--line);
  background: var(--surface);
  color: var(--state);
}

.fu-02__box svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
  grid-area: 1/1;
}

.fu-02__tick {
  display: none;
}

.fu-02__msg {
  min-block-size: 1.5rem;
}

.fu-02__idle,
.fu-02__done {
  margin: 0;
  font-family: var(--mono);
  font-size: .75rem;
  line-height: 1.5;
  color: var(--muted);
}

.fu-02__done {
  display: none;
}

.fu-02__done a {
  color: var(--ink);
  text-decoration: underline;
  text-underline-offset: 3px;
}
/* ── the pure-CSS "file selected" state ── */

.fu-02__card:has(.fu-02__input:required:valid) {
  --state: var(--ok);
}

.fu-02__card:has(.fu-02__input:required:valid) .fu-02__labelText::after {
  content: " — attached";
}

.fu-02__card:has(.fu-02__input:required:valid) .fu-02__plus {
  display: none;
}

.fu-02__card:has(.fu-02__input:required:valid) .fu-02__tick {
  display: block;
}

.fu-02__card:has(.fu-02__input:required:valid) .fu-02__idle {
  display: none;
}

.fu-02__card:has(.fu-02__input:required:valid) .fu-02__done {
  display: block;
  color: color-mix(in oklab,var(--ok) 70%,var(--ink));
  transition: opacity .35s ease, transform .35s cubic-bezier(.16,1,.3,1);
}

@starting-style {
  .fu-02__card:has(.fu-02__input:required:valid) .fu-02__done {
    opacity: 0;
    transform: translateY(6px);
  }

  .fu-02__card:has(.fu-02__input:required:valid) .fu-02__tick {
    opacity: 0;
  }
}

.fu-02__card:has(.fu-02__input:required:valid) .fu-02__tick {
  transition: opacity .3s ease .05s;
}

@media (prefers-color-scheme: dark) {
  .fu-02:not([data-theme="light"]) {
    --bg: #0e0d0b;
    --surface: #191713;
    --ink: #f6f2e8;
    --muted: #a29a8b;
    --line: #f6f2e8;
    --acc: #ff7a45;
    --ok: #38d67f;
  }
}

.fu-02[data-theme="dark"] {
  --bg: #0e0d0b;
  --surface: #191713;
  --ink: #f6f2e8;
  --muted: #a29a8b;
  --line: #f6f2e8;
  --acc: #ff7a45;
  --ok: #38d67f;
}

@media (prefers-reduced-motion: reduce) {
  .fu-02 * {
    animation: none !important;
    transition: none !important;
  }

  .fu-02__label:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-02__card,
    .fu-02__label,
    .fu-02__box {
    border: 2px solid CanvasText;
  }

  .fu-02__dots i:nth-child(-n+2) {
    background: CanvasText;
  }
}
/* ── in-demo theme toggle ── */

.fu-02 {
  position: relative;
}

.fu-02__theme {
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

.fu-02__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-02__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-02__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-02__sun {
  display: none;
}

.fu-02__theme[aria-pressed="true"] .fu-02__sun {
  display: block;
}

.fu-02__theme[aria-pressed="true"] .fu-02__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-02__theme {
    transition: none;
  }

  .fu-02__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-02__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-02');
  const btn = root && root.querySelector('.fu-02__theme');
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
