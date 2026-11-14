---
source: "codefronts"
url: "https://codefronts.com/layouts/css-dashboard-layouts/modular-masonry-grid-dashboard/"
title: "Modular Masonry Grid Dashboard"
section: "layouts"
category: "css-dashboard-layouts"
category_name: "CSS Dashboard Layouts"
description: "Eight numbered widgets, two packing engines, one toggle — the fairest fight in CSS."
has_js: "false"
---

Here's a working CSS Dashboard Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Modular Masonry Grid Dashboard
Source: https://codefronts.com/layouts/css-dashboard-layouts/modular-masonry-grid-dashboard/

Eight numbered widgets, two packing engines, one toggle — the fairest fight in CSS. Engine A (multi-column) gives true Pinterest masonry but pours DOWN each column: watch the numbers read 1-4-6 vertically. Engine B (grid + dense flow) keeps left-to-right reading order and backfills holes, but quantizes heights to a row rhythm. The numbers ON the cards make each tradeoff visible in two seconds — the comparison every masonry article hand-waves, made interactive.
## HTML
```html
<section class="cdl-15" aria-label="Masonry packing comparison demo">
  <div class="cdl-15__stage">
    <header class="cdl-15__head">
      <h2>Widget board</h2>
      <div class="cdl-15__seg" role="group" aria-label="Packing engine">
        <label><input type="radio" name="cdl15" id="cdl15-cols" checked><span>A · columns</span></label>
        <label><input type="radio" name="cdl15" id="cdl15-grid"><span>B · grid dense</span></label>
      </div>
      <p class="cdl-15__note"><span class="cdl-15__note--a">reading order flows <b>down</b> each column</span><span class="cdl-15__note--b">reading order stays <b>left → right</b>, holes backfilled</span></p>
    </header>
    <div class="cdl-15__board">
      <article class="cdl-15__card" style="--rows:6"><b class="cdl-15__n">1</b><h3>Sales pulse</h3><p class="cdl-15__big">$12,940</p><p class="cdl-15__txt">Today · ▲ 7% vs Friday</p></article>
      <article class="cdl-15__card" style="--rows:8"><b class="cdl-15__n">2</b><h3>Traffic</h3><div class="cdl-15__bars" aria-hidden="true"><i style="--h:40%"></i><i style="--h:62%"></i><i style="--h:50%"></i><i style="--h:78%"></i><i style="--h:66%"></i><i style="--h:92%"></i></div><p class="cdl-15__txt">Organic up 12% after the changelog post hit the front page.</p></article>
      <article class="cdl-15__card" style="--rows:6"><b class="cdl-15__n">3</b><h3>Note to self</h3><p class="cdl-15__txt">Ship the pricing experiment behind a flag Tuesday. Watch AOV, not conversion, for the first 48h.</p></article>
      <article class="cdl-15__card" style="--rows:5"><b class="cdl-15__n">4</b><h3>NPS</h3><p class="cdl-15__big">+61</p></article>
      <article class="cdl-15__card" style="--rows:7"><b class="cdl-15__n">5</b><h3>On-call</h3><p class="cdl-15__txt">Rotation: Priya → Sam → Jo.</p><p class="cdl-15__txt">Quiet week — 2 pages, both auto-resolved. Postmortem for #221 due Thu.</p></article>
      <article class="cdl-15__card" style="--rows:5"><b class="cdl-15__n">6</b><h3>Signups</h3><p class="cdl-15__big">312<small>/wk</small></p></article>
      <article class="cdl-15__card" style="--rows:6"><b class="cdl-15__n">7</b><h3>Churn watch</h3><p class="cdl-15__txt">3 accounts idle 21+ days. Playbook emails queued for Monday 09:00.</p></article>
      <article class="cdl-15__card" style="--rows:6"><b class="cdl-15__n">8</b><h3>Build</h3><p class="cdl-15__big cdl-15__ok">passing</p><p class="cdl-15__txt">main · 4m ago</p></article>
    </div>
  </div>
</section>
```
## CSS
```css
.cdl-15,
.cdl-15 *,
.cdl-15 *::before,
.cdl-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cdl-15 {
  background: var(--bg);
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  --bg: oklch(0.975 0.006 55);
  --panel: oklch(1 0 0);
  --edge: oklch(0.9 0.015 55);
  --ink: oklch(0.27 0.02 45);
  --mut: oklch(0.54 0.03 45);
  --acc: oklch(0.62 0.15 45);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
}

.cdl-15__stage {
  width: 100%;
  height: 100vh;
  border: 1px solid var(--edge);
  background: linear-gradient(175deg,var(--bg),oklch(0.958 0.01 55));
  padding: 18px;
}

.cdl-15__head {
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
  margin-bottom: 16px;
}

.cdl-15__head h2 {
  font-size: 16px;
  letter-spacing: -.01em;
  margin-right: auto;
}

.cdl-15__seg {
  display: flex;
  gap: 4px;
  background: var(--panel);
  border: 1px solid var(--edge);
  border-radius: 11px;
  padding: 3px;
}

.cdl-15__seg label {
  position: relative;
  cursor: pointer;
}

.cdl-15__seg input {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.cdl-15__seg span {
  display: block;
  font-size: 12px;
  font-weight: 700;
  color: var(--mut);
  padding: 7px 13px;
  border-radius: 8px;
  transition: background .15s,color .15s;
}

.cdl-15__seg label:hover span {
  color: var(--ink);
}

.cdl-15__seg label:has(:checked) span {
  background: var(--acc);
  color: oklch(1 0 0);
}

.cdl-15__seg label:has(:focus-visible) span {
  outline: 2px solid var(--acc);
  outline-offset: 2px;
}

.cdl-15__note {
  flex-basis: 100%;
  font-size: 12px;
  color: var(--mut);
}

.cdl-15__note b {
  color: var(--acc);
}

.cdl-15__note--a,
.cdl-15__note--b {
  display: none;
}

.cdl-15:has(#cdl15-cols:checked) .cdl-15__note--a {
  display: inline;
}

.cdl-15:has(#cdl15-grid:checked) .cdl-15__note--b {
  display: inline;
}

.cdl-15:has(#cdl15-cols:checked) .cdl-15__board {
  columns: 3 240px;
  column-gap: 14px;
}

.cdl-15:has(#cdl15-cols:checked) .cdl-15__card {
  break-inside: avoid;
  margin-bottom: 14px;
}

.cdl-15:has(#cdl15-grid:checked) .cdl-15__board {
  display: grid;
  gap: 14px;
  grid-template-columns: repeat(auto-fill,minmax(min(240px,100%),1fr));
  grid-auto-rows: 8px;
  grid-auto-flow: dense;
}

.cdl-15:has(#cdl15-grid:checked) .cdl-15__card {
  grid-row: span var(--rows);
}

.cdl-15__card {
  position: relative;
  background: var(--panel);
  border: 1px solid var(--edge);
  border-radius: 14px;
  padding: 15px 16px;
  display: flex;
  flex-direction: column;
  gap: 7px;
  overflow: hidden;
  transition: border-color .2s,box-shadow .2s;
}

.cdl-15__card:hover {
  border-color: color-mix(in oklch,var(--acc) 50%,var(--edge));
  box-shadow: 0 10px 24px -18px oklch(0.4 0.08 45/.6);
}

.cdl-15__n {
  position: absolute;
  top: 10px;
  right: 12px;
  width: 22px;
  height: 22px;
  display: grid;
  place-items: center;
  font-size: 11px;
  font-weight: 800;
  color: var(--acc);
  background: color-mix(in oklch,var(--acc) 12%,white);
  border-radius: 7px;
}

.cdl-15__card h3 {
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--mut);
}

.cdl-15__big {
  font-size: 24px;
  font-weight: 700;
  letter-spacing: -.01em;
  font-variant-numeric: tabular-nums;
}

.cdl-15__big small {
  font-size: 13px;
  color: var(--mut);
  font-weight: 600;
}

.cdl-15__ok {
  color: oklch(0.55 0.14 155);
}

.cdl-15__txt {
  font-size: 12.5px;
  line-height: 1.5;
  color: var(--mut);
}

.cdl-15__bars {
  display: flex;
  align-items: flex-end;
  gap: 6px;
  height: 56px;
}

.cdl-15__bars i {
  flex: 1;
  height: var(--h);
  border-radius: 3px 3px 0 0;
  background: linear-gradient(to top,color-mix(in oklch,var(--acc) 30%,transparent),var(--acc));
}

@media (prefers-reduced-motion: reduce) {
  .cdl-15 * {
    transition: none !important;
  }
}
```
