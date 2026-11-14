---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-brutalist-concrete-slab-button/"
title: "CSS Brutalist Concrete Slab Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "Board-formed concrete: horizontal shutter lines from the timber mould, aggregate speckle scattered through the mix, chipped corners cut by clip-path, and a…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Brutalist Concrete Slab Button
Source: https://codefronts.com/components/css-buttons/css-brutalist-concrete-slab-button/

Board-formed concrete: horizontal shutter lines from the timber mould, aggregate speckle scattered through the mix, chipped corners cut by clip-path, and a press that drops the slab into its own shadow with a puff of dust at the base.
## HTML
```html
<div class="cb-30">
  <div class="cb-30__stage">
    <button class="cb-30__btn" type="button">
      <span class="cb-30__dust" aria-hidden="true"></span>
      <span class="cb-30__label">Pour it</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Archivo:wght@600;700&display=swap');

.cb-30 {
  --bg: #c9c6c0;
  --grey: #8f8d88;
  --grey-hi: #a8a6a1;
  --grey-lo: #5d5b57;
  --fleck: #e6e3dc;
  --fleck-2: #54524e;
  --ink: #141412;
  --sans: "Archivo Black",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: repeating-linear-gradient(0deg, rgba(0,0,0,.035) 0 1px, transparent 1px 22px), var(--bg);
  font-family: var(--sans);
}

@supports (color: oklch(50% 0 0)) {
  .cb-30 {
    --bg: oklch(82% .004 85);
    --grey: oklch(62% .004 85);
    --grey-hi: oklch(70% .004 85);
    --grey-lo: oklch(44% .004 85);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-30:not([data-theme="light"]) {
    --bg: #2e2d2b;
    --grey: #514f4c;
    --grey-hi: #615f5b;
    --grey-lo: #2f2e2c;
    --fleck: #8c8983;
    --fleck-2: #26251f;
    --ink: #f2f0eb;
  }
}

.cb-30[data-theme="dark"] {
  --bg: #2e2d2b;
  --grey: #514f4c;
  --grey-hi: #615f5b;
  --grey-lo: #2f2e2c;
  --fleck: #8c8983;
  --fleck-2: #26251f;
  --ink: #f2f0eb;
}

.cb-30,
.cb-30 *,
.cb-30 *::before,
.cb-30 *::after {
  box-sizing: border-box;
}

.cb-30__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-30__btn {
  position: relative;
  cursor: pointer;
  display: grid;
  place-items: center;
  min-height: 4.5rem;
  padding: 0 3rem;
  border: 0;
  clip-path: polygon(2.5% 0,100% 0,100% 88%,97% 100%,0 100%,0 9%);
  font: inherit;
  font-size: 1.25rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--ink);
  background-color: var(--grey);
  background-image: radial-gradient(.055rem .055rem at 18% 32%, color-mix(in oklab,var(--fleck) 55%,transparent) 99%, transparent), radial-gradient(.045rem .045rem at 62% 71%, color-mix(in oklab,var(--fleck-2) 45%,transparent) 99%, transparent), radial-gradient(.04rem .04rem at 84% 18%, color-mix(in oklab,var(--fleck) 40%,transparent) 99%, transparent), repeating-linear-gradient(0deg, rgba(0,0,0,.07) 0 1px, transparent 1px 14px), linear-gradient(168deg, var(--grey-hi), var(--grey) 55%, var(--grey-lo));
  background-size: 13px 13px, 19px 19px, 29px 29px, 100% 100%, 100% 100%;
  text-shadow: 0 1px 0 rgba(255,255,255,.28), 0 -1px 0 rgba(0,0,0,.3);
  box-shadow: 0 8px 0 0 var(--grey-lo), 0 16px 22px -8px rgba(0,0,0,.5);
  transition: translate .1s linear, box-shadow .1s linear, filter .25s ease;
}

.cb-30__label {
  position: relative;
  z-index: 2;
}

.cb-30__btn:hover {
  filter: brightness(1.05);
}

.cb-30__btn:focus-visible {
  outline: 4px solid var(--ink);
  outline-offset: 6px;
}

.cb-30__btn:active {
  translate: 0 8px;
  box-shadow: 0 0 0 0 var(--grey-lo), 0 4px 8px -4px rgba(0,0,0,.5);
}

.cb-30__dust {
  position: absolute;
  left: 50%;
  bottom: -.35rem;
  width: 9rem;
  height: 1.1rem;
  margin-left: -4.5rem;
  border-radius: 50%;
  pointer-events: none;
  opacity: 0;
  background: radial-gradient(closest-side, rgba(255,255,255,.85), transparent 72%);
  filter: blur(4px);
}

.cb-30__btn:active .cb-30__dust {
  animation: cb-30-dust .55s ease-out;
}

@keyframes cb-30-dust {
  0% {
    opacity: .85;
    scale: .4 .5;
  }

  100% {
    opacity: 0;
    scale: 1.5 1.3;
  }
}

.cb-30__btn:disabled {
  cursor: not-allowed;
  filter: grayscale(.5) brightness(.85);
  box-shadow: 0 4px 0 0 var(--grey-lo);
}

@media (prefers-reduced-motion: reduce) {
  .cb-30__btn {
    transition: none;
  }

  .cb-30__dust {
    display: none;
  }
}

@media (forced-colors: active) {
  .cb-30__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 2px solid ButtonText;
    box-shadow: none;
    text-shadow: none;
    clip-path: none;
  }

  .cb-30__dust {
    display: none;
  }
}
```
