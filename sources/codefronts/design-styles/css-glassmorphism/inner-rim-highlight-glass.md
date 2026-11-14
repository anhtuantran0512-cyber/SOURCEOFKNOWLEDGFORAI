---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/inner-rim-highlight-glass/"
title: "Inner Rim Highlight Glass"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "The detail that separates convincing glass from a translucent rectangle: a two-stop inset rim."
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Inner Rim Highlight Glass
Source: https://codefronts.com/design-styles/css-glassmorphism/inner-rim-highlight-glass/

The detail that separates convincing glass from a translucent rectangle: a two-stop inset rim. A bright inset 0 1px 0 rgba(255,255,255,.5) on the top edge reads as light catching the bevel, a dimmer inset 0 -1px 0 rgba(255,255,255,.15) at the bottom reads as bounce light. Three panels compare no rim, top-only and the full pair.
## HTML
```html
<div class="gm-07">
  <input class="gm-07__sr" type="checkbox" id="gm-07-theme">
  <label class="gm-07__theme" for="gm-07-theme" title="Switch theme">
    <svg class="gm-07__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-07__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-07__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-07__stage">
    <section class="gm-07__wrap" aria-labelledby="gm-07-h">
      <header class="gm-07__head">
        <p class="gm-07__eyebrow">box-shadow · inset</p>
        <h2 class="gm-07__h" id="gm-07-h">One inset line is the whole illusion</h2>
        <p class="gm-07__sub">Same blur, same tint, same radius in all three. Only the rim changes — and only the third one looks like glass.</p>
      </header>

      <ul class="gm-07__grid">
        <li class="gm-07__panel gm-07__panel--none">
          <p class="gm-07__pill">no rim</p>
          <h3 class="gm-07__title">Flat translucency</h3>
          <p class="gm-07__copy">A blurred rectangle with a border. Nothing tells the eye the surface has thickness, so it reads as a hole in the page.</p>
          <code class="gm-07__snip">box-shadow: none;</code>
        </li>
        <li class="gm-07__panel gm-07__panel--top">
          <p class="gm-07__pill">top rim</p>
          <h3 class="gm-07__title">Light from above</h3>
          <p class="gm-07__copy">One bright inset line on the top edge and the panel gains a bevel. This alone gets you 80% of the way there.</p>
          <code class="gm-07__snip">inset 0 1px 0 rgba(255,255,255,.5)</code>
        </li>
        <li class="gm-07__panel gm-07__panel--full">
          <p class="gm-07__pill">full rim</p>
          <h3 class="gm-07__title">Pressed into the surface</h3>
          <p class="gm-07__copy">Add the dim bottom bounce plus a soft specular sweep and the panel sits <em>in</em> the page instead of on it. This is the collection default.</p>
          <code class="gm-07__snip">+ inset 0 -1px 0 rgba(255,255,255,.15)</code>
        </li>
      </ul>

      <aside class="gm-07__legend">
        <p class="gm-07__lrow"><span class="gm-07__lkey">Top edge</span><span class="gm-07__lval">Bright, 0.4–0.6 alpha. Reads as the light source hitting the bevel.</span></p>
        <p class="gm-07__lrow"><span class="gm-07__lkey">Bottom edge</span><span class="gm-07__lval">Dim, 0.1–0.2 alpha. Reads as bounce light off the surface below.</span></p>
        <p class="gm-07__lrow"><span class="gm-07__lkey">Ambient</span><span class="gm-07__lval">One soft downward outer shadow. Never symmetric — that is neumorphism.</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-07 {
  --a1: rgba(56,189,248,.55);
  --a2: rgba(217,70,239,.55);
  --a3: rgba(250,204,21,.4);
  --a4: rgba(20,184,166,.45);
  --base: #060810;
  --base2: #131033;
  --ink: #f9fafe;
  --muted: rgba(249,250,254,.7);
  --tint: #ffffff;
  --rim: rgba(255,255,255,.5);
  --rim2: rgba(255,255,255,.15);
  --edge: rgba(255,255,255,.18);
  --amb: 0 26px 60px -28px rgba(0,0,0,.65);
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
  background: radial-gradient(52% 44% at 12% 18%, var(--a1) 0%, transparent 60%), radial-gradient(52% 44% at 88% 16%, var(--a2) 0%, transparent 60%), radial-gradient(44% 38% at 74% 90%, var(--a3) 0%, transparent 58%), radial-gradient(48% 42% at 20% 88%, var(--a4) 0%, transparent 60%), linear-gradient(164deg, var(--base) 0%, var(--base2) 52%, var(--base) 100%);
}

.gm-07 *,
.gm-07 *::before,
.gm-07 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-07 {
    --a1: oklch(0.78 0.16 220 / .56);
    --a2: oklch(0.68 0.25 325 / .56);
    --a3: oklch(0.88 0.16 95 / .42);
    --a4: oklch(0.76 0.14 180 / .46);
    --base: oklch(0.13 0.025 275);
    --base2: oklch(0.22 0.1 290);
  }
}

.gm-07__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-07__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.gm-07__theme {
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

.gm-07__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-07__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-07__theme:hover {
  scale: 1.06;
}

.gm-07__sr:focus-visible + .gm-07__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-07__moon {
  display: none;
}

.gm-07__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3.5rem);
}

.gm-07__wrap {
  inline-size: min(74rem,100%);
}

.gm-07__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 44rem;
  margin-block-end: clamp(1.5rem,3.5vw,2.5rem);
}

.gm-07__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-07__h {
  margin: 0;
  font-size: clamp(1.85rem,4.4vw,2.9rem);
  font-weight: 600;
  letter-spacing: -.03em;
  line-height: 1.05;
  text-wrap: balance;
}

.gm-07__sub {
  margin: 0;
  font-size: clamp(.95rem,1.4vw,1.05rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-07__grid {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(1rem,2vw,1.5rem);
  grid-template-columns: repeat(auto-fit,minmax(16rem,1fr));
}

.gm-07__panel {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: .55rem;
  padding: clamp(1.15rem,2vw,1.6rem);
  border-radius: 1.4rem;
  background: rgba(255,255,255,.11);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(22px) saturate(160%);
  backdrop-filter: blur(22px) saturate(160%);
  transition: translate .22s cubic-bezier(.2,.7,.3,1);
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-07__panel {
    background: color-mix(in oklab, var(--tint) 14%, transparent);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-07__panel {
    background: rgba(18,16,44,.86);
  }
}

.gm-07__panel--none {
  box-shadow: none;
}

.gm-07__panel--top {
  box-shadow: inset 0 1px 0 var(--rim), var(--amb);
}

.gm-07__panel--full {
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2), var(--amb);
}

.gm-07__panel--full::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  pointer-events: none;
  background: linear-gradient(145deg, rgba(255,255,255,.16), transparent 42%);
}

.gm-07__panel:hover {
  translate: 0 -4px;
}

.gm-07__pill {
  margin: 0;
  align-self: flex-start;
  padding: .3rem .58rem;
  border-radius: .5rem;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  background: rgba(255,255,255,.16);
  border: 1px solid var(--edge);
}

.gm-07__title {
  margin: .2rem 0 0;
  position: relative;
  font-size: clamp(1.15rem,2vw,1.42rem);
  font-weight: 600;
  letter-spacing: -.02em;
}

.gm-07__copy {
  margin: 0;
  position: relative;
  font-size: .93rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-07__snip {
  margin: auto 0 0;
  position: relative;
  display: block;
  padding: .55rem .7rem;
  border-radius: .6rem;
  font-family: var(--mono);
  font-size: .7rem;
  line-height: 1.45;
  color: var(--ink);
  background: rgba(0,0,0,.28);
  border: 1px solid var(--rim2);
  overflow-wrap: anywhere;
}

.gm-07__legend {
  margin-block-start: clamp(1rem,2vw,1.5rem);
  padding: clamp(1rem,1.8vw,1.35rem);
  border-radius: 1.1rem;
  border: 1px solid var(--edge);
  background: rgba(255,255,255,.08);
  -webkit-backdrop-filter: blur(18px) saturate(150%);
  backdrop-filter: blur(18px) saturate(150%);
  box-shadow: inset 0 1px 0 var(--rim2);
  display: grid;
  gap: .5rem;
}

.gm-07__lrow {
  margin: 0;
  display: grid;
  grid-template-columns: 8rem 1fr;
  gap: .8rem;
  align-items: baseline;
}

.gm-07__lkey {
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  color: var(--ink);
}

.gm-07__lval {
  font-size: .88rem;
  line-height: 1.45;
  color: var(--muted);
}

@media (max-width: 32rem) {
  .gm-07__lrow {
    grid-template-columns: 1fr;
  }
}

.gm-07[data-theme="light"],
.gm-07:has(#gm-07-theme:checked) {
  --a1: rgba(125,211,252,.5);
  --a2: rgba(240,171,252,.55);
  --a3: rgba(254,240,138,.5);
  --a4: rgba(153,246,228,.5);
  --base: #f0f3fa;
  --base2: #e2e6fb;
  --ink: #0f1220;
  --muted: rgba(15,18,32,.68);
  --rim: rgba(255,255,255,.95);
  --rim2: rgba(255,255,255,.5);
  --edge: rgba(15,18,32,.1);
  --amb: 0 22px 48px -28px rgba(24,20,60,.45);
}

.gm-07:has(#gm-07-theme:checked) .gm-07__sun {
  display: none;
}

.gm-07:has(#gm-07-theme:checked) .gm-07__moon {
  display: block;
}

.gm-07[data-theme="light"] .gm-07__snip,
.gm-07:has(#gm-07-theme:checked) .gm-07__snip {
  background: rgba(255,255,255,.6);
  color: #0f1220;
  border-color: rgba(15,18,32,.12);
}

@media (prefers-reduced-motion: reduce) {
  .gm-07 *,
    .gm-07 *::before,
    .gm-07 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .gm-07__panel,
    .gm-07__legend,
    .gm-07__theme,
    .gm-07__pill {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }

  .gm-07__panel--full::before {
    display: none;
  }
}
```
