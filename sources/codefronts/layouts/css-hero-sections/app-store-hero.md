---
source: "codefronts"
url: "https://codefronts.com/layouts/css-hero-sections/app-store-hero/"
title: "App Store Hero"
section: "layouts"
category: "css-hero-sections"
category_name: "CSS Hero Sections"
description: "iOS-pastel app-launch hero — three phone mockups fanned in lavender, soft pink, powder blue, with App Store and Google Play CTA pills below."
has_js: "false"
---

Here's a working CSS Hero Section from CodeFronts. Use it as-is or adapt to your framework. All classes are scoped under a unique prefix so the code won't collide with your existing styles. MIT licensed.
Demo: App Store Hero
Source: https://codefronts.com/layouts/css-hero-sections/app-store-hero/

iOS-pastel app-launch hero — three phone mockups fanned in lavender, soft pink, powder blue, with App Store and Google Play CTA pills below.
## HTML
```html
<section class="hs-23" aria-label="Hero">
  <div class="hs-23__copy">
    <span class="hs-23__eye">★★★★★ &nbsp; #1 in Lifestyle</span>
    <h2>Mood, sleep, joy — <em>tracked gently.</em></h2>
    <p>The wellness journal that doesn't gamify your serotonin into a streak.</p>
    <div class="hs-23__stores">
      <a href="#ios"><span>Download on the</span><strong>App Store</strong></a>
      <a href="#android"><span>Get it on</span><strong>Google Play</strong></a>
    </div>
  </div>
  <div class="hs-23__fan" aria-hidden="true">
    <span class="hs-23__phone hs-23__p1"></span>
    <span class="hs-23__phone hs-23__p2"></span>
    <span class="hs-23__phone hs-23__p3"></span>
  </div>
</section>
```
## CSS
```css
.hs-23 {
  display: grid;
  grid-template-columns: 1fr 1fr;
  width: 100%;
  min-height: 100vh;
  padding: clamp(28px, 5vw, 56px);
  gap: clamp(20px, 4vw, 48px);
  align-items: center;
  background: linear-gradient(135deg, #e8def0 0%, #fde0e4 50%, #d8e8f0 100%);
  font-family: 'Inter', system-ui, sans-serif;
  color: #3a2a55;
  box-sizing: border-box;
}

.hs-23__eye {
  display: inline-block;
  padding: 5px 12px;
  background: #fff;
  color: #c98ae0;
  border-radius: 999px;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.04em;
  margin-bottom: 18px;
}

.hs-23 h2 {
  margin: 0 0 16px;
  font-size: clamp(32px, 5vw, 50px);
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.05;
  color: #3a2a55;
}

.hs-23 h2 em {
  background: linear-gradient(90deg, #c98ae0, #f59ab8);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  font-style: italic;
}

.hs-23 p {
  margin: 0 0 24px;
  font-size: 16px;
  line-height: 1.55;
  color: #6a5a85;
  max-width: 420px;
}

.hs-23__stores {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.hs-23__stores a {
  display: inline-flex;
  flex-direction: column;
  padding: 10px 22px;
  background: #3a2a55;
  color: #fff;
  border-radius: 12px;
  text-decoration: none;
  transition: transform 0.15s;
}

.hs-23__stores a:hover {
  transform: translateY(-1px);
}

.hs-23__stores a span {
  font-size: 10px;
  opacity: 0.7;
  letter-spacing: 0.04em;
}

.hs-23__stores a strong {
  font-size: 14.5px;
  font-weight: 700;
}

.hs-23__fan {
  position: relative;
  height: 100%;
  min-height: 360px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hs-23__phone {
  position: absolute;
  width: 130px;
  height: 280px;
  border-radius: 24px;
  border: 3px solid #fff;
  box-shadow: 0 22px 50px rgba(120,80,150,0.25), inset 0 0 0 2px rgba(255,255,255,0.4);
}

.hs-23__p1 {
  background: linear-gradient(180deg, #c98ae0 0%, #a160c0 100%);
  transform: rotate(-12deg) translateX(-90px);
}

.hs-23__p2 {
  background: linear-gradient(180deg, #fde0e4 0%, #f59ab8 100%);
  z-index: 2;
  width: 145px;
  height: 300px;
}

.hs-23__p3 {
  background: linear-gradient(180deg, #d8e8f0 0%, #94b4d4 100%);
  transform: rotate(12deg) translateX(90px);
}

@media (max-width: 720px) {
  .hs-23 {
    grid-template-columns: 1fr;
  }
}

@media (prefers-reduced-motion: reduce) {
  .hs-23__stores a {
    transition: none;
  }
}
```
