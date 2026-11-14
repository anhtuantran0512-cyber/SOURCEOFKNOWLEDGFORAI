---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-grain-texture/tactile-card-surface-with-subtle-noise/"
title: "Tactile Card Surface with Subtle Noise"
section: "design-styles"
category: "css-grain-texture"
category_name: "CSS Grain and Noise Textures"
description: "The reason most card UIs feel like plastic is that they have no surface."
has_js: "false"
---

Here's a working CSS Grain and Noise Texture from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tactile Card Surface with Subtle Noise
Source: https://codefronts.com/design-styles/css-grain-texture/tactile-card-surface-with-subtle-noise/

The reason most card UIs feel like plastic is that they have no surface. This is the fix that costs 4% opacity: a fine noise layer, a one-pixel inset highlight along the top edge, and a shadow tuned to the same light direction. Six product cards, three elevation levels, one texture token — and grain weight that scales with elevation the way real light does.
## HTML
```html
<section class="grn-09" aria-labelledby="grn-09-title">
  <div class="grn-09__theme">
    <input class="grn-09__theme-input" type="checkbox" id="grn-09-theme">
    <label class="grn-09__theme-label" for="grn-09-theme">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/></svg>
      <span class="grn-09__sr">Toggle dark theme</span>
    </label>
  </div>

  <main class="grn-09__shell">
    <header class="grn-09__head">
      <p class="grn-09__kicker">Objects · winter catalogue</p>
      <h1 class="grn-09__h1" id="grn-09-title">Surfaces you can almost feel</h1>
      <p class="grn-09__lede">Every card carries the same noise token at a weight tied to its elevation, plus a lit top edge. Four percent opacity is the entire difference between plastic and material.</p>
    </header>

    <ul class="grn-09__grid">
      <li class="grn-09__card grn-09__card--e3">
        <p class="grn-09__eyebrow">Elevation 3 · 0.055</p>
        <h2 class="grn-09__name">Cast brass desk bell</h2>
        <p class="grn-09__meta">Solid brass, unlacquered. Develops a patina.</p>
        <div class="grn-09__foot"><span class="grn-09__price">£48</span><a class="grn-09__btn" href="#grn-09-title">Add</a></div>
      </li>
      <li class="grn-09__card grn-09__card--e2">
        <p class="grn-09__eyebrow">Elevation 2 · 0.045</p>
        <h2 class="grn-09__name">Linen-bound notebook</h2>
        <p class="grn-09__meta">120gsm, lies flat, 192 pages.</p>
        <div class="grn-09__foot"><span class="grn-09__price">£22</span><a class="grn-09__btn" href="#grn-09-title">Add</a></div>
      </li>
      <li class="grn-09__card grn-09__card--e1">
        <p class="grn-09__eyebrow">Elevation 1 · 0.035</p>
        <h2 class="grn-09__name">Stoneware cup, glazed</h2>
        <p class="grn-09__meta">Thrown in Stoke. Dishwasher safe.</p>
        <div class="grn-09__foot"><span class="grn-09__price">£16</span><a class="grn-09__btn" href="#grn-09-title">Add</a></div>
      </li>
      <li class="grn-09__card grn-09__card--e2">
        <p class="grn-09__eyebrow">Elevation 2 · 0.045</p>
        <h2 class="grn-09__name">Waxed canvas tool roll</h2>
        <p class="grn-09__meta">18oz canvas, brass press studs.</p>
        <div class="grn-09__foot"><span class="grn-09__price">£64</span><a class="grn-09__btn" href="#grn-09-title">Add</a></div>
      </li>
      <li class="grn-09__card grn-09__card--e1">
        <p class="grn-09__eyebrow">Elevation 1 · 0.035</p>
        <h2 class="grn-09__name">Beech drawing board</h2>
        <p class="grn-09__meta">Oiled beech, A3, cleated back.</p>
        <div class="grn-09__foot"><span class="grn-09__price">£38</span><a class="grn-09__btn" href="#grn-09-title">Add</a></div>
      </li>
      <li class="grn-09__card grn-09__card--flat">
        <p class="grn-09__eyebrow">Control · 0</p>
        <h2 class="grn-09__name">The same card, no grain</h2>
        <p class="grn-09__meta">Identical fill, shadow and radius. This is the one that looks like plastic.</p>
        <div class="grn-09__foot"><span class="grn-09__price">—</span><a class="grn-09__btn grn-09__btn--ghost" href="#grn-09-title">Compare</a></div>
      </li>
    </ul>
  </main>
</section>
```
## CSS
```css
.grn-09 {
  --grn-09-noise: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='grn09n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23grn09n)'/%3E%3C/svg%3E");
  --grn-09-bg: #efe9df;
  --grn-09-surf: #fbf8f3;
  --grn-09-line: #ddd4c6;
  --grn-09-ink: #211d17;
  --grn-09-mut: #6c6355;
  --grn-09-acc: #8a5a2b;
  --grn-09-acc: oklch(50% 0.1 62);
  --grn-09-e1: 0.035;
  --grn-09-e2: 0.045;
  --grn-09-e3: 0.055;
  --grn-09-blend: multiply;
  --grn-09-hl: rgba(255, 255, 255, 0.9);
  --grn-09-font-display: "Space Grotesk", "Inter Tight", ui-sans-serif, system-ui, sans-serif;
  --grn-09-font-mono: ui-monospace, "SFMono-Regular", "JetBrains Mono", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  background-image: var(--grn-09-noise), linear-gradient(var(--grn-09-bg), var(--grn-09-bg));
  background-blend-mode: multiply, normal;
  background-color: var(--grn-09-bg);
  color: var(--grn-09-ink);
  font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
  line-height: 1.55;
}

.grn-09 *,
.grn-09 *::before,
.grn-09 *::after {
  box-sizing: border-box;
}

.grn-09 :focus-visible {
  outline: 2px solid var(--grn-09-acc);
  outline-offset: 3px;
}

.grn-09 code {
  font-family: var(--grn-09-font-mono);
  font-size: 0.9em;
}

.grn-09__sr {
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

.grn-09:has(.grn-09__theme-input:checked) {
  --grn-09-bg: #14120f;
  --grn-09-surf: #1e1b16;
  --grn-09-line: #322c23;
  --grn-09-ink: #f3eee5;
  --grn-09-mut: #a79c8b;
  --grn-09-acc: #e0a463;
  --grn-09-acc: oklch(78% 0.12 70);
  --grn-09-blend: overlay;
  --grn-09-hl: rgba(255, 255, 255, 0.14);
  --grn-09-e1: 0.05;
  --grn-09-e2: 0.065;
  --grn-09-e3: 0.08;
}

@media (prefers-color-scheme: dark) {
  .grn-09 {
    --grn-09-bg: #14120f;
    --grn-09-surf: #1e1b16;
    --grn-09-line: #322c23;
    --grn-09-ink: #f3eee5;
    --grn-09-mut: #a79c8b;
    --grn-09-acc: #e0a463;
    --grn-09-acc: oklch(78% 0.12 70);
    --grn-09-blend: overlay;
    --grn-09-hl: rgba(255, 255, 255, 0.14);
    --grn-09-e1: 0.05;
    --grn-09-e2: 0.065;
    --grn-09-e3: 0.08;
  }

  .grn-09:has(.grn-09__theme-input:checked) {
    --grn-09-bg: #efe9df;
    --grn-09-surf: #fbf8f3;
    --grn-09-line: #ddd4c6;
    --grn-09-ink: #211d17;
    --grn-09-mut: #6c6355;
    --grn-09-acc: #8a5a2b;
    --grn-09-acc: oklch(50% 0.1 62);
    --grn-09-blend: multiply;
    --grn-09-hl: rgba(255, 255, 255, 0.9);
    --grn-09-e1: 0.035;
    --grn-09-e2: 0.045;
    --grn-09-e3: 0.055;
  }
}

@media (prefers-color-scheme: light) {
  .grn-09:has(.grn-09__theme-input:checked) {
    --grn-09-bg: #14120f;
    --grn-09-surf: #1e1b16;
    --grn-09-line: #322c23;
    --grn-09-ink: #f3eee5;
    --grn-09-mut: #a79c8b;
    --grn-09-acc: #e0a463;
    --grn-09-acc: oklch(78% 0.12 70);
    --grn-09-blend: overlay;
    --grn-09-hl: rgba(255, 255, 255, 0.14);
    --grn-09-e1: 0.05;
    --grn-09-e2: 0.065;
    --grn-09-e3: 0.08;
  }
}

.grn-09__theme {
  position: absolute;
  inset-block-start: clamp(1rem, 3vw, 1.75rem);
  inset-inline-end: clamp(0.85rem, 3vw, 1.75rem);
  z-index: 40;
}

.grn-09__theme-input {
  position: absolute;
  inset: 0;
  opacity: 0;
  inline-size: 100%;
  block-size: 100%;
  margin: 0;
  cursor: pointer;
}

.grn-09__theme-label {
  display: grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  border: 1px solid var(--grn-09-line);
  border-radius: 999px;
  background: var(--grn-09-surf);
  color: var(--grn-09-ink);
  cursor: pointer;
  box-shadow: inset 0 1px 0 var(--grn-09-hl);
}

.grn-09__theme-label svg {
  inline-size: 20px;
  block-size: 20px;
}

.grn-09__theme-input:focus-visible + .grn-09__theme-label {
  outline: 2px solid var(--grn-09-acc);
  outline-offset: 3px;
}

.grn-09__shell {
  inline-size: min(74rem, calc(100% - clamp(1.5rem, 5vw, 4rem)));
  margin-inline: auto;
  padding-block: clamp(3rem, 8vw, 5.5rem) clamp(2.5rem, 6vw, 4rem);
  display: grid;
  gap: clamp(2rem, 5vw, 3rem);
}

.grn-09__head {
  max-inline-size: 44rem;
  display: grid;
  gap: 0.6rem;
}

.grn-09__kicker {
  margin: 0;
  font: 500 0.72rem/1 var(--grn-09-font-mono);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--grn-09-acc);
}

.grn-09__h1 {
  margin: 0;
  font: 600 clamp(2rem, 5.4vw, 3.4rem)/1.03 var(--grn-09-font-display);
  letter-spacing: -0.035em;
  text-wrap: balance;
}

.grn-09__lede {
  margin: 0;
  max-inline-size: 38rem;
  color: var(--grn-09-mut);
  font-size: clamp(0.95rem, 1.9vw, 1.08rem);
  text-wrap: pretty;
}

.grn-09__grid {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(0.9rem, 2.2vw, 1.4rem);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
}

.grn-09__card {
  position: relative;
  isolation: isolate;
  overflow: hidden;
  display: grid;
  align-content: start;
  gap: 0.45rem;
  padding: clamp(1.1rem, 2.6vw, 1.5rem);
  border-radius: 16px;
  background: var(--grn-09-surf);
  border: 1px solid var(--grn-09-line);
  min-inline-size: 0;
}

.grn-09__card::after {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  background-image: var(--grn-09-noise);
  mix-blend-mode: var(--grn-09-blend);
  opacity: var(--grn-09-w, 0.04);
}

.grn-09__card--e1 {
  --grn-09-w: var(--grn-09-e1);
  box-shadow: inset 0 1px 0 var(--grn-09-hl), 0 1px 2px rgba(30, 22, 12, 0.08);
}

.grn-09__card--e2 {
  --grn-09-w: var(--grn-09-e2);
  box-shadow: inset 0 1px 0 var(--grn-09-hl), 0 6px 14px -8px rgba(30, 22, 12, 0.22);
}

.grn-09__card--e3 {
  --grn-09-w: var(--grn-09-e3);
  box-shadow: inset 0 1px 0 var(--grn-09-hl), 0 18px 40px -22px rgba(30, 22, 12, 0.35);
}

.grn-09__card--flat {
  --grn-09-w: 0;
  box-shadow: inset 0 1px 0 var(--grn-09-hl), 0 6px 14px -8px rgba(30, 22, 12, 0.22);
}

.grn-09__eyebrow {
  margin: 0;
  font: 500 0.68rem/1 var(--grn-09-font-mono);
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--grn-09-mut);
}

.grn-09__name {
  margin: 0;
  font: 600 1.08rem/1.25 var(--grn-09-font-display);
  letter-spacing: -0.015em;
  text-wrap: balance;
}

.grn-09__meta {
  margin: 0;
  color: var(--grn-09-mut);
  font-size: 0.87rem;
  text-wrap: pretty;
}

.grn-09__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  margin-block-start: 0.5rem;
  padding-block-start: 0.75rem;
  border-block-start: 1px solid var(--grn-09-line);
}

.grn-09__price {
  font: 600 1.05rem/1 var(--grn-09-font-mono);
}

.grn-09__btn {
  display: inline-flex;
  align-items: center;
  min-block-size: 44px;
  padding-inline: 1.05rem;
  border-radius: 10px;
  background-image: var(--grn-09-noise), linear-gradient(var(--grn-09-acc), var(--grn-09-acc));
  background-blend-mode: soft-light, normal;
  color: var(--grn-09-surf);
  text-decoration: none;
  font: 600 0.85rem/1 var(--grn-09-font-display);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.22);
}

.grn-09__btn--ghost {
  background-image: none;
  background: transparent;
  border: 1px solid var(--grn-09-line);
  color: var(--grn-09-mut);
  box-shadow: none;
}

.grn-09__btn:hover {
  filter: brightness(1.07);
}

.grn-09__card {
  transition: transform 300ms cubic-bezier(0.22, 1, 0.36, 1), box-shadow 300ms ease;
}

.grn-09__card::after {
  transition: opacity 260ms ease;
}

@media (hover: hover) and (pointer: fine) {
  .grn-09__card:hover {
    transform: translateY(-4px);
  }

  .grn-09__card:hover::after {
    opacity: calc(var(--grn-09-w, 0.04) * 1.35);
  }

  .grn-09__card--e1:hover {
    box-shadow: inset 0 1px 0 var(--grn-09-hl), 0 10px 22px -12px rgba(30, 22, 12, 0.26);
  }
}

@media (prefers-reduced-motion: reduce) {
  .grn-09__card,
    .grn-09__card::after {
    transition-duration: 1ms;
  }

  .grn-09__card:hover {
    transform: none;
  }
}
```
