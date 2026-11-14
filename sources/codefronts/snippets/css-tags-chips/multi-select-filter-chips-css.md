---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tags-chips/multi-select-filter-chips-css/"
title: "Multi-Select Filter Chips CSS"
section: "snippets"
category: "css-tags-chips"
category_name: "CSS Tags & Chips"
description: "Working multi-select filter chips — not a mockup."
has_js: "false"
---

Here's a working CSS Tags & Chip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Select Filter Chips CSS
Source: https://codefronts.com/snippets/css-tags-chips/multi-select-filter-chips-css/

Working multi-select filter chips — not a mockup. Each chip is a real <label> + hidden checkbox, the result tiles below genuinely filter through :has() with zero JavaScript, a CSS counter reports how many filters are on and how many results survived, and one <button type="reset"> clears everything because the stage is a <form>. A state strip underneath documents rest / selected / disabled so you can copy the exact chip anatomy, not just the idea.
## HTML
```html
<section class="ctc-01" aria-label="Multi-select filter chips demo">
  <form class="ctc-01__stage">
    <div class="ctc-01__wrap">
      <header class="ctc-01__head">
        <p class="ctc-01__kicker">Filter chips · pure CSS state</p>
        <h1>Check a chip. The grid obeys.</h1>
      </header>
      <fieldset class="ctc-01__rail">
        <legend class="ctc-01__sr">Filter snippets by category</legend>
        <div class="ctc-01__chips">
          <label class="ctc-01__chip"><input class="ctc-01__sr" type="checkbox" id="ctc01-ui"><span>UI kits</span></label>
          <label class="ctc-01__chip"><input class="ctc-01__sr" type="checkbox" id="ctc01-anim"><span>Animation</span></label>
          <label class="ctc-01__chip"><input class="ctc-01__sr" type="checkbox" id="ctc01-form"><span>Forms</span></label>
          <label class="ctc-01__chip"><input class="ctc-01__sr" type="checkbox" id="ctc01-nav"><span>Navigation</span></label>
          <label class="ctc-01__chip"><input class="ctc-01__sr" type="checkbox" id="ctc01-fx"><span>Effects</span></label>
        </div>
        <span class="ctc-01__active" aria-hidden="true"></span>
        <button class="ctc-01__clear" type="reset">Clear all</button>
      </fieldset>
      <div class="ctc-01__grid">
        <article data-cat="ui" style="--h:255"><i></i><div><h3>Pricing cards</h3><p>UI kits</p></div><b>1.2k</b></article>
        <article data-cat="anim" style="--h:150"><i></i><div><h3>Spring easing</h3><p>Animation</p></div><b>860</b></article>
        <article data-cat="form" style="--h:40"><i></i><div><h3>Tag input</h3><p>Forms</p></div><b>2.4k</b></article>
        <article data-cat="ui" style="--h:255"><i></i><div><h3>Data tables</h3><p>UI kits</p></div><b>640</b></article>
        <article data-cat="nav" style="--h:320"><i></i><div><h3>Mega menu</h3><p>Navigation</p></div><b>1.9k</b></article>
        <article data-cat="fx" style="--h:200"><i></i><div><h3>Aurora borders</h3><p>Effects</p></div><b>3.1k</b></article>
        <article data-cat="form" style="--h:40"><i></i><div><h3>Range slider</h3><p>Forms</p></div><b>720</b></article>
        <article data-cat="anim" style="--h:150"><i></i><div><h3>View timelines</h3><p>Animation</p></div><b>540</b></article>
        <article data-cat="nav" style="--h:320"><i></i><div><h3>Breadcrumbs</h3><p>Navigation</p></div><b>410</b></article>
        <article data-cat="fx" style="--h:200"><i></i><div><h3>Liquid fill</h3><p>Effects</p></div><b>980</b></article>
      </div>
      <p class="ctc-01__result"><output aria-hidden="true"></output> of 10 results — chips are native checkboxes, filtering is <code>:has()</code>, “Clear all” is <code>type="reset"</code>. No JavaScript anywhere.</p>
      <footer class="ctc-01__spec" aria-label="Chip states">
        <span class="ctc-01__speclab">States</span>
        <span class="ctc-01__chip" aria-hidden="true"><span>Rest</span></span>
        <span class="ctc-01__chip" data-demo-checked aria-hidden="true"><span>Selected</span></span>
        <label class="ctc-01__chip"><input class="ctc-01__sr" type="checkbox" disabled><span>Disabled</span></label>
        <span class="ctc-01__spechint">Hover lifts · <kbd>Tab</kbd> + <kbd>Space</kbd> toggles with a visible ring</span>
      </footer>
    </div>
  </form>
</section>
```
## CSS
```css
.ctc-01,
.ctc-01 *,
.ctc-01 *::before,
.ctc-01 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.ctc-01 {
  --bg: oklch(0.975 0.005 85);
  --ink: oklch(0.23 0.02 60);
  --mut: oklch(0.5 0.02 60);
  --line: oklch(0.88 0.014 75);
  --acc: oklch(0.55 0.16 45);
  --card: oklch(0.998 0.002 85);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
}

.ctc-01__stage {
  width: 100%;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: grid;
  place-items: center;
  background: radial-gradient(80cqi 55cqi at 50% -12%,color-mix(in oklch,var(--acc) 10%,transparent),transparent 70%),var(--bg);
  container: ctc01/inline-size;
  border: 0;
}

.ctc-01__wrap {
  width: min(860px,100%);
  padding: clamp(20px,4cqi,44px);
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.ctc-01__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

.ctc-01__kicker {
  font-size: 11.5px;
  font-weight: 800;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
}

.ctc-01__head h1 {
  font-size: clamp(24px,3.6cqi,38px);
  font-weight: 800;
  letter-spacing: -.03em;
  margin-top: 6px;
}

.ctc-01__rail {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 9px;
  border: 0;
}

.ctc-01__chips {
  display: flex;
  flex-wrap: wrap;
  gap: 9px;
  counter-reset: ctc01sel;
}

.ctc-01__chip {
  position: relative;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  min-height: 44px;
  padding: 0 19px;
  border-radius: 99px;
  border: 1.5px solid var(--line);
  background: var(--card);
  font-size: 14px;
  font-weight: 650;
  color: var(--mut);
  cursor: pointer;
  user-select: none;
  transition: border-color .2s,background .25s,color .2s,translate .2s,box-shadow .2s;
}

.ctc-01__chip::before {
  content: "";
  width: 0;
  height: 8px;
  border-left: 2.5px solid currentColor;
  border-bottom: 2.5px solid currentColor;
  rotate: -45deg;
  translate: 0 -2px;
  scale: 0;
  opacity: 0;
  transition: scale .3s cubic-bezier(.34,1.56,.64,1),opacity .2s,width .25s cubic-bezier(.34,1.56,.64,1);
}

.ctc-01__chip:hover {
  border-color: color-mix(in oklch,var(--acc) 45%,var(--line));
  color: var(--ink);
  translate: 0 -1px;
  box-shadow: 0 6px 14px -8px oklch(0.23 0.02 60/.4);
}

.ctc-01__chip:has(:focus-visible) {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ctc-01__chip:has(:checked),
.ctc-01__chip[data-demo-checked] {
  background: var(--ink);
  border-color: var(--ink);
  color: oklch(0.97 0.005 85);
  box-shadow: 0 8px 18px -8px oklch(0.23 0.02 60/.5);
}

.ctc-01__chip:has(:checked)::before,
.ctc-01__chip[data-demo-checked]::before {
  width: 13px;
  scale: 1;
  opacity: 1;
}

.ctc-01__chips .ctc-01__chip:has(:checked) {
  counter-increment: ctc01sel;
}

.ctc-01__chip:has(:disabled) {
  opacity: .45;
  cursor: not-allowed;
  border-style: dashed;
}

.ctc-01__chip:has(:disabled):hover {
  translate: none;
  box-shadow: none;
  color: var(--mut);
  border-color: var(--line);
}

.ctc-01__active {
  display: none;
  align-items: center;
  min-height: 30px;
  padding: 0 12px;
  border-radius: 99px;
  background: color-mix(in oklch,var(--acc) 14%,transparent);
  color: var(--acc);
  font-size: 12.5px;
  font-weight: 800;
  font-variant-numeric: tabular-nums;
}

.ctc-01__active::after {
  content: counter(ctc01sel) " on";
}

.ctc-01__rail:has(input:checked) .ctc-01__active {
  display: inline-flex;
}

.ctc-01__clear {
  margin-left: auto;
  min-height: 44px;
  padding: 0 14px;
  border: 0;
  border-radius: 10px;
  background: none;
  font: inherit;
  font-size: 13px;
  font-weight: 700;
  color: var(--mut);
  cursor: pointer;
  text-decoration: underline 1.5px color-mix(in oklch,var(--mut) 40%,transparent);
  text-underline-offset: 3px;
  transition: color .2s;
}

.ctc-01__clear:hover,
.ctc-01__clear:focus-visible {
  color: var(--acc);
}

.ctc-01__clear:focus-visible {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.ctc-01__grid {
  display: grid;
  grid-template-columns: repeat(auto-fill,minmax(min(235px,100%),1fr));
  gap: 10px;
  counter-reset: ctc01vis;
}

.ctc-01__grid article {
  display: grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: 12px;
  counter-increment: ctc01vis;
  padding: 12px 14px;
  border-radius: 14px;
  border: 1px solid var(--line);
  background: var(--card);
  transition: translate .2s,box-shadow .2s;
}

.ctc-01__grid article:hover {
  translate: 0 -2px;
  box-shadow: 0 12px 22px -14px oklch(0.23 0.02 60/.4);
}

.ctc-01__grid i {
  width: 34px;
  height: 34px;
  border-radius: 10px;
  background: linear-gradient(140deg,oklch(0.85 0.07 var(--h)),oklch(0.62 0.13 calc(var(--h) + 40)));
}

.ctc-01__grid h3 {
  font-size: 13.5px;
  font-weight: 750;
  letter-spacing: -.01em;
}

.ctc-01__grid p {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .07em;
  text-transform: uppercase;
  color: oklch(0.62 0.11 var(--h));
  margin-top: 2px;
}

.ctc-01__grid b {
  font-size: 11.5px;
  font-weight: 700;
  color: var(--mut);
  font-variant-numeric: tabular-nums;
  background: oklch(0.94 0.008 80);
  padding: 4px 8px;
  border-radius: 99px;
}

.ctc-01__stage:has(.ctc-01__chips input:checked) .ctc-01__grid article {
  display: none;
}

.ctc-01__stage:has(#ctc01-ui:checked) article[data-cat="ui"] {
  display: grid;
}

.ctc-01__stage:has(#ctc01-anim:checked) article[data-cat="anim"] {
  display: grid;
}

.ctc-01__stage:has(#ctc01-form:checked) article[data-cat="form"] {
  display: grid;
}

.ctc-01__stage:has(#ctc01-nav:checked) article[data-cat="nav"] {
  display: grid;
}

.ctc-01__stage:has(#ctc01-fx:checked) article[data-cat="fx"] {
  display: grid;
}

.ctc-01__result {
  font-size: 13px;
  color: var(--mut);
}

.ctc-01__result output {
  font-weight: 800;
  color: var(--ink);
}

.ctc-01__result output::after {
  content: counter(ctc01vis);
}

.ctc-01__result code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .9em;
  background: oklch(0.92 0.01 75);
  padding: 1px 6px;
  border-radius: 5px;
}

.ctc-01__spec {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 9px;
  padding-top: 16px;
  border-top: 1px dashed var(--line);
}

.ctc-01__speclab {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--mut);
  margin-right: 4px;
}

.ctc-01__spechint {
  font-size: 12px;
  color: var(--mut);
  margin-left: auto;
}

.ctc-01__spechint kbd {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .85em;
  font-weight: 700;
  background: oklch(0.93 0.01 80);
  border: 1px solid var(--line);
  border-bottom-width: 2px;
  border-radius: 5px;
  padding: 1px 5px;
}

@container ctc01 (width < 620px) {
  .ctc-01__clear {
    margin-left: 0;
  }

  .ctc-01__spechint {
    margin-left: 0;
    width: 100%;
  }
}

@media (prefers-reduced-motion: reduce) {
  .ctc-01 * {
    transition-duration: .01ms !important;
  }
}
```
