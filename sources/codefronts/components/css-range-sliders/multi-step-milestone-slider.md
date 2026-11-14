---
source: "codefronts"
url: "https://codefronts.com/components/css-range-sliders/multi-step-milestone-slider/"
title: "Multi-Step Milestone Slider"
section: "components"
category: "css-range-sliders"
category_name: "CSS Range Sliders"
description: "A corporate pricing tier slider with four snapping milestone steps, an animated progress line with spring overshoot, step dots that morph from pending to…"
has_js: "true"
---

Here's a working CSS Range Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Multi-Step Milestone Slider
Source: https://codefronts.com/components/css-range-sliders/multi-step-milestone-slider/

A corporate pricing tier slider with four snapping milestone steps, an animated progress line with spring overshoot, step dots that morph from pending to done to active states, and live plan detail cards.
## HTML
```html
<div class="rs-05">
  <div class="rs-05__card">
    <div class="rs-05__plan-badge">Pricing Plan</div>
    <div class="rs-05__title">Choose Your Plan</div>
    <div class="rs-05__subtitle">Drag the slider to see plan details</div>
    <div class="rs-05__steps" id="rs-05-steps">
      <div class="rs-05__progress-line" id="rs-05-line" style="width:0%"></div>
    </div>
    <div class="rs-05__input-wrap">
      <input class="rs-05__input" type="range" min="0" max="3" step="1" value="0" id="rs-05-inp">
    </div>
    <div class="rs-05__detail">
      <div class="rs-05__detail-name" id="rs-05-plan-name">Free</div>
      <div class="rs-05__detail-price" id="rs-05-plan-price">$0<span>/month</span></div>
      <div class="rs-05__detail-perks" id="rs-05-plan-perks">Up to 3 projects · 1 GB storage · Community support</div>
    </div>
  </div>
</div>
```
## CSS
```css
.rs-05,
.rs-05 *,
.rs-05 *::before,
.rs-05 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rs-05 ::selection {
  background: #1e3a8a;
  color: #fff;
}

.rs-05 {
  --bg: #f8fafc;
  --card: #ffffff;
  --navy: #1e3a8a;
  --blue: #3b82f6;
  --active: #1d4ed8;
  --track: #e2e8f0;
  --text: #0f172a;
  --muted: #94a3b8;
  --success: #10b981;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.rs-05__card {
  background: var(--card);
  border-radius: 24px;
  padding: 40px 36px;
  width: 100%;
  max-width: 500px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.08), 0 1px 4px rgba(0,0,0,0.04);
}

.rs-05__plan-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #eff6ff;
  border: 1px solid #bfdbfe;
  color: var(--active);
  font-size: 12px;
  font-weight: 700;
  padding: 5px 12px;
  border-radius: 20px;
  margin-bottom: 20px;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}

.rs-05__plan-badge::before {
  content: '';
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--success);
  display: inline-block;
}

.rs-05__title {
  font-size: 22px;
  font-weight: 800;
  color: var(--text);
  margin-bottom: 6px;
}

.rs-05__subtitle {
  font-size: 14px;
  color: var(--muted);
  margin-bottom: 40px;
}

.rs-05__steps {
  display: flex;
  justify-content: space-between;
  position: relative;
  margin-bottom: 16px;
}

.rs-05__steps::before {
  content: '';
  position: absolute;
  top: 16px;
  left: 16px;
  right: 16px;
  height: 4px;
  background: var(--track);
  border-radius: 99px;
  z-index: 0;
}

.rs-05__progress-line {
  position: absolute;
  top: 16px;
  left: 16px;
  height: 4px;
  background: linear-gradient(90deg, var(--active), var(--blue));
  border-radius: 99px;
  z-index: 1;
  transition: width 0.4s cubic-bezier(0.34,1.56,0.64,1);
}

.rs-05__step {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  position: relative;
  z-index: 2;
}

.rs-05__dot {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--track);
  border: 3px solid var(--track);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
  font-weight: 700;
  color: var(--muted);
  transition: background 0.3s, border-color 0.3s, color 0.3s, transform 0.3s, box-shadow 0.3s;
}

.rs-05__step.active .rs-05__dot {
  background: var(--active);
  border-color: var(--active);
  color: #fff;
  transform: scale(1.15);
  box-shadow: 0 0 0 4px rgba(29,78,216,0.2);
}

.rs-05__step.done .rs-05__dot {
  background: var(--success);
  border-color: var(--success);
  color: #fff;
}

.rs-05__step-name {
  font-size: 11px;
  font-weight: 600;
  color: var(--muted);
  transition: color 0.3s;
  white-space: nowrap;
}

.rs-05__step.active .rs-05__step-name,
.rs-05__step.done .rs-05__step-name {
  color: var(--text);
}

.rs-05__input-wrap {
  margin-bottom: 32px;
}

.rs-05__input {
  width: 100%;
  -webkit-appearance: none;
  appearance: none;
  height: 4px;
  background: transparent;
  outline: none;
  cursor: pointer;
  margin-top: -2px;
}

.rs-05__input::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 0;
  height: 0;
  opacity: 0;
}

.rs-05__detail {
  background: #eff6ff;
  border-radius: 16px;
  padding: 20px;
  border: 1px solid #bfdbfe;
  transition: opacity 0.3s;
}

.rs-05__detail-name {
  font-size: 16px;
  font-weight: 800;
  color: var(--navy);
  margin-bottom: 4px;
}

.rs-05__detail-price {
  font-size: 32px;
  font-weight: 900;
  color: var(--active);
  margin-bottom: 4px;
}

.rs-05__detail-price span {
  font-size: 14px;
  font-weight: 500;
  color: var(--muted);
}

.rs-05__detail-perks {
  font-size: 13px;
  color: var(--text);
  opacity: 0.7;
}

@media (prefers-reduced-motion: reduce) {
  .rs-05__dot,
    .rs-05__step-name,
    .rs-05__progress-line {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  const inp = document.getElementById('rs-05-inp');
  const stepsEl = document.getElementById('rs-05-steps');
  const line = document.getElementById('rs-05-line');
  const plans = [
    { name:'Free', price:'$0', perks:'Up to 3 projects · 1 GB storage · Community support', dots:'F' },
    { name:'Starter', price:'$12', perks:'Up to 20 projects · 10 GB storage · Email support', dots:'S' },
    { name:'Pro', price:'$39', perks:'Unlimited projects · 100 GB storage · Priority support', dots:'P' },
    { name:'Enterprise', price:'$99', perks:'Everything in Pro · SSO · SLA · Dedicated manager', dots:'E' },
  ];
  const linePcts = [0, 33.3, 66.6, 100];
  // Build step dots
  plans.forEach((p,i)=>{
    const step = document.createElement('div');
    step.className = 'rs-05__step';
    step.dataset.idx = i;
    step.innerHTML = `<div class="rs-05__dot">${p.dots}</div><div class="rs-05__step-name">${p.name}</div>`;
    stepsEl.appendChild(step);
  });
  function update(){
    const v = +inp.value;
    const p = plans[v];
    line.style.width = linePcts[v]+'%';
    document.querySelectorAll('.rs-05__step').forEach((s,i)=>{
      s.classList.toggle('active', i===v);
      s.classList.toggle('done', i<v);
    });
    document.getElementById('rs-05-plan-name').textContent = p.name;
    document.getElementById('rs-05-plan-price').innerHTML = p.price+'<span>/month</span>';
    document.getElementById('rs-05-plan-perks').textContent = p.perks;
  }
  inp.addEventListener('input', update);
  update();
})();
```
