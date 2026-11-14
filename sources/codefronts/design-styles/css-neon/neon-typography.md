---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/neon-typography/"
title: "Neon Heading and Display Type Glow"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "Display type as a typographic problem rather than an effect: how stroke weight and letter-spacing govern how much glow a glyph can carry before its counters…"
has_js: "false"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neon Heading and Display Type Glow
Source: https://codefronts.com/design-styles/css-neon/neon-typography/

Display type as a typographic problem rather than an effect: how stroke weight and letter-spacing govern how much glow a glyph can carry before its counters fill in and the whole line smears. Four specimens hold the same glow stack while weight and tracking change, so the failure point is visible instead of theoretical.
## HTML
```html
<section class="nn-10" aria-labelledby="nn-10-heading">
  <div class="nn-10__stage">
    <div class="nn-10__theme">
      <input class="nn-10__tin" type="checkbox" id="nn-10-theme">
      <label class="nn-10__tlab" for="nn-10-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-10__head">
      <p class="nn-10__kicker">Weight &middot; tracking &middot; aperture</p>
      <h2 class="nn-10__heading" id="nn-10-heading">How much glow can a glyph carry?</h2>
      <p class="nn-10__sub">Same stack, same hue, same size on all four lines. Only weight and letter-spacing change &mdash; and that decides whether the word survives.</p>
    </header>

    <ol class="nn-10__ladder">
      <li class="nn-10__step">
        <p class="nn-10__spec nn-10__spec--w300">Meridian</p>
        <div class="nn-10__meta">
          <p class="nn-10__grade nn-10__grade--warn">300 / tracking 0.02em</p>
          <p class="nn-10__note">Strokes are thinner than the core layer, so the glyph starts to dissolve into its own light.</p>
        </div>
      </li>
      <li class="nn-10__step">
        <p class="nn-10__spec nn-10__spec--w500">Meridian</p>
        <div class="nn-10__meta">
          <p class="nn-10__grade nn-10__grade--ok">500 / tracking 0.04em</p>
          <p class="nn-10__note">The working range. Stroke reads as solid, counters stay open, halo sits outside the letter.</p>
        </div>
      </li>
      <li class="nn-10__step">
        <p class="nn-10__spec nn-10__spec--w800">Meridian</p>
        <div class="nn-10__meta">
          <p class="nn-10__grade nn-10__grade--ok">800 / tracking 0.1em</p>
          <p class="nn-10__note">Heavy weights need the extra tracking; without it the halos of adjacent stems merge.</p>
        </div>
      </li>
      <li class="nn-10__step">
        <p class="nn-10__spec nn-10__spec--tight">Meridian</p>
        <div class="nn-10__meta">
          <p class="nn-10__grade nn-10__grade--bad">800 / tracking 0 &mdash; smears</p>
          <p class="nn-10__note">The counters fill and the gaps between letters glow brighter than the strokes. Same stack, no room.</p>
        </div>
      </li>
    </ol>

    <div class="nn-10__rule">
      <p class="nn-10__rtext">Every layer here is sized in <span class="nn-10__code">em</span>, so the light scales with the type: <span class="nn-10__code">0 0 .06em</span> core, <span class="nn-10__code">0 0 .3em</span> halo, <span class="nn-10__code">0 0 .8em</span> bloom.</p>
    </div>
  </div>
</section>
```
## CSS
```css
.nn-10 {
  --nn-10-bad: #f4a4a4;
  --nn-10-warn: #f0c88a;
  --nn-10-spec-neon: #ff6ec7;
}

@media (prefers-color-scheme: light) {
  .nn-10 {
    --nn-10-bad: #a12a20;
    --nn-10-warn: #78490a;
  }

  .nn-10:has(#nn-10-theme:checked) {
    --nn-10-bad: #f4a4a4;
    --nn-10-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-10:has(#nn-10-theme:checked) {
    --nn-10-bad: #a12a20;
    --nn-10-warn: #78490a;
  }
}

.nn-10[data-theme="light"] {
  --nn-10-bad: #a12a20;
  --nn-10-warn: #78490a;
}

.nn-10 {
  --nn-10-spec-ink: #fdeef3;
  --nn-10-spec-dim: #bb8c9c;
}

.nn-10__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-10__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-10__tlab {
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

.nn-10__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-10__tlab:hover {
  opacity: 1;
}

.nn-10__tin:focus-visible + .nn-10__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-10:has(#nn-10-theme:checked) {
    --nn-10-bg: #150409;
    --nn-10-well: #1e070d;
    --nn-10-line: #3a1520;
    --nn-10-ink: #fdeef3;
    --nn-10-muted: #bb8c9c;
    --nn-10-neon: #ff6ec7;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-10:has(#nn-10-theme:checked) {
    --nn-10-bg: #f1e9ec;
    --nn-10-well: #26101a;
    --nn-10-line: #d0bfc6;
    --nn-10-ink: #1a0a10;
    --nn-10-muted: #5e4650;
    --nn-10-neon: #a31462;
  }
}

.nn-10 {
  --nn-10-hue: 340;
  --nn-10-bg: #150409;
  --nn-10-well: #1e070d;
  --nn-10-line: #3a1520;
  --nn-10-ink: #fdeef3;
  --nn-10-muted: #bb8c9c;
  --nn-10-neon: #ff6ec7;
  --nn-10-core-a: .9;
  --nn-10-halo-a: .45;
  --nn-10-bloom-a: .22;
  --nn-10-core: rgba(255, 110, 199, .9);
  --nn-10-halo: rgba(255, 110, 199, .45);
  --nn-10-bloom: rgba(255, 110, 199, .22);
  --nn-10-font-display: "Avenir Next Condensed", "Roboto Condensed", "Arial Narrow", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-10-bg);
  color: var(--nn-10-ink);
  font-family: system-ui, sans-serif;
}

.nn-10 *,
.nn-10 *::before,
.nn-10 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-10 {
    --nn-10-bg: oklch(15% 0.045 12);
    --nn-10-well: oklch(19% 0.055 12);
    --nn-10-line: oklch(30% 0.07 8);
    --nn-10-ink: oklch(96% 0.018 350);
    --nn-10-muted: oklch(74% 0.045 350);
    --nn-10-neon: oklch(78% 0.2 var(--nn-10-hue));
    --nn-10-core: oklch(80% 0.2 var(--nn-10-hue) / var(--nn-10-core-a));
    --nn-10-halo: oklch(76% 0.19 var(--nn-10-hue) / var(--nn-10-halo-a));
    --nn-10-bloom: oklch(72% 0.18 var(--nn-10-hue) / var(--nn-10-bloom-a));
  }
}

@media (prefers-color-scheme: light) {
  .nn-10 {
    --nn-10-bg: #f1e9ec;
    --nn-10-well: #26101a;
    --nn-10-line: #d0bfc6;
    --nn-10-ink: #1a0a10;
    --nn-10-muted: #5e4650;
    --nn-10-neon: #a31462;
  }
}

.nn-10[data-theme="light"] {
  --nn-10-bg: #f1e9ec;
  --nn-10-well: #26101a;
  --nn-10-line: #d0bfc6;
  --nn-10-ink: #1a0a10;
  --nn-10-muted: #5e4650;
  --nn-10-neon: #a31462;
}

.nn-10[data-theme="dark"] {
  --nn-10-bad: #f4a4a4;
  --nn-10-warn: #f0c88a;
  --nn-10-bg: #150409;
  --nn-10-well: #1e070d;
  --nn-10-line: #3a1520;
  --nn-10-ink: #fdeef3;
  --nn-10-muted: #bb8c9c;
  --nn-10-neon: #ff6ec7;
}

.nn-10__stage {
  max-width: 68rem;
  margin: 0 auto;
  padding: clamp(1.75rem, 5vw, 2.75rem) clamp(1.25rem, 5vw, 2.5rem) clamp(2.25rem, 6vw, 3rem);
  display: grid;
  gap: clamp(1.75rem, 4.5vw, 2.5rem);
}

.nn-10__kicker {
  margin: 0 0 .5rem;
  font-family: var(--nn-10-font-display);
  font-size: .8rem;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--nn-10-neon);
}

.nn-10__heading {
  margin: 0;
  font-family: var(--nn-10-font-display);
  font-size: clamp(1.6rem, 6vw, 2.6rem);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: .02em;
  text-wrap: balance;
}

.nn-10__sub {
  margin: .6rem 0 0;
  max-width: 42rem;
  font-size: .92rem;
  line-height: 1.65;
  color: var(--nn-10-muted);
  text-wrap: pretty;
}

.nn-10__ladder {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 0;
  border-top: 1px solid var(--nn-10-line);
}

.nn-10__step {
  display: grid;
  gap: 1rem;
  align-items: center;
  padding: clamp(1.5rem, 4vw, 2.25rem) 0;
  border-bottom: 1px solid var(--nn-10-line);
  grid-template-columns: 1fr;
}

@media (min-width: 54rem) {
  .nn-10__step {
    grid-template-columns: minmax(0, 1fr) minmax(0, 18rem);
    gap: 2rem;
  }
}

.nn-10__spec {
  margin: 0;
  font-family: var(--nn-10-font-display);
  font-size: clamp(2.4rem, 12vw, 4.5rem);
  line-height: 1;
  color: var(--nn-10-ink);
  text-transform: uppercase;
  min-inline-size: 0;
  text-shadow: 0 0 .06em var(--nn-10-core), 0 0 .3em var(--nn-10-halo), 0 0 .8em var(--nn-10-bloom);
}

.nn-10__spec--w300 {
  font-weight: 300;
  letter-spacing: .02em;
}

.nn-10__spec--w500 {
  font-weight: 500;
  letter-spacing: .04em;
}

.nn-10__spec--w800 {
  font-weight: 800;
  letter-spacing: .1em;
}

.nn-10__spec--tight {
  font-weight: 800;
  letter-spacing: 0;
}

.nn-10__meta {
  display: grid;
  gap: .4rem;
  min-inline-size: 0;
}

.nn-10__grade {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: .74rem;
  letter-spacing: .04em;
}

.nn-10__grade--ok {
  color: var(--nn-10-neon);
}

.nn-10__grade--warn {
  color: var(--nn-10-warn);
}

.nn-10__grade--bad {
  color: var(--nn-10-bad);
}

.nn-10__note {
  margin: 0;
  font-size: .82rem;
  line-height: 1.6;
  color: var(--nn-10-muted);
  text-wrap: pretty;
}

.nn-10__rule {
  padding: 1.1rem 1.25rem;
  border: 1px solid var(--nn-10-line);
}

.nn-10__rtext {
  margin: 0;
  font-size: .88rem;
  line-height: 1.7;
  color: var(--nn-10-ink);
  text-wrap: pretty;
}

.nn-10__code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .82em;
  color: var(--nn-10-neon);
}
```
