---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-3d/backface-visibility-and-two-sided-elements/"
title: "Backface Visibility and Two Sided Elements"
section: "design-styles"
category: "css-3d"
category_name: "CSS 3D Effects"
description: "Every transformed element has a back, and by default you look straight through to a mirrored copy of its front."
has_js: "false"
---

Here's a working CSS 3D Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Backface Visibility and Two Sided Elements
Source: https://codefronts.com/design-styles/css-3d/backface-visibility-and-two-sided-elements/

Every transformed element has a back, and by default you look straight through to a mirrored copy of its front. backface-visibility: hidden stops that, which is what lets two elements stacked back to back behave as one two-sided object. Both states rotate side by side so the mirrored-text artefact is visible rather than described.
## HTML
```html
<section class="d3-05" aria-labelledby="d3-05-title">
  <h2 class="d3-05__sr" id="d3-05-title">Backface visibility compared</h2>

  <div class="d3-05__theme">
    <input class="d3-05__theme-input" type="checkbox" id="d3-05-theme">
    <label class="d3-05__theme-label" for="d3-05-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="d3-05__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="d3-05__stage">
    <div class="d3-05__viewport">
      <header class="d3-05__head">
        <span class="d3-05__kicker">Vantage Club &mdash; card artwork QA</span>
        <strong>What the back of a rotated card actually shows</strong>
      </header>

      <div class="d3-05__rows">
        <section class="d3-05__row">
          <p class="d3-05__cap"><b class="d3-05__badge d3-05__badge--no">Default</b> one panel, <code>backface-visibility: visible</code></p>
          <div class="d3-05__scene">
            <div class="d3-05__spin d3-05__spin--bad">
              <article class="d3-05__card">
                <span class="d3-05__brand">VANTAGE</span>
                <span class="d3-05__chip" aria-hidden="true"></span>
                <span class="d3-05__num">4821 &nbsp;0093 &nbsp;7712</span>
                <span class="d3-05__owner">A. NAKAMURA<em>Member since 2019</em></span>
              </article>
            </div>
          </div>
          <p class="d3-05__verdict d3-05__verdict--no">Past 90&deg; you read the front through the card &mdash; mirrored.</p>
        </section>

        <section class="d3-05__row">
          <p class="d3-05__cap"><b class="d3-05__badge d3-05__badge--ok">Fixed</b> two panels, <code>backface-visibility: hidden</code></p>
          <div class="d3-05__scene">
            <div class="d3-05__spin d3-05__spin--good">
              <article class="d3-05__card d3-05__card--hide">
                <span class="d3-05__brand">VANTAGE</span>
                <span class="d3-05__chip" aria-hidden="true"></span>
                <span class="d3-05__num">4821 &nbsp;0093 &nbsp;7712</span>
                <span class="d3-05__owner">A. NAKAMURA<em>Member since 2019</em></span>
              </article>
              <article class="d3-05__card d3-05__card--hide d3-05__card--rear">
                <span class="d3-05__stripe" aria-hidden="true"></span>
                <span class="d3-05__sig">Authorised signature</span>
                <span class="d3-05__cvv">CVV 042</span>
              </article>
            </div>
          </div>
          <p class="d3-05__verdict d3-05__verdict--ok">The back is its own artwork, pre-rotated 180&deg;.</p>
        </section>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.d3-05 {
  --d3-05-bg: #0c0d10;
  --d3-05-surf: #16181d;
  --d3-05-line: #2b3037;
  --d3-05-ink: #f0f2f4;
  --d3-05-mut: #949aa4;
  --d3-05-acc: #2fd4d0;
  --d3-05-acc: oklch(80% 0.12 190);
  --d3-05-acc2: #7c5cff;
  --d3-05-acc2: oklch(62% 0.2 288);
  --d3-05-no: #ff6b5e;
  --d3-05-no: oklch(70% 0.18 28);
  --d3-05-turn: 8s;
  --d3-05-font-display: "Oswald", "Barlow Condensed", "Arial Narrow", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: radial-gradient(58rem 28rem at 80% -10%, color-mix(in oklab, var(--d3-05-acc2) 22%, transparent), transparent 62%), radial-gradient(46rem 24rem at 0% 100%, color-mix(in oklab, var(--d3-05-acc) 16%, transparent), transparent 60%), var(--d3-05-bg);
  color: var(--d3-05-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.d3-05 *,
.d3-05 *::before,
.d3-05 *::after {
  box-sizing: border-box;
}

.d3-05__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.d3-05:has(.d3-05__theme-input:checked) {
  --d3-05-bg: #eef0f3;
  --d3-05-surf: #ffffff;
  --d3-05-line: #d5d9e0;
  --d3-05-ink: #101317;
  --d3-05-mut: #5c646f;
  --d3-05-acc: #05807c;
  --d3-05-acc: oklch(52% 0.1 190);
  --d3-05-acc2: #4a2ad4;
  --d3-05-acc2: oklch(45% 0.21 288);
  --d3-05-no: #c0261a;
  --d3-05-no: oklch(52% 0.19 28);
}

@media (prefers-color-scheme: light) {
  .d3-05:has(.d3-05__theme-input:checked) {
    --d3-05-bg: #eef0f3;
    --d3-05-surf: #ffffff;
    --d3-05-line: #d5d9e0;
    --d3-05-ink: #101317;
    --d3-05-mut: #5c646f;
    --d3-05-acc: #05807c;
    --d3-05-acc: oklch(52% 0.1 190);
    --d3-05-acc2: #4a2ad4;
    --d3-05-acc2: oklch(45% 0.21 288);
    --d3-05-no: #c0261a;
    --d3-05-no: oklch(52% 0.19 28);
  }
}

@media (prefers-color-scheme: dark) {
  .d3-05:has(.d3-05__theme-input:checked) {
    --d3-05-bg: #eef0f3;
    --d3-05-surf: #ffffff;
    --d3-05-line: #d5d9e0;
    --d3-05-ink: #101317;
    --d3-05-mut: #5c646f;
    --d3-05-acc: #05807c;
    --d3-05-acc: oklch(52% 0.1 190);
    --d3-05-acc2: #4a2ad4;
    --d3-05-acc2: oklch(45% 0.21 288);
    --d3-05-no: #c0261a;
    --d3-05-no: oklch(52% 0.19 28);
  }
}

.d3-05__theme {
  position: absolute;
  inset-block-start: clamp(0.75rem, 3vw, 1.5rem);
  inset-inline-end: clamp(0.75rem, 3vw, 1.5rem);
  z-index: 20;
}

.d3-05__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.d3-05__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--d3-05-line);
  border-radius: 12px;
  background: var(--d3-05-surf);
  color: var(--d3-05-ink);
  cursor: pointer;
}

.d3-05__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.d3-05__theme-input:focus-visible + .d3-05__theme-label {
  outline: 2px solid var(--d3-05-acc);
  outline-offset: 3px;
}

.d3-05__stage {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(3.5rem, 9vw, 5rem) clamp(0.75rem, 4vw, 2.5rem);
}

.d3-05__viewport {
  inline-size: 100%;
  max-inline-size: 60rem;
  overflow: hidden;
  display: grid;
  gap: clamp(1.1rem, 3.5vw, 1.8rem);
  padding: clamp(1rem, 3.5vw, 2rem);
  border: 1px solid var(--d3-05-line);
  border-radius: 24px;
  background: color-mix(in oklab, var(--d3-05-surf) 78%, transparent);
  box-shadow: 0 40px 90px -50px #000;
}

.d3-05__head {
  display: grid;
  gap: 0.2rem;
}

.d3-05__kicker {
  font: 700 0.66rem/1.4 ui-monospace, Menlo, monospace;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--d3-05-acc);
}

.d3-05__head strong {
  font: 600 clamp(1.2rem, 4vw, 1.9rem)/1.1 var(--d3-05-font-display);
  letter-spacing: 0.005em;
}

.d3-05__rows {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  gap: clamp(1rem, 3vw, 1.75rem);
}

.d3-05__row {
  display: grid;
  gap: 0.7rem;
}

.d3-05__cap {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.4rem;
  font: 500 clamp(0.72rem, 2vw, 0.82rem)/1.3 system-ui, sans-serif;
  color: var(--d3-05-mut);
}

.d3-05__cap code {
  font: 600 0.95em/1 ui-monospace, Menlo, monospace;
  color: var(--d3-05-ink);
}

.d3-05__badge {
  padding: 0.18rem 0.5rem;
  border-radius: 999px;
  font: 800 0.62rem/1.5 ui-monospace, Menlo, monospace;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #fff;
}

.d3-05__badge--ok {
  background: var(--d3-05-acc);
  color: #04201f;
}

.d3-05__badge--no {
  background: var(--d3-05-no);
}

.d3-05__scene {
  perspective: 1000px;
  perspective-origin: 50% 45%;
  block-size: clamp(11rem, 30vw, 13.5rem);
  display: grid;
  place-items: center;
}

.d3-05__spin {
  position: relative;
  inline-size: min(100%, 20rem);
  aspect-ratio: 1.586;
  transform-style: preserve-3d;
}

.d3-05__spin--bad {
  animation: d3-05-turn var(--d3-05-turn) linear infinite;
}

.d3-05__spin--good {
  animation: d3-05-turn var(--d3-05-turn) linear infinite;
}

@keyframes d3-05-turn {
  from {
    transform: rotateY(0deg);
  }

  to {
    transform: rotateY(360deg);
  }
}

.d3-05__card {
  position: absolute;
  inset: 0;
  padding: clamp(0.85rem, 3vw, 1.2rem);
  display: grid;
  align-content: space-between;
  border-radius: 16px;
  background: linear-gradient(140deg, #1d2330 0%, #101722 45%, #0b1a22 100%);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 26px 50px -24px #000, inset 0 1px 0 rgba(255, 255, 255, 0.12);
  overflow: hidden;
  color: #eef4f6;
}

.d3-05__card::before {
  content: "";
  position: absolute;
  inset-block-start: -40%;
  inset-inline-end: -20%;
  inline-size: 70%;
  block-size: 160%;
  background: linear-gradient(120deg, transparent, color-mix(in oklab, var(--d3-05-acc) 55%, transparent), color-mix(in oklab, var(--d3-05-acc2) 55%, transparent), transparent);
  transform: rotate(18deg);
  opacity: 0.45;
}

.d3-05__card--hide {
  backface-visibility: hidden;
}

.d3-05__card--rear {
  transform: rotateY(180deg);
  background: linear-gradient(140deg, #0e141d, #161c26);
  align-content: start;
  gap: 0.55rem;
}

.d3-05__brand {
  position: relative;
  font: 700 clamp(0.85rem, 2.6vw, 1.05rem)/1 var(--d3-05-font-display);
  letter-spacing: 0.32em;
}

.d3-05__chip {
  position: relative;
  inline-size: 2.6rem;
  block-size: 1.9rem;
  border-radius: 6px;
  background: linear-gradient(150deg, #f5d68a, #b98d3a);
  box-shadow: inset 0 0 0 1px rgba(0, 0, 0, 0.25);
}

.d3-05__num {
  position: relative;
  font: 500 clamp(0.85rem, 2.8vw, 1.05rem)/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.06em;
}

.d3-05__owner {
  position: relative;
  display: grid;
  gap: 0.1rem;
  font: 600 0.7rem/1.2 ui-monospace, Menlo, monospace;
  letter-spacing: 0.12em;
}

.d3-05__owner em {
  font: 400 0.62rem/1.2 ui-monospace, Menlo, monospace;
  font-style: normal;
  letter-spacing: 0.06em;
  color: rgba(238, 244, 246, 0.6);
}

.d3-05__stripe {
  display: block;
  block-size: 2.6rem;
  margin: 0.2rem -1.2rem 0;
  background: #05070a;
}

.d3-05__sig {
  display: block;
  padding: 0.45rem 0.6rem;
  border-radius: 4px;
  background: rgba(255, 255, 255, 0.88);
  color: #0b0f14;
  font: 500 0.66rem/1 ui-monospace, Menlo, monospace;
}

.d3-05__cvv {
  font: 600 0.68rem/1 ui-monospace, Menlo, monospace;
  letter-spacing: 0.14em;
  color: rgba(238, 244, 246, 0.75);
}

.d3-05__verdict {
  margin: 0;
  font: 500 clamp(0.7rem, 1.9vw, 0.8rem)/1.4 system-ui, sans-serif;
}

.d3-05__verdict--no {
  color: var(--d3-05-no);
}

.d3-05__verdict--ok {
  color: var(--d3-05-acc);
}

@media (prefers-reduced-motion: reduce) {
  .d3-05__spin--bad {
    animation: none;
    transform: rotateY(205deg);
  }

  .d3-05__spin--good {
    animation: none;
    transform: rotateY(205deg);
  }
}
```
