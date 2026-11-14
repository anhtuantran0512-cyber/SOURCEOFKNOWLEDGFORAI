---
source: "codefronts"
url: "https://codefronts.com/components/css-svg-stroke-buttons/scroll-triggered-button-stroke-with-animation-timeline/"
title: "Scroll Triggered Button Stroke with animation-timeline"
section: "components"
category: "css-svg-stroke-buttons"
category_name: "CSS SVG Stroke Buttons"
description: "A long-form essay whose inline calls to action draw themselves as they rise into the column, and undraw if you scroll back up — with a reading-progress ring…"
has_js: "false"
---

Here's a working CSS SVG Stroke Button from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll Triggered Button Stroke with animation-timeline
Source: https://codefronts.com/components/css-svg-stroke-buttons/scroll-triggered-button-stroke-with-animation-timeline/

A long-form essay whose inline calls to action draw themselves as they rise into the column, and undraw if you scroll back up — with a reading-progress ring in the corner driven by scroll() rather than view(). No IntersectionObserver, no scroll listener, and an @supports not block that hands unsupported engines a finished border instead of an invisible one.
## HTML
```html
<section class="svgb-17">
  <input class="svgb-17__ti" type="checkbox" id="svgb-17-theme">
  <label class="svgb-17__toggle" for="svgb-17-theme">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor" stroke="none"/></svg>
    <span class="svgb-17__sr">Switch colour scheme</span>
  </label>
  <div class="svgb-17__scroller">
    <div class="svgb-17__meter" aria-hidden="true">
      <svg viewBox="0 0 56 56">
        <circle class="svgb-17__mbase" cx="28" cy="28" r="25" pathLength="1"/>
        <circle class="svgb-17__mfill" cx="28" cy="28" r="25" pathLength="1"/>
      </svg>
    </div>
    <article class="svgb-17__article">
      <p class="svgb-17__kicker">Craft &middot; Issue 04</p>
      <h1 class="svgb-17__h1">The line that draws itself</h1>
      <p class="svgb-17__lede">Scroll-driven animation moved a whole category of interaction out of JavaScript and into the style sheet. What it changed is not the effect &mdash; it is who owns the clock.</p>

      <p class="svgb-17__p">For a decade the recipe was fixed: observe the element, add a class, let a transition run. It worked, and it always carried the same three costs &mdash; a listener, a layout read, and a state that the browser could not reason about.</p>
      <p class="svgb-17__p">A view timeline replaces all three with a declaration. The element's progress through the scrollport <em>is</em> the animation's time, so scrolling backwards runs it backwards, and nothing has to be told when to start.</p>

      <div class="svgb-17__ctaline">
        <button class="svgb-17__btn" type="button">
          <svg class="svgb-17__frame" viewBox="0 0 300 62" aria-hidden="true">
            <rect class="svgb-17__base" x="2" y="2" width="296" height="58" rx="6" pathLength="1"/>
            <rect class="svgb-17__ink" x="2" y="2" width="296" height="58" rx="6" pathLength="1"/>
          </svg>
          <span class="svgb-17__label">Read the spec notes</span>
        </button>
        <span class="svgb-17__hint">entry 100% &rarr; contain 55%</span>
      </div>

      <p class="svgb-17__p">The range is the design decision. Begin at <code>entry 100%</code> &mdash; the instant the button is wholly inside the scrollport, never a pixel earlier &mdash; and finish at <code>contain 55%</code>, while it still sits well inside the viewport. The whole draw happens where the reader is actually looking.</p>
      <blockquote class="svgb-17__quote">A reveal that finishes late reads as a bug, because the reader is already looking at the thing you are still animating.</blockquote>
      <p class="svgb-17__p">Fill mode is the part that catches everyone. Without <code>both</code>, the animation applies only inside its range and the border reverts the moment you scroll past it.</p>

      <div class="svgb-17__ctaline">
        <button class="svgb-17__btn svgb-17__btn--late" type="button">
          <svg class="svgb-17__frame" viewBox="0 0 300 62" aria-hidden="true">
            <rect class="svgb-17__base" x="2" y="2" width="296" height="58" rx="6" pathLength="1"/>
            <rect class="svgb-17__ink" x="2" y="2" width="296" height="58" rx="6" pathLength="1"/>
          </svg>
          <span class="svgb-17__label">Subscribe to Craft</span>
        </button>
        <span class="svgb-17__hint">contain 10% &rarr; contain 50%</span>
      </div>

      <p class="svgb-17__p">Everything here degrades to a plain, fully drawn border where scroll-driven animation is unavailable &mdash; and to the same finished state for anyone who has asked for reduced motion.</p>
      <p class="svgb-17__end">&#9633;</p>
    </article>
  </div>
</section>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=Archivo:wght@400;500;600&display=swap');

.svgb-17 {
  --svgb-17-bg: #f6f4ef;
  --svgb-17-bg: oklch(0.968 0.008 85);
  --svgb-17-fg: #17161c;
  --svgb-17-fg: oklch(0.20 0.008 285);
  --svgb-17-muted: #6b6875;
  --svgb-17-muted: oklch(0.555 0.014 285);
  --svgb-17-rest: rgba(23, 22, 28, 0.16);
  --svgb-17-rest: oklch(0.20 0.008 285 / 0.16);
  --svgb-17-stroke: #a8320f;
  --svgb-17-stroke: oklch(0.48 0.17 38);
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  background: var(--svgb-17-bg);
  position: relative;
  color: var(--svgb-17-fg);
  font-family: 'Newsreader', ui-serif, Georgia, serif;
}

.svgb-17 *,
.svgb-17 *::before,
.svgb-17 *::after {
  box-sizing: border-box;
}

.svgb-17__scroller {
  block-size: 100svh;
  overflow-y: auto;
  overflow-x: hidden;
  scrollbar-width: thin;
  scrollbar-color: var(--svgb-17-rest) transparent;
}

.svgb-17__meter {
  position: sticky;
  z-index: 4;
  inset-block-start: calc(100svh - 76px);
  inset-inline-start: clamp(16px, 4vw, 40px);
  inline-size: 56px;
  block-size: 56px;
  margin-block-end: -56px;
}

.svgb-17__meter svg {
  inline-size: 100%;
  block-size: 100%;
  transform: rotate(-90deg);
  overflow: visible;
}

.svgb-17__meter circle {
  fill: none;
}

.svgb-17__mbase {
  stroke: var(--svgb-17-rest);
  stroke-width: 2px;
}

.svgb-17__mfill {
  stroke: var(--svgb-17-stroke);
  stroke-width: 2.6px;
  stroke-linecap: round;
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  animation: svgb-17-read linear both;
  animation-timeline: scroll(nearest block);
}

@keyframes svgb-17-read {
  to {
    stroke-dashoffset: 0;
  }
}

.svgb-17__article {
  max-width: 62ch;
  margin-inline: auto;
  padding: clamp(48px, 12vh, 120px) clamp(22px, 6vw, 40px) clamp(160px, 34vh, 340px);
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.svgb-17__kicker {
  margin: 0;
  font-family: 'Archivo', system-ui, sans-serif;
  font-size: 11px;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--svgb-17-stroke);
}

.svgb-17__h1 {
  margin: 0;
  font-size: clamp(38px, 7vw, 68px);
  font-weight: 400;
  line-height: 1.02;
  letter-spacing: -0.03em;
  text-wrap: balance;
}

.svgb-17__lede {
  margin: 0;
  font-size: clamp(19px, 2.4vw, 24px);
  line-height: 1.5;
  color: color-mix(in oklab, var(--svgb-17-fg) 82%, transparent);
}

.svgb-17__p {
  margin: 0;
  font-size: 18px;
  line-height: 1.66;
  text-wrap: pretty;
}

.svgb-17__p code {
  font-family: ui-monospace, monospace;
  font-size: 0.86em;
  padding: 1px 5px;
  border-radius: 4px;
  background: color-mix(in oklab, var(--svgb-17-fg) 7%, transparent);
}

.svgb-17__quote {
  margin: 10px 0;
  padding-inline-start: 22px;
  border-inline-start: 2px solid var(--svgb-17-stroke);
  font-size: clamp(20px, 2.6vw, 26px);
  font-style: italic;
  line-height: 1.4;
}

.svgb-17__end {
  margin: 18px 0 0;
  color: var(--svgb-17-muted);
}

.svgb-17__ctaline {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 16px;
  padding-block: 10px;
}

.svgb-17__hint {
  font-family: 'Archivo', system-ui, sans-serif;
  font-size: 11px;
  letter-spacing: 0.06em;
  color: var(--svgb-17-muted);
}

.svgb-17__btn {
  position: relative;
  inline-size: min(300px, 100%);
  block-size: 62px;
  display: grid;
  place-items: center;
  border: 0;
  padding: 0;
  border-radius: 6px;
  background: color-mix(in oklab, var(--svgb-17-stroke) 7%, transparent);
  color: inherit;
  font-family: 'Archivo', system-ui, sans-serif;
  font-size: 15px;
  font-weight: 500;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
}

.svgb-17__label {
  position: relative;
  z-index: 1;
}

.svgb-17__btn:focus-visible {
  outline: 2px solid var(--svgb-17-stroke);
  outline-offset: 4px;
}

.svgb-17__frame {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  overflow: visible;
}

.svgb-17__frame rect {
  fill: none;
  stroke-linecap: round;
}

.svgb-17__base {
  stroke: var(--svgb-17-rest);
  stroke-width: 1.4px;
}

@keyframes svgb-17-draw {
  to {
    stroke-dashoffset: 0;
  }
}

.svgb-17__ink {
  stroke: var(--svgb-17-stroke);
  stroke-width: 2.2px;
  stroke-dasharray: 1;
  stroke-dashoffset: 1;
  animation: svgb-17-draw linear both;
  animation-timeline: view();
  /* start only once the button is fully inside the scrollport, finish while it is
       still comfortably in view — so the draw is always watched, never missed */
  animation-range: entry 100% contain 55%;
}

.svgb-17__btn--late .svgb-17__ink {
  animation-range: contain 10% contain 50%;
}

@supports not (animation-timeline: view()) {
  .svgb-17__ink {
    animation: none;
    stroke-dashoffset: 0;
  }

  .svgb-17__mfill {
    animation: none;
    stroke-dashoffset: 0.65;
    opacity: 0.4;
  }
}

.svgb-17__ti {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.svgb-17__toggle {
  position: absolute;
  z-index: 6;
  inset-block-start: 16px;
  inset-inline-end: 22px;
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border-radius: 999px;
  border: 1px solid color-mix(in oklab, currentColor 20%, transparent);
  background: color-mix(in oklab, currentColor 8%, transparent);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  color: inherit;
  cursor: pointer;
  transition: background 160ms ease, transform 160ms ease;
}

.svgb-17__toggle:hover {
  background: color-mix(in oklab, currentColor 15%, transparent);
}

.svgb-17__toggle:active {
  transform: scale(0.94);
}

.svgb-17__toggle svg {
  inline-size: 18px;
  block-size: 18px;
  transition: transform 400ms cubic-bezier(0.2, 0.7, 0.3, 1);
}

.svgb-17__ti:checked + .svgb-17__toggle svg {
  transform: rotate(180deg);
}

.svgb-17__ti:focus-visible + .svgb-17__toggle {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.svgb-17__sr {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.svgb-17:has(#svgb-17-theme:checked) {
  --svgb-17-bg: #100f13;
  --svgb-17-bg: oklch(0.18 0.008 285);
  --svgb-17-fg: #f0eef4;
  --svgb-17-fg: oklch(0.96 0.006 285);
  --svgb-17-muted: #918e9b;
  --svgb-17-muted: oklch(0.68 0.014 285);
  --svgb-17-rest: rgba(240, 238, 244, 0.18);
  --svgb-17-rest: oklch(0.96 0.006 285 / 0.18);
  --svgb-17-stroke: #ff9070;
  --svgb-17-stroke: oklch(0.79 0.15 40);
}

@media (prefers-reduced-motion: reduce) {
  .svgb-17__ink {
    animation: none;
    stroke-dashoffset: 0;
  }

  .svgb-17__mfill {
    animation: none;
    stroke-dashoffset: 0.65;
    opacity: 0.4;
  }

  .svgb-17__toggle,
    .svgb-17__toggle svg {
    transition: none;
  }
}
```
