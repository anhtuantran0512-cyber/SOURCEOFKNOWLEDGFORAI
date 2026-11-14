---
source: "codefronts"
url: "https://codefronts.com/snippets/css-tooltips/recipe-ingredient-card/"
title: "Recipe Ingredient Card"
section: "snippets"
category: "css-tooltips"
category_name: "CSS Tooltips"
description: "A warm cookbook page where ingredient names carry dotted underlines."
has_js: "false"
---

Here's a working CSS Tooltip from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Recipe Ingredient Card
Source: https://codefronts.com/snippets/css-tooltips/recipe-ingredient-card/

A warm cookbook page where ingredient names carry dotted underlines. Hover one and a side card lifts in with nutrition facts, substitution suggestions, and a sourcing note — designed for recipe sites, meal-plan apps, food databases.
## HTML
```html
<div class="tp-14">
  <div class="tp-14__card">
    <div class="tp-14__title">Roasted Lemon Herb Chicken</div>
    <div class="tp-14__subtitle">French Country · Serves 4</div>
    <div class="tp-14__meta">
      <div class="tp-14__meta-item"><div class="tp-14__meta-label">Prep</div><div class="tp-14__meta-val">20 min</div></div>
      <div class="tp-14__meta-item"><div class="tp-14__meta-label">Cook</div><div class="tp-14__meta-val">1 hr 15 min</div></div>
      <div class="tp-14__meta-item"><div class="tp-14__meta-label">Total</div><div class="tp-14__meta-val">1 hr 35 min</div></div>
      <div class="tp-14__meta-item"><div class="tp-14__meta-label">Difficulty</div><div class="tp-14__meta-val">Medium</div></div>
    </div>
    <div class="tp-14__section-head">Ingredients</div>
    <ul class="tp-14__list">
      <li>
        <span class="tp-14__qty">1 whole (3–4 lb)</span>
        <span class="tp-14__t">
          <span class="tp-14__name">free-range chicken</span>
          <div class="tp-14__tip">
            <div class="tp-14__tip-head"><div class="tp-14__ing-name">Free-Range Chicken</div><div class="tp-14__ing-type">Poultry · whole bird</div></div>
            <div class="tp-14__nutrition">
              <div class="tp-14__nut-title">Per 100g (roasted, no skin)</div>
              <div class="tp-14__nut-row"><span class="tp-14__nut-name">Calories</span><span class="tp-14__nut-val">165 kcal</span></div>
              <div class="tp-14__bar-wrap"><div class="tp-14__bar" style="width:55%"></div></div>
              <div class="tp-14__nut-row"><span class="tp-14__nut-name">Protein</span><span class="tp-14__nut-val">31g</span></div>
              <div class="tp-14__nut-row"><span class="tp-14__nut-name">Iron</span><span class="tp-14__nut-val">1.1mg (14% DV)</span></div>
            </div>
            <div class="tp-14__subs"><div class="tp-14__subs-title">Substitutions</div><div class="tp-14__sub">Cornish game hens (halve cook time)</div><div class="tp-14__sub">Bone-in chicken pieces</div></div>
            <div class="tp-14__note">Look for air-chilled, free-range birds — less water retention gives crispier skin.</div>
          </div>
        </span>
      </li>
      <li>
        <span class="tp-14__qty">2 whole heads</span>
        <span class="tp-14__t">
          <span class="tp-14__name">garlic</span>
          <div class="tp-14__tip">
            <div class="tp-14__tip-head"><div class="tp-14__ing-name">Garlic</div><div class="tp-14__ing-type">Allium · bulb</div></div>
            <div class="tp-14__nutrition">
              <div class="tp-14__nut-title">Per 3 cloves (9g)</div>
              <div class="tp-14__nut-row"><span class="tp-14__nut-name">Calories</span><span class="tp-14__nut-val">13 kcal</span></div>
              <div class="tp-14__bar-wrap"><div class="tp-14__bar" style="width:10%"></div></div>
              <div class="tp-14__nut-row"><span class="tp-14__nut-name">Allicin</span><span class="tp-14__nut-val">high (antimicrobial)</span></div>
              <div class="tp-14__nut-row"><span class="tp-14__nut-name">Vit C</span><span class="tp-14__nut-val">9% DV</span></div>
            </div>
            <div class="tp-14__subs"><div class="tp-14__subs-title">Substitutions</div><div class="tp-14__sub">Roasted garlic paste (2 tbsp)</div><div class="tp-14__sub">Shallots (milder flavour)</div></div>
            <div class="tp-14__note">Do not peel — roasted whole heads caramelize beautifully.</div>
          </div>
        </span>
      </li>
      <li>
        <span class="tp-14__qty">2 medium</span>
        <span class="tp-14__t">
          <span class="tp-14__name">lemons, zested and halved</span>
          <div class="tp-14__tip">
            <div class="tp-14__tip-head"><div class="tp-14__ing-name">Lemon</div><div class="tp-14__ing-type">Citrus fruit · fresh</div></div>
            <div class="tp-14__nutrition">
              <div class="tp-14__nut-title">Per 1 medium lemon (84g)</div>
              <div class="tp-14__nut-row"><span class="tp-14__nut-name">Calories</span><span class="tp-14__nut-val">22 kcal</span></div>
              <div class="tp-14__bar-wrap"><div class="tp-14__bar" style="width:15%"></div></div>
              <div class="tp-14__nut-row"><span class="tp-14__nut-name">Vitamin C</span><span class="tp-14__nut-val">51mg (56% DV)</span></div>
              <div class="tp-14__nut-row"><span class="tp-14__nut-name">Citric acid</span><span class="tp-14__nut-val">tenderises meat</span></div>
            </div>
            <div class="tp-14__subs"><div class="tp-14__subs-title">Substitutions</div><div class="tp-14__sub">Meyer lemons (sweeter)</div><div class="tp-14__sub">1½ limes + ½ orange</div></div>
            <div class="tp-14__note">Microplane the zest before cutting — releases essential oils lost once sliced.</div>
          </div>
        </span>
      </li>
      <li>
        <span class="tp-14__qty">¼ cup, fresh</span>
        <span class="tp-14__t">
          <span class="tp-14__name">thyme and rosemary</span>
          <div class="tp-14__tip">
            <div class="tp-14__tip-head"><div class="tp-14__ing-name">Fresh Herbs</div><div class="tp-14__ing-type">Lamiaceae · aromatic</div></div>
            <div class="tp-14__nutrition">
              <div class="tp-14__nut-title">Per tbsp fresh thyme (2.4g)</div>
              <div class="tp-14__nut-row"><span class="tp-14__nut-name">Thymol</span><span class="tp-14__nut-val">antimicrobial terpene</span></div>
              <div class="tp-14__bar-wrap"><div class="tp-14__bar" style="width:30%"></div></div>
              <div class="tp-14__nut-row"><span class="tp-14__nut-name">Iron</span><span class="tp-14__nut-val">1.7mg (10% DV)</span></div>
              <div class="tp-14__nut-row"><span class="tp-14__nut-name">Rosmarinic</span><span class="tp-14__nut-val">antioxidant</span></div>
            </div>
            <div class="tp-14__subs"><div class="tp-14__subs-title">Substitutions</div><div class="tp-14__sub">Dried herbs (use ⅓ the quantity)</div><div class="tp-14__sub">Herbes de Provence (1 tbsp)</div></div>
            <div class="tp-14__note">Slide whole sprigs under the skin — the fat bastes the herbs during roasting.</div>
          </div>
        </span>
      </li>
      <li>
        <span class="tp-14__qty">4 tbsp, softened</span>
        <span class="tp-14__t">
          <span class="tp-14__name">unsalted butter</span>
          <div class="tp-14__tip">
            <div class="tp-14__tip-head"><div class="tp-14__ing-name">Unsalted Butter</div><div class="tp-14__ing-type">Dairy · fat</div></div>
            <div class="tp-14__nutrition">
              <div class="tp-14__nut-title">Per tbsp (14g)</div>
              <div class="tp-14__nut-row"><span class="tp-14__nut-name">Calories</span><span class="tp-14__nut-val">102 kcal</span></div>
              <div class="tp-14__bar-wrap"><div class="tp-14__bar" style="width:78%"></div></div>
              <div class="tp-14__nut-row"><span class="tp-14__nut-name">Saturated</span><span class="tp-14__nut-val">7.3g</span></div>
              <div class="tp-14__nut-row"><span class="tp-14__nut-name">Vitamin A</span><span class="tp-14__nut-val">7% DV</span></div>
            </div>
            <div class="tp-14__subs"><div class="tp-14__subs-title">Substitutions</div><div class="tp-14__sub">Ghee (higher smoke point)</div><div class="tp-14__sub">Olive oil (dairy-free)</div></div>
            <div class="tp-14__note">Unsalted lets you control seasoning. European-style (84%+ fat) gives richer results.</div>
          </div>
        </span>
      </li>
    </ul>
  </div>
</div>
```
## CSS
```css
.tp-14 {
  width: 100%;
  min-height: 100vh;
  background: #fdf8f0;
  /* Right room — ingredient cards pop to the RIGHT of each name,
       ~280px wide. The recipe card is centered with extra right space. */
  padding: 40px 320px 40px 28px;
  font-family: Georgia, serif;
}

.tp-14__card {
  max-width: 480px;
  margin: 0 auto;
  background: #fff;
  border: 1px solid rgba(180, 160, 120, 0.25);
  border-radius: 2px;
  padding: 32px 36px;
  box-shadow: 0 2px 22px rgba(100, 80, 40, 0.08), 0 0 0 4px rgba(180, 160, 120, 0.06);
}

.tp-14__title {
  font-family: Georgia, serif;
  font-size: 26px;
  font-style: italic;
  color: #2c2010;
  margin-bottom: 4px;
  line-height: 1.2;
}

.tp-14__subtitle {
  font-size: 12px;
  color: #a09070;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 20px;
}

.tp-14__meta {
  display: flex;
  gap: 20px;
  margin-bottom: 22px;
  padding-bottom: 16px;
  border-bottom: 1px solid rgba(180, 160, 120, 0.2);
  flex-wrap: wrap;
}

.tp-14__meta-label {
  font-size: 8.5px;
  color: #b0a080;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.tp-14__meta-val {
  font-size: 13px;
  color: #5a4828;
  font-style: italic;
  margin-top: 1px;
}

.tp-14__section-head {
  font-family: Georgia, serif;
  font-size: 12px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #8a7050;
  margin-bottom: 12px;
  font-weight: 400;
}

.tp-14__list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.tp-14__list li {
  font-size: 15px;
  color: #3a2c18;
  line-height: 1.9;
  border-bottom: 1px dashed rgba(180, 160, 120, 0.15);
  display: flex;
  align-items: baseline;
  gap: 6px;
}

.tp-14__list li:last-child {
  border-bottom: none;
}

.tp-14__qty {
  color: #a09070;
  font-size: 13px;
  font-style: italic;
  min-width: 110px;
  flex-shrink: 0;
}

.tp-14__t {
  position: relative;
  display: inline-block;
  cursor: help;
}

.tp-14__name {
  border-bottom: 1px dotted rgba(140, 100, 40, 0.4);
  transition: color .15s, border-color .15s;
  color: #3a2c18;
}

.tp-14__t:hover .tp-14__name {
  color: #8a5020;
  border-bottom-color: rgba(138, 80, 32, 0.6);
}

.tp-14__tip {
  position: absolute;
  left: calc(100% + 14px);
  top: 50%;
  transform: translateY(-50%) translateX(6px);
  z-index: 200;
  width: 240px;
  background: #fff;
  border: 1px solid rgba(180, 160, 120, 0.3);
  border-radius: 4px;
  opacity: 0;
  visibility: hidden;
  pointer-events: none;
  transition: opacity .2s, transform .2s cubic-bezier(0.22, 1, 0.36, 1), visibility 0s linear .2s;
  box-shadow: 4px 6px 22px rgba(80, 60, 20, 0.15);
  overflow: hidden;
  text-align: left;
  font-family: 'Inter', system-ui, sans-serif;
}

.tp-14__t:hover .tp-14__tip {
  opacity: 1;
  visibility: visible;
  transform: translateY(-50%) translateX(0);
  transition-delay: 0s;
}

.tp-14__tip-head {
  background: #f8f2e6;
  padding: 11px 13px;
  border-bottom: 1px solid rgba(180, 160, 120, 0.2);
}

.tp-14__ing-name {
  font-family: Georgia, serif;
  font-size: 14px;
  font-style: italic;
  color: #3a2c18;
  margin-bottom: 2px;
}

.tp-14__ing-type {
  font-size: 9.5px;
  color: #a09070;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.tp-14__nutrition {
  padding: 10px 13px;
  border-bottom: 1px solid rgba(180, 160, 120, 0.12);
}

.tp-14__nut-title {
  font-size: 8.5px;
  color: #b0a080;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 6px;
}

.tp-14__nut-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 3px;
  font-size: 10.5px;
}

.tp-14__nut-name {
  color: #7a6a50;
}

.tp-14__nut-val {
  color: #5a4828;
  font-family: Georgia, serif;
  font-style: italic;
}

.tp-14__bar-wrap {
  height: 2px;
  background: rgba(180, 160, 120, 0.15);
  border-radius: 1px;
  margin: 2px 0 6px;
  overflow: hidden;
}

.tp-14__bar {
  height: 100%;
  border-radius: 1px;
  background: linear-gradient(to right, #c8a060, #e8c080);
}

.tp-14__subs {
  padding: 10px 13px;
  border-bottom: 1px solid rgba(180, 160, 120, 0.12);
}

.tp-14__subs-title {
  font-size: 8.5px;
  color: #b0a080;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 6px;
}

.tp-14__sub {
  font-size: 10.5px;
  color: #7a6a50;
  margin-bottom: 4px;
  padding-left: 9px;
  position: relative;
}

.tp-14__sub::before {
  content: '→';
  position: absolute;
  left: 0;
  color: #c8a060;
  font-size: 9px;
}

.tp-14__note {
  padding: 10px 13px;
  font-size: 9.5px;
  font-style: italic;
  color: #9a8a68;
  line-height: 1.5;
  font-family: Georgia, serif;
}
```
