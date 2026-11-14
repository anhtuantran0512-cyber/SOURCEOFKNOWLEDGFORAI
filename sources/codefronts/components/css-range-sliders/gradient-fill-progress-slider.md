---
source: "codefronts"
url: "https://codefronts.com/components/css-range-sliders/gradient-fill-progress-slider/"
title: "Gradient Fill Progress Slider"
section: "components"
category: "css-range-sliders"
category_name: "CSS Range Sliders"
description: "A clean course-progress slider where the filled portion carries a continuous sunset-orange-to-violet gradient, the percentage display mirrors the same…"
has_js: "true"
---

Here's a working CSS Range Slider from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Gradient Fill Progress Slider
Source: https://codefronts.com/components/css-range-sliders/gradient-fill-progress-slider/

A clean course-progress slider where the filled portion carries a continuous sunset-orange-to-violet gradient, the percentage display mirrors the same gradient via background-clip, and milestone cards illuminate as thresholds are crossed.
## HTML
```html
<div class="rs-09">
  <div class="rs-09__card">
    <div class="rs-09__top">
      <div>
        <div class="rs-09__title">Course Progress</div>
        <div class="rs-09__sub">Drag to explore your journey</div>
      </div>
      <div class="rs-09__pct-badge"><span id="rs-09-pct">67</span>%</div>
    </div>
    <div class="rs-09__track-wrap">
      <div class="rs-09__track-bg"></div>
      <div class="rs-09__track-fill" id="rs-09-fill"></div>
      <input class="rs-09__input" type="range" min="0" max="100" value="67" id="rs-09-inp">
    </div>
    <div class="rs-09__steps" id="rs-09-steps">
      <div class="rs-09__step active" data-min="0">
        <div class="rs-09__step-icon">🏁</div>
        <div class="rs-09__step-name">Foundations</div>
        <div class="rs-09__step-desc">0–33% complete</div>
      </div>
      <div class="rs-09__step active" data-min="34">
        <div class="rs-09__step-icon">🔬</div>
        <div class="rs-09__step-name">Deep Dive</div>
        <div class="rs-09__step-desc">34–66% complete</div>
      </div>
      <div class="rs-09__step" data-min="67">
        <div class="rs-09__step-icon">🚀</div>
        <div class="rs-09__step-name">Mastery</div>
        <div class="rs-09__step-desc">67–100% complete</div>
      </div>
    </div>
  </div>
</div>
```
## CSS
```css
.rs-09,
.rs-09 *,
.rs-09 *::before,
.rs-09 *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.rs-09 ::selection {
  background: #f472b6;
  color: #fff;
}

.rs-09 {
  --bg: #fafafa;
  --card: #ffffff;
  --grad: linear-gradient(90deg,#f97316,#ec4899,#a855f7);
  --text: #111827;
  --muted: #9ca3af;
  --border: #f3f4f6;
  background: var(--bg);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 40px 24px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

.rs-09__card {
  background: var(--card);
  border-radius: 24px;
  padding: 36px;
  max-width: 440px;
  width: 100%;
  box-shadow: 0 4px 24px rgba(0,0,0,0.06), 0 1px 4px rgba(0,0,0,0.04);
}

.rs-09__top {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  margin-bottom: 8px;
}

.rs-09__title {
  font-size: 20px;
  font-weight: 800;
  color: var(--text);
}

.rs-09__pct-badge {
  font-size: 28px;
  font-weight: 900;
  letter-spacing: -1px;
  background: var(--grad);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-variant-numeric: tabular-nums;
}

.rs-09__sub {
  font-size: 13px;
  color: var(--muted);
  margin-bottom: 36px;
}

.rs-09__track-wrap {
  position: relative;
  height: 48px;
  display: flex;
  align-items: center;
  margin-bottom: 32px;
  padding: 0 12px;
}

.rs-09__track-bg {
  position: absolute;
  left: 12px;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  height: 12px;
  background: var(--border);
  border-radius: 99px;
}

.rs-09__track-fill {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  height: 12px;
  background: var(--grad);
  border-radius: 99px;
  transition: width 0.05s;
}

.rs-09__input {
  position: absolute;
  width: calc(100% - 24px);
  left: 12px;
  top: 0;
  -webkit-appearance: none;
  appearance: none;
  height: 48px;
  background: transparent;
  cursor: pointer;
  outline: none;
  z-index: 2;
  margin: 0;
}

.rs-09__input::-webkit-slider-runnable-track {
  height: 12px;
  background: transparent;
  border-radius: 99px;
}

.rs-09__input::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: #fff;
  border: 4px solid #ec4899;
  box-shadow: 0 0 0 6px rgba(236,72,153,0.12), 0 4px 16px rgba(0,0,0,0.15);
  cursor: grab;
  transition: transform 0.15s, box-shadow 0.15s;
  margin-top: -6px;
}

.rs-09__input:active::-webkit-slider-thumb {
  transform: scale(1.15);
  box-shadow: 0 0 0 10px rgba(236,72,153,0.15), 0 4px 16px rgba(0,0,0,0.15);
  cursor: grabbing;
}

.rs-09__input::-moz-range-track {
  height: 12px;
  background: transparent;
  border-radius: 99px;
}

.rs-09__input::-moz-range-thumb {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  border: 4px solid #ec4899;
  background: #fff;
  box-shadow: 0 0 0 6px rgba(236,72,153,0.12), 0 4px 16px rgba(0,0,0,0.15);
  cursor: grab;
  box-sizing: border-box;
}

.rs-09__steps {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: 12px;
}

.rs-09__step {
  padding: 14px;
  border-radius: 14px;
  background: var(--border);
  transition: background 0.3s, box-shadow 0.3s;
}

.rs-09__step.active {
  background: linear-gradient(135deg, rgba(249,115,22,0.1), rgba(168,85,247,0.1));
  box-shadow: inset 0 0 0 1px rgba(236,72,153,0.25);
}

.rs-09__step-icon {
  font-size: 22px;
  margin-bottom: 6px;
}

.rs-09__step-name {
  font-size: 12px;
  font-weight: 700;
  color: var(--text);
  margin-bottom: 2px;
}

.rs-09__step-desc {
  font-size: 10px;
  color: var(--muted);
}

@media (prefers-reduced-motion: reduce) {
  .rs-09__track-fill,
    .rs-09__step {
    transition: none;
  }
}
```

## JavaScript
```js
(function(){
  const inp = document.getElementById('rs-09-inp');
  const fill = document.getElementById('rs-09-fill');
  const pct = document.getElementById('rs-09-pct');
  const steps = document.querySelectorAll('.rs-09__step');
  const thresholds = [0, 34, 67];
  // Track recess matches the input's left:12px + width:calc(100% - 24px)
  // so the thumb-center travels from 12px to (wrap-width - 12px). The
  // fill must use the same recessed coordinate space — % of the
  // input's effective range, NOT % of the full wrap — otherwise the
  // gradient extends past the thumb (because % of full-wrap > % of
  // recessed-range at high values).
  const trackInset = 12;
  function update(){
    const v = +inp.value;
    const min = +inp.min || 0;
    const max = +inp.max || 100;
    const wrapW = inp.parentElement.getBoundingClientRect().width;
    const usable = Math.max(0, wrapW - trackInset * 2);
    const frac = (v - min) / (max - min);
    fill.style.width = (usable * frac) + 'px';
    pct.textContent = v;
    steps.forEach((s, i) => {
      s.classList.toggle('active', v >= thresholds[i]);
    });
  }
  inp.addEventListener('input', update);
  window.addEventListener('resize', update);
  update();
})();
```
