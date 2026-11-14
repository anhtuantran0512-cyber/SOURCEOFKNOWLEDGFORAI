---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-vintage-rx-pharmacy-label-button/"
title: "CSS Vintage Rx Pharmacy Label Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "An apothecary label on aged amber stock: typewriter setting with a red rule, a serrated tear edge along the top, and a rubber \"REFILL\" stamp that thuds in at…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Vintage Rx Pharmacy Label Button
Source: https://codefronts.com/components/css-buttons/css-vintage-rx-pharmacy-label-button/

An apothecary label on aged amber stock: typewriter setting with a red rule, a serrated tear edge along the top, and a rubber "REFILL" stamp that thuds in at an angle on hover — slightly off-register and unevenly inked, the way a real stamp lands.
## HTML
```html
<div class="cb-43">
  <div class="cb-43__stage">
    <button class="cb-43__btn" type="button">
      <span class="cb-43__head">
        <span class="cb-43__rx">℞</span>
        <span class="cb-43__no">No. 40218</span>
      </span>
      <span class="cb-43__name">Tincture of Focus</span>
      <span class="cb-43__dose">Take one capsule at dawn · 30 ct · 1953</span>
      <span class="cb-43__stamp" aria-hidden="true">Refill</span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Special+Elite&family=Courier+Prime:wght@400;700&display=swap');

.cb-43 {
  --bg: #2b241b;
  --paper: #e8d9b0;
  --paper-lo: #d6c393;
  --ink: #2a2318;
  --rule: #a8321f;
  --stamp: #9b2b21;
  --mono: "Courier Prime",ui-monospace,"Courier New",Courier,monospace;
  --slab: "Special Elite",ui-monospace,"Courier New",Courier,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(34rem 22rem at 50% 34%, rgba(255,255,255,.06), transparent 72%), var(--bg);
  font-family: var(--mono);
}

@supports (color: oklch(50% 0 0)) {
  .cb-43 {
    --paper: oklch(88% .05 88);
    --paper-lo: oklch(81% .06 86);
    --rule: oklch(48% .16 33);
    --stamp: oklch(44% .16 30);
  }
}

@media (prefers-color-scheme: light) {
  .cb-43:not([data-theme="dark"]) {
    --bg: #3a3126;
  }
}

.cb-43[data-theme="light"] {
  --bg: #3a3126;
}

.cb-43,
.cb-43 *,
.cb-43 *::before,
.cb-43 *::after {
  box-sizing: border-box;
}

.cb-43__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-43__btn {
  position: relative;
  overflow: hidden;
  cursor: pointer;
  display: grid;
  gap: .45rem;
  justify-items: start;
  width: min(100%,22rem);
  padding: 1.3rem 1.4rem 1.2rem;
  border: 0;
  border-radius: .15rem;
  text-align: left;
  color: var(--ink);
  background-color: var(--paper);
  background-image: radial-gradient(.05rem .05rem at 30% 42%, rgba(90,70,40,.22) 99%, transparent), radial-gradient(3rem 2rem at 84% 22%, rgba(150,110,50,.16), transparent 72%), radial-gradient(2.4rem 1.8rem at 14% 82%, rgba(150,110,50,.14), transparent 74%), linear-gradient(168deg, var(--paper), var(--paper-lo));
  background-size: 6px 6px, 100% 100%, 100% 100%, 100% 100%;
  -webkit-mask: conic-gradient(from -45deg at 50% 100%, #000 90deg, transparent 0) 0 0/.7rem .35rem repeat-x, linear-gradient(#000,#000) 0 100%/100% calc(100% - .34rem) no-repeat;
  mask: conic-gradient(from -45deg at 50% 100%, #000 90deg, transparent 0) 0 0/.7rem .35rem repeat-x, linear-gradient(#000,#000) 0 100%/100% calc(100% - .34rem) no-repeat;
  filter: drop-shadow(0 12px 18px rgba(0,0,0,.5));
  transition: translate .3s cubic-bezier(.16,1,.3,1), filter .3s ease;
  -webkit-tap-highlight-color: transparent;
}

.cb-43__head {
  display: flex;
  align-items: baseline;
  gap: .6rem;
  margin-top: .35rem;
}

.cb-43__rx {
  font-family: var(--slab);
  font-size: 1.5rem;
  line-height: 1;
  color: var(--rule);
}

.cb-43__no {
  font-size: .75rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  font-variant-numeric: tabular-nums;
}

.cb-43__name {
  position: relative;
  font-family: var(--slab);
  font-size: 1.35rem;
  line-height: 1.1;
  letter-spacing: -.01em;
  padding-bottom: .35rem;
}

.cb-43__name::after {
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 2px;
  background: var(--rule);
}

.cb-43__dose {
  font-size: .8125rem;
  line-height: 1.5;
  color: color-mix(in oklab,var(--ink) 82%,var(--paper));
  font-variant-numeric: tabular-nums;
}

.cb-43__stamp {
  position: absolute;
  right: .9rem;
  bottom: .55rem;
  padding: .25rem .7rem;
  font-family: var(--slab);
  font-size: 1.25rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--stamp);
  border: 2px solid var(--stamp);
  border-radius: .2rem;
  -webkit-mask: radial-gradient(.09rem .09rem at 32% 44%, transparent 99%, #000 0) 0 0/5px 5px, linear-gradient(#000,#000);
  mask: radial-gradient(.09rem .09rem at 32% 44%, transparent 99%, #000 0) 0 0/5px 5px, linear-gradient(#000,#000);
  -webkit-mask-composite: source-in;
  mask-composite: intersect;
  rotate: -14deg;
  scale: 1.6;
  opacity: 0;
  transition: scale .34s cubic-bezier(.2,1.6,.4,1), opacity .2s ease;
}

.cb-43__btn:is(:hover,:focus-visible) {
  translate: 0 -2px;
  filter: drop-shadow(0 18px 24px rgba(0,0,0,.55));
}

.cb-43__btn:is(:hover,:focus-visible) .cb-43__stamp {
  scale: 1;
  opacity: .88;
}

.cb-43__btn:focus-visible {
  outline: 2px solid var(--rule);
  outline-offset: 4px;
}

.cb-43__btn:active {
  translate: 0 1px;
}

.cb-43__btn:disabled {
  cursor: not-allowed;
  filter: grayscale(.5);
  opacity: .7;
}

@media (prefers-reduced-motion: reduce) {
  .cb-43__btn,
    .cb-43__stamp {
    transition: opacity .15s linear;
  }

  .cb-43__stamp {
    scale: 1;
  }
}

@media (forced-colors: active) {
  .cb-43__btn {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
    mask: none;
    -webkit-mask: none;
    filter: none;
  }

  .cb-43__stamp {
    color: ButtonText;
    border-color: ButtonText;
    mask: none;
    -webkit-mask: none;
  }

  .cb-43__name::after {
    background: ButtonText;
  }
}
```
