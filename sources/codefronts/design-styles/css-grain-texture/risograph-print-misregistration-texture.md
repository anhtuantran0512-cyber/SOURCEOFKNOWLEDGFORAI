---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/risograph-print-misregistration-texture/"
title: "Risograph Print Misregistration Texture"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "Risograph printing is cheap, slightly wrong, and beloved for exactly that."
has_js: "false"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Risograph Print Misregistration Texture
Source: https://codefronts.com/design-styles/css-grain-texture/risograph-print-misregistration-texture/

Risograph printing is cheap, slightly wrong, and beloved for exactly that. The look is two spot inks printed in separate passes that never line up perfectly, over-printing where they overlap and showing paper where they miss. This is a full event poster built from that mechanism: two offset ink layers, multiply overprint, and grain that belongs to the paper rather than the ink.
## HTML
```html
<section class="grn-17" aria-labelledby="grn-17-title">
  <div class="grn-17__theme">
    <input class="grn-17__theme-input" type="checkbox" id="grn-17-theme">
    <label class="grn-17__theme-label" for="grn-17-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-17__sr">Toggle dark theme</span>
    </label>
  </div>

  <main class="grn-17__shell">
    <article class="grn-17__poster">
      <span class="grn-17__ink grn-17__ink--a" aria-hidden="true"></span>
      <span class="grn-17__ink grn-17__ink--b" aria-hidden="true"></span>
      <span class="grn-17__paper" aria-hidden="true"></span>

      <div class="grn-17__poster-body">
        <p class="grn-17__pre">Bracken Press · Open studio</p>
        <h1 class="grn-17__h1" id="grn-17-title">
          <span class="grn-17__mis" data-grn-17-text="Two Inks">Two Inks</span>
          <span class="grn-17__mis" data-grn-17-text="One Pass">One Pass</span>
          <span class="grn-17__mis" data-grn-17-text="Slightly Wrong">Slightly Wrong</span>
        </h1>
        <p class="grn-17__lede">Fourteen printers, one drum, and a paper feed that has never once lined up. Two nights of riso, screen and letterpress in the Sackville Yard workshops.</p>
        <dl class="grn-17__facts">
          <div><dt>When</dt><dd>19–20 June, 6pm</dd></div>
          <div><dt>Where</dt><dd>Unit 7, Sackville Yard</dd></div>
          <div><dt>Entry</dt><dd>Free, bring paper</dd></div>
        </dl>
        <a class="grn-17__cta" href="#grn-17-title">Reserve a press slot</a>
      </div>
    </article>

    <section class="grn-17__notes" aria-labelledby="grn-17-h-notes">
      <h2 class="grn-17__h2" id="grn-17-h-notes">How the misregistration is built</h2>
      <ol class="grn-17__steps">
        <li><b>Duplicate the shape set.</b> Two absolutely positioned layers, identical geometry.</li>
        <li><b>Offset each by a few pixels.</b> Different directions. 2–5px reads as print; 8px reads as a bug.</li>
        <li><b>Blend both in multiply.</b> Overlaps darken into a third colour, exactly like overprinted ink.</li>
        <li><b>Put the grain on top.</b> It is the paper showing through, not dust on the ink.</li>
      </ol>
    </section>
  </main>
</section>
```
## CSS
```css
.grn-17 {
  --grn-17-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='190' height='190'%3E%3Cfilter id='grn17n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.7' numOctaves='4' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='190' height='190' filter='url(%23grn17n)'/%3E%3C/svg%3E");
  --grn-17-paper: #f6f1e4;
  --grn-17-paper: oklch(95% 0.02 90);
  --grn-17-ink-a: #ff48a0;
  --grn-17-ink-a: oklch(70% 0.28 5);
  --grn-17-ink-b: #1f4bd8;
  --grn-17-ink-b: oklch(48% 0.24 265);
  --grn-17-ink: #14110c;
  --grn-17-mut: #6a6152;
  --grn-17-line: #ddd4bf;
  --grn-17-shift: 4px;
  --grn-17-grain: 0.09;
  --grn-17-font-display: "Archivo Black", "Anton", "Helvetica Neue", Impact, sans-serif;
  --grn-17-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background: var(--grn-17-paper);
  color: var(--grn-17-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.grn-17 *,
.grn-17 *::before,
.grn-17 *::after {
  box-sizing: border-box;
}

.grn-17 :focus-visible {
  outline: 2px solid var(--grn-17-ink-b);
  outline-offset: 3px;
}

.grn-17 code {
  font-family: var(--grn-17-font-mono);
  font-size: 0.9em;
}

.grn-17__sr {
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

.grn-17:has(.grn-17__theme-input:checked) {
  --grn-17-paper: #14120d;
  --grn-17-paper: oklch(18% 0.01 90);
  --grn-17-ink: #f5efe1;
  --grn-17-mut: #a49a86;
  --grn-17-line: #322c22;
  --grn-17-ink-a: #ff5fae;
  --grn-17-ink-a: oklch(74% 0.26 3);
  --grn-17-ink-b: #4d79ff;
  --grn-17-ink-b: oklch(62% 0.22 268);
  --grn-17-grain: 0.12;
}

@media (prefers-color-scheme: dark) {
  .grn-17 {
    --grn-17-paper: #14120d;
    --grn-17-paper: oklch(18% 0.01 90);
    --grn-17-ink: #f5efe1;
    --grn-17-mut: #a49a86;
    --grn-17-line: #322c22;
    --grn-17-ink-a: #ff5fae;
    --grn-17-ink-a: oklch(74% 0.26 3);
    --grn-17-ink-b: #4d79ff;
    --grn-17-ink-b: oklch(62% 0.22 268);
    --grn-17-grain: 0.12;
  }

  .grn-17:has(.grn-17__theme-input:checked) {
    --grn-17-paper: #f6f1e4;
    --grn-17-paper: oklch(95% 0.02 90);
    --grn-17-ink: #14110c;
    --grn-17-mut: #6a6152;
    --grn-17-line: #ddd4bf;
    --grn-17-ink-a: #ff48a0;
    --grn-17-ink-a: oklch(70% 0.28 5);
    --grn-17-ink-b: #1f4bd8;
    --grn-17-ink-b: oklch(48% 0.24 265);
    --grn-17-grain: 0.09;
  }
}

@media (prefers-color-scheme: light) {
  .grn-17:has(.grn-17__theme-input:checked) {
    --grn-17-paper: #14120d;
    --grn-17-paper: oklch(18% 0.01 90);
    --grn-17-ink: #f5efe1;
    --grn-17-mut: #a49a86;
    --grn-17-line: #322c22;
    --grn-17-ink-a: #ff5fae;
    --grn-17-ink-a: oklch(74% 0.26 3);
    --grn-17-ink-b: #4d79ff;
    --grn-17-ink-b: oklch(62% 0.22 268);
    --grn-17-grain: 0.12;
  }
}

.grn-17__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 60;
}

.grn-17__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-17__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 2px solid var(--grn-17-ink);
  border-radius: 0;
  background: var(--grn-17-paper);
  color: var(--grn-17-ink);
  cursor: pointer;
}

.grn-17__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-17__shell {
  inline-size: min(70rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(2rem, 6vw, 3.5rem) clamp(2.5rem, 6vw, 4rem);
  display: grid;
  gap: clamp(1.8rem, 4.5vw, 2.8rem);
}

.grn-17__poster {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  border: 2px solid var(--grn-17-ink);
  background: var(--grn-17-paper);
  min-block-size: min(80svh, 44rem);
  display: grid;
  align-items: end;
}

.grn-17__ink {
  position: absolute;
  inset: -8%;
  pointer-events: none;
  mix-blend-mode: multiply;
  background-repeat: no-repeat;
}

.grn-17__ink--a {
  translate: calc(var(--grn-17-shift) * -1) calc(var(--grn-17-shift) * 0.6);
  opacity: 0.92;
  background-image: radial-gradient(38% 30% at 74% 16%, var(--grn-17-ink-a) 0 62%, transparent 64%), radial-gradient(26% 22% at 18% 76%, var(--grn-17-ink-a) 0 60%, transparent 62%), linear-gradient(178deg, transparent 0 72%, var(--grn-17-ink-a) 72% 80%, transparent 80%);
}

.grn-17__ink--b {
  translate: var(--grn-17-shift) calc(var(--grn-17-shift) * -0.5);
  rotate: 0.3deg;
  opacity: 0.88;
  background-image: radial-gradient(34% 27% at 66% 22%, var(--grn-17-ink-b) 0 62%, transparent 64%), radial-gradient(30% 24% at 26% 82%, var(--grn-17-ink-b) 0 60%, transparent 62%), linear-gradient(178deg, transparent 0 74%, var(--grn-17-ink-b) 74% 81%, transparent 81%);
}

.grn-17__paper {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image: var(--grn-17-noise);
  opacity: var(--grn-17-grain);
  mix-blend-mode: multiply;
}

.grn-17__poster-body {
  position: relative;
  z-index: 3;
  display: grid;
  gap: 0.9rem;
  padding: clamp(1.5rem, 5vw, 3.2rem);
  max-inline-size: 46rem;
}

.grn-17__pre {
  margin: 0;
  font: 400 0.74rem/1 var(--grn-17-font-mono);
  letter-spacing: 0.2em;
  text-transform: uppercase;
}

.grn-17__h1 {
  margin: 0;
  display: grid;
  gap: 0.1rem;
  font: 400 clamp(2.4rem, 9vw, 5.6rem)/0.9 var(--grn-17-font-display);
  letter-spacing: -0.03em;
  text-transform: uppercase;
}

.grn-17__mis {
  position: relative;
  display: block;
  color: var(--grn-17-ink);
  isolation: isolate;
}

.grn-17__mis::before,
.grn-17__mis::after {
  content: attr(data-grn-17-text);
  position: absolute;
  inset-block-start: 0;
  inset-inline-start: 0;
  pointer-events: none;
  mix-blend-mode: multiply;
}

.grn-17__mis::before {
  color: var(--grn-17-ink-a);
  translate: calc(var(--grn-17-shift) * -0.7) calc(var(--grn-17-shift) * 0.35);
}

.grn-17__mis::after {
  color: var(--grn-17-ink-b);
  translate: calc(var(--grn-17-shift) * 0.7) calc(var(--grn-17-shift) * -0.35);
}

.grn-17__lede {
  margin: 0;
  max-inline-size: 32rem;
  font-size: clamp(0.97rem, 2vw, 1.12rem);
  text-wrap: pretty;
}

.grn-17__facts {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 1.8rem;
  margin: 0.4rem 0 0;
  padding-block-start: 0.9rem;
  border-block-start: 2px solid var(--grn-17-ink);
}

.grn-17__facts > div {
  display: grid;
  gap: 0.1rem;
}

.grn-17__facts dt {
  margin: 0;
  font: 400 0.66rem/1 var(--grn-17-font-mono);
  letter-spacing: 0.14em;
  text-transform: uppercase;
  opacity: 0.7;
}

.grn-17__facts dd {
  margin: 0;
  font: 500 0.98rem/1.2 var(--grn-17-font-mono);
}

.grn-17__cta {
  justify-self: start;
  display: inline-flex;
  align-items: center;
  min-block-size: 50px;
  margin-block-start: 0.4rem;
  padding-inline: 1.5rem;
  border: 2px solid var(--grn-17-ink);
  background: var(--grn-17-ink-a);
  color: #14110c;
  text-decoration: none;
  font: 400 0.9rem/1 var(--grn-17-font-display);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  box-shadow: var(--grn-17-shift) var(--grn-17-shift) 0 var(--grn-17-ink-b);
}

.grn-17__cta:hover {
  translate: 2px 2px;
  box-shadow: 2px 2px 0 var(--grn-17-ink-b);
}

.grn-17__notes {
  display: grid;
  gap: 0.8rem;
  padding: clamp(1.2rem, 3vw, 1.8rem);
  border: 2px solid var(--grn-17-ink);
}

.grn-17__h2 {
  margin: 0;
  font: 400 clamp(1.1rem, 2.8vw, 1.5rem)/1.15 var(--grn-17-font-display);
  text-transform: uppercase;
  letter-spacing: -0.01em;
}

.grn-17__steps {
  margin: 0;
  padding-inline-start: 1.4rem;
  display: grid;
  gap: 0.5rem;
  color: var(--grn-17-mut);
  font-size: 0.92rem;
}

.grn-17__steps b {
  color: var(--grn-17-ink);
  font-weight: 600;
}

.grn-17__cta {
  transition: translate 160ms ease, box-shadow 160ms ease;
}

@media (prefers-reduced-motion: reduce) {
  .grn-17__cta {
    transition-duration: 1ms;
  }
}
```
