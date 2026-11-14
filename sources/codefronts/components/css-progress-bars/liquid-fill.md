---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/liquid-fill/"
title: "Liquid Fill Progress Bar for Storage and Quota Meters"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "A quota meter that fills like a vessel: two SVG wave layers drifting at different speeds over a rising liquid level, with the percentage set in the middle of…"
has_js: "false"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Liquid Fill Progress Bar for Storage and Quota Meters
Source: https://codefronts.com/components/css-progress-bars/liquid-fill/

A quota meter that fills like a vessel: two SVG wave layers drifting at different speeds over a rising liquid level, with the percentage set in the middle of the glass. Entirely CSS — the level is chosen by radio inputs, so there is no JavaScript at all.
## HTML
```html
<div class="pb-11">
  <input class="pb-11__sr" type="radio" name="pb-11-lvl" id="pb-11-r1">
  <input class="pb-11__sr" type="radio" name="pb-11-lvl" id="pb-11-r2" checked>
  <input class="pb-11__sr" type="radio" name="pb-11-lvl" id="pb-11-r3">
  <input class="pb-11__sr" type="radio" name="pb-11-lvl" id="pb-11-r4">

  <input class="pb-11__sr" type="checkbox" id="pb-11-light">
  <label class="pb-11__theme" for="pb-11-light" title="Switch light or dark theme">
    <svg class="pb-11__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-11__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="pb-11__vh">Switch light or dark theme</span>
  </label>

  <div class="pb-11__stage">
    <div class="pb-11__card">
      <header class="pb-11__head">
        <p class="pb-11__eyebrow"><span class="pb-11__badge">Storage</span><span class="pb-11__mono">team-workspace &middot; 20 GB plan</span></p>
        <h2 class="pb-11__title">Workspace quota</h2>
      </header>

      <div class="pb-11__vessel" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-label="Workspace storage used">
        <div class="pb-11__liquid">
          <svg class="pb-11__wave pb-11__wave--back" viewBox="0 0 1200 60" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path d="M0 30 C 150 8 250 8 300 30 C 350 52 450 52 600 30 C 750 8 850 8 900 30 C 950 52 1050 52 1200 30 V60 H0 Z" fill="currentColor"/></svg>
          <svg class="pb-11__wave pb-11__wave--front" viewBox="0 0 1200 60" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path d="M0 34 C 120 14 240 54 360 34 C 480 14 600 54 720 34 C 840 14 960 54 1080 34 C 1140 24 1170 26 1200 34 V60 H0 Z" fill="currentColor"/></svg>
        </div>
        <p class="pb-11__readout">
          <span class="pb-11__pct"><span class="pb-11__pctNum">64</span><span class="pb-11__pctSign">%</span></span>
          <span class="pb-11__bytes pb-11__mono">12.8 GB of 20 GB</span>
        </p>
      </div>

      <p class="pb-11__status">
        <span class="pb-11__statusIcon" aria-hidden="true">
          <svg class="pb-11__iconOk" viewBox="0 0 24 24" fill="none"><path d="M6 12.4l4 4L18.4 8" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <svg class="pb-11__iconWarn" viewBox="0 0 24 24" fill="none"><path d="M12 4.5l8.4 15H3.6z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/><path d="M12 10v3.6m0 2.4v.2" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></svg>
        </span>
        <span class="pb-11__statusText"></span>
      </p>

      <fieldset class="pb-11__levels">
        <legend class="pb-11__vh">Choose a storage level to preview</legend>
        <label class="pb-11__lvl" for="pb-11-r1">18%<span>3.6 GB</span></label>
        <label class="pb-11__lvl" for="pb-11-r2">64%<span>12.8 GB</span></label>
        <label class="pb-11__lvl" for="pb-11-r3">78%<span>15.7 GB</span></label>
        <label class="pb-11__lvl" for="pb-11-r4">96%<span>19.2 GB</span></label>
      </fieldset>
      <p class="pb-11__note pb-11__mono">zero JavaScript &mdash; level state lives in :has()</p>
    </div>
  </div>
</div>
```
## CSS
```css
.pb-11 {
  --bg: #04070c;
  --card: #0a0f18;
  --ink: #e9f4ff;
  --muted: rgba(233,244,255,.6);
  --line: rgba(233,244,255,.12);
  --glass: rgba(233,244,255,.06);
  --accent: #22d3ee;
  --accent-2: #38bdf8;
  --warn: #f59e0b;
  --err: #ef4444;
  --value: 64;
  --liquid: var(--accent);
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

@supports (color: oklch(80% .14 200)) {
  .pb-11 {
    --accent: oklch(82% .13 199);
    --accent-2: oklch(78% .13 220);
    --warn: oklch(78% .16 70);
    --err: oklch(64% .21 25);
  }
}

.pb-11 *,
.pb-11 *::before,
.pb-11 *::after {
  box-sizing: border-box;
}

.pb-11__sr {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.pb-11__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pb-11__stage {
  display: grid;
  place-items: center;
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(85% 60% at 50% -10%,color-mix(in srgb,var(--accent) 20%,transparent),transparent 62%);
}

.pb-11__theme {
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

.pb-11__theme:hover {
  transform: translateY(-1px);
  background: rgba(255,255,255,.12);
}

.pb-11__sr:focus-visible + .pb-11__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-11__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-11__sun {
  display: none;
}

.pb-11__moon {
  display: block;
}

.pb-11__card {
  inline-size: min(26rem,100%);
  display: grid;
  gap: clamp(.9rem,2.4vw,1.3rem);
  justify-items: center;
  padding: clamp(1.3rem,3.4vw,2rem);
  border-radius: 1.6rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--card) 92%,transparent);
  -webkit-backdrop-filter: blur(14px);
  backdrop-filter: blur(14px);
  box-shadow: 0 1px 0 rgba(255,255,255,.05) inset,0 34px 80px -44px rgba(0,0,0,.95);
}

.pb-11__head {
  display: grid;
  gap: .4rem;
  justify-items: center;
  text-align: center;
}

.pb-11__eyebrow {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  align-items: center;
  justify-content: center;
}

.pb-11__badge {
  font-family: var(--mono);
  font-size: .64rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  padding: .26rem .5rem;
  border-radius: .4rem;
  color: var(--accent);
  background: color-mix(in srgb,var(--accent) 14%,transparent);
  border: 1px solid color-mix(in srgb,var(--accent) 30%,transparent);
}

.pb-11__mono {
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pb-11__title {
  margin: 0;
  font-size: clamp(1.3rem,3.2vw,1.7rem);
  letter-spacing: -.02em;
  font-weight: 650;
}

.pb-11__vessel {
  position: relative;
  inline-size: min(13rem,60vw);
  aspect-ratio: 3 / 4;
  border-radius: 1.6rem;
  overflow: hidden;
  border: 1px solid color-mix(in srgb,var(--liquid) 34%,transparent);
  background: var(--glass);
  box-shadow: 0 0 0 1px rgba(255,255,255,.04) inset,0 20px 50px -30px color-mix(in srgb,var(--liquid) 60%,transparent);
}

.pb-11__vessel::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  border-radius: inherit;
  background: linear-gradient(115deg,rgba(255,255,255,.16),transparent 42%,transparent 70%,rgba(255,255,255,.07));
}

.pb-11__liquid {
  position: absolute;
  inset-inline: 0;
  inset-block-end: 0;
  block-size: calc(var(--value) * 1%);
  color: var(--liquid);
  background: color-mix(in srgb,var(--liquid) 72%,transparent);
  transition: block-size .55s cubic-bezier(.4,0,.2,1),background .4s;
}

.pb-11__wave {
  position: absolute;
  inset-block-start: -1.05rem;
  inset-inline-start: 0;
  inline-size: 200%;
  block-size: 1.4rem;
  will-change: transform;
}

.pb-11__wave--front {
  animation: pb-11-drift 7s linear infinite;
  opacity: .95;
}

.pb-11__wave--back {
  animation: pb-11-drift 11s linear infinite reverse;
  opacity: .5;
}

@keyframes pb-11-drift {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(-50%);
  }
}

.pb-11__readout {
  position: absolute;
  inset: 0;
  margin: 0;
  display: grid;
  place-content: center;
  gap: .15rem;
  text-align: center;
}

.pb-11__pct {
  display: flex;
  align-items: baseline;
  justify-content: center;
  gap: .1rem;
  font-family: var(--mono);
  font-weight: 600;
  letter-spacing: -.04em;
}

.pb-11__pctNum {
  font-size: clamp(2.6rem,9vw,3.4rem);
}

.pb-11__pctSign {
  font-size: 1.1rem;
  opacity: .7;
}

.pb-11__bytes {
  color: color-mix(in srgb,var(--ink) 82%,transparent);
}

.pb-11__status {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .5rem;
  font-size: .88rem;
  font-weight: 550;
}

.pb-11__statusIcon {
  inline-size: 1.2rem;
  block-size: 1.2rem;
  display: grid;
  place-items: center;
  color: var(--liquid);
}

.pb-11__statusIcon svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
  grid-area: 1/1;
  display: none;
}

.pb-11__iconOk {
  display: block;
}

.pb-11__levels {
  inline-size: 100%;
  margin: 0;
  padding: 0;
  border: 0;
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: .4rem;
}

.pb-11__lvl {
  display: grid;
  gap: .1rem;
  justify-items: center;
  padding: .5rem .3rem;
  border-radius: .7rem;
  cursor: pointer;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 4%,transparent);
  font-size: .8rem;
  font-weight: 600;
  font-family: var(--mono);
  transition: background .18s,border-color .18s,transform .18s;
}

.pb-11__lvl span {
  font-size: .62rem;
  font-weight: 400;
  color: var(--muted);
}

.pb-11__lvl:hover {
  transform: translateY(-1px);
  background: color-mix(in srgb,var(--ink) 9%,transparent);
}

.pb-11__note {
  margin: 0;
  opacity: .7;
}

.pb-11:has(#pb-11-r1:checked) {
  --value: 18;
  --liquid: var(--accent);
}

.pb-11:has(#pb-11-r2:checked) {
  --value: 64;
  --liquid: var(--accent-2);
}

.pb-11:has(#pb-11-r3:checked) {
  --value: 78;
  --liquid: var(--warn);
}

.pb-11:has(#pb-11-r4:checked) {
  --value: 96;
  --liquid: var(--err);
}

.pb-11:has(#pb-11-r1:checked) .pb-11__lvl[for="pb-11-r1"],
.pb-11:has(#pb-11-r2:checked) .pb-11__lvl[for="pb-11-r2"],
.pb-11:has(#pb-11-r3:checked) .pb-11__lvl[for="pb-11-r3"],
.pb-11:has(#pb-11-r4:checked) .pb-11__lvl[for="pb-11-r4"] {
  border-color: color-mix(in srgb,var(--liquid) 55%,transparent);
  background: color-mix(in srgb,var(--liquid) 15%,transparent);
  color: var(--ink);
}

.pb-11:has(#pb-11-r1:checked) .pb-11__pctNum::before {
  content: "18";
}

.pb-11:has(#pb-11-r2:checked) .pb-11__pctNum::before {
  content: "64";
}

.pb-11:has(#pb-11-r3:checked) .pb-11__pctNum::before {
  content: "78";
}

.pb-11:has(#pb-11-r4:checked) .pb-11__pctNum::before {
  content: "96";
}

.pb-11:has(.pb-11__sr:checked) .pb-11__pctNum {
  font-size: 0;
}

.pb-11:has(.pb-11__sr:checked) .pb-11__pctNum::before {
  font-size: clamp(2.6rem,9vw,3.4rem);
}

.pb-11:has(#pb-11-r1:checked) .pb-11__bytes::before {
  content: "3.6 GB of 20 GB";
}

.pb-11:has(#pb-11-r2:checked) .pb-11__bytes::before {
  content: "12.8 GB of 20 GB";
}

.pb-11:has(#pb-11-r3:checked) .pb-11__bytes::before {
  content: "15.7 GB of 20 GB";
}

.pb-11:has(#pb-11-r4:checked) .pb-11__bytes::before {
  content: "19.2 GB of 20 GB";
}

.pb-11:has(.pb-11__sr:checked) .pb-11__bytes {
  font-size: 0;
}

.pb-11:has(.pb-11__sr:checked) .pb-11__bytes::before {
  font-size: .72rem;
}

.pb-11:has(#pb-11-r1:checked) .pb-11__statusText::before {
  content: "Healthy — plenty of room";
}

.pb-11:has(#pb-11-r2:checked) .pb-11__statusText::before {
  content: "Healthy — 7.2 GB free";
}

.pb-11:has(#pb-11-r3:checked) .pb-11__statusText::before {
  content: "Getting full — 4.3 GB free";
}

.pb-11:has(#pb-11-r4:checked) .pb-11__statusText::before {
  content: "Almost out of space — 0.8 GB free";
}

.pb-11:has(#pb-11-r3:checked) .pb-11__iconOk,
.pb-11:has(#pb-11-r4:checked) .pb-11__iconOk {
  display: none;
}

.pb-11:has(#pb-11-r3:checked) .pb-11__iconWarn,
.pb-11:has(#pb-11-r4:checked) .pb-11__iconWarn {
  display: block;
}

.pb-11:has(#pb-11-r3:checked) .pb-11__status,
.pb-11:has(#pb-11-r4:checked) .pb-11__status {
  color: var(--liquid);
}

.pb-11[data-theme="light"],
.pb-11:has(#pb-11-light:checked) {
  --bg: #f2f7fb;
  --card: #ffffff;
  --ink: #08131f;
  --muted: rgba(8,19,31,.62);
  --line: rgba(8,19,31,.1);
  --glass: rgba(8,19,31,.04);
  --accent: #0891b2;
  --accent-2: #0284c7;
  --warn: #d97706;
  --err: #dc2626;
}

.pb-11:has(#pb-11-light:checked) .pb-11__theme {
  background: rgba(8,19,31,.05);
}

.pb-11:has(#pb-11-light:checked) .pb-11__sun {
  display: block;
}

.pb-11:has(#pb-11-light:checked) .pb-11__moon {
  display: none;
}

@media (prefers-color-scheme: light) {
  .pb-11:not([data-theme="dark"]):not(:has(#pb-11-light:checked)) {
    --bg: #f2f7fb;
    --card: #ffffff;
    --ink: #08131f;
    --muted: rgba(8,19,31,.62);
    --line: rgba(8,19,31,.1);
    --glass: rgba(8,19,31,.04);
    --accent: #0891b2;
    --accent-2: #0284c7;
    --warn: #d97706;
    --err: #dc2626;
  }

  .pb-11:not([data-theme="dark"]):not(:has(#pb-11-light:checked)) .pb-11__theme {
    background: rgba(8,19,31,.05);
  }

  .pb-11:not([data-theme="dark"]):not(:has(#pb-11-light:checked)) .pb-11__sun {
    display: block;
  }

  .pb-11:not([data-theme="dark"]):not(:has(#pb-11-light:checked)) .pb-11__moon {
    display: none;
  }

  .pb-11:not([data-theme="light"]):has(#pb-11-light:checked) {
    --bg: #04070c;
    --card: #0a0f18;
    --ink: #e9f4ff;
    --muted: rgba(233,244,255,.6);
    --line: rgba(233,244,255,.12);
    --glass: rgba(233,244,255,.06);
    --accent: #22d3ee;
    --accent-2: #38bdf8;
    --warn: #f59e0b;
    --err: #ef4444;
  }

  .pb-11:not([data-theme="light"]):has(#pb-11-light:checked) .pb-11__theme {
    background: rgba(255,255,255,.06);
  }

  .pb-11:not([data-theme="light"]):has(#pb-11-light:checked) .pb-11__sun {
    display: none;
  }

  .pb-11:not([data-theme="light"]):has(#pb-11-light:checked) .pb-11__moon {
    display: block;
  }
}

@supports not selector(:has(*)) {
  .pb-11__levels {
    display: none;
  }

  .pb-11__pctNum::before,
    .pb-11__bytes::before {
    content: none;
  }

  .pb-11__statusText::before {
    content: "Healthy — 7.2 GB free";
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-11 *,
    .pb-11 *::before,
    .pb-11 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .pb-11__card,
    .pb-11__vessel,
    .pb-11__lvl,
    .pb-11__theme {
    border-color: CanvasText;
    box-shadow: none;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  .pb-11__liquid {
    background: Highlight;
  }

  .pb-11__vessel::after {
    display: none;
  }
}
```
