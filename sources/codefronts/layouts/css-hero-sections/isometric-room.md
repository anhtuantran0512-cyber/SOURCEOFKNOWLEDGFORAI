---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/isometric-room/"
title: "Isometric Room"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Cozy WFH isometric — a CSS-painted desk + laptop + plant + lamp scene rendered with `transform: skewY()`."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Isometric Room
Source: https://codefronts.com/layouts/css-hero-sections/isometric-room/

Cozy WFH isometric — a CSS-painted desk + laptop + plant + lamp scene rendered with `transform: skewY()`. Mauve, dusty rose, and sage — the calm-productivity aesthetic.
## HTML
```html
<section class="hs-26" aria-label="Hero">
  <div class="hs-26__copy">
    <span class="hs-26__eye">/ for the home office crowd</span>
    <h2>Deep work, <em>without the doom-tabs.</em></h2>
    <p>
      A focus timer that stays in the menu bar, not your face. Three tasks a day, one calm
      afternoon.
    </p>
    <a class="hs-26__cta" href="#start">Start a session →</a>
  </div>
  <div class="hs-26__scene" aria-hidden="true">
    <div class="hs-26__desk">
      <div class="hs-26__laptop"><span></span></div>
      <div class="hs-26__mug"></div>
      <div class="hs-26__plant"><span></span><span></span></div>
      <div class="hs-26__lamp"><span></span></div>
    </div>
    <div class="hs-26__floor"></div>
  </div>
</section>
```
## CSS
```css
.hs-26 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  width: 100%;
  min-height: 100vh;
  padding: clamp(28px, 5vw, 56px);
  gap: clamp(20px, 4vw, 48px);
  align-items: center;
  background: radial-gradient(70% 60% at 70% 30%, rgba(216,150,180,0.18), transparent 70%), #f0e8e2;
  font-family: 'Inter', system-ui, sans-serif;
  color: #4a2840;
  box-sizing: border-box;
}

.hs-26__eye {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  letter-spacing: 0.16em;
  color: #8a5a78;
  margin-bottom: 14px;
}

.hs-26 h2 {
  margin: 0 0 16px;
  font-family: 'Cormorant Garamond', Georgia, serif;
  font-size: clamp(32px, 5vw, 50px);
  font-weight: 600;
  letter-spacing: -0.015em;
  line-height: 1.05;
}

.hs-26 h2 em {
  color: #8a5a78;
  font-style: italic;
}

.hs-26 p {
  margin: 0 0 22px;
  font-size: 15.5px;
  line-height: 1.6;
  color: #6a4858;
  max-width: 420px;
}

.hs-26__cta {
  display: inline-block;
  padding: 12px 22px;
  background: #4a2840;
  color: #f0e8e2;
  border-radius: 999px;
  text-decoration: none;
  font-weight: 600;
  font-size: 14px;
  transition: background 0.18s;
}

.hs-26__cta:hover {
  background: #8a5a78;
}

.hs-26__scene {
  position: relative;
  height: 320px;
  display: grid;
  place-items: center;
  perspective: 800px;
}

.hs-26__floor {
  position: absolute;
  bottom: 30px;
  left: 10%;
  right: 10%;
  height: 180px;
  background: linear-gradient(180deg, #d8b8c8 0%, #b890a8 100%);
  transform: rotateX(60deg);
  border-radius: 14px;
}

.hs-26__desk {
  position: relative;
  width: 220px;
  height: 140px;
  background: linear-gradient(135deg, #e0c8a8 0%, #b89878 100%);
  transform: rotateX(60deg) rotateZ(-30deg);
  transform-style: preserve-3d;
  border-radius: 4px;
  box-shadow: 0 22px 40px rgba(74,40,64,0.25);
}

.hs-26__laptop {
  position: absolute;
  top: 18%;
  left: 30%;
  width: 70px;
  height: 50px;
  background: #4a2840;
  border-radius: 4px;
  transform: translateZ(20px);
}

.hs-26__laptop span {
  position: absolute;
  inset: 4px;
  background: #d8a8c0;
  border-radius: 2px;
}

.hs-26__mug {
  position: absolute;
  top: 30%;
  right: 14%;
  width: 22px;
  height: 22px;
  background: #c0d8a8;
  border-radius: 4px;
  transform: translateZ(20px);
}

.hs-26__plant {
  position: absolute;
  top: -6%;
  right: 6%;
  width: 30px;
  height: 50px;
}

.hs-26__plant span {
  position: absolute;
  bottom: 0;
  width: 30px;
  height: 14px;
  background: #b89878;
  border-radius: 4px 4px 12px 12px;
  transform: translateZ(20px);
}

.hs-26__plant span:nth-child(2) {
  width: 6px;
  height: 28px;
  bottom: 12px;
  left: 12px;
  background: #6a8a6a;
  border-radius: 6px 6px 0 0;
}

.hs-26__lamp {
  position: absolute;
  top: -10%;
  left: 12%;
  width: 18px;
  height: 60px;
  background: #d8a8c0;
  border-radius: 4px;
}

.hs-26__lamp span {
  position: absolute;
  top: -10px;
  left: -10px;
  width: 38px;
  height: 18px;
  background: #f0c0a8;
  border-radius: 50% 50% 4px 4px;
}

@media (max-width: 720px) {
  .hs-26 {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hs-26__cta {
    transition: none;
  }
}
```
