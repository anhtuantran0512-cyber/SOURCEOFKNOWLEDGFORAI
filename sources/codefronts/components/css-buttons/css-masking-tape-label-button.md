---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-masking-tape-label-button/"
title: "CSS Masking Tape Label Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A strip of drafting tape stuck slightly crooked: translucent so the surface shows through, fibrous weave running lengthwise, ragged torn ends cut by a…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Masking Tape Label Button
Source: https://codefronts.com/components/css-buttons/css-masking-tape-label-button/

A strip of drafting tape stuck slightly crooked: translucent so the surface shows through, fibrous weave running lengthwise, ragged torn ends cut by a repeating mask, and a hand-written label. Hover presses the tape flatter; pressing sticks it down.
## HTML
```html
<div class="cb-33">
  <div class="cb-33__stage">
    <button class="cb-33__btn" type="button">
      <span class="cb-33__label">pin this for later</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@500;600;700&display=swap');

.cb-33 {
  --bg: #dfd8c8;
  --tape: rgba(238,226,190,.9);
  --tape-2: rgba(222,206,164,.92);
  --ink: #3a3226;
  --hand: "Caveat",ui-rounded,"Comic Sans MS",cursive;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: repeating-linear-gradient(0deg, rgba(0,0,0,.03) 0 1px, transparent 1px 1.75rem), repeating-linear-gradient(90deg, rgba(0,0,0,.03) 0 1px, transparent 1px 1.75rem), var(--bg);
  font-family: var(--hand);
}

@supports (color: oklch(50% 0 0)) {
  .cb-33 {
    --bg: oklch(88% .022 88);
    --ink: oklch(30% .02 75);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-33:not([data-theme="light"]) {
    --bg: #26231d;
    --tape: rgba(206,190,150,.86);
    --tape-2: rgba(184,168,128,.9);
    --ink: #2b251b;
  }
}

.cb-33[data-theme="dark"] {
  --bg: #26231d;
  --tape: rgba(206,190,150,.86);
  --tape-2: rgba(184,168,128,.9);
  --ink: #2b251b;
}

.cb-33,
.cb-33 *,
.cb-33 *::before,
.cb-33 *::after {
  box-sizing: border-box;
}

.cb-33__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-33__btn {
  cursor: pointer;
  border: 0;
  padding: .85rem 2.4rem;
  border-radius: 0;
  font: inherit;
  font-size: 1.5rem;
  font-weight: 600;
  letter-spacing: .01em;
  color: var(--ink);
  background-color: var(--tape);
  background-image: repeating-linear-gradient(90deg, rgba(255,255,255,.22) 0 1px, transparent 1px 2px), repeating-linear-gradient(90deg, rgba(0,0,0,.045) 0 1px, transparent 1px 5px), linear-gradient(102deg, rgba(255,255,255,.3), transparent 40%, rgba(0,0,0,.07)), linear-gradient(180deg, var(--tape), var(--tape-2));
  -webkit-mask: radial-gradient(.22rem .3rem at 0 50%, transparent 96%, #000 0) 0 0/.42rem .5rem repeat-y, radial-gradient(.22rem .3rem at 100% 50%, transparent 96%, #000 0) 100% 0/.42rem .5rem repeat-y, linear-gradient(#000,#000) .4rem 0/calc(100% - .8rem) 100% no-repeat;
  mask: radial-gradient(.22rem .3rem at 0 50%, transparent 96%, #000 0) 0 0/.42rem .5rem repeat-y, radial-gradient(.22rem .3rem at 100% 50%, transparent 96%, #000 0) 100% 0/.42rem .5rem repeat-y, linear-gradient(#000,#000) .4rem 0/calc(100% - .8rem) 100% no-repeat;
  rotate: -1.7deg;
  filter: drop-shadow(0 4px 5px rgba(60,48,30,.28));
  transition: rotate .4s cubic-bezier(.16,1,.3,1), translate .4s cubic-bezier(.16,1,.3,1), filter .35s ease;
  -webkit-tap-highlight-color: transparent;
}

.cb-33__label {
  display: inline-block;
  transition: rotate .4s cubic-bezier(.16,1,.3,1);
}

.cb-33__btn:is(:hover,:focus-visible) {
  rotate: -.4deg;
  translate: 0 -2px;
  filter: drop-shadow(0 8px 9px rgba(60,48,30,.3));
}

.cb-33__btn:is(:hover,:focus-visible) .cb-33__label {
  rotate: .6deg;
}

.cb-33__btn:active {
  rotate: -1.2deg;
  translate: 0 1px;
  filter: drop-shadow(0 2px 2px rgba(60,48,30,.3));
}

.cb-33__btn:focus-visible {
  outline: 2px dashed var(--ink);
  outline-offset: 4px;
}

.cb-33__btn:disabled {
  cursor: not-allowed;
  opacity: .6;
  filter: none;
}

@media (prefers-reduced-motion: reduce) {
  .cb-33__btn,
    .cb-33__label {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-33__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    mask: none;
    -webkit-mask: none;
    filter: none;
    rotate: 0deg;
  }
}
```
