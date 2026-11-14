---
source: "codefronts"
url: "https://codefronts.com/components/css-cards/recipe-food-card/"
title: "Recipe Food Card"
section: "components"
category: "css-cards"
category_name: "CSS Cards"
description: "Recipe tile with CSS-drawn salmon-on-rice plate, prep time / servings / difficulty meta, star rating, cuisine chip, tag pills, and a 44×44 bookmark button."
has_js: "false"
---

Here's a working CSS Card from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Recipe Food Card
Source: https://codefronts.com/components/css-cards/recipe-food-card/

Recipe tile with CSS-drawn salmon-on-rice plate, prep time / servings / difficulty meta, star rating, cuisine chip, tag pills, and a 44×44 bookmark button.
## HTML
```html
<section class="card-03" aria-label="Recipes">
  <header class="card-03__head">
    <div class="card-03__eyebrow">
      <span class="card-03__eye-dot" aria-hidden="true"></span>
      TODAY&#39;S PICK · WEEKNIGHT
    </div>
    <div class="card-03__title-row">
      <h3 class="card-03__title">Cook something great tonight</h3>
      <a href="#all" class="card-03__all">
        Explore all
        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
      </a>
    </div>
  </header>

  <div class="card-03__row">

    <article class="card-03__card card-03__card--hero">
      <div class="card-03__media">
        <img class="card-03__img" src="https://images.unsplash.com/photo-1580476262798-bddd9f4b7369?w=1000&q=80&auto=format&fit=crop" alt="Miso-glazed salmon with sesame rice" loading="lazy" decoding="async">
        <div class="card-03__badges">
          <span class="card-03__badge card-03__badge--pick">
            <svg width="9" height="9" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            EDITOR&#39;S PICK
          </span>
        </div>
        <button type="button" class="card-03__save" aria-label="Save recipe">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
          <span class="card-03__save-count">8.2k</span>
        </button>
        <div class="card-03__pantry" aria-hidden="true">
          <span class="card-03__pantry-dot"></span>
          You have 9/12 ingredients
        </div>
        <div class="card-03__quick">
          <button type="button" class="card-03__quick-btn">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>
            Start cook mode
          </button>
        </div>
      </div>
      <div class="card-03__body">
        <div class="card-03__chips">
          <span class="card-03__chip card-03__chip--cuisine">MAIN · JAPANESE</span>
          <span class="card-03__chip card-03__chip--diet">HIGH-PROTEIN</span>
          <span class="card-03__chip card-03__chip--diet card-03__chip--gluten">GLUTEN-FREE</span>
        </div>
        <div class="card-03__title-block">
          <h4 class="card-03__recipe-title">Miso-Glazed Salmon with Sesame Rice</h4>
          <div class="card-03__rating">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            <span class="card-03__rating-num">4.9</span>
            <span class="card-03__rating-count">(1,247)</span>
          </div>
        </div>
        <p class="card-03__desc">Sweet-savory miso glaze on flaky salmon, crispy sesame rice, quick pickled cucumber. On the table in 25.</p>
        <div class="card-03__meta">
          <div class="card-03__meta-item">
            <div class="card-03__meta-icon card-03__meta-icon--time">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            </div>
            <div class="card-03__meta-text">
              <span class="card-03__meta-label">Total</span>
              <span class="card-03__meta-value">25 min</span>
            </div>
          </div>
          <div class="card-03__meta-item">
            <div class="card-03__meta-icon card-03__meta-icon--serves">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/></svg>
            </div>
            <div class="card-03__meta-text">
              <span class="card-03__meta-label">Serves</span>
              <span class="card-03__meta-value">4</span>
            </div>
          </div>
          <div class="card-03__meta-item">
            <div class="card-03__meta-icon card-03__meta-icon--level">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="6 15 12 9 18 15"/></svg>
            </div>
            <div class="card-03__meta-text">
              <span class="card-03__meta-label">Level</span>
              <span class="card-03__meta-value">Medium</span>
            </div>
          </div>
          <div class="card-03__meta-item">
            <div class="card-03__meta-icon card-03__meta-icon--cal">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2s4 4 4 8a4 4 0 0 1-8 0c0-1 1-2 1-2s2 2 2 5a5 5 0 0 0 6 0"/></svg>
            </div>
            <div class="card-03__meta-text">
              <span class="card-03__meta-label">Calories</span>
              <span class="card-03__meta-value">480</span>
            </div>
          </div>
        </div>
        <div class="card-03__foot">
          <div class="card-03__author">
            <span class="card-03__avatar card-03__avatar--chef">SN</span>
            <div class="card-03__author-text">
              <span class="card-03__author-name">
                Sana Novak
                <svg class="card-03__verified" role="img" aria-label="Verified chef" width="11" height="11" viewBox="0 0 24 24" fill="none"><path d="M12 2 L14 4 L17 3 L18 6 L21 7 L20 10 L22 12 L20 14 L21 17 L18 18 L17 21 L14 20 L12 22 L10 20 L7 21 L6 18 L3 17 L4 14 L2 12 L4 10 L3 7 L6 6 L7 3 L10 4 Z" fill="#c2410c"/><path d="M9 12 L11 14 L15 10" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
              </span>
              <span class="card-03__author-role">Test Kitchen · 4h ago</span>
            </div>
          </div>
          <a class="card-03__cta" href="#recipe">
            View recipe
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>
          </a>
        </div>
      </div>
    </article>

    <div class="card-03__col">

      <article class="card-03__card card-03__card--sm">
        <div class="card-03__media card-03__media--sm">
          <img class="card-03__img" src="https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600&q=80&auto=format&fit=crop" alt="Green shakshuka bowl" loading="lazy" decoding="async">
          <span class="card-03__badge card-03__badge--vegan">
            <svg width="8" height="8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7z"/></svg>
            VEGAN
          </span>
          <button type="button" class="card-03__save card-03__save--sm" aria-label="Save recipe">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
          </button>
          <span class="card-03__time-sm">
            <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            20 min
          </span>
        </div>
        <div class="card-03__body card-03__body--sm">
          <span class="card-03__chip-sm">BRUNCH</span>
          <h4 class="card-03__title-sm">Herby Green Shakshuka</h4>
          <div class="card-03__rating-sm">
            <svg width="9" height="9" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            4.7 · <span class="card-03__rating-count-sm">823 saves</span>
          </div>
        </div>
      </article>

      <article class="card-03__card card-03__card--sm">
        <div class="card-03__media card-03__media--sm">
          <img class="card-03__img" src="https://images.unsplash.com/photo-1509365465985-25d11c17e812?w=600&q=80&auto=format&fit=crop" alt="Chocolate babka bread" loading="lazy" decoding="async">
          <span class="card-03__badge card-03__badge--trending">
            <svg width="8" height="8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="17 6 12 11 8 8 3 13"/><polyline points="14 6 17 6 17 9"/></svg>
            TRENDING
          </span>
          <button type="button" class="card-03__save card-03__save--sm" aria-label="Save recipe">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
          </button>
          <span class="card-03__time-sm">
            <svg width="9" height="9" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            2 hr
          </span>
        </div>
        <div class="card-03__body card-03__body--sm">
          <span class="card-03__chip-sm">DESSERT</span>
          <h4 class="card-03__title-sm">Salted Chocolate Babka</h4>
          <div class="card-03__rating-sm">
            <svg width="9" height="9" viewBox="0 0 24 24" fill="#f59e0b" aria-hidden="true"><path d="M12 2l3 6.9 7.5.7-5.6 5.1 1.7 7.3L12 18.3 5.4 22l1.7-7.3L1.5 9.6l7.5-.7z"/></svg>
            4.9 · <span class="card-03__rating-count-sm">2.1k saves</span>
          </div>
        </div>
      </article>

    </div>

  </div>
</section>
```
## CSS
```css
.card-03 {
  width: 100%;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: clamp(28px, 5vw, 56px) clamp(20px, 4vw, 40px);
  box-sizing: border-box;
  background: radial-gradient(ellipse at 20% 15%, rgba(234, 88, 12, 0.05) 0%, transparent 45%), radial-gradient(ellipse at 80% 85%, rgba(184, 69, 31, 0.05) 0%, transparent 45%), linear-gradient(180deg, #fbeee2 0%, #f2d8bf 100%);
  font-family: 'Inter', system-ui, sans-serif;
  --focus: #b8451f;
  --accent: #c2410c;
}

.card-03 *,
.card-03 *::before,
.card-03 *::after {
  box-sizing: border-box;
}
/* ── header ── */

.card-03__head {
  width: 100%;
  max-width: 780px;
  margin: 0 auto 18px;
}

.card-03__eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.14em;
  color: #9a3412;
  padding: 4px 10px;
  background: rgba(194, 65, 12, 0.08);
  border: 1px solid rgba(194, 65, 12, 0.18);
  border-radius: 999px;
  margin-bottom: 10px;
}

.card-03__eye-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #c2410c;
  box-shadow: 0 0 8px rgba(194, 65, 12, 0.5);
  animation: card-03-pulse 2s ease-in-out infinite;
}

.card-03__title-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.card-03__title {
  font-size: 20px;
  font-weight: 800;
  color: #1a1a1a;
  margin: 0;
  letter-spacing: -0.025em;
  background: linear-gradient(180deg, #1a1a1a 0%, #4b4b57 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-03__all {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 12px;
  font-weight: 700;
  color: #9a3412;
  text-decoration: none;
  padding: 6px 12px;
  background: rgba(255, 255, 255, 0.6);
  border-radius: 999px;
  transition: color 0.18s, background 0.18s;
}

.card-03__all:hover {
  color: #7c2d12;
  background: rgba(255, 255, 255, 0.9);
}

.card-03__all:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* ── row: 1 hero + 2 small ── */

.card-03__row {
  width: 100%;
  max-width: 780px;
  display: grid;
  grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr);
  gap: 14px;
  align-items: stretch;
}

.card-03__col {
  display: flex;
  flex-direction: column;
  gap: 14px;
  min-width: 0;
}
/* ── card base ── */

.card-03__card {
  background: #fff;
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 12px 30px -18px rgba(120, 40, 10, 0.16), 0 0 0 1px rgba(255, 255, 255, 0.5) inset;
  transition: transform 0.35s ease, box-shadow 0.35s, border-color 0.35s;
  display: flex;
  flex-direction: column;
}

.card-03__card:hover {
  transform: translateY(-3px);
  border-color: rgba(194, 65, 12, 0.24);
  box-shadow: 0 24px 44px -18px rgba(120, 40, 10, 0.24), 0 0 0 1px rgba(255, 255, 255, 0.5) inset;
}

.card-03__card--sm {
  flex: 1;
}
/* ── media ── */

.card-03__media {
  position: relative;
  overflow: hidden;
  background: #f5e6d3;
  aspect-ratio: 4/3;
}

.card-03__media--sm {
  aspect-ratio: 16/9;
}

.card-03__img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.5s ease, filter 0.5s;
}

.card-03__card:hover .card-03__img {
  transform: scale(1.05);
}
/* badges */

.card-03__badges {
  position: absolute;
  top: 10px;
  left: 10px;
  display: flex;
  gap: 5px;
  flex-wrap: wrap;
  max-width: calc(100% - 60px);
}

.card-03__badge {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  padding: 3px 8px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.14em;
  border-radius: 5px;
}

.card-03__badge--pick {
  background: linear-gradient(180deg, #fef3c7 0%, #fde68a 100%);
  color: #78350f;
  border: 1px solid rgba(146, 64, 14, 0.22);
  box-shadow: 0 2px 5px rgba(245, 158, 11, 0.28);
}

.card-03__badge--vegan {
  background: linear-gradient(180deg, #d1fae5 0%, #a7f3d0 100%);
  color: #065f46;
  border: 1px solid rgba(6, 95, 70, 0.2);
  box-shadow: 0 2px 5px rgba(52, 211, 153, 0.22);
}

.card-03__badge--trending {
  background: rgba(220, 38, 38, 0.9);
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.14);
  box-shadow: 0 2px 5px rgba(220, 38, 38, 0.3);
}
/* save button */

.card-03__save {
  position: absolute;
  top: 10px;
  right: 10px;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 4px 8px 4px 6px;
  background: rgba(255, 255, 255, 0.92);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 999px;
  color: #1a1a1a;
  font: 700 10.5px 'Inter', sans-serif;
  cursor: pointer;
  transition: color 0.18s, background 0.18s, transform 0.18s;
}

.card-03__save:hover {
  color: #c2410c;
  transform: scale(1.05);
  background: rgba(255, 255, 255, 0.98);
}

.card-03__save:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}

.card-03__save-count {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 10px;
  font-variant-numeric: tabular-nums;
}

.card-03__save--sm {
  padding: 5px;
  top: 8px;
  right: 8px;
}

.card-03__save--sm .card-03__save-count {
  display: none;
}
/* pantry indicator */

.card-03__pantry {
  position: absolute;
  bottom: 10px;
  left: 12px;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 3px 8px;
  background: rgba(255, 255, 255, 0.92);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  border: 1px solid rgba(0, 0, 0, 0.06);
  border-radius: 999px;
  color: #065f46;
  font: 700 10px 'Inter', sans-serif;
  letter-spacing: -0.005em;
}

.card-03__pantry-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #10b981;
  box-shadow: 0 0 6px #10b981;
  animation: card-03-pulse 2s ease-in-out infinite;
}
/* quick / cook mode button (appears on hover) */

.card-03__quick {
  position: absolute;
  bottom: 44px;
  left: 12px;
  right: 12px;
  opacity: 0;
  transform: translateY(10px);
  transition: opacity 0.25s, transform 0.25s;
  pointer-events: none;
}

.card-03__card:hover .card-03__quick {
  opacity: 1;
  transform: translateY(0);
  pointer-events: auto;
}

.card-03__quick-btn {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  width: 100%;
  justify-content: center;
  min-height: 36px;
  padding: 8px 12px;
  background: rgba(26, 26, 26, 0.92);
  -webkit-backdrop-filter: blur(8px);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 10px;
  color: #fff;
  font: 700 12px 'Inter', sans-serif;
  cursor: pointer;
  letter-spacing: -0.01em;
  transition: background 0.18s;
}

.card-03__quick-btn:hover {
  background: #1a1a1a;
}

.card-03__quick-btn:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* time badge on small cards */

.card-03__time-sm {
  position: absolute;
  bottom: 8px;
  right: 8px;
  display: inline-flex;
  align-items: center;
  gap: 3px;
  padding: 3px 7px;
  background: rgba(0, 0, 0, 0.55);
  -webkit-backdrop-filter: blur(6px);
  backdrop-filter: blur(6px);
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 999px;
  color: #fff;
  font: 700 10px 'Inter', sans-serif;
}
/* ── body ── */

.card-03__body {
  padding: 16px 18px 16px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.card-03__chips {
  display: flex;
  align-items: center;
  gap: 5px;
  flex-wrap: wrap;
}

.card-03__chip {
  display: inline-flex;
  align-items: center;
  padding: 3px 8px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 0.14em;
  border-radius: 999px;
  text-transform: uppercase;
}

.card-03__chip--cuisine {
  color: #9a3412;
  background: rgba(194, 65, 12, 0.10);
  border: 1px solid rgba(194, 65, 12, 0.20);
}

.card-03__chip--diet {
  color: #065f46;
  background: rgba(52, 211, 153, 0.10);
  border: 1px solid rgba(52, 211, 153, 0.24);
}

.card-03__chip--gluten {
  color: #92400e;
  background: rgba(245, 158, 11, 0.10);
  border: 1px solid rgba(245, 158, 11, 0.24);
}

.card-03__title-block {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 10px;
}

.card-03__recipe-title {
  font-size: 17px;
  font-weight: 800;
  color: #1a1a1a;
  margin: 0;
  letter-spacing: -0.02em;
  line-height: 1.3;
  background: linear-gradient(180deg, #1a1a1a 0%, #4b4b57 130%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
}

.card-03__rating {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 3px 8px;
  background: rgba(245, 158, 11, 0.08);
  border: 1px solid rgba(245, 158, 11, 0.18);
  border-radius: 999px;
  flex-shrink: 0;
}

.card-03__rating-num {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 11px;
  font-weight: 800;
  color: #92400e;
  font-variant-numeric: tabular-nums;
}

.card-03__rating-count {
  font-size: 10px;
  color: #a1a1aa;
  font-weight: 600;
}

.card-03__desc {
  font-size: 12.5px;
  color: #6b6b7c;
  margin: 0;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
/* meta grid */

.card-03__meta {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 8px;
  padding: 12px;
  background: linear-gradient(180deg, #faf7f2 0%, #f5eee2 100%);
  border: 1px solid rgba(0, 0, 0, 0.04);
  border-radius: 12px;
}

.card-03__meta-item {
  display: flex;
  align-items: center;
  gap: 8px;
  min-width: 0;
}

.card-03__meta-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 26px;
  height: 26px;
  border-radius: 8px;
  flex-shrink: 0;
}

.card-03__meta-icon--time {
  background: rgba(99, 102, 241, 0.12);
  color: #4338ca;
}

.card-03__meta-icon--serves {
  background: rgba(52, 211, 153, 0.14);
  color: #059669;
}

.card-03__meta-icon--level {
  background: rgba(245, 158, 11, 0.14);
  color: #92400e;
}

.card-03__meta-icon--cal {
  background: rgba(220, 38, 38, 0.12);
  color: #b91c1c;
}

.card-03__meta-text {
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.card-03__meta-label {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 8.5px;
  font-weight: 800;
  letter-spacing: 0.12em;
  color: #9ca3af;
  text-transform: uppercase;
}

.card-03__meta-value {
  font-size: 12px;
  font-weight: 800;
  color: #1a1a1a;
  letter-spacing: -0.01em;
  font-variant-numeric: tabular-nums;
}
/* foot (author + CTA) */

.card-03__foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  padding-top: 8px;
  border-top: 1px dashed rgba(0, 0, 0, 0.08);
}

.card-03__author {
  display: flex;
  align-items: center;
  gap: 8px;
}

.card-03__avatar {
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: linear-gradient(135deg, #c2410c, #7c2d12);
  color: #fff;
  font-size: 10px;
  font-weight: 800;
  border: 1.5px solid #fff;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  letter-spacing: -0.01em;
}

.card-03__author-text {
  display: flex;
  flex-direction: column;
  gap: 0;
  min-width: 0;
}

.card-03__author-name {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-size: 11.5px;
  font-weight: 700;
  color: #1a1a1a;
  letter-spacing: -0.005em;
}

.card-03__author-role {
  font-size: 10px;
  color: #9ca3af;
  letter-spacing: -0.005em;
}

.card-03__cta {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  min-height: 32px;
  padding: 7px 12px;
  border-radius: 999px;
  background: linear-gradient(180deg, #1e1e2c 0%, #06070c 100%);
  color: #fff;
  font: 700 11.5px 'Inter', sans-serif;
  text-decoration: none;
  letter-spacing: -0.005em;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.22), 0 0 0 1px rgba(255, 255, 255, 0.14) inset;
  transition: transform 0.18s, background 0.18s;
}

.card-03__cta:hover {
  transform: translateY(-1px);
  background: linear-gradient(180deg, #c2410c 0%, #7c2d12 100%);
}

.card-03__cta:focus-visible {
  outline: 2px solid var(--focus);
  outline-offset: 2px;
}
/* ── small card body ── */

.card-03__body--sm {
  padding: 12px 14px 14px;
  gap: 6px;
}

.card-03__chip-sm {
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 8.5px;
  font-weight: 800;
  letter-spacing: 0.14em;
  color: #9a3412;
  align-self: flex-start;
}

.card-03__title-sm {
  font-size: 13px;
  font-weight: 800;
  color: #1a1a1a;
  margin: 0;
  letter-spacing: -0.015em;
  line-height: 1.3;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-03__rating-sm {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  font-family: ui-monospace, 'JetBrains Mono', Menlo, monospace;
  font-size: 10px;
  font-weight: 800;
  color: #92400e;
  font-variant-numeric: tabular-nums;
  padding: 2px 6px;
  background: rgba(245, 158, 11, 0.08);
  border-radius: 999px;
  align-self: flex-start;
  letter-spacing: -0.005em;
}

.card-03__rating-count-sm {
  color: #a1a1aa;
  font-weight: 700;
}
/* mobile */

@media (max-width: 700px) {
  .card-03__row {
    grid-template-columns: 1fr;
    max-width: 360px;
  }

  .card-03__title-row {
    flex-direction: column;
    align-items: flex-start;
  }

  .card-03__meta {
    grid-template-columns: repeat(2, 1fr);
  }
}

@keyframes card-03-pulse {
  0%,
    100% {
    transform: scale(1);
    opacity: 1;
  }

  50% {
    transform: scale(1.4);
    opacity: 0.7;
  }
}

@media (prefers-reduced-motion: reduce) {
  .card-03__card,
    .card-03__img,
    .card-03__save,
    .card-03__quick,
    .card-03__cta {
    transition: none;
  }

  .card-03__card:hover {
    transform: none;
  }

  .card-03__card:hover .card-03__img {
    transform: none;
  }

  .card-03__save:hover,
    .card-03__cta:hover {
    transform: none;
  }

  .card-03__eye-dot,
    .card-03__pantry-dot {
    animation: none;
  }
}
```
