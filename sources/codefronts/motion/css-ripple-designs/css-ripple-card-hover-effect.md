---
source: "codefronts"
url: "https://codefronts.com/motion/css-ripple-designs/css-ripple-card-hover-effect/"
title: "Ripple Card Hover Reveal"
section: "motion"
category: "css-ripple-designs"
category_name: "CSS Ripple Effects"
description: "A ripple opens from the card's corner and carries a state change with it — the detail row that was hidden."
has_js: "false"
---

Here's a working CSS Ripple Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Ripple Card Hover Reveal
Source: https://codefronts.com/motion/css-ripple-designs/css-ripple-card-hover-effect/

A ripple opens from the card's corner and carries a state change with it — the detail row that was hidden. The gate matters more than the effect: without @media (hover: hover) a touch device fires the hover state on tap and leaves it stuck, so the card ends up in a state the user cannot exit. Focus-within gets the same reveal for keyboard users.
## HTML
```html
<section class="rpl-16" aria-labelledby="rpl-16-title">
  <input class="rpl-16__theme-input" type="checkbox" id="rpl-16-theme">
  <label class="rpl-16__theme" for="rpl-16-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="rpl-16__theme-sr">Switch between dark and light theme</span>
  </label>
  <div class="rpl-16__wrap">
    <header class="rpl-16__head">
      <h1 class="rpl-16__h1" id="rpl-16-title">Field kits</h1>
      <p class="rpl-16__sub">Hover a kit to see what ships inside.</p>
    </header>
    <div class="rpl-16__grid">
      <article class="rpl-16__card">
        <span class="rpl-16__img" data-t="1" aria-hidden="true"></span>
        <div class="rpl-16__body">
          <p class="rpl-16__kind">Starter</p>
          <h2 class="rpl-16__name">Tide Pool Kit</h2>
          <p class="rpl-16__price">$68</p>
          <p class="rpl-16__reveal">Hand lens, salinity strips, waterproof log, tide chart card.</p>
        </div>
      </article>
      <article class="rpl-16__card">
        <span class="rpl-16__img" data-t="2" aria-hidden="true"></span>
        <div class="rpl-16__body">
          <p class="rpl-16__kind">Popular</p>
          <h2 class="rpl-16__name">Riverbed Kit</h2>
          <p class="rpl-16__price">$124</p>
          <p class="rpl-16__reveal">Flow meter, sediment sieve set, sample vials, field guide.</p>
        </div>
      </article>
      <article class="rpl-16__card">
        <span class="rpl-16__img" data-t="3" aria-hidden="true"></span>
        <div class="rpl-16__body">
          <p class="rpl-16__kind">Complete</p>
          <h2 class="rpl-16__name">Estuary Kit</h2>
          <p class="rpl-16__price">$210</p>
          <p class="rpl-16__reveal">Everything in Riverbed, plus a turbidity tube and drone mount.</p>
        </div>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.rpl-16 {
  --rpl-16-bg: #f6f7f9;
  --rpl-16-bg: oklch(0.968 0.004 250);
  --rpl-16-card: #ffffff;
  --rpl-16-card: oklch(1 0 0);
  --rpl-16-line: #e5e8ee;
  --rpl-16-line: oklch(0.920 0.006 250);
  --rpl-16-fg: #12161c;
  --rpl-16-fg: oklch(0.20 0.010 250);
  --rpl-16-muted: #575f6c;
  --rpl-16-muted: oklch(0.495 0.014 250);
  --rpl-16-accent: #0f7d6b;
  --rpl-16-accent: oklch(0.50 0.10 175);
  --rpl-16-ink: rgba(15, 125, 107, 0.12);
  --rpl-16-ink: oklch(0.50 0.10 175 / 0.12);
  --rpl-16-dur: 720ms;
  position: relative;
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  min-block-size: 100svh;
  padding: clamp(18px, 4vw, 56px);
  background: var(--rpl-16-bg);
  color: var(--rpl-16-fg);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
  box-sizing: border-box;
}

.rpl-16 *,
.rpl-16 *::before,
.rpl-16 *::after {
  box-sizing: border-box;
}

@media (prefers-color-scheme: dark) {
  .rpl-16:not(:has(#rpl-16-theme:checked)) {
    --rpl-16-bg: #0a0c10;
    --rpl-16-bg: oklch(0.16 0.008 250);
    --rpl-16-card: #14171d;
    --rpl-16-card: oklch(0.215 0.010 250);
    --rpl-16-line: #232831;
    --rpl-16-line: oklch(0.29 0.012 250);
    --rpl-16-fg: #eef1f5;
    --rpl-16-fg: oklch(0.955 0.005 250);
    --rpl-16-muted: #939ba8;
    --rpl-16-muted: oklch(0.70 0.014 250);
    --rpl-16-accent: #55d9bf;
    --rpl-16-accent: oklch(0.82 0.11 175);
    --rpl-16-ink: rgba(85, 217, 191, 0.13);
    --rpl-16-ink: oklch(0.82 0.11 175 / 0.13);
  }
}

@media (prefers-color-scheme: light) {
  .rpl-16:has(#rpl-16-theme:checked) {
    --rpl-16-bg: #0a0c10;
    --rpl-16-bg: oklch(0.16 0.008 250);
    --rpl-16-card: #14171d;
    --rpl-16-card: oklch(0.215 0.010 250);
    --rpl-16-line: #232831;
    --rpl-16-line: oklch(0.29 0.012 250);
    --rpl-16-fg: #eef1f5;
    --rpl-16-fg: oklch(0.955 0.005 250);
    --rpl-16-muted: #939ba8;
    --rpl-16-muted: oklch(0.70 0.014 250);
    --rpl-16-accent: #55d9bf;
    --rpl-16-accent: oklch(0.82 0.11 175);
    --rpl-16-ink: rgba(85, 217, 191, 0.13);
    --rpl-16-ink: oklch(0.82 0.11 175 / 0.13);
  }
}

.rpl-16__wrap {
  inline-size: 100%;
  max-inline-size: 1080px;
  display: flex;
  flex-direction: column;
  gap: clamp(20px, 3vw, 34px);
}

.rpl-16__head {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.rpl-16__h1 {
  margin: 0;
  font-size: clamp(28px, 5vw, 42px);
  font-weight: 620;
  letter-spacing: -0.032em;
}

.rpl-16__sub {
  margin: 0;
  font-size: 14.5px;
  color: var(--rpl-16-muted);
}

.rpl-16__grid {
  display: grid;
  gap: clamp(14px, 2vw, 20px);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 260px), 1fr));
}

.rpl-16__card {
  position: relative;
  display: flex;
  flex-direction: column;
  border: 1px solid var(--rpl-16-line);
  border-radius: 22px;
  background: var(--rpl-16-card);
  overflow: hidden;
  isolation: isolate;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1), border-color 320ms ease;
}

.rpl-16__img {
  display: block;
  block-size: clamp(150px, 20vh, 180px);
  background: linear-gradient(150deg, oklch(0.72 0.09 190), oklch(0.52 0.10 220));
}

.rpl-16__img[data-t="2"] {
  background: linear-gradient(150deg, oklch(0.74 0.10 150), oklch(0.50 0.09 195));
}

.rpl-16__img[data-t="3"] {
  background: linear-gradient(150deg, oklch(0.70 0.10 95), oklch(0.48 0.10 165));
}

.rpl-16__body {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 20px;
}

.rpl-16__kind {
  margin: 0;
  font-size: 10.5px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--rpl-16-accent);
  font-weight: 650;
}

.rpl-16__name {
  margin: 0;
  font-size: 19px;
  font-weight: 600;
  letter-spacing: -0.02em;
}

.rpl-16__price {
  margin: 0;
  font-size: 15px;
  color: var(--rpl-16-muted);
  font-variant-numeric: tabular-nums;
}

.rpl-16__reveal {
  margin: 0;
  font-size: 13px;
  line-height: 1.55;
  color: var(--rpl-16-muted);
  max-block-size: 0;
  opacity: 0;
  overflow: hidden;
  transition: max-block-size 380ms cubic-bezier(0.2, 0.7, 0.3, 1), opacity 260ms linear, margin 380ms ease;
  text-wrap: pretty;
}
/* Hover ripple, gated behind (hover: hover) so a touch tap never leaves it stuck open. */

.rpl-16__card::after {
  content: "";
  position: absolute;
  inset-block-start: 30%;
  inset-inline-start: 50%;
  inline-size: 200%;
  aspect-ratio: 1;
  border-radius: 50%;
  background: var(--rpl-16-ink);
  transform: translate(-50%, -50%) scale(0);
  opacity: 0;
  pointer-events: none;
  z-index: 0;
  transition: transform var(--rpl-16-dur) cubic-bezier(0.12, 0.72, 0.28, 1), opacity var(--rpl-16-dur) ease;
}

@media (hover: hover) and (pointer: fine) {
  .rpl-16__card:hover,
    .rpl-16__card:focus-within {
    transform: translateY(-4px);
    border-color: color-mix(in oklab, var(--rpl-16-accent) 40%, var(--rpl-16-line));
  }

  .rpl-16__card:hover::after,
    .rpl-16__card:focus-within::after {
    transform: translate(-50%, -50%) scale(1);
    opacity: 1;
  }

  .rpl-16__card:hover .rpl-16__reveal,
    .rpl-16__card:focus-within .rpl-16__reveal {
    max-block-size: 6em;
    opacity: 1;
    margin-block-start: 6px;
  }
}

@media (hover: none) {
  .rpl-16__reveal {
    max-block-size: 6em;
    opacity: 1;
    margin-block-start: 6px;
  }
}

@media (prefers-reduced-motion: reduce) {
  .rpl-16__card,
    .rpl-16__card::after,
    .rpl-16__reveal {
    transition: none;
  }

  .rpl-16__card::after {
    display: none;
  }

  .rpl-16__reveal {
    max-block-size: 6em;
    opacity: 1;
    margin-block-start: 6px;
  }
}

.rpl-16 {
  position: relative;
}

.rpl-16__theme-input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.rpl-16__theme {
  position: absolute;
  z-index: 60;
  inset-block-start: 14px;
  inset-inline-end: 14px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab, currentColor 22%, transparent);
  background: color-mix(in oklab, currentColor 8%, transparent);
  color: inherit;
  cursor: pointer;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  transition: background 160ms ease, border-color 160ms ease, transform 160ms ease;
}

.rpl-16__theme:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
  border-color: color-mix(in oklab, currentColor 38%, transparent);
}

.rpl-16__theme:active {
  transform: scale(0.94);
}

.rpl-16__theme svg {
  inline-size: 19px;
  block-size: 19px;
  display: block;
  transition: transform 320ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.rpl-16__theme-input:checked + .rpl-16__theme svg {
  transform: rotate(180deg);
}

.rpl-16__theme-input:focus-visible + .rpl-16__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.rpl-16__theme-sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (prefers-reduced-motion: reduce) {
  .rpl-16__theme,
    .rpl-16__theme svg {
    transition: none;
  }
}
```
