---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tables/nutrition-facts-label-tailwind-css/"
title: "Nutrition Facts Label in Tailwind CSS"
section: "snippets"
category: "tailwind-css-tables"
category_name: "Tailwind CSS Tables"
description: "An FDA-style Nutrition Facts panel rebuilt as one semantic table: nutrient names are row headers, the % Daily Value column is a real column header, and the…"
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Nutrition Facts Label in Tailwind CSS
Source: https://codefronts.com/snippets/tailwind-css-tables/nutrition-facts-label-tailwind-css/

An FDA-style Nutrition Facts panel rebuilt as one semantic table: nutrient names are row headers, the % Daily Value column is a real column header, and the label's famous rule hierarchy — 10px, 5px and 1px bars — is just border-t-[10px], border-t-[5px] and border-t. Set in Libre Franklin, the closest open match to the label's Helvetica, with the calorie figure fluid via clamp().
## HTML
```html
<section class="ttb-11 grid-cols-1 w-full min-h-svh grid place-items-center bg-ttb11-bg px-5 py-14 font-ttb11-sans text-black" aria-label="Nutrition facts label demo">
  <div class="grid w-full justify-items-center gap-6">
    <div class="max-w-sm text-center">
      <p class="text-[11px] font-bold tracking-[0.2em] text-ttb11-acc uppercase">Cold-pressed · 240 mL</p>
      <h2 class="mt-1.5 text-2xl font-black tracking-[-0.02em]">Avocado Green Smoothie</h2>
    </div>
    <div class="w-full max-w-[320px] border-[3px] border-black bg-white p-2 shadow-[8px_8px_0_oklch(0_0_0/0.14)]">
      <table class="w-full border-collapse text-[13px] tabular-nums">
        <caption class="border-b border-black pb-1 text-left">
          <span class="block text-[44px] leading-[0.9] font-black tracking-[-0.04em]">Nutrition Facts</span>
          <span class="mt-1.5 block text-[14px]">2 servings per container</span>
          <span class="flex justify-between text-[15px] font-black"><span>Serving size</span><span>1 cup (240mL)</span></span>
        </caption>
        <tbody class="border-t-[10px] border-black">
          <tr><td colspan="2" class="pt-1 text-[11px] font-black">Amount per serving</td></tr>
          <tr class="align-baseline"><th scope="row" class="text-left text-[26px] leading-none font-black">Calories</th><td class="text-right text-[clamp(44px,14vw,52px)] leading-none font-black">280</td></tr>
        </tbody>
        <tbody class="border-t-[5px] border-black [&_td]:py-[3px] [&_td]:text-right [&_td]:font-bold [&_th]:py-[3px] [&_th]:text-left [&_th]:font-normal [&_tr+tr]:border-t [&_tr+tr]:border-black">
          <tr><td colspan="2" class="text-[11px] font-bold">% Daily Value*</td></tr>
          <tr><th scope="row"><b class="font-black">Total Fat</b> 14g</th><td>18%</td></tr>
          <tr><th scope="row" class="pl-4!">Saturated Fat 2g</th><td>10%</td></tr>
          <tr><th scope="row" class="pl-4!"><i>Trans</i> Fat 0g</th><td></td></tr>
          <tr><th scope="row"><b class="font-black">Cholesterol</b> 0mg</th><td>0%</td></tr>
          <tr><th scope="row"><b class="font-black">Sodium</b> 85mg</th><td>4%</td></tr>
          <tr><th scope="row"><b class="font-black">Total Carbohydrate</b> 32g</th><td>12%</td></tr>
          <tr><th scope="row" class="pl-4!">Dietary Fiber 6g</th><td>21%</td></tr>
          <tr><th scope="row" class="pl-4!">Total Sugars 18g</th><td></td></tr>
          <tr><th scope="row" class="pl-8!">Includes 10g Added Sugars</th><td>20%</td></tr>
          <tr><th scope="row"><b class="font-black">Protein</b> 5g</th><td></td></tr>
        </tbody>
        <tbody class="border-t-[10px] border-black [&_td]:py-[3px] [&_td]:text-right [&_th]:py-[3px] [&_th]:text-left [&_th]:font-normal [&_tr+tr]:border-t [&_tr+tr]:border-black">
          <tr><th scope="row">Vitamin D 2mcg</th><td>10%</td></tr>
          <tr><th scope="row">Calcium 260mg</th><td>20%</td></tr>
          <tr><th scope="row">Iron 8mg</th><td>45%</td></tr>
          <tr><th scope="row">Potassium 640mg</th><td>15%</td></tr>
        </tbody>
        <tfoot class="border-t-[5px] border-black">
          <tr><td colspan="2" class="pt-1.5 text-[10px] leading-snug">* The % Daily Value (DV) tells you how much a nutrient in a serving of food contributes to a daily diet. 2,000 calories a day is used for general nutrition advice.</td></tr>
        </tfoot>
      </table>
    </div>
  </div>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttb11-bg: #f1ece4;
  --color-ttb11-bg: oklch(0.94 0.013 80);
  --color-ttb11-acc: #3f7a2e;
  --color-ttb11-acc: oklch(0.52 0.12 140);
  --font-ttb11-sans: 'Libre Franklin', 'Helvetica Neue', Arial, sans-serif;
}
/* Root rule: the full-bleed contract, stated in CSS as well as in the markup's utilities, so the
   stage is sized before the browser build compiles. */

.ttb-11 {
  width: 100%;
  min-height: 100svh;
}
```
