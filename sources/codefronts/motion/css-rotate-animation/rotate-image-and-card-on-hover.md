---
source: "codefronts"
url: "https://codefronts.com/motion/css-rotate-animation/rotate-image-and-card-on-hover/"
title: "Rotate Image and Card on Hover"
section: "motion"
category: "css-rotate-animation"
category_name: "CSS Rotate Animations"
description: "A three-to-six degree tilt on hover, eased in both directions, with the transition declared on the base selector rather than inside :hover."
has_js: "false"
---

Here's a working CSS Rotate Animation from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Rotate Image and Card on Hover
Source: https://codefronts.com/motion/css-rotate-animation/rotate-image-and-card-on-hover/

A three-to-six degree tilt on hover, eased in both directions, with the transition declared on the base selector rather than inside :hover. The demo shows both versions so you can feel the difference: the broken card snaps back the instant the pointer leaves, the correct one eases out. The whole effect is gated behind a pointer query so touch users never get a stuck transform.
## HTML
```html
<section class="rot-02" aria-labelledby="rot-02-h">
  <fieldset class="rot-02__theme">
    <legend class="rot-02__themelegend">Theme</legend>
    <input class="rot-02__themeinput" type="radio" name="rot-02-theme" id="rot-02-theme-auto" checked>
    <label class="rot-02__themeopt" for="rot-02-theme-auto">Auto</label>
    <input class="rot-02__themeinput" type="radio" name="rot-02-theme" id="rot-02-theme-light">
    <label class="rot-02__themeopt" for="rot-02-theme-light">Light</label>
    <input class="rot-02__themeinput" type="radio" name="rot-02-theme" id="rot-02-theme-dark">
    <label class="rot-02__themeopt" for="rot-02-theme-dark">Dark</label>
  </fieldset>

  <div class="rot-02__stage">
    <header class="rot-02__head">
      <p class="rot-02__eyebrow">Hover · Sable Atlas</p>
      <h2 class="rot-02__h" id="rot-02-h">Four degrees is a response. Forty-five is a stunt.</h2>
      <p class="rot-02__sub">Hover both cards. They tilt identically on the way in — the difference is entirely in what happens when the pointer leaves.</p>
    </header>

    <div class="rot-02__pair">
      <article class="rot-02__card rot-02__card--right" tabindex="0">
        <p class="rot-02__chip">transition on the base selector</p>
        <div class="rot-02__art" aria-hidden="true">
          <span class="rot-02__artmark"></span>
          <span class="rot-02__artgrain"></span>
        </div>
        <h3 class="rot-02__cardh">Atlas Field Notes</h3>
        <p class="rot-02__cardp">Volume four. Ninety-six pages, sewn binding, printed in Vale.</p>
        <p class="rot-02__foot">Eases out as cleanly as it eased in</p>
      </article>

      <article class="rot-02__card rot-02__card--wrong" tabindex="0">
        <p class="rot-02__chip rot-02__chip--warn">transition inside :hover</p>
        <div class="rot-02__art" aria-hidden="true">
          <span class="rot-02__artmark"></span>
          <span class="rot-02__artgrain"></span>
        </div>
        <h3 class="rot-02__cardh">Atlas Field Notes</h3>
        <p class="rot-02__cardp">Volume four. Ninety-six pages, sewn binding, printed in Vale.</p>
        <p class="rot-02__foot rot-02__foot--warn">Snaps flat the instant you leave</p>
      </article>
    </div>

    <p class="rot-02__note">Both cards are wrapped in <span class="rot-02__code">@media (hover: hover) and (pointer: fine)</span>, so on a phone neither one tilts — a tap can otherwise leave <span class="rot-02__code">:hover</span> matching and the transform stuck.</p>
  </div>
</section>
```
## CSS
```css
.rot-02 {
  --page: #f4f1ea;
  --surface: #fffdf8;
  --ink: #221c14;
  --muted: #6d6355;
  --rule: #ded6c7;
  --accent: #c2542b;
  --tilt: 4deg;
  --lift: -5px;
  --ease: cubic-bezier(0.22, 0.7, 0.25, 1);
  --radius: 0.75rem;
  --font-display: "Iowan Old Style", "Palatino Linotype", Palatino, Georgia, serif;
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
  .rot-02 {
    --accent: oklch(0.56 0.16 38);
  }
}

.rot-02 *,
.rot-02 *::before,
.rot-02 *::after {
  box-sizing: border-box;
}

.rot-02__stage {
  display: grid;
  place-items: center;
  gap: clamp(1.75rem, 5vw, 3rem);
  padding: clamp(1.25rem, 4vw, 3.5rem);
  padding-block-start: 5.25rem;
}

.rot-02__head {
  max-inline-size: 38rem;
  min-inline-size: 0;
  text-align: center;
}

.rot-02__eyebrow {
  margin: 0 0 0.75rem;
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--accent);
}

.rot-02__h {
  margin: 0 0 0.75rem;
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 5vw, 2.5rem);
  font-weight: 400;
  line-height: 1.12;
  letter-spacing: -0.01em;
}

.rot-02__sub {
  margin: 0;
  font-size: 0.9375rem;
  line-height: 1.65;
  color: var(--muted);
  text-wrap: pretty;
}

.rot-02__code {
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.85em;
  color: var(--ink);
  border-block-end: 1px solid var(--rule);
}

.rot-02__pair {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
  gap: clamp(1.5rem, 5vw, 3rem);
  inline-size: min(100%, 44rem);
  padding: 1.25rem;
}

.rot-02__card {
  min-inline-size: 0;
  display: grid;
  gap: 0.6rem;
  padding: 1.25rem 1.25rem 1.4rem;
  border-radius: var(--radius);
  background: var(--surface);
  box-shadow: 0 1px 0 var(--rule);
  transform-origin: 50% 85%;
  outline: none;
}

.rot-02__card--right {
  transition: transform 220ms var(--ease), box-shadow 220ms var(--ease);
}

.rot-02__chip {
  justify-self: start;
  margin: 0;
  padding: 0.2rem 0.5rem;
  border-radius: 0.3rem;
  background: color-mix(in srgb, var(--accent) 12%, transparent);
  color: var(--accent);
  font-family: ui-monospace, Menlo, Consolas, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.01em;
}

.rot-02__chip--warn {
  background: color-mix(in srgb, var(--ink) 8%, transparent);
  color: var(--muted);
}

.rot-02__art {
  position: relative;
  aspect-ratio: 4 / 3;
  border-radius: calc(var(--radius) - 0.25rem);
  background: linear-gradient(150deg, #e7dcc8 0%, #cbb99c 55%, #a89273 100%);
  overflow: hidden;
}

.rot-02__artmark {
  position: absolute;
  inset-block-end: 12%;
  inset-inline-start: 10%;
  inline-size: 32%;
  aspect-ratio: 1;
  border: 2px solid rgba(34, 28, 20, 0.55);
  border-radius: 50%;
}

.rot-02__artgrain {
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(115deg, rgba(255, 255, 255, 0.22) 0 1px, transparent 1px 7px);
}

.rot-02__cardh {
  margin: 0.2rem 0 0;
  font-family: var(--font-display);
  font-size: 1.125rem;
  font-weight: 400;
}

.rot-02__cardp {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.6;
  color: var(--muted);
  min-inline-size: 0;
}

.rot-02__foot {
  margin: 0.35rem 0 0;
  font-size: 0.75rem;
  letter-spacing: 0.02em;
  color: var(--accent);
}

.rot-02__foot--warn {
  color: var(--muted);
}

.rot-02__note {
  inline-size: min(100%, 38rem);
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.7;
  color: var(--muted);
  text-align: center;
  text-wrap: pretty;
}

@media (hover: hover) and (pointer: fine) {
  .rot-02__card--right:hover,
    .rot-02__card--right:focus-visible {
    transform: rotate(var(--tilt)) translateY(var(--lift));
    box-shadow: 0 18px 34px -20px rgba(34, 28, 20, 0.45);
  }

  .rot-02__card--wrong:hover,
    .rot-02__card--wrong:focus-visible {
    transform: rotate(calc(var(--tilt) * -1)) translateY(var(--lift));
    box-shadow: 0 18px 34px -20px rgba(34, 28, 20, 0.45);
    transition: transform 220ms var(--ease), box-shadow 220ms var(--ease);
  }
}

.rot-02__card:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
  .rot-02__card {
    transition: none;
  }

  .rot-02__card--right:hover,
    .rot-02__card--right:focus-visible,
    .rot-02__card--wrong:hover,
    .rot-02__card--wrong:focus-visible {
    transform: none;
    box-shadow: 0 0 0 2px var(--accent);
  }
}

.rot-02__theme {
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

.rot-02__themelegend {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-02__themeinput {
  position: absolute;
  inline-size: 1px;
  block-size: 1px;
  margin: 0;
  overflow: hidden;
  clip-path: inset(50%);
}

.rot-02__themeopt {
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

.rot-02__themeopt:hover {
  opacity: 0.85;
}

.rot-02__themeinput:checked + .rot-02__themeopt {
  opacity: 1;
  background: color-mix(in srgb, currentColor 15%, transparent);
}

.rot-02__themeinput:focus-visible + .rot-02__themeopt {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (forced-colors: active) {
  .rot-02__theme {
    border-color: CanvasText;
    background: Canvas;
  }

  .rot-02__themeinput:checked + .rot-02__themeopt {
    background: Highlight;
    color: HighlightText;
  }
}

@media (prefers-color-scheme: dark) {
  .rot-02:not(:has(#rot-02-theme-light:checked)) {
    --page: #141109;
    --surface: #1d1810;
    --ink: #f3ece0;
    --muted: #a89b86;
    --rule: #332b1f;
    --accent: #ff8f5e;
  }

  .rot-02:not(:has(#rot-02-theme-light:checked)) .rot-02__card {
    box-shadow: 0 1px 0 #2b2317;
  }

  .rot-02:not(:has(#rot-02-theme-light:checked)) .rot-02__art {
    background: linear-gradient(150deg, #4a3f2c 0%, #6b5a3f 55%, #2f2718 100%);
  }
}

@media (prefers-color-scheme: light) {
  .rot-02:has(#rot-02-theme-dark:checked) {
    --page: #141109;
    --surface: #1d1810;
    --ink: #f3ece0;
    --muted: #a89b86;
    --rule: #332b1f;
    --accent: #ff8f5e;
  }
}

[data-theme="dark"] .rot-02:not(:has(#rot-02-theme-light:checked)) {
  --page: #141109;
  --surface: #1d1810;
  --ink: #f3ece0;
  --muted: #a89b86;
  --rule: #332b1f;
  --accent: #ff8f5e;
}

[data-theme="dark"] .rot-02:not(:has(#rot-02-theme-light:checked)) .rot-02__art {
  background: linear-gradient(150deg, #4a3f2c 0%, #6b5a3f 55%, #2f2718 100%);
}

.rot-02:has(#rot-02-theme-dark:checked) {
  --page: #141109;
  --surface: #1d1810;
  --ink: #f3ece0;
  --muted: #a89b86;
  --rule: #332b1f;
  --accent: #ff8f5e;
}

.rot-02:has(#rot-02-theme-dark:checked) .rot-02__card {
  box-shadow: 0 1px 0 #2b2317;
}

.rot-02:has(#rot-02-theme-dark:checked) .rot-02__art {
  background: linear-gradient(150deg, #4a3f2c 0%, #6b5a3f 55%, #2f2718 100%);
}

.rot-02:has(#rot-02-theme-light:checked) {
  --page: #f4f1ea;
  --surface: #fffdf8;
  --ink: #221c14;
  --muted: #6d6355;
  --rule: #ded6c7;
  --accent: #c2542b;
}

.rot-02:has(#rot-02-theme-light:checked) .rot-02__art {
  background: linear-gradient(150deg, #e7dcc8 0%, #cbb99c 55%, #a89273 100%);
}
```
