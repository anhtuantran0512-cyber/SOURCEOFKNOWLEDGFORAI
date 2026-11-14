---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/segmented-battery/"
title: "Segmented Battery Style Progress Bar"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "A ten-cell battery meter that changes character with its charge: accent above 30%, amber from 10 to 30, red below, with a lightning bolt and a cell-by-cell…"
has_js: "false"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Segmented Battery Style Progress Bar
Source: https://codefronts.com/components/css-progress-bars/segmented-battery/

A ten-cell battery meter that changes character with its charge: accent above 30%, amber from 10 to 30, red below, with a lightning bolt and a cell-by-cell charging animation. Colour never travels alone — every state also writes its own label.
## HTML
```html
<div class="pb-14">
  <input class="pb-14__sr" type="radio" name="pb-14-l" id="pb-14-l8">
  <input class="pb-14__sr" type="radio" name="pb-14-l" id="pb-14-l6" checked>
  <input class="pb-14__sr" type="radio" name="pb-14-l" id="pb-14-l2">
  <input class="pb-14__sr" type="radio" name="pb-14-l" id="pb-14-l1">
  <input class="pb-14__sr" type="checkbox" id="pb-14-charge">
  <input class="pb-14__sr" type="checkbox" id="pb-14-light">
  <label class="pb-14__theme" for="pb-14-light" title="Switch light or dark theme">
    <svg class="pb-14__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-14__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="pb-14__vh">Switch light or dark theme</span>
  </label>

  <div class="pb-14__stage">
    <div class="pb-14__card">
      <header class="pb-14__head">
        <p class="pb-14__eyebrow"><span class="pb-14__badge">Power</span><span class="pb-14__mono">MacBook Air &middot; 15in</span></p>
        <p class="pb-14__readout"><span class="pb-14__pct"></span><span class="pb-14__remain"></span></p>
      </header>

      <div class="pb-14__batteryWrap">
        <div class="pb-14__shell" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-label="Battery level">
          <span class="pb-14__cells">
            <i class="pb-14__cell"></i><i class="pb-14__cell"></i><i class="pb-14__cell"></i><i class="pb-14__cell"></i><i class="pb-14__cell"></i>
            <i class="pb-14__cell"></i><i class="pb-14__cell"></i><i class="pb-14__cell"></i><i class="pb-14__cell"></i><i class="pb-14__cell"></i>
          </span>
          <svg class="pb-14__bolt" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M13.4 2.8 6.2 13.4h4.6L10 21.2l7.4-10.8h-4.7z" fill="currentColor" stroke="currentColor" stroke-width="1.1" stroke-linejoin="round"/></svg>
        </div>
      </div>

      <p class="pb-14__status">
        <span class="pb-14__statusIcon" aria-hidden="true">
          <svg class="pb-14__iOk" viewBox="0 0 24 24" fill="none"><path d="M6 12.4l4 4L18.4 8" stroke="currentColor" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <svg class="pb-14__iLow" viewBox="0 0 24 24" fill="none"><path d="M12 4.5l8.4 15H3.6z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M12 10v3.6m0 2.4v.2" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
          <svg class="pb-14__iBolt" viewBox="0 0 24 24" fill="none"><path d="M13.4 2.8 6.2 13.4h4.6L10 21.2l7.4-10.8h-4.7z" fill="currentColor"/></svg>
        </span>
        <span class="pb-14__statusText"></span>
      </p>

      <div class="pb-14__controls">
        <fieldset class="pb-14__levels">
          <legend class="pb-14__vh">Battery level</legend>
          <label class="pb-14__lvl" for="pb-14-l8">82%</label>
          <label class="pb-14__lvl" for="pb-14-l6">62%</label>
          <label class="pb-14__lvl" for="pb-14-l2">18%</label>
          <label class="pb-14__lvl" for="pb-14-l1">6%</label>
        </fieldset>
        <label class="pb-14__toggle" for="pb-14-charge">
          <svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M13.4 2.8 6.2 13.4h4.6L10 21.2l7.4-10.8h-4.7z" fill="currentColor"/></svg>
          <span>Charging</span>
        </label>
      </div>
      <p class="pb-14__note pb-14__mono">colour band + label &mdash; never colour alone</p>
    </div>
  </div>
</div>
```
## CSS
```css
.pb-14 {
  --bg: #06080a;
  --card: #0b0f13;
  --ink: #eaf2ee;
  --muted: rgba(234,242,238,.58);
  --line: rgba(234,242,238,.24);
  --track: rgba(234,242,238,.09);
  --ok: #34d399;
  --warn: #f59e0b;
  --err: #ef4444;
  --fill: var(--ok);
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

@supports (color: oklch(78% .15 162)) {
  .pb-14 {
    --ok: oklch(78% .15 162);
    --warn: oklch(78% .16 70);
    --err: oklch(64% .21 25);
  }
}

.pb-14 *,
.pb-14 *::before,
.pb-14 *::after {
  box-sizing: border-box;
}

.pb-14__sr {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.pb-14__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pb-14__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(80% 55% at 50% -5%,color-mix(in srgb,var(--fill) 16%,transparent),transparent 60%);
}

.pb-14__theme {
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

.pb-14__theme:hover {
  transform: translateY(-1px);
  background: rgba(255,255,255,.12);
}

.pb-14__sr:focus-visible + .pb-14__theme {
  outline: 2px solid var(--fill);
  outline-offset: 3px;
}

.pb-14__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-14__sun {
  display: none;
}

.pb-14__moon {
  display: block;
}

.pb-14__card {
  inline-size: min(34rem,100%);
  display: grid;
  gap: clamp(1rem,2.4vw,1.5rem);
  justify-items: center;
  padding: clamp(1.4rem,3.4vw,2.2rem);
  border-radius: 1.6rem;
  border: 1px solid rgba(255,255,255,.09);
  background: color-mix(in srgb,var(--card) 92%,transparent);
  -webkit-backdrop-filter: blur(14px);
  backdrop-filter: blur(14px);
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset,0 34px 80px -44px rgba(0,0,0,.95);
}

.pb-14__head {
  display: grid;
  gap: .5rem;
  justify-items: center;
  text-align: center;
}

.pb-14__eyebrow {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  align-items: center;
  justify-content: center;
}

.pb-14__badge {
  font-family: var(--mono);
  font-size: .64rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  padding: .26rem .5rem;
  border-radius: .4rem;
  color: var(--fill);
  background: color-mix(in srgb,var(--fill) 14%,transparent);
  border: 1px solid color-mix(in srgb,var(--fill) 30%,transparent);
}

.pb-14__mono {
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pb-14__readout {
  margin: 0;
  display: flex;
  align-items: baseline;
  gap: .6rem;
  flex-wrap: wrap;
  justify-content: center;
}

.pb-14__pct {
  font-family: var(--mono);
  font-size: clamp(2.4rem,8vw,3.4rem);
  font-weight: 600;
  letter-spacing: -.04em;
  font-variant-numeric: tabular-nums;
}

.pb-14__remain {
  font-size: .85rem;
  color: var(--muted);
}

.pb-14__batteryWrap {
  inline-size: 100%;
  display: grid;
  place-items: center;
  padding-inline: .5rem;
}

.pb-14__shell {
  position: relative;
  inline-size: min(22rem,100%);
  block-size: clamp(3.4rem,11vw,4.4rem);
  border: 2px solid var(--line);
  border-radius: .85rem;
  padding: .32rem;
  background: color-mix(in srgb,var(--ink) 4%,transparent);
  box-shadow: 0 2px 4px rgba(0,0,0,.35) inset,0 0 0 4px rgba(255,255,255,.02);
}

.pb-14__shell::after {
  content: "";
  position: absolute;
  inset-block-start: 32%;
  inset-inline-start: 100%;
  inline-size: .36rem;
  block-size: 36%;
  border-radius: 0 .22rem .22rem 0;
  background: var(--line);
}

.pb-14__cells {
  display: grid;
  grid-template-columns: repeat(10,1fr);
  gap: .22rem;
  block-size: 100%;
}

.pb-14__cell {
  border-radius: .24rem;
  background: var(--track);
  transition: background .3s cubic-bezier(.4,0,.2,1);
}

.pb-14__bolt {
  position: absolute;
  inset: 0;
  margin: auto;
  inline-size: 2rem;
  block-size: 2rem;
  color: #04140d;
  opacity: 0;
  filter: drop-shadow(0 0 6px rgba(255,255,255,.55));
  transition: opacity .25s;
}

.pb-14__status {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .5rem;
  font-size: .9rem;
  font-weight: 550;
  color: var(--fill);
}

.pb-14__statusIcon {
  inline-size: 1.2rem;
  block-size: 1.2rem;
  display: grid;
  place-items: center;
}

.pb-14__statusIcon svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
  grid-area: 1/1;
  display: none;
}

.pb-14__iOk {
  display: block;
}

.pb-14__controls {
  inline-size: 100%;
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
  align-items: center;
  justify-content: space-between;
}

.pb-14__levels {
  margin: 0;
  padding: 0;
  border: 0;
  display: flex;
  gap: .35rem;
  flex-wrap: wrap;
}

.pb-14__lvl {
  min-block-size: 2.5rem;
  display: grid;
  place-items: center;
  padding: .5rem .85rem;
  border-radius: .7rem;
  cursor: pointer;
  border: 1px solid rgba(255,255,255,.12);
  background: color-mix(in srgb,var(--ink) 5%,transparent);
  font-family: var(--mono);
  font-size: .8rem;
  font-weight: 600;
  transition: background .18s,border-color .18s,transform .18s;
}

.pb-14__lvl:hover {
  transform: translateY(-1px);
  background: color-mix(in srgb,var(--ink) 11%,transparent);
}

.pb-14__toggle {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-block-size: 2.5rem;
  padding: .5rem .9rem;
  border-radius: .7rem;
  cursor: pointer;
  border: 1px solid rgba(255,255,255,.12);
  background: color-mix(in srgb,var(--ink) 5%,transparent);
  font-size: .82rem;
  font-weight: 600;
  transition: background .18s,border-color .18s,color .18s;
}

.pb-14__toggle svg {
  inline-size: .95rem;
  block-size: .95rem;
}

.pb-14__note {
  margin: 0;
  opacity: .7;
}

.pb-14:has(#pb-14-l8:checked) {
  --fill: var(--ok);
}

.pb-14:has(#pb-14-l6:checked) {
  --fill: var(--ok);
}

.pb-14:has(#pb-14-l2:checked) {
  --fill: var(--warn);
}

.pb-14:has(#pb-14-l1:checked) {
  --fill: var(--err);
}

.pb-14:has(#pb-14-l8:checked) .pb-14__cell:nth-child(-n+8),
.pb-14:has(#pb-14-l6:checked) .pb-14__cell:nth-child(-n+6),
.pb-14:has(#pb-14-l2:checked) .pb-14__cell:nth-child(-n+2),
.pb-14:has(#pb-14-l1:checked) .pb-14__cell:nth-child(-n+1) {
  background: var(--fill);
}

.pb-14:has(#pb-14-l8:checked) .pb-14__pct::before {
  content: "82%";
}

.pb-14:has(#pb-14-l6:checked) .pb-14__pct::before {
  content: "62%";
}

.pb-14:has(#pb-14-l2:checked) .pb-14__pct::before {
  content: "18%";
}

.pb-14:has(#pb-14-l1:checked) .pb-14__pct::before {
  content: "6%";
}

.pb-14:has(#pb-14-l8:checked) .pb-14__remain::before {
  content: "about 6 hr 20 min left";
}

.pb-14:has(#pb-14-l6:checked) .pb-14__remain::before {
  content: "about 4 hr 45 min left";
}

.pb-14:has(#pb-14-l2:checked) .pb-14__remain::before {
  content: "about 40 min left";
}

.pb-14:has(#pb-14-l1:checked) .pb-14__remain::before {
  content: "about 12 min left";
}

.pb-14:has(#pb-14-l8:checked) .pb-14__statusText::before,
.pb-14:has(#pb-14-l6:checked) .pb-14__statusText::before {
  content: "Healthy";
}

.pb-14:has(#pb-14-l2:checked) .pb-14__statusText::before {
  content: "Low — charge soon";
}

.pb-14:has(#pb-14-l1:checked) .pb-14__statusText::before {
  content: "Critical — connect power now";
}

.pb-14:has(#pb-14-l2:checked) .pb-14__iOk,
.pb-14:has(#pb-14-l1:checked) .pb-14__iOk {
  display: none;
}

.pb-14:has(#pb-14-l2:checked) .pb-14__iLow,
.pb-14:has(#pb-14-l1:checked) .pb-14__iLow {
  display: block;
}

.pb-14:has(#pb-14-l8:checked) .pb-14__lvl[for="pb-14-l8"],
.pb-14:has(#pb-14-l6:checked) .pb-14__lvl[for="pb-14-l6"],
.pb-14:has(#pb-14-l2:checked) .pb-14__lvl[for="pb-14-l2"],
.pb-14:has(#pb-14-l1:checked) .pb-14__lvl[for="pb-14-l1"] {
  border-color: color-mix(in srgb,var(--fill) 55%,transparent);
  background: color-mix(in srgb,var(--fill) 16%,transparent);
}

.pb-14:has(#pb-14-charge:checked) .pb-14__toggle {
  border-color: color-mix(in srgb,var(--fill) 55%,transparent);
  background: color-mix(in srgb,var(--fill) 16%,transparent);
  color: var(--fill);
}

.pb-14:has(#pb-14-charge:checked) .pb-14__bolt {
  opacity: 1;
}

.pb-14:has(#pb-14-charge:checked) .pb-14__statusText::before {
  content: "Charging — power adapter connected";
}

.pb-14:has(#pb-14-charge:checked) .pb-14__iOk,
.pb-14:has(#pb-14-charge:checked) .pb-14__iLow {
  display: none;
}

.pb-14:has(#pb-14-charge:checked) .pb-14__iBolt {
  display: block;
}

@keyframes pb-14-charge {
  0%,
    100% {
    opacity: .3;
  }

  50% {
    opacity: 1;
  }
}

.pb-14:has(#pb-14-charge:checked) .pb-14__cell {
  animation: pb-14-charge 1.7s ease-in-out infinite;
}

.pb-14:has(#pb-14-charge:checked) .pb-14__cell:nth-child(1) {
  animation-delay: 0s;
}

.pb-14:has(#pb-14-charge:checked) .pb-14__cell:nth-child(2) {
  animation-delay: .09s;
}

.pb-14:has(#pb-14-charge:checked) .pb-14__cell:nth-child(3) {
  animation-delay: .18s;
}

.pb-14:has(#pb-14-charge:checked) .pb-14__cell:nth-child(4) {
  animation-delay: .27s;
}

.pb-14:has(#pb-14-charge:checked) .pb-14__cell:nth-child(5) {
  animation-delay: .36s;
}

.pb-14:has(#pb-14-charge:checked) .pb-14__cell:nth-child(6) {
  animation-delay: .45s;
}

.pb-14:has(#pb-14-charge:checked) .pb-14__cell:nth-child(7) {
  animation-delay: .54s;
}

.pb-14:has(#pb-14-charge:checked) .pb-14__cell:nth-child(8) {
  animation-delay: .63s;
}

.pb-14:has(#pb-14-charge:checked) .pb-14__cell:nth-child(9) {
  animation-delay: .72s;
}

.pb-14:has(#pb-14-charge:checked) .pb-14__cell:nth-child(10) {
  animation-delay: .81s;
}

.pb-14[data-theme="light"],
.pb-14:has(#pb-14-light:checked) {
  --bg: #f3f6f4;
  --card: #ffffff;
  --ink: #0a1410;
  --muted: rgba(10,20,16,.6);
  --line: rgba(10,20,16,.28);
  --track: rgba(10,20,16,.09);
  --ok: #059669;
  --warn: #d97706;
  --err: #dc2626;
}

.pb-14:has(#pb-14-light:checked) .pb-14__card {
  border-color: rgba(10,20,16,.1);
}

.pb-14:has(#pb-14-light:checked) .pb-14__theme {
  background: rgba(10,20,16,.05);
}

.pb-14:has(#pb-14-light:checked) .pb-14__sun {
  display: block;
}

.pb-14:has(#pb-14-light:checked) .pb-14__moon {
  display: none;
}

.pb-14:has(#pb-14-light:checked) .pb-14__bolt {
  color: #f8fffb;
}

@media (prefers-color-scheme: light) {
  .pb-14:not([data-theme="dark"]):not(:has(#pb-14-light:checked)) {
    --bg: #f3f6f4;
    --card: #ffffff;
    --ink: #0a1410;
    --muted: rgba(10,20,16,.6);
    --line: rgba(10,20,16,.28);
    --track: rgba(10,20,16,.09);
    --ok: #059669;
    --warn: #d97706;
    --err: #dc2626;
  }

  .pb-14:not([data-theme="dark"]):not(:has(#pb-14-light:checked)) .pb-14__card {
    border-color: rgba(10,20,16,.1);
  }

  .pb-14:not([data-theme="dark"]):not(:has(#pb-14-light:checked)) .pb-14__theme {
    background: rgba(10,20,16,.05);
  }

  .pb-14:not([data-theme="dark"]):not(:has(#pb-14-light:checked)) .pb-14__sun {
    display: block;
  }

  .pb-14:not([data-theme="dark"]):not(:has(#pb-14-light:checked)) .pb-14__moon {
    display: none;
  }

  .pb-14:not([data-theme="dark"]):not(:has(#pb-14-light:checked)) .pb-14__bolt {
    color: #f8fffb;
  }

  .pb-14:not([data-theme="light"]):has(#pb-14-light:checked) {
    --bg: #06080a;
    --card: #0b0f13;
    --ink: #eaf2ee;
    --muted: rgba(234,242,238,.58);
    --line: rgba(234,242,238,.24);
    --track: rgba(234,242,238,.09);
    --ok: #34d399;
    --warn: #f59e0b;
    --err: #ef4444;
  }

  .pb-14:not([data-theme="light"]):has(#pb-14-light:checked) .pb-14__card {
    border-color: rgba(255,255,255,.09);
  }

  .pb-14:not([data-theme="light"]):has(#pb-14-light:checked) .pb-14__theme {
    background: rgba(255,255,255,.06);
  }

  .pb-14:not([data-theme="light"]):has(#pb-14-light:checked) .pb-14__sun {
    display: none;
  }

  .pb-14:not([data-theme="light"]):has(#pb-14-light:checked) .pb-14__moon {
    display: block;
  }

  .pb-14:not([data-theme="light"]):has(#pb-14-light:checked) .pb-14__bolt {
    color: #04140d;
  }
}

@supports not selector(:has(*)) {
  .pb-14__controls {
    display: none;
  }

  .pb-14__cell:nth-child(-n+6) {
    background: var(--ok);
  }

  .pb-14__pct::before {
    content: "62%";
  }

  .pb-14__remain::before {
    content: "about 4 hr 45 min left";
  }

  .pb-14__statusText::before {
    content: "Healthy";
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-14 *,
    .pb-14 *::before,
    .pb-14 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .pb-14__card,
    .pb-14__shell,
    .pb-14__lvl,
    .pb-14__toggle,
    .pb-14__theme {
    border-color: CanvasText;
    box-shadow: none;
  }

  .pb-14__cell {
    background: Canvas;
    border: 1px solid CanvasText;
  }

  .pb-14:has(#pb-14-l8:checked) .pb-14__cell:nth-child(-n+8),
    .pb-14:has(#pb-14-l6:checked) .pb-14__cell:nth-child(-n+6),
    .pb-14:has(#pb-14-l2:checked) .pb-14__cell:nth-child(-n+2),
    .pb-14:has(#pb-14-l1:checked) .pb-14__cell:nth-child(-n+1) {
    background: Highlight;
  }
}
```
