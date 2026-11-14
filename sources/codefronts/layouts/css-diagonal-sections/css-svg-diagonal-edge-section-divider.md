---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-svg-diagonal-edge-section-divider/"
title: "CSS SVG Diagonal Edge Section Divider"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "The same straight diagonal edge, drawn with an inline SVG polygon instead of clip-path."
has_js: "false"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS SVG Diagonal Edge Section Divider
Source: https://codefronts.com/layouts/css-diagonal-sections/css-svg-diagonal-edge-section-divider/

The same straight diagonal edge, drawn with an inline SVG polygon instead of clip-path. preserveAspectRatio="none" stretches the shape to any width so the slope is whatever you specify, at every viewport, with no sub-pixel seam and no dependency on clip-path support. The howItWorks explains exactly when SVG beats a clip — and when it does not.
## HTML
```html
<div class="dgs-20">
  <input class="dgs-20__sronly" type="checkbox" id="dgs-20-dark">
  <label class="dgs-20__theme" for="dgs-20-dark">
    <svg class="dgs-20__i dgs-20__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-20__i dgs-20__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-20__srtext">Toggle dark theme</span>
  </label>
  <fieldset class="dgs-20__ctl">
    <legend class="dgs-20__vh">Edge layers</legend>
    <input class="dgs-20__sr" type="radio" name="dgs-20-l" id="dgs-20-l1"><label for="dgs-20-l1">Single</label>
    <input class="dgs-20__sr" type="radio" name="dgs-20-l" id="dgs-20-l2" checked><label for="dgs-20-l2">Offset</label>
    <input class="dgs-20__sr" type="radio" name="dgs-20-l" id="dgs-20-l3"><label for="dgs-20-l3">Triple</label>
  </fieldset>

  <div class="dgs-20__stage">
    <section class="dgs-20__above" aria-labelledby="dgs-20-a">
      <div class="dgs-20__wrap">
        <p class="dgs-20__eyebrow">Ninth Street Roastery &mdash; est. 2019</p>
        <h2 class="dgs-20__display" id="dgs-20-a">Roasted Tuesday. On your table Thursday.</h2>
        <p class="dgs-20__lede">Single origin, two washed and one natural, cupped every week before it ships. Bags are date-stamped with the roast, not the sell-by.</p>
      </div>
      <svg class="dgs-20__edge" viewBox="0 0 1200 120" preserveAspectRatio="none" aria-hidden="true" focusable="false">
        <polygon class="dgs-20__edge1" points="0,120 1200,0 1200,120"/>
        <polygon class="dgs-20__edge2" points="0,120 1200,12 1200,120"/>
        <polygon class="dgs-20__edge3" points="0,120 1200,26 1200,120"/>
      </svg>
    </section>

    <section class="dgs-20__band" aria-labelledby="dgs-20-b">
      <div class="dgs-20__wrap">
        <p class="dgs-20__eyebrow dgs-20__eyebrow--on">This week on the bar</p>
        <h2 class="dgs-20__h2" id="dgs-20-b">A straight SVG edge, stacked in three inks</h2>
        <p class="dgs-20__body">An SVG polygon does what a clip-path cannot: several edges at once. Three overlapping triangles with <code class="dgs-20__code">preserveAspectRatio: none</code> stretch to any width and print like a mis-registered riso pull &mdash; and because the shape is a polygon, every edge stays perfectly straight.</p>
        <ul class="dgs-20__lots">
          <li>
            <img src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&amp;fit=crop&amp;w=700&amp;q=70" alt="An espresso being poured into a small white cup" width="700" height="500" loading="lazy" decoding="async">
            <strong>Kamwangi AB</strong><span>Kenya &middot; washed</span><em>Blackcurrant, cane sugar</em><b>&pound;14.50</b>
          </li>
          <li>
            <img src="https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&amp;fit=crop&amp;w=700&amp;q=70" alt="Latte art in a ceramic cup on a wooden counter" width="700" height="500" loading="lazy" decoding="async">
            <strong>Finca La Ilusi&oacute;n</strong><span>Colombia &middot; natural</span><em>Cherry, cocoa nib</em><b>&pound;16.00</b>
          </li>
          <li>
            <img src="https://images.unsplash.com/photo-1447933601403-0c6688de566e?auto=format&amp;fit=crop&amp;w=700&amp;q=70" alt="A flat white in a grey cup seen from above" width="700" height="500" loading="lazy" decoding="async">
            <strong>Shakiso</strong><span>Ethiopia &middot; washed</span><em>Jasmine, lemon peel</em><b>&pound;15.25</b>
          </li>
        </ul>
      </div>
    </section>

    <section class="dgs-20__below" aria-labelledby="dgs-20-c">
      <div class="dgs-20__wrap dgs-20__cols">
        <h2 class="dgs-20__h3" id="dgs-20-c">When SVG beats clip-path</h2>
        <p class="dgs-20__note">Layered edges, a stroke along the diagonal, a gradient fill on the wedge alone, or a shape that must be identical in an exported PDF. The trade is one extra element and a <code class="dgs-20__code">viewBox</code> to keep in sync with the band colour.</p>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,[email protected],400;12..96,600;12..96,800&family=Courier+Prime:wght@400;700&display=swap');

.dgs-20 {
  --l2: .55;
  --l3: .3;
  --cream: #f7f1e4;
  --cream2: #ece2ce;
  --ink: #191410;
  --muted: #5d5346;
  --ink-band: #12100e;
  --on-band: #f9f4e8;
  --orange: #ff5b23;
  --teal: #0e7f76;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--cream);
  color: var(--ink);
  font-family: 'Bricolage Grotesque', system-ui, -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

.dgs-20 *,
.dgs-20 *::before,
.dgs-20 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.65 0.2 40)) {
  .dgs-20 {
    --cream: oklch(0.955 0.02 85);
    --cream2: oklch(0.912 0.03 85);
    --ink: oklch(0.2 0.015 60);
    --muted: oklch(0.47 0.02 60);
    --ink-band: oklch(0.175 0.01 60);
    --on-band: oklch(0.965 0.015 85);
    --orange: oklch(0.685 0.2 42);
    --teal: oklch(0.52 0.1 185);
  }
}

.dgs-20__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-20__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.dgs-20__ctl {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 40;
  margin: 0;
  padding: 3px;
  display: flex;
  gap: 3px;
  border: 2px solid var(--ink);
  background: var(--cream);
}

.dgs-20__ctl label {
  min-inline-size: 3rem;
  min-block-size: 2.5rem;
  display: grid;
  place-items: center;
  padding-inline: .75rem;
  font-family: 'Courier Prime', monospace;
  font-size: .74rem;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--muted);
  cursor: pointer;
  transition: background .18s ease, color .18s ease;
}

.dgs-20__ctl label:hover {
  color: var(--ink);
}

.dgs-20__sr:checked + label {
  background: var(--orange);
  color: #fff;
}

.dgs-20__sr:focus-visible + label {
  outline: 2px solid var(--teal);
  outline-offset: 2px;
}

.dgs-20__stage {
  display: flow-root;
}

.dgs-20__wrap {
  inline-size: min(72rem, 100%);
  margin-inline: auto;
}

.dgs-20__above {
  position: relative;
  padding: clamp(3.5rem, 8vw, 6rem) clamp(1.25rem, 5vw, 4rem) clamp(5rem, 12vw, 9rem);
}

.dgs-20__eyebrow {
  margin: 0 0 1rem;
  font-family: 'Courier Prime', monospace;
  font-size: .76rem;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--orange);
}

.dgs-20__eyebrow--on {
  color: var(--orange);
}

.dgs-20__display {
  margin: 0 0 1.1rem;
  max-inline-size: 24ch;
  font-size: clamp(2.2rem, 7vw, 4.4rem);
  font-weight: 800;
  line-height: 1.0;
  letter-spacing: -.04em;
  text-wrap: balance;
}

.dgs-20__lede {
  margin: 0;
  max-inline-size: 52ch;
  font-size: clamp(1.02rem, 2vw, 1.18rem);
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-20__edge {
  position: absolute;
  inset-block-end: -1px;
  inset-inline: 0;
  inline-size: 100%;
  block-size: clamp(2.5rem, 8vw, 7.5rem);
  display: block;
}

.dgs-20__edge1 {
  fill: var(--ink-band);
}

.dgs-20__edge2 {
  fill: var(--orange);
  opacity: var(--l2);
}

.dgs-20__edge3 {
  fill: var(--teal);
  opacity: var(--l3);
}

.dgs-20__band {
  position: relative;
  z-index: 1;
  background: var(--ink-band);
  color: var(--on-band);
  margin-block-start: -1px;
  padding: clamp(2.5rem, 6vw, 4rem) clamp(1.25rem, 5vw, 4rem) clamp(3.5rem, 8vw, 5.5rem);
}

.dgs-20__h2 {
  margin: 0 0 1rem;
  max-inline-size: 26ch;
  font-size: clamp(1.6rem, 4.6vw, 2.7rem);
  font-weight: 600;
  line-height: 1.06;
  letter-spacing: -.035em;
  text-wrap: balance;
}

.dgs-20__body {
  margin: 0 0 clamp(2rem, 5vw, 3rem);
  max-inline-size: 58ch;
  color: rgba(249,244,232,.8);
  text-wrap: pretty;
}

.dgs-20__code {
  font-family: 'Courier Prime', monospace;
  font-size: .88em;
  padding: .1em .35em;
  background: rgba(249,244,232,.14);
}

.dgs-20__lots {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(1rem, 2.5vw, 1.5rem);
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
}

.dgs-20__lots li {
  display: grid;
  gap: .35rem;
  padding-block-end: 1rem;
  border-block-end: 2px solid rgba(249,244,232,.25);
}

.dgs-20__lots img {
  inline-size: 100%;
  block-size: clamp(9rem, 22vw, 12rem);
  object-fit: cover;
  margin-block-end: .6rem;
  background: #2a231d;
  filter: saturate(.85) contrast(1.06);
}

.dgs-20__lots strong {
  font-size: 1.1rem;
  font-weight: 600;
  letter-spacing: -.02em;
}

.dgs-20__lots span {
  font-family: 'Courier Prime', monospace;
  font-size: .74rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--orange);
}

.dgs-20__lots em {
  font-style: normal;
  font-size: .92rem;
  color: rgba(249,244,232,.72);
}

.dgs-20__lots b {
  font-family: 'Courier Prime', monospace;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.dgs-20__below {
  background: var(--cream2);
  padding: clamp(3rem, 7vw, 4.5rem) clamp(1.25rem, 5vw, 4rem) clamp(4rem, 9vw, 6rem);
}

.dgs-20__cols {
  display: grid;
  gap: 1rem clamp(2rem, 6vw, 4rem);
  grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
  align-items: start;
}

.dgs-20__h3 {
  margin: 0;
  font-size: clamp(1.3rem, 3.4vw, 1.9rem);
  font-weight: 600;
  letter-spacing: -.03em;
}

.dgs-20__note {
  margin: 0;
  max-inline-size: 58ch;
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-20__below .dgs-20__code {
  background: rgba(25,20,16,.08);
  color: var(--ink);
}

.dgs-20:has(#dgs-20-l1:checked) {
  --l2: 0;
  --l3: 0;
}

.dgs-20:has(#dgs-20-l3:checked) {
  --l2: .8;
  --l3: .6;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-20 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-20__band {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
    border-block-start: 1px solid CanvasText;
  }

  .dgs-20__edge2,
    .dgs-20__edge3 {
    display: none;
  }

  .dgs-20__edge1 {
    fill: CanvasText;
  }

  .dgs-20__ctl,
    .dgs-20__ctl label {
    border: 1px solid CanvasText;
  }

  .dgs-20__sr:checked + label {
    background: Highlight;
    color: HighlightText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-20__sronly,
.dgs-20__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-20__theme {
  position: absolute;
  inset-block-start: clamp(.85rem, 2.2vw, 1.5rem);
  inset-inline-end: clamp(.85rem, 2.2vw, 1.5rem);
  z-index: 60;
  display: grid;
  place-items: center;
  inline-size: 2.5rem;
  block-size: 2.5rem;
  border-radius: 999px;
  border: 1px solid currentColor;
  color: inherit;
  background: rgba(127,127,127,.16);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  cursor: pointer;
  transition: translate .2s ease;
}

.dgs-20__theme:hover {
  translate: 0 -1px;
}

.dgs-20__sronly:focus-visible + .dgs-20__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-20__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-20__i--sun {
  display: none;
}

.dgs-20:has(#dgs-20-dark:checked) .dgs-20__i--moon {
  display: none;
}

.dgs-20:has(#dgs-20-dark:checked) .dgs-20__i--sun {
  display: block;
}

.dgs-20:has(#dgs-20-dark:checked) {
  --cream: #131410;
  --ink: #f2f2ea;
  --muted: #9fa094;
  --line: #2d2e28;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-20__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-20__theme {
    border-color: CanvasText;
  }
}
```
