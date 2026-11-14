---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-chalkboard-menu-button/"
title: "CSS Chalkboard Menu Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "Slate with real chalk behaviour: a dusty, slightly uneven board, a hand-drawn double border, letterforms that sit in the tooth of the surface via a soft…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Chalkboard Menu Button
Source: https://codefronts.com/components/css-buttons/css-chalkboard-menu-button/

Slate with real chalk behaviour: a dusty, slightly uneven board, a hand-drawn double border, letterforms that sit in the tooth of the surface via a soft light shadow, and a puff of chalk dust when you press. The hover wipes a faint smudge across the board.
## HTML
```html
<div class="cb-38">
  <div class="cb-38__stage">
    <button class="cb-38__btn" type="button">
      <span class="cb-38__smudge" aria-hidden="true"></span>
      <span class="cb-38__dust" aria-hidden="true"></span>
      <span class="cb-38__label">Today's special</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap');

.cb-38 {
  --bg: #20242b;
  --slate: #26302f;
  --slate-2: #1b2322;
  --chalk: #f4f1e6;
  --frame: .35rem;
  --hand: "Patrick Hand",ui-rounded,"Comic Sans MS",cursive;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: repeating-linear-gradient(92deg, rgba(0,0,0,.05) 0 2px, transparent 2px 9px), var(--bg);
  font-family: var(--hand);
}

@supports (color: oklch(50% 0 0)) {
  .cb-38 {
    --slate: oklch(30% .015 175);
    --slate-2: oklch(23% .015 175);
    --chalk: oklch(96% .01 90);
  }
}

@media (prefers-color-scheme: light) {
  .cb-38:not([data-theme="dark"]) {
    --bg: #2c3238;
  }
}

.cb-38[data-theme="light"] {
  --bg: #2c3238;
}

.cb-38,
.cb-38 *,
.cb-38 *::before,
.cb-38 *::after {
  box-sizing: border-box;
}

.cb-38__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-38__btn {
  position: relative;
  cursor: pointer;
  display: grid;
  place-items: center;
  min-height: 4.25rem;
  padding: 0 2.75rem;
  border: 2px dashed color-mix(in oklab,var(--chalk) 52%,transparent);
  border-radius: .5rem;
  font: inherit;
  font-size: 1.5rem;
  letter-spacing: .02em;
  background-color: var(--slate);
  background-image: radial-gradient(.08rem .08rem at 24% 36%, rgba(244,241,230,.2) 99%, transparent), radial-gradient(.06rem .06rem at 68% 72%, rgba(244,241,230,.16) 99%, transparent), radial-gradient(8rem 5rem at 20% 15%, rgba(255,255,255,.05), transparent 70%), radial-gradient(9rem 6rem at 82% 88%, rgba(255,255,255,.04), transparent 72%), linear-gradient(160deg, var(--slate), var(--slate-2));
  background-size: 9px 9px, 13px 13px, 100% 100%, 100% 100%, 100% 100%;
  box-shadow: 0 16px 26px -16px rgba(0,0,0,.8), inset 0 0 30px rgba(0,0,0,.35);
  transition: translate .22s cubic-bezier(.16,1,.3,1), box-shadow .25s ease;
  -webkit-tap-highlight-color: transparent;
}

.cb-38__btn::before {
  content: '';
  position: absolute;
  inset: var(--frame);
  pointer-events: none;
  border: 1px dashed color-mix(in oklab,var(--chalk) 28%,transparent);
  border-radius: .35rem;
  rotate: .25deg;
}

.cb-38__label {
  position: relative;
  z-index: 3;
  color: color-mix(in oklab,var(--chalk) 92%,transparent);
  text-shadow: 0 0 1px color-mix(in oklab,var(--chalk) 55%,transparent), 0 0 7px color-mix(in oklab,var(--chalk) 20%,transparent), 0 1px 0 rgba(0,0,0,.35);
}

.cb-38__smudge {
  position: absolute;
  inset: 0;
  z-index: 2;
  pointer-events: none;
  opacity: 0;
  background: linear-gradient(104deg, transparent 30%, rgba(244,241,230,.1) 50%, transparent 70%);
  transition: opacity .4s ease;
}

.cb-38__btn:is(:hover,:focus-visible) {
  translate: 0 -2px;
}

.cb-38__btn:is(:hover,:focus-visible) .cb-38__smudge {
  opacity: 1;
}

.cb-38__btn:focus-visible {
  outline: 2px solid var(--chalk);
  outline-offset: 5px;
}

.cb-38__btn:active {
  translate: 0 1px;
  box-shadow: 0 6px 12px -10px rgba(0,0,0,.8), inset 0 0 36px rgba(0,0,0,.45);
}

.cb-38__dust {
  position: absolute;
  left: 50%;
  bottom: -.5rem;
  width: 8rem;
  height: 1.2rem;
  margin-left: -4rem;
  border-radius: 50%;
  pointer-events: none;
  opacity: 0;
  background: radial-gradient(closest-side, rgba(244,241,230,.6), transparent 74%);
  filter: blur(4px);
}

.cb-38__btn:active .cb-38__dust {
  animation: cb-38-dust .6s ease-out;
}

@keyframes cb-38-dust {
  0% {
    opacity: .75;
    scale: .4 .5;
  }

  100% {
    opacity: 0;
    scale: 1.6 1.4;
  }
}

.cb-38__btn:disabled {
  cursor: not-allowed;
  opacity: .55;
}

@media (prefers-reduced-motion: reduce) {
  .cb-38__btn,
    .cb-38__smudge {
    transition: none;
  }

  .cb-38__dust {
    display: none;
  }
}

@media (forced-colors: active) {
  .cb-38__btn {
    background: ButtonFace;
    border: 2px solid ButtonText;
    box-shadow: none;
  }

  .cb-38__label {
    color: ButtonText;
    text-shadow: none;
  }

  .cb-38__smudge,
    .cb-38__dust {
    display: none;
  }

  .cb-38__btn::before {
    display: none;
  }
}
```
