---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/stacked-glass/"
title: "Layered Stacked Glass Cards"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "Four glass cards fanned like a held deck, each rotated a few degrees and each refracting the ones behind it."
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Layered Stacked Glass Cards
Source: https://codefronts.com/design-styles/css-glassmorphism/stacked-glass/

Four glass cards fanned like a held deck, each rotated a few degrees and each refracting the ones behind it. Hover — or focus any card with the keyboard — and the deck spreads: rotation increases, offsets widen, and the depth that was implied becomes explicit. All motion is rotate and translate, so it runs entirely on the compositor.
## HTML
```html
<div class="gm-22">
  <input class="gm-22__sr" type="checkbox" id="gm-22-theme">
  <label class="gm-22__theme" for="gm-22-theme" title="Switch theme">
    <svg class="gm-22__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-22__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-22__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-22__stage">
    <header class="gm-22__head">
      <p class="gm-22__eyebrow">rotate · translate · glass on glass</p>
      <h2 class="gm-22__h">A held deck of frosted cards</h2>
      <p class="gm-22__sub">Hover the deck, or tab into it. Rotation and offset widen from the same depth index — nothing else moves.</p>
    </header>

    <div class="gm-22__deck">
      <article class="gm-22__card gm-22__card--4" aria-hidden="true">
        <p class="gm-22__tag">04</p>
      </article>
      <article class="gm-22__card gm-22__card--3" aria-hidden="true">
        <p class="gm-22__tag">03</p>
      </article>
      <article class="gm-22__card gm-22__card--2" aria-hidden="true">
        <p class="gm-22__tag">02</p>
      </article>
      <article class="gm-22__card gm-22__card--1" aria-labelledby="gm-22-ch">
        <p class="gm-22__tag">01 · front</p>
        <h3 class="gm-22__ch" id="gm-22-ch">Materials pass</h3>
        <p class="gm-22__ccopy">Every card is real glass, so the overlap regions blur what is already blurred. That density difference is what makes the stack read as physical.</p>
        <dl class="gm-22__meta">
          <div><dt>cards</dt><dd>4</dd></div>
          <div><dt>angle step</dt><dd>4° → 7°</dd></div>
        </dl>
        <button class="gm-22__cta" type="button">Open pass</button>
      </article>
    </div>

    <p class="gm-22__foot">Reduced motion swaps the spread for a static offset — the depth still reads, nothing animates.</p>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-22 {
  --a1: rgba(236,72,153,.55);
  --a2: rgba(56,189,248,.55);
  --a3: rgba(167,139,250,.55);
  --a4: rgba(250,204,21,.35);
  --base: #06070f;
  --base2: #160f31;
  --ink: #f9fafe;
  --muted: rgba(249,250,254,.7);
  --tint: #ffffff;
  --accent: #f9a8d4;
  --rim: rgba(255,255,255,.55);
  --rim2: rgba(255,255,255,.15);
  --edge: rgba(255,255,255,.2);
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  overflow: hidden;
  box-sizing: border-box;
  color: var(--ink);
  isolation: isolate;
  font-family: 'Geist',ui-sans-serif,system-ui,-apple-system,'Segoe UI',sans-serif;
  background: radial-gradient(52% 44% at 10% 16%, var(--a1) 0%, transparent 60%), radial-gradient(50% 44% at 88% 14%, var(--a2) 0%, transparent 60%), radial-gradient(52% 46% at 78% 88%, var(--a3) 0%, transparent 62%), radial-gradient(40% 34% at 18% 90%, var(--a4) 0%, transparent 56%), linear-gradient(158deg, var(--base) 0%, var(--base2) 52%, var(--base) 100%);
}

.gm-22 *,
.gm-22 *::before,
.gm-22 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-22 {
    --a1: oklch(0.7 0.24 350 / .56);
    --a2: oklch(0.78 0.16 220 / .56);
    --a3: oklch(0.7 0.19 292 / .56);
    --a4: oklch(0.88 0.16 95 / .36);
    --base: oklch(0.13 0.025 282);
    --base2: oklch(0.23 0.1 298);
    --accent: oklch(0.84 0.11 350);
  }
}

.gm-22__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-22__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-22__theme {
  position: absolute;
  inset-block-start: 1.15rem;
  inset-inline-end: 1.15rem;
  z-index: 20;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 999px;
  color: var(--ink);
  background: rgba(255,255,255,.14);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(10px) saturate(160%);
  backdrop-filter: blur(10px) saturate(160%);
  box-shadow: inset 0 1px 0 var(--rim), 0 10px 24px -14px rgba(0,0,0,.7);
  transition: scale .18s ease;
}

.gm-22__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-22__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-22__theme:hover {
  scale: 1.06;
}

.gm-22__sr:focus-visible + .gm-22__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-22__moon {
  display: none;
}

.gm-22__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(1.5rem,4vw,2.5rem);
  padding: clamp(1.5rem,5vw,4rem);
}

.gm-22__head {
  display: grid;
  gap: .55rem;
  justify-items: center;
  text-align: center;
  max-inline-size: 42rem;
}

.gm-22__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-22__h {
  margin: 0;
  font-size: clamp(1.8rem,4.4vw,2.8rem);
  font-weight: 600;
  letter-spacing: -.035em;
  line-height: 1.05;
  text-wrap: balance;
}

.gm-22__sub {
  margin: 0;
  font-size: clamp(.95rem,1.4vw,1.05rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-22__deck {
  position: relative;
  inline-size: min(27rem,100%);
  min-block-size: 19rem;
  margin-inline-end: clamp(0rem,8vw,6rem);
}

.gm-22__card {
  --i: 0;
  position: absolute;
  inset-block-start: 0;
  inset-inline-start: 0;
  inline-size: 100%;
  min-block-size: 17rem;
  display: flex;
  flex-direction: column;
  gap: .6rem;
  padding: clamp(1.15rem,2.2vw,1.6rem);
  border-radius: 1.6rem;
  border: 1px solid var(--edge);
  background: rgba(255,255,255,.13);
  transform-origin: bottom center;
  rotate: calc(var(--i) * 4deg);
  translate: calc(var(--i) * 1.6rem) calc(var(--i) * .35rem);
  z-index: calc(10 - var(--i));
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2), 0 28px 66px -30px rgba(0,0,0,.7);
  transition: rotate .38s cubic-bezier(.2,.7,.3,1), translate .38s cubic-bezier(.2,.7,.3,1);
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-22__card {
    background: color-mix(in oklab, var(--tint) 13%, transparent);
  }
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-22__card {
    -webkit-backdrop-filter: blur(22px) saturate(170%);
    backdrop-filter: blur(22px) saturate(170%);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-22__card {
    background: rgba(20,14,44,.9);
  }
}

.gm-22__card--1 {
  --i: 0;
  position: relative;
  background: rgba(255,255,255,.18);
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-22__card--1 {
    background: color-mix(in oklab, var(--tint) 18%, transparent);
  }
}

.gm-22__card--2 {
  --i: 1;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.38), 0 24px 58px -32px rgba(0,0,0,.6);
}

.gm-22__card--3 {
  --i: 2;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.26), 0 20px 50px -34px rgba(0,0,0,.5);
}

.gm-22__card--4 {
  --i: 3;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.16);
}

.gm-22__deck:hover .gm-22__card,
.gm-22__deck:focus-within .gm-22__card {
  rotate: calc(var(--i) * 7deg);
  translate: calc(var(--i) * 3.1rem) calc(var(--i) * -.4rem);
}

.gm-22__tag {
  margin: 0;
  align-self: flex-start;
  padding: .28rem .55rem;
  border-radius: .5rem;
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  background: rgba(255,255,255,.16);
  border: 1px solid var(--edge);
}

.gm-22__card--2 .gm-22__tag,
.gm-22__card--3 .gm-22__tag,
.gm-22__card--4 .gm-22__tag {
  position: absolute;
  inset-block-start: 1.15rem;
  inset-inline-end: 1.1rem;
  align-self: auto;
  opacity: .6;
}

.gm-22__ch {
  margin: .25rem 0 0;
  font-size: clamp(1.25rem,2.4vw,1.6rem);
  font-weight: 600;
  letter-spacing: -.025em;
}

.gm-22__ccopy {
  margin: 0;
  font-size: .94rem;
  line-height: 1.55;
  color: var(--ink);
  opacity: .86;
  text-wrap: pretty;
}

.gm-22__meta {
  margin: auto 0 0;
  padding-block-start: .9rem;
  border-block-start: 1px solid var(--rim2);
  display: flex;
  gap: 1.6rem;
}

.gm-22__meta div {
  display: grid;
  gap: .15rem;
}

.gm-22__meta dt {
  font-family: var(--mono);
  font-size: .62rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-22__meta dd {
  margin: 0;
  font-family: var(--mono);
  font-size: .88rem;
  font-variant-numeric: tabular-nums;
}

.gm-22__cta {
  align-self: flex-start;
  min-block-size: 2.75rem;
  padding: .7rem 1.1rem;
  border-radius: .9rem;
  cursor: pointer;
  font: inherit;
  font-size: .94rem;
  font-weight: 500;
  color: #2a0d20;
  background: var(--accent);
  border: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5), 0 14px 30px -16px rgba(0,0,0,.7);
  transition: translate .18s ease;
}

.gm-22__cta:hover {
  translate: 0 -2px;
}

.gm-22__cta:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-22__foot {
  margin: 0;
  font-size: .85rem;
  color: var(--muted);
  text-align: center;
}

.gm-22[data-theme="light"],
.gm-22:has(#gm-22-theme:checked) {
  --a1: rgba(249,168,212,.55);
  --a2: rgba(125,211,252,.55);
  --a3: rgba(196,181,253,.55);
  --a4: rgba(254,240,138,.45);
  --base: #f2f1fb;
  --base2: #e6e3fb;
  --ink: #10101f;
  --muted: rgba(16,16,31,.68);
  --rim: rgba(255,255,255,.95);
  --rim2: rgba(255,255,255,.5);
  --edge: rgba(16,16,31,.12);
  --accent: #db2777;
}

.gm-22:has(#gm-22-theme:checked) .gm-22__sun {
  display: none;
}

.gm-22:has(#gm-22-theme:checked) .gm-22__moon {
  display: block;
}

.gm-22[data-theme="light"] .gm-22__cta,
.gm-22:has(#gm-22-theme:checked) .gm-22__cta {
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .gm-22 *,
    .gm-22 *::before,
    .gm-22 *::after {
    transition: none !important;
    animation: none !important;
  }

  .gm-22__deck:hover .gm-22__card,
    .gm-22__deck:focus-within .gm-22__card {
    rotate: calc(var(--i) * 4deg);
    translate: calc(var(--i) * 1.6rem) calc(var(--i) * .35rem);
  }
}

@media (forced-colors: active) {
  .gm-22__card,
    .gm-22__cta,
    .gm-22__theme,
    .gm-22__tag {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }
}
```
