---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-diagonal-section-divider-between-two-colors/"
title: "CSS Diagonal Section Divider Between Two Colors"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "The simplest job in the collection and the one people search for most: two solid colour bands meeting on a diagonal with no gap, no seam and no hairline of…"
has_js: "false"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Diagonal Section Divider Between Two Colors
Source: https://codefronts.com/layouts/css-diagonal-sections/css-diagonal-section-divider-between-two-colors/

The simplest job in the collection and the one people search for most: two solid colour bands meeting on a diagonal with no gap, no seam and no hairline of page background showing through the join. The angle is one token; the fix is a 1px overlap plus a matched pull-up, and the demo labels both sides of the join so you can see exactly where the pixels go.
## HTML
```html
<div class="dgs-03">
  <input class="dgs-03__sronly" type="checkbox" id="dgs-03-dark">
  <label class="dgs-03__theme" for="dgs-03-dark">
    <svg class="dgs-03__i dgs-03__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-03__i dgs-03__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-03__srtext">Toggle dark theme</span>
  </label>
  <fieldset class="dgs-03__ctl">
    <legend class="dgs-03__vh">Diagonal boundary controls</legend>
    <input class="dgs-03__sr" type="radio" name="dgs-03-a" id="dgs-03-a1"><label for="dgs-03-a1">Soft</label>
    <input class="dgs-03__sr" type="radio" name="dgs-03-a" id="dgs-03-a2" checked><label for="dgs-03-a2">Medium</label>
    <input class="dgs-03__sr" type="radio" name="dgs-03-a" id="dgs-03-a3"><label for="dgs-03-a3">Steep</label>
    <input class="dgs-03__sr" type="checkbox" id="dgs-03-flip"><label for="dgs-03-flip">Reverse</label>
  </fieldset>

  <div class="dgs-03__stage">
    <section class="dgs-03__intro" aria-labelledby="dgs-03-a">
      <div class="dgs-03__wrap">
        <p class="dgs-03__eyebrow">Marbrook Clinic</p>
        <h2 class="dgs-03__display" id="dgs-03-a">Therapy that fits around a working week</h2>
        <p class="dgs-03__lede">Fifty-minute sessions, evenings and weekends included, with the same clinician every time. Most members are matched within three days.</p>
        <ul class="dgs-03__chips">
          <li>Matched in 3 days</li>
          <li>Evening slots</li>
          <li>Covered by 40+ insurers</li>
        </ul>
      </div>
    </section>

    <section class="dgs-03__band" aria-labelledby="dgs-03-b">
      <div class="dgs-03__wrap">
        <h2 class="dgs-03__h2" id="dgs-03-b">One background, two colours, no extra element</h2>
        <p class="dgs-03__body">The boundary between cream and clay is not a border or a pseudo-element — it is a hard colour stop inside a single <code class="dgs-03__code">linear-gradient()</code> painted on this one section. Because a gradient has no geometry, nothing is clipped, nothing overflows, and the join can never leave a seam.</p>
        <p class="dgs-03__mono" aria-hidden="true">background: linear-gradient(var(--dir), var(--from) 0 50%, var(--to) 50% 100%)</p>
        <div class="dgs-03__quote">
          <blockquote>
            <p>I had cancelled on two clinics before because of my shifts. Booking around them instead was the difference.</p>
          </blockquote>
          <figcaption class="dgs-03__by"><span>Priya R.</span><span>Member since 2025</span></figcaption>
        </div>
      </div>
    </section>

    <section class="dgs-03__after" aria-labelledby="dgs-03-c">
      <div class="dgs-03__wrap">
        <h2 class="dgs-03__h3" id="dgs-03-c">What happens in week one</h2>
        <ol class="dgs-03__steps">
          <li><span>01</span><strong>Fifteen-minute intake call</strong><em>A clinician, not a form — usually the same day you sign up.</em></li>
          <li><span>02</span><strong>Two matches to choose from</strong><em>Profiles, availability and approach, side by side.</em></li>
          <li><span>03</span><strong>First session booked</strong><em>Video or phone, and you keep the slot each week.</em></li>
        </ol>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Instrument+Sans:wght@400;500;600&display=swap');

.dgs-03 {
  --stop: 46%;
  --dir: 172deg;
  --cream: #faf5ee;
  --cream2: #f2e9dc;
  --clay: #b5502f;
  --clay-ink: #fdf6f0;
  --ink: #22190f;
  --muted: #6b5c4c;
  --line: #e2d5c3;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--cream);
  color: var(--ink);
  font-family: 'Instrument Sans', system-ui, -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

.dgs-03 *,
.dgs-03 *::before,
.dgs-03 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.6 0.14 40)) {
  .dgs-03 {
    --cream: oklch(0.973 0.014 75);
    --cream2: oklch(0.935 0.024 75);
    --clay: oklch(0.535 0.135 39);
    --clay-ink: oklch(0.975 0.012 60);
    --ink: oklch(0.24 0.03 60);
    --muted: oklch(0.5 0.03 62);
    --line: oklch(0.885 0.028 72);
  }
}

.dgs-03__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-03__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.dgs-03__ctl {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 40;
  margin: 0;
  padding: .25rem;
  display: flex;
  gap: .15rem;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: rgba(250,245,238,.85);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
}

.dgs-03__ctl label {
  min-inline-size: 2.9rem;
  min-block-size: 2.5rem;
  display: grid;
  place-items: center;
  padding-inline: .75rem;
  border-radius: 999px;
  font-size: .76rem;
  font-weight: 500;
  color: var(--muted);
  cursor: pointer;
  transition: background .2s ease, color .2s ease;
}

.dgs-03__ctl label:hover {
  color: var(--ink);
}

.dgs-03__sr:checked + label {
  background: var(--clay);
  color: var(--clay-ink);
}

.dgs-03__sr:focus-visible + label {
  outline: 2px solid var(--clay);
  outline-offset: 2px;
}

.dgs-03__stage {
  display: flow-root;
}

.dgs-03__wrap {
  inline-size: min(66rem, 100%);
  margin-inline: auto;
}

.dgs-03__intro {
  background: var(--cream);
  padding: clamp(4rem, 10vw, 7rem) clamp(1.25rem, 5vw, 4rem) clamp(3.5rem, 8vw, 5.5rem);
}

.dgs-03__eyebrow {
  margin: 0 0 1rem;
  font-size: .74rem;
  font-weight: 600;
  letter-spacing: .2em;
  text-transform: uppercase;
  color: var(--clay);
}

.dgs-03__display {
  margin: 0 0 1.25rem;
  max-inline-size: 26ch;
  font-family: 'Instrument Serif', ui-serif, Georgia, serif;
  font-weight: 400;
  font-size: clamp(2.4rem, 8vw, 5rem);
  line-height: 1.0;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.dgs-03__lede {
  margin: 0 0 1.75rem;
  max-inline-size: 48ch;
  font-size: clamp(1.02rem, 2vw, 1.2rem);
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-03__chips {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
}

.dgs-03__chips li {
  padding: .45rem .9rem;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--cream2);
  font-size: .84rem;
}

.dgs-03__band {
  position: relative;
  z-index: 1;
  margin-block-start: -1px;
  color: var(--clay-ink);
  background: linear-gradient(var(--dir), var(--cream) 0 var(--stop), var(--clay) var(--stop) 100%);
  padding: clamp(3rem, 7vw, 4.5rem) clamp(1.25rem, 5vw, 4rem) clamp(4rem, 9vw, 6.5rem);
}

.dgs-03__h2 {
  margin: 0 0 1.1rem;
  max-inline-size: 30ch;
  color: var(--ink);
  font-family: 'Instrument Serif', ui-serif, Georgia, serif;
  font-weight: 400;
  font-size: clamp(1.75rem, 5vw, 3.1rem);
  line-height: 1.06;
  letter-spacing: -.02em;
  text-wrap: balance;
}

.dgs-03__body {
  margin: 0 0 1.4rem;
  max-inline-size: 58ch;
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-03__code {
  font-family: ui-monospace, 'SF Mono', Menlo, monospace;
  font-size: .88em;
  padding: .1em .35em;
  border-radius: 4px;
  background: rgba(34,25,15,.07);
}

.dgs-03__mono {
  margin: 0 0 clamp(2.5rem, 6vw, 4rem);
  font-family: ui-monospace, 'SF Mono', Menlo, monospace;
  font-size: clamp(.62rem, 1.5vw, .76rem);
  color: var(--clay);
  overflow-wrap: anywhere;
}

.dgs-03__quote {
  max-inline-size: 44rem;
  padding: clamp(1.5rem, 4vw, 2.25rem);
  border: 1px solid rgba(253,246,240,.35);
  border-radius: 18px;
  background: rgba(253,246,240,.09);
  -webkit-backdrop-filter: blur(4px);
  backdrop-filter: blur(4px);
}

.dgs-03__quote blockquote {
  margin: 0;
}

.dgs-03__quote p {
  margin: 0;
  font-family: 'Instrument Serif', ui-serif, Georgia, serif;
  font-size: clamp(1.15rem, 2.8vw, 1.65rem);
  line-height: 1.28;
  font-style: italic;
  text-wrap: pretty;
}

.dgs-03__by {
  margin-block-start: 1.1rem;
  display: flex;
  flex-wrap: wrap;
  gap: .3rem 1rem;
  font-size: .8rem;
  letter-spacing: .04em;
}

.dgs-03__by span:last-child {
  opacity: .72;
}

.dgs-03__after {
  background: var(--cream2);
  padding: clamp(3.5rem, 8vw, 5.5rem) clamp(1.25rem, 5vw, 4rem) clamp(4rem, 9vw, 6.5rem);
}

.dgs-03__h3 {
  margin: 0 0 1.75rem;
  font-family: 'Instrument Serif', ui-serif, Georgia, serif;
  font-weight: 400;
  font-size: clamp(1.5rem, 4vw, 2.3rem);
  letter-spacing: -.02em;
}

.dgs-03__steps {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1.25rem;
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
}

.dgs-03__steps li {
  display: grid;
  gap: .35rem;
  padding-block-start: 1rem;
  border-block-start: 1px solid var(--clay);
}

.dgs-03__steps span {
  font-family: ui-monospace, Menlo, monospace;
  font-size: .72rem;
  letter-spacing: .12em;
  color: var(--clay);
}

.dgs-03__steps strong {
  font-size: 1.02rem;
  letter-spacing: -.01em;
}

.dgs-03__steps em {
  font-style: normal;
  font-size: .92rem;
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-03:has(#dgs-03-a1:checked) {
  --dir: 177deg;
}

.dgs-03:has(#dgs-03-a3:checked) {
  --dir: 163deg;
}

.dgs-03:has(#dgs-03-flip:checked) {
  --dir: 188deg;
}

.dgs-03:has(#dgs-03-flip:checked):has(#dgs-03-a1:checked) {
  --dir: 183deg;
}

.dgs-03:has(#dgs-03-flip:checked):has(#dgs-03-a3:checked) {
  --dir: 197deg;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-03 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-03__band {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
    border-block-start: 1px solid CanvasText;
  }

  .dgs-03__h2,
    .dgs-03__body,
    .dgs-03__mono {
    color: CanvasText;
  }

  .dgs-03__quote,
    .dgs-03__chips li,
    .dgs-03__ctl label {
    border: 1px solid CanvasText;
  }

  .dgs-03__sr:checked + label {
    background: Highlight;
    color: HighlightText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-03__sronly,
.dgs-03__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-03__theme {
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

.dgs-03__theme:hover {
  translate: 0 -1px;
}

.dgs-03__sronly:focus-visible + .dgs-03__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-03__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-03__i--sun {
  display: none;
}

.dgs-03:has(#dgs-03-dark:checked) .dgs-03__i--moon {
  display: none;
}

.dgs-03:has(#dgs-03-dark:checked) .dgs-03__i--sun {
  display: block;
}

.dgs-03:has(#dgs-03-dark:checked) {
  --cream: #14150f;
  --ink: #f3f2ea;
  --muted: #a0a094;
  --line: #2f302a;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-03__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-03__theme {
    border-color: CanvasText;
  }
}
```
