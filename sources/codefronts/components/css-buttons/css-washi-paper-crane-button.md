---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-washi-paper-crane-button/"
title: "CSS Washi Paper Crane Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "Handmade washi stock with fibrous speckle, a deckled bottom edge cut by a mask, and a folded paper wing that lifts off the corner on hover — the crane's fold…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Washi Paper Crane Button
Source: https://codefronts.com/components/css-buttons/css-washi-paper-crane-button/

Handmade washi stock with fibrous speckle, a deckled bottom edge cut by a mask, and a folded paper wing that lifts off the corner on hover — the crane's fold lines are a single conic-gradient shading pass, and the whole button tilts on its long axis like a sheet being picked up.
## HTML
```html
<div class="cb-22">
  <div class="cb-22__stage">
    <button class="cb-22__btn" type="button">
      <span class="cb-22__crane" aria-hidden="true"><span class="cb-22__wing"></span></span>
      <span class="cb-22__label">Send a note</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Zen+Maru+Gothic:wght@400;500;700&display=swap');

.cb-22 {
  --bg: #efe9df;
  --paper: #fbf7f0;
  --fibre: #cdbfa8;
  --ink: #2c2620;
  --accent: #b4573f;
  --radius: .35rem;
  --sans: "Zen Maru Gothic",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(50rem 30rem at 50% 20%, color-mix(in oklab,white 60%,transparent), transparent 65%), var(--bg);
  font-family: var(--sans);
}

@supports (color: oklch(50% 0 0)) {
  .cb-22 {
    --bg: oklch(93.5% .012 85);
    --paper: oklch(97.5% .01 85);
    --fibre: oklch(80% .022 78);
    --accent: oklch(55% .13 35);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-22:not([data-theme="light"]) {
    --bg: #1b1815;
    --paper: #272220;
    --fibre: #463d34;
    --ink: #f2ece2;
    --accent: #e08a6f;
  }
}

.cb-22[data-theme="dark"] {
  --bg: #1b1815;
  --paper: #272220;
  --fibre: #463d34;
  --ink: #f2ece2;
  --accent: #e08a6f;
}

.cb-22,
.cb-22 *,
.cb-22 *::before,
.cb-22 *::after {
  box-sizing: border-box;
}

.cb-22__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-22__btn {
  position: relative;
  cursor: pointer;
  display: grid;
  grid-auto-flow: column;
  align-items: center;
  gap: .85rem;
  min-height: 3.5rem;
  padding: .9rem 1.9rem 1.1rem;
  border: 0;
  border-radius: var(--radius);
  font: inherit;
  font-size: 1rem;
  font-weight: 500;
  letter-spacing: .03em;
  color: var(--ink);
  background-color: var(--paper);
  background-image: radial-gradient(.05rem .05rem at 12% 24%, color-mix(in oklab,var(--fibre) 45%,transparent) 99%, transparent), radial-gradient(.04rem .04rem at 63% 71%, color-mix(in oklab,var(--fibre) 35%,transparent) 99%, transparent), radial-gradient(.045rem .045rem at 84% 33%, color-mix(in oklab,var(--fibre) 30%,transparent) 99%, transparent), linear-gradient(170deg, color-mix(in oklab,white 30%,transparent), transparent 55%);
  background-size: 9px 9px, 14px 14px, 19px 19px, 100% 100%;
  -webkit-mask: radial-gradient(.42rem .3rem at 50% 100%, transparent 96%, #000 0) 0 100%/1.15rem .38rem repeat-x, linear-gradient(#000,#000) 0 0/100% calc(100% - .37rem) no-repeat;
  mask: radial-gradient(.42rem .3rem at 50% 100%, transparent 96%, #000 0) 0 100%/1.15rem .38rem repeat-x, linear-gradient(#000,#000) 0 0/100% calc(100% - .37rem) no-repeat;
  filter: drop-shadow(0 10px 14px color-mix(in oklab,var(--ink) 22%,transparent));
  transition: rotate .45s cubic-bezier(.16,1,.3,1), translate .45s cubic-bezier(.16,1,.3,1), filter .35s ease;
}

.cb-22__label {
  position: relative;
  z-index: 2;
}

.cb-22__crane {
  position: relative;
  width: 1.5rem;
  height: 1.35rem;
  flex: none;
  background: var(--accent);
  clip-path: polygon(0 68%,52% 8%,100% 46%,60% 100%);
  transition: rotate .5s cubic-bezier(.16,1,.3,1);
}

.cb-22__wing {
  position: absolute;
  inset: 0;
  background: color-mix(in oklab,var(--accent) 65%,white);
  clip-path: polygon(6% 62%,52% 10%,58% 62%);
  transform-origin: 52% 62%;
  transition: rotate .55s cubic-bezier(.16,1,.3,1);
}

.cb-22__btn:is(:hover,:focus-visible) {
  rotate: -1.4deg;
  translate: 0 -3px;
  filter: drop-shadow(0 18px 22px color-mix(in oklab,var(--ink) 28%,transparent));
}

.cb-22__btn:is(:hover,:focus-visible) .cb-22__crane {
  rotate: -12deg;
}

.cb-22__btn:is(:hover,:focus-visible) .cb-22__wing {
  rotate: -38deg;
}

.cb-22__btn:active {
  rotate: 0deg;
  translate: 0 1px;
  filter: drop-shadow(0 4px 6px color-mix(in oklab,var(--ink) 25%,transparent));
}

.cb-22__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 5px;
}

.cb-22__btn:disabled {
  cursor: not-allowed;
  filter: none;
  opacity: .55;
}

@media (prefers-reduced-motion: reduce) {
  .cb-22__btn,
    .cb-22__crane,
    .cb-22__wing {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-22__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    mask: none;
    -webkit-mask: none;
    filter: none;
  }

  .cb-22__crane {
    background: ButtonText;
  }
}
```
