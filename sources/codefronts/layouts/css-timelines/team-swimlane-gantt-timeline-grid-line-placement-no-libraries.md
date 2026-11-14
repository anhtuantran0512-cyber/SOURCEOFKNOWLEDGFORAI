---
source: "codefronts"
url: "https://codefronts.com/layouts/css-timelines/team-swimlane-gantt-timeline-grid-line-placement-no-libraries/"
title: "Team Swimlane Gantt Timeline — Grid-Line Placement, No Libraries"
section: "layouts"
category: "css-timelines"
category_name: "CSS Timelines"
description: "A real project Gantt without a charting library: team swimlanes as grid rows, a 12-week header, and every task bar positioned purely by grid-column line…"
has_js: "false"
---

Here's a working CSS Timeline from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Team Swimlane Gantt Timeline — Grid-Line Placement, No Libraries
Source: https://codefronts.com/layouts/css-timelines/team-swimlane-gantt-timeline-grid-line-placement-no-libraries/

A real project Gantt without a charting library: team swimlanes as grid rows, a 12-week header, and every task bar positioned purely by grid-column line numbers — change a task's start and length by editing two integers in the HTML. Week gridlines come from one repeating gradient; the current week is a highlighted column band.
## HTML
```html
<section class="tls-07" aria-label="Team gantt timeline demo">
  <div class="tls-07__inner">
    <header class="tls-07__head"><h3 class="tls-07__title">Q3 delivery plan</h3><p class="tls-07__sub">12 weeks · 3 teams</p></header>
    <div class="tls-07__chart">
      <div class="tls-07__weeks" aria-hidden="true">
        <span></span><span>W1</span><span>W2</span><span>W3</span><span>W4</span><span>W5</span><span>W6</span><span>W7</span><span>W8</span><span>W9</span><span>W10</span><span>W11</span><span>W12</span>
      </div>
      <div class="tls-07__lanes">
        <div class="tls-07__nowband" aria-hidden="true"></div>
        <p class="tls-07__lane">Design</p>
        <!-- grid-column: (week + 1) / span duration -->
        <div class="tls-07__bar" style="--c:#7c3aed;grid-column:2/span 3;grid-row:1"><span class="tls-07__bfill" style="width:100%"></span><span class="tls-07__bname">Discovery<span class="tls-07__sr"> — weeks 1 to 3, done</span></span></div>
        <div class="tls-07__bar" style="--c:#7c3aed;grid-column:5/span 4;grid-row:1"><span class="tls-07__bfill" style="width:60%"></span><span class="tls-07__bname">Design system<span class="tls-07__sr"> — weeks 4 to 7, 60% done</span></span></div>
        <p class="tls-07__lane" style="grid-row:2">Engineering</p>
        <div class="tls-07__bar" style="--c:#0e7490;grid-column:4/span 5;grid-row:2"><span class="tls-07__bfill" style="width:75%"></span><span class="tls-07__bname">Core build<span class="tls-07__sr"> — weeks 3 to 7, 75% done</span></span></div>
        <div class="tls-07__bar" style="--c:#0e7490;grid-column:9/span 4;grid-row:2"><span class="tls-07__bfill" style="width:0%"></span><span class="tls-07__bname">Hardening<span class="tls-07__sr"> — weeks 8 to 11, not started</span></span></div>
        <p class="tls-07__lane" style="grid-row:3">Marketing</p>
        <div class="tls-07__bar" style="--c:#b45309;grid-column:7/span 3;grid-row:3"><span class="tls-07__bfill" style="width:30%"></span><span class="tls-07__bname">Launch prep<span class="tls-07__sr"> — weeks 6 to 8, 30% done</span></span></div>
        <div class="tls-07__bar" style="--c:#b45309;grid-column:11/span 3;grid-row:3"><span class="tls-07__bfill" style="width:0%"></span><span class="tls-07__bname">Campaign<span class="tls-07__sr"> — weeks 10 to 12, not started</span></span></div>
      </div>
    </div>
  </div>
</section>
```
## CSS
```css
.tls-07,
.tls-07 *,
.tls-07 *::before,
.tls-07 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.tls-07 {
  min-height: 100vh;
  width: 100%;
  --tl-line: #e7e5e4;
  --tl-ink: #1c1917;
  --tl-mut: #78716c;
  --label: 110px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: #fafaf9;
  padding: 64px 24px;
  display: grid;
  place-items: center;
}

.tls-07__inner {
  width: min(880px,100%);
}

.tls-07__head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 22px;
}

.tls-07__title {
  font-size: clamp(20px,3.5vw,26px);
  font-weight: 800;
  color: var(--tl-ink);
  letter-spacing: -.02em;
}

.tls-07__sub {
  font-size: 12.5px;
  color: var(--tl-mut);
}

.tls-07__chart {
  background: #fff;
  border: 1px solid var(--tl-line);
  border-radius: 14px;
  padding: 18px 20px 22px;
  overflow: hidden;
}

.tls-07__weeks {
  display: grid;
  grid-template-columns: var(--label) repeat(12,1fr);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .06em;
  color: var(--tl-mut);
  text-align: center;
  padding-bottom: 10px;
  border-bottom: 1px solid var(--tl-line);
  margin-bottom: 14px;
}

.tls-07__lanes {
  position: relative;
  display: grid;
  grid-template-columns: var(--label) repeat(12,1fr);
  grid-auto-rows: 44px;
  row-gap: 10px;
  align-items: center;
  background: repeating-linear-gradient(90deg,transparent 0,transparent calc((100% - var(--label)) / 12 - 1px),var(--tl-line) calc((100% - var(--label)) / 12 - 1px),var(--tl-line) calc((100% - var(--label)) / 12));
  background-position: var(--label) 0;
  background-repeat: no-repeat;
  background-size: calc(100% - var(--label)) 100%;
  background-origin: padding-box;
}

.tls-07__nowband {
  grid-column: 9;
  grid-row: 1/-1;
  height: 100%;
  background: rgb(220 38 38 / .06);
  border-inline: 1px dashed rgb(220 38 38 / .4);
}

.tls-07__lane {
  grid-column: 1;
  font-size: 12.5px;
  font-weight: 700;
  color: var(--tl-mut);
  padding-right: 14px;
}

.tls-07__bar {
  position: relative;
  height: 30px;
  border-radius: 8px;
  background: color-mix(in srgb,var(--c) 14%,#fff);
  border: 1px solid color-mix(in srgb,var(--c) 40%,#fff);
  overflow: hidden;
  display: flex;
  align-items: center;
}

.tls-07__bfill {
  position: absolute;
  inset: 0 auto 0 0;
  background: color-mix(in srgb,var(--c) 26%,#fff);
}

.tls-07__bname {
  position: relative;
  font-size: 11px;
  font-weight: 700;
  color: var(--c);
  padding-inline: 10px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.tls-07__sr {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip-path: inset(50%);
  white-space: nowrap;
}

@media (max-width: 640px) {
  .tls-07__weeks {
    display: none;
  }

  .tls-07__lanes {
    grid-template-columns: 1fr;
    grid-auto-rows: auto;
    background: none;
  }

  .tls-07__nowband {
    display: none;
  }

  .tls-07__lane {
    grid-row: auto!important;
    padding: 6px 0 2px;
  }

  .tls-07__bar {
    grid-column: 1!important;
    grid-row: auto!important;
  }
}
```

## JavaScript
```js
/* No JavaScript — every bar is grid-column: start / span duration (two integers = the whole API); week gridlines are one repeating-linear-gradient sized to the fr tracks. */
```
