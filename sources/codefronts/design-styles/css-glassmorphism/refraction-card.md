---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/refraction-card/"
title: "Refractive Glass Card"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "The displacement technique from demo 05, applied as a real product card: avatar, heading, description, metadata and a CTA — sitting on a lens layer that…"
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Refractive Glass Card
Source: https://codefronts.com/design-styles/css-glassmorphism/refraction-card/

The displacement technique from demo 05, applied as a real product card: avatar, heading, description, metadata and a CTA — sitting on a lens layer that visibly warps the ruled background beneath it. Where demo 05 teaches the filter, this shows what it looks like carrying actual content.
## HTML
```html
<div class="gm-20">
  <svg class="gm-20__defs" aria-hidden="true" focusable="false">
    <filter id="gm-20-refract" x="-20%" y="-20%" width="140%" height="140%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.016" numOctaves="2" seed="12" result="n"/>
      <feGaussianBlur in="n" stdDeviation="1.2" result="s"/>
      <feDisplacementMap in="SourceGraphic" in2="s" scale="22" xChannelSelector="R" yChannelSelector="G"/>
    </filter>
    <filter id="gm-20-refract-hi" x="-25%" y="-25%" width="150%" height="150%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.019" numOctaves="2" seed="5" result="n"/>
      <feDisplacementMap in="SourceGraphic" in2="n" scale="40" xChannelSelector="R" yChannelSelector="B"/>
    </filter>
  </svg>

  <input class="gm-20__sr" type="checkbox" id="gm-20-theme">
  <label class="gm-20__theme" for="gm-20-theme" title="Switch theme">
    <svg class="gm-20__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-20__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-20__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-20__stage">
    <div class="gm-20__rules" aria-hidden="true"></div>
    <article class="gm-20__card" aria-labelledby="gm-20-h">
      <div class="gm-20__lens" aria-hidden="true"></div>
      <div class="gm-20__lens gm-20__lens--hi" aria-hidden="true"></div>
      <div class="gm-20__fringe" aria-hidden="true"></div>

      <div class="gm-20__body">
        <div class="gm-20__top">
          <img class="gm-20__avatar" src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=160&h=160&q=80" width="80" height="80" loading="lazy" decoding="async" alt="Portrait of Jordan Lee">
          <div class="gm-20__ident">
            <p class="gm-20__eyebrow">Refraction · scale 22</p>
            <h2 class="gm-20__h" id="gm-20-h">Jordan Lee</h2>
            <p class="gm-20__role">Rendering · Atlas Materials</p>
          </div>
        </div>

        <p class="gm-20__copy">Look at the rulings behind the card. They are perfectly straight — the bend at the edges is <code>feDisplacementMap</code> pushing the backdrop pixels sideways, not a blur pretending to be depth.</p>

        <dl class="gm-20__meta">
          <div><dt>baseFrequency</dt><dd>0.016</dd></div>
          <div><dt>octaves</dt><dd>2</dd></div>
          <div><dt>scale</dt><dd>22 → 40</dd></div>
        </dl>

        <div class="gm-20__actions">
          <button class="gm-20__cta" type="button">Open material</button>
          <button class="gm-20__ghost" type="button">Copy filter</button>
        </div>
      </div>
    </article>
    <p class="gm-20__hint">Hover the card — the stronger lens fades in on <span class="gm-20__code">opacity</span>, so the turbulence never re-runs.</p>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-20 {
  --a1: rgba(165,180,252,.6);
  --a2: rgba(103,232,249,.55);
  --a3: rgba(240,171,252,.55);
  --a4: rgba(110,231,183,.45);
  --base: #f0f3fb;
  --base2: #e2e8fd;
  --ink: #0f1120;
  --muted: rgba(15,17,32,.68);
  --tint: #ffffff;
  --accent: #0284c7;
  --rim: rgba(255,255,255,.95);
  --rim2: rgba(255,255,255,.5);
  --edge: rgba(15,17,32,.12);
  --line: rgba(15,17,32,.1);
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
  background: radial-gradient(54% 46% at 14% 16%, var(--a1) 0%, transparent 62%), radial-gradient(48% 42% at 86% 14%, var(--a2) 0%, transparent 58%), radial-gradient(50% 44% at 80% 88%, var(--a3) 0%, transparent 60%), radial-gradient(42% 36% at 14% 90%, var(--a4) 0%, transparent 58%), linear-gradient(160deg, var(--base) 0%, var(--base2) 52%, var(--base) 100%);
}

.gm-20 *,
.gm-20 *::before,
.gm-20 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-20 {
    --a1: oklch(0.68 0.19 280 / .62);
    --a2: oklch(0.82 0.16 200 / .56);
    --a3: oklch(0.84 0.13 320 / .5);
    --a4: oklch(0.8 0.15 165 / .42);
    --base: oklch(0.97 0.008 275);
    --base2: oklch(0.93 0.015 285);
    --accent: oklch(0.85 0.11 220);
  }
}

.gm-20__defs {
  position: absolute;
  inline-size: 0;
  block-size: 0;
  overflow: hidden;
}

.gm-20__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-20__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-20__theme {
  position: absolute;
  inset-block-start: 1.15rem;
  inset-inline-end: 1.15rem;
  z-index: 9;
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

.gm-20__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-20__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-20__theme:hover {
  scale: 1.06;
}

.gm-20__sr:focus-visible + .gm-20__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-20__moon {
  display: none;
}

.gm-20__stage {
  position: relative;
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  align-content: center;
  gap: 1.1rem;
  padding: clamp(1.25rem,4vw,3.5rem);
}

.gm-20__rules {
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  background-image: repeating-linear-gradient(0deg, var(--line) 0 1px, transparent 1px 2.4rem), repeating-linear-gradient(90deg, var(--line) 0 1px, transparent 1px 2.4rem);
  mask-image: radial-gradient(120% 100% at 50% 50%, #000 20%, transparent 80%);
}

.gm-20__card {
  position: relative;
  z-index: 1;
  inline-size: min(33rem,100%);
  border-radius: 1.85rem;
  overflow: hidden;
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2), 0 38px 84px -34px rgba(0,0,0,.78);
  transition: translate .3s cubic-bezier(.2,.7,.3,1);
}

.gm-20__card:hover {
  translate: 0 -5px;
}

.gm-20__lens {
  position: absolute;
  inset: 0;
  z-index: 0;
  border-radius: inherit;
  -webkit-backdrop-filter: blur(2px) saturate(165%);
  backdrop-filter: blur(2px) saturate(165%);
  mask-image: radial-gradient(115% 115% at 50% 50%, transparent 46%, #000 86%);
  -webkit-mask-image: radial-gradient(115% 115% at 50% 50%, transparent 46%, #000 86%);
}

@supports (backdrop-filter: url(#gm-20-refract)) {
  .gm-20__lens {
    backdrop-filter: blur(2px) saturate(165%) url(#gm-20-refract);
  }

  .gm-20__lens--hi {
    backdrop-filter: blur(1px) saturate(175%) url(#gm-20-refract-hi);
  }
}

.gm-20__lens--hi {
  opacity: 0;
  transition: opacity .32s ease;
}

.gm-20__card:hover .gm-20__lens--hi {
  opacity: 1;
}

.gm-20__fringe {
  position: absolute;
  inset: 0;
  z-index: 0;
  border-radius: inherit;
  pointer-events: none;
  translate: 1px 0;
  opacity: .1;
  mix-blend-mode: screen;
  background: linear-gradient(100deg, #7dd3fc, transparent 58%, #f0abfc);
  mask-image: radial-gradient(115% 115% at 50% 50%, transparent 52%, #000 92%);
  -webkit-mask-image: radial-gradient(115% 115% at 50% 50%, transparent 52%, #000 92%);
}

.gm-20__body {
  position: relative;
  z-index: 1;
  display: grid;
  gap: 1rem;
  padding: clamp(1.4rem,3vw,2rem);
  background: rgba(255,255,255,.13);
  -webkit-backdrop-filter: blur(18px) saturate(170%);
  backdrop-filter: blur(18px) saturate(170%);
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-20__body {
    background: color-mix(in oklab, var(--tint) 14%, transparent);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-20__body {
    background: rgba(18,14,44,.9);
  }
}

.gm-20__top {
  display: flex;
  align-items: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.gm-20__avatar {
  inline-size: 4rem;
  block-size: 4rem;
  flex: none;
  border-radius: 1.1rem;
  object-fit: cover;
  background: rgba(255,255,255,.12);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim2), 0 12px 26px -16px rgba(0,0,0,.7);
}

.gm-20__ident {
  display: grid;
  gap: .12rem;
  min-inline-size: 0;
}

.gm-20__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-20__h {
  margin: 0;
  font-size: clamp(1.4rem,3vw,1.85rem);
  font-weight: 600;
  letter-spacing: -.03em;
  line-height: 1.1;
}

.gm-20__role {
  margin: 0;
  font-size: .88rem;
  color: var(--muted);
}

.gm-20__copy {
  margin: 0;
  font-size: .98rem;
  line-height: 1.6;
  color: var(--ink);
  opacity: .88;
  text-wrap: pretty;
}

.gm-20__copy code {
  font-family: var(--mono);
  font-size: .86rem;
  padding: .1rem .34rem;
  border-radius: .32rem;
  background: rgba(0,0,0,.28);
  border: 1px solid var(--rim2);
}

.gm-20__meta {
  margin: 0;
  padding-block-start: .95rem;
  border-block-start: 1px solid var(--rim2);
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.gm-20__meta div {
  display: grid;
  gap: .15rem;
}

.gm-20__meta dt {
  font-family: var(--mono);
  font-size: .62rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-20__meta dd {
  margin: 0;
  font-family: var(--mono);
  font-size: .9rem;
  font-variant-numeric: tabular-nums;
}

.gm-20__actions {
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
}

.gm-20__cta,
.gm-20__ghost {
  min-block-size: 2.75rem;
  padding: .75rem 1.15rem;
  border-radius: .9rem;
  cursor: pointer;
  font: inherit;
  font-size: .94rem;
  font-weight: 500;
  transition: translate .18s ease, background .18s ease;
}

.gm-20__cta {
  color: #06202c;
  background: var(--accent);
  border: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.5), 0 14px 30px -16px rgba(0,0,0,.7);
}

.gm-20__ghost {
  color: var(--ink);
  background: rgba(255,255,255,.13);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim2);
}

.gm-20__cta:hover,
.gm-20__ghost:hover {
  translate: 0 -2px;
}

.gm-20__cta:focus-visible,
.gm-20__ghost:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-20__hint {
  position: relative;
  z-index: 1;
  margin: 0;
  font-size: .85rem;
  color: var(--muted);
  text-align: center;
}

.gm-20__code {
  font-family: var(--mono);
  font-size: .78rem;
  padding: .1rem .34rem;
  border-radius: .32rem;
  background: rgba(255,255,255,.12);
  border: 1px solid var(--edge);
  color: var(--ink);
}

.gm-20[data-theme="light"],
.gm-20:has(#gm-20-theme:checked) {
  --a1: rgba(129,140,248,.6);
  --a2: rgba(34,211,238,.55);
  --a3: rgba(240,171,252,.5);
  --a4: rgba(52,211,153,.4);
  --base: #05060f;
  --base2: #141033;
  --ink: #f9fafe;
  --muted: rgba(249,250,254,.7);
  --rim: rgba(255,255,255,.55);
  --rim2: rgba(255,255,255,.15);
  --edge: rgba(255,255,255,.2);
  --line: rgba(255,255,255,.12);
  --accent: #7dd3fc;
}

.gm-20:has(#gm-20-theme:checked) .gm-20__sun {
  display: none;
}

.gm-20:has(#gm-20-theme:checked) .gm-20__moon {
  display: block;
}

.gm-20[data-theme="light"] .gm-20__cta,
.gm-20:has(#gm-20-theme:checked) .gm-20__cta {
  color: #fff;
}

.gm-20[data-theme="light"] .gm-20__copy code,
.gm-20:has(#gm-20-theme:checked) .gm-20__copy code {
  background: rgba(15,17,32,.07);
}

@media (prefers-reduced-motion: reduce) {
  .gm-20 *,
    .gm-20 *::before,
    .gm-20 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .gm-20__card,
    .gm-20__cta,
    .gm-20__ghost,
    .gm-20__theme {
    border-color: CanvasText;
    box-shadow: none;
    background: Canvas;
  }

  .gm-20__lens,
    .gm-20__fringe {
    display: none;
  }

  .gm-20__body {
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }
}
```
