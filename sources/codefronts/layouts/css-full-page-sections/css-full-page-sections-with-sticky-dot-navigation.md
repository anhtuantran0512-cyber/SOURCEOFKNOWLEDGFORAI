---
source: "codefronts"
url: "https://codefronts.com/layouts/css-full-page-sections/css-full-page-sections-with-sticky-dot-navigation/"
title: "CSS Full Page Sections with Sticky Dot Navigation"
section: "layouts"
category: "css-full-page-sections"
category_name: "CSS Full Page Sections"
description: "Six full-viewport panels with a fixed dot rail down the right edge."
has_js: "false"
---

Here's a working CSS Full Page Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Full Page Sections with Sticky Dot Navigation
Source: https://codefronts.com/layouts/css-full-page-sections/css-full-page-sections-with-sticky-dot-navigation/

Six full-viewport panels with a fixed dot rail down the right edge. Every dot is a real anchor with a label, so it is keyboard reachable and screen-reader announced &mdash; and the active dot grows and fills as its panel passes, driven by view-timeline-name plus timeline-scope rather than a scroll listener. Where scroll-driven animation is missing, :target keeps the active state working.
## HTML
```html
<div class="fps-05">
  <input class="fps-05__sr" type="checkbox" id="fps-05-dark">
  <label class="fps-05__theme" for="fps-05-dark" title="Switch light or dark theme">
    <svg class="fps-05__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="fps-05__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="fps-05__vh">Switch light or dark theme</span>
  </label>

  <nav class="fps-05__rail" aria-label="Section navigation">
    <a class="fps-05__link" href="#fps-05-s1"><span class="fps-05__label">Overview</span><span class="fps-05__dot fps-05__dot--1"></span></a>
    <a class="fps-05__link" href="#fps-05-s2"><span class="fps-05__label">Signals</span><span class="fps-05__dot fps-05__dot--2"></span></a>
    <a class="fps-05__link" href="#fps-05-s3"><span class="fps-05__label">Routing</span><span class="fps-05__dot fps-05__dot--3"></span></a>
    <a class="fps-05__link" href="#fps-05-s4"><span class="fps-05__label">Audit</span><span class="fps-05__dot fps-05__dot--4"></span></a>
    <a class="fps-05__link" href="#fps-05-s5"><span class="fps-05__label">Scale</span><span class="fps-05__dot fps-05__dot--5"></span></a>
    <a class="fps-05__link" href="#fps-05-s6"><span class="fps-05__label">Start</span><span class="fps-05__dot fps-05__dot--6"></span></a>
  </nav>

  <div class="fps-05__scroller" tabindex="0" role="group" aria-label="Full page sections, six panels">

    <section class="fps-05__panel fps-05__panel--1" id="fps-05-s1" aria-labelledby="fps-05-h1">
      <div class="fps-05__stage">
        <p class="fps-05__eyebrow"><span class="fps-05__num">01 / 06</span><span class="fps-05__mono">view-timeline-name</span></p>
        <h2 class="fps-05__title" id="fps-05-h1">A dot rail that knows where you are</h2>
        <p class="fps-05__lead">Six panels, six anchors, zero scroll listeners. Each panel publishes a view timeline and each dot consumes it, so the active state is computed by the compositor &mdash; not by a handler racing your scroll.</p>
        <p class="fps-05__cue"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5v13.5M6.5 12.6 12 18.2l5.5-5.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Watch the rail as you scroll &mdash; or Tab into it</p>
      </div>
    </section>

    <section class="fps-05__panel fps-05__panel--2" id="fps-05-s2" aria-labelledby="fps-05-h2">
      <div class="fps-05__stage">
        <p class="fps-05__eyebrow"><span class="fps-05__num">02 / 06</span><span class="fps-05__mono">timeline-scope</span></p>
        <h2 class="fps-05__title fps-05__title--sm" id="fps-05-h2">Hoisting a timeline out of the scroller</h2>
        <p class="fps-05__lead">A timeline name is only visible to descendants. The rail is fixed and lives outside the panels, so the demo root declares <code>timeline-scope</code> for all six names &mdash; that one line is what lets an element animate to a sibling subtree's scroll.</p>
        <pre class="fps-05__code"><code>.fps-05{ <mark>timeline-scope</mark>:--p1,--p2,--p3,--p4,--p5,--p6 }
.fps-05__panel--2{ view-timeline-name:--p2 }
.fps-05__dot--2{ animation-timeline:--p2 }</code></pre>
      </div>
    </section>

    <section class="fps-05__panel fps-05__panel--3" id="fps-05-s3" aria-labelledby="fps-05-h3">
      <div class="fps-05__stage">
        <p class="fps-05__eyebrow"><span class="fps-05__num">03 / 06</span><span class="fps-05__mono">animation-range: cover</span></p>
        <h2 class="fps-05__title fps-05__title--sm" id="fps-05-h3">Why the active band sits at 50%</h2>
        <p class="fps-05__lead">The <code>cover</code> range starts when a panel first enters the scrollport and ends when it fully leaves. A panel exactly one scrollport tall is therefore perfectly aligned at 50% progress &mdash; so the dot is keyed to light between 47% and 53% and nowhere else.</p>
        <ul class="fps-05__marks">
          <li><strong>0%</strong><span>panel's top edge enters from below</span></li>
          <li><strong>50%</strong><span>panel fills the scrollport &mdash; dot active</span></li>
          <li><strong>100%</strong><span>panel's bottom edge leaves the top</span></li>
        </ul>
      </div>
    </section>

    <section class="fps-05__panel fps-05__panel--4" id="fps-05-s4" aria-labelledby="fps-05-h4">
      <div class="fps-05__stage">
        <p class="fps-05__eyebrow"><span class="fps-05__num">04 / 06</span><span class="fps-05__mono">44px hit target</span></p>
        <h2 class="fps-05__title fps-05__title--sm" id="fps-05-h4">Ten-pixel dots, forty-four-pixel targets</h2>
        <p class="fps-05__lead">The visual can be tiny; the target cannot. Each anchor is padded out to 44&nbsp;px in both axes to satisfy WCAG 2.2 target size, its label is real text revealed on hover and focus rather than a <code>title</code> attribute, and the focus ring is a 2&nbsp;px outline at full contrast.</p>
      </div>
    </section>

    <section class="fps-05__panel fps-05__panel--5" id="fps-05-s5" aria-labelledby="fps-05-h5">
      <div class="fps-05__stage">
        <p class="fps-05__eyebrow"><span class="fps-05__num">05 / 06</span><span class="fps-05__mono">:target fallback</span></p>
        <h2 class="fps-05__title fps-05__title--sm" id="fps-05-h5">What happens on a browser without scroll-driven CSS</h2>
        <p class="fps-05__lead">The rail still works. The active state also comes from <code>:target</code> &mdash; shipped unconditionally, so a clicked dot stays lit and <code>:has()</code> lights the first dot before anything is clicked. Nothing is hidden, nothing breaks.</p>
      </div>
    </section>

    <section class="fps-05__panel fps-05__panel--6" id="fps-05-s6" aria-labelledby="fps-05-h6">
      <div class="fps-05__stage">
        <p class="fps-05__eyebrow"><span class="fps-05__num">06 / 06</span><span class="fps-05__mono">ship it</span></p>
        <h2 class="fps-05__title fps-05__title--sm" id="fps-05-h6">Four edits to add a seventh panel</h2>
        <p class="fps-05__lead">Give the section an id, give it a <code>view-timeline-name</code>, add that name to <code>timeline-scope</code>, copy one dot anchor. There is no index arithmetic and no count stored anywhere in the CSS.</p>
        <a class="fps-05__top" href="#fps-05-s1">Return to panel one</a>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fps-05 {
  --bg: #f8f8fb;
  --panel: #ffffff;
  --panel2: #f0f0f6;
  --ink: #0d0d16;
  --muted: rgba(13,13,22,.6);
  --line: rgba(13,13,22,.10);
  --accent: #4f46e5;
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
  timeline-scope: --fps05-1,--fps05-2,--fps05-3,--fps05-4,--fps05-5,--fps05-6;
}

@supports (color: oklch(50% .1 250)) {
  .fps-05 {
    --accent: oklch(52% .21 278);
    --ink: oklch(13% .015 285);
    --bg: oklch(97.6% .004 285);
    --panel2: oklch(95.2% .008 285);
  }
}

.fps-05 * {
  box-sizing: border-box;
}

.fps-05 h2,
.fps-05 p,
.fps-05 ul,
.fps-05 pre {
  margin: 0;
}

.fps-05 code {
  font-family: var(--mono);
  font-size: .92em;
}

.fps-05__sr,
.fps-05__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.fps-05__theme {
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
  box-shadow: 0 8px 24px -12px rgba(13,13,22,.35);
}

.fps-05__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.fps-05__theme svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.fps-05__moon {
  display: none;
}

.fps-05__sr:focus-visible + .fps-05__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fps-05__rail {
  position: fixed;
  inset-block-start: 50%;
  inset-inline-end: clamp(.35rem,1.4vw,1rem);
  translate: 0 -50%;
  z-index: 75;
  display: grid;
  justify-items: end;
}

.fps-05__link {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: .6rem;
  min-inline-size: 2.75rem;
  min-block-size: 2.75rem;
  padding-inline: .6rem;
  border-radius: 999px;
  text-decoration: none;
  color: var(--ink);
}

.fps-05__link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.fps-05__label {
  font-size: .76rem;
  letter-spacing: .01em;
  color: var(--ink);
  white-space: nowrap;
  padding: .2rem .5rem;
  border-radius: .5rem;
  border: 1px solid var(--line);
  background: rgba(255,255,255,.72);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  opacity: 0;
  translate: .35rem 0;
  transition: opacity .22s ease, translate .22s ease;
}

.fps-05__link:hover .fps-05__label,
.fps-05__link:focus-visible .fps-05__label {
  opacity: 1;
  translate: 0 0;
}

.fps-05__dot {
  inline-size: .62rem;
  block-size: .62rem;
  border-radius: 999px;
  background: var(--ink);
  opacity: .32;
  transition: opacity .25s ease, scale .25s ease;
  flex: none;
}

@supports (animation-timeline: view()) {
  .fps-05__panel--1 {
    view-timeline-name: --fps05-1;
    view-timeline-axis: block;
  }

  .fps-05__panel--2 {
    view-timeline-name: --fps05-2;
    view-timeline-axis: block;
  }

  .fps-05__panel--3 {
    view-timeline-name: --fps05-3;
    view-timeline-axis: block;
  }

  .fps-05__panel--4 {
    view-timeline-name: --fps05-4;
    view-timeline-axis: block;
  }

  .fps-05__panel--5 {
    view-timeline-name: --fps05-5;
    view-timeline-axis: block;
  }

  .fps-05__panel--6 {
    view-timeline-name: --fps05-6;
    view-timeline-axis: block;
  }

  .fps-05__dot {
    animation: fps-05-dot linear both;
    animation-range: cover 0% cover 100%;
  }

  .fps-05__dot--1 {
    animation-timeline: --fps05-1;
  }

  .fps-05__dot--2 {
    animation-timeline: --fps05-2;
  }

  .fps-05__dot--3 {
    animation-timeline: --fps05-3;
  }

  .fps-05__dot--4 {
    animation-timeline: --fps05-4;
  }

  .fps-05__dot--5 {
    animation-timeline: --fps05-5;
  }

  .fps-05__dot--6 {
    animation-timeline: --fps05-6;
  }
}

@keyframes fps-05-dot {
  0%,
    40% {
    scale: 1;
    opacity: .32;
    background: var(--ink);
  }

  47%,
    53% {
    scale: 2.1;
    opacity: 1;
    background: var(--accent);
  }

  60%,
    100% {
    scale: 1;
    opacity: .32;
    background: var(--ink);
  }
}

.fps-05:has(#fps-05-s1:target) .fps-05__dot--1,
.fps-05:has(#fps-05-s2:target) .fps-05__dot--2,
.fps-05:has(#fps-05-s3:target) .fps-05__dot--3,
.fps-05:has(#fps-05-s4:target) .fps-05__dot--4,
.fps-05:has(#fps-05-s5:target) .fps-05__dot--5,
.fps-05:has(#fps-05-s6:target) .fps-05__dot--6,
.fps-05:not(:has(section:target)) .fps-05__dot--1 {
  scale: 2.1;
  opacity: 1;
  background: var(--accent);
}

.fps-05__scroller {
  block-size: 100dvh;
  overflow-y: auto;
  overflow-x: hidden;
  scroll-snap-type: y mandatory;
  scroll-behavior: smooth;
  overscroll-behavior-y: contain;
  scrollbar-width: none;
}

.fps-05__scroller::-webkit-scrollbar {
  width: 0;
  height: 0;
}

.fps-05__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.fps-05__panel {
  position: relative;
  min-block-size: 100dvh;
  scroll-snap-align: start;
  background: var(--panel);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(2rem,5vh,3.5rem) clamp(3.5rem,8vw,7rem) calc(clamp(2rem,5vh,3.5rem) + 4rem);
}

.fps-05__panel:nth-child(even) {
  background: var(--panel2);
}

.fps-05__panel + .fps-05__panel {
  margin-block-start: -4rem;
  border-start-start-radius: 1.75rem;
  border-start-end-radius: 1.75rem;
  border-block-start: 1px solid var(--line);
  box-shadow: 0 -30px 64px -34px rgba(13,13,22,.22);
}

@supports not (height: 100dvh) {
  .fps-05__scroller {
    block-size: 100vh;
  }

  .fps-05__panel {
    min-block-size: 100vh;
  }
}

.fps-05__stage {
  inline-size: min(58rem,100%);
  display: grid;
  gap: clamp(.9rem,2.2vh,1.4rem);
  justify-items: start;
}

.fps-05__eyebrow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .7rem;
}

.fps-05__num {
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
}

.fps-05__mono {
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--muted);
  padding: .22rem .5rem;
  border: 1px solid var(--line);
  border-radius: .45rem;
}

.fps-05__title {
  font-size: clamp(2rem,5.6vw,3.9rem);
  line-height: 1.03;
  letter-spacing: -.04em;
  font-weight: 600;
  max-inline-size: 20ch;
  text-wrap: balance;
}

.fps-05__title--sm {
  font-size: clamp(1.65rem,3.6vw,2.55rem);
  letter-spacing: -.03em;
  max-inline-size: 28ch;
}

.fps-05__lead {
  font-size: clamp(.98rem,1.35vw,1.14rem);
  line-height: 1.6;
  color: var(--muted);
  max-inline-size: 58ch;
  text-wrap: pretty;
}

.fps-05__cue {
  display: flex;
  align-items: center;
  gap: .55rem;
  font-family: var(--mono);
  font-size: .82rem;
  color: var(--muted);
}

.fps-05__cue svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  animation: fps-05-bob 2.4s ease-in-out infinite;
}

@keyframes fps-05-bob {
  0%,
    100% {
    translate: 0 -2px;
  }

  50% {
    translate: 0 3px;
  }
}

.fps-05__code {
  padding: 1rem 1.1rem;
  border-radius: 1rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 4%,transparent);
  overflow-x: auto;
}

.fps-05__code code {
  font-size: clamp(.76rem,1vw,.87rem);
  line-height: 1.75;
  color: var(--muted);
  white-space: pre;
}

.fps-05__code mark {
  background: color-mix(in srgb,var(--accent) 15%,transparent);
  color: var(--accent);
  border-radius: .25rem;
  padding: .05rem .2rem;
}

.fps-05__marks {
  list-style: none;
  padding: 0;
  display: grid;
  gap: .35rem;
  inline-size: 100%;
}

.fps-05__marks li {
  display: grid;
  grid-template-columns: 4.5rem 1fr;
  gap: 1rem;
  padding: .7rem 0;
  border-block-start: 1px solid var(--line);
  align-items: baseline;
}

.fps-05__marks strong {
  font-family: var(--mono);
  font-size: .85rem;
  color: var(--accent);
  font-variant-numeric: tabular-nums;
}

.fps-05__marks span {
  font-size: .94rem;
  color: var(--muted);
}

.fps-05__top {
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

.fps-05__top:hover {
  background: color-mix(in srgb,var(--accent) 8%,transparent);
}

.fps-05__top:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fps-05[data-theme="dark"],
.fps-05:has(#fps-05-dark:checked) {
  --bg: #07070c;
  --panel: #0b0b11;
  --panel2: #11111a;
  --ink: #f3f3f9;
  --muted: rgba(243,243,249,.62);
  --line: rgba(243,243,249,.13);
  --accent: #a5b4fc;
}

.fps-05:has(#fps-05-dark:checked) .fps-05__theme,
.fps-05:has(#fps-05-dark:checked) .fps-05__label {
  background: rgba(255,255,255,.07);
}

.fps-05:has(#fps-05-dark:checked) .fps-05__sun {
  display: none;
}

.fps-05:has(#fps-05-dark:checked) .fps-05__moon {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .fps-05:not([data-theme="light"]):not(:has(#fps-05-dark:checked)) {
    --bg: #07070c;
    --panel: #0b0b11;
    --panel2: #11111a;
    --ink: #f3f3f9;
    --muted: rgba(243,243,249,.62);
    --line: rgba(243,243,249,.13);
    --accent: #a5b4fc;
  }

  .fps-05:not([data-theme="light"]):not(:has(#fps-05-dark:checked)) .fps-05__theme,
    .fps-05:not([data-theme="light"]):not(:has(#fps-05-dark:checked)) .fps-05__label {
    background: rgba(255,255,255,.07);
  }

  .fps-05:not([data-theme="light"]):not(:has(#fps-05-dark:checked)) .fps-05__sun {
    display: none;
  }

  .fps-05:not([data-theme="light"]):not(:has(#fps-05-dark:checked)) .fps-05__moon {
    display: block;
  }
}

@supports not selector(:has(*)) {
  .fps-05__theme {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fps-05__scroller {
    scroll-snap-type: none;
    scroll-behavior: auto;
  }

  .fps-05 *,
    .fps-05 *::before,
    .fps-05 *::after {
    transition: none !important;
  }

  .fps-05__cue svg {
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .fps-05__panel,
    .fps-05__code,
    .fps-05__theme,
    .fps-05__label,
    .fps-05__top {
    border-color: CanvasText;
    box-shadow: none;
    background: Canvas;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  .fps-05__dot {
    background: CanvasText;
    opacity: 1;
  }
}
```
