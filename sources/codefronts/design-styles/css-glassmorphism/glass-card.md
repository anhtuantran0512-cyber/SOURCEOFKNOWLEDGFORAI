---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/glass-card/"
title: "Frosted Glass Card Component"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "The reference implementation of the whole technique in one card: 24px blur, 180% saturate, a double inset rim, a real photo, and a monospace spec strip that…"
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Frosted Glass Card Component
Source: https://codefronts.com/design-styles/css-glassmorphism/glass-card/

The reference implementation of the whole technique in one card: 24px blur, 180% saturate, a double inset rim, a real photo, and a monospace spec strip that names every value used. If you copy one thing from this collection into a project, copy this — then read demos 01 and 02 to understand why the numbers are what they are.
## HTML
```html
<div class="gm-11">
  <input class="gm-11__sr" type="checkbox" id="gm-11-theme">
  <label class="gm-11__theme" for="gm-11-theme" title="Switch theme">
    <svg class="gm-11__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-11__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-11__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-11__stage">
    <article class="gm-11__card" aria-labelledby="gm-11-h">
      <div class="gm-11__top">
        <img class="gm-11__photo" src="https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=192&h=192&q=80" width="96" height="96" loading="lazy" decoding="async" alt="Portrait of Alex Chen">
        <div class="gm-11__ident">
          <p class="gm-11__eyebrow">Design engineering</p>
          <h2 class="gm-11__h" id="gm-11-h">Alex Chen</h2>
          <p class="gm-11__role">Shipping the Atlas glass system</p>
        </div>
        <span class="gm-11__badge">Reference</span>
      </div>

      <p class="gm-11__copy">One card, five declarations. A translucent film, a blur, a saturation boost, a two-stop inset rim and one soft ambient shadow — everything else on this page is a variation of these five lines.</p>

      <ul class="gm-11__stats">
        <li><span class="gm-11__snum">24px</span><span class="gm-11__slabel">blur</span></li>
        <li><span class="gm-11__snum">180%</span><span class="gm-11__slabel">saturate</span></li>
        <li><span class="gm-11__snum">16%</span><span class="gm-11__slabel">film</span></li>
      </ul>

      <div class="gm-11__actions">
        <button class="gm-11__cta" type="button">Copy the recipe</button>
        <button class="gm-11__ghost" type="button">Open in playground</button>
      </div>

      <p class="gm-11__spec">backdrop-filter: blur(24px) saturate(180%) · inset 0 1px 0 rgba(255,255,255,.5)</p>
    </article>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-11 {
  --a1: rgba(216,180,254,.6);
  --a2: rgba(103,232,249,.55);
  --a3: rgba(253,164,175,.55);
  --a4: rgba(254,240,138,.5);
  --base: #f1f3fb;
  --base2: #e4e8fd;
  --ink: #0f1120;
  --muted: rgba(15,17,32,.68);
  --tint: #ffffff;
  --accent: #7c3aed;
  --rim: rgba(255,255,255,.95);
  --rim2: rgba(255,255,255,.5);
  --edge: rgba(15,17,32,.12);
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
  background: radial-gradient(56% 46% at 14% 16%, var(--a1) 0%, transparent 62%), radial-gradient(48% 42% at 86% 12%, var(--a2) 0%, transparent 58%), radial-gradient(52% 46% at 80% 86%, var(--a3) 0%, transparent 60%), radial-gradient(42% 36% at 14% 90%, var(--a4) 0%, transparent 58%), linear-gradient(160deg, var(--base) 0%, var(--base2) 52%, var(--base) 100%);
}

.gm-11 *,
.gm-11 *::before,
.gm-11 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-11 {
    --a1: oklch(0.68 0.24 305 / .62);
    --a2: oklch(0.82 0.16 200 / .56);
    --a3: oklch(0.72 0.19 15 / .5);
    --a4: oklch(0.88 0.16 95 / .36);
    --base: oklch(0.97 0.008 275);
    --base2: oklch(0.93 0.015 285);
    --accent: oklch(0.85 0.09 292);
  }
}

.gm-11__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-11__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-11__theme {
  position: absolute;
  inset-block-start: 1.15rem;
  inset-inline-end: 1.15rem;
  z-index: 8;
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

.gm-11__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-11__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-11__theme:hover {
  scale: 1.06;
}

.gm-11__sr:focus-visible + .gm-11__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-11__moon {
  display: none;
}

.gm-11__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,5vw,4rem);
}

.gm-11__card {
  position: relative;
  inline-size: min(34rem,100%);
  display: grid;
  gap: 1.15rem;
  padding: clamp(1.4rem,3vw,2.1rem);
  border-radius: 1.75rem;
  background: rgba(255,255,255,.16);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2), 0 34px 70px -32px rgba(0,0,0,.7);
  transition: translate .3s cubic-bezier(.2,.7,.3,1), box-shadow .3s ease;
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-11__card {
    background: color-mix(in oklab, var(--tint) 16%, transparent);
  }
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-11__card {
    -webkit-backdrop-filter: blur(24px) saturate(180%);
    backdrop-filter: blur(24px) saturate(180%);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-11__card {
    background: rgba(20,14,46,.9);
  }
}

.gm-11__card::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  pointer-events: none;
  background: linear-gradient(146deg, rgba(255,255,255,.14), transparent 44%);
}

.gm-11__card:hover {
  translate: 0 -6px;
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2), 0 44px 84px -32px rgba(0,0,0,.75);
}

.gm-11__top {
  position: relative;
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.gm-11__photo {
  inline-size: 4.5rem;
  block-size: 4.5rem;
  border-radius: 1.15rem;
  object-fit: cover;
  flex: none;
  background: rgba(255,255,255,.12);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim2), 0 12px 26px -16px rgba(0,0,0,.7);
}

.gm-11__ident {
  display: grid;
  gap: .15rem;
  min-inline-size: 0;
}

.gm-11__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-11__h {
  margin: 0;
  font-size: clamp(1.45rem,3vw,1.9rem);
  font-weight: 600;
  letter-spacing: -.03em;
  line-height: 1.1;
}

.gm-11__role {
  margin: 0;
  font-size: .9rem;
  color: var(--muted);
}

.gm-11__badge {
  margin-inline-start: auto;
  padding: .32rem .6rem;
  border-radius: .55rem;
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  background: rgba(255,255,255,.16);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim2);
}

.gm-11__copy {
  margin: 0;
  position: relative;
  font-size: 1rem;
  line-height: 1.6;
  color: var(--ink);
  opacity: .88;
  text-wrap: pretty;
}

.gm-11__stats {
  list-style: none;
  margin: 0;
  padding: 1rem 0 0;
  position: relative;
  border-block-start: 1px solid var(--rim2);
  display: flex;
  flex-wrap: wrap;
  gap: 1.6rem;
}

.gm-11__stats li {
  display: grid;
  gap: .15rem;
}

.gm-11__snum {
  font-family: var(--mono);
  font-size: 1.15rem;
  font-weight: 500;
  font-variant-numeric: tabular-nums;
  letter-spacing: -.01em;
}

.gm-11__slabel {
  font-family: var(--mono);
  font-size: .62rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-11__actions {
  position: relative;
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
}

.gm-11__cta,
.gm-11__ghost {
  min-block-size: 2.75rem;
  padding: .75rem 1.2rem;
  border-radius: .9rem;
  cursor: pointer;
  font: inherit;
  font-size: .94rem;
  font-weight: 500;
  transition: translate .18s ease, background .18s ease;
}

.gm-11__cta {
  color: #160c2c;
  background: var(--accent);
  border: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5), 0 14px 30px -16px rgba(0,0,0,.7);
}

.gm-11__ghost {
  color: var(--ink);
  background: rgba(255,255,255,.12);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(12px);
  backdrop-filter: blur(12px);
  box-shadow: inset 0 1px 0 var(--rim2);
}

.gm-11__cta:hover,
.gm-11__ghost:hover {
  translate: 0 -2px;
}

.gm-11__cta:focus-visible,
.gm-11__ghost:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-11__spec {
  margin: 0;
  position: relative;
  padding-block-start: .9rem;
  border-block-start: 1px solid var(--rim2);
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .02em;
  line-height: 1.6;
  color: var(--muted);
  overflow-wrap: anywhere;
}

.gm-11[data-theme="light"],
.gm-11:has(#gm-11-theme:checked) {
  --a1: rgba(168,85,247,.6);
  --a2: rgba(34,211,238,.55);
  --a3: rgba(251,113,133,.5);
  --a4: rgba(250,204,21,.35);
  --base: #06070f;
  --base2: #170f33;
  --ink: #f9fafe;
  --muted: rgba(249,250,254,.72);
  --rim: rgba(255,255,255,.5);
  --rim2: rgba(255,255,255,.15);
  --edge: rgba(255,255,255,.2);
  --accent: #c4b5fd;
}

.gm-11:has(#gm-11-theme:checked) .gm-11__sun {
  display: none;
}

.gm-11:has(#gm-11-theme:checked) .gm-11__moon {
  display: block;
}

.gm-11[data-theme="light"] .gm-11__cta,
.gm-11:has(#gm-11-theme:checked) .gm-11__cta {
  color: #fff;
}

@media (prefers-reduced-motion: reduce) {
  .gm-11 *,
    .gm-11 *::before,
    .gm-11 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .gm-11__card,
    .gm-11__cta,
    .gm-11__ghost,
    .gm-11__theme,
    .gm-11__badge {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }

  .gm-11__card::before {
    display: none;
  }
}
```
