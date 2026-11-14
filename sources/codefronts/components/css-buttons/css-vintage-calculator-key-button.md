---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-vintage-calculator-key-button/"
title: "CSS Vintage Calculator Key Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A 1974 desk calculator key: warm beige ABS with a dished top, a chamfered skirt, tight 3px travel, and the orange function key beside it."
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Vintage Calculator Key Button
Source: https://codefronts.com/components/css-buttons/css-vintage-calculator-key-button/

A 1974 desk calculator key: warm beige ABS with a dished top, a chamfered skirt, tight 3px travel, and the orange function key beside it. The dish is two counter-facing radial gradients, and the press collapses a hard shadow stack so it lands with an audible-looking stop.
## HTML
```html
<div class="cb-47">
  <div class="cb-47__stage">
    <div class="cb-47__pad">
      <button class="cb-47__key" type="button">Total</button>
      <button class="cb-47__key cb-47__key--accent" type="button">C</button>
    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600&display=swap');

.cb-47 {
  --bg: #3d3a33;
  --panel: #57534a;
  --cap: #e0d8c6;
  --cap-lo: #cdc4ae;
  --skirt: #b3a992;
  --skirt-lo: #8d8471;
  --ink: #3a352b;
  --accent: #e0642a;
  --accent-lo: #c14f1c;
  --accent-ink: #fff3e6;
  --sans: "Oswald",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(30rem 20rem at 50% 42%, rgba(255,255,255,.06), transparent 72%), var(--bg);
  font-family: var(--sans);
}

@supports (color: oklch(50% 0 0)) {
  .cb-47 {
    --cap: oklch(89% .022 88);
    --cap-lo: oklch(83% .026 86);
    --accent: oklch(62% .17 43);
  }
}

@media (prefers-color-scheme: dark) {
  .cb-47:not([data-theme="light"]) {
    --bg: #22211d;
    --panel: #33322c;
  }
}

.cb-47[data-theme="dark"] {
  --bg: #22211d;
  --panel: #33322c;
}

.cb-47,
.cb-47 *,
.cb-47 *::before,
.cb-47 *::after {
  box-sizing: border-box;
}

.cb-47__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-47__pad {
  display: flex;
  gap: .7rem;
  padding: .85rem;
  border-radius: .5rem;
  background: linear-gradient(180deg, color-mix(in oklab,var(--panel) 88%,white 6%), var(--panel));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.16), inset 0 -2px 5px rgba(0,0,0,.45), 0 16px 26px -14px rgba(0,0,0,.7);
}

.cb-47__key {
  cursor: pointer;
  display: grid;
  place-items: center;
  min-width: 5.5rem;
  min-height: 3.4rem;
  padding: 0 1.2rem;
  border: 0;
  border-radius: .3rem .3rem .45rem .45rem;
  font: inherit;
  font-size: .9375rem;
  font-weight: 500;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--ink);
  background: radial-gradient(120% 100% at 50% -18%, rgba(0,0,0,.15), transparent 58%), radial-gradient(120% 90% at 50% 118%, rgba(255,255,255,.6), transparent 56%), linear-gradient(180deg, var(--cap-lo), var(--cap));
  text-shadow: 0 1px 0 rgba(255,255,255,.55);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5), inset 0 -1px 0 rgba(0,0,0,.12), 0 1px 0 var(--skirt), 0 2px 0 var(--skirt-lo), 0 3px 0 var(--skirt-lo), 0 7px 11px -5px rgba(0,0,0,.45);
  transition: translate .08s linear, box-shadow .08s linear, filter .2s ease;
  -webkit-tap-highlight-color: transparent;
}

.cb-47__key--accent {
  min-width: 3.6rem;
  color: var(--accent-ink);
  background: radial-gradient(120% 100% at 50% -18%, rgba(0,0,0,.22), transparent 58%), radial-gradient(120% 90% at 50% 118%, rgba(255,255,255,.32), transparent 56%), linear-gradient(180deg, var(--accent-lo), var(--accent));
  text-shadow: 0 1px 0 rgba(0,0,0,.35);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.35), inset 0 -1px 0 rgba(0,0,0,.25), 0 1px 0 #a4400f, 0 2px 0 #8d370c, 0 3px 0 #8d370c, 0 7px 11px -5px rgba(0,0,0,.5);
}

.cb-47__key:hover {
  filter: brightness(1.04);
}

.cb-47__key:active {
  translate: 0 3px;
  box-shadow: inset 0 1px 3px rgba(0,0,0,.28), 0 1px 0 var(--skirt-lo), 0 2px 4px -2px rgba(0,0,0,.45);
}

.cb-47__key--accent:active {
  box-shadow: inset 0 1px 3px rgba(0,0,0,.4), 0 1px 0 #8d370c, 0 2px 4px -2px rgba(0,0,0,.5);
}

.cb-47__key:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.cb-47__key:disabled {
  cursor: not-allowed;
  filter: grayscale(.5) brightness(.94);
  box-shadow: 0 1px 0 var(--skirt-lo);
  translate: 0 2px;
}

@media (prefers-reduced-motion: reduce) {
  .cb-47__key {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-47__pad {
    background: Canvas;
    box-shadow: none;
    border: 1px solid CanvasText;
  }

  .cb-47__key {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
    text-shadow: none;
  }
}
```
