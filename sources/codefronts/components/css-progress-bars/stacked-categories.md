---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/stacked-categories/"
title: "Stacked Category Progress Bar for Budget and Analytics"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "One bar, five categories, no chart library: segments sized by flex-grow from their own percentage, a legend with values, and a CSS-only tooltip on hover and…"
has_js: "false"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stacked Category Progress Bar for Budget and Analytics
Source: https://codefronts.com/components/css-progress-bars/stacked-categories/

One bar, five categories, no chart library: segments sized by flex-grow from their own percentage, a legend with values, and a CSS-only tooltip on hover and keyboard focus. The pattern behind every budget and storage-breakdown panel.
## HTML
```html
<div class="pb-20">
  <input class="pb-20__sr" type="checkbox" id="pb-20-light">
  <label class="pb-20__theme" for="pb-20-light" title="Switch light or dark theme">
    <svg class="pb-20__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-20__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="pb-20__vh">Switch light or dark theme</span>
  </label>

  <div class="pb-20__stage">
    <div class="pb-20__card">
      <header class="pb-20__head">
        <span class="pb-20__headMeta">
          <span class="pb-20__eyebrow pb-20__mono">August 2026 &middot; personal</span>
          <h2 class="pb-20__title">Where the money went</h2>
        </span>
        <span class="pb-20__total"><span class="pb-20__totalNum">&pound;3,200</span><span class="pb-20__totalKey pb-20__mono">spent</span></span>
      </header>

      <div class="pb-20__bar" role="img" aria-label="Monthly budget breakdown: housing 35 percent, food 20 percent, transport 15 percent, savings 20 percent, other 10 percent">
        <span class="pb-20__seg" style="--pct:35; --c:var(--c1)" tabindex="0">
          <span class="pb-20__vh">Housing, 35 percent, 1,120 pounds</span>
          <span class="pb-20__tip" aria-hidden="true"><b>Housing</b><i class="pb-20__mono">&pound;1,120 &middot; 35%</i></span>
        </span>
        <span class="pb-20__seg" style="--pct:20; --c:var(--c2)" tabindex="0">
          <span class="pb-20__vh">Food, 20 percent, 640 pounds</span>
          <span class="pb-20__tip" aria-hidden="true"><b>Food</b><i class="pb-20__mono">&pound;640 &middot; 20%</i></span>
        </span>
        <span class="pb-20__seg" style="--pct:15; --c:var(--c3)" tabindex="0">
          <span class="pb-20__vh">Transport, 15 percent, 480 pounds</span>
          <span class="pb-20__tip" aria-hidden="true"><b>Transport</b><i class="pb-20__mono">&pound;480 &middot; 15%</i></span>
        </span>
        <span class="pb-20__seg" style="--pct:20; --c:var(--c4)" tabindex="0">
          <span class="pb-20__vh">Savings, 20 percent, 640 pounds</span>
          <span class="pb-20__tip" aria-hidden="true"><b>Savings</b><i class="pb-20__mono">&pound;640 &middot; 20%</i></span>
        </span>
        <span class="pb-20__seg" style="--pct:10; --c:var(--c5)" tabindex="0">
          <span class="pb-20__vh">Other, 10 percent, 320 pounds</span>
          <span class="pb-20__tip" aria-hidden="true"><b>Other</b><i class="pb-20__mono">&pound;320 &middot; 10%</i></span>
        </span>
      </div>

      <dl class="pb-20__legend">
        <div class="pb-20__item"><dt><i class="pb-20__dot" style="--c:var(--c1)"></i>Housing</dt><dd><span class="pb-20__mono">&pound;1,120</span><span class="pb-20__pct pb-20__mono">35%</span></dd></div>
        <div class="pb-20__item"><dt><i class="pb-20__dot" style="--c:var(--c2)"></i>Food</dt><dd><span class="pb-20__mono">&pound;640</span><span class="pb-20__pct pb-20__mono">20%</span></dd></div>
        <div class="pb-20__item"><dt><i class="pb-20__dot" style="--c:var(--c3)"></i>Transport</dt><dd><span class="pb-20__mono">&pound;480</span><span class="pb-20__pct pb-20__mono">15%</span></dd></div>
        <div class="pb-20__item"><dt><i class="pb-20__dot" style="--c:var(--c4)"></i>Savings</dt><dd><span class="pb-20__mono">&pound;640</span><span class="pb-20__pct pb-20__mono">20%</span></dd></div>
        <div class="pb-20__item"><dt><i class="pb-20__dot" style="--c:var(--c5)"></i>Other</dt><dd><span class="pb-20__mono">&pound;320</span><span class="pb-20__pct pb-20__mono">10%</span></dd></div>
      </dl>

      <p class="pb-20__note">Hover or tab through the segments. Values live in the legend too &mdash; colour is never the only carrier.</p>
    </div>
  </div>
</div>
```
## CSS
```css
.pb-20 {
  --bg: #0a0b0f;
  --card: #101218;
  --card2: #151821;
  --ink: #eceff5;
  --muted: rgba(236,239,245,.6);
  --line: rgba(236,239,245,.12);
  --track: rgba(236,239,245,.08);
  --c1: #6366f1;
  --c2: #f59e0b;
  --c3: #06b6d4;
  --c4: #22c55e;
  --c5: #94a3b8;
  --sans: system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono: ui-monospace,"JetBrains Mono","Geist Mono",SFMono-Regular,Menlo,monospace;
  inline-size: 100%;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(60% .2 275)) {
  .pb-20 {
    --c1: oklch(60% .2 275);
    --c2: oklch(78% .16 70);
    --c3: oklch(72% .13 205);
    --c4: oklch(74% .18 145);
    --c5: oklch(72% .03 250);
  }
}

.pb-20 *,
.pb-20 *::before,
.pb-20 *::after {
  box-sizing: border-box;
}

.pb-20__sr {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.pb-20__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pb-20__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(80% 55% at 10% 0%,color-mix(in srgb,var(--c1) 16%,transparent),transparent 58%), radial-gradient(70% 55% at 100% 100%,color-mix(in srgb,var(--c3) 12%,transparent),transparent 60%);
}

.pb-20__theme {
  position: absolute;
  inset-block-start: clamp(.9rem,2.4vw,1.6rem);
  inset-inline-end: clamp(.9rem,2.4vw,1.6rem);
  z-index: 5;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  cursor: pointer;
  border-radius: 99px;
  border: 1px solid var(--line);
  color: var(--ink);
  background: rgba(255,255,255,.06);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  transition: background .2s,transform .2s;
}

.pb-20__theme:hover {
  transform: translateY(-1px);
  background: rgba(255,255,255,.12);
}

.pb-20__sr:focus-visible + .pb-20__theme {
  outline: 2px solid var(--c1);
  outline-offset: 3px;
}

.pb-20__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-20__sun {
  display: none;
}

.pb-20__moon {
  display: block;
}

.pb-20__card {
  inline-size: min(44rem,100%);
  display: grid;
  gap: clamp(1.1rem,2.6vw,1.6rem);
  padding: clamp(1.3rem,3.4vw,2.2rem);
  border-radius: 1.5rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--card) 92%,transparent);
  -webkit-backdrop-filter: blur(14px);
  backdrop-filter: blur(14px);
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset,0 32px 76px -44px rgba(0,0,0,.95);
}

.pb-20__head {
  display: flex;
  flex-wrap: wrap;
  gap: .9rem;
  align-items: flex-end;
  justify-content: space-between;
}

.pb-20__headMeta {
  display: grid;
  gap: .25rem;
}

.pb-20__eyebrow {
  letter-spacing: .1em;
  text-transform: uppercase;
  font-size: .66rem;
}

.pb-20__mono {
  font-family: var(--mono);
  font-size: .74rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pb-20__title {
  margin: 0;
  font-size: clamp(1.35rem,3.2vw,1.95rem);
  line-height: 1.14;
  letter-spacing: -.024em;
  font-weight: 650;
}

.pb-20__total {
  display: grid;
  gap: .05rem;
  justify-items: end;
}

.pb-20__totalNum {
  font-size: clamp(1.5rem,4vw,2.1rem);
  font-weight: 700;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.pb-20__totalKey {
  letter-spacing: .1em;
  text-transform: uppercase;
  font-size: .62rem;
}

.pb-20__bar {
  display: flex;
  inline-size: 100%;
  block-size: 2.2rem;
  border-radius: .7rem;
  overflow: visible;
  padding: 0;
  background: var(--track);
  border: 1px solid var(--line);
  box-shadow: 0 2px 5px rgba(0,0,0,.35) inset;
  isolation: isolate;
}

.pb-20__seg {
  position: relative;
  flex: var(--pct) 1 0;
  background: var(--c);
  cursor: default;
  border-inline-end: 1px solid color-mix(in srgb,var(--card) 70%,transparent);
  transition: filter .18s;
}

.pb-20__seg:first-child {
  border-start-start-radius: .65rem;
  border-end-start-radius: .65rem;
}

.pb-20__seg:last-child {
  border-inline-end: 0;
  border-start-end-radius: .65rem;
  border-end-end-radius: .65rem;
}

.pb-20__seg:hover,
.pb-20__seg:focus-visible {
  filter: brightness(1.18);
  z-index: 2;
}

.pb-20__seg:focus-visible {
  outline: 2px solid var(--ink);
  outline-offset: 2px;
}

.pb-20__tip {
  position: absolute;
  inset-block-end: calc(100% + .6rem);
  inset-inline-start: 50%;
  z-index: 3;
  display: grid;
  gap: .05rem;
  padding: .45rem .65rem;
  border-radius: .55rem;
  white-space: nowrap;
  pointer-events: none;
  background: var(--ink);
  color: var(--card);
  opacity: 0;
  translate: -50% .25rem;
  box-shadow: 0 10px 24px -14px rgba(0,0,0,.8);
  transition: opacity .18s,translate .18s;
}

.pb-20__tip b {
  font-size: .78rem;
}

.pb-20__tip i {
  font-style: normal;
  color: color-mix(in srgb,var(--card) 78%,var(--ink));
}

.pb-20__tip::after {
  content: "";
  position: absolute;
  inset-block-start: 100%;
  inset-inline-start: 50%;
  translate: -50% 0;
  border: .3rem solid transparent;
  border-block-start-color: var(--ink);
}

.pb-20__seg:hover .pb-20__tip,
.pb-20__seg:focus-visible .pb-20__tip {
  opacity: 1;
  translate: -50% 0;
}

.pb-20__legend {
  margin: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(9.5rem,1fr));
  gap: .15rem .9rem;
}

.pb-20__item {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: .6rem;
  padding-block: .55rem;
  border-block-start: 1px solid var(--line);
}

.pb-20__item dt {
  display: flex;
  align-items: center;
  gap: .45rem;
  font-size: .85rem;
  font-weight: 550;
}

.pb-20__item dd {
  margin: 0;
  display: flex;
  gap: .5rem;
  align-items: baseline;
}

.pb-20__dot {
  inline-size: .6rem;
  block-size: .6rem;
  border-radius: .2rem;
  background: var(--c);
  flex: none;
}

.pb-20__pct {
  color: var(--ink);
  font-weight: 600;
  min-inline-size: 2.4rem;
  text-align: end;
}

.pb-20__note {
  margin: 0;
  font-size: .8rem;
  color: var(--muted);
  text-wrap: pretty;
}

.pb-20[data-theme="light"],
.pb-20:has(#pb-20-light:checked) {
  --bg: #f5f6fa;
  --card: #ffffff;
  --card2: #f8f9fc;
  --ink: #0b0d14;
  --muted: rgba(11,13,20,.6);
  --line: rgba(11,13,20,.1);
  --track: rgba(11,13,20,.07);
  --c1: #4f46e5;
  --c2: #d97706;
  --c3: #0891b2;
  --c4: #16a34a;
  --c5: #64748b;
}

.pb-20:has(#pb-20-light:checked) .pb-20__theme {
  background: rgba(11,13,20,.05);
}

.pb-20:has(#pb-20-light:checked) .pb-20__sun {
  display: block;
}

.pb-20:has(#pb-20-light:checked) .pb-20__moon {
  display: none;
}

@media (prefers-color-scheme: light) {
  .pb-20:not([data-theme="dark"]):not(:has(#pb-20-light:checked)) {
    --bg: #f5f6fa;
    --card: #ffffff;
    --card2: #f8f9fc;
    --ink: #0b0d14;
    --muted: rgba(11,13,20,.6);
    --line: rgba(11,13,20,.1);
    --track: rgba(11,13,20,.07);
    --c1: #4f46e5;
    --c2: #d97706;
    --c3: #0891b2;
    --c4: #16a34a;
    --c5: #64748b;
  }

  .pb-20:not([data-theme="dark"]):not(:has(#pb-20-light:checked)) .pb-20__theme {
    background: rgba(11,13,20,.05);
  }

  .pb-20:not([data-theme="dark"]):not(:has(#pb-20-light:checked)) .pb-20__sun {
    display: block;
  }

  .pb-20:not([data-theme="dark"]):not(:has(#pb-20-light:checked)) .pb-20__moon {
    display: none;
  }

  .pb-20:not([data-theme="light"]):has(#pb-20-light:checked) {
    --bg: #0a0b0f;
    --card: #101218;
    --card2: #151821;
    --ink: #eceff5;
    --muted: rgba(236,239,245,.6);
    --line: rgba(236,239,245,.12);
    --track: rgba(236,239,245,.08);
    --c1: #6366f1;
    --c2: #f59e0b;
    --c3: #06b6d4;
    --c4: #22c55e;
    --c5: #94a3b8;
  }

  @supports (color: oklch(60% .2 275)) {
    .pb-20:not([data-theme="light"]):has(#pb-20-light:checked) {
      --c1: oklch(60% .2 275);
      --c2: oklch(78% .16 70);
      --c3: oklch(72% .13 205);
      --c4: oklch(74% .18 145);
      --c5: oklch(72% .03 250);
    }
  }

  .pb-20:not([data-theme="light"]):has(#pb-20-light:checked) .pb-20__theme {
    background: rgba(255,255,255,.06);
  }

  .pb-20:not([data-theme="light"]):has(#pb-20-light:checked) .pb-20__sun {
    display: none;
  }

  .pb-20:not([data-theme="light"]):has(#pb-20-light:checked) .pb-20__moon {
    display: block;
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-20 *,
    .pb-20 *::before,
    .pb-20 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .pb-20__card,
    .pb-20__bar,
    .pb-20__theme {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  .pb-20__seg {
    background: Canvas;
    border-inline-end: 2px solid CanvasText;
  }

  .pb-20__tip {
    background: Canvas;
    color: CanvasText;
    border: 1px solid CanvasText;
  }
}
```
