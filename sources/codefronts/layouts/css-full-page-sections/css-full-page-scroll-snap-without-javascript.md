---
source: "codefronts"
url: "https://codefronts.com/layouts/css-full-page-sections/css-full-page-scroll-snap-without-javascript/"
title: "CSS Full Page Scroll Snap Without JavaScript"
section: "layouts"
category: "css-full-page-sections"
category_name: "CSS Full Page Sections"
description: "The library replacement: a four-section one-page scroller built from three CSS declarations and nothing else &mdash; no fullpage.js, no observers, no…"
has_js: "false"
---

Here's a working CSS Full Page Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Full Page Scroll Snap Without JavaScript
Source: https://codefronts.com/layouts/css-full-page-sections/css-full-page-scroll-snap-without-javascript/

The library replacement: a four-section one-page scroller built from three CSS declarations and nothing else &mdash; no fullpage.js, no observers, no 60&nbsp;kB of script. A side rail of anchor links jumps between sections using native scroll-behavior, and an honest trade-off panel lists exactly which library features you give up.
## HTML
```html
<div class="fps-02">
  <input class="fps-02__sr" type="checkbox" id="fps-02-dark">
  <label class="fps-02__theme" for="fps-02-dark" title="Switch light or dark theme">
    <svg class="fps-02__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="fps-02__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="fps-02__vh">Switch light or dark theme</span>
  </label>

  <nav class="fps-02__rail" aria-label="Section links">
    <a href="#fps-02-s1"><span class="fps-02__rn">01</span><span class="fps-02__rl">Overview</span></a>
    <a href="#fps-02-s2"><span class="fps-02__rn">02</span><span class="fps-02__rl">The three rules</span></a>
    <a href="#fps-02-s3"><span class="fps-02__rn">03</span><span class="fps-02__rl">Trade-offs</span></a>
    <a href="#fps-02-s4"><span class="fps-02__rn">04</span><span class="fps-02__rl">Ship it</span></a>
  </nav>

  <div class="fps-02__scroller" tabindex="0" role="group" aria-label="One page scroller, four sections">

    <section class="fps-02__panel" id="fps-02-s1" aria-labelledby="fps-02-h1">
      <div class="fps-02__stage fps-02__stage--split">
        <div class="fps-02__col">
          <p class="fps-02__eyebrow"><span class="fps-02__num">01 / 04</span><span class="fps-02__mono">0&nbsp;kB of JavaScript</span></p>
          <h2 class="fps-02__title" id="fps-02-h1">A one-page scroller with nothing to install</h2>
          <p class="fps-02__lead">Full-viewport sections, native momentum, smooth anchor jumps, working back button. Everything a full-page scrolling library gives you, minus the library &mdash; and minus the scroll hijacking that breaks trackpads.</p>
          <ul class="fps-02__facts">
            <li><strong>3</strong><span>CSS declarations</span></li>
            <li><strong>0</strong><span>dependencies</span></li>
            <li><strong>0</strong><span>wheel listeners</span></li>
          </ul>
        </div>
        <aside class="fps-02__code" aria-label="Core CSS">
          <p class="fps-02__codehead">the entire engine</p>
          <pre><code>.scroller{
  block-size:100dvh;
  overflow-y:auto;
  <mark>scroll-snap-type:y mandatory;</mark>
  scroll-behavior:smooth;
}
.panel{
  min-block-size:100dvh;
  <mark>scroll-snap-align:start;</mark>
}</code></pre>
        </aside>
      </div>
    </section>

    <section class="fps-02__panel" id="fps-02-s2" aria-labelledby="fps-02-h2">
      <div class="fps-02__stage">
        <p class="fps-02__eyebrow"><span class="fps-02__num">02 / 04</span><span class="fps-02__mono">how it works</span></p>
        <h2 class="fps-02__title fps-02__title--sm" id="fps-02-h2">Three rules, in the order they matter</h2>
        <ol class="fps-02__steps">
          <li>
            <p class="fps-02__sh"><span>01</span>Own the scrollport</p>
            <p class="fps-02__sp">A container with <code>overflow-y:auto</code> and <code>block-size:100dvh</code>. Snapping applies to the element that scrolls, so it must be yours &mdash; never <code>html</code>.</p>
          </li>
          <li>
            <p class="fps-02__sh"><span>02</span>Declare the snap axis</p>
            <p class="fps-02__sp"><code>scroll-snap-type:y mandatory</code>. The compositor now lands the scroll on the nearest snap point on its own thread, off the main thread entirely.</p>
          </li>
          <li>
            <p class="fps-02__sh"><span>03</span>Mark the snap edges</p>
            <p class="fps-02__sp"><code>scroll-snap-align:start</code> on each <code>min-block-size:100dvh</code> panel. Every panel top becomes a stop; the sequence is now a scroller.</p>
          </li>
        </ol>
      </div>
    </section>

    <section class="fps-02__panel" id="fps-02-s3" aria-labelledby="fps-02-h3">
      <div class="fps-02__stage">
        <p class="fps-02__eyebrow"><span class="fps-02__num">03 / 04</span><span class="fps-02__mono">honest comparison</span></p>
        <h2 class="fps-02__title fps-02__title--sm" id="fps-02-h3">What you gain, what you give up</h2>
        <div class="fps-02__cols">
          <div class="fps-02__card fps-02__card--yes">
            <p class="fps-02__ch"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 12.8l4.6 4.4L19.5 6.9" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"/></svg>You gain</p>
            <ul>
              <li>Native touch momentum and iOS rubber-banding</li>
              <li>Space, Page&nbsp;Up/Down and arrow keys, for free</li>
              <li>Find-in-page and screen readers keep working</li>
              <li>Snap runs on the compositor thread &mdash; no jank</li>
              <li>Nothing to load, nothing to version-bump</li>
            </ul>
          </div>
          <div class="fps-02__card fps-02__card--no">
            <p class="fps-02__ch"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M6.5 6.5l11 11M17.5 6.5l-11 11" stroke="currentColor" stroke-width="2.1" stroke-linecap="round"/></svg>You give up</p>
            <ul>
              <li>No programmatic <code>moveTo(n)</code> section API</li>
              <li>No <code>afterLoad</code> / <code>onLeave</code> lifecycle callbacks</li>
              <li>No section-change events without an observer</li>
              <li>No horizontal sub-slides inside a section</li>
              <li>One-per-gesture needs <code>scroll-snap-stop</code></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="fps-02__panel" id="fps-02-s4" aria-labelledby="fps-02-h4">
      <div class="fps-02__stage">
        <p class="fps-02__eyebrow"><span class="fps-02__num">04 / 04</span><span class="fps-02__mono">copy the pattern</span></p>
        <h2 class="fps-02__title fps-02__title--sm" id="fps-02-h4">Then add script only where it earns its place</h2>
        <p class="fps-02__lead">Start from the CSS. If the design later needs a section-change event for analytics or a lazy video, one <code>IntersectionObserver</code> at <code>threshold:.6</code> gives you the callback and the scroller still works when that script fails.</p>
        <p class="fps-02__quote">&ldquo;We replaced a full-page library with 12 lines of CSS and the marketing site's Largest Contentful Paint dropped by 340&nbsp;ms.&rdquo;<span>Priya Sharma &middot; front-end lead</span></p>
        <a class="fps-02__top" href="#fps-02-s1">Back to the first panel</a>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fps-02 {
  --bg: #fbfbfd;
  --panel: #ffffff;
  --panel2: #f2f2f7;
  --ink: #0e0e14;
  --muted: rgba(14,14,20,.6);
  --line: rgba(14,14,20,.10);
  --accent: #6d28d9;
  --yes: #0f766e;
  --no: #9f1239;
  --pad: clamp(1.25rem,5vw,4.5rem);
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
  .fps-02 {
    --accent: oklch(50% .22 292);
    --yes: oklch(48% .1 175);
    --no: oklch(48% .16 12);
    --ink: oklch(14% .01 285);
  }
}

.fps-02 * {
  box-sizing: border-box;
}

.fps-02 h2,
.fps-02 p,
.fps-02 ul,
.fps-02 ol,
.fps-02 pre {
  margin: 0;
}

.fps-02 code {
  font-family: var(--mono);
  font-size: .92em;
}

.fps-02__sr,
.fps-02__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.fps-02__theme {
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
  box-shadow: 0 8px 24px -12px rgba(14,14,20,.35);
}

.fps-02__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.fps-02__theme svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.fps-02__moon {
  display: none;
}

.fps-02__sr:focus-visible + .fps-02__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fps-02__rail {
  display: none;
  grid-template-columns: 1fr;
  gap: .15rem;
  position: fixed;
  inset-block-start: 50%;
  inset-inline-start: clamp(.6rem,2vw,1.5rem);
  translate: 0 -50%;
  z-index: 70;
  padding: .5rem;
  border-radius: 1rem;
  background: rgba(255,255,255,.6);
  border: 1px solid var(--line);
  -webkit-backdrop-filter: blur(12px) saturate(160%);
  backdrop-filter: blur(12px) saturate(160%);
  box-shadow: 0 18px 40px -26px rgba(14,14,20,.5);
}

.fps-02__rail a {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: .55rem;
  min-block-size: 2.75rem;
  min-inline-size: 2.75rem;
  padding: .4rem .7rem;
  border-radius: .7rem;
  font-size: .82rem;
  color: var(--muted);
  text-decoration: none;
  white-space: nowrap;
  transition: background .2s ease,color .2s ease;
}

.fps-02__rail a:hover {
  background: color-mix(in srgb,var(--ink) 6%,transparent);
  color: var(--ink);
}

.fps-02__rail a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fps-02__rn {
  font-family: var(--mono);
  font-size: .68rem;
  color: var(--accent);
  letter-spacing: .06em;
}

@media (min-width: 68rem) {
  .fps-02__rail {
    display: grid;
  }

  .fps-02__rail a {
    justify-content: flex-start;
  }
}

.fps-02__scroller {
  block-size: 100dvh;
  overflow-y: auto;
  overflow-x: hidden;
  scroll-snap-type: y mandatory;
  scroll-behavior: smooth;
  overscroll-behavior-y: contain;
  scrollbar-width: none;
}

.fps-02__scroller::-webkit-scrollbar {
  width: 0;
  height: 0;
}

.fps-02__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.fps-02__panel {
  position: relative;
  min-block-size: 100dvh;
  scroll-snap-align: start;
  scroll-margin-block-start: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--panel);
  padding: clamp(2rem,5vh,3.5rem) var(--pad) calc(clamp(2rem,5vh,3.5rem) + 4rem);
  padding-inline-start: clamp(1.25rem,10vw,7rem);
}

@media (min-width: 68rem) {
  .fps-02__panel {
    padding-inline-start: clamp(11rem,20vw,15rem);
  }
}

.fps-02__panel:nth-child(even) {
  background: var(--panel2);
}

.fps-02__panel + .fps-02__panel {
  margin-block-start: -4rem;
  border-start-start-radius: 1.75rem;
  border-start-end-radius: 1.75rem;
  border-block-start: 1px solid var(--line);
  box-shadow: 0 -30px 64px -34px rgba(14,14,20,.22);
}

@supports not (height: 100dvh) {
  .fps-02__scroller {
    block-size: 100vh;
  }

  .fps-02__panel {
    min-block-size: 100vh;
  }
}

@media (max-width: 67.99rem) {
  .fps-02__panel {
    padding-inline-start: var(--pad);
  }
}

.fps-02__stage {
  inline-size: min(66rem,100%);
  display: grid;
  gap: clamp(1rem,2.4vh,1.5rem);
  justify-items: start;
}

.fps-02__stage--split {
  grid-template-columns: 1.1fr .9fr;
  gap: clamp(1.5rem,4vw,3.5rem);
  align-items: center;
}

@media (max-width: 56rem) {
  .fps-02__stage--split {
    grid-template-columns: 1fr;
  }
}

.fps-02__col {
  display: grid;
  gap: clamp(.9rem,2vh,1.35rem);
  justify-items: start;
}

.fps-02__eyebrow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .7rem;
}

.fps-02__num {
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
}

.fps-02__mono {
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--muted);
  padding: .22rem .5rem;
  border: 1px solid var(--line);
  border-radius: .45rem;
}

.fps-02__title {
  font-size: clamp(2rem,5.4vw,3.9rem);
  line-height: 1.03;
  letter-spacing: -.04em;
  font-weight: 600;
  max-inline-size: 20ch;
  text-wrap: balance;
}

.fps-02__title--sm {
  font-size: clamp(1.7rem,3.8vw,2.75rem);
  letter-spacing: -.03em;
  max-inline-size: 28ch;
}

.fps-02__lead {
  font-size: clamp(1rem,1.4vw,1.15rem);
  line-height: 1.6;
  color: var(--muted);
  max-inline-size: 58ch;
  text-wrap: pretty;
}

.fps-02__facts {
  list-style: none;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: clamp(1rem,3vw,2.25rem);
}

.fps-02__facts li {
  display: grid;
  gap: .1rem;
}

.fps-02__facts strong {
  font-size: clamp(1.6rem,3vw,2.2rem);
  font-weight: 600;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.fps-02__facts span {
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.fps-02__code {
  inline-size: 100%;
  border-radius: 1.25rem;
  border: 1px solid var(--line);
  overflow: hidden;
  background: color-mix(in srgb,var(--ink) 4%,transparent);
  box-shadow: 0 26px 56px -34px rgba(14,14,20,.4);
}

.fps-02__codehead {
  font-family: var(--mono);
  font-size: .66rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
  padding: .7rem .95rem;
  border-block-end: 1px solid var(--line);
}

.fps-02__code pre {
  padding: 1rem .95rem 1.2rem;
  overflow-x: auto;
}

.fps-02__code code {
  font-size: clamp(.78rem,1.05vw,.9rem);
  line-height: 1.75;
  color: var(--muted);
  white-space: pre;
}

.fps-02__code mark {
  background: color-mix(in srgb,var(--accent) 14%,transparent);
  color: var(--accent);
  border-radius: .25rem;
  padding: .05rem .15rem;
}

.fps-02__steps {
  list-style: none;
  padding: 0;
  display: grid;
  gap: .4rem;
  inline-size: 100%;
}

.fps-02__steps li {
  padding: clamp(.9rem,1.8vh,1.2rem) 0;
  border-block-start: 1px solid var(--line);
  display: grid;
  gap: .4rem;
}

.fps-02__sh {
  display: flex;
  align-items: baseline;
  gap: .7rem;
  font-size: 1.05rem;
  font-weight: 550;
  letter-spacing: -.01em;
}

.fps-02__sh span {
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--accent);
}

.fps-02__sp {
  font-size: .96rem;
  line-height: 1.6;
  color: var(--muted);
  max-inline-size: 64ch;
  text-wrap: pretty;
}

.fps-02__cols {
  display: grid;
  grid-template-columns: repeat(auto-fit,minmax(16rem,1fr));
  gap: clamp(.85rem,2vw,1.5rem);
  inline-size: 100%;
}

.fps-02__card {
  padding: clamp(1.1rem,2.4vw,1.6rem);
  border-radius: 1.25rem;
  border: 1px solid var(--line);
  background: var(--bg);
  display: grid;
  gap: .85rem;
}

.fps-02__ch {
  display: flex;
  align-items: center;
  gap: .5rem;
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .12em;
  text-transform: uppercase;
}

.fps-02__ch svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.fps-02__card--yes .fps-02__ch {
  color: var(--yes);
}

.fps-02__card--no .fps-02__ch {
  color: var(--no);
}

.fps-02__card ul {
  list-style: none;
  padding: 0;
  display: grid;
  gap: .55rem;
}

.fps-02__card li {
  position: relative;
  padding-inline-start: 1.1rem;
  font-size: .94rem;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.fps-02__card li::before {
  content: '';
  position: absolute;
  inset-inline-start: 0;
  inset-block-start: .55em;
  inline-size: .35rem;
  block-size: .35rem;
  border-radius: 999px;
  background: currentColor;
  opacity: .45;
}

.fps-02__quote {
  font-size: clamp(1.05rem,2vw,1.4rem);
  line-height: 1.45;
  letter-spacing: -.02em;
  max-inline-size: 44ch;
  padding-inline-start: 1.1rem;
  border-inline-start: 2px solid var(--accent);
  display: grid;
  gap: .6rem;
  text-wrap: pretty;
}

.fps-02__quote span {
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.fps-02__top {
  min-block-size: 2.75rem;
  display: inline-flex;
  align-items: center;
  padding: .7rem 1.15rem;
  border-radius: 999px;
  font-size: .9rem;
  text-decoration: none;
  color: var(--accent);
  border: 1px solid color-mix(in srgb,var(--accent) 40%,transparent);
  transition: background .2s ease;
}

.fps-02__top:hover {
  background: color-mix(in srgb,var(--accent) 8%,transparent);
}

.fps-02__top:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fps-02[data-theme="dark"],
.fps-02:has(#fps-02-dark:checked) {
  --bg: #08080c;
  --panel: #0c0c12;
  --panel2: #12121a;
  --ink: #f4f4f8;
  --muted: rgba(244,244,248,.62);
  --line: rgba(244,244,248,.13);
  --accent: #c4b5fd;
  --yes: #5eead4;
  --no: #fda4af;
}

.fps-02:has(#fps-02-dark:checked) .fps-02__theme,
.fps-02:has(#fps-02-dark:checked) .fps-02__rail {
  background: rgba(255,255,255,.06);
}

.fps-02:has(#fps-02-dark:checked) .fps-02__sun {
  display: none;
}

.fps-02:has(#fps-02-dark:checked) .fps-02__moon {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .fps-02:not([data-theme="light"]):not(:has(#fps-02-dark:checked)) {
    --bg: #08080c;
    --panel: #0c0c12;
    --panel2: #12121a;
    --ink: #f4f4f8;
    --muted: rgba(244,244,248,.62);
    --line: rgba(244,244,248,.13);
    --accent: #c4b5fd;
    --yes: #5eead4;
    --no: #fda4af;
  }

  .fps-02:not([data-theme="light"]):not(:has(#fps-02-dark:checked)) .fps-02__theme,
    .fps-02:not([data-theme="light"]):not(:has(#fps-02-dark:checked)) .fps-02__rail {
    background: rgba(255,255,255,.06);
  }

  .fps-02:not([data-theme="light"]):not(:has(#fps-02-dark:checked)) .fps-02__sun {
    display: none;
  }

  .fps-02:not([data-theme="light"]):not(:has(#fps-02-dark:checked)) .fps-02__moon {
    display: block;
  }
}

@supports not selector(:has(*)) {
  .fps-02__theme {
    display: none;
  }
}

@media (max-height: 40rem) {
  .fps-02__scroller {
    scroll-snap-type: y proximity;
  }

  .fps-02__panel {
    padding-block: 1.25rem 3rem;
  }

  .fps-02__stage {
    gap: .7rem;
  }

  .fps-02__code pre {
    padding-block: .7rem .8rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fps-02__scroller {
    scroll-snap-type: none;
    scroll-behavior: auto;
  }

  .fps-02 *,
    .fps-02 *::before,
    .fps-02 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fps-02__panel,
    .fps-02__card,
    .fps-02__code,
    .fps-02__rail,
    .fps-02__theme,
    .fps-02__top {
    border-color: CanvasText;
    box-shadow: none;
    background: Canvas;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  .fps-02__code mark {
    background: Highlight;
    color: HighlightText;
  }
}
```
