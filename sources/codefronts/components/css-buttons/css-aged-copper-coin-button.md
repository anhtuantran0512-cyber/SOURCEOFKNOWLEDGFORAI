---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-aged-copper-coin-button/"
title: "CSS Aged Copper Coin Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A struck copper coin with a milled edge, verdigris patina blooming in the low spots, and a real 3D flip to its reverse face on click."
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aged Copper Coin Button
Source: https://codefronts.com/components/css-buttons/css-aged-copper-coin-button/

A struck copper coin with a milled edge, verdigris patina blooming in the low spots, and a real 3D flip to its reverse face on click. Two faces, preserve-3d, backface-visibility — and a checkbox holding the state, so no JavaScript is involved.
## HTML
```html
<div class="cb-27">
  <div class="cb-27__stage">
    <label class="cb-27__btn">
      <input type="checkbox" aria-label="Flip the coin to see the reverse">
      <span class="cb-27__disc" aria-hidden="true">
        <span class="cb-27__face cb-27__face--front">
          <span class="cb-27__edge"></span>
          <span class="cb-27__patina"></span>
          <span class="cb-27__type">1892</span>
        </span>
        <span class="cb-27__face cb-27__face--back">
          <span class="cb-27__edge"></span>
          <span class="cb-27__patina"></span>
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3.5 14.4 9l5.6.6-4.2 3.8 1.2 5.6L12 16.3 7 19l1.2-5.6L4 9.6 9.6 9 12 3.5z"/></svg>
        </span>
      </span>
    </label>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&display=swap');

.cb-27 {
  --bg: #1c2420;
  --cu: #b06a3c;
  --cu-hi: #e8a76d;
  --cu-lo: #6d3c1c;
  --patina: #3f8f74;
  --ink: #3a1c0b;
  --reed-hi: #dc9a63;
  --reed-lo: #7d4623;
  --size: 8.5rem;
  --serif: "Cinzel",ui-serif,Georgia,"Times New Roman",serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(34rem 22rem at 50% 42%, color-mix(in oklab,var(--cu) 16%,transparent), transparent 72%), var(--bg);
  font-family: var(--serif);
  perspective: 900px;
}

@supports (color: oklch(50% 0 0)) {
  .cb-27 {
    --cu: oklch(60% .11 48);
    --cu-hi: oklch(78% .1 62);
    --cu-lo: oklch(40% .09 45);
    --patina: oklch(60% .09 165);
  }
}

@media (prefers-color-scheme: light) {
  .cb-27:not([data-theme="dark"]) {
    --bg: #2b3630;
  }
}

.cb-27[data-theme="light"] {
  --bg: #2b3630;
}

.cb-27,
.cb-27 *,
.cb-27 *::before,
.cb-27 *::after {
  box-sizing: border-box;
}

.cb-27__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
  perspective: 900px;
}

.cb-27__btn {
  position: relative;
  cursor: pointer;
  display: block;
  width: var(--size);
  height: var(--size);
  -webkit-tap-highlight-color: transparent;
}

.cb-27__btn input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.cb-27__disc {
  position: relative;
  display: block;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: rotate .85s cubic-bezier(.16,1,.3,1), translate .3s ease;
}

.cb-27__face {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  isolation: isolate;
  overflow: hidden;
  border-radius: 50%;
  backface-visibility: hidden;
  color: var(--ink);
  background: radial-gradient(circle at 32% 26%, var(--cu-hi), transparent 52%), radial-gradient(circle at 70% 78%, var(--cu-lo), transparent 55%), linear-gradient(150deg, var(--cu), color-mix(in oklab,var(--cu) 78%,black));
  box-shadow: inset 0 2px 4px rgba(255,255,255,.35), inset 0 -3px 6px rgba(0,0,0,.4), 0 16px 26px -12px rgba(0,0,0,.7);
}

.cb-27__face--back {
  rotate: y 180deg;
}

.cb-27__face svg {
  width: 36%;
  height: 36%;
  position: relative;
  z-index: 3;
  filter: drop-shadow(0 1px 0 rgba(255,255,255,.4));
}

.cb-27__edge {
  position: absolute;
  inset: 0;
  z-index: 2;
  border-radius: 50%;
  background: repeating-conic-gradient(from 0deg, var(--reed-hi) 0deg 1.5deg, var(--reed-lo) 1.5deg 3deg);
  -webkit-mask: radial-gradient(farthest-side, transparent calc(100% - 6px), #000 calc(100% - 6px));
  mask: radial-gradient(farthest-side, transparent calc(100% - 6px), #000 calc(100% - 6px));
  opacity: .9;
}

.cb-27__patina {
  position: absolute;
  inset: 0;
  z-index: 1;
  border-radius: 50%;
  mix-blend-mode: color-burn;
  opacity: .55;
  background: radial-gradient(2.4rem 1.8rem at 22% 72%, var(--patina), transparent 70%), radial-gradient(1.8rem 2.2rem at 78% 30%, var(--patina), transparent 72%), radial-gradient(1.2rem 1rem at 58% 84%, var(--patina), transparent 70%);
}

.cb-27__type {
  position: relative;
  z-index: 3;
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: .12em;
  font-variant-numeric: tabular-nums;
  text-shadow: 0 1px 0 rgba(255,255,255,.42), 0 -1px 0 rgba(0,0,0,.45);
}

.cb-27__btn:hover .cb-27__disc {
  translate: 0 -3px;
}

.cb-27__btn:has(input:focus-visible) .cb-27__disc {
  outline: 2px solid var(--cu-hi);
  outline-offset: 6px;
  border-radius: 50%;
}

.cb-27__btn:has(input:checked) .cb-27__disc {
  rotate: y 180deg;
}

.cb-27__btn:active .cb-27__disc {
  scale: .97;
}

@media (prefers-reduced-motion: reduce) {
  .cb-27__disc {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-27__face {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .cb-27__edge,
    .cb-27__patina {
    display: none;
  }
}
```
