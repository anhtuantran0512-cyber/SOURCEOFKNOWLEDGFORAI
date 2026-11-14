---
source: "codefronts"
url: "https://codefronts.com/components/css-flip-cards/restaurant-menu-item-recipe-card/"
title: "Restaurant Menu Item Recipe Card"
section: "components"
category: "css-flip-cards"
category_name: "CSS Flip Cards"
description: "Front presents a dish SVG illustration with price tag; back breaks down key ingredients, allergen warnings, and a per-serving nutrition panel."
has_js: "false"
---

Here's a working CSS Flip Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Restaurant Menu Item Recipe Card
Source: https://codefronts.com/components/css-flip-cards/restaurant-menu-item-recipe-card/

Front presents a dish SVG illustration with price tag; back breaks down key ingredients, allergen warnings, and a per-serving nutrition panel.
## HTML
```html
<div class="fc-13">
  <div class="fc-13__scene">
    <div class="fc-13__card">
      <div class="fc-13__front">
        <div class="fc-13__dish-img">
          <svg class="fc-13__dish-svg" width="180" height="160" viewBox="0 0 180 160" fill="none">
            <!-- plate -->
            <ellipse cx="90" cy="110" rx="78" ry="30" fill="rgba(30,20,10,.6)"/>
            <ellipse cx="90" cy="105" rx="76" ry="28" fill="#2a1a08"/>
            <ellipse cx="90" cy="103" rx="68" ry="24" fill="#1a0e04"/>
            <!-- pasta swirls -->
            <path d="M55 95 Q70 80 85 95 Q100 110 115 95 Q130 80 125 95" stroke="rgba(217,119,6,.8)" stroke-width="5" fill="none" stroke-linecap="round"/>
            <path d="M60 100 Q75 85 90 100 Q105 115 120 100" stroke="rgba(180,100,20,.7)" stroke-width="4" fill="none" stroke-linecap="round"/>
            <path d="M65 90 Q80 75 95 90 Q110 105 125 90" stroke="rgba(240,150,30,.6)" stroke-width="3" fill="none" stroke-linecap="round"/>
            <!-- meatballs -->
            <circle cx="72" cy="88" r="14" fill="rgba(139,69,19,.85)"/>
            <circle cx="72" cy="88" r="10" fill="rgba(160,82,45,.8)"/>
            <circle cx="108" cy="93" r="13" fill="rgba(139,69,19,.85)"/>
            <circle cx="108" cy="93" r="9" fill="rgba(160,82,45,.8)"/>
            <!-- sauce -->
            <ellipse cx="90" cy="95" rx="35" ry="12" fill="rgba(180,30,10,.35)"/>
            <!-- herbs -->
            <circle cx="78" cy="76" r="3" fill="rgba(34,197,94,.7)"/>
            <circle cx="85" cy="74" r="2" fill="rgba(34,197,94,.6)"/>
            <circle cx="95" cy="78" r="2.5" fill="rgba(34,197,94,.7)"/>
            <!-- parmesan -->
            <ellipse cx="90" cy="85" rx="20" ry="6" fill="rgba(255,235,180,.3)"/>
          </svg>
          <div class="fc-13__price-tag">$24</div>
        </div>
        <div class="fc-13__dish-info">
          <div class="fc-13__cuisine">Italian · Pasta</div>
          <div class="fc-13__dish-name">Spaghetti al Ragu</div>
          <div class="fc-13__dish-desc">House-made spaghetti with slow-cooked Bolognese, fresh parmesan, and wild basil.</div>
          <div class="fc-13__badges">
            <span class="fc-13__badge">🌶 Medium</span>
            <span class="fc-13__badge">Chef's Pick</span>
          </div>
        </div>
        <div class="fc-13__front-hint">Hover for ingredients & nutrition →</div>
      </div>
      <div class="fc-13__back">
        <div class="fc-13__back-section">Key Ingredients</div>
        <div class="fc-13__ingredients">
          <span class="fc-13__ingredient">Spaghetti pasta</span>
          <span class="fc-13__ingredient">Beef mince (15%)</span>
          <span class="fc-13__ingredient">San Marzano tomato</span>
          <span class="fc-13__ingredient">Parmigiano 24mo</span>
          <span class="fc-13__ingredient">Soffritto base</span>
          <span class="fc-13__ingredient">Fresh basil</span>
          <span class="fc-13__ingredient">Dry white wine</span>
          <span class="fc-13__ingredient">Extra virgin olive oil</span>
        </div>
        <div class="fc-13__back-section">Allergens</div>
        <div class="fc-13__allergens">
          <span class="fc-13__allergen">⚠ Gluten</span>
          <span class="fc-13__allergen">⚠ Dairy</span>
          <span class="fc-13__allergen">⚠ Sulphites</span>
        </div>
        <div class="fc-13__back-section">Nutrition per serving</div>
        <div class="fc-13__nutrition">
          <div class="fc-13__nut-item"><div class="fc-13__nut-num">620</div><div class="fc-13__nut-lbl">kcal</div></div>
          <div class="fc-13__nut-item"><div class="fc-13__nut-num">42g</div><div class="fc-13__nut-lbl">Carbs</div></div>
          <div class="fc-13__nut-item"><div class="fc-13__nut-num">38g</div><div class="fc-13__nut-lbl">Protein</div></div>
          <div class="fc-13__nut-item"><div class="fc-13__nut-num">22g</div><div class="fc-13__nut-lbl">Fat</div></div>
        </div>
        <button class="fc-13__add-btn">Add to Order — $24</button>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.fc-13,
.fc-13 *,
.fc-13 *::before,
.fc-13 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.fc-13 ::selection {
  background: #dc2626;
  color: #fff;
}

.fc-13 {
  --bg: #0c0400;
  --red: #dc2626;
  --amber: #d97706;
  --cream: #fef3c7;
  --card-w: 340px;
  --card-h: 460px;
  font-family: 'Segoe UI',system-ui,sans-serif;
  background: radial-gradient(ellipse at 50% 40%,#1a0800,#0c0400 65%);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 20px;
  color: var(--cream);
}

.fc-13__scene {
  width: var(--card-w);
  height: var(--card-h);
  cursor: pointer;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 12px 30px rgba(0,0,0,.45);
}

.fc-13__card {
  width: 100%;
  height: 100%;
  position: relative;
}
/* Sliding cover — no 3D rotation. Front slides left out, back slides in
   from the right at the same time. Reads as a menu card filing system,
   not a flip. */

.fc-13__front,
.fc-13__back {
  position: absolute;
  inset: 0;
  border-radius: 20px;
  overflow: hidden;
  transition: transform .55s cubic-bezier(.4,0,.2,1);
}

.fc-13__back {
  transform: translateX(100%);
}

.fc-13__scene:hover .fc-13__front {
  transform: translateX(-100%);
}

.fc-13__scene:hover .fc-13__back {
  transform: translateX(0);
}
/* FRONT */

.fc-13__front {
  background: #111008;
  border: 1px solid rgba(217,119,6,.2);
  display: flex;
  flex-direction: column;
}

.fc-13__dish-img {
  height: 220px;
  flex-shrink: 0;
  background: linear-gradient(160deg,#1a0800,#2d1200,#0d0800);
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.fc-13__dish-img::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 50% 60%,rgba(217,119,6,.3),transparent 65%);
}

.fc-13__dish-svg {
  position: relative;
  z-index: 1;
}

.fc-13__price-tag {
  position: absolute;
  top: 14px;
  right: 14px;
  z-index: 2;
  background: rgba(0,0,0,.7);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(217,119,6,.4);
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 16px;
  font-weight: 800;
  color: var(--amber);
}

.fc-13__dish-info {
  padding: 20px 22px;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.fc-13__cuisine {
  font-size: 10px;
  letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--amber);
  font-weight: 700;
}

.fc-13__dish-name {
  font-size: 22px;
  font-weight: 800;
  color: var(--cream);
}

.fc-13__dish-desc {
  font-size: 13px;
  color: rgba(254,243,199,.55);
  line-height: 1.6;
}

.fc-13__badges {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
  margin-top: 4px;
}

.fc-13__badge {
  font-size: 10px;
  padding: 3px 9px;
  border-radius: 20px;
  background: rgba(220,38,38,.1);
  border: 1px solid rgba(220,38,38,.2);
  color: rgba(254,243,199,.7);
}

.fc-13__front-hint {
  padding: 0 22px 16px;
  margin-top: auto;
  font-size: 10px;
  color: rgba(254,243,199,.2);
  letter-spacing: .08em;
}
/* BACK */

.fc-13__back {
  background: linear-gradient(160deg,#0e0800,#12090a);
  border: 1px solid rgba(220,38,38,.2);
  /* Initial off-canvas position set by the shared sliding rule above. */
  display: flex;
  flex-direction: column;
  padding: 24px;
  gap: 12px;
}

.fc-13__back-section {
  font-size: 10px;
  letter-spacing: .15em;
  text-transform: uppercase;
  font-weight: 700;
  color: var(--amber);
}

.fc-13__ingredients {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 6px;
}

.fc-13__ingredient {
  display: flex;
  align-items: center;
  gap: 7px;
  font-size: 12px;
  color: rgba(254,243,199,.7);
}

.fc-13__ingredient::before {
  content: '';
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--amber);
  flex-shrink: 0;
}

.fc-13__allergens {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.fc-13__allergen {
  font-size: 10px;
  padding: 3px 8px;
  border-radius: 6px;
  border: 1px solid rgba(220,38,38,.3);
  background: rgba(220,38,38,.08);
  color: rgba(254,243,199,.6);
}

.fc-13__nutrition {
  display: grid;
  grid-template-columns: repeat(4,1fr);
  gap: 6px;
}

.fc-13__nut-item {
  text-align: center;
  padding: 8px 4px;
  border-radius: 8px;
  background: rgba(255,255,255,.04);
  border: 1px solid rgba(255,255,255,.07);
}

.fc-13__nut-num {
  font-size: 15px;
  font-weight: 800;
  color: var(--cream);
}

.fc-13__nut-lbl {
  font-size: 9px;
  text-transform: uppercase;
  letter-spacing: .08em;
  color: rgba(254,243,199,.35);
  margin-top: 2px;
}

.fc-13__add-btn {
  margin-top: auto;
  width: 100%;
  padding: 13px;
  background: linear-gradient(135deg,var(--red),var(--amber));
  color: #fff;
  font-size: 13px;
  font-weight: 800;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  letter-spacing: .04em;
}

@media (prefers-reduced-motion: reduce) {
  .fc-13__card {
    transition: none;
  }
}
```
