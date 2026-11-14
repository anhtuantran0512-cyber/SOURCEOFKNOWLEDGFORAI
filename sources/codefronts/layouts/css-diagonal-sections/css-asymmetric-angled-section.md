---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-asymmetric-angled-section/"
title: "CSS Asymmetric Angled Section"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "The left and right ends of the same edge sit at different depths, so the cut is not a rotation of anything — it cannot be produced by skewY() at any angle."
has_js: "false"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Asymmetric Angled Section
Source: https://codefronts.com/layouts/css-diagonal-sections/css-asymmetric-angled-section/

The left and right ends of the same edge sit at different depths, so the cut is not a rotation of anything — it cannot be produced by skewY() at any angle. This is pure polygon() territory: two independent tokens, one per side, plus a mid-point that lets the edge change slope halfway across. The demo explains the constraint plainly, because that is the search behind it.
## HTML
```html
<div class="dgs-11">
  <input class="dgs-11__sronly" type="checkbox" id="dgs-11-dark">
  <label class="dgs-11__theme" for="dgs-11-dark">
    <svg class="dgs-11__i dgs-11__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-11__i dgs-11__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-11__srtext">Toggle dark theme</span>
  </label>
  <fieldset class="dgs-11__ctl">
    <legend class="dgs-11__vh">Apex controls</legend>
    <input class="dgs-11__sr" type="radio" name="dgs-11-p" id="dgs-11-p1"><label for="dgs-11-p1">22%</label>
    <input class="dgs-11__sr" type="radio" name="dgs-11-p" id="dgs-11-p2" checked><label for="dgs-11-p2">64%</label>
    <input class="dgs-11__sr" type="radio" name="dgs-11-p" id="dgs-11-p3"><label for="dgs-11-p3">88%</label>
  </fieldset>

  <div class="dgs-11__stage">
    <section class="dgs-11__top" aria-labelledby="dgs-11-a">
      <div class="dgs-11__wrap">
        <p class="dgs-11__meta"><span>Ostrava Type</span><span>Release 07 &mdash; Variable</span></p>
        <h2 class="dgs-11__display" id="dgs-11-a">Grotesk<br><em>Ostrava</em></h2>
        <p class="dgs-11__lede">Nine weights, one variable axis, and a display cut with the spacing pulled tight enough for a poster at 400&nbsp;pt.</p>
      </div>
    </section>

    <section class="dgs-11__band" aria-labelledby="dgs-11-b">
      <div class="dgs-11__wrap">
        <div class="dgs-11__asym">
          <p class="dgs-11__num" aria-hidden="true">07</p>
          <div>
            <h2 class="dgs-11__h2" id="dgs-11-b">The apex does not have to sit in the middle</h2>
            <p class="dgs-11__body">A three-point polygon puts the high corner wherever you want it. Move the apex to 22% and the band feels like it is being lifted from the left; at 88% it drops away to the right. Symmetry is a choice, not a default.</p>
            <p class="dgs-11__mono" aria-hidden="true">polygon(0 var(--cut), var(--apex) 0, 100% var(--cut2), 100% 100%, 0 100%)</p>
          </div>
        </div>
        <dl class="dgs-11__specimen">
          <div><dt>Aa</dt><dd>Light 300</dd></div>
          <div><dt>Aa</dt><dd>Regular 400</dd></div>
          <div><dt>Aa</dt><dd>Bold 700</dd></div>
          <div><dt>Aa</dt><dd>Extra 800</dd></div>
        </dl>
      </div>
    </section>

    <section class="dgs-11__after" aria-labelledby="dgs-11-c">
      <div class="dgs-11__wrap">
        <h2 class="dgs-11__h3" id="dgs-11-c">Licensing</h2>
        <ul class="dgs-11__lic">
          <li><strong>Desktop</strong><span>5 users</span><em>&euro;120</em></li>
          <li><strong>Web</strong><span>250k views / mo</span><em>&euro;180</em></li>
          <li><strong>Full family</strong><span>Desktop + web + app</span><em>&euro;390</em></li>
        </ul>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=Space+Grotesk:wght@400;500&display=swap');

.dgs-11 {
  --cut: clamp(1.25rem, 4vw, 4.5rem);
  --cut2: clamp(2.5rem, 8vw, 9rem);
  --apex: 64%;
  --paper: #f2f0eb;
  --paper2: #e6e3db;
  --ink: #100f0d;
  --muted: #56534c;
  --mustard: #e8b400;
  --on-mustard: #100f0d;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--paper);
  color: var(--ink);
  font-family: 'Space Grotesk', system-ui, -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
}

.dgs-11 *,
.dgs-11 *::before,
.dgs-11 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.8 0.16 90)) {
  .dgs-11 {
    --paper: oklch(0.952 0.008 85);
    --paper2: oklch(0.915 0.011 85);
    --ink: oklch(0.155 0.006 80);
    --muted: oklch(0.455 0.01 80);
    --mustard: oklch(0.815 0.155 88);
  }
}

.dgs-11__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-11__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.dgs-11__ctl {
  position: absolute;
  inset-block-start: 0;
  inset-inline-end: 0;
  z-index: 40;
  margin: 0;
  padding: 0;
  border: 0;
  display: flex;
  background: var(--ink);
}

.dgs-11__ctl label {
  min-inline-size: 3rem;
  min-block-size: 2.75rem;
  display: grid;
  place-items: center;
  padding-inline: .8rem;
  font-family: ui-monospace, Menlo, monospace;
  font-size: .72rem;
  letter-spacing: .06em;
  color: rgba(242,240,235,.6);
  cursor: pointer;
  transition: background .18s ease, color .18s ease;
}

.dgs-11__ctl label:hover {
  color: var(--paper);
}

.dgs-11__sr:checked + label {
  background: var(--mustard);
  color: var(--on-mustard);
}

.dgs-11__sr:focus-visible + label {
  outline: 2px solid var(--mustard);
  outline-offset: -3px;
}

.dgs-11__stage {
  display: flow-root;
}

.dgs-11__wrap {
  inline-size: min(78rem, 100%);
  margin-inline: auto;
}

.dgs-11__top {
  padding: clamp(3.5rem, 8vw, 6rem) clamp(1.25rem, 5vw, 4rem) calc(var(--cut2) + clamp(2.5rem, 6vw, 4rem));
}

.dgs-11__meta {
  margin: 0 0 clamp(1.5rem, 4vw, 2.5rem);
  display: flex;
  flex-wrap: wrap;
  gap: .35rem 1.5rem;
  justify-content: space-between;
  padding-block-end: .6rem;
  border-block-end: 2px solid var(--ink);
  font-family: ui-monospace, Menlo, monospace;
  font-size: .72rem;
  letter-spacing: .14em;
  text-transform: uppercase;
}

.dgs-11__display {
  margin: 0 0 1.5rem;
  font-family: 'Syne', sans-serif;
  font-weight: 800;
  font-size: clamp(3.2rem, 15vw, 10rem);
  line-height: .82;
  letter-spacing: -.05em;
}

.dgs-11__display em {
  font-style: normal;
  font-weight: 400;
  color: var(--muted);
}

.dgs-11__lede {
  margin: 0;
  max-inline-size: 44ch;
  font-size: clamp(1rem, 2vw, 1.15rem);
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-11__band {
  position: relative;
  z-index: 1;
  background: var(--mustard);
  color: var(--on-mustard);
  clip-path: polygon(0 var(--cut), var(--apex) 0, 100% var(--cut2), 100% 100%, 0 100%);
  margin-block-start: calc(var(--cut2) * -1 - 1px);
  padding: calc(var(--cut2) + clamp(3rem, 7vw, 5rem)) clamp(1.25rem, 5vw, 4rem) clamp(3.5rem, 8vw, 5.5rem);
}

.dgs-11__asym {
  display: grid;
  gap: clamp(1.5rem, 4vw, 3rem);
  grid-template-columns: minmax(0, auto) minmax(0, 1fr);
  align-items: start;
}

.dgs-11__num {
  margin: 0;
  font-family: 'Syne', sans-serif;
  font-weight: 800;
  font-size: clamp(3rem, 12vw, 8rem);
  line-height: .8;
  letter-spacing: -.06em;
  opacity: .28;
}

.dgs-11__h2 {
  margin: 0 0 1rem;
  max-inline-size: 26ch;
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: clamp(1.6rem, 4.6vw, 2.9rem);
  line-height: 1.02;
  letter-spacing: -.035em;
  text-wrap: balance;
}

.dgs-11__body {
  margin: 0 0 1.1rem;
  max-inline-size: 54ch;
  color: rgba(16,15,13,.78);
  text-wrap: pretty;
}

.dgs-11__mono {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: clamp(.6rem, 1.5vw, .74rem);
  color: rgba(16,15,13,.6);
  overflow-wrap: anywhere;
}

.dgs-11__specimen {
  margin: clamp(2.5rem, 6vw, 4rem) 0 0;
  display: grid;
  gap: 0;
  grid-template-columns: repeat(auto-fit, minmax(9rem, 1fr));
  border-block-start: 2px solid var(--ink);
}

.dgs-11__specimen > div {
  padding: 1rem .5rem 0;
  border-inline-end: 1px solid rgba(16,15,13,.2);
}

.dgs-11__specimen > div:last-child {
  border-inline-end: 0;
}

.dgs-11__specimen dt {
  font-family: 'Syne', sans-serif;
  font-size: clamp(2.5rem, 8vw, 4rem);
  line-height: 1;
  letter-spacing: -.04em;
}

.dgs-11__specimen > div:nth-child(1) dt {
  font-weight: 400;
}

.dgs-11__specimen > div:nth-child(2) dt {
  font-weight: 600;
}

.dgs-11__specimen > div:nth-child(3) dt {
  font-weight: 700;
}

.dgs-11__specimen > div:nth-child(4) dt {
  font-weight: 800;
}

.dgs-11__specimen dd {
  margin: .4rem 0 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: .68rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(16,15,13,.65);
}

.dgs-11__after {
  background: var(--paper2);
  padding: clamp(3.5rem, 8vw, 5rem) clamp(1.25rem, 5vw, 4rem) clamp(4rem, 9vw, 6rem);
}

.dgs-11__h3 {
  margin: 0 0 1.25rem;
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-size: clamp(1.3rem, 3.4vw, 1.9rem);
  letter-spacing: -.03em;
}

.dgs-11__lic {
  list-style: none;
  margin: 0;
  padding: 0;
}

.dgs-11__lic li {
  display: grid;
  gap: .2rem 1.5rem;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1fr) auto;
  align-items: baseline;
  padding-block: .95rem;
  border-block-start: 1px solid rgba(16,15,13,.18);
}

.dgs-11__lic li:last-child {
  border-block-end: 1px solid rgba(16,15,13,.18);
}

.dgs-11__lic strong {
  font-weight: 700;
}

.dgs-11__lic span {
  font-size: .88rem;
  color: var(--muted);
}

.dgs-11__lic em {
  font-style: normal;
  font-family: 'Syne', sans-serif;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.dgs-11:has(#dgs-11-p1:checked) {
  --apex: 22%;
}

.dgs-11:has(#dgs-11-p3:checked) {
  --apex: 88%;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-11 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-11__band {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
    border-block: 1px solid CanvasText;
  }

  .dgs-11__ctl label {
    border: 1px solid CanvasText;
  }

  .dgs-11__sr:checked + label {
    background: Highlight;
    color: HighlightText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-11__sronly,
.dgs-11__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-11__theme {
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

.dgs-11__theme:hover {
  translate: 0 -1px;
}

.dgs-11__sronly:focus-visible + .dgs-11__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-11__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-11__i--sun {
  display: none;
}

.dgs-11:has(#dgs-11-dark:checked) .dgs-11__i--moon {
  display: none;
}

.dgs-11:has(#dgs-11-dark:checked) .dgs-11__i--sun {
  display: block;
}

.dgs-11:has(#dgs-11-dark:checked) {
  --paper: #111318;
  --ink: #eef1f6;
  --muted: #98a0ad;
  --line: #242a33;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-11__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-11__theme {
    border-color: CanvasText;
  }
}
```
