---
source: "codefronts"
url: "https://codefronts.com/motion/css-view-transitions/add-to-cart-badge-counter-morph/"
title: "Add to Cart Badge Counter Morph"
section: "motion"
category: "css-view-transitions"
category_name: "CSS View Transitions"
description: "The product thumbnail travels to the cart icon while the badge count updates in the same transition."
has_js: "true"
---

Here's a working CSS View Transition from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Add to Cart Badge Counter Morph
Source: https://codefronts.com/motion/css-view-transitions/add-to-cart-badge-counter-morph/

The product thumbnail travels to the cart icon while the badge count updates in the same transition. Two named elements participate: the image, whose old position is the product card and whose new position is the cart, and the badge, which morphs between counts. The ordering trap is that the badge must already exist before the transition, or you get a fade instead of a morph.
## HTML
```html
<section class="vtr-11" aria-labelledby="vtr-11-heading">
  <fieldset class="vtr-11__theme">
    <legend class="vtr-11__themelegend">Theme</legend>
    <input class="vtr-11__themeinput" type="radio" name="vtr-11-theme" id="vtr-11-theme-auto" checked>
    <label class="vtr-11__themeopt" for="vtr-11-theme-auto">Auto</label>
    <input class="vtr-11__themeinput" type="radio" name="vtr-11-theme" id="vtr-11-theme-light">
    <label class="vtr-11__themeopt" for="vtr-11-theme-light">Light</label>
    <input class="vtr-11__themeinput" type="radio" name="vtr-11-theme" id="vtr-11-theme-dark">
    <label class="vtr-11__themeopt" for="vtr-11-theme-dark">Dark</label>
  </fieldset>
  <div class="vtr-11__stage">
    <header class="vtr-11__head">
      <div>
        <p class="vtr-11__kicker">Nova Supply</p>
        <h2 class="vtr-11__heading" id="vtr-11-heading">Two names, one flight</h2>
      </div>
      <button class="vtr-11__cart" type="button" aria-label="Cart">
        <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M4 5h2.2l2.3 9.4h9.1l2-6.4H7" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/><circle cx="10" cy="19" r="1.5" fill="currentColor"/><circle cx="17.5" cy="19" r="1.5" fill="currentColor"/></svg>
        <span class="vtr-11__slot" id="vtr-11-slot"></span>
        <span class="vtr-11__badge" id="vtr-11-badge">0</span>
      </button>
    </header>

    <ul class="vtr-11__products">
      <li class="vtr-11__product">
        <span class="vtr-11__art vtr-11__art--a" data-vtr11-art></span>
        <div class="vtr-11__ptext">
          <p class="vtr-11__pname">Basalt Desk Mat</p>
          <p class="vtr-11__pprice">48.00</p>
        </div>
        <button class="vtr-11__add" type="button" data-vtr11-add>Add</button>
      </li>
      <li class="vtr-11__product">
        <span class="vtr-11__art vtr-11__art--b" data-vtr11-art></span>
        <div class="vtr-11__ptext">
          <p class="vtr-11__pname">Fern Notebook, ruled</p>
          <p class="vtr-11__pprice">14.00</p>
        </div>
        <button class="vtr-11__add" type="button" data-vtr11-add>Add</button>
      </li>
      <li class="vtr-11__product">
        <span class="vtr-11__art vtr-11__art--c" data-vtr11-art></span>
        <div class="vtr-11__ptext">
          <p class="vtr-11__pname">Orbit Cable Set</p>
          <p class="vtr-11__pprice">22.50</p>
        </div>
        <button class="vtr-11__add" type="button" data-vtr11-add>Add</button>
      </li>
    </ul>

    <p class="vtr-11__status" id="vtr-11-status" role="status" aria-live="polite">Cart is empty</p>
  </div>
</section>
```
## CSS
```css
.vtr-11 {
  --bg: #fff7f3;
  --surface: #ffffff;
  --line: #f3ddd2;
  --ink: #2a1610;
  --muted: #7d5c50;
  --accent: #f2653c;
  --accent-soft: #ffe6dd;
  --font-display: "Helvetica Neue", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  color-scheme: light dark;
}

.vtr-11 *,
.vtr-11 *::before,
.vtr-11 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0% 0 0)) {
  .vtr-11 {
    --bg: oklch(97.5% 0.015 40);
    --line: oklch(90% 0.035 40);
    --ink: oklch(24% 0.04 35);
    --muted: oklch(50% 0.045 40);
    --accent: oklch(65% 0.18 38);
    --accent-soft: oklch(93% 0.05 40);
  }
}

@media (prefers-color-scheme: dark) {
  .vtr-11 {
    --bg: #1a100c;
    --surface: #241611;
    --line: #3a241c;
    --ink: #ffeee7;
    --muted: #c09a8c;
    --accent: #ff8a5f;
    --accent-soft: #3d2117;
  }
}

.vtr-11[data-theme="light"] {
  --bg: #fff7f3;
  --surface: #ffffff;
  --line: #f3ddd2;
  --ink: #2a1610;
  --muted: #7d5c50;
  --accent: #f2653c;
  --accent-soft: #ffe6dd;
}

.vtr-11[data-theme="dark"] {
  --bg: #1a100c;
  --surface: #241611;
  --line: #3a241c;
  --ink: #ffeee7;
  --muted: #c09a8c;
  --accent: #ff8a5f;
  --accent-soft: #3d2117;
}

.vtr-11__stage {
  max-width: 46rem;
  margin: 0 auto;
  padding: clamp(1.5rem, 4vw, 3rem) clamp(1rem, 4vw, 2rem);
  display: grid;
  gap: 1.25rem;
}

.vtr-11__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  flex-wrap: wrap;
}

.vtr-11__kicker {
  margin: 0 0 0.3rem;
  font-size: 0.7rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
}

.vtr-11__heading {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.35rem, 4.4vw, 1.9rem);
  font-weight: 700;
  letter-spacing: -0.025em;
}

.vtr-11__cart {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 3rem;
  height: 3rem;
  min-height: 44px;
  border: 0;
  border-radius: 999px;
  background: var(--surface);
  color: var(--ink);
  cursor: pointer;
  box-shadow: 0 10px 24px -14px rgba(242, 101, 60, 0.8);
}

.vtr-11__cart:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.vtr-11__slot {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  pointer-events: none;
}

.vtr-11__slot .vtr-11__art {
  width: 1.1rem;
  height: 1.1rem;
  border-radius: 0.25rem;
}

.vtr-11__badge {
  position: absolute;
  top: -0.25rem;
  right: -0.25rem;
  min-width: 1.35rem;
  height: 1.35rem;
  padding: 0 0.3rem;
  display: grid;
  place-items: center;
  border-radius: 999px;
  background: var(--accent);
  color: #ffffff;
  font-size: 0.72rem;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
  view-transition-name: vtr-11-badge;
}

.vtr-11__products {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0.6rem;
}

.vtr-11__product {
  display: grid;
  grid-template-columns: 3.25rem 1fr auto;
  gap: 0.85rem;
  align-items: center;
  padding: 0.7rem 0.85rem;
  border-radius: 1rem;
  background: var(--surface);
  border: 1px solid var(--line);
  min-inline-size: 0;
}

.vtr-11__art {
  display: block;
  width: 3.25rem;
  height: 3.25rem;
  border-radius: 0.6rem;
}

.vtr-11__art--a {
  background: linear-gradient(135deg, #1f2937, #64748b);
}

.vtr-11__art--b {
  background: linear-gradient(135deg, #166534, #86efac);
}

.vtr-11__art--c {
  background: linear-gradient(135deg, #7c2d12, #fdba74);
}

.vtr-11__ptext {
  min-inline-size: 0;
}

.vtr-11__pname {
  margin: 0 0 0.15rem;
  font-size: 0.9rem;
  font-weight: 600;
}

.vtr-11__pprice {
  margin: 0;
  font-size: 0.8rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.vtr-11__add {
  min-height: 44px;
  padding: 0 1.1rem;
  border: 0;
  border-radius: 999px;
  background: var(--accent);
  color: #ffffff;
  font-size: 0.82rem;
  font-weight: 700;
  cursor: pointer;
}

.vtr-11__add:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.vtr-11__status {
  margin: 0;
  padding: 0.6rem 0.8rem;
  border-radius: 0.75rem;
  background: var(--accent-soft);
  font-size: 0.8rem;
  color: var(--ink);
}

::view-transition-group(vtr-11-fly) {
  animation-duration: 520ms;
  animation-timing-function: cubic-bezier(0.32, 0.72, 0, 1);
}

::view-transition-group(vtr-11-badge) {
  animation-duration: 320ms;
}

@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(vtr-11-fly),
    ::view-transition-group(vtr-11-badge) {
    animation-duration: 1ms;
  }
}
/* Theme switch (added 2026-08-24). Pure CSS: three radios + :has(). Auto
   follows the OS and the site's [data-theme] stamp; Light and Dark pin the
   palette. Values are the demo's own [data-theme] palettes reused verbatim,
   so the toggle can never drift from the site-theme rendering. */

.vtr-11 {
  position: relative;
}

.vtr-11__theme {
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

.vtr-11__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-11__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.vtr-11__themeopt {
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

.vtr-11__themeopt:hover {
  opacity: 0.85;
}

.vtr-11__themeinput:checked + .vtr-11__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.vtr-11__themeinput:focus-visible + .vtr-11__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
/* Explicit pins beat both the OS query and the site stamp. */

.vtr-11:has(#vtr-11-theme-light:checked) {
  --bg: #fff7f3;
  --surface: #ffffff;
  --line: #f3ddd2;
  --ink: #2a1610;
  --muted: #7d5c50;
  --accent: #f2653c;
  --accent-soft: #ffe6dd;
}

.vtr-11:has(#vtr-11-theme-dark:checked) {
  --bg: #1a100c;
  --surface: #241611;
  --line: #3a241c;
  --ink: #ffeee7;
  --muted: #c09a8c;
  --accent: #ff8a5f;
  --accent-soft: #3d2117;
}
```

## JavaScript
```js
(() => {
  const root = document.querySelector('.vtr-11');
  if (!root || root.dataset.vtr11) return;
  root.dataset.vtr11 = 'on';
  const badge = root.querySelector('#vtr-11-badge');
  const slot = root.querySelector('#vtr-11-slot');
  const status = root.querySelector('#vtr-11-status');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let count = 0, busy = false;
  const commit = (art) => {
    count += 1;
    badge.textContent = String(count);
    slot.replaceChildren(art);
    status.textContent = count + (count === 1 ? ' item in cart' : ' items in cart');
  };
  root.addEventListener('click', async (e) => {
    const btn = e.target.closest('[data-vtr11-add]');
    if (!btn || busy) return;
    const src = btn.closest('.vtr-11__product').querySelector('[data-vtr11-art]');
    const art = src.cloneNode(true);
    if (!document.startViewTransition || reduce.matches) { commit(art); return; }
    busy = true;
    src.style.viewTransitionName = 'vtr-11-fly';
    art.style.viewTransitionName = 'vtr-11-fly';
    try { await document.startViewTransition(() => { src.style.viewTransitionName = ''; commit(art); }).finished; }
    finally { art.style.viewTransitionName = ''; src.style.viewTransitionName = ''; busy = false; }
  });
})();
```
