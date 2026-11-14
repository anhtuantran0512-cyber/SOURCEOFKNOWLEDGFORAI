---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/dithered-bayer-matrix-shading-effect/"
title: "Dithered Bayer Matrix Shading Effect"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "Ordered dithering — the 4×4 Bayer matrix that gave early Macintosh and Game Boy graphics their look — rebuilt in CSS as a tiled threshold map."
has_js: "false"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Dithered Bayer Matrix Shading Effect
Source: https://codefronts.com/design-styles/css-grain-texture/dithered-bayer-matrix-shading-effect/

Ordered dithering — the 4×4 Bayer matrix that gave early Macintosh and Game Boy graphics their look — rebuilt in CSS as a tiled threshold map. Combined with hard-light it turns any smooth gradient into stepped, pixel-honest shading, and it doubles as the most aggressive banding fix in this collection.
## HTML
```html
<section class="grn-15" aria-labelledby="grn-15-title">
  <div class="grn-15__theme">
    <input class="grn-15__theme-input" type="checkbox" id="grn-15-theme">
    <label class="grn-15__theme-label" for="grn-15-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-15__sr">Toggle dark theme</span>
    </label>
  </div>

  <main class="grn-15__shell">
    <header class="grn-15__head">
      <p class="grn-15__kicker">Ordered dither · 4×4 Bayer</p>
      <h1 class="grn-15__h1" id="grn-15-title">Thresholds, not noise</h1>
      <p class="grn-15__lede">Sixteen dispersed threshold values tiled at four pixels, blended in <code>hard-light</code>. The same maths that gave 1984 its shading, running as one CSS layer.</p>
    </header>

    <div class="grn-15__stage">
      <div class="grn-15__field">
        <span class="grn-15__dither" aria-hidden="true"></span>
        <div class="grn-15__field-copy">
          <p class="grn-15__badge">4×4 · 8 bands · hard-light</p>
          <h2 class="grn-15__h2">Sunset, quantised</h2>
          <p class="grn-15__field-b">A stepped gradient of eight flat bands. The matrix breaks each boundary into a dot pattern that your eye averages back into a smooth ramp.</p>
        </div>
      </div>
    </div>

    <section class="grn-15__matrices" aria-labelledby="grn-15-h-mx">
      <div class="grn-15__mx-head">
        <h2 class="grn-15__h2" id="grn-15-h-mx">Matrix size sets the era</h2>
        <p class="grn-15__note">Same source gradient, same blend mode, three matrices.</p>
      </div>
      <ul class="grn-15__mx-list">
        <li class="grn-15__mx">
          <span class="grn-15__swatch grn-15__swatch--m2" aria-hidden="true"></span>
          <b>2×2</b><span>Four levels. Early monochrome displays, chunky and unmistakable.</span>
        </li>
        <li class="grn-15__mx">
          <span class="grn-15__swatch grn-15__swatch--m4" aria-hidden="true"></span>
          <b>4×4</b><span>Sixteen levels. The classic Macintosh and Atari look, and the default here.</span>
        </li>
        <li class="grn-15__mx">
          <span class="grn-15__swatch grn-15__swatch--m8" aria-hidden="true"></span>
          <b>8×8</b><span>Sixty-four levels. Nearly continuous — use it as a texture, not a statement.</span>
        </li>
      </ul>
    </section>

    <section class="grn-15__photo-block" aria-labelledby="grn-15-h-photo">
      <h2 class="grn-15__h2" id="grn-15-h-photo">One-bit image treatment</h2>
      <div class="grn-15__photos">
        <figure class="grn-15__fig">
          <div class="grn-15__plate">
            <img class="grn-15__img" src="https://picsum.photos/id/1011/1000/1200" alt="A person sitting on a kayak on a still lake" loading="lazy" width="1000" height="1200">
            <span class="grn-15__dither" aria-hidden="true"></span>
          </div>
          <figcaption>grayscale(1) contrast(1.45) + 4×4</figcaption>
        </figure>
        <figure class="grn-15__fig">
          <div class="grn-15__plate">
            <img class="grn-15__img" src="https://picsum.photos/id/1024/1000/1200" alt="A bear standing in shallow water" loading="lazy" width="1000" height="1200">
            <span class="grn-15__dither grn-15__dither--coarse" aria-hidden="true"></span>
          </div>
          <figcaption>Same treatment at 8px tile</figcaption>
        </figure>
      </div>
    </section>
  </main>
</section>
```
## CSS
```css
.grn-15 {
  --grn-15-m4: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='4' height='4' shape-rendering='crispEdges'%3E%3Cg%3E%3Crect x='0' y='0' width='1' height='1' fill='%23000'/%3E%3Crect x='2' y='0' width='1' height='1' fill='%23606060'/%3E%3Crect x='1' y='2' width='1' height='1' fill='%23909090'/%3E%3Crect x='3' y='2' width='1' height='1' fill='%23303030'/%3E%3Crect x='2' y='1' width='1' height='1' fill='%23e0e0e0'/%3E%3Crect x='0' y='1' width='1' height='1' fill='%23a0a0a0'/%3E%3Crect x='3' y='3' width='1' height='1' fill='%23c0c0c0'/%3E%3Crect x='1' y='3' width='1' height='1' fill='%23505050'/%3E%3Crect x='1' y='1' width='1' height='1' fill='%23202020'/%3E%3Crect x='3' y='1' width='1' height='1' fill='%23808080'/%3E%3Crect x='0' y='3' width='1' height='1' fill='%23f0f0f0'/%3E%3Crect x='2' y='3' width='1' height='1' fill='%23707070'/%3E%3Crect x='3' y='0' width='1' height='1' fill='%23404040'/%3E%3Crect x='1' y='0' width='1' height='1' fill='%23b0b0b0'/%3E%3Crect x='0' y='2' width='1' height='1' fill='%23d0d0d0'/%3E%3Crect x='2' y='2' width='1' height='1' fill='%23101010'/%3E%3C/g%3E%3C/svg%3E");
  --grn-15-m2: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='2' height='2' shape-rendering='crispEdges'%3E%3Crect x='0' y='0' width='1' height='1' fill='%23000'/%3E%3Crect x='1' y='0' width='1' height='1' fill='%23aaa'/%3E%3Crect x='1' y='1' width='1' height='1' fill='%23555'/%3E%3Crect x='0' y='1' width='1' height='1' fill='%23fff'/%3E%3C/svg%3E");
  --grn-15-m8: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='8' height='8'%3E%3Cfilter id='grn15d'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.5' numOctaves='1' seed='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3CfeComponentTransfer%3E%3CfeFuncR type='discrete' tableValues='0 0.14 0.28 0.42 0.57 0.71 0.85 1'/%3E%3CfeFuncG type='discrete' tableValues='0 0.14 0.28 0.42 0.57 0.71 0.85 1'/%3E%3CfeFuncB type='discrete' tableValues='0 0.14 0.28 0.42 0.57 0.71 0.85 1'/%3E%3C/feComponentTransfer%3E%3C/filter%3E%3Crect width='8' height='8' filter='url(%23grn15d)'/%3E%3C/svg%3E");
  --grn-15-matrix: var(--grn-15-m4);
  --grn-15-bg: #05070f;
  --grn-15-surf: #0c1120;
  --grn-15-line: #1d2740;
  --grn-15-ink: #e8eeff;
  --grn-15-mut: #8f9dc0;
  --grn-15-acc: #38bdf8;
  --grn-15-acc: oklch(76% 0.14 232);
  --grn-15-acc2: #fb7185;
  --grn-15-acc2: oklch(72% 0.17 15);
  --grn-15-font-display: "Space Grotesk", "Inter Tight", ui-sans-serif, system-ui, sans-serif;
  --grn-15-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--grn-15-bg);
  color: var(--grn-15-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.grn-15 *,
.grn-15 *::before,
.grn-15 *::after {
  box-sizing: border-box;
}

.grn-15 :focus-visible {
  outline: 2px solid var(--grn-15-acc);
  outline-offset: 3px;
}

.grn-15 code {
  font-family: var(--grn-15-font-mono);
  font-size: 0.9em;
}

.grn-15__sr {
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

.grn-15:has(.grn-15__theme-input:checked) {
  --grn-15-bg: #eef1f8;
  --grn-15-surf: #ffffff;
  --grn-15-line: #d5dced;
  --grn-15-ink: #05070f;
  --grn-15-mut: #556180;
  --grn-15-acc: #0369a1;
  --grn-15-acc: oklch(48% 0.11 235);
  --grn-15-acc2: #be123c;
  --grn-15-acc2: oklch(50% 0.19 16);
}

@media (prefers-color-scheme: light) {
  .grn-15 {
    --grn-15-bg: #eef1f8;
    --grn-15-surf: #ffffff;
    --grn-15-line: #d5dced;
    --grn-15-ink: #05070f;
    --grn-15-mut: #556180;
    --grn-15-acc: #0369a1;
    --grn-15-acc: oklch(48% 0.11 235);
    --grn-15-acc2: #be123c;
    --grn-15-acc2: oklch(50% 0.19 16);
  }

  .grn-15:has(.grn-15__theme-input:checked) {
    --grn-15-bg: #05070f;
    --grn-15-surf: #0c1120;
    --grn-15-line: #1d2740;
    --grn-15-ink: #e8eeff;
    --grn-15-mut: #8f9dc0;
    --grn-15-acc: #38bdf8;
    --grn-15-acc: oklch(76% 0.14 232);
    --grn-15-acc2: #fb7185;
    --grn-15-acc2: oklch(72% 0.17 15);
  }
}

@media (prefers-color-scheme: dark) {
  .grn-15:has(.grn-15__theme-input:checked) {
    --grn-15-bg: #eef1f8;
    --grn-15-surf: #ffffff;
    --grn-15-line: #d5dced;
    --grn-15-ink: #05070f;
    --grn-15-mut: #556180;
    --grn-15-acc: #0369a1;
    --grn-15-acc: oklch(48% 0.11 235);
    --grn-15-acc2: #be123c;
    --grn-15-acc2: oklch(50% 0.19 16);
  }
}

.grn-15__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 40;
}

.grn-15__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-15__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--grn-15-line);
  border-radius: 4px;
  background: var(--grn-15-surf);
  color: var(--grn-15-ink);
  cursor: pointer;
}

.grn-15__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-15__shell {
  inline-size: min(74rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(3rem, 8vw, 5rem) clamp(2.5rem, 6vw, 4rem);
  display: grid;
  gap: clamp(2rem, 5vw, 3rem);
}

.grn-15__head {
  max-inline-size: 44rem;
  display: grid;
  gap: 0.6rem;
}

.grn-15__kicker {
  margin: 0;
  font: 500 0.72rem/1 var(--grn-15-font-mono);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--grn-15-acc);
}

.grn-15__h1 {
  margin: 0;
  font: 600 clamp(2rem, 5.4vw, 3.4rem)/1.02 var(--grn-15-font-display);
  letter-spacing: -0.04em;
  text-wrap: balance;
}

.grn-15__lede {
  margin: 0;
  max-inline-size: 38rem;
  color: var(--grn-15-mut);
  font-size: clamp(0.95rem, 1.9vw, 1.07rem);
  text-wrap: pretty;
}

.grn-15__dither {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image: var(--grn-15-matrix);
  background-size: 4px 4px;
  background-repeat: repeat;
  image-rendering: pixelated;
  image-rendering: crisp-edges;
  mix-blend-mode: hard-light;
  opacity: 0.55;
}

.grn-15__dither--coarse {
  background-size: 8px 8px;
}

.grn-15__stage {
  display: grid;
}

.grn-15__field {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: grid;
  align-items: end;
  min-block-size: clamp(16rem, 42vw, 26rem);
  border: 1px solid var(--grn-15-line);
  border-radius: 6px;
  background-image: linear-gradient(172deg, var(--grn-15-acc2) 0% 12%, color-mix(in oklab, var(--grn-15-acc2) 70%, var(--grn-15-acc)) 12% 26%, color-mix(in oklab, var(--grn-15-acc2) 45%, var(--grn-15-acc)) 26% 40%, color-mix(in oklab, var(--grn-15-acc) 70%, var(--grn-15-acc2)) 40% 54%, var(--grn-15-acc) 54% 68%, color-mix(in oklab, var(--grn-15-acc) 60%, var(--grn-15-bg)) 68% 82%, color-mix(in oklab, var(--grn-15-acc) 25%, var(--grn-15-bg)) 82% 92%, var(--grn-15-bg) 92% 100%);
}

.grn-15__field-copy {
  position: relative;
  z-index: 2;
  display: grid;
  gap: 0.5rem;
  max-inline-size: 34rem;
  padding: clamp(1.2rem, 3.4vw, 2.2rem);
  color: #f4f8ff;
}

.grn-15__badge {
  margin: 0;
  justify-self: start;
  padding: 0.25rem 0.6rem;
  border-radius: 4px;
  background: rgba(4, 8, 18, 0.6);
  font: 500 0.7rem/1.5 var(--grn-15-font-mono);
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.grn-15__h2 {
  margin: 0;
  font: 600 clamp(1.3rem, 3.4vw, 1.9rem)/1.1 var(--grn-15-font-display);
  letter-spacing: -0.03em;
}

.grn-15__field-b {
  margin: 0;
  max-inline-size: 32rem;
  font-size: 0.93rem;
  color: rgba(244, 248, 255, 0.86);
  text-wrap: pretty;
}

.grn-15__note {
  margin: 0;
  color: var(--grn-15-mut);
  font-size: 0.87rem;
}

.grn-15__matrices {
  display: grid;
  gap: 1rem;
}

.grn-15__mx-head {
  display: grid;
  gap: 0.3rem;
  padding-block-end: 0.7rem;
  border-block-end: 1px solid var(--grn-15-line);
}

.grn-15__mx-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(0.8rem, 2vw, 1.3rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 14rem), 1fr));
}

.grn-15__mx {
  display: grid;
  gap: 0.35rem;
  min-inline-size: 0;
}

.grn-15__mx b {
  font: 600 0.95rem/1 var(--grn-15-font-mono);
}

.grn-15__mx span:last-child {
  color: var(--grn-15-mut);
  font-size: 0.85rem;
  text-wrap: pretty;
}

.grn-15__swatch {
  position: relative;
  isolation: isolate;
  display: block;
  block-size: clamp(7rem, 16vw, 10rem);
  border: 1px solid var(--grn-15-line);
  border-radius: 6px;
  overflow: hidden;
  background-image: linear-gradient(160deg, var(--grn-15-acc) 0% 20%, color-mix(in oklab, var(--grn-15-acc) 60%, var(--grn-15-bg)) 20% 45%, color-mix(in oklab, var(--grn-15-acc) 30%, var(--grn-15-bg)) 45% 72%, var(--grn-15-bg) 72% 100%);
}

.grn-15__swatch::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  image-rendering: pixelated;
  mix-blend-mode: hard-light;
  opacity: 0.6;
}

.grn-15__swatch--m2::after {
  background-image: var(--grn-15-m2);
  background-size: 4px 4px;
}

.grn-15__swatch--m4::after {
  background-image: var(--grn-15-m4);
  background-size: 4px 4px;
}

.grn-15__swatch--m8::after {
  background-image: var(--grn-15-m8);
  background-size: 8px 8px;
}

.grn-15__photo-block {
  display: grid;
  gap: 1rem;
}

.grn-15__photos {
  display: grid;
  gap: clamp(0.8rem, 2vw, 1.3rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr));
}

.grn-15__fig {
  margin: 0;
  display: grid;
  gap: 0.4rem;
  min-inline-size: 0;
}

.grn-15__fig figcaption {
  color: var(--grn-15-mut);
  font: 400 0.78rem/1.4 var(--grn-15-font-mono);
}

.grn-15__plate {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  aspect-ratio: 5 / 6;
  border: 1px solid var(--grn-15-line);
  border-radius: 6px;
  background: var(--grn-15-surf);
}

.grn-15__img {
  position: absolute;
  inset: 0;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  filter: grayscale(1) contrast(1.45) brightness(1.02);
}

.grn-15__swatch,
.grn-15__plate {
  transition: transform 280ms cubic-bezier(0.22, 1, 0.36, 1);
}

@media (hover: hover) and (pointer: fine) {
  .grn-15__mx:hover .grn-15__swatch,
    .grn-15__fig:hover .grn-15__plate {
    transform: translateY(-3px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .grn-15__swatch,
    .grn-15__plate {
    transition-duration: 1ms;
    transform: none;
  }
}
```
