---
source: "codefronts"
url: "https://codefronts.com/layouts/css-full-page-sections/css-scroll-driven-section-parallax-backgrounds/"
title: "CSS Scroll Driven Section Parallax Backgrounds"
section: "layouts"
category: "css-full-page-sections"
category_name: "CSS Full Page Sections"
description: "Four full-viewport panels where the photograph, a colour wash and the headline each travel at a different rate as the panel crosses the scrollport &mdash;…"
has_js: "false"
---

Here's a working CSS Full Page Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Scroll Driven Section Parallax Backgrounds
Source: https://codefronts.com/layouts/css-full-page-sections/css-scroll-driven-section-parallax-backgrounds/

Four full-viewport panels where the photograph, a colour wash and the headline each travel at a different rate as the panel crosses the scrollport &mdash; real depth from animation-timeline: view(), no scroll listener and no background-attachment: fixed (which simply does not work on iOS). Under prefers-reduced-motion every layer locks into place.
## HTML
```html
<div class="fps-07">
  <input class="fps-07__sr" type="checkbox" id="fps-07-dark">
  <label class="fps-07__theme" for="fps-07-dark" title="Switch light or dark theme">
    <svg class="fps-07__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="fps-07__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="fps-07__vh">Switch light or dark theme</span>
  </label>

  <div class="fps-07__scroller" tabindex="0" role="group" aria-label="Parallax photo sections, four panels">

    <section class="fps-07__panel" style="--h:205" id="fps-07-s1" aria-labelledby="fps-07-h1">
      <img class="fps-07__photo" src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=1600&amp;auto=format" alt="Still alpine lake below a treeline ridge at dusk" width="1600" height="1067" loading="eager" decoding="async">
      <span class="fps-07__wash" aria-hidden="true"></span>
      <div class="fps-07__stage">
        <p class="fps-07__eyebrow"><span class="fps-07__num">01 / 04</span><span class="fps-07__mono">animation-timeline: view()</span></p>
        <h2 class="fps-07__title" id="fps-07-h1">Three layers, three rates, one scroll</h2>
        <p class="fps-07__lead">The photograph travels 18% of the panel height, the colour wash 8%, the type barely at all. Nothing here is timed &mdash; every layer is a pure function of how far this panel has crossed the screen.</p>
        <p class="fps-07__cue"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5v13.5M6.5 12.6 12 18.2l5.5-5.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Scroll slowly to see the layers separate</p>
      </div>
    </section>

    <section class="fps-07__panel" style="--h:150" id="fps-07-s2" aria-labelledby="fps-07-h2">
      <img class="fps-07__photo" src="https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=1600&amp;auto=format" alt="Fog drifting between tall conifers on a hillside" width="1600" height="1067" loading="lazy" decoding="async">
      <span class="fps-07__wash" aria-hidden="true"></span>
      <div class="fps-07__stage">
        <p class="fps-07__eyebrow"><span class="fps-07__num">02 / 04</span><span class="fps-07__mono">why not background-attachment</span></p>
        <h2 class="fps-07__title fps-07__title--sm" id="fps-07-h2">The fixed-background trick has always been broken</h2>
        <p class="fps-07__lead">iOS Safari ignores <code>background-attachment: fixed</code> entirely &mdash; the image just scrolls with the section &mdash; and Android Chrome repaints the whole layer every frame to honour it. A translating child stays on the compositor and behaves the same everywhere.</p>
        <pre class="fps-07__code"><code>.panel{ background-attachment:fixed } <mark>/* no */</mark>
.panel__photo{ translate:0 var(--y) }  <mark>/* yes */</mark></code></pre>
      </div>
    </section>

    <section class="fps-07__panel" style="--h:262" id="fps-07-s3" aria-labelledby="fps-07-h3">
      <img class="fps-07__photo" src="https://images.unsplash.com/photo-1519681393784-d120267933ba?w=1600&amp;auto=format" alt="Snow-covered peak under a dense field of stars" width="1600" height="1067" loading="lazy" decoding="async">
      <span class="fps-07__wash" aria-hidden="true"></span>
      <div class="fps-07__stage">
        <p class="fps-07__eyebrow"><span class="fps-07__num">03 / 04</span><span class="fps-07__mono">the slack rule</span></p>
        <h2 class="fps-07__title fps-07__title--sm" id="fps-07-h3">A layer that moves 9% needs 9% to spare</h2>
        <p class="fps-07__lead">Translate a full-bleed image without pre-scaling it and the panel's own background shows at the extremes of the range. The rule of thumb: <code>scale</code> at least 1&nbsp;+&nbsp;(2&nbsp;&times;&nbsp;amplitude), so &plusmn;9% travel wants <code>scale:1.14</code> or more.</p>
        <ul class="fps-07__marks">
          <li><strong>photo</strong><span>&plusmn;9% travel &middot; scale 1.14</span></li>
          <li><strong>wash</strong><span>&plusmn;4% travel &middot; no scale needed</span></li>
          <li><strong>type</strong><span>+2.5% &rarr; &minus;1% &middot; fades in</span></li>
        </ul>
      </div>
    </section>

    <section class="fps-07__panel" style="--h:95" id="fps-07-s4" aria-labelledby="fps-07-h4">
      <img class="fps-07__photo" src="https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=1600&amp;auto=format" alt="Sunlight breaking through a stand of tall birch trees" width="1600" height="1067" loading="lazy" decoding="async">
      <span class="fps-07__wash" aria-hidden="true"></span>
      <div class="fps-07__stage">
        <p class="fps-07__eyebrow"><span class="fps-07__num">04 / 04</span><span class="fps-07__mono">prefers-reduced-motion</span></p>
        <h2 class="fps-07__title fps-07__title--sm" id="fps-07-h4">Reduced motion means fully static</h2>
        <p class="fps-07__lead">Parallax is one of the most reliable ways to make a reader queasy. When motion is reduced this demo removes the animations, resets every layer to its rest position, and switches snapping and smooth scrolling off &mdash; what is left is four photographic panels and nothing that moves.</p>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap');

.fps-07 {
  --ink: #ffffff;
  --muted: rgba(255,255,255,.76);
  --line: rgba(255,255,255,.24);
  --base: #0b0f14;
  --veil: .42;
  --sans: 'Geist',system-ui,-apple-system,'Segoe UI',sans-serif;
  --mono: 'Geist Mono',ui-monospace,'SFMono-Regular',Menlo,monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  position: relative;
  isolation: isolate;
  background: var(--base);
  color: var(--ink);
  font-family: var(--sans);
  -webkit-font-smoothing: antialiased;
}

.fps-07 * {
  box-sizing: border-box;
}

.fps-07 h2,
.fps-07 p,
.fps-07 ul,
.fps-07 pre {
  margin: 0;
}

.fps-07 code {
  font-family: var(--mono);
  font-size: .92em;
}

.fps-07__sr,
.fps-07__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.fps-07__theme {
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
  color: #fff;
  background: rgba(0,0,0,.32);
  border: 1px solid var(--line);
  -webkit-backdrop-filter: blur(10px) saturate(150%);
  backdrop-filter: blur(10px) saturate(150%);
}

.fps-07__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.fps-07__theme svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.fps-07__moon {
  display: none;
}

.fps-07__sr:focus-visible + .fps-07__theme {
  outline: 2px solid #fff;
  outline-offset: 3px;
}

.fps-07__scroller {
  block-size: 100dvh;
  overflow-y: auto;
  overflow-x: hidden;
  scroll-snap-type: y mandatory;
  scroll-behavior: smooth;
  overscroll-behavior-y: contain;
  scrollbar-width: none;
}

.fps-07__scroller::-webkit-scrollbar {
  width: 0;
  height: 0;
}

.fps-07__scroller:focus-visible {
  outline: 2px solid #fff;
  outline-offset: -2px;
}

.fps-07__panel {
  position: relative;
  min-block-size: 100dvh;
  scroll-snap-align: start;
  overflow: hidden;
  isolation: isolate;
  display: flex;
  align-items: flex-end;
  justify-content: flex-start;
  padding: clamp(2rem,5vh,3.5rem) clamp(1.25rem,5vw,4.5rem) calc(clamp(2.5rem,7vh,4.5rem) + 3.5rem);
  background: hsl(var(--h) 30% 12%);
}

.fps-07__panel + .fps-07__panel {
  margin-block-start: -3.5rem;
  border-start-start-radius: 2rem;
  border-start-end-radius: 2rem;
  border-block-start: 1px solid var(--line);
}

@supports not (height: 100dvh) {
  .fps-07__scroller {
    block-size: 100vh;
  }

  .fps-07__panel {
    min-block-size: 100vh;
  }
}

.fps-07__photo {
  position: absolute;
  inset: 0;
  z-index: -2;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  scale: 1.16;
  translate: 0 0;
  border-radius: inherit;
}

.fps-07__wash {
  position: absolute;
  inset: -6% 0;
  z-index: -1;
  pointer-events: none;
  border-radius: inherit;
  background: linear-gradient(to top,rgba(0,0,0,.86) 0%,rgba(0,0,0,.45) 42%,rgba(0,0,0,.12) 74%,rgba(0,0,0,.3) 100%), radial-gradient(120% 70% at 12% 88%,hsl(var(--h) 80% 42% / .45),transparent 70%);
}

@supports (background: oklch(50% .1 40 / .4)) {
  .fps-07__wash {
    background: linear-gradient(to top,rgba(0,0,0,.86) 0%,rgba(0,0,0,.45) 42%,rgba(0,0,0,.12) 74%,rgba(0,0,0,.3) 100%), radial-gradient(120% 70% at 12% 88%,oklch(52% .17 calc(var(--h) * 1deg) / .5),transparent 70%);
  }
}

@supports (animation-timeline: view()) {
  .fps-07__panel {
    view-timeline-name: --fps07;
    view-timeline-axis: block;
  }

  .fps-07__photo {
    animation: fps-07-back linear both;
    animation-timeline: --fps07;
    animation-range: cover 0% cover 100%;
  }

  .fps-07__wash {
    animation: fps-07-mid linear both;
    animation-timeline: --fps07;
    animation-range: cover 0% cover 100%;
  }

  .fps-07__stage {
    animation: fps-07-fore linear both;
    animation-timeline: --fps07;
    animation-range: cover 12% cover 62%;
  }
}

@keyframes fps-07-back {
  from {
    translate: 0 -9%;
    scale: 1.16;
  }

  to {
    translate: 0 9%;
    scale: 1.16;
  }
}

@keyframes fps-07-mid {
  from {
    translate: 0 -4%;
  }

  to {
    translate: 0 4%;
  }
}

@keyframes fps-07-fore {
  from {
    translate: 0 3%;
    opacity: .4;
  }

  60%,
    100% {
    translate: 0 0;
    opacity: 1;
  }
}

.fps-07__stage {
  inline-size: min(56rem,100%);
  display: grid;
  gap: clamp(.85rem,2vh,1.35rem);
  justify-items: start;
}

.fps-07__eyebrow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: .7rem;
}

.fps-07__num {
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #fff;
}

.fps-07__mono {
  font-family: var(--mono);
  font-size: .7rem;
  color: var(--muted);
  padding: .22rem .5rem;
  border-radius: .45rem;
  border: 1px solid var(--line);
  background: rgba(0,0,0,.28);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
}

.fps-07__title {
  font-size: clamp(2.1rem,6.4vw,4.6rem);
  line-height: 1.0;
  letter-spacing: -.045em;
  font-weight: 600;
  max-inline-size: 20ch;
  text-wrap: balance;
  text-shadow: 0 2px 30px rgba(0,0,0,.5);
}

.fps-07__title--sm {
  font-size: clamp(1.7rem,4vw,3rem);
  letter-spacing: -.035em;
  max-inline-size: 26ch;
}

.fps-07__lead {
  font-size: clamp(1rem,1.4vw,1.16rem);
  line-height: 1.6;
  color: var(--muted);
  max-inline-size: 58ch;
  text-wrap: pretty;
  text-shadow: 0 1px 18px rgba(0,0,0,.55);
}

.fps-07__lead code {
  color: #fff;
}

.fps-07__cue {
  display: flex;
  align-items: center;
  gap: .55rem;
  font-family: var(--mono);
  font-size: .8rem;
  color: var(--muted);
}

.fps-07__cue svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
  animation: fps-07-bob 2.4s ease-in-out infinite;
}

@keyframes fps-07-bob {
  0%,
    100% {
    translate: 0 -2px;
  }

  50% {
    translate: 0 3px;
  }
}

.fps-07__code {
  padding: .95rem 1.1rem;
  border-radius: 1rem;
  border: 1px solid var(--line);
  overflow-x: auto;
  background: rgba(0,0,0,.4);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
}

.fps-07__code code {
  font-size: clamp(.76rem,1vw,.86rem);
  line-height: 1.7;
  color: var(--muted);
  white-space: pre;
}

.fps-07__code mark {
  background: transparent;
  color: #fff;
  font-weight: 500;
}

.fps-07__marks {
  list-style: none;
  padding: 0;
  display: grid;
  gap: .3rem;
  inline-size: min(34rem,100%);
}

.fps-07__marks li {
  display: grid;
  grid-template-columns: 5rem 1fr;
  gap: 1rem;
  padding: .6rem 0;
  border-block-start: 1px solid var(--line);
  align-items: baseline;
}

.fps-07__marks strong {
  font-family: var(--mono);
  font-size: .78rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  font-weight: 500;
}

.fps-07__marks span {
  font-family: var(--mono);
  font-size: .82rem;
  color: var(--muted);
}

.fps-07[data-theme="dark"],
.fps-07:has(#fps-07-dark:checked) {
  --veil: .62;
}

.fps-07:has(#fps-07-dark:checked) .fps-07__photo {
  opacity: .72;
}

.fps-07:has(#fps-07-dark:checked) .fps-07__sun {
  display: none;
}

.fps-07:has(#fps-07-dark:checked) .fps-07__moon {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .fps-07:not([data-theme="light"]):not(:has(#fps-07-dark:checked)) .fps-07__photo {
    opacity: .72;
  }

  .fps-07:not([data-theme="light"]):not(:has(#fps-07-dark:checked)) .fps-07__sun {
    display: none;
  }

  .fps-07:not([data-theme="light"]):not(:has(#fps-07-dark:checked)) .fps-07__moon {
    display: block;
  }
}

@supports not selector(:has(*)) {
  .fps-07__theme {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fps-07__scroller {
    scroll-snap-type: none;
    scroll-behavior: auto;
  }

  .fps-07 *,
    .fps-07 *::before,
    .fps-07 *::after {
    animation: none !important;
    transition: none !important;
  }

  .fps-07__photo {
    translate: 0 0 !important;
    scale: 1.02 !important;
  }

  .fps-07__wash {
    translate: 0 0 !important;
  }

  .fps-07__stage {
    translate: 0 0 !important;
    opacity: 1 !important;
  }
}

@media (forced-colors: active) {
  .fps-07__wash {
    display: none;
  }

  .fps-07__panel {
    background: Canvas;
    color: CanvasText;
  }

  .fps-07__code,
    .fps-07__mono,
    .fps-07__theme {
    background: Canvas;
    border-color: CanvasText;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }
}
```
