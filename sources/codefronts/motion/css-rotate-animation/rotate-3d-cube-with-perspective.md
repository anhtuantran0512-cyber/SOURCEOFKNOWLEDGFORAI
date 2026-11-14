---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/rotate-3d-cube-with-perspective/"
title: "Rotate 3D Cube with Perspective"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "Six faces, one rotating container, and the three declarations that make a real cube instead of a flat cross: perspective on the parent, transform-style:…"
has_js: "false"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rotate 3D Cube with Perspective
Source: https://codefronts.com/motion/css-rotate-animation/rotate-3d-cube-with-perspective/

Six faces, one rotating container, and the three declarations that make a real cube instead of a flat cross: perspective on the parent, transform-style: preserve-3d on the cube, and translateZ at half the edge length on every face. It rotates on two axes at once so the corners and edges stay legible at every frame.
## HTML
```html
<section class="rot-06" aria-labelledby="rot-06-h">
  <fieldset class="rot-06__theme">
    <legend class="rot-06__themelegend">Theme</legend>
    <input class="rot-06__themeinput" type="radio" name="rot-06-theme" id="rot-06-theme-auto" checked>
    <label class="rot-06__themeopt" for="rot-06-theme-auto">Auto</label>
    <input class="rot-06__themeinput" type="radio" name="rot-06-theme" id="rot-06-theme-light">
    <label class="rot-06__themeopt" for="rot-06-theme-light">Light</label>
    <input class="rot-06__themeinput" type="radio" name="rot-06-theme" id="rot-06-theme-dark">
    <label class="rot-06__themeopt" for="rot-06-theme-dark">Dark</label>
  </fieldset>
  <label class="rot-06__pause">
    <input class="rot-06__pausebox" type="checkbox" id="rot-06-pause">
    <span class="rot-06__pausedot" aria-hidden="true">
      <svg viewBox="0 0 16 16" width="12" height="12" focusable="false"><rect x="4" y="3" width="3" height="10" rx="1" fill="currentColor"></rect><rect x="9" y="3" width="3" height="10" rx="1" fill="currentColor"></rect></svg>
    </span>
    <span class="rot-06__pausetext">Pause</span>
  </label>

  <div class="rot-06__stage">
    <header class="rot-06__head">
      <p class="rot-06__eyebrow">Prism · Volumetric</p>
      <h2 class="rot-06__h" id="rot-06-h">Six faces, two axes, one 3D context</h2>
      <p class="rot-06__sub">Perspective lives on the stage. The cube only rotates. Each face is a rotation followed by a push outward of half an edge.</p>
    </header>

    <div class="rot-06__scene">
      <div class="rot-06__cube" aria-hidden="true">
        <span class="rot-06__face rot-06__face--front">front</span>
        <span class="rot-06__face rot-06__face--back">back</span>
        <span class="rot-06__face rot-06__face--right">right</span>
        <span class="rot-06__face rot-06__face--left">left</span>
        <span class="rot-06__face rot-06__face--top">top</span>
        <span class="rot-06__face rot-06__face--bottom">bottom</span>
      </div>
    </div>

    <div class="rot-06__facts">
      <article class="rot-06__fact">
        <h3 class="rot-06__facth">perspective: 900px</h3>
        <p class="rot-06__factp">On the <span class="rot-06__code">.rot-06__scene</span> parent. Put it on the cube and the faces flatten into a scaled projection with no vanishing point.</p>
      </article>
      <article class="rot-06__fact">
        <h3 class="rot-06__facth">preserve-3d</h3>
        <p class="rot-06__factp">On the cube. An ancestor with <span class="rot-06__code">overflow: hidden</span>, a <span class="rot-06__code">filter</span> or <span class="rot-06__code">opacity</span> below 1 flattens the whole context.</p>
      </article>
      <article class="rot-06__fact">
        <h3 class="rot-06__facth">rotate then translateZ</h3>
        <p class="rot-06__factp">Order is load-bearing. Rotating first turns the face's own axes, so the push moves it outward instead of sideways.</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.rot-06 {
  --page: #070c1c;
  --surface: rgba(255, 255, 255, 0.06);
  --ink: #e8edff;
  --muted: #97a3c8;
  --rule: rgba(150, 175, 255, 0.18);
  --accent: #4fd8d0;
  --edge: clamp(6rem, 22vw, 9.5rem);
  --half: calc(var(--edge) / 2);
  --persp: 900px;
  --spin: 16s;
  --font-display: "Trebuchet MS", "Lucida Grande", "Lucida Sans Unicode", system-ui, sans-serif;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: radial-gradient(120% 90% at 50% -10%, #12204a 0%, #070c1c 55%, #04060f 100%);
  color: var(--ink);
  font-family: var(--font-display);
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(0 0 0)) {
  .rot-06 {
    --accent: oklch(0.82 0.12 190);
  }
}

.rot-06 *,
.rot-06 *::before,
.rot-06 *::after {
  box-sizing: border-box;
}

.rot-06__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.5rem, 4vw, 2.75rem);
  padding: clamp(1.5rem, 4vw, 3.5rem);
  padding-block-start: 5.5rem;
}

.rot-06__head {
  max-inline-size: 38rem;
  min-inline-size: 0;
  text-align: center;
}

.rot-06__eyebrow {
  margin: 0 0 0.6rem;
  font-size: 0.6875rem;
  font-weight: 700;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--accent);
}

.rot-06__h {
  margin: 0 0 0.65rem;
  font-size: clamp(1.375rem, 4.6vw, 2.25rem);
  font-weight: 700;
  letter-spacing: -0.01em;
  line-height: 1.15;
}

.rot-06__sub {
  margin: 0;
  font-size: 0.9375rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-06__code {
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.85em;
  color: var(--accent);
}

.rot-06__scene {
  display: grid;
  place-items: center;
  inline-size: calc(var(--edge) * 2.1);
  block-size: calc(var(--edge) * 2.1);
  perspective: var(--persp);
  perspective-origin: 50% 40%;
}

.rot-06__cube {
  position: relative;
  inline-size: var(--edge);
  block-size: var(--edge);
  transform-style: preserve-3d;
  animation: rot-06-tumble var(--spin) linear infinite;
}

.rot-06__face {
  position: absolute;
  inset: 0;
  display: grid;
  place-items: center;
  border: 1px solid var(--rule);
  background: var(--surface);
  backface-visibility: visible;
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: color-mix(in srgb, var(--ink) 70%, transparent);
  box-shadow: inset 0 0 40px -14px color-mix(in srgb, var(--accent) 45%, transparent);
}

.rot-06__face--front {
  transform: translateZ(var(--half));
}

.rot-06__face--back {
  transform: rotateY(180deg) translateZ(var(--half));
}

.rot-06__face--right {
  transform: rotateY(90deg) translateZ(var(--half));
}

.rot-06__face--left {
  transform: rotateY(-90deg) translateZ(var(--half));
}

.rot-06__face--top {
  transform: rotateX(90deg) translateZ(var(--half));
}

.rot-06__face--bottom {
  transform: rotateX(-90deg) translateZ(var(--half));
}

@keyframes rot-06-tumble {
  from {
    transform: rotateX(-22deg) rotateY(0deg);
  }

  to {
    transform: rotateX(-22deg) rotateY(360deg);
  }
}

.rot-06__facts {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(13rem, 1fr));
  gap: 0.75rem;
  inline-size: min(100%, 48rem);
}

.rot-06__fact {
  min-inline-size: 0;
  padding: 1rem;
  border: 1px solid var(--rule);
  border-radius: 0.875rem;
  background: rgba(255, 255, 255, 0.05);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
}

.rot-06__facth {
  margin: 0 0 0.4rem;
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--accent);
}

.rot-06__factp {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.6;
  color: var(--muted);
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .rot-06__cube {
    animation: none;
    transform: rotateX(-22deg) rotateY(-38deg);
  }
}

.rot-06:has(.rot-06__pausebox:checked) .rot-06__cube {
  animation-play-state: paused;
}

.rot-06__theme {
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

.rot-06__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-06__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-06__themeopt {
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

.rot-06__themeopt:hover {
  opacity: 0.85;
}

.rot-06__themeinput:checked + .rot-06__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-06__themeinput:focus-visible + .rot-06__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.rot-06__pause {
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

.rot-06__pausebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-06__pausedot {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  inline-size: 2.25rem;
  block-size: 2.25rem;
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 12%, transparent);
}

.rot-06__pause:has(.rot-06__pausebox:focus-visible) {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.rot-06:has(.rot-06__pausebox:checked) .rot-06__pausedot {
  background: var(--accent);
  color: #04121a;
}

@media (forced-colors: active) {
  .rot-06__theme,
    .rot-06__pause {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-06__themeinput:checked + .rot-06__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: light) {
  .rot-06:not(:has(#rot-06-theme-dark:checked)) {
    --ink: #0d1430;
    --muted: #55618a;
    --rule: rgba(20, 34, 80, 0.16);
    --surface: rgba(20, 40, 100, 0.06);
    --accent: #0f8f88;
    background: radial-gradient(120% 90% at 50% -10%, #eef3ff 0%, #e4eaf8 55%, #dbe2f2 100%);
  }

  .rot-06:not(:has(#rot-06-theme-dark:checked)) .rot-06__fact {
    background: rgba(255, 255, 255, 0.6);
  }
}

@media (prefers-color-scheme: dark) {
  .rot-06:has(#rot-06-theme-light:checked) {
    --ink: #0d1430;
    --muted: #55618a;
    --rule: rgba(20, 34, 80, 0.16);
    --surface: rgba(20, 40, 100, 0.06);
    --accent: #0f8f88;
    background: radial-gradient(120% 90% at 50% -10%, #eef3ff 0%, #e4eaf8 55%, #dbe2f2 100%);
  }

  .rot-06:has(#rot-06-theme-light:checked) .rot-06__fact {
    background: rgba(255, 255, 255, 0.6);
  }
}

[data-theme="light"] .rot-06:not(:has(#rot-06-theme-dark:checked)) {
  --ink: #0d1430;
  --muted: #55618a;
  --rule: rgba(20, 34, 80, 0.16);
  --surface: rgba(20, 40, 100, 0.06);
  --accent: #0f8f88;
  background: radial-gradient(120% 90% at 50% -10%, #eef3ff 0%, #e4eaf8 55%, #dbe2f2 100%);
}

.rot-06:has(#rot-06-theme-light:checked) {
  --ink: #0d1430;
  --muted: #55618a;
  --rule: rgba(20, 34, 80, 0.16);
  --surface: rgba(20, 40, 100, 0.06);
  --accent: #0f8f88;
  background: radial-gradient(120% 90% at 50% -10%, #eef3ff 0%, #e4eaf8 55%, #dbe2f2 100%);
}

.rot-06:has(#rot-06-theme-light:checked) .rot-06__fact {
  background: rgba(255, 255, 255, 0.6);
}

.rot-06:has(#rot-06-theme-light:checked) .rot-06__pausedot {
  color: #ffffff;
}

.rot-06:has(#rot-06-theme-dark:checked) {
  --ink: #e8edff;
  --muted: #97a3c8;
  --rule: rgba(150, 175, 255, 0.18);
  --surface: rgba(255, 255, 255, 0.06);
  --accent: #4fd8d0;
  background: radial-gradient(120% 90% at 50% -10%, #12204a 0%, #070c1c 55%, #04060f 100%);
}

.rot-06:has(#rot-06-theme-dark:checked) .rot-06__fact {
  background: rgba(255, 255, 255, 0.05);
}
/* Site-theme bridge: the per-demo page stamps [data-theme] on the iframe
   root. Without these rules a dark-by-default demo followed the OS instead
   of the site when the visitor was on OS-light + site-dark. Guarded by the
   light toggle so the in-demo switch still wins. */

[data-theme="dark"] .rot-06:not(:has(#rot-06-theme-light:checked)) {
  --ink: #e8edff;
  --muted: #97a3c8;
  --rule: rgba(150, 175, 255, 0.18);
  --surface: rgba(255, 255, 255, 0.06);
  --accent: #4fd8d0;
  background: radial-gradient(120% 90% at 50% -10%, #12204a 0%, #070c1c 55%, #04060f 100%);
}

[data-theme="dark"] .rot-06:not(:has(#rot-06-theme-light:checked)) .rot-06__fact {
  background: rgba(255, 255, 255, 0.05);
}
```
