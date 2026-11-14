---
source: "codefronts"
url: "https://codefronts.com/components/css-progress-bars/conic-ring/"
title: "Conic Gradient Ring Progress Indicator"
section: "components"
category: "css-progress-bars"
category_name: "CSS Progress Bars"
description: "Circular progress with no SVG at all: one conic-gradient whose sweep angle is calc(var(--value) * 3.6deg), made animatable by registering --value with…"
has_js: "false"
---

Here's a working CSS Progress Bar from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Conic Gradient Ring Progress Indicator
Source: https://codefronts.com/components/css-progress-bars/conic-ring/

Circular progress with no SVG at all: one conic-gradient whose sweep angle is calc(var(--value) * 3.6deg), made animatable by registering --value with @property. Three sizes from the same six declarations.
## HTML
```html
<div class="pb-13">
  <input class="pb-13__sr" type="radio" name="pb-13-v" id="pb-13-v1">
  <input class="pb-13__sr" type="radio" name="pb-13-v" id="pb-13-v2" checked>
  <input class="pb-13__sr" type="radio" name="pb-13-v" id="pb-13-v3">
  <input class="pb-13__sr" type="checkbox" id="pb-13-light">
  <label class="pb-13__theme" for="pb-13-light" title="Switch light or dark theme">
    <svg class="pb-13__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="pb-13__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="pb-13__vh">Switch light or dark theme</span>
  </label>

  <div class="pb-13__stage">
    <header class="pb-13__intro">
      <p class="pb-13__eyebrow"><span class="pb-13__badge">Conic</span><span class="pb-13__mono">calc(var(--value) * 3.6deg)</span></p>
      <h2 class="pb-13__title">A ring with no SVG</h2>
      <p class="pb-13__lead">One gradient, one registered custom property, three sizes. The sweep transitions because <code>@property</code> gave <code>--value</code> a type.</p>
    </header>

    <div class="pb-13__rings">
      <figure class="pb-13__item" style="--size:5.5rem; --thick:.55rem">
        <div class="pb-13__ring" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-label="Move goal">
          <span class="pb-13__hole"><span class="pb-13__num"></span></span>
        </div>
        <figcaption class="pb-13__cap">Move<span class="pb-13__mono">small</span></figcaption>
      </figure>
      <figure class="pb-13__item pb-13__item--mid" style="--size:8.5rem; --thick:.8rem">
        <div class="pb-13__ring" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-label="Exercise goal">
          <span class="pb-13__hole"><span class="pb-13__num"></span></span>
        </div>
        <figcaption class="pb-13__cap">Exercise<span class="pb-13__mono">medium</span></figcaption>
      </figure>
      <figure class="pb-13__item" style="--size:11.5rem; --thick:1.05rem">
        <div class="pb-13__ring" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-label="Stand goal">
          <span class="pb-13__hole"><span class="pb-13__num"></span></span>
        </div>
        <figcaption class="pb-13__cap">Stand<span class="pb-13__mono">large</span></figcaption>
      </figure>
    </div>

    <fieldset class="pb-13__vals">
      <legend class="pb-13__vh">Choose a value</legend>
      <label class="pb-13__val" for="pb-13-v1">32%</label>
      <label class="pb-13__val" for="pb-13-v2">68%</label>
      <label class="pb-13__val" for="pb-13-v3">100%</label>
    </fieldset>
    <p class="pb-13__note pb-13__mono" id="pb-13-note">no script &mdash; :has() sets --value, @property animates it</p>
  </div>
</div>
```
## CSS
```css
@property --pb13-value {
  syntax: '<number>';
  initial-value: 0;
  inherits: true;
}

.pb-13 {
  --bg: #0a0710;
  --card: #100b1a;
  --ink: #f4eeff;
  --muted: rgba(244,238,255,.6);
  --line: rgba(244,238,255,.12);
  --track: rgba(244,238,255,.1);
  --accent: #c084fc;
  --accent-2: #f472b6;
  --pb13-value: 68;
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

@supports (color: oklch(78% .18 310)) {
  .pb-13 {
    --accent: oklch(78% .18 310);
    --accent-2: oklch(74% .18 350);
  }
}

.pb-13 *,
.pb-13 *::before,
.pb-13 *::after {
  box-sizing: border-box;
}

.pb-13__sr {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.pb-13__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.pb-13__stage {
  display: grid;
  place-items: center;
  align-content: center;
  gap: clamp(1.2rem,3vw,2rem);
  min-block-size: 100vh;
  padding: clamp(1.1rem,4vw,3.5rem);
  background: radial-gradient(85% 60% at 50% -5%,color-mix(in srgb,var(--accent) 20%,transparent),transparent 62%), radial-gradient(60% 50% at 90% 100%,color-mix(in srgb,var(--accent-2) 16%,transparent),transparent 60%);
}

.pb-13__theme {
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

.pb-13__theme:hover {
  transform: translateY(-1px);
  background: rgba(255,255,255,.12);
}

.pb-13__sr:focus-visible + .pb-13__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.pb-13__theme svg {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.pb-13__sun {
  display: none;
}

.pb-13__moon {
  display: block;
}

.pb-13__intro {
  inline-size: min(40rem,100%);
  display: grid;
  gap: .5rem;
  justify-items: center;
  text-align: center;
}

.pb-13__eyebrow {
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .55rem;
  align-items: center;
  justify-content: center;
}

.pb-13__badge {
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

.pb-13__mono {
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.pb-13__title {
  margin: 0;
  font-size: clamp(1.5rem,4vw,2.3rem);
  letter-spacing: -.026em;
  font-weight: 650;
}

.pb-13__lead {
  margin: 0;
  max-inline-size: 46ch;
  font-size: clamp(.9rem,1.5vw,1rem);
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.pb-13__lead code {
  font-family: var(--mono);
  font-size: .85em;
  color: var(--accent);
}

.pb-13__rings {
  display: flex;
  flex-wrap: wrap;
  gap: clamp(1.2rem,4vw,2.6rem);
  align-items: flex-end;
  justify-content: center;
}

.pb-13__item {
  margin: 0;
  display: grid;
  gap: .7rem;
  justify-items: center;
}

.pb-13__ring {
  position: relative;
  inline-size: var(--size);
  block-size: var(--size);
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: conic-gradient(from -90deg,var(--accent) 0 calc(var(--pb13-value) * 3.6deg),var(--track) 0);
  box-shadow: 0 20px 45px -28px color-mix(in srgb,var(--accent) 65%,transparent);
}

.pb-13__item--mid .pb-13__ring {
  background: conic-gradient(from -90deg,var(--accent-2) 0 calc(var(--pb13-value) * 3.6deg),var(--track) 0);
}

.pb-13__hole {
  position: absolute;
  inset: var(--thick);
  border-radius: 50%;
  display: grid;
  place-items: center;
  background: var(--card);
  box-shadow: 0 0 0 1px rgba(255,255,255,.05) inset;
}

.pb-13__num {
  font-family: var(--mono);
  font-weight: 600;
  letter-spacing: -.03em;
  font-size: calc(var(--size) / 4.6);
  font-variant-numeric: tabular-nums;
}

.pb-13__num::after {
  content: "%";
  font-size: .5em;
  opacity: .6;
  margin-inline-start: .05em;
}

.pb-13__cap {
  display: grid;
  gap: .1rem;
  justify-items: center;
  font-size: .85rem;
  font-weight: 600;
}

.pb-13__vals {
  margin: 0;
  padding: 0;
  border: 0;
  display: flex;
  gap: .45rem;
  flex-wrap: wrap;
  justify-content: center;
}

.pb-13__val {
  min-block-size: 2.5rem;
  display: grid;
  place-items: center;
  padding: .55rem 1.05rem;
  border-radius: .75rem;
  cursor: pointer;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 5%,transparent);
  font-family: var(--mono);
  font-size: .82rem;
  font-weight: 600;
  transition: background .18s,border-color .18s,transform .18s;
}

.pb-13__val:hover {
  transform: translateY(-1px);
  background: color-mix(in srgb,var(--ink) 11%,transparent);
}

.pb-13__note {
  margin: 0;
  opacity: .75;
}

.pb-13:has(#pb-13-v1:checked) {
  --pb13-value: 32;
}

.pb-13:has(#pb-13-v2:checked) {
  --pb13-value: 68;
}

.pb-13:has(#pb-13-v3:checked) {
  --pb13-value: 100;
}

.pb-13:has(#pb-13-v1:checked) .pb-13__num::before {
  content: "32";
}

.pb-13:has(#pb-13-v2:checked) .pb-13__num::before {
  content: "68";
}

.pb-13:has(#pb-13-v3:checked) .pb-13__num::before {
  content: "100";
}

.pb-13:has(#pb-13-v1:checked) .pb-13__val[for="pb-13-v1"],
.pb-13:has(#pb-13-v2:checked) .pb-13__val[for="pb-13-v2"],
.pb-13:has(#pb-13-v3:checked) .pb-13__val[for="pb-13-v3"] {
  border-color: color-mix(in srgb,var(--accent) 55%,transparent);
  background: color-mix(in srgb,var(--accent) 16%,transparent);
}

@supports (transition: --pb13-value 1s) {
  .pb-13 {
    transition: --pb13-value .6s cubic-bezier(.4,0,.2,1);
  }
}

.pb-13[data-theme="light"],
.pb-13:has(#pb-13-light:checked) {
  --bg: #f8f5fd;
  --card: #ffffff;
  --ink: #170c26;
  --muted: rgba(23,12,38,.62);
  --line: rgba(23,12,38,.1);
  --track: rgba(23,12,38,.09);
  --accent: #9333ea;
  --accent-2: #db2777;
}

.pb-13:has(#pb-13-light:checked) .pb-13__theme {
  background: rgba(23,12,38,.05);
}

.pb-13:has(#pb-13-light:checked) .pb-13__sun {
  display: block;
}

.pb-13:has(#pb-13-light:checked) .pb-13__moon {
  display: none;
}

@media (prefers-color-scheme: light) {
  .pb-13:not([data-theme="dark"]):not(:has(#pb-13-light:checked)) {
    --bg: #f8f5fd;
    --card: #ffffff;
    --ink: #170c26;
    --muted: rgba(23,12,38,.62);
    --line: rgba(23,12,38,.1);
    --track: rgba(23,12,38,.09);
    --accent: #9333ea;
    --accent-2: #db2777;
  }

  .pb-13:not([data-theme="dark"]):not(:has(#pb-13-light:checked)) .pb-13__theme {
    background: rgba(23,12,38,.05);
  }

  .pb-13:not([data-theme="dark"]):not(:has(#pb-13-light:checked)) .pb-13__sun {
    display: block;
  }

  .pb-13:not([data-theme="dark"]):not(:has(#pb-13-light:checked)) .pb-13__moon {
    display: none;
  }

  .pb-13:not([data-theme="light"]):has(#pb-13-light:checked) {
    --bg: #0a0710;
    --card: #100b1a;
    --ink: #f4eeff;
    --muted: rgba(244,238,255,.6);
    --line: rgba(244,238,255,.12);
    --track: rgba(244,238,255,.1);
    --accent: #c084fc;
    --accent-2: #f472b6;
  }

  .pb-13:not([data-theme="light"]):has(#pb-13-light:checked) .pb-13__theme {
    background: rgba(255,255,255,.06);
  }

  .pb-13:not([data-theme="light"]):has(#pb-13-light:checked) .pb-13__sun {
    display: none;
  }

  .pb-13:not([data-theme="light"]):has(#pb-13-light:checked) .pb-13__moon {
    display: block;
  }
}

@supports not selector(:has(*)) {
  .pb-13__vals {
    display: none;
  }

  .pb-13__num::before {
    content: "68";
  }
}

@media (prefers-reduced-motion: reduce) {
  .pb-13,
    .pb-13 *,
    .pb-13 *::before,
    .pb-13 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .pb-13__ring {
    background: Canvas;
    border: 2px solid CanvasText;
    box-shadow: none;
  }

  .pb-13__hole,
    .pb-13__val,
    .pb-13__theme {
    border: 1px solid CanvasText;
    background: Canvas;
  }
}
```
