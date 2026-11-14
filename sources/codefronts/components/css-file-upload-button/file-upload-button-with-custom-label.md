---
source: "codefronts"
url: "https://codefronts.com/components/css-file-upload-button/file-upload-button-with-custom-label/"
title: "File Upload Button with Custom Label"
section: "components"
category: "css-file-upload-button"
category_name: "CSS File Upload Buttons"
description: "The one pattern every other demo in this collection is built on: a visually hidden but still focusable <input type=\"file\"> paired with a <label> you can…"
has_js: "true"
---

Here's a working CSS File Upload Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: File Upload Button with Custom Label
Source: https://codefronts.com/components/css-file-upload-button/file-upload-button-with-custom-label/

The one pattern every other demo in this collection is built on: a visually hidden but still focusable <input type="file"> paired with a <label> you can style like any button. The browser's native picker still opens, the control still lands in the tab order, and screen readers still announce it as a file input — because the input is clipped, not display:none. Hover spins a conic halo through a registered @property angle; focus projects onto the label with an adjacent-sibling selector.
## HTML
```html
<div class="fu-01">
  <button class="fu-01__theme" type="button" aria-pressed="false" aria-label="Switch to dark theme">
    <svg class="fu-01__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="fu-01__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.9 5.9 7.3 7.3M16.7 16.7l1.4 1.4M18.1 5.9l-1.4 1.4M7.3 16.7l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
  </button>
  <div class="fu-01__stack">
    <div class="fu-01__field">
      <input class="fu-01__input" id="fu-01-file" type="file" accept=".pdf,.docx,.rtf" aria-describedby="fu-01-hint">
      <label class="fu-01__label" for="fu-01-file">
        <span class="fu-01__glyph" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" focusable="false">
            <path d="M12 15.5V4.5m0 0L8.2 8.3M12 4.5l3.8 3.8" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M4.5 14.5v3.2A2.3 2.3 0 0 0 6.8 20h10.4a2.3 2.3 0 0 0 2.3-2.3v-3.2" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/>
          </svg>
        </span>
        <span class="fu-01__text">Attach a document</span>
      </label>
    </div>
    <p class="fu-01__hint" id="fu-01-hint">PDF, DOCX or RTF <span aria-hidden="true">·</span> up to 25 MB</p>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

@property --fu-01-spin {
  syntax: '<angle>';
  inherits: false;
  initial-value: 0deg;
}

.fu-01 {
  --bg: #f4f5f8;
  --surface: #ffffff;
  --ink: #0c1016;
  --muted: #616b7a;
  --line: #e3e7ee;
  --acc: #4b34f5;
  --acc-ink: #ffffff;
  --ring: #4b34f5;
  --shadow: rgba(12,16,22,.14);
  --radius: 999px;
  --size: 3.5rem;
  --sans: "Instrument Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: "Geist Mono",ui-monospace,SFMono-Regular,Menlo,monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
  background: radial-gradient(110% 70% at 50% -10%, color-mix(in oklab,var(--acc) 14%,transparent), transparent 62%), var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.fu-01,
.fu-01 *,
.fu-01 *::before,
.fu-01 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0 0 0)) {
  .fu-01 {
    --acc: oklch(52% .26 279);
    --ink: oklch(16% .02 265);
    --muted: oklch(52% .015 265);
  }
}

.fu-01__stack {
  display: grid;
  justify-items: center;
  gap: 1rem;
  text-align: center;
}

.fu-01__field {
  position: relative;
  isolation: isolate;
  border-radius: var(--radius);
}

.fu-01__field::before {
  content: "";
  position: absolute;
  inset: -2px;
  z-index: -1;
  border-radius: inherit;
  background: conic-gradient(from var(--fu-01-spin),
      color-mix(in oklab,var(--acc) 85%,white), color-mix(in oklab,var(--acc) 35%,transparent),
      color-mix(in oklab,var(--acc) 90%,black), color-mix(in oklab,var(--acc) 85%,white));
  opacity: 0;
  transition: opacity .35s ease;
}

.fu-01__field::after {
  content: "";
  position: absolute;
  inset: -14px;
  z-index: -2;
  border-radius: inherit;
  background: radial-gradient(closest-side, color-mix(in oklab,var(--acc) 32%,transparent), transparent);
  opacity: 0;
  transition: opacity .4s ease;
}

.fu-01__field:hover::before,
.fu-01__field:focus-within::before {
  opacity: 1;
  animation: fu-01-spin 4.5s linear infinite;
}

.fu-01__field:hover::after,
.fu-01__field:focus-within::after {
  opacity: 1;
}

@keyframes fu-01-spin {
  to {
    --fu-01-spin: 360deg;
  }
}

.fu-01__input {
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

.fu-01__label {
  display: inline-flex;
  align-items: center;
  gap: .7rem;
  cursor: pointer;
  user-select: none;
  min-block-size: var(--size);
  padding: .75rem 1.6rem .75rem 1.15rem;
  border-radius: var(--radius);
  background: linear-gradient(180deg, color-mix(in oklab,var(--ink) 88%,white), var(--ink));
  color: #fff;
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: -.015em;
  box-shadow: 0 1px 0 color-mix(in oklab,white 22%,transparent) inset, 0 10px 24px -12px var(--shadow), 0 2px 6px -3px var(--shadow);
  transition: transform .28s cubic-bezier(.16,1,.3,1), box-shadow .28s ease, background .28s ease;
}

.fu-01__label:hover {
  transform: translateY(-2px);
  box-shadow: 0 1px 0 color-mix(in oklab,white 26%,transparent) inset, 0 20px 34px -16px var(--shadow), 0 4px 10px -4px var(--shadow);
}

.fu-01__label:active {
  transform: translateY(0) scale(.985);
}

.fu-01__input:focus-visible + .fu-01__label {
  outline: 2px solid var(--ring);
  outline-offset: 3px;
}

.fu-01__glyph {
  display: grid;
  place-items: center;
  inline-size: 2rem;
  block-size: 2rem;
  border-radius: 999px;
  flex: none;
  background: color-mix(in oklab,var(--acc) 78%,white);
  color: #fff;
  transition: transform .3s cubic-bezier(.16,1,.3,1), background .3s ease;
}

.fu-01__glyph svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.fu-01__label:hover .fu-01__glyph {
  transform: translateY(-2px);
  background: var(--acc);
}

.fu-01__text {
  padding-block: .05em;
}

@supports (text-box-trim: trim-both) {
  .fu-01__text {
    text-box-trim: trim-both;
    text-box-edge: cap alphabetic;
    padding-block: 0;
  }
}

.fu-01__hint {
  margin: 0;
  font-family: var(--mono);
  font-size: .75rem;
  letter-spacing: .02em;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.fu-01__hint span {
  margin-inline: .35rem;
  opacity: .6;
}

@media (prefers-color-scheme: dark) {
  .fu-01:not([data-theme="light"]) {
    --bg: #080a0f;
    --surface: #11141b;
    --ink: #f3f5f9;
    --muted: #8f98a8;
    --line: #232936;
    --acc: #8f7bff;
    --shadow: rgba(0,0,0,.6);
  }

  .fu-01:not([data-theme="light"]) .fu-01__label {
    background: linear-gradient(180deg,#1b2130,#12161f);
    color: #f3f5f9;
    box-shadow: 0 1px 0 color-mix(in oklab,white 10%,transparent) inset, 0 18px 34px -18px #000;
  }
}

.fu-01[data-theme="dark"] {
  --bg: #080a0f;
  --surface: #11141b;
  --ink: #f3f5f9;
  --muted: #8f98a8;
  --line: #232936;
  --acc: #8f7bff;
  --shadow: rgba(0,0,0,.6);
}

.fu-01[data-theme="dark"] .fu-01__label {
  background: linear-gradient(180deg,#1b2130,#12161f);
  color: #f3f5f9;
  box-shadow: 0 1px 0 color-mix(in oklab,white 10%,transparent) inset, 0 18px 34px -18px #000;
}

@media (prefers-reduced-motion: reduce) {
  .fu-01 * {
    animation: none !important;
    transition: none !important;
  }

  .fu-01__label:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-01__label {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }

  .fu-01__glyph {
    background: Highlight;
    color: HighlightText;
  }

  .fu-01__field::before,
    .fu-01__field::after {
    display: none;
  }
}
/* ── in-demo theme toggle ── */

.fu-01 {
  position: relative;
}

.fu-01__theme {
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

.fu-01__theme:hover {
  background: color-mix(in oklab,currentColor 22%,transparent);
  border-color: color-mix(in oklab,currentColor 55%,transparent);
  transform: translateY(-1px);
}

.fu-01__theme:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.fu-01__theme svg {
  grid-area: 1/1;
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.fu-01__sun {
  display: none;
}

.fu-01__theme[aria-pressed="true"] .fu-01__sun {
  display: block;
}

.fu-01__theme[aria-pressed="true"] .fu-01__moon {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .fu-01__theme {
    transition: none;
  }

  .fu-01__theme:hover {
    transform: none;
  }
}

@media (forced-colors: active) {
  .fu-01__theme {
    border: 1px solid ButtonText;
    background: ButtonFace;
    color: ButtonText;
  }
}
```

## JavaScript
```js
(() => {                                      // in-demo light/dark toggle
  const root = document.querySelector('.fu-01');
  const btn = root && root.querySelector('.fu-01__theme');
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
