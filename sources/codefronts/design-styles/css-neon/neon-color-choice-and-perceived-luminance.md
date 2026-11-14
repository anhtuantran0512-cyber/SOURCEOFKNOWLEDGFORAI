---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/neon-color-choice-and-perceived-luminance/"
title: "Neon Color Choice and Perceived Luminance"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "Why cyan and magenta glow convincingly while a deep blue or a brown reads as mud at identical shadow values."
has_js: "false"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Color Choice and Perceived Luminance
Source: https://codefronts.com/design-styles/css-neon/neon-color-choice-and-perceived-luminance/

Why cyan and magenta glow convincingly while a deep blue or a brown reads as mud at identical shadow values. Perceived luminance varies enormously by hue at the same nominal lightness, so one fixed alpha and blur produces wildly different results across a palette. One recipe is applied to eight hues, the failures are labelled, then the same eight are corrected with oklch().
## HTML
```html
<section class="nn-03" aria-labelledby="nn-03-heading">
  <div class="nn-03__stage">
    <div class="nn-03__theme">
      <input class="nn-03__tin" type="checkbox" id="nn-03-theme">
      <label class="nn-03__tlab" for="nn-03-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-03__head">
      <p class="nn-03__kicker">One recipe &middot; eight hues</p>
      <h2 class="nn-03__heading" id="nn-03-heading">Some hues glow. Others go muddy.</h2>
      <p class="nn-03__sub">Identical blur, identical alpha, identical ground. Only the hue changes &mdash; and that is enough to break the effect.</p>
    </header>

    <section class="nn-03__row" aria-labelledby="nn-03-naive">
      <h3 class="nn-03__rtitle" id="nn-03-naive">
        <span class="nn-03__tag nn-03__tag--bad">Naive</span>
        hsl(h 100% 50%) at a fixed alpha
      </h3>
      <ul class="nn-03__grid">
        <li class="nn-03__item" style="--nn-03-h: 195;"><span class="nn-03__swatch nn-03__swatch--naive"></span><p class="nn-03__name">Cyan</p><p class="nn-03__verdict nn-03__verdict--ok">reads as light</p></li>
        <li class="nn-03__item" style="--nn-03-h: 150;"><span class="nn-03__swatch nn-03__swatch--naive"></span><p class="nn-03__name">Spring</p><p class="nn-03__verdict nn-03__verdict--ok">reads as light</p></li>
        <li class="nn-03__item" style="--nn-03-h: 95;"><span class="nn-03__swatch nn-03__swatch--naive"></span><p class="nn-03__name">Lime</p><p class="nn-03__verdict nn-03__verdict--ok">too hot, blows out</p></li>
        <li class="nn-03__item" style="--nn-03-h: 48;"><span class="nn-03__swatch nn-03__swatch--naive"></span><p class="nn-03__name">Amber</p><p class="nn-03__verdict nn-03__verdict--ok">reads as light</p></li>
        <li class="nn-03__item" style="--nn-03-h: 22;"><span class="nn-03__swatch nn-03__swatch--naive"></span><p class="nn-03__name">Warm red</p><p class="nn-03__verdict nn-03__verdict--warn">dull, needs lift</p></li>
        <li class="nn-03__item" style="--nn-03-h: 322;"><span class="nn-03__swatch nn-03__swatch--naive"></span><p class="nn-03__name">Magenta</p><p class="nn-03__verdict nn-03__verdict--ok">reads as light</p></li>
        <li class="nn-03__item" style="--nn-03-h: 272;"><span class="nn-03__swatch nn-03__swatch--naive"></span><p class="nn-03__name">Violet</p><p class="nn-03__verdict nn-03__verdict--warn">dim halo</p></li>
        <li class="nn-03__item" style="--nn-03-h: 245;"><span class="nn-03__swatch nn-03__swatch--naive"></span><p class="nn-03__name">Deep blue</p><p class="nn-03__verdict nn-03__verdict--bad">muddy &mdash; no headroom</p></li>
      </ul>
    </section>

    <section class="nn-03__row" aria-labelledby="nn-03-fixed">
      <h3 class="nn-03__rtitle" id="nn-03-fixed">
        <span class="nn-03__tag nn-03__tag--good">Corrected</span>
        oklch(85% 0.16 h) &mdash; lightness held constant
      </h3>
      <ul class="nn-03__grid">
        <li class="nn-03__item" style="--nn-03-h: 195;"><span class="nn-03__swatch nn-03__swatch--fixed"></span><p class="nn-03__name">Cyan</p><p class="nn-03__verdict nn-03__verdict--ok">matched</p></li>
        <li class="nn-03__item" style="--nn-03-h: 150;"><span class="nn-03__swatch nn-03__swatch--fixed"></span><p class="nn-03__name">Spring</p><p class="nn-03__verdict nn-03__verdict--ok">matched</p></li>
        <li class="nn-03__item" style="--nn-03-h: 95;"><span class="nn-03__swatch nn-03__swatch--fixed"></span><p class="nn-03__name">Lime</p><p class="nn-03__verdict nn-03__verdict--ok">matched</p></li>
        <li class="nn-03__item" style="--nn-03-h: 48;"><span class="nn-03__swatch nn-03__swatch--fixed"></span><p class="nn-03__name">Amber</p><p class="nn-03__verdict nn-03__verdict--ok">matched</p></li>
        <li class="nn-03__item" style="--nn-03-h: 22;"><span class="nn-03__swatch nn-03__swatch--fixed"></span><p class="nn-03__name">Warm red</p><p class="nn-03__verdict nn-03__verdict--ok">matched</p></li>
        <li class="nn-03__item" style="--nn-03-h: 322;"><span class="nn-03__swatch nn-03__swatch--fixed"></span><p class="nn-03__name">Magenta</p><p class="nn-03__verdict nn-03__verdict--ok">matched</p></li>
        <li class="nn-03__item" style="--nn-03-h: 272;"><span class="nn-03__swatch nn-03__swatch--fixed"></span><p class="nn-03__name">Violet</p><p class="nn-03__verdict nn-03__verdict--ok">matched</p></li>
        <li class="nn-03__item" style="--nn-03-h: 245;"><span class="nn-03__swatch nn-03__swatch--fixed"></span><p class="nn-03__name">Deep blue</p><p class="nn-03__verdict nn-03__verdict--ok">chroma clamped, still lit</p></li>
      </ul>
    </section>

    <p class="nn-03__rule">When a hue looks weak, lift its lightness &mdash; not the shadow alpha. Alpha flattens the falloff and turns a glow back into a smudge.</p>
  </div>
</section>
```
## CSS
```css
.nn-03 {
  --nn-03-bad: #f4a4a4;
  --nn-03-warn: #f0c88a;
}

@media (prefers-color-scheme: light) {
  .nn-03 {
    --nn-03-bad: #a12a20;
    --nn-03-warn: #78490a;
  }

  .nn-03:has(#nn-03-theme:checked) {
    --nn-03-bad: #f4a4a4;
    --nn-03-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-03:has(#nn-03-theme:checked) {
    --nn-03-bad: #a12a20;
    --nn-03-warn: #78490a;
  }
}

.nn-03[data-theme="light"] {
  --nn-03-bad: #a12a20;
  --nn-03-warn: #78490a;
}

.nn-03 {
  --nn-03-spec-ink: #f5efe9;
  --nn-03-spec-dim: #a2968d;
}

.nn-03__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-03__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-03__tlab {
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

.nn-03__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-03__tlab:hover {
  opacity: 1;
}

.nn-03__tin:focus-visible + .nn-03__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-03:has(#nn-03-theme:checked) {
    --nn-03-bg: #131110;
    --nn-03-well: #1a1716;
    --nn-03-line: #322c29;
    --nn-03-ink: #f5efe9;
    --nn-03-muted: #a2968d;
    --nn-03-accent: #f0dcc8;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-03:has(#nn-03-theme:checked) {
    --nn-03-bg: #edeae6;
    --nn-03-well: #26211f;
    --nn-03-line: #cbc4bd;
    --nn-03-ink: #191614;
    --nn-03-muted: #5a514b;
    --nn-03-accent: #3d3530;
  }
}

.nn-03 {
  --nn-03-bg: #131110;
  --nn-03-well: #1a1716;
  --nn-03-line: #322c29;
  --nn-03-ink: #f5efe9;
  --nn-03-muted: #a2968d;
  --nn-03-accent: #f0dcc8;
  --nn-03-font-display: "Helvetica Neue", "Inter Tight", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-03-bg);
  color: var(--nn-03-ink);
  font-family: system-ui, sans-serif;
}

.nn-03 *,
.nn-03 *::before,
.nn-03 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-03 {
    --nn-03-bg: oklch(17% 0.008 45);
    --nn-03-well: oklch(21% 0.01 45);
    --nn-03-line: oklch(31% 0.012 45);
    --nn-03-ink: oklch(96% 0.012 60);
    --nn-03-muted: oklch(73% 0.014 55);
    --nn-03-accent: oklch(91% 0.03 70);
  }
}

@media (prefers-color-scheme: light) {
  .nn-03 {
    --nn-03-bg: #edeae6;
    --nn-03-well: #26211f;
    --nn-03-line: #cbc4bd;
    --nn-03-ink: #191614;
    --nn-03-muted: #5a514b;
    --nn-03-accent: #3d3530;
  }
}

.nn-03[data-theme="light"] {
  --nn-03-bg: #edeae6;
  --nn-03-well: #26211f;
  --nn-03-line: #cbc4bd;
  --nn-03-ink: #191614;
  --nn-03-muted: #5a514b;
  --nn-03-accent: #3d3530;
}

.nn-03[data-theme="dark"] {
  --nn-03-bad: #f4a4a4;
  --nn-03-warn: #f0c88a;
  --nn-03-bg: #131110;
  --nn-03-well: #1a1716;
  --nn-03-line: #322c29;
  --nn-03-ink: #f5efe9;
  --nn-03-muted: #a2968d;
  --nn-03-accent: #f0dcc8;
}

.nn-03__stage {
  max-width: 72rem;
  margin: 0 auto;
  padding: clamp(1rem, 3.5vw, 1.5rem) clamp(.75rem, 3.5vw, 1.5rem) clamp(1.5rem, 4vw, 2rem);
  display: grid;
  gap: clamp(1rem, 3vw, 1.5rem);
}

.nn-03__kicker {
  margin: 0 0 .35rem;
  font-family: var(--nn-03-font-display);
  font-size: .66rem;
  letter-spacing: .28em;
  text-transform: uppercase;
  color: var(--nn-03-muted);
}

.nn-03__heading {
  margin: 0;
  font-family: var(--nn-03-font-display);
  font-size: clamp(1.3rem, 4.5vw, 1.95rem);
  font-weight: 600;
  letter-spacing: .06em;
  text-transform: uppercase;
  text-wrap: balance;
}

.nn-03__sub {
  margin: .45rem 0 0;
  max-width: 40rem;
  font-size: .85rem;
  line-height: 1.55;
  color: var(--nn-03-muted);
  text-wrap: pretty;
}

.nn-03__row {
  display: grid;
  gap: .6rem;
  padding: .75rem;
  border: 1px solid var(--nn-03-line);
  background: var(--nn-03-well);
}

.nn-03__rtitle {
  margin: 0;
  display: flex;
  align-items: center;
  gap: .5rem;
  flex-wrap: wrap;
  font-family: ui-monospace, Menlo, monospace;
  font-size: .72rem;
  font-weight: 400;
  color: var(--nn-03-spec-dim);
  min-inline-size: 0;
}

.nn-03__tag {
  padding: .15rem .4rem;
  border: 1px solid var(--nn-03-line);
  font-family: var(--nn-03-font-display);
  font-size: .6rem;
  letter-spacing: .16em;
  text-transform: uppercase;
}

.nn-03__tag--bad {
  color: #ff9f9f;
  border-color: #4b2a2a;
}

.nn-03__tag--good {
  color: #a8f0c0;
  border-color: #234634;
}

.nn-03__grid {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: .5rem;
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

@media (min-width: 26rem) {
  .nn-03__grid {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }
}

@media (min-width: 60rem) {
  .nn-03__grid {
    grid-template-columns: repeat(8, minmax(0, 1fr));
  }
}

.nn-03__item {
  display: grid;
  gap: .3rem;
  justify-items: center;
  padding: .75rem .25rem .5rem;
  min-inline-size: 0;
}

.nn-03__swatch {
  width: 100%;
  max-width: 3.5rem;
  aspect-ratio: 1;
  border-radius: 2px;
}

.nn-03__swatch--naive {
  background: hsl(var(--nn-03-h) 100% 50%);
  box-shadow: 0 0 .3rem hsl(var(--nn-03-h) 100% 50% / .9), 0 0 clamp(.75rem, 3vw, 1.4rem) hsl(var(--nn-03-h) 100% 50% / .45);
}

.nn-03__swatch--fixed {
  background: #cccccc;
  box-shadow: 0 0 .3rem rgba(204, 204, 204, .9), 0 0 clamp(.75rem, 3vw, 1.4rem) rgba(204, 204, 204, .45);
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-03__swatch--fixed {
    background: oklch(85% 0.16 var(--nn-03-h));
  }
}

@supports (color: color-mix(in oklab, red, blue)) {
  .nn-03__swatch--fixed {
    box-shadow: 0 0 .3rem color-mix(in oklab, oklch(85% 0.16 var(--nn-03-h)) 90%, transparent), 0 0 clamp(.75rem, 3vw, 1.4rem) color-mix(in oklab, oklch(85% 0.16 var(--nn-03-h)) 45%, transparent);
  }
}

.nn-03__name {
  margin: .2rem 0 0;
  font-size: .72rem;
  font-weight: 600;
  text-align: center;
  color: var(--nn-03-spec-ink);
}

.nn-03__verdict {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: .6rem;
  line-height: 1.35;
  text-align: center;
  color: var(--nn-03-spec-dim);
}

.nn-03__verdict--warn {
  color: #f0c88a;
}

.nn-03__verdict--bad {
  color: #ff9f9f;
}

.nn-03__rule {
  margin: 0;
  padding: .9rem 1rem;
  border: 1px solid var(--nn-03-line);
  border-left: 2px solid var(--nn-03-accent);
  font-size: .84rem;
  line-height: 1.6;
  color: var(--nn-03-ink);
  text-wrap: pretty;
}
```
