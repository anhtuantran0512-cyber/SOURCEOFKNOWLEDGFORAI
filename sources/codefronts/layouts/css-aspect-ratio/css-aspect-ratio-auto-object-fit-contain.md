---
source: "codefronts"
url: "https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-auto-object-fit-contain/"
title: "CSS Aspect Ratio Auto Object Fit Contain"
section: "layouts"
category: "css-aspect-ratio"
category_name: "CSS Aspect Ratio Demos"
description: "The logo wall: eight brand marks with wildly different intrinsic shapes — 800×120 wordmarks, 320×320 badges, 240×420 crests — normalized into identical 3:2…"
has_js: "false"
---

Here's a working CSS Aspect Ratio Demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: CSS Aspect Ratio Auto Object Fit Contain
Source: https://codefronts.com/layouts/css-aspect-ratio/css-aspect-ratio-auto-object-fit-contain/

The logo wall: eight brand marks with wildly different intrinsic shapes — 800×120 wordmarks, 320×320 badges, 240×420 crests — normalized into identical 3:2 cells. The cell imposes the ratio; object-fit: contain letterboxes each mark, undistorted, at its largest fitting size; and the images themselves keep aspect-ratio: auto (their intrinsic truth) — which is precisely what contain preserves. A cover/fill/contain switch is built in so you can watch the wrong object-fit ruin a logo in real time.
## HTML
```html
<section class="car-14" aria-label="Logo cloud object-fit contain demo">
  <div class="car-14__stage" id="car14-top">
    <header class="car-14__head">
      <p class="car-14__kicker">Northwind · Trust wall</p>
      <h1>Eight logo shapes. One visual size.</h1>
      <p class="car-14__lede">Each cell is <code>aspect-ratio:3/2</code>; each mark keeps its intrinsic shape (<code>aspect-ratio:auto</code>) and scales by <code>object-fit</code>. Flip the fit and watch what each policy does to the same eight files:</p>
      <fieldset class="car-14__switch">
        <legend class="car-14__sr">Object-fit mode</legend>
        <label><input type="radio" name="car14-fit" id="car14-contain" checked><span>contain — whole &amp; true</span></label>
        <label><input type="radio" name="car14-fit" id="car14-cover"><span>cover — crops the marks</span></label>
        <label><input type="radio" name="car14-fit" id="car14-fill"><span>fill — stretches (default!)</span></label>
      </fieldset>
    </header>
    <ul class="car-14__wall">
      <li class="car-14__cell"><img src="data:image/svg+xml;utf8,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20800%20120'%20width='800'%20height='120'%3E%3Ctext%20x='400'%20y='78'%20text-anchor='middle'%20font-family='Arial,sans-serif'%20font-size='84'%20font-weight='800'%20letter-spacing='16'%20fill='%23404a66'%3EMERIDIAN%3C/text%3E%3C/svg%3E" width="800" height="120" alt="Meridian logo, ultra-wide wordmark"><span>800 × 120</span></li>
      <li class="car-14__cell"><img src="data:image/svg+xml;utf8,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20320%20320'%20width='320'%20height='320'%3E%3Ccircle%20cx='160'%20cy='160'%20r='140'%20fill='none'%20stroke='%23404a66'%20stroke-width='22'/%3E%3Ctext%20x='160'%20y='196'%20text-anchor='middle'%20font-family='Arial,sans-serif'%20font-size='110'%20font-weight='800'%20fill='%23404a66'%3EO%3C/text%3E%3C/svg%3E" width="320" height="320" alt="Orbital logo, square badge"><span>320 × 320</span></li>
      <li class="car-14__cell"><img src="data:image/svg+xml;utf8,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20240%20420'%20width='240'%20height='420'%3E%3Cpath%20d='M120%2016%20224%2088v168l-104%20148L16%20256V88z'%20fill='none'%20stroke='%23404a66'%20stroke-width='18'/%3E%3Ctext%20x='120'%20y='240'%20text-anchor='middle'%20font-family='Arial,sans-serif'%20font-size='96'%20font-weight='800'%20fill='%23404a66'%3EA%3C/text%3E%3C/svg%3E" width="240" height="420" alt="Axis logo, tall crest"><span>240 × 420</span></li>
      <li class="car-14__cell"><img src="data:image/svg+xml;utf8,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20560%20140'%20width='560'%20height='140'%3E%3Ctext%20x='280'%20y='92'%20text-anchor='middle'%20font-family='Georgia,serif'%20font-size='86'%20font-style='italic'%20font-weight='700'%20fill='%23404a66'%3EJuniper%3C/text%3E%3C/svg%3E" width="560" height="140" alt="Juniper logo, serif wordmark"><span>560 × 140</span></li>
      <li class="car-14__cell"><img src="data:image/svg+xml;utf8,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20400%20200'%20width='400'%20height='200'%3E%3Crect%20x='14'%20y='14'%20width='172'%20height='172'%20rx='34'%20fill='%23404a66'/%3E%3Ctext%20x='100'%20y='128'%20text-anchor='middle'%20font-family='Arial,sans-serif'%20font-size='92'%20font-weight='800'%20fill='%23f2f4f8'%3EB%3C/text%3E%3Ctext%20x='300'%20y='128'%20text-anchor='middle'%20font-family='Arial,sans-serif'%20font-size='72'%20font-weight='800'%20fill='%23404a66'%3EBOLT%3C/text%3E%3C/svg%3E" width="400" height="200" alt="Bolt logo, icon plus wordmark"><span>400 × 200</span></li>
      <li class="car-14__cell"><img src="data:image/svg+xml;utf8,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20640%20160'%20width='640'%20height='160'%3E%3Ctext%20x='320'%20y='104'%20text-anchor='middle'%20font-family='Arial,sans-serif'%20font-size='72'%20font-weight='300'%20letter-spacing='30'%20fill='%23404a66'%3EFRAMEFIELD%3C/text%3E%3C/svg%3E" width="640" height="160" alt="Framefield logo, light-weight wordmark"><span>640 × 160</span></li>
      <li class="car-14__cell"><img src="data:image/svg+xml;utf8,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20300'%20width='300'%20height='300'%3E%3Cpath%20d='M150%2022l38%2076%2084%2012-61%2060%2014%2084-75-40-75%2040%2014-84-61-60%2084-12z'%20fill='%23404a66'/%3E%3C/svg%3E" width="300" height="300" alt="Stellar logo, star badge"><span>300 × 300</span></li>
      <li class="car-14__cell"><img src="data:image/svg+xml;utf8,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20480%20240'%20width='480'%20height='240'%3E%3Cellipse%20cx='240'%20cy='120'%20rx='210'%20ry='86'%20fill='none'%20stroke='%23404a66'%20stroke-width='14'/%3E%3Ctext%20x='240'%20y='150'%20text-anchor='middle'%20font-family='Arial,sans-serif'%20font-size='82'%20font-weight='800'%20letter-spacing='6'%20fill='%23404a66'%3EHALO%3C/text%3E%3C/svg%3E" width="480" height="240" alt="Halo logo, ellipse wordmark"><span>480 × 240</span></li>
    </ul>
    <footer class="car-14__foot">Equal cells ≠ equal pixels — <code>contain</code> gives every mark the same visual <em>budget</em> and lets its intrinsic ratio spend it. A demo from the CodeFronts aspect-ratio collection.</footer>
  </div>
</section>
```
## CSS
```css
.car-14,
.car-14 *,
.car-14 *::before,
.car-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.car-14 {
  --bg: oklch(0.98 0.004 250);
  --ink: oklch(0.24 0.02 260);
  --mut: oklch(0.5 0.015 260);
  --line: oklch(0.9 0.008 255);
  --acc: oklch(0.5 0.14 265);
  font-family: 'Segoe UI',system-ui,sans-serif;
  color: var(--ink);
  container-type: inline-size;
  display: block;
  width: 100%;
  min-height: 100vh;
  min-height: 100svh;
  background: var(--bg);
}

.car-14__stage {
  width: 100%;
  container: car14/inline-size;
  height: 100vh;
  height: 100svh;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  background: var(--bg);
}

.car-14__head {
  padding: clamp(24px,4.5cqi,48px) clamp(16px,4cqi,44px) 8px;
  max-width: 900px;
}

.car-14__kicker {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--acc);
}

.car-14__head h1 {
  font-size: clamp(24px,4cqi,40px);
  letter-spacing: -.025em;
  font-weight: 800;
  margin-top: 8px;
}

.car-14__lede {
  margin-top: 10px;
  font-size: 14px;
  line-height: 1.65;
  color: var(--mut);
}

.car-14__lede code,
.car-14__foot code {
  font-family: ui-monospace,Menlo,Consolas,monospace;
  font-size: .88em;
  background: oklch(0.92 0.008 255);
  padding: 2px 6px;
  border-radius: 5px;
  color: var(--acc);
}

.car-14__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.car-14__switch {
  border: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 16px;
}

.car-14__switch label {
  cursor: pointer;
}

.car-14__switch input {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
}

.car-14__switch span {
  display: grid;
  place-items: center;
  min-height: 44px;
  padding: 0 16px;
  border-radius: 99px;
  border: 1.5px solid var(--line);
  font-size: 13px;
  font-weight: 600;
  color: var(--mut);
  transition: border-color .2s,background .2s,color .2s;
}

.car-14__switch input:checked + span {
  border-color: var(--acc);
  background: var(--acc);
  color: oklch(0.99 0 0);
}

.car-14__switch input:focus-visible + span {
  outline: 3px solid var(--acc);
  outline-offset: 2px;
}

.car-14__switch span:hover {
  border-color: var(--acc);
}

.car-14__wall {
  list-style: none;
  flex: 1;
  display: grid;
  gap: 12px;
  grid-template-columns: repeat(auto-fill,minmax(min(200px,100%),1fr));
  align-content: start;
  padding: clamp(16px,3cqi,28px) clamp(16px,4cqi,44px);
}

.car-14__cell {
  position: relative;
  aspect-ratio: 3/2;
  display: grid;
  place-items: center;
  border: 1px solid var(--line);
  border-radius: 14px;
  background: oklch(1 0 0);
  transition: border-color .25s,box-shadow .25s,translate .25s;
}

.car-14__cell:hover {
  border-color: color-mix(in oklch,var(--acc) 45%,var(--line));
  box-shadow: 0 10px 26px oklch(0.3 0.03 260/.08);
  translate: 0 -2px;
}

.car-14__cell img {
  width: 74%;
  height: 58%;
  object-fit: contain;
  filter: grayscale(.2) opacity(.68);
  transition: filter .25s,scale .25s;
}

.car-14__cell:hover img {
  filter: none;
  scale: 1.03;
}

.car-14__cell span {
  position: absolute;
  right: 10px;
  bottom: 8px;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 9.5px;
  color: oklch(0.62 0.01 260);
  letter-spacing: .04em;
}

.car-14:has(#car14-cover:checked) .car-14__cell img {
  object-fit: cover;
}

.car-14:has(#car14-fill:checked) .car-14__cell img {
  object-fit: fill;
}

.car-14__foot {
  padding: 14px clamp(16px,4cqi,44px) 30px;
  border-top: 1px solid var(--line);
  font-size: 12.5px;
  line-height: 1.7;
  color: var(--mut);
}

@media (prefers-reduced-motion: reduce) {
  .car-14 * {
    transition-duration: .01ms !important;
  }
}
```
