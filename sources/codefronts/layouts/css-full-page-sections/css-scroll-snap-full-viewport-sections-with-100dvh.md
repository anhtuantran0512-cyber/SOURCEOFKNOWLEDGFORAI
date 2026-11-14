---
source: "codefronts"
url: "https://codefronts.com/layouts/css-full-page-sections/css-scroll-snap-full-viewport-sections-with-100dvh/"
title: "CSS Scroll Snap Full Viewport Sections with 100dvh"
section: "layouts"
category: "css-full-page-sections"
category_name: "CSS Full Page Sections"
description: "The reference build for the whole collection: four snapping full-viewport panels sized with 100dvh, plus a fourth panel deliberately built on 100vh so you…"
has_js: "false"
---

Here's a working CSS Full Page Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Scroll Snap Full Viewport Sections with 100dvh
Source: https://codefronts.com/layouts/css-full-page-sections/css-scroll-snap-full-viewport-sections-with-100dvh/

The reference build for the whole collection: four snapping full-viewport panels sized with 100dvh, plus a fourth panel deliberately built on 100vh so you can see the mobile bug it causes. A side-by-side device diagram shows exactly what the collapsing address bar does to vh, and a unit table settles dvh vs svh vs lvh once and for all.
## HTML
```html
<div class="fps-01">
  <input class="fps-01__sr" type="checkbox" id="fps-01-dark">
  <label class="fps-01__theme" for="fps-01-dark" title="Switch light or dark theme">
    <svg class="fps-01__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="fps-01__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="fps-01__vh">Switch light or dark theme</span>
  </label>

  <div class="fps-01__scroller" tabindex="0" role="group" aria-label="Full viewport section scroller, four panels">

    <section class="fps-01__panel" id="fps-01-s1" aria-labelledby="fps-01-h1">
      <div class="fps-01__stage">
        <p class="fps-01__eyebrow"><span class="fps-01__num">01 / 04</span><span class="fps-01__mono">min-block-size: 100dvh</span></p>
        <h2 class="fps-01__title" id="fps-01-h1">Panels that fill the screen &mdash; and keep filling it</h2>
        <p class="fps-01__lead">Four snapping sections, one owned scroll container, zero JavaScript. Every panel is exactly as tall as the visible viewport, so the snap position never drifts when a mobile toolbar slides away.</p>
        <ul class="fps-01__chips">
          <li class="fps-01__chip fps-01__chip--on">100dvh<span>tracks the live viewport</span></li>
          <li class="fps-01__chip">100svh<span>toolbars shown</span></li>
          <li class="fps-01__chip">100lvh<span>toolbars hidden</span></li>
        </ul>
        <p class="fps-01__cue"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5v13.5M6.5 12.6 12 18.2l5.5-5.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Scroll &mdash; the next panel&rsquo;s edge is already showing</p>
      </div>
    </section>

    <section class="fps-01__panel fps-01__panel--diagram" id="fps-01-s2" aria-labelledby="fps-01-h2">
      <div class="fps-01__stage">
        <p class="fps-01__eyebrow"><span class="fps-01__num">02 / 04</span><span class="fps-01__mono">the address-bar problem</span></p>
        <h2 class="fps-01__title fps-01__title--sm" id="fps-01-h2">What the collapsing toolbar actually does</h2>
        <div class="fps-01__devices">
          <figure class="fps-01__device fps-01__device--bad">
            <div class="fps-01__screen">
              <span class="fps-01__bar">codefronts.com</span>
              <div class="fps-01__fill fps-01__fill--over"><span>100vh</span></div>
              <span class="fps-01__clip">bottom 96px under the toolbar</span>
            </div>
            <figcaption>Legacy <code>100vh</code> resolves against the <em>large</em> viewport. The panel is taller than the screen from the first paint.</figcaption>
          </figure>
          <figure class="fps-01__device fps-01__device--good">
            <div class="fps-01__screen">
              <span class="fps-01__bar">codefronts.com</span>
              <div class="fps-01__fill"><span>100dvh</span></div>
            </div>
            <figcaption><code>100dvh</code> measures what the user can see right now, and re-measures as the browser chrome moves.</figcaption>
          </figure>
        </div>
      </div>
    </section>

    <section class="fps-01__panel" id="fps-01-s3" aria-labelledby="fps-01-h3">
      <div class="fps-01__stage">
        <p class="fps-01__eyebrow"><span class="fps-01__num">03 / 04</span><span class="fps-01__mono">unit reference</span></p>
        <h2 class="fps-01__title fps-01__title--sm" id="fps-01-h3">Which viewport unit, and when</h2>
        <dl class="fps-01__table">
          <div class="fps-01__row"><dt>100dvh</dt><dd><strong>Snapping panels.</strong> Height follows the live viewport, so panel height and scrollport height stay equal while toolbars animate.</dd></div>
          <div class="fps-01__row"><dt>100svh</dt><dd><strong>Panels with pinned bottom chrome.</strong> Always the short measurement, so a sticky action bar is never swallowed by the browser UI.</dd></div>
          <div class="fps-01__row"><dt>100lvh</dt><dd><strong>Decorative full-bleed art.</strong> Intentionally taller than the screen; fine for a background image, wrong for a snap target.</dd></div>
          <div class="fps-01__row fps-01__row--warn"><dt>100vh</dt><dd><strong>Legacy.</strong> Identical to <code>lvh</code>. Keep it only inside <code>@supports not (height:100dvh)</code> as the fallback.</dd></div>
        </dl>
      </div>
    </section>

    <section class="fps-01__panel fps-01__panel--broken" id="fps-01-s4" aria-labelledby="fps-01-h4">
      <div class="fps-01__stage">
        <p class="fps-01__eyebrow"><span class="fps-01__num">04 / 04</span><span class="fps-01__mono fps-01__mono--warn">min-height: 100vh &middot; labelled comparison</span></p>
        <h2 class="fps-01__title fps-01__title--sm" id="fps-01-h4">This panel is the broken one</h2>
        <p class="fps-01__lead">It is the only panel in the collection sized with <code>100vh</code>. On a desktop it looks identical. Open the demo on an iPhone and this panel overshoots the screen: its footer line hides behind the address bar, and the snap edge lands mid-sentence.</p>
        <p class="fps-01__foot">Bottom line of panel 04 &mdash; visible here, hidden on iOS Safari.</p>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fps-01 {
  --bg: #f7f8fa;
  --panel: #ffffff;
  --panel2: #eef1f6;
  --ink: #0c0e14;
  --muted: rgba(12,14,20,.62);
  --line: rgba(12,14,20,.10);
  --accent: #2563eb;
  --accent-ink: #ffffff;
  --warn: #b45309;
  --warn-soft: rgba(180,83,9,.10);
  --shadow: 0 -34px 70px -34px rgba(12,14,20,.20);
  --sans: 'Geist',system-ui,-apple-system,'Segoe UI',sans-serif;
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  isolation: isolate;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}

@supports (color: oklch(50% .1 250)) {
  .fps-01 {
    --accent: oklch(58% .19 258);
    --warn: oklch(56% .13 62);
    --ink: oklch(16% .015 265);
    --bg: oklch(97.4% .004 265);
    --panel2: oklch(95% .008 265);
  }
}

.fps-01 * {
  box-sizing: border-box;
}

.fps-01 h2,
.fps-01 p,
.fps-01 dl,
.fps-01 dd,
.fps-01 figure,
.fps-01 figcaption {
  margin: 0;
}

.fps-01 code {
  font-family: var(--mono);
  font-size: .92em;
}

.fps-01__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.fps-01__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.fps-01__theme {
  position: fixed;
  inset-block-start: 1.15rem;
  inset-inline-end: 1.15rem;
  z-index: 80;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  border-radius: 999px;
  cursor: pointer;
  color: var(--ink);
  background: rgba(255,255,255,.62);
  border: 1px solid var(--line);
  -webkit-backdrop-filter: blur(10px) saturate(150%);
  backdrop-filter: blur(10px) saturate(150%);
  box-shadow: 0 8px 24px -12px rgba(12,14,20,.35);
}

.fps-01__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.fps-01__theme svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.fps-01__moon {
  display: none;
}

.fps-01__sr:focus-visible + .fps-01__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fps-01__scroller {
  block-size: 100dvh;
  overflow-y: auto;
  overflow-x: hidden;
  scroll-snap-type: y mandatory;
  scroll-behavior: smooth;
  overscroll-behavior-y: contain;
  scrollbar-width: none;
}

.fps-01__scroller::-webkit-scrollbar {
  width: 0;
  height: 0;
}

.fps-01__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.fps-01__panel {
  position: relative;
  min-block-size: 100dvh;
  scroll-snap-align: start;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(2rem,5vh,3.75rem) clamp(1.25rem,5vw,4.5rem) calc(clamp(2rem,5vh,3.75rem) + 4.5rem);
  background: var(--panel);
}

.fps-01__panel:nth-child(even) {
  background: var(--panel2);
}

.fps-01__panel + .fps-01__panel {
  margin-block-start: -4.5rem;
  border-start-start-radius: 2rem;
  border-start-end-radius: 2rem;
  border-block-start: 1px solid var(--line);
  box-shadow: var(--shadow);
}

@supports not (height: 100dvh) {
  .fps-01__scroller {
    block-size: 100vh;
  }

  .fps-01__panel {
    min-block-size: 100vh;
  }
}

.fps-01__panel--broken {
  min-block-size: 100vh;
  background: var(--warn-soft);
}

.fps-01__stage {
  inline-size: min(64rem,100%);
  display: grid;
  gap: clamp(1rem,2.4vh,1.6rem);
  justify-items: start;
}

.fps-01__eyebrow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .7rem;
}

.fps-01__num {
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
  font-weight: 500;
}

.fps-01__mono {
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .04em;
  color: var(--muted);
  padding: .22rem .5rem;
  border: 1px solid var(--line);
  border-radius: .45rem;
}

.fps-01__mono--warn {
  color: var(--warn);
  border-color: color-mix(in srgb,var(--warn) 40%,transparent);
}

.fps-01__title {
  font-size: clamp(2.1rem,6.2vw,4.5rem);
  line-height: 1.02;
  letter-spacing: -.04em;
  font-weight: 600;
  max-inline-size: 22ch;
  text-wrap: balance;
}

.fps-01__title--sm {
  font-size: clamp(1.75rem,4vw,2.9rem);
  letter-spacing: -.03em;
  max-inline-size: 26ch;
}

.fps-01__lead {
  font-size: clamp(1rem,1.5vw,1.2rem);
  line-height: 1.55;
  color: var(--muted);
  max-inline-size: 56ch;
  text-wrap: pretty;
}

.fps-01__lead code {
  color: var(--ink);
}

.fps-01__chips {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .6rem;
}

.fps-01__chip {
  display: grid;
  gap: .15rem;
  padding: .6rem .85rem;
  border-radius: .85rem;
  border: 1px solid var(--line);
  font-family: var(--mono);
  font-size: .9rem;
  background: color-mix(in srgb,var(--ink) 3%,transparent);
}

.fps-01__chip span {
  font-family: var(--sans);
  font-size: .72rem;
  color: var(--muted);
  letter-spacing: 0;
}

.fps-01__chip--on {
  border-color: var(--accent);
  color: var(--accent);
  background: color-mix(in srgb,var(--accent) 8%,transparent);
}

.fps-01__chip--on span {
  color: color-mix(in srgb,var(--accent) 75%,var(--ink));
}

.fps-01__cue {
  display: flex;
  align-items: center;
  gap: .55rem;
  font-size: .85rem;
  color: var(--muted);
  font-family: var(--mono);
}

.fps-01__cue svg {
  inline-size: 1.1rem;
  block-size: 1.1rem;
  animation: fps-01-bob 2.4s ease-in-out infinite;
}

@keyframes fps-01-bob {
  0%,
    100% {
    translate: 0 -2px;
  }

  50% {
    translate: 0 3px;
  }
}

.fps-01__devices {
  display: grid;
  gap: clamp(1rem,3vw,2rem);
  grid-template-columns: repeat(auto-fit,minmax(15rem,1fr));
  inline-size: 100%;
}

.fps-01__device {
  display: grid;
  gap: .85rem;
}

.fps-01__screen {
  position: relative;
  block-size: clamp(11rem,26vh,16rem);
  border-radius: 1.4rem;
  overflow: hidden;
  border: 1px solid var(--line);
  background: var(--panel);
  box-shadow: 0 22px 44px -28px rgba(12,14,20,.45);
  display: grid;
  grid-template-rows: auto 1fr;
}

.fps-01__bar {
  font-family: var(--mono);
  font-size: .62rem;
  color: var(--muted);
  padding: .5rem .75rem;
  border-block-end: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 4%,transparent);
}

.fps-01__fill {
  display: grid;
  place-items: center;
  font-family: var(--mono);
  font-size: 1.1rem;
  font-weight: 500;
  background: color-mix(in srgb,var(--accent) 12%,transparent);
  color: var(--accent);
  border-block-start: 2px solid var(--accent);
}

.fps-01__fill--over {
  background: repeating-linear-gradient(135deg,var(--warn-soft) 0 10px,transparent 10px 20px),color-mix(in srgb,var(--warn) 10%,transparent);
  color: var(--warn);
  border-block-start-color: var(--warn);
  translate: 0 0;
  block-size: calc(100% + 2.4rem);
}

.fps-01__clip {
  position: absolute;
  inset-inline: 0;
  inset-block-end: 0;
  padding: .45rem .7rem;
  font-family: var(--mono);
  font-size: .6rem;
  color: var(--accent-ink);
  background: var(--warn);
  text-align: center;
}

.fps-01__device figcaption {
  font-size: .86rem;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.fps-01__table {
  inline-size: 100%;
  display: grid;
  gap: .5rem;
}

.fps-01__row {
  display: grid;
  grid-template-columns: minmax(5.5rem,7rem) 1fr;
  gap: clamp(.75rem,2vw,1.75rem);
  align-items: start;
  padding: clamp(.8rem,1.6vh,1.1rem) 0;
  border-block-start: 1px solid var(--line);
}

.fps-01__row dt {
  font-family: var(--mono);
  font-size: .95rem;
  color: var(--accent);
}

.fps-01__row dd {
  font-size: .98rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.fps-01__row dd strong {
  color: var(--ink);
  font-weight: 550;
}

.fps-01__row--warn dt {
  color: var(--warn);
}

.fps-01__foot {
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--warn);
  padding-block-start: .6rem;
  border-block-start: 1px dashed color-mix(in srgb,var(--warn) 45%,transparent);
}

.fps-01[data-theme="dark"],
.fps-01:has(#fps-01-dark:checked) {
  --bg: #07080b;
  --panel: #0b0d12;
  --panel2: #11141b;
  --ink: #f2f4f9;
  --muted: rgba(242,244,249,.62);
  --line: rgba(242,244,249,.13);
  --accent: #7dd3fc;
  --accent-ink: #06111c;
  --warn: #fbbf24;
  --warn-soft: rgba(251,191,36,.09);
  --shadow: 0 -34px 70px -34px rgba(0,0,0,.7);
}

.fps-01:has(#fps-01-dark:checked) .fps-01__theme {
  background: rgba(255,255,255,.07);
}

.fps-01:has(#fps-01-dark:checked) .fps-01__sun {
  display: none;
}

.fps-01:has(#fps-01-dark:checked) .fps-01__moon {
  display: block;
}

.fps-01:has(#fps-01-dark:checked) .fps-01__clip {
  color: #1c1305;
}

@media (prefers-color-scheme: dark) {
  .fps-01:not([data-theme="light"]):not(:has(#fps-01-dark:checked)) {
    --bg: #07080b;
    --panel: #0b0d12;
    --panel2: #11141b;
    --ink: #f2f4f9;
    --muted: rgba(242,244,249,.62);
    --line: rgba(242,244,249,.13);
    --accent: #7dd3fc;
    --accent-ink: #06111c;
    --warn: #fbbf24;
    --warn-soft: rgba(251,191,36,.09);
    --shadow: 0 -34px 70px -34px rgba(0,0,0,.7);
  }

  .fps-01:not([data-theme="light"]):not(:has(#fps-01-dark:checked)) .fps-01__theme {
    background: rgba(255,255,255,.07);
  }

  .fps-01:not([data-theme="light"]):not(:has(#fps-01-dark:checked)) .fps-01__sun {
    display: none;
  }

  .fps-01:not([data-theme="light"]):not(:has(#fps-01-dark:checked)) .fps-01__moon {
    display: block;
  }

  .fps-01:not([data-theme="light"]):not(:has(#fps-01-dark:checked)) .fps-01__clip {
    color: #1c1305;
  }
}

@supports not selector(:has(*)) {
  .fps-01__theme {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fps-01__scroller {
    scroll-snap-type: none;
    scroll-behavior: auto;
  }

  .fps-01 *,
    .fps-01 *::before,
    .fps-01 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fps-01__panel,
    .fps-01__chip,
    .fps-01__screen,
    .fps-01__theme,
    .fps-01__mono {
    border-color: CanvasText;
    box-shadow: none;
    background: Canvas;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  .fps-01__fill,
    .fps-01__fill--over {
    background: Canvas;
    color: CanvasText;
  }
}
```
