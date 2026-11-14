---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/card-deck-fan-out-rotation/"
title: "Card Deck Fan Out Rotation"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "A stack of five cards that fans into an arc, each rotated by an index-derived angle about a pivot below the deck so they pivot like cards held in a hand."
has_js: "true"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Card Deck Fan Out Rotation
Source: https://codefronts.com/motion/css-rotate-animation/card-deck-fan-out-rotation/

A stack of five cards that fans into an arc, each rotated by an index-derived angle about a pivot below the deck so they pivot like cards held in a hand. The formula centres the fan for any count: angle = (index - (count - 1) / 2) x step. Twenty lines of JavaScript hold the open state, because hover alone would exclude every touch device.
## HTML
```html
<section class="rot-17" aria-labelledby="rot-17-h">
  <fieldset class="rot-17__theme">
    <legend class="rot-17__themelegend">Theme</legend>
    <input class="rot-17__themeinput" type="radio" name="rot-17-theme" id="rot-17-theme-auto" checked>
    <label class="rot-17__themeopt" for="rot-17-theme-auto">Auto</label>
    <input class="rot-17__themeinput" type="radio" name="rot-17-theme" id="rot-17-theme-light">
    <label class="rot-17__themeopt" for="rot-17-theme-light">Light</label>
    <input class="rot-17__themeinput" type="radio" name="rot-17-theme" id="rot-17-theme-dark">
    <label class="rot-17__themeopt" for="rot-17-theme-dark">Dark</label>
  </fieldset>

  <div class="rot-17__stage">
    <header class="rot-17__head">
      <p class="rot-17__eyebrow">Talon Club · Table four</p>
      <h2 class="rot-17__h" id="rot-17-h">A fan that stays centred at any count</h2>
      <p class="rot-17__sub">Each card rotates by its index minus half the count, times the step. The pivot sits below the deck, where a hand would be.</p>
    </header>

    <div class="rot-17__table">
      <div class="rot-17__deck" id="rot-17-deck" data-fan="closed" style="--count: 5">
        <article class="rot-17__card" style="--n: 0">
          <span class="rot-17__pip rot-17__pip--red">A</span>
          <span class="rot-17__suit rot-17__suit--red">&#9829;</span>
          <span class="rot-17__foot">Aperture</span>
        </article>
        <article class="rot-17__card" style="--n: 1">
          <span class="rot-17__pip">K</span>
          <span class="rot-17__suit">&#9824;</span>
          <span class="rot-17__foot">Basalt</span>
        </article>
        <article class="rot-17__card" style="--n: 2">
          <span class="rot-17__pip rot-17__pip--red">Q</span>
          <span class="rot-17__suit rot-17__suit--red">&#9830;</span>
          <span class="rot-17__foot">Meridian</span>
        </article>
        <article class="rot-17__card" style="--n: 3">
          <span class="rot-17__pip">J</span>
          <span class="rot-17__suit">&#9827;</span>
          <span class="rot-17__foot">Sable</span>
        </article>
        <article class="rot-17__card" style="--n: 4">
          <span class="rot-17__pip">10</span>
          <span class="rot-17__suit">&#9824;</span>
          <span class="rot-17__foot">Vale</span>
        </article>
      </div>
    </div>

    <div class="rot-17__controls">
      <button class="rot-17__btn" type="button" id="rot-17-toggle" aria-expanded="false" aria-controls="rot-17-deck">Fan the hand</button>
      <output class="rot-17__angles" id="rot-17-angles" aria-live="polite">Closed · all five cards at 0°</output>
    </div>

    <p class="rot-17__fine">Five cards at a 13 degree step give -26, -13, 0, 13 and 26. Add a sixth and the same formula redistributes all six without a single new value.</p>
  </div>
</section>
```
## CSS
```css
.rot-17 {
  --page: #0d2019;
  --felt: #14372a;
  --surface: #fbf8f1;
  --ink: #f1efe6;
  --card-ink: #1a1a1a;
  --muted: #9db3a6;
  --rule: #1f4a39;
  --gold: #d8b45c;
  --red: #b8262b;
  --step: 13deg;
  --pivot: 165%;
  --stagger: 40ms;
  --rise: -0.9rem;
  --cardw: clamp(4.5rem, 17vw, 6.25rem);
  --font-display: Copperplate, "Copperplate Gothic Light", "Trajan Pro", Optima, serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: radial-gradient(120% 90% at 50% 10%, var(--felt) 0%, var(--page) 70%, #061009 100%);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(0 0 0)) {
  .rot-17 {
    --gold: oklch(0.79 0.11 88);
    --red: oklch(0.5 0.2 25);
  }
}

.rot-17 *,
.rot-17 *::before,
.rot-17 *::after {
  box-sizing: border-box;
}

.rot-17__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.5rem, 4vw, 2.5rem);
  padding: clamp(1.25rem, 4vw, 3rem);
  padding-block-start: 5.25rem;
}

.rot-17__head {
  max-inline-size: 36rem;
  min-inline-size: 0;
  text-align: center;
}

.rot-17__eyebrow {
  margin: 0 0 0.6rem;
  font-family: var(--font-display);
  font-size: 0.6875rem;
  letter-spacing: 0.26em;
  text-transform: uppercase;
  color: var(--gold);
}

.rot-17__h {
  margin: 0 0 0.6rem;
  font-family: var(--font-display);
  font-size: clamp(1.25rem, 4.4vw, 2rem);
  font-weight: 400;
  letter-spacing: 0.02em;
  line-height: 1.16;
}

.rot-17__sub {
  margin: 0;
  font-size: 0.9375rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-17__table {
  inline-size: min(100%, 34rem);
  display: grid;
  place-items: end center;
  block-size: clamp(13rem, 42vw, 17rem);
  padding-block-end: 1rem;
}

.rot-17__deck {
  position: relative;
  inline-size: var(--cardw);
  block-size: calc(var(--cardw) * 1.45);
}

.rot-17__card {
  position: absolute;
  inset: 0;
  display: grid;
  grid-template-rows: auto 1fr auto;
  padding: 0.5rem 0.55rem;
  border: 1px solid var(--gold);
  border-radius: 0.4rem;
  background: var(--surface);
  color: var(--card-ink);
  transform-origin: 50% var(--pivot);
  transform: rotate(0deg);
  transition: transform 420ms cubic-bezier(0.22, 0.8, 0.28, 1);
  transition-delay: calc(var(--n) * var(--stagger));
  box-shadow: 0 10px 20px -14px rgba(0, 0, 0, 0.85);
}

.rot-17__deck[data-fan="open"] .rot-17__card {
  transform: rotate(calc((var(--n) - (var(--count) - 1) / 2) * var(--step))) translateY(var(--rise));
}

.rot-17__pip {
  font-family: var(--font-display);
  font-size: 0.9375rem;
  letter-spacing: 0.04em;
}

.rot-17__pip--red,
.rot-17__suit--red {
  color: var(--red);
}

.rot-17__suit {
  align-self: center;
  justify-self: center;
  font-size: clamp(1.25rem, 5vw, 1.75rem);
  line-height: 1;
}

.rot-17__foot {
  font-size: 0.5625rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #6b6b6b;
}

.rot-17__controls {
  display: flex;
  align-items: center;
  gap: 0.875rem;
  flex-wrap: wrap;
  justify-content: center;
}

.rot-17__btn {
  min-block-size: 2.75rem;
  padding: 0 1.25rem;
  border: 1px solid var(--gold);
  border-radius: 999px;
  background: transparent;
  color: var(--ink);
  font-family: var(--font-display);
  font-size: 0.8125rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  cursor: pointer;
}

.rot-17__btn:hover {
  background: color-mix(in srgb, var(--gold) 20%, transparent);
}

.rot-17__btn:focus-visible {
  outline: 2px solid var(--gold);
  outline-offset: 3px;
}

.rot-17__angles {
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.75rem;
  color: var(--muted);
}

.rot-17__fine {
  inline-size: min(100%, 34rem);
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.65;
  text-align: center;
  color: var(--muted);
  text-wrap: pretty;
}

@media (hover: hover) and (pointer: fine) {
  .rot-17__deck:hover .rot-17__card {
    transform: rotate(calc((var(--n) - (var(--count) - 1) / 2) * var(--step))) translateY(var(--rise));
  }
}

@media (prefers-reduced-motion: reduce) {
  .rot-17__card {
    transition: none;
  }
}

.rot-17__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 9;
  display: flex;
  align-items: center;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 8%, transparent);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  font-family: system-ui, sans-serif;
}

.rot-17__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-17__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-17__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.6875rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: inherit;
  opacity: 0.55;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}

.rot-17__themeopt:hover {
  opacity: 0.85;
}

.rot-17__themeinput:checked + .rot-17__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-17__themeinput:focus-visible + .rot-17__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .rot-17__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-17__themeinput:checked + .rot-17__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: light) {
  .rot-17:not(:has(#rot-17-theme-dark:checked)) {
    --page: #e8ede4;
    --felt: #cfdcc9;
    --ink: #16261d;
    --muted: #55705f;
    --rule: #b9cbb2;
    --gold: #8a6a18;
    background: radial-gradient(120% 90% at 50% 10%, #dfe9da 0%, #e8ede4 70%, #d6e0d0 100%);
  }
}

@media (prefers-color-scheme: dark) {
  .rot-17:has(#rot-17-theme-light:checked) {
    --page: #e8ede4;
    --felt: #cfdcc9;
    --ink: #16261d;
    --muted: #55705f;
    --rule: #b9cbb2;
    --gold: #8a6a18;
    background: radial-gradient(120% 90% at 50% 10%, #dfe9da 0%, #e8ede4 70%, #d6e0d0 100%);
  }
}

[data-theme="light"] .rot-17:not(:has(#rot-17-theme-dark:checked)) {
  --page: #e8ede4;
  --felt: #cfdcc9;
  --ink: #16261d;
  --muted: #55705f;
  --rule: #b9cbb2;
  --gold: #8a6a18;
  background: radial-gradient(120% 90% at 50% 10%, #dfe9da 0%, #e8ede4 70%, #d6e0d0 100%);
}

.rot-17:has(#rot-17-theme-light:checked) {
  --page: #e8ede4;
  --felt: #cfdcc9;
  --ink: #16261d;
  --muted: #55705f;
  --rule: #b9cbb2;
  --gold: #8a6a18;
  background: radial-gradient(120% 90% at 50% 10%, #dfe9da 0%, #e8ede4 70%, #d6e0d0 100%);
}

.rot-17:has(#rot-17-theme-dark:checked) {
  --page: #0d2019;
  --felt: #14372a;
  --ink: #f1efe6;
  --muted: #9db3a6;
  --rule: #1f4a39;
  --gold: #d8b45c;
  background: radial-gradient(120% 90% at 50% 10%, #14372a 0%, #0d2019 70%, #061009 100%);
}
/* Site-theme bridge: the per-demo page stamps [data-theme] on the iframe
   root. Without these rules a dark-by-default demo followed the OS instead
   of the site when the visitor was on OS-light + site-dark. Guarded by the
   light toggle so the in-demo switch still wins. */

[data-theme="dark"] .rot-17:not(:has(#rot-17-theme-light:checked)) {
  --page: #0d2019;
  --felt: #14372a;
  --ink: #f1efe6;
  --muted: #9db3a6;
  --rule: #1f4a39;
  --gold: #d8b45c;
  background: radial-gradient(120% 90% at 50% 10%, #14372a 0%, #0d2019 70%, #061009 100%);
}
```

## JavaScript
```js
(() => {
  const deck = document.querySelector('.rot-17__deck');
  if (!deck || deck.dataset.rot17) return;
  deck.dataset.rot17 = '1';
  const btn = document.querySelector('.rot-17__btn');
  const out = document.querySelector('.rot-17__angles');
  const count = Number(getComputedStyle(deck).getPropertyValue('--count')) || 5;
  const step = 13;
  const angles = Array.from({ length: count }, (_, n) => ((n - (count - 1) / 2) * step).toFixed(0) + '°');
  const sync = () => {
    const open = deck.dataset.fan === 'open';
    btn.setAttribute('aria-expanded', String(open));
    btn.textContent = open ? 'Close the hand' : 'Fan the hand';
    out.textContent = open ? 'Open · ' + angles.join(' · ') : 'Closed · all ' + count + ' cards at 0°';
  };
  btn.addEventListener('click', () => {
    deck.dataset.fan = deck.dataset.fan === 'open' ? 'closed' : 'open';
    sync();
  });
  sync();
})();
```
