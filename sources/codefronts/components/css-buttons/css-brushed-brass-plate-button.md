---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-brushed-brass-plate-button/"
title: "CSS Brushed Brass Plate Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A machined brass nameplate: horizontal brush grain from stacked repeating gradients, four countersunk screws, engraved letterforms cut with a two-shadow…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Brushed Brass Plate Button
Source: https://codefronts.com/components/css-buttons/css-brushed-brass-plate-button/

A machined brass nameplate: horizontal brush grain from stacked repeating gradients, four countersunk screws, engraved letterforms cut with a two-shadow bevel, and a specular band that sweeps across the metal as the pointer crosses it.
## HTML
```html
<div class="cb-21">
  <div class="cb-21__stage">
    <button class="cb-21__btn" type="button">
      <span class="cb-21__screw cb-21__screw--tl" aria-hidden="true"></span>
      <span class="cb-21__screw cb-21__screw--tr" aria-hidden="true"></span>
      <span class="cb-21__screw cb-21__screw--bl" aria-hidden="true"></span>
      <span class="cb-21__screw cb-21__screw--br" aria-hidden="true"></span>
      <span class="cb-21__sheen" aria-hidden="true"></span>
      <span class="cb-21__label">Reserve a table</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&display=swap');

.cb-21 {
  --bg: #171310;
  --brass: #b08d4f;
  --brass-hi: #e6cd94;
  --brass-lo: #7d6132;
  --engrave: #4a3717;
  --radius: .5rem;
  --serif: "Cinzel",ui-serif,Georgia,"Times New Roman",serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(40rem 24rem at 50% 40%, color-mix(in oklab,var(--brass) 14%,transparent), transparent 70%), var(--bg);
  font-family: var(--serif);
}

@supports (color: oklch(50% 0 0)) {
  .cb-21 {
    --brass: oklch(66% .08 82);
    --brass-hi: oklch(86% .08 88);
    --brass-lo: oklch(48% .07 80);
    --engrave: oklch(33% .05 72);
  }
}

@media (prefers-color-scheme: light) {
  .cb-21:not([data-theme="dark"]) {
    --bg: #2a231c;
  }
}

.cb-21[data-theme="light"] {
  --bg: #2a231c;
}

.cb-21,
.cb-21 *,
.cb-21 *::before,
.cb-21 *::after {
  box-sizing: border-box;
}

.cb-21__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-21__btn {
  position: relative;
  overflow: hidden;
  isolation: isolate;
  cursor: pointer;
  min-height: 4rem;
  padding: 0 3.1rem;
  border: 1px solid var(--brass-lo);
  border-radius: var(--radius);
  font: inherit;
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--engrave);
  background: repeating-linear-gradient(90deg, rgba(255,255,255,.10) 0 1px, transparent 1px 2px, rgba(0,0,0,.07) 2px 3px, transparent 3px 5px), repeating-linear-gradient(90deg, rgba(255,255,255,.05) 0 1px, transparent 1px 7px), linear-gradient(112deg, var(--brass-hi), var(--brass) 34%, var(--brass-lo) 62%, var(--brass) 86%);
  text-shadow: 0 1px 0 color-mix(in oklab,white 55%,transparent), 0 -1px 0 color-mix(in oklab,black 42%,transparent);
  box-shadow: inset 0 1px 0 color-mix(in oklab,white 45%,transparent), inset 0 -1px 0 color-mix(in oklab,black 35%,transparent), 0 14px 26px -14px rgba(0,0,0,.75);
  transition: translate .18s ease, box-shadow .22s ease, filter .3s ease;
}

.cb-21__label {
  position: relative;
  z-index: 3;
}

.cb-21__sheen {
  position: absolute;
  inset: 0;
  z-index: 2;
  pointer-events: none;
  background: linear-gradient(100deg, transparent 38%, rgba(255,255,255,.42) 50%, transparent 62%);
  translate: -62% 0;
  transition: translate .85s cubic-bezier(.16,1,.3,1);
}

.cb-21__btn:is(:hover,:focus-visible) .cb-21__sheen {
  translate: 62% 0;
}

.cb-21__btn:hover {
  filter: brightness(1.05);
}

.cb-21__screw {
  position: absolute;
  z-index: 3;
  width: .55rem;
  height: .55rem;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 30%, #f0e0b8, #8d6f38 60%, #5c4520);
  box-shadow: inset 0 -1px 1px rgba(0,0,0,.5), 0 1px 1px rgba(255,255,255,.25);
  transition: rotate .3s ease;
}

.cb-21__screw::after {
  content: '';
  position: absolute;
  inset: 22% 12%;
  background: rgba(0,0,0,.55);
  clip-path: polygon(0 42%,100% 42%,100% 58%,0 58%);
}

.cb-21__screw--tl {
  top: .5rem;
  left: .6rem;
}

.cb-21__screw--tr {
  top: .5rem;
  right: .6rem;
  rotate: 34deg;
}

.cb-21__screw--bl {
  bottom: .5rem;
  left: .6rem;
  rotate: -22deg;
}

.cb-21__screw--br {
  bottom: .5rem;
  right: .6rem;
  rotate: 12deg;
}

.cb-21__btn:active {
  translate: 0 1px;
  box-shadow: inset 0 2px 6px rgba(0,0,0,.5);
}

.cb-21__btn:active .cb-21__screw {
  rotate: 12deg;
}

.cb-21__btn:focus-visible {
  outline: 2px solid var(--brass-hi);
  outline-offset: 4px;
}

.cb-21__btn:disabled {
  cursor: not-allowed;
  filter: grayscale(.7) brightness(.85);
}

@media (prefers-reduced-motion: reduce) {
  .cb-21__btn,
    .cb-21__sheen,
    .cb-21__screw {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-21__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    text-shadow: none;
    box-shadow: none;
  }

  .cb-21__sheen,
    .cb-21__screw {
    display: none;
  }
}
```
