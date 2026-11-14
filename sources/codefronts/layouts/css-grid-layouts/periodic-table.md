---
source: "codefronts"
url: "https://codefronts.com/layouts/css-grid-layouts/periodic-table/"
title: "Periodic Table"
section: "layouts"
category: "css-grid-layouts"
category_name: "CSS Grid Layouts"
description: "The final boss of grid placement: a real 18-column periodic table where hydrogen sits at 1/1, helium jumps to column 18, and the d-block gap appears because…"
has_js: "false"
---

Here's a working CSS Grid Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Periodic Table
Source: https://codefronts.com/layouts/css-grid-layouts/periodic-table/

The final boss of grid placement: a real 18-column periodic table where hydrogen sits at 1/1, helium jumps to column 18, and the d-block gap appears because elements are PLACED, not flowed. A working sample of periods 1–4 with category coloring — the demo that proves you understand grid coordinates.
## HTML
```html
<section class="cgl-30" aria-label="Periodic table grid demo">
  <div class="cgl-30__scroll">
    <div class="cgl-30__table" role="group" aria-label="Periodic table, periods 1 to 4 sample">
      <button type="button" style="--c:oklch(0.75 0.14 150)"><i>1</i><b>H</b><span>hydrogen</span></button>
      <button type="button" style="--c:oklch(0.75 0.12 300);grid-column:18"><i>2</i><b>He</b><span>helium</span></button>
      <button type="button" style="--c:oklch(0.72 0.16 25)"><i>3</i><b>Li</b><span>lithium</span></button>
      <button type="button" style="--c:oklch(0.78 0.13 85)"><i>4</i><b>Be</b><span>beryllium</span></button>
      <button type="button" style="--c:oklch(0.74 0.12 200);grid-column:13"><i>5</i><b>B</b><span>boron</span></button>
      <button type="button" style="--c:oklch(0.75 0.14 150)"><i>6</i><b>C</b><span>carbon</span></button>
      <button type="button" style="--c:oklch(0.75 0.14 150)"><i>7</i><b>N</b><span>nitrogen</span></button>
      <button type="button" style="--c:oklch(0.75 0.14 150)"><i>8</i><b>O</b><span>oxygen</span></button>
      <button type="button" style="--c:oklch(0.7 0.15 350)"><i>9</i><b>F</b><span>fluorine</span></button>
      <button type="button" style="--c:oklch(0.75 0.12 300)"><i>10</i><b>Ne</b><span>neon</span></button>
      <button type="button" style="--c:oklch(0.72 0.16 25)"><i>11</i><b>Na</b><span>sodium</span></button>
      <button type="button" style="--c:oklch(0.78 0.13 85)"><i>12</i><b>Mg</b><span>magnesium</span></button>
      <button type="button" style="--c:oklch(0.74 0.12 200);grid-column:13"><i>13</i><b>Al</b><span>aluminium</span></button>
      <button type="button" style="--c:oklch(0.74 0.12 200)"><i>14</i><b>Si</b><span>silicon</span></button>
      <button type="button" style="--c:oklch(0.75 0.14 150)"><i>15</i><b>P</b><span>phosphorus</span></button>
      <button type="button" style="--c:oklch(0.75 0.14 150)"><i>16</i><b>S</b><span>sulfur</span></button>
      <button type="button" style="--c:oklch(0.7 0.15 350)"><i>17</i><b>Cl</b><span>chlorine</span></button>
      <button type="button" style="--c:oklch(0.75 0.12 300)"><i>18</i><b>Ar</b><span>argon</span></button>
      <button type="button" style="--c:oklch(0.72 0.16 25)"><i>19</i><b>K</b><span>potassium</span></button>
      <button type="button" style="--c:oklch(0.78 0.13 85)"><i>20</i><b>Ca</b><span>calcium</span></button>
      <button type="button" style="--c:oklch(0.76 0.1 240)"><i>21</i><b>Sc</b><span>scandium</span></button>
      <button type="button" style="--c:oklch(0.76 0.1 240)"><i>22</i><b>Ti</b><span>titanium</span></button>
      <button type="button" style="--c:oklch(0.76 0.1 240)"><i>23</i><b>V</b><span>vanadium</span></button>
      <button type="button" style="--c:oklch(0.76 0.1 240)"><i>24</i><b>Cr</b><span>chromium</span></button>
      <button type="button" style="--c:oklch(0.76 0.1 240)"><i>25</i><b>Mn</b><span>manganese</span></button>
      <button type="button" style="--c:oklch(0.76 0.1 240)"><i>26</i><b>Fe</b><span>iron</span></button>
    </div>
  </div>
  <p class="cgl-30__note">Periods 1–4 (partial). He and B/Al are explicitly placed; auto-flow draws the rest of the silhouette.</p>
</section>
```
## CSS
```css
.cgl-30,
.cgl-30 *,
.cgl-30 *::before,
.cgl-30 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.cgl-30 {
  width: 100%;
  min-height: 100vh;
  --bg: oklch(0.15 0.015 260);
  font-family: system-ui,sans-serif;
  background: var(--bg);
  padding: 1.4rem;
}

.cgl-30 .cgl-30__scroll {
  overflow-x: auto;
  padding-block-end: 6px;
}

.cgl-30 .cgl-30__table {
  display: grid;
  grid-template-columns: repeat(18,minmax(30px,1fr));
  gap: 4px;
  min-inline-size: 620px;
}

.cgl-30 .cgl-30__table button {
  aspect-ratio: 1/1.05;
  display: grid;
  grid-template-rows: auto 1fr auto;
  padding: 3px 4px;
  border-radius: 6px;
  cursor: pointer;
  background: color-mix(in oklab,var(--c) 16%,var(--bg));
  border: 1px solid color-mix(in oklab,var(--c) 40%,var(--bg));
  transition: background .2s ease,translate .2s ease;
}

.cgl-30 .cgl-30__table button:hover {
  background: color-mix(in oklab,var(--c) 32%,var(--bg));
  translate: 0 -2px;
}

.cgl-30 .cgl-30__table button:focus-visible {
  outline: 2px solid var(--c);
  outline-offset: 2px;
}

.cgl-30 .cgl-30__table i {
  font-style: normal;
  font-size: .5rem;
  justify-self: start;
  color: color-mix(in oklab,var(--c) 75%,white);
  font-variant-numeric: tabular-nums;
}

.cgl-30 .cgl-30__table b {
  font-size: clamp(.7rem,2.2vw,.95rem);
  color: white;
  place-self: center;
}

.cgl-30 .cgl-30__table span {
  font-size: .42rem;
  letter-spacing: .02em;
  color: color-mix(in oklab,var(--c) 60%,white);
  justify-self: center;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  max-inline-size: 100%;
}

.cgl-30 .cgl-30__note {
  font-size: .7rem;
  color: oklch(0.62 0.02 260);
  margin-block-start: .8rem;
}

@media (prefers-reduced-motion: reduce) {
  .cgl-30 .cgl-30__table button {
    transition: none;
  }
}
```

## JavaScript
```js
/* No JavaScript — two explicit grid-column placements per period + forward-only auto-flow draw the table's iconic silhouette. */
```
