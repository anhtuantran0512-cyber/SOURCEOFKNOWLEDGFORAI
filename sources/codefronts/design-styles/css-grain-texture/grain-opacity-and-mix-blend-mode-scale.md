---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/grain-opacity-and-mix-blend-mode-scale/"
title: "Grain Opacity and mix-blend-mode Scale"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "Grain has two dials after generation: how strong it is and how it composites."
has_js: "false"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Grain Opacity and mix-blend-mode Scale
Source: https://codefronts.com/design-styles/css-grain-texture/grain-opacity-and-mix-blend-mode-scale/

Grain has two dials after generation: how strong it is and how it composites. This is the full matrix — eight mix-blend-mode values against one identical noise layer, plus a five-step opacity scale with the range that actually ships marked on it. The difference between "expensive" and "dirty" is almost always one of these two numbers.
## HTML
```html
<section class="grn-04" aria-labelledby="grn-04-title">
  <div class="grn-04__theme">
    <input class="grn-04__theme-input" type="checkbox" id="grn-04-theme">
    <label class="grn-04__theme-label" for="grn-04-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-04__sr">Toggle dark theme</span>
    </label>
  </div>

  <main class="grn-04__shell">
    <header class="grn-04__head">
      <p class="grn-04__kicker">Composite reference · 04</p>
      <h1 class="grn-04__h1" id="grn-04-title">Same noise. Eight composites. Only three ship.</h1>
      <p class="grn-04__lede">One grain layer, one opacity, eight <code>mix-blend-mode</code> values. Then the opacity scale, with the band that survives design review marked on it.</p>
    </header>

    <section class="grn-04__band" aria-labelledby="grn-04-h-op">
      <div class="grn-04__band-head">
        <h2 class="grn-04__h2" id="grn-04-h-op">Opacity scale</h2>
        <p class="grn-04__note">Blend held at <code>overlay</code>. The marked band is where production lives.</p>
      </div>
      <ol class="grn-04__scale">
        <li class="grn-04__stop"><span class="grn-04__chip" style="--grn-04-local: 0.02"></span><span class="grn-04__num">0.02</span><span class="grn-04__lab">invisible</span></li>
        <li class="grn-04__stop grn-04__stop--ship"><span class="grn-04__chip" style="--grn-04-local: 0.05"></span><span class="grn-04__num">0.05</span><span class="grn-04__lab">light UI</span></li>
        <li class="grn-04__stop grn-04__stop--ship"><span class="grn-04__chip" style="--grn-04-local: 0.09"></span><span class="grn-04__num">0.09</span><span class="grn-04__lab">dark UI</span></li>
        <li class="grn-04__stop"><span class="grn-04__chip" style="--grn-04-local: 0.18"></span><span class="grn-04__num">0.18</span><span class="grn-04__lab">editorial</span></li>
        <li class="grn-04__stop"><span class="grn-04__chip" style="--grn-04-local: 0.4"></span><span class="grn-04__num">0.40</span><span class="grn-04__lab">effect, not texture</span></li>
      </ol>
    </section>

    <section class="grn-04__band" aria-labelledby="grn-04-h-blend">
      <div class="grn-04__band-head">
        <h2 class="grn-04__h2" id="grn-04-h-blend">Blend mode matrix</h2>
        <p class="grn-04__note">Opacity held at <code>0.32</code> so the differences are legible at tile size.</p>
      </div>
      <ul class="grn-04__matrix">
        <li class="grn-04__cell grn-04__cell--pick"><span class="grn-04__tile" style="--grn-04-mode: overlay"></span><span class="grn-04__mode">overlay</span><span class="grn-04__lab">embedded · default</span></li>
        <li class="grn-04__cell grn-04__cell--pick"><span class="grn-04__tile" style="--grn-04-mode: soft-light"></span><span class="grn-04__mode">soft-light</span><span class="grn-04__lab">gentle · large fields</span></li>
        <li class="grn-04__cell grn-04__cell--pick"><span class="grn-04__tile" style="--grn-04-mode: multiply"></span><span class="grn-04__mode">multiply</span><span class="grn-04__lab">darkens only · paper</span></li>
        <li class="grn-04__cell"><span class="grn-04__tile" style="--grn-04-mode: screen"></span><span class="grn-04__mode">screen</span><span class="grn-04__lab">lightens only · dust</span></li>
        <li class="grn-04__cell"><span class="grn-04__tile" style="--grn-04-mode: luminosity"></span><span class="grn-04__mode">luminosity</span><span class="grn-04__lab">hue-safe · photos</span></li>
        <li class="grn-04__cell"><span class="grn-04__tile" style="--grn-04-mode: color-burn"></span><span class="grn-04__mode">color-burn</span><span class="grn-04__lab">clips hard</span></li>
        <li class="grn-04__cell"><span class="grn-04__tile" style="--grn-04-mode: hard-light"></span><span class="grn-04__mode">hard-light</span><span class="grn-04__lab">too contrasty</span></li>
        <li class="grn-04__cell"><span class="grn-04__tile" style="--grn-04-mode: normal"></span><span class="grn-04__mode">normal</span><span class="grn-04__lab">grey veil · avoid</span></li>
      </ul>
    </section>

    <section class="grn-04__demo" aria-labelledby="grn-04-h-live">
      <div class="grn-04__demo-copy">
        <h2 class="grn-04__h2" id="grn-04-h-live">The same rule at hero scale</h2>
        <p class="grn-04__note">Modes that look identical on a 140px tile diverge across a full-bleed field. This panel runs <code>soft-light</code> at <code>0.07</code> — the setting that survives the most design reviews.</p>
        <p class="grn-04__isolate"><code>isolation: isolate</code> is on this panel. Remove it and the grain blends against the page instead.</p>
      </div>
    </section>
  </main>
</section>
```
## CSS
```css
.grn-04 {
  --grn-04-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='grn04n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23grn04n)'/%3E%3C/svg%3E");
  --grn-04-bg: #0f0b16;
  --grn-04-surf: #191128;
  --grn-04-line: #2f2145;
  --grn-04-ink: #f0eaff;
  --grn-04-mut: #a394c4;
  --grn-04-acc: #a78bfa;
  --grn-04-acc: oklch(75% 0.16 296);
  --grn-04-acc2: #f472b6;
  --grn-04-acc2: oklch(72% 0.19 350);
  --grn-04-op: 0.32;
  --grn-04-font-display: "Space Grotesk", "Inter Tight", ui-sans-serif, system-ui, sans-serif;
  --grn-04-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--grn-04-bg);
  color: var(--grn-04-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.grn-04 *,
.grn-04 *::before,
.grn-04 *::after {
  box-sizing: border-box;
}

.grn-04 :focus-visible {
  outline: 2px solid var(--grn-04-acc);
  outline-offset: 3px;
}

.grn-04 code {
  font-family: var(--grn-04-font-mono);
  font-size: 0.9em;
}

.grn-04__sr {
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

.grn-04:has(.grn-04__theme-input:checked) {
  --grn-04-bg: #f6f3fc;
  --grn-04-surf: #ffffff;
  --grn-04-line: #e0d7f2;
  --grn-04-ink: #140f1f;
  --grn-04-mut: #63558a;
  --grn-04-acc: #7c3aed;
  --grn-04-acc: oklch(54% 0.23 295);
  --grn-04-acc2: #db2777;
  --grn-04-acc2: oklch(56% 0.21 355);
  --grn-04-op: 0.26;
}

@media (prefers-color-scheme: light) {
  .grn-04 {
    --grn-04-bg: #f6f3fc;
    --grn-04-surf: #ffffff;
    --grn-04-line: #e0d7f2;
    --grn-04-ink: #140f1f;
    --grn-04-mut: #63558a;
    --grn-04-acc: #7c3aed;
    --grn-04-acc: oklch(54% 0.23 295);
    --grn-04-acc2: #db2777;
    --grn-04-acc2: oklch(56% 0.21 355);
    --grn-04-op: 0.26;
  }

  .grn-04:has(.grn-04__theme-input:checked) {
    --grn-04-bg: #0f0b16;
    --grn-04-surf: #191128;
    --grn-04-line: #2f2145;
    --grn-04-ink: #f0eaff;
    --grn-04-mut: #a394c4;
    --grn-04-acc: #a78bfa;
    --grn-04-acc: oklch(75% 0.16 296);
    --grn-04-acc2: #f472b6;
    --grn-04-acc2: oklch(72% 0.19 350);
    --grn-04-op: 0.32;
  }
}

@media (prefers-color-scheme: dark) {
  .grn-04:has(.grn-04__theme-input:checked) {
    --grn-04-bg: #f6f3fc;
    --grn-04-surf: #ffffff;
    --grn-04-line: #e0d7f2;
    --grn-04-ink: #140f1f;
    --grn-04-mut: #63558a;
    --grn-04-acc: #7c3aed;
    --grn-04-acc: oklch(54% 0.23 295);
    --grn-04-acc2: #db2777;
    --grn-04-acc2: oklch(56% 0.21 355);
    --grn-04-op: 0.26;
  }
}

.grn-04__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 40;
}

.grn-04__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-04__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--grn-04-line);
  border-radius: 999px;
  background: var(--grn-04-surf);
  color: var(--grn-04-ink);
  cursor: pointer;
}

.grn-04__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-04__theme-input:focus-visible + .grn-04__theme-label {
  outline: 2px solid var(--grn-04-acc);
  outline-offset: 3px;
}

.grn-04__shell {
  inline-size: min(76rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(3rem, 8vw, 5.5rem) clamp(2.5rem, 6vw, 4rem);
  display: grid;
  gap: clamp(2.2rem, 5vw, 3.4rem);
}

.grn-04__head {
  max-inline-size: 46rem;
  display: grid;
  gap: 0.7rem;
}

.grn-04__kicker {
  margin: 0;
  font: 500 0.72rem/1 var(--grn-04-font-mono);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--grn-04-acc);
}

.grn-04__h1 {
  margin: 0;
  font: 600 clamp(2rem, 5.4vw, 3.5rem)/1.03 var(--grn-04-font-display);
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.grn-04__lede {
  margin: 0;
  max-inline-size: 40rem;
  color: var(--grn-04-mut);
  font-size: clamp(0.95rem, 1.9vw, 1.09rem);
  text-wrap: pretty;
}

.grn-04__band {
  display: grid;
  gap: 1rem;
}

.grn-04__band-head {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 0.35rem 1rem;
  padding-block-end: 0.6rem;
  border-block-end: 1px solid var(--grn-04-line);
}

.grn-04__h2 {
  margin: 0;
  font: 600 clamp(1.1rem, 2.6vw, 1.4rem)/1.2 var(--grn-04-font-display);
  letter-spacing: -0.015em;
}

.grn-04__note {
  margin: 0;
  max-inline-size: 44rem;
  color: var(--grn-04-mut);
  font-size: 0.88rem;
  text-wrap: pretty;
}

.grn-04__scale {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(0.5rem, 1.4vw, 0.9rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 8.5rem), 1fr));
}

.grn-04__stop {
  display: grid;
  gap: 0.3rem;
  min-inline-size: 0;
}

.grn-04__chip {
  position: relative;
  display: block;
  block-size: clamp(5.5rem, 12vw, 7.5rem);
  border-radius: 12px;
  overflow: hidden;
  isolation: isolate;
  background: linear-gradient(150deg, var(--grn-04-acc), var(--grn-04-acc2) 70%, var(--grn-04-surf));
}

.grn-04__chip::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image: var(--grn-04-noise);
  opacity: var(--grn-04-local, 0.05);
  mix-blend-mode: overlay;
}

.grn-04__num {
  font: 500 0.88rem/1 var(--grn-04-font-mono);
}

.grn-04__lab {
  font-size: 0.72rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--grn-04-mut);
}

.grn-04__stop--ship .grn-04__chip {
  box-shadow: 0 0 0 2px var(--grn-04-acc);
}

.grn-04__stop--ship .grn-04__lab {
  color: var(--grn-04-acc);
  font-weight: 600;
}

.grn-04__matrix {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(0.55rem, 1.5vw, 0.95rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 9.5rem), 1fr));
}

.grn-04__cell {
  display: grid;
  gap: 0.3rem;
  min-inline-size: 0;
}

.grn-04__tile {
  position: relative;
  display: block;
  block-size: clamp(6rem, 13vw, 8rem);
  border-radius: 12px;
  overflow: hidden;
  isolation: isolate;
  background: conic-gradient(from 210deg at 30% 20%, var(--grn-04-acc), var(--grn-04-acc2) 40%, var(--grn-04-surf) 78%, var(--grn-04-acc));
}

.grn-04__tile::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image: var(--grn-04-noise);
  opacity: var(--grn-04-op);
  mix-blend-mode: var(--grn-04-mode, overlay);
}

.grn-04__mode {
  font: 500 0.85rem/1.2 var(--grn-04-font-mono);
}

.grn-04__cell--pick .grn-04__tile {
  box-shadow: 0 0 0 2px var(--grn-04-acc);
}

.grn-04__cell--pick .grn-04__mode {
  color: var(--grn-04-acc);
}

.grn-04__demo {
  position: relative;
  overflow: hidden;
  border-radius: 20px;
  isolation: isolate;
  background: radial-gradient(130% 130% at 78% 8%, var(--grn-04-acc2) 0%, var(--grn-04-acc) 38%, var(--grn-04-surf) 82%);
}

.grn-04__demo::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image: var(--grn-04-noise);
  opacity: 0.07;
  mix-blend-mode: soft-light;
}

.grn-04__demo-copy {
  position: relative;
  z-index: 1;
  display: grid;
  gap: 0.7rem;
  max-inline-size: 40rem;
  padding: clamp(1.8rem, 5vw, 3.2rem);
}

.grn-04__demo-copy .grn-04__h2,
.grn-04__demo-copy .grn-04__note {
  color: #f7f4ff;
}

.grn-04__isolate {
  margin: 0;
  padding: 0.6rem 0.85rem;
  border-radius: 10px;
  background: rgba(12, 6, 22, 0.42);
  color: #f7f4ff;
  font: 400 0.84rem/1.5 var(--grn-04-font-mono);
  backdrop-filter: blur(3px);
}

.grn-04__chip,
.grn-04__tile {
  transition: transform 280ms cubic-bezier(0.22, 1, 0.36, 1);
}

@media (hover: hover) and (pointer: fine) {
  .grn-04__stop:hover .grn-04__chip,
    .grn-04__cell:hover .grn-04__tile {
    transform: translateY(-3px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .grn-04__chip,
    .grn-04__tile {
    transition-duration: 1ms;
    transform: none;
  }
}
```
