---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/fermentation-calendar/"
title: "Fermentation Calendar Timeline — Process Stages as Duration Bars"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "A Gantt in an apron: process stages (primary ferment, cold crash, conditioning) drawn as duration bars on a shared week grid, each bar positioned and sized…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Fermentation Calendar Timeline — Process Stages as Duration Bars
Source: https://codefronts.com/layouts/css-timelines/fermentation-calendar/

A Gantt in an apron: process stages (primary ferment, cold crash, conditioning) drawn as duration bars on a shared week grid, each bar positioned and sized purely by grid-column line math from inline tokens — the duration-first timeline for recipes, aging processes, brewing logs and any 'what happens when' production cycle.
## HTML
```html
<section class="tls-14" aria-label="Fermentation calendar timeline demo">
  <div class="tls-14__board" style="--tl-weeks:10;--tl-nowweek:4">
    <header class="tls-14__head">
      <h3 class="tls-14__title">Saison № 12 — cellar calendar</h3>
      <p class="tls-14__sub">Pitched <time datetime="2026-06-21">Jun 21</time> · week 4 of 10</p>
    </header>
    <div class="tls-14__weeks" aria-hidden="true"><span>W1</span><span>W2</span><span>W3</span><span>W4</span><span>W5</span><span>W6</span><span>W7</span><span>W8</span><span>W9</span><span>W10</span></div>
    <ol class="tls-14__chart" role="list">
      <li class="tls-14__bar" style="--s:1;--d:2;--mix:0%" data-temp="21°C ambient">Primary ferment</li>
      <li class="tls-14__bar" style="--s:3;--d:1;--mix:18%" data-temp="21°C · gravity check">Diacetyl rest</li>
      <li class="tls-14__bar" style="--s:4;--d:2;--mix:32%" data-temp="2°C crash">Cold crash</li>
      <li class="tls-14__bar" style="--s:6;--d:3;--mix:48%" data-temp="12°C · 2.4 vol CO₂">Bottle conditioning</li>
      <li class="tls-14__bar" style="--s:9;--d:2;--mix:64%" data-temp="8°C cellar">Rest &amp; taste</li>
    </ol>
    <div class="tls-14__nowline" aria-hidden="true"><span>today</span></div>
  </div>
</section>
```
## CSS
```css
.tls-14,
.tls-14 *,
.tls-14 *::before,
.tls-14 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-14 {
  min-height: 100vh;
  width: 100%;
  --tl-accent: #c2410c;
  --tl-paper: #fdf9f2;
  --tl-ink: #3d2f24;
  --tl-mut: #a08b76;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #efe7da;
  padding: 56px 24px;
  display: grid;
  place-items: center;
}

.tls-14__board {
  width: min(680px,100%);
  position: relative;
  background: var(--tl-paper);
  border: 1px solid #e2d5c2;
  border-radius: 14px;
  padding: 24px 28px 30px;
}

.tls-14__head {
  margin-bottom: 20px;
}

.tls-14__title {
  font-family: Georgia,serif;
  font-size: clamp(18px,3vw,23px);
  font-weight: 700;
  color: var(--tl-ink);
}

.tls-14__sub {
  font-size: 12.5px;
  color: var(--tl-mut);
  margin-top: 3px;
}

.tls-14__weeks {
  display: grid;
  grid-template-columns: repeat(var(--tl-weeks),1fr);
  font-family: ui-monospace,Menlo,monospace;
  font-size: 9.5px;
  color: var(--tl-mut);
  text-align: center;
  margin-bottom: 6px;
}

.tls-14__chart {
  list-style: none;
  display: grid;
  grid-template-columns: repeat(var(--tl-weeks),1fr);
  grid-auto-rows: 38px;
  row-gap: 8px;
  background: repeating-linear-gradient(90deg,transparent 0 calc(100% / var(--tl-weeks) - 1px),#eadfce calc(100% / var(--tl-weeks) - 1px) calc(100% / var(--tl-weeks)));
  border-radius: 8px;
  position: relative;
  padding-block: 8px;
}

.tls-14__bar {
  grid-column: var(--s) / span var(--d);
  position: relative;
  display: flex;
  align-items: center;
  background: color-mix(in oklab,var(--tl-accent),#f5e0c8 var(--mix));
  color: #fff;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: .01em;
  border-radius: 7px;
  padding-inline: 12px;
  min-width: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  box-shadow: inset 0 -2px 0 rgba(60,30,0,.18);
  cursor: default;
}

.tls-14__bar[style*="--mix:48%"],
.tls-14__bar[style*="--mix:64%"] {
  color: #5c3a1e;
}

.tls-14__bar:hover::after,
.tls-14__bar:focus-visible::after {
  content: attr(data-temp);
  position: absolute;
  left: 10px;
  bottom: calc(100% + 6px);
  z-index: 2;
  background: var(--tl-ink);
  color: var(--tl-paper);
  font-size: 10.5px;
  font-weight: 600;
  border-radius: 6px;
  padding: 4px 9px;
  white-space: nowrap;
}

.tls-14__nowline {
  position: absolute;
  top: 86px;
  bottom: 24px;
  left: calc(28px + (100% - 56px) * (var(--tl-nowweek) - .5) / var(--tl-weeks));
  width: 2px;
  background: #16a34a;
  border-radius: 1px;
}

.tls-14__nowline span {
  position: absolute;
  top: -16px;
  left: 50%;
  translate: -50% 0;
  font-size: 9px;
  font-weight: 800;
  letter-spacing: .14em;
  text-transform: uppercase;
  color: #16a34a;
}

@media (max-width: 520px) {
  .tls-14__weeks span:nth-child(odd) {
    visibility: hidden;
  }
}
```

## JavaScript
```js
/* No JavaScript — each bar is grid-column:var(--s)/span var(--d); the week ruling and the today-line divide by the same --tl-weeks token, so scale changes stay in sync. */
```
