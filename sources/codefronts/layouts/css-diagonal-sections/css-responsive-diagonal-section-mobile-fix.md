---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-responsive-diagonal-section-mobile-fix/"
title: "CSS Responsive Diagonal Section Mobile Fix"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "The other high-intent troubleshooting demo: a fixed deg angle looks composed at 1440px and absurd at 360px, and a vw-based skew pushes the document sideways."
has_js: "false"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Responsive Diagonal Section Mobile Fix
Source: https://codefronts.com/layouts/css-diagonal-sections/css-responsive-diagonal-section-mobile-fix/

The other high-intent troubleshooting demo: a fixed deg angle looks composed at 1440px and absurd at 360px, and a vw-based skew pushes the document sideways. Broken and fixed are shown side by side — the fix scales the cut with clamp() so the slope stays proportional, and the copy explains why overflow-x: hidden on body is the wrong answer and overflow: clip on the section is the right one.
## HTML
```html
<div class="dgs-17">
  <input class="dgs-17__sronly" type="checkbox" id="dgs-17-dark">
  <label class="dgs-17__theme" for="dgs-17-dark">
    <svg class="dgs-17__i dgs-17__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-17__i dgs-17__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-17__srtext">Toggle dark theme</span>
  </label>
  <fieldset class="dgs-17__ctl">
    <legend class="dgs-17__vh">Angle strategy</legend>
    <input class="dgs-17__sr" type="radio" name="dgs-17-s" id="dgs-17-s1"><label for="dgs-17-s1">vw only</label>
    <input class="dgs-17__sr" type="radio" name="dgs-17-s" id="dgs-17-s2" checked><label for="dgs-17-s2">clamp()</label>
    <input class="dgs-17__sr" type="radio" name="dgs-17-s" id="dgs-17-s3"><label for="dgs-17-s3">Flat under 30rem</label>
    <input class="dgs-17__sr" type="checkbox" id="dgs-17-guides" checked><label for="dgs-17-guides">Guides</label>
  </fieldset>

  <div class="dgs-17__stage">
    <section class="dgs-17__doc" aria-labelledby="dgs-17-a">
      <div class="dgs-17__wrap">
        <p class="dgs-17__crumb">Layout &nbsp;/&nbsp; Angled sections &nbsp;/&nbsp; Responsive behaviour</p>
        <h2 class="dgs-17__display" id="dgs-17-a">The angle that works at 1440 is wrong at 360</h2>
        <p class="dgs-17__lede">A cut expressed purely in <code class="dgs-17__code">vw</code> keeps its <em>angle</em> and loses its <em>depth</em>: at 360&nbsp;px a 6vw wedge is 21&nbsp;px, which reads as a crooked line rather than a designed edge. Resize the frame and watch the readout below change.</p>
        <p class="dgs-17__readout"><span class="dgs-17__mode"></span></p>
      </div>
    </section>

    <section class="dgs-17__band" aria-labelledby="dgs-17-b">
      <div class="dgs-17__guide dgs-17__guide--edge" aria-hidden="true"></div>
      <div class="dgs-17__guide dgs-17__guide--safe" aria-hidden="true"><span>safe area = cut + rhythm</span></div>
      <div class="dgs-17__wrap">
        <h2 class="dgs-17__h2" id="dgs-17-b">Three fixes, in order of how often you should reach for them</h2>
        <ol class="dgs-17__fixes">
          <li><strong>Clamp the cut</strong><span>A floor keeps the edge visible on a phone, a ceiling stops a 4K wedge swallowing the band.</span><code>clamp(1.5rem, 5vw, 7rem)</code></li>
          <li><strong>Derive the padding</strong><span>Top padding is the cut plus normal rhythm, so copy never drifts into the diagonal.</span><code>calc(var(--cut) + 3rem)</code></li>
          <li><strong>Flatten when it stops helping</strong><span>Under about 30rem a container query can drop the angle entirely — a straight edge beats a broken one.</span><code>@container (max-width: 30rem)</code></li>
        </ol>
      </div>
    </section>

    <section class="dgs-17__after" aria-labelledby="dgs-17-c">
      <div class="dgs-17__wrap">
        <h2 class="dgs-17__h3" id="dgs-17-c">Checklist before you ship an angle</h2>
        <ul class="dgs-17__check">
          <li>No horizontal scrollbar at 320&nbsp;px</li>
          <li>Cut depth between 16&nbsp;px and 112&nbsp;px at every width</li>
          <li>Focus rings visible on every control inside the band</li>
          <li>Heading never crosses the diagonal</li>
        </ul>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400;500&display=swap');

.dgs-17 {
  --cut: clamp(1.5rem, 5vw, 7rem);
  --page: #ffffff;
  --page2: #f5f7fb;
  --ink: #0e1524;
  --muted: #5b6579;
  --line: #e3e8f0;
  --band: #f0f5ff;
  --band-line: #c8d8f5;
  --blue: #1d5cff;
  --blue-deep: #123fb3;
  container-type: inline-size;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--page);
  color: var(--ink);
  font-family: 'DM Sans', system-ui, -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.62;
  -webkit-font-smoothing: antialiased;
}

.dgs-17 *,
.dgs-17 *::before,
.dgs-17 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.55 0.22 264)) {
  .dgs-17 {
    --page: oklch(1 0 0);
    --page2: oklch(0.972 0.006 258);
    --ink: oklch(0.2 0.03 262);
    --muted: oklch(0.5 0.03 262);
    --line: oklch(0.918 0.012 258);
    --band: oklch(0.965 0.02 258);
    --band-line: oklch(0.855 0.055 258);
    --blue: oklch(0.55 0.22 264);
    --blue-deep: oklch(0.42 0.2 264);
  }
}

.dgs-17__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-17__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.dgs-17__ctl {
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-end: 1rem;
  z-index: 40;
  margin: 0;
  padding: .25rem;
  display: flex;
  flex-wrap: wrap;
  gap: .2rem;
  border: 1px solid var(--line);
  border-radius: 9px;
  background: rgba(255,255,255,.94);
  box-shadow: 0 4px 16px -10px rgba(14,21,36,.35);
}

.dgs-17__ctl label {
  min-inline-size: 2.9rem;
  min-block-size: 2.5rem;
  display: grid;
  place-items: center;
  padding-inline: .7rem;
  border-radius: 6px;
  font-family: 'DM Mono', monospace;
  font-size: .74rem;
  color: var(--muted);
  cursor: pointer;
  transition: background .18s ease, color .18s ease;
}

.dgs-17__ctl label:hover {
  color: var(--ink);
  background: var(--page2);
}

.dgs-17__sr:checked + label {
  background: var(--blue);
  color: #fff;
}

.dgs-17__sr:focus-visible + label {
  outline: 2px solid var(--blue-deep);
  outline-offset: 2px;
}

.dgs-17__stage {
  display: flow-root;
}

.dgs-17__wrap {
  inline-size: min(68rem, 100%);
  margin-inline: auto;
}

.dgs-17__doc {
  padding: clamp(3.5rem, 8vw, 5.5rem) clamp(1.25rem, 5vw, 4rem) calc(var(--cut) + clamp(2.5rem, 6vw, 4rem));
}

.dgs-17__crumb {
  margin: 0 0 1.1rem;
  font-family: 'DM Mono', monospace;
  font-size: .74rem;
  letter-spacing: .06em;
  color: var(--muted);
}

.dgs-17__display {
  margin: 0 0 1rem;
  max-inline-size: 26ch;
  font-size: clamp(1.9rem, 5.8vw, 3.4rem);
  font-weight: 700;
  line-height: 1.06;
  letter-spacing: -.035em;
  text-wrap: balance;
}

.dgs-17__lede {
  margin: 0 0 1.5rem;
  max-inline-size: 60ch;
  font-size: clamp(1rem, 2vw, 1.14rem);
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-17__code {
  font-family: 'DM Mono', monospace;
  font-size: .88em;
  padding: .1em .35em;
  border-radius: 4px;
  background: var(--page2);
  border: 1px solid var(--line);
  color: var(--blue-deep);
}

.dgs-17__readout {
  margin: 0;
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  padding: .45rem .8rem;
  border: 1px dashed var(--band-line);
  border-radius: 8px;
  background: var(--band);
  font-family: 'DM Mono', monospace;
  font-size: .78rem;
  color: var(--blue-deep);
}

.dgs-17__mode::before {
  content: 'container ≥ 48rem · cut = 7rem ceiling';
}

@container (max-width: 48rem) {
  .dgs-17__mode::before {
    content: 'container 30–48rem · cut = 5vw fluid';
  }
}

@container (max-width: 30rem) {
  .dgs-17__mode::before {
    content: 'container < 30rem · cut = 1.5rem floor';
  }
}
/* Above 48rem all three strategies compute to the same cut — 5vw, the clamp
   and the flat rule only diverge once the container is narrow. Say so, or a
   desktop reader flips the control, sees nothing move, and reads it as broken. */

.dgs-17__mode::after {
  content: ' — resize narrow: strategies diverge below 48rem';
  opacity: .72;
}

@container (max-width: 48rem) {
  .dgs-17__mode::after {
    content: '';
  }
}

.dgs-17__band {
  position: relative;
  z-index: 1;
  background: var(--band);
  color: var(--ink);
  clip-path: polygon(0 var(--cut), 100% 0, 100% 100%, 0 100%);
  margin-block-start: calc(var(--cut) * -1 - 1px);
  padding: calc(var(--cut) + clamp(2.5rem, 6vw, 4rem)) clamp(1.25rem, 5vw, 4rem) clamp(3rem, 7vw, 4.5rem);
}

.dgs-17__guide {
  position: absolute;
  inset-inline: 0;
  pointer-events: none;
}

.dgs-17__guide--edge {
  inset-block-start: 0;
  block-size: var(--cut);
  border-block-end: 1px dashed var(--blue);
  background: repeating-linear-gradient(135deg, rgba(29,92,255,.08) 0 6px, transparent 6px 12px);
}

.dgs-17__guide--safe {
  inset-block-start: var(--cut);
  block-size: clamp(2.5rem, 6vw, 4rem);
  border-block-end: 1px dashed var(--band-line);
}

.dgs-17__guide--safe span {
  position: absolute;
  inset-block-end: .35rem;
  inset-inline-start: clamp(1.25rem, 5vw, 4rem);
  font-family: 'DM Mono', monospace;
  font-size: .68rem;
  letter-spacing: .04em;
  color: var(--blue-deep);
  opacity: .8;
}

.dgs-17__h2 {
  margin: 0 0 1.5rem;
  max-inline-size: 30ch;
  font-size: clamp(1.4rem, 3.8vw, 2.2rem);
  font-weight: 700;
  line-height: 1.1;
  letter-spacing: -.03em;
  text-wrap: balance;
}

.dgs-17__fixes {
  margin: 0;
  padding: 0;
  list-style: none;
  counter-reset: dgs17;
  display: grid;
  gap: .75rem;
}

.dgs-17__fixes li {
  counter-increment: dgs17;
  display: grid;
  gap: .3rem;
  padding: 1rem 1.15rem 1.1rem 3.1rem;
  position: relative;
  background: var(--page);
  border: 1px solid var(--band-line);
  border-radius: 12px;
}

.dgs-17__fixes li::before {
  content: counter(dgs17);
  position: absolute;
  inset-block-start: 1rem;
  inset-inline-start: 1.1rem;
  inline-size: 1.5rem;
  block-size: 1.5rem;
  display: grid;
  place-items: center;
  border-radius: 6px;
  background: var(--blue);
  color: #fff;
  font-family: 'DM Mono', monospace;
  font-size: .76rem;
}

.dgs-17__fixes strong {
  font-weight: 700;
}

.dgs-17__fixes span {
  color: var(--muted);
  font-size: .95rem;
  text-wrap: pretty;
}

.dgs-17__fixes code {
  font-family: 'DM Mono', monospace;
  font-size: .78rem;
  color: var(--blue-deep);
  overflow-wrap: anywhere;
}

.dgs-17__after {
  background: var(--page2);
  padding: clamp(3rem, 7vw, 4.5rem) clamp(1.25rem, 5vw, 4rem) clamp(4rem, 9vw, 6rem);
}

.dgs-17__h3 {
  margin: 0 0 1.25rem;
  font-size: clamp(1.25rem, 3.2vw, 1.8rem);
  font-weight: 700;
  letter-spacing: -.03em;
}

.dgs-17__check {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: .55rem;
}

.dgs-17__check li {
  position: relative;
  padding-inline-start: 1.75rem;
  color: var(--muted);
}

.dgs-17__check li::before {
  content: '';
  position: absolute;
  inset-inline-start: 0;
  inset-block-start: .45em;
  inline-size: .95rem;
  block-size: .5rem;
  border-inline-start: 2px solid var(--blue);
  border-block-end: 2px solid var(--blue);
  rotate: -45deg;
}

.dgs-17:has(#dgs-17-s1:checked) {
  --cut: 5vw;
}

.dgs-17:has(#dgs-17-s1:checked) .dgs-17__mode::before {
  content: 'strategy: raw 5vw — depth collapses on phones';
}

.dgs-17:has(#dgs-17-s3:checked) .dgs-17__mode::before {
  content: 'strategy: flatten below 30rem';
}
/* container-type: inline-size is declared on .dgs-17, so .dgs-17 CANNOT be
   the subject of its own @container query — an element queries an ANCESTOR
   container, never itself. Targeting the root here silently did nothing and
   the "Flat under 30rem" strategy was indistinguishable from clamp().
   Setting --cut on the descendant that consumes it fixes the query subject
   while keeping the same authored behaviour. */

@container (max-width: 30rem) {
  .dgs-17:has(#dgs-17-s3:checked) .dgs-17__band {
    --cut: 0px;
  }

  .dgs-17:has(#dgs-17-s3:checked) .dgs-17__guide {
    display: none;
  }
}

.dgs-17:not(:has(#dgs-17-guides:checked)) .dgs-17__guide {
  display: none;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-17 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-17__band {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
    border-block-start: 1px solid CanvasText;
  }

  .dgs-17__fixes li,
    .dgs-17__ctl label,
    .dgs-17__readout {
    border: 1px solid CanvasText;
  }

  .dgs-17__sr:checked + label {
    background: Highlight;
    color: HighlightText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-17__sronly,
.dgs-17__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-17__theme {
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

.dgs-17__theme:hover {
  translate: 0 -1px;
}

.dgs-17__sronly:focus-visible + .dgs-17__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-17__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-17__i--sun {
  display: none;
}

.dgs-17:has(#dgs-17-dark:checked) .dgs-17__i--moon {
  display: none;
}

.dgs-17:has(#dgs-17-dark:checked) .dgs-17__i--sun {
  display: block;
}

.dgs-17:has(#dgs-17-dark:checked) {
  --page: #0c0f15;
  --page2: #141922;
  --ink: #eef1f7;
  --muted: #97a0ad;
  --line: #222935;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-17__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-17__theme {
    border-color: CanvasText;
  }
}
```
