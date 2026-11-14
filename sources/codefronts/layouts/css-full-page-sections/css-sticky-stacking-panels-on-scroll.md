---
source: "codefronts"
url: "https://codefronts.com/layouts/css-full-page-sections/css-sticky-stacking-panels-on-scroll/"
title: "CSS Sticky Stacking Panels on Scroll"
section: "layouts"
category: "css-full-page-sections"
category_name: "CSS Full Page Sections"
description: "Five full-height panels that pin at the top and stack over one another like a deck of sheets &mdash; each one parking 1.4&nbsp;rem lower than the last so…"
has_js: "false"
---

Here's a working CSS Full Page Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Sticky Stacking Panels on Scroll
Source: https://codefronts.com/layouts/css-full-page-sections/css-sticky-stacking-panels-on-scroll/

Five full-height panels that pin at the top and stack over one another like a deck of sheets &mdash; each one parking 1.4&nbsp;rem lower than the last so every previous panel keeps a visible tab. Built from position: sticky and a per-panel index variable, with no JavaScript and no scroll listeners, and it degrades to a plain scroller wherever sticky is unavailable.
## HTML
```html
<div class="fps-04">
  <input class="fps-04__sr" type="checkbox" id="fps-04-dark">
  <label class="fps-04__theme" for="fps-04-dark" title="Switch light or dark theme">
    <svg class="fps-04__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="fps-04__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="fps-04__vh">Switch light or dark theme</span>
  </label>

  <div class="fps-04__scroller" tabindex="0" role="group" aria-label="Stacking panel sequence, five panels">
    <div class="fps-04__stack">

      <section class="fps-04__panel" style="--i:0; --h:255" id="fps-04-s1" aria-labelledby="fps-04-h1">
        <div class="fps-04__stage">
          <p class="fps-04__eyebrow"><span class="fps-04__num">01 / 05</span><span class="fps-04__mono">position: sticky</span></p>
          <h2 class="fps-04__title" id="fps-04-h1">Panels that pin, then stack</h2>
          <p class="fps-04__lead">Scroll once. This panel stays where it is while the next sheet rides over it, parking 1.4&nbsp;rem lower so its edge stays on screen. Five sheets, one <code>position:sticky</code> rule, no scroll listeners.</p>
          <p class="fps-04__cue"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5v13.5M6.5 12.6 12 18.2l5.5-5.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Scroll to build the deck</p>
        </div>
      </section>

      <section class="fps-04__panel" style="--i:1; --h:200" id="fps-04-s2" aria-labelledby="fps-04-h2">
        <div class="fps-04__stage">
          <p class="fps-04__eyebrow"><span class="fps-04__num">02 / 05</span><span class="fps-04__mono">the containing block</span></p>
          <h2 class="fps-04__title fps-04__title--sm" id="fps-04-h2">Siblings in one wrapper stack. Nested ones do not.</h2>
          <p class="fps-04__lead">A sticky element stays pinned only while its own parent is on screen. Put all five panels in one wrapper and each stays pinned for the whole sequence &mdash; wrap each panel in its own box and every sheet unpins the moment its box scrolls away.</p>
          <ul class="fps-04__list">
            <li><strong>One wrapper</strong><span>All five pins persist. This is the stack.</span></li>
            <li><strong>One wrapper per panel</strong><span>Each pin dies with its box. This is a plain scroller.</span></li>
          </ul>
        </div>
      </section>

      <section class="fps-04__panel" style="--i:2; --h:160" id="fps-04-s3" aria-labelledby="fps-04-h3">
        <div class="fps-04__stage">
          <p class="fps-04__eyebrow"><span class="fps-04__num">03 / 05</span><span class="fps-04__mono">why proximity</span></p>
          <h2 class="fps-04__title fps-04__title--sm" id="fps-04-h3">Mandatory snapping fights a pinned panel</h2>
          <p class="fps-04__lead">A pinned panel's snap edge sits at the top of the scrollport permanently, so <code>mandatory</code> keeps pulling the scroll back to it. <code>proximity</code> snaps only when the reader comes to rest near an edge &mdash; which is exactly what a stack wants.</p>
          <pre class="fps-04__code"><code>.scroller{ scroll-snap-type:y <mark>proximity</mark>; }
.panel  { scroll-snap-align:start; }</code></pre>
        </div>
      </section>

      <section class="fps-04__panel" style="--i:3; --h:95" id="fps-04-s4" aria-labelledby="fps-04-h4">
        <div class="fps-04__stage">
          <p class="fps-04__eyebrow"><span class="fps-04__num">04 / 05</span><span class="fps-04__mono">the silent killer</span></p>
          <h2 class="fps-04__title fps-04__title--sm" id="fps-04-h4">Six ancestor properties that break sticky</h2>
          <ul class="fps-04__grid">
            <li><code>overflow:hidden</code></li>
            <li><code>overflow:clip</code></li>
            <li><code>transform</code></li>
            <li><code>filter</code></li>
            <li><code>contain:paint</code></li>
            <li><code>will-change:transform</code></li>
          </ul>
          <p class="fps-04__lead">Any one of these on any ancestor changes the containing block or the scrollport, and the panel stops pinning with no console warning of any kind. If a stack refuses to pin, walk up the tree and delete exactly one of the six.</p>
        </div>
      </section>

      <section class="fps-04__panel" style="--i:4; --h:30" id="fps-04-s5" aria-labelledby="fps-04-h5">
        <div class="fps-04__stage">
          <p class="fps-04__eyebrow"><span class="fps-04__num">05 / 05</span><span class="fps-04__mono">the deck, complete</span></p>
          <h2 class="fps-04__title fps-04__title--sm" id="fps-04-h5">Five sheets, one index variable</h2>
          <p class="fps-04__lead">Pin offset, panel height, shadow depth and dimming all read from the same <code>--i</code> on each section. Add a sixth panel, give it <code>--i:5</code>, and the whole effect extends itself.</p>
          <p class="fps-04__quote">&ldquo;The stack replaced three scroll listeners and a resize observer on our case-study template.&rdquo;<span>Jordan Lee &middot; design engineer</span></p>
        </div>
      </section>

    </div>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fps-04 {
  --bg: #f4f6f8;
  --ink: #0b1014;
  --muted: rgba(11,16,20,.62);
  --line: rgba(11,16,20,.10);
  --accent: #0d9488;
  --step: 1.4rem;
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
}

@supports (color: oklch(50% .1 250)) {
  .fps-04 {
    --accent: oklch(56% .12 185);
    --ink: oklch(14% .015 220);
    --bg: oklch(96.5% .006 220);
  }
}

.fps-04 * {
  box-sizing: border-box;
}

.fps-04 h2,
.fps-04 p,
.fps-04 ul,
.fps-04 pre {
  margin: 0;
}

.fps-04 code {
  font-family: var(--mono);
  font-size: .92em;
}

.fps-04__sr,
.fps-04__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.fps-04__theme {
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
  background: rgba(255,255,255,.6);
  border: 1px solid var(--line);
  -webkit-backdrop-filter: blur(10px) saturate(150%);
  backdrop-filter: blur(10px) saturate(150%);
  box-shadow: 0 8px 24px -12px rgba(11,16,20,.35);
}

.fps-04__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.fps-04__theme svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.fps-04__moon {
  display: none;
}

.fps-04__sr:focus-visible + .fps-04__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fps-04__scroller {
  block-size: 100dvh;
  overflow-y: auto;
  overflow-x: hidden;
  scroll-snap-type: y proximity;
  scroll-behavior: smooth;
  overscroll-behavior-y: contain;
  scrollbar-width: none;
}

.fps-04__scroller::-webkit-scrollbar {
  width: 0;
  height: 0;
}

.fps-04__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.fps-04__stack {
  position: relative;
}

.fps-04__panel {
  position: sticky;
  inset-block-start: calc(var(--i) * var(--step));
  min-block-size: calc(100dvh - var(--i) * var(--step));
  scroll-snap-align: start;
  z-index: calc(var(--i) + 1);
  isolation: isolate;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(2rem,5vh,3.5rem) clamp(1.25rem,5vw,4.5rem) clamp(2.5rem,6vh,4rem);
  border-start-start-radius: 1.9rem;
  border-start-end-radius: 1.9rem;
  border-block-start: 1px solid var(--line);
  background: hsl(var(--h) 42% 97%);
  box-shadow: 0 -22px 50px -26px rgba(11,16,20,.28);
}

@supports (background: oklch(90% .05 40)) {
  .fps-04__panel {
    background: oklch(97% .022 calc(var(--h) * 1deg));
  }
}

.fps-04__panel::after {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  border-radius: inherit;
  background: var(--ink);
  opacity: calc(var(--i) * .012);
}

@supports not (position: sticky) {
  .fps-04__panel {
    position: relative;
    min-block-size: 100dvh;
    inset-block-start: auto;
  }
}

@supports not (height: 100dvh) {
  .fps-04__scroller {
    block-size: 100vh;
  }

  .fps-04__panel {
    min-block-size: calc(100vh - var(--i) * var(--step));
  }
}

.fps-04__stage {
  inline-size: min(60rem,100%);
  display: grid;
  gap: clamp(.9rem,2.2vh,1.4rem);
  justify-items: start;
}

.fps-04__eyebrow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .7rem;
}

.fps-04__num {
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: hsl(var(--h) 55% 34%);
}

@supports (color: oklch(40% .1 40)) {
  .fps-04__num {
    color: oklch(48% .13 calc(var(--h) * 1deg));
  }
}

.fps-04__mono {
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--muted);
  padding: .22rem .5rem;
  border: 1px solid var(--line);
  border-radius: .45rem;
}

.fps-04__title {
  font-size: clamp(2rem,5.6vw,4rem);
  line-height: 1.03;
  letter-spacing: -.04em;
  font-weight: 600;
  max-inline-size: 20ch;
  text-wrap: balance;
}

.fps-04__title--sm {
  font-size: clamp(1.65rem,3.6vw,2.6rem);
  letter-spacing: -.03em;
  max-inline-size: 28ch;
}

.fps-04__lead {
  font-size: clamp(.98rem,1.35vw,1.14rem);
  line-height: 1.6;
  color: var(--muted);
  max-inline-size: 58ch;
  text-wrap: pretty;
}

.fps-04__cue {
  display: flex;
  align-items: center;
  gap: .55rem;
  font-family: var(--mono);
  font-size: .82rem;
  color: var(--muted);
}

.fps-04__cue svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  animation: fps-04-bob 2.4s ease-in-out infinite;
}

@keyframes fps-04-bob {
  0%,
    100% {
    translate: 0 -2px;
  }

  50% {
    translate: 0 3px;
  }
}

.fps-04__list {
  list-style: none;
  padding: 0;
  display: grid;
  gap: .5rem;
  inline-size: 100%;
}

.fps-04__list li {
  display: grid;
  gap: .15rem;
  padding: .85rem 0;
  border-block-start: 1px solid var(--line);
}

.fps-04__list strong {
  font-family: var(--mono);
  font-size: .82rem;
  letter-spacing: .02em;
  font-weight: 500;
}

.fps-04__list span {
  font-size: .94rem;
  color: var(--muted);
}

.fps-04__grid {
  list-style: none;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(11rem,1fr));
  gap: .5rem;
  inline-size: 100%;
}

.fps-04__grid li {
  padding: .7rem .85rem;
  border-radius: .8rem;
  border: 1px solid var(--line);
  background: rgba(255,255,255,.6);
  font-family: var(--mono);
  font-size: .82rem;
}

.fps-04__code {
  padding: 1rem 1.1rem;
  border-radius: 1rem;
  border: 1px solid var(--line);
  background: rgba(255,255,255,.6);
  overflow-x: auto;
}

.fps-04__code code {
  font-size: clamp(.78rem,1vw,.88rem);
  line-height: 1.7;
  color: var(--muted);
  white-space: pre;
}

.fps-04__code mark {
  background: color-mix(in srgb,var(--accent) 16%,transparent);
  color: var(--accent);
  border-radius: .25rem;
  padding: .05rem .2rem;
}

.fps-04__quote {
  font-size: clamp(1.05rem,1.9vw,1.35rem);
  line-height: 1.45;
  letter-spacing: -.02em;
  max-inline-size: 44ch;
  padding-inline-start: 1.05rem;
  border-inline-start: 2px solid var(--accent);
  display: grid;
  gap: .55rem;
  text-wrap: pretty;
}

.fps-04__quote span {
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.fps-04[data-theme="dark"],
.fps-04:has(#fps-04-dark:checked) {
  --bg: #05080a;
  --ink: #eef4f6;
  --muted: rgba(238,244,246,.62);
  --line: rgba(238,244,246,.13);
  --accent: #5eead4;
}

.fps-04:has(#fps-04-dark:checked) .fps-04__theme {
  background: rgba(255,255,255,.07);
}

.fps-04:has(#fps-04-dark:checked) .fps-04__sun {
  display: none;
}

.fps-04:has(#fps-04-dark:checked) .fps-04__moon {
  display: block;
}

.fps-04:has(#fps-04-dark:checked) .fps-04__panel {
  background: hsl(var(--h) 34% 8%);
  box-shadow: 0 -22px 50px -26px rgba(0,0,0,.8);
}

.fps-04:has(#fps-04-dark:checked) .fps-04__panel::after {
  background: #000;
  opacity: calc(var(--i) * .05);
}

.fps-04:has(#fps-04-dark:checked) .fps-04__num {
  color: hsl(var(--h) 70% 76%);
}

.fps-04:has(#fps-04-dark:checked) .fps-04__grid li,
.fps-04:has(#fps-04-dark:checked) .fps-04__code {
  background: rgba(255,255,255,.05);
}

@media (prefers-color-scheme: dark) {
  .fps-04:not([data-theme="light"]):not(:has(#fps-04-dark:checked)) {
    --bg: #05080a;
    --ink: #eef4f6;
    --muted: rgba(238,244,246,.62);
    --line: rgba(238,244,246,.13);
    --accent: #5eead4;
  }

  .fps-04:not([data-theme="light"]):not(:has(#fps-04-dark:checked)) .fps-04__theme {
    background: rgba(255,255,255,.07);
  }

  .fps-04:not([data-theme="light"]):not(:has(#fps-04-dark:checked)) .fps-04__sun {
    display: none;
  }

  .fps-04:not([data-theme="light"]):not(:has(#fps-04-dark:checked)) .fps-04__moon {
    display: block;
  }

  .fps-04:not([data-theme="light"]):not(:has(#fps-04-dark:checked)) .fps-04__panel {
    background: hsl(var(--h) 34% 8%);
    box-shadow: 0 -22px 50px -26px rgba(0,0,0,.8);
  }

  .fps-04:not([data-theme="light"]):not(:has(#fps-04-dark:checked)) .fps-04__panel::after {
    background: #000;
    opacity: calc(var(--i) * .05);
  }

  .fps-04:not([data-theme="light"]):not(:has(#fps-04-dark:checked)) .fps-04__num {
    color: hsl(var(--h) 70% 76%);
  }

  .fps-04:not([data-theme="light"]):not(:has(#fps-04-dark:checked)) .fps-04__grid li,
    .fps-04:not([data-theme="light"]):not(:has(#fps-04-dark:checked)) .fps-04__code {
    background: rgba(255,255,255,.05);
  }
}

@supports (background: oklch(10% .02 40)) {
  .fps-04:has(#fps-04-dark:checked) .fps-04__panel {
    background: oklch(17% .028 calc(var(--h) * 1deg));
  }

  .fps-04:has(#fps-04-dark:checked) .fps-04__num {
    color: oklch(82% .13 calc(var(--h) * 1deg));
  }
}

@supports not selector(:has(*)) {
  .fps-04__theme {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fps-04__scroller {
    scroll-snap-type: none;
    scroll-behavior: auto;
  }

  .fps-04 *,
    .fps-04 *::before,
    .fps-04 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fps-04__panel,
    .fps-04__grid li,
    .fps-04__code,
    .fps-04__theme {
    border: 1px solid CanvasText;
    box-shadow: none;
    background: Canvas;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  .fps-04__panel::after {
    display: none;
  }
}
```
