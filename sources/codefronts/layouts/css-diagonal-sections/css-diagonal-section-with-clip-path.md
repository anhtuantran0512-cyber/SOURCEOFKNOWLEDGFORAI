---
source: "codefronts"
url: "https://codefronts.com/layouts/css-diagonal-sections/css-diagonal-section-with-clip-path/"
title: "CSS Diagonal Section with clip-path"
section: "layouts"
category: "css-diagonal-sections"
category_name: "CSS Diagonal Sections"
description: "The reference build every other demo in this collection varies: one clip-path: polygon() on the section, one --cut custom property driving the angle, and…"
has_js: "false"
---

Here's a working CSS Diagonal Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Diagonal Section with clip-path
Source: https://codefronts.com/layouts/css-diagonal-sections/css-diagonal-section-with-clip-path/

The reference build every other demo in this collection varies: one clip-path: polygon() on the section, one --cut custom property driving the angle, and flat neighbours above and below so the diagonal is unmistakable. The band is pulled up under the section above it by exactly its own cut depth, which is what makes the two blocks read as a single continuous page instead of a floating panel.
## HTML
```html
<div class="dgs-01">
  <input class="dgs-01__sronly" type="checkbox" id="dgs-01-dark">
  <label class="dgs-01__theme" for="dgs-01-dark">
    <svg class="dgs-01__i dgs-01__i--moon" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M20.5 14.3A8.4 8.4 0 0 1 9.7 3.5a8.5 8.5 0 1 0 10.8 10.8Z" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round"/></svg>
    <svg class="dgs-01__i dgs-01__i--sun" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4.1" stroke="currentColor" stroke-width="1.7"/><path d="M12 3.2v2M12 18.8v2M3.2 12h2M18.8 12h2M5.7 5.7l1.4 1.4M16.9 16.9l1.4 1.4M18.3 5.7l-1.4 1.4M7.1 16.9l-1.4 1.4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>
    <span class="dgs-01__srtext">Toggle dark theme</span>
  </label>
  <fieldset class="dgs-01__ctl">
    <legend class="dgs-01__vh">Angled band controls</legend>
    <input class="dgs-01__sr" type="radio" name="dgs-01-cut" id="dgs-01-c1"><label for="dgs-01-c1">3vw</label>
    <input class="dgs-01__sr" type="radio" name="dgs-01-cut" id="dgs-01-c2" checked><label for="dgs-01-c2">5vw</label>
    <input class="dgs-01__sr" type="radio" name="dgs-01-cut" id="dgs-01-c3"><label for="dgs-01-c3">9vw</label>
    <input class="dgs-01__sr" type="checkbox" id="dgs-01-flip"><label class="dgs-01__wide" for="dgs-01-flip">Mirror</label>
    <input class="dgs-01__sr" type="checkbox" id="dgs-01-invert"><label class="dgs-01__wide" for="dgs-01-invert">Invert</label>
  </fieldset>

  <div class="dgs-01__stage">
    <section class="dgs-01__masthead" aria-labelledby="dgs-01-a">
      <div class="dgs-01__wrap">
        <p class="dgs-01__kicker"><span>Northwind Deploy</span><span>Issue 04 — Preview Environments</span></p>
        <h2 class="dgs-01__display" id="dgs-01-a">Every branch<br>gets a URL</h2>
        <div class="dgs-01__lead">
          <p>Push, and a preview build is live in about forty seconds. Reviewers open a link instead of pulling a branch, and the environment is torn down the moment the pull request closes.</p>
          <dl class="dgs-01__meta">
            <div><dt>Regions</dt><dd>34</dd></div>
            <div><dt>Median build</dt><dd>40s</dd></div>
            <div><dt>Config</dt><dd>None</dd></div>
          </dl>
        </div>
      </div>
    </section>

    <section class="dgs-01__cut" aria-labelledby="dgs-01-b">
      <div class="dgs-01__wrap">
        <p class="dgs-01__rule"><span>01</span> The cut is one custom property deep</p>
        <h2 class="dgs-01__h2" id="dgs-01-b">A single polygon, four coordinates, zero wrappers</h2>
        <p class="dgs-01__body">This band is an ordinary block section. <code class="dgs-01__code">clip-path: polygon()</code> removes the triangle above the diagonal, and the same <code class="dgs-01__code">--cut</code> token that shapes the polygon also pulls the band up under its neighbour and pads the copy clear of the edge.</p>
        <p class="dgs-01__mono" aria-hidden="true">clip-path: polygon(0 var(--cut), 100% 0, 100% 100%, 0 100%)</p>
      </div>
    </section>

    <section class="dgs-01__foot" aria-labelledby="dgs-01-c">
      <div class="dgs-01__wrap">
        <h2 class="dgs-01__h3" id="dgs-01-c">Flat again underneath</h2>
        <p class="dgs-01__body dgs-01__body--tight">The band's bottom edge is square on purpose. Two angled edges in a row read as a slice through the page rather than a join.</p>
        <ul class="dgs-01__index">
          <li><span>Length units</span><span>Stable slope at any height</span></li>
          <li><span>Percent units</span><span>Slope drifts as content grows</span></li>
          <li><span>Seam</span><span>1px negative-margin overlap</span></li>
        </ul>
      </div>
    </section>
  </div>
</div>
```
## CSS
```css
@import url('https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;700;800&display=swap');

.dgs-01 {
  --cut: clamp(1.75rem, 5vw, 6.5rem);
  --paper: #f4f1ea;
  --paper2: #e9e5da;
  --ink: #14130f;
  --muted: #5d5a51;
  --line: #d5d0c2;
  --band: #14130f;
  --band-ink: #f6f4ee;
  --band-muted: #a8a49a;
  --accent: #d0432a;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  display: block;
  position: relative;
  box-sizing: border-box;
  overflow-x: clip;
  background: var(--paper);
  color: var(--ink);
  font-family: 'Archivo', system-ui, -apple-system, 'Segoe UI', sans-serif;
  font-size: 16px;
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
}

.dgs-01 *,
.dgs-01 *::before,
.dgs-01 *::after {
  box-sizing: border-box;
}

@supports (color: oklch(0.6 0.2 30)) {
  .dgs-01 {
    --paper: oklch(0.957 0.012 85);
    --paper2: oklch(0.918 0.015 85);
    --ink: oklch(0.18 0.01 80);
    --muted: oklch(0.48 0.012 80);
    --line: oklch(0.855 0.016 85);
    --band: oklch(0.18 0.01 80);
    --band-ink: oklch(0.96 0.008 85);
    --band-muted: oklch(0.71 0.012 85);
    --accent: oklch(0.575 0.185 32);
  }
}

.dgs-01__vh {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-01__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  opacity: 0;
  pointer-events: none;
}

.dgs-01__ctl {
  position: absolute;
  inset-block-start: 0;
  inset-inline-end: 0;
  z-index: 40;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 0;
  padding: 0;
  border: 0;
  background: var(--paper);
  border-inline-start: 1px solid var(--ink);
  border-block-end: 1px solid var(--ink);
}

.dgs-01__ctl label {
  min-inline-size: 2.75rem;
  min-block-size: 2.75rem;
  display: grid;
  place-items: center;
  padding-inline: .55rem;
  font-size: .68rem;
  font-weight: 500;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--muted);
  border-inline-start: 1px solid var(--line);
  cursor: pointer;
  transition: background .18s ease, color .18s ease;
}

.dgs-01__ctl label:first-of-type {
  border-inline-start: 0;
}

.dgs-01__ctl label:hover {
  color: var(--ink);
  background: var(--paper2);
}

.dgs-01__ctl .dgs-01__wide {
  letter-spacing: .08em;
}

.dgs-01__sr:checked + label {
  background: var(--ink);
  color: var(--paper);
}

.dgs-01__sr:focus-visible + label {
  outline: 2px solid var(--accent);
  outline-offset: -3px;
}

.dgs-01__stage {
  display: flow-root;
}

.dgs-01__wrap {
  inline-size: min(72rem, 100%);
  margin-inline: auto;
}

.dgs-01__masthead {
  padding: clamp(4rem, 9vw, 7rem) clamp(1.25rem, 5vw, 4rem) calc(var(--cut) + clamp(3rem, 7vw, 5rem));
}

.dgs-01__kicker {
  margin: 0 0 clamp(1.5rem, 4vw, 2.5rem);
  display: flex;
  flex-wrap: wrap;
  gap: .5rem 1.5rem;
  justify-content: space-between;
  padding-block-end: .7rem;
  border-block-end: 1px solid var(--ink);
  font-size: .72rem;
  font-weight: 500;
  letter-spacing: .16em;
  text-transform: uppercase;
}

.dgs-01__kicker span:first-child {
  color: var(--accent);
}

.dgs-01__kicker span:last-child {
  color: var(--muted);
}

.dgs-01__display {
  margin: 0 0 clamp(1.75rem, 4vw, 2.75rem);
  font-size: clamp(2.6rem, 11vw, 7rem);
  font-weight: 800;
  line-height: .92;
  letter-spacing: -.045em;
  text-transform: none;
}

.dgs-01__lead {
  display: grid;
  gap: clamp(1.5rem, 4vw, 3rem);
  grid-template-columns: repeat(auto-fit, minmax(17rem, 1fr));
  align-items: start;
}

.dgs-01__lead p {
  margin: 0;
  max-inline-size: 46ch;
  font-size: clamp(1.02rem, 2vw, 1.22rem);
  color: var(--muted);
  text-wrap: pretty;
}

.dgs-01__meta {
  margin: 0;
  display: grid;
  gap: 0;
  align-content: start;
}

.dgs-01__meta > div {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  padding-block: .6rem;
  border-block-start: 1px solid var(--line);
}

.dgs-01__meta > div:last-child {
  border-block-end: 1px solid var(--line);
}

.dgs-01__meta dt {
  font-size: .74rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--muted);
}

.dgs-01__meta dd {
  margin: 0;
  font-weight: 700;
  font-variant-numeric: tabular-nums;
}

.dgs-01__cut {
  position: relative;
  z-index: 1;
  background: var(--band);
  color: var(--band-ink);
  clip-path: polygon(0 var(--cut), 100% 0, 100% 100%, 0 100%);
  margin-block-start: calc(var(--cut) * -1 - 1px);
  padding: calc(var(--cut) + clamp(3rem, 7vw, 5rem)) clamp(1.25rem, 5vw, 4rem) clamp(3.5rem, 8vw, 5.5rem);
}

.dgs-01__rule {
  margin: 0 0 1.1rem;
  display: flex;
  align-items: baseline;
  gap: .8rem;
  font-size: .72rem;
  font-weight: 500;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--band-muted);
}

.dgs-01__rule span:first-child {
  color: var(--accent);
  font-weight: 700;
}

.dgs-01__h2 {
  margin: 0 0 1.1rem;
  max-inline-size: 30ch;
  font-size: clamp(1.6rem, 4.6vw, 2.9rem);
  font-weight: 700;
  line-height: 1.04;
  letter-spacing: -.035em;
  text-wrap: balance;
}

.dgs-01__h3 {
  margin: 0 0 .8rem;
  font-size: clamp(1.35rem, 3.6vw, 2.1rem);
  font-weight: 700;
  line-height: 1.1;
  letter-spacing: -.03em;
}

.dgs-01__body {
  margin: 0 0 1.6rem;
  max-inline-size: 62ch;
  color: var(--band-muted);
  text-wrap: pretty;
}

.dgs-01__foot .dgs-01__body {
  color: var(--muted);
}

.dgs-01__body--tight {
  margin-block-end: clamp(1.75rem, 4vw, 2.5rem);
}

.dgs-01__code {
  font-family: ui-monospace, 'SF Mono', Menlo, Consolas, monospace;
  font-size: .88em;
  padding: .1em .35em;
  background: rgba(255,255,255,.1);
}

.dgs-01__mono {
  margin: 0;
  font-family: ui-monospace, 'SF Mono', Menlo, Consolas, monospace;
  font-size: clamp(.62rem, 1.5vw, .78rem);
  color: var(--accent);
  overflow-wrap: anywhere;
}

.dgs-01__foot {
  background: var(--paper2);
  margin-block-start: -1px;
  padding: clamp(3.5rem, 8vw, 5.5rem) clamp(1.25rem, 5vw, 4rem) clamp(4rem, 9vw, 6.5rem);
}

.dgs-01__index {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 0;
}

.dgs-01__index li {
  display: flex;
  flex-wrap: wrap;
  gap: .25rem 1.5rem;
  justify-content: space-between;
  padding-block: .85rem;
  border-block-start: 1px solid var(--line);
}

.dgs-01__index li:last-child {
  border-block-end: 1px solid var(--line);
}

.dgs-01__index span:first-child {
  font-weight: 700;
  letter-spacing: -.01em;
}

.dgs-01__index span:last-child {
  color: var(--muted);
  font-size: .92rem;
}

.dgs-01:has(#dgs-01-c1:checked) {
  --cut: clamp(1rem, 3vw, 4rem);
}

.dgs-01:has(#dgs-01-c3:checked) {
  --cut: clamp(2.5rem, 9vw, 11rem);
}

.dgs-01:has(#dgs-01-flip:checked) .dgs-01__cut {
  clip-path: polygon(0 0, 100% var(--cut), 100% 100%, 0 100%);
}

.dgs-01:has(#dgs-01-invert:checked) {
  --paper: #16150f;
  --paper2: #1e1c15;
  --ink: #f4f1ea;
  --muted: #a19d92;
  --line: #33302a;
  --band: #f4f1ea;
  --band-ink: #16150f;
  --band-muted: #5d5a51;
  --accent: #ff7a52;
}

.dgs-01:has(#dgs-01-invert:checked) .dgs-01__code {
  background: rgba(0,0,0,.08);
}

@media (prefers-color-scheme: dark) {
  .dgs-01:not(:has(#dgs-01-invert:checked)) {
    --paper: #16150f;
    --paper2: #1e1c15;
    --ink: #f4f1ea;
    --muted: #a19d92;
    --line: #33302a;
    --band: #f4f1ea;
    --band-ink: #16150f;
    --band-muted: #5d5a51;
    --accent: #ff7a52;
  }

  .dgs-01:not(:has(#dgs-01-invert:checked)) .dgs-01__code {
    background: rgba(0,0,0,.08);
  }
}

@media (prefers-reduced-motion: reduce) {
  .dgs-01 * {
    transition: none !important;
    animation: none !important;
  }
}

@media (forced-colors: active) {
  .dgs-01__cut {
    forced-color-adjust: none;
    background: Canvas;
    color: CanvasText;
    border-block-start: 1px solid CanvasText;
  }

  .dgs-01__ctl,
    .dgs-01__ctl label {
    border-color: CanvasText;
  }

  .dgs-01__sr:checked + label {
    background: Highlight;
    color: HighlightText;
  }
}
/* Standard top-right theme toggle — pure CSS (checkbox + :has()), so demos
   that ship no script stay tagged Pure CSS. Placed on the root rather than
   inside a demo's own control panel so every demo exposes it in one place. */

.dgs-01__sronly,
.dgs-01__srtext {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.dgs-01__theme {
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

.dgs-01__theme:hover {
  translate: 0 -1px;
}

.dgs-01__sronly:focus-visible + .dgs-01__theme {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}

.dgs-01__i {
  inline-size: 1.15rem;
  block-size: 1.15rem;
}

.dgs-01__i--sun {
  display: none;
}

.dgs-01:has(#dgs-01-dark:checked) .dgs-01__i--moon {
  display: none;
}

.dgs-01:has(#dgs-01-dark:checked) .dgs-01__i--sun {
  display: block;
}

.dgs-01:has(#dgs-01-dark:checked) {
  --paper: #16150f;
  --paper2: #1e1c15;
  --ink: #f4f1ea;
  --muted: #a19d92;
  --line: #33302a;
  --band: #f4f1ea;
  --band-ink: #16150f;
  --band-muted: #5d5a51;
}

@media (prefers-reduced-motion: reduce) {
  .dgs-01__theme {
    transition: none;
  }
}

@media (forced-colors: active) {
  .dgs-01__theme {
    border-color: CanvasText;
  }
}
```
