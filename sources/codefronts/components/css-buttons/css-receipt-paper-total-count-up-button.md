---
source: "codefronts"
url: "https://codefronts.com/components/css-buttons/css-receipt-paper-total-count-up-button/"
title: "CSS Receipt Paper Total Count-Up Button"
section: "components"
category: "css-buttons"
category_name: "CSS Buttons"
description: "A thermal receipt whose total counts up from zero when you press it — the number is animated by CSS, using a registered integer property fed into…"
has_js: "false"
---

Here's a working CSS Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Receipt Paper Total Count-Up Button
Source: https://codefronts.com/components/css-buttons/css-receipt-paper-total-count-up-button/

A thermal receipt whose total counts up from zero when you press it — the number is animated by CSS, using a registered integer property fed into counter-reset and printed through content. Zigzag torn bottom edge, faded thermal ink, monospaced columns.
## HTML
```html
<div class="cb-49">
  <div class="cb-49__stage">
    <label class="cb-49__btn">
      <input type="checkbox" aria-label="Total the order">
      <span class="cb-49__head">Corner Roastery</span>
      <span class="cb-49__row"><span>Filter, 12oz</span><span>18.00</span></span>
      <span class="cb-49__row"><span>Beans, 250g</span><span>22.60</span></span>
      <span class="cb-49__row"><span>Service</span><span>8.00</span></span>
      <span class="cb-49__rule" aria-hidden="true"></span>
      <span class="cb-49__totalRow">
        <span class="cb-49__totalLabel">Total</span>
        <span class="cb-49__totalVal">
          <span class="cb-49__total" aria-hidden="true"></span>
          <span class="cb-49__fallback">$48.60</span>
        </span>
      </span>
      <span class="cb-49__foot">Tap to tally · thank you</span>
    </label>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&display=swap');

@property --cb-49-n {
  syntax: '<integer>';
  inherits: false;
  initial-value: 0;
}

.cb-49 {
  --bg: #26262a;
  --paper: #f7f4ec;
  --paper-lo: #e7e2d5;
  --ink: #2c2a26;
  --muted: #7c776c;
  --accent: #1f6f5c;
  --mono: "Courier Prime",ui-monospace,"Courier New",Courier,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: radial-gradient(30rem 20rem at 50% 34%, rgba(255,255,255,.05), transparent 72%), var(--bg);
  font-family: var(--mono);
}

@supports (color: oklch(50% 0 0)) {
  .cb-49 {
    --paper: oklch(97% .012 90);
    --paper-lo: oklch(91% .014 88);
    --accent: oklch(48% .1 168);
  }
}

@media (prefers-color-scheme: light) {
  .cb-49:not([data-theme="dark"]) {
    --bg: #313136;
  }
}

.cb-49[data-theme="light"] {
  --bg: #313136;
}

.cb-49,
.cb-49 *,
.cb-49 *::before,
.cb-49 *::after {
  box-sizing: border-box;
}

.cb-49__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,6vw,4rem);
}

.cb-49__btn {
  position: relative;
  cursor: pointer;
  display: grid;
  gap: .4rem;
  width: min(100%,17rem);
  padding: 1.2rem 1.15rem 1.6rem;
  color: var(--ink);
  font-size: .8125rem;
  line-height: 1.5;
  font-variant-numeric: tabular-nums;
  background-color: var(--paper);
  background-image: radial-gradient(.05rem .05rem at 30% 40%, rgba(90,84,70,.14) 99%, transparent), linear-gradient(180deg, var(--paper), var(--paper-lo));
  background-size: 5px 5px, 100% 100%;
  -webkit-mask: conic-gradient(from 135deg at 50% 0, #000 90deg, transparent 0) 0 100%/.76rem .4rem repeat-x, linear-gradient(#000,#000) 0 0/100% calc(100% - .38rem) no-repeat;
  mask: conic-gradient(from 135deg at 50% 0, #000 90deg, transparent 0) 0 100%/.76rem .4rem repeat-x, linear-gradient(#000,#000) 0 0/100% calc(100% - .38rem) no-repeat;
  filter: drop-shadow(0 12px 18px rgba(0,0,0,.5));
  transition: translate .3s cubic-bezier(.16,1,.3,1), filter .3s ease;
  -webkit-tap-highlight-color: transparent;
}

.cb-49__btn input {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  clip-path: inset(50%);
}

.cb-49__head {
  text-align: center;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  font-size: .75rem;
}

.cb-49__row {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  color: var(--muted);
}

.cb-49__rule {
  display: block;
  height: 0;
  border-top: 1px dashed color-mix(in oklab,var(--ink) 35%,transparent);
  margin: .35rem 0;
}

.cb-49__totalRow {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 1rem;
}

.cb-49__totalLabel {
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  font-size: .75rem;
}

.cb-49__totalVal {
  position: relative;
  font-size: 1.5rem;
  font-weight: 700;
  letter-spacing: -.02em;
  color: var(--accent);
}

.cb-49__total {
  display: none;
}

.cb-49__fallback {
  display: inline;
}

@supports (counter-reset: x var(--cb-49-n)) {
  .cb-49__total {
    display: inline;
    counter-reset: cb-49-a calc(var(--cb-49-n) / 100) cb-49-b calc(var(--cb-49-n) - (var(--cb-49-n) / 100) * 100);
  }

  .cb-49__total::after {
    content: "$" counter(cb-49-a) "." counter(cb-49-b, decimal-leading-zero);
  }

  .cb-49__fallback {
    display: none;
  }
}

.cb-49__foot {
  text-align: center;
  font-size: .6875rem;
  color: var(--muted);
  letter-spacing: .06em;
}

.cb-49__btn:has(input:checked) .cb-49__total {
  animation: cb-49-count 1.5s cubic-bezier(.2,.9,.2,1) forwards;
}

@keyframes cb-49-count {
  from {
    --cb-49-n: 0;
  }

  to {
    --cb-49-n: 4860;
  }
}

.cb-49__btn:has(input:checked) .cb-49__rule {
  border-top-style: solid;
}

.cb-49__btn:is(:hover,:has(input:focus-visible)) {
  translate: 0 -2px;
  filter: drop-shadow(0 18px 24px rgba(0,0,0,.55));
}

.cb-49__btn:has(input:focus-visible) {
  outline: 2px solid var(--accent);
  outline-offset: 4px;
}

.cb-49__btn:active {
  translate: 0 1px;
}

@media (prefers-reduced-motion: reduce) {
  .cb-49__btn {
    transition: none;
  }

  .cb-49__btn:has(input:checked) .cb-49__total {
    animation: none;
    --cb-49-n: 4860;
  }
}

@media (forced-colors: active) {
  .cb-49__btn {
    background: Canvas;
    color: CanvasText;
    border: 1px solid CanvasText;
    mask: none;
    -webkit-mask: none;
    filter: none;
  }

  .cb-49__totalVal {
    color: CanvasText;
  }
}
```
