---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-wine-velvet-ribbon-button/"
title: "CSS Wine Velvet Ribbon Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "Crushed burgundy velvet cut as an awards ribbon: notched swallow-tail ends, a nap sheen that shifts direction as the pointer crosses (the way velvet changes…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Wine Velvet Ribbon Button
Source: https://codefronts.com/components/css-buttons/css-wine-velvet-ribbon-button/

Crushed burgundy velvet cut as an awards ribbon: notched swallow-tail ends, a nap sheen that shifts direction as the pointer crosses (the way velvet changes tone when you brush it), and gold-foil lettering with a proper bevel.
## HTML
```html
<div class="cb-35">
  <div class="cb-35__stage">
    <span class="cb-35__wrap">
      <button class="cb-35__btn" type="button">
        <span class="cb-35__nap cb-35__nap--a" aria-hidden="true"></span>
        <span class="cb-35__nap cb-35__nap--b" aria-hidden="true"></span>
        <span class="cb-35__label">Reserve the cellar</span>
      </button>
    </span>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&display=swap');

.cb-35 {
  --bg: #160b10;
  --wine: #5c1026;
  --wine-hi: #8a1c3a;
  --wine-lo: #320611;
  --foil: #e8c67a;
  --serif: "Playfair Display",ui-serif,Georgia,"Times New Roman",serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(34rem 22rem at 50% 42%, color-mix(in oklab,var(--wine) 32%,transparent), transparent 74%), var(--bg);
  font-family: var(--serif);
}

@supports (color: oklch(50% 0 0)) {
  .cb-35 {
    --wine: oklch(33% .14 12);
    --wine-hi: oklch(42% .17 10);
    --wine-lo: oklch(22% .11 12);
    --foil: oklch(84% .1 84);
  }
}

@media (prefers-color-scheme: light) {
  .cb-35:not([data-theme="dark"]) {
    --bg: #241118;
  }
}

.cb-35[data-theme="light"] {
  --bg: #241118;
}

.cb-35,
.cb-35 *,
.cb-35 *::before,
.cb-35 *::after {
  box-sizing: border-box;
}

.cb-35__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-35__wrap {
  display: inline-block;
  filter: drop-shadow(0 16px 24px rgba(0,0,0,.65));
  transition: translate .35s cubic-bezier(.16,1,.3,1), filter .35s ease;
}

.cb-35__wrap:has(:hover) {
  translate: 0 -2px;
  filter: drop-shadow(0 22px 30px rgba(0,0,0,.7));
}

.cb-35__wrap:has(:focus-visible) {
  outline: 2px solid var(--foil);
  outline-offset: 6px;
}

.cb-35__btn {
  position: relative;
  overflow: hidden;
  cursor: pointer;
  display: grid;
  place-items: center;
  min-height: 5.5rem;
  padding: 0 2.8rem 2.1rem;
  border: 0;
  /* Band across the top, a tail at each end, and a V notch cut up into each tail.
       One continuous outline — no self-intersection, so no stray wedges. */
  clip-path: polygon(
      0 0, 100% 0,
      100% 100%, 91% 74%, 82% 100%,
      82% 58%, 18% 58%,
      18% 100%, 9% 74%, 0 100%);
  font: inherit;
  font-size: 1.0625rem;
  font-weight: 600;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--foil);
  background-color: var(--wine);
  background-image: radial-gradient(.045rem .045rem at 30% 40%, rgba(255,255,255,.1) 99%, transparent), radial-gradient(.04rem .04rem at 72% 66%, rgba(0,0,0,.2) 99%, transparent), linear-gradient(165deg, var(--wine-hi), var(--wine) 50%, var(--wine-lo));
  background-size: 9px 9px, 13px 13px, 100% 100%;
  transition: scale .2s cubic-bezier(.16,1,.3,1);
}

.cb-35__label {
  position: relative;
  z-index: 3;
  padding-bottom: .4rem;
  background: linear-gradient(180deg,#fbeec2,#dfb96a 52%,#a67c30);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  filter: drop-shadow(0 1px 0 rgba(0,0,0,.55));
}

.cb-35__nap {
  position: absolute;
  inset: 0;
  z-index: 2;
  pointer-events: none;
  transition: opacity .5s ease;
}

.cb-35__nap--a {
  background: linear-gradient(78deg, rgba(255,255,255,.16), transparent 55%);
  opacity: 1;
}

.cb-35__nap--b {
  background: linear-gradient(-78deg, rgba(255,255,255,.2), transparent 58%);
  opacity: 0;
}

.cb-35__btn:is(:hover,:focus-visible) .cb-35__nap--a {
  opacity: 0;
}

.cb-35__btn:is(:hover,:focus-visible) .cb-35__nap--b {
  opacity: 1;
}

.cb-35__btn:focus-visible {
  outline: none;
}

.cb-35__btn:active {
  scale: .99;
}

.cb-35__btn:disabled {
  cursor: not-allowed;
  filter: grayscale(.6) brightness(.8);
}

@media (prefers-reduced-motion: reduce) {
  .cb-35__wrap,
    .cb-35__btn,
    .cb-35__nap {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-35__btn {
    clip-path: none;
    background: ButtonFace;
    border: 1px solid ButtonText;
  }

  .cb-35__label {
    background: none;
    -webkit-text-fill-color: ButtonText;
    color: ButtonText;
    filter: none;
  }

  .cb-35__nap {
    display: none;
  }

  .cb-35__wrap {
    filter: none;
  }
}
```
