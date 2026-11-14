---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-mercury-bead-morph-button/"
title: "CSS Mercury Bead Morph Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A bead of mercury detaches from the button, stretches, and is reabsorbed on hover — genuine metaball merging, produced by an SVG goo filter (blur, then a…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Mercury Bead Morph Button
Source: https://codefronts.com/components/css-buttons/css-mercury-bead-morph-button/

A bead of mercury detaches from the button, stretches, and is reabsorbed on hover — genuine metaball merging, produced by an SVG goo filter (blur, then a hard alpha threshold) applied to a layer of plain CSS shapes. No canvas, no WebGL, no JavaScript.
## HTML
```html
<div class="cb-31">
  <div class="cb-31__stage">
    <svg class="cb-31__defs" aria-hidden="true" focusable="false" width="0" height="0">
      <filter id="cb-31-goo">
        <feGaussianBlur in="SourceGraphic" stdDeviation="7" result="b"></feGaussianBlur>
        <feColorMatrix in="b" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 20 -9" result="g"></feColorMatrix>
        <feBlend in="SourceGraphic" in2="g"></feBlend>
      </filter>
    </svg>
    <button class="cb-31__btn" type="button">
      <span class="cb-31__goo" aria-hidden="true">
        <span class="cb-31__pill"></span>
        <span class="cb-31__bead"></span>
      </span>
      <span class="cb-31__label">Liquify</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap');

.cb-31 {
  --bg: #0c0e12;
  --hg: #c9d2dc;
  --hg-hi: #ffffff;
  --hg-lo: #5c6672;
  --ink: #0b0d11;
  --sans: "Space Grotesk",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(36rem 22rem at 50% 45%, #1b2029, transparent 72%), var(--bg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@media (prefers-color-scheme: light) {
  .cb-31:not([data-theme="dark"]) {
    --bg: #e7eaee;
  }
}

.cb-31[data-theme="light"] {
  --bg: #e7eaee;
}

.cb-31,
.cb-31 *,
.cb-31 *::before,
.cb-31 *::after {
  box-sizing: border-box;
}

.cb-31__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-31__defs {
  position: absolute;
  width: 0;
  height: 0;
  overflow: hidden;
}

.cb-31__btn {
  position: relative;
  cursor: pointer;
  border: 0;
  background: transparent;
  width: 16rem;
  height: 8rem;
  padding: 0;
  font: inherit;
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: -.01em;
  color: var(--ink);
  -webkit-tap-highlight-color: transparent;
}

.cb-31__label {
  position: absolute;
  z-index: 3;
  left: 3.9rem;
  top: 50%;
  translate: 0 -50%;
  transition: translate .5s cubic-bezier(.16,1,.3,1), color .4s ease;
}

.cb-31__goo {
  position: absolute;
  inset: 0;
  z-index: 1;
  filter: url(#cb-31-goo);
}
/* Both shapes paint the SAME gradient at the SAME size, so at rest the bead is
   pixel-identical to the pill's left cap and disappears into it completely. */

.cb-31__pill,
.cb-31__bead {
  position: absolute;
  border-radius: 999px;
  background-image: radial-gradient(120% 120% at 30% 20%, var(--hg-hi), transparent 55%), linear-gradient(160deg, var(--hg), var(--hg-lo));
  background-size: 8.2rem 3.2rem, 8.2rem 3.2rem;
  background-position: 0 0, 0 0;
  background-repeat: no-repeat;
}

.cb-31__pill {
  left: 2.2rem;
  top: 2.4rem;
  width: 8.2rem;
  height: 3.2rem;
}

.cb-31__bead {
  left: 2.2rem;
  top: 2.4rem;
  width: 3.2rem;
  height: 3.2rem;
  transition: translate .75s cubic-bezier(.16,1,.3,1), scale .75s cubic-bezier(.16,1,.3,1);
}

.cb-31__btn:is(:hover,:focus-visible) .cb-31__bead {
  translate: 8.4rem 0;
  scale: .62;
}

.cb-31__btn:is(:hover,:focus-visible) .cb-31__label {
  translate: .4rem -50%;
}

.cb-31__btn:focus-visible {
  outline: 2px solid var(--hg);
  outline-offset: 2px;
  border-radius: 1rem;
}

.cb-31__btn:active .cb-31__bead {
  scale: .5;
}

.cb-31__btn:disabled {
  cursor: not-allowed;
  filter: grayscale(1) brightness(.8);
}

@media (prefers-reduced-motion: reduce) {
  .cb-31__bead,
    .cb-31__label {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-31__goo {
    display: none;
  }

  .cb-31__btn {
    border: 1px solid ButtonText;
    background: ButtonFace;
    width: auto;
    height: auto;
    padding: 1rem 2rem;
  }

  .cb-31__label {
    position: static;
    translate: none;
    color: ButtonText;
  }
}
```
