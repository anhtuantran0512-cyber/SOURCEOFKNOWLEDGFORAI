---
source: "codefronts"
url: "https://codefronts.com/layouts/css-full-page-sections/css-full-screen-portfolio-gallery-scroll-sections/"
title: "CSS Full Screen Portfolio Gallery Scroll Sections"
section: "layouts"
category: "css-full-page-sections"
category_name: "CSS Full Page Sections"
description: "Five full-viewport panels, one project each: a full-bleed photograph, a serif project title, and a role / year / discipline line set in monospace."
has_js: "false"
---

Here's a working CSS Full Page Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Full Screen Portfolio Gallery Scroll Sections
Source: https://codefronts.com/layouts/css-full-page-sections/css-full-screen-portfolio-gallery-scroll-sections/

Five full-viewport panels, one project each: a full-bleed photograph, a serif project title, and a role / year / discipline line set in monospace. object-fit: cover keeps every image undistorted at any aspect ratio, and the next panel's rounded top edge always shows so the reader knows there is more work below.
## HTML
```html
<div class="fps-10">
  <input class="fps-10__sr" type="checkbox" id="fps-10-dark">
  <label class="fps-10__theme" for="fps-10-dark" title="Switch light or dark theme">
    <svg class="fps-10__sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.4" stroke="currentColor" stroke-width="1.7"/><path d="M12 2.6v2.3M12 19.1v2.3M2.6 12h2.3M19.1 12h2.3M5.3 5.3l1.7 1.7M17 17l1.7 1.7M18.7 5.3L17 7M7 17l-1.7 1.7" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <svg class="fps-10__moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.4A8.4 8.4 0 0 1 9.6 3.5 8.6 8.6 0 1 0 20.5 14.4Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <span class="fps-10__vh">Switch light or dark theme</span>
  </label>

  <div class="fps-10__scroller" tabindex="0" role="group" aria-label="Selected work, five projects">

    <section class="fps-10__panel" id="fps-10-s1" aria-labelledby="fps-10-h1">
      <img class="fps-10__img" style="object-position:50% 46%" src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600&amp;auto=format" alt="Sunlit minimalist living space with pale timber flooring" width="1600" height="1067" loading="eager" decoding="async" fetchpriority="high">
      <span class="fps-10__scrim" aria-hidden="true"></span>
      <div class="fps-10__stage">
        <p class="fps-10__collection">Selected work &mdash; Maya Okonkwo</p>
        <p class="fps-10__index"><span>01</span> / 05</p>
        <h2 class="fps-10__title" id="fps-10-h1">Nordhavn Interiors</h2>
        <p class="fps-10__meta"><span>Art direction &amp; web</span><span>2026</span><span>Retail</span></p>
        <p class="fps-10__note">A 340-page catalogue reduced to eleven full-screen rooms. Bounce rate fell 22% in the first month.</p>
        <p class="fps-10__cue"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5v13.5M6.5 12.6 12 18.2l5.5-5.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Four more below</p>
      </div>
    </section>

    <section class="fps-10__panel" id="fps-10-s2" aria-labelledby="fps-10-h2">
      <img class="fps-10__img" style="object-position:50% 40%" src="https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=1600&amp;auto=format" alt="Empty open-plan studio office with glass partitions" width="1600" height="1067" loading="lazy" decoding="async">
      <span class="fps-10__scrim" aria-hidden="true"></span>
      <div class="fps-10__stage">
        <p class="fps-10__index"><span>02</span> / 05</p>
        <h2 class="fps-10__title" id="fps-10-h2">Fold Workspace</h2>
        <p class="fps-10__meta"><span>Product design</span><span>2026</span><span>SaaS</span></p>
        <p class="fps-10__note">Desk booking for hybrid teams. Shipped the floor-plan picker in six weeks with two engineers.</p>
      </div>
    </section>

    <section class="fps-10__panel" id="fps-10-s3" aria-labelledby="fps-10-h3">
      <img class="fps-10__img" style="object-position:50% 52%" src="https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=1600&amp;auto=format" alt="Low lounge seating beside a dark panelled wall" width="1600" height="1067" loading="lazy" decoding="async">
      <span class="fps-10__scrim" aria-hidden="true"></span>
      <div class="fps-10__stage">
        <p class="fps-10__index"><span>03</span> / 05</p>
        <h2 class="fps-10__title" id="fps-10-h3">Ashgrove Hotel</h2>
        <p class="fps-10__meta"><span>Identity &amp; booking flow</span><span>2025</span><span>Hospitality</span></p>
        <p class="fps-10__note">One-screen-per-room booking. Direct reservations up 31% against the previous template.</p>
      </div>
    </section>

    <section class="fps-10__panel" id="fps-10-s4" aria-labelledby="fps-10-h4">
      <img class="fps-10__img" style="object-position:50% 38%" src="https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=1600&amp;auto=format" alt="Four colleagues reviewing work around a meeting table" width="1600" height="1067" loading="lazy" decoding="async">
      <span class="fps-10__scrim" aria-hidden="true"></span>
      <div class="fps-10__stage">
        <p class="fps-10__index"><span>04</span> / 05</p>
        <h2 class="fps-10__title" id="fps-10-h4">Quorum Research</h2>
        <p class="fps-10__meta"><span>Design system</span><span>2025</span><span>Civic</span></p>
        <p class="fps-10__note">Forty-one components, one accessibility audit, zero contrast failures at hand-off.</p>
      </div>
    </section>

    <section class="fps-10__panel" id="fps-10-s5" aria-labelledby="fps-10-h5">
      <img class="fps-10__img" style="object-position:50% 44%" src="https://images.unsplash.com/photo-1531297484001-80022131f5a1?w=1600&amp;auto=format" alt="Laptop on a desk lit by saturated pink and blue light" width="1600" height="1067" loading="lazy" decoding="async">
      <span class="fps-10__scrim" aria-hidden="true"></span>
      <div class="fps-10__stage">
        <p class="fps-10__index"><span>05</span> / 05</p>
        <h2 class="fps-10__title" id="fps-10-h5">Halcyon Player</h2>
        <p class="fps-10__meta"><span>Interaction design</span><span>2024</span><span>Audio</span></p>
        <p class="fps-10__note">A listening app with one control. Retention at day 30 doubled after the redesign.</p>
        <a class="fps-10__top" href="#fps-10-s1">Back to the first project</a>
      </div>
    </section>

  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Geist+Mono:wght@400;500&family=Geist:wght@400;500&family=Instrument+Serif:ital@0;1&display=swap');

.fps-10 {
  --ink: #ffffff;
  --muted: rgba(255,255,255,.74);
  --line: rgba(255,255,255,.26);
  --base: #0a0a0c;
  --serif: 'Instrument Serif',ui-serif,Georgia,'Times New Roman',serif;
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

.fps-10 * {
  box-sizing: border-box;
}

.fps-10 h2,
.fps-10 p {
  margin: 0;
}

.fps-10__sr,
.fps-10__vh {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.fps-10__theme {
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
  background: rgba(0,0,0,.34);
  border: 1px solid var(--line);
  -webkit-backdrop-filter: blur(10px) saturate(150%);
  backdrop-filter: blur(10px) saturate(150%);
}

.fps-10__theme::after {
  content: '';
  position: absolute;
  inset: -2px;
  border-radius: inherit;
}

.fps-10__theme svg {
  inline-size: 1.05rem;
  block-size: 1.05rem;
}

.fps-10__moon {
  display: none;
}

.fps-10__sr:focus-visible + .fps-10__theme {
  outline: 2px solid #fff;
  outline-offset: 3px;
}

.fps-10__scroller {
  block-size: 100dvh;
  overflow-y: auto;
  overflow-x: hidden;
  scroll-snap-type: y mandatory;
  scroll-behavior: smooth;
  overscroll-behavior-y: contain;
  scrollbar-width: none;
}

.fps-10__scroller::-webkit-scrollbar {
  width: 0;
  height: 0;
}

.fps-10__scroller:focus-visible {
  outline: 2px solid #fff;
  outline-offset: -2px;
}

.fps-10__panel {
  position: relative;
  min-block-size: 100dvh;
  scroll-snap-align: start;
  overflow: hidden;
  isolation: isolate;
  display: flex;
  align-items: flex-end;
  padding: clamp(2rem,5vh,3.5rem) clamp(1.25rem,5vw,4.5rem) calc(clamp(2.5rem,6vh,4rem) + 3.5rem);
  background: #141418;
}

.fps-10__panel + .fps-10__panel {
  margin-block-start: -3.5rem;
  border-start-start-radius: 2rem;
  border-start-end-radius: 2rem;
  border-block-start: 1px solid var(--line);
}

@supports not (height: 100dvh) {
  .fps-10__scroller {
    block-size: 100vh;
  }

  .fps-10__panel {
    min-block-size: 100vh;
  }
}

.fps-10__img {
  position: absolute;
  inset: 0;
  z-index: -2;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  border-radius: inherit;
}

.fps-10__scrim {
  position: absolute;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  border-radius: inherit;
  background: linear-gradient(to top,rgba(0,0,0,.88) 0%,rgba(0,0,0,.5) 34%,rgba(0,0,0,.12) 66%,rgba(0,0,0,.28) 100%);
}

.fps-10__stage {
  inline-size: min(58rem,100%);
  display: grid;
  gap: clamp(.55rem,1.4vh,.9rem);
  justify-items: start;
}

.fps-10__collection {
  font-family: var(--mono);
  font-size: .7rem;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--muted);
  padding: .3rem .6rem;
  border: 1px solid var(--line);
  border-radius: .5rem;
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
}

.fps-10__index {
  font-family: var(--mono);
  font-size: .78rem;
  letter-spacing: .1em;
  color: var(--muted);
  font-variant-numeric: tabular-nums;
}

.fps-10__index span {
  color: #fff;
  font-size: 1rem;
}

.fps-10__title {
  font-family: var(--serif);
  font-weight: 400;
  font-size: clamp(2.9rem,10vw,7.5rem);
  line-height: .92;
  letter-spacing: -.02em;
  text-wrap: balance;
  text-shadow: 0 2px 40px rgba(0,0,0,.5);
}

.fps-10__meta {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem .75rem;
  align-items: center;
  font-family: var(--mono);
  font-size: .76rem;
  color: var(--muted);
}

.fps-10__meta span {
  padding: .25rem .55rem;
  border: 1px solid var(--line);
  border-radius: .45rem;
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
}

.fps-10__note {
  font-size: clamp(.95rem,1.3vw,1.1rem);
  line-height: 1.55;
  color: var(--muted);
  max-inline-size: 48ch;
  text-wrap: pretty;
  text-shadow: 0 1px 16px rgba(0,0,0,.6);
}

.fps-10__cue {
  display: flex;
  align-items: center;
  gap: .5rem;
  font-family: var(--mono);
  font-size: .76rem;
  color: var(--muted);
}

.fps-10__cue svg {
  inline-size: 1rem;
  block-size: 1rem;
  animation: fps-10-bob 2.4s ease-in-out infinite;
}

@keyframes fps-10-bob {
  0%,
    100% {
    translate: 0 -2px;
  }

  50% {
    translate: 0 3px;
  }
}

.fps-10__top {
  margin-block-start: .35rem;
  min-block-size: 2.75rem;
  display: inline-flex;
  align-items: center;
  padding: .7rem 1.15rem;
  border-radius: 999px;
  font-size: .9rem;
  text-decoration: none;
  color: #fff;
  border: 1px solid var(--line);
  background: rgba(0,0,0,.32);
  transition: background .2s ease;
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
}

.fps-10__top:hover {
  background: rgba(0,0,0,.55);
}

.fps-10__top:focus-visible {
  outline: 2px solid #fff;
  outline-offset: 3px;
}

.fps-10[data-theme="dark"] .fps-10__img,
.fps-10:has(#fps-10-dark:checked) .fps-10__img {
  opacity: .66;
}

.fps-10:has(#fps-10-dark:checked) .fps-10__sun {
  display: none;
}

.fps-10:has(#fps-10-dark:checked) .fps-10__moon {
  display: block;
}

@media (prefers-color-scheme: dark) {
  .fps-10:not([data-theme="light"]):not(:has(#fps-10-dark:checked)) .fps-10__img {
    opacity: .66;
  }

  .fps-10:not([data-theme="light"]):not(:has(#fps-10-dark:checked)) .fps-10__sun {
    display: none;
  }

  .fps-10:not([data-theme="light"]):not(:has(#fps-10-dark:checked)) .fps-10__moon {
    display: block;
  }
}

@supports not selector(:has(*)) {
  .fps-10__theme {
    display: none;
  }
}

@media (prefers-reduced-motion: reduce) {
  .fps-10__scroller {
    scroll-snap-type: none;
    scroll-behavior: auto;
  }

  .fps-10 *,
    .fps-10 *::before,
    .fps-10 *::after {
    animation: none !important;
    transition: none !important;
  }
}

@media (forced-colors: active) {
  .fps-10__scrim {
    display: none;
  }

  .fps-10__panel {
    background: Canvas;
    color: CanvasText;
  }

  .fps-10__collection,
    .fps-10__meta span,
    .fps-10__top,
    .fps-10__theme {
    border-color: CanvasText;
    background: Canvas;
    -webkit-backdrop-filter: none;
    backdrop-filter: none;
  }
}
```
