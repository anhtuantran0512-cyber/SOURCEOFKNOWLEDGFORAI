---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/before-after-hero/"
title: "Before/After Hero"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Native <input type=\"range\"> drives a CSS clip-path slider that wipes between a \"before\" desert scene and an \"after\" lush scene."
has_js: "true"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Before/After Hero
Source: https://codefronts.com/layouts/css-hero-sections/before-after-hero/

Native <input type="range"> drives a CSS clip-path slider that wipes between a "before" desert scene and an "after" lush scene. Burnt orange + petrol blue + cream.
## HTML
```html
<section class="hs-09" aria-label="Hero">
  <div class="hs-09__stage">
    <div class="hs-09__after" aria-hidden="true">
      <div class="hs-09__mountains hs-09__after-m"></div>
      <span class="hs-09__sun"></span>
      <span class="hs-09__label">AFTER</span>
    </div>
    <div class="hs-09__before" aria-hidden="true" id="hs-09__clip">
      <div class="hs-09__mountains hs-09__before-m"></div>
      <span class="hs-09__moon"></span>
      <span class="hs-09__label">BEFORE</span>
    </div>
    <input
      type="range"
      min="0"
      max="100"
      value="50"
      class="hs-09__slider"
      id="hs-09__range"
      aria-label="Compare before and after"
      aria-valuetext="50 percent"
    />
    <span class="hs-09__handle" aria-hidden="true" id="hs-09__handle"></span>
  </div>
  <div class="hs-09__copy">
    <h2>Restoration, <em>one acre at a time.</em></h2>
    <p>Drag the slider. We turn dust to forest in 18 months — proven on three continents.</p>
    <a class="hs-09__cta" href="#donate">Plant a tree →</a>
  </div>
</section>
```
## CSS
```css
.hs-09 {
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  width: 100%;
  min-height: 100vh;
  padding: clamp(24px, 4vw, 48px);
  gap: clamp(20px, 4vw, 48px);
  align-items: center;
  background: #f7ecd9;
  font-family: 'Inter', system-ui, sans-serif;
  color: #2c4a4f;
  box-sizing: border-box;
}

.hs-09__stage {
  position: relative;
  height: 100%;
  min-height: 360px;
  border-radius: 12px;
  overflow: hidden;
  border: 4px solid #2c4a4f;
  box-shadow: 8px 8px 0 #c75a2b;
}

.hs-09__after,
.hs-09__before {
  position: absolute;
  inset: 0;
}

.hs-09__after {
  background: linear-gradient(180deg, #87b8a8 0%, #c8b890 70%, #d6c69a 100%);
}

.hs-09__before {
  background: linear-gradient(180deg, #c75a2b 0%, #e8a36e 60%, #f0b87a 100%);
  clip-path: inset(0 50% 0 0);
}

.hs-09__mountains {
  position: absolute;
  bottom: 30%;
  left: 0;
  right: 0;
  height: 40%;
}

.hs-09__after-m {
  background: linear-gradient(135deg, transparent 50%, #4a6b58 50%) 0 0/120px 80px, linear-gradient(45deg, transparent 50%, #4a6b58 50%) 60px 0/120px 80px;
  background-repeat: repeat-x;
}

.hs-09__before-m {
  background: linear-gradient(135deg, transparent 50%, #8a3614 50%) 0 0/120px 80px, linear-gradient(45deg, transparent 50%, #8a3614 50%) 60px 0/120px 80px;
  background-repeat: repeat-x;
}

.hs-09__sun {
  position: absolute;
  top: 18%;
  left: 70%;
  width: 70px;
  height: 70px;
  border-radius: 50%;
  background: #f7d875;
  box-shadow: 0 0 50px rgba(247,216,117,0.6);
}

.hs-09__moon {
  position: absolute;
  top: 14%;
  left: 26%;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  background: #f7ecd9;
  box-shadow: 0 0 30px rgba(247,236,217,0.4);
}

.hs-09__label {
  position: absolute;
  bottom: 12px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.18em;
  padding: 4px 10px;
  background: #2c4a4f;
  color: #f7ecd9;
}

.hs-09__after .hs-09__label {
  right: 14px;
}

.hs-09__before .hs-09__label {
  left: 14px;
  background: #8a3614;
}

.hs-09__slider {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  cursor: ew-resize;
  margin: 0;
  z-index: 3;
}

.hs-09__handle {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 50%;
  width: 3px;
  background: #f7ecd9;
  box-shadow: 0 0 0 1px #2c4a4f;
  pointer-events: none;
  z-index: 2;
}

.hs-09__handle::after {
  content: '⇆';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  width: 38px;
  height: 38px;
  background: #f7ecd9;
  border: 2px solid #2c4a4f;
  border-radius: 50%;
  color: #2c4a4f;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 700;
}

.hs-09__copy {
  padding: 12px 0;
}

.hs-09 h2 {
  margin: 0 0 14px;
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(28px, 4.5vw, 44px);
  font-weight: 700;
  letter-spacing: -0.01em;
  line-height: 1.1;
  color: #2c4a4f;
}

.hs-09 h2 em {
  color: #c75a2b;
  font-style: italic;
}

.hs-09 p {
  margin: 0 0 22px;
  font-size: 15px;
  line-height: 1.6;
  color: #4a6b58;
}

.hs-09__cta {
  display: inline-block;
  padding: 12px 22px;
  background: #c75a2b;
  color: #f7ecd9;
  border-radius: 4px;
  text-decoration: none;
  font-weight: 700;
  font-size: 14px;
  transition: background 0.18s;
}

.hs-09__cta:hover {
  background: #8a3614;
}

@media (max-width: 720px) {
  .hs-09 {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hs-09__cta {
    transition: none;
  }
}
```

## JavaScript
```js
(function () {
  var range = document.getElementById('hs-09__range');
  var clip  = document.getElementById('hs-09__clip');
  var handle= document.getElementById('hs-09__handle');
  if (!range || !clip || !handle) return;
  function update() {
    var v = range.value;
    clip.style.clipPath = 'inset(0 ' + (100 - v) + '% 0 0)';
    handle.style.left = v + '%';
    range.setAttribute('aria-valuetext', v + ' percent');
  }
  range.addEventListener('input', update);
  update();
})();
```
