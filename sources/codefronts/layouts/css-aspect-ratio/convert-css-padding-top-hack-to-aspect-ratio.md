---
source: "codefronts"
url: "https://codefronts.com/layouts/css-aspect-ratio/convert-css-padding-top-hack-to-aspect-ratio/"
title: "Convert CSS Padding Top Hack to Aspect Ratio"
section: "layouts"
category: "css-aspect-ratio"
category_name: "CSS Aspect Ratio Demos"
description: "The migration sheet for retiring 2015's cleverest hack: side-by-side live boxes prove padding-top: 56.25% and aspect-ratio: 16/9 produce identical geometry,…"
has_js: "false"
---

Here's a working CSS Aspect Ratio Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Convert CSS Padding Top Hack to Aspect Ratio
Source: https://codefronts.com/layouts/css-aspect-ratio/convert-css-padding-top-hack-to-aspect-ratio/

The migration sheet for retiring 2015's cleverest hack: side-by-side live boxes prove padding-top: 56.25% and aspect-ratio: 16/9 produce identical geometry, a diff shows exactly which lines you delete (the wrapper's positioning, the child's absolute inset — all of it), and a ratio picker re-derives both implementations plus the conversion table in real time. Includes the formula the hack was built on — percentage padding resolves against WIDTH — so you can convert any legacy percentage you meet in the wild, then never write one again.
## HTML
```html
<section class="car-15" aria-label="Padding hack to aspect ratio migration demo">
  <div class="car-15__stage" id="car15-top">
    <header class="car-15__head">
      <div>
        <p class="car-15__kicker">Refactor sheet · est. 5 minutes per component</p>
        <h1>Retire the padding-top hack</h1>
        <p class="car-15__lede">Both boxes below are live. One is 2015's wrapper ritual, one is a single 2026 declaration — pick a ratio and confirm they never disagree.</p>
      </div>
      <fieldset class="car-15__picker">
        <legend>Target ratio</legend>
        <label><input type="radio" name="car15-r" id="car15-r169" checked><span>16:9</span></label>
        <label><input type="radio" name="car15-r" id="car15-r43"><span>4:3</span></label>
        <label><input type="radio" name="car15-r" id="car15-r11"><span>1:1</span></label>
        <label><input type="radio" name="car15-r" id="car15-r219"><span>21:9</span></label>
      </fieldset>
    </header>
    <main class="car-15__panels">
      <article class="car-15__panel">
        <header class="car-15__phead car-15__phead--del"><b>BEFORE</b><span>the hack — 6 declarations, 2 elements</span></header>
        <pre class="car-15__code"><code><del>.embed{ position:relative;</del>
<del>  height:0;</del>
<del>  padding-top:<b class="car-15__padval"></b>; }</del>
<del>.embed &gt; *{ position:absolute;</del>
<del>  inset:0; width:100%;</del>
<del>  height:100%; }</del></code></pre>
        <div class="car-15__livewrap"><div class="car-15__live car-15__live--legacy"><div><b class="car-15__rationame"></b><span>padding-top: <i class="car-15__padval"></i> of width</span></div></div></div>
      </article>
      <article class="car-15__panel">
        <header class="car-15__phead car-15__phead--ins"><b>AFTER</b><span>the property — 1 declaration, 1 element</span></header>
        <pre class="car-15__code"><code><ins>.embed{ aspect-ratio:<b class="car-15__ratioval"></b>; }</ins>

<em>/* + content may flow inside it,
   + can derive width from height,
   + obeys min/max guardrails */</em></code></pre>
        <div class="car-15__livewrap"><div class="car-15__live car-15__live--modern"><div><b class="car-15__rationame"></b><span>aspect-ratio: <i class="car-15__ratioval"></i></span></div></div></div>
      </article>
      <aside class="car-15__aside">
        <h2>Conversion table</h2>
        <table>
          <thead><tr><th scope="col">Legacy padding</th><th scope="col">aspect-ratio</th><th scope="col">Used for</th></tr></thead>
          <tbody>
            <tr class="car-15__row--169"><td>56.25%</td><td>16 / 9</td><td>video, embeds</td></tr>
            <tr class="car-15__row--43"><td>75%</td><td>4 / 3</td><td>cards, photos</td></tr>
            <tr class="car-15__row--11"><td>100%</td><td>1 / 1</td><td>squares, avatars</td></tr>
            <tr class="car-15__row--219"><td>42.86%</td><td>21 / 9</td><td>cinematic heroes</td></tr>
            <tr><td>177.78%</td><td>9 / 16</td><td>stories, portrait</td></tr>
          </tbody>
        </table>
        <p class="car-15__formula"><b>The formula</b>padding-% = height ÷ width × 100 — vertical padding percentages resolve against <em>width</em>; that quirk was the entire hack. The property reads the other way up: width / height.</p>
        <ol class="car-15__steps">
          <li>Grep for <code>padding-top:</code> / <code>padding-bottom:</code> with % near embed wrappers.</li>
          <li>Divide back to a ratio (56.25 → 16/9). Mind the flip.</li>
          <li>Delete: <code>height:0</code>, the padding line, the child's <code>position:absolute; inset:0</code>.</li>
          <li>Keep <code>width/height:100%</code> on iframe/video children. Ship.</li>
        </ol>
      </aside>
    </main>
    <footer class="car-15__foot">The percentage was a compiled artifact; the ratio is source code. A demo from the CodeFronts aspect-ratio collection.</footer>
  </div>
</section>
```
## CSS
```css
.car-15,
.car-15 *,
.car-15 *::before,
.car-15 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-15 {
  --bg: oklch(0.97 0.005 100);
  --ink: oklch(0.25 0.02 90);
  --mut: oklch(0.5 0.02 90);
  --line: oklch(0.88 0.012 100);
  --del: oklch(0.58 0.19 25);
  --ins: oklch(0.55 0.15 150);
  --acc: oklch(0.55 0.14 250);
  --pad: 56.25%;
  --ratio: 16/9;
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.car-15:has(#car15-r43:checked) {
  --pad: 75%;
  --ratio: 4/3;
}

.car-15:has(#car15-r11:checked) {
  --pad: 100%;
  --ratio: 1/1;
}

.car-15:has(#car15-r219:checked) {
  --pad: 42.86%;
  --ratio: 21/9;
}

.car-15__stage {
  width: 100%;
  container: car15/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  background: var(--bg);
}

.car-15__head {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: 20px;
  flex-wrap: wrap;
  padding: clamp(22px,4cqi,44px) clamp(16px,4cqi,44px) 18px;
}

.car-15__kicker {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--acc);
}

.car-15__head h1 {
  font-size: clamp(24px,4cqi,40px);
  letter-spacing: -.025em;
  font-weight: 800;
  margin-top: 8px;
}

.car-15__lede {
  margin-top: 10px;
  font-size: 14px;
  line-height: 1.6;
  color: var(--mut);
  max-width: 56ch;
}

.car-15__picker {
  border: 1px solid var(--line);
  border-radius: 14px;
  padding: 12px 14px 14px;
  background: oklch(1 0 0);
}

.car-15__picker legend {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--mut);
  padding: 0 4px;
}

.car-15__picker label {
  display: inline-grid;
  margin-right: 6px;
  cursor: pointer;
}

.car-15__picker input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.car-15__picker span {
  display: grid;
  place-items: center;
  min-width: 56px;
  min-height: 44px;
  border-radius: 10px;
  border: 1.5px solid var(--line);
  font-family: ui-monospace,Menlo,monospace;
  font-size: 13px;
  font-weight: 700;
  transition: border-color .2s,background .2s,color .2s;
}

.car-15__picker input:checked + span {
  border-color: var(--ink);
  background: var(--ink);
  color: var(--bg);
}

.car-15__picker input:focus-visible + span {
  outline: 3px solid var(--acc);
  outline-offset: 2px;
}

.car-15__picker span:hover {
  border-color: var(--acc);
}

.car-15__panels {
  display: grid;
  grid-template-columns: minmax(0,1fr) minmax(0,1fr) minmax(280px,340px);
  gap: clamp(14px,2.5cqi,24px);
  align-items: start;
  padding: 0 clamp(16px,4cqi,44px) 8px;
}

.car-15__panel {
  border: 1px solid var(--line);
  border-radius: 16px;
  background: oklch(1 0 0);
  overflow: hidden;
}

.car-15__phead {
  display: flex;
  align-items: baseline;
  gap: 10px;
  padding: 12px 16px;
  border-bottom: 1px solid var(--line);
}

.car-15__phead b {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: .14em;
  padding: 4px 9px;
  border-radius: 7px;
}

.car-15__phead--del b {
  background: color-mix(in oklch,var(--del) 14%,white);
  color: var(--del);
}

.car-15__phead--ins b {
  background: color-mix(in oklch,var(--ins) 14%,white);
  color: var(--ins);
}

.car-15__phead span {
  font-size: 11.5px;
  color: var(--mut);
}

.car-15__code {
  padding: 14px 16px;
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: 12px;
  line-height: 1.75;
  overflow-x: auto;
  background: oklch(0.985 0.004 100);
}

.car-15__code del {
  display: block;
  text-decoration: none;
  background: color-mix(in oklch,var(--del) 9%,transparent);
  color: color-mix(in oklch,var(--del) 70%,var(--ink));
  border-left: 3px solid var(--del);
  padding-left: 9px;
  margin-left: -9px;
}

.car-15__code ins {
  display: block;
  text-decoration: none;
  background: color-mix(in oklch,var(--ins) 11%,transparent);
  color: color-mix(in oklch,var(--ins) 60%,var(--ink));
  border-left: 3px solid var(--ins);
  padding-left: 9px;
  margin-left: -9px;
  font-weight: 700;
}

.car-15__code em {
  display: block;
  font-style: normal;
  color: var(--mut);
  margin-top: 2px;
}

.car-15__code b {
  font-weight: 800;
}

.car-15__livewrap {
  padding: 4px 16px 16px;
}

.car-15__live {
  border-radius: 12px;
  overflow: hidden;
}

.car-15__live--legacy {
  position: relative;
  height: 0;
  padding-top: var(--pad);
  background: linear-gradient(140deg,oklch(0.62 0.13 25/.85),oklch(0.45 0.11 25/.9));
}

.car-15__live--legacy > div {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.car-15__live--modern {
  aspect-ratio: var(--ratio);
  background: linear-gradient(140deg,oklch(0.6 0.12 150/.85),oklch(0.4 0.1 165/.9));
}

.car-15__live > div {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
  color: oklch(0.99 0 0);
  height: 100%;
}

.car-15__live b {
  font-size: clamp(20px,3cqi,30px);
  font-weight: 800;
  letter-spacing: -.02em;
}

.car-15__live span {
  font-size: clamp(10px,1.6cqi,12px);
  opacity: .9;
}

.car-15__live i {
  font-style: normal;
  font-family: ui-monospace,Menlo,monospace;
  font-weight: 700;
}

.car-15__rationame::after {
  content: "16:9";
}

.car-15:has(#car15-r43:checked) .car-15__rationame::after {
  content: "4:3";
}

.car-15:has(#car15-r11:checked) .car-15__rationame::after {
  content: "1:1";
}

.car-15:has(#car15-r219:checked) .car-15__rationame::after {
  content: "21:9";
}

.car-15__padval::after {
  content: "56.25%";
}

.car-15:has(#car15-r43:checked) .car-15__padval::after {
  content: "75%";
}

.car-15:has(#car15-r11:checked) .car-15__padval::after {
  content: "100%";
}

.car-15:has(#car15-r219:checked) .car-15__padval::after {
  content: "42.86%";
}

.car-15__ratioval::after {
  content: "16 / 9";
}

.car-15:has(#car15-r43:checked) .car-15__ratioval::after {
  content: "4 / 3";
}

.car-15:has(#car15-r11:checked) .car-15__ratioval::after {
  content: "1 / 1";
}

.car-15:has(#car15-r219:checked) .car-15__ratioval::after {
  content: "21 / 9";
}

.car-15__aside {
  border: 1px solid var(--line);
  border-radius: 16px;
  background: oklch(1 0 0);
  padding: 16px;
}

.car-15__aside h2 {
  font-size: 12px;
  font-weight: 800;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--mut);
}

.car-15__aside table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
  font-size: 12.5px;
}

.car-15__aside th {
  text-align: left;
  font-size: 10px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--mut);
  padding: 6px 8px;
  border-bottom: 1.5px solid var(--line);
}

.car-15__aside td {
  padding: 8px;
  border-bottom: 1px solid var(--line);
  font-family: ui-monospace,Menlo,monospace;
  font-size: 12px;
}

.car-15__aside td:last-child {
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--mut);
}

.car-15:has(#car15-r169:checked) .car-15__row--169,
.car-15:has(#car15-r43:checked) .car-15__row--43,
.car-15:has(#car15-r11:checked) .car-15__row--11,
.car-15:has(#car15-r219:checked) .car-15__row--219 {
  background: color-mix(in oklch,var(--acc) 10%,transparent);
}

.car-15__formula {
  margin-top: 14px;
  font-size: 12px;
  line-height: 1.6;
  color: var(--mut);
  border-left: 3px solid var(--acc);
  padding-left: 11px;
}

.car-15__formula b {
  display: block;
  font-size: 10.5px;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--acc);
  margin-bottom: 3px;
}

.car-15__steps {
  margin: 14px 0 2px 18px;
  font-size: 12.5px;
  line-height: 1.6;
  color: var(--mut);
  display: flex;
  flex-direction: column;
  gap: 7px;
}

.car-15__steps code {
  font-family: ui-monospace,Menlo,monospace;
  font-size: .92em;
  background: oklch(0.93 0.01 100);
  padding: 1px 5px;
  border-radius: 4px;
  color: var(--ink);
}

.car-15__foot {
  padding: 16px clamp(16px,4cqi,44px) 30px;
  font-size: 12.5px;
  color: var(--mut);
  border-top: 1px solid var(--line);
  margin-top: 14px;
}

@container car15 (width < 960px) {
  .car-15__panels {
    grid-template-columns: 1fr 1fr;
  }

  .car-15__aside {
    grid-column: 1/-1;
  }
}

@container car15 (width < 640px) {
  .car-15__panels {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .car-15 * {
    transition-duration: .01ms !important;
  }
}
```
