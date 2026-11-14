---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-brutalist-glitch-button/"
title: "CSS Brutalist Glitch Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "Neo-brutalist slab with a hard offset shadow that snaps flat when pressed, and a hover glitch built from two duplicate labels sliced by clip-path and pushed…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Brutalist Glitch Button
Source: https://codefronts.com/components/css-buttons/css-brutalist-glitch-button/

Neo-brutalist slab with a hard offset shadow that snaps flat when pressed, and a hover glitch built from two duplicate labels sliced by clip-path and pushed apart in cyan and magenta. Steps-based timing keeps it digital — no easing, no blur, no JavaScript.
## HTML
```html
<div class="cb-16">
  <div class="cb-16__stage">
    <button class="cb-16__btn" type="button" data-label="Enter the archive">Enter the archive</button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&display=swap');

.cb-16 {
  --bg: #e8e6df;
  --slab: #f7f5ef;
  --ink: #0a0a0a;
  --accent: #facc15;
  --ghost-1: #22d3ee;
  --ghost-2: #f43f5e;
  --offset: 6px;
  --mono: "Space Mono",ui-monospace,"SFMono-Regular",Menlo,Consolas,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: repeating-linear-gradient(90deg, color-mix(in oklab,var(--ink) 5%,transparent) 0 1px, transparent 1px 3rem), repeating-linear-gradient(0deg, color-mix(in oklab,var(--ink) 5%,transparent) 0 1px, transparent 1px 3rem), var(--bg);
  font-family: var(--mono);
}

@supports (color: oklch(50% 0 0)) {
  .cb-16 {
    --bg: oklch(92% .008 95);
    --accent: oklch(87% .17 92);
    --ghost-1: oklch(82% .13 200);
    --ghost-2: oklch(66% .21 12);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-16:not([data-theme="light"]) {
    --bg: #101010;
    --slab: #1b1b1b;
    --ink: #f5f5f0;
  }
}

.cb-16[data-theme="dark"] {
  --bg: #101010;
  --slab: #1b1b1b;
  --ink: #f5f5f0;
}

.cb-16,
.cb-16 *,
.cb-16 *::before,
.cb-16 *::after {
  box-sizing: border-box;
}

.cb-16__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-16__btn {
  position: relative;
  cursor: pointer;
  display: grid;
  place-items: center;
  min-height: 3.5rem;
  padding: 0 2rem;
  border: 2px solid var(--ink);
  border-radius: 0;
  font: inherit;
  font-size: .9375rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .1em;
  color: var(--ink);
  background: var(--slab);
  box-shadow: var(--offset) var(--offset) 0 0 var(--ink);
  transition: translate .12s steps(2,end), box-shadow .12s steps(2,end), background-color .15s steps(2,end);
}

.cb-16__btn::before,
.cb-16__btn::after {
  content: attr(data-label);
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  padding: 0 2rem;
  pointer-events: none;
  opacity: 0;
  white-space: nowrap;
}

.cb-16__btn::before {
  color: var(--ghost-1);
  clip-path: inset(0 0 55% 0);
}

.cb-16__btn::after {
  color: var(--ghost-2);
  clip-path: inset(55% 0 0 0);
}

.cb-16__btn:is(:hover,:focus-visible) {
  background: var(--accent);
}

.cb-16__btn:is(:hover,:focus-visible)::before {
  animation: cb-16-a .48s steps(2,end) infinite;
}

.cb-16__btn:is(:hover,:focus-visible)::after {
  animation: cb-16-b .56s steps(2,end) infinite;
}

@keyframes cb-16-a {
  0%,
    100% {
    translate: 0 0;
    opacity: 0;
  }

  20% {
    translate: -3px -2px;
    opacity: 1;
  }

  45% {
    translate: 4px 1px;
    opacity: 1;
    clip-path: inset(0 0 68% 0);
  }

  70% {
    translate: -2px 2px;
    opacity: 1;
    clip-path: inset(0 0 42% 0);
  }
}

@keyframes cb-16-b {
  0%,
    100% {
    translate: 0 0;
    opacity: 0;
  }

  25% {
    translate: 3px 2px;
    opacity: 1;
  }

  50% {
    translate: -4px -1px;
    opacity: 1;
    clip-path: inset(48% 0 0 0);
  }

  75% {
    translate: 2px -2px;
    opacity: 1;
    clip-path: inset(62% 0 0 0);
  }
}

.cb-16__btn:focus-visible {
  outline: 3px dashed var(--ink);
  outline-offset: 5px;
}

.cb-16__btn:active {
  translate: var(--offset) var(--offset);
  box-shadow: 0 0 0 0 var(--ink);
}

.cb-16__btn:disabled {
  cursor: not-allowed;
  color: color-mix(in oklab,var(--ink) 40%,var(--slab));
  box-shadow: var(--offset) var(--offset) 0 0 color-mix(in oklab,var(--ink) 35%,var(--slab));
}

@media (prefers-reduced-motion: reduce) {
  .cb-16__btn {
    transition: none;
  }

  .cb-16__btn::before,
    .cb-16__btn::after {
    animation: none !important;
    display: none;
  }
}

@media (forced-colors: active) {
  .cb-16__btn {
    background: ButtonFace;
    color: ButtonText;
    border-color: ButtonText;
    box-shadow: var(--offset) var(--offset) 0 0 ButtonText;
  }

  .cb-16__btn::before,
    .cb-16__btn::after {
    display: none;
  }
}
```
