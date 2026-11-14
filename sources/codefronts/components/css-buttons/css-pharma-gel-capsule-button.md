---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-pharma-gel-capsule-button/"
title: "CSS Pharma Gel Capsule Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A two-tone gelatin capsule with a wet specular streak, a visible seam where the halves overlap, and a dose of liquid that rises through the shell on hover."
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Pharma Gel Capsule Button
Source: https://codefronts.com/components/css-buttons/css-pharma-gel-capsule-button/

A two-tone gelatin capsule with a wet specular streak, a visible seam where the halves overlap, and a dose of liquid that rises through the shell on hover. Press it and the capsule compresses along its long axis like soft gelatin.
## HTML
```html
<div class="cb-26">
  <div class="cb-26__stage">
    <button class="cb-26__btn" type="button">
      <span class="cb-26__dose" aria-hidden="true"></span>
      <span class="cb-26__shine" aria-hidden="true"></span>
      <span class="cb-26__label">Take one daily</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@500;600;700&display=swap');

.cb-26 {
  --bg: #eef2f4;
  --cap: #f6f8fa;
  --body: #e0483c;
  --liquid: #ffb347;
  --ink: #ffffff;
  --ink-alt: #3a2d2b;
  --cap-w: 5.5rem;
  --sans: "DM Sans",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(34rem 20rem at 50% 40%, #ffffff, transparent 70%), var(--bg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .cb-26 {
    --bg: oklch(95.5% .006 220);
    --body: oklch(58% .19 28);
    --liquid: oklch(82% .14 72);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-26:not([data-theme="light"]) {
    --bg: #141819;
    --cap: #dfe6ea;
    --body: #c4372c;
  }
}

.cb-26[data-theme="dark"] {
  --bg: #141819;
  --cap: #dfe6ea;
  --body: #c4372c;
}

.cb-26,
.cb-26 *,
.cb-26 *::before,
.cb-26 *::after {
  box-sizing: border-box;
}

.cb-26__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-26__btn {
  position: relative;
  overflow: hidden;
  isolation: isolate;
  cursor: pointer;
  min-height: 3.5rem;
  padding: 0 2.2rem 0 calc(var(--cap-w) + 1rem);
  border: 0;
  border-radius: 999px;
  font: inherit;
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: -.005em;
  color: var(--ink);
  background-image: linear-gradient(90deg, var(--cap) 0 var(--cap-w), var(--body) var(--cap-w) 100%), linear-gradient(90deg, transparent calc(var(--cap-w) - .5rem), rgba(0,0,0,.14) calc(var(--cap-w) - .1rem), rgba(255,255,255,.32) calc(var(--cap-w) + .2rem), transparent calc(var(--cap-w) + .7rem));
  box-shadow: inset 0 -.35rem .7rem rgba(0,0,0,.18), inset 0 .3rem .5rem rgba(255,255,255,.5), 0 14px 26px -14px rgba(30,20,18,.55);
  transition: scale .3s cubic-bezier(.16,1,.3,1), translate .3s cubic-bezier(.16,1,.3,1), box-shadow .3s ease;
  -webkit-tap-highlight-color: transparent;
}

.cb-26__label {
  position: relative;
  z-index: 4;
  text-shadow: 0 1px 1px rgba(80,20,14,.4);
}
/* The dose has square corners on purpose: the capsule's own overflow:hidden +
   border-radius clip it, so the liquid takes the exact shape of the rounded cap. */

.cb-26__dose {
  position: absolute;
  z-index: 2;
  left: 0;
  top: 0;
  bottom: 0;
  right: calc(100% - var(--cap-w));
  transform-origin: 50% 100%;
  background: linear-gradient(180deg,
      color-mix(in oklab,var(--liquid) 70%,white),
      var(--liquid) 42%,
      color-mix(in oklab,var(--liquid) 82%,black));
  box-shadow: inset 0 .1rem 0 rgba(255,255,255,.6), inset 0 -.3rem .5rem rgba(120,60,0,.22);
  scale: 1 .22;
  transition: scale .55s cubic-bezier(.16,1,.3,1);
}

.cb-26__shine {
  position: absolute;
  z-index: 3;
  inset: 14% 8% auto;
  height: 26%;
  border-radius: 999px;
  pointer-events: none;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,.85) 20%, rgba(255,255,255,.5) 58%, transparent);
  filter: blur(1.5px);
}

.cb-26__btn:is(:hover,:focus-visible) .cb-26__dose {
  scale: 1 .84;
}

.cb-26__btn:hover {
  translate: 0 -2px;
}

.cb-26__btn:active {
  scale: 1.03 .9;
  translate: 0 1px;
  box-shadow: inset 0 .3rem .8rem rgba(0,0,0,.28);
}

.cb-26__btn:focus-visible {
  outline: 2px solid var(--body);
  outline-offset: 4px;
}

.cb-26__btn:disabled {
  cursor: not-allowed;
  filter: grayscale(.75);
  opacity: .7;
}

@media (prefers-reduced-motion: reduce) {
  .cb-26__btn,
    .cb-26__dose {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-26__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .cb-26__dose,
    .cb-26__shine {
    display: none;
  }
}
```
