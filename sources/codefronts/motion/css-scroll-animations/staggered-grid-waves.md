---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/staggered-grid-waves/"
title: "The Four View Timeline Ranges Compared"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "A view timeline exposes four named ranges and choosing the wrong one is the most common reason a scroll-bound animation feels mistimed."
has_js: "false"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: The Four View Timeline Ranges Compared
Source: https://codefronts.com/motion/css-scroll-animations/staggered-grid-waves/

A view timeline exposes four named ranges and choosing the wrong one is the most common reason a scroll-bound animation feels mistimed. Four identical cards, one per range, each labelled with exactly when it starts and ends — a reference card you can scroll rather than a spec paragraph you have to hold in your head.
## HTML
```html
<section class="sa-14" aria-labelledby="sa-14-h">
  <fieldset class="sa-14__theme">
    <legend class="sa-14__themelegend">Theme</legend>
    <input class="sa-14__themeinput" type="radio" name="sa-14-theme" id="sa-14-theme-auto" checked>
    <label class="sa-14__themeopt" for="sa-14-theme-auto">Auto</label>
    <input class="sa-14__themeinput" type="radio" name="sa-14-theme" id="sa-14-theme-light">
    <label class="sa-14__themeopt" for="sa-14-theme-light">Light</label>
    <input class="sa-14__themeinput" type="radio" name="sa-14-theme" id="sa-14-theme-dark">
    <label class="sa-14__themeopt" for="sa-14-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-14__stage">
    <header class="sa-14__head">
      <p class="sa-14__eyebrow">Reference · four ranges</p>
      <h2 class="sa-14__h" id="sa-14-h">cover, contain, entry, exit</h2>
      <p class="sa-14__sub">Four identical cards. Identical keyframes. Only <span class="sa-14__mono">animation-range</span> differs. Scroll slowly and watch where each one starts and stops moving.</p>
    </header>

    <div class="sa-14__scroller" tabindex="0" role="region" aria-label="Four view timeline ranges, scrollable">
      <div class="sa-14__inner">
        <p class="sa-14__hint">Scroll down · each card is its own subject</p>

        <article class="sa-14__card sa-14__card--cover">
          <p class="sa-14__rname">cover</p>
          <p class="sa-14__rdef">Starts the instant the card first overlaps the scrollport. Ends the instant it no longer overlaps at all.</p>
          <p class="sa-14__ruse">Use for a full scrub that should consume every available pixel of the card's passage.</p>
        </article>

        <article class="sa-14__card sa-14__card--contain">
          <p class="sa-14__rname">contain</p>
          <p class="sa-14__rdef">Starts when the card is fully inside the scrollport. Ends when it stops being fully inside.</p>
          <p class="sa-14__ruse">Use while the card is completely readable. Collapses to zero length if the card is taller than the scrollport.</p>
        </article>

        <article class="sa-14__card sa-14__card--entry">
          <p class="sa-14__rname">entry</p>
          <p class="sa-14__rdef">Starts at first overlap. Ends when the card is fully inside the scrollport.</p>
          <p class="sa-14__ruse">Use for arrival motion that must be finished by the time the card has landed.</p>
        </article>

        <article class="sa-14__card sa-14__card--exit">
          <p class="sa-14__rname">exit</p>
          <p class="sa-14__rdef">Starts when the card begins to leave the scrollport. Ends when it has fully left.</p>
          <p class="sa-14__ruse">Use for departure treatments — dimming a card that is on its way out of view.</p>
        </article>

        <p class="sa-14__hint">Scroll back up. Every range runs backward, because progress is position.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.sa-14 {
  --page: #faf8f3;
  --surface: #ffffff;
  --ink: #14120e;
  --muted: #5d574c;
  --rule: #d9d3c6;
  --accent: #14120e;
  --page: oklch(97.5% 0.008 85);
  --surface: oklch(100% 0 0);
  --ink: oklch(17% 0.01 70);
  --muted: oklch(48% 0.015 70);
  --rule: oklch(86% 0.014 80);
  --accent: oklch(17% 0.01 70);
  --font-display: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
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

.sa-14 *,
.sa-14 *::before,
.sa-14 *::after {
  box-sizing: border-box;
}

.sa-14__stage {
  max-inline-size: 46rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.sa-14__head {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  padding-block-end: 1.5rem;
  border-block-end: 1px solid var(--rule);
}

.sa-14__eyebrow {
  margin: 0;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--muted);
}

.sa-14__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.75rem, 5.5vw, 2.875rem);
  font-weight: 400;
  font-style: italic;
  letter-spacing: -0.02em;
  line-height: 1.08;
}

.sa-14__sub {
  margin: 0;
  font-size: 1rem;
  line-height: 1.7;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-14__mono {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.85em;
  color: var(--ink);
}

.sa-14__scroller {
  block-size: 62vh;
  min-block-size: 21rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  border-block: 1px solid var(--rule);
}

.sa-14__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sa-14__inner {
  display: flex;
  flex-direction: column;
  gap: 3rem;
  padding: 3rem 0.25rem 6rem;
}

.sa-14__hint {
  margin: 0;
  font-size: 0.75rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
}

.sa-14__card {
  display: flex;
  flex-direction: column;
  gap: 0.625rem;
  padding: 1.75rem 0 1.75rem 1.5rem;
  border-inline-start: 1px solid var(--rule);
  border-block-end: 1px solid var(--rule);
  background: var(--surface);
  opacity: 1;
  transform: none;
  min-inline-size: 0;
}

.sa-14__rname {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 1.375rem;
  font-weight: 500;
  letter-spacing: -0.02em;
}

.sa-14__rdef {
  margin: 0;
  font-family: var(--font-display);
  font-size: 1.0625rem;
  line-height: 1.55;
  text-wrap: pretty;
}

.sa-14__ruse {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

@keyframes sa-14-shift {
  from {
    opacity: 0.18;
    transform: translateY(1.5rem);
  }

  to {
    opacity: 1;
    transform: none;
  }
}

@supports (animation-timeline: view()) {
  .sa-14__card {
    animation: sa-14-shift linear both;
    animation-timeline: view(block);
  }

  .sa-14__card--cover {
    animation-range: cover;
  }

  .sa-14__card--contain {
    animation-range: contain;
  }

  .sa-14__card--entry {
    animation-range: entry;
  }

  .sa-14__card--exit {
    animation-range: exit;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sa-14__card {
    animation: none;
    opacity: 1;
    transform: none;
  }
}

.sa-14__theme {
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

.sa-14__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-14__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-14__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.5rem;
  border-block-end: 2px solid transparent;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-14__themeinput:checked + .sa-14__themeopt {
  color: var(--ink);
  border-block-end-color: var(--ink);
}

.sa-14__themeinput:focus-visible + .sa-14__themeopt {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 34rem) {
  .sa-14 {
    padding: 4.25rem 1rem 3rem;
  }

  .sa-14__inner {
    gap: 2.25rem;
  }
}

@media (forced-colors: active) {
  .sa-14__card {
    border: 1px solid CanvasText;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-14:not(:has(#sa-14-theme-light:checked)) {
    --page: #16150f;
    --surface: #1d1c15;
    --ink: #f4f0e6;
    --muted: #a39c8c;
    --rule: #332f25;
    --accent: #f4f0e6;
  }
}

@media (prefers-color-scheme: light) {
  .sa-14:has(#sa-14-theme-dark:checked) {
    --page: #16150f;
    --surface: #1d1c15;
    --ink: #f4f0e6;
    --muted: #a39c8c;
    --rule: #332f25;
    --accent: #f4f0e6;
  }
}

[data-theme="dark"] .sa-14:not(:has(#sa-14-theme-light:checked)) {
  --page: #16150f;
  --surface: #1d1c15;
  --ink: #f4f0e6;
  --muted: #a39c8c;
  --rule: #332f25;
  --accent: #f4f0e6;
}

.sa-14:has(#sa-14-theme-dark:checked) {
  --page: #16150f;
  --surface: #1d1c15;
  --ink: #f4f0e6;
  --muted: #a39c8c;
  --rule: #332f25;
  --accent: #f4f0e6;
}

.sa-14:has(#sa-14-theme-light:checked) {
  --page: #faf8f3;
  --surface: #ffffff;
  --ink: #14120e;
  --muted: #5d574c;
  --rule: #d9d3c6;
  --accent: #14120e;
}
```
