---
source: "codefronts"
url: "https://codefronts.com/layouts/css-full-page-sections/css-scroll-spy-active-link-state-without-javascript/"
title: "CSS Scroll Spy Active Link State Without JavaScript"
section: "layouts"
category: "css-full-page-sections"
category_name: "CSS Full Page Sections"
description: "A docs-style top nav whose active link lights up as each full-viewport section passes &mdash; the lozenge behind the word fills and the label goes solid,…"
has_js: "true"
---

Here's a working CSS Full Page Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Scroll Spy Active Link State Without JavaScript
Source: https://codefronts.com/layouts/css-full-page-sections/css-scroll-spy-active-link-state-without-javascript/

A docs-style top nav whose active link lights up as each full-viewport section passes &mdash; the lozenge behind the word fills and the label goes solid, driven entirely by view-timeline-name and timeline-scope. A ten-line IntersectionObserver runs only to keep aria-current truthful, and doubles as the visual fallback where scroll-driven CSS is missing.
## HTML
```html
<div class="fps-06">
  <input class="fps-06__sr" type="checkbox" id="fps-06-dark">
  <label class="fps-06__theme" for="fps-06-dark" title="Switch light or dark theme">
    <svg class="fps-06__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="fps-06__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="fps-06__vh">Switch light or dark theme</span>
  </label>

  <nav class="fps-06__nav" aria-label="On this page">
    <a class="fps-06__link fps-06__link--1" href="#fps-06-s1" aria-current="true">Overview</a>
    <a class="fps-06__link fps-06__link--2" href="#fps-06-s2">Install</a>
    <a class="fps-06__link fps-06__link--3" href="#fps-06-s3">Tokens</a>
    <a class="fps-06__link fps-06__link--4" href="#fps-06-s4">Theming</a>
    <a class="fps-06__link fps-06__link--5" href="#fps-06-s5">Changelog</a>
  </nav>

  <div class="fps-06__scroller" tabindex="0" role="group" aria-label="Documentation sections, five panels">

    <section class="fps-06__panel fps-06__panel--1" id="fps-06-s1" aria-labelledby="fps-06-h1">
      <div class="fps-06__stage">
        <p class="fps-06__eyebrow"><span class="fps-06__num">01 / 05</span><span class="fps-06__mono">scroll spy</span></p>
        <h2 class="fps-06__title" id="fps-06-h1">The nav link knows which section you are reading</h2>
        <p class="fps-06__lead">Five full-viewport sections, one fixed nav. Each section publishes a view timeline; each link consumes one. The active lozenge is computed by the compositor from geometry the browser already has &mdash; no scroll handler, no offset maths, no drift on a fast flick.</p>
        <p class="fps-06__cue"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5v13.5M6.5 12.6 12 18.2l5.5-5.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Scroll and watch the nav above</p>
      </div>
    </section>

    <section class="fps-06__panel fps-06__panel--2" id="fps-06-s2" aria-labelledby="fps-06-h2">
      <div class="fps-06__stage">
        <p class="fps-06__eyebrow"><span class="fps-06__num">02 / 05</span><span class="fps-06__mono">install</span></p>
        <h2 class="fps-06__title fps-06__title--sm" id="fps-06-h2">Three declarations and a scope</h2>
        <pre class="fps-06__code"><code>.root  { <mark>timeline-scope</mark>:--s1,--s2,--s3,--s4,--s5 }
.panel--2 { <mark>view-timeline-name</mark>:--s2; view-timeline-axis:block }
.link--2::before{
  animation:on linear both;
  <mark>animation-timeline</mark>:--s2;
  animation-range:cover 0% cover 100%;
}</code></pre>
        <p class="fps-06__lead">The scope line is the one people miss: a timeline name is visible only to descendants, and a fixed nav is not a descendant of the section it tracks.</p>
      </div>
    </section>

    <section class="fps-06__panel fps-06__panel--3" id="fps-06-s3" aria-labelledby="fps-06-h3">
      <div class="fps-06__stage">
        <p class="fps-06__eyebrow"><span class="fps-06__num">03 / 05</span><span class="fps-06__mono">tokens</span></p>
        <h2 class="fps-06__title fps-06__title--sm" id="fps-06-h3">Only two properties animate</h2>
        <ul class="fps-06__marks">
          <li><strong>opacity</strong><span>0 &rarr; 1 on the lozenge behind the label</span></li>
          <li><strong>scale</strong><span>.86 &rarr; 1, so the fill feels like it lands</span></li>
          <li><strong>color</strong><span>inherited swap on the label &mdash; cheap, no layout</span></li>
        </ul>
        <p class="fps-06__lead">No width, no <code>left</code>, no box-shadow on the hot path. Both animated properties live on the compositor, so the nav stays smooth while the main thread is busy hydrating the page.</p>
      </div>
    </section>

    <section class="fps-06__panel fps-06__panel--4" id="fps-06-s4" aria-labelledby="fps-06-h4">
      <div class="fps-06__stage">
        <p class="fps-06__eyebrow"><span class="fps-06__num">04 / 05</span><span class="fps-06__mono">theming</span></p>
        <h2 class="fps-06__title fps-06__title--sm" id="fps-06-h4">What the ten lines of JavaScript are for</h2>
        <p class="fps-06__lead">Exactly one thing CSS cannot do: write to the accessibility tree. The observer keeps <code>aria-current</code> truthful for screen-reader users, and where scroll-driven CSS is unavailable it also becomes the visual driver, through an unconditional <code>[aria-current="true"]</code> rule that the animation overrides wherever it runs.</p>
        <p class="fps-06__quote">&ldquo;Two sources of truth for one piece of state is how scroll spies get flickery. Let CSS own the pixels and the observer own the semantics.&rdquo;<span>Maya Okonkwo &middot; accessibility engineer</span></p>
      </div>
    </section>

    <section class="fps-06__panel fps-06__panel--5" id="fps-06-s5" aria-labelledby="fps-06-h5">
      <div class="fps-06__stage">
        <p class="fps-06__eyebrow"><span class="fps-06__num">05 / 05</span><span class="fps-06__mono">changelog</span></p>
        <h2 class="fps-06__title fps-06__title--sm" id="fps-06-h5">Why not a scroll listener</h2>
        <p class="fps-06__lead">A <code>scroll</code> handler recomputing section offsets fires up to sixty times a second on the main thread, reads layout, and still lags a hard flick because it is reacting rather than interpolating. The view timeline is evaluated from geometry the compositor already holds, so the active link cannot fall behind the scroll.</p>
        <a class="fps-06__top" href="#fps-06-s1">Back to the top section</a>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fps-06 {
  --bg: #f6f9f7;
  --panel: #ffffff;
  --panel2: #eef4f0;
  --ink: #08120d;
  --muted: rgba(8,18,13,.6);
  --line: rgba(8,18,13,.10);
  --accent: #047857;
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
  timeline-scope: --fps06-1,--fps06-2,--fps06-3,--fps06-4,--fps06-5;
}

@supports (color: oklch(50% .1 250)) {
  .fps-06 {
    --accent: oklch(50% .12 165);
    --ink: oklch(13% .015 165);
    --bg: oklch(97.5% .008 165);
    --panel2: oklch(95% .013 165);
  }
}

.fps-06 * {
  box-sizing: border-box;
}

.fps-06 h2,
.fps-06 p,
.fps-06 ul,
.fps-06 pre {
  margin: 0;
}

.fps-06 code {
  font-family: var(--mono);
  font-size: .92em;
}

.fps-06__sr,
.fps-06__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.fps-06__theme {
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
  box-shadow: 0 8px 24px -12px rgba(8,18,13,.35);
}

.fps-06__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.fps-06__theme svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.fps-06__moon {
  display: none;
}

.fps-06__sr:focus-visible + .fps-06__theme {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fps-06__nav {
  position: fixed;
  inset-block-start: 1.15rem;
  inset-inline-start: 50%;
  translate: -50% 0;
  z-index: 75;
  display: flex;
  align-items: center;
  gap: .15rem;
  padding: .3rem;
  border-radius: 999px;
  max-inline-size: calc(100% - 8rem);
  overflow-x: auto;
  scrollbar-width: none;
  background: rgba(255,255,255,.7);
  border: 1px solid var(--line);
  -webkit-backdrop-filter: blur(14px) saturate(160%);
  backdrop-filter: blur(14px) saturate(160%);
  box-shadow: 0 14px 34px -22px rgba(8,18,13,.45);
}

.fps-06__nav::-webkit-scrollbar {
  height: 0;
}

.fps-06__link {
  position: relative;
  isolation: isolate;
  display: inline-flex;
  align-items: center;
  white-space: nowrap;
  min-block-size: 2.25rem;
  padding: .4rem .85rem;
  border-radius: 999px;
  font-size: .85rem;
  letter-spacing: -.005em;
  text-decoration: none;
  color: var(--muted);
  transition: color .22s ease;
}

.fps-06__link::before {
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  border-radius: inherit;
  background: color-mix(in srgb,var(--accent) 13%,transparent);
  border: 1px solid color-mix(in srgb,var(--accent) 26%,transparent);
  opacity: 0;
  scale: .86;
}

.fps-06__link:hover {
  color: var(--ink);
}

.fps-06__link:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@supports (animation-timeline: view()) {
  .fps-06__panel--1 {
    view-timeline-name: --fps06-1;
    view-timeline-axis: block;
  }

  .fps-06__panel--2 {
    view-timeline-name: --fps06-2;
    view-timeline-axis: block;
  }

  .fps-06__panel--3 {
    view-timeline-name: --fps06-3;
    view-timeline-axis: block;
  }

  .fps-06__panel--4 {
    view-timeline-name: --fps06-4;
    view-timeline-axis: block;
  }

  .fps-06__panel--5 {
    view-timeline-name: --fps06-5;
    view-timeline-axis: block;
  }

  .fps-06__link::before {
    animation: fps-06-on linear both;
    animation-range: cover 0% cover 100%;
  }

  .fps-06__link {
    animation: fps-06-ink linear both;
    animation-range: cover 0% cover 100%;
  }

  .fps-06__link--1,
    .fps-06__link--1::before {
    animation-timeline: --fps06-1;
  }

  .fps-06__link--2,
    .fps-06__link--2::before {
    animation-timeline: --fps06-2;
  }

  .fps-06__link--3,
    .fps-06__link--3::before {
    animation-timeline: --fps06-3;
  }

  .fps-06__link--4,
    .fps-06__link--4::before {
    animation-timeline: --fps06-4;
  }

  .fps-06__link--5,
    .fps-06__link--5::before {
    animation-timeline: --fps06-5;
  }
}

@keyframes fps-06-on {
  0%,
    42% {
    opacity: 0;
    scale: .86;
  }

  48%,
    52% {
    opacity: 1;
    scale: 1;
  }

  58%,
    100% {
    opacity: 0;
    scale: .86;
  }
}

@keyframes fps-06-ink {
  0%,
    42% {
    color: var(--muted);
  }

  48%,
    52% {
    color: var(--accent);
  }

  58%,
    100% {
    color: var(--muted);
  }
}

.fps-06__link[aria-current="true"] {
  color: var(--accent);
}

.fps-06__link[aria-current="true"]::before {
  opacity: 1;
  scale: 1;
  transition: opacity .22s ease, scale .22s ease;
}

.fps-06__scroller {
  block-size: 100dvh;
  overflow-y: auto;
  overflow-x: hidden;
  scroll-snap-type: y mandatory;
  scroll-behavior: smooth;
  overscroll-behavior-y: contain;
  scrollbar-width: none;
}

.fps-06__scroller::-webkit-scrollbar {
  width: 0;
  height: 0;
}

.fps-06__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.fps-06__panel {
  position: relative;
  min-block-size: 100dvh;
  scroll-snap-align: start;
  scroll-margin-block-start: 0;
  background: var(--panel);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: clamp(4.5rem,10vh,6rem) clamp(1.25rem,5vw,4.5rem) calc(clamp(2rem,5vh,3.5rem) + 4rem);
}

.fps-06__panel:nth-child(even) {
  background: var(--panel2);
}

.fps-06__panel + .fps-06__panel {
  margin-block-start: -4rem;
  border-start-start-radius: 1.75rem;
  border-start-end-radius: 1.75rem;
  border-block-start: 1px solid var(--line);
  box-shadow: 0 -30px 64px -34px rgba(8,18,13,.22);
}

@supports not (height: 100dvh) {
  .fps-06__scroller {
    block-size: 100vh;
  }

  .fps-06__panel {
    min-block-size: 100vh;
  }
}

.fps-06__stage {
  inline-size: min(58rem,100%);
  display: grid;
  gap: clamp(.9rem,2.2vh,1.4rem);
  justify-items: start;
}

.fps-06__eyebrow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .7rem;
}

.fps-06__num {
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
}

.fps-06__mono {
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--muted);
  padding: .22rem .5rem;
  border: 1px solid var(--line);
  border-radius: .45rem;
}

.fps-06__title {
  font-size: clamp(1.95rem,5.2vw,3.7rem);
  line-height: 1.04;
  letter-spacing: -.04em;
  font-weight: 600;
  max-inline-size: 21ch;
  text-wrap: balance;
}

.fps-06__title--sm {
  font-size: clamp(1.65rem,3.6vw,2.55rem);
  letter-spacing: -.03em;
  max-inline-size: 28ch;
}

.fps-06__lead {
  font-size: clamp(.98rem,1.35vw,1.14rem);
  line-height: 1.6;
  color: var(--muted);
  max-inline-size: 60ch;
  text-wrap: pretty;
}

.fps-06__cue {
  display: flex;
  align-items: center;
  gap: .55rem;
  font-family: var(--mono);
  font-size: .82rem;
  color: var(--muted);
}

.fps-06__cue svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  animation: fps-06-bob 2.4s ease-in-out infinite;
}

@keyframes fps-06-bob {
  0%,
    100% {
    translate: 0 -2px;
  }

  50% {
    translate: 0 3px;
  }
}

.fps-06__code {
  padding: 1rem 1.1rem;
  border-radius: 1rem;
  border: 1px solid var(--line);
  background: color-mix(in srgb,var(--ink) 4%,transparent);
  overflow-x: auto;
}

.fps-06__code code {
  font-size: clamp(.76rem,1vw,.87rem);
  line-height: 1.75;
  color: var(--muted);
  white-space: pre;
}

.fps-06__code mark {
  background: color-mix(in srgb,var(--accent) 14%,transparent);
  color: var(--accent);
  border-radius: .25rem;
  padding: .05rem .2rem;
}

.fps-06__marks {
  list-style: none;
  padding: 0;
  display: grid;
  gap: .35rem;
  inline-size: 100%;
}

.fps-06__marks li {
  display: grid;
  grid-template-columns: 6rem 1fr;
  gap: 1rem;
  padding: .7rem 0;
  border-block-start: 1px solid var(--line);
  align-items: baseline;
}

.fps-06__marks strong {
  font-family: var(--mono);
  font-size: .82rem;
  color: var(--accent);
}

.fps-06__marks span {
  font-size: .94rem;
  color: var(--muted);
}

.fps-06__quote {
  font-size: clamp(1.02rem,1.85vw,1.3rem);
  line-height: 1.45;
  letter-spacing: -.02em;
  max-inline-size: 46ch;
  padding-inline-start: 1.05rem;
  border-inline-start: 2px solid var(--accent);
  display: grid;
  gap: .55rem;
  text-wrap: pretty;
}

.fps-06__quote span {
  font-family: var(--mono);
  font-size: .68rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
}

.fps-06__top {
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

.fps-06__top:hover {
  background: color-mix(in srgb,var(--accent) 8%,transparent);
}

.fps-06__top:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.fps-06[data-theme="dark"],
.fps-06:has(#fps-06-dark:checked) {
  --bg: #050b08;
  --panel: #08100c;
  --panel2: #0d1712;
  --ink: #eff7f2;
  --muted: rgba(239,247,242,.62);
  --line: rgba(239,247,242,.13);
  --accent: #6ee7b7;
}

.fps-06:has(#fps-06-dark:checked) .fps-06__theme,
.fps-06:has(#fps-06-dark:checked) .fps-06__nav {
  background: rgba(255,255,255,.07);
}

.fps-06:has(#fps-06-dark:checked) .fps-06__sun {
  display: none;
}

.fps-06:has(#fps-06-dark:checked) .fps-06__moon {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .fps-06:not([data-theme="light"]):not(:has(#fps-06-dark:checked)) {
    --bg: #050b08;
    --panel: #08100c;
    --panel2: #0d1712;
    --ink: #eff7f2;
    --muted: rgba(239,247,242,.62);
    --line: rgba(239,247,242,.13);
    --accent: #6ee7b7;
  }

  .fps-06:not([data-theme="light"]):not(:has(#fps-06-dark:checked)) .fps-06__theme,
    .fps-06:not([data-theme="light"]):not(:has(#fps-06-dark:checked)) .fps-06__nav {
    background: rgba(255,255,255,.07);
  }

  .fps-06:not([data-theme="light"]):not(:has(#fps-06-dark:checked)) .fps-06__sun {
    display: none;
  }

  .fps-06:not([data-theme="light"]):not(:has(#fps-06-dark:checked)) .fps-06__moon {
    display: block;
  }
}

@supports not selector(:has(*)) {
  .fps-06__theme {
    display: none;
  }
}

@media (max-height: 40rem) {
  .fps-06__panel {
    padding-block: 3.25rem 3rem;
  }

  .fps-06__stage {
    gap: .7rem;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fps-06__scroller {
    scroll-snap-type: none;
    scroll-behavior: auto;
  }

  .fps-06__cue svg {
    animation: none !important;
  }

  .fps-06 *,
    .fps-06 *::before,
    .fps-06 *::after {
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fps-06__panel,
    .fps-06__code,
    .fps-06__nav,
    .fps-06__theme,
    .fps-06__top {
    border-color: CanvasText;
    box-shadow: none;
    background: Canvas;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }

  .fps-06__link[aria-current="true"] {
    background: Highlight;
    color: HighlightText;
  }

  .fps-06__link::before {
    display: none;
  }
}
```

## JavaScript
```js
const fps06 = document.querySelector('.fps-06');
if (fps06) {
  const scroller = fps06.querySelector('.fps-06__scroller');
  const links = [...fps06.querySelectorAll('.fps-06__link')];
  if (!CSS.supports('animation-timeline: view()')) fps06.dataset.fallback = 'on';
  const spy = new IntersectionObserver((entries) => {
    const seen = entries.find((e) => e.isIntersecting);
    if (!seen) return;
    for (const link of links) {
      const on = link.hash === '#' + seen.target.id;
      on ? link.setAttribute('aria-current', 'true') : link.removeAttribute('aria-current');
    }
  }, { root: scroller, threshold: 0.6 });
  for (const panel of fps06.querySelectorAll('.fps-06__panel')) spy.observe(panel);
}
```
