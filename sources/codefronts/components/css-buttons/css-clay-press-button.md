---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-clay-press-button/"
title: "CSS Clay Press Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "Fat, matte, extruded clay: two inner shadows carve the highlight and the shade, an outer shadow grounds it, and pressing squashes the shape on both axes so…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Clay Press Button
Source: https://codefronts.com/components/css-buttons/css-clay-press-button/

Fat, matte, extruded clay: two inner shadows carve the highlight and the shade, an outer shadow grounds it, and pressing squashes the shape on both axes so it deforms like real material instead of just moving down.
## HTML
```html
<div class="cb-18">
  <div class="cb-18__stage">
    <button class="cb-18__btn" type="button">
      <span class="cb-18__ico" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 5v14M5 12h14"/></svg>
      </span>
      <span>Make something</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@600;700;800&display=swap');

.cb-18 {
  --bg: #e8ecf7;
  --clay: #7c8cf8;
  --deep: #2a3480;
  --ink: #ffffff;
  --chip: #fbbf24;
  --radius: 1.5rem;
  --spring: linear(0,.38 7%,.82 15%,1.08 23%,1.12 28%,1.05 37%,1 52%,1);
  --sans: "Nunito",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(30rem 20rem at 50% 40%, #ffffff, transparent 70%), var(--bg);
  font-family: var(--sans);
}

@supports (color: oklch(50% 0 0)) {
  .cb-18 {
    --bg: oklch(93.5% .02 265);
    --clay: oklch(68% .16 275);
    --deep: oklch(35% .14 275);
    --chip: oklch(84% .16 82);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-18:not([data-theme="light"]) {
    --bg: #181b28;
    --clay: #5b68d8;
    --deep: #080a16;
  }
}

.cb-18[data-theme="dark"] {
  --bg: #181b28;
  --clay: #5b68d8;
  --deep: #080a16;
}

.cb-18,
.cb-18 *,
.cb-18 *::before,
.cb-18 *::after {
  box-sizing: border-box;
}

.cb-18__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-18__btn {
  cursor: pointer;
  display: grid;
  grid-auto-flow: column;
  align-items: center;
  gap: .7rem;
  min-height: 4rem;
  padding: 0 2rem 0 1.4rem;
  border: 0;
  border-radius: var(--radius);
  font: inherit;
  font-size: 1.0625rem;
  font-weight: 800;
  letter-spacing: -.01em;
  color: var(--ink);
  background: var(--clay);
  box-shadow: inset 8px 8px 16px color-mix(in oklab,white 45%,transparent), inset -10px -10px 20px color-mix(in oklab,var(--deep) 42%,transparent), 0 18px 32px -16px color-mix(in oklab,var(--deep) 65%,transparent);
  transition: translate .35s cubic-bezier(.16,1,.3,1), scale .35s cubic-bezier(.16,1,.3,1), box-shadow .3s ease;
  -webkit-tap-highlight-color: transparent;
}

@supports (transition-timing-function: linear(0,1)) {
  .cb-18__btn {
    transition: translate .5s var(--spring), scale .5s var(--spring), box-shadow .3s ease;
  }
}

.cb-18__ico {
  display: grid;
  place-items: center;
  width: 2.1rem;
  height: 2.1rem;
  border-radius: 50%;
  color: var(--deep);
  background: var(--chip);
  box-shadow: inset 3px 3px 6px color-mix(in oklab,white 55%,transparent), inset -3px -3px 6px color-mix(in oklab,var(--deep) 30%,transparent);
  transition: rotate .5s cubic-bezier(.16,1,.3,1);
}

.cb-18__ico svg {
  width: 1.05rem;
  height: 1.05rem;
}

.cb-18__btn:hover {
  translate: 0 -3px;
}

.cb-18__btn:hover .cb-18__ico {
  rotate: 90deg;
}

.cb-18__btn:active {
  scale: .96 .9;
  translate: 0 2px;
  box-shadow: inset 7px 7px 15px color-mix(in oklab,var(--deep) 38%,transparent), inset -7px -7px 14px color-mix(in oklab,white 32%,transparent), 0 6px 12px -10px color-mix(in oklab,var(--deep) 60%,transparent);
}

.cb-18__btn:focus-visible {
  outline: 3px solid color-mix(in oklab,var(--deep) 60%,var(--clay));
  outline-offset: 5px;
}

.cb-18__btn:disabled {
  cursor: not-allowed;
  filter: grayscale(.6);
  opacity: .6;
}

@media (prefers-reduced-motion: reduce) {
  .cb-18__btn,
    .cb-18__ico {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-18__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .cb-18__ico {
    box-shadow: none;
    border: 1px solid ButtonText;
  }
}
```
