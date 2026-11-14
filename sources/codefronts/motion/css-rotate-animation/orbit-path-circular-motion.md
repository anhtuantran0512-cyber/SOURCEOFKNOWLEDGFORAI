---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/orbit-path-circular-motion/"
title: "Orbit Path Circular Motion"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "A satellite circling a centre, and the choice that defines the technique: rotating a long invisible arm is the compatible way to do it, but the arm drags the…"
has_js: "false"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Orbit Path Circular Motion
Source: https://codefronts.com/motion/css-rotate-animation/orbit-path-circular-motion/

A satellite circling a centre, and the choice that defines the technique: rotating a long invisible arm is the compatible way to do it, but the arm drags the satellite's own orientation around with it. Both versions run side by side — the naive one and the counter-rotated fix — with a note on where offset-path: circle() fits.
## HTML
```html
<section class="rot-15" aria-labelledby="rot-15-h">
  <fieldset class="rot-15__theme">
    <legend class="rot-15__themelegend">Theme</legend>
    <input class="rot-15__themeinput" type="radio" name="rot-15-theme" id="rot-15-theme-auto" checked>
    <label class="rot-15__themeopt" for="rot-15-theme-auto">Auto</label>
    <input class="rot-15__themeinput" type="radio" name="rot-15-theme" id="rot-15-theme-light">
    <label class="rot-15__themeopt" for="rot-15-theme-light">Light</label>
    <input class="rot-15__themeinput" type="radio" name="rot-15-theme" id="rot-15-theme-dark">
    <label class="rot-15__themeopt" for="rot-15-theme-dark">Dark</label>
  </fieldset>
  <label class="rot-15__pause">
    <input class="rot-15__pausebox" type="checkbox" id="rot-15-pause">
    <span class="rot-15__pausedot" aria-hidden="true">
      <svg viewBox="0 0 16 16" width="12" height="12" focusable="false"><rect x="4" y="3" width="3" height="10" rx="1" fill="currentColor"></rect><rect x="9" y="3" width="3" height="10" rx="1" fill="currentColor"></rect></svg>
    </span>
    <span class="rot-15__pausetext">Pause</span>
  </label>

  <div class="rot-15__stage">
    <header class="rot-15__head">
      <p class="rot-15__eyebrow">Orbit Systems · Station keeping</p>
      <h2 class="rot-15__h" id="rot-15-h">Travelling a circle without tumbling</h2>
      <p class="rot-15__sub">Both satellites orbit on a rotating arm. Only the right one counter-rotates, which is why its label stays the right way up.</p>
    </header>

    <div class="rot-15__pair">
      <figure class="rot-15__system">
        <div class="rot-15__space" aria-hidden="true">
          <span class="rot-15__ring rot-15__ring--1"></span>
          <span class="rot-15__core"></span>
          <span class="rot-15__arm rot-15__arm--1">
            <span class="rot-15__sat">
              <span class="rot-15__sattag">NAIVE</span>
            </span>
          </span>
        </div>
        <figcaption class="rot-15__cap">Arm only — the satellite inherits the arm's rotation and tumbles as it travels.</figcaption>
      </figure>

      <figure class="rot-15__system">
        <div class="rot-15__space" aria-hidden="true">
          <span class="rot-15__ring rot-15__ring--2"></span>
          <span class="rot-15__core"></span>
          <span class="rot-15__arm rot-15__arm--2">
            <span class="rot-15__sat">
              <span class="rot-15__counter">
                <span class="rot-15__sattag">FIXED</span>
              </span>
            </span>
          </span>
        </div>
        <figcaption class="rot-15__cap">Arm plus an inner element running the same keyframe in reverse. The rotations cancel; only the position moves.</figcaption>
      </figure>
    </div>

    <article class="rot-15__note">
      <h3 class="rot-15__noteh">The declarative alternative</h3>
      <pre class="rot-15__pre">offset-path: circle(6rem at 50% 50%);
offset-rotate: 0deg;
animation: rot-15-travel 9s linear infinite;</pre>
      <p class="rot-15__notep"><span class="rot-15__code">offset-distance</span> animates progress along the path and <span class="rot-15__code">offset-rotate: 0deg</span> keeps the element upright with no counter-rotation at all. The arm technique ships here because it makes the inheritance lesson visible — and that lesson applies to every nested rotation you will write.</p>
    </article>
  </div>
</section>
```
## CSS
```css
.rot-15 {
  --page: #05070d;
  --surface: #0c111b;
  --ink: #e4ecf7;
  --muted: #8896ac;
  --rule: #1b2433;
  --accent: #6fe3ff;
  --r1: clamp(3.5rem, 13vw, 5.25rem);
  --r2: clamp(3.5rem, 13vw, 5.25rem);
  --p1: 9s;
  --p2: 9s;
  --font-display: Verdana, Geneva, "DejaVu Sans", system-ui, sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: radial-gradient(130% 100% at 50% 0%, #101a30 0%, var(--page) 60%, #020306 100%);
  color: var(--ink);
  font-family: var(--font-display);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(0 0 0)) {
  .rot-15 {
    --accent: oklch(0.86 0.13 210);
  }
}

.rot-15 *,
.rot-15 *::before,
.rot-15 *::after {
  box-sizing: border-box;
}

.rot-15__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.75rem, 4.5vw, 3rem);
  padding: clamp(1.5rem, 4vw, 3.5rem);
  padding-block-start: 5.5rem;
}

.rot-15__head {
  max-inline-size: 36rem;
  min-inline-size: 0;
  text-align: center;
}

.rot-15__eyebrow {
  margin: 0 0 0.6rem;
  font-size: 0.625rem;
  font-weight: 700;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--accent);
}

.rot-15__h {
  margin: 0 0 0.6rem;
  font-size: clamp(1.25rem, 4.2vw, 2rem);
  font-weight: 700;
  letter-spacing: -0.01em;
  line-height: 1.18;
}

.rot-15__sub {
  margin: 0;
  font-size: 0.875rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-15__code {
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.85em;
  color: var(--accent);
}

.rot-15__pair {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
  gap: clamp(1.5rem, 5vw, 3rem);
  inline-size: min(100%, 44rem);
}

.rot-15__system {
  margin: 0;
  min-inline-size: 0;
  display: grid;
  justify-items: center;
  gap: 0.9rem;
}

.rot-15__space {
  position: relative;
  inline-size: calc(var(--r1) * 2.9);
  aspect-ratio: 1;
  display: grid;
  place-items: center;
}

.rot-15__ring {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  border: 1px dashed var(--rule);
  border-radius: 50%;
}

.rot-15__ring--1 {
  inline-size: calc(var(--r1) * 2);
  block-size: calc(var(--r1) * 2);
  margin: calc(var(--r1) * -1) 0 0 calc(var(--r1) * -1);
}

.rot-15__ring--2 {
  inline-size: calc(var(--r2) * 2);
  block-size: calc(var(--r2) * 2);
  margin: calc(var(--r2) * -1) 0 0 calc(var(--r2) * -1);
}

.rot-15__core {
  position: absolute;
  inline-size: 2.25rem;
  aspect-ratio: 1;
  border-radius: 50%;
  background: radial-gradient(circle at 36% 32%, #ffffff, var(--accent) 55%, #14607a 100%);
  box-shadow: 0 0 24px -4px color-mix(in srgb, var(--accent) 60%, transparent);
}

.rot-15__arm {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  block-size: 0;
  transform-origin: 0 0;
  animation: rot-15-orbit var(--p1) linear infinite;
}

.rot-15__arm--1 {
  inline-size: var(--r1);
  animation-duration: var(--p1);
}

.rot-15__arm--2 {
  inline-size: var(--r2);
  animation-duration: var(--p2);
}

.rot-15__sat {
  position: absolute;
  inset-block-start: 0;
  inset-inline-end: 0;
  display: grid;
  place-items: center;
  inline-size: 3.1rem;
  block-size: 1.5rem;
  translate: 50% -50%;
  border: 1px solid var(--accent);
  border-radius: 0.2rem;
  background: var(--surface);
}

.rot-15__counter {
  display: grid;
  place-items: center;
  animation: rot-15-orbit var(--p2) linear infinite reverse;
}

.rot-15__sattag {
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.5625rem;
  letter-spacing: 0.12em;
  color: var(--accent);
}

@keyframes rot-15-orbit {
  to {
    transform: rotate(360deg);
  }
}

.rot-15__cap {
  margin: 0;
  font-size: 0.75rem;
  line-height: 1.55;
  text-align: center;
  color: var(--muted);
  min-inline-size: 0;
}

.rot-15__note {
  inline-size: min(100%, 40rem);
  display: grid;
  gap: 0.75rem;
  padding: clamp(0.875rem, 3vw, 1.25rem);
  border: 1px solid var(--rule);
  border-radius: 0.75rem;
  background: var(--surface);
}

.rot-15__noteh {
  margin: 0;
  font-size: 0.8125rem;
  font-weight: 700;
  letter-spacing: 0.02em;
}

.rot-15__pre {
  margin: 0;
  padding: 0.75rem;
  border-radius: 0.5rem;
  background: rgba(255, 255, 255, 0.04);
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.75rem;
  line-height: 1.6;
  color: var(--ink);
  overflow-x: auto;
}

.rot-15__notep {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.65;
  color: var(--muted);
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .rot-15__arm {
    animation: none;
  }

  .rot-15__arm--1 {
    transform: rotate(-52deg);
  }

  .rot-15__arm--2 {
    transform: rotate(38deg);
  }

  .rot-15__counter {
    animation: none;
    transform: rotate(-38deg);
  }
}

.rot-15:has(.rot-15__pausebox:checked) .rot-15__arm,
.rot-15:has(.rot-15__pausebox:checked) .rot-15__counter {
  animation-play-state: paused;
}

.rot-15__theme {
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

.rot-15__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-15__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-15__themeopt {
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

.rot-15__themeopt:hover {
  opacity: 0.85;
}

.rot-15__themeinput:checked + .rot-15__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-15__themeinput:focus-visible + .rot-15__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.rot-15__pause {
  position: absolute;
  inset-block-start: 0.875rem;
  inset-inline-start: 0.875rem;
  z-index: 9;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  margin: 0;
  padding: 0.1875rem 0.75rem 0.1875rem 0.1875rem;
  border: 1px solid color-mix(in srgb, currentColor 18%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 8%, transparent);
  font-family: system-ui, sans-serif;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  user-select: none;
}

.rot-15__pausebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-15__pausedot {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  inline-size: 2.25rem;
  block-size: 2.25rem;
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 12%, transparent);
}

.rot-15__pause:has(.rot-15__pausebox:focus-visible) {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.rot-15:has(.rot-15__pausebox:checked) .rot-15__pausedot {
  background: var(--accent);
  color: #03151c;
}

@media (forced-colors: active) {
  .rot-15__theme,
    .rot-15__pause {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-15__themeinput:checked + .rot-15__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: light) {
  .rot-15:not(:has(#rot-15-theme-dark:checked)) {
    --page: #eef2f8;
    --surface: #ffffff;
    --ink: #0e1626;
    --muted: #5b6a80;
    --rule: #ccd6e4;
    --accent: #0f7b96;
    background: radial-gradient(130% 100% at 50% 0%, #ffffff 0%, #eef2f8 60%, #e2e8f2 100%);
  }

  .rot-15:not(:has(#rot-15-theme-dark:checked)) .rot-15__pre {
    background: rgba(15, 30, 50, 0.05);
  }
}

@media (prefers-color-scheme: dark) {
  .rot-15:has(#rot-15-theme-light:checked) {
    --page: #eef2f8;
    --surface: #ffffff;
    --ink: #0e1626;
    --muted: #5b6a80;
    --rule: #ccd6e4;
    --accent: #0f7b96;
    background: radial-gradient(130% 100% at 50% 0%, #ffffff 0%, #eef2f8 60%, #e2e8f2 100%);
  }

  .rot-15:has(#rot-15-theme-light:checked) .rot-15__pre {
    background: rgba(15, 30, 50, 0.05);
  }
}

[data-theme="light"] .rot-15:not(:has(#rot-15-theme-dark:checked)) {
  --page: #eef2f8;
  --surface: #ffffff;
  --ink: #0e1626;
  --muted: #5b6a80;
  --rule: #ccd6e4;
  --accent: #0f7b96;
  background: radial-gradient(130% 100% at 50% 0%, #ffffff 0%, #eef2f8 60%, #e2e8f2 100%);
}

.rot-15:has(#rot-15-theme-light:checked) {
  --page: #eef2f8;
  --surface: #ffffff;
  --ink: #0e1626;
  --muted: #5b6a80;
  --rule: #ccd6e4;
  --accent: #0f7b96;
  background: radial-gradient(130% 100% at 50% 0%, #ffffff 0%, #eef2f8 60%, #e2e8f2 100%);
}

.rot-15:has(#rot-15-theme-light:checked) .rot-15__pre {
  background: rgba(15, 30, 50, 0.05);
}

.rot-15:has(#rot-15-theme-light:checked) .rot-15__pausedot {
  color: #ffffff;
}

.rot-15:has(#rot-15-theme-dark:checked) {
  --page: #05070d;
  --surface: #0c111b;
  --ink: #e4ecf7;
  --muted: #8896ac;
  --rule: #1b2433;
  --accent: #6fe3ff;
  background: radial-gradient(130% 100% at 50% 0%, #101a30 0%, #05070d 60%, #020306 100%);
}

.rot-15:has(#rot-15-theme-dark:checked) .rot-15__pre {
  background: rgba(255, 255, 255, 0.04);
}
/* Site-theme bridge: the per-demo page stamps [data-theme] on the iframe
   root. Without these rules a dark-by-default demo followed the OS instead
   of the site when the visitor was on OS-light + site-dark. Guarded by the
   light toggle so the in-demo switch still wins. */

[data-theme="dark"] .rot-15:not(:has(#rot-15-theme-light:checked)) {
  --page: #05070d;
  --surface: #0c111b;
  --ink: #e4ecf7;
  --muted: #8896ac;
  --rule: #1b2433;
  --accent: #6fe3ff;
  background: radial-gradient(130% 100% at 50% 0%, #101a30 0%, #05070d 60%, #020306 100%);
}

[data-theme="dark"] .rot-15:not(:has(#rot-15-theme-light:checked)) .rot-15__pre {
  background: rgba(255, 255, 255, 0.04);
}
```
