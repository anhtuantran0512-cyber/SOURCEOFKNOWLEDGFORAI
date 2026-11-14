---
source: "codefronts"
url: "https://codefronts.com/navigation/css-mobile-navigation/neumorphic-bottom-navigation/"
title: "Neumorphic Bottom Navigation"
section: "navigation"
category: "css-mobile-navigation"
category_name: "CSS Mobile Navigation Patterns"
description: "A soft-UI neumorphic bottom navigation bar on a warm light-gray background."
has_js: "false"
---

Here's a working CSS Mobile Navigation Pattern from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Neumorphic Bottom Navigation
Source: https://codefronts.com/navigation/css-mobile-navigation/neumorphic-bottom-navigation/

A soft-UI neumorphic bottom navigation bar on a warm light-gray background. Active tabs press inward with a CSS inset box-shadow. Four pages switch with a fade-slide transition driven by radio inputs.
## HTML
```html
<div class="mn-16">
  <input type="radio" name="mn-16-tab" id="mn-16-t1" checked>
  <input type="radio" name="mn-16-tab" id="mn-16-t2">
  <input type="radio" name="mn-16-tab" id="mn-16-t3">
  <input type="radio" name="mn-16-tab" id="mn-16-t4">

  <div class="mn-16__pages">
    <div class="mn-16__page" data-p="1">
      <div class="mn-16__page-title">Overview</div>
      <div class="mn-16__page-sub">Good morning, Taylor ☀️</div>
      <div class="mn-16__stat-row" style="margin-bottom:14px">
        <div class="mn-16__stat-pill"><div class="val">7.4k</div><div class="lbl">Steps</div></div>
        <div class="mn-16__stat-pill"><div class="val">420</div><div class="lbl">Calories</div></div>
        <div class="mn-16__stat-pill"><div class="val">6.5h</div><div class="lbl">Sleep</div></div>
      </div>
      <div class="mn-16__neu-card">
        <h4>Daily Goal</h4>
        <p>74% complete — keep going!</p>
      </div>
      <div class="mn-16__neu-inset">
        <h4>Steps Progress</h4>
        <div class="mn-16__progress-track"><div class="mn-16__progress-fill" style="width:74%"></div></div>
        <div class="mn-16__progress-label"><span>7,400 steps</span><span>10,000</span></div>
      </div>
    </div>

    <div class="mn-16__page" data-p="2">
      <div class="mn-16__page-title">Workouts</div>
      <div class="mn-16__page-sub">This week's activity</div>
      <div class="mn-16__icon-row">
        <div class="mn-16__neu-icon-btn">🏃</div>
        <div class="mn-16__neu-icon-btn">🚴</div>
        <div class="mn-16__neu-icon-btn">🏊</div>
        <div class="mn-16__neu-icon-btn">🧘</div>
      </div>
      <div class="mn-16__neu-card">
        <h4>Morning Run</h4>
        <p>5.2 km · 28 min · 310 cal burned</p>
      </div>
      <div class="mn-16__neu-card">
        <h4>Strength Training</h4>
        <p>45 min · Full body · 280 cal burned</p>
      </div>
    </div>

    <div class="mn-16__page" data-p="3">
      <div class="mn-16__page-title">Nutrition</div>
      <div class="mn-16__page-sub">Today's intake</div>
      <div class="mn-16__neu-inset">
        <h4>Calories</h4>
        <div class="mn-16__progress-track"><div class="mn-16__progress-fill" style="width:60%;background:linear-gradient(90deg,#43d9b0,#4f7cff)"></div></div>
        <div class="mn-16__progress-label"><span>1,240 eaten</span><span>2,000 goal</span></div>
      </div>
      <div class="mn-16__neu-card">
        <h4>Protein · 68g</h4>
        <p>Chicken, eggs, Greek yogurt</p>
      </div>
      <div class="mn-16__neu-card">
        <h4>Carbs · 142g</h4>
        <p>Oats, rice, banana</p>
      </div>
    </div>

    <div class="mn-16__page" data-p="4">
      <div class="mn-16__page-title">Profile</div>
      <div class="mn-16__page-sub">Your health data</div>
      <div class="mn-16__neu-card" style="display:flex;align-items:center;gap:16px">
        <div style="width:52px;height:52px;border-radius:50%;background:linear-gradient(135deg,#4f7cff,#43d9b0);display:flex;align-items:center;justify-content:center;font-size:24px;box-shadow:3px 3px 8px var(--shadow-dark),-3px -3px 8px var(--shadow-light)">🏃</div>
        <div><h4>Taylor Kim</h4><p style="font-size:12px;color:var(--muted)">Premium · Since 2022</p></div>
      </div>
      <div class="mn-16__neu-inset">
        <h4>Weekly Streak</h4>
        <div style="display:flex;gap:8px;margin-top:6px">
          <div style="flex:1;height:32px;border-radius:8px;background:linear-gradient(135deg,#4f7cff,#43d9b0);opacity:1"></div>
          <div style="flex:1;height:32px;border-radius:8px;background:linear-gradient(135deg,#4f7cff,#43d9b0);opacity:1"></div>
          <div style="flex:1;height:32px;border-radius:8px;background:linear-gradient(135deg,#4f7cff,#43d9b0);opacity:1"></div>
          <div style="flex:1;height:32px;border-radius:8px;background:linear-gradient(135deg,#4f7cff,#43d9b0);opacity:0.4"></div>
          <div style="flex:1;height:32px;border-radius:8px;background:linear-gradient(135deg,#4f7cff,#43d9b0);opacity:1"></div>
          <div style="flex:1;height:32px;border-radius:8px;background:var(--bg);box-shadow:inset 2px 2px 5px var(--shadow-dark),inset -2px -2px 5px var(--shadow-light)"></div>
          <div style="flex:1;height:32px;border-radius:8px;background:var(--bg);box-shadow:inset 2px 2px 5px var(--shadow-dark),inset -2px -2px 5px var(--shadow-light)"></div>
        </div>
      </div>
    </div>
  </div>

  <div class="mn-16__navbar">
    <label for="mn-16-t1" class="mn-16__nav-item">
      <div class="mn-16__nav-icon">🏠</div>
      <span class="mn-16__nav-label">Home</span>
    </label>
    <label for="mn-16-t2" class="mn-16__nav-item">
      <div class="mn-16__nav-icon">🏃</div>
      <span class="mn-16__nav-label">Workout</span>
    </label>
    <label for="mn-16-t3" class="mn-16__nav-item">
      <div class="mn-16__nav-icon">🥗</div>
      <span class="mn-16__nav-label">Nutrition</span>
    </label>
    <label for="mn-16-t4" class="mn-16__nav-item">
      <div class="mn-16__nav-icon">👤</div>
      <span class="mn-16__nav-label">Profile</span>
    </label>
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

.mn-16 {
  --bg: #e0e5ec;
  --text: #2d3748;
  --muted: #8899aa;
  --accent: #4f7cff;
  --accent2: #ff6b9d;
  --accent3: #43d9b0;
  --accent4: #ffb347;
  --shadow-light: rgba(255,255,255,0.8);
  --shadow-dark: rgba(163,177,198,0.7);
  width: 375px;
  height: 667px;
  position: relative;
  overflow: hidden;
  background: var(--bg);
  border-radius: 32px;
  box-shadow: 0 30px 80px rgba(0,0,0,0.5);
}

.mn-16 input[type="radio"] {
  display: none;
}
/* Page area */

.mn-16__pages {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 88px;
  padding: 32px 24px 16px;
}

.mn-16__page {
  position: absolute;
  inset: 0;
  padding: 32px 24px 16px;
  opacity: 0;
  pointer-events: none;
  transform: translateY(12px);
  transition: opacity 0.3s, transform 0.3s cubic-bezier(0.4,0,0.2,1);
}

#mn-16-t1:checked ~ .mn-16__pages .mn-16__page[data-p="1"],
#mn-16-t2:checked ~ .mn-16__pages .mn-16__page[data-p="2"],
#mn-16-t3:checked ~ .mn-16__pages .mn-16__page[data-p="3"],
#mn-16-t4:checked ~ .mn-16__pages .mn-16__page[data-p="4"] {
  opacity: 1;
  pointer-events: all;
  transform: translateY(0);
}
/* Page heading */

.mn-16__page-title {
  font-size: 26px;
  font-weight: 700;
  color: var(--text);
  letter-spacing: -0.5px;
  margin-bottom: 4px;
}

.mn-16__page-sub {
  font-size: 13px;
  color: var(--muted);
  margin-bottom: 28px;
}
/* Neumorphic cards */

.mn-16__neu-card {
  background: var(--bg);
  border-radius: 20px;
  padding: 20px;
  margin-bottom: 14px;
  box-shadow: 6px 6px 14px var(--shadow-dark), -6px -6px 14px var(--shadow-light);
}

.mn-16__neu-card h4 {
  font-size: 14px;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 6px;
}

.mn-16__neu-card p {
  font-size: 12px;
  color: var(--muted);
  line-height: 1.6;
}
/* Neumorphic inset card */

.mn-16__neu-inset {
  background: var(--bg);
  border-radius: 16px;
  padding: 16px;
  margin-bottom: 14px;
  box-shadow: inset 4px 4px 10px var(--shadow-dark), inset -4px -4px 10px var(--shadow-light);
}

.mn-16__neu-inset h4 {
  font-size: 13px;
  font-weight: 600;
  color: var(--text);
  margin-bottom: 8px;
}
/* Progress bar */

.mn-16__progress-track {
  height: 8px;
  border-radius: 4px;
  background: var(--bg);
  box-shadow: inset 2px 2px 5px var(--shadow-dark), inset -2px -2px 5px var(--shadow-light);
  overflow: hidden;
  margin-bottom: 6px;
}

.mn-16__progress-fill {
  height: 100%;
  border-radius: 4px;
  background: linear-gradient(90deg, var(--accent), var(--accent3));
}

.mn-16__progress-label {
  display: flex;
  justify-content: space-between;
  font-size: 11px;
  color: var(--muted);
}
/* Icon row */

.mn-16__icon-row {
  display: flex;
  gap: 12px;
  margin-bottom: 14px;
}

.mn-16__neu-icon-btn {
  width: 52px;
  height: 52px;
  border-radius: 14px;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 22px;
  box-shadow: 4px 4px 10px var(--shadow-dark), -4px -4px 10px var(--shadow-light);
  cursor: pointer;
  transition: box-shadow 0.15s;
}

.mn-16__neu-icon-btn:active {
  box-shadow: inset 3px 3px 8px var(--shadow-dark), inset -3px -3px 8px var(--shadow-light);
}
/* Bottom nav bar */

.mn-16__navbar {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 88px;
  background: var(--bg);
  display: flex;
  align-items: center;
  justify-content: space-around;
  padding: 0 16px 12px;
  box-shadow: 0 -2px 20px rgba(163,177,198,0.4);
}

.mn-16__nav-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  cursor: pointer;
  padding: 8px 16px;
  border-radius: 16px;
  transition: all 0.2s;
  position: relative;
}
/* Inset pressed state for active tab */

#mn-16-t1:checked ~ .mn-16__navbar label[for="mn-16-t1"],
#mn-16-t2:checked ~ .mn-16__navbar label[for="mn-16-t2"],
#mn-16-t3:checked ~ .mn-16__navbar label[for="mn-16-t3"],
#mn-16-t4:checked ~ .mn-16__navbar label[for="mn-16-t4"] {
  box-shadow: inset 3px 3px 8px var(--shadow-dark), inset -3px -3px 8px var(--shadow-light);
}

.mn-16__nav-icon {
  font-size: 22px;
  line-height: 1;
  transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.mn-16__nav-label {
  font-size: 10px;
  font-weight: 600;
  color: var(--muted);
  transition: color 0.2s;
}

#mn-16-t1:checked ~ .mn-16__navbar label[for="mn-16-t1"] .mn-16__nav-label {
  color: var(--accent);
}

#mn-16-t2:checked ~ .mn-16__navbar label[for="mn-16-t2"] .mn-16__nav-label {
  color: var(--accent2);
}

#mn-16-t3:checked ~ .mn-16__navbar label[for="mn-16-t3"] .mn-16__nav-label {
  color: var(--accent3);
}

#mn-16-t4:checked ~ .mn-16__navbar label[for="mn-16-t4"] .mn-16__nav-label {
  color: var(--accent4);
}

#mn-16-t1:checked ~ .mn-16__navbar label[for="mn-16-t1"] .mn-16__nav-icon,
#mn-16-t2:checked ~ .mn-16__navbar label[for="mn-16-t2"] .mn-16__nav-icon,
#mn-16-t3:checked ~ .mn-16__navbar label[for="mn-16-t3"] .mn-16__nav-icon,
#mn-16-t4:checked ~ .mn-16__navbar label[for="mn-16-t4"] .mn-16__nav-icon {
  transform: scale(1.15);
}
/* Dot stat row */

.mn-16__stat-row {
  display: flex;
  gap: 12px;
}

.mn-16__stat-pill {
  flex: 1;
  background: var(--bg);
  border-radius: 14px;
  padding: 14px 12px;
  text-align: center;
  box-shadow: 4px 4px 10px var(--shadow-dark), -4px -4px 10px var(--shadow-light);
}

.mn-16__stat-pill .val {
  font-size: 20px;
  font-weight: 700;
  color: var(--text);
}

.mn-16__stat-pill .lbl {
  font-size: 10px;
  color: var(--muted);
  margin-top: 2px;
}

@media (prefers-reduced-motion: reduce) {
  .mn-16__page,
    .mn-16__nav-icon,
    .mn-16__nav-label {
    transition: none;
  }
}
```
