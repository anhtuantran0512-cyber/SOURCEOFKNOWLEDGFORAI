---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/rotate-text-around-a-circle/"
title: "Rotate Text Around a Circle"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "Text set around a circle with one formula and no SVG: every character gets its own span, rotated by its index times 360 over the character count, then pushed…"
has_js: "false"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rotate Text Around a Circle
Source: https://codefronts.com/motion/css-rotate-animation/rotate-text-around-a-circle/

Text set around a circle with one formula and no SVG: every character gets its own span, rotated by its index times 360 over the character count, then pushed outward with a translate. The wrapper carries an aria-label with the readable string, because a screen reader announcing thirty separate letters is worse than useless.
## HTML
```html
<section class="rot-16" aria-labelledby="rot-16-h">
  <fieldset class="rot-16__theme">
    <legend class="rot-16__themelegend">Theme</legend>
    <input class="rot-16__themeinput" type="radio" name="rot-16-theme" id="rot-16-theme-auto" checked>
    <label class="rot-16__themeopt" for="rot-16-theme-auto">Auto</label>
    <input class="rot-16__themeinput" type="radio" name="rot-16-theme" id="rot-16-theme-light">
    <label class="rot-16__themeopt" for="rot-16-theme-light">Light</label>
    <input class="rot-16__themeinput" type="radio" name="rot-16-theme" id="rot-16-theme-dark">
    <label class="rot-16__themeopt" for="rot-16-theme-dark">Dark</label>
  </fieldset>
  <label class="rot-16__pause">
    <input class="rot-16__pausebox" type="checkbox" id="rot-16-pause">
    <span class="rot-16__pausedot" aria-hidden="true">
      <svg viewBox="0 0 16 16" width="12" height="12" focusable="false"><rect x="4" y="3" width="3" height="10" rx="1" fill="currentColor"></rect><rect x="9" y="3" width="3" height="10" rx="1" fill="currentColor"></rect></svg>
    </span>
    <span class="rot-16__pausetext">Pause</span>
  </label>

  <div class="rot-16__stage">
    <header class="rot-16__head">
      <p class="rot-16__eyebrow">Vale Roastery · Seal</p>
      <h2 class="rot-16__h" id="rot-16-h">One formula, thirty glyphs, one ring</h2>
      <p class="rot-16__sub">Each character is rotated by its index times 360 over the count, then pushed out along its own axis. Change the string, change the count, and the ring closes itself.</p>
    </header>

    <div class="rot-16__seal">
      <div class="rot-16__ring rot-16__spin" style="--count: 30" aria-label="Vale Roastery · Single Origin · Est 1994" role="img">
        <span class="rot-16__ch" style="--i: 0" aria-hidden="true">V</span>
        <span class="rot-16__ch" style="--i: 1" aria-hidden="true">A</span>
        <span class="rot-16__ch" style="--i: 2" aria-hidden="true">L</span>
        <span class="rot-16__ch" style="--i: 3" aria-hidden="true">E</span>
        <span class="rot-16__ch" style="--i: 4" aria-hidden="true">·</span>
        <span class="rot-16__ch" style="--i: 5" aria-hidden="true">R</span>
        <span class="rot-16__ch" style="--i: 6" aria-hidden="true">O</span>
        <span class="rot-16__ch" style="--i: 7" aria-hidden="true">A</span>
        <span class="rot-16__ch" style="--i: 8" aria-hidden="true">S</span>
        <span class="rot-16__ch" style="--i: 9" aria-hidden="true">T</span>
        <span class="rot-16__ch" style="--i: 10" aria-hidden="true">E</span>
        <span class="rot-16__ch" style="--i: 11" aria-hidden="true">R</span>
        <span class="rot-16__ch" style="--i: 12" aria-hidden="true">Y</span>
        <span class="rot-16__ch" style="--i: 13" aria-hidden="true">·</span>
        <span class="rot-16__ch" style="--i: 14" aria-hidden="true">S</span>
        <span class="rot-16__ch" style="--i: 15" aria-hidden="true">I</span>
        <span class="rot-16__ch" style="--i: 16" aria-hidden="true">N</span>
        <span class="rot-16__ch" style="--i: 17" aria-hidden="true">G</span>
        <span class="rot-16__ch" style="--i: 18" aria-hidden="true">L</span>
        <span class="rot-16__ch" style="--i: 19" aria-hidden="true">E</span>
        <span class="rot-16__ch" style="--i: 20" aria-hidden="true">·</span>
        <span class="rot-16__ch" style="--i: 21" aria-hidden="true">O</span>
        <span class="rot-16__ch" style="--i: 22" aria-hidden="true">R</span>
        <span class="rot-16__ch" style="--i: 23" aria-hidden="true">I</span>
        <span class="rot-16__ch" style="--i: 24" aria-hidden="true">G</span>
        <span class="rot-16__ch" style="--i: 25" aria-hidden="true">I</span>
        <span class="rot-16__ch" style="--i: 26" aria-hidden="true">N</span>
        <span class="rot-16__ch" style="--i: 27" aria-hidden="true">·</span>
        <span class="rot-16__ch" style="--i: 28" aria-hidden="true">9</span>
        <span class="rot-16__ch" style="--i: 29" aria-hidden="true">4</span>
      </div>
      <div class="rot-16__core">
        <span class="rot-16__coreh">Est<br>1994</span>
      </div>
    </div>

    <div class="rot-16__notes">
      <article class="rot-16__note">
        <h3 class="rot-16__noteh">The step</h3>
        <pre class="rot-16__pre">rotate(calc(var(--i) * (360deg / var(--count))))
translateY(calc(var(--radius) * -1))</pre>
        <p class="rot-16__notep">Rotate first, then push outward. Reverse the order and every glyph lands on top of the next.</p>
      </article>
      <article class="rot-16__note">
        <h3 class="rot-16__noteh">The announcement</h3>
        <p class="rot-16__notep">The wrapper carries <span class="rot-16__code">aria-label</span> with the readable string and every span is <span class="rot-16__code">aria-hidden</span>. Without that, a screen reader reads out thirty separate characters.</p>
        <p class="rot-16__notep">For an ellipse, a wave or real kerning along the curve, use SVG <span class="rot-16__code">textPath</span> instead — per-character rotation only makes circles and arcs.</p>
      </article>
    </div>
  </div>
</section>
```
## CSS
```css
.rot-16 {
  --page: #ece4dc;
  --surface: #f3ece5;
  --ink: #2c2118;
  --muted: #6d5d50;
  --rule: #d8cbbe;
  --accent: #b8306e;
  --radius: clamp(4.5rem, 17vw, 7rem);
  --ring-dur: 40s;
  --font-display: Didot, "Playfair Display", "Times New Roman", Georgia, serif;
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
  .rot-16 {
    --accent: oklch(0.52 0.18 355);
  }
}

.rot-16 *,
.rot-16 *::before,
.rot-16 *::after {
  box-sizing: border-box;
}

.rot-16__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.75rem, 4.5vw, 3rem);
  padding: clamp(1.5rem, 4vw, 3.5rem);
  padding-block-start: 5.5rem;
}

.rot-16__head {
  max-inline-size: 36rem;
  min-inline-size: 0;
  text-align: center;
}

.rot-16__eyebrow {
  margin: 0 0 0.6rem;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.24em;
  text-transform: uppercase;
  color: var(--accent);
}

.rot-16__h {
  margin: 0 0 0.6rem;
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 5vw, 2.5rem);
  font-weight: 400;
  line-height: 1.1;
}

.rot-16__sub {
  margin: 0;
  font-size: 0.9375rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-16__code {
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.85em;
  color: var(--accent);
}

.rot-16__seal {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: calc(var(--radius) * 2.75);
  aspect-ratio: 1;
  border-radius: 50%;
  background: var(--surface);
  box-shadow: 10px 10px 22px rgba(120, 100, 84, 0.32), -10px -10px 22px rgba(255, 255, 255, 0.85), inset 0 0 0 1px rgba(255, 255, 255, 0.5);
}

.rot-16__ring {
  position: absolute;
  inset: 0;
}

.rot-16__spin {
  animation: rot-16-ring var(--ring-dur) linear infinite;
}

@keyframes rot-16-ring {
  to {
    transform: rotate(360deg);
  }
}

.rot-16__ch {
  position: absolute;
  inset-block-start: 50%;
  inset-inline-start: 50%;
  inline-size: 1.2em;
  margin: -0.6em 0 0 -0.6em;
  font-family: var(--font-display);
  font-size: clamp(0.875rem, 3.2vw, 1.125rem);
  font-weight: 500;
  letter-spacing: 0.02em;
  text-align: center;
  color: var(--ink);
  transform-origin: 50% 50%;
  transform: rotate(calc(var(--i) * (360deg / var(--count)))) translateY(calc(var(--radius) * -1));
}

.rot-16__core {
  position: relative;
  display: grid;
  place-items: center;
  inline-size: calc(var(--radius) * 1.05);
  aspect-ratio: 1;
  border: 1px solid var(--accent);
  border-radius: 50%;
  background: var(--surface);
  box-shadow: inset 4px 4px 10px rgba(120, 100, 84, 0.25), inset -4px -4px 10px rgba(255, 255, 255, 0.9);
}

.rot-16__coreh {
  font-family: var(--font-display);
  font-size: clamp(0.875rem, 3vw, 1.125rem);
  line-height: 1.25;
  text-align: center;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--accent);
}

.rot-16__notes {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
  gap: 1rem;
  inline-size: min(100%, 44rem);
}

.rot-16__note {
  min-inline-size: 0;
  display: grid;
  gap: 0.6rem;
  padding: 1rem;
  border-radius: 0.875rem;
  background: var(--surface);
  box-shadow: 6px 6px 14px rgba(120, 100, 84, 0.24), -6px -6px 14px rgba(255, 255, 255, 0.8);
}

.rot-16__noteh {
  margin: 0;
  font-family: var(--font-display);
  font-size: 1rem;
  font-weight: 500;
}

.rot-16__pre {
  margin: 0;
  padding: 0.65rem;
  border-radius: 0.5rem;
  background: color-mix(in srgb, var(--accent) 8%, transparent);
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.6875rem;
  line-height: 1.6;
  overflow-x: auto;
}

.rot-16__notep {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.65;
  color: var(--muted);
  min-inline-size: 0;
}

@media (prefers-reduced-motion: reduce) {
  .rot-16__spin {
    animation: none;
  }
}

.rot-16:has(.rot-16__pausebox:checked) .rot-16__spin {
  animation-play-state: paused;
}

.rot-16__theme {
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

.rot-16__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-16__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-16__themeopt {
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

.rot-16__themeopt:hover {
  opacity: 0.85;
}

.rot-16__themeinput:checked + .rot-16__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-16__themeinput:focus-visible + .rot-16__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.rot-16__pause {
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

.rot-16__pausebox {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-16__pausedot {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  inline-size: 2.25rem;
  block-size: 2.25rem;
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 12%, transparent);
}

.rot-16__pause:has(.rot-16__pausebox:focus-visible) {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

.rot-16:has(.rot-16__pausebox:checked) .rot-16__pausedot {
  background: var(--accent);
  color: #fdf6f9;
}

@media (forced-colors: active) {
  .rot-16__theme,
    .rot-16__pause {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-16__themeinput:checked + .rot-16__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: dark) {
  .rot-16:not(:has(#rot-16-theme-light:checked)) {
    --page: #191410;
    --surface: #211a15;
    --ink: #f0e6dc;
    --muted: #a3907f;
    --rule: #33291f;
    --accent: #ff7ab0;
  }

  .rot-16:not(:has(#rot-16-theme-light:checked)) .rot-16__seal {
    box-shadow: 10px 10px 22px rgba(0, 0, 0, 0.6), -10px -10px 22px rgba(255, 255, 255, 0.05), inset 0 0 0 1px rgba(255, 255, 255, 0.06);
  }

  .rot-16:not(:has(#rot-16-theme-light:checked)) .rot-16__core {
    box-shadow: inset 4px 4px 10px rgba(0, 0, 0, 0.6), inset -4px -4px 10px rgba(255, 255, 255, 0.05);
  }

  .rot-16:not(:has(#rot-16-theme-light:checked)) .rot-16__note {
    box-shadow: 6px 6px 14px rgba(0, 0, 0, 0.55), -6px -6px 14px rgba(255, 255, 255, 0.04);
  }
}

@media (prefers-color-scheme: light) {
  .rot-16:has(#rot-16-theme-dark:checked) {
    --page: #191410;
    --surface: #211a15;
    --ink: #f0e6dc;
    --muted: #a3907f;
    --rule: #33291f;
    --accent: #ff7ab0;
  }
}

[data-theme="dark"] .rot-16:not(:has(#rot-16-theme-light:checked)) {
  --page: #191410;
  --surface: #211a15;
  --ink: #f0e6dc;
  --muted: #a3907f;
  --rule: #33291f;
  --accent: #ff7ab0;
}

[data-theme="dark"] .rot-16:not(:has(#rot-16-theme-light:checked)) .rot-16__seal {
  box-shadow: 10px 10px 22px rgba(0, 0, 0, 0.6), -10px -10px 22px rgba(255, 255, 255, 0.05), inset 0 0 0 1px rgba(255, 255, 255, 0.06);
}

.rot-16:has(#rot-16-theme-dark:checked) {
  --page: #191410;
  --surface: #211a15;
  --ink: #f0e6dc;
  --muted: #a3907f;
  --rule: #33291f;
  --accent: #ff7ab0;
}

.rot-16:has(#rot-16-theme-dark:checked) .rot-16__seal {
  box-shadow: 10px 10px 22px rgba(0, 0, 0, 0.6), -10px -10px 22px rgba(255, 255, 255, 0.05), inset 0 0 0 1px rgba(255, 255, 255, 0.06);
}

.rot-16:has(#rot-16-theme-dark:checked) .rot-16__core {
  box-shadow: inset 4px 4px 10px rgba(0, 0, 0, 0.6), inset -4px -4px 10px rgba(255, 255, 255, 0.05);
}

.rot-16:has(#rot-16-theme-dark:checked) .rot-16__note {
  box-shadow: 6px 6px 14px rgba(0, 0, 0, 0.55), -6px -6px 14px rgba(255, 255, 255, 0.04);
}

.rot-16:has(#rot-16-theme-dark:checked) .rot-16__pausedot {
  color: #1a0f14;
}

.rot-16:has(#rot-16-theme-light:checked) {
  --page: #ece4dc;
  --surface: #f3ece5;
  --ink: #2c2118;
  --muted: #6d5d50;
  --rule: #d8cbbe;
  --accent: #b8306e;
}

.rot-16:has(#rot-16-theme-light:checked) .rot-16__seal {
  box-shadow: 10px 10px 22px rgba(120, 100, 84, 0.32), -10px -10px 22px rgba(255, 255, 255, 0.85), inset 0 0 0 1px rgba(255, 255, 255, 0.5);
}

.rot-16:has(#rot-16-theme-light:checked) .rot-16__core {
  box-shadow: inset 4px 4px 10px rgba(120, 100, 84, 0.25), inset -4px -4px 10px rgba(255, 255, 255, 0.9);
}

.rot-16:has(#rot-16-theme-light:checked) .rot-16__note {
  box-shadow: 6px 6px 14px rgba(120, 100, 84, 0.24), -6px -6px 14px rgba(255, 255, 255, 0.8);
}
```
