---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mobile-navigation/split-screen-navigation/"
title: "Split-Screen Navigation"
section: "navigation"
category: "css-mobile-navigation"
category_name: "CSS Mobile Navigation Patterns"
description: "A split-panel layout with a narrow 120px left category sidebar and a full-height right content panel."
has_js: "false"
---

Here's a working CSS Mobile Navigation Pattern from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Split-Screen Navigation
Source: https://codefronts.com/navigation/css-mobile-navigation/split-screen-navigation/

A split-panel layout with a narrow 120px left category sidebar and a full-height right content panel. Radio inputs switch categories with a fade-slide page transition and a right-edge active indicator.
## HTML
```html
<div class="mn-14">
  <input type="radio" name="mn-14-cat" id="mn-14-c1" checked>
  <input type="radio" name="mn-14-cat" id="mn-14-c2">
  <input type="radio" name="mn-14-cat" id="mn-14-c3">
  <input type="radio" name="mn-14-cat" id="mn-14-c4">

  <div class="mn-14__left">
    <label for="mn-14-c1" class="mn-14__cat-item">
      <div class="mn-14__cat-icon" style="background:rgba(139,92,246,0.2)">🎮</div>
      <span class="mn-14__cat-name">Gaming</span>
      <div class="mn-14__cat-indicator"></div>
    </label>
    <label for="mn-14-c2" class="mn-14__cat-item">
      <div class="mn-14__cat-icon" style="background:rgba(34,197,94,0.2)">🌿</div>
      <span class="mn-14__cat-name">Nature</span>
      <div class="mn-14__cat-indicator"></div>
    </label>
    <label for="mn-14-c3" class="mn-14__cat-item">
      <div class="mn-14__cat-icon" style="background:rgba(239,68,68,0.2)">❤️</div>
      <span class="mn-14__cat-name">Health</span>
      <div class="mn-14__cat-indicator"></div>
    </label>
    <label for="mn-14-c4" class="mn-14__cat-item">
      <div class="mn-14__cat-icon" style="background:rgba(59,130,246,0.2)">📱</div>
      <span class="mn-14__cat-name">Tech</span>
      <div class="mn-14__cat-indicator"></div>
    </label>
  </div>

  <div class="mn-14__right">
    <div class="mn-14__panel" data-p="1">
      <div class="mn-14__panel-header"><h2>Gaming</h2></div>
      <div class="mn-14__panel-body">
        <div class="mn-14__product-card">
          <div class="mn-14__product-img" style="background:rgba(139,92,246,0.2)">🎮</div>
          <div class="mn-14__product-info"><h4>Pro Controller</h4><p>Wireless · 40hr battery</p></div>
          <div class="mn-14__product-price">$79</div>
        </div>
        <div class="mn-14__product-card">
          <div class="mn-14__product-img" style="background:rgba(139,92,246,0.15)">🎧</div>
          <div class="mn-14__product-info"><h4>Gaming Headset</h4><p>7.1 Surround · Noise cancel</p></div>
          <div class="mn-14__product-price">$120</div>
        </div>
        <div class="mn-14__product-card">
          <div class="mn-14__product-img" style="background:rgba(139,92,246,0.15)">🖥️</div>
          <div class="mn-14__product-info"><h4>144Hz Monitor</h4><p>27" IPS · 1ms response</p></div>
          <div class="mn-14__product-price">$349</div>
        </div>
      </div>
    </div>

    <div class="mn-14__panel" data-p="2">
      <div class="mn-14__panel-header"><h2>Nature</h2></div>
      <div class="mn-14__panel-body">
        <div class="mn-14__product-card">
          <div class="mn-14__product-img" style="background:rgba(34,197,94,0.15)">🌱</div>
          <div class="mn-14__product-info"><h4>Succulent Set</h4><p>6-pack · Indoor</p></div>
          <div class="mn-14__product-price">$32</div>
        </div>
        <div class="mn-14__product-card">
          <div class="mn-14__product-img" style="background:rgba(34,197,94,0.15)">🪴</div>
          <div class="mn-14__product-info"><h4>Ceramic Planter</h4><p>Matte White · 8"</p></div>
          <div class="mn-14__product-price">$28</div>
        </div>
        <div class="mn-14__product-card">
          <div class="mn-14__product-img" style="background:rgba(34,197,94,0.15)">🌿</div>
          <div class="mn-14__product-info"><h4>Plant Fertilizer</h4><p>Organic · 500ml</p></div>
          <div class="mn-14__product-price">$14</div>
        </div>
      </div>
    </div>

    <div class="mn-14__panel" data-p="3">
      <div class="mn-14__panel-header"><h2>Health</h2></div>
      <div class="mn-14__panel-body">
        <div class="mn-14__product-card">
          <div class="mn-14__product-img" style="background:rgba(239,68,68,0.15)">⌚</div>
          <div class="mn-14__product-info"><h4>Fitness Tracker</h4><p>Heart rate · Sleep</p></div>
          <div class="mn-14__product-price">$89</div>
        </div>
        <div class="mn-14__product-card">
          <div class="mn-14__product-img" style="background:rgba(239,68,68,0.15)">💊</div>
          <div class="mn-14__product-info"><h4>Vitamin D3</h4><p>5000 IU · 90 caps</p></div>
          <div class="mn-14__product-price">$22</div>
        </div>
      </div>
    </div>

    <div class="mn-14__panel" data-p="4">
      <div class="mn-14__panel-header"><h2>Tech</h2></div>
      <div class="mn-14__panel-body">
        <div class="mn-14__product-card">
          <div class="mn-14__product-img" style="background:rgba(59,130,246,0.15)">🎧</div>
          <div class="mn-14__product-info"><h4>ANC Earbuds</h4><p>Wireless · 30hr</p></div>
          <div class="mn-14__product-price">$149</div>
        </div>
        <div class="mn-14__product-card">
          <div class="mn-14__product-img" style="background:rgba(59,130,246,0.15)">📱</div>
          <div class="mn-14__product-info"><h4>Charging Pad</h4><p>15W · Qi2 compatible</p></div>
          <div class="mn-14__product-price">$35</div>
        </div>
        <div class="mn-14__product-card">
          <div class="mn-14__product-img" style="background:rgba(59,130,246,0.15)">🖱️</div>
          <div class="mn-14__product-info"><h4>Wireless Mouse</h4><p>Silent click · Ergonomic</p></div>
          <div class="mn-14__product-price">$55</div>
        </div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
*,
*::before,
*::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: #0f0f13;
  font-family: 'Segoe UI', sans-serif;
}

.mn-14 {
  width: 375px;
  height: 667px;
  position: relative;
  overflow: hidden;
  border-radius: 32px;
  box-shadow: 0 30px 80px rgba(0,0,0,0.6);
}

.mn-14 input[type="radio"] {
  display: none;
}
/* Toggle button */

.mn-14__toggle-btn {
  position: absolute;
  top: 20px;
  right: 20px;
  z-index: 30;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: rgba(255,255,255,0.15);
  border: 1px solid rgba(255,255,255,0.25);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
}
/* Left panel — category list */

.mn-14__left {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 120px;
  background: #1a1a2e;
  display: flex;
  flex-direction: column;
  padding-top: 80px;
}

.mn-14__cat-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  padding: 16px 8px;
  cursor: pointer;
  position: relative;
  transition: background 0.2s;
}

.mn-14__cat-icon {
  width: 44px;
  height: 44px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.mn-14__cat-name {
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.3px;
  color: rgba(255,255,255,0.4);
  text-align: center;
  transition: color 0.2s;
}

.mn-14__cat-indicator {
  position: absolute;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 3px;
  height: 0;
  background: #fff;
  border-radius: 3px 0 0 3px;
  transition: height 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
/* Active state via radio siblings */

#mn-14-c1:checked ~ .mn-14__left label[for="mn-14-c1"] .mn-14__cat-name,
#mn-14-c2:checked ~ .mn-14__left label[for="mn-14-c2"] .mn-14__cat-name,
#mn-14-c3:checked ~ .mn-14__left label[for="mn-14-c3"] .mn-14__cat-name,
#mn-14-c4:checked ~ .mn-14__left label[for="mn-14-c4"] .mn-14__cat-name {
  color: rgba(255,255,255,0.95);
}

#mn-14-c1:checked ~ .mn-14__left label[for="mn-14-c1"] .mn-14__cat-icon,
#mn-14-c2:checked ~ .mn-14__left label[for="mn-14-c2"] .mn-14__cat-icon,
#mn-14-c3:checked ~ .mn-14__left label[for="mn-14-c3"] .mn-14__cat-icon,
#mn-14-c4:checked ~ .mn-14__left label[for="mn-14-c4"] .mn-14__cat-icon {
  transform: scale(1.1);
}

#mn-14-c1:checked ~ .mn-14__left label[for="mn-14-c1"] .mn-14__cat-indicator,
#mn-14-c2:checked ~ .mn-14__left label[for="mn-14-c2"] .mn-14__cat-indicator,
#mn-14-c3:checked ~ .mn-14__left label[for="mn-14-c3"] .mn-14__cat-indicator,
#mn-14-c4:checked ~ .mn-14__left label[for="mn-14-c4"] .mn-14__cat-indicator {
  height: 28px;
}
/* Right panel */

.mn-14__right {
  position: absolute;
  top: 0;
  left: 120px;
  right: 0;
  bottom: 0;
  overflow: hidden;
}

.mn-14__panel {
  position: absolute;
  inset: 0;
  padding: 0;
  opacity: 0;
  pointer-events: none;
  transform: translateX(20px);
  transition: opacity 0.3s, transform 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  overflow-y: auto;
}

#mn-14-c1:checked ~ .mn-14__right .mn-14__panel[data-p="1"],
#mn-14-c2:checked ~ .mn-14__right .mn-14__panel[data-p="2"],
#mn-14-c3:checked ~ .mn-14__right .mn-14__panel[data-p="3"],
#mn-14-c4:checked ~ .mn-14__right .mn-14__panel[data-p="4"] {
  opacity: 1;
  pointer-events: all;
  transform: translateX(0);
}
/* Panel header */

.mn-14__panel-header {
  height: 80px;
  display: flex;
  align-items: flex-end;
  padding: 0 16px 14px;
  position: relative;
  flex-shrink: 0;
}

.mn-14__panel-header h2 {
  font-size: 22px;
  font-weight: 700;
  color: #fff;
  letter-spacing: -0.4px;
}

.mn-14__panel-body {
  padding: 12px 14px 20px;
}
/* Product cards */

.mn-14__product-card {
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px;
  padding: 14px;
  margin-bottom: 10px;
  display: flex;
  gap: 12px;
  align-items: center;
}

.mn-14__product-img {
  width: 52px;
  height: 52px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 26px;
  flex-shrink: 0;
}

.mn-14__product-info {
  flex: 1;
}

.mn-14__product-info h4 {
  font-size: 13px;
  font-weight: 600;
  color: rgba(255,255,255,0.9);
  margin-bottom: 2px;
}

.mn-14__product-info p {
  font-size: 11px;
  color: rgba(255,255,255,0.4);
}

.mn-14__product-price {
  font-size: 14px;
  font-weight: 700;
  color: rgba(255,255,255,0.9);
}
/* Unique left panel colors per category */

#mn-14-c1:checked ~ .mn-14__left {
  background: linear-gradient(180deg, #1a1a2e 0%, #1a1232 100%);
}

#mn-14-c2:checked ~ .mn-14__left {
  background: linear-gradient(180deg, #0c1f0c 0%, #0a2e0a 100%);
}

#mn-14-c3:checked ~ .mn-14__left {
  background: linear-gradient(180deg, #1a0c0c 0%, #2e0a0a 100%);
}

#mn-14-c4:checked ~ .mn-14__left {
  background: linear-gradient(180deg, #0c1a2e 0%, #0a1a3a 100%);
}

.mn-14__panel[data-p="1"] {
  background: linear-gradient(160deg, #1a1232, #0d0a1f);
}

.mn-14__panel[data-p="2"] {
  background: linear-gradient(160deg, #0a2e0a, #051505);
}

.mn-14__panel[data-p="3"] {
  background: linear-gradient(160deg, #2e0a0a, #1a0505);
}

.mn-14__panel[data-p="4"] {
  background: linear-gradient(160deg, #0a1a3a, #050d20);
}

@media (prefers-reduced-motion: reduce) {
  .mn-14__panel,
    .mn-14__cat-icon,
    .mn-14__cat-indicator {
    transition: none;
  }
}
```
