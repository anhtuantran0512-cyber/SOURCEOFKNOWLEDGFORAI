---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/scale-zoom-transition/"
title: "Zoom Page Transition Scale In and Out"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "A scale-based route change: the outgoing screen recedes slightly and the incoming one arrives from just under full size."
has_js: "false"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Zoom Page Transition Scale In and Out
Source: https://codefronts.com/motion/css-page-transitions/scale-zoom-transition/

A scale-based route change: the outgoing screen recedes slightly and the incoming one arrives from just under full size. It carries more weight than a fade and suits full-bleed, single-purpose surfaces like a kiosk or a display screen. The one thing to know is that scaling a full route can soften text mid-animation unless the transform lands on whole pixels.
## HTML
```html
<section class="pt-12" aria-labelledby="pt-12-h">
  <div class="pt-12__theme">
    <input class="pt-12__theme-input" type="checkbox" id="pt-12-theme">
    <label class="pt-12__theme-label" for="pt-12-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-12__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-12__stage">
    <header class="pt-12__head">
      <p class="pt-12__kicker">Page transitions / 12</p>
      <h2 class="pt-12__h" id="pt-12-h">Scale, but only a little</h2>
      <p class="pt-12__lede">A kiosk surface, swapped with no script. Screens are DOM sections held by radio inputs; nothing navigates.</p>
    </header>

    <div class="pt-12__kiosk">
      <div class="pt-12__view">
        <div class="pt-12__veil" aria-hidden="true"></div>
        <main class="pt-12__screen pt-12__screen--1">
          <p class="pt-12__eyebrow">Vale Museum &middot; West Wing</p>
          <h3 class="pt-12__title">Now showing</h3>
          <p class="pt-12__big">Light and Water</p>
          <p class="pt-12__text">Fourteen works on paper, 1911 to 1934. Gallery 4, until the end of November.</p>
        </main>
        <main class="pt-12__screen pt-12__screen--2">
          <p class="pt-12__eyebrow">Vale Museum &middot; Visit</p>
          <h3 class="pt-12__title">Today</h3>
          <p class="pt-12__big">10:00 &ndash; 18:00</p>
          <p class="pt-12__text">Last entry 17:15. The cafe closes at 17:30 and the west stair is closed for maintenance.</p>
        </main>
        <main class="pt-12__screen pt-12__screen--3">
          <p class="pt-12__eyebrow">Vale Museum &middot; Wayfinding</p>
          <h3 class="pt-12__title">Getting there</h3>
          <p class="pt-12__big">Gallery 4</p>
          <p class="pt-12__text">Up the main stair, left at the reading room, through the double doors. Step-free route via the east lift.</p>
        </main>
      </div>

      <nav class="pt-12__pads" aria-label="Kiosk screens">
        <input class="pt-12__radio" type="radio" name="pt-12-r" id="pt-12-r1" checked>
        <label class="pt-12__pad" for="pt-12-r1">Now showing</label>
        <input class="pt-12__radio" type="radio" name="pt-12-r" id="pt-12-r2">
        <label class="pt-12__pad" for="pt-12-r2">Today</label>
        <input class="pt-12__radio" type="radio" name="pt-12-r" id="pt-12-r3">
        <label class="pt-12__pad" for="pt-12-r3">Getting there</label>
      </nav>
    </div>

    <p class="pt-12__note">Both screens end on exactly <code>scale(1)</code>. That final frame is what makes the type sharp again &mdash; while the scale is running, glyphs are resampled and slightly soft.</p>
  </div>
</section>
```
## CSS
```css
.pt-12 {
  --pt-12-bg: #efe7de;
  --pt-12-s1: #fbf7f2;
  --pt-12-s2: #e3d7c9;
  --pt-12-line: #c8b6a2;
  --pt-12-ink: #2e2216;
  --pt-12-mut: #6d5b47;
  --pt-12-acc: #8a4b23;
  --pt-12-dur: 420ms;
  --pt-12-font-display: "Rockwell", "Roboto Slab", Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--pt-12-bg);
  color: var(--pt-12-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.pt-12 *,
.pt-12 *::before,
.pt-12 *::after {
  box-sizing: border-box;
}

.pt-12:has(.pt-12__theme-input:checked) {
  --pt-12-bg: #16110c;
  --pt-12-s1: #1e1811;
  --pt-12-s2: #2a2118;
  --pt-12-line: #40332a;
  --pt-12-ink: #f2e8dc;
  --pt-12-mut: #ab9781;
  --pt-12-acc: #e0965f;
}

@media (prefers-color-scheme: dark) {
  .pt-12 {
    --pt-12-bg: #16110c;
    --pt-12-s1: #1e1811;
    --pt-12-s2: #2a2118;
    --pt-12-line: #40332a;
    --pt-12-ink: #f2e8dc;
    --pt-12-mut: #ab9781;
    --pt-12-acc: #e0965f;
  }

  .pt-12:has(.pt-12__theme-input:checked) {
    --pt-12-bg: #efe7de;
    --pt-12-s1: #fbf7f2;
    --pt-12-s2: #e3d7c9;
    --pt-12-line: #c8b6a2;
    --pt-12-ink: #2e2216;
    --pt-12-mut: #6d5b47;
    --pt-12-acc: #8a4b23;
  }
}

@media (prefers-color-scheme: light) {
  .pt-12:has(.pt-12__theme-input:checked) {
    --pt-12-bg: #16110c;
    --pt-12-s1: #1e1811;
    --pt-12-s2: #2a2118;
    --pt-12-line: #40332a;
    --pt-12-ink: #f2e8dc;
    --pt-12-mut: #ab9781;
    --pt-12-acc: #e0965f;
  }
}

@supports (color: oklch(0.5 0.12 50)) {
  .pt-12 {
    --pt-12-acc: oklch(0.48 0.12 48);
  }

  .pt-12:has(.pt-12__theme-input:checked) {
    --pt-12-acc: oklch(0.76 0.11 55);
  }

  @media (prefers-color-scheme: dark) {
    .pt-12 {
      --pt-12-acc: oklch(0.76 0.11 55);
    }

    .pt-12:has(.pt-12__theme-input:checked) {
      --pt-12-acc: oklch(0.48 0.12 48);
    }
  }
}

.pt-12__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-12__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 9;
}

.pt-12__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-12__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 2px solid var(--pt-12-ink);
  background: var(--pt-12-s1);
  color: var(--pt-12-ink);
  cursor: pointer;
  box-shadow: 5px 5px 0 var(--pt-12-ink);
}

.pt-12__theme-label svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.pt-12__theme-input:focus-visible + .pt-12__theme-label {
  outline: 2px solid var(--pt-12-acc);
  outline-offset: 3px;
}

.pt-12__stage {
  max-inline-size: 60rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.25rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.5rem;
}

.pt-12__kicker {
  margin: 0 0 0.45rem;
  font-family: var(--pt-12-font-display);
  font-size: 0.75rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--pt-12-acc);
}

.pt-12__h {
  margin: 0 0 0.5rem;
  font-family: var(--pt-12-font-display);
  font-size: clamp(1.5rem, 4.8vw, 2.3rem);
  font-weight: 700;
  letter-spacing: -0.01em;
}

.pt-12__lede {
  margin: 0;
  max-inline-size: 40rem;
  color: var(--pt-12-mut);
  font-size: 0.94rem;
  text-wrap: pretty;
}

.pt-12__kiosk {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 0.9rem;
}

.pt-12__view {
  position: relative;
  overflow: hidden;
  min-inline-size: 0;
  block-size: 19rem;
  background: var(--pt-12-s1);
  border: 2px solid var(--pt-12-ink);
  box-shadow: 10px 10px 0 var(--pt-12-line);
}

.pt-12__veil {
  position: absolute;
  inset: 0;
  z-index: 3;
  background: var(--pt-12-bg);
  opacity: 0;
  pointer-events: none;
}

.pt-12__screen {
  position: absolute;
  inset: 0;
  display: none;
  padding: clamp(1.2rem, 4vw, 2.2rem);
  align-content: center;
}

.pt-12__eyebrow {
  margin: 0 0 0.6rem;
  font-family: var(--pt-12-font-display);
  font-size: 0.78rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--pt-12-acc);
}

.pt-12__title {
  margin: 0 0 0.2rem;
  font-size: 0.95rem;
  font-weight: 400;
  color: var(--pt-12-mut);
}

.pt-12__big {
  margin: 0 0 0.7rem;
  font-family: var(--pt-12-font-display);
  font-size: clamp(1.8rem, 7vw, 3rem);
  font-weight: 700;
  line-height: 1.05;
  letter-spacing: -0.02em;
}

.pt-12__text {
  margin: 0;
  max-inline-size: 34rem;
  font-size: 0.95rem;
  color: var(--pt-12-mut);
  text-wrap: pretty;
}

.pt-12__pads {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.pt-12__radio {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
}

.pt-12__pad {
  flex: 1 1 8rem;
  min-inline-size: 0;
  min-block-size: 2.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0.5rem 0.9rem;
  background: var(--pt-12-s2);
  border: 2px solid var(--pt-12-ink);
  font-family: var(--pt-12-font-display);
  font-size: 0.85rem;
  letter-spacing: 0.04em;
  cursor: pointer;
}

.pt-12__radio:checked + .pt-12__pad {
  background: var(--pt-12-ink);
  color: var(--pt-12-s1);
  box-shadow: 4px 4px 0 var(--pt-12-line);
}

.pt-12__radio:focus-visible + .pt-12__pad {
  outline: 2px solid var(--pt-12-acc);
  outline-offset: 3px;
}

.pt-12__note {
  margin: 0;
  font-size: 0.86rem;
  color: var(--pt-12-mut);
  max-inline-size: 46rem;
  text-wrap: pretty;
}

.pt-12__note code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.86em;
}

.pt-12__kiosk:has(#pt-12-r1:checked) .pt-12__screen--1,
.pt-12__kiosk:has(#pt-12-r2:checked) .pt-12__screen--2,
.pt-12__kiosk:has(#pt-12-r3:checked) .pt-12__screen--3 {
  display: grid;
}

.pt-12__kiosk:has(#pt-12-r1:checked) .pt-12__screen--1 {
  animation: pt-12-zoom-1 var(--pt-12-dur) cubic-bezier(0.2, 0.8, 0.2, 1) both;
}

.pt-12__kiosk:has(#pt-12-r2:checked) .pt-12__screen--2 {
  animation: pt-12-zoom-2 var(--pt-12-dur) cubic-bezier(0.2, 0.8, 0.2, 1) both;
}

.pt-12__kiosk:has(#pt-12-r3:checked) .pt-12__screen--3 {
  animation: pt-12-zoom-3 var(--pt-12-dur) cubic-bezier(0.2, 0.8, 0.2, 1) both;
}

.pt-12__kiosk:has(#pt-12-r1:checked) .pt-12__veil {
  animation: pt-12-veil-1 var(--pt-12-dur) linear both;
}

.pt-12__kiosk:has(#pt-12-r2:checked) .pt-12__veil {
  animation: pt-12-veil-2 var(--pt-12-dur) linear both;
}

.pt-12__kiosk:has(#pt-12-r3:checked) .pt-12__veil {
  animation: pt-12-veil-3 var(--pt-12-dur) linear both;
}

@keyframes pt-12-zoom-1 {
  0%,
    35% {
    opacity: 0;
    transform: scale(1.045);
  }

  100% {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes pt-12-zoom-2 {
  0%,
    35% {
    opacity: 0;
    transform: scale(1.045);
  }

  100% {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes pt-12-zoom-3 {
  0%,
    35% {
    opacity: 0;
    transform: scale(1.045);
  }

  100% {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes pt-12-veil-1 {
  0% {
    opacity: 0;
  }

  30% {
    opacity: 1;
  }

  100% {
    opacity: 0;
  }
}

@keyframes pt-12-veil-2 {
  0% {
    opacity: 0;
  }

  30% {
    opacity: 1;
  }

  100% {
    opacity: 0;
  }
}

@keyframes pt-12-veil-3 {
  0% {
    opacity: 0;
  }

  30% {
    opacity: 1;
  }

  100% {
    opacity: 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pt-12 {
    --pt-12-dur: 110ms;
  }

  @keyframes pt-12-zoom-1 {
    from {
      opacity: 0.4;
      transform: scale(1);
    }

    to {
      opacity: 1;
      transform: scale(1);
    }
  }

  @keyframes pt-12-zoom-2 {
    from {
      opacity: 0.4;
      transform: scale(1);
    }

    to {
      opacity: 1;
      transform: scale(1);
    }
  }

  @keyframes pt-12-zoom-3 {
    from {
      opacity: 0.4;
      transform: scale(1);
    }

    to {
      opacity: 1;
      transform: scale(1);
    }
  }
}
```
