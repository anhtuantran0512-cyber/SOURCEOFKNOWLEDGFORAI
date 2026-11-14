---
source: "codefronts"
url: "https://codefronts.com/snippets/css-table-styles/nutrition-facts-label/"
title: "Nutrition Facts Label"
section: "snippets"
category: "css-table-styles"
category_name: "CSS Tables"
description: "A pixel-perfect FDA-replica Nutrition Facts panel built with a nested HTML table, precise border-width hierarchy (thick, medium, thin), and a scanning accent…"
has_js: "false"
---

Here's a working CSS Table from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Nutrition Facts Label
Source: https://codefronts.com/snippets/css-table-styles/nutrition-facts-label/

A pixel-perfect FDA-replica Nutrition Facts panel built with a nested HTML table, precise border-width hierarchy (thick, medium, thin), and a scanning accent line animation — no images required.
## HTML
```html
<div class="ct-11">
  <div class="ct-11__context">
    <div class="ct-11__context-title">🥑 AvocadoBlast Smoothie</div>
    <div class="ct-11__context-sub">Precisely styled FDA-replica Nutrition Facts using pure CSS table borders, bold weights, and strict typographic hierarchy — no images needed.</div>
  </div>

  <div class="ct-11__label">
    <div class="ct-11__label-title">Nutrition<br>Facts</div>
    <div class="ct-11__serving-line">2 servings per container</div>
    <div class="ct-11__serving-line">Serving size <span class="ct-11__serving-amount">1 cup (240mL)</span></div>

    <div class="ct-11__bar--thick"></div>

    <div class="ct-11__calories-row">
      <div>
        <div class="ct-11__cal-label">Amount per serving</div>
        <div style="font-size:13px;font-weight:900">Calories</div>
      </div>
      <div class="ct-11__cal-number">280</div>
    </div>

    <div class="ct-11__dv-header">% Daily Value*</div>

    <table>
      <tbody>
        <tr>
          <td><span class="ct-11__label-bold">Total Fat</span> <span class="ct-11__label-normal">14g</span></td>
          <td>18%</td>
        </tr>
        <tr>
          <td class="ct-11__indent"><span class="ct-11__label-normal">Saturated Fat 2g</span></td>
          <td>10%</td>
        </tr>
        <tr>
          <td class="ct-11__indent"><span class="ct-11__label-normal">Trans Fat 0g</span></td>
          <td></td>
        </tr>
        <tr>
          <td><span class="ct-11__label-bold">Cholesterol</span> <span class="ct-11__label-normal">0mg</span></td>
          <td>0%</td>
        </tr>
        <tr>
          <td><span class="ct-11__label-bold">Sodium</span> <span class="ct-11__label-normal">85mg</span></td>
          <td>4%</td>
        </tr>
        <tr>
          <td><span class="ct-11__label-bold">Total Carbohydrate</span> <span class="ct-11__label-normal">32g</span></td>
          <td>12%</td>
        </tr>
        <tr>
          <td class="ct-11__indent"><span class="ct-11__label-normal">Dietary Fiber 6g</span></td>
          <td>21%</td>
        </tr>
        <tr>
          <td class="ct-11__indent"><span class="ct-11__label-normal">Total Sugars 18g</span></td>
          <td></td>
        </tr>
        <tr>
          <td class="ct-11__indent2"><span class="ct-11__label-normal">Includes 10g Added Sugars</span></td>
          <td>20%</td>
        </tr>
        <tr>
          <td><span class="ct-11__label-bold">Protein</span> <span class="ct-11__label-normal">5g</span></td>
          <td></td>
        </tr>
      </tbody>
    </table>

    <div class="ct-11__bar--medium"></div>

    <table>
      <tbody>
        <tr>
          <td style="font-size:11px">Vitamin D 2mcg</td>
          <td style="font-size:11px">10%</td>
        </tr>
        <tr>
          <td style="font-size:11px">Calcium 260mg</td>
          <td style="font-size:11px">20%</td>
        </tr>
        <tr>
          <td style="font-size:11px">Iron 8mg</td>
          <td style="font-size:11px">45%</td>
        </tr>
        <tr>
          <td style="font-size:11px">Potassium 640mg</td>
          <td style="font-size:11px">15%</td>
        </tr>
      </tbody>
    </table>

    <div class="ct-11__dv-note">
      *The % Daily Value tells you how much a nutrient in a serving of food contributes to a daily diet. 2,000 calories a day is used for general nutrition advice.
    </div>
  </div>
</div>
```
## CSS
```css
.ct-11,
.ct-11 *,
.ct-11 *::before,
.ct-11 *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.ct-11 ::selection {
  background: #000;
  color: #fff;
}

.ct-11 {
  --bg: #f0ece6;
  --card: #ffffff;
  --border: #000000;
  --text: #000000;
  --sub: #1a1a1a;
  --accent: #e63946;
  font-family: 'Arial Black', 'Arial', Helvetica, sans-serif;
  background: var(--bg);
  /* The .ct-11 wrapper sets --text but never applies it. Without an
       explicit color declaration on the wrapper, descendant text inherits
       whatever color the host page or the iframe root sets — on
       codefronts that is the dark-theme token (~#f0eeff), so the FDA
       label text renders pale-violet-on-cream and is barely readable.
       Black-on-cream is the actual design intent. */
  color: var(--text);
  padding: 40px 24px;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 24px;
}

.ct-11__context {
  text-align: center;
  max-width: 380px;
}

.ct-11__context-title {
  font-size: 22px;
  font-weight: 900;
  letter-spacing: -0.5px;
  margin-bottom: 4px;
}

.ct-11__context-sub {
  font-size: 13px;
  color: #555;
}
/* THE NUTRITION LABEL */

.ct-11__label {
  width: 320px;
  background: var(--card);
  border: 3px solid var(--border);
  padding: 8px;
  box-shadow: 8px 8px 0 rgba(0,0,0,0.15);
}

.ct-11__label-title {
  font-size: 42px;
  font-weight: 900;
  line-height: 0.9;
  border-bottom: 1px solid var(--border);
  padding-bottom: 4px;
  margin-bottom: 4px;
  letter-spacing: -2px;
}

.ct-11__serving-line {
  font-size: 12px;
  font-weight: 400;
  margin: 4px 0;
  font-family: Arial, sans-serif;
}

.ct-11__serving-amount {
  font-size: 13px;
  font-weight: 700;
}
/* Big thick bar */

.ct-11__bar--thick {
  border-top: 9px solid var(--border);
  margin: 4px 0;
}

.ct-11__bar--medium {
  border-top: 5px solid var(--border);
  margin: 2px 0;
}

.ct-11__bar--thin {
  border-top: 1px solid var(--border);
  margin: 1px 0;
}

.ct-11__calories-row {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  padding: 2px 0;
}

.ct-11__cal-label {
  font-size: 13px;
  font-weight: 900;
}

.ct-11__cal-number {
  font-size: 56px;
  font-weight: 900;
  line-height: 1;
}

.ct-11__dv-header {
  text-align: right;
  font-size: 9px;
  font-weight: 700;
  font-family: Arial, sans-serif;
  border-top: 5px solid var(--border);
  padding-top: 3px;
  margin-bottom: 2px;
}

.ct-11 table {
  width: 100%;
  border-collapse: collapse;
  font-family: Arial, sans-serif;
}

.ct-11 tbody tr {
  border-top: 1px solid var(--border);
}

.ct-11 tbody tr:first-child {
  border-top: none;
}

.ct-11 tbody td {
  padding: 2px 0;
  font-size: 12px;
  vertical-align: middle;
}

.ct-11 tbody td:last-child {
  text-align: right;
  font-weight: 700;
  font-size: 12px;
}

.ct-11__label-bold {
  font-weight: 900;
}

.ct-11__label-normal {
  font-weight: 400;
}

.ct-11__indent {
  padding-left: 14px !important;
}

.ct-11__indent2 {
  padding-left: 28px !important;
}

.ct-11__dv-note {
  font-size: 9px;
  font-family: Arial, sans-serif;
  border-top: 5px solid var(--border);
  padding-top: 6px;
  margin-top: 4px;
  line-height: 1.4;
}
/* Animated scan line for fun */

.ct-11__label::after {
  content: '';
  display: block;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--accent), transparent);
  background-size: 60% 100%;
  background-repeat: no-repeat;
  animation: ct-11-scan 3s ease-in-out infinite;
  margin-top: 6px;
}

@keyframes ct-11-scan {
  0% {
    background-position: -60% 0;
  }

  100% {
    background-position: 160% 0;
  }
}
/* Hover interactive rows */

.ct-11 tbody tr {
  transition: background 0.15s;
  cursor: default;
}

.ct-11 tbody tr:hover {
  background: rgba(230,57,70,0.06);
}

@media (prefers-reduced-motion: reduce) {
  .ct-11__label::after {
    animation: none;
  }

  .ct-11 tbody tr {
    transition: none;
  }
}
```
