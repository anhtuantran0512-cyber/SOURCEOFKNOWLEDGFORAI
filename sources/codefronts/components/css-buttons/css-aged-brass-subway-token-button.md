---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-aged-brass-subway-token-button/"
title: "CSS Aged Brass Subway Token Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A 1953 transit token: milled rim, tarnished brass, and a knocked-out letter you can see the background through — a mask-composite cut, not a coloured glyph."
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aged Brass Subway Token Button
Source: https://codefronts.com/components/css-buttons/css-aged-brass-subway-token-button/

A 1953 transit token: milled rim, tarnished brass, and a knocked-out letter you can see the background through — a mask-composite cut, not a coloured glyph. Press it and the token drops into the slot and springs back up.
## HTML
```html
<div class="cb-42">
  <div class="cb-42__stage">
    <button class="cb-42__btn" type="button" aria-label="Use one transit token">
      <span class="cb-42__slot" aria-hidden="true"></span>
      <span class="cb-42__disc" aria-hidden="true">
        <span class="cb-42__rim"></span>
        <span class="cb-42__patina"></span>
        <span class="cb-42__glyph">T</span>
      </span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&display=swap');

.cb-42 {
  --bg: #191c1a;
  --brass: #a98a4a;
  --brass-hi: #dcbe7c;
  --brass-lo: #6d5527;
  --patina: #4f7a5f;
  --reed-hi: #cfae68;
  --reed-lo: #7a5f2c;
  --size: 7.5rem;
  --sans: "Oswald",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(30rem 20rem at 50% 44%, #26302a, transparent 74%), var(--bg);
  font-family: var(--sans);
}

@supports (color: oklch(50% 0 0)) {
  .cb-42 {
    --brass: oklch(64% .08 88);
    --brass-hi: oklch(82% .09 90);
    --brass-lo: oklch(44% .07 85);
  }
}

@media (prefers-color-scheme: light) {
  .cb-42:not([data-theme="dark"]) {
    --bg: #242926;
  }
}

.cb-42[data-theme="light"] {
  --bg: #242926;
}

.cb-42,
.cb-42 *,
.cb-42 *::before,
.cb-42 *::after {
  box-sizing: border-box;
}

.cb-42__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-42__btn {
  position: relative;
  cursor: pointer;
  border: 0;
  background: transparent;
  padding: 0;
  width: var(--size);
  height: calc(var(--size) + 1.4rem);
  display: grid;
  place-items: start center;
  font: inherit;
  -webkit-tap-highlight-color: transparent;
}

.cb-42__slot {
  position: absolute;
  left: 12%;
  right: 12%;
  bottom: .35rem;
  height: .5rem;
  border-radius: 999px;
  background: linear-gradient(180deg, #0a0c0b, #1d221f);
  box-shadow: inset 0 2px 4px rgba(0,0,0,.9), 0 1px 0 rgba(255,255,255,.08);
}

.cb-42__disc {
  position: relative;
  display: grid;
  place-items: center;
  width: var(--size);
  height: var(--size);
  border-radius: 50%;
  isolation: isolate;
  color: var(--brass-lo);
  background: radial-gradient(circle at 34% 28%, var(--brass-hi), transparent 54%), radial-gradient(circle at 72% 78%, var(--brass-lo), transparent 56%), linear-gradient(152deg, var(--brass), color-mix(in oklab,var(--brass) 80%,black));
  box-shadow: inset 0 2px 3px rgba(255,255,255,.4), inset 0 -3px 6px rgba(0,0,0,.45), 0 14px 22px -10px rgba(0,0,0,.8);
  transition: translate .3s cubic-bezier(.16,1,.3,1), scale .3s ease, filter .3s ease;
}

.cb-42__rim {
  position: absolute;
  inset: 0;
  z-index: 2;
  border-radius: 50%;
  background: repeating-conic-gradient(from 0deg, var(--reed-hi) 0deg 1.6deg, var(--reed-lo) 1.6deg 3.2deg);
  -webkit-mask: radial-gradient(farthest-side, transparent calc(100% - 6px), #000 calc(100% - 6px));
  mask: radial-gradient(farthest-side, transparent calc(100% - 6px), #000 calc(100% - 6px));
  opacity: .85;
}

.cb-42__patina {
  position: absolute;
  inset: 0;
  z-index: 1;
  border-radius: 50%;
  mix-blend-mode: color-burn;
  opacity: .45;
  background: radial-gradient(2rem 1.6rem at 26% 74%, var(--patina), transparent 72%), radial-gradient(1.6rem 2rem at 76% 32%, var(--patina), transparent 74%);
}

.cb-42__glyph {
  position: relative;
  z-index: 3;
  font-size: 3.1rem;
  font-weight: 700;
  line-height: 1;
  color: var(--brass-lo);
  text-shadow: 0 1px 0 rgba(255,255,255,.35), 0 -1px 0 rgba(0,0,0,.45);
}

@supports ((mask-composite: exclude) or (-webkit-mask-composite: destination-out)) {
  .cb-42__glyph {
    color: transparent;
    text-shadow: none;
  }

  .cb-42__disc {
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Ctext x='60' y='86' font-family='Oswald,sans-serif' font-size='78' font-weight='700' text-anchor='middle' fill='%23000'%3ET%3C/text%3E%3C/svg%3E") 50% 50%/60% 60% no-repeat, linear-gradient(#000,#000);
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Ctext x='60' y='86' font-family='Oswald,sans-serif' font-size='78' font-weight='700' text-anchor='middle' fill='%23000'%3ET%3C/text%3E%3C/svg%3E") 50% 50%/60% 60% no-repeat, linear-gradient(#000,#000);
    -webkit-mask-composite: destination-out;
    mask-composite: exclude;
  }
}

.cb-42__btn:hover .cb-42__disc {
  translate: 0 -3px;
  filter: brightness(1.06);
}

.cb-42__btn:focus-visible {
  outline: none;
}

.cb-42__btn:focus-visible .cb-42__disc {
  outline: 2px solid var(--brass-hi);
  outline-offset: 5px;
}

.cb-42__btn:active .cb-42__disc {
  animation: cb-42-drop .62s cubic-bezier(.3,.05,.4,1);
}

@keyframes cb-42-drop {
  0% {
    translate: 0 0;
  }

  38% {
    translate: 0 1.15rem;
    scale: 1 .94;
  }

  62% {
    translate: 0 -.3rem;
    scale: 1 1.02;
  }

  100% {
    translate: 0 0;
    scale: 1 1;
  }
}

.cb-42__btn:disabled {
  cursor: not-allowed;
  filter: grayscale(.7) brightness(.85);
}

@media (prefers-reduced-motion: reduce) {
  .cb-42__disc {
    transition: none;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .cb-42__disc {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
    mask: none;
    -webkit-mask: none;
  }

  .cb-42__glyph {
    color: ButtonText;
    text-shadow: none;
  }

  .cb-42__rim,
    .cb-42__patina,
    .cb-42__slot {
    display: none;
  }
}
```
