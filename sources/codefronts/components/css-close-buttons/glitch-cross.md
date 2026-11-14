---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/glitch-cross/"
title: "Glitch Cross Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "A cyberpunk dismiss for dark dashboards and game UI: on hover the × splits into cyan and magenta ghosts that jitter on opposite X offsets while clip-path…"
has_js: "false"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Glitch Cross Close Button
Source: https://codefronts.com/components/css-close-buttons/glitch-cross/

A cyberpunk dismiss for dark dashboards and game UI: on hover the × splits into cyan and magenta ghosts that jitter on opposite X offsets while clip-path slices strobe horizontal tears across the glyph — the full RGB-split glitch, built from two pseudo-element copies and two keyframe tracks.
## HTML
```html
<section class="ccb-16" aria-label="Glitch close button demo">
  <button class="ccb-16__close" type="button" aria-label="Close">
    <span class="ccb-16__x" aria-hidden="true"></span>
  </button>
</section>
```
## CSS
```css
.ccb-16,
.ccb-16 *,
.ccb-16 *::before,
.ccb-16 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-16 {
  --c1: oklch(0.85 0.15 195);
  --c2: oklch(0.65 0.26 345);
  font-family: ui-monospace,'Cascadia Code',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: radial-gradient(100% 110% at 50% 0%,oklch(0.22 0.03 280 / .9),transparent 60%),oklch(0.13 0.015 280);
}

.ccb-16 .ccb-16__close {
  display: grid;
  place-items: center;
  width: 72px;
  height: 72px;
  border: 1px solid oklch(0.85 0.15 195 / .35);
  border-radius: 12px;
  background: oklch(0.17 0.02 280);
  cursor: pointer;
  isolation: isolate;
  box-shadow: 0 0 0 1px rgba(0,0,0,.6),0 18px 40px -20px rgba(0,0,0,.9);
  transition: border-color .2s ease;
}

.ccb-16 .ccb-16__x {
  position: relative;
  width: 26px;
  height: 26px;
  --bars: linear-gradient(45deg,transparent calc(50% - 1.25px),currentColor calc(50% - 1.25px) calc(50% + 1.25px),transparent calc(50% + 1.25px)),linear-gradient(-45deg,transparent calc(50% - 1.25px),currentColor calc(50% - 1.25px) calc(50% + 1.25px),transparent calc(50% + 1.25px));
  background: var(--bars);
  color: #fff;
}

.ccb-16 .ccb-16__x::before,
.ccb-16 .ccb-16__x::after {
  content: "";
  position: absolute;
  inset: 0;
  background: var(--bars);
  mix-blend-mode: screen;
  opacity: 0;
}

.ccb-16 .ccb-16__x::before {
  color: var(--c1);
}

.ccb-16 .ccb-16__x::after {
  color: var(--c2);
}

.ccb-16 .ccb-16__close:hover .ccb-16__x::before {
  opacity: 1;
  animation: ccb-16-g1 .32s steps(2,jump-none) infinite;
}

.ccb-16 .ccb-16__close:hover .ccb-16__x::after {
  opacity: 1;
  animation: ccb-16-g2 .44s steps(2,jump-none) infinite;
}

.ccb-16 .ccb-16__close:hover {
  border-color: var(--c1);
}

@keyframes ccb-16-g1 {
  0% {
    transform: translateX(-3px);
    clip-path: inset(0 0 62% 0);
  }

  23% {
    transform: translateX(2px);
    clip-path: inset(38% 0 21% 0);
  }

  41% {
    transform: translateX(-2px);
    clip-path: inset(71% 0 0 0);
  }

  67% {
    transform: translateX(3px);
    clip-path: inset(12% 0 55% 0);
  }

  100% {
    transform: translateX(-1px);
    clip-path: inset(45% 0 32% 0);
  }
}

@keyframes ccb-16-g2 {
  0% {
    transform: translateX(3px);
    clip-path: inset(58% 0 8% 0);
  }

  19% {
    transform: translateX(-2px);
    clip-path: inset(9% 0 70% 0);
  }

  47% {
    transform: translateX(2px);
    clip-path: inset(33% 0 40% 0);
  }

  73% {
    transform: translateX(-3px);
    clip-path: inset(80% 0 2% 0);
  }

  100% {
    transform: translateX(1px);
    clip-path: inset(21% 0 48% 0);
  }
}

.ccb-16 .ccb-16__close:active {
  transform: scale(.93);
}

.ccb-16 .ccb-16__close:focus-visible {
  outline: 2.5px solid var(--c1);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .ccb-16 .ccb-16__close:hover .ccb-16__x::before,
    .ccb-16 .ccb-16__close:hover .ccb-16__x::after {
    animation: none;
    opacity: 0;
  }
}
```

## JavaScript
```js
/* No JavaScript — two gradient-drawn ghost copies jitter on desynced steps() tracks; clip-path:inset() strobes the scanline tears. */
```
