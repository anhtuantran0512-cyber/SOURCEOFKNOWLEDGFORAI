---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/parallax-cosmos/"
title: "Animation Range Start and End Control"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "By default an animation spans its entire timeline."
has_js: "false"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Animation Range Start and End Control
Source: https://codefronts.com/motion/css-scroll-animations/parallax-cosmos/

By default an animation spans its entire timeline. animation-range-start and animation-range-end cut it down to a slice, taking range names, percentages, lengths, or a name and an offset together. Three identical layers run on one timeline with three different ranges, each range printed beside the layer it controls.
## HTML
```html
<section class="sa-12" aria-labelledby="sa-12-h">
  <fieldset class="sa-12__theme">
    <legend class="sa-12__themelegend">Theme</legend>
    <input class="sa-12__themeinput" type="radio" name="sa-12-theme" id="sa-12-theme-auto" checked>
    <label class="sa-12__themeopt" for="sa-12-theme-auto">Auto</label>
    <input class="sa-12__themeinput" type="radio" name="sa-12-theme" id="sa-12-theme-light">
    <label class="sa-12__themeopt" for="sa-12-theme-light">Light</label>
    <input class="sa-12__themeinput" type="radio" name="sa-12-theme" id="sa-12-theme-dark">
    <label class="sa-12__themeopt" for="sa-12-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-12__stage">
    <header class="sa-12__head">
      <p class="sa-12__eyebrow">animation-range</p>
      <h2 class="sa-12__h" id="sa-12-h">Three slices of one timeline</h2>
      <p class="sa-12__sub">One scroller, one name, three consumers. The only difference between the layers is the range printed next to each one.</p>
    </header>

    <div class="sa-12__grid">
      <ol class="sa-12__legend">
        <li class="sa-12__lrow"><span class="sa-12__chip sa-12__chip--far">Far</span><code class="sa-12__code">animation-range: 0% 100%</code><span class="sa-12__lnote">whole timeline, slowest travel</span></li>
        <li class="sa-12__lrow"><span class="sa-12__chip sa-12__chip--mid">Mid</span><code class="sa-12__code">animation-range: 10% 75%</code><span class="sa-12__lnote">starts late, finishes early, then holds</span></li>
        <li class="sa-12__lrow"><span class="sa-12__chip sa-12__chip--near">Near</span><code class="sa-12__code">animation-range: 25% 60%</code><span class="sa-12__lnote">a 35% slice, so it moves fastest</span></li>
      </ol>

      <div class="sa-12__scroller" tabindex="0" role="region" aria-label="Layered range comparison, scrollable">
        <div class="sa-12__viewport">
          <span class="sa-12__layer sa-12__layer--far" aria-hidden="true"><span class="sa-12__ltag">Far</span></span>
          <span class="sa-12__layer sa-12__layer--mid" aria-hidden="true"><span class="sa-12__ltag">Mid</span></span>
          <span class="sa-12__layer sa-12__layer--near" aria-hidden="true"><span class="sa-12__ltag">Near</span></span>
        </div>
        <div class="sa-12__copy">
          <h3 class="sa-12__ch">Ranges, not durations</h3>
          <p class="sa-12__p">Scroll on. Each layer is bound to the same timeline and moves only inside its own range, so they separate and re-converge at predictable offsets.</p>
          <p class="sa-12__p">The Near layer has the shortest range, which means the least scroll distance for the same keyframes — so it travels fastest.</p>
          <p class="sa-12__p">Give the Mid layer <span class="sa-12__mono">10% 75%</span> and it idles for the first tenth of the scroll, then settles a quarter before the end.</p>
          <p class="sa-12__p">Set two endpoints that resolve to the same offset and the layer stops interpolating entirely — a zero-length range, and the most common range bug.</p>
          <p class="sa-12__p">Nothing here reads <span class="sa-12__mono">animation-duration</span>. On a scroll timeline it is ignored outright.</p>
          <p class="sa-12__p">A range endpoint can also be a length. <span class="sa-12__mono">animation-range: 120px 640px</span> ties the slice to scroll distance rather than to a proportion of the scroller.</p>
          <p class="sa-12__p">Mixing units across the two endpoints is legal, so <span class="sa-12__mono">0% 400px</span> resolves as you would expect: start at the top, finish four hundred pixels down.</p>
          <p class="sa-12__p">Print the values while you tune them. A range is one of the few CSS declarations whose effect is invisible in devtools until you scroll.</p>
          <p class="sa-12__p">When two layers should meet at a specific point, give them a shared endpoint rather than matching durations. Endpoints are exact; rates are not.</p>
          <p class="sa-12__p">Named ranges belong to view timelines. On this scroll timeline only percentages and lengths resolve, which demo 06 covers from the other side.</p>
          <p class="sa-12__p">A range with a start beyond 100% is legal and silent: the layer freezes at its first keyframe for the entire scroll and never reports a problem.</p>
          <p class="sa-12__p">Ranges compose with fill mode. Outside its slice a layer holds whichever end frame fill mode allows, which is what keeps the composition intact at the top and bottom.</p>
          <p class="sa-12__p">For a hand-off between two layers, end one range exactly where the next begins. Overlapping slices read as hesitation.</p>
          <p class="sa-12__p">The Near layer's 35% slice is the shortest here, so it covers the most distance per pixel scrolled — rate is a consequence of range, never of duration.</p>
          <p class="sa-12__p">Widen every range by the same amount and the whole composition slows without any of the layers changing their relationship.</p>
          <p class="sa-12__p">Keep the values in the interface while you tune. Once the mapping is learned they can go, and the panel on the left is the shippable half.</p>
        </div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.sa-12 {
  --page: #070b18;
  --surface: #0e1428;
  --ink: #e9ecfb;
  --muted: #8e97c4;
  --rule: #1e2647;
  --accent: #8b7bff;
  --far: #2b3564;
  --mid: #4a54a8;
  --near: #8b7bff;
  --page: oklch(15% 0.035 268);
  --surface: oklch(20% 0.04 268);
  --ink: oklch(94% 0.015 280);
  --muted: oklch(68% 0.05 278);
  --rule: oklch(28% 0.045 270);
  --accent: oklch(68% 0.17 288);
  --font-display: ui-sans-serif, system-ui, "Helvetica Neue", sans-serif;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  position: relative;
  padding: 3.5rem 1rem 3rem;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

.sa-12 *,
.sa-12 *::before,
.sa-12 *::after {
  box-sizing: border-box;
}

.sa-12__stage {
  max-inline-size: 61rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.sa-12__head {
  display: flex;
  flex-direction: column;
  gap: 0.375rem;
}

.sa-12__eyebrow {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
}

.sa-12__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.375rem, 4vw, 2.125rem);
  font-weight: 650;
  letter-spacing: -0.02em;
  line-height: 1.1;
}

.sa-12__sub {
  margin: 0;
  max-inline-size: 44rem;
  font-size: 0.875rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-12__grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1.5fr);
  gap: 0.75rem;
  align-items: start;
}

.sa-12__legend {
  margin: 0;
  padding: 0.5rem;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.375rem;
  background: var(--surface);
  border-radius: 0.5rem;
}

.sa-12__lrow {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem;
  padding: 0.625rem 0.5rem;
  background: color-mix(in srgb, var(--ink) 4%, transparent);
  border-radius: 0.375rem;
  min-inline-size: 0;
}

.sa-12__chip {
  flex: 0 0 auto;
  padding: 0.125rem 0.4375rem;
  border-radius: 0.25rem;
  font-size: 0.625rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--page);
}

.sa-12__chip--far {
  background: var(--far);
  color: var(--ink);
}

.sa-12__chip--mid {
  background: var(--mid);
  color: var(--ink);
}

.sa-12__chip--near {
  background: var(--near);
}

.sa-12__code {
  flex: 1 1 100%;
  min-inline-size: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.6875rem;
  color: var(--ink);
  word-break: break-word;
}

.sa-12__lnote {
  flex: 1 1 100%;
  font-size: 0.6875rem;
  line-height: 1.4;
  color: var(--muted);
}

.sa-12__mono {
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.85em;
  color: var(--accent);
}

.sa-12__scroller {
  block-size: 62vh;
  min-block-size: 20rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  background: var(--surface);
  border-radius: 0.5rem;
  scroll-timeline: --sa-12-track block;
}

.sa-12__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sa-12__viewport {
  position: sticky;
  inset-block-start: 0;
  block-size: 11rem;
  overflow: hidden;
  background: linear-gradient(180deg, color-mix(in srgb, var(--accent) 12%, var(--surface)), var(--surface));
}

.sa-12__layer {
  position: absolute;
  inset-inline: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  block-size: 3.25rem;
  will-change: transform;
}

.sa-12__ltag {
  padding: 0.1875rem 0.5rem;
  border-radius: 0.25rem;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.625rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.sa-12__layer--far {
  inset-block-start: 1rem;
  background: var(--far);
  transform: translate3d(0, -3.5rem, 0);
}

.sa-12__layer--far .sa-12__ltag {
  color: var(--ink);
}

.sa-12__layer--mid {
  inset-block-start: 4rem;
  background: var(--mid);
  transform: translate3d(0, -5.5rem, 0);
}

.sa-12__layer--mid .sa-12__ltag {
  color: var(--ink);
}

.sa-12__layer--near {
  inset-block-start: 7rem;
  background: var(--near);
  transform: translate3d(0, -8rem, 0);
}

.sa-12__layer--near .sa-12__ltag {
  color: var(--page);
  font-weight: 700;
}

.sa-12__copy {
  min-block-size: calc(100% + 6rem);
  padding: 1rem 1rem 3rem;
  display: flex;
  flex-direction: column;
  gap: 0.625rem;
}

.sa-12__ch {
  margin: 0;
  font-family: var(--font-display);
  font-size: 0.9375rem;
  font-weight: 650;
}

.sa-12__p {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

@keyframes sa-12-far {
  from {
    transform: translate3d(0, 0, 0);
  }

  to {
    transform: translate3d(0, -3.5rem, 0);
  }
}

@keyframes sa-12-mid {
  from {
    transform: translate3d(0, 0, 0);
  }

  to {
    transform: translate3d(0, -5.5rem, 0);
  }
}

@keyframes sa-12-near {
  from {
    transform: translate3d(0, 0, 0);
  }

  to {
    transform: translate3d(0, -8rem, 0);
  }
}

@supports (animation-timeline: scroll()) {
  .sa-12__layer--far {
    animation: sa-12-far linear both;
    animation-timeline: --sa-12-track;
    animation-range: 0% 100%;
  }

  .sa-12__layer--mid {
    animation: sa-12-mid linear both;
    animation-timeline: --sa-12-track;
    animation-range: 10% 75%;
  }

  .sa-12__layer--near {
    animation: sa-12-near linear both;
    animation-timeline: --sa-12-track;
    animation-range: 25% 60%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sa-12__layer--far {
    animation: none;
    transform: translate3d(0, -3.5rem, 0);
  }

  .sa-12__layer--mid {
    animation: none;
    transform: translate3d(0, -5.5rem, 0);
  }

  .sa-12__layer--near {
    animation: none;
    transform: translate3d(0, -8rem, 0);
  }
}

.sa-12__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 9;
  display: inline-flex;
  gap: 0.125rem;
  margin: 0;
  padding: 0.1875rem;
  border: 1px solid var(--rule);
  border-radius: 0.375rem;
  background: var(--surface);
}

.sa-12__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-12__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-12__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.625rem;
  border-radius: 0.25rem;
  font-family: ui-monospace, Menlo, monospace;
  font-size: 0.625rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-12__themeinput:checked + .sa-12__themeopt {
  color: var(--page);
  background: var(--accent);
}

.sa-12__themeinput:focus-visible + .sa-12__themeopt {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 48rem) {
  .sa-12__grid {
    grid-template-columns: minmax(0, 1fr);
  }

  .sa-12 {
    padding-block-start: 4.25rem;
  }
}

@media (forced-colors: active) {
  .sa-12__layer {
    border: 1px solid CanvasText;
  }
}

@media (prefers-color-scheme: light) {
  .sa-12:not(:has(#sa-12-theme-dark:checked)) {
    --page: #eef0f9;
    --surface: #ffffff;
    --ink: #14183a;
    --muted: #5d6490;
    --rule: #d8dcf0;
    --accent: #5b46e0;
    --far: #c3c8ea;
    --mid: #8f97d8;
    --near: #5b46e0;
  }

  .sa-12:not(:has(#sa-12-theme-dark:checked)) .sa-12__layer--far .sa-12__ltag,
    .sa-12:not(:has(#sa-12-theme-dark:checked)) .sa-12__layer--mid .sa-12__ltag {
    color: #14183a;
  }

  .sa-12:not(:has(#sa-12-theme-dark:checked)) .sa-12__layer--near .sa-12__ltag {
    color: #ffffff;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-12:has(#sa-12-theme-light:checked) {
    --page: #eef0f9;
    --surface: #ffffff;
    --ink: #14183a;
    --muted: #5d6490;
    --rule: #d8dcf0;
    --accent: #5b46e0;
    --far: #c3c8ea;
    --mid: #8f97d8;
    --near: #5b46e0;
  }
}

[data-theme="light"] .sa-12:not(:has(#sa-12-theme-dark:checked)) {
  --page: #eef0f9;
  --surface: #ffffff;
  --ink: #14183a;
  --muted: #5d6490;
  --rule: #d8dcf0;
  --accent: #5b46e0;
  --far: #c3c8ea;
  --mid: #8f97d8;
  --near: #5b46e0;
}

.sa-12:has(#sa-12-theme-light:checked) {
  --page: #eef0f9;
  --surface: #ffffff;
  --ink: #14183a;
  --muted: #5d6490;
  --rule: #d8dcf0;
  --accent: #5b46e0;
  --far: #c3c8ea;
  --mid: #8f97d8;
  --near: #5b46e0;
}

.sa-12:has(#sa-12-theme-light:checked) .sa-12__layer--near .sa-12__ltag {
  color: #ffffff;
}

.sa-12:has(#sa-12-theme-dark:checked) {
  --page: #070b18;
  --surface: #0e1428;
  --ink: #e9ecfb;
  --muted: #8e97c4;
  --rule: #1e2647;
  --accent: #8b7bff;
  --far: #2b3564;
  --mid: #4a54a8;
  --near: #8b7bff;
}
```
