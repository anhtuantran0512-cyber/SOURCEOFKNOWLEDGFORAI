---
source: "codefronts"
url: "https://codefronts.com/layouts/css-full-page-sections/css-horizontal-scroll-snap-full-screen-panels/"
title: "CSS Horizontal Scroll Snap Full Screen Panels"
section: "layouts"
category: "css-full-page-sections"
category_name: "CSS Full Page Sections"
description: "Five full-viewport panels that scroll sideways with scroll-snap-type: x mandatory &mdash; and flip to a vertical stack under 48&nbsp;rem, because horizontal…"
has_js: "false"
---

Here's a working CSS Full Page Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Horizontal Scroll Snap Full Screen Panels
Source: https://codefronts.com/layouts/css-full-page-sections/css-horizontal-scroll-snap-full-screen-panels/

Five full-viewport panels that scroll sideways with scroll-snap-type: x mandatory &mdash; and flip to a vertical stack under 48&nbsp;rem, because horizontal scrolling on a phone is hostile. Chapter anchors, a visible next-panel edge, keyboard arrow support from the native scrollport, and no JavaScript at all.
## HTML
```html
<div class="fps-11">
  <input class="fps-11__sr" type="checkbox" id="fps-11-dark">
  <label class="fps-11__theme" for="fps-11-dark" title="Switch light or dark theme">
    <svg class="fps-11__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="fps-11__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="fps-11__vh">Switch light or dark theme</span>
  </label>

  <nav class="fps-11__chapters" aria-label="Chapters">
    <a href="#fps-11-s1">01</a><a href="#fps-11-s2">02</a><a href="#fps-11-s3">03</a><a href="#fps-11-s4">04</a><a href="#fps-11-s5">05</a>
  </nav>

  <div class="fps-11__scroller" tabindex="0" role="group" aria-label="Horizontal chapter panels, five chapters. Use left and right arrow keys.">

    <section class="fps-11__panel" style="--h:196" id="fps-11-s1" aria-labelledby="fps-11-h1">
      <div class="fps-11__stage">
        <p class="fps-11__eyebrow"><span class="fps-11__num">Chapter 01</span><span class="fps-11__mono">scroll-snap-type: x mandatory</span></p>
        <h2 class="fps-11__title" id="fps-11-h1">Sideways, on purpose</h2>
        <p class="fps-11__lead">Five full-viewport chapters on one horizontal scrollport. The technique is identical to the vertical case &mdash; a flex row that will not wrap, snapping on the inline axis, and a container that owns its own scroll.</p>
        <p class="fps-11__cue"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4.5 12h13.5M12.6 6.5 18.2 12l-5.6 5.5" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Scroll right, or press the right arrow key</p>
      </div>
    </section>

    <section class="fps-11__panel" style="--h:152" id="fps-11-s2" aria-labelledby="fps-11-h2">
      <div class="fps-11__stage">
        <p class="fps-11__eyebrow"><span class="fps-11__num">Chapter 02</span><span class="fps-11__mono">overscroll-behavior-x</span></p>
        <h2 class="fps-11__title fps-11__title--sm" id="fps-11-h2">The declaration that stops the browser going back</h2>
        <p class="fps-11__lead">A horizontal overscroll at the first panel is indistinguishable from a swipe-back gesture. <code>overscroll-behavior-x: contain</code> keeps the gesture inside your scroller, and it is the difference between a slider and an accidental exit.</p>
        <pre class="fps-11__code"><code>.scroller{
  overflow-x:auto;
  scroll-snap-type:x mandatory;
  <mark>overscroll-behavior-x:contain;</mark>
}</code></pre>
      </div>
    </section>

    <section class="fps-11__panel" style="--h:96" id="fps-11-s3" aria-labelledby="fps-11-h3">
      <div class="fps-11__stage">
        <p class="fps-11__eyebrow"><span class="fps-11__num">Chapter 03</span><span class="fps-11__mono">the mobile flip</span></p>
        <h2 class="fps-11__title fps-11__title--sm" id="fps-11-h3">Below 48rem this becomes a vertical scroller</h2>
        <p class="fps-11__lead">Vertical is muscle memory on a phone. Rather than shrinking the horizontal experience, one media query changes the flex direction and the snap axis &mdash; same markup, same panels, a gesture people already have.</p>
        <p class="fps-11__hint">Narrow this window past 48&nbsp;rem to watch the axis flip.</p>
      </div>
    </section>

    <section class="fps-11__panel" style="--h:44" id="fps-11-s4" aria-labelledby="fps-11-h4">
      <div class="fps-11__stage">
        <p class="fps-11__eyebrow"><span class="fps-11__num">Chapter 04</span><span class="fps-11__mono">discoverability</span></p>
        <h2 class="fps-11__title fps-11__title--sm" id="fps-11-h4">Always show a sliver of what is next</h2>
        <p class="fps-11__lead">Horizontal scrollers fail mostly because readers never realise they can scroll. Each panel here is pulled 4&nbsp;rem left with a rounded leading edge, so the next chapter's colour is on screen from the start &mdash; plus chapter anchors for people who would rather click.</p>
      </div>
    </section>

    <section class="fps-11__panel" style="--h:320" id="fps-11-s5" aria-labelledby="fps-11-h5">
      <div class="fps-11__stage">
        <p class="fps-11__eyebrow"><span class="fps-11__num">Chapter 05</span><span class="fps-11__mono">keyboard, for free</span></p>
        <h2 class="fps-11__title fps-11__title--sm" id="fps-11-h5">A focusable scrollport is already accessible</h2>
        <p class="fps-11__lead">Give the container <code>tabindex="0"</code> and a labelled <code>role="group"</code> and the browser handles Left, Right, Home, End and Page&nbsp;Up/Down itself. No key handler, no synthetic scrolling, nothing to get wrong.</p>
        <a class="fps-11__top" href="#fps-11-s1">Back to chapter one</a>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fps-11 {
  --bg: #f6fbfd;
  --ink: #04141a;
  --muted: rgba(4,20,26,.62);
  --line: rgba(4,20,26,.11);
  --accent: #0e7490;
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
  .fps-11 {
    --accent: oklch(52% .11 220);
    --ink: oklch(14% .02 220);
    --bg: oklch(98% .008 220);
  }
}

.fps-11 * {
  box-sizing: border-box;
}

.fps-11 h2,
.fps-11 p,
.fps-11 pre {
  margin: 0;
}

.fps-11 code {
  font-family: var(--mono);
  font-size: .92em;
}

.fps-11__sr,
.fps-11__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.fps-11__theme {
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
  background: rgba(255,255,255,.66);
  border: 1px solid var(--line);
  -webkit-backdrop-filter: blur(10px) saturate(150%);
  backdrop-filter: blur(10px) saturate(150%);
  box-shadow: 0 8px 24px -12px rgba(4,20,26,.35);
}

.fps-11__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.fps-11__theme svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.fps-11__moon {
  display: none;
}

.fps-11__sr:focus-visible + .fps-11__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fps-11__chapters {
  position: fixed;
  inset-block-end: 1.15rem;
  inset-inline-start: 50%;
  translate: -50% 0;
  z-index: 75;
  display: flex;
  gap: .15rem;
  padding: .3rem;
  border-radius: 999px;
  background: rgba(255,255,255,.7);
  border: 1px solid var(--line);
  -webkit-backdrop-filter: blur(12px) saturate(160%);
  backdrop-filter: blur(12px) saturate(160%);
  box-shadow: 0 14px 34px -22px rgba(4,20,26,.45);
}

.fps-11__chapters a {
  min-inline-size: 2.75rem;
  min-block-size: 2.4rem;
  display: grid;
  place-items: center;
  border-radius: 999px;
  font-family: var(--mono);
  font-size: .74rem;
  letter-spacing: .06em;
  text-decoration: none;
  color: var(--muted);
  transition: background .2s ease, color .2s ease;
}

.fps-11__chapters a:hover {
  background: color-mix(in srgb,var(--accent) 10%,transparent);
  color: var(--accent);
}

.fps-11__chapters a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fps-11__scroller {
  display: flex;
  flex-wrap: nowrap;
  block-size: 100dvh;
  overflow-x: auto;
  overflow-y: hidden;
  scroll-snap-type: x mandatory;
  scroll-behavior: smooth;
  overscroll-behavior-x: contain;
  overscroll-behavior-y: none;
  scrollbar-width: none;
}

.fps-11__scroller::-webkit-scrollbar {
  width: 0;
  height: 0;
}

.fps-11__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.fps-11__panel {
  position: relative;
  flex: 0 0 100%;
  block-size: 100dvh;
  scroll-snap-align: start;
  display: flex;
  align-items: center;
  padding: clamp(2rem,5vh,3.5rem) clamp(1.25rem,5vw,4.5rem) calc(clamp(2rem,5vh,3.5rem) + 4.5rem);
  padding-inline-start: clamp(2.5rem,6vw,6rem);
  background: hsl(var(--h) 62% 96%);
}

@supports (background: oklch(90% .05 40)) {
  .fps-11__panel {
    background: oklch(96.5% .03 calc(var(--h) * 1deg));
  }
}

.fps-11__panel + .fps-11__panel {
  margin-inline-start: -4rem;
  padding-inline-start: calc(clamp(2.5rem,6vw,6rem) + 4rem);
  border-start-start-radius: 2rem;
  border-end-start-radius: 2rem;
  border-inline-start: 1px solid var(--line);
  box-shadow: -30px 0 64px -34px rgba(4,20,26,.25);
}

@supports not (height: 100dvh) {
  .fps-11__scroller,
    .fps-11__panel {
    block-size: 100vh;
  }
}

.fps-11__stage {
  inline-size: min(48rem,100%);
  display: grid;
  gap: clamp(.85rem,2vh,1.35rem);
  justify-items: start;
}

.fps-11__eyebrow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .7rem;
}

.fps-11__num {
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: hsl(var(--h) 60% 30%);
}

@supports (color: oklch(40% .1 40)) {
  .fps-11__num {
    color: oklch(45% .13 calc(var(--h) * 1deg));
  }
}

.fps-11__mono {
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--muted);
  padding: .22rem .5rem;
  border: 1px solid var(--line);
  border-radius: .45rem;
  background: rgba(255,255,255,.5);
}

.fps-11__title {
  font-size: clamp(2.1rem,6vw,4.4rem);
  line-height: 1.02;
  letter-spacing: -.045em;
  font-weight: 600;
  max-inline-size: 18ch;
  text-wrap: balance;
}

.fps-11__title--sm {
  font-size: clamp(1.65rem,3.6vw,2.7rem);
  letter-spacing: -.035em;
  max-inline-size: 24ch;
}

.fps-11__lead {
  font-size: clamp(.98rem,1.35vw,1.14rem);
  line-height: 1.6;
  color: var(--muted);
  max-inline-size: 52ch;
  text-wrap: pretty;
}

.fps-11__cue {
  display: flex;
  align-items: center;
  gap: .55rem;
  font-family: var(--mono);
  font-size: .8rem;
  color: var(--muted);
}

.fps-11__cue svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  animation: fps-11-nudge 2.4s ease-in-out infinite;
}

@keyframes fps-11-nudge {
  0%,
    100% {
    translate: -2px 0;
  }

  50% {
    translate: 4px 0;
  }
}

.fps-11__hint {
  font-family: var(--mono);
  font-size: .76rem;
  color: var(--accent);
  padding: .5rem .75rem;
  border-radius: .6rem;
  border: 1px dashed color-mix(in srgb,var(--accent) 40%,transparent);
}

.fps-11__code {
  padding: 1rem 1.1rem;
  border-radius: 1rem;
  border: 1px solid var(--line);
  background: rgba(255,255,255,.6);
  overflow-x: auto;
}

.fps-11__code code {
  font-size: clamp(.76rem,1vw,.87rem);
  line-height: 1.7;
  color: var(--muted);
  white-space: pre;
}

.fps-11__code mark {
  background: color-mix(in srgb,var(--accent) 15%,transparent);
  color: var(--accent);
  border-radius: .25rem;
  padding: .05rem .2rem;
}

.fps-11__top {
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

.fps-11__top:hover {
  background: color-mix(in srgb,var(--accent) 9%,transparent);
}

.fps-11__top:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

@media (max-width: 48rem) {
  .fps-11__scroller {
    flex-direction: column;
    overflow-x: hidden;
    overflow-y: auto;
    scroll-snap-type: y mandatory;
    overscroll-behavior-y: contain;
    overscroll-behavior-x: auto;
  }

  .fps-11__panel {
    flex: 0 0 auto;
    block-size: auto;
    min-block-size: 100dvh;
    padding-inline: clamp(1.25rem,5vw,2rem);
  }

  .fps-11__panel + .fps-11__panel {
    margin-inline-start: 0;
    margin-block-start: -3.5rem;
    padding-inline-start: clamp(1.25rem,5vw,2rem);
    border-inline-start: 0;
    border-block-start: 1px solid var(--line);
    border-start-start-radius: 1.75rem;
    border-start-end-radius: 1.75rem;
    border-end-start-radius: 0;
    box-shadow: 0 -30px 64px -34px rgba(4,20,26,.25);
  }

  @supports not (height: 100dvh) {
    .fps-11__panel {
      min-block-size: 100vh;
    }
  }

  .fps-11__cue svg {
    rotate: 90deg;
  }
}

.fps-11[data-theme="dark"],
.fps-11:has(#fps-11-dark:checked) {
  --bg: #04090b;
  --ink: #eef8fb;
  --muted: rgba(238,248,251,.62);
  --line: rgba(238,248,251,.13);
  --accent: #67e8f9;
}

.fps-11:has(#fps-11-dark:checked) .fps-11__theme,
.fps-11:has(#fps-11-dark:checked) .fps-11__chapters,
.fps-11:has(#fps-11-dark:checked) .fps-11__mono,
.fps-11:has(#fps-11-dark:checked) .fps-11__code {
  background: rgba(255,255,255,.06);
}

.fps-11:has(#fps-11-dark:checked) .fps-11__sun {
  display: none;
}

.fps-11:has(#fps-11-dark:checked) .fps-11__moon {
  display: block;
}

.fps-11:has(#fps-11-dark:checked) .fps-11__panel {
  background: hsl(var(--h) 45% 8%);
}

.fps-11:has(#fps-11-dark:checked) .fps-11__num {
  color: hsl(var(--h) 75% 76%);
}

@media (prefers-color-scheme: dark) {
  .fps-11:not([data-theme="light"]):not(:has(#fps-11-dark:checked)) {
    --bg: #04090b;
    --ink: #eef8fb;
    --muted: rgba(238,248,251,.62);
    --line: rgba(238,248,251,.13);
    --accent: #67e8f9;
  }

  .fps-11:not([data-theme="light"]):not(:has(#fps-11-dark:checked)) .fps-11__theme,
    .fps-11:not([data-theme="light"]):not(:has(#fps-11-dark:checked)) .fps-11__chapters,
    .fps-11:not([data-theme="light"]):not(:has(#fps-11-dark:checked)) .fps-11__mono,
    .fps-11:not([data-theme="light"]):not(:has(#fps-11-dark:checked)) .fps-11__code {
    background: rgba(255,255,255,.06);
  }

  .fps-11:not([data-theme="light"]):not(:has(#fps-11-dark:checked)) .fps-11__sun {
    display: none;
  }

  .fps-11:not([data-theme="light"]):not(:has(#fps-11-dark:checked)) .fps-11__moon {
    display: block;
  }

  .fps-11:not([data-theme="light"]):not(:has(#fps-11-dark:checked)) .fps-11__panel {
    background: hsl(var(--h) 45% 8%);
  }

  .fps-11:not([data-theme="light"]):not(:has(#fps-11-dark:checked)) .fps-11__num {
    color: hsl(var(--h) 75% 76%);
  }
}

@supports (background: oklch(10% .02 40)) {
  .fps-11:has(#fps-11-dark:checked) .fps-11__panel {
    background: oklch(16% .035 calc(var(--h) * 1deg));
  }
}

@supports not selector(:has(*)) {
  .fps-11__theme {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fps-11__scroller {
    scroll-snap-type: none;
    scroll-behavior: auto;
  }

  .fps-11 *,
    .fps-11 *::before,
    .fps-11 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fps-11__panel,
    .fps-11__code,
    .fps-11__chapters,
    .fps-11__theme,
    .fps-11__mono,
    .fps-11__top {
    border-color: CanvasText;
    box-shadow: none;
    background: Canvas;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }
}
```
