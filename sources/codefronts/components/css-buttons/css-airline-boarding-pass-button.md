---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-airline-boarding-pass-button/"
title: "CSS Airline Boarding Pass Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A boarding pass with a genuinely perforated seam: a mask punches half-circles down the divide, the stub tears away and rotates on hover, and a barcode is…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Airline Boarding Pass Button
Source: https://codefronts.com/components/css-buttons/css-airline-boarding-pass-button/

A boarding pass with a genuinely perforated seam: a mask punches half-circles down the divide, the stub tears away and rotates on hover, and a barcode is drawn with one repeating gradient. Flight numbers use tabular-nums so nothing shifts as they change.
## HTML
```html
<div class="cb-41">
  <div class="cb-41__stage">
    <button class="cb-41__btn" type="button">
      <span class="cb-41__body">
        <span class="cb-41__band">
          <span class="cb-41__brand">Meridian Air</span>
          <span class="cb-41__seat">14A · Zone 2</span>
        </span>
        <span class="cb-41__route">
          <span class="cb-41__code">LHR</span>
          <svg class="cb-41__plane" viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M2 13.5 22 9l-1 3.2-6.6 2.2-2.2 5.1-2.1.6 1-5-6.6 2.2L2 13.5z"/></svg>
          <span class="cb-41__code">JFK</span>
        </span>
        <span class="cb-41__meta">
          <span>Boards <b>18:40</b></span>
          <span>Gate <b>B22</b></span>
          <span>Flt <b>MA 214</b></span>
        </span>
      </span>
      <span class="cb-41__stub">
        <span class="cb-41__stubTop">Tap to check in</span>
        <span class="cb-41__bars" aria-hidden="true"></span>
        <span class="cb-41__stubSeat">14A</span>
      </span>
    </button>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&display=swap');

.cb-41 {
  --bg: #0e1b24;
  --card: #fbfbf8;
  --card-lo: #eceae2;
  --ink: #131a20;
  --muted: #6b7480;
  --brand: #0f5f7a;
  --sans: "Archivo",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(38rem 24rem at 50% 30%, #16303e, transparent 72%), var(--bg);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(50% 0 0)) {
  .cb-41 {
    --brand: oklch(45% .09 217);
    --card: oklch(98.5% .004 90);
  }
}

@media (prefers-color-scheme: light) {
  .cb-41:not([data-theme="dark"]) {
    --bg: #123040;
  }
}

.cb-41[data-theme="light"] {
  --bg: #123040;
}

.cb-41,
.cb-41 *,
.cb-41 *::before,
.cb-41 *::after {
  box-sizing: border-box;
}

.cb-41__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-41__btn {
  position: relative;
  cursor: pointer;
  border: 0;
  padding: 0;
  background: transparent;
  display: grid;
  grid-template-columns: 1fr auto;
  align-items: stretch;
  width: min(100%,30rem);
  text-align: left;
  font: inherit;
  color: var(--ink);
  filter: drop-shadow(0 18px 26px rgba(0,0,0,.55));
  transition: translate .35s cubic-bezier(.16,1,.3,1), filter .35s ease;
  -webkit-tap-highlight-color: transparent;
}

.cb-41__body,
.cb-41__stub {
  background: linear-gradient(170deg, var(--card), var(--card-lo));
}

.cb-41__body {
  display: grid;
  gap: .8rem;
  padding: 1rem 1.15rem 1.1rem;
  border-radius: .6rem 0 0 .6rem;
  border-right: 1px dashed color-mix(in oklab,var(--ink) 28%,transparent);
}

.cb-41__band {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: .75rem;
}

.cb-41__brand {
  font-size: .75rem;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--brand);
}

.cb-41__seat {
  font-size: .6875rem;
  font-weight: 600;
  letter-spacing: .06em;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.cb-41__route {
  display: flex;
  align-items: center;
  gap: .75rem;
}

.cb-41__code {
  font-size: 1.75rem;
  font-weight: 800;
  letter-spacing: -.02em;
  line-height: 1;
}

.cb-41__plane {
  width: 1.3rem;
  height: 1.3rem;
  color: var(--brand);
  transition: translate .5s cubic-bezier(.16,1,.3,1);
}

.cb-41__meta {
  display: flex;
  flex-wrap: wrap;
  gap: .35rem 1.1rem;
  font-size: .75rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.cb-41__meta b {
  color: var(--ink);
  font-weight: 700;
}

.cb-41__stub {
  display: grid;
  gap: .55rem;
  justify-items: center;
  align-content: center;
  padding: 1rem .85rem;
  border-radius: 0 .6rem .6rem 0;
  transform-origin: 0% 50%;
  transition: rotate .45s cubic-bezier(.16,1,.3,1), translate .45s cubic-bezier(.16,1,.3,1);
}

.cb-41__stubTop {
  font-size: .625rem;
  font-weight: 800;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--brand);
  text-align: center;
}

.cb-41__bars {
  display: block;
  width: 4.5rem;
  height: 2.6rem;
  background: repeating-linear-gradient(90deg,
      var(--ink) 0 2px, transparent 2px 4px, var(--ink) 4px 5px, transparent 5px 8px,
      var(--ink) 8px 11px, transparent 11px 12px, var(--ink) 12px 13px, transparent 13px 16px);
}

.cb-41__stubSeat {
  font-size: .9375rem;
  font-weight: 800;
  letter-spacing: .04em;
  font-variant-numeric: tabular-nums;
}
/* Each piece carries its OWN half of the perforation, on its own edge. Masking the
   whole button instead would leave the dot column behind in the button's coordinate
   space — so once the stub rotates, the holes stop following it and start slicing
   its corners. */

@supports ((mask-composite: exclude) or (-webkit-mask-composite: xor)) {
  .cb-41__body {
    -webkit-mask: radial-gradient(.3rem .3rem at 100% 50%, #000 96%, transparent 0) 100% -.475rem/.6rem .95rem repeat-y, linear-gradient(#000,#000);
    mask: radial-gradient(.3rem .3rem at 100% 50%, #000 96%, transparent 0) 100% -.475rem/.6rem .95rem repeat-y, linear-gradient(#000,#000);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    border-right: 0;
  }

  .cb-41__stub {
    -webkit-mask: radial-gradient(.3rem .3rem at 0 50%, #000 96%, transparent 0) 0 -.475rem/.6rem .95rem repeat-y, linear-gradient(#000,#000);
    mask: radial-gradient(.3rem .3rem at 0 50%, #000 96%, transparent 0) 0 -.475rem/.6rem .95rem repeat-y, linear-gradient(#000,#000);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
  }
}

.cb-41__btn:is(:hover,:focus-visible) {
  translate: 0 -3px;
  filter: drop-shadow(0 26px 34px rgba(0,0,0,.6));
}

.cb-41__btn:is(:hover,:focus-visible) .cb-41__stub {
  rotate: 3.5deg;
  translate: .4rem 0;
}

.cb-41__btn:is(:hover,:focus-visible) .cb-41__plane {
  translate: .3rem 0;
}

.cb-41__btn:focus-visible {
  outline: 2px solid var(--brand);
  outline-offset: 5px;
}

.cb-41__btn:active {
  translate: 0 1px;
}

.cb-41__btn:disabled {
  cursor: not-allowed;
  filter: grayscale(.6);
}

@media (prefers-reduced-motion: reduce) {
  .cb-41__btn,
    .cb-41__stub,
    .cb-41__plane {
    transition: none;
  }
}

@media (forced-colors: active) {
  .cb-41__btn {
    mask: none;
    -webkit-mask: none;
    filter: none;
  }

  .cb-41__body,
    .cb-41__stub {
    background: ButtonFace;
    border: 1px solid ButtonText;
    color: ButtonText;
  }

  .cb-41__bars {
    background: ButtonText;
  }
}
```
