---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-lacquered-walnut-wood-button/"
title: "CSS Lacquered Walnut Wood Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "Book-matched walnut under high-gloss lacquer: grain built from four repeating gradients at incommensurate frequencies so it never visibly tiles, a brass…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Lacquered Walnut Wood Button
Source: https://codefronts.com/components/css-buttons/css-lacquered-walnut-wood-button/

Book-matched walnut under high-gloss lacquer: grain built from four repeating gradients at incommensurate frequencies so it never visibly tiles, a brass inlay label, and a gloss band that travels across the finish on hover the way light moves over varnish.
## HTML
```html
<div class="cb-25">
  <div class="cb-25__stage">
    <button class="cb-25__btn" type="button">
      <span class="cb-25__gloss" aria-hidden="true"></span>
      <span class="cb-25__label">Open the cabinet</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&display=swap');

.cb-25 {
  --bg: #120d09;
  --wood: #5b3a1f;
  --wood-hi: #7d5229;
  --wood-lo: #33200f;
  --radius: .65rem;
  --serif: "Cormorant Garamond",ui-serif,Georgia,"Times New Roman",serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(40rem 24rem at 50% 40%, color-mix(in oklab,#d8a55e 12%,transparent), transparent 70%), var(--bg);
  font-family: var(--serif);
}

@supports (color: oklch(50% 0 0)) {
  .cb-25 {
    --wood: oklch(38% .07 55);
    --wood-hi: oklch(47% .08 58);
    --wood-lo: oklch(25% .05 52);
  }
}

@media (prefers-color-scheme: light) {
  .cb-25:not([data-theme="dark"]) {
    --bg: #221812;
  }
}

.cb-25[data-theme="light"] {
  --bg: #221812;
}

.cb-25,
.cb-25 *,
.cb-25 *::before,
.cb-25 *::after {
  box-sizing: border-box;
}

.cb-25__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-25__btn {
  position: relative;
  overflow: hidden;
  isolation: isolate;
  cursor: pointer;
  min-height: 4rem;
  padding: 0 2.6rem;
  border: 1px solid #22150b;
  border-radius: var(--radius);
  font: inherit;
  font-size: 1.25rem;
  font-weight: 600;
  letter-spacing: .06em;
  color: #e8cd97;
  background-color: var(--wood);
  background-image: repeating-linear-gradient(92deg, rgba(0,0,0,.14) 0 1px, transparent 1px 3px), repeating-linear-gradient(88deg, rgba(0,0,0,.10) 0 2px, transparent 2px 7px), repeating-linear-gradient(91deg, rgba(255,255,255,.055) 0 1px, transparent 1px 11px), repeating-linear-gradient(89deg, rgba(0,0,0,.16) 0 3px, transparent 3px 23px), linear-gradient(100deg, var(--wood-hi), var(--wood) 45%, var(--wood-lo));
  box-shadow: inset 0 1px 0 rgba(255,255,255,.22), inset 0 -2px 4px rgba(0,0,0,.45), 0 16px 30px -14px rgba(0,0,0,.8);
  transition: translate .22s cubic-bezier(.16,1,.3,1), box-shadow .25s ease, filter .3s ease;
}

.cb-25__label {
  position: relative;
  z-index: 3;
  background: linear-gradient(180deg,#f6e3ae,#c99f4f 55%,#8d6a2c);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  filter: drop-shadow(0 1px 0 rgba(0,0,0,.6));
}

.cb-25__btn::before {
  content: '';
  position: absolute;
  inset: 0 0 auto;
  height: 38%;
  z-index: 2;
  pointer-events: none;
  background: linear-gradient(180deg, rgba(255,255,255,.16), transparent);
  border-radius: var(--radius) var(--radius) 0 0;
}

.cb-25__gloss {
  position: absolute;
  inset: -20% -30%;
  z-index: 2;
  pointer-events: none;
  background: linear-gradient(104deg, transparent 40%, rgba(255,255,255,.34) 50%, transparent 60%);
  translate: -60% 0;
  transition: translate .9s cubic-bezier(.16,1,.3,1);
}

.cb-25__btn:is(:hover,:focus-visible) .cb-25__gloss {
  translate: 60% 0;
}

.cb-25__btn:hover {
  translate: 0 -2px;
  filter: brightness(1.06);
}

.cb-25__btn:active {
  translate: 0 1px;
  box-shadow: inset 0 3px 8px rgba(0,0,0,.6);
}

.cb-25__btn:focus-visible {
  outline: 2px solid #e8cd97;
  outline-offset: 4px;
}

.cb-25__btn:disabled {
  cursor: not-allowed;
  filter: grayscale(.6) brightness(.8);
}

@media (prefers-reduced-motion: reduce) {
  .cb-25__btn,
    .cb-25__gloss {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-25__btn {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
  }

  .cb-25__label {
    background: none;
    color: ButtonText;
    -webkit-text-fill-color: ButtonText;
    filter: none;
  }

  .cb-25__gloss {
    display: none;
  }
}
```
