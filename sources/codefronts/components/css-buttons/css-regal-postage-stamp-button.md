---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-regal-postage-stamp-button/"
title: "CSS Regal Postage Stamp Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A commemorative stamp with true perforations on all four edges, an engraved portrait in sepia, a denomination cartouche, and a postmark that lands across the…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Regal Postage Stamp Button
Source: https://codefronts.com/components/css-buttons/css-regal-postage-stamp-button/

A commemorative stamp with true perforations on all four edges, an engraved portrait in sepia, a denomination cartouche, and a postmark that lands across the corner on hover — concentric rings plus a wavy cancellation bar, rotated and slightly off-centre.
## HTML
```html
<div class="cb-45">
  <div class="cb-45__stage">
    <button class="cb-45__btn" type="button">
      <span class="cb-45__inner">
        <span class="cb-45__win">
          <img class="cb-45__art" src="https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=700&amp;q=70&amp;auto=format&amp;fit=crop" alt="Engraved view of a European cathedral square" width="700" height="500" loading="lazy" decoding="async">
        </span>
        <span class="cb-45__caption">
          <span class="cb-45__country">Post &amp; Telegraph</span>
          <span class="cb-45__label">Send the letter</span>
        </span>
        <span class="cb-45__value">7½<small>d</small></span>
      </span>
      <span class="cb-45__mark" aria-hidden="true">
        <span class="cb-45__markRing"></span>
        <span class="cb-45__markRing"></span>
        <span class="cb-45__markBar"></span>
      </span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=EB+Garamond:wght@500;600&display=swap');

.cb-45 {
  --bg: #20211c;
  --stock: #f0e6cf;
  --stock-lo: #ddd0b3;
  --ink: #2d2a1f;
  --accent: #7b3f2f;
  --mark: #2c3a4a;
  --serif: "Cinzel",ui-serif,Georgia,"Times New Roman",serif;
  --body: "EB Garamond",ui-serif,Georgia,serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(32rem 20rem at 50% 40%, rgba(255,255,255,.06), transparent 72%), var(--bg);
  font-family: var(--body);
}

@supports (color: oklch(50% 0 0)) {
  .cb-45 {
    --stock: oklch(93% .03 88);
    --stock-lo: oklch(86% .04 86);
    --accent: oklch(42% .09 38);
  }
}

@media (prefers-color-scheme: light) {
  .cb-45:not([data-theme="dark"]) {
    --bg: #2b2c25;
  }
}

.cb-45[data-theme="light"] {
  --bg: #2b2c25;
}

.cb-45,
.cb-45 *,
.cb-45 *::before,
.cb-45 *::after {
  box-sizing: border-box;
}

.cb-45__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-45__btn {
  position: relative;
  cursor: pointer;
  border: 0;
  padding: .55rem;
  width: 13.5rem;
  font: inherit;
  color: var(--ink);
  text-align: center;
  background: linear-gradient(165deg, var(--stock), var(--stock-lo));
  -webkit-mask: radial-gradient(.3rem .3rem at 50% 0, #000 96%, transparent 0) 0 0/.62rem .62rem repeat-x, radial-gradient(.3rem .3rem at 50% 100%, #000 96%, transparent 0) 0 100%/.62rem .62rem repeat-x, radial-gradient(.3rem .3rem at 0 50%, #000 96%, transparent 0) 0 0/.62rem .62rem repeat-y, radial-gradient(.3rem .3rem at 100% 50%, #000 96%, transparent 0) 100% 0/.62rem .62rem repeat-y, linear-gradient(#000,#000);
  mask: radial-gradient(.3rem .3rem at 50% 0, #000 96%, transparent 0) 0 0/.62rem .62rem repeat-x, radial-gradient(.3rem .3rem at 50% 100%, #000 96%, transparent 0) 0 100%/.62rem .62rem repeat-x, radial-gradient(.3rem .3rem at 0 50%, #000 96%, transparent 0) 0 0/.62rem .62rem repeat-y, radial-gradient(.3rem .3rem at 100% 50%, #000 96%, transparent 0) 100% 0/.62rem .62rem repeat-y, linear-gradient(#000,#000);
  -webkit-mask-composite: xor;
  mask-composite: exclude;
  filter: drop-shadow(0 12px 18px rgba(0,0,0,.55));
  transition: translate .32s cubic-bezier(.16,1,.3,1), rotate .32s cubic-bezier(.16,1,.3,1), filter .32s ease;
  -webkit-tap-highlight-color: transparent;
}

.cb-45__inner {
  display: grid;
  gap: .5rem;
  padding: .7rem .65rem .6rem;
  border: 1px solid color-mix(in oklab,var(--ink) 35%,transparent);
}
/* The flat fallback stays a legible engraved-looking plate if the photo 404s. */

.cb-45__win {
  display: block;
  aspect-ratio: 7/5;
  overflow: hidden;
  background: repeating-linear-gradient(28deg, color-mix(in oklab,var(--ink) 30%,transparent) 0 1px, transparent 1px 5px), color-mix(in oklab,var(--ink) 18%,var(--stock));
}

.cb-45__art {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: sepia(.72) contrast(1.25) saturate(.7) brightness(.95);
}

.cb-45__caption {
  display: grid;
  gap: .15rem;
}

.cb-45__country {
  font-family: var(--serif);
  font-size: .6875rem;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--accent);
}

.cb-45__label {
  font-family: var(--serif);
  font-size: .9375rem;
  font-weight: 600;
  letter-spacing: .03em;
}

.cb-45__value {
  position: absolute;
  top: 1rem;
  right: 1rem;
  padding: .15rem .35rem;
  font-family: var(--serif);
  font-size: .9375rem;
  font-weight: 700;
  line-height: 1;
  color: var(--stock);
  background: var(--accent);
  border-radius: .1rem;
  font-variant-numeric: tabular-nums;
}

.cb-45__value small {
  font-size: .6875rem;
}

.cb-45__mark {
  position: absolute;
  left: .9rem;
  top: 1.4rem;
  width: 6.5rem;
  height: 6.5rem;
  pointer-events: none;
  rotate: -16deg;
  scale: 1.5;
  opacity: 0;
  transition: scale .38s cubic-bezier(.2,1.5,.4,1), opacity .22s ease;
}

.cb-45__markRing {
  position: absolute;
  inset: 0;
  border: 2px solid var(--mark);
  border-radius: 50%;
}

.cb-45__markRing:last-of-type {
  inset: 12%;
  border-width: 1px;
}

.cb-45__markBar {
  position: absolute;
  left: -25%;
  right: -25%;
  top: 46%;
  height: .9rem;
  background: repeating-linear-gradient(0deg, var(--mark) 0 2px, transparent 2px 5px);
  -webkit-mask: radial-gradient(.4rem .35rem at 50% 0, transparent 96%, #000 0) 0 0/.8rem .9rem repeat-x;
  mask: radial-gradient(.4rem .35rem at 50% 0, transparent 96%, #000 0) 0 0/.8rem .9rem repeat-x;
  opacity: .85;
}

.cb-45__btn:is(:hover,:focus-visible) {
  translate: 0 -3px;
  rotate: -1.2deg;
  filter: drop-shadow(0 20px 26px rgba(0,0,0,.6));
}

.cb-45__btn:is(:hover,:focus-visible) .cb-45__mark {
  scale: 1;
  opacity: .72;
}

.cb-45__btn:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 5px;
}

.cb-45__btn:active {
  translate: 0 1px;
  rotate: 0deg;
}

.cb-45__btn:disabled {
  cursor: not-allowed;
  filter: grayscale(.6);
  opacity: .75;
}

@media (prefers-reduced-motion: reduce) {
  .cb-45__btn,
    .cb-45__mark {
    transition: opacity .15s linear;
  }

  .cb-45__mark {
    scale: 1;
  }
}

@media (forced-colors: active) {
  .cb-45__btn {
    mask: none;
    -webkit-mask: none;
    filter: none;
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .cb-45__value {
    background: ButtonFace;
    color: ButtonText;
    border: 1px solid ButtonText;
  }

  .cb-45__mark {
    display: none;
  }
}
```
