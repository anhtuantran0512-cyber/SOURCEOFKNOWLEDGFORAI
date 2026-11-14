---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/css-glow-anatomy-with-layered-box-shadow/"
title: "CSS Glow Anatomy with Layered Box Shadow"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "The reference build the rest of this collection borrows from."
has_js: "false"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Glow Anatomy with Layered Box Shadow
Source: https://codefronts.com/design-styles/css-neon/css-glow-anatomy-with-layered-box-shadow/

The reference build the rest of this collection borrows from. One element carries one annotated shadow stack, so you can see why a single large blur reads as a coloured smudge while three stacked shadows — a tight bright core, a mid halo, a wide dim bloom — read as emitted light. Each layer is labelled with its offset, blur, spread and alpha.
## HTML
```html
<section class="nn-01" aria-labelledby="nn-01-heading">
  <div class="nn-01__stage">
    <div class="nn-01__theme">
      <input class="nn-01__tin" type="checkbox" id="nn-01-theme">
      <label class="nn-01__tlab" for="nn-01-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-01__head">
      <p class="nn-01__kicker">core &middot; halo &middot; bloom</p>
      <h2 class="nn-01__heading" id="nn-01-heading">A glow is three shadows, not one</h2>
      <p class="nn-01__sub">Same element, same hue, same ground. The only difference is how the blur is distributed.</p>
    </header>

    <div class="nn-01__compare">
      <figure class="nn-01__cell">
        <figcaption class="nn-01__caption">
          <span class="nn-01__tag nn-01__tag--bad">One layer</span>
          Single 48px blur &mdash; reads as a smudge
        </figcaption>
        <div class="nn-01__well">
          <div class="nn-01__chip nn-01__chip--single">orbit-api</div>
        </div>
        <p class="nn-01__mono">box-shadow: 0 0 48px rgba(34,211,238,.55)</p>
      </figure>

      <figure class="nn-01__cell">
        <figcaption class="nn-01__caption">
          <span class="nn-01__tag nn-01__tag--good">Three layers</span>
          Tight core, mid halo, wide dim bloom &mdash; reads as light
        </figcaption>
        <div class="nn-01__well">
          <div class="nn-01__chip nn-01__chip--stack">orbit-api</div>
        </div>
        <p class="nn-01__mono">box-shadow: core, halo, bloom</p>
      </figure>
    </div>

    <ol class="nn-01__layers">
      <li class="nn-01__layer">
        <span class="nn-01__swatch nn-01__swatch--core" aria-hidden="true"></span>
        <div class="nn-01__ltext">
          <h3 class="nn-01__ltitle">1 &mdash; Core</h3>
          <p class="nn-01__lnote">Defines where the light appears to come from. Steep, almost opaque.</p>
        </div>
        <dl class="nn-01__vals">
          <div><dt>offset</dt><dd>0 0</dd></div>
          <div><dt>blur</dt><dd>6px</dd></div>
          <div><dt>spread</dt><dd>0</dd></div>
          <div><dt>alpha</dt><dd>.95</dd></div>
        </dl>
      </li>
      <li class="nn-01__layer">
        <span class="nn-01__swatch nn-01__swatch--halo" aria-hidden="true"></span>
        <div class="nn-01__ltext">
          <h3 class="nn-01__ltitle">2 &mdash; Halo</h3>
          <p class="nn-01__lnote">Carries the falloff. Roughly half the core alpha, three times the blur.</p>
        </div>
        <dl class="nn-01__vals">
          <div><dt>offset</dt><dd>0 0</dd></div>
          <div><dt>blur</dt><dd>20px</dd></div>
          <div><dt>spread</dt><dd>0</dd></div>
          <div><dt>alpha</dt><dd>.5</dd></div>
        </dl>
      </li>
      <li class="nn-01__layer">
        <span class="nn-01__swatch nn-01__swatch--bloom" aria-hidden="true"></span>
        <div class="nn-01__ltext">
          <h3 class="nn-01__ltitle">3 &mdash; Bloom</h3>
          <p class="nn-01__lnote">Ambient wash. Keep it under .3 alpha or it flattens the other two.</p>
        </div>
        <dl class="nn-01__vals">
          <div><dt>offset</dt><dd>0 0</dd></div>
          <div><dt>blur</dt><dd>52px</dd></div>
          <div><dt>spread</dt><dd>4px</dd></div>
          <div><dt>alpha</dt><dd>.28</dd></div>
        </dl>
      </li>
    </ol>

    <p class="nn-01__rule">Glow is additive brightness, so it only reads as light against a dark ground. On white there is nothing to add to and the same stack renders as a blurry coloured shadow.</p>
  </div>
</section>
```
## CSS
```css
.nn-01 {
  --nn-01-bad: #f4a4a4;
  --nn-01-warn: #f0c88a;
  --nn-01-spec-neon: #22d3ee;
}

@media (prefers-color-scheme: light) {
  .nn-01 {
    --nn-01-bad: #a12a20;
    --nn-01-warn: #78490a;
  }

  .nn-01:has(#nn-01-theme:checked) {
    --nn-01-bad: #f4a4a4;
    --nn-01-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-01:has(#nn-01-theme:checked) {
    --nn-01-bad: #a12a20;
    --nn-01-warn: #78490a;
  }
}

.nn-01[data-theme="light"] {
  --nn-01-bad: #a12a20;
  --nn-01-warn: #78490a;
}

.nn-01 {
  --nn-01-spec-ink: #eaf5f8;
  --nn-01-spec-dim: #97a6b4;
}

.nn-01__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-01__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-01__tlab {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  min-height: 44px;
  padding: 0 .8rem;
  border: 1px solid currentColor;
  font-size: .7rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  cursor: pointer;
  opacity: .7;
}

.nn-01__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-01__tlab:hover {
  opacity: 1;
}

.nn-01__tin:focus-visible + .nn-01__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-01:has(#nn-01-theme:checked) {
    --nn-01-bg: #08090c;
    --nn-01-well: #0c0e13;
    --nn-01-line: #1e2430;
    --nn-01-ink: #eaf5f8;
    --nn-01-muted: #97a6b4;
    --nn-01-neon: #22d3ee;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-01:has(#nn-01-theme:checked) {
    --nn-01-bg: #e9ecef;
    --nn-01-well: #23282f;
    --nn-01-line: #c3cad2;
    --nn-01-ink: #14171c;
    --nn-01-muted: #4d5764;
    --nn-01-neon: #0e7490;
  }
}

.nn-01 {
  --nn-01-hue: 195;
  --nn-01-bg: #08090c;
  --nn-01-well: #0c0e13;
  --nn-01-line: #1e2430;
  --nn-01-ink: #eaf5f8;
  --nn-01-muted: #97a6b4;
  --nn-01-neon: #22d3ee;
  --nn-01-core: rgba(34, 211, 238, .95);
  --nn-01-halo: rgba(34, 211, 238, .5);
  --nn-01-bloom: rgba(34, 211, 238, .28);
  --nn-01-font-display: ui-monospace, "JetBrains Mono", "SFMono-Regular", Menlo, monospace;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-01-bg);
  color: var(--nn-01-ink);
  font-family: system-ui, sans-serif;
}

.nn-01 *,
.nn-01 *::before,
.nn-01 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-01 {
    --nn-01-bg: oklch(15% 0.012 255);
    --nn-01-well: oklch(18% 0.016 255);
    --nn-01-line: oklch(28% 0.02 250);
    --nn-01-ink: oklch(96% 0.014 210);
    --nn-01-muted: oklch(72% 0.02 235);
    --nn-01-neon: oklch(85% 0.15 var(--nn-01-hue));
    --nn-01-core: oklch(88% 0.16 var(--nn-01-hue) / .95);
    --nn-01-halo: oklch(82% 0.15 var(--nn-01-hue) / .5);
    --nn-01-bloom: oklch(78% 0.14 var(--nn-01-hue) / .28);
  }
}

@media (prefers-color-scheme: light) {
  .nn-01 {
    --nn-01-bg: #e9ecef;
    --nn-01-well: #23282f;
    --nn-01-line: #c3cad2;
    --nn-01-ink: #14171c;
    --nn-01-muted: #4d5764;
    --nn-01-neon: #0e7490;
  }
}

.nn-01[data-theme="light"] {
  --nn-01-bg: #e9ecef;
  --nn-01-well: #23282f;
  --nn-01-line: #c3cad2;
  --nn-01-ink: #14171c;
  --nn-01-muted: #4d5764;
  --nn-01-neon: #0e7490;
}

.nn-01[data-theme="dark"] {
  --nn-01-bad: #f4a4a4;
  --nn-01-warn: #f0c88a;
  --nn-01-bg: #08090c;
  --nn-01-well: #0c0e13;
  --nn-01-line: #1e2430;
  --nn-01-ink: #eaf5f8;
  --nn-01-muted: #97a6b4;
  --nn-01-neon: #22d3ee;
}

.nn-01__stage {
  max-width: 66rem;
  margin: 0 auto;
  padding: clamp(1.5rem, 5vw, 2rem) clamp(1.25rem, 5vw, 2rem) clamp(2rem, 6vw, 2.5rem);
  display: grid;
  gap: clamp(1.5rem, 4vw, 2rem);
}

.nn-01__kicker {
  margin: 0 0 .6rem;
  font-family: var(--nn-01-font-display);
  font-size: .72rem;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--nn-01-neon);
}

.nn-01__heading {
  margin: 0;
  font-family: var(--nn-01-font-display);
  font-size: clamp(1.35rem, 5vw, 2.1rem);
  font-weight: 600;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.nn-01__sub {
  margin: .6rem 0 0;
  max-width: 38rem;
  font-size: .92rem;
  line-height: 1.6;
  color: var(--nn-01-muted);
  text-wrap: pretty;
}

.nn-01__compare {
  display: grid;
  gap: 1.25rem;
  grid-template-columns: 1fr;
}

@media (min-width: 52rem) {
  .nn-01__compare {
    grid-template-columns: 1fr 1fr;
  }
}

.nn-01__cell {
  margin: 0;
  display: grid;
  gap: .75rem;
  min-inline-size: 0;
}

.nn-01__caption {
  display: flex;
  align-items: center;
  gap: .6rem;
  flex-wrap: wrap;
  font-size: .78rem;
  color: var(--nn-01-muted);
  min-inline-size: 0;
}

.nn-01__tag {
  padding: .22rem .5rem;
  border: 1px solid var(--nn-01-line);
  border-radius: 2px;
  font-family: var(--nn-01-font-display);
  font-size: .64rem;
  letter-spacing: .1em;
  text-transform: uppercase;
}

.nn-01__tag--bad {
  color: var(--nn-01-bad);
  border-color: #4a2830;
}

.nn-01__tag--good {
  color: var(--nn-01-neon);
  border-color: color-mix(in srgb, var(--nn-01-neon) 40%, transparent);
}

.nn-01__well {
  display: grid;
  place-items: center;
  min-height: clamp(10rem, 30vw, 14rem);
  padding: clamp(1.5rem, 6vw, 3rem);
  border: 1px solid var(--nn-01-line);
  background: var(--nn-01-well);
  overflow: hidden;
}

.nn-01__chip {
  padding: .9rem 1.5rem;
  border: 1px solid var(--nn-01-spec-neon);
  border-radius: 4px;
  background: #0b1418;
  color: var(--nn-01-spec-ink);
  font-family: var(--nn-01-font-display);
  font-size: clamp(.82rem, 2.6vw, .95rem);
  letter-spacing: .04em;
}

.nn-01__chip--single {
  box-shadow: 0 0 clamp(1.5rem, 8vw, 3rem) var(--nn-01-halo);
}

.nn-01__chip--stack {
  box-shadow: 0 0 clamp(.25rem, 1vw, .38rem) var(--nn-01-core), 0 0 clamp(.75rem, 3.5vw, 1.25rem) var(--nn-01-halo), 0 0 clamp(1.75rem, 8vw, 3.25rem) .25rem var(--nn-01-bloom);
}

.nn-01__mono {
  margin: 0;
  font-family: var(--nn-01-font-display);
  font-size: .7rem;
  line-height: 1.5;
  color: var(--nn-01-muted);
  overflow-wrap: anywhere;
}

.nn-01__layers {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0;
  border-top: 1px solid var(--nn-01-line);
}

.nn-01__layer {
  display: grid;
  grid-template-columns: 2.75rem 1fr;
  gap: .9rem 1rem;
  align-items: start;
  padding: 1rem 0;
  border-bottom: 1px solid var(--nn-01-line);
}

@media (min-width: 46rem) {
  .nn-01__layer {
    grid-template-columns: 2.75rem minmax(0, 1fr) auto;
    align-items: center;
  }
}

.nn-01__swatch {
  width: 2.75rem;
  height: 2.75rem;
  border: 1px solid var(--nn-01-spec-neon);
  border-radius: 3px;
  background: #0b1418;
}

.nn-01__swatch--core {
  box-shadow: 0 0 .38rem var(--nn-01-core);
}

.nn-01__swatch--halo {
  box-shadow: 0 0 1.25rem var(--nn-01-halo);
}

.nn-01__swatch--bloom {
  box-shadow: 0 0 2.5rem .25rem var(--nn-01-bloom);
}

.nn-01__ltext {
  min-inline-size: 0;
}

.nn-01__ltitle {
  margin: 0 0 .25rem;
  font-family: var(--nn-01-font-display);
  font-size: .82rem;
  font-weight: 600;
  color: var(--nn-01-neon);
}

.nn-01__lnote {
  margin: 0;
  font-size: .8rem;
  line-height: 1.55;
  color: var(--nn-01-muted);
  text-wrap: pretty;
}

.nn-01__vals {
  margin: 0;
  grid-column: 1 / -1;
  display: flex;
  flex-wrap: wrap;
  gap: .4rem .5rem;
}

@media (min-width: 46rem) {
  .nn-01__vals {
    grid-column: auto;
    justify-content: flex-end;
  }
}

.nn-01__vals div {
  display: flex;
  gap: .35rem;
  align-items: baseline;
  padding: .2rem .45rem;
  border: 1px solid var(--nn-01-line);
  font-family: var(--nn-01-font-display);
  font-size: .66rem;
}

.nn-01__vals dt {
  color: var(--nn-01-muted);
}

.nn-01__vals dd {
  margin: 0;
  color: var(--nn-01-ink);
}

.nn-01__rule {
  margin: 0;
  padding: 1rem 1.1rem;
  border: 1px solid var(--nn-01-line);
  border-left: 2px solid var(--nn-01-neon);
  font-size: .86rem;
  line-height: 1.6;
  color: var(--nn-01-ink);
  text-wrap: pretty;
}
```
