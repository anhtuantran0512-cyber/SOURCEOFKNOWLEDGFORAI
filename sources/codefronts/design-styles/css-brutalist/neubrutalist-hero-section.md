---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/neubrutalist-hero-section/"
title: "Neubrutalist Hero Section"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "A landing hero with a clamped 4-6rem headline, one word sitting on a rotated pastel highlight block, two buttons and a bordered sticker card floating beside…"
has_js: "false"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neubrutalist Hero Section
Source: https://codefronts.com/design-styles/css-brutalist/neubrutalist-hero-section/

A landing hero with a clamped 4-6rem headline, one word sitting on a rotated pastel highlight block, two buttons and a bordered sticker card floating beside the copy. The load sequence is a single staggered CSS animation driven by --i per element — no JS, no observer, and it switches itself off under prefers-reduced-motion.
## HTML
```html
<div class="brt-11">
  <input class="brt-11__sr" type="checkbox" id="brt-11-dark">
  <label class="brt-11__theme" for="brt-11-dark">
    <svg class="brt-11__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-11__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    <span class="brt-11__vh">Dark theme</span>
  </label>

  <div class="brt-11__stage">
    <section class="brt-11__hero" aria-labelledby="brt-11-h">
      <div class="brt-11__copy">
        <p class="brt-11__in brt-11__eyebrow" style="--i:0">Now in every region</p>
        <h1 class="brt-11__in brt-11__h" id="brt-11-h" style="--i:1">Ship the page, <span class="brt-11__mark">not the meeting</span></h1>
        <p class="brt-11__in brt-11__lede" style="--i:2">Pagecraft turns a written brief into a live, responsive page you can edit in the browser — and hands your engineers real CSS when they want it.</p>
        <div class="brt-11__in brt-11__actions" style="--i:3">
          <a class="brt-11__cta" href="#brt-11-h">Start building free</a>
          <a class="brt-11__ghost" href="#brt-11-h">
            <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M8 5.5l11 6.5-11 6.5z" stroke="currentColor" stroke-width="2.4" stroke-linejoin="round"/></svg>
            Watch the 90-second tour
          </a>
        </div>
        <ul class="brt-11__in brt-11__proof" style="--i:4">
          <li><b>1,284</b> teams building</li>
          <li><b>40s</b> median deploy</li>
          <li><b>4.9</b> average rating</li>
        </ul>
      </div>

      <aside class="brt-11__in brt-11__side" style="--i:2">
        <div class="brt-11__card">
          <p class="brt-11__cardl">This week</p>
          <p class="brt-11__cardn">18 pages</p>
          <ul class="brt-11__list">
            <li><span class="brt-11__dot" aria-hidden="true"></span>pricing-v4 · published</li>
            <li><span class="brt-11__dot brt-11__dot--b" aria-hidden="true"></span>careers · in review</li>
            <li><span class="brt-11__dot brt-11__dot--c" aria-hidden="true"></span>changelog · draft</li>
          </ul>
        </div>
        <p class="brt-11__sticker" aria-hidden="true">No build step</p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap');

.brt-11 {
  --page: #fdf3e3;
  --panel: #ffffff;
  --ink: #0b0b0f;
  --on: #0b0b0f;
  --muted: #4a4a52;
  --lilac: #c4b5fd;
  --mint: #86efac;
  --coral: #fda4af;
  --butter: #fde68a;
  --sky: #93c5fd;
  --hl: #86efac;
  --edge: #000000;
  --sh: #000000;
  --bw: 3px;
  --r: 16px;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: 'Space Grotesk','Sora',ui-sans-serif,system-ui,sans-serif;
}

.brt-11 *,
.brt-11 *::before,
.brt-11 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-11 {
    --page: oklch(0.958 0.032 82);
    --panel: oklch(1 0 0);
    --ink: oklch(0.16 0.01 285);
    --lilac: oklch(0.82 0.11 296);
    --mint: oklch(0.89 0.13 155);
    --coral: oklch(0.83 0.10 15);
    --butter: oklch(0.92 0.11 95);
    --sky: oklch(0.83 0.09 250);
    --hl: oklch(0.89 0.13 155);
  }
}

.brt-11__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.brt-11__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.brt-11__theme {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  border-radius: 10px;
  box-shadow: 4px 4px 0 var(--sh);
  cursor: pointer;
  transition: translate .14s ease, box-shadow .14s ease;
}

.brt-11__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-11__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-11__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-11__sr:focus-visible + .brt-11__theme {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-11__sun {
  display: none;
}

.brt-11__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,5vw,4rem);
}

.brt-11__hero {
  inline-size: min(76rem,100%);
  display: grid;
  gap: clamp(2rem,5vw,3.5rem);
  grid-template-columns: repeat(auto-fit,minmax(min(19rem,100%),1fr));
  align-items: center;
}

.brt-11__in {
  animation: brt-11-rise .5s cubic-bezier(.2,.9,.2,1) both;
  animation-delay: calc(var(--i,0) * 70ms);
}

@keyframes brt-11-rise {
  from {
    opacity: 0;
    translate: 0 14px;
  }

  to {
    opacity: 1;
    translate: 0 0;
  }
}

.brt-11__copy {
  max-inline-size: 34rem;
}

.brt-11__eyebrow {
  display: inline-block;
  margin: 0 0 1rem;
  padding: .35rem .7rem;
  background: var(--panel);
  color: var(--ink);
  border: 2px solid var(--edge);
  border-radius: 999px;
  box-shadow: 3px 3px 0 var(--sh);
  font-size: .76rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
}

.brt-11__h {
  margin: 0;
  font-size: clamp(2.6rem,8vw,5.2rem);
  font-weight: 700;
  letter-spacing: -.038em;
  line-height: .98;
  text-wrap: balance;
}

.brt-11__mark {
  position: relative;
  isolation: isolate;
  white-space: nowrap;
}

.brt-11__mark::before {
  content: '';
  position: absolute;
  inset: .12em -.22em .06em;
  z-index: -1;
  background: var(--hl);
  border: var(--bw) solid var(--edge);
  border-radius: 9px;
  rotate: -1.8deg;
}

.brt-11__lede {
  margin: 1.25rem 0 0;
  max-inline-size: 44ch;
  font-size: clamp(1rem,1.6vw,1.15rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.brt-11__actions {
  display: flex;
  flex-wrap: wrap;
  gap: .85rem;
  margin-block-start: 1.75rem;
}

.brt-11__cta {
  display: inline-flex;
  align-items: center;
  min-block-size: 3rem;
  padding: .85rem 1.4rem;
  background: var(--ink);
  color: var(--page);
  text-decoration: none;
  font-weight: 700;
  font-size: 1.02rem;
  border: var(--bw) solid var(--edge);
  border-radius: 12px;
  box-shadow: 5px 5px 0 var(--sh);
  transition: translate .14s ease, box-shadow .14s ease;
}

.brt-11__cta:hover {
  translate: -1px -1px;
  box-shadow: 7px 7px 0 var(--sh);
}

.brt-11__cta:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-11__cta:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-11__ghost {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  min-block-size: 3rem;
  padding: .85rem 1.2rem;
  background: var(--panel);
  color: var(--ink);
  text-decoration: none;
  font-weight: 700;
  font-size: 1.02rem;
  border: var(--bw) solid var(--edge);
  border-radius: 12px;
  box-shadow: 5px 5px 0 var(--sh);
  transition: translate .14s ease, box-shadow .14s ease, background .14s ease;
}

.brt-11__ghost svg {
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.brt-11__ghost:hover {
  background: var(--sky);
  color: var(--on);
  translate: -1px -1px;
  box-shadow: 7px 7px 0 var(--sh);
}

.brt-11__ghost:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-11__ghost:focus-visible {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-11__proof {
  list-style: none;
  margin: 2rem 0 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .6rem 1.75rem;
  font-size: .9rem;
  color: var(--muted);
}

.brt-11__proof b {
  display: block;
  font-size: 1.35rem;
  color: var(--ink);
  letter-spacing: -.02em;
  font-variant-numeric: tabular-nums;
}

.brt-11__side {
  position: relative;
  justify-self: center;
}

.brt-11__card {
  inline-size: min(22rem,100%);
  padding: 1.35rem 1.4rem;
  rotate: 1.6deg;
  background: var(--panel);
  border: var(--bw) solid var(--edge);
  border-radius: var(--r);
  box-shadow: 10px 10px 0 var(--sh);
}

.brt-11__cardl {
  margin: 0;
  font-size: .74rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.brt-11__cardn {
  margin: .2rem 0 1rem;
  font-size: 2.6rem;
  font-weight: 700;
  letter-spacing: -.035em;
  line-height: 1;
}

.brt-11__list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .55rem;
  font-size: .9rem;
  font-weight: 600;
}

.brt-11__list li {
  display: flex;
  align-items: center;
  gap: .55rem;
  padding: .55rem .65rem;
  background: var(--page);
  border: 2px solid var(--edge);
  border-radius: 9px;
}

.brt-11__dot {
  inline-size: .85rem;
  block-size: .85rem;
  flex: none;
  background: var(--mint);
  border: 2px solid var(--edge);
  border-radius: 50%;
}

.brt-11__dot--b {
  background: var(--butter);
}

.brt-11__dot--c {
  background: var(--coral);
}

.brt-11__sticker {
  position: absolute;
  inset-block-end: -1.4rem;
  inset-inline-start: -1rem;
  margin: 0;
  rotate: -7deg;
  padding: .55rem .85rem;
  background: var(--coral);
  color: var(--on);
  border: var(--bw) solid var(--edge);
  border-radius: 10px;
  box-shadow: 4px 4px 0 var(--sh);
  font-size: .85rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
}

.brt-11:has(#brt-11-dark:checked) {
  --page: #191521;
  --panel: #241f2e;
  --ink: #f9f6ef;
  --muted: #bab5c6;
  --edge: #f9f6ef;
  --sh: #f9f6ef;
}

.brt-11:has(#brt-11-dark:checked) .brt-11__moon {
  display: none;
}

.brt-11:has(#brt-11-dark:checked) .brt-11__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-11:not(:has(#brt-11-dark:checked)) {
    --page: #191521;
    --panel: #241f2e;
    --ink: #f9f6ef;
    --muted: #bab5c6;
    --edge: #f9f6ef;
    --sh: #f9f6ef;
  }

  .brt-11:not(:has(#brt-11-dark:checked)) .brt-11__moon {
    display: none;
  }

  .brt-11:not(:has(#brt-11-dark:checked)) .brt-11__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-11 *,
    .brt-11 *::before,
    .brt-11 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .brt-11__card,
    .brt-11__cta,
    .brt-11__ghost,
    .brt-11__sticker,
    .brt-11__theme {
    border-color: CanvasText;
    box-shadow: none;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-11__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
/* At 320px the highlighted phrase alone is wider than the column, so the
   nowrap that protects the highlight from splitting across lines must
   yield. The ::before still tracks each resulting line box. */

@media (max-width: 22.5rem) {
  .brt-11__mark {
    white-space: normal;
  }
}
```
