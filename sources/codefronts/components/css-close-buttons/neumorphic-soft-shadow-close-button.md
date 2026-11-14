---
source: "codefronts"
url: "https://codefronts.com/components/css-close-buttons/neumorphic-soft-shadow-close-button/"
title: "Neumorphic Soft Shadow Close Button"
section: "components"
category: "css-close-buttons"
category_name: "CSS Close Buttons"
description: "A tactile soft-UI dismiss: the button appears extruded from a putty-coloured surface by dual opposing box-shadows (light from the top-left, dark to the…"
has_js: "false"
---

Here's a working CSS Close Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Soft Shadow Close Button
Source: https://codefronts.com/components/css-close-buttons/neumorphic-soft-shadow-close-button/

A tactile soft-UI dismiss: the button appears extruded from a putty-coloured surface by dual opposing box-shadows (light from the top-left, dark to the bottom-right), then visibly presses IN when clicked by swapping to inset shadows — a physical push-button without a single layout shift.
## HTML
```html
<section class="ccb-07" aria-label="Neumorphic close button demo">
  <div class="ccb-07__panel">
    <button class="ccb-07__close" type="button" aria-label="Close"></button>
    <span class="ccb-07__hint">press me</span>
  </div>
</section>
```
## CSS
```css
.ccb-07,
.ccb-07 *,
.ccb-07 *::before,
.ccb-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ccb-07 {
  --surface: oklch(0.9 0.015 260);
  --lite: color-mix(in oklab,var(--surface) 30%,white);
  --dark: color-mix(in oklab,var(--surface) 88%,black);
  --ink: oklch(0.45 0.04 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  width: 100%;
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 48px 24px;
  background: var(--surface);
}

.ccb-07 .ccb-07__panel {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 18px;
}

.ccb-07 .ccb-07__close {
  position: relative;
  width: 64px;
  height: 64px;
  border: none;
  border-radius: 50%;
  background: var(--surface);
  cursor: pointer;
  box-shadow: -6px -6px 14px var(--lite),6px 6px 14px var(--dark);
  transition: box-shadow .09s ease;
}

.ccb-07 .ccb-07__close::before,
.ccb-07 .ccb-07__close::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  width: 20px;
  height: 2.5px;
  border-radius: 2px;
  background: var(--ink);
  transition: opacity .09s ease;
}

.ccb-07 .ccb-07__close::before {
  transform: translate(-50%,-50%) rotate(45deg);
}

.ccb-07 .ccb-07__close::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.ccb-07 .ccb-07__close:hover {
  box-shadow: -8px -8px 18px var(--lite),8px 8px 18px var(--dark);
}

.ccb-07 .ccb-07__close:active {
  box-shadow: inset -5px -5px 12px var(--lite),inset 5px 5px 12px var(--dark);
}

.ccb-07 .ccb-07__close:active::before,
.ccb-07 .ccb-07__close:active::after {
  opacity: .65;
}

.ccb-07 .ccb-07__close:focus-visible {
  outline: 3px solid oklch(0.5 0.18 265);
  outline-offset: 3px;
}

.ccb-07 .ccb-07__hint {
  font-size: 12px;
  letter-spacing: .05em;
  color: color-mix(in oklab,var(--ink) 60%,transparent);
}

@media (prefers-reduced-motion: reduce) {
  .ccb-07 .ccb-07__close,
    .ccb-07 .ccb-07__close::before,
    .ccb-07 .ccb-07__close::after {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — dual opposing box-shadows extrude the button; :active swaps them to inset for a physical press, zero layout shift. */
```
