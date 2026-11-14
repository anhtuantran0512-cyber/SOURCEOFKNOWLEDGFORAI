---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/stratigraphy-timeline/"
title: "Stratigraphy Timeline — Geological Layer Blocks with Depth Scale"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "Deep time as sediment: stacked era blocks whose heights are proportional to duration, textured with pure-CSS grain gradients, flanked by a depth scale — the…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Stratigraphy Timeline — Geological Layer Blocks with Depth Scale
Source: https://codefronts.com/layouts/css-timelines/stratigraphy-timeline/

Deep time as sediment: stacked era blocks whose heights are proportional to duration, textured with pure-CSS grain gradients, flanked by a depth scale — the layered-block metaphor that fits geology, archaeology dig reports, company history 'eras' and any dataset where duration should be FELT, not just labeled.
## HTML
```html
<section class="tls-09" aria-label="Stratigraphy timeline demo">
  <div class="tls-09__frame">
    <header class="tls-09__head"><h3 class="tls-09__title">Deep time, to scale</h3><p class="tls-09__sub">Layer height = era duration (Ma = million years ago)</p></header>
    <div class="tls-09__dig">
      <div class="tls-09__scale" aria-hidden="true"><span>0</span><span>50</span><span>100</span><span>150</span><span>200 Ma</span></div>
      <ol class="tls-09__col" role="list">
        <li class="tls-09__layer" style="--span:23;--c:oklch(.82 .09 95)">
          <div class="tls-09__chip"><b>Neogene &amp; Quaternary</b><span>23 Ma – now</span></div>
          <p class="tls-09__note">Grasslands spread; hominins appear</p>
        </li>
        <li class="tls-09__layer" style="--span:43;--c:oklch(.75 .1 70)">
          <div class="tls-09__chip"><b>Paleogene</b><span>66 – 23 Ma</span></div>
          <p class="tls-09__note">Mammals radiate into vacant niches</p>
          <span class="tls-09__seam"><i aria-hidden="true"></i>K–Pg extinction · 66 Ma</span>
        </li>
        <li class="tls-09__layer" style="--span:79;--c:oklch(.68 .1 145)">
          <div class="tls-09__chip"><b>Cretaceous</b><span>145 – 66 Ma</span></div>
          <p class="tls-09__note">First flowering plants; T. rex at the very end</p>
        </li>
        <li class="tls-09__layer" style="--span:56;--c:oklch(.6 .09 230)">
          <div class="tls-09__chip"><b>Jurassic</b><span>201 – 145 Ma</span></div>
          <p class="tls-09__note">Giant sauropods; first birds</p>
        </li>
      </ol>
    </div>
  </div>
</section>
```
## CSS
```css
.tls-09,
.tls-09 *,
.tls-09 *::before,
.tls-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-09 {
  min-height: 100vh;
  width: 100%;
  --tl-ink: #2b2419;
  --tl-mut: #8c8172;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #f3efe7;
  padding: 56px 24px;
  display: grid;
  place-items: center;
}

.tls-09__frame {
  width: min(620px,100%);
}

.tls-09__head {
  margin-bottom: 18px;
}

.tls-09__title {
  font-family: Georgia,'Times New Roman',serif;
  font-size: clamp(20px,3vw,26px);
  font-weight: 700;
  color: var(--tl-ink);
  letter-spacing: -.01em;
}

.tls-09__sub {
  font-size: 12.5px;
  color: var(--tl-mut);
  margin-top: 4px;
}

.tls-09__dig {
  display: grid;
  grid-template-columns: auto 1fr;
  gap: 14px;
}

.tls-09__scale {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-end;
  font-family: ui-monospace,Menlo,monospace;
  font-size: 10.5px;
  color: var(--tl-mut);
  padding-block: 2px;
  font-variant-numeric: tabular-nums;
}

.tls-09__col {
  list-style: none;
  height: 520px;
  display: flex;
  flex-direction: column;
  border: 2px solid #3d3426;
  border-radius: 6px;
  overflow: hidden;
}

.tls-09__layer {
  position: relative;
  flex-grow: var(--span);
  min-height: 34px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 4px;
  padding: 12px 18px;
  background: linear-gradient(180deg,color-mix(in oklab,var(--c),#fff 8%),var(--c)),var(--c);
  background-blend-mode: normal;
}

.tls-09__layer::before {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(180deg,rgba(40,30,10,.06) 0 1px,transparent 1px 4px),repeating-linear-gradient(180deg,transparent 0 22px,rgba(40,30,10,.05) 22px 26px);
  pointer-events: none;
}

.tls-09__layer + .tls-09__layer {
  border-top: 2px dashed rgba(40,30,10,.28);
}

.tls-09__chip {
  position: relative;
  display: inline-flex;
  align-items: baseline;
  gap: 10px;
  align-self: flex-start;
  background: rgba(255,253,248,.92);
  border-radius: 8px;
  padding: 5px 12px;
}

.tls-09__chip b {
  font-family: Georgia,serif;
  font-size: 14.5px;
  color: var(--tl-ink);
}

.tls-09__chip span {
  font-family: ui-monospace,Menlo,monospace;
  font-size: 10.5px;
  color: var(--tl-mut);
  font-variant-numeric: tabular-nums;
}

.tls-09__note {
  position: relative;
  font-size: 12px;
  color: rgba(30,22,8,.75);
  opacity: 0;
  translate: 0 4px;
  transition: opacity .2s,translate .2s;
  text-wrap: pretty;
}

.tls-09__layer:hover .tls-09__note {
  opacity: 1;
  translate: 0 0;
}

.tls-09__seam {
  position: absolute;
  top: 0;
  left: 18px;
  translate: 0 -50%;
  z-index: 1;
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-size: 10.5px;
  font-weight: 700;
  letter-spacing: .04em;
  color: #7f1d1d;
  background: #fef2f2;
  border: 1px solid #fca5a5;
  border-radius: 999px;
  padding: 3px 10px;
}

.tls-09__seam i {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #dc2626;
}

@media (prefers-reduced-motion: reduce) {
  .tls-09__note {
    opacity: 1;
    translate: 0 0;
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — layer heights are flex-grow:var(--span) proportions inside a fixed-height column; sediment grain is stacked repeating-linear-gradients. */
```
