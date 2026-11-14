---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-brutalist/sticker-style-feature-cards/"
title: "Sticker Style Feature Cards"
section: "design-styles"
category: "css-brutalist"
category_name: "CSS Brutalism"
description: "Six feature cards pasted onto the page at slightly different angles, each one straightening under the pointer as its shadow deepens."
has_js: "false"
---

Here's a working CSS Brutalism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Sticker Style Feature Cards
Source: https://codefronts.com/design-styles/css-brutalist/sticker-style-feature-cards/

Six feature cards pasted onto the page at slightly different angles, each one straightening under the pointer as its shadow deepens. Every card's tilt is a single --rot value set inline, so the composition is data, not a pile of :nth-child overrides — and because rotate is its own property now, the hover transition can't fight a transform shorthand.
## HTML
```html
<div class="brt-04">
  <input class="brt-04__sr" type="checkbox" id="brt-04-dark">
  <label class="brt-04__theme" for="brt-04-dark">
    <svg class="brt-04__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20 14.2A8.2 8.2 0 0 1 9.8 4 8.4 8.4 0 1 0 20 14.2" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg>
    <svg class="brt-04__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.2" stroke="currentColor" stroke-width="2.2"/><path d="M12 3v2.2M12 18.8V21M3 12h2.2M18.8 12H21M5.6 5.6l1.6 1.6M16.8 16.8l1.6 1.6M18.4 5.6l-1.6 1.6M7.2 16.8l-1.6 1.6" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/></svg>
    <span class="brt-04__vh">Dark theme</span>
  </label>

  <div class="brt-04__stage">
    <section class="brt-04__wrap" aria-labelledby="brt-04-h">
      <header class="brt-04__head">
        <p class="brt-04__eyebrow">Why teams switch</p>
        <h2 class="brt-04__h" id="brt-04-h">Everything sticks together</h2>
      </header>
      <ul class="brt-04__grid">
        <li class="brt-04__card" style="--rot:-2deg">
          <span class="brt-04__icon"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M13 2 4 14h6l-1 8 9-12h-6z" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/></svg></span>
          <h3 class="brt-04__t"><a href="#brt-04-h">Deploys in 40 seconds</a></h3>
          <p class="brt-04__p">Push to main and the build is live before your coffee lands. Rollbacks are one keystroke.</p>
        </li>
        <li class="brt-04__card" style="--rot:1.5deg">
          <span class="brt-04__icon"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 3l7.5 3.4v5.1c0 4.3-3 8-7.5 9.5-4.5-1.5-7.5-5.2-7.5-9.5V6.4z" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/><path d="M8.6 12.2l2.4 2.3 4.4-4.6" stroke="currentColor" stroke-width="2.4" stroke-linecap="square"/></svg></span>
          <h3 class="brt-04__t"><a href="#brt-04-h">SOC 2 without the binder</a></h3>
          <p class="brt-04__p">Audit trails, SSO and device checks ship on by default. Evidence exports as CSV.</p>
        </li>
        <li class="brt-04__card" style="--rot:-1deg">
          <span class="brt-04__icon"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 18V8m5 10V4m5 14v-6m5 6V9" stroke="currentColor" stroke-width="2.6" stroke-linecap="square"/></svg></span>
          <h3 class="brt-04__t"><a href="#brt-04-h">Numbers you can trust</a></h3>
          <p class="brt-04__p">Every metric links back to the raw event. No pipeline mystery, no nightly reconciliation.</p>
        </li>
        <li class="brt-04__card" style="--rot:2.5deg">
          <span class="brt-04__icon"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="9" cy="8.5" r="3.2" stroke="currentColor" stroke-width="2.2"/><path d="M3 20c1.2-3 3.4-4.5 6-4.5S13.8 17 15 20" stroke="currentColor" stroke-width="2.2" stroke-linecap="square"/><path d="M16 5.5a3.2 3.2 0 0 1 0 6M18 20c-.5-2-1.2-3.4-2.2-4.4" stroke="currentColor" stroke-width="2.2" stroke-linecap="square"/></svg></span>
          <h3 class="brt-04__t"><a href="#brt-04-h">Guests, not seats</a></h3>
          <p class="brt-04__p">Invite a client to one project for free. They see what you share and nothing else.</p>
        </li>
        <li class="brt-04__card" style="--rot:-2.5deg">
          <span class="brt-04__icon"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="3.5" y="5" width="17" height="14" rx="2" stroke="currentColor" stroke-width="2.2"/><path d="M3.5 9.5h17M8 3.5V6m8-2.5V6" stroke="currentColor" stroke-width="2.2" stroke-linecap="square"/></svg></span>
          <h3 class="brt-04__t"><a href="#brt-04-h">Schedules that hold</a></h3>
          <p class="brt-04__p">Timezones, freezes and on-call windows are one calendar the whole team can read.</p>
        </li>
        <li class="brt-04__card" style="--rot:1deg">
          <span class="brt-04__icon"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 7h16M4 12h11M4 17h7" stroke="currentColor" stroke-width="2.6" stroke-linecap="square"/><circle cx="19" cy="16.5" r="3" stroke="currentColor" stroke-width="2.2"/></svg></span>
          <h3 class="brt-04__t"><a href="#brt-04-h">Search that finds it</a></h3>
          <p class="brt-04__p">Full-text across docs, tickets and commits, ranked by what your team opened last.</p>
        </li>
      </ul>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&display=swap');

.brt-04 {
  --page: #fbf7f0;
  --panel: #ffffff;
  --ink: #0b0b0f;
  --on: #0b0b0f;
  --muted: #4a4a52;
  --lilac: #c4b5fd;
  --mint: #86efac;
  --coral: #fda4af;
  --butter: #fde68a;
  --sky: #93c5fd;
  --edge: #000000;
  --sh: #000000;
  --bw: 3px;
  --r: 16px;
  --icon-r: 50%;
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

.brt-04 *,
.brt-04 *::before,
.brt-04 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .brt-04 {
    --page: oklch(0.975 0.014 84);
    --panel: oklch(1 0 0);
    --ink: oklch(0.16 0.01 285);
    --lilac: oklch(0.82 0.11 296);
    --mint: oklch(0.89 0.13 155);
    --coral: oklch(0.83 0.10 15);
    --butter: oklch(0.92 0.11 95);
    --sky: oklch(0.83 0.09 250);
  }
}

.brt-04__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.brt-04__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.brt-04__theme {
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

.brt-04__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
}

.brt-04__theme svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
}

.brt-04__theme:active {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--sh);
}

.brt-04__sr:focus-visible + .brt-04__theme {
  outline: 3px solid var(--edge);
  outline-offset: 3px;
}

.brt-04__sun {
  display: none;
}

.brt-04__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.5rem,5vw,3.5rem);
}

.brt-04__wrap {
  inline-size: min(70rem,100%);
}

.brt-04__head {
  margin-block-end: clamp(1.75rem,4vw,2.5rem);
  text-align: center;
}

.brt-04__eyebrow {
  display: inline-block;
  margin: 0 0 .7rem;
  padding: .3rem .65rem;
  rotate: -2deg;
  background: var(--sky);
  color: var(--on);
  border: 2px solid var(--edge);
  border-radius: 7px;
  box-shadow: 3px 3px 0 var(--sh);
  font-size: .74rem;
  font-weight: 700;
  letter-spacing: .14em;
  text-transform: uppercase;
}

.brt-04__h {
  margin: 0;
  font-size: clamp(2rem,5.2vw,3.1rem);
  font-weight: 700;
  letter-spacing: -.025em;
  line-height: 1.02;
  text-wrap: balance;
}

.brt-04__grid {
  list-style: none;
  margin: 0;
  padding: .5rem;
  display: grid;
  gap: clamp(1.25rem,2.8vw,2rem);
  grid-template-columns: repeat(auto-fit,minmax(min(16rem,100%),1fr));
}

.brt-04__card {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: .65rem;
  padding: clamp(1.1rem,2vw,1.5rem);
  border: var(--bw) solid var(--edge);
  border-radius: var(--r);
  box-shadow: 6px 6px 0 var(--sh);
  color: var(--on);
  rotate: var(--rot,0deg);
  transition: rotate .16s ease, translate .16s ease, box-shadow .16s ease;
}

.brt-04__card:nth-child(4n+1) {
  background: var(--butter);
}

.brt-04__card:nth-child(4n+2) {
  background: var(--mint);
}

.brt-04__card:nth-child(4n+3) {
  background: var(--lilac);
}

.brt-04__card:nth-child(4n+4) {
  background: var(--coral);
}

@media (hover: hover) {
  .brt-04__card:hover {
    rotate: 0deg;
    translate: -2px -3px;
    box-shadow: 10px 10px 0 var(--sh);
    z-index: 2;
  }
}

.brt-04__card:has(a:focus-visible) {
  rotate: 0deg;
  translate: -2px -3px;
  box-shadow: 10px 10px 0 var(--sh);
  z-index: 2;
}

.brt-04__icon {
  display: grid;
  place-items: center;
  inline-size: 3rem;
  block-size: 3rem;
  background: var(--panel);
  color: var(--ink);
  border: var(--bw) solid var(--edge);
  border-radius: var(--icon-r);
  box-shadow: 3px 3px 0 var(--sh);
}

.brt-04__icon svg {
  inline-size: 1.5rem;
  block-size: 1.5rem;
}

.brt-04__t {
  margin: .35rem 0 0;
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: -.015em;
  line-height: 1.15;
}

.brt-04__t a {
  color: inherit;
  text-decoration: none;
}

.brt-04__t a::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: var(--r);
}

.brt-04__t a:focus-visible {
  outline: none;
}

.brt-04__card:has(a:focus-visible) .brt-04__t a::after {
  outline: 3px solid var(--edge);
  outline-offset: 4px;
}

.brt-04__p {
  margin: 0;
  font-size: .95rem;
  line-height: 1.5;
  opacity: .8;
  text-wrap: pretty;
}

.brt-04:has(#brt-04-dark:checked) {
  --page: #14131a;
  --panel: #221f2b;
  --ink: #f7f5ef;
  --muted: #b5b1c2;
  --edge: #f7f5ef;
  --sh: #f7f5ef;
}

.brt-04:has(#brt-04-dark:checked) .brt-04__moon {
  display: none;
}

.brt-04:has(#brt-04-dark:checked) .brt-04__sun {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .brt-04:not(:has(#brt-04-dark:checked)) {
    --page: #14131a;
    --panel: #221f2b;
    --ink: #f7f5ef;
    --muted: #b5b1c2;
    --edge: #f7f5ef;
    --sh: #f7f5ef;
  }

  .brt-04:not(:has(#brt-04-dark:checked)) .brt-04__moon {
    display: none;
  }

  .brt-04:not(:has(#brt-04-dark:checked)) .brt-04__sun {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .brt-04 *,
    .brt-04 *::before,
    .brt-04 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .brt-04__card,
    .brt-04__icon,
    .brt-04__theme {
    border-color: CanvasText;
    box-shadow: none;
  }
}
/* stage children default to min-width:auto, so a wide heading or grid
   track forces the panel past the stage; 0 lets it shrink instead */

.brt-04__stage > * {
  min-inline-size: 0;
  max-inline-size: 100%;
}
```
