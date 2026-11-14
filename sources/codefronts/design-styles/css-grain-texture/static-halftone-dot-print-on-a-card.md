---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/static-halftone-dot-print-on-a-card/"
title: "Static Halftone Dot Print on a Card"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "Halftone is how ink reproduces a continuous-tone photograph, and CSS can do it with one radial-gradient and one blend mode."
has_js: "false"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Static Halftone Dot Print on a Card
Source: https://codefronts.com/design-styles/css-grain-texture/static-halftone-dot-print-on-a-card/

Halftone is how ink reproduces a continuous-tone photograph, and CSS can do it with one radial-gradient and one blend mode. This is the newspaper treatment done properly: a dot screen at a real print angle, dot pitch scaled to the surface, and the contrast pre-boost that stops halftone turning everything to grey mush.
## HTML
```html
<section class="grn-14" aria-labelledby="grn-14-title">
  <div class="grn-14__theme">
    <input class="grn-14__theme-input" type="checkbox" id="grn-14-theme">
    <label class="grn-14__theme-label" for="grn-14-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-14__sr">Toggle dark theme</span>
    </label>
  </div>

  <main class="grn-14__shell">
    <header class="grn-14__masthead">
      <p class="grn-14__rule">Late edition · No. 214 · Printed on recycled stock</p>
      <h1 class="grn-14__h1" id="grn-14-title">The Dot Screen</h1>
      <p class="grn-14__lede">One <code>radial-gradient</code>, one blend mode, one contrast boost. Everything below is ink on paper as far as your eye is concerned.</p>
    </header>

    <article class="grn-14__lead">
      <div class="grn-14__plate grn-14__plate--duo">
        <img class="grn-14__img" src="https://picsum.photos/id/1005/1400/1000" alt="A portrait of a person looking away from the camera in strong daylight" loading="lazy" width="1400" height="1000">
        <span class="grn-14__screen grn-14__screen--k" aria-hidden="true"></span>
        <span class="grn-14__screen grn-14__screen--r" aria-hidden="true"></span>
      </div>
      <div class="grn-14__lead-copy">
        <p class="grn-14__tag">Two inks · screens at 15° and 75°</p>
        <h2 class="grn-14__h2">Duotone, the way two-ink presses actually work</h2>
        <p class="grn-14__body">A black screen at fifteen degrees, a red screen at seventy-five, and thirty degrees of separation so the two grids never beat against each other. The photograph underneath is pushed to contrast 1.6 and fully desaturated before either screen lands on it.</p>
        <dl class="grn-14__spec">
          <div><dt>Pitch</dt><dd>6px</dd></div>
          <div><dt>Angles</dt><dd>15° / 75°</dd></div>
          <div><dt>Contrast</dt><dd>1.6</dd></div>
        </dl>
      </div>
    </article>

    <ul class="grn-14__grid">
      <li class="grn-14__card">
        <div class="grn-14__plate" style="--grn-14-pitch: 4px">
          <img class="grn-14__img" src="https://picsum.photos/id/1074/900/1100" alt="A lion resting in dry grass" loading="lazy" width="900" height="1100">
          <span class="grn-14__screen grn-14__screen--k" aria-hidden="true"></span>
        </div>
        <h3 class="grn-14__card-h">Fine screen · 4px</h3>
        <p class="grn-14__card-b">Magazine pitch. Holds detail, reads as print rather than as pattern.</p>
      </li>
      <li class="grn-14__card">
        <div class="grn-14__plate" style="--grn-14-pitch: 7px">
          <img class="grn-14__img" src="https://picsum.photos/id/1080/900/1100" alt="A close-up of strawberries in a crate" loading="lazy" width="900" height="1100">
          <span class="grn-14__screen grn-14__screen--k" aria-hidden="true"></span>
        </div>
        <h3 class="grn-14__card-h">Newsprint · 7px</h3>
        <p class="grn-14__card-b">The default. Visibly a screen at reading distance, still legible as an image.</p>
      </li>
      <li class="grn-14__card">
        <div class="grn-14__plate" style="--grn-14-pitch: 11px">
          <img class="grn-14__img" src="https://picsum.photos/id/1084/900/1100" alt="A mountain lake surrounded by pines" loading="lazy" width="900" height="1100">
          <span class="grn-14__screen grn-14__screen--k" aria-hidden="true"></span>
        </div>
        <h3 class="grn-14__card-h">Pop · 11px</h3>
        <p class="grn-14__card-b">Coarse enough to become the subject. Use once per page, never behind type.</p>
      </li>
    </ul>
  </main>
</section>
```
## CSS
```css
.grn-14 {
  --grn-14-bg: #f2efe8;
  --grn-14-surf: #fbfaf6;
  --grn-14-ink: #14110e;
  --grn-14-mut: #5d574d;
  --grn-14-line: #d8d2c5;
  --grn-14-acc: #d2231f;
  --grn-14-acc: oklch(53% 0.21 28);
  --grn-14-pitch: 6px;
  --grn-14-angle: 15deg;
  --grn-14-dot: 1.15px;
  --grn-14-font-display: "Instrument Serif", "Playfair Display", Georgia, serif;
  --grn-14-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--grn-14-bg);
  color: var(--grn-14-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.grn-14 *,
.grn-14 *::before,
.grn-14 *::after {
  box-sizing: border-box;
}

.grn-14 :focus-visible {
  outline: 2px solid var(--grn-14-acc);
  outline-offset: 3px;
}

.grn-14 code {
  font-family: var(--grn-14-font-mono);
  font-size: 0.9em;
}

.grn-14__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
  border: 0;
}

.grn-14:has(.grn-14__theme-input:checked) {
  --grn-14-bg: #100e0c;
  --grn-14-surf: #191614;
  --grn-14-ink: #f4f1ea;
  --grn-14-mut: #a29a8c;
  --grn-14-line: #2e2823;
  --grn-14-acc: #ff6b5e;
  --grn-14-acc: oklch(74% 0.17 30);
}

@media (prefers-color-scheme: dark) {
  .grn-14 {
    --grn-14-bg: #100e0c;
    --grn-14-surf: #191614;
    --grn-14-ink: #f4f1ea;
    --grn-14-mut: #a29a8c;
    --grn-14-line: #2e2823;
    --grn-14-acc: #ff6b5e;
    --grn-14-acc: oklch(74% 0.17 30);
  }

  .grn-14:has(.grn-14__theme-input:checked) {
    --grn-14-bg: #f2efe8;
    --grn-14-surf: #fbfaf6;
    --grn-14-ink: #14110e;
    --grn-14-mut: #5d574d;
    --grn-14-line: #d8d2c5;
    --grn-14-acc: #d2231f;
    --grn-14-acc: oklch(53% 0.21 28);
  }
}

@media (prefers-color-scheme: light) {
  .grn-14:has(.grn-14__theme-input:checked) {
    --grn-14-bg: #100e0c;
    --grn-14-surf: #191614;
    --grn-14-ink: #f4f1ea;
    --grn-14-mut: #a29a8c;
    --grn-14-line: #2e2823;
    --grn-14-acc: #ff6b5e;
    --grn-14-acc: oklch(74% 0.17 30);
  }
}

.grn-14__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 40;
}

.grn-14__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-14__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--grn-14-line);
  border-radius: 999px;
  background: var(--grn-14-surf);
  color: var(--grn-14-ink);
  cursor: pointer;
}

.grn-14__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-14__shell {
  inline-size: min(78rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(2.5rem, 7vw, 4.5rem) clamp(2.5rem, 6vw, 4rem);
  display: grid;
  gap: clamp(2rem, 5vw, 3.2rem);
}

.grn-14__masthead {
  display: grid;
  gap: 0.5rem;
  padding-block-end: clamp(1rem, 3vw, 1.6rem);
  border-block-end: 3px double var(--grn-14-ink);
}

.grn-14__rule {
  margin: 0;
  font: 400 0.72rem/1 var(--grn-14-font-mono);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--grn-14-mut);
}

.grn-14__h1 {
  margin: 0;
  font: 400 clamp(2.8rem, 10vw, 6.5rem)/0.92 var(--grn-14-font-display);
  letter-spacing: -0.03em;
}

.grn-14__lede {
  margin: 0;
  max-inline-size: 40rem;
  color: var(--grn-14-mut);
  font-size: clamp(0.95rem, 1.9vw, 1.06rem);
  text-wrap: pretty;
}

.grn-14__plate {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  background: var(--grn-14-ink);
  aspect-ratio: 7 / 5;
}

.grn-14__img {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  filter: grayscale(1) contrast(1.6) brightness(1.06);
}

.grn-14__screen {
  position: absolute;
  inset: -30%;
  pointer-events: none;
  background-image: radial-gradient(circle at center, var(--grn-14-screen-col, #fff) 0 var(--grn-14-dot), transparent calc(var(--grn-14-dot) + 0.45px));
  background-size: var(--grn-14-pitch) var(--grn-14-pitch);
}

.grn-14__screen--k {
  --grn-14-screen-col: #ffffff;
  transform: rotate(var(--grn-14-angle));
  mix-blend-mode: screen;
  opacity: 0.92;
}

.grn-14__screen--r {
  --grn-14-screen-col: var(--grn-14-acc);
  transform: rotate(75deg);
  mix-blend-mode: lighten;
  opacity: 0.7;
}

.grn-14__lead {
  display: grid;
  gap: clamp(1.2rem, 3vw, 2.2rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 20rem), 1fr));
  align-items: start;
}

.grn-14__plate--duo {
  aspect-ratio: 7 / 5;
  border: 1px solid var(--grn-14-line);
}

.grn-14__lead-copy {
  display: grid;
  gap: 0.65rem;
  min-inline-size: 0;
}

.grn-14__tag {
  margin: 0;
  font: 500 0.7rem/1 var(--grn-14-font-mono);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--grn-14-acc);
}

.grn-14__h2 {
  margin: 0;
  font: 400 clamp(1.5rem, 4vw, 2.4rem)/1.08 var(--grn-14-font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.grn-14__body {
  margin: 0;
  max-inline-size: 34rem;
  color: var(--grn-14-mut);
  font-size: clamp(0.93rem, 1.9vw, 1.02rem);
  text-wrap: pretty;
}

.grn-14__spec {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem 1.6rem;
  margin: 0.3rem 0 0;
  padding-block-start: 0.8rem;
  border-block-start: 1px solid var(--grn-14-line);
}

.grn-14__spec > div {
  display: grid;
  gap: 0.1rem;
}

.grn-14__spec dt {
  margin: 0;
  font: 400 0.66rem/1 var(--grn-14-font-mono);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--grn-14-mut);
}

.grn-14__spec dd {
  margin: 0;
  font: 500 1rem/1 var(--grn-14-font-mono);
}

.grn-14__grid {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(1rem, 2.5vw, 1.6rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr));
}

.grn-14__card {
  display: grid;
  gap: 0.5rem;
  min-inline-size: 0;
}

.grn-14__card .grn-14__plate {
  aspect-ratio: 9 / 11;
  border: 1px solid var(--grn-14-line);
}

.grn-14__card-h {
  margin: 0.2rem 0 0;
  font: 400 1.15rem/1.15 var(--grn-14-font-display);
}

.grn-14__card-b {
  margin: 0;
  color: var(--grn-14-mut);
  font-size: 0.87rem;
  text-wrap: pretty;
}

@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 2dppx) {
  .grn-14 {
    --grn-14-pitch: 5px;
    --grn-14-dot: 0.95px;
  }
}

.grn-14__screen {
  transition: opacity 300ms ease;
}

@media (hover: hover) and (pointer: fine) {
  .grn-14__card:hover .grn-14__screen--k,
    .grn-14__lead:hover .grn-14__screen--k {
    opacity: 0.7;
  }
}

@media (prefers-reduced-motion: reduce) {
  .grn-14__screen {
    transition-duration: 1ms;
  }
}
```
