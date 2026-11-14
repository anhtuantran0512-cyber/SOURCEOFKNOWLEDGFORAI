---
source: "codefronts"
url: "https://codefronts.com/components/css-range-sliders/password-strength-indicator-slider/"
title: "Password Strength Indicator Slider"
section: "components"
category: "css-range-sliders"
category_name: "CSS Range Sliders"
description: "A security-themed slider where dragging through character count zones triggers animated color transitions across the shield icon, segmented strength bars,…"
has_js: "true"
---

Here's a working CSS Range Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Password Strength Indicator Slider
Source: https://codefronts.com/components/css-range-sliders/password-strength-indicator-slider/

A security-themed slider where dragging through character count zones triggers animated color transitions across the shield icon, segmented strength bars, fill track, thumb, and checklist items — from weak red through fair amber to strong cyan.
## HTML
```html
<div class="rs-12">
  <div class="rs-12__card">
    <div class="rs-12__shield" id="rs-12-shield">🔒</div>
    <div class="rs-12__title">Password Strength</div>
    <div class="rs-12__sub">Adjust character count to see strength change</div>
    <div class="rs-12__strength-label">
      <span class="rs-12__label-text">Strength level</span>
      <span class="rs-12__label-badge" id="rs-12-badge">Weak</span>
    </div>
    <div class="rs-12__segments" id="rs-12-segs">
      <div class="rs-12__seg"></div>
      <div class="rs-12__seg"></div>
      <div class="rs-12__seg"></div>
      <div class="rs-12__seg"></div>
    </div>
    <div class="rs-12__track-wrap">
      <div class="rs-12__track-bg"></div>
      <div class="rs-12__track-fill" id="rs-12-fill" style="width:20%"></div>
      <input class="rs-12__input" type="range" min="4" max="32" value="8" id="rs-12-inp">
    </div>
    <div class="rs-12__big-num" id="rs-12-num" style="color:var(--c-weak)">8</div>
    <div class="rs-12__big-label">characters</div>
    <div class="rs-12__checklist">
      <div class="rs-12__check" id="rs-12-c1">
        <div class="rs-12__check-icon" id="rs-12-i1">✗</div>
        <span>8+ characters for basic security</span>
      </div>
      <div class="rs-12__check" id="rs-12-c2">
        <div class="rs-12__check-icon" id="rs-12-i2">✗</div>
        <span>12+ characters recommended</span>
      </div>
      <div class="rs-12__check" id="rs-12-c3">
        <div class="rs-12__check-icon" id="rs-12-i3">✗</div>
        <span>20+ characters for maximum security</span>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.rs-12,
.rs-12 *,
.rs-12 *::before,
.rs-12 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rs-12 ::selection {
  background: #10b981;
  color: #fff;
}

.rs-12 {
  --bg: #0f172a;
  --card: #1e293b;
  --border: #334155;
  --text: #f1f5f9;
  --muted: #64748b;
  --c-weak: #ef4444;
  --c-fair: #f59e0b;
  --c-good: #10b981;
  --c-strong: #06b6d4;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.rs-12__card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 24px;
  padding: 36px;
  max-width: 420px;
  width: 100%;
  box-shadow: 0 20px 60px rgba(0,0,0,0.5);
}

.rs-12__shield {
  width: 56px;
  height: 56px;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 28px;
  margin-bottom: 20px;
  transition: background 0.4s, box-shadow 0.4s;
  background: rgba(239,68,68,0.15);
  box-shadow: 0 0 24px rgba(239,68,68,0.2);
}

.rs-12__title {
  font-size: 20px;
  font-weight: 800;
  color: var(--text);
  margin-bottom: 4px;
}

.rs-12__sub {
  font-size: 13px;
  color: var(--muted);
  margin-bottom: 28px;
}

.rs-12__strength-label {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}

.rs-12__label-text {
  font-size: 13px;
  color: var(--muted);
}

.rs-12__label-badge {
  font-size: 12px;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 20px;
  transition: background 0.4s, color 0.4s;
}

.rs-12__segments {
  display: flex;
  gap: 4px;
  margin-bottom: 24px;
}

.rs-12__seg {
  flex: 1;
  height: 6px;
  border-radius: 3px;
  background: var(--border);
  transition: background 0.3s;
}

.rs-12__track-wrap {
  position: relative;
  height: 48px;
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.rs-12__track-bg {
  position: absolute;
  width: 100%;
  height: 10px;
  border-radius: 5px;
  background: var(--border);
}

.rs-12__track-fill {
  position: absolute;
  left: 0;
  height: 10px;
  border-radius: 5px;
  transition: width 0.05s, background 0.4s;
  background: var(--c-weak);
}

.rs-12__input {
  position: absolute;
  width: 100%;
  -webkit-appearance: none;
  appearance: none;
  height: 48px;
  background: transparent;
  cursor: pointer;
  outline: none;
  z-index: 2;
}

.rs-12__input::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 2px 12px rgba(0,0,0,0.4);
  border: 3px solid var(--c-weak);
  cursor: grab;
  transition: border-color 0.4s, transform 0.15s;
}

.rs-12__input:active::-webkit-slider-thumb {
  transform: scale(1.15);
  cursor: grabbing;
}

.rs-12__input::-moz-range-thumb {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  border: 3px solid var(--c-weak);
  background: #fff;
  cursor: grab;
}

.rs-12__big-num {
  font-size: 64px;
  font-weight: 900;
  letter-spacing: -4px;
  line-height: 1;
  margin-bottom: 4px;
  font-variant-numeric: tabular-nums;
  transition: color 0.4s;
}

.rs-12__big-label {
  font-size: 13px;
  color: var(--muted);
}

.rs-12__checklist {
  margin-top: 24px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.rs-12__check {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 13px;
  color: var(--muted);
  transition: color 0.3s;
}

.rs-12__check.ok {
  color: var(--text);
}

.rs-12__check-icon {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  background: var(--border);
  transition: background 0.3s;
  flex-shrink: 0;
}

.rs-12__check.ok .rs-12__check-icon {
  background: var(--c-good);
}

@media (prefers-reduced-motion: reduce) {
  .rs-12__track-fill,
    .rs-12__seg,
    .rs-12__shield,
    .rs-12__big-num {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  const inp = document.getElementById('rs-12-inp');
  const fill = document.getElementById('rs-12-fill');
  const num = document.getElementById('rs-12-num');
  const badge = document.getElementById('rs-12-badge');
  const shield = document.getElementById('rs-12-shield');
  const segs = document.querySelectorAll('.rs-12__seg');
  const thumb = inp;
  const levels = [
    { min:4,  max:7,  color:'#ef4444', label:'Weak',   badge:'#fef2f2/#991b1b', icon:'🔓', segs:1 },
    { min:8,  max:11, color:'#f59e0b', label:'Fair',   badge:'#fffbeb/#92400e', icon:'🔒', segs:2 },
    { min:12, max:19, color:'#10b981', label:'Good',   badge:'#ecfdf5/#065f46', icon:'🛡️', segs:3 },
    { min:20, max:32, color:'#06b6d4', label:'Strong', badge:'#ecfeff/#164e63', icon:'🔐', segs:4 },
  ];
  function getLevel(v){
    return levels.find(l=> v>=l.min && v<=l.max) || levels[3];
  }
  function update(){
    const v = +inp.value;
    const pct = (v-4)/(32-4)*100;
    const lv = getLevel(v);
    fill.style.width = pct+'%';
    fill.style.background = lv.color;
    num.textContent = v;
    num.style.color = lv.color;
    badge.textContent = lv.label;
    badge.style.background = lv.badge.split('/')[0];
    badge.style.color = lv.badge.split('/')[1];
    shield.style.background = lv.color+'26';
    shield.style.boxShadow = '0 0 24px '+lv.color+'33';
    shield.textContent = lv.icon;
    segs.forEach((s,i) => { s.style.background = i<lv.segs ? lv.color : ''; });
    // checks
    [[1,8],[2,12],[3,20]].forEach(([idx,min])=>{
      const ok = v>=min;
      document.getElementById('rs-12-c'+idx).classList.toggle('ok', ok);
      const ico = document.getElementById('rs-12-i'+idx);
      ico.textContent = ok ? '✓' : '✗';
    });
  }
  inp.addEventListener('input', update);
  update();
})();
```
