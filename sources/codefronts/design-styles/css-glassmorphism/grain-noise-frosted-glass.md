---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/grain-noise-frosted-glass/"
title: "Grain Noise Frosted Glass"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "The difference between glass and plastic is grain."
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Grain Noise Frosted Glass
Source: https://codefronts.com/design-styles/css-glassmorphism/grain-noise-frosted-glass/

The difference between glass and plastic is grain. Two otherwise identical frosted panels sit side by side — one over a clean gradient, one over the same gradient plus a fine feTurbulence noise layer — and the grainy one reads as physical etched glass while the clean one looks like a smudge filter.
## HTML
```html
<div class="gm-06">
  <svg class="gm-06__defs" aria-hidden="true" focusable="false">
    <filter id="gm-06-grain" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" stitchTiles="stitch" seed="11"/>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
    <filter id="gm-06-grain-fine" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="1.6" numOctaves="2" stitchTiles="stitch" seed="4"/>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
  </svg>

  <input class="gm-06__sr" type="checkbox" id="gm-06-theme">
  <label class="gm-06__theme" for="gm-06-theme" title="Switch theme">
    <svg class="gm-06__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-06__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-06__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-06__stage">
    <section class="gm-06__wrap" aria-labelledby="gm-06-h">
      <header class="gm-06__head">
        <p class="gm-06__eyebrow">feTurbulence · fractalNoise</p>
        <h2 class="gm-06__h" id="gm-06-h">Grain is what makes frost believable</h2>
        <p class="gm-06__sub">Identical panels, identical blur. The right-hand half has a noise layer under the glass — that is the entire difference between etched glass and a smudge.</p>
      </header>

      <div class="gm-06__compare">
        <article class="gm-06__side">
          <div class="gm-06__panel">
            <p class="gm-06__pill">no noise</p>
            <h3 class="gm-06__title">Clean gradient</h3>
            <p class="gm-06__copy">The blur has nothing but a smooth ramp to average, so the frost flattens into a plastic sheet. Look at the edge transition — it is too perfect.</p>
            <p class="gm-06__meta">blur(24px) saturate(160%)</p>
          </div>
        </article>
        <article class="gm-06__side gm-06__side--noise">
          <div class="gm-06__noise" aria-hidden="true"></div>
          <div class="gm-06__panel gm-06__panel--grain">
            <p class="gm-06__pill">baseFrequency 0.9</p>
            <h3 class="gm-06__title">Etched glass</h3>
            <p class="gm-06__copy">Same blur, but now it is averaging real high-frequency detail. The surface scatters light unevenly — which is what physical frost actually does.</p>
            <p class="gm-06__meta">+ under-noise 50% · surface grain 8%</p>
          </div>
        </article>
      </div>

      <p class="gm-06__foot">Two layers do the work: coarse noise <em>under</em> the glass for the blur to sample, fine noise <em>over</em> it at 8% with <span class="gm-06__code">mix-blend-mode: overlay</span> for the surface itself.</p>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-06 {
  --a1: rgba(253,186,116,.55);
  --a2: rgba(196,181,253,.55);
  --a3: rgba(125,211,252,.5);
  --a4: rgba(249,168,212,.5);
  --base: #f4f1ec;
  --base2: #e6e3f7;
  --ink: #141118;
  --muted: rgba(20,17,24,.68);
  --tint: #ffffff;
  --rim: rgba(255,255,255,.95);
  --rim2: rgba(255,255,255,.5);
  --edge: rgba(20,17,24,.1);
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
  background: radial-gradient(52% 44% at 14% 20%, var(--a1) 0%, transparent 60%), radial-gradient(52% 44% at 86% 14%, var(--a2) 0%, transparent 60%), radial-gradient(48% 42% at 78% 88%, var(--a3) 0%, transparent 60%), radial-gradient(46% 40% at 18% 90%, var(--a4) 0%, transparent 58%), linear-gradient(160deg, var(--base) 0%, var(--base2) 52%, var(--base) 100%);
}

.gm-06 *,
.gm-06 *::before,
.gm-06 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-06 {
    --a1: oklch(0.78 0.17 55 / .56);
    --a2: oklch(0.68 0.24 305 / .56);
    --a3: oklch(0.7 0.17 235 / .52);
    --a4: oklch(0.7 0.24 350 / .46);
    --base: oklch(0.97 0.008 275);
    --base2: oklch(0.93 0.015 285);
  }
}

.gm-06__defs {
  position: absolute;
  inline-size: 0;
  block-size: 0;
  overflow: hidden;
}

.gm-06__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-06__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-06__theme {
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

.gm-06__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-06__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-06__theme:hover {
  scale: 1.06;
}

.gm-06__sr:focus-visible + .gm-06__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-06__moon {
  display: none;
}

.gm-06__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3.5rem);
}

.gm-06__wrap {
  inline-size: min(74rem,100%);
}

.gm-06__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 44rem;
  margin-block-end: clamp(1.5rem,3.5vw,2.5rem);
}

.gm-06__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-06__h {
  margin: 0;
  font-size: clamp(1.85rem,4.4vw,2.9rem);
  font-weight: 600;
  letter-spacing: -.03em;
  line-height: 1.05;
  text-wrap: balance;
}

.gm-06__sub {
  margin: 0;
  font-size: clamp(.95rem,1.4vw,1.05rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-06__compare {
  display: grid;
  gap: clamp(1rem,2vw,1.5rem);
  grid-template-columns: repeat(auto-fit,minmax(17rem,1fr));
}

.gm-06__side {
  position: relative;
  isolation: isolate;
  padding: clamp(1.1rem,2vw,1.6rem);
  border-radius: 1.5rem;
  overflow: hidden;
  border: 1px solid var(--edge);
  background: rgba(255,255,255,.03);
}

.gm-06__noise {
  position: absolute;
  inset: -10%;
  z-index: 0;
  pointer-events: none;
  filter: url(#gm-06-grain);
  opacity: .5;
}

.gm-06__panel {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  gap: .55rem;
  padding: clamp(1.1rem,1.9vw,1.5rem);
  border-radius: 1.2rem;
  border: 1px solid var(--edge);
  background: rgba(255,255,255,.11);
  -webkit-backdrop-filter: blur(24px) saturate(160%);
  backdrop-filter: blur(24px) saturate(160%);
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2), 0 26px 56px -26px rgba(0,0,0,.6);
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-06__panel {
    background: color-mix(in oklab, var(--tint) 14%, transparent);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-06__panel {
    background: rgba(22,14,44,.86);
  }
}

.gm-06__panel--grain::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  pointer-events: none;
  filter: url(#gm-06-grain-fine);
  opacity: .08;
  mix-blend-mode: overlay;
}

.gm-06__pill {
  margin: 0;
  align-self: flex-start;
  padding: .3rem .58rem;
  border-radius: .5rem;
  font-family: var(--mono);
  font-size: .7rem;
  font-variant-numeric: tabular-nums;
  background: rgba(255,255,255,.16);
  border: 1px solid var(--edge);
}

.gm-06__title {
  margin: .2rem 0 0;
  font-size: clamp(1.2rem,2.1vw,1.5rem);
  font-weight: 600;
  letter-spacing: -.02em;
}

.gm-06__copy {
  margin: 0;
  font-size: .93rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-06__meta {
  margin: .3rem 0 0;
  padding-block-start: .7rem;
  border-block-start: 1px solid var(--rim2);
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .04em;
  color: var(--muted);
}

.gm-06__foot {
  margin: clamp(1.1rem,2vw,1.6rem) 0 0;
  max-inline-size: 46rem;
  font-size: .9rem;
  line-height: 1.55;
  color: var(--muted);
}

.gm-06__code {
  font-family: var(--mono);
  font-size: .8rem;
  padding: .12rem .38rem;
  border-radius: .35rem;
  background: rgba(255,255,255,.12);
  border: 1px solid var(--edge);
  color: var(--ink);
}

.gm-06[data-theme="light"],
.gm-06:has(#gm-06-theme:checked) {
  --a1: rgba(251,146,60,.55);
  --a2: rgba(168,85,247,.55);
  --a3: rgba(14,165,233,.5);
  --a4: rgba(236,72,153,.45);
  --base: #08070f;
  --base2: #1d1030;
  --ink: #fbf9f7;
  --muted: rgba(251,249,247,.7);
  --rim: rgba(255,255,255,.5);
  --rim2: rgba(255,255,255,.14);
  --edge: rgba(255,255,255,.2);
}

.gm-06:has(#gm-06-theme:checked) .gm-06__sun {
  display: none;
}

.gm-06:has(#gm-06-theme:checked) .gm-06__moon {
  display: block;
}

.gm-06[data-theme="light"] .gm-06__noise,
.gm-06:has(#gm-06-theme:checked) .gm-06__noise {
  opacity: .38;
  mix-blend-mode: multiply;
}

@media (prefers-reduced-motion: reduce) {
  .gm-06 *,
    .gm-06 *::before,
    .gm-06 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .gm-06__panel,
    .gm-06__side,
    .gm-06__theme,
    .gm-06__pill {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }

  .gm-06__noise,
    .gm-06__panel--grain::after {
    display: none;
  }
}
```
