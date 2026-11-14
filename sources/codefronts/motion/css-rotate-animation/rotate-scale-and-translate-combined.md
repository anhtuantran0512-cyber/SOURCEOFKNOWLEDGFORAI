---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/rotate-scale-and-translate-combined/"
title: "Rotate Scale and Translate Combined"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "rotate(45deg) translateX(120px) and translateX(120px) rotate(45deg) land in completely different places, because each function transforms the coordinate…"
has_js: "false"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rotate Scale and Translate Combined
Source: https://codefronts.com/motion/css-rotate-animation/rotate-scale-and-translate-combined/

rotate(45deg) translateX(120px) and translateX(120px) rotate(45deg) land in completely different places, because each function transforms the coordinate system the next one works in. Both are drawn here over the same axes so the difference is a diagram rather than a claim, followed by the modern independent properties that apply in a fixed order instead.
## HTML
```html
<section class="rot-10" aria-labelledby="rot-10-h">
  <fieldset class="rot-10__theme">
    <legend class="rot-10__themelegend">Theme</legend>
    <input class="rot-10__themeinput" type="radio" name="rot-10-theme" id="rot-10-theme-auto" checked>
    <label class="rot-10__themeopt" for="rot-10-theme-auto">Auto</label>
    <input class="rot-10__themeinput" type="radio" name="rot-10-theme" id="rot-10-theme-light">
    <label class="rot-10__themeopt" for="rot-10-theme-light">Light</label>
    <input class="rot-10__themeinput" type="radio" name="rot-10-theme" id="rot-10-theme-dark">
    <label class="rot-10__themeopt" for="rot-10-theme-dark">Dark</label>
  </fieldset>
  <label class="rot-10__step">
    <input class="rot-10__stepbox" type="checkbox" id="rot-10-step">
    <span class="rot-10__stepdot" aria-hidden="true">
      <svg viewBox="0 0 16 16" width="12" height="12" focusable="false"><path d="M4 3.5v9l8-4.5z" fill="currentColor"></path></svg>
    </span>
    <span class="rot-10__steptext">Step through</span>
  </label>

  <div class="rot-10__stage">
    <header class="rot-10__head">
      <p class="rot-10__eyebrow">Composition order</p>
      <h2 class="rot-10__h" id="rot-10-h">Same two functions. Two different places.</h2>
      <p class="rot-10__sub">Each function transforms the coordinate system the next one operates in. Turn on <span class="rot-10__code">Step through</span> to walk each sequence one function at a time.</p>
    </header>

    <div class="rot-10__pair">
      <figure class="rot-10__plot">
        <figcaption class="rot-10__plotcap">transform: rotate(45deg) translateX(120px)</figcaption>
        <div class="rot-10__ground">
          <span class="rot-10__axis rot-10__axis--x" aria-hidden="true"></span>
          <span class="rot-10__axis rot-10__axis--y" aria-hidden="true"></span>
          <span class="rot-10__ghost" aria-hidden="true"></span>
          <span class="rot-10__tile rot-10__tile--rotfirst" aria-hidden="true">A</span>
        </div>
        <p class="rot-10__plotnote">Rotates the axes first, then travels along the rotated X. The tile leaves on a diagonal.</p>
      </figure>

      <figure class="rot-10__plot">
        <figcaption class="rot-10__plotcap">transform: translateX(120px) rotate(45deg)</figcaption>
        <div class="rot-10__ground">
          <span class="rot-10__axis rot-10__axis--x" aria-hidden="true"></span>
          <span class="rot-10__axis rot-10__axis--y" aria-hidden="true"></span>
          <span class="rot-10__ghost" aria-hidden="true"></span>
          <span class="rot-10__tile rot-10__tile--transfirst" aria-hidden="true">B</span>
        </div>
        <p class="rot-10__plotnote">Travels along the screen X first, then spins in place. Same distance, different heading.</p>
      </figure>
    </div>

    <article class="rot-10__modern">
      <h3 class="rot-10__modernh">The modern alternative</h3>
      <div class="rot-10__modernbody">
        <div class="rot-10__ground rot-10__ground--sm">
          <span class="rot-10__axis rot-10__axis--x" aria-hidden="true"></span>
          <span class="rot-10__axis rot-10__axis--y" aria-hidden="true"></span>
          <span class="rot-10__ghost" aria-hidden="true"></span>
          <span class="rot-10__tile rot-10__tile--indep" aria-hidden="true">C</span>
        </div>
        <div class="rot-10__moderntext">
          <pre class="rot-10__pre">translate: 120px 0;
rotate: 45deg;
scale: 1.1;</pre>
          <p class="rot-10__modernp">Three separate properties, applied in a fixed order — translate, then rotate, then scale — regardless of how they are written. Each one can be animated on its own, and a hover that changes <span class="rot-10__code">scale</span> no longer has to restate the rotation.</p>
        </div>
      </div>
    </article>
  </div>
</section>
```
## CSS
```css
.rot-10 {
  --page: #eef1f4;
  --surface: #ffffff;
  --ink: #10161d;
  --muted: #576373;
  --rule: #cfd6de;
  --grid: #dde3ea;
  --accent: #1f5fd0;
  --angle: 45deg;
  --shift: clamp(3rem, 12vw, 6.5rem);
  --scl: 1.1;
  --seq: 5s;
  --font-display: "Courier New", ui-monospace, Menlo, monospace;
  position: relative;
  width: 100%;
  min-height: 100vh;
  display: block;
  box-sizing: border-box;
  background: var(--page);
  color: var(--ink);
  font-family: system-ui, sans-serif;
  -webkit-font-smoothing: antialiased;
}

@supports (color: oklch(0 0 0)) {
  .rot-10 {
    --accent: oklch(0.5 0.19 262);
  }
}

.rot-10 *,
.rot-10 *::before,
.rot-10 *::after {
  box-sizing: border-box;
}

.rot-10__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.25rem, 3.5vw, 2rem);
  padding: clamp(1.25rem, 4vw, 3rem);
  padding-block-start: 5.25rem;
}

.rot-10__head {
  max-inline-size: 38rem;
  min-inline-size: 0;
  text-align: center;
}

.rot-10__eyebrow {
  margin: 0 0 0.55rem;
  font-family: var(--font-display);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--accent);
}

.rot-10__h {
  margin: 0 0 0.55rem;
  font-family: var(--font-display);
  font-size: clamp(1.375rem, 4.6vw, 2.125rem);
  font-weight: 700;
  line-height: 1.15;
}

.rot-10__sub {
  margin: 0;
  font-size: 0.9375rem;
  line-height: 1.6;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-10__code {
  font-family: var(--font-display);
  font-size: 0.9em;
  color: var(--accent);
}

.rot-10__pair {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
  gap: clamp(1rem, 3vw, 1.5rem);
  inline-size: min(100%, 50rem);
}

.rot-10__plot {
  margin: 0;
  min-inline-size: 0;
  display: grid;
  gap: 0.6rem;
  padding: 0.875rem;
  border: 1px solid var(--rule);
  border-radius: 0.5rem;
  background: var(--surface);
}

.rot-10__plotcap {
  font-family: var(--font-display);
  font-size: 0.75rem;
  letter-spacing: -0.01em;
  color: var(--accent);
  word-break: break-word;
}

.rot-10__ground {
  position: relative;
  aspect-ratio: 1;
  min-inline-size: 0;
  border: 1px solid var(--rule);
  background-image: repeating-linear-gradient(0deg, var(--grid) 0 1px, transparent 1px 1.25rem), repeating-linear-gradient(90deg, var(--grid) 0 1px, transparent 1px 1.25rem);
  overflow: hidden;
}

.rot-10__ground--sm {
  inline-size: min(100%, 13rem);
}

.rot-10__axis {
  position: absolute;
  background: color-mix(in srgb, var(--ink) 35%, transparent);
}

.rot-10__axis--x {
  inset-block-start: 50%;
  inset-inline: 0;
  block-size: 1px;
}

.rot-10__axis--y {
  inset-inline-start: 50%;
  inset-block: 0;
  inline-size: 1px;
}

.rot-10__ghost {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  margin: -1.375rem 0 0 -1.375rem;
  border: 1px dashed color-mix(in srgb, var(--ink) 40%, transparent);
}

.rot-10__tile {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  display: grid;
  place-items: center;
  inline-size: 2.75rem;
  block-size: 2.75rem;
  margin: -1.375rem 0 0 -1.375rem;
  background: var(--accent);
  color: #ffffff;
  font-family: var(--font-display);
  font-size: 0.9375rem;
  font-weight: 700;
}

.rot-10__tile--rotfirst {
  transform: rotate(var(--angle)) translateX(var(--shift));
}

.rot-10__tile--transfirst {
  transform: translateX(var(--shift)) rotate(var(--angle));
}

.rot-10__tile--indep {
  transform: none;
  translate: var(--shift) 0;
  rotate: var(--angle);
  scale: var(--scl);
}

.rot-10__plotnote {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.55;
  color: var(--muted);
  min-inline-size: 0;
}

.rot-10__modern {
  inline-size: min(100%, 50rem);
  display: grid;
  gap: 0.875rem;
  padding: clamp(0.875rem, 3vw, 1.25rem);
  border: 1px solid var(--rule);
  border-radius: 0.5rem;
  background: var(--surface);
}

.rot-10__modernh {
  margin: 0;
  font-family: var(--font-display);
  font-size: 0.875rem;
  font-weight: 700;
  letter-spacing: 0.02em;
}

.rot-10__modernbody {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(13rem, 1fr));
  gap: 1rem;
  align-items: start;
}

.rot-10__moderntext {
  min-inline-size: 0;
  display: grid;
  gap: 0.75rem;
}

.rot-10__pre {
  margin: 0;
  padding: 0.75rem;
  border-radius: 0.375rem;
  background: color-mix(in srgb, var(--accent) 8%, transparent);
  font-family: var(--font-display);
  font-size: 0.8125rem;
  line-height: 1.5;
  overflow-x: auto;
}

.rot-10__modernp {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.65;
  color: var(--muted);
  min-inline-size: 0;
}

@keyframes rot-10-seq-a {
  0%,
    12% {
    transform: rotate(0deg) translateX(0);
  }

  32%,
    48% {
    transform: rotate(var(--angle)) translateX(0);
  }

  70%,
    100% {
    transform: rotate(var(--angle)) translateX(var(--shift));
  }
}

@keyframes rot-10-seq-b {
  0%,
    12% {
    transform: translateX(0) rotate(0deg);
  }

  32%,
    48% {
    transform: translateX(var(--shift)) rotate(0deg);
  }

  70%,
    100% {
    transform: translateX(var(--shift)) rotate(var(--angle));
  }
}

.rot-10:has(.rot-10__stepbox:checked) .rot-10__tile--rotfirst {
  animation: rot-10-seq-a var(--seq) ease-in-out infinite;
}

.rot-10:has(.rot-10__stepbox:checked) .rot-10__tile--transfirst {
  animation: rot-10-seq-b var(--seq) ease-in-out infinite;
}

.rot-10:has(.rot-10__stepbox:checked) .rot-10__stepdot {
  background: var(--accent);
  color: #ffffff;
}

@media (prefers-reduced-motion: reduce) {
  .rot-10:has(.rot-10__stepbox:checked) .rot-10__tile--rotfirst {
    animation: none;
    transform: rotate(var(--angle)) translateX(var(--shift));
  }

  .rot-10:has(.rot-10__stepbox:checked) .rot-10__tile--transfirst {
    animation: none;
    transform: translateX(var(--shift)) rotate(var(--angle));
  }
}

.rot-10__theme {
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

.rot-10__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-10__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-10__themeopt {
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

.rot-10__themeopt:hover {
  opacity: 0.85;
}

.rot-10__themeinput:checked + .rot-10__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-10__themeinput:focus-visible + .rot-10__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.rot-10__step {
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
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  user-select: none;
}

.rot-10__stepbox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-10__stepdot {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  inline-size: 2.25rem;
  block-size: 2.25rem;
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 12%, transparent);
}

.rot-10__step:has(.rot-10__stepbox:focus-visible) {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .rot-10__theme,
    .rot-10__step {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-10__themeinput:checked + .rot-10__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: dark) {
  .rot-10:not(:has(#rot-10-theme-light:checked)) {
    --page: #0c1016;
    --surface: #131922;
    --ink: #e6ecf4;
    --muted: #8b97a8;
    --rule: #232c38;
    --grid: #1b232e;
    --accent: #6fa8ff;
  }

  .rot-10:not(:has(#rot-10-theme-light:checked)) .rot-10__tile {
    color: #08101c;
  }
}

@media (prefers-color-scheme: light) {
  .rot-10:has(#rot-10-theme-dark:checked) {
    --page: #0c1016;
    --surface: #131922;
    --ink: #e6ecf4;
    --muted: #8b97a8;
    --rule: #232c38;
    --grid: #1b232e;
    --accent: #6fa8ff;
  }
}

[data-theme="dark"] .rot-10:not(:has(#rot-10-theme-light:checked)) {
  --page: #0c1016;
  --surface: #131922;
  --ink: #e6ecf4;
  --muted: #8b97a8;
  --rule: #232c38;
  --grid: #1b232e;
  --accent: #6fa8ff;
}

[data-theme="dark"] .rot-10:not(:has(#rot-10-theme-light:checked)) .rot-10__tile {
  color: #08101c;
}

.rot-10:has(#rot-10-theme-dark:checked) {
  --page: #0c1016;
  --surface: #131922;
  --ink: #e6ecf4;
  --muted: #8b97a8;
  --rule: #232c38;
  --grid: #1b232e;
  --accent: #6fa8ff;
}

.rot-10:has(#rot-10-theme-dark:checked) .rot-10__tile {
  color: #08101c;
}

.rot-10:has(#rot-10-theme-dark:checked) .rot-10__stepdot {
  color: #08101c;
}

.rot-10:has(#rot-10-theme-light:checked) {
  --page: #eef1f4;
  --surface: #ffffff;
  --ink: #10161d;
  --muted: #576373;
  --rule: #cfd6de;
  --grid: #dde3ea;
  --accent: #1f5fd0;
}

.rot-10:has(#rot-10-theme-light:checked) .rot-10__tile {
  color: #ffffff;
}
```
