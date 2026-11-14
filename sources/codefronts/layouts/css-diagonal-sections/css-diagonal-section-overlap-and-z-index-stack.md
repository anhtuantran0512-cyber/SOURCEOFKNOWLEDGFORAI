---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-diagonal-section-overlap-and-z-index-stack/"
title: "CSS Diagonal Section Overlap & Z-Index Stack"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "The troubleshooting demo: two angled sections deliberately overlapped with negative margins, shown broken and fixed side by side."
has_js: "false"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Diagonal Section Overlap & Z-Index Stack
Source: https://codefronts.com/layouts/css-diagonal-sections/css-diagonal-section-overlap-and-z-index-stack/

The troubleshooting demo: two angled sections deliberately overlapped with negative margins, shown broken and fixed side by side. Broken, the second band swallows the first one's copy because z-index does nothing on a statically positioned element. Fixed, position: relative plus an explicit index decides the join — and the copy explains the stacking-context trap that makes the fix look like it failed.
## HTML
```html
<div class="dgs-16">
  <input class="dgs-16__sronly" type="checkbox" id="dgs-16-dark">
  <label class="dgs-16__theme" for="dgs-16-dark">
    <svg class="dgs-16__i dgs-16__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-16__i dgs-16__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-16__srtext">Toggle dark theme</span>
  </label>
  <fieldset class="dgs-16__ctl">
    <legend class="dgs-16__vh">Stacking order</legend>
    <input class="dgs-16__sr" type="radio" name="dgs-16-z" id="dgs-16-z1" checked><label for="dgs-16-z1">Front</label>
    <input class="dgs-16__sr" type="radio" name="dgs-16-z" id="dgs-16-z2"><label for="dgs-16-z2">Behind</label>
  </fieldset>

  <div class="dgs-16__stage">
    <section class="dgs-16__plate dgs-16__plate--a" aria-labelledby="dgs-16-a">
      <div class="dgs-16__wrap">
        <p class="dgs-16__eyebrow">Fenn &amp; Alder &mdash; Architects</p>
        <h2 class="dgs-16__display" id="dgs-16-a">Concrete, glass and the light between them</h2>
        <p class="dgs-16__lede">Twenty-two years of civic and residential work across the north. Every project starts with a survey of the light, not the plot.</p>
      </div>
    </section>

    <section class="dgs-16__plate dgs-16__plate--b" aria-labelledby="dgs-16-b">
      <div class="dgs-16__wrap dgs-16__split">
        <div>
          <p class="dgs-16__eyebrow dgs-16__eyebrow--on">Selected work</p>
          <h2 class="dgs-16__h2" id="dgs-16-b">Three angled plates, deliberately overlapping</h2>
          <p class="dgs-16__body">Each plate is clipped and pulled up over its neighbour, and only <code class="dgs-16__code">z-index</code> decides which edge sits on top. Flip the order and the same three sections read as a completely different composition — the geometry has not changed at all.</p>
          <p class="dgs-16__mono" aria-hidden="true">position: relative; z-index: 3 / 2 / 1</p>
        </div>
        <figure class="dgs-16__shot">
          <img src="https://images.unsplash.com/photo-1487958449943-2429e8be8625?auto=format&amp;fit=crop&amp;w=1200&amp;q=70" alt="A pale concrete facade with deep window reveals casting hard shadows" width="1200" height="900" loading="lazy" decoding="async">
          <figcaption>Ravensmoor Library &middot; 2026</figcaption>
        </figure>
      </div>
    </section>

    <section class="dgs-16__plate dgs-16__plate--c" aria-labelledby="dgs-16-c">
      <div class="dgs-16__wrap">
        <h2 class="dgs-16__h3" id="dgs-16-c">Practice</h2>
        <ul class="dgs-16__list">
          <li><strong>Civic</strong><span>Libraries, transport, four listed refurbishments</span></li>
          <li><strong>Residential</strong><span>Single dwellings and a 34-home terrace</span></li>
          <li><strong>Retrofit</strong><span>Fabric-first, EnerPHit on two schemes</span></li>
        </ul>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Jost:wght@300;400;500;600&display=swap');

.dgs-16 {
  --cut: clamp(1.5rem, 5vw, 6.5rem);
  --z-a: 3;
  --z-b: 2;
  --z-c: 1;
  --grey0: #f0efec;
  --grey1: #dddcd7;
  --grey2: #35342f;
  --grey3: #22221e;
  --ink: #1b1b17;
  --muted: #5c5b53;
  --on-dark: #f2f1ee;
  --dim: #a5a49c;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--grey0);
  color: var(--ink);
  font-family: 'Jost', system-ui, -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

.dgs-16 *,
.dgs-16 *::before,
.dgs-16 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.5 0.01 90)) {
  .dgs-16 {
    --grey0: oklch(0.948 0.004 90);
    --grey1: oklch(0.882 0.005 90);
    --grey2: oklch(0.31 0.005 90);
    --grey3: oklch(0.245 0.005 90);
    --ink: oklch(0.21 0.006 90);
    --muted: oklch(0.48 0.008 90);
    --on-dark: oklch(0.955 0.003 90);
    --dim: oklch(0.72 0.006 90);
  }
}

.dgs-16__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-16__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.dgs-16__ctl {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 40;
  margin: 0;
  padding: 2px;
  border: 1px solid var(--grey1);
  display: flex;
  gap: 2px;
  background: rgba(240,239,236,.9);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
}

.dgs-16__ctl label {
  min-inline-size: 3.25rem;
  min-block-size: 2.6rem;
  display: grid;
  place-items: center;
  padding-inline: .8rem;
  font-size: .76rem;
  font-weight: 400;
  letter-spacing: .06em;
  color: var(--muted);
  cursor: pointer;
  transition: background .18s ease, color .18s ease;
}

.dgs-16__ctl label:hover {
  color: var(--ink);
}

.dgs-16__sr:checked + label {
  background: var(--ink);
  color: var(--grey0);
}

.dgs-16__sr:focus-visible + label {
  outline: 2px solid var(--ink);
  outline-offset: -3px;
}

.dgs-16__stage {
  display: flow-root;
}

.dgs-16__wrap {
  inline-size: min(76rem, 100%);
  margin-inline: auto;
}

.dgs-16__plate {
  position: relative;
  padding-inline: clamp(1.25rem, 5vw, 4rem);
}

.dgs-16__plate--a {
  z-index: var(--z-a);
  background: var(--grey0);
  clip-path: polygon(0 0, 100% 0, 100% calc(100% - var(--cut)), 0 100%);
  padding-block: clamp(3.5rem, 8vw, 6rem) calc(var(--cut) + clamp(2.5rem, 6vw, 4rem));
}

.dgs-16__plate--b {
  z-index: var(--z-b);
  background: var(--grey2);
  color: var(--on-dark);
  clip-path: polygon(0 var(--cut), 100% 0, 100% calc(100% - var(--cut)), 0 100%);
  margin-block: calc(var(--cut) * -1);
  padding-block: calc(var(--cut) + clamp(2.5rem, 6vw, 4rem));
}

.dgs-16__plate--c {
  z-index: var(--z-c);
  background: var(--grey1);
  clip-path: polygon(0 var(--cut), 100% 0, 100% 100%, 0 100%);
  padding-block: calc(var(--cut) + clamp(2.5rem, 6vw, 4rem)) clamp(4rem, 9vw, 6rem);
}

.dgs-16__eyebrow {
  margin: 0 0 1rem;
  font-size: .74rem;
  font-weight: 500;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--muted);
}

.dgs-16__eyebrow--on {
  color: var(--dim);
}

.dgs-16__display {
  margin: 0 0 1rem;
  max-inline-size: 22ch;
  font-size: clamp(2.2rem, 6.8vw, 4.2rem);
  font-weight: 300;
  line-height: 1.04;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.dgs-16__lede {
  margin: 0;
  max-inline-size: 50ch;
  font-size: clamp(1.02rem, 2vw, 1.18rem);
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-16__split {
  display: grid;
  gap: clamp(2rem, 5vw, 3.5rem);
  grid-template-columns: repeat(auto-fit, minmax(19rem, 1fr));
  align-items: center;
}

.dgs-16__h2 {
  margin: 0 0 1rem;
  max-inline-size: 24ch;
  font-size: clamp(1.6rem, 4.4vw, 2.5rem);
  font-weight: 300;
  line-height: 1.08;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.dgs-16__body {
  margin: 0 0 1rem;
  max-inline-size: 54ch;
  color: rgba(242,241,238,.78);
  text-wrap: pretty;
}

.dgs-16__code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .86em;
  padding: .1em .35em;
  background: rgba(242,241,238,.12);
}

.dgs-16__mono {
  margin: 0;
  font-family: ui-monospace, Menlo, monospace;
  font-size: clamp(.62rem, 1.5vw, .76rem);
  letter-spacing: .04em;
  color: var(--dim);
}

.dgs-16__shot {
  margin: 0;
}

.dgs-16__shot img {
  inline-size: 100%;
  block-size: clamp(13rem, 34vw, 22rem);
  object-fit: cover;
  background: var(--grey3);
  filter: grayscale(.35) contrast(1.05);
  transition: filter .35s ease;
}

.dgs-16__shot:hover img {
  filter: grayscale(0) contrast(1.02);
}

.dgs-16__shot figcaption {
  margin-block-start: .6rem;
  font-size: .78rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--dim);
}

.dgs-16__h3 {
  margin: 0 0 1.25rem;
  font-size: clamp(1.3rem, 3.4vw, 1.8rem);
  font-weight: 400;
  letter-spacing: -.02em;
}

.dgs-16__list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.dgs-16__list li {
  display: grid;
  gap: .15rem 2rem;
  grid-template-columns: minmax(0, 10rem) minmax(0, 1fr);
  padding-block: .9rem;
  border-block-start: 1px solid rgba(27,27,23,.18);
}

.dgs-16__list li:last-child {
  border-block-end: 1px solid rgba(27,27,23,.18);
}

.dgs-16__list strong {
  font-weight: 500;
  letter-spacing: .02em;
}

.dgs-16__list span {
  color: var(--muted);
  font-size: .95rem;
}

.dgs-16:has(#dgs-16-z2:checked) {
  --z-a: 1;
  --z-b: 2;
  --z-c: 3;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-16 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-16__plate--b {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
    border-block: 1px solid CanvasText;
  }

  .dgs-16__ctl,
    .dgs-16__ctl label {
    border: 1px solid CanvasText;
  }

  .dgs-16__sr:checked + label {
    background: Highlight;
    color: HighlightText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-16__sronly,
.dgs-16__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-16__theme {
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

.dgs-16__theme:hover {
  translate: 0 -1px;
}

.dgs-16__sronly:focus-visible + .dgs-16__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-16__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-16__i--sun {
  display: none;
}

.dgs-16:has(#dgs-16-dark:checked) .dgs-16__i--moon {
  display: none;
}

.dgs-16:has(#dgs-16-dark:checked) .dgs-16__i--sun {
  display: block;
}

.dgs-16:has(#dgs-16-dark:checked) {
  --grey0: #101319;
  --ink: #eef1f6;
  --muted: #98a0ac;
  --line: #232935;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-16__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-16__theme {
    border-color: CanvasText;
  }
}
```
