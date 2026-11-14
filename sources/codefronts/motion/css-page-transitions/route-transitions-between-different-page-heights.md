---
source: "codefronts"
url: "https://codefronts.com/motion/css-page-transitions/route-transitions-between-different-page-heights/"
title: "Route Transitions Between Different Page Heights"
section: "motion"
category: "css-page-transitions"
category_name: "CSS Page Transitions"
description: "The most common visible bug in a hand-rolled transition: a short route becoming a tall one moves the scrollbar and the footer mid-animation."
has_js: "false"
---

Here's a working CSS Page Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Route Transitions Between Different Page Heights
Source: https://codefronts.com/motion/css-page-transitions/route-transitions-between-different-page-heights/

The most common visible bug in a hand-rolled transition: a short route becoming a tall one moves the scrollbar and the footer mid-animation. The broken version is shown first so the symptom is recognisable, then three fixes side by side &mdash; lock the container height for the duration, animate the height as part of the transition, or take both routes out of flow so document height never changes at all.
## HTML
```html
<section class="pt-04" aria-labelledby="pt-04-h">
  <div class="pt-04__theme">
    <input class="pt-04__theme-input" type="checkbox" id="pt-04-theme">
    <label class="pt-04__theme-label" for="pt-04-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="pt-04__sr">Toggle dark theme</span>
    </label>
  </div>

  <div class="pt-04__stage">
    <header class="pt-04__head">
      <p class="pt-04__kicker">Page transitions / 04</p>
      <h2 class="pt-04__h" id="pt-04-h">The height jump, and three fixes</h2>
      <p class="pt-04__lede">Each frame swaps the same two checkout steps &mdash; a short one and a tall one &mdash; with no script. Watch the ruler under each frame: if it moves, the document height moved.</p>
    </header>

    <div class="pt-04__frames">
      <article class="pt-04__frame pt-04__frame--broken">
        <div class="pt-04__label"><span class="pt-04__badge pt-04__badge--bad">Broken</span><p class="pt-04__label-t">Container height follows the content &mdash; the ruler jumps</p></div>
        <div class="pt-04__switch" role="group" aria-label="Broken frame route">
          <input class="pt-04__radio" type="radio" name="pt-04-a" id="pt-04-a1" checked>
          <label class="pt-04__pill" for="pt-04-a1">Step 2 &middot; short</label>
          <input class="pt-04__radio" type="radio" name="pt-04-a" id="pt-04-a2">
          <label class="pt-04__pill" for="pt-04-a2">Step 3 &middot; tall</label>
        </div>
        <div class="pt-04__view">
          <div class="pt-04__overlay" aria-hidden="true"></div>
          <div class="pt-04__route pt-04__route--short">
            <h3 class="pt-04__route-h">Shipping method</h3>
            <p class="pt-04__row"><b>Standard</b><span>4&ndash;6 days &middot; free</span></p>
            <p class="pt-04__row"><b>Express</b><span>2 days &middot; $14</span></p>
          </div>
          <div class="pt-04__route pt-04__route--tall">
            <h3 class="pt-04__route-h">Payment</h3>
            <p class="pt-04__row"><b>Card</b><span>Visa &middot; 4421</span></p>
            <p class="pt-04__row"><b>Billing</b><span>Same as shipping</span></p>
            <p class="pt-04__row"><b>Subtotal</b><span>$248.00</span></p>
            <p class="pt-04__row"><b>Tax</b><span>$21.08</span></p>
            <p class="pt-04__row pt-04__row--total"><b>Total</b><span>$269.08</span></p>
          </div>
        </div>
        <div class="pt-04__ruler" aria-hidden="true"><span></span><span></span><span></span></div>
      </article>

      <article class="pt-04__frame pt-04__frame--lock">
        <div class="pt-04__label"><span class="pt-04__badge">Fix 1</span><p class="pt-04__label-t">Height locked to the taller route &mdash; steady, with dead space</p></div>
        <div class="pt-04__switch" role="group" aria-label="Locked frame route">
          <input class="pt-04__radio" type="radio" name="pt-04-b" id="pt-04-b1" checked>
          <label class="pt-04__pill" for="pt-04-b1">Step 2 &middot; short</label>
          <input class="pt-04__radio" type="radio" name="pt-04-b" id="pt-04-b2">
          <label class="pt-04__pill" for="pt-04-b2">Step 3 &middot; tall</label>
        </div>
        <div class="pt-04__view">
          <div class="pt-04__overlay" aria-hidden="true"></div>
          <div class="pt-04__route pt-04__route--short">
            <h3 class="pt-04__route-h">Shipping method</h3>
            <p class="pt-04__row"><b>Standard</b><span>4&ndash;6 days &middot; free</span></p>
            <p class="pt-04__row"><b>Express</b><span>2 days &middot; $14</span></p>
          </div>
          <div class="pt-04__route pt-04__route--tall">
            <h3 class="pt-04__route-h">Payment</h3>
            <p class="pt-04__row"><b>Card</b><span>Visa &middot; 4421</span></p>
            <p class="pt-04__row"><b>Billing</b><span>Same as shipping</span></p>
            <p class="pt-04__row"><b>Subtotal</b><span>$248.00</span></p>
            <p class="pt-04__row"><b>Tax</b><span>$21.08</span></p>
            <p class="pt-04__row pt-04__row--total"><b>Total</b><span>$269.08</span></p>
          </div>
        </div>
        <div class="pt-04__ruler" aria-hidden="true"><span></span><span></span><span></span></div>
      </article>

      <article class="pt-04__frame pt-04__frame--pt-04-grow">
        <div class="pt-04__label"><span class="pt-04__badge">Fix 2</span><p class="pt-04__label-t">Height animated as part of the transition</p></div>
        <div class="pt-04__switch" role="group" aria-label="Animated height frame route">
          <input class="pt-04__radio" type="radio" name="pt-04-c" id="pt-04-c1" checked>
          <label class="pt-04__pill" for="pt-04-c1">Step 2 &middot; short</label>
          <input class="pt-04__radio" type="radio" name="pt-04-c" id="pt-04-c2">
          <label class="pt-04__pill" for="pt-04-c2">Step 3 &middot; tall</label>
        </div>
        <div class="pt-04__view">
          <div class="pt-04__overlay" aria-hidden="true"></div>
          <div class="pt-04__route pt-04__route--short">
            <h3 class="pt-04__route-h">Shipping method</h3>
            <p class="pt-04__row"><b>Standard</b><span>4&ndash;6 days &middot; free</span></p>
            <p class="pt-04__row"><b>Express</b><span>2 days &middot; $14</span></p>
          </div>
          <div class="pt-04__route pt-04__route--tall">
            <h3 class="pt-04__route-h">Payment</h3>
            <p class="pt-04__row"><b>Card</b><span>Visa &middot; 4421</span></p>
            <p class="pt-04__row"><b>Billing</b><span>Same as shipping</span></p>
            <p class="pt-04__row"><b>Subtotal</b><span>$248.00</span></p>
            <p class="pt-04__row"><b>Tax</b><span>$21.08</span></p>
            <p class="pt-04__row pt-04__row--total"><b>Total</b><span>$269.08</span></p>
          </div>
        </div>
        <div class="pt-04__ruler" aria-hidden="true"><span></span><span></span><span></span></div>
      </article>

      <article class="pt-04__frame pt-04__frame--abs">
        <div class="pt-04__label"><span class="pt-04__badge">Fix 3</span><p class="pt-04__label-t">Both routes out of flow &mdash; document height never changes</p></div>
        <div class="pt-04__switch" role="group" aria-label="Absolute frame route">
          <input class="pt-04__radio" type="radio" name="pt-04-d" id="pt-04-d1" checked>
          <label class="pt-04__pill" for="pt-04-d1">Step 2 &middot; short</label>
          <input class="pt-04__radio" type="radio" name="pt-04-d" id="pt-04-d2">
          <label class="pt-04__pill" for="pt-04-d2">Step 3 &middot; tall</label>
        </div>
        <div class="pt-04__view">
          <div class="pt-04__overlay" aria-hidden="true"></div>
          <div class="pt-04__route pt-04__route--short">
            <h3 class="pt-04__route-h">Shipping method</h3>
            <p class="pt-04__row"><b>Standard</b><span>4&ndash;6 days &middot; free</span></p>
            <p class="pt-04__row"><b>Express</b><span>2 days &middot; $14</span></p>
          </div>
          <div class="pt-04__route pt-04__route--tall">
            <h3 class="pt-04__route-h">Payment</h3>
            <p class="pt-04__row"><b>Card</b><span>Visa &middot; 4421</span></p>
            <p class="pt-04__row"><b>Billing</b><span>Same as shipping</span></p>
            <p class="pt-04__row"><b>Subtotal</b><span>$248.00</span></p>
            <p class="pt-04__row"><b>Tax</b><span>$21.08</span></p>
            <p class="pt-04__row pt-04__row--total"><b>Total</b><span>$269.08</span></p>
          </div>
        </div>
        <div class="pt-04__ruler" aria-hidden="true"><span></span><span></span><span></span></div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.pt-04 {
  --pt-04-bg: #eff2f3;
  --pt-04-s1: #ffffff;
  --pt-04-s2: #e4e9ea;
  --pt-04-s3: #d5dcdd;
  --pt-04-line: #c3cccd;
  --pt-04-ink: #171d1e;
  --pt-04-mut: #566063;
  --pt-04-acc: #0d7a63;
  --pt-04-bad: #b3402c;
  --pt-04-short: 8.5rem;
  --pt-04-tall: 15rem;
  --pt-04-dur: 620ms;
  --pt-04-font-display: "Roboto Condensed", "Archivo Narrow", "Helvetica Neue", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--pt-04-bg);
  color: var(--pt-04-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.5;
}

.pt-04 *,
.pt-04 *::before,
.pt-04 *::after {
  box-sizing: border-box;
}

.pt-04:has(.pt-04__theme-input:checked) {
  --pt-04-bg: #0c1112;
  --pt-04-s1: #141a1b;
  --pt-04-s2: #1b2223;
  --pt-04-s3: #232b2c;
  --pt-04-line: #2e3839;
  --pt-04-ink: #e8eeee;
  --pt-04-mut: #93a0a2;
  --pt-04-acc: #4fd0ae;
  --pt-04-bad: #f08a72;
}

@media (prefers-color-scheme: dark) {
  .pt-04 {
    --pt-04-bg: #0c1112;
    --pt-04-s1: #141a1b;
    --pt-04-s2: #1b2223;
    --pt-04-s3: #232b2c;
    --pt-04-line: #2e3839;
    --pt-04-ink: #e8eeee;
    --pt-04-mut: #93a0a2;
    --pt-04-acc: #4fd0ae;
    --pt-04-bad: #f08a72;
  }

  .pt-04:has(.pt-04__theme-input:checked) {
    --pt-04-bg: #eff2f3;
    --pt-04-s1: #ffffff;
    --pt-04-s2: #e4e9ea;
    --pt-04-s3: #d5dcdd;
    --pt-04-line: #c3cccd;
    --pt-04-ink: #171d1e;
    --pt-04-mut: #566063;
    --pt-04-acc: #0d7a63;
    --pt-04-bad: #b3402c;
  }
}

@media (prefers-color-scheme: light) {
  .pt-04:has(.pt-04__theme-input:checked) {
    --pt-04-bg: #0c1112;
    --pt-04-s1: #141a1b;
    --pt-04-s2: #1b2223;
    --pt-04-s3: #232b2c;
    --pt-04-line: #2e3839;
    --pt-04-ink: #e8eeee;
    --pt-04-mut: #93a0a2;
    --pt-04-acc: #4fd0ae;
    --pt-04-bad: #f08a72;
  }
}

@supports (color: oklch(0.5 0.1 170)) {
  .pt-04 {
    --pt-04-acc: oklch(0.5 0.1 172);
    --pt-04-bad: oklch(0.53 0.16 32);
  }

  .pt-04:has(.pt-04__theme-input:checked) {
    --pt-04-acc: oklch(0.82 0.13 172);
    --pt-04-bad: oklch(0.75 0.13 32);
  }

  @media (prefers-color-scheme: dark) {
    .pt-04 {
      --pt-04-acc: oklch(0.82 0.13 172);
      --pt-04-bad: oklch(0.75 0.13 32);
    }

    .pt-04:has(.pt-04__theme-input:checked) {
      --pt-04-acc: oklch(0.5 0.1 172);
      --pt-04-bad: oklch(0.53 0.16 32);
    }
  }
}

.pt-04__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pt-04__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 8;
}

.pt-04__theme-input {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
}

.pt-04__theme-label {
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border: 0;
  background: var(--pt-04-s2);
  color: var(--pt-04-mut);
  cursor: pointer;
  box-shadow: inset 0 0 0 1px var(--pt-04-line);
}

.pt-04__theme-label svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
}

.pt-04__theme-input:focus-visible + .pt-04__theme-label {
  outline: 2px solid var(--pt-04-acc);
  outline-offset: 2px;
}

.pt-04__stage {
  max-inline-size: 74rem;
  margin-inline: auto;
  padding: clamp(1.25rem, 4vw, 3rem) clamp(1rem, 4vw, 2.25rem) 3rem;
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.5rem;
}

.pt-04__kicker {
  margin: 0 0 0.5rem;
  font-family: var(--pt-04-font-display);
  font-size: 0.78rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--pt-04-mut);
}

.pt-04__h {
  margin: 0 0 0.55rem;
  font-family: var(--pt-04-font-display);
  font-size: clamp(1.5rem, 5vw, 2.3rem);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.005em;
}

.pt-04__lede {
  margin: 0;
  max-inline-size: 44rem;
  color: var(--pt-04-mut);
  font-size: 0.95rem;
  text-wrap: pretty;
}

.pt-04__frames {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.25rem;
}

@media (min-width: 56rem) {
  .pt-04__frames {
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
  }
}

.pt-04__frame {
  min-inline-size: 0;
  display: grid;
  gap: 0.7rem;
  align-content: start;
  padding: 1rem;
  background: var(--pt-04-s1);
}

.pt-04__label {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem;
  min-inline-size: 0;
}

.pt-04__badge {
  font-family: var(--pt-04-font-display);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 0.25rem 0.5rem;
  background: var(--pt-04-acc);
  color: var(--pt-04-s1);
}

.pt-04__badge--bad {
  background: var(--pt-04-bad);
}

.pt-04__label-t {
  margin: 0;
  font-size: 0.8rem;
  color: var(--pt-04-mut);
  min-inline-size: 0;
}

.pt-04__switch {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.pt-04__radio {
  position: absolute;
  opacity: 0;
  inline-size: 1px;
  block-size: 1px;
}

.pt-04__pill {
  display: flex;
  align-items: center;
  min-block-size: 2.75rem;
  padding: 0.4rem 0.85rem;
  background: var(--pt-04-s2);
  color: var(--pt-04-mut);
  font-family: var(--pt-04-font-display);
  font-size: 0.85rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  cursor: pointer;
}

.pt-04__radio:checked + .pt-04__pill {
  background: var(--pt-04-ink);
  color: var(--pt-04-bg);
}

.pt-04__radio:focus-visible + .pt-04__pill {
  outline: 2px solid var(--pt-04-acc);
  outline-offset: 2px;
}

.pt-04__view {
  position: relative;
  overflow: hidden;
  min-inline-size: 0;
  background: var(--pt-04-s2);
}

.pt-04__overlay {
  position: absolute;
  inset: 0;
  z-index: 3;
  background: var(--pt-04-ink);
  transform: scaleX(0);
  transform-origin: left center;
  pointer-events: none;
}

.pt-04__route {
  padding: 0.95rem 1.05rem;
  display: none;
}

.pt-04__route-h {
  margin: 0 0 0.6rem;
  font-family: var(--pt-04-font-display);
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}

.pt-04__row {
  margin: 0 0 0.4rem;
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  justify-content: space-between;
  min-inline-size: 0;
  font-size: 0.88rem;
  border-block-end: 1px solid var(--pt-04-line);
  padding-block-end: 0.4rem;
}

.pt-04__row span {
  color: var(--pt-04-mut);
  font-variant-numeric: tabular-nums;
}

.pt-04__row--total {
  border-block-end: 0;
  font-weight: 700;
}

.pt-04__row--total span {
  color: var(--pt-04-acc);
}

.pt-04__ruler {
  display: flex;
  gap: 0.35rem;
  align-items: center;
}

.pt-04__ruler span {
  block-size: 0.3rem;
  flex: 1 1 0;
  background: var(--pt-04-s3);
}

.pt-04__ruler span:first-child {
  background: var(--pt-04-acc);
  flex: 0 0 1.5rem;
}

.pt-04__frame:has(#pt-04-a1:checked) .pt-04__route--short,
.pt-04__frame:has(#pt-04-b1:checked) .pt-04__route--short,
.pt-04__frame:has(#pt-04-c1:checked) .pt-04__route--short,
.pt-04__frame:has(#pt-04-d1:checked) .pt-04__route--short,
.pt-04__frame:has(#pt-04-a2:checked) .pt-04__route--tall,
.pt-04__frame:has(#pt-04-b2:checked) .pt-04__route--tall,
.pt-04__frame:has(#pt-04-c2:checked) .pt-04__route--tall,
.pt-04__frame:has(#pt-04-d2:checked) .pt-04__route--tall {
  display: block;
  animation: pt-04-in var(--pt-04-dur) linear both;
}

.pt-04__frame:has(.pt-04__radio:checked) .pt-04__overlay {
  animation: pt-04-sweep-a var(--pt-04-dur) cubic-bezier(0.5, 0, 0.3, 1) both;
}

.pt-04__frame:has(#pt-04-a2:checked) .pt-04__overlay,
.pt-04__frame:has(#pt-04-b2:checked) .pt-04__overlay,
.pt-04__frame:has(#pt-04-c2:checked) .pt-04__overlay,
.pt-04__frame:has(#pt-04-d2:checked) .pt-04__overlay {
  animation-name: pt-04-sweep-b;
}

@keyframes pt-04-sweep-a {
  0% {
    transform: scaleX(0);
    transform-origin: left center;
  }

  40%,
    52% {
    transform: scaleX(1);
    transform-origin: left center;
  }

  53% {
    transform: scaleX(1);
    transform-origin: right center;
  }

  100% {
    transform: scaleX(0);
    transform-origin: right center;
  }
}

@keyframes pt-04-sweep-b {
  0% {
    transform: scaleX(0);
    transform-origin: left center;
  }

  40%,
    52% {
    transform: scaleX(1);
    transform-origin: left center;
  }

  53% {
    transform: scaleX(1);
    transform-origin: right center;
  }

  100% {
    transform: scaleX(0);
    transform-origin: right center;
  }
}

@keyframes pt-04-in {
  0%,
    45% {
    opacity: 0;
  }

  60%,
    100% {
    opacity: 1;
  }
}

.pt-04__frame--broken .pt-04__view {
  min-block-size: 0;
}

.pt-04__frame--lock .pt-04__view {
  min-block-size: var(--pt-04-tall);
}

.pt-04__frame--pt-04-grow .pt-04__view {
  block-size: var(--pt-04-short);
  transition: block-size var(--pt-04-dur) cubic-bezier(0.4, 0, 0.2, 1);
}

.pt-04__frame--pt-04-grow:has(#pt-04-c2:checked) .pt-04__view {
  block-size: var(--pt-04-tall);
}

.pt-04__frame--abs .pt-04__view {
  block-size: var(--pt-04-tall);
}

.pt-04__frame--abs .pt-04__route {
  position: absolute;
  inset: 0;
}

@media (prefers-reduced-motion: reduce) {
  .pt-04 {
    --pt-04-dur: 120ms;
  }

  .pt-04__frame--pt-04-grow .pt-04__view {
    transition-duration: 0s;
  }

  @keyframes pt-04-sweep-a {
    0%,
        100% {
      transform: scaleX(0);
    }

    50% {
      transform: scaleX(0.001);
    }
  }

  @keyframes pt-04-sweep-b {
    0%,
        100% {
      transform: scaleX(0);
    }

    50% {
      transform: scaleX(0.001);
    }
  }

  @keyframes pt-04-in {
    from {
      opacity: 0.6;
    }

    to {
      opacity: 1;
    }
  }
}
```
