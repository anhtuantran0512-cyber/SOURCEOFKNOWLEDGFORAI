---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/tinting-svg-noise-with-fecolormatrix/"
title: "Tinting SVG Noise with feColorMatrix"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "Raw feTurbulence writes independent noise into red, green and blue, so untinted grain is colour confetti."
has_js: "false"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tinting SVG Noise with feColorMatrix
Source: https://codefronts.com/design-styles/css-grain-texture/tinting-svg-noise-with-fecolormatrix/

Raw feTurbulence writes independent noise into red, green and blue, so untinted grain is colour confetti. feColorMatrix fixes that properly: flatten the RGB to a constant tint and drive the alpha channel from the noise luminance. The result is single-hue grain you can colour like any other design token — shown here as six named film stocks.
## HTML
```html
<section class="grn-05" aria-labelledby="grn-05-title">
  <svg class="grn-05__defs" width="0" height="0" aria-hidden="true" focusable="false">
    <filter id="grn-05-amber" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" seed="12" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.98  0 0 0 0 0.66  0 0 0 0 0.19  0.33 0.33 0.33 0 0"/>
      <feComponentTransfer><feFuncA type="table" tableValues="0 0.35 0.9"/></feComponentTransfer>
    </filter>
    <filter id="grn-05-cyan" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" seed="5" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.13  0 0 0 0 0.78  0 0 0 0 0.85  0.33 0.33 0.33 0 0"/>
      <feComponentTransfer><feFuncA type="table" tableValues="0 0.3 0.85"/></feComponentTransfer>
    </filter>
    <filter id="grn-05-magenta" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.7" numOctaves="4" seed="19" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.86  0 0 0 0 0.12  0 0 0 0 0.55  0.33 0.33 0.33 0 0"/>
      <feComponentTransfer><feFuncA type="table" tableValues="0 0.4 1"/></feComponentTransfer>
    </filter>
    <filter id="grn-05-neutral" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" seed="31" stitchTiles="stitch"/>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
    <filter id="grn-05-olive" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
      <feTurbulence type="turbulence" baseFrequency="0.45" numOctaves="2" seed="8" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.55  0 0 0 0 0.62  0 0 0 0 0.24  0.33 0.33 0.33 0 0"/>
      <feComponentTransfer><feFuncA type="table" tableValues="0 0.28 0.7"/></feComponentTransfer>
    </filter>
    <filter id="grn-05-ink" x="0" y="0" width="100%" height="100%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="1.1" numOctaves="2" seed="44" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0.05  0 0 0 0 0.06  0 0 0 0 0.09  0.33 0.33 0.33 0 0"/>
      <feComponentTransfer><feFuncA type="table" tableValues="0 0.5 1"/></feComponentTransfer>
    </filter>
  </svg>

  <div class="grn-05__theme">
    <input class="grn-05__theme-input" type="checkbox" id="grn-05-theme">
    <label class="grn-05__theme-label" for="grn-05-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-05__sr">Toggle dark theme</span>
    </label>
  </div>

  <main class="grn-05__shell">
    <header class="grn-05__head">
      <p class="grn-05__kicker">Stock library · 05</p>
      <h1 class="grn-05__h1" id="grn-05-title">Tinted grain, one hue, no confetti</h1>
      <p class="grn-05__lede">Six filter chains. Each flattens the noise to a single tint with <code>feColorMatrix</code> and moves the texture into the alpha channel, so the grain composites in <code>normal</code> blend mode over anything.</p>
    </header>

    <ul class="grn-05__stocks">
      <li class="grn-05__stock">
        <div class="grn-05__frame grn-05__frame--amber" role="img" aria-label="Warm amber tinted grain over a magenta and teal gradient"></div>
        <div class="grn-05__body">
          <div class="grn-05__row"><h2 class="grn-05__name">Amber 400</h2><span class="grn-05__code">warm</span></div>
          <p class="grn-05__desc">Tungsten-balanced press texture. Reads as paper warmth on cream surfaces.</p>
          <code class="grn-05__matrix">0.98 0.66 0.19</code>
        </div>
      </li>
      <li class="grn-05__stock">
        <div class="grn-05__frame grn-05__frame--cyan" role="img" aria-label="Cool cyan tinted grain over a magenta and teal gradient"></div>
        <div class="grn-05__body">
          <div class="grn-05__row"><h2 class="grn-05__name">Cyan 200</h2><span class="grn-05__code">cool</span></div>
          <p class="grn-05__desc">Daylight stock. The safest tint for dark product UI — it lifts without yellowing.</p>
          <code class="grn-05__matrix">0.13 0.78 0.85</code>
        </div>
      </li>
      <li class="grn-05__stock">
        <div class="grn-05__frame grn-05__frame--magenta" role="img" aria-label="Hot magenta tinted grain over a magenta and teal gradient"></div>
        <div class="grn-05__body">
          <div class="grn-05__row"><h2 class="grn-05__name">Magenta 700</h2><span class="grn-05__code">hot</span></div>
          <p class="grn-05__desc">Four octaves and a hard alpha table. Editorial covers, not settings screens.</p>
          <code class="grn-05__matrix">0.86 0.12 0.55</code>
        </div>
      </li>
      <li class="grn-05__stock">
        <div class="grn-05__frame grn-05__frame--neutral" role="img" aria-label="Neutral grey grain over a magenta and teal gradient"></div>
        <div class="grn-05__body">
          <div class="grn-05__row"><h2 class="grn-05__name">Neutral</h2><span class="grn-05__code">saturate 0</span></div>
          <p class="grn-05__desc">The one-line version. No tint, no alpha shaping, correct for 90% of interfaces.</p>
          <code class="grn-05__matrix">saturate · 0</code>
        </div>
      </li>
      <li class="grn-05__stock">
        <div class="grn-05__frame grn-05__frame--olive" role="img" aria-label="Olive veined turbulence over a magenta and teal gradient"></div>
        <div class="grn-05__body">
          <div class="grn-05__row"><h2 class="grn-05__name">Olive Veil</h2><span class="grn-05__code">turbulence</span></div>
          <p class="grn-05__desc">Low-frequency turbulence, soft alpha table. Cloth and clay surfaces.</p>
          <code class="grn-05__matrix">0.55 0.62 0.24</code>
        </div>
      </li>
      <li class="grn-05__stock">
        <div class="grn-05__frame grn-05__frame--ink" role="img" aria-label="Near-black ink grain over a magenta and teal gradient"></div>
        <div class="grn-05__body">
          <div class="grn-05__row"><h2 class="grn-05__name">Ink 950</h2><span class="grn-05__code">dense</span></div>
          <p class="grn-05__desc">High frequency, full alpha range. The only stock that survives on white.</p>
          <code class="grn-05__matrix">0.05 0.06 0.09</code>
        </div>
      </li>
    </ul>

    <aside class="grn-05__why">
      <h2 class="grn-05__h2">Why the alpha row matters</h2>
      <p class="grn-05__why-body">The alpha row <code>0.33 0.33 0.33 0 0</code> computes coverage from the incoming luminance. Without it, zeroed RGB rows paint a solid rectangle of flat tint — the most common way this chain fails. With it, the noise decides where the tint lands, the hue never varies, and the layer needs no blend mode at all.</p>
    </aside>
  </main>
</section>
```
## CSS
```css
.grn-05 {
  --grn-05-bg: #12060f;
  --grn-05-surf: #1e0c19;
  --grn-05-line: #3a1830;
  --grn-05-ink: #fdeaf7;
  --grn-05-mut: #c093b3;
  --grn-05-acc: #f472b6;
  --grn-05-acc: oklch(72% 0.19 350);
  --grn-05-acc2: #2dd4bf;
  --grn-05-acc2: oklch(78% 0.13 180);
  --grn-05-grain: 0.7;
  --grn-05-font-display: "Space Grotesk", "Inter Tight", ui-sans-serif, system-ui, sans-serif;
  --grn-05-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--grn-05-bg);
  color: var(--grn-05-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.grn-05 *,
.grn-05 *::before,
.grn-05 *::after {
  box-sizing: border-box;
}

.grn-05 :focus-visible {
  outline: 2px solid var(--grn-05-acc);
  outline-offset: 3px;
}

.grn-05 code {
  font-family: var(--grn-05-font-mono);
  font-size: 0.9em;
}

.grn-05__sr {
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

.grn-05__defs {
  position: absolute;
  width: 0;
  height: 0;
  overflow: hidden;
}

.grn-05:has(.grn-05__theme-input:checked) {
  --grn-05-bg: #fdf2f9;
  --grn-05-surf: #ffffff;
  --grn-05-line: #f2d6e8;
  --grn-05-ink: #17070f;
  --grn-05-mut: #7c5169;
  --grn-05-acc: #be185d;
  --grn-05-acc: oklch(50% 0.19 355);
  --grn-05-acc2: #0d9488;
  --grn-05-acc2: oklch(58% 0.11 182);
  --grn-05-grain: 0.5;
}

@media (prefers-color-scheme: light) {
  .grn-05 {
    --grn-05-bg: #fdf2f9;
    --grn-05-surf: #ffffff;
    --grn-05-line: #f2d6e8;
    --grn-05-ink: #17070f;
    --grn-05-mut: #7c5169;
    --grn-05-acc: #be185d;
    --grn-05-acc: oklch(50% 0.19 355);
    --grn-05-acc2: #0d9488;
    --grn-05-acc2: oklch(58% 0.11 182);
    --grn-05-grain: 0.5;
  }

  .grn-05:has(.grn-05__theme-input:checked) {
    --grn-05-bg: #12060f;
    --grn-05-surf: #1e0c19;
    --grn-05-line: #3a1830;
    --grn-05-ink: #fdeaf7;
    --grn-05-mut: #c093b3;
    --grn-05-acc: #f472b6;
    --grn-05-acc: oklch(72% 0.19 350);
    --grn-05-acc2: #2dd4bf;
    --grn-05-acc2: oklch(78% 0.13 180);
    --grn-05-grain: 0.7;
  }
}

@media (prefers-color-scheme: dark) {
  .grn-05:has(.grn-05__theme-input:checked) {
    --grn-05-bg: #fdf2f9;
    --grn-05-surf: #ffffff;
    --grn-05-line: #f2d6e8;
    --grn-05-ink: #17070f;
    --grn-05-mut: #7c5169;
    --grn-05-acc: #be185d;
    --grn-05-acc: oklch(50% 0.19 355);
    --grn-05-acc2: #0d9488;
    --grn-05-acc2: oklch(58% 0.11 182);
    --grn-05-grain: 0.5;
  }
}

.grn-05__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 40;
}

.grn-05__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-05__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--grn-05-line);
  border-radius: 999px;
  background: var(--grn-05-surf);
  color: var(--grn-05-ink);
  cursor: pointer;
}

.grn-05__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-05__theme-input:focus-visible + .grn-05__theme-label {
  outline: 2px solid var(--grn-05-acc);
  outline-offset: 3px;
}

.grn-05__shell {
  inline-size: min(78rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(3rem, 8vw, 5.5rem) clamp(2.5rem, 6vw, 4rem);
  display: grid;
  gap: clamp(2rem, 5vw, 3.2rem);
}

.grn-05__head {
  max-inline-size: 46rem;
  display: grid;
  gap: 0.7rem;
}

.grn-05__kicker {
  margin: 0;
  font: 500 0.72rem/1 var(--grn-05-font-mono);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--grn-05-acc);
}

.grn-05__h1 {
  margin: 0;
  font: 600 clamp(2rem, 5.4vw, 3.5rem)/1.03 var(--grn-05-font-display);
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.grn-05__lede {
  margin: 0;
  max-inline-size: 40rem;
  color: var(--grn-05-mut);
  font-size: clamp(0.95rem, 1.9vw, 1.09rem);
  text-wrap: pretty;
}

.grn-05__stocks {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(1rem, 2.4vw, 1.5rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
}

.grn-05__stock {
  display: grid;
  grid-template-rows: auto 1fr;
  overflow: hidden;
  border: 1px solid var(--grn-05-line);
  border-radius: 16px;
  background: var(--grn-05-surf);
  min-inline-size: 0;
}

.grn-05__frame {
  position: relative;
  block-size: clamp(9rem, 19vw, 11.5rem);
  background: linear-gradient(135deg, var(--grn-05-acc) 0%, color-mix(in oklab, var(--grn-05-acc) 40%, var(--grn-05-acc2)) 52%, var(--grn-05-acc2) 100%);
}

.grn-05__frame::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: var(--grn-05-grain);
}

.grn-05__frame--amber::after {
  filter: url(#grn-05-amber);
}

.grn-05__frame--cyan::after {
  filter: url(#grn-05-cyan);
}

.grn-05__frame--magenta::after {
  filter: url(#grn-05-magenta);
}

.grn-05__frame--neutral::after {
  filter: url(#grn-05-neutral);
  mix-blend-mode: overlay;
}

.grn-05__frame--olive::after {
  filter: url(#grn-05-olive);
}

.grn-05__frame--ink::after {
  filter: url(#grn-05-ink);
}

.grn-05__body {
  display: grid;
  align-content: start;
  gap: 0.5rem;
  padding: clamp(1rem, 2.2vw, 1.35rem);
}

.grn-05__row {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 0.6rem;
}

.grn-05__name {
  margin: 0;
  font: 600 1.05rem/1.2 var(--grn-05-font-display);
}

.grn-05__code {
  font: 400 0.7rem/1 var(--grn-05-font-mono);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--grn-05-mut);
}

.grn-05__desc {
  margin: 0;
  color: var(--grn-05-mut);
  font-size: 0.87rem;
  text-wrap: pretty;
}

.grn-05__matrix {
  justify-self: start;
  padding: 0.25rem 0.55rem;
  border-radius: 6px;
  background: color-mix(in oklab, var(--grn-05-acc) 14%, transparent);
  color: var(--grn-05-ink);
  font-size: 0.76rem;
  letter-spacing: 0.04em;
}

.grn-05__why {
  display: grid;
  gap: 0.6rem;
  padding: clamp(1.2rem, 3vw, 1.9rem);
  border: 1px solid var(--grn-05-line);
  border-radius: 16px;
  background: var(--grn-05-surf);
}

.grn-05__h2 {
  margin: 0;
  font: 600 clamp(1.1rem, 2.6vw, 1.35rem)/1.2 var(--grn-05-font-display);
}

.grn-05__why-body {
  margin: 0;
  max-inline-size: 52rem;
  color: var(--grn-05-mut);
  font-size: 0.92rem;
  text-wrap: pretty;
}

.grn-05__stock {
  transition: transform 300ms cubic-bezier(0.22, 1, 0.36, 1), border-color 240ms ease;
}

@media (hover: hover) and (pointer: fine) {
  .grn-05__stock:hover {
    transform: translateY(-4px);
    border-color: var(--grn-05-acc);
  }
}

@media (prefers-reduced-motion: reduce) {
  .grn-05__stock {
    transition-duration: 1ms;
  }

  .grn-05__stock:hover {
    transform: none;
  }
}
```
