---
source: "codefronts"
url: "https://codefronts.com/motion/css-scroll-animations/debug-scroll-timeline-not-running/"
title: "Debugging a Timeline That Does Not Run"
section: "motion"
category: "css-scroll-animations"
category_name: "CSS Scroll Animations"
description: "Scroll timelines fail silently: no error, no warning, nothing moves."
has_js: "false"
---

Here's a working CSS Scroll Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Debugging a Timeline That Does Not Run
Source: https://codefronts.com/motion/css-scroll-animations/debug-scroll-timeline-not-running/

Scroll timelines fail silently: no error, no warning, nothing moves. This is the closing reference — five toggles, each introducing one of the five real causes, with the symptom named beside it. Flip one at a time and learn to recognise each failure by sight rather than by guessing.
## HTML
```html
<section class="sa-08" aria-labelledby="sa-08-h">
  <fieldset class="sa-08__theme">
    <legend class="sa-08__themelegend">Theme</legend>
    <input class="sa-08__themeinput" type="radio" name="sa-08-theme" id="sa-08-theme-auto" checked>
    <label class="sa-08__themeopt" for="sa-08-theme-auto">Auto</label>
    <input class="sa-08__themeinput" type="radio" name="sa-08-theme" id="sa-08-theme-light">
    <label class="sa-08__themeopt" for="sa-08-theme-light">Light</label>
    <input class="sa-08__themeinput" type="radio" name="sa-08-theme" id="sa-08-theme-dark">
    <label class="sa-08__themeopt" for="sa-08-theme-dark">Dark</label>
  </fieldset>

  <div class="sa-08__stage">
    <header class="sa-08__head">
      <p class="sa-08__eyebrow">Closing reference · five causes</p>
      <h2 class="sa-08__h" id="sa-08-h">It does not run and nothing says why</h2>
      <p class="sa-08__sub">Break the working example on purpose, one cause at a time, and match each symptom to its fix.</p>
    </header>

    <div class="sa-08__grid">
      <fieldset class="sa-08__causes">
        <legend class="sa-08__clegend">Introduce a fault</legend>
        <div class="sa-08__crow">
          <input class="sa-08__cbox" type="checkbox" id="sa-08-c1">
          <label class="sa-08__clabel" for="sa-08-c1"><span class="sa-08__cnum">01</span><span class="sa-08__ctext">Scroller is not scrollable</span></label>
          <p class="sa-08__csym">Symptom · frozen at the first frame. Fix · <span class="sa-08__mono">overflow-y: auto</span> plus content taller than the box.</p>
        </div>
        <div class="sa-08__crow">
          <input class="sa-08__cbox" type="checkbox" id="sa-08-c2">
          <label class="sa-08__clabel" for="sa-08-c2"><span class="sa-08__cnum">02</span><span class="sa-08__ctext">Subject outside the timeline owner</span></label>
          <p class="sa-08__csym">Symptom · no motion at all, name unresolved. Fix · move it inside, or use <span class="sa-08__mono">timeline-scope</span>.</p>
        </div>
        <div class="sa-08__crow">
          <input class="sa-08__cbox" type="checkbox" id="sa-08-c3">
          <label class="sa-08__clabel" for="sa-08-c3"><span class="sa-08__cnum">03</span><span class="sa-08__ctext">Range resolves to zero length</span></label>
          <p class="sa-08__csym">Symptom · snaps between end frames, never interpolates. Fix · check <span class="sa-08__mono">animation-range</span> order.</p>
        </div>
        <div class="sa-08__crow">
          <input class="sa-08__cbox" type="checkbox" id="sa-08-c4">
          <label class="sa-08__clabel" for="sa-08-c4"><span class="sa-08__cnum">04</span><span class="sa-08__ctext">Property is not animatable</span></label>
          <p class="sa-08__csym">Symptom · a jump, not a scrub. Fix · animate <span class="sa-08__mono">transform</span> or <span class="sa-08__mono">opacity</span>, or register the property.</p>
        </div>
        <div class="sa-08__crow">
          <input class="sa-08__cbox" type="checkbox" id="sa-08-c5">
          <label class="sa-08__clabel" for="sa-08-c5"><span class="sa-08__cnum">05</span><span class="sa-08__ctext">overflow: hidden ancestor</span></label>
          <p class="sa-08__csym">Symptom · scroll container gone, sticky dead too. Fix · audit computed overflow up the chain.</p>
        </div>
      </fieldset>

      <div class="sa-08__demo">
        <p class="sa-08__dtag">Live subject</p>
        <div class="sa-08__wrap">
          <div class="sa-08__scroller" tabindex="0" role="region" aria-label="Debugging subject, scrollable">
            <div class="sa-08__sticky"><span class="sa-08__marker"></span></div>
            <div class="sa-08__body">
              <p class="sa-08__p">The marker above is bound to this panel's scroll. With no fault selected it tracks your position exactly.</p>
              <p class="sa-08__p">Turn on cause 01 and the panel stops scrolling: the marker holds its first frame and nothing in the console mentions it.</p>
              <p class="sa-08__p">Cause 03 collapses the range, so the marker jumps between its two end frames with nothing in between.</p>
              <p class="sa-08__p">Cause 05 clips the ancestor, and the panel stops being a scroll container at all.</p>
              <p class="sa-08__p">Each of these is a one-line mistake in real code, and none of them reports itself.</p>
              <p class="sa-08__p">Cause 02 is the one that survives code review, because the selector and the name both look right — only the tree is wrong.</p>
              <p class="sa-08__p">Cause 04 is a keyframe fault wearing a timeline costume: the binding is fine, the property simply cannot interpolate.</p>
              <p class="sa-08__p">Work the list in order. Scroller, then owner, then range, then property, then ancestors — cheapest check first.</p>
              <p class="sa-08__p">Before anything else, confirm the engine supports the feature at all. In Safari every one of these symptoms is expected.</p>
              <p class="sa-08__p">When it does run, the marker sweeps the full width of its track between the top and the bottom of this panel.</p>
              <p class="sa-08__p">Keep a working example beside the broken one. Half of debugging a silent feature is having something correct to compare against.</p>
              <p class="sa-08__p">Check the scroller with two numbers: computed overflow, and scrollHeight against clientHeight. If the second pair matches, there is no range to read.</p>
              <p class="sa-08__p">Check the owner by walking up from the subject. If you never pass the element that declares the name, the name is not visible from here.</p>
              <p class="sa-08__p">Check the range by widening it to 0% 100% temporarily. If motion appears, the range was the fault and the binding was always fine.</p>
              <p class="sa-08__p">Check the property by swapping the keyframes for a plain opacity fade. If that scrubs, the original property was the problem.</p>
              <p class="sa-08__p">Check the ancestors last, because it is the slowest check — but it is the one that catches faults introduced by somebody else's component.</p>
              <p class="sa-08__p">Five causes, five checks, in that order. Almost every report resolves inside the first three.</p>
            </div>
          </div>
        </div>
        <p class="sa-08__hint">One fault at a time. The failures look alike, which is exactly why they are hard.</p>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.sa-08 {
  --page: #17150f;
  --surface: #201d15;
  --ink: #f5eeda;
  --muted: #a89b7c;
  --rule: #332e21;
  --accent: #e8b33c;
  --page: oklch(19% 0.015 85);
  --surface: oklch(24% 0.018 85);
  --ink: oklch(94% 0.03 90);
  --muted: oklch(70% 0.045 88);
  --rule: oklch(31% 0.022 85);
  --accent: oklch(80% 0.15 85);
  --font-display: ui-monospace, "JetBrains Mono", "SFMono-Regular", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  position: relative;
  padding: 3.75rem 1rem 3rem;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
}

.sa-08 *,
.sa-08 *::before,
.sa-08 *::after {
  box-sizing: border-box;
}

.sa-08__stage {
  max-inline-size: 62rem;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.sa-08__head {
  display: flex;
  flex-direction: column;
  gap: 0.375rem;
  padding-block-end: 0.75rem;
  border-block-end: 1px solid var(--rule);
}

.sa-08__eyebrow {
  margin: 0;
  font-family: var(--font-display);
  font-size: 0.625rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent);
}

.sa-08__h {
  margin: 0;
  font-family: var(--font-display);
  font-size: clamp(1.25rem, 3.8vw, 1.875rem);
  font-weight: 500;
  letter-spacing: -0.03em;
  line-height: 1.14;
}

.sa-08__sub {
  margin: 0;
  max-inline-size: 44rem;
  font-size: 0.875rem;
  line-height: 1.55;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-08__mono {
  font-family: var(--font-display);
  font-size: 0.85em;
  color: var(--accent);
}

.sa-08__grid {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr);
  gap: 0.75rem;
  align-items: start;
}

.sa-08__causes {
  margin: 0;
  padding: 0;
  border: 0;
  display: flex;
  flex-direction: column;
}

.sa-08__clegend {
  padding: 0 0 0.5rem;
  font-family: var(--font-display);
  font-size: 0.625rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.sa-08__crow {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  padding-block: 0.5rem;
  border-block-start: 1px solid var(--rule);
}

.sa-08__cbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-08__clabel {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  min-block-size: 2.75rem;
  padding: 0 0.5rem;
  font-size: 0.8125rem;
  font-weight: 600;
  cursor: pointer;
  user-select: none;
}

.sa-08__cnum {
  flex: 0 0 auto;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  inline-size: 1.75rem;
  block-size: 1.75rem;
  border: 1px solid var(--rule);
  font-family: var(--font-display);
  font-size: 0.625rem;
  color: var(--muted);
}

.sa-08__ctext {
  min-inline-size: 0;
}

.sa-08__cbox:checked + .sa-08__clabel {
  color: var(--accent);
}

.sa-08__cbox:checked + .sa-08__clabel .sa-08__cnum {
  border-color: var(--accent);
  background: var(--accent);
  color: var(--page);
}

.sa-08__cbox:checked + .sa-08__clabel .sa-08__ctext::after {
  content: " · fault on";
  font-family: var(--font-display);
  font-size: 0.6875rem;
  letter-spacing: 0.06em;
}

.sa-08__cbox:focus-visible + .sa-08__clabel {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.sa-08__csym {
  margin: 0 0 0 3.125rem;
  font-size: 0.6875rem;
  line-height: 1.5;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-08__demo {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  min-inline-size: 0;
}

.sa-08__dtag {
  margin: 0;
  font-family: var(--font-display);
  font-size: 0.625rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--muted);
}

.sa-08__wrap {
  border: 1px solid var(--rule);
  background: var(--surface);
}

.sa-08__scroller {
  block-size: 52vh;
  min-block-size: 17rem;
  overflow-y: auto;
  overscroll-behavior: contain;
  scroll-timeline: --sa-08-track block;
}

.sa-08__scroller:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: -2px;
}

.sa-08__sticky {
  position: sticky;
  inset-block-start: 0;
  z-index: 2;
  block-size: 0.75rem;
  margin: 0.5rem;
  background: color-mix(in srgb, var(--ink) 10%, transparent);
}

.sa-08__marker {
  display: block;
  inline-size: 25%;
  block-size: 100%;
  background: var(--accent);
  transform: translateX(300%);
}

.sa-08__body {
  min-block-size: calc(100% + 6rem);
  padding: 0.75rem 0.875rem 4rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.sa-08__p {
  margin: 0;
  font-size: 0.75rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.sa-08__hint {
  margin: 0;
  font-size: 0.6875rem;
  line-height: 1.5;
  color: var(--muted);
}

@keyframes sa-08-run {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(300%);
  }
}

@keyframes sa-08-jump {
  from {
    transform: translateX(0);
  }

  to {
    transform: translateX(300%);
  }
}

@supports (animation-timeline: scroll()) {
  .sa-08__marker {
    animation: sa-08-run linear both;
    animation-timeline: --sa-08-track;
  }

  .sa-08:has(#sa-08-c1:checked) .sa-08__scroller {
    overflow-y: hidden;
  }

  .sa-08:has(#sa-08-c2:checked) .sa-08__marker {
    animation-timeline: --sa-08-missing;
  }

  .sa-08:has(#sa-08-c3:checked) .sa-08__marker {
    animation-range: 50% 50%;
  }

  .sa-08:has(#sa-08-c4:checked) .sa-08__marker {
    animation-name: sa-08-jump;
    animation-timing-function: steps(1, end);
  }

  .sa-08:has(#sa-08-c5:checked) .sa-08__wrap {
    overflow: hidden;
  }

  .sa-08:has(#sa-08-c5:checked) .sa-08__scroller {
    overflow-y: hidden;
  }
}

@media (prefers-reduced-motion: reduce) {
  .sa-08__marker {
    animation: none;
    transform: translateX(300%);
  }
}

.sa-08__theme {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-end: 0.875rem;
  z-index: 9;
  display: inline-flex;
  gap: 0;
  margin: 0;
  padding: 0;
  border: 1px solid var(--rule);
  background: var(--surface);
}

.sa-08__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-08__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.sa-08__themeopt {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 2.25rem;
  min-inline-size: 2.75rem;
  padding: 0 0.625rem;
  font-family: var(--font-display);
  font-size: 0.625rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  user-select: none;
}

.sa-08__themeinput:checked + .sa-08__themeopt {
  color: var(--page);
  background: var(--accent);
}

.sa-08__themeinput:focus-visible + .sa-08__themeopt {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

@media (max-width: 48rem) {
  .sa-08__grid {
    grid-template-columns: minmax(0, 1fr);
  }

  .sa-08 {
    padding-block-start: 4.25rem;
  }
}

@media (forced-colors: active) {
  .sa-08__marker {
    background: Highlight;
  }
}

@media (prefers-color-scheme: light) {
  .sa-08:not(:has(#sa-08-theme-dark:checked)) {
    --page: #fbf7ec;
    --surface: #ffffff;
    --ink: #1d1a12;
    --muted: #6b6144;
    --rule: #e0d8c0;
    --accent: #a06f05;
  }

  .sa-08:not(:has(#sa-08-theme-dark:checked)) .sa-08__themeinput:checked + .sa-08__themeopt,
    .sa-08:not(:has(#sa-08-theme-dark:checked)) .sa-08__cbox:checked + .sa-08__clabel .sa-08__cnum {
    color: #ffffff;
  }
}

@media (prefers-color-scheme: dark) {
  .sa-08:has(#sa-08-theme-light:checked) {
    --page: #fbf7ec;
    --surface: #ffffff;
    --ink: #1d1a12;
    --muted: #6b6144;
    --rule: #e0d8c0;
    --accent: #a06f05;
  }

  .sa-08:has(#sa-08-theme-light:checked) .sa-08__themeinput:checked + .sa-08__themeopt,
    .sa-08:has(#sa-08-theme-light:checked) .sa-08__cbox:checked + .sa-08__clabel .sa-08__cnum {
    color: #ffffff;
  }
}

[data-theme="light"] .sa-08:not(:has(#sa-08-theme-dark:checked)) {
  --page: #fbf7ec;
  --surface: #ffffff;
  --ink: #1d1a12;
  --muted: #6b6144;
  --rule: #e0d8c0;
  --accent: #a06f05;
}

.sa-08:has(#sa-08-theme-light:checked) {
  --page: #fbf7ec;
  --surface: #ffffff;
  --ink: #1d1a12;
  --muted: #6b6144;
  --rule: #e0d8c0;
  --accent: #a06f05;
}

.sa-08:has(#sa-08-theme-light:checked) .sa-08__themeinput:checked + .sa-08__themeopt,
.sa-08:has(#sa-08-theme-light:checked) .sa-08__cbox:checked + .sa-08__clabel .sa-08__cnum {
  color: #ffffff;
}

.sa-08:has(#sa-08-theme-dark:checked) {
  --page: #17150f;
  --surface: #201d15;
  --ink: #f5eeda;
  --muted: #a89b7c;
  --rule: #332e21;
  --accent: #e8b33c;
}
```
