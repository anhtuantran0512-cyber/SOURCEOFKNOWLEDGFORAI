---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/visionos-depth-layer-stack/"
title: "visionOS Depth Layer Stack"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "Four glass sheets stacked front-to-back with rising blur (12 → 16 → 20 → 24px) and falling opacity, each offset a few pixels so the stack reads as physical…"
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: visionOS Depth Layer Stack
Source: https://codefronts.com/design-styles/css-glassmorphism/visionos-depth-layer-stack/

Four glass sheets stacked front-to-back with rising blur (12 → 16 → 20 → 24px) and falling opacity, each offset a few pixels so the stack reads as physical depth. This is the visionOS rule in one surface: depth is communicated by looking through layers, not by drop shadows — each sheet refracts the sheets behind it.
## HTML
```html
<div class="gm-03">
  <input class="gm-03__sr" type="checkbox" id="gm-03-theme">
  <label class="gm-03__theme" for="gm-03-theme" title="Switch theme">
    <svg class="gm-03__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-03__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-03__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-03__stage">
    <section class="gm-03__wrap" aria-labelledby="gm-03-h">
      <header class="gm-03__head">
        <p class="gm-03__eyebrow">spatial · glass on glass</p>
        <h2 class="gm-03__h" id="gm-03-h">Depth you read by looking through it</h2>
        <p class="gm-03__sub">Four sheets, blur rising and material thinning with distance. No drop shadow does the work — the front sheet refracts the ones behind it.</p>
      </header>

      <div class="gm-03__stack">
        <div class="gm-03__layer gm-03__layer--4" aria-hidden="true"><p class="gm-03__tag">blur 24px · α .09</p></div>
        <div class="gm-03__layer gm-03__layer--3" aria-hidden="true"><p class="gm-03__tag">blur 20px · α .12</p></div>
        <div class="gm-03__layer gm-03__layer--2" aria-hidden="true"><p class="gm-03__tag">blur 16px · α .16</p></div>
        <div class="gm-03__layer gm-03__layer--1">
          <p class="gm-03__tag">blur 12px · α .20</p>
          <h3 class="gm-03__title">Ambient Session</h3>
          <p class="gm-03__copy">Front sheet holds the content. Everything behind it exists to give the eye distance — and to prove the blur chain compounds.</p>
          <dl class="gm-03__specs">
            <div><dt>Layers</dt><dd>4</dd></div>
            <div><dt>Blur step</dt><dd>+4px</dd></div>
            <div><dt>Offset</dt><dd>1.35rem</dd></div>
          </dl>
        </div>
      </div>

      <p class="gm-03__foot">Hover the stack to parallax it — <span class="gm-03__code">translate</span> and <span class="gm-03__code">rotate</span> only, so the depth cue costs nothing on the main thread.</p>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-03 {
  --a1: rgba(99,102,241,.6);
  --a2: rgba(6,182,212,.5);
  --a3: rgba(217,70,239,.5);
  --a4: rgba(250,204,21,.35);
  --base: #060814;
  --base2: #101a3a;
  --ink: #f7f9ff;
  --muted: rgba(247,249,255,.68);
  --tint: #ffffff;
  --rim: rgba(255,255,255,.55);
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
  background: radial-gradient(56% 46% at 78% 14%, var(--a1) 0%, transparent 62%), radial-gradient(48% 42% at 14% 24%, var(--a2) 0%, transparent 60%), radial-gradient(52% 46% at 26% 88%, var(--a3) 0%, transparent 62%), radial-gradient(40% 34% at 88% 82%, var(--a4) 0%, transparent 58%), linear-gradient(168deg, var(--base) 0%, var(--base2) 55%, var(--base) 100%);
}

.gm-03 *,
.gm-03 *::before,
.gm-03 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-03 {
    --a1: oklch(0.62 0.22 275 / .62);
    --a2: oklch(0.78 0.15 205 / .52);
    --a3: oklch(0.68 0.25 325 / .5);
    --a4: oklch(0.88 0.16 95 / .36);
    --base: oklch(0.14 0.03 265);
    --base2: oklch(0.26 0.09 265);
    --ink: oklch(0.99 0.004 265);
    --muted: oklch(0.99 0.004 265 / .68);
  }
}

.gm-03__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-03__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-03__theme {
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

.gm-03__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-03__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-03__theme:hover {
  scale: 1.06;
}

.gm-03__sr:focus-visible + .gm-03__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-03__moon {
  display: none;
}

.gm-03__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3.5rem);
}

.gm-03__wrap {
  inline-size: min(60rem,100%);
  display: grid;
  justify-items: center;
  gap: clamp(1.5rem,4vw,2.75rem);
}

.gm-03__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 42rem;
  text-align: center;
  justify-items: center;
}

.gm-03__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-03__h {
  margin: 0;
  font-size: clamp(1.85rem,4.4vw,2.9rem);
  font-weight: 600;
  letter-spacing: -.03em;
  line-height: 1.05;
  text-wrap: balance;
}

.gm-03__sub {
  margin: 0;
  font-size: clamp(.95rem,1.4vw,1.05rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-03__stack {
  position: relative;
  inline-size: min(30rem,100%);
  min-block-size: 22rem;
  perspective: 1200px;
  transform-style: preserve-3d;
}

.gm-03__layer {
  --b: 12px;
  --al: .2;
  --i: 0;
  position: absolute;
  inset-block-start: 0;
  inset-inline-start: 0;
  inline-size: 100%;
  padding: clamp(1.1rem,2vw,1.6rem);
  border-radius: 1.5rem;
  border: 1px solid var(--edge);
  background: rgba(255,255,255,.16);
  translate: calc(var(--i) * 1.35rem) calc(var(--i) * -1.05rem);
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2), 0 30px 70px -30px rgba(0,0,0,.7);
  transition: translate .4s cubic-bezier(.2,.7,.3,1), rotate .4s cubic-bezier(.2,.7,.3,1);
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-03__layer {
    background: color-mix(in oklab, var(--tint) calc(var(--al) * 100%), transparent);
  }
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-03__layer {
    -webkit-backdrop-filter: blur(var(--b)) saturate(150%);
    backdrop-filter: blur(var(--b)) saturate(150%);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-03__layer {
    background: rgba(18,20,45,.72);
  }

  .gm-03__layer--1 {
    background: rgba(18,20,45,.9);
  }
}

.gm-03__layer--1 {
  --i: 0;
  --b: 12px;
  --al: .2;
  position: relative;
  z-index: 4;
  min-block-size: 16rem;
  display: flex;
  flex-direction: column;
  gap: .65rem;
}

.gm-03__layer--2 {
  --i: 1;
  --b: 16px;
  --al: .16;
  z-index: 3;
  block-size: 15rem;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.35), 0 24px 60px -32px rgba(0,0,0,.6);
}

.gm-03__layer--3 {
  --i: 2;
  --b: 20px;
  --al: .12;
  z-index: 2;
  block-size: 14rem;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.22), 0 20px 50px -34px rgba(0,0,0,.5);
}

.gm-03__layer--4 {
  --i: 3;
  --b: 24px;
  --al: .09;
  z-index: 1;
  block-size: 13rem;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.14);
}

.gm-03__stack:hover .gm-03__layer {
  rotate: -1.2deg;
}

.gm-03__stack:hover .gm-03__layer--2 {
  translate: calc(1.7rem) calc(-1.35rem);
}

.gm-03__stack:hover .gm-03__layer--3 {
  translate: calc(3.4rem) calc(-2.7rem);
}

.gm-03__stack:hover .gm-03__layer--4 {
  translate: calc(5.1rem) calc(-4.05rem);
}

.gm-03__tag {
  margin: 0;
  align-self: flex-start;
  padding: .28rem .55rem;
  border-radius: .5rem;
  font-family: var(--mono);
  font-size: .7rem;
  font-variant-numeric: tabular-nums;
  color: var(--ink);
  background: rgba(255,255,255,.16);
  border: 1px solid var(--edge);
}

.gm-03__layer--2 .gm-03__tag,
.gm-03__layer--3 .gm-03__tag,
.gm-03__layer--4 .gm-03__tag {
  position: absolute;
  inset-block-end: .85rem;
  inset-inline-end: .9rem;
  opacity: .65;
}

.gm-03__title {
  margin: .35rem 0 0;
  font-size: clamp(1.3rem,2.4vw,1.65rem);
  font-weight: 600;
  letter-spacing: -.02em;
}

.gm-03__copy {
  margin: 0;
  font-size: .94rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-03__specs {
  margin: auto 0 0;
  padding-block-start: .9rem;
  border-block-start: 1px solid var(--rim2);
  display: flex;
  flex-wrap: wrap;
  gap: 1.4rem;
}

.gm-03__specs div {
  display: grid;
  gap: .15rem;
}

.gm-03__specs dt {
  font-family: var(--mono);
  font-size: .64rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-03__specs dd {
  margin: 0;
  font-size: 1rem;
  font-weight: 600;
  font-variant-numeric: tabular-nums;
}

.gm-03__foot {
  margin: 0;
  max-inline-size: 36rem;
  text-align: center;
  font-size: .88rem;
  line-height: 1.5;
  color: var(--muted);
}

.gm-03__code {
  font-family: var(--mono);
  font-size: .8rem;
  padding: .15rem .4rem;
  border-radius: .4rem;
  background: rgba(255,255,255,.12);
  border: 1px solid var(--edge);
  color: var(--ink);
}

.gm-03[data-theme="light"],
.gm-03:has(#gm-03-theme:checked) {
  --a1: rgba(165,180,252,.55);
  --a2: rgba(103,232,249,.5);
  --a3: rgba(240,171,252,.5);
  --a4: rgba(254,240,138,.5);
  --base: #eef2fb;
  --base2: #dde7fb;
  --ink: #0f1220;
  --muted: rgba(15,18,32,.66);
  --rim: rgba(255,255,255,.95);
  --rim2: rgba(255,255,255,.5);
  --edge: rgba(15,18,32,.1);
}

.gm-03:has(#gm-03-theme:checked) .gm-03__sun {
  display: none;
}

.gm-03:has(#gm-03-theme:checked) .gm-03__moon {
  display: block;
}

@media (prefers-reduced-motion: reduce) {
  .gm-03 *,
    .gm-03 *::before,
    .gm-03 *::after {
    transition: none !important;
    animation: none !important;
  }

  .gm-03__stack:hover .gm-03__layer {
    rotate: none;
  }
}

@media (forced-colors: active) {
  .gm-03__layer,
    .gm-03__theme,
    .gm-03__tag {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }
}
```
