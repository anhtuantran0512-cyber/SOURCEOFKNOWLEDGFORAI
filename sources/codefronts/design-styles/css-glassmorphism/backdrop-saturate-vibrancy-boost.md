---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/backdrop-saturate-vibrancy-boost/"
title: "Backdrop Saturate Vibrancy Boost"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "Blur alone gives you grey glass."
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Backdrop Saturate Vibrancy Boost
Source: https://codefronts.com/design-styles/css-glassmorphism/backdrop-saturate-vibrancy-boost/

Blur alone gives you grey glass. Three panels — blur(20px) with no saturate, with saturate(140%) and with saturate(180%) — show why every Apple material pairs the two: saturation puts back the chroma that averaging pixels takes away. The right-hand panel visibly lifts the magenta and cyan out of the mesh behind it.
## HTML
```html
<div class="gm-02">
  <input class="gm-02__sr" type="checkbox" id="gm-02-theme">
  <label class="gm-02__theme" for="gm-02-theme" title="Switch theme">
    <svg class="gm-02__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-02__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-02__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-02__stage">
    <section class="gm-02__wrap" aria-labelledby="gm-02-h">
      <header class="gm-02__head">
        <p class="gm-02__eyebrow">backdrop-filter · saturate()</p>
        <h2 class="gm-02__h" id="gm-02-h">Vibrancy is saturate, not blur</h2>
        <p class="gm-02__sub">Same 20px blur in all three. Only the saturate multiplier changes — and it is the difference between grey frosting and an Apple material.</p>
      </header>

      <ul class="gm-02__grid">
        <li class="gm-02__panel gm-02__panel--a">
          <div class="gm-02__top">
            <p class="gm-02__pill">saturate(100%)</p>
            <p class="gm-02__flag">baseline</p>
          </div>
          <h3 class="gm-02__tier">Blur only</h3>
          <p class="gm-02__copy">Averaging pixels pulls colour toward the local mean. The mesh behind this panel loses its magenta and reads slightly muddy.</p>
          <div class="gm-02__chips" aria-hidden="true"><span class="gm-02__chip gm-02__chip--v"></span><span class="gm-02__chip gm-02__chip--c"></span><span class="gm-02__chip gm-02__chip--p"></span></div>
          <p class="gm-02__meta">blur(20px) · no chroma recovery</p>
        </li>
        <li class="gm-02__panel gm-02__panel--b">
          <div class="gm-02__top">
            <p class="gm-02__pill">saturate(140%)</p>
            <p class="gm-02__flag gm-02__flag--ok">product default</p>
          </div>
          <h3 class="gm-02__tier">Natural lift</h3>
          <p class="gm-02__copy">Chroma comes back without going synthetic. This is the value that survives photography, dark mode and a colour-blindness sim.</p>
          <div class="gm-02__chips" aria-hidden="true"><span class="gm-02__chip gm-02__chip--v"></span><span class="gm-02__chip gm-02__chip--c"></span><span class="gm-02__chip gm-02__chip--p"></span></div>
          <p class="gm-02__meta">blur(20px) saturate(140%)</p>
        </li>
        <li class="gm-02__panel gm-02__panel--c">
          <div class="gm-02__top">
            <p class="gm-02__pill">saturate(180%)</p>
            <p class="gm-02__flag gm-02__flag--hot">vibrant material</p>
          </div>
          <h3 class="gm-02__tier">iOS vibrancy</h3>
          <p class="gm-02__copy">The Big Sur and iOS 26 chrome value. Colour bleeds up through the glass — dramatic on gradients, risky over faces.</p>
          <div class="gm-02__chips" aria-hidden="true"><span class="gm-02__chip gm-02__chip--v"></span><span class="gm-02__chip gm-02__chip--c"></span><span class="gm-02__chip gm-02__chip--p"></span></div>
          <p class="gm-02__meta">blur(20px) saturate(180%)</p>
        </li>
      </ul>

      <p class="gm-02__foot"><span class="gm-02__code">blur() saturate()</span> in that order. Reverse them and the boost is averaged away before you see it.</p>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-02 {
  --a1: rgba(236,72,153,.6);
  --a2: rgba(34,211,238,.55);
  --a3: rgba(251,191,36,.45);
  --a4: rgba(129,140,248,.5);
  --base: #07091a;
  --base2: #180d2e;
  --ink: #f8f9fe;
  --muted: rgba(248,249,254,.68);
  --tint: #ffffff;
  --rim: rgba(255,255,255,.5);
  --rim2: rgba(255,255,255,.14);
  --edge: rgba(255,255,255,.18);
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
  background: radial-gradient(52% 44% at 8% 22%, var(--a1) 0%, transparent 60%), radial-gradient(46% 40% at 92% 16%, var(--a2) 0%, transparent 58%), radial-gradient(46% 44% at 68% 92%, var(--a3) 0%, transparent 60%), radial-gradient(52% 46% at 30% 86%, var(--a4) 0%, transparent 62%), linear-gradient(155deg, var(--base) 0%, var(--base2) 50%, var(--base) 100%);
}

.gm-02 *,
.gm-02 *::before,
.gm-02 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-02 {
    --a1: oklch(0.7 0.25 350 / .62);
    --a2: oklch(0.82 0.16 200 / .56);
    --a3: oklch(0.85 0.17 85 / .48);
    --a4: oklch(0.68 0.19 280 / .52);
    --base: oklch(0.15 0.035 280);
    --base2: oklch(0.23 0.1 300);
    --ink: oklch(0.98 0.004 285);
    --muted: oklch(0.98 0.004 285 / .68);
  }
}

.gm-02__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-02__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-02__theme {
  position: absolute;
  inset-block-start: 1.15rem;
  inset-inline-end: 1.15rem;
  z-index: 6;
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

.gm-02__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-02__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-02__theme:hover {
  scale: 1.06;
}

.gm-02__sr:focus-visible + .gm-02__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-02__moon {
  display: none;
}

.gm-02__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3.5rem);
}

.gm-02__wrap {
  inline-size: min(72rem,100%);
}

.gm-02__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 44rem;
  margin-block-end: clamp(1.5rem,3.5vw,2.5rem);
}

.gm-02__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-02__h {
  margin: 0;
  font-size: clamp(1.85rem,4.4vw,2.9rem);
  font-weight: 600;
  letter-spacing: -.03em;
  line-height: 1.05;
  text-wrap: balance;
}

.gm-02__sub {
  margin: 0;
  font-size: clamp(.95rem,1.4vw,1.05rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-02__grid {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(1rem,2vw,1.5rem);
  grid-template-columns: repeat(auto-fit,minmax(16rem,1fr));
}

.gm-02__panel {
  --sat: 100%;
  display: flex;
  flex-direction: column;
  gap: .6rem;
  padding: clamp(1.15rem,2vw,1.6rem);
  border-radius: 1.35rem;
  background: rgba(255,255,255,.1);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2), 0 28px 60px -26px rgba(0,0,0,.65);
  transition: translate .25s cubic-bezier(.2,.7,.3,1);
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-02__panel {
    background: color-mix(in oklab, var(--tint) 15%, transparent);
  }
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-02__panel {
    -webkit-backdrop-filter: blur(20px) saturate(var(--sat));
    backdrop-filter: blur(20px) saturate(var(--sat));
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-02__panel {
    background: rgba(20,14,40,.82);
  }
}

.gm-02__panel--a {
  --sat: 100%;
}

.gm-02__panel--b {
  --sat: 140%;
}

.gm-02__panel--c {
  --sat: 180%;
}

.gm-02__panel:hover {
  translate: 0 -4px;
}

.gm-02__top {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .5rem;
}

.gm-02__pill {
  margin: 0;
  padding: .32rem .6rem;
  border-radius: .55rem;
  font-family: var(--mono);
  font-size: .74rem;
  font-variant-numeric: tabular-nums;
  background: rgba(255,255,255,.16);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim2);
}

.gm-02__flag {
  margin: 0;
  font-size: .68rem;
  font-weight: 500;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-02__flag--ok {
  color: #7ff0c0;
}

.gm-02__flag--hot {
  color: #ffb3e6;
}

.gm-02__tier {
  margin: .15rem 0 0;
  font-size: 1.15rem;
  font-weight: 600;
  letter-spacing: -.015em;
}

.gm-02__copy {
  margin: 0;
  font-size: .92rem;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-02__chips {
  display: flex;
  gap: .4rem;
  margin-block-start: .35rem;
}

.gm-02__chip {
  inline-size: 2.6rem;
  block-size: 1.5rem;
  border-radius: .45rem;
  border: 1px solid var(--rim2);
  box-shadow: inset 0 1px 0 var(--rim2);
}

.gm-02__chip--v {
  background: rgba(236,72,153,.85);
}

.gm-02__chip--c {
  background: rgba(34,211,238,.85);
}

.gm-02__chip--p {
  background: rgba(129,140,248,.85);
}

.gm-02__panel--a .gm-02__chip {
  filter: saturate(100%);
}

.gm-02__panel--b .gm-02__chip {
  filter: saturate(140%);
}

.gm-02__panel--c .gm-02__chip {
  filter: saturate(180%);
}

.gm-02__meta {
  margin: auto 0 0;
  padding-block-start: .7rem;
  border-block-start: 1px solid var(--rim2);
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .04em;
  color: var(--muted);
}

.gm-02__foot {
  margin: clamp(1.1rem,2vw,1.6rem) 0 0;
  font-size: .9rem;
  color: var(--muted);
}

.gm-02__code {
  font-family: var(--mono);
  font-size: .82rem;
  padding: .2rem .45rem;
  border-radius: .4rem;
  background: rgba(255,255,255,.12);
  border: 1px solid var(--edge);
  color: var(--ink);
}

.gm-02[data-theme="light"],
.gm-02:has(#gm-02-theme:checked) {
  --a1: rgba(244,114,182,.5);
  --a2: rgba(103,232,249,.5);
  --a3: rgba(253,224,71,.5);
  --a4: rgba(165,180,252,.5);
  --base: #f1f3fa;
  --base2: #e3e9fd;
  --ink: #111220;
  --muted: rgba(17,18,32,.66);
  --rim: rgba(255,255,255,.9);
  --rim2: rgba(255,255,255,.45);
  --edge: rgba(17,18,32,.1);
}

.gm-02:has(#gm-02-theme:checked) .gm-02__sun {
  display: none;
}

.gm-02:has(#gm-02-theme:checked) .gm-02__moon {
  display: block;
}

.gm-02[data-theme="light"] .gm-02__flag--ok,
.gm-02:has(#gm-02-theme:checked) .gm-02__flag--ok {
  color: #047857;
}

.gm-02[data-theme="light"] .gm-02__flag--hot,
.gm-02:has(#gm-02-theme:checked) .gm-02__flag--hot {
  color: #a21caf;
}

@media (prefers-reduced-motion: reduce) {
  .gm-02 *,
    .gm-02 *::before,
    .gm-02 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .gm-02__panel,
    .gm-02__theme,
    .gm-02__pill {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }
}
```
