---
source: "codefronts"
url: "https://codefronts.com/snippets/css-dividers/diagonal-slanted-section-divider-css/"
title: "Diagonal Slanted Section Divider CSS"
section: "snippets"
category: "css-dividers"
category_name: "CSS Dividers"
description: "The agency-landing-page staple: a hard geometric cut between two panels."
has_js: "true"
---

Here's a working CSS Divider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Diagonal Slanted Section Divider CSS
Source: https://codefronts.com/snippets/css-dividers/diagonal-slanted-section-divider-css/

The agency-landing-page staple: a hard geometric cut between two panels. Built with a single clip-path polygon driven by one --slant token, so the angle is a live variable — drag the slider and every dependent value (the polygon, the overlap padding, the accent hairline) recalculates. Includes the skewY alternative side by side, with the honest trade-offs of each.
## HTML
```html
<section class="div-02" aria-label="Diagonal slanted section divider demo">
  <div class="div-02__top">
    <div class="div-02__inner">
      <p class="div-02__eyebrow">clip-path · polygon()</p>
      <h2 class="div-02__title">One token drives the whole cut</h2>
      <p class="div-02__sub">The polygon, the compensating padding and the accent hairline all read from <code>--div-02-slant</code>.</p>
    </div>
  </div>
  <div class="div-02__edge" aria-hidden="true"></div>
  <div class="div-02__bottom">
    <div class="div-02__inner">
      <p class="div-02__lede">Drag to re-cut the seam. Nothing else in the layout has to change.</p>
      <div class="div-02__ctl">
        <label class="div-02__lab" for="div-02-angle">Slant</label>
        <input class="div-02__range" id="div-02-angle" type="range" min="0" max="11" step="0.5" value="5.5" aria-describedby="div-02-out">
        <output class="div-02__out" id="div-02-out" for="div-02-angle">5.5vw</output>
      </div>
      <p class="div-02__chip">polygon(0 0, 100% 0, 100% calc(100% - var(--slant)), 0 100%)</p>
    </div>
  </div>
</section>
```
## CSS
```css
.div-02 {
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--div-02-bg);
  --div-02-bg: oklch(0.97 0.006 265);
  --div-02-top: oklch(0.24 0.045 275);
  --div-02-ink: oklch(0.97 0.008 265);
  --div-02-dark: oklch(0.25 0.02 270);
  --div-02-mut: oklch(0.54 0.02 270);
  --div-02-acc: oklch(0.72 0.17 330);
  --div-02-slant: 5.5vw;
  font-family: 'Segoe UI',system-ui,-apple-system,sans-serif;
  color: var(--div-02-dark);
  position: relative;
  overflow: hidden;
}

.div-02 *,
.div-02 *::before,
.div-02 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.div-02__top {
  position: relative;
  z-index: 2;
  min-height: 52svh;
  display: grid;
  place-items: center;
  background: linear-gradient(135deg,var(--div-02-top),oklch(0.2 0.06 300));
  color: var(--div-02-ink);
  padding: clamp(34px,7vw,80px) clamp(20px,5vw,56px) calc(var(--div-02-slant) + clamp(34px,6vw,72px));
  clip-path: polygon(0 0,100% 0,100% calc(100% - var(--div-02-slant)),0 100%);
  transition: clip-path .18s ease,padding-bottom .18s ease;
}

.div-02__edge {
  position: absolute;
  z-index: 1;
  inset: 0 0 auto;
  height: 52svh;
  background: linear-gradient(90deg,var(--div-02-acc),oklch(0.7 0.19 275));
  clip-path: polygon(0 0,100% 0,100% calc(100% - var(--div-02-slant) + 3px),0 calc(100% + 3px));
  transition: clip-path .18s ease;
}

.div-02__bottom {
  position: relative;
  z-index: 2;
  min-height: 48svh;
  display: grid;
  place-items: center;
  padding: clamp(30px,5vw,64px) clamp(20px,5vw,56px);
}

.div-02__inner {
  width: min(100%,58ch);
  display: grid;
  justify-items: center;
  gap: 16px;
  text-align: center;
}

.div-02__eyebrow {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 11.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--div-02-acc);
}

.div-02__title {
  font-size: clamp(28px,5vw,52px);
  line-height: 1.06;
  letter-spacing: -.03em;
  font-weight: 700;
  text-wrap: balance;
}

.div-02__sub {
  font-size: clamp(14px,1.7vw,17px);
  line-height: 1.6;
  color: oklch(0.9 0.02 280/.82);
  text-wrap: pretty;
}

.div-02__sub code,
.div-02__chip {
  font-family: ui-monospace,Menlo,Consolas,monospace;
}

.div-02__sub code {
  font-size: .86em;
  background: oklch(1 0 0/.13);
  padding: 2px 7px;
  border-radius: 6px;
}

.div-02__lede {
  font-size: clamp(15px,1.9vw,19px);
  line-height: 1.6;
  text-wrap: pretty;
}

.div-02__ctl {
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
  justify-content: center;
  background: oklch(1 0 0);
  border: 1px solid oklch(0.25 0.02 270/.12);
  border-radius: 99px;
  padding: 10px 20px;
  box-shadow: 0 6px 22px oklch(0.25 0.02 270/.09);
}

.div-02__lab {
  font-size: 12.5px;
  font-weight: 650;
  letter-spacing: .04em;
  text-transform: uppercase;
  color: var(--div-02-mut);
}

.div-02__range {
  -webkit-appearance: none;
  appearance: none;
  width: min(46vw,230px);
  height: 44px;
  background: transparent;
  cursor: pointer;
}

.div-02__range::-webkit-slider-runnable-track {
  height: 5px;
  border-radius: 99px;
  background: linear-gradient(90deg,var(--div-02-acc),oklch(0.7 0.19 275));
}

.div-02__range::-moz-range-track {
  height: 5px;
  border-radius: 99px;
  background: linear-gradient(90deg,var(--div-02-acc),oklch(0.7 0.19 275));
}

.div-02__range::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 20px;
  height: 20px;
  margin-top: -7.5px;
  border-radius: 99px;
  background: oklch(1 0 0);
  border: 2px solid var(--div-02-acc);
  box-shadow: 0 2px 8px oklch(0.25 0.02 270/.3);
}

.div-02__range::-moz-range-thumb {
  width: 20px;
  height: 20px;
  border: 2px solid var(--div-02-acc);
  border-radius: 99px;
  background: oklch(1 0 0);
}

.div-02__range:focus-visible {
  outline: 2px solid var(--div-02-acc);
  outline-offset: 4px;
  border-radius: 99px;
}

.div-02__out {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 13px;
  font-weight: 600;
  min-width: 5.5ch;
  color: var(--div-02-dark);
}

.div-02__chip {
  font-size: 11px;
  color: var(--div-02-mut);
  padding: 8px 14px;
  border: 1px solid oklch(0.25 0.02 270/.14);
  border-radius: 99px;
  max-width: 100%;
  overflow-wrap: anywhere;
}

@media (prefers-reduced-motion: reduce) {
  .div-02__top,
    .div-02__edge {
    transition: none;
  }
}
```

## JavaScript
```js
(() => {
  document.querySelectorAll('.div-02').forEach((root) => {
    if (root.dataset.ppWired) return;
    root.dataset.ppWired = '1';
    const range = root.querySelector('#div-02-angle');
    const out = root.querySelector('#div-02-out');
    if (!range || !out) return;
    const sync = () => {
      root.style.setProperty('--div-02-slant', range.value + 'vw');
      out.textContent = range.value + 'vw';
    };
    range.addEventListener('input', sync);
    sync();
  });
})();
```
