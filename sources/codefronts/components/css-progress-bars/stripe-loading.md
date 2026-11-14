---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/stripe-loading/"
title: "Animated Stripe Loading Bar"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "The striped bar, rebuilt properly: 45&deg; repeating-linear-gradient hatching that slides forever, shown as both a determinate fill with a value label and an…"
has_js: "false"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animated Stripe Loading Bar
Source: https://codefronts.com/components/css-progress-bars/stripe-loading/

The striped bar, rebuilt properly: 45&deg; repeating-linear-gradient hatching that slides forever, shown as both a determinate fill with a value label and an indeterminate full-track sweep — so you can see exactly which one your state needs.
## HTML
```html
<div class="pb-15">
  <input class="pb-15__sr" type="checkbox" id="pb-15-light">
  <label class="pb-15__theme" for="pb-15-light" title="Switch light or dark theme">
    <svg class="pb-15__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-15__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="pb-15__vh">Switch light or dark theme</span>
  </label>

  <div class="pb-15__stage">
    <div class="pb-15__card">
      <header class="pb-15__head">
        <p class="pb-15__eyebrow"><span class="pb-15__badge">Stripes</span><span class="pb-15__mono">repeating-linear-gradient(45deg, …)</span></p>
        <h2 class="pb-15__title">Determinate or not &mdash; pick deliberately</h2>
        <p class="pb-15__lead">Same hatching, two different contracts. The left bar knows how much work is left; the right one only knows that work is happening.</p>
      </header>

      <section class="pb-15__block" aria-labelledby="pb-15-h1">
        <p class="pb-15__blockHead"><span id="pb-15-h1">Determinate</span><span class="pb-15__mono">aria-valuenow="68"</span></p>
        <div class="pb-15__bar" role="progressbar" aria-valuenow="68" aria-valuemin="0" aria-valuemax="100" aria-valuetext="68 percent of the import complete" aria-label="Importing records" style="--value:68">
          <span class="pb-15__fill"></span>
          <span class="pb-15__label pb-15__mono">68% &middot; 8,432 of 12,400 records</span>
        </div>
        <p class="pb-15__cap">Width comes from <code>--value</code>; the stripes slide inside it.</p>
      </section>

      <section class="pb-15__block" aria-labelledby="pb-15-h2">
        <p class="pb-15__blockHead"><span id="pb-15-h2">Indeterminate</span><span class="pb-15__mono">aria-busy="true"</span></p>
        <div class="pb-15__bar pb-15__bar--indet" role="progressbar" aria-busy="true" aria-valuemin="0" aria-valuemax="100" aria-label="Rebuilding search index">
          <span class="pb-15__fill"></span>
          <span class="pb-15__label pb-15__mono">Rebuilding search index&hellip;</span>
        </div>
        <p class="pb-15__cap">No <code>aria-valuenow</code> at all &mdash; the fill covers the whole track.</p>
      </section>

      <div class="pb-15__meta">
        <p class="pb-15__mono">--tile: 1.4rem &middot; 1s linear infinite</p>
        <p class="pb-15__mono">zero JavaScript</p>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.pb-15 {
  --bg: #0b0806;
  --card: #130d09;
  --ink: #fff4ec;
  --muted: rgba(255,244,236,.62);
  --line: rgba(255,244,236,.13);
  --track: rgba(255,244,236,.08);
  --accent: #fb923c;
  --accent-2: #f97316;
  --tile: 1.4rem;
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

@supports (color: oklch(76% .16 50)) {
  .pb-15 {
    --accent: oklch(78% .15 55);
    --accent-2: oklch(70% .18 45);
  }
}

.pb-15 *,
.pb-15 *::before,
.pb-15 *::after {
  box-sizing: border-box;
}

.pb-15__sr {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.pb-15__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pb-15__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(85% 60% at 10% 0%,color-mix(in srgb,var(--accent) 18%,transparent),transparent 60%);
}

.pb-15__theme {
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

.pb-15__theme:hover {
  transform: translateY(-1px);
  background: rgba(255,255,255,.12);
}

.pb-15__sr:focus-visible + .pb-15__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-15__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-15__sun {
  display: none;
}

.pb-15__moon {
  display: block;
}

.pb-15__card {
  inline-size: min(42rem,100%);
  display: grid;
  gap: clamp(1.1rem,2.6vw,1.7rem);
  padding: clamp(1.3rem,3.4vw,2.2rem);
  border-radius: 1.5rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--card) 92%,transparent);
  -webkit-backdrop-filter: blur(14px);
  backdrop-filter: blur(14px);
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset,0 32px 76px -44px rgba(0,0,0,.95);
}

.pb-15__head {
  display: grid;
  gap: .5rem;
}

.pb-15__eyebrow {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .55rem;
  align-items: center;
}

.pb-15__badge {
  font-family: var(--mono);
  font-size: .64rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  padding: .26rem .5rem;
  border-radius: .4rem;
  color: var(--accent);
  background: color-mix(in srgb,var(--accent) 15%,transparent);
  border: 1px solid color-mix(in srgb,var(--accent) 32%,transparent);
}

.pb-15__mono {
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pb-15__title {
  margin: 0;
  font-size: clamp(1.35rem,3.2vw,1.95rem);
  line-height: 1.14;
  letter-spacing: -.022em;
  font-weight: 650;
  text-wrap: balance;
}

.pb-15__lead {
  margin: 0;
  max-inline-size: 52ch;
  font-size: clamp(.9rem,1.5vw,1rem);
  line-height: 1.62;
  color: var(--muted);
  text-wrap: pretty;
}

.pb-15__block {
  display: grid;
  gap: .5rem;
}

.pb-15__blockHead {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
  align-items: baseline;
  justify-content: space-between;
  font-size: .85rem;
  font-weight: 600;
}

.pb-15__bar {
  position: relative;
  inline-size: 100%;
  block-size: 2.4rem;
  border-radius: .75rem;
  overflow: hidden;
  background: var(--track);
  border: 1px solid var(--line);
  box-shadow: 0 2px 4px rgba(0,0,0,.35) inset;
  display: grid;
  place-items: center;
}

.pb-15__fill {
  position: absolute;
  inset-block: 0;
  inset-inline-start: 0;
  inline-size: calc(var(--value,0) * 1%);
  background-color: var(--accent-2);
  background-image: repeating-linear-gradient(45deg,rgba(255,255,255,.24) 0 calc(var(--tile) / 2),transparent calc(var(--tile) / 2) var(--tile));
  background-size: var(--tile) var(--tile);
  background-repeat: repeat;
  animation: pb-15-slide 1s linear infinite;
  transition: inline-size .4s cubic-bezier(.4,0,.2,1);
}

@keyframes pb-15-slide {
  from {
    background-position: 0 0;
  }

  to {
    background-position: var(--tile) 0;
  }
}

.pb-15__bar--indet .pb-15__fill {
  inline-size: 100%;
  background-color: color-mix(in srgb,var(--accent-2) 55%,transparent);
  animation-duration: .85s;
}

.pb-15__label {
  position: relative;
  z-index: 1;
  padding: .2rem .6rem;
  border-radius: .45rem;
  font-size: .76rem;
  font-weight: 600;
  color: var(--ink);
  background: rgba(0,0,0,.42);
  -webkit-backdrop-filter: blur(4px);
  backdrop-filter: blur(4px);
}

.pb-15__cap {
  margin: 0;
  font-size: .78rem;
  color: var(--muted);
}

.pb-15__cap code {
  font-family: var(--mono);
  font-size: .85em;
  color: var(--accent);
}

.pb-15__meta {
  display: flex;
  flex-wrap: wrap;
  gap: .8rem;
  justify-content: space-between;
  padding-block-start: .4rem;
  border-block-start: 1px solid var(--line);
}

.pb-15__meta p {
  margin: 0;
  opacity: .75;
}

.pb-15[data-theme="light"],
.pb-15:has(#pb-15-light:checked) {
  --bg: #fdf7f2;
  --card: #ffffff;
  --ink: #1a0f07;
  --muted: rgba(26,15,7,.62);
  --line: rgba(26,15,7,.1);
  --track: rgba(26,15,7,.08);
  --accent: #ea580c;
  --accent-2: #c2410c;
}

.pb-15:has(#pb-15-light:checked) .pb-15__theme {
  background: rgba(26,15,7,.05);
}

.pb-15:has(#pb-15-light:checked) .pb-15__sun {
  display: block;
}

.pb-15:has(#pb-15-light:checked) .pb-15__moon {
  display: none;
}

.pb-15:has(#pb-15-light:checked) .pb-15__label {
  color: #fff;
  background: rgba(0,0,0,.5);
}

@media (prefers-color-scheme: light) {
  .pb-15:not([data-theme="dark"]):not(:has(#pb-15-light:checked)) {
    --bg: #fdf7f2;
    --card: #ffffff;
    --ink: #1a0f07;
    --muted: rgba(26,15,7,.62);
    --line: rgba(26,15,7,.1);
    --track: rgba(26,15,7,.08);
    --accent: #ea580c;
    --accent-2: #c2410c;
  }

  .pb-15:not([data-theme="dark"]):not(:has(#pb-15-light:checked)) .pb-15__theme {
    background: rgba(26,15,7,.05);
  }

  .pb-15:not([data-theme="dark"]):not(:has(#pb-15-light:checked)) .pb-15__sun {
    display: block;
  }

  .pb-15:not([data-theme="dark"]):not(:has(#pb-15-light:checked)) .pb-15__moon {
    display: none;
  }

  .pb-15:not([data-theme="dark"]):not(:has(#pb-15-light:checked)) .pb-15__label {
    color: #fff;
    background: rgba(0,0,0,.5);
  }

  .pb-15:not([data-theme="light"]):has(#pb-15-light:checked) {
    --bg: #0b0806;
    --card: #130d09;
    --ink: #fff4ec;
    --muted: rgba(255,244,236,.62);
    --line: rgba(255,244,236,.13);
    --track: rgba(255,244,236,.08);
    --accent: #fb923c;
    --accent-2: #f97316;
  }

  .pb-15:not([data-theme="light"]):has(#pb-15-light:checked) .pb-15__theme {
    background: rgba(255,255,255,.06);
  }

  .pb-15:not([data-theme="light"]):has(#pb-15-light:checked) .pb-15__sun {
    display: none;
  }

  .pb-15:not([data-theme="light"]):has(#pb-15-light:checked) .pb-15__moon {
    display: block;
  }

  .pb-15:not([data-theme="light"]):has(#pb-15-light:checked) .pb-15__label {
    color: var(--ink);
    background: rgba(0,0,0,.42);
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-15 *,
    .pb-15 *::before,
    .pb-15 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .pb-15__card,
    .pb-15__bar,
    .pb-15__theme {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  .pb-15__fill {
    background: Highlight;
  }

  .pb-15__label {
    background: Canvas;
    color: CanvasText;
    border: 1px solid CanvasText;
  }
}
```
