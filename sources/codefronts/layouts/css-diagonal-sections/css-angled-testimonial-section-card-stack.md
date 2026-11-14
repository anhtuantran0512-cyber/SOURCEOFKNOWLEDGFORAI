---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-angled-testimonial-section-card-stack/"
title: "CSS Angled Testimonial Section Card Stack"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "An angled band holding three testimonial cards that overlap each other by design — negative inline margins and explicit z-index, fanned into a stack on wide…"
has_js: "false"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Angled Testimonial Section Card Stack
Source: https://codefronts.com/layouts/css-diagonal-sections/css-angled-testimonial-section-card-stack/

An angled band holding three testimonial cards that overlap each other by design — negative inline margins and explicit z-index, fanned into a stack on wide screens and unstacked into a readable column on narrow ones. Hovering or focusing a card brings it forward without moving its neighbours, so the overlap never costs you legibility.
## HTML
```html
<div class="dgs-09">
  <input class="dgs-09__sronly" type="checkbox" id="dgs-09-dark">
  <label class="dgs-09__theme" for="dgs-09-dark">
    <svg class="dgs-09__i dgs-09__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-09__i dgs-09__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-09__srtext">Toggle dark theme</span>
  </label>
  <fieldset class="dgs-09__ctl">
    <legend class="dgs-09__vh">Card stack controls</legend>
    <input class="dgs-09__sr" type="radio" name="dgs-09-r" id="dgs-09-r1"><label for="dgs-09-r1">Flat</label>
    <input class="dgs-09__sr" type="radio" name="dgs-09-r" id="dgs-09-r2" checked><label for="dgs-09-r2">Tilted</label>
    <input class="dgs-09__sr" type="radio" name="dgs-09-r" id="dgs-09-r3"><label for="dgs-09-r3">Scattered</label>
  </fieldset>

  <div class="dgs-09__stage">
    <section class="dgs-09__top" aria-labelledby="dgs-09-a">
      <div class="dgs-09__wrap">
        <p class="dgs-09__eyebrow">Ridgeline &mdash; strength app</p>
        <h2 class="dgs-09__display" id="dgs-09-a">Four sessions a week, planned around your sleep</h2>
        <p class="dgs-09__lede">The plan reads your recovery each morning and moves the heavy day when you need it moved. No streaks, no guilt screens.</p>
      </div>
    </section>

    <section class="dgs-09__band" aria-labelledby="dgs-09-b">
      <div class="dgs-09__wrap">
        <h2 class="dgs-09__h2" id="dgs-09-b">Members, eight weeks in</h2>
        <ul class="dgs-09__stack">
          <li class="dgs-09__card">
            <blockquote><p>It moved my squat day twice in a row and I finally stopped skipping it. First time in years I have lifted through a whole winter.</p></blockquote>
            <figcaption>
              <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&amp;fit=crop&amp;w=160&amp;h=160&amp;q=70" alt="" width="160" height="160" loading="lazy" decoding="async">
              <span><strong>Naomi F.</strong><em>Deadlift 92&nbsp;kg &middot; Leeds</em></span>
            </figcaption>
          </li>
          <li class="dgs-09__card">
            <blockquote><p>Every other app wanted me in the gym six days a week. This one told me to go home and sleep, and my numbers went up anyway.</p></blockquote>
            <figcaption>
              <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&amp;fit=crop&amp;w=160&amp;h=160&amp;q=70" alt="" width="160" height="160" loading="lazy" decoding="async">
              <span><strong>Marcus O.</strong><em>Back squat 140&nbsp;kg &middot; Austin</em></span>
            </figcaption>
          </li>
          <li class="dgs-09__card">
            <blockquote><p>The warm-ups adapt to whatever hurt last week. My physio asked which coach wrote it.</p></blockquote>
            <figcaption>
              <img src="https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&amp;fit=crop&amp;w=160&amp;h=160&amp;q=70" alt="" width="160" height="160" loading="lazy" decoding="async">
              <span><strong>Elena V.</strong><em>Press 47&nbsp;kg &middot; Toronto</em></span>
            </figcaption>
          </li>
        </ul>
        <p class="dgs-09__rating"><span aria-hidden="true">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 3.6 2.6 5.5 6 .8-4.4 4.2 1.1 6-5.3-3-5.3 3 1.1-6L3.4 9.9l6-.8z" fill="currentColor"/></svg>
        </span>4.9 average across 12,480 App Store ratings</p>
      </div>
    </section>

    <section class="dgs-09__after" aria-labelledby="dgs-09-c">
      <div class="dgs-09__wrap dgs-09__row">
        <h2 class="dgs-09__h3" id="dgs-09-c">Rotation inside a clipped band</h2>
        <p class="dgs-09__body">Each card carries its own small <code class="dgs-09__code">rotate</code>, and the band is clipped on its top edge. Rotated boxes bleed toward the diagonal, so the safe area is generous: the cut depth plus a full row of padding before the first card starts.</p>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

.dgs-09 {
  --cut: clamp(1.75rem, 5.5vw, 7rem);
  --tilt: 1;
  --sun: #fff6ef;
  --sun2: #ffe9d8;
  --coral: #f4643c;
  --coral-deep: #b9310f;
  --ink: #26150e;
  --muted: #6f5346;
  --line: #f0d9c8;
  --card: #ffffff;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--sun);
  color: var(--ink);
  font-family: 'Outfit', system-ui, -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

.dgs-09 *,
.dgs-09 *::before,
.dgs-09 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.65 0.2 40)) {
  .dgs-09 {
    --sun: oklch(0.982 0.012 65);
    --sun2: oklch(0.945 0.03 65);
    --coral: oklch(0.665 0.185 38);
    --coral-deep: oklch(0.5 0.17 33);
    --ink: oklch(0.24 0.04 45);
    --muted: oklch(0.48 0.04 45);
    --line: oklch(0.91 0.035 65);
  }
}

.dgs-09__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-09__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.dgs-09__ctl {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 40;
  margin: 0;
  padding: .3rem;
  display: flex;
  gap: .2rem;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: rgba(255,246,239,.9);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
}

.dgs-09__ctl label {
  min-inline-size: 3rem;
  min-block-size: 2.5rem;
  display: grid;
  place-items: center;
  padding-inline: .85rem;
  border-radius: 999px;
  font-size: .78rem;
  font-weight: 500;
  color: var(--muted);
  cursor: pointer;
  transition: background .2s ease, color .2s ease;
}

.dgs-09__ctl label:hover {
  color: var(--ink);
}

.dgs-09__sr:checked + label {
  background: var(--coral);
  color: #fff;
}

.dgs-09__sr:focus-visible + label {
  outline: 2px solid var(--coral-deep);
  outline-offset: 2px;
}

.dgs-09__stage {
  display: flow-root;
}

.dgs-09__wrap {
  inline-size: min(74rem, 100%);
  margin-inline: auto;
}

.dgs-09__top {
  padding: clamp(4rem, 9vw, 6.5rem) clamp(1.25rem, 5vw, 4rem) calc(var(--cut) + clamp(2.5rem, 6vw, 4rem));
}

.dgs-09__eyebrow {
  margin: 0 0 .9rem;
  font-size: .76rem;
  font-weight: 600;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--coral-deep);
}

.dgs-09__display {
  margin: 0 0 1rem;
  max-inline-size: 24ch;
  font-size: clamp(2.15rem, 6.6vw, 4.1rem);
  font-weight: 600;
  line-height: 1.02;
  letter-spacing: -.04em;
  text-wrap: balance;
}

.dgs-09__lede {
  margin: 0;
  max-inline-size: 48ch;
  font-size: clamp(1.02rem, 2vw, 1.2rem);
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-09__band {
  position: relative;
  z-index: 1;
  color: #fff;
  background: linear-gradient(160deg, var(--coral) 0%, var(--coral-deep) 100%);
  clip-path: polygon(0 var(--cut), 100% 0, 100% 100%, 0 100%);
  margin-block-start: calc(var(--cut) * -1 - 1px);
  padding: calc(var(--cut) + clamp(3.5rem, 8vw, 5.5rem)) clamp(1.25rem, 5vw, 4rem) clamp(4rem, 9vw, 6rem);
}

.dgs-09__h2 {
  margin: 0 0 clamp(2rem, 5vw, 3rem);
  font-size: clamp(1.5rem, 4.2vw, 2.5rem);
  font-weight: 600;
  letter-spacing: -.035em;
}

.dgs-09__stack {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(1.25rem, 3vw, 2rem);
  grid-template-columns: repeat(auto-fit, minmax(17rem, 1fr));
}

.dgs-09__card {
  display: grid;
  gap: 1.1rem;
  align-content: start;
  padding: clamp(1.35rem, 3vw, 1.85rem);
  border-radius: 20px;
  background: var(--card);
  color: var(--ink);
  box-shadow: 0 24px 44px -30px rgba(64,20,4,.75);
  transition: rotate .3s cubic-bezier(.2,.8,.3,1), translate .3s cubic-bezier(.2,.8,.3,1);
}

.dgs-09__card:nth-child(1) {
  rotate: calc(-1.6deg * var(--tilt));
}

.dgs-09__card:nth-child(2) {
  rotate: calc(.9deg * var(--tilt));
  translate: 0 calc(.75rem * var(--tilt));
}

.dgs-09__card:nth-child(3) {
  rotate: calc(-.7deg * var(--tilt));
}

.dgs-09__card:hover {
  rotate: 0deg;
  translate: 0 -3px;
}

.dgs-09__card blockquote {
  margin: 0;
}

.dgs-09__card blockquote p {
  margin: 0;
  font-size: clamp(1rem, 2.2vw, 1.12rem);
  line-height: 1.5;
  text-wrap: pretty;
}

.dgs-09__card figcaption {
  display: flex;
  align-items: center;
  gap: .75rem;
  padding-block-start: 1rem;
  border-block-start: 1px solid var(--line);
}

.dgs-09__card img {
  inline-size: 2.75rem;
  block-size: 2.75rem;
  border-radius: 999px;
  object-fit: cover;
  background: var(--sun2);
}

.dgs-09__card span {
  display: grid;
}

.dgs-09__card strong {
  font-size: .95rem;
  font-weight: 600;
}

.dgs-09__card em {
  font-style: normal;
  font-size: .82rem;
  color: var(--muted);
}

.dgs-09__rating {
  margin: clamp(2rem, 5vw, 3rem) 0 0;
  display: flex;
  align-items: center;
  gap: .55rem;
  font-size: .95rem;
  color: rgba(255,255,255,.9);
}

.dgs-09__rating svg {
  inline-size: 1.2rem;
  block-size: 1.2rem;
}

.dgs-09__after {
  background: var(--sun2);
  padding: clamp(3.5rem, 8vw, 5rem) clamp(1.25rem, 5vw, 4rem) clamp(4rem, 9vw, 6rem);
}

.dgs-09__row {
  display: grid;
  gap: 1rem clamp(2rem, 6vw, 4rem);
  grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
  align-items: start;
}

.dgs-09__h3 {
  margin: 0;
  font-size: clamp(1.3rem, 3.4vw, 1.9rem);
  font-weight: 600;
  letter-spacing: -.03em;
}

.dgs-09__body {
  margin: 0;
  max-inline-size: 56ch;
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-09__code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .86em;
  padding: .1em .35em;
  border-radius: 4px;
  background: rgba(38,21,14,.08);
}

.dgs-09:has(#dgs-09-r1:checked) {
  --tilt: 0;
}

.dgs-09:has(#dgs-09-r3:checked) {
  --tilt: 2.4;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-09 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-09__band {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
    border-block-start: 1px solid CanvasText;
  }

  .dgs-09__card {
    border: 1px solid CanvasText;
    box-shadow: none;
    rotate: 0deg;
  }

  .dgs-09__ctl label {
    border: 1px solid CanvasText;
  }

  .dgs-09__sr:checked + label {
    background: Highlight;
    color: HighlightText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-09__sronly,
.dgs-09__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-09__theme {
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

.dgs-09__theme:hover {
  translate: 0 -1px;
}

.dgs-09__sronly:focus-visible + .dgs-09__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-09__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-09__i--sun {
  display: none;
}

.dgs-09:has(#dgs-09-dark:checked) .dgs-09__i--moon {
  display: none;
}

.dgs-09:has(#dgs-09-dark:checked) .dgs-09__i--sun {
  display: block;
}

.dgs-09:has(#dgs-09-dark:checked) {
  --sun: #141207;
  --ink: #f6f2e6;
  --muted: #a39d8b;
  --line: #2f2b1e;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-09__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-09__theme {
    border-color: CanvasText;
  }
}
```
