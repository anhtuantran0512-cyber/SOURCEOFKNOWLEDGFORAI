---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-diagonal-section-with-rounded-edge-angles/"
title: "CSS Diagonal Section with Rounded Edge Angles"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "An angled edge that still has a soft radius where it meets the edge of the viewport."
has_js: "false"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Diagonal Section with Rounded Edge Angles
Source: https://codefronts.com/layouts/css-diagonal-sections/css-diagonal-section-with-rounded-edge-angles/

An angled edge that still has a soft radius where it meets the edge of the viewport. clip-path: polygon() cannot round a corner — that is the constraint behind the query — so the shipped technique is a border-radius wrapper with overflow: clip, and the demo also shows the clip-path: path() alternative with real arc commands, plus exactly why that one does not scale.
## HTML
```html
<div class="dgs-13">
  <input class="dgs-13__sronly" type="checkbox" id="dgs-13-dark">
  <label class="dgs-13__theme" for="dgs-13-dark">
    <svg class="dgs-13__i dgs-13__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-13__i dgs-13__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-13__srtext">Toggle dark theme</span>
  </label>
  <fieldset class="dgs-13__ctl">
    <legend class="dgs-13__vh">Corner radius</legend>
    <input class="dgs-13__sr" type="radio" name="dgs-13-r" id="dgs-13-r1"><label for="dgs-13-r1">Sharp</label>
    <input class="dgs-13__sr" type="radio" name="dgs-13-r" id="dgs-13-r2" checked><label for="dgs-13-r2">Soft</label>
    <input class="dgs-13__sr" type="radio" name="dgs-13-r" id="dgs-13-r3"><label for="dgs-13-r3">Pillow</label>
  </fieldset>

  <div class="dgs-13__stage">
    <section class="dgs-13__top" aria-labelledby="dgs-13-a">
      <div class="dgs-13__wrap">
        <p class="dgs-13__eyebrow">Sprout &mdash; family money</p>
        <h2 class="dgs-13__display" id="dgs-13-a">Pocket money that teaches the boring part</h2>
        <p class="dgs-13__lede">Chores, savings goals and a card with a hard limit. Parents approve, children learn what interest actually does over a year.</p>
      </div>
    </section>

    <section class="dgs-13__band" aria-labelledby="dgs-13-b">
      <div class="dgs-13__wrap">
        <h2 class="dgs-13__h2" id="dgs-13-b">An angled edge with rounded ends</h2>
        <p class="dgs-13__body">A clip-path corner is always a sharp point. This band is a rounded rectangle painted by a pseudo-element and then skewed, so the diagonal is a straight cut while both ends keep a soft radius — the friendliest version of the angle.</p>
        <div class="dgs-13__goals">
          <article>
            <p class="dgs-13__goal">Skateboard</p>
            <p class="dgs-13__amt">&pound;48<span> of &pound;80</span></p>
            <div class="dgs-13__meter" role="img" aria-label="60 percent saved"><span style="inline-size: 60%"></span></div>
          </article>
          <article>
            <p class="dgs-13__goal">Concert ticket</p>
            <p class="dgs-13__amt">&pound;31<span> of &pound;45</span></p>
            <div class="dgs-13__meter" role="img" aria-label="69 percent saved"><span style="inline-size: 69%"></span></div>
          </article>
          <article>
            <p class="dgs-13__goal">Rainy day</p>
            <p class="dgs-13__amt">&pound;120<span> of &pound;150</span></p>
            <div class="dgs-13__meter" role="img" aria-label="80 percent saved"><span style="inline-size: 80%"></span></div>
          </article>
        </div>
      </div>
    </section>

    <section class="dgs-13__after" aria-labelledby="dgs-13-c">
      <div class="dgs-13__wrap dgs-13__cols">
        <h2 class="dgs-13__h3" id="dgs-13-c">Why a pseudo-element</h2>
        <p class="dgs-13__note">Skewing the section itself would tilt the copy and the progress bars with it. Skewing a painted layer behind the content leaves every glyph upright and keeps the radius, because <code class="dgs-13__code">border-radius</code> survives a transform where a clip path has no radius at all.</p>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');

.dgs-13 {
  --ang: -4.5deg;
  --r: 2.25rem;
  --lift: clamp(2rem, 6vw, 5rem);
  --page: #fffafd;
  --page2: #fdf0f7;
  --ink: #2a1030;
  --muted: #6f5476;
  --line: #f5dcea;
  --pink: #ff5fa2;
  --violet: #7c4dff;
  --on-band: #fff6fb;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--page);
  color: var(--ink);
  font-family: 'Nunito', system-ui, -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

.dgs-13 *,
.dgs-13 *::before,
.dgs-13 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.7 0.2 350)) {
  .dgs-13 {
    --page: oklch(0.99 0.008 340);
    --page2: oklch(0.965 0.02 340);
    --ink: oklch(0.26 0.07 320);
    --muted: oklch(0.5 0.05 320);
    --line: oklch(0.925 0.03 340);
    --pink: oklch(0.7 0.2 5);
    --violet: oklch(0.55 0.23 295);
  }
}

.dgs-13__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-13__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.dgs-13__ctl {
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
  background: rgba(255,250,253,.94);
  box-shadow: 0 8px 24px -18px rgba(42,16,48,.6);
}

.dgs-13__ctl label {
  min-inline-size: 3rem;
  min-block-size: 2.5rem;
  display: grid;
  place-items: center;
  padding-inline: .85rem;
  border-radius: 999px;
  font-size: .78rem;
  font-weight: 700;
  color: var(--muted);
  cursor: pointer;
  transition: background .2s ease, color .2s ease;
}

.dgs-13__ctl label:hover {
  color: var(--ink);
}

.dgs-13__sr:checked + label {
  background: var(--violet);
  color: #fff;
}

.dgs-13__sr:focus-visible + label {
  outline: 2px solid var(--violet);
  outline-offset: 2px;
}

.dgs-13__stage {
  display: flow-root;
}

.dgs-13__wrap {
  inline-size: min(70rem, 100%);
  margin-inline: auto;
}

.dgs-13__top {
  padding: clamp(4rem, 9vw, 6.5rem) clamp(1.25rem, 5vw, 4rem) calc(var(--lift) + clamp(2rem, 5vw, 3.5rem));
}

.dgs-13__eyebrow {
  margin: 0 0 .9rem;
  font-size: .78rem;
  font-weight: 800;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--pink);
}

.dgs-13__display {
  margin: 0 0 1rem;
  max-inline-size: 24ch;
  font-size: clamp(2.1rem, 6.4vw, 3.9rem);
  font-weight: 800;
  line-height: 1.05;
  letter-spacing: -.035em;
  text-wrap: balance;
}

.dgs-13__lede {
  margin: 0;
  max-inline-size: 48ch;
  font-size: clamp(1.02rem, 2vw, 1.18rem);
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-13__band {
  position: relative;
  z-index: 1;
  isolation: isolate;
  color: var(--on-band);
  margin-block-start: calc(var(--lift) * -1);
  padding: calc(var(--lift) + clamp(2.5rem, 6vw, 4rem)) clamp(1.25rem, 5vw, 4rem) clamp(3rem, 7vw, 4.5rem);
}

.dgs-13__band::before {
  content: '';
  position: absolute;
  inset: 0 -6vw;
  z-index: -1;
  border-radius: var(--r);
  background: linear-gradient(104deg, var(--violet) 0%, var(--pink) 100%);
  transform: skewY(var(--ang));
  transform-origin: 50% 0;
  box-shadow: 0 30px 60px -40px rgba(124,77,255,.9);
  transition: border-radius .3s ease, transform .3s ease;
}

.dgs-13__h2 {
  margin: 0 0 1rem;
  max-inline-size: 24ch;
  font-size: clamp(1.6rem, 4.4vw, 2.6rem);
  font-weight: 800;
  line-height: 1.06;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.dgs-13__body {
  margin: 0 0 clamp(2rem, 5vw, 3rem);
  max-inline-size: 54ch;
  color: rgba(255,246,251,.88);
  text-wrap: pretty;
}

.dgs-13__goals {
  display: grid;
  gap: clamp(.75rem, 2vw, 1.1rem);
  grid-template-columns: repeat(auto-fit, minmax(14rem, 1fr));
}

.dgs-13__goals article {
  padding: 1.1rem 1.2rem 1.3rem;
  border-radius: 20px;
  background: rgba(255,255,255,.16);
  border: 1px solid rgba(255,255,255,.3);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
}

.dgs-13__goal {
  margin: 0 0 .3rem;
  font-size: .82rem;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: rgba(255,246,251,.8);
}

.dgs-13__amt {
  margin: 0 0 .8rem;
  font-size: clamp(1.5rem, 4vw, 2rem);
  font-weight: 800;
  letter-spacing: -.03em;
  font-variant-numeric: tabular-nums;
}

.dgs-13__amt span {
  font-size: .8rem;
  font-weight: 600;
  opacity: .8;
  letter-spacing: 0;
}

.dgs-13__meter {
  block-size: .6rem;
  border-radius: 999px;
  background: rgba(42,16,48,.28);
  overflow: clip;
}

.dgs-13__meter span {
  display: block;
  block-size: 100%;
  border-radius: 999px;
  background: #fff6fb;
  animation: dgs-13-fill 1.1s cubic-bezier(.2,.8,.3,1) both;
}

@keyframes dgs-13-fill {
  from {
    scale: 0 1;
    transform-origin: left;
  }
}

.dgs-13__after {
  background: var(--page2);
  padding: clamp(3rem, 7vw, 4.5rem) clamp(1.25rem, 5vw, 4rem) clamp(4rem, 9vw, 6rem);
}

.dgs-13__cols {
  display: grid;
  gap: 1rem clamp(2rem, 6vw, 4rem);
  grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
  align-items: start;
}

.dgs-13__h3 {
  margin: 0;
  font-size: clamp(1.3rem, 3.4vw, 1.9rem);
  font-weight: 800;
  letter-spacing: -.03em;
}

.dgs-13__note {
  margin: 0;
  max-inline-size: 58ch;
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-13__code {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .86em;
  padding: .1em .35em;
  border-radius: 5px;
  background: rgba(42,16,48,.07);
}

.dgs-13:has(#dgs-13-r1:checked) {
  --r: 0rem;
}

.dgs-13:has(#dgs-13-r3:checked) {
  --r: 4.5rem;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-13 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-13__band::before {
    background: Canvas;
    border: 1px solid CanvasText;
    box-shadow: none;
  }

  .dgs-13__band {
    forced-color-adjust: none;
    color: CanvasText;
  }

  .dgs-13__goals article,
    .dgs-13__ctl label {
    border: 1px solid CanvasText;
  }

  .dgs-13__sr:checked + label {
    background: Highlight;
    color: HighlightText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-13__sronly,
.dgs-13__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-13__theme {
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

.dgs-13__theme:hover {
  translate: 0 -1px;
}

.dgs-13__sronly:focus-visible + .dgs-13__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-13__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-13__i--sun {
  display: none;
}

.dgs-13:has(#dgs-13-dark:checked) .dgs-13__i--moon {
  display: none;
}

.dgs-13:has(#dgs-13-dark:checked) .dgs-13__i--sun {
  display: block;
}

.dgs-13:has(#dgs-13-dark:checked) {
  --page: #0e1014;
  --page2: #171a20;
  --ink: #f0f2f6;
  --muted: #9aa2ad;
  --line: #252a32;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-13__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-13__theme {
    border-color: CanvasText;
  }
}
```
