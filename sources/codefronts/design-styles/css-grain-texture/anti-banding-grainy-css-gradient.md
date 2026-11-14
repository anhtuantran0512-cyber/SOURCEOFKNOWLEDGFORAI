---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/anti-banding-grainy-css-gradient/"
title: "Anti-Banding Grainy CSS Gradient"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "Banding is not a bug in your gradient, it is the 8-bit display pipeline showing through."
has_js: "false"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Anti-Banding Grainy CSS Gradient
Source: https://codefronts.com/design-styles/css-grain-texture/anti-banding-grainy-css-gradient/

Banding is not a bug in your gradient, it is the 8-bit display pipeline showing through. The fix is the same one film and print have used for a century: add noise. This is a full-bleed dusk hero built the correct way — oklab interpolation, a grain dither layer, and an honest side-by-side against the untreated version.
## HTML
```html
<section class="grn-07" aria-labelledby="grn-07-title">
  <div class="grn-07__theme">
    <input class="grn-07__theme-input" type="checkbox" id="grn-07-theme">
    <label class="grn-07__theme-label" for="grn-07-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-07__sr">Toggle dark theme</span>
    </label>
  </div>

  <header class="grn-07__hero">
    <div class="grn-07__hero-copy">
      <p class="grn-07__kicker">Dusk · 21:04 · clear</p>
      <h1 class="grn-07__h1" id="grn-07-title">A gradient with nowhere to hide</h1>
      <p class="grn-07__lede">Deep blue to violet across a full viewport is the hardest banding case on the web. This one is interpolated in <code>oklab</code>, stopped three times through the dark third, and dithered with grain at 3.5%.</p>
      <dl class="grn-07__specs">
        <div><dt>Interpolation</dt><dd>in oklab</dd></div>
        <div><dt>Dither</dt><dd>0.035</dd></div>
        <div><dt>Stops</dt><dd>6</dd></div>
      </dl>
    </div>
  </header>

  <main class="grn-07__main">
    <section class="grn-07__ab" aria-labelledby="grn-07-h-ab">
      <div class="grn-07__ab-head">
        <h2 class="grn-07__h2" id="grn-07-h-ab">The same ramp, treated and untreated</h2>
        <p class="grn-07__note">If you cannot see the difference, turn your screen brightness down — banding lives in the shadows.</p>
      </div>
      <div class="grn-07__ab-grid">
        <figure class="grn-07__panel grn-07__panel--raw">
          <div class="grn-07__field"></div>
          <figcaption><b>Untreated</b><span>sRGB interpolation, two stops, no dither</span></figcaption>
        </figure>
        <figure class="grn-07__panel grn-07__panel--fixed">
          <div class="grn-07__field"></div>
          <figcaption><b>Treated</b><span>oklab, six stops, 3.5% grain dither</span></figcaption>
        </figure>
      </div>
    </section>

    <section class="grn-07__steps" aria-labelledby="grn-07-h-steps">
      <h2 class="grn-07__h2" id="grn-07-h-steps">Ship it in this order</h2>
      <ol class="grn-07__list">
        <li><b>Interpolate in oklab.</b> Perceptually even steps mean smaller bands before you dither anything.</li>
        <li><b>Add stops where it bands.</b> Almost always the darkest third. Two extra stops halve the step size.</li>
        <li><b>Dither with grain at 0.03.</b> Raise in 0.005 increments until the bands go. Stop there.</li>
        <li><b>Check on an OLED phone at low brightness.</b> The harshest banding test that exists, and the one nobody runs.</li>
      </ol>
    </section>
  </main>
</section>
```
## CSS
```css
.grn-07 {
  --grn-07-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='grn07n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='180' height='180' filter='url(%23grn07n)'/%3E%3C/svg%3E");
  --grn-07-c1: #060b1f;
  --grn-07-c1: oklch(18% 0.06 268);
  --grn-07-c2: #21215c;
  --grn-07-c2: oklch(32% 0.11 280);
  --grn-07-c3: #6d3f8f;
  --grn-07-c3: oklch(48% 0.15 310);
  --grn-07-c4: #d97757;
  --grn-07-c4: oklch(70% 0.13 40);
  --grn-07-bg: #08060f;
  --grn-07-surf: #120f1d;
  --grn-07-line: #262138;
  --grn-07-ink: #f2eefb;
  --grn-07-mut: #a49bbd;
  --grn-07-dither: 0.035;
  --grn-07-font-display: "Space Grotesk", "Inter Tight", ui-sans-serif, system-ui, sans-serif;
  --grn-07-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--grn-07-bg);
  color: var(--grn-07-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.grn-07 *,
.grn-07 *::before,
.grn-07 *::after {
  box-sizing: border-box;
}

.grn-07 :focus-visible {
  outline: 2px solid var(--grn-07-c4);
  outline-offset: 3px;
}

.grn-07 code {
  font-family: var(--grn-07-font-mono);
  font-size: 0.9em;
}

.grn-07__sr {
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

.grn-07:has(.grn-07__theme-input:checked) {
  --grn-07-bg: #f4f1fa;
  --grn-07-surf: #ffffff;
  --grn-07-line: #e2dcf0;
  --grn-07-ink: #120f1d;
  --grn-07-mut: #625a7c;
  --grn-07-c1: #dfd8f2;
  --grn-07-c1: oklch(89% 0.04 290);
  --grn-07-c2: #a99ede;
  --grn-07-c2: oklch(74% 0.09 288);
  --grn-07-c3: #c68fb8;
  --grn-07-c3: oklch(72% 0.1 340);
  --grn-07-c4: #f0b083;
  --grn-07-c4: oklch(82% 0.1 55);
  --grn-07-dither: 0.03;
}

@media (prefers-color-scheme: light) {
  .grn-07 {
    --grn-07-bg: #f4f1fa;
    --grn-07-surf: #ffffff;
    --grn-07-line: #e2dcf0;
    --grn-07-ink: #120f1d;
    --grn-07-mut: #625a7c;
    --grn-07-c1: #dfd8f2;
    --grn-07-c1: oklch(89% 0.04 290);
    --grn-07-c2: #a99ede;
    --grn-07-c2: oklch(74% 0.09 288);
    --grn-07-c3: #c68fb8;
    --grn-07-c3: oklch(72% 0.1 340);
    --grn-07-c4: #f0b083;
    --grn-07-c4: oklch(82% 0.1 55);
    --grn-07-dither: 0.03;
  }

  .grn-07:has(.grn-07__theme-input:checked) {
    --grn-07-bg: #08060f;
    --grn-07-surf: #120f1d;
    --grn-07-line: #262138;
    --grn-07-ink: #f2eefb;
    --grn-07-mut: #a49bbd;
    --grn-07-c1: #060b1f;
    --grn-07-c1: oklch(18% 0.06 268);
    --grn-07-c2: #21215c;
    --grn-07-c2: oklch(32% 0.11 280);
    --grn-07-c3: #6d3f8f;
    --grn-07-c3: oklch(48% 0.15 310);
    --grn-07-c4: #d97757;
    --grn-07-c4: oklch(70% 0.13 40);
    --grn-07-dither: 0.035;
  }
}

@media (prefers-color-scheme: dark) {
  .grn-07:has(.grn-07__theme-input:checked) {
    --grn-07-bg: #f4f1fa;
    --grn-07-surf: #ffffff;
    --grn-07-line: #e2dcf0;
    --grn-07-ink: #120f1d;
    --grn-07-mut: #625a7c;
    --grn-07-c1: #dfd8f2;
    --grn-07-c1: oklch(89% 0.04 290);
    --grn-07-c2: #a99ede;
    --grn-07-c2: oklch(74% 0.09 288);
    --grn-07-c3: #c68fb8;
    --grn-07-c3: oklch(72% 0.1 340);
    --grn-07-c4: #f0b083;
    --grn-07-c4: oklch(82% 0.1 55);
    --grn-07-dither: 0.03;
  }
}

.grn-07__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 40;
}

.grn-07__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-07__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid rgba(255, 255, 255, 0.28);
  border-radius: 999px;
  background: rgba(10, 8, 20, 0.4);
  color: #f2eefb;
  cursor: pointer;
  backdrop-filter: blur(6px);
}

.grn-07__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-07__theme-input:focus-visible + .grn-07__theme-label {
  outline: 2px solid var(--grn-07-c4);
  outline-offset: 3px;
}

.grn-07__hero {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  min-block-size: min(86svh, 46rem);
  display: grid;
  align-items: end;
  background-image: radial-gradient(120% 90% at 78% 6%, color-mix(in oklab, var(--grn-07-c4) 55%, transparent) 0%, transparent 58%), linear-gradient(in oklab 168deg, var(--grn-07-c1) 0%, var(--grn-07-c1) 14%, var(--grn-07-c2) 38%, var(--grn-07-c2) 48%, var(--grn-07-c3) 74%, var(--grn-07-c4) 100%);
}

.grn-07__hero::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: 1;
  pointer-events: none;
  background-image: var(--grn-07-noise);
  opacity: var(--grn-07-dither);
  mix-blend-mode: overlay;
}

.grn-07__hero-copy {
  position: relative;
  z-index: 2;
  inline-size: min(70rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(4rem, 12vw, 7rem);
  display: grid;
  gap: 0.85rem;
  max-inline-size: 44rem;
}

.grn-07__kicker {
  margin: 0;
  font: 500 0.74rem/1 var(--grn-07-font-mono);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: color-mix(in oklab, var(--grn-07-ink) 78%, transparent);
}

.grn-07__h1 {
  margin: 0;
  font: 600 clamp(2.3rem, 7vw, 4.6rem)/0.99 var(--grn-07-font-display);
  letter-spacing: -0.04em;
  text-wrap: balance;
}

.grn-07__lede {
  margin: 0;
  max-inline-size: 34rem;
  color: color-mix(in oklab, var(--grn-07-ink) 82%, transparent);
  font-size: clamp(0.97rem, 2vw, 1.14rem);
  text-wrap: pretty;
}

.grn-07__specs {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: 0.5rem 0 0;
}

.grn-07__specs > div {
  display: grid;
  gap: 0.1rem;
  padding: 0.55rem 0.85rem;
  border: 1px solid rgba(255, 255, 255, 0.22);
  border-radius: 10px;
  background: rgba(8, 6, 15, 0.3);
  backdrop-filter: blur(4px);
}

.grn-07__specs dt {
  margin: 0;
  font: 400 0.68rem/1 var(--grn-07-font-mono);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  opacity: 0.7;
}

.grn-07__specs dd {
  margin: 0;
  font: 500 0.88rem/1.2 var(--grn-07-font-mono);
}

.grn-07__main {
  inline-size: min(70rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(2.5rem, 7vw, 4.5rem);
  display: grid;
  gap: clamp(2rem, 5vw, 3rem);
}

.grn-07__ab {
  display: grid;
  gap: 1rem;
}

.grn-07__ab-head {
  display: grid;
  gap: 0.35rem;
  padding-block-end: 0.7rem;
  border-block-end: 1px solid var(--grn-07-line);
}

.grn-07__h2 {
  margin: 0;
  font: 600 clamp(1.15rem, 2.8vw, 1.5rem)/1.2 var(--grn-07-font-display);
  letter-spacing: -0.02em;
}

.grn-07__note {
  margin: 0;
  color: var(--grn-07-mut);
  font-size: 0.88rem;
  text-wrap: pretty;
}

.grn-07__ab-grid {
  display: grid;
  gap: clamp(0.8rem, 2vw, 1.3rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr));
}

.grn-07__panel {
  margin: 0;
  display: grid;
  gap: 0.6rem;
  min-inline-size: 0;
}

.grn-07__field {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  block-size: clamp(11rem, 26vw, 17rem);
  border-radius: 14px;
}

.grn-07__panel--raw .grn-07__field {
  background-image: linear-gradient(168deg, var(--grn-07-c1), var(--grn-07-c3));
}

.grn-07__panel--fixed .grn-07__field {
  background-image: linear-gradient(in oklab 168deg, var(--grn-07-c1) 0%, var(--grn-07-c1) 12%, var(--grn-07-c2) 34%, var(--grn-07-c2) 46%, var(--grn-07-c3) 78%, var(--grn-07-c3) 100%);
}

.grn-07__panel--fixed .grn-07__field::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image: var(--grn-07-noise);
  opacity: var(--grn-07-dither);
  mix-blend-mode: overlay;
}

.grn-07__panel figcaption {
  display: grid;
  gap: 0.15rem;
}

.grn-07__panel figcaption b {
  font: 600 0.95rem/1.2 var(--grn-07-font-display);
}

.grn-07__panel figcaption span {
  color: var(--grn-07-mut);
  font: 400 0.8rem/1.4 var(--grn-07-font-mono);
}

.grn-07__steps {
  display: grid;
  gap: 0.9rem;
  padding: clamp(1.2rem, 3vw, 1.9rem);
  border: 1px solid var(--grn-07-line);
  border-radius: 16px;
  background: var(--grn-07-surf);
}

.grn-07__list {
  margin: 0;
  padding-inline-start: 1.3rem;
  display: grid;
  gap: 0.55rem;
  color: var(--grn-07-mut);
  font-size: 0.92rem;
}

.grn-07__list b {
  color: var(--grn-07-ink);
  font-weight: 600;
}

.grn-07__list::marker {
  color: var(--grn-07-c4);
}

@media (prefers-reduced-motion: reduce) {
  .grn-07 * {
    animation-duration: 1ms !important;
    transition-duration: 1ms !important;
  }
}
```
