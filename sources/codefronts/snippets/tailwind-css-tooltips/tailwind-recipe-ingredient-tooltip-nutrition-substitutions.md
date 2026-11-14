---
source: "codefronts"
url: "https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-recipe-ingredient-tooltip-nutrition-substitutions/"
title: "Tailwind Recipe Ingredient Tooltip with Nutrition and Substitutions"
section: "snippets"
category: "tailwind-css-tooltips"
category_name: "Tailwind CSS Tooltips"
description: "A cookbook page where each ingredient carries a dotted underline and opens a side card with nutrition, substitutions and a sourcing note."
has_js: "false"
---

Here's a working CSS demo from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Tailwind Recipe Ingredient Tooltip with Nutrition and Substitutions
Source: https://codefronts.com/snippets/tailwind-css-tooltips/tailwind-recipe-ingredient-tooltip-nutrition-substitutions/

A cookbook page where each ingredient carries a dotted underline and opens a side card with nutrition, substitutions and a sourcing note. Warm paper palette, Georgia for the recipe, Inter inside the card &mdash; the port's value is that the two typographic registers are now visible per element instead of split across sixteen rules.
## HTML
```html
<section class="ttp-14 w-full min-h-svh bg-ttp14-stage py-10 pr-[320px] pl-7 font-ttp14-serif max-xl:pr-7">
  <article class="mx-auto max-w-[480px] rounded-[2px] border border-ttp14-edge bg-white px-9 py-8 shadow-[0_2px_22px_rgba(100,80,40,0.08),0_0_0_4px_rgba(180,160,120,0.06)]">
    <h2 class="m-0 mb-1 text-[26px] italic leading-tight text-ttp14-ink">Roasted Lemon Herb Chicken</h2>
    <div class="mb-5 text-xs uppercase tracking-[0.08em] text-ttp14-meta">French Country · Serves 4</div>
    <div class="mb-5.5 flex flex-wrap gap-5 border-b border-ttp14-edge pb-4">
      <div><div class="ttp14-mlabel">Prep</div><div class="ttp14-mval">20 min</div></div>
      <div><div class="ttp14-mlabel">Cook</div><div class="ttp14-mval">1 hr 15 min</div></div>
      <div><div class="ttp14-mlabel">Total</div><div class="ttp14-mval">1 hr 35 min</div></div>
      <div><div class="ttp14-mlabel">Difficulty</div><div class="ttp14-mval">Medium</div></div>
    </div>
    <h3 class="mb-3 text-xs font-normal uppercase tracking-[0.12em] text-ttp14-head">Ingredients</h3>
    <ul class="m-0 list-none p-0">

      <li class="flex items-baseline gap-1.5 border-b border-dashed border-ttp14-edge text-[15px] leading-[1.9] text-ttp14-ink">
        <span class="ttp14-qty">1 whole (3–4 lb)</span>
        <span class="group relative inline-block">
          <button type="button" aria-describedby="ttp14-i1" class="ttp14-name">free-range chicken</button>
          <span id="ttp14-i1" role="tooltip" class="ttp14-card">
            <span class="ttp14-chead"><span class="ttp14-cname">Free-Range Chicken</span><span class="ttp14-ctype">Poultry · whole bird</span></span>
            <span class="ttp14-sec"><span class="ttp14-slabel">Per 100g (roasted, no skin)</span><span class="ttp14-nrow"><span class="ttp14-nname">Calories</span><span class="ttp14-nval">165 kcal</span></span><span class="ttp14-bar"><span class="ttp14-fill w-[55%]"></span></span><span class="ttp14-nrow"><span class="ttp14-nname">Protein</span><span class="ttp14-nval">31g</span></span><span class="ttp14-nrow"><span class="ttp14-nname">Iron</span><span class="ttp14-nval">1.1mg (14% DV)</span></span></span>
            <span class="ttp14-sec"><span class="ttp14-slabel">Substitutions</span><span class="ttp14-sub">Cornish game hens (halve cook time)</span><span class="ttp14-sub">Bone-in chicken pieces</span></span>
            <span class="ttp14-note">Look for air-chilled, free-range birds — less water retention gives crispier skin.</span>
          </span>
        </span>
      </li>

      <li class="flex items-baseline gap-1.5 border-b border-dashed border-ttp14-edge text-[15px] leading-[1.9] text-ttp14-ink">
        <span class="ttp14-qty">2 whole heads</span>
        <span class="group relative inline-block">
          <button type="button" aria-describedby="ttp14-i2" class="ttp14-name">garlic</button>
          <span id="ttp14-i2" role="tooltip" class="ttp14-card">
            <span class="ttp14-chead"><span class="ttp14-cname">Garlic</span><span class="ttp14-ctype">Allium · bulb</span></span>
            <span class="ttp14-sec"><span class="ttp14-slabel">Per 3 cloves (9g)</span><span class="ttp14-nrow"><span class="ttp14-nname">Calories</span><span class="ttp14-nval">13 kcal</span></span><span class="ttp14-bar"><span class="ttp14-fill w-[10%]"></span></span><span class="ttp14-nrow"><span class="ttp14-nname">Allicin</span><span class="ttp14-nval">high (antimicrobial)</span></span><span class="ttp14-nrow"><span class="ttp14-nname">Vit C</span><span class="ttp14-nval">9% DV</span></span></span>
            <span class="ttp14-sec"><span class="ttp14-slabel">Substitutions</span><span class="ttp14-sub">Roasted garlic paste (2 tbsp)</span><span class="ttp14-sub">Shallots (milder flavour)</span></span>
            <span class="ttp14-note">Do not peel — roasted whole heads caramelise beautifully.</span>
          </span>
        </span>
      </li>

      <li class="flex items-baseline gap-1.5 border-b border-dashed border-ttp14-edge text-[15px] leading-[1.9] text-ttp14-ink">
        <span class="ttp14-qty">2 medium</span>
        <span class="group relative inline-block">
          <button type="button" aria-describedby="ttp14-i3" class="ttp14-name">lemons, zested and halved</button>
          <span id="ttp14-i3" role="tooltip" class="ttp14-card">
            <span class="ttp14-chead"><span class="ttp14-cname">Lemon</span><span class="ttp14-ctype">Citrus fruit · fresh</span></span>
            <span class="ttp14-sec"><span class="ttp14-slabel">Per 1 medium lemon (84g)</span><span class="ttp14-nrow"><span class="ttp14-nname">Calories</span><span class="ttp14-nval">22 kcal</span></span><span class="ttp14-bar"><span class="ttp14-fill w-[15%]"></span></span><span class="ttp14-nrow"><span class="ttp14-nname">Vitamin C</span><span class="ttp14-nval">51mg (56% DV)</span></span><span class="ttp14-nrow"><span class="ttp14-nname">Citric acid</span><span class="ttp14-nval">tenderises meat</span></span></span>
            <span class="ttp14-sec"><span class="ttp14-slabel">Substitutions</span><span class="ttp14-sub">Meyer lemons (sweeter)</span><span class="ttp14-sub">1½ limes + ½ orange</span></span>
            <span class="ttp14-note">Microplane the zest before cutting — releases essential oils lost once sliced.</span>
          </span>
        </span>
      </li>

      <li class="flex items-baseline gap-1.5 border-b border-dashed border-ttp14-edge text-[15px] leading-[1.9] text-ttp14-ink">
        <span class="ttp14-qty">¼ cup, fresh</span>
        <span class="group relative inline-block">
          <button type="button" aria-describedby="ttp14-i4" class="ttp14-name">thyme and rosemary</button>
          <span id="ttp14-i4" role="tooltip" class="ttp14-card">
            <span class="ttp14-chead"><span class="ttp14-cname">Fresh Herbs</span><span class="ttp14-ctype">Lamiaceae · aromatic</span></span>
            <span class="ttp14-sec"><span class="ttp14-slabel">Per tbsp fresh thyme (2.4g)</span><span class="ttp14-nrow"><span class="ttp14-nname">Thymol</span><span class="ttp14-nval">antimicrobial terpene</span></span><span class="ttp14-bar"><span class="ttp14-fill w-[30%]"></span></span><span class="ttp14-nrow"><span class="ttp14-nname">Iron</span><span class="ttp14-nval">1.7mg (10% DV)</span></span><span class="ttp14-nrow"><span class="ttp14-nname">Rosmarinic</span><span class="ttp14-nval">antioxidant</span></span></span>
            <span class="ttp14-sec"><span class="ttp14-slabel">Substitutions</span><span class="ttp14-sub">Dried herbs (use ⅓ the quantity)</span><span class="ttp14-sub">Herbes de Provence (1 tbsp)</span></span>
            <span class="ttp14-note">Slide whole sprigs under the skin — the fat bastes the herbs during roasting.</span>
          </span>
        </span>
      </li>

      <li class="flex items-baseline gap-1.5 text-[15px] leading-[1.9] text-ttp14-ink">
        <span class="ttp14-qty">4 tbsp, softened</span>
        <span class="group relative inline-block">
          <button type="button" aria-describedby="ttp14-i5" class="ttp14-name">unsalted butter</button>
          <span id="ttp14-i5" role="tooltip" class="ttp14-card">
            <span class="ttp14-chead"><span class="ttp14-cname">Unsalted Butter</span><span class="ttp14-ctype">Dairy · fat</span></span>
            <span class="ttp14-sec"><span class="ttp14-slabel">Per tbsp (14g)</span><span class="ttp14-nrow"><span class="ttp14-nname">Calories</span><span class="ttp14-nval">102 kcal</span></span><span class="ttp14-bar"><span class="ttp14-fill w-[78%]"></span></span><span class="ttp14-nrow"><span class="ttp14-nname">Saturated</span><span class="ttp14-nval">7.3g</span></span><span class="ttp14-nrow"><span class="ttp14-nname">Vitamin A</span><span class="ttp14-nval">7% DV</span></span></span>
            <span class="ttp14-sec"><span class="ttp14-slabel">Substitutions</span><span class="ttp14-sub">Ghee (higher smoke point)</span><span class="ttp14-sub">Olive oil (dairy-free)</span></span>
            <span class="ttp14-note">Unsalted lets you control seasoning. European-style (84%+ fat) gives richer results.</span>
          </span>
        </span>
      </li>
    </ul>
  </article>
</section>
```
## CSS
```css
@import "tailwindcss";

@theme {
  --color-ttp14-stage: #fdf8f0;
  --color-ttp14-stage: oklch(0.98 0.015 85);
  --color-ttp14-well: #f8f2e6;
  --color-ttp14-well: oklch(0.96 0.018 85);
  --color-ttp14-edge: #e0d4bd;
  --color-ttp14-edge: oklch(0.87 0.03 85);
  --color-ttp14-ink: #3a2c18;
  --color-ttp14-ink: oklch(0.31 0.04 70);
  --color-ttp14-body: #6a5a3e;
  --color-ttp14-body: oklch(0.47 0.05 78);
  --color-ttp14-meta: #7d6c4c;
  --color-ttp14-meta: oklch(0.54 0.05 80);
  --color-ttp14-head: #705a3a;
  --color-ttp14-head: oklch(0.5 0.05 75);
  --color-ttp14-accent: #8a5020;
  --color-ttp14-accent: oklch(0.47 0.1 55);
  --color-ttp14-bar1: #c8a060;
  --color-ttp14-bar2: #e8c080;
  --font-ttp14-serif: Georgia, 'Times New Roman', serif;
  --font-ttp14-sans: 'Inter', system-ui, sans-serif;
}

.ttp-14 {
  width: 100%;
  min-height: 100svh;
}
/* Five ingredients, one card anatomy: header, nutrition, subs, note. */

.ttp-14 .ttp14-mlabel {
  @apply text-[9px] uppercase tracking-[0.12em] text-ttp14-meta;
}

.ttp-14 .ttp14-mval {
  @apply mt-px text-[13px] italic text-ttp14-body;
}

.ttp-14 .ttp14-qty {
  @apply min-w-[110px] shrink-0 text-[13px] italic text-ttp14-meta;
}

.ttp-14 .ttp14-name {
  @apply cursor-help border-0 border-b border-dotted border-ttp14-accent/50 bg-transparent p-0 font-ttp14-serif text-[15px] text-ttp14-ink transition-colors duration-150 hover:border-ttp14-accent hover:text-ttp14-accent focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-ttp14-accent;
}

.ttp-14 .ttp14-card {
  @apply pointer-events-none invisible absolute top-1/2 left-[calc(100%+14px)] z-50 block w-60 max-w-[calc(100vw-48px)] -translate-y-1/2 translate-x-1.5 overflow-hidden rounded border border-ttp14-edge bg-white text-left font-ttp14-sans opacity-0 shadow-[4px_6px_22px_rgba(80,60,20,0.15)] transition-[opacity,translate,visibility] duration-200 ease-[cubic-bezier(0.22,1,0.36,1)] group-hover:visible group-hover:translate-x-0 group-hover:opacity-100 group-focus-within:visible group-focus-within:translate-x-0 group-focus-within:opacity-100;
}

.ttp-14 .ttp14-chead {
  @apply block border-b border-ttp14-edge bg-ttp14-well px-3.25 py-2.75;
}

.ttp-14 .ttp14-cname {
  @apply mb-0.5 block font-ttp14-serif text-sm italic text-ttp14-ink;
}

.ttp-14 .ttp14-ctype {
  @apply block text-[10px] uppercase tracking-[0.08em] text-ttp14-meta;
}

.ttp-14 .ttp14-sec {
  @apply block border-b border-ttp14-edge px-3.25 py-2.5;
}

.ttp-14 .ttp14-slabel {
  @apply mb-1.5 block text-[9px] uppercase tracking-[0.1em] text-ttp14-meta;
}

.ttp-14 .ttp14-nrow {
  @apply mb-0.75 flex justify-between text-[10.5px];
}

.ttp-14 .ttp14-nname {
  @apply text-ttp14-body;
}

.ttp-14 .ttp14-nval {
  @apply font-ttp14-serif italic text-ttp14-ink;
}

.ttp-14 .ttp14-bar {
  @apply my-0.5 mb-1.5 block h-0.5 overflow-hidden rounded-[1px] bg-ttp14-edge;
}

.ttp-14 .ttp14-fill {
  @apply block h-full rounded-[1px] bg-linear-to-r from-ttp14-bar1 to-ttp14-bar2;
}

.ttp-14 .ttp14-sub {
  @apply relative mb-1 block pl-2.25 text-[10.5px] text-ttp14-body before:absolute before:left-0 before:text-[9px] before:text-ttp14-accent before:content-['→'];
}

.ttp-14 .ttp14-note {
  @apply block px-3.25 py-2.5 font-ttp14-serif text-[10.5px] italic leading-[1.5] text-ttp14-body;
}

@media (max-width: 1279px) {
  .ttp-14 .ttp14-card {
    @apply static hidden mt-2 w-full translate-x-0 translate-y-0 group-hover:block group-focus-within:block;
  }
}
```
