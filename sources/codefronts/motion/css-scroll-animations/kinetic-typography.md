---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/kinetic-typography/"
title: "Scroll Timeline Axis and Horizontal Scrollers"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "Scroll timelines are not vertical by default so much as block by default."
has_js: "false"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Scroll Timeline Axis and Horizontal Scrollers
Source: https://codefronts.com/motion/css-scroll-animations/kinetic-typography/

Scroll timelines are not vertical by default so much as block by default. Switching to scroll(inline) or scroll-timeline-axis: inline binds progress to horizontal scrolling instead, which is what a filmstrip, a card rail or a table with frozen columns needs. The indicator here tracks inline progress across a nine-frame rail.
## HTML
```html
<section class="sa-13" aria-labelledby="sa-13-h">
  <fieldset class="sa-13__theme">
    <legend class="sa-13__themelegend">Theme</legend>
    <input class="sa-13__themeinput" type="radio" name="sa-13-theme" id="sa-13-theme-auto" checked>
    <label class="sa-13__themeopt" for="sa-13-theme-auto">Auto</label>
    <input class="sa-13__themeinput" type="radio" name="sa-13-theme" id="sa-13-theme-light">
    <label class="sa-13__themeopt" for="sa-13-theme-light">Light</label>
    <input class="sa-13__themeinput" type="radio" name="sa-13-theme" id="sa-13-theme-dark">
    <label class="sa-13__themeopt" for="sa-13-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-13__stage">
    <header class="sa-13__head">
      <p class="sa-13__eyebrow">axis: inline</p>
      <h2 class="sa-13__h" id="sa-13-h">The scrollbar that acts as the clock</h2>
      <p class="sa-13__sub">Drag the rail sideways, or focus it and use the arrow keys. Progress is read from the rail's horizontal overflow — <span class="sa-13__mono">scroll-timeline: --sa-13-rail inline</span>.</p>
    </header>

    <div class="sa-13__rail" tabindex="0" role="region" aria-label="Prism build frames, scrolls horizontally">
      <div class="sa-13__gauge">
        <p class="sa-13__glabel">inline<br>progress</p>
        <div class="sa-13__gtrack"><span class="sa-13__gfill"></span></div>
      </div>
      <ol class="sa-13__frames">
        <li class="sa-13__frame"><p class="sa-13__fnum">01</p><p class="sa-13__ft">Checkout</p><p class="sa-13__fm">prism/web · 0.9s</p></li>
        <li class="sa-13__frame"><p class="sa-13__fnum">02</p><p class="sa-13__ft">Restore cache</p><p class="sa-13__fm">hit · 4.2s</p></li>
        <li class="sa-13__frame"><p class="sa-13__fnum">03</p><p class="sa-13__ft">Install deps</p><p class="sa-13__fm">1,204 packages</p></li>
        <li class="sa-13__frame"><p class="sa-13__fnum">04</p><p class="sa-13__ft">Typecheck</p><p class="sa-13__fm">no errors</p></li>
        <li class="sa-13__frame"><p class="sa-13__fnum">05</p><p class="sa-13__ft">Unit tests</p><p class="sa-13__fm">912 passed</p></li>
        <li class="sa-13__frame"><p class="sa-13__fnum">06</p><p class="sa-13__ft">Bundle</p><p class="sa-13__fm">412 kB gzip</p></li>
        <li class="sa-13__frame"><p class="sa-13__fnum">07</p><p class="sa-13__ft">Visual diff</p><p class="sa-13__fm">2 to review</p></li>
        <li class="sa-13__frame"><p class="sa-13__fnum">08</p><p class="sa-13__ft">Sign artifacts</p><p class="sa-13__fm">Priya Sharma</p></li>
        <li class="sa-13__frame"><p class="sa-13__fnum">09</p><p class="sa-13__ft">Deploy to production</p><p class="sa-13__fm">Sable · eu-west</p></li>
      </ol>
    </div>

    <ul class="sa-13__facts">
      <li class="sa-13__fact"><span class="sa-13__fk">inline</span> resolves through writing mode. <span class="sa-13__fk">x</span> is physical and never changes.</li>
      <li class="sa-13__fact">The axis belongs to the timeline owner. Consumers only name the timeline.</li>
      <li class="sa-13__fact">No <span class="sa-13__mono">overflow-x</span> means no inline scroll to read, and no error either.</li>
    </ul>
  </div>
</section>
```
## CSS
```css
.sa-13 {
  --page: #000000;
  --surface: #0a0a0a;
  --ink: #f2f2f2;
  --muted: #7d7d7d;
  --rule: #1c1c1c;
  --accent: #b6ff2e;
  --page: oklch(0% 0 0);
  --surface: oklch(12% 0 0);
  --ink: oklch(96% 0 0);
  --muted: oklch(58% 0 0);
  --rule: oklch(21% 0 0);
  --accent: oklch(90% 0.22 122);
  --sa-13-frame: 11rem;
  --font-display: ui-monospace, "JetBrains Mono", "SFMono-Regular", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  position: relative;
  padding: 3.5rem 1rem 2.5rem;
  background: var(--page);
  color: var(--ink);
  font-family: var(--font-display);
}

.sa-13 *,
.sa-13 *::before,
.sa-13 *::after {
  box-sizing: border-box;
}

.sa-13__stage {
  max-inline-size: 64rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 0.875rem;
}

.sa-13__head {
  display: flex;
  flex-direction: column;
  gap: 0.375rem;
}

.sa-13__eyebrow {
  margin: 0;
  font-size: 0.6875rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.sa-13__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.25rem, 3.6vw, 1.875rem);
  font-weight: 500;
  letter-spacing: -0.03em;
  line-height: 1.1;
}

.sa-13__sub {
  margin: 0;
  max-inline-size: 46rem;
  font-family: system-ui, sans-serif;
  font-size: 0.8125rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-13__mono {
  color: var(--accent);
}

.sa-13__rail {
  display: flex;
  align-items: stretch;
  gap: 0.5rem;
  padding: 0.5rem;
  overflow-x: auto;
  overflow-y: hidden;
  overscroll-behavior-inline: contain;
  scroll-snap-type: inline mandatory;
  scroll-timeline: --sa-13-rail inline;
  background: var(--surface);
}

.sa-13__rail:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.sa-13__gauge {
  position: sticky;
  inset-inline-start: 0;
  z-index: 2;
  flex: 0 0 auto;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 0.5rem;
  inline-size: 4.25rem;
  padding: 0.625rem 0.5rem;
  background: var(--page);
}

.sa-13__glabel {
  margin: 0;
  font-size: 0.5625rem;
  line-height: 1.3;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
}

.sa-13__gtrack {
  block-size: 0.375rem;
  background: var(--rule);
}

.sa-13__gfill {
  display: block;
  block-size: 100%;
  inline-size: 100%;
  background: var(--accent);
  transform-origin: left center;
  transform: scaleX(1);
}

.sa-13__frames {
  display: flex;
  gap: 0.5rem;
  margin: 0;
  padding: 0;
  list-style: none;
}

.sa-13__frame {
  flex: 0 0 var(--sa-13-frame);
  scroll-snap-align: center;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  min-block-size: 9.5rem;
  padding: 0.625rem 0.75rem;
  border: 1px solid var(--rule);
  background: var(--page);
  min-inline-size: 0;
}

.sa-13__fnum {
  margin: 0 0 auto;
  font-size: 1.75rem;
  font-weight: 500;
  letter-spacing: -0.04em;
  color: var(--rule);
}

.sa-13__ft {
  margin: 0;
  font-size: 0.8125rem;
  font-weight: 500;
}

.sa-13__fm {
  margin: 0;
  font-size: 0.6875rem;
  color: var(--muted);
}

.sa-13__frame:nth-child(9) {
  border-color: var(--accent);
}

.sa-13__frame:nth-child(9) .sa-13__ft {
  color: var(--accent);
}

.sa-13__facts {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr));
  gap: 0.5rem;
}

.sa-13__fact {
  padding: 0.625rem 0.75rem;
  border-block-start: 1px solid var(--rule);
  font-family: system-ui, sans-serif;
  font-size: 0.75rem;
  line-height: 1.5;
  color: var(--muted);
  min-inline-size: 0;
  text-wrap: pretty;
}

.sa-13__fk {
  font-family: var(--font-display);
  color: var(--accent);
}

@keyframes sa-13-fill {
  from {
    transform: scaleX(0.02);
  }

  to {
    transform: scaleX(1);
  }
}

@supports (animation-timeline: scroll()) {
  .sa-13__gfill {
    animation: sa-13-fill linear both;
    animation-timeline: --sa-13-rail;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sa-13__gfill {
    animation: none;
    transform: scaleX(1);
  }

  .sa-13__rail {
    scroll-behavior: auto;
  }
}

.sa-13__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 9;
  display: inline-flex;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid var(--rule);
  background: var(--surface);
}

.sa-13__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-13__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-13__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.625rem;
  font-size: 0.625rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-13__themeinput:checked + .sa-13__themeopt {
  color: var(--page);
  background: var(--accent);
}

.sa-13__themeinput:focus-visible + .sa-13__themeopt {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 34rem) {
  .sa-13 {
    --sa-13-frame: 9.5rem;
    padding-block-start: 4.25rem;
  }
}

@media (forced-colors: active) {
  .sa-13__gfill {
    background: Highlight;
  }
}

@media (prefers-color-scheme: light) {
  .sa-13:not(:has(#sa-13-theme-dark:checked)) {
    --page: #ffffff;
    --surface: #f4f4f4;
    --ink: #101010;
    --muted: #5f5f5f;
    --rule: #dcdcdc;
    --accent: #3f7a00;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-13:has(#sa-13-theme-light:checked) {
    --page: #ffffff;
    --surface: #f4f4f4;
    --ink: #101010;
    --muted: #5f5f5f;
    --rule: #dcdcdc;
    --accent: #3f7a00;
  }
}

[data-theme="light"] .sa-13:not(:has(#sa-13-theme-dark:checked)) {
  --page: #ffffff;
  --surface: #f4f4f4;
  --ink: #101010;
  --muted: #5f5f5f;
  --rule: #dcdcdc;
  --accent: #3f7a00;
}

.sa-13:has(#sa-13-theme-light:checked) {
  --page: #ffffff;
  --surface: #f4f4f4;
  --ink: #101010;
  --muted: #5f5f5f;
  --rule: #dcdcdc;
  --accent: #3f7a00;
}

.sa-13:has(#sa-13-theme-light:checked) .sa-13__themeinput:checked + .sa-13__themeopt {
  color: #ffffff;
}

.sa-13:has(#sa-13-theme-dark:checked) {
  --page: #000000;
  --surface: #0a0a0a;
  --ink: #f2f2f2;
  --muted: #7d7d7d;
  --rule: #1c1c1c;
  --accent: #b6ff2e;
}
```
