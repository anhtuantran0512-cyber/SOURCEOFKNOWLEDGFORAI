---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/scroll-driven-svg-stroke-draw/"
title: "Scroll Driven SVG Stroke Dashoffset"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "Binding stroke-dashoffset to a scroll timeline draws a path as the reader descends."
has_js: "false"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll Driven SVG Stroke Dashoffset
Source: https://codefronts.com/motion/css-scroll-animations/scroll-driven-svg-stroke-draw/

Binding stroke-dashoffset to a scroll timeline draws a path as the reader descends. Two details make it predictable: pathLength normalisation, so the numbers do not depend on the real geometry, and stroke-dasharray, without which dashoffset has nothing to offset and the animation appears not to run at all.
## HTML
```html
<section class="sa-04" aria-labelledby="sa-04-h">
  <fieldset class="sa-04__theme">
    <legend class="sa-04__themelegend">Theme</legend>
    <input class="sa-04__themeinput" type="radio" name="sa-04-theme" id="sa-04-theme-auto" checked>
    <label class="sa-04__themeopt" for="sa-04-theme-auto">Auto</label>
    <input class="sa-04__themeinput" type="radio" name="sa-04-theme" id="sa-04-theme-light">
    <label class="sa-04__themeopt" for="sa-04-theme-light">Light</label>
    <input class="sa-04__themeinput" type="radio" name="sa-04-theme" id="sa-04-theme-dark">
    <label class="sa-04__themeopt" for="sa-04-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-04__stage">
    <header class="sa-04__head">
      <p class="sa-04__eyebrow">stroke-dashoffset</p>
      <h2 class="sa-04__h" id="sa-04-h">A path drawn by the scroll position</h2>
      <p class="sa-04__sub">The route is normalised with <span class="sa-04__mono">pathLength="100"</span>, so the dash arithmetic is percentages regardless of the curve's real length.</p>
    </header>

    <div class="sa-04__scroller" tabindex="0" role="region" aria-label="Sable rollout route, scrollable">
      <div class="sa-04__canvas">
        <svg class="sa-04__svg" viewBox="0 0 120 220" fill="none" aria-hidden="true" focusable="false">
          <path class="sa-04__ghost" d="M20 12 C 96 44, 24 84, 96 116 C 30 150, 92 172, 40 208" pathLength="100"></path>
          <path class="sa-04__path" d="M20 12 C 96 44, 24 84, 96 116 C 30 150, 92 172, 40 208" pathLength="100"></path>
        </svg>
      </div>
      <div class="sa-04__copy">
        <h3 class="sa-04__ch">Sable · staged rollout</h3>
        <p class="sa-04__p">The route is drawn as you descend and undrawn as you go back up. Progress is the scroll offset, so there is no state to reset.</p>
        <dl class="sa-04__spec">
          <div class="sa-04__srow"><dt class="sa-04__dt">stroke-dasharray</dt><dd class="sa-04__dd">100 200 — a dash the full length of the path, then a gap twice as long</dd></div>
          <div class="sa-04__srow"><dt class="sa-04__dt">stroke-dashoffset</dt><dd class="sa-04__dd">100 to 0 — pushes the dash out of view, then back in</dd></div>
          <div class="sa-04__srow"><dt class="sa-04__dt">pathLength</dt><dd class="sa-04__dd">100 — normalises the geometry so the two numbers above stay meaningful</dd></div>
          <div class="sa-04__srow"><dt class="sa-04__dt">cost</dt><dd class="sa-04__dd">painted, not composited — fine for one path, not for forty</dd></div>
        </dl>
        <p class="sa-04__p">Remove the dasharray and nothing appears to happen. That is the single most common failure with this technique.</p>
        <p class="sa-04__p">The ghost path underneath is the same geometry at a lower contrast. Drawing the route twice gives the reader a sense of how much is left, which a single stroke cannot.</p>
        <p class="sa-04__p">Splitting the route into two paths with adjacent ranges draws one segment after another, which suits a staged rollout better than one continuous line.</p>
        <p class="sa-04__p">If the stroke has to carry a gradient, apply it to the stroke rather than to a filter. Filters on a repainting path are the expensive combination.</p>
        <p class="sa-04__p">For a long map route, measure before you ship. One path is comfortable; a dozen animating at once is a different conversation.</p>
        <p class="sa-04__p">Reversing the draw is free. Scroll back up and the offset runs from 0 toward 100 again, because progress is position rather than playback.</p>
        <p class="sa-04__p">To draw from the other end, negate the offset: animate from <span class="sa-04__mono">-100</span> to <span class="sa-04__mono">0</span> and the dash enters from the opposite side.</p>
        <p class="sa-04__p">A round cap adds half a stroke width at each end, so a path that must land exactly on a marker should use a butt cap while you calibrate.</p>
        <p class="sa-04__p">Sable's rollout map uses this for the route and a transform for the moving pin. The pin costs nothing; the route is the part worth measuring.</p>
        <p class="sa-04__p">Under reduced motion the path is simply drawn — the finished state is the base style, so nothing needs to be undone.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.sa-04 {
  --page: #ffffff;
  --surface: #fafafa;
  --ink: #0c0c0c;
  --muted: #6a6a6a;
  --rule: #dcdcdc;
  --accent: #c5182b;
  --page: oklch(100% 0 0);
  --surface: oklch(98% 0 0);
  --ink: oklch(14% 0 0);
  --muted: oklch(52% 0 0);
  --rule: oklch(88% 0 0);
  --accent: oklch(50% 0.2 25);
  --font-display: "Times New Roman", "Iowan Old Style", Georgia, serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  position: relative;
  padding: 4.5rem 1.5rem 4rem;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

.sa-04 *,
.sa-04 *::before,
.sa-04 *::after {
  box-sizing: border-box;
}

.sa-04__stage {
  max-inline-size: 54rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.sa-04__head {
  display: flex;
  flex-direction: column;
  gap: 0.625rem;
  padding-block-end: 1.25rem;
  border-block-end: 1px solid var(--rule);
}

.sa-04__eyebrow {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sa-04__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.75rem, 5vw, 2.75rem);
  font-weight: 400;
  letter-spacing: -0.02em;
  line-height: 1.08;
}

.sa-04__sub {
  margin: 0;
  max-inline-size: 42rem;
  font-size: 0.9375rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-04__mono {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.85em;
  color: var(--ink);
}

.sa-04__scroller {
  display: grid;
  grid-template-columns: 8rem minmax(0, 1fr);
  gap: 1.5rem;
  block-size: 60vh;
  min-block-size: 20rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  border-block: 1px solid var(--rule);
  scroll-timeline: --sa-04-route block;
}

.sa-04__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.sa-04__canvas {
  position: sticky;
  inset-block-start: 0;
  align-self: start;
  padding-block: 1.5rem;
  border-inline-end: 1px solid var(--rule);
}

.sa-04__svg {
  display: block;
  inline-size: 100%;
  block-size: auto;
}

.sa-04__ghost {
  stroke: var(--rule);
  stroke-width: 2.5;
  stroke-linecap: round;
}

.sa-04__path {
  stroke: var(--accent);
  stroke-width: 3;
  stroke-linecap: round;
  stroke-dasharray: 100 200;
  stroke-dashoffset: 0;
}

.sa-04__copy {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  min-block-size: 30rem;
  padding: 1.5rem 0 3rem;
  min-inline-size: 0;
}

.sa-04__ch {
  margin: 0;
  font-family: var(--font-display);
  font-size: 1.25rem;
  font-weight: 400;
}

.sa-04__p {
  margin: 0;
  font-size: 0.9375rem;
  line-height: 1.7;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-04__spec {
  margin: 0;
  display: flex;
  flex-direction: column;
}

.sa-04__srow {
  display: grid;
  grid-template-columns: minmax(0, 9rem) minmax(0, 1fr);
  gap: 0.75rem;
  padding-block: 0.625rem;
  border-block-start: 1px solid var(--rule);
}

.sa-04__dt {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.02em;
  color: var(--accent);
  min-inline-size: 0;
}

.sa-04__dd {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.5;
  color: var(--muted);
  min-inline-size: 0;
  text-wrap: pretty;
}

@keyframes sa-04-draw {
  from {
    stroke-dashoffset: 100;
  }

  to {
    stroke-dashoffset: 0;
  }
}

@supports (animation-timeline: scroll()) {
  .sa-04__path {
    animation: sa-04-draw linear both;
    animation-timeline: --sa-04-route;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sa-04__path {
    animation: none;
    stroke-dashoffset: 0;
  }
}

.sa-04__theme {
  position: absolute;
  inset-block-start: 1.25rem;
  inset-inline-end: 1.25rem;
  z-index: 9;
  display: inline-flex;
  gap: 0.25rem;
  margin: 0;
  padding: 0;
  border: 0;
}

.sa-04__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-04__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-04__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.5rem;
  border-block-end: 2px solid transparent;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.625rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-04__themeinput:checked + .sa-04__themeopt {
  color: var(--accent);
  border-block-end-color: var(--accent);
}

.sa-04__themeinput:focus-visible + .sa-04__themeopt {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 40rem) {
  .sa-04__scroller {
    grid-template-columns: 5rem minmax(0, 1fr);
    gap: 1rem;
  }

  .sa-04 {
    padding: 4.5rem 1rem 3rem;
  }
}

@media (forced-colors: active) {
  .sa-04__path {
    stroke: Highlight;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-04:not(:has(#sa-04-theme-light:checked)) {
    --page: #0b0b0b;
    --surface: #131313;
    --ink: #f2f2f2;
    --muted: #9a9a9a;
    --rule: #262626;
    --accent: #ff5a68;
  }
}

@media (prefers-color-scheme: light) {
  .sa-04:has(#sa-04-theme-dark:checked) {
    --page: #0b0b0b;
    --surface: #131313;
    --ink: #f2f2f2;
    --muted: #9a9a9a;
    --rule: #262626;
    --accent: #ff5a68;
  }
}

[data-theme="dark"] .sa-04:not(:has(#sa-04-theme-light:checked)) {
  --page: #0b0b0b;
  --surface: #131313;
  --ink: #f2f2f2;
  --muted: #9a9a9a;
  --rule: #262626;
  --accent: #ff5a68;
}

.sa-04:has(#sa-04-theme-dark:checked) {
  --page: #0b0b0b;
  --surface: #131313;
  --ink: #f2f2f2;
  --muted: #9a9a9a;
  --rule: #262626;
  --accent: #ff5a68;
}

.sa-04:has(#sa-04-theme-light:checked) {
  --page: #ffffff;
  --surface: #fafafa;
  --ink: #0c0c0c;
  --muted: #6a6a6a;
  --rule: #dcdcdc;
  --accent: #c5182b;
}
```
