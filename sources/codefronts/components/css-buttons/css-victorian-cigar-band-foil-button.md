---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-victorian-cigar-band-foil-button/"
title: "CSS Victorian Cigar Band Foil Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A cigar band in embossed gold foil: scalloped top and bottom edges, a guilloché lattice engraved into the field, a laurel medallion struck in the centre, and…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Victorian Cigar Band Foil Button
Source: https://codefronts.com/components/css-buttons/css-victorian-cigar-band-foil-button/

A cigar band in embossed gold foil: scalloped top and bottom edges, a guilloché lattice engraved into the field, a laurel medallion struck in the centre, and small-caps lettering raised with a two-tone bevel. Hover tilts the foil so the light runs the other way.
## HTML
```html
<div class="cb-46">
  <div class="cb-46__stage">
    <button class="cb-46__btn" type="button">
      <span class="cb-46__lattice" aria-hidden="true"></span>
      <span class="cb-46__medal" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"><path d="M12 4c-2.4 2.6-3.4 5.6-3 8.6.3 2.4 1.5 4.4 3 6.4 1.5-2 2.7-4 3-6.4.4-3-.6-6-3-8.6z"/><path d="M8.4 9.6c-1.6.3-2.8 1.2-3.6 2.6M15.6 9.6c1.6.3 2.8 1.2 3.6 2.6"/></svg>
      </span>
      <span class="cb-46__label">Havana Reserve</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&display=swap');

.cb-46 {
  --bg: #1a120c;
  --ink: #3c2a0c;
  --ink-hi: #fff3d0;
  --radius: .2rem;
  --serif: "Cinzel",ui-serif,Georgia,"Times New Roman",serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(32rem 20rem at 50% 42%, rgba(215,170,90,.16), transparent 72%), var(--bg);
  font-family: var(--serif);
}

@media (prefers-color-scheme: light) {
  .cb-46:not([data-theme="dark"]) {
    --bg: #241810;
  }
}

.cb-46[data-theme="light"] {
  --bg: #241810;
}

.cb-46,
.cb-46 *,
.cb-46 *::before,
.cb-46 *::after {
  box-sizing: border-box;
}

.cb-46__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-46__btn {
  position: relative;
  overflow: hidden;
  cursor: pointer;
  display: grid;
  grid-auto-flow: column;
  align-items: center;
  gap: .85rem;
  min-height: 4.5rem;
  padding: 1rem 2.4rem;
  border: 0;
  border-radius: var(--radius);
  font: inherit;
  font-size: 1.0625rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--ink);
  background: linear-gradient(104deg, #7d5a1e, #f6e3ae 22%, #c99f4f 42%, #8d6a2c 58%, #f2dda6 78%, #8a6528);
  background-size: 180% 100%;
  background-position: 0% 0%;
  text-shadow: 0 1px 0 rgba(255,247,220,.72), 0 -1px 0 rgba(60,42,12,.5);
  -webkit-mask: radial-gradient(.42rem .42rem at 50% 100%, #000 96%, transparent 0) 0 0/.84rem .42rem repeat-x, radial-gradient(.42rem .42rem at 50% 0, #000 96%, transparent 0) 0 100%/.84rem .42rem repeat-x, linear-gradient(#000,#000) 0 .4rem/100% calc(100% - .8rem) no-repeat;
  mask: radial-gradient(.42rem .42rem at 50% 100%, #000 96%, transparent 0) 0 0/.84rem .42rem repeat-x, radial-gradient(.42rem .42rem at 50% 0, #000 96%, transparent 0) 0 100%/.84rem .42rem repeat-x, linear-gradient(#000,#000) 0 .4rem/100% calc(100% - .8rem) no-repeat;
  filter: drop-shadow(0 10px 16px rgba(0,0,0,.6));
  transition: background-position .7s cubic-bezier(.16,1,.3,1), translate .3s cubic-bezier(.16,1,.3,1), filter .3s ease;
  -webkit-tap-highlight-color: transparent;
}

.cb-46__lattice {
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: .5;
  background: repeating-linear-gradient(30deg, rgba(60,42,12,.16) 0 1px, transparent 1px 7px), repeating-linear-gradient(-30deg, rgba(60,42,12,.14) 0 1px, transparent 1px 7px);
}

.cb-46__medal {
  position: relative;
  z-index: 2;
  display: grid;
  place-items: center;
  width: 2.1rem;
  height: 2.1rem;
  border-radius: 50%;
  color: var(--ink);
  background: radial-gradient(circle at 36% 30%, #fbeec2, #c99f4f 62%, #8a6528);
  box-shadow: inset 0 1px 0 rgba(255,247,220,.7), inset 0 -1px 2px rgba(60,42,12,.5), 0 1px 2px rgba(0,0,0,.4);
}

.cb-46__medal svg {
  width: 1.2rem;
  height: 1.2rem;
}

.cb-46__label {
  position: relative;
  z-index: 2;
}

.cb-46__btn:is(:hover,:focus-visible) {
  background-position: 100% 0%;
  translate: 0 -2px;
  filter: drop-shadow(0 16px 22px rgba(0,0,0,.65));
}

.cb-46__btn:focus-visible {
  outline: 2px solid #f6e3ae;
  outline-offset: 5px;
}

.cb-46__btn:active {
  translate: 0 1px;
  filter: drop-shadow(0 4px 8px rgba(0,0,0,.6));
}

.cb-46__btn:disabled {
  cursor: not-allowed;
  filter: grayscale(.7);
  opacity: .75;
}

@media (prefers-reduced-motion: reduce) {
  .cb-46__btn {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-46__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    mask: none;
    -webkit-mask: none;
    text-shadow: none;
    filter: none;
  }

  .cb-46__lattice {
    display: none;
  }

  .cb-46__medal {
    background: ButtonFace;
    border: 1px solid ButtonText;
    box-shadow: none;
  }
}
```
