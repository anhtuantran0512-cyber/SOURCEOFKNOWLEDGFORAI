---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-play-pause-button/"
title: "CSS Play Pause Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "One shape that morphs between a play triangle and two pause bars — no icon swap, no SVG library."
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Play Pause Button
Source: https://codefronts.com/components/css-buttons/css-play-pause-button/

One shape that morphs between a play triangle and two pause bars — no icon swap, no SVG library. Both states are clip-path: polygon() with the same point count, so the browser interpolates every vertex; a progress ring sits around it and the whole thing is a single checkbox.
## HTML
```html
<div class="cb-13">
  <div class="cb-13__stage">
    <label class="cb-13__btn">
      <input type="checkbox" aria-label="Play or pause the episode">
      <span class="cb-13__ring" aria-hidden="true"></span>
      <span class="cb-13__glyph" aria-hidden="true">
        <span class="cb-13__half cb-13__half--l"></span>
        <span class="cb-13__half cb-13__half--r"></span>
      </span>
    </label>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700&display=swap');

.cb-13 {
  --bg: #0d0b14;
  --surface: #191426;
  --ink: #f4f1ff;
  --accent: #c084fc;
  --accent-2: #38bdf8;
  --size: 5.5rem;
  --radius: 999px;
  --sans: "Outfit",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(40rem 26rem at 50% 45%, color-mix(in oklab,var(--accent) 16%,transparent), transparent 70%), var(--bg);
  font-family: var(--sans);
}

@supports (color: oklch(50% 0 0)) {
  .cb-13 {
    --accent: oklch(78% .16 305);
    --accent-2: oklch(78% .13 222);
    --surface: oklch(22% .04 295);
  }
}

@media (prefers-color-scheme: light) {
  .cb-13:not([data-theme="dark"]) {
    --bg: #f4f1fb;
    --surface: #ffffff;
    --ink: #1a1230;
    --accent: #7c3aed;
    --accent-2: #0284c7;
  }
}

.cb-13[data-theme="light"] {
  --bg: #f4f1fb;
  --surface: #ffffff;
  --ink: #1a1230;
  --accent: #7c3aed;
  --accent-2: #0284c7;
}

.cb-13,
.cb-13 *,
.cb-13 *::before,
.cb-13 *::after {
  box-sizing: border-box;
}

.cb-13__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-13__btn {
  position: relative;
  cursor: pointer;
  display: grid;
  place-items: center;
  width: var(--size);
  height: var(--size);
  border-radius: var(--radius);
  background: linear-gradient(160deg, color-mix(in oklab,var(--surface) 80%,white 6%), var(--surface));
  box-shadow: inset 0 1px 0 color-mix(in oklab,white 20%,transparent), 0 18px 40px -18px color-mix(in oklab,var(--accent) 70%,transparent);
  transition: scale .4s cubic-bezier(.16,1,.3,1), box-shadow .4s ease;
  -webkit-tap-highlight-color: transparent;
}

.cb-13__btn input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.cb-13__ring {
  position: absolute;
  inset: -.45rem;
  border-radius: 50%;
  background: conic-gradient(from 0deg, transparent 0 55%, var(--accent-2), var(--accent), transparent);
  -webkit-mask: radial-gradient(farthest-side,transparent calc(100% - 2.5px),#000 calc(100% - 2.5px));
  mask: radial-gradient(farthest-side,transparent calc(100% - 2.5px),#000 calc(100% - 2.5px));
  opacity: .28;
  transition: opacity .4s ease;
}

.cb-13__glyph {
  position: relative;
  width: 42%;
  height: 42%;
  translate: 4% 0;
  transition: translate .5s cubic-bezier(.16,1,.3,1);
}

.cb-13__half {
  position: absolute;
  inset: 0;
  background: var(--ink);
  transition: clip-path .5s cubic-bezier(.16,1,.3,1), background-color .3s ease;
}
/* Play: the triangle split down the middle — the two halves meet seamlessly. */

.cb-13__half--l {
  clip-path: polygon(22% 6%,50% 24%,50% 76%,22% 94%);
}

.cb-13__half--r {
  clip-path: polygon(50% 24%,90% 50%,90% 50%,50% 76%);
}

.cb-13__btn:hover {
  scale: 1.05;
}

.cb-13__btn:active {
  scale: .95;
}

.cb-13__btn:has(input:focus-visible) {
  outline: 2px solid var(--accent);
  outline-offset: 6px;
}

.cb-13__btn:has(input:checked) {
  box-shadow: inset 0 1px 0 color-mix(in oklab,white 22%,transparent), 0 22px 50px -18px color-mix(in oklab,var(--accent-2) 80%,transparent);
}

.cb-13__btn:has(input:checked) .cb-13__glyph {
  translate: 0 0;
}
/* Pause: each half becomes its own bar — same four points, so every vertex interpolates. */

.cb-13__btn:has(input:checked) .cb-13__half--l {
  clip-path: polygon(14% 6%,39% 6%,39% 94%,14% 94%);
}

.cb-13__btn:has(input:checked) .cb-13__half--r {
  clip-path: polygon(61% 6%,86% 6%,86% 94%,61% 94%);
}

.cb-13__btn:has(input:checked) .cb-13__ring {
  opacity: 1;
  animation: cb-13-spin 2.6s linear infinite;
}

@keyframes cb-13-spin {
  to {
    rotate: 1turn;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-13__btn,
    .cb-13__glyph,
    .cb-13__half,
    .cb-13__ring {
    transition: none;
  }

  .cb-13__btn:has(input:checked) .cb-13__ring {
    animation: none;
    opacity: 1;
  }
}

@media (forced-colors: active) {
  .cb-13__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
  }

  .cb-13__half {
    background: ButtonText;
  }

  .cb-13__ring {
    display: none;
  }
}
```
