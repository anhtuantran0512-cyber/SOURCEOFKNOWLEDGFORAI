---
source: "codefronts"
url: "https://codefronts.com/layouts/css-split-screen/before-after-slider/"
title: "Before/After Slider"
section: "layouts"
category: "css-split-screen"
category_name: "CSS Split Screen Layouts"
description: "Skincare brand before/after — clinical white + millennial pink + sage green."
has_js: "true"
---

Here's a working CSS Split Screen Layout from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Before/After Slider
Source: https://codefronts.com/layouts/css-split-screen/before-after-slider/

Skincare brand before/after — clinical white + millennial pink + sage green. Drag the native <input type="range"> to wipe between two states. Pure CSS via :has() on the input value (modern browsers); falls back to a clean static split otherwise.
## HTML
```html
<section class="ss-bef" aria-label="Before and after skincare result">
  <div class="ss-bef-stage" style="--reveal: 50%">
    <div class="ss-bef-after" aria-hidden="true">
      <span class="ss-bef-label">AFTER</span>
      <span class="ss-bef-face ss-bef-face-after"></span>
    </div>
    <div class="ss-bef-before" aria-hidden="true">
      <span class="ss-bef-label">BEFORE</span>
      <span class="ss-bef-face ss-bef-face-before"></span>
    </div>
    <span class="ss-bef-handle" aria-hidden="true"> <span></span><span></span> </span>
  </div>
  <article class="ss-bef-content">
    <span class="ss-bef-eye">— Real client · 12 weeks</span>
    <h2>Quiet skin,<br /><em>loud confidence.</em></h2>
    <p>
      Drag the slider to see the result of our 12-week ritual: gentle exfoliation, daily SPF, and
      the Oat Renewal serum.
    </p>
    <label class="ss-bef-control">
      <span>Reveal</span>
      <input type="range" min="0" max="100" value="50" id="ss-bef-r" aria-label="Reveal amount" />
    </label>
    <ul class="ss-bef-stats">
      <li><strong>92%</strong> reduced redness</li>
      <li><strong>87%</strong> smoother texture</li>
      <li><strong>4.9★</strong> average rating</li>
    </ul>
    <button type="button" class="ss-bef-cta">Start the ritual →</button>
  </article>
</section>
```
## CSS
```css
.ss-bef {
  width: 100%;
  display: grid;
  grid-template-columns: 50% 50%;
  min-height: 100vh;
  font-family: 'Inter', system-ui, sans-serif;
  background: #fff;
  color: #2a2a2a;
  border-radius: 0;
  overflow: hidden;
}

.ss-bef-stage {
  position: relative;
  background: #f7f3ee;
  overflow: hidden;
  isolation: isolate;
  --reveal: 50%;
}

.ss-bef-stage:has(#ss-bef-r) {
  --reveal: calc(var(--ss-bef-pct, 50) * 1%);
}

.ss-bef-after,
.ss-bef-before {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.ss-bef-after {
  background: linear-gradient(135deg, #ffe0e6 0%, #ffd0db 100%);
}

.ss-bef-before {
  background: linear-gradient(135deg, #efe2d4 0%, #d4c4ae 100%);
  clip-path: inset(0 0 0 var(--reveal));
}

.ss-bef-label {
  position: absolute;
  top: 18px;
  font-family: 'Inter', sans-serif;
  font-size: 10.5px;
  font-weight: 800;
  letter-spacing: 0.3em;
  padding: 5px 12px;
  background: rgba(255,255,255,0.92);
  color: #2a2a2a;
}

.ss-bef-after .ss-bef-label {
  right: 18px;
  color: #c41560;
}

.ss-bef-before .ss-bef-label {
  left: 18px;
  color: #5a3825;
}

.ss-bef-face {
  width: 200px;
  height: 240px;
  border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
  position: relative;
}

.ss-bef-face-after {
  background: linear-gradient(180deg, #f8d4c8 0%, #e8b4a8 100%);
  box-shadow: 0 14px 40px rgba(196,21,96,0.18), inset -10px -20px 40px rgba(196,21,96,0.08);
}

.ss-bef-face-before {
  background: linear-gradient(180deg, #d8a888 0%, #c08868 100%);
  box-shadow: inset -10px -20px 40px rgba(0,0,0,0.18);
}

.ss-bef-face-before::before,
.ss-bef-face-before::after {
  content: '';
  position: absolute;
  background: rgba(196,90,28,0.4);
  border-radius: 50%;
}

.ss-bef-face-before::before {
  top: 30%;
  left: 25%;
  width: 12px;
  height: 12px;
  box-shadow: 14px 6px 0 -2px rgba(196,90,28,0.3), -8px 18px 0 -3px rgba(196,90,28,0.35), 26px 22px 0 -4px rgba(196,90,28,0.3);
}

.ss-bef-face-before::after {
  top: 50%;
  right: 22%;
  width: 10px;
  height: 10px;
  box-shadow: -8px 6px 0 -2px rgba(196,90,28,0.3), 4px 14px 0 -3px rgba(196,90,28,0.4);
}

.ss-bef-handle {
  position: absolute;
  top: 0;
  bottom: 0;
  left: var(--reveal);
  width: 2px;
  background: #fff;
  box-shadow: 0 0 0 1px rgba(0,0,0,0.1), 0 0 18px rgba(196,21,96,0.45);
  transform: translateX(-1px);
  pointer-events: none;
  z-index: 5;
}

.ss-bef-handle span:nth-child(1),
.ss-bef-handle span:nth-child(2) {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 32px;
  height: 32px;
  background: #fff;
  border-radius: 50%;
  box-shadow: 0 4px 12px rgba(0,0,0,0.18);
}

.ss-bef-handle span:nth-child(1) {
  right: 18px;
}

.ss-bef-handle span:nth-child(2) {
  left: 18px;
}

.ss-bef-handle span:nth-child(1)::before,
.ss-bef-handle span:nth-child(2)::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  border: solid #c41560;
  border-width: 2px 2px 0 0;
  width: 8px;
  height: 8px;
}

.ss-bef-handle span:nth-child(1)::before {
  transform: translate(-25%, -50%) rotate(45deg);
}

.ss-bef-handle span:nth-child(2)::before {
  transform: translate(-75%, -50%) rotate(-135deg);
}

.ss-bef-content {
  padding: 44px 44px;
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.ss-bef-eye {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #6a8a5a;
}

.ss-bef-content h2 {
  margin: 4px 0 0;
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(34px, 4.5vw, 52px);
  font-weight: 500;
  line-height: 0.96;
  letter-spacing: -0.02em;
  color: #2a2a2a;
}

.ss-bef-content h2 em {
  font-style: italic;
  color: #c41560;
}

.ss-bef-content p {
  margin: 0;
  font-size: 15px;
  line-height: 1.6;
  color: #5a5a5a;
  max-width: 420px;
}

.ss-bef-control {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-top: 4px;
}

.ss-bef-control span {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #6a8a5a;
}

.ss-bef-control input[type="range"] {
  width: 100%;
  accent-color: #c41560;
}

.ss-bef-stats {
  list-style: none;
  margin: 0;
  padding: 14px 0;
  border-top: 1px solid #e0e0e0;
  border-bottom: 1px solid #e0e0e0;
  display: flex;
  gap: 22px;
  font-size: 13px;
  flex-wrap: wrap;
}

.ss-bef-stats li {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.ss-bef-stats strong {
  font-family: 'Cormorant Garamond', serif;
  font-size: 24px;
  font-weight: 500;
  color: #c41560;
  font-style: italic;
}

.ss-bef-cta {
  align-self: flex-start;
  padding: 14px 24px;
  background: #c41560;
  color: #fff;
  border: 0;
  border-radius: 28px;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 0.04em;
  cursor: pointer;
  box-shadow: 0 6px 18px rgba(196,21,96,0.3);
  transition: transform 0.12s, box-shadow 0.12s;
}

.ss-bef-cta:hover {
  transform: translateY(-1px);
  box-shadow: 0 10px 24px rgba(196,21,96,0.45);
}

@media (max-width: 720px) {
  .ss-bef {
    grid-template-columns: 1fr;
  }

  .ss-bef-stage {
    min-height: 320px;
  }
}
```

## JavaScript
```js
/* Wire the range input to the CSS custom property so the slider drives
   the clip-path reveal. Pure CSS would be possible via :has() but value-
   reading from CSS isn't supported widely yet; this 5-line script is the
   reliable cross-browser path. */
(function () {
  var slider = document.getElementById('ss-bef-r');
  var stage  = slider && slider.closest('.ss-bef').querySelector('.ss-bef-stage');
  if (!slider || !stage) return;
  function sync() { stage.style.setProperty('--ss-bef-pct', slider.value); }
  slider.addEventListener('input', sync);
  sync();
})();
```
