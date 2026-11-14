---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/basefrequency-numoctaves-grain-size/"
title: "baseFrequency and numOctaves Grain Size Control"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "A specimen sheet for the only two attributes that decide whether your grain reads as expensive film stock or as a broken JPEG."
has_js: "false"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: baseFrequency and numOctaves Grain Size Control
Source: https://codefronts.com/design-styles/css-grain-texture/basefrequency-numoctaves-grain-size/

A specimen sheet for the only two attributes that decide whether your grain reads as expensive film stock or as a broken JPEG. Nine baseFrequency steps from 0.05 to 1.6, an octave ramp beside them, and the two-value baseFrequency trick that stretches grain into brushed metal.
## HTML
```html
<section class="grn-02" aria-labelledby="grn-02-title">
  <svg class="grn-02__defs" width="0" height="0" aria-hidden="true" focusable="false">
    <filter id="grn-02-f005" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="3" seed="11" stitchTiles="stitch"/></filter>
    <filter id="grn-02-f015" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.15" numOctaves="3" seed="11" stitchTiles="stitch"/></filter>
    <filter id="grn-02-f030" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.3" numOctaves="3" seed="11" stitchTiles="stitch"/></filter>
    <filter id="grn-02-f050" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.5" numOctaves="3" seed="11" stitchTiles="stitch"/></filter>
    <filter id="grn-02-f080" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" seed="11" stitchTiles="stitch"/></filter>
    <filter id="grn-02-f120" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="1.2" numOctaves="3" seed="11" stitchTiles="stitch"/></filter>
    <filter id="grn-02-f160" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="1.6" numOctaves="3" seed="11" stitchTiles="stitch"/></filter>
    <filter id="grn-02-o1" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.75" numOctaves="1" seed="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
    <filter id="grn-02-o2" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.75" numOctaves="2" seed="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
    <filter id="grn-02-o4" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.75" numOctaves="4" seed="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
    <filter id="grn-02-aniso-v" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.02 0.9" numOctaves="3" seed="6" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
    <filter id="grn-02-aniso-h" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.9 0.02" numOctaves="3" seed="6" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
  </svg>

  <div class="grn-02__theme">
    <input class="grn-02__theme-input" type="checkbox" id="grn-02-theme">
    <label class="grn-02__theme-label" for="grn-02-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-02__sr">Toggle dark theme</span>
    </label>
  </div>

  <main class="grn-02__shell">
    <header class="grn-02__head">
      <p class="grn-02__kicker">Specimen sheet · 02</p>
      <h1 class="grn-02__h1" id="grn-02-title">Grain size is one number, and most people guess it</h1>
      <p class="grn-02__lede">Seven frequency steps, an octave ramp, and the two-value form that streaks the lattice. Everything else — type, seed, blend mode, opacity — is held constant.</p>
    </header>

    <section class="grn-02__block" aria-labelledby="grn-02-h-freq">
      <div class="grn-02__block-head">
        <h2 class="grn-02__h2" id="grn-02-h-freq">baseFrequency ramp</h2>
        <p class="grn-02__block-note">Bigger number, smaller grain. <code>numOctaves</code> pinned at 3.</p>
      </div>
      <ol class="grn-02__ramp">
        <li class="grn-02__step"><span class="grn-02__tile grn-02__tile--f005"></span><span class="grn-02__val">0.05</span><span class="grn-02__tag">cloud</span></li>
        <li class="grn-02__step"><span class="grn-02__tile grn-02__tile--f015"></span><span class="grn-02__val">0.15</span><span class="grn-02__tag">blotch</span></li>
        <li class="grn-02__step"><span class="grn-02__tile grn-02__tile--f030"></span><span class="grn-02__val">0.30</span><span class="grn-02__tag">coarse</span></li>
        <li class="grn-02__step"><span class="grn-02__tile grn-02__tile--f050"></span><span class="grn-02__val">0.50</span><span class="grn-02__tag">sand</span></li>
        <li class="grn-02__step grn-02__step--ship"><span class="grn-02__tile grn-02__tile--f080"></span><span class="grn-02__val">0.80</span><span class="grn-02__tag">ship this</span></li>
        <li class="grn-02__step"><span class="grn-02__tile grn-02__tile--f120"></span><span class="grn-02__val">1.20</span><span class="grn-02__tag">fine</span></li>
        <li class="grn-02__step"><span class="grn-02__tile grn-02__tile--f160"></span><span class="grn-02__val">1.60</span><span class="grn-02__tag">aliases</span></li>
      </ol>
    </section>

    <div class="grn-02__pair">
      <section class="grn-02__block" aria-labelledby="grn-02-h-oct">
        <div class="grn-02__block-head">
          <h2 class="grn-02__h2" id="grn-02-h-oct">numOctaves ramp</h2>
          <p class="grn-02__block-note">Same size, different character. <code>baseFrequency</code> pinned at 0.75.</p>
        </div>
        <ol class="grn-02__ramp grn-02__ramp--wide">
          <li class="grn-02__step"><span class="grn-02__tile grn-02__tile--o1"></span><span class="grn-02__val">1</span><span class="grn-02__tag">smooth</span></li>
          <li class="grn-02__step"><span class="grn-02__tile grn-02__tile--o2"></span><span class="grn-02__val">2</span><span class="grn-02__tag">soft</span></li>
          <li class="grn-02__step grn-02__step--ship"><span class="grn-02__tile grn-02__tile--o3"></span><span class="grn-02__val">3</span><span class="grn-02__tag">organic</span></li>
          <li class="grn-02__step"><span class="grn-02__tile grn-02__tile--o4"></span><span class="grn-02__val">4</span><span class="grn-02__tag">crunchy</span></li>
        </ol>
      </section>

      <section class="grn-02__block" aria-labelledby="grn-02-h-aniso">
        <div class="grn-02__block-head">
          <h2 class="grn-02__h2" id="grn-02-h-aniso">Two values, one streak</h2>
          <p class="grn-02__block-note"><code>baseFrequency="0.02 0.9"</code> stretches the lattice.</p>
        </div>
        <div class="grn-02__aniso">
          <figure class="grn-02__fig">
            <span class="grn-02__tile grn-02__tile--aniso-v"></span>
            <figcaption>0.02 0.9 · vertical rain</figcaption>
          </figure>
          <figure class="grn-02__fig">
            <span class="grn-02__tile grn-02__tile--aniso-h"></span>
            <figcaption>0.9 0.02 · brushed metal</figcaption>
          </figure>
        </div>
      </section>
    </div>

    <aside class="grn-02__dpr" aria-labelledby="grn-02-h-dpr">
      <h2 class="grn-02__h2" id="grn-02-h-dpr">The retina correction</h2>
      <p class="grn-02__dpr-body"><code>baseFrequency</code> resolves in user space, not device pixels — so grain tuned on a 1x monitor spreads across three times as many pixels on a 3x phone and reads as dirt. This sheet ships the fix: a <code>min-resolution: 2dppx</code> query that raises the frequency on dense displays. The tile below is running whichever value your current screen asked for.</p>
      <div class="grn-02__dpr-tile"><span class="grn-02__dpr-label">live on this display</span></div>
    </aside>
  </main>
</section>
```
## CSS
```css
.grn-02 {
  --grn-02-bg: #f5f1e8;
  --grn-02-surf: #fffdf8;
  --grn-02-line: #ddd5c4;
  --grn-02-ink: #1d1a14;
  --grn-02-mut: #6f6857;
  --grn-02-acc: #b4531f;
  --grn-02-acc: oklch(52% 0.14 45);
  --grn-02-ship: 0.8;
  --grn-02-grain-op: 0.72;
  --grn-02-font-display: "Fraunces", "Playfair Display", Georgia, "Times New Roman", serif;
  --grn-02-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--grn-02-bg);
  color: var(--grn-02-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.grn-02 *,
.grn-02 *::before,
.grn-02 *::after {
  box-sizing: border-box;
}

.grn-02 :focus-visible {
  outline: 2px solid var(--grn-02-acc);
  outline-offset: 3px;
}

.grn-02 code {
  font-family: var(--grn-02-font-mono);
  font-size: 0.9em;
}

.grn-02__sr {
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

.grn-02__defs {
  position: absolute;
  width: 0;
  height: 0;
  overflow: hidden;
}

.grn-02:has(.grn-02__theme-input:checked) {
  --grn-02-bg: #14120e;
  --grn-02-surf: #1d1a15;
  --grn-02-line: #35301f;
  --grn-02-ink: #f3eee2;
  --grn-02-mut: #a89e88;
  --grn-02-acc: #f0844a;
  --grn-02-acc: oklch(74% 0.14 48);
  --grn-02-grain-op: 0.6;
  --grn-02-grain-blend: screen;
}

@media (prefers-color-scheme: dark) {
  .grn-02 {
    --grn-02-bg: #14120e;
    --grn-02-surf: #1d1a15;
    --grn-02-line: #35301f;
    --grn-02-ink: #f3eee2;
    --grn-02-mut: #a89e88;
    --grn-02-acc: #f0844a;
    --grn-02-acc: oklch(74% 0.14 48);
    --grn-02-grain-op: 0.6;
    --grn-02-grain-blend: screen;
  }

  .grn-02:has(.grn-02__theme-input:checked) {
    --grn-02-bg: #f5f1e8;
    --grn-02-surf: #fffdf8;
    --grn-02-line: #ddd5c4;
    --grn-02-ink: #1d1a14;
    --grn-02-mut: #6f6857;
    --grn-02-acc: #b4531f;
    --grn-02-acc: oklch(52% 0.14 45);
    --grn-02-grain-op: 0.72;
    --grn-02-grain-blend: multiply;
  }
}

@media (prefers-color-scheme: light) {
  .grn-02:has(.grn-02__theme-input:checked) {
    --grn-02-bg: #14120e;
    --grn-02-surf: #1d1a15;
    --grn-02-line: #35301f;
    --grn-02-ink: #f3eee2;
    --grn-02-mut: #a89e88;
    --grn-02-acc: #f0844a;
    --grn-02-acc: oklch(74% 0.14 48);
    --grn-02-grain-op: 0.6;
    --grn-02-grain-blend: screen;
  }
}

.grn-02__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 40;
}

.grn-02__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-02__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--grn-02-line);
  border-radius: 999px;
  background: var(--grn-02-surf);
  color: var(--grn-02-ink);
  cursor: pointer;
}

.grn-02__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-02__theme-input:focus-visible + .grn-02__theme-label {
  outline: 2px solid var(--grn-02-acc);
  outline-offset: 3px;
}

.grn-02__shell {
  inline-size: min(74rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(3rem, 8vw, 5.5rem) clamp(2.5rem, 6vw, 4rem);
  display: grid;
  gap: clamp(2.2rem, 5vw, 3.5rem);
}

.grn-02__head {
  max-inline-size: 46rem;
  display: grid;
  gap: 0.7rem;
}

.grn-02__kicker {
  margin: 0;
  font: 500 0.72rem/1 var(--grn-02-font-mono);
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--grn-02-acc);
}

.grn-02__h1 {
  margin: 0;
  font: 500 clamp(2rem, 5.2vw, 3.3rem)/1.06 var(--grn-02-font-display);
  letter-spacing: -0.02em;
  text-wrap: balance;
}

.grn-02__lede {
  margin: 0;
  max-inline-size: 40rem;
  color: var(--grn-02-mut);
  font-size: clamp(0.95rem, 1.9vw, 1.08rem);
  text-wrap: pretty;
}

.grn-02__block {
  display: grid;
  gap: 1rem;
}

.grn-02__block-head {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 0.4rem 1rem;
  padding-block-end: 0.6rem;
  border-block-end: 1px solid var(--grn-02-line);
}

.grn-02__h2 {
  margin: 0;
  font: 500 clamp(1.1rem, 2.6vw, 1.4rem)/1.15 var(--grn-02-font-display);
}

.grn-02__block-note {
  margin: 0;
  color: var(--grn-02-mut);
  font-size: 0.85rem;
}

.grn-02__ramp {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(0.5rem, 1.4vw, 0.85rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 7.5rem), 1fr));
}

.grn-02__ramp--wide {
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 8.5rem), 1fr));
}

.grn-02__step {
  display: grid;
  gap: 0.35rem;
  min-inline-size: 0;
}

.grn-02__tile {
  position: relative;
  display: block;
  block-size: clamp(6rem, 13vw, 8rem);
  border: 1px solid var(--grn-02-line);
  border-radius: 10px;
  overflow: hidden;
  background: linear-gradient(160deg, var(--grn-02-surf), var(--grn-02-bg));
  isolation: isolate;
}

.grn-02__tile::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  opacity: var(--grn-02-grain-op);
  mix-blend-mode: var(--grn-02-grain-blend, multiply);
}

.grn-02__tile--f005::after {
  filter: url(#grn-02-f005);
}

.grn-02__tile--f015::after {
  filter: url(#grn-02-f015);
}

.grn-02__tile--f030::after {
  filter: url(#grn-02-f030);
}

.grn-02__tile--f050::after {
  filter: url(#grn-02-f050);
}

.grn-02__tile--f080::after {
  filter: url(#grn-02-f080);
}

.grn-02__tile--f120::after {
  filter: url(#grn-02-f120);
}

.grn-02__tile--f160::after {
  filter: url(#grn-02-f160);
}

.grn-02__tile--o1::after {
  filter: url(#grn-02-o1);
}

.grn-02__tile--o2::after {
  filter: url(#grn-02-o2);
}

.grn-02__tile--o3::after {
  filter: url(#grn-02-f080);
}

.grn-02__tile--o4::after {
  filter: url(#grn-02-o4);
}

.grn-02__tile--aniso-v::after {
  filter: url(#grn-02-aniso-v);
  opacity: 0.85;
}

.grn-02__tile--aniso-h::after {
  filter: url(#grn-02-aniso-h);
  opacity: 0.85;
}

.grn-02__val {
  font: 500 0.9rem/1 var(--grn-02-font-mono);
  letter-spacing: 0.02em;
}

.grn-02__tag {
  font-size: 0.74rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--grn-02-mut);
}

.grn-02__step--ship .grn-02__tile {
  border-color: var(--grn-02-acc);
  box-shadow: 0 0 0 2px color-mix(in oklab, var(--grn-02-acc) 25%, transparent);
}

.grn-02__step--ship .grn-02__tag {
  color: var(--grn-02-acc);
  font-weight: 600;
}

.grn-02__pair {
  display: grid;
  gap: clamp(1.5rem, 4vw, 2.5rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 20rem), 1fr));
}

.grn-02__aniso {
  display: grid;
  gap: clamp(0.6rem, 1.6vw, 1rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 9rem), 1fr));
}

.grn-02__fig {
  margin: 0;
  display: grid;
  gap: 0.4rem;
  min-inline-size: 0;
}

.grn-02__fig figcaption {
  font: 400 0.74rem/1.3 var(--grn-02-font-mono);
  color: var(--grn-02-mut);
}

.grn-02__fig .grn-02__tile {
  block-size: clamp(7rem, 16vw, 9.5rem);
}

.grn-02__dpr {
  display: grid;
  gap: 0.8rem;
  padding: clamp(1.1rem, 3vw, 1.8rem);
  border: 1px solid var(--grn-02-line);
  border-radius: 14px;
  background: var(--grn-02-surf);
}

.grn-02__dpr-body {
  margin: 0;
  max-inline-size: 48rem;
  color: var(--grn-02-mut);
  font-size: 0.92rem;
  text-wrap: pretty;
}

.grn-02__dpr-tile {
  position: relative;
  display: grid;
  align-items: end;
  block-size: clamp(6rem, 14vw, 8.5rem);
  border-radius: 10px;
  overflow: hidden;
  padding: 0.7rem 0.9rem;
  background: linear-gradient(120deg, var(--grn-02-acc), color-mix(in oklab, var(--grn-02-acc) 35%, var(--grn-02-surf)));
  isolation: isolate;
}

.grn-02__dpr-tile::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  filter: url(#grn-02-f080);
  opacity: 0.55;
  mix-blend-mode: overlay;
}

.grn-02__dpr-label {
  position: relative;
  z-index: 1;
  font: 500 0.72rem/1 var(--grn-02-font-mono);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #fffdf8;
}

@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 2dppx) {
  .grn-02__dpr-tile::after {
    filter: url(#grn-02-f120);
    opacity: 0.62;
  }
}

.grn-02__tile {
  transition: transform 300ms cubic-bezier(0.22, 1, 0.36, 1);
}

@media (hover: hover) and (pointer: fine) {
  .grn-02__step:hover .grn-02__tile,
    .grn-02__fig:hover .grn-02__tile {
    transform: translateY(-3px);
  }
}

@media (prefers-reduced-motion: reduce) {
  .grn-02__tile {
    transition-duration: 1ms;
    transform: none;
  }
}
```
