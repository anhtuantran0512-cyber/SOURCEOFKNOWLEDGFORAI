---
source: "codefronts"
url: "https://codefronts.com/components/css-toggles-switches/split-flap-board/"
title: "Split-Flap Board"
section: "components"
category: "css-toggles-switches"
category_name: "CSS Toggles & Switches"
description: "A retro-mechanical airport departure board built from CSS-only rotateX flips."
has_js: "false"
---

Here's a working CSS Toggles & Switche from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Split-Flap Board
Source: https://codefronts.com/components/css-toggles-switches/split-flap-board/

A retro-mechanical airport departure board built from CSS-only rotateX flips. Toggling cycles both rows simultaneously — OFFLINE flips to ONLINE, STANDBY flips to ACTIVE — with each character flipping in sequence for the cascading split-flap feel.
## HTML
```html
<label class="tgl-32">
  <input class="tgl-32__input" type="checkbox" checked>
  <span class="tgl-32__stage" aria-hidden="true">
    <span class="tgl-32__row">
      <span class="tgl-32__lbl">Status</span>
      <span class="tgl-32__board">
        <span class="tgl-32__char" data-off="O" data-on="O"></span>
        <span class="tgl-32__char" data-off="F" data-on="N"></span>
        <span class="tgl-32__char" data-off="F" data-on="L"></span>
        <span class="tgl-32__char" data-off="L" data-on="I"></span>
        <span class="tgl-32__char" data-off="I" data-on="N"></span>
        <span class="tgl-32__char" data-off="N" data-on="E"></span>
        <span class="tgl-32__char" data-off="E" data-on="·"></span>
      </span>
    </span>
    <span class="tgl-32__row">
      <span class="tgl-32__lbl">Mode</span>
      <span class="tgl-32__board">
        <span class="tgl-32__char" data-off="S" data-on="A"></span>
        <span class="tgl-32__char" data-off="T" data-on="C"></span>
        <span class="tgl-32__char" data-off="A" data-on="T"></span>
        <span class="tgl-32__char" data-off="N" data-on="I"></span>
        <span class="tgl-32__char" data-off="D" data-on="V"></span>
        <span class="tgl-32__char" data-off="B" data-on="E"></span>
        <span class="tgl-32__char" data-off="Y" data-on="·"></span>
      </span>
    </span>
  </span>
</label>
```
## CSS
```css
.tgl-32 {
  --tgl-32-bg: #0a0a12;
  --tgl-32-border: #1a1a28;
  --tgl-32-ash: #7a7a98;
  --tgl-32-volt: #e0ff00;
  --tgl-32-ice: #00e5ff;
  --tgl-32-flip: 0.5s;
  font-family: "Inconsolata", "Roboto Mono", ui-monospace, monospace;
  font-size: 14px;
  min-height: 100vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 24px;
  padding: 48px 20px;
  background: #14141e;
  box-sizing: border-box;
}

.tgl-32__input {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  white-space: nowrap;
  border: 0;
}

.tgl-32__stage {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.tgl-32__row {
  display: flex;
  align-items: center;
  gap: 10px;
}

.tgl-32__lbl {
  min-width: 56px;
  font-size: 12px;
  color: var(--tgl-32-ash);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.tgl-32__board {
  display: flex;
  gap: 4px;
}
/* Each char is a black tile with a horizontal seam down the middle and
   a CSS-only flip. The letter is rendered via data-off/data-on attrs in
   a pseudo, so toggling swaps which attr is shown. */

.tgl-32__char {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 38px;
  border-radius: 5px;
  background: var(--tgl-32-bg);
  border: 1px solid var(--tgl-32-border);
  font-size: 18px;
  font-weight: 500;
  color: var(--tgl-32-ash);
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.04), inset 0 -1px 0 rgba(0,0,0,0.3);
  overflow: hidden;
  transform-style: preserve-3d;
  perspective: 400px;
  transition: color var(--tgl-32-flip) ease;
}
/* Seam across the middle of every char tile. */

.tgl-32__char::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  height: 1px;
  background: rgba(0,0,0,0.6);
  z-index: 2;
  pointer-events: none;
}
/* The letter itself lives in ::before so we can flip it independently
   of the tile chrome. Default shows the off character. */

.tgl-32__char::before {
  content: attr(data-off);
  display: inline-block;
  transform-origin: center;
  animation: tgl-32-off var(--tgl-32-flip) ease both;
}

@keyframes tgl-32-off {
  0% {
    transform: rotateX(-90deg);
  }

  50% {
    content: attr(data-off);
  }

  100% {
    transform: rotateX(0);
  }
}

@keyframes tgl-32-on {
  0% {
    transform: rotateX(0);
  }

  50% {
    transform: rotateX(-90deg);
  }

  51% {
    transform: rotateX(90deg);
  }

  100% {
    transform: rotateX(0);
  }
}
/* Stagger — each char is delayed 80ms further than the previous so the
   board cascades. Both rows share the same stagger pattern. */

.tgl-32__board .tgl-32__char:nth-child(1) {
  animation-delay: 0ms;
}

.tgl-32__board .tgl-32__char:nth-child(2) {
  animation-delay: 80ms;
}

.tgl-32__board .tgl-32__char:nth-child(3) {
  animation-delay: 160ms;
}

.tgl-32__board .tgl-32__char:nth-child(4) {
  animation-delay: 240ms;
}

.tgl-32__board .tgl-32__char:nth-child(5) {
  animation-delay: 320ms;
}

.tgl-32__board .tgl-32__char:nth-child(6) {
  animation-delay: 400ms;
}

.tgl-32__board .tgl-32__char:nth-child(7) {
  animation-delay: 480ms;
}

.tgl-32__input:checked ~ .tgl-32__stage .tgl-32__char {
  color: var(--tgl-32-volt);
}

.tgl-32__input:checked ~ .tgl-32__stage .tgl-32__row:nth-child(2) .tgl-32__char {
  color: var(--tgl-32-ice);
}

.tgl-32__input:checked ~ .tgl-32__stage .tgl-32__char::before {
  content: attr(data-on);
  animation: tgl-32-on var(--tgl-32-flip) ease both;
  animation-delay: inherit;
}

.tgl-32__input:checked ~ .tgl-32__stage .tgl-32__board .tgl-32__char:nth-child(1) {
  animation-delay: 0ms;
}

.tgl-32__input:checked ~ .tgl-32__stage .tgl-32__board .tgl-32__char:nth-child(2) {
  animation-delay: 80ms;
}

.tgl-32__input:checked ~ .tgl-32__stage .tgl-32__board .tgl-32__char:nth-child(3) {
  animation-delay: 160ms;
}

.tgl-32__input:checked ~ .tgl-32__stage .tgl-32__board .tgl-32__char:nth-child(4) {
  animation-delay: 240ms;
}

.tgl-32__input:checked ~ .tgl-32__stage .tgl-32__board .tgl-32__char:nth-child(5) {
  animation-delay: 320ms;
}

.tgl-32__input:checked ~ .tgl-32__stage .tgl-32__board .tgl-32__char:nth-child(6) {
  animation-delay: 400ms;
}

.tgl-32__input:checked ~ .tgl-32__stage .tgl-32__board .tgl-32__char:nth-child(7) {
  animation-delay: 480ms;
}

.tgl-32__input:focus-visible ~ .tgl-32__stage {
  outline: 2px solid var(--tgl-32-volt);
  outline-offset: 6px;
  border-radius: 6px;
}

@media (prefers-reduced-motion: reduce) {
  .tgl-32__char,
    .tgl-32__char::before {
    animation: none;
    transition: none;
  }

  .tgl-32__char::before {
    content: attr(data-off);
  }

  .tgl-32__input:checked ~ .tgl-32__stage .tgl-32__char::before {
    content: attr(data-on);
  }
}
```

## JavaScript
```js
/* No JavaScript — content:attr(data-off/on) swaps mid-keyframe behind a rotateX flip, with 80ms per-tile delays cascading the board. */
```
