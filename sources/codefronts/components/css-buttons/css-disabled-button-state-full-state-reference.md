---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-disabled-button-state-full-state-reference/"
title: "CSS Disabled Button State (Full State Reference)"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "Every button state side by side in one row — rest, hover, focus, pressed, truly disabled, and aria-disabled (focusable, explains itself, refuses activation)."
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Disabled Button State (Full State Reference)
Source: https://codefronts.com/components/css-buttons/css-disabled-button-state-full-state-reference/

Every button state side by side in one row — rest, hover, focus, pressed, truly disabled, and aria-disabled (focusable, explains itself, refuses activation). The hover/focus/pressed cards are frozen with state classes so you can compare all six simultaneously instead of chasing a pointer.
## HTML
```html
<div class="cb-07">
  <div class="cb-07__stage">
    <div class="cb-07__row">
      <button class="cb-07__btn" type="button">Rest</button>
      <button class="cb-07__btn is-hover" type="button">Hover</button>
      <button class="cb-07__btn is-focus" type="button">Focus</button>
      <button class="cb-07__btn is-active" type="button">Pressed</button>
      <button class="cb-07__btn" type="button" disabled>Disabled</button>
      <button class="cb-07__btn" type="button" aria-disabled="true" aria-describedby="cb-07-why">Unavailable</button>
      <span class="cb-07__sr" id="cb-07-why">Complete the form above to enable this action</span>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700&display=swap');

.cb-07 {
  --bg: #f5f5f3;
  --accent: #0f766e;
  --ink: #ffffff;
  --muted: #6b7280;
  --fill: var(--accent);
  --fill-h: #0d6a62;
  --fill-a: #0b5a53;
  --fill-d: #dcdcd8;
  --radius: .7rem;
  --sans: "Schibsted Grotesk",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--bg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .cb-07 {
    --bg: oklch(96.8% .004 110);
    --accent: oklch(48% .1 180);
    --fill-h: oklch(44% .1 180);
    --fill-a: oklch(39% .09 180);
    --fill-d: oklch(89% .006 110);
    --muted: oklch(48% .01 260);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-07:not([data-theme="light"]) {
    --bg: #0b0d0d;
    --accent: #14b8a6;
    --ink: #04201d;
    --fill-h: #0fa295;
    --fill-a: #0c8b80;
    --fill-d: #23282a;
    --muted: #9aa3a8;
  }
}

.cb-07[data-theme="dark"] {
  --bg: #0b0d0d;
  --accent: #14b8a6;
  --ink: #04201d;
  --fill-h: #0fa295;
  --fill-a: #0c8b80;
  --fill-d: #23282a;
  --muted: #9aa3a8;
}

.cb-07,
.cb-07 *,
.cb-07 *::before,
.cb-07 *::after {
  box-sizing: border-box;
}

.cb-07__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-07__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.cb-07__row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: .75rem;
  max-width: 44rem;
}

.cb-07__btn {
  cursor: pointer;
  display: grid;
  place-items: center;
  min-height: 3rem;
  min-width: 7.5rem;
  padding: 0 1.35rem;
  border: 0;
  border-radius: var(--radius);
  font: inherit;
  font-size: .9375rem;
  font-weight: 600;
  color: var(--ink);
  background: var(--fill);
  box-shadow: 0 8px 18px -12px color-mix(in oklab,var(--accent) 85%,transparent);
  transition: background-color .18s ease, translate .18s cubic-bezier(.16,1,.3,1), scale .18s ease;
}

.cb-07__btn:hover,
.cb-07__btn.is-hover {
  --fill: var(--fill-h);
  translate: 0 -1px;
}

.cb-07__btn:focus-visible,
.cb-07__btn.is-focus {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cb-07__btn:active,
.cb-07__btn.is-active {
  --fill: var(--fill-a);
  translate: 0 1px;
  scale: .985;
  box-shadow: none;
}

.cb-07__btn:disabled,
.cb-07__btn[aria-disabled="true"] {
  --fill: var(--fill-d);
  color: var(--muted);
  cursor: not-allowed;
  box-shadow: none;
  translate: 0;
  scale: 1;
}

.cb-07__btn[aria-disabled="true"] {
  cursor: not-allowed;
}

.cb-07__btn[aria-disabled="true"]:active {
  animation: cb-07-nope .32s cubic-bezier(.36,.07,.19,.97);
}

@keyframes cb-07-nope {
  0%,
    100% {
    translate: 0 0;
  }

  25% {
    translate: -3px 0;
  }

  75% {
    translate: 3px 0;
  }
}

@media (prefers-reduced-motion: reduce) {
  .cb-07__btn {
    transition: none;
  }

  .cb-07__btn[aria-disabled="true"]:active {
    animation: none;
    outline: 2px dashed var(--muted);
    outline-offset: 2px;
  }
}

@media (forced-colors: active) {
  .cb-07__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .cb-07__btn:disabled,
    .cb-07__btn[aria-disabled="true"] {
    color: GrayText;
    border-color: GrayText;
  }
}
```
