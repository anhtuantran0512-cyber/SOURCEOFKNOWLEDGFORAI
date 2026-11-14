---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/glass-toggle/"
title: "Frosted Glass Toggle Switch"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "A switch where both the track and the thumb are glass, so the thumb refracts the track it slides over."
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Frosted Glass Toggle Switch
Source: https://codefronts.com/design-styles/css-glassmorphism/glass-toggle/

A switch where both the track and the thumb are glass, so the thumb refracts the track it slides over. Built on a real <input type="checkbox" role="switch"> with the :checked sibling combinator — no JavaScript, correct semantics, and a 44px hit area on every row.
## HTML
```html
<div class="gm-18">
  <input class="gm-18__sr" type="checkbox" id="gm-18-theme">
  <label class="gm-18__theme" for="gm-18-theme" title="Switch theme">
    <svg class="gm-18__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-18__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-18__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-18__stage">
    <section class="gm-18__card" aria-labelledby="gm-18-h">
      <header class="gm-18__head">
        <p class="gm-18__eyebrow">role=&quot;switch&quot; · :checked</p>
        <h2 class="gm-18__h" id="gm-18-h">Edge settings</h2>
        <p class="gm-18__sub">Track and thumb are both frosted, so the thumb refracts the rail it slides along.</p>
      </header>

      <ul class="gm-18__rows">
        <li class="gm-18__row">
          <input class="gm-18__input" type="checkbox" role="switch" id="gm-18-a" checked>
          <label class="gm-18__label" for="gm-18-a">
            <span class="gm-18__ltext"><span class="gm-18__lname">Edge caching</span><span class="gm-18__ldesc">Serve static assets from 34 regions</span></span>
            <span class="gm-18__track" aria-hidden="true"><span class="gm-18__thumb"></span></span>
          </label>
        </li>
        <li class="gm-18__row">
          <input class="gm-18__input" type="checkbox" role="switch" id="gm-18-b">
          <label class="gm-18__label" for="gm-18-b">
            <span class="gm-18__ltext"><span class="gm-18__lname">Preview comments</span><span class="gm-18__ldesc">Let reviewers annotate deploy previews</span></span>
            <span class="gm-18__track" aria-hidden="true"><span class="gm-18__thumb"></span></span>
          </label>
        </li>
        <li class="gm-18__row">
          <input class="gm-18__input" type="checkbox" role="switch" id="gm-18-c" checked>
          <label class="gm-18__label" for="gm-18-c">
            <span class="gm-18__ltext"><span class="gm-18__lname">Reduced transparency</span><span class="gm-18__ldesc">Swap glass surfaces for opaque fills</span></span>
            <span class="gm-18__track" aria-hidden="true"><span class="gm-18__thumb"></span></span>
          </label>
        </li>
        <li class="gm-18__row gm-18__row--sm">
          <input class="gm-18__input" type="checkbox" role="switch" id="gm-18-d">
          <label class="gm-18__label" for="gm-18-d">
            <span class="gm-18__ltext"><span class="gm-18__lname">Compact switch</span><span class="gm-18__ldesc">Same recipe at a smaller --h token</span></span>
            <span class="gm-18__track" aria-hidden="true"><span class="gm-18__thumb"></span></span>
          </label>
        </li>
      </ul>

      <p class="gm-18__foot">One token drives the size: <span class="gm-18__code">--h</span> sets the track height and the thumb travel derives from it.</p>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-18 {
  --a1: rgba(45,212,191,.5);
  --a2: rgba(129,140,248,.6);
  --a3: rgba(251,113,133,.45);
  --a4: rgba(250,204,21,.35);
  --base: #05070f;
  --base2: #121533;
  --ink: #f9fafe;
  --muted: rgba(249,250,254,.68);
  --tint: #ffffff;
  --accent: #5eead4;
  --rim: rgba(255,255,255,.5);
  --rim2: rgba(255,255,255,.14);
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
  background: radial-gradient(50% 42% at 10% 18%, var(--a1) 0%, transparent 58%), radial-gradient(54% 46% at 86% 14%, var(--a2) 0%, transparent 62%), radial-gradient(46% 40% at 82% 88%, var(--a3) 0%, transparent 58%), radial-gradient(42% 36% at 16% 90%, var(--a4) 0%, transparent 58%), linear-gradient(160deg, var(--base) 0%, var(--base2) 52%, var(--base) 100%);
}

.gm-18 *,
.gm-18 *::before,
.gm-18 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-18 {
    --a1: oklch(0.82 0.15 178 / .52);
    --a2: oklch(0.68 0.19 280 / .62);
    --a3: oklch(0.72 0.19 15 / .46);
    --a4: oklch(0.88 0.16 95 / .36);
    --base: oklch(0.13 0.025 272);
    --base2: oklch(0.23 0.09 280);
    --accent: oklch(0.86 0.13 175);
  }
}

.gm-18__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-18__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-18__theme {
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

.gm-18__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-18__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-18__theme:hover {
  scale: 1.06;
}

.gm-18__sr:focus-visible + .gm-18__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-18__moon {
  display: none;
}

.gm-18__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3.5rem);
}

.gm-18__card {
  inline-size: min(34rem,100%);
  display: grid;
  gap: 1.25rem;
  padding: clamp(1.4rem,3vw,2rem);
  border-radius: 1.75rem;
  background: rgba(255,255,255,.14);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(26px) saturate(175%);
  backdrop-filter: blur(26px) saturate(175%);
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2), 0 34px 74px -32px rgba(0,0,0,.7);
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-18__card {
    background: color-mix(in oklab, var(--tint) 14%, transparent);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-18__card {
    background: rgba(16,16,42,.92);
  }
}

.gm-18__head {
  display: grid;
  gap: .35rem;
}

.gm-18__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-18__h {
  margin: 0;
  font-size: clamp(1.5rem,3.2vw,2rem);
  font-weight: 600;
  letter-spacing: -.03em;
  line-height: 1.1;
}

.gm-18__sub {
  margin: 0;
  font-size: .94rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-18__rows {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .35rem;
}

.gm-18__row {
  --h: 1.7rem;
}

.gm-18__row--sm {
  --h: 1.3rem;
}

.gm-18__input {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-18__label {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  min-block-size: 2.75rem;
  padding: .7rem .25rem;
  cursor: pointer;
  border-block-end: 1px solid var(--rim2);
}

.gm-18__row:last-child .gm-18__label {
  border-block-end: 0;
}

.gm-18__ltext {
  display: grid;
  gap: .1rem;
  min-inline-size: 0;
}

.gm-18__lname {
  font-size: .96rem;
  font-weight: 500;
  letter-spacing: -.01em;
}

.gm-18__ldesc {
  font-size: .8rem;
  line-height: 1.4;
  color: var(--muted);
}

.gm-18__track {
  position: relative;
  flex: none;
  inline-size: calc(var(--h) * 1.85);
  block-size: var(--h);
  border-radius: 999px;
  background: rgba(255,255,255,.12);
  border: 1px solid var(--edge);
  box-shadow: inset 0 2px 5px rgba(0,0,0,.34);
  transition: background .22s ease, border-color .22s ease;
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-18__track {
    background: color-mix(in oklab, var(--tint) 12%, transparent);
  }
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-18__track {
    -webkit-backdrop-filter: blur(14px) saturate(160%);
    backdrop-filter: blur(14px) saturate(160%);
  }
}

.gm-18__thumb {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: .15rem;
  inline-size: calc(var(--h) - .4rem);
  block-size: calc(var(--h) - .4rem);
  border-radius: 999px;
  translate: 0 -50%;
  background: rgba(255,255,255,.46);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.75), 0 3px 8px rgba(0,0,0,.4);
  transition: translate .26s cubic-bezier(.34,1.4,.5,1), background .22s ease;
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-18__thumb {
    background: color-mix(in oklab, var(--tint) 46%, transparent);
  }
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-18__thumb {
    -webkit-backdrop-filter: blur(10px) saturate(180%);
    backdrop-filter: blur(10px) saturate(180%);
  }
}

.gm-18__input:checked ~ .gm-18__label .gm-18__track,
.gm-18__input:checked + .gm-18__label .gm-18__track {
  background: rgba(94,234,212,.42);
  border-color: rgba(94,234,212,.5);
}

@supports (background: color-mix(in oklab, red 10%, transparent)) {
  .gm-18__input:checked + .gm-18__label .gm-18__track {
    background: color-mix(in oklab, var(--accent) 42%, transparent);
  }
}

.gm-18__input:checked + .gm-18__label .gm-18__thumb {
  translate: calc(var(--h) * .85) -50%;
  background: rgba(255,255,255,.9);
}

.gm-18__input:focus-visible + .gm-18__label .gm-18__track {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-18__label:hover .gm-18__track {
  border-color: rgba(255,255,255,.4);
}

.gm-18__foot {
  margin: 0;
  font-size: .85rem;
  color: var(--muted);
}

.gm-18__code {
  font-family: var(--mono);
  font-size: .78rem;
  padding: .12rem .36rem;
  border-radius: .35rem;
  background: rgba(255,255,255,.12);
  border: 1px solid var(--rim2);
  color: var(--ink);
}

.gm-18[data-theme="light"],
.gm-18:has(#gm-18-theme:checked) {
  --a1: rgba(153,246,228,.5);
  --a2: rgba(165,180,252,.6);
  --a3: rgba(253,164,175,.5);
  --a4: rgba(254,240,138,.5);
  --base: #f0f3fb;
  --base2: #e3e7fc;
  --ink: #0f1120;
  --muted: rgba(15,17,32,.68);
  --rim: rgba(255,255,255,.95);
  --rim2: rgba(255,255,255,.5);
  --edge: rgba(15,17,32,.14);
  --accent: #0d9488;
}

.gm-18:has(#gm-18-theme:checked) .gm-18__sun {
  display: none;
}

.gm-18:has(#gm-18-theme:checked) .gm-18__moon {
  display: block;
}

.gm-18[data-theme="light"] .gm-18__track,
.gm-18:has(#gm-18-theme:checked) .gm-18__track {
  box-shadow: inset 0 2px 4px rgba(16,20,45,.16);
}

.gm-18[data-theme="light"] .gm-18__thumb,
.gm-18:has(#gm-18-theme:checked) .gm-18__thumb {
  background: rgba(255,255,255,.95);
  box-shadow: inset 0 1px 0 #fff, 0 2px 6px rgba(16,20,45,.3);
}

@media (prefers-reduced-motion: reduce) {
  .gm-18 *,
    .gm-18 *::before,
    .gm-18 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .gm-18__card,
    .gm-18__track,
    .gm-18__theme {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }

  .gm-18__input:checked + .gm-18__label .gm-18__track {
    background: Highlight;
  }

  .gm-18__thumb {
    background: CanvasText;
  }
}
```
