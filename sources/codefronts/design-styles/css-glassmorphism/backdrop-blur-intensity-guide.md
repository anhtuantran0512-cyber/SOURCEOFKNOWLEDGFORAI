---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-glassmorphism/backdrop-blur-intensity-guide/"
title: "Backdrop Blur Intensity Guide"
section: "design-styles"
category: "css-glassmorphism"
category_name: "CSS Glassmorphism"
description: "Four identical glass panels sit over one shared gradient mesh at blur(4px), blur(12px), blur(24px) and blur(40px) so you can eyeball the exact radius your…"
has_js: "false"
---

Here's a working CSS Glassmorphism from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Backdrop Blur Intensity Guide
Source: https://codefronts.com/design-styles/css-glassmorphism/backdrop-blur-intensity-guide/

Four identical glass panels sit over one shared gradient mesh at blur(4px), blur(12px), blur(24px) and blur(40px) so you can eyeball the exact radius your brand needs before you commit a token. Each panel carries its value in a monospace pill, and a decision-guide strip translates the scale into intent — 4px is depth, 40px is privacy.
## HTML
```html
<div class="gm-01">
  <input class="gm-01__sr" type="checkbox" id="gm-01-theme">
  <label class="gm-01__theme" for="gm-01-theme" title="Switch theme">
    <svg class="gm-01__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="gm-01__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="gm-01__vh">Switch light or dark theme</span>
  </label>

  <div class="gm-01__stage">
    <section class="gm-01__wrap" aria-labelledby="gm-01-h">
      <header class="gm-01__head">
        <p class="gm-01__eyebrow">backdrop-filter · blur()</p>
        <h2 class="gm-01__h" id="gm-01-h">Pick a blur radius by looking through it</h2>
        <p class="gm-01__sub">One background, one panel recipe, four radii. Everything else is held constant, so the only variable you are judging is the blur.</p>
      </header>

      <ul class="gm-01__grid">
        <li class="gm-01__panel gm-01__panel--1">
          <p class="gm-01__pill">blur(4px)</p>
          <h3 class="gm-01__tier">Barely there</h3>
          <p class="gm-01__copy">The mesh reads straight through. Use for hairline separation — sticky table headers, toolbars over dense content.</p>
          <p class="gm-01__meta">depth · 4.5:1 text needs a tint</p>
        </li>
        <li class="gm-01__panel gm-01__panel--2">
          <p class="gm-01__pill">blur(12px)</p>
          <h3 class="gm-01__tier">Product default</h3>
          <p class="gm-01__copy">Shape survives, detail goes. The safest brand token — navbars, command palettes, popovers, inline sheets.</p>
          <p class="gm-01__meta">balance · comfortable contrast</p>
        </li>
        <li class="gm-01__panel gm-01__panel--3">
          <p class="gm-01__pill">blur(24px)</p>
          <h3 class="gm-01__tier">Frosted</h3>
          <p class="gm-01__copy">Colour without content. The iOS 26 / visionOS sheet value — cards and modals that must hold long-form copy.</p>
          <p class="gm-01__meta">frost · text-safe at 90% alpha</p>
        </li>
        <li class="gm-01__panel gm-01__panel--4">
          <p class="gm-01__pill">blur(40px)</p>
          <h3 class="gm-01__tier">Privacy glass</h3>
          <p class="gm-01__copy">A wash of ambient colour. Reach for it when the backdrop must be unreadable — auth screens, lock overlays, blurred previews.</p>
          <p class="gm-01__meta">privacy · heaviest to composite</p>
        </li>
      </ul>

      <aside class="gm-01__legend" aria-label="Decision guide">
        <p class="gm-01__lrow"><span class="gm-01__lkey">4 – 8px</span><span class="gm-01__lval">Depth cue. The user still reads what is behind.</span></p>
        <p class="gm-01__lrow"><span class="gm-01__lkey">10 – 16px</span><span class="gm-01__lval">Chrome default. Blur enough to separate, cheap enough to scroll.</span></p>
        <p class="gm-01__lrow"><span class="gm-01__lkey">20 – 28px</span><span class="gm-01__lval">Content surfaces. Pair with 160–180% saturate.</span></p>
        <p class="gm-01__lrow"><span class="gm-01__lkey">32px +</span><span class="gm-01__lval">Privacy. Budget one compositor layer and avoid on long scrolls.</span></p>
      </aside>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.gm-01 {
  /* sRGB baseline — upgraded to oklch under @supports */
  --a1: rgba(168,85,247,.55);
  --a2: rgba(56,189,248,.5);
  --a3: rgba(244,114,182,.45);
  --a4: rgba(45,212,191,.4);
  --base: #080a14;
  --base2: #150f2c;
  --ink: #f7f8fd;
  --muted: rgba(247,248,253,.68);
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
  -webkit-text-size-adjust: 100%;
  background: radial-gradient(58% 46% at 12% 16%, var(--a1) 0%, transparent 62%), radial-gradient(50% 42% at 86% 10%, var(--a2) 0%, transparent 60%), radial-gradient(54% 48% at 78% 84%, var(--a3) 0%, transparent 62%), radial-gradient(48% 42% at 20% 90%, var(--a4) 0%, transparent 60%), linear-gradient(162deg, var(--base) 0%, var(--base2) 52%, var(--base) 100%);
}

.gm-01 *,
.gm-01 *::before,
.gm-01 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.1 300)) {
  .gm-01 {
    --a1: oklch(0.68 0.24 305 / .58);
    --a2: oklch(0.78 0.16 220 / .52);
    --a3: oklch(0.74 0.19 5 / .46);
    --a4: oklch(0.82 0.15 175 / .42);
    --base: oklch(0.16 0.03 275);
    --base2: oklch(0.24 0.09 295);
    --ink: oklch(0.98 0.005 285);
    --muted: oklch(0.98 0.005 285 / .68);
  }
}

.gm-01__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.gm-01__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}
/* theme pill — top right, pure CSS */

.gm-01__theme {
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
  background: color-mix(in oklab, var(--tint) 14%, transparent);
  border: 1px solid var(--edge);
  -webkit-backdrop-filter: blur(10px) saturate(160%);
  backdrop-filter: blur(10px) saturate(160%);
  box-shadow: inset 0 1px 0 var(--rim), 0 10px 24px -14px rgba(0,0,0,.7);
  transition: scale .18s ease, background .18s ease;
}

.gm-01__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.gm-01__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.gm-01__theme:hover {
  scale: 1.06;
}

.gm-01__sr:focus-visible + .gm-01__theme {
  outline: 2px solid var(--ink);
  outline-offset: 3px;
}

.gm-01__moon {
  display: none;
}

.gm-01__stage {
  min-height: 100vh;
  min-height: 100svh;
  display: grid;
  place-items: center;
  padding: clamp(1.25rem,4vw,3.5rem);
}

.gm-01__wrap {
  inline-size: min(78rem,100%);
}

.gm-01__head {
  display: grid;
  gap: .6rem;
  max-inline-size: 46rem;
  margin-block-end: clamp(1.5rem,3.5vw,2.5rem);
}

.gm-01__eyebrow {
  margin: 0;
  font-family: var(--mono);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--muted);
}

.gm-01__h {
  margin: 0;
  font-size: clamp(1.85rem,4.4vw,2.9rem);
  font-weight: 600;
  letter-spacing: -.03em;
  line-height: 1.05;
  text-wrap: balance;
}

.gm-01__sub {
  margin: 0;
  font-size: clamp(.95rem,1.4vw,1.05rem);
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-01__grid {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(.9rem,1.8vw,1.4rem);
  grid-template-columns: repeat(auto-fit,minmax(14rem,1fr));
}

.gm-01__panel {
  --b: 12px;
  position: relative;
  display: flex;
  flex-direction: column;
  gap: .55rem;
  padding: clamp(1.1rem,1.8vw,1.5rem);
  border-radius: 1.25rem;
  background: rgba(255,255,255,.1);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2), 0 26px 54px -24px rgba(0,0,0,.62);
  transition: translate .25s cubic-bezier(.2,.7,.3,1), box-shadow .25s ease;
}

@supports (background: color-mix(in oklab, white 10%, transparent)) {
  .gm-01__panel {
    background: color-mix(in oklab, var(--tint) 16%, transparent);
  }
}

@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-01__panel {
    -webkit-backdrop-filter: blur(var(--b)) saturate(150%);
    backdrop-filter: blur(var(--b)) saturate(150%);
  }
}

@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .gm-01__panel {
    background: rgba(22,18,40,.8);
  }
}

.gm-01__panel--1 {
  --b: 4px;
}

.gm-01__panel--2 {
  --b: 12px;
}

.gm-01__panel--3 {
  --b: 24px;
}

.gm-01__panel--4 {
  --b: 40px;
}

.gm-01__panel:hover {
  translate: 0 -4px;
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 var(--rim2), 0 34px 64px -24px rgba(0,0,0,.7);
}

.gm-01__pill {
  margin: 0;
  align-self: flex-start;
  padding: .32rem .6rem;
  border-radius: .55rem;
  font-family: var(--mono);
  font-size: .74rem;
  font-variant-numeric: tabular-nums;
  letter-spacing: .02em;
  background: rgba(255,255,255,.16);
  border: 1px solid var(--edge);
  box-shadow: inset 0 1px 0 var(--rim2);
}

.gm-01__tier {
  margin: .2rem 0 0;
  font-size: 1.12rem;
  font-weight: 600;
  letter-spacing: -.015em;
}

.gm-01__copy {
  margin: 0;
  font-size: .9rem;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.gm-01__meta {
  margin: auto 0 0;
  padding-block-start: .7rem;
  border-block-start: 1px solid var(--rim2);
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .06em;
  color: var(--muted);
}

.gm-01__legend {
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

.gm-01__lrow {
  margin: 0;
  display: grid;
  grid-template-columns: 6.5rem 1fr;
  gap: .75rem;
  align-items: baseline;
}

.gm-01__lkey {
  font-family: var(--mono);
  font-size: .74rem;
  letter-spacing: .04em;
  color: var(--ink);
}

.gm-01__lval {
  font-size: .88rem;
  line-height: 1.45;
  color: var(--muted);
}

@media (max-width: 30rem) {
  .gm-01__lrow {
    grid-template-columns: 1fr;
  }
}
/* light theme — checkbox, attribute or system preference */

.gm-01[data-theme="light"],
.gm-01:has(#gm-01-theme:checked) {
  --a1: rgba(192,132,252,.5);
  --a2: rgba(125,211,252,.5);
  --a3: rgba(251,146,60,.4);
  --a4: rgba(110,231,183,.42);
  --base: #eef1f8;
  --base2: #dfe6fb;
  --ink: #12131c;
  --muted: rgba(18,19,28,.66);
  --tint: #ffffff;
  --rim: rgba(255,255,255,.9);
  --rim2: rgba(255,255,255,.4);
  --edge: rgba(18,19,28,.1);
}

.gm-01:has(#gm-01-theme:checked) .gm-01__sun {
  display: none;
}

.gm-01:has(#gm-01-theme:checked) .gm-01__moon {
  display: block;
}

.gm-01[data-theme="light"] .gm-01__panel,
.gm-01:has(#gm-01-theme:checked) .gm-01__panel {
  box-shadow: inset 0 1px 0 var(--rim), inset 0 -1px 0 rgba(255,255,255,.5), 0 24px 48px -26px rgba(30,26,60,.4);
}

@media (prefers-reduced-motion: reduce) {
  .gm-01 *,
    .gm-01 *::before,
    .gm-01 *::after {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .gm-01__panel,
    .gm-01__legend,
    .gm-01__theme,
    .gm-01__pill {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
    background: Canvas;
  }
}
```
