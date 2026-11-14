---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/scroll-driven-rotate-view-timeline/"
title: "Scroll Driven Rotate View Timeline"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "Rotation bound to scroll position with animation-timeline: view() and not a single scroll listener."
has_js: "false"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll Driven Rotate View Timeline
Source: https://codefronts.com/motion/css-rotate-animation/scroll-driven-rotate-view-timeline/

Rotation bound to scroll position with animation-timeline: view() and not a single scroll listener. Each marginal rule turns as its row passes through the scroller, driven entirely by the element's own visibility progress. The whole effect sits behind an @supports gate with a correctly-oriented static fallback declared first.
## HTML
```html
<section class="rot-08" aria-labelledby="rot-08-h">
  <fieldset class="rot-08__theme">
    <legend class="rot-08__themelegend">Theme</legend>
    <input class="rot-08__themeinput" type="radio" name="rot-08-theme" id="rot-08-theme-auto" checked>
    <label class="rot-08__themeopt" for="rot-08-theme-auto">Auto</label>
    <input class="rot-08__themeinput" type="radio" name="rot-08-theme" id="rot-08-theme-light">
    <label class="rot-08__themeopt" for="rot-08-theme-light">Light</label>
    <input class="rot-08__themeinput" type="radio" name="rot-08-theme" id="rot-08-theme-dark">
    <label class="rot-08__themeopt" for="rot-08-theme-dark">Dark</label>
  </fieldset>

  <div class="rot-08__stage">
    <header class="rot-08__head">
      <p class="rot-08__eyebrow">Quill Review · Field dispatch</p>
      <h2 class="rot-08__h" id="rot-08-h">The scroll position is the timeline</h2>
      <p class="rot-08__sub">Scroll the column. Each marginal mark turns according to how far its row has travelled through the scroller — no listener, no requestAnimationFrame.</p>
    </header>

    <div class="rot-08__scroller" tabindex="0" aria-label="Scrollable dispatch column">
      <article class="rot-08__row">
        <span class="rot-08__mark" aria-hidden="true"></span>
        <div class="rot-08__body">
          <h3 class="rot-08__rowh">The kiln at Vale</h3>
          <p class="rot-08__p">Fired twice a week since 1974. Sam Rivera keeps the log in pencil because the heat ruins ink, and the numbers have not moved more than two degrees in a decade.</p>
        </div>
      </article>
      <article class="rot-08__row">
        <span class="rot-08__mark" aria-hidden="true"></span>
        <div class="rot-08__body">
          <h3 class="rot-08__rowh">Ranger, eleven miles out</h3>
          <p class="rot-08__p">The survey boat runs a fixed transect. Its instruments log depth every four seconds, which over a season becomes the most boring and most useful dataset the office holds.</p>
        </div>
      </article>
      <article class="rot-08__row">
        <span class="rot-08__mark" aria-hidden="true"></span>
        <div class="rot-08__body">
          <h3 class="rot-08__rowh">A note on ranges</h3>
          <p class="rot-08__p">The default range covers an element's entire pass through the scrollport, which is why a scroll-bound rotation so often finishes before you have properly seen it start. Narrow the range and the motion lands where the reader is looking.</p>
        </div>
      </article>
      <article class="rot-08__row">
        <span class="rot-08__mark" aria-hidden="true"></span>
        <div class="rot-08__body">
          <h3 class="rot-08__rowh">Basalt yard, night shift</h3>
          <p class="rot-08__p">Jordan Lee walks the perimeter at two, again at five. The gate hinge has been rotating on the same pin for thirty years and nobody has thought to replace it.</p>
        </div>
      </article>
      <article class="rot-08__row">
        <span class="rot-08__mark" aria-hidden="true"></span>
        <div class="rot-08__body">
          <h3 class="rot-08__rowh">Where the fallback matters</h3>
          <p class="rot-08__p">In an engine without scroll-driven animations, every mark on this page sits at its resting angle and the column reads exactly as it should. That is the whole point of declaring the static state first.</p>
        </div>
      </article>
    </div>

    <p class="rot-08__fine">Gated behind <span class="rot-08__code">@supports (animation-timeline: view())</span>. Firefox has not shipped scroll-driven animations, so it renders the static angle declared above the gate.</p>
  </div>
</section>
```
## CSS
```css
.rot-08 {
  --page: #faf8f4;
  --surface: #faf8f4;
  --ink: #171310;
  --muted: #5f574e;
  --rule: #d9d2c7;
  --accent: #97141f;
  --turn: 90deg;
  --font-display: Georgia, "Times New Roman", "Liberation Serif", serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-display);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(0 0 0)) {
  .rot-08 {
    --accent: oklch(0.46 0.18 25);
  }
}

.rot-08 *,
.rot-08 *::before,
.rot-08 *::after {
  box-sizing: border-box;
}

.rot-08__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.25rem, 3vw, 1.75rem);
  padding: clamp(1.25rem, 4vw, 3rem);
  padding-block-start: 5.25rem;
}

.rot-08__head {
  max-inline-size: 36rem;
  min-inline-size: 0;
}

.rot-08__eyebrow {
  margin: 0 0 0.6rem;
  font-family: system-ui, sans-serif;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--accent);
}

.rot-08__h {
  margin: 0 0 0.6rem;
  font-size: clamp(1.5rem, 5vw, 2.5rem);
  font-weight: 400;
  line-height: 1.1;
  letter-spacing: -0.01em;
}

.rot-08__sub {
  margin: 0;
  font-family: system-ui, sans-serif;
  font-size: 0.9375rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-08__code {
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.8em;
  color: var(--accent);
}

.rot-08__scroller {
  inline-size: min(100%, 36rem);
  block-size: min(60vh, 26rem);
  overflow-y: auto;
  overscroll-behavior: contain;
  border-block: 1px solid var(--rule);
  scrollbar-width: thin;
}

.rot-08__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

.rot-08__row {
  display: grid;
  grid-template-columns: 3rem minmax(0, 1fr);
  gap: 1rem;
  padding: clamp(1.75rem, 6vw, 3rem) 0.25rem;
  border-block-end: 1px solid var(--rule);
}

.rot-08__row:last-child {
  border-block-end: 0;
}

.rot-08__mark {
  inline-size: 2rem;
  block-size: 2rem;
  border: 1.5px solid var(--accent);
  border-radius: 0.125rem;
  transform-origin: 50% 50%;
  transform: rotate(0deg);
}

.rot-08__mark::before {
  content: "";
  display: block;
  inline-size: 100%;
  block-size: 1.5px;
  margin-block-start: calc(50% - 0.75px);
  background: var(--accent);
}

.rot-08__body {
  min-inline-size: 0;
}

.rot-08__rowh {
  margin: 0 0 0.4rem;
  font-size: 1.125rem;
  font-weight: 400;
}

.rot-08__p {
  margin: 0;
  font-size: 0.9375rem;
  line-height: 1.7;
  color: var(--muted);
  text-wrap: pretty;
  min-inline-size: 0;
}

.rot-08__fine {
  inline-size: min(100%, 36rem);
  margin: 0;
  font-family: system-ui, sans-serif;
  font-size: 0.75rem;
  line-height: 1.6;
  color: var(--muted);
}

@supports (animation-timeline: view()) {
  .rot-08__scroller {
    scroll-timeline-name: none;
  }

  .rot-08__mark {
    animation: rot-08-scrollturn linear both;
    animation-timeline: view();
    animation-range: entry 10% cover 60%;
  }

  @keyframes rot-08-scrollturn {
    from {
      transform: rotate(0deg);
    }

    to {
      transform: rotate(var(--turn));
    }
  }
}

@media (prefers-reduced-motion: reduce) {
  .rot-08__mark {
    animation: none;
    transform: rotate(var(--turn));
  }
}

.rot-08__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 9;
  display: flex;
  align-items: center;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 8%, transparent);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  font-family: system-ui, sans-serif;
}

.rot-08__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-08__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-08__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.6875rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: inherit;
  opacity: 0.55;
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}

.rot-08__themeopt:hover {
  opacity: 0.85;
}

.rot-08__themeinput:checked + .rot-08__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-08__themeinput:focus-visible + .rot-08__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .rot-08__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-08__themeinput:checked + .rot-08__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: dark) {
  .rot-08:not(:has(#rot-08-theme-light:checked)) {
    --page: #100e0c;
    --surface: #100e0c;
    --ink: #f2ece4;
    --muted: #a1978b;
    --rule: #2b2620;
    --accent: #ff7d72;
  }
}

@media (prefers-color-scheme: light) {
  .rot-08:has(#rot-08-theme-dark:checked) {
    --page: #100e0c;
    --surface: #100e0c;
    --ink: #f2ece4;
    --muted: #a1978b;
    --rule: #2b2620;
    --accent: #ff7d72;
  }
}

[data-theme="dark"] .rot-08:not(:has(#rot-08-theme-light:checked)) {
  --page: #100e0c;
  --surface: #100e0c;
  --ink: #f2ece4;
  --muted: #a1978b;
  --rule: #2b2620;
  --accent: #ff7d72;
}

.rot-08:has(#rot-08-theme-dark:checked) {
  --page: #100e0c;
  --surface: #100e0c;
  --ink: #f2ece4;
  --muted: #a1978b;
  --rule: #2b2620;
  --accent: #ff7d72;
}

.rot-08:has(#rot-08-theme-light:checked) {
  --page: #faf8f4;
  --surface: #faf8f4;
  --ink: #171310;
  --muted: #5f574e;
  --rule: #d9d2c7;
  --accent: #97141f;
}
```
