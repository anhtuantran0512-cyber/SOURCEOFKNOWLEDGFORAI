---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/brutalist-stamp/"
title: "Neo-Brutalist Badge Component CSS"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "Neubrutalism reduced to its three load-bearing rules: 2.5px solid-black borders, a hard zero-blur offset shadow, and colors that refuse to apologize. Badges…"
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neo-Brutalist Badge Component CSS
Source: https://codefronts.com/snippets/css-tags-chips/brutalist-stamp/

Neubrutalism reduced to its three load-bearing rules: 2.5px solid-black borders, a hard zero-blur offset shadow, and colors that refuse to apologize. Badges press INTO their shadow on hover (translate toward the offset while the shadow shrinks by the same amount — the move Gumroad made famous), sticker variants sit deliberately crooked and straighten when touched, and the checked state of the filter row is a full color-block inversion. No gradient anywhere in the file.
## HTML
```html
<section class="ctc-14" aria-label="Neo-brutalist badge demo">
  <div class="ctc-14__stage">
    <div class="ctc-14__wrap">
      <header class="ctc-14__head">
        <p class="ctc-14__kicker">NEUBRUTALISM · SHADOWS DON'T BLUR</p>
        <h1>Press it into the paper</h1>
      </header>
      <div class="ctc-14__panel">
        <p class="ctc-14__lab">01 · Badges — hover presses, click lands flat</p>
        <div class="ctc-14__row">
          <a class="ctc-14__b" style="--c:oklch(0.8 0.16 85)" href="#ctc14">BESTSELLER</a>
          <a class="ctc-14__b" style="--c:oklch(0.75 0.14 190)" href="#ctc14">FREE SHIPPING</a>
          <a class="ctc-14__b" style="--c:oklch(0.7 0.19 20)" href="#ctc14">50% OFF</a>
          <a class="ctc-14__b" style="--c:oklch(0.72 0.18 140)" href="#ctc14">IN STOCK</a>
        </div>
      </div>
      <div class="ctc-14__panel">
        <p class="ctc-14__lab">02 · Stickers — crooked at rest, straighten on touch</p>
        <div class="ctc-14__row ctc-14__row--stick">
          <span class="ctc-14__b ctc-14__b--stick" style="--c:oklch(0.8 0.16 85)">NEW DROP ✷</span>
          <span class="ctc-14__b ctc-14__b--stick" style="--c:oklch(0.9 0.02 90)">AS SEEN ON TV</span>
          <span class="ctc-14__b ctc-14__b--stick" style="--c:oklch(0.7 0.19 20);color:oklch(0.97 0.01 90)">HOT!</span>
        </div>
      </div>
      <form class="ctc-14__panel">
        <p class="ctc-14__lab">03 · Filter row — selected = full inversion, not a tint</p>
        <div class="ctc-14__row">
          <label class="ctc-14__b ctc-14__b--chk" style="--c:oklch(0.8 0.16 85)"><input class="ctc-14__sr" type="checkbox" checked><span>PRINTS</span></label>
          <label class="ctc-14__b ctc-14__b--chk" style="--c:oklch(0.75 0.14 190)"><input class="ctc-14__sr" type="checkbox"><span>ZINES</span></label>
          <label class="ctc-14__b ctc-14__b--chk" style="--c:oklch(0.72 0.18 140)"><input class="ctc-14__sr" type="checkbox"><span>TEES</span></label>
          <label class="ctc-14__b ctc-14__b--chk" style="--c:oklch(0.9 0.02 90)"><input class="ctc-14__sr" type="checkbox"><span>STICKERS</span></label>
          <button class="ctc-14__b ctc-14__reset" type="reset" style="--c:oklch(0.97 0.01 90)">RESET ↺</button>
        </div>
      </form>
      <p class="ctc-14__note">translate + shadow always sum to 5px — that conservation is the whole "pressed object" illusion. Selected chips invert wholesale via <code>:has(:checked)</code>; brutalism doesn't do 40% tints.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.ctc-14,
.ctc-14 *,
.ctc-14 *::before,
.ctc-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-14 {
  --bg: oklch(0.93 0.04 95);
  --ink: oklch(0.18 0 0);
  --mut: oklch(0.45 0.01 90);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-14__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  padding: clamp(16px,4cqi,48px);
  background: radial-gradient(oklch(0.18 0 0/.14) 1.5px,transparent 1.5px) 0 0/22px 22px,var(--bg);
  container: ctc14/inline-size;
}

.ctc-14__wrap {
  width: min(660px,100%);
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.ctc-14__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ctc-14__kicker {
  display: inline-block;
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .18em;
  background: var(--ink);
  color: var(--bg);
  padding: 6px 10px;
  width: fit-content;
}

.ctc-14__head h1 {
  font-size: clamp(26px,4.2cqi,42px);
  font-weight: 900;
  letter-spacing: -.02em;
  text-transform: uppercase;
  margin: 12px 0 4px;
}

.ctc-14__panel {
  background: oklch(0.97 0.01 95);
  border: 2.5px solid var(--ink);
  box-shadow: 7px 7px 0 0 var(--ink);
  padding: 18px;
}

.ctc-14__lab {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--mut);
  margin-bottom: 14px;
}

.ctc-14__row {
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  align-items: center;
}

.ctc-14__b {
  --c: oklch(0.8 0.16 85);
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 18px;
  border: 2.5px solid var(--ink);
  background: var(--c);
  color: var(--ink);
  font-size: 13.5px;
  font-weight: 800;
  letter-spacing: .06em;
  text-decoration: none;
  cursor: pointer;
  user-select: none;
  box-shadow: 5px 5px 0 0 var(--ink);
  transition: translate .12s,box-shadow .12s,rotate .25s cubic-bezier(.34,1.56,.64,1);
}

a.ctc-14__b:hover,
a.ctc-14__b:focus-visible,
.ctc-14__b--chk:hover,
.ctc-14__reset:hover,
.ctc-14__reset:focus-visible {
  translate: 2px 2px;
  box-shadow: 3px 3px 0 0 var(--ink);
}

a.ctc-14__b:active,
.ctc-14__b--chk:active,
.ctc-14__reset:active {
  translate: 5px 5px;
  box-shadow: 0 0 0 0 var(--ink);
}

a.ctc-14__b:focus-visible,
.ctc-14__reset:focus-visible {
  outline: 2.5px dashed var(--ink);
  outline-offset: 3px;
}

.ctc-14__b--stick {
  rotate: -3deg;
}

.ctc-14__row--stick .ctc-14__b--stick:nth-child(2) {
  rotate: 2.5deg;
}

.ctc-14__row--stick .ctc-14__b--stick:nth-child(3) {
  rotate: -2deg;
}

.ctc-14__b--stick:hover {
  rotate: 0deg;
  translate: 2px 2px;
  box-shadow: 3px 3px 0 0 var(--ink);
}

.ctc-14__b--chk:has(:focus-visible) {
  outline: 2.5px dashed var(--ink);
  outline-offset: 3px;
}

.ctc-14__b--chk:has(:checked) {
  background: var(--ink);
  color: var(--c);
}

.ctc-14__b--chk span::before {
  content: "□ ";
  font-weight: 900;
}

.ctc-14__b--chk:has(:checked) span::before {
  content: "■ ";
}

.ctc-14__reset {
  font: inherit;
  font-size: 13.5px;
  font-weight: 800;
  letter-spacing: .06em;
}

.ctc-14__note {
  font-size: 12.5px;
  line-height: 1.65;
  color: var(--mut);
  border-left: 4px solid var(--ink);
  padding-left: 12px;
  font-weight: 600;
}

.ctc-14__note code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .9em;
  background: oklch(0.88 0.03 95);
  padding: 1px 5px;
  border: 1.5px solid var(--ink);
}

@media (prefers-reduced-motion: reduce) {
  .ctc-14 * {
    transition-duration: .01ms !important;
  }

  .ctc-14__b--stick {
    rotate: 0deg;
  }
}
```
