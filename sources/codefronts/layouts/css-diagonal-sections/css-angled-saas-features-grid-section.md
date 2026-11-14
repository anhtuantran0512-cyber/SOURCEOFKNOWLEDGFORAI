---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-angled-saas-features-grid-section/"
title: "CSS Angled SaaS Features Grid Section"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "Four feature columns with inline SVG icons inside an angled band."
has_js: "false"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Angled SaaS Features Grid Section
Source: https://codefronts.com/layouts/css-diagonal-sections/css-angled-saas-features-grid-section/

Four feature columns with inline SVG icons inside an angled band. The grid is a plain auto-fit layout that knows nothing about the geometry — the section is clipped, the columns are not — which is the whole point: an angled band is a container decision, and everything inside it stays on the normal grid.
## HTML
```html
<div class="dgs-07">
  <input class="dgs-07__sronly" type="checkbox" id="dgs-07-dark">
  <label class="dgs-07__theme" for="dgs-07-dark">
    <svg class="dgs-07__i dgs-07__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-07__i dgs-07__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-07__srtext">Toggle dark theme</span>
  </label>
  <fieldset class="dgs-07__ctl">
    <legend class="dgs-07__vh">Band controls</legend>
    <input class="dgs-07__sr" type="radio" name="dgs-07-t" id="dgs-07-t1" checked><label for="dgs-07-t1">Lilac</label>
    <input class="dgs-07__sr" type="radio" name="dgs-07-t" id="dgs-07-t2"><label for="dgs-07-t2">Sage</label>
    <input class="dgs-07__sr" type="radio" name="dgs-07-t" id="dgs-07-t3"><label for="dgs-07-t3">Apricot</label>
    <input class="dgs-07__sr" type="checkbox" id="dgs-07-tight"><label for="dgs-07-tight">Compact</label>
  </fieldset>

  <div class="dgs-07__stage">
    <section class="dgs-07__intro" aria-labelledby="dgs-07-a">
      <div class="dgs-07__wrap">
        <p class="dgs-07__eyebrow">Loop &mdash; design review</p>
        <h2 class="dgs-07__display" id="dgs-07-a">Feedback that lands on the frame, not in a thread</h2>
        <p class="dgs-07__lede">Comments live on the artboard, versions are diffed side by side, and every decision is written back to the file it belongs to.</p>
      </div>
    </section>

    <section class="dgs-07__band" aria-labelledby="dgs-07-b">
      <div class="dgs-07__wrap">
        <header class="dgs-07__head">
          <p class="dgs-07__eyebrow dgs-07__eyebrow--on">Built for review day</p>
          <h2 class="dgs-07__h2" id="dgs-07-b">Six things reviewers stop asking for</h2>
        </header>
        <ul class="dgs-07__cards">
          <li>
            <span class="dgs-07__icon"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><rect x="3.5" y="4.5" width="17" height="12" rx="2.2" stroke="currentColor" stroke-width="1.8"/><path d="M8 20h8M12 16.5V20" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></span>
            <strong>Pinned frame comments</strong>
            <p>Threads anchor to coordinates and survive a re-export.</p>
          </li>
          <li>
            <span class="dgs-07__icon"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 3v18M4 8h16M4 16h16" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></span>
            <strong>Version diffing</strong>
            <p>Two revisions, one overlay, changed layers highlighted.</p>
          </li>
          <li>
            <span class="dgs-07__icon"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="8.2" stroke="currentColor" stroke-width="1.8"/><path d="M12 8.2v4.4l3 1.9" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></span>
            <strong>Review deadlines</strong>
            <p>Auto-nudges at 24 hours, escalation at 48.</p>
          </li>
          <li>
            <span class="dgs-07__icon"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M4 7h10M4 12h16M4 17h7" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></span>
            <strong>Decision log</strong>
            <p>Every approval written back as a file annotation.</p>
          </li>
          <li>
            <span class="dgs-07__icon"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M12 4.5 19 8v8l-7 3.5L5 16V8l7-3.5Z" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg></span>
            <strong>Token sync</strong>
            <p>Colour and type changes flow to the code side.</p>
          </li>
          <li>
            <span class="dgs-07__icon"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="9" cy="9" r="3.4" stroke="currentColor" stroke-width="1.8"/><path d="M3.8 19.5c.9-2.9 2.9-4.4 5.2-4.4s4.3 1.5 5.2 4.4M16 6.2a3.4 3.4 0 0 1 0 6.6" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg></span>
            <strong>Guest reviewers</strong>
            <p>Client links that expire without a seat licence.</p>
          </li>
        </ul>
      </div>
    </section>

    <section class="dgs-07__after" aria-labelledby="dgs-07-c">
      <div class="dgs-07__wrap dgs-07__row">
        <h2 class="dgs-07__h3" id="dgs-07-c">Cards inside an angled band</h2>
        <p class="dgs-07__body">The grid never knows about the angle. All the geometry is on the section: a clipped top edge, a negative pull-up, and top padding equal to the cut plus the usual rhythm — so no card ever collides with the diagonal.</p>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap');

.dgs-07 {
  --cut: clamp(1.75rem, 5.5vw, 7rem);
  --pad: clamp(1.35rem, 3vw, 1.85rem);
  --band: #ece7ff;
  --band-ink: #241a4d;
  --band-soft: #5b4fa0;
  --accent: #6d4df6;
  --page: #ffffff;
  --page2: #f7f6fb;
  --ink: #17151f;
  --muted: #5c5a6b;
  --line: #e8e6f0;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--page);
  color: var(--ink);
  font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

.dgs-07 *,
.dgs-07 *::before,
.dgs-07 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.6 0.2 292)) {
  .dgs-07 {
    --band: oklch(0.925 0.045 295);
    --band-ink: oklch(0.28 0.09 292);
    --band-soft: oklch(0.48 0.09 292);
    --accent: oklch(0.56 0.22 291);
    --page: oklch(1 0 0);
    --page2: oklch(0.972 0.006 292);
    --ink: oklch(0.19 0.02 292);
    --muted: oklch(0.5 0.02 292);
    --line: oklch(0.918 0.01 292);
  }
}

.dgs-07__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-07__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.dgs-07__ctl {
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
  background: rgba(255,255,255,.92);
  box-shadow: 0 6px 22px -14px rgba(23,21,31,.4);
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
}

.dgs-07__ctl label {
  min-inline-size: 3rem;
  min-block-size: 2.5rem;
  display: grid;
  place-items: center;
  padding-inline: .8rem;
  border-radius: 999px;
  font-size: .78rem;
  font-weight: 500;
  color: var(--muted);
  cursor: pointer;
  transition: background .2s ease, color .2s ease;
}

.dgs-07__ctl label:hover {
  color: var(--ink);
  background: var(--page2);
}

.dgs-07__sr:checked + label {
  background: var(--accent);
  color: #fff;
}

.dgs-07__sr:focus-visible + label {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.dgs-07__stage {
  display: flow-root;
}

.dgs-07__wrap {
  inline-size: min(74rem, 100%);
  margin-inline: auto;
}

.dgs-07__intro {
  padding: clamp(4rem, 9vw, 6.5rem) clamp(1.25rem, 5vw, 4rem) calc(var(--cut) + clamp(2.5rem, 6vw, 4rem));
}

.dgs-07__eyebrow {
  margin: 0 0 .9rem;
  font-size: .76rem;
  font-weight: 600;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: var(--accent);
}

.dgs-07__eyebrow--on {
  color: var(--band-soft);
}

.dgs-07__display {
  margin: 0 0 1rem;
  max-inline-size: 24ch;
  font-size: clamp(2.1rem, 6.5vw, 4rem);
  font-weight: 700;
  line-height: 1.04;
  letter-spacing: -.04em;
  text-wrap: balance;
}

.dgs-07__lede {
  margin: 0;
  max-inline-size: 50ch;
  font-size: clamp(1.02rem, 2vw, 1.2rem);
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-07__band {
  position: relative;
  z-index: 1;
  background: var(--band);
  color: var(--band-ink);
  clip-path: polygon(0 var(--cut), 100% 0, 100% 100%, 0 100%);
  margin-block-start: calc(var(--cut) * -1 - 1px);
  padding: calc(var(--cut) + clamp(3rem, 7vw, 5rem)) clamp(1.25rem, 5vw, 4rem) clamp(3.5rem, 8vw, 5.5rem);
}

.dgs-07__head {
  margin-block-end: clamp(1.75rem, 4vw, 2.75rem);
}

.dgs-07__h2 {
  margin: 0;
  max-inline-size: 22ch;
  font-size: clamp(1.6rem, 4.4vw, 2.6rem);
  font-weight: 700;
  line-height: 1.06;
  letter-spacing: -.035em;
  text-wrap: balance;
}

.dgs-07__cards {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: clamp(.75rem, 1.6vw, 1.1rem);
  grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
}

.dgs-07__cards li {
  display: grid;
  gap: .55rem;
  align-content: start;
  padding: var(--pad);
  border-radius: 18px;
  background: var(--page);
  border: 1px solid rgba(36,26,77,.07);
  box-shadow: 0 1px 2px rgba(36,26,77,.05), 0 14px 30px -24px rgba(36,26,77,.5);
  transition: translate .24s cubic-bezier(.2,.8,.3,1), box-shadow .24s ease;
}

.dgs-07__cards li:hover {
  translate: 0 -3px;
  box-shadow: 0 2px 4px rgba(36,26,77,.06), 0 22px 40px -26px rgba(36,26,77,.6);
}

.dgs-07__icon {
  inline-size: 2.5rem;
  block-size: 2.5rem;
  display: grid;
  place-items: center;
  border-radius: 12px;
  background: var(--band);
  color: var(--accent);
}

.dgs-07__icon svg {
  inline-size: 1.3rem;
  block-size: 1.3rem;
}

.dgs-07__cards strong {
  font-size: 1.02rem;
  font-weight: 600;
  letter-spacing: -.015em;
  color: var(--ink);
}

.dgs-07__cards p {
  margin: 0;
  font-size: .92rem;
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-07__after {
  background: var(--page2);
  padding: clamp(3rem, 7vw, 5rem) clamp(1.25rem, 5vw, 4rem) clamp(4rem, 9vw, 6rem);
}

.dgs-07__row {
  display: grid;
  gap: 1rem clamp(2rem, 6vw, 4rem);
  grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
  align-items: start;
}

.dgs-07__h3 {
  margin: 0;
  font-size: clamp(1.3rem, 3.4vw, 1.9rem);
  font-weight: 700;
  letter-spacing: -.03em;
}

.dgs-07__body {
  margin: 0;
  max-inline-size: 56ch;
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-07:has(#dgs-07-t2:checked) {
  --band: #e2f0e4;
  --band-ink: #16301f;
  --band-soft: #3d6b4b;
  --accent: #2f8055;
}

.dgs-07:has(#dgs-07-t3:checked) {
  --band: #ffeadf;
  --band-ink: #3d1f10;
  --band-soft: #8a4b2a;
  --accent: #c9581f;
}

.dgs-07:has(#dgs-07-tight:checked) {
  --pad: 1rem;
}

.dgs-07:has(#dgs-07-tight:checked) .dgs-07__cards {
  grid-template-columns: repeat(auto-fit, minmax(12rem, 1fr));
}

@media (prefers-reduced-motion: reduce) {
  .dgs-07 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-07__band {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
    border-block-start: 1px solid CanvasText;
  }

  .dgs-07__cards li,
    .dgs-07__icon,
    .dgs-07__ctl label {
    border: 1px solid CanvasText;
    box-shadow: none;
  }

  .dgs-07__sr:checked + label {
    background: Highlight;
    color: HighlightText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-07__sronly,
.dgs-07__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-07__theme {
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

.dgs-07__theme:hover {
  translate: 0 -1px;
}

.dgs-07__sronly:focus-visible + .dgs-07__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-07__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-07__i--sun {
  display: none;
}

.dgs-07:has(#dgs-07-dark:checked) .dgs-07__i--moon {
  display: none;
}

.dgs-07:has(#dgs-07-dark:checked) .dgs-07__i--sun {
  display: block;
}

.dgs-07:has(#dgs-07-dark:checked) {
  --page: #0c0f14;
  --page2: #141922;
  --ink: #eef2f8;
  --muted: #96a0b0;
  --line: #222935;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-07__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-07__theme {
    border-color: CanvasText;
  }
}
```
