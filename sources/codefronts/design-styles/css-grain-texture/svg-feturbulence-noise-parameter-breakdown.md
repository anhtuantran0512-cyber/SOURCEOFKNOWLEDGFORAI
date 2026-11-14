---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/svg-feturbulence-noise-parameter-breakdown/"
title: "SVG feTurbulence Noise Parameter Breakdown"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "Every grain effect on the modern web comes out of one SVG primitive: <feTurbulence>."
has_js: "false"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: SVG feTurbulence Noise Parameter Breakdown
Source: https://codefronts.com/design-styles/css-grain-texture/svg-feturbulence-noise-parameter-breakdown/

Every grain effect on the modern web comes out of one SVG primitive: <feTurbulence>. This demo is the parameter sheet for it — six live plates, each changing exactly one attribute (type, baseFrequency, numOctaves, seed, stitchTiles) so you can see what each dial does before guessing at values in production.
## HTML
```html
<section class="grn-01" aria-labelledby="grn-01-title">
  <svg class="grn-01__defs" width="0" height="0" aria-hidden="true" focusable="false">
    <filter id="grn-01-fractal-fine" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" seed="4" stitchTiles="stitch"/>
    </filter>
    <filter id="grn-01-fractal-coarse" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.16" numOctaves="3" seed="4" stitchTiles="stitch"/>
    </filter>
    <filter id="grn-01-turb" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="turbulence" baseFrequency="0.55" numOctaves="2" seed="9" stitchTiles="stitch"/>
    </filter>
    <filter id="grn-01-oct1" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.7" numOctaves="1" seed="4" stitchTiles="stitch"/>
    </filter>
    <filter id="grn-01-oct5" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.7" numOctaves="5" seed="4" stitchTiles="stitch"/>
    </filter>
    <filter id="grn-01-mono" x="0" y="0" width="100%" height="100%">
      <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="3" seed="21" stitchTiles="stitch"/>
      <feColorMatrix type="saturate" values="0"/>
    </filter>
  </svg>

  <div class="grn-01__theme">
    <input class="grn-01__theme-input" type="checkbox" id="grn-01-theme">
    <label class="grn-01__theme-label" for="grn-01-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-01__sr">Toggle dark theme</span>
    </label>
  </div>

  <main class="grn-01__shell">
    <header class="grn-01__head">
      <p class="grn-01__kicker">Texture lab · 01</p>
      <h1 class="grn-01__h1" id="grn-01-title">Every grain on the web starts here</h1>
      <p class="grn-01__lede">Six plates. One <code>&lt;feTurbulence&gt;</code> attribute changed per plate, everything else held constant. Read it as a decision table, not a gallery.</p>
    </header>

    <ul class="grn-01__plates">
      <li class="grn-01__plate">
        <div class="grn-01__swatch grn-01__swatch--fine" role="img" aria-label="Fine even film grain covering a cyan gradient"></div>
        <div class="grn-01__meta">
          <h2 class="grn-01__name">Fine film grain</h2>
          <dl class="grn-01__spec">
            <dt>type</dt><dd>fractalNoise</dd>
            <dt>baseFrequency</dt><dd>0.9</dd>
            <dt>numOctaves</dt><dd>3</dd>
          </dl>
          <p class="grn-01__note">The production default. Reads as photographic tooth at any size.</p>
        </div>
      </li>

      <li class="grn-01__plate">
        <div class="grn-01__swatch grn-01__swatch--coarse" role="img" aria-label="Coarse cloudy noise covering a cyan gradient"></div>
        <div class="grn-01__meta">
          <h2 class="grn-01__name">Coarse cloud</h2>
          <dl class="grn-01__spec">
            <dt>type</dt><dd>fractalNoise</dd>
            <dt>baseFrequency</dt><dd>0.16</dd>
            <dt>numOctaves</dt><dd>3</dd>
          </dl>
          <p class="grn-01__note">Same filter, one dial. Low frequency stops being grain and becomes weather.</p>
        </div>
      </li>

      <li class="grn-01__plate">
        <div class="grn-01__swatch grn-01__swatch--turb" role="img" aria-label="Veined marble-like turbulence over a cyan gradient"></div>
        <div class="grn-01__meta">
          <h2 class="grn-01__name">Veined turbulence</h2>
          <dl class="grn-01__spec">
            <dt>type</dt><dd>turbulence</dd>
            <dt>baseFrequency</dt><dd>0.55</dd>
            <dt>numOctaves</dt><dd>2</dd>
          </dl>
          <p class="grn-01__note"><code>turbulence</code> takes absolute values, so it creases. Marble, smoke, ink.</p>
        </div>
      </li>

      <li class="grn-01__plate">
        <div class="grn-01__swatch grn-01__swatch--oct1" role="img" aria-label="Smooth single-octave noise over a cyan gradient"></div>
        <div class="grn-01__meta">
          <h2 class="grn-01__name">One octave</h2>
          <dl class="grn-01__spec">
            <dt>numOctaves</dt><dd>1</dd>
            <dt>character</dt><dd>smooth</dd>
            <dt>cost</dt><dd>lowest</dd>
          </dl>
          <p class="grn-01__note">A single pass is soft and cheap. Good for large hero fields.</p>
        </div>
      </li>

      <li class="grn-01__plate">
        <div class="grn-01__swatch grn-01__swatch--oct5" role="img" aria-label="Crunchy five-octave noise over a cyan gradient"></div>
        <div class="grn-01__meta">
          <h2 class="grn-01__name">Five octaves</h2>
          <dl class="grn-01__spec">
            <dt>numOctaves</dt><dd>5</dd>
            <dt>character</dt><dd>crunchy</dd>
            <dt>cost</dt><dd>steep</dd>
          </dl>
          <p class="grn-01__note">Detail you cannot see at 6% opacity, paid for at every repaint.</p>
        </div>
      </li>

      <li class="grn-01__plate">
        <div class="grn-01__swatch grn-01__swatch--mono" role="img" aria-label="Desaturated monochrome grain over a cyan gradient"></div>
        <div class="grn-01__meta">
          <h2 class="grn-01__name">Desaturated</h2>
          <dl class="grn-01__spec">
            <dt>chain</dt><dd>+ feColorMatrix</dd>
            <dt>saturate</dt><dd>0</dd>
            <dt>result</dt><dd>neutral</dd>
          </dl>
          <p class="grn-01__note">Kills the colour confetti. Almost always what you want on UI.</p>
        </div>
      </li>
    </ul>

    <footer class="grn-01__foot">
      <p class="grn-01__foot-line">Copy the <code>&lt;svg&gt;</code> block once per document. Reference its filter ids from as many surfaces as you like — the noise is generated, so extra references cost nothing over the network.</p>
    </footer>
  </main>
</section>
```
## CSS
```css
.grn-01 {
  --grn-01-bg: #0d1418;
  --grn-01-surf: #131e24;
  --grn-01-line: #26383f;
  --grn-01-ink: #e8f2f5;
  --grn-01-mut: #8ba6af;
  --grn-01-acc: #22d3ee;
  --grn-01-acc: oklch(82% 0.13 200);
  --grn-01-acc-deep: #0e7490;
  --grn-01-acc-deep: oklch(50% 0.1 218);
  --grn-01-grain-op: 0.55;
  --grn-01-radius: 14px;
  --grn-01-font-display: "Space Grotesk", "Inter Tight", ui-sans-serif, system-ui, sans-serif;
  --grn-01-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--grn-01-bg);
  color: var(--grn-01-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
}

.grn-01 *,
.grn-01 *::before,
.grn-01 *::after {
  box-sizing: border-box;
}

.grn-01 :focus-visible {
  outline: 2px solid var(--grn-01-acc);
  outline-offset: 3px;
}

.grn-01 code {
  font-family: var(--grn-01-font-mono);
  font-size: 0.92em;
}

.grn-01__sr {
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

.grn-01__defs {
  position: absolute;
  width: 0;
  height: 0;
  overflow: hidden;
}

.grn-01:has(.grn-01__theme-input:checked) {
  --grn-01-bg: #eef4f6;
  --grn-01-surf: #ffffff;
  --grn-01-line: #cddde2;
  --grn-01-ink: #0d1418;
  --grn-01-mut: #5a747d;
  --grn-01-acc: #0891b2;
  --grn-01-acc: oklch(62% 0.12 213);
  --grn-01-acc-deep: #a5f3fc;
  --grn-01-acc-deep: oklch(92% 0.07 197);
  --grn-01-grain-op: 0.4;
}

@media (prefers-color-scheme: light) {
  .grn-01 {
    --grn-01-bg: #eef4f6;
    --grn-01-surf: #ffffff;
    --grn-01-line: #cddde2;
    --grn-01-ink: #0d1418;
    --grn-01-mut: #5a747d;
    --grn-01-acc: #0891b2;
    --grn-01-acc: oklch(62% 0.12 213);
    --grn-01-acc-deep: #a5f3fc;
    --grn-01-acc-deep: oklch(92% 0.07 197);
    --grn-01-grain-op: 0.4;
  }

  .grn-01:has(.grn-01__theme-input:checked) {
    --grn-01-bg: #0d1418;
    --grn-01-surf: #131e24;
    --grn-01-line: #26383f;
    --grn-01-ink: #e8f2f5;
    --grn-01-mut: #8ba6af;
    --grn-01-acc: #22d3ee;
    --grn-01-acc: oklch(82% 0.13 200);
    --grn-01-acc-deep: #0e7490;
    --grn-01-acc-deep: oklch(50% 0.1 218);
    --grn-01-grain-op: 0.55;
  }
}

@media (prefers-color-scheme: dark) {
  .grn-01:has(.grn-01__theme-input:checked) {
    --grn-01-bg: #eef4f6;
    --grn-01-surf: #ffffff;
    --grn-01-line: #cddde2;
    --grn-01-ink: #0d1418;
    --grn-01-mut: #5a747d;
    --grn-01-acc: #0891b2;
    --grn-01-acc: oklch(62% 0.12 213);
    --grn-01-acc-deep: #a5f3fc;
    --grn-01-acc-deep: oklch(92% 0.07 197);
    --grn-01-grain-op: 0.4;
  }
}

.grn-01__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 40;
}

.grn-01__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-01__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--grn-01-line);
  border-radius: 999px;
  background: var(--grn-01-surf);
  color: var(--grn-01-ink);
  cursor: pointer;
}

.grn-01__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-01__theme-input:focus-visible + .grn-01__theme-label {
  outline: 2px solid var(--grn-01-acc);
  outline-offset: 3px;
}

.grn-01__shell {
  inline-size: min(76rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(3rem, 8vw, 5.5rem) clamp(2.5rem, 6vw, 4rem);
}

.grn-01__head {
  max-inline-size: 44rem;
  display: grid;
  gap: 0.7rem;
}

.grn-01__kicker {
  margin: 0;
  font: 500 0.72rem/1 var(--grn-01-font-mono);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--grn-01-acc);
}

.grn-01__h1 {
  margin: 0;
  font: 600 clamp(2rem, 5.4vw, 3.4rem)/1.04 var(--grn-01-font-display);
  letter-spacing: -0.03em;
  text-wrap: balance;
}

.grn-01__lede {
  margin: 0;
  max-inline-size: 38rem;
  color: var(--grn-01-mut);
  font-size: clamp(0.95rem, 1.9vw, 1.09rem);
  text-wrap: pretty;
}

.grn-01__plates {
  list-style: none;
  margin: clamp(2.2rem, 5vw, 3.4rem) 0 0;
  padding: 0;
  display: grid;
  gap: clamp(1rem, 2.4vw, 1.6rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
}

.grn-01__plate {
  position: relative;
  display: grid;
  grid-template-rows: auto 1fr;
  overflow: hidden;
  border: 1px solid var(--grn-01-line);
  border-radius: var(--grn-01-radius);
  background: var(--grn-01-surf);
  min-inline-size: 0;
}

.grn-01__swatch {
  position: relative;
  block-size: clamp(9rem, 20vw, 12rem);
  background: linear-gradient(148deg, var(--grn-01-acc) 0%, var(--grn-01-acc-deep) 58%, var(--grn-01-bg) 100%);
  isolation: isolate;
}

.grn-01__swatch::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: var(--grn-01-grain-op);
  mix-blend-mode: overlay;
}

.grn-01__swatch--fine::after {
  filter: url(#grn-01-fractal-fine);
}

.grn-01__swatch--coarse::after {
  filter: url(#grn-01-fractal-coarse);
}

.grn-01__swatch--turb::after {
  filter: url(#grn-01-turb);
}

.grn-01__swatch--oct1::after {
  filter: url(#grn-01-oct1);
}

.grn-01__swatch--oct5::after {
  filter: url(#grn-01-oct5);
}

.grn-01__swatch--mono::after {
  filter: url(#grn-01-mono);
  opacity: calc(var(--grn-01-grain-op) + 0.2);
  mix-blend-mode: soft-light;
}

.grn-01__meta {
  display: grid;
  align-content: start;
  gap: 0.6rem;
  padding: clamp(0.95rem, 2vw, 1.25rem);
}

.grn-01__name {
  margin: 0;
  font: 600 1.02rem/1.2 var(--grn-01-font-display);
  letter-spacing: -0.01em;
}

.grn-01__spec {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 0.15rem 0.6rem;
  margin: 0;
  padding-block: 0.5rem;
  border-block: 1px solid var(--grn-01-line);
  font: 400 0.76rem/1.5 var(--grn-01-font-mono);
}

.grn-01__spec dt {
  margin: 0;
  color: var(--grn-01-mut);
}

.grn-01__spec dd {
  margin: 0;
  color: var(--grn-01-ink);
}

.grn-01__note {
  margin: 0;
  color: var(--grn-01-mut);
  font-size: 0.86rem;
  text-wrap: pretty;
}

.grn-01__foot {
  margin-block-start: clamp(2rem, 5vw, 3rem);
  padding-block-start: 1.25rem;
  border-block-start: 1px solid var(--grn-01-line);
}

.grn-01__foot-line {
  margin: 0;
  max-inline-size: 46rem;
  color: var(--grn-01-mut);
  font-size: 0.9rem;
  text-wrap: pretty;
}

.grn-01__plate {
  transition: border-color 240ms ease, transform 320ms cubic-bezier(0.22, 1, 0.36, 1);
}

@media (hover: hover) and (pointer: fine) {
  .grn-01__plate:hover {
    border-color: var(--grn-01-acc);
    transform: translateY(-3px);
  }

  .grn-01__plate:hover .grn-01__swatch::after {
    opacity: calc(var(--grn-01-grain-op) + 0.18);
  }
}

.grn-01__swatch::after {
  transition: opacity 300ms ease;
}

@media (prefers-reduced-motion: reduce) {
  .grn-01__plate,
    .grn-01__swatch::after {
    transition-duration: 1ms;
  }

  .grn-01__plate:hover {
    transform: none;
  }
}
```
