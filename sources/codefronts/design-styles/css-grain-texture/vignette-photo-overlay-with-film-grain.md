---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/vignette-photo-overlay-with-film-grain/"
title: "Vignette Photo Overlay with Film Grain"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "The darkroom treatment, in CSS: a radial vignette to pull the eye inward, film grain composited in luminosity so it never shifts the photo's colour, and a…"
has_js: "false"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Vignette Photo Overlay with Film Grain
Source: https://codefronts.com/design-styles/css-grain-texture/vignette-photo-overlay-with-film-grain/

The darkroom treatment, in CSS: a radial vignette to pull the eye inward, film grain composited in luminosity so it never shifts the photo's colour, and a print-style caption plate. Three photos, three grain weights, and the layer order that makes the difference between "treated" and "filtered".
## HTML
```html
<section class="grn-08" aria-labelledby="grn-08-title">
  <div class="grn-08__theme">
    <input class="grn-08__theme-input" type="checkbox" id="grn-08-theme">
    <label class="grn-08__theme-label" for="grn-08-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-08__sr">Toggle dark theme</span>
    </label>
  </div>

  <main class="grn-08__shell">
    <header class="grn-08__head">
      <p class="grn-08__kicker">Roll 04 · 400 ISO · pushed one stop</p>
      <h1 class="grn-08__h1" id="grn-08-title">Contact sheet</h1>
      <p class="grn-08__lede">Vignette below the grain, grain in <code>luminosity</code>, weight set per frame. No filters, no canvas, no image processing — four layers of CSS over an ordinary <code>&lt;img&gt;</code>.</p>
    </header>

    <div class="grn-08__sheet">
      <figure class="grn-08__frame" style="--grn-08-weight: 0.13">
        <div class="grn-08__plate">
          <img class="grn-08__img" src="https://picsum.photos/id/1015/1200/1500" alt="A river running between steep rock walls under an overcast sky" loading="lazy" width="1200" height="1500">
          <span class="grn-08__vignette" aria-hidden="true"></span>
          <span class="grn-08__grain" aria-hidden="true"></span>
        </div>
        <figcaption class="grn-08__cap">
          <b>01 · Gorge</b>
          <span>Bright, flat frame. Grain pushed to 0.13 to give the sky some tooth.</span>
        </figcaption>
      </figure>

      <figure class="grn-08__frame grn-08__frame--wide" style="--grn-08-weight: 0.07">
        <div class="grn-08__plate">
          <img class="grn-08__img" src="https://picsum.photos/id/1039/1600/1000" alt="A waterfall seen from above, surrounded by dense forest" loading="lazy" width="1600" height="1000">
          <span class="grn-08__vignette" aria-hidden="true"></span>
          <span class="grn-08__grain" aria-hidden="true"></span>
        </div>
        <figcaption class="grn-08__cap">
          <b>02 · Falls</b>
          <span>Dark and contrasty. Grain held at 0.07 — any more and the shadows turn to mud.</span>
        </figcaption>
      </figure>

      <figure class="grn-08__frame" style="--grn-08-weight: 0.1">
        <div class="grn-08__plate">
          <img class="grn-08__img" src="https://picsum.photos/id/1043/1200/1500" alt="A person standing on a rock outcrop looking across a valley" loading="lazy" width="1200" height="1500">
          <span class="grn-08__vignette" aria-hidden="true"></span>
          <span class="grn-08__grain" aria-hidden="true"></span>
        </div>
        <figcaption class="grn-08__cap">
          <b>03 · Outcrop</b>
          <span>Falloff kept outside the figure so the vignette reads as lens, not retouching.</span>
        </figcaption>
      </figure>
    </div>

    <aside class="grn-08__order">
      <h2 class="grn-08__h2">Layer order, bottom to top</h2>
      <ol class="grn-08__stack">
        <li><b>Photograph</b><span>object-fit: cover, aspect-ratio declared</span></li>
        <li><b>Vignette</b><span>radial-gradient, transparent to 45%</span></li>
        <li><b>Grain</b><span>mix-blend-mode: luminosity — above the vignette</span></li>
        <li><b>Caption plate</b><span>own backdrop, always legible</span></li>
      </ol>
    </aside>
  </main>
</section>
```
## CSS
```css
.grn-08 {
  --grn-08-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='170' height='170'%3E%3Cfilter id='grn08n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.82' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='170' height='170' filter='url(%23grn08n)'/%3E%3C/svg%3E");
  --grn-08-noise-fine: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='170' height='170'%3E%3Cfilter id='grn08f'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='1.25' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='170' height='170' filter='url(%23grn08f)'/%3E%3C/svg%3E");
  --grn-08-bg: #0a0a0b;
  --grn-08-surf: #141416;
  --grn-08-line: #262629;
  --grn-08-ink: #f0efec;
  --grn-08-mut: #97948d;
  --grn-08-acc: #e8b84b;
  --grn-08-acc: oklch(80% 0.13 85);
  --grn-08-weight: 0.1;
  --grn-08-font-display: "Instrument Serif", "Playfair Display", Georgia, serif;
  --grn-08-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--grn-08-bg);
  color: var(--grn-08-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.grn-08 *,
.grn-08 *::before,
.grn-08 *::after {
  box-sizing: border-box;
}

.grn-08 :focus-visible {
  outline: 2px solid var(--grn-08-acc);
  outline-offset: 3px;
}

.grn-08 code {
  font-family: var(--grn-08-font-mono);
  font-size: 0.9em;
}

.grn-08__sr {
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

.grn-08:has(.grn-08__theme-input:checked) {
  --grn-08-bg: #f2f0ec;
  --grn-08-surf: #ffffff;
  --grn-08-line: #ded9d1;
  --grn-08-ink: #0a0a0b;
  --grn-08-mut: #635f58;
  --grn-08-acc: #9a6b12;
  --grn-08-acc: oklch(55% 0.11 78);
}

@media (prefers-color-scheme: light) {
  .grn-08 {
    --grn-08-bg: #f2f0ec;
    --grn-08-surf: #ffffff;
    --grn-08-line: #ded9d1;
    --grn-08-ink: #0a0a0b;
    --grn-08-mut: #635f58;
    --grn-08-acc: #9a6b12;
    --grn-08-acc: oklch(55% 0.11 78);
  }

  .grn-08:has(.grn-08__theme-input:checked) {
    --grn-08-bg: #0a0a0b;
    --grn-08-surf: #141416;
    --grn-08-line: #262629;
    --grn-08-ink: #f0efec;
    --grn-08-mut: #97948d;
    --grn-08-acc: #e8b84b;
    --grn-08-acc: oklch(80% 0.13 85);
  }
}

@media (prefers-color-scheme: dark) {
  .grn-08:has(.grn-08__theme-input:checked) {
    --grn-08-bg: #f2f0ec;
    --grn-08-surf: #ffffff;
    --grn-08-line: #ded9d1;
    --grn-08-ink: #0a0a0b;
    --grn-08-mut: #635f58;
    --grn-08-acc: #9a6b12;
    --grn-08-acc: oklch(55% 0.11 78);
  }
}

.grn-08__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 40;
}

.grn-08__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-08__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--grn-08-line);
  border-radius: 999px;
  background: var(--grn-08-surf);
  color: var(--grn-08-ink);
  cursor: pointer;
}

.grn-08__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-08__theme-input:focus-visible + .grn-08__theme-label {
  outline: 2px solid var(--grn-08-acc);
  outline-offset: 3px;
}

.grn-08__shell {
  inline-size: min(78rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(3rem, 8vw, 5.5rem) clamp(2.5rem, 6vw, 4rem);
  display: grid;
  gap: clamp(2rem, 5vw, 3.2rem);
}

.grn-08__head {
  max-inline-size: 46rem;
  display: grid;
  gap: 0.6rem;
}

.grn-08__kicker {
  margin: 0;
  font: 400 0.74rem/1 var(--grn-08-font-mono);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--grn-08-acc);
}

.grn-08__h1 {
  margin: 0;
  font: 400 clamp(2.6rem, 8vw, 5rem)/0.95 var(--grn-08-font-display);
  letter-spacing: -0.02em;
}

.grn-08__lede {
  margin: 0;
  max-inline-size: 38rem;
  color: var(--grn-08-mut);
  font-size: clamp(0.95rem, 1.9vw, 1.08rem);
  text-wrap: pretty;
}

.grn-08__sheet {
  display: grid;
  gap: clamp(1rem, 2.5vw, 1.6rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
  align-items: start;
}

.grn-08__frame {
  margin: 0;
  display: grid;
  gap: 0.7rem;
  min-inline-size: 0;
}

.grn-08__frame--wide {
  grid-column: span 1;
}

@media (min-width: 60rem) {
  .grn-08__frame--wide {
    grid-column: span 1;
  }
}

.grn-08__plate {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  border-radius: 4px;
  aspect-ratio: 4 / 5;
  background: #101012;
}

.grn-08__frame--wide .grn-08__plate {
  aspect-ratio: 4 / 5;
}

.grn-08__img {
  position: absolute;
  inset: 0;
  z-index: 0;
  inline-size: 100%;
  block-size: 100%;
  object-fit: cover;
  display: block;
  filter: contrast(1.04) saturate(0.94);
}

.grn-08__vignette {
  position: absolute;
  inset: 0;
  z-index: 1;
  pointer-events: none;
  background: radial-gradient(120% 100% at 50% 46%, transparent 45%, rgba(6, 5, 8, 0.24) 76%, rgba(6, 5, 8, 0.44) 100%);
}

.grn-08__grain {
  position: absolute;
  inset: 0;
  z-index: 2;
  pointer-events: none;
  background-image: var(--grn-08-noise);
  opacity: var(--grn-08-weight);
  mix-blend-mode: luminosity;
}

@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 2dppx) {
  .grn-08__grain {
    background-image: var(--grn-08-noise-fine);
    opacity: calc(var(--grn-08-weight) * 1.15);
  }
}

.grn-08__cap {
  display: grid;
  gap: 0.2rem;
}

.grn-08__cap b {
  font: 500 0.9rem/1.2 var(--grn-08-font-mono);
  letter-spacing: 0.04em;
}

.grn-08__cap span {
  color: var(--grn-08-mut);
  font-size: 0.85rem;
  text-wrap: pretty;
}

.grn-08__order {
  display: grid;
  gap: 0.9rem;
  padding: clamp(1.2rem, 3vw, 1.9rem);
  border: 1px solid var(--grn-08-line);
  border-radius: 14px;
  background: var(--grn-08-surf);
}

.grn-08__h2 {
  margin: 0;
  font: 400 clamp(1.3rem, 3vw, 1.7rem)/1.15 var(--grn-08-font-display);
}

.grn-08__stack {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0.1rem;
  counter-reset: grn08;
}

.grn-08__stack li {
  display: grid;
  grid-template-columns: 1.6rem minmax(0, 1fr);
  gap: 0.15rem 0.6rem;
  padding-block: 0.55rem;
  border-block-start: 1px solid var(--grn-08-line);
  counter-increment: grn08;
}

.grn-08__stack li::before {
  content: counter(grn08);
  grid-row: span 2;
  font: 400 0.8rem/1.6 var(--grn-08-font-mono);
  color: var(--grn-08-acc);
}

.grn-08__stack b {
  font-weight: 600;
  font-size: 0.92rem;
}

.grn-08__stack span {
  color: var(--grn-08-mut);
  font: 400 0.8rem/1.4 var(--grn-08-font-mono);
}

.grn-08__plate {
  transition: transform 420ms cubic-bezier(0.22, 1, 0.36, 1);
}

.grn-08__img {
  transition: scale 620ms cubic-bezier(0.22, 1, 0.36, 1);
}

@media (hover: hover) and (pointer: fine) {
  .grn-08__frame:hover .grn-08__img {
    scale: 1.035;
  }

  .grn-08__frame:hover .grn-08__grain {
    opacity: calc(var(--grn-08-weight) * 1.25);
  }
}

.grn-08__grain {
  transition: opacity 300ms ease;
}

@media (prefers-reduced-motion: reduce) {
  .grn-08__plate,
    .grn-08__img,
    .grn-08__grain {
    transition-duration: 1ms;
  }

  .grn-08__frame:hover .grn-08__img {
    scale: 1;
  }
}
```
