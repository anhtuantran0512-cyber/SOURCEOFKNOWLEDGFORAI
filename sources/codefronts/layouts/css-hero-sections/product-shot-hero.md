---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/product-shot-hero/"
title: "Product Shot Hero"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "Apple-keynote product shot — a CSS-painted device front-and-centre with floating feature badges that pulse around it. Ice blue + chrome silver on warm white."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: Product Shot Hero
Source: https://codefronts.com/layouts/css-hero-sections/product-shot-hero/

Apple-keynote product shot — a CSS-painted device front-and-centre with floating feature badges that pulse around it. Ice blue + chrome silver on warm white.
## HTML
```html
<section class="hs-21" aria-label="Hero">
  <div class="hs-21__stage">
    <div class="hs-21__device" aria-hidden="true">
      <div class="hs-21__screen"></div>
      <div class="hs-21__cam"></div>
    </div>
    <span class="hs-21__pulse hs-21__p1"><strong>· chip</strong>16-core neural</span>
    <span class="hs-21__pulse hs-21__p2"><strong>· battery</strong>22 hours</span>
    <span class="hs-21__pulse hs-21__p3"><strong>· weight</strong>1.24 kg</span>
  </div>
  <div class="hs-21__copy">
    <h2>The lightest pro<br />laptop we've ever <em>shipped.</em></h2>
    <a class="hs-21__cta" href="#buy">From $1,499 →</a>
  </div>
</section>
```
## CSS
```css
.hs-21 {
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  width: 100%;
  min-height: 100vh;
  padding: clamp(28px, 5vw, 56px);
  gap: clamp(24px, 4vw, 56px);
  align-items: center;
  background: radial-gradient(circle at 30% 30%, #d8e8f0 0%, transparent 50%), radial-gradient(circle at 80% 70%, #e8eef2 0%, transparent 50%), #f8fafc;
  font-family: 'Inter', system-ui, sans-serif;
  color: #1a2840;
  box-sizing: border-box;
}

.hs-21__stage {
  position: relative;
  height: 100%;
  min-height: 320px;
  display: grid;
  place-items: center;
}

.hs-21__device {
  width: 320px;
  height: 200px;
  background: linear-gradient(160deg, #b8c8d8 0%, #8090a8 50%, #607080 100%);
  border-radius: 14px;
  position: relative;
  box-shadow: 0 22px 60px rgba(96,112,128,0.4), inset 0 1px 0 rgba(255,255,255,0.5), inset 0 -2px 0 rgba(0,0,0,0.18);
}

.hs-21__screen {
  position: absolute;
  inset: 8px;
  background: linear-gradient(135deg, #1a2840 0%, #0a1428 100%);
  border-radius: 7px;
  box-shadow: inset 0 0 0 2px #0a1428;
}

.hs-21__cam {
  position: absolute;
  top: 4px;
  left: 50%;
  transform: translateX(-50%);
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #1a2840;
}

.hs-21__pulse {
  position: absolute;
  background: #fff;
  border: 1px solid #d0d8e0;
  padding: 8px 12px;
  border-radius: 999px;
  font-size: 12.5px;
  color: #1a2840;
  display: inline-flex;
  flex-direction: column;
  gap: 1px;
  box-shadow: 0 8px 22px rgba(96,112,128,0.18);
  animation: hs-21-bob 4s ease-in-out infinite;
}

.hs-21__pulse strong {
  font-family: 'JetBrains Mono', monospace;
  font-size: 10px;
  color: #6b85a5;
  font-weight: 600;
  letter-spacing: 0.04em;
}

.hs-21__p1 {
  top: 10%;
  left: 4%;
  animation-delay: 0s;
}

.hs-21__p2 {
  top: 35%;
  right: 0;
  animation-delay: -1.3s;
}

.hs-21__p3 {
  bottom: 12%;
  left: 12%;
  animation-delay: -2.6s;
}

@keyframes hs-21-bob {
  0%,
    100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-6px);
  }
}

.hs-21__copy {
  padding: 12px 0;
}

.hs-21 h2 {
  margin: 0 0 22px;
  font-size: clamp(30px, 4.5vw, 48px);
  font-weight: 700;
  letter-spacing: -0.025em;
  line-height: 1.05;
  color: #1a2840;
}

.hs-21 h2 em {
  background: linear-gradient(90deg, #6b85a5, #b8c8d8);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  font-style: italic;
  font-weight: 800;
}

.hs-21__cta {
  display: inline-block;
  padding: 13px 24px;
  background: #1a2840;
  color: #f8fafc;
  border-radius: 999px;
  text-decoration: none;
  font-weight: 600;
  font-size: 14.5px;
  transition: transform 0.15s;
}

.hs-21__cta:hover {
  transform: translateY(-1px);
}

@media (max-width: 720px) {
  .hs-21 {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hs-21__pulse {
    animation: none;
  }

  .hs-21__cta {
    transition: none;
  }
}
```
