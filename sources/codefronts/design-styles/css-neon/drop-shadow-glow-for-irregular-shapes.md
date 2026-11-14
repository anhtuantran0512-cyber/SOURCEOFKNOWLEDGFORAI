---
source: "codefronts"
url: "https://codefronts.com/design-styles/css-neon/drop-shadow-glow-for-irregular-shapes/"
title: "Drop Shadow Glow for Irregular Shapes"
section: "design-styles"
category: "css-neon"
category_name: "CSS Neon Effects"
description: "box-shadow follows the element's border box, so a glow on a transparent image, an inline <svg> or a clip-path shape halos the rectangle instead of the artwork."
has_js: "false"
---

Here's a working CSS Neon Effect from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Drop Shadow Glow for Irregular Shapes
Source: https://codefronts.com/design-styles/css-neon/drop-shadow-glow-for-irregular-shapes/

box-shadow follows the element's border box, so a glow on a transparent image, an inline <svg> or a clip-path shape halos the rectangle instead of the artwork. filter: drop-shadow() follows the alpha channel instead. Both are applied to the same shape here, labelled, with the box version visibly wrong — plus what the swap costs you.
## HTML
```html
<section class="nn-02" aria-labelledby="nn-02-heading">
  <div class="nn-02__stage">
    <div class="nn-02__theme">
      <input class="nn-02__tin" type="checkbox" id="nn-02-theme">
      <label class="nn-02__tlab" for="nn-02-theme">
        <svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M8 1.5v2M8 12.5v2M1.5 8h2M12.5 8h2M3.4 3.4l1.4 1.4M11.2 11.2l1.4 1.4M12.6 3.4l-1.4 1.4M4.8 11.2l-1.4 1.4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"></path><circle cx="8" cy="8" r="2.6" fill="none" stroke="currentColor" stroke-width="1.5"></circle></svg>
        Flip light / dark
      </label>
    </div>
    <header class="nn-02__head">
      <p class="nn-02__kicker">Border box vs alpha channel</p>
      <h2 class="nn-02__heading" id="nn-02-heading">Glow on a shape that is not a rectangle</h2>
      <p class="nn-02__sub">The same beacon mark, the same hue, the same blur budget &mdash; painted from two different geometries.</p>
    </header>

    <div class="nn-02__compare">
      <figure class="nn-02__cell">
        <figcaption class="nn-02__caption">
          <span class="nn-02__tag nn-02__tag--bad">box-shadow</span>
          Halos the element box, not the artwork
        </figcaption>
        <div class="nn-02__well">
          <div class="nn-02__mark nn-02__mark--box">
            <svg viewBox="0 0 48 48" aria-hidden="true" focusable="false">
              <path d="M24 3 30 18 45 24 30 30 24 45 18 30 3 24 18 18Z" fill="currentColor"></path>
            </svg>
          </div>
        </div>
        <p class="nn-02__mono">box-shadow: 0 0 6px, 0 0 18px &mdash; the rectangle glows</p>
      </figure>

      <figure class="nn-02__cell">
        <figcaption class="nn-02__caption">
          <span class="nn-02__tag nn-02__tag--good">filter: drop-shadow</span>
          Traces the alpha, so the glow follows the strokes
        </figcaption>
        <div class="nn-02__well">
          <div class="nn-02__mark nn-02__mark--drop">
            <svg viewBox="0 0 48 48" aria-hidden="true" focusable="false">
              <path d="M24 3 30 18 45 24 30 30 24 45 18 30 3 24 18 18Z" fill="currentColor"></path>
            </svg>
          </div>
        </div>
        <p class="nn-02__mono">filter: drop-shadow(0 0 6px) drop-shadow(0 0 18px)</p>
      </figure>
    </div>

    <div class="nn-02__notes">
      <div class="nn-02__note">
        <h3 class="nn-02__ntitle">The clip-path case is worse than a misplaced halo</h3>
        <p class="nn-02__ntext">A clip cuts everything the element paints, including its own <code>box-shadow</code>. The glow does not move to the wrong place &mdash; it stops existing.</p>
        <div class="nn-02__clips">
          <div class="nn-02__clipcell">
            <div class="nn-02__blade nn-02__blade--clipped"></div>
            <p class="nn-02__clabel">clip-path + box-shadow &mdash; shadow clipped away</p>
          </div>
          <div class="nn-02__clipcell">
            <div class="nn-02__blade nn-02__blade--filtered"></div>
            <p class="nn-02__clabel">clip-path + drop-shadow &mdash; glow follows the silhouette</p>
          </div>
        </div>
      </div>

      <div class="nn-02__note nn-02__note--cost">
        <h3 class="nn-02__ntitle">What the swap costs</h3>
        <ul class="nn-02__costs">
          <li>Each <code>drop-shadow()</code> rasterises and blurs the element again.</li>
          <li>Blur time scales with blurred area, so wide blooms on large elements hurt most.</li>
          <li>Two functions is the practical limit before the stack blurs its own core.</li>
          <li>Never animate the filter string; animate <code>opacity</code> on a built glow layer.</li>
        </ul>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.nn-02 {
  --nn-02-bad: #f4a4a4;
  --nn-02-warn: #f0c88a;
  --nn-02-spec-neon: #ffb028;
}

@media (prefers-color-scheme: light) {
  .nn-02 {
    --nn-02-bad: #a12a20;
    --nn-02-warn: #78490a;
  }

  .nn-02:has(#nn-02-theme:checked) {
    --nn-02-bad: #f4a4a4;
    --nn-02-warn: #f0c88a;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-02:has(#nn-02-theme:checked) {
    --nn-02-bad: #a12a20;
    --nn-02-warn: #78490a;
  }
}

.nn-02[data-theme="light"] {
  --nn-02-bad: #a12a20;
  --nn-02-warn: #78490a;
}

.nn-02 {
  --nn-02-spec-ink: #edf1fa;
  --nn-02-spec-dim: #8f9db9;
}

.nn-02__theme {
  position: absolute;
  inset-block-start: clamp(10px, 2vw, 18px);
  inset-inline-end: clamp(10px, 2vw, 18px);
  z-index: 5;
  display: flex;
  justify-content: flex-end;
}

.nn-02__tin {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.nn-02__tlab {
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

.nn-02__tlab svg {
  width: .9rem;
  height: .9rem;
  flex: none;
}

.nn-02__tlab:hover {
  opacity: 1;
}

.nn-02__tin:focus-visible + .nn-02__tlab {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}

@media (prefers-color-scheme: light) {
  .nn-02:has(#nn-02-theme:checked) {
    --nn-02-bg: #070c18;
    --nn-02-well: #0a1122;
    --nn-02-line: #1c2740;
    --nn-02-ink: #edf1fa;
    --nn-02-muted: #8f9db9;
    --nn-02-neon: #ffb028;
  }
}

@media (prefers-color-scheme: dark) {
  .nn-02:has(#nn-02-theme:checked) {
    --nn-02-bg: #e7e9f0;
    --nn-02-well: #1a2135;
    --nn-02-line: #c2c8d6;
    --nn-02-ink: #131725;
    --nn-02-muted: #4b5470;
    --nn-02-neon: #8a5200;
  }
}

.nn-02 {
  --nn-02-hue: 62;
  --nn-02-bg: #070c18;
  --nn-02-well: #0a1122;
  --nn-02-line: #1c2740;
  --nn-02-ink: #edf1fa;
  --nn-02-muted: #8f9db9;
  --nn-02-neon: #ffb028;
  --nn-02-core: rgba(255, 176, 40, .9);
  --nn-02-halo: rgba(255, 176, 40, .45);
  --nn-02-font-display: "Avenir Next Condensed", "Roboto Condensed", "Arial Narrow", system-ui, sans-serif;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: block;
  box-sizing: border-box;
  background: var(--nn-02-bg);
  color: var(--nn-02-ink);
  font-family: system-ui, sans-serif;
}

.nn-02 *,
.nn-02 *::before,
.nn-02 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(50% 0.1 200)) {
  .nn-02 {
    --nn-02-bg: oklch(15% 0.03 265);
    --nn-02-well: oklch(18.5% 0.038 265);
    --nn-02-line: oklch(29% 0.045 265);
    --nn-02-ink: oklch(96% 0.012 265);
    --nn-02-muted: oklch(71% 0.03 265);
    --nn-02-neon: oklch(83% 0.16 var(--nn-02-hue));
    --nn-02-core: oklch(86% 0.17 var(--nn-02-hue) / .9);
    --nn-02-halo: oklch(80% 0.16 var(--nn-02-hue) / .45);
  }
}

@media (prefers-color-scheme: light) {
  .nn-02 {
    --nn-02-bg: #e7e9f0;
    --nn-02-well: #1a2135;
    --nn-02-line: #c2c8d6;
    --nn-02-ink: #131725;
    --nn-02-muted: #4b5470;
    --nn-02-neon: #8a5200;
  }
}

.nn-02[data-theme="light"] {
  --nn-02-bg: #e7e9f0;
  --nn-02-well: #1a2135;
  --nn-02-line: #c2c8d6;
  --nn-02-ink: #131725;
  --nn-02-muted: #4b5470;
  --nn-02-neon: #8a5200;
}

.nn-02[data-theme="dark"] {
  --nn-02-bad: #f4a4a4;
  --nn-02-warn: #f0c88a;
  --nn-02-bg: #070c18;
  --nn-02-well: #0a1122;
  --nn-02-line: #1c2740;
  --nn-02-ink: #edf1fa;
  --nn-02-muted: #8f9db9;
  --nn-02-neon: #ffb028;
}

.nn-02__stage {
  max-width: 68rem;
  margin: 0 auto;
  padding: clamp(1.25rem, 4vw, 1.75rem) clamp(1rem, 4vw, 1.75rem) clamp(1.75rem, 5vw, 2.25rem);
  display: grid;
  gap: clamp(1.25rem, 3.5vw, 1.75rem);
}

.nn-02__kicker {
  margin: 0 0 .4rem;
  font-family: var(--nn-02-font-display);
  font-size: .82rem;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--nn-02-neon);
}

.nn-02__heading {
  margin: 0;
  font-family: var(--nn-02-font-display);
  font-size: clamp(1.6rem, 6vw, 2.6rem);
  font-weight: 600;
  letter-spacing: .01em;
  text-transform: uppercase;
  text-wrap: balance;
}

.nn-02__sub {
  margin: .5rem 0 0;
  max-width: 40rem;
  font-size: .9rem;
  line-height: 1.6;
  color: var(--nn-02-muted);
  text-wrap: pretty;
}

.nn-02__compare {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr;
}

@media (min-width: 50rem) {
  .nn-02__compare {
    grid-template-columns: 1fr 1fr;
  }
}

.nn-02__cell {
  margin: 0;
  display: grid;
  gap: .6rem;
  min-inline-size: 0;
}

.nn-02__caption {
  display: flex;
  align-items: center;
  gap: .55rem;
  flex-wrap: wrap;
  font-size: .78rem;
  color: var(--nn-02-muted);
  min-inline-size: 0;
}

.nn-02__tag {
  padding: .2rem .45rem;
  border: 1px solid var(--nn-02-line);
  font-family: var(--nn-02-font-display);
  font-size: .68rem;
  letter-spacing: .12em;
  text-transform: uppercase;
}

.nn-02__tag--bad {
  color: var(--nn-02-bad);
  border-color: #46232c;
}

.nn-02__tag--good {
  color: var(--nn-02-neon);
  border-color: color-mix(in srgb, var(--nn-02-neon) 45%, transparent);
}

.nn-02__well {
  display: grid;
  place-items: center;
  min-height: clamp(9rem, 26vw, 12rem);
  padding: clamp(1.25rem, 5vw, 2.25rem);
  border: 1px solid var(--nn-02-line);
  background: var(--nn-02-well);
  overflow: hidden;
}

.nn-02__mark {
  color: var(--nn-02-spec-neon);
  line-height: 0;
}

.nn-02__mark svg {
  width: clamp(3rem, 12vw, 4.5rem);
  height: auto;
  display: block;
}

.nn-02__mark--box {
  box-shadow: 0 0 .38rem var(--nn-02-core), 0 0 clamp(.75rem, 3vw, 1.15rem) var(--nn-02-halo);
}

.nn-02__mark--drop {
  filter: drop-shadow(0 0 .38rem var(--nn-02-core)) drop-shadow(0 0 clamp(.75rem, 3vw, 1.15rem) var(--nn-02-halo));
}

.nn-02__mono {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: .68rem;
  line-height: 1.5;
  color: var(--nn-02-muted);
  overflow-wrap: anywhere;
}

.nn-02__notes {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr;
}

@media (min-width: 58rem) {
  .nn-02__notes {
    grid-template-columns: 1.5fr 1fr;
  }
}

.nn-02__note {
  padding: 1rem 1.1rem;
  border: 1px solid var(--nn-02-line);
  min-inline-size: 0;
}

.nn-02__ntitle {
  margin: 0 0 .4rem;
  font-family: var(--nn-02-font-display);
  font-size: 1rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: .06em;
}

.nn-02__ntext {
  margin: 0 0 1rem;
  font-size: .82rem;
  line-height: 1.6;
  color: var(--nn-02-muted);
  text-wrap: pretty;
}

.nn-02__ntext code,
.nn-02__costs code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .95em;
  color: var(--nn-02-neon);
}

.nn-02__clips {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr;
}

@media (min-width: 30rem) {
  .nn-02__clips {
    grid-template-columns: 1fr 1fr;
  }
}

.nn-02__clipcell {
  display: grid;
  gap: .5rem;
  justify-items: center;
  min-inline-size: 0;
}

.nn-02__blade {
  width: 100%;
  max-width: 9rem;
  aspect-ratio: 3 / 2;
  background: var(--nn-02-spec-neon);
  clip-path: polygon(0 0, 100% 22%, 78% 100%, 14% 76%);
}

.nn-02__blade--clipped {
  box-shadow: 0 0 .38rem var(--nn-02-core), 0 0 1.5rem var(--nn-02-halo);
}

.nn-02__blade--filtered {
  filter: drop-shadow(0 0 .38rem var(--nn-02-core)) drop-shadow(0 0 clamp(.75rem, 3vw, 1.15rem) var(--nn-02-halo));
}

.nn-02__clabel {
  margin: 0;
  font-size: .72rem;
  line-height: 1.45;
  text-align: center;
  color: var(--nn-02-muted);
}

.nn-02__costs {
  margin: 0;
  padding-left: 1.1rem;
  display: grid;
  gap: .5rem;
  font-size: .82rem;
  line-height: 1.55;
  color: var(--nn-02-muted);
}

.nn-02__costs li::marker {
  color: var(--nn-02-neon);
}
```
